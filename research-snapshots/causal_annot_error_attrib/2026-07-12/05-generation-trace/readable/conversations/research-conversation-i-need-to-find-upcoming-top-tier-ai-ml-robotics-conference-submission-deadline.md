# Research conversation: I need to find upcoming top-tier AI/ML/robotics conference submission deadlines that are AFTER 2026-05-18 (today). Searc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-afa08300d4c78e69b.jsonl`
- **Structured JSON:** [`5c128c11c3b2491b71d0.json`](../../sessions/5c/5c128c11c3b2491b71d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-18T18:18:36.058Z_

I need to find upcoming top-tier AI/ML/robotics conference submission deadlines that are AFTER 2026-05-18 (today). Search for:

1. WebSearch: "NeurIPS 2026 submission deadline"
2. WebSearch: "ICML 2026 submission deadline"
3. WebSearch: "ICLR 2027 submission deadline"
4. WebSearch: "CoRL 2026 submission deadline"
5. WebSearch: "CVPR 2027 submission deadline"
6. WebSearch: "ECCV 2026 submission deadline"
7. WebSearch: "AAAI 2027 submission deadline"
8. WebSearch: "RSS 2026 submission deadline"
9. WebSearch: "IROS 2026 submission deadline"
10. WebSearch: "top AI conference deadlines 2026 2027"

For each venue, report:
- Conference name and year
- Abstract deadline (if separate)
- Full paper submission deadline
- Whether the deadline is AFTER 2026-05-18
- Conference tier (top-tier like NeurIPS/ICML/ICLR, or solid like CoRL/IROS/RSS)

Only include venues where the submission deadline has NOT yet passed as of 2026-05-18.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "d6a933ea-39f7-4bdb-8f53-616731de28d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T18:18:36.061Z_

```json
{
  "parentUuid": "d6a933ea-39f7-4bdb-8f53-616731de28d4",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b3f7db65-c7d3-49e4-81fb-af91c5f7ab57",
  "timestamp": "2026-05-18T18:18:36.061Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T18:18:39.075Z_



I'll search for all these conference deadlines. Let me first load the WebSearch tool, then run all searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3f7db65-c7d3-49e4-81fb-af91c5f7ab57",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVeZL1KK9x5f1e9eNhP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f8a01c6-42b6-4b2d-a48a-3e862cc33c7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DV416Ns5dsWLACmTCdqpTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 835,
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

_source line 4 · 2026-05-18T18:18:39.436Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AH3Hhq7M4xEXUyJoimfg5V`</summary>

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
  "parentUuid": "5f8a01c6-42b6-4b2d-a48a-3e862cc33c7d",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVeZL1KK9x5f1e9eNhP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a41728fd-7706-4cb4-9261-cfbcf0a18ec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DV416Ns5dsWLACmTCdqpTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 835,
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

### Tool result

_source line 5 · 2026-05-18T18:18:39.438Z_

<details><summary>↩ Tool result · `toolu_01AH3Hhq7M4xEXUyJoimfg5V`</summary>

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
  "parentUuid": "a41728fd-7706-4cb4-9261-cfbcf0a18ec9",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "4fcfd5fe-dcd2-466f-8baa-a5360e5c8979",
  "sourceToolAssistantUUID": "a41728fd-7706-4cb4-9261-cfbcf0a18ec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T18:18:43.913Z_



Now let me run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fcfd5fe-dcd2-466f-8baa-a5360e5c8979",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f9a5ec6-fad0-4e96-b3d9-425c9b2d956d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 7 · 2026-05-18T18:18:44.376Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VmjazDGT8NCfoQvwweyXPM`</summary>

```json
{
  "query": "NeurIPS 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f9a5ec6-fad0-4e96-b3d9-425c9b2d956d",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ef5fd60-d701-4703-af3d-828bce92d733",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 8 · 2026-05-18T18:18:44.815Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018uQkKAcAxwNbYm6fRmGpGP`</summary>

```json
{
  "query": "ICML 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ef5fd60-d701-4703-af3d-828bce92d733",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bf1ab78-2267-4191-a697-69e9a4ba7036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 9 · 2026-05-18T18:18:44.913Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R1Zkgac6MoGJNQ9DZua1ti`</summary>

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
  "parentUuid": "5bf1ab78-2267-4191-a697-69e9a4ba7036",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6211c7a-c489-40b6-983b-ce796f619000",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 10 · 2026-05-18T18:18:45.277Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XXCR6xsog9RSs55goqeUKg`</summary>

```json
{
  "query": "CoRL 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6211c7a-c489-40b6-983b-ce796f619000",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71f8e3d7-28c6-4293-bf6a-8fdfb778fba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 11 · 2026-05-18T18:18:45.715Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ug2DposwH6enoddWmBoQcE`</summary>

```json
{
  "query": "CVPR 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71f8e3d7-28c6-4293-bf6a-8fdfb778fba1",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42700a59-050c-4061-99c3-e7b711bbbe15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 12 · 2026-05-18T18:18:45.948Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JqUJZLyzEUyDh2cpVmB4H7`</summary>

```json
{
  "query": "ECCV 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42700a59-050c-4061-99c3-e7b711bbbe15",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b983efb2-0ff0-478a-a4c6-e1c7629276ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 13 · 2026-05-18T18:18:46.135Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UXqNgrDT16yhmGKQ9RgmkL`</summary>

```json
{
  "query": "AAAI 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b983efb2-0ff0-478a-a4c6-e1c7629276ac",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b48a6611-ca4c-4659-9feb-750afd4a2e9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 14 · 2026-05-18T18:18:46.565Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NFwzq38C77k4A1utrxSLSV`</summary>

```json
{
  "query": "RSS 2026 submission deadline robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b48a6611-ca4c-4659-9feb-750afd4a2e9a",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d153880a-ec43-4d93-b115-9dc27d172bd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 15 · 2026-05-18T18:18:46.580Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KpwWi1jWkCxGMLQ6A6v26b`</summary>

```json
{
  "query": "IROS 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d153880a-ec43-4d93-b115-9dc27d172bd2",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5829dd8d-07f5-48bc-8a95-fb02034c92e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 16 · 2026-05-18T18:18:47.012Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0158C6gQ79PniQXaRmZ4LCMr`</summary>

```json
{
  "query": "top AI conference deadlines 2026 2027"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5829dd8d-07f5-48bc-8a95-fb02034c92e7",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVepY3wkCtmNS3FDMkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82e3af7f-ddc1-4574-bb27-d86e62424028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZJdUSSNpXK7SPtqz2n7e9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 17 · 2026-05-18T18:18:48.360Z_

<details><summary>↩ Tool result · `toolu_01R1Zkgac6MoGJNQ9DZua1ti`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"}]

Based on the search results, I found that ICLR 2027 is predicted to occur on July 31, 2027, based on 2026 schedule patterns. However, the search results do not contain specific information about the submission deadline for ICLR 2027. 

The current search results show information about ICLR 2026, but the ICLR 2027 Call for Papers and detailed submission deadlines do not appear to be officially published yet. I recommend checking the official ICLR website (iclr.cc) or monitoring conference deadline tracking sites for the official announcement of the ICLR 2027 submission deadline once it becomes available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6211c7a-c489-40b6-983b-ce796f619000",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "5b1f5dd5-319d-4f20-b9a6-9155449ad402",
  "sourceToolAssistantUUID": "b6211c7a-c489-40b6-983b-ce796f619000",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T18:18:48.878Z_

<details><summary>↩ Tool result · `toolu_01VmjazDGT8NCfoQvwweyXPM`</summary>

```text
Web search results for query: "NeurIPS 2026 submission deadline"

Links: [{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/neurips-2026.html"},{"title":"2026 Conference","url":"https://neurips.cc/"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"}]

Based on the search results, here are the key submission deadlines for NeurIPS 2026:

## Main Submission Deadlines

Abstract submission deadline: May 4, 2026 (AOE)

Full paper submission deadline, including all supplementary materials: May 6, 2026 AOE

## Important Notes

- The different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines

- All authors must have an OpenReview profile when submitting

## Conference Details

The Fortieth annual conference is held Sun. Dec 6th through Sat the 12th, 2026 at the International Convention Centre in Sydney, Australia.

If you're planning to submit, note that you'll need to prepare your abstract by May 4 and have your complete paper with supplementary materials ready by May 6, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ef5fd60-d701-4703-af3d-828bce92d733",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "3fb157b3-53f7-47d4-900a-8adaf033e51c",
  "sourceToolAssistantUUID": "5ef5fd60-d701-4703-af3d-828bce92d733",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T18:18:48.910Z_

<details><summary>↩ Tool result · `toolu_018uQkKAcAxwNbYm6fRmGpGP`</summary>

```text
Web search results for query: "ICML 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"ICML 2026 Call for Post-Conference Workshops","url":"https://icml.cc/Conferences/2026/CallForWorkshops"},{"title":"2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected","url":"https://eu.36kr.com/en/p/3540848514510723"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ICML 2026","url":"https://icml.cc/"},{"title":"ICML 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=icml26"},{"title":"Update ICML 2025 and 2026 conference data · huggingface/ai-deadlines at 55d2124","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/55d21240bacc3ac62397280592b3dd5ded9e5683"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"}]

Based on the search results, here is the ICML 2026 submission deadline information:

The deadline for ICML 2026 paper submissions is January 28, 2026.

Additionally, there are two-stage submission requirements:
- An abstract must first be submitted by the Abstract submission deadline on OpenReview.
- After submitting the abstract, it will be possible to modify the submission to also upload the full paper PDF, which must be uploaded by the Full paper submission deadline.

Abstract and paper submission deadlines are strict. In no circumstances will extensions be given.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bf1ab78-2267-4191-a697-69e9a4ba7036",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "55e1f846-7e2b-47f0-b78f-11c85af5a5d9",
  "sourceToolAssistantUUID": "5bf1ab78-2267-4191-a697-69e9a4ba7036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T18:18:49.042Z_

<details><summary>↩ Tool result · `toolu_01Ug2DposwH6enoddWmBoQcE`</summary>

```text
Web search results for query: "CVPR 2027 submission deadline"

Links: [{"title":"CVPR: Computer Vision and Pattern Recognition 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=628"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"CVPR 2026 - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/"},{"title":"2025 Dates and Deadlines - CVPR 2026","url":"https://cvpr.thecvf.com/Conferences/2025/Dates"},{"title":"One Year Calendar of Computer Image Analysis, Computer Vision Conferences","url":"https://conferences.visionbib.com/Browse-data.php?year=2027"},{"title":"2027 Conference","url":"https://wacv.thecvf.com/"},{"title":"Conference Calendar for Computer Vision, Image Analysis and Related Topics","url":"http://conferences.visionbib.com/Iris-Conferences.html"},{"title":"Important Dates and Deadlines - CVPR 2026","url":"https://cvpr.thecvf.com/Conferences/2026/Dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Add CVPR 2027 conference information · huggingface/ai-deadlines at 9d3c540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/9d3c5404835da9e75af6f42d683290ceb23d374f"}]

Based on the search results, I found information about CVPR 2027:

CVPR 2027 will be held in Seattle from June 19-26, 2027 at the Seattle Convention Center. However, the submission deadlines have not yet been announced.

For the most up-to-date information about the submission deadline, I recommend checking the official CVPR website at cvpr.thecvf.com or monitoring the conference's official announcements, as the specific deadline date for CVPR 2027 has not been confirmed yet.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42700a59-050c-4061-99c3-e7b711bbbe15",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "91573aac-1ee7-4de9-b7a1-30eca083ebee",
  "sourceToolAssistantUUID": "42700a59-050c-4061-99c3-e7b711bbbe15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T18:18:49.147Z_

<details><summary>↩ Tool result · `toolu_01XXCR6xsog9RSs55goqeUKg`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Registration","url":"https://www.corl.org/attending/registration"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"}]

Based on the search results, here are the key submission deadlines for CoRL 2026:

Abstract submission deadline: May 26, 2026 11:59 UTC

Paper submission deadline: Thursday, May 28, 2026 EOD

CoRL 2026 will be held at the JW Marriott Austin in Austin, TX from November 9–12, 2026, with a workshop day on November 9 and the main conference on November 10–12.

The main paper should be 8 pages, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71f8e3d7-28c6-4293-bf6a-8fdfb778fba1",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "4c98fa8a-b54a-48e7-9b4b-7b04b36f3ce4",
  "sourceToolAssistantUUID": "71f8e3d7-28c6-4293-bf6a-8fdfb778fba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T18:18:49.886Z_

<details><summary>↩ Tool result · `toolu_01UXqNgrDT16yhmGKQ9RgmkL`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI Conference on Artificial Intelligence","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"}]

Based on the search results, here's what I found about the AAAI 2027 submission deadline:

The AAAI 2027 paper submission deadline is TBD (to be determined). However, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

The Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027. Additionally, track-specific deadlines are listed on their respective CFP, so different tracks may have different submission deadlines.

For the most current and detailed information, you can check the official AAAI-27 conference page at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b48a6611-ca4c-4659-9feb-750afd4a2e9a",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "3c7adfdd-7c64-466a-8b28-8e60cf7740ed",
  "sourceToolAssistantUUID": "b48a6611-ca4c-4659-9feb-750afd4a2e9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T18:18:50.453Z_

<details><summary>↩ Tool result · `toolu_01JqUJZLyzEUyDh2cpVmB4H7`</summary>

```text
Web search results for query: "ECCV 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://eccv.ecva.net/Conferences/2026/Dates"},{"title":"2026 Conference","url":"https://eccv.ecva.net/"},{"title":"ECCV 2026 Submission Policies","url":"https://eccv.ecva.net/Conferences/2026/SubmissionPolicies"},{"title":"ECCV 2026 Call for Papers","url":"https://eccv.ecva.net/Conferences/2026/CallForPapers"},{"title":"ECCV 2026 - AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=eccv26"},{"title":"Update ECCV 2026 with complete deadline information · huggingface/ai-deadlines at 3bccf2b","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/3bccf2b883c17d4536b469411fa413dc8711fdbb"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=eccv26"},{"title":"ECCV 2026 Conference | OpenReview","url":"https://openreview.net/group?id=thecvf.com%2FECCV%2F2026%2FConference"},{"title":"ECCV 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=eccv26"},{"title":"European Conference on Computer Vision (ECCV), 2026 | ServiceNow AI Research","url":"https://www.servicenow.com/research/event/2026-eccv.html"}]

Based on the search results, here are the key deadlines for ECCV 2026:

**Paper Registration Deadline:** February 26, 2026, at 11:00 PM CET

**Paper Submission Deadline:** March 5, 2026, at 11:00 PM CET

**Supplementary Materials Deadline:** March 12, 2026, at 11:00 PM CET

The submission deadline will not be extended.

The conference itself will be held September 8th through September 12th, 2026 at the Malmö Arena and Malmömässan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b983efb2-0ff0-478a-a4c6-e1c7629276ac",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "29e555b3-11da-4588-a859-ae84a5439d8e",
  "sourceToolAssistantUUID": "b983efb2-0ff0-478a-a4c6-e1c7629276ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T18:18:50.782Z_

<details><summary>↩ Tool result · `toolu_01KpwWi1jWkCxGMLQ6A6v26b`</summary>

```text
Web search results for query: "IROS 2026 submission deadline"

Links: [{"title":"IROS 2026 | IEEE/RSJ International Conference on Intelligent Robots and Systems","url":"https://2026.ieee-iros.org/"},{"title":"Update IROS 2026 conference data with official deadlines · huggingface/ai-deadlines at f5a1d9a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f5a1d9a7d8b4274d4c60ae755f25de60c466079d"},{"title":"Start Page of the Conference Management System","url":"https://ras.papercept.net/conferences/scripts/start.pl"},{"title":"IROS and CASE 2026 Paper Submission Deadline April 30","url":"https://www.linkedin.com/posts/ieee-transactions-on-robotics_robotics-iros2026-case2026-activity-7445124375567056896-L8xx"},{"title":"Important Dates - IROS 2026 | IEEE/RSJ International Conference on Intelligent Robots and Systems","url":"https://2026.ieee-iros.org/about/important-dates/"},{"title":"IROS 2026 in Pittsburgh,USA: Dates,Deadline,Fees & Registration Tips - Conference Inc.","url":"https://conferenceinc.net/post/iros-2026/"},{"title":"IROS: Intelligent RObots and Systems 2027 2026 2025 .. ...","url":"http://www.wikicfp.com/cfp/program?id=1660"},{"title":"International Conference on Intelligent Robots and Systems (IROS)","url":"https://www.allconferencealert.com/event/1870021"},{"title":"The Call for Papers for IROS 2026 is officially OPEN! Join ...","url":"https://www.facebook.com/ieeeiros/posts/-the-call-for-papers-for-iros-2026-is-officially-openjoin-one-of-the-worlds-larg/862566436746807/"},{"title":"Start Page of the Conference Management System - PaperPlaza","url":"https://ras.papercept.net/conferences/scripts-n/start.pl"}]

Based on the search results, here's the submission deadline information for IROS 2026:

The paper submission deadline for IROS 2026 is March 2, 2026, with paper video submission deadline on March 5, 2026. 

The paper acceptance notification is scheduled for June 16, 2026, and the final paper submission deadline is July 10, 2026.

IROS 2026 will take place from September 27 to October 1, 2026, in Pittsburgh, Pennsylvania, USA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5829dd8d-07f5-48bc-8a95-fb02034c92e7",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "cc443761-1057-484c-bbae-818c55aa0193",
  "sourceToolAssistantUUID": "5829dd8d-07f5-48bc-8a95-fb02034c92e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T18:18:51.115Z_

<details><summary>↩ Tool result · `toolu_01NFwzq38C77k4A1utrxSLSV`</summary>

```text
Web search results for query: "RSS 2026 submission deadline robotics"

Links: [{"title":"Call for Papers · Robotics: Science and Systems","url":"https://roboticsconference.org/information/cfp/"},{"title":"RSS 2026","url":"https://roboticsconference.org/"},{"title":"RSS SemRob 2026","url":"https://semrob.github.io/"},{"title":"[Meetings] RSS 2026 Call for Papers","url":"https://groups.google.com/g/rl-list/c/NDYhLboynpg"},{"title":"RSS 2026 Conference - Robotics","url":"https://openreview.net/group?id=roboticsfoundation.org%2FRSS%2F2026%2FConference"},{"title":"RSS: Robotics: Science and Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2506&f=Robotics"},{"title":"Robotics: Science and Systems on X: \"📢 Save the Date! RSS 2026 will take place July 13–17, 2026 in Sydney, Australia. Submission deadlines to be announced soon (likely mid–late January 2026). 🦾 Prepare your best work! https://t.co/ybIds7mOMq\" / X","url":"https://x.com/RoboticsSciSys/status/1976107492808482875"},{"title":"Calendar - RSS Foundation","url":"https://roboticsfoundation.org/policies/calendar/"},{"title":"Call for Workshops · Robotics: Science and Systems","url":"https://roboticsconference.org/information/cfw/"}]

Based on the search results, here's what I found about RSS 2026 submission deadlines:

## Main Conference Paper Submission

The search results show that RSS 2026 is being held July 13-17, 2026, in Sydney, Australia. However, the specific paper submission deadline is not explicitly stated in these results. According to the RSS Foundation's calendar, the paper submission deadline typically falls at the end of January for the conference held the same year, so it would be expected around late January 2026.

## Workshop Submissions

For workshops, proposals should be submitted by February 12, 2026, 23:59 AOE.

## Supplementary Materials

The deadline for the submission of supplementary material is one week after the deadline for paper submissions.

For more specific information about the exact paper submission deadline, I'd recommend checking the official RSS 2026 Call for Papers page at roboticsconference.org/information/cfp/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d153880a-ec43-4d93-b115-9dc27d172bd2",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "9022661f-71c7-423d-8ae8-4caf930d1bf7",
  "sourceToolAssistantUUID": "d153880a-ec43-4d93-b115-9dc27d172bd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T18:18:55.109Z_

<details><summary>↩ Tool result · `toolu_0158C6gQ79PniQXaRmZ4LCMr`</summary>

```text
Web search results for query: "top AI conference deadlines 2026 2027"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Deadlines - a Hugging Face Space by huggingface","url":"https://huggingface.co/spaces/huggingface/ai-deadlines"},{"title":"AI Conference Deadlines","url":"https://nunoduarte.github.io/deadlines/"},{"title":"GitHub - khairulislam/ML-conferences: List of ML conferences with important dates and accepted paper list · GitHub","url":"https://github.com/khairulislam/ML-conferences"},{"title":"AI Conferences 2026 — CFP Deadlines & Dates (NeurIPS, ICML, CVPR, AAAI) | TLDL | TLDL","url":"https://www.tldl.io/resources/ai-conferences-2026"},{"title":"Top Artificial Intelligence (AI) Conferences for 2026: A Researcher's Guide--iConf","url":"https://www.iconf.org/news/731"},{"title":"AI Conference Deadlines 2026 | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/"},{"title":"23 AI Conferences Worth Attending in 2026: Complete Guide with Dates, Locations, and What to Expect | ALM Corp","url":"https://almcorp.com/blog/ai-conferences-2026-complete-guide/"}]

I found comprehensive information about top AI conference deadlines for 2026 and 2027. Here are some key conferences:

## Major 2026 AI Conferences:

**AAAI-26** - January 20-27, 2026 in Singapore EXPO

**ICLR 2026** - April 23-27, 2026 in Rio de Janeiro, Brazil with paper submission deadline September 20, 2025

**CVPR 2026** - July 2-7, 2026 in San Diego, California, United States

**ICML 2026** - June 16-19, 2026 in Amsterdam, Netherlands

**NeurIPS 2026** - December 6, 2026 in Sydney, Australia with paper submission deadline May 11, 2026

**ECCV 2026** - September 27-October 1, 2026 in Sydney, Australia

## Major 2027 AI Conferences:

**AAAI-27** - February 8-11, 2027 in Helsinki, Finland

**ICML 2027** - May 16-21, 2027 in Toronto, Canada

For more detailed and regularly updated deadline information, several resources maintain comprehensive lists: aideadlines.org and Hugging Face's AI Deadlines app which shows a curated list of upcoming AI conference and workshop deadlines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82e3af7f-ddc1-4574-bb27-d86e62424028",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "d880c36e-dffb-453f-b9d8-c55e324f445a",
  "sourceToolAssistantUUID": "82e3af7f-ddc1-4574-bb27-d86e62424028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-18T18:18:58.156Z_

Let me get more specific details on a few conferences where deadlines may still be upcoming.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d880c36e-dffb-453f-b9d8-c55e324f445a",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVfxjShhtDB7JJbhTjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39362a7f-006c-4736-aa85-84e4d6202048",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXPnY6RxiV8LhrT3HkBeuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 9559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7092,
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

_source line 28 · 2026-05-18T18:18:59.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WUYmpEoWGmAD9J81PgDThT`</summary>

```json
{
  "query": "NeurIPS 2026 abstract deadline May 11 or May 4 exact date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39362a7f-006c-4736-aa85-84e4d6202048",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVfxjShhtDB7JJbhTjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d1f858b-38a2-49c3-900a-d165b8d6ffe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXPnY6RxiV8LhrT3HkBeuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 9559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7092,
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

_source line 29 · 2026-05-18T18:18:59.622Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VtK7Lzhb3nEqhqnD5yd3MS`</summary>

```json
{
  "query": "AAAI 2027 submission deadline August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d1f858b-38a2-49c3-900a-d165b8d6ffe2",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVfxjShhtDB7JJbhTjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7dec152-8d39-4987-8a5e-6b1bdb4c34e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXPnY6RxiV8LhrT3HkBeuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 9559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7092,
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

_source line 30 · 2026-05-18T18:18:59.628Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NvLPUz3ye1UyYzKfWEDqPB`</summary>

```json
{
  "query": "ICML 2027 submission deadline date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7dec152-8d39-4987-8a5e-6b1bdb4c34e3",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVfxjShhtDB7JJbhTjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5c17967-7acf-4d26-b92b-d15a981c8f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXPnY6RxiV8LhrT3HkBeuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 9559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7092,
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

_source line 31 · 2026-05-18T18:19:00.151Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011K4n7sbAQxsffbCkLza3qM`</summary>

```json
{
  "query": "CVPR 2027 paper submission deadline November 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5c17967-7acf-4d26-b92b-d15a981c8f56",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVfxjShhtDB7JJbhTjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05f2aef2-0b3d-4b45-9749-dde44a253535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXPnY6RxiV8LhrT3HkBeuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 9559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7092,
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

_source line 32 · 2026-05-18T18:19:00.811Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XYztr8tGTQmPcHgLeS4FWk`</summary>

```json
{
  "query": "CoRL 2026 abstract deadline May 26 paper deadline May 28"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05f2aef2-0b3d-4b45-9749-dde44a253535",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVfxjShhtDB7JJbhTjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9af60dd7-1181-4bf8-8cae-604599625347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXPnY6RxiV8LhrT3HkBeuE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 9559,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7092
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 282,
          "cache_read_input_tokens": 9559,
          "cache_creation_input_tokens": 7092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7092,
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

_source line 33 · 2026-05-18T18:19:02.373Z_

<details><summary>↩ Tool result · `toolu_01WUYmpEoWGmAD9J81PgDThT`</summary>

```text
Web search results for query: "NeurIPS 2026 abstract deadline May 11 or May 4 exact date"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"NeurIPS 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/neurips-2026.html"},{"title":"NeurIPS Conference on X: \"The NeurIPS 2026 submission site opening has been moved to April 15th. Note that all tracks (Main Submission, Evaluations &amp; Datasets, and Position Papers) share the same dates. The final submission deadlines remain unchanged: • Paper Abstracts: May 4th (AOE) • Full Papers:\" / X","url":"https://x.com/NeurIPSConf/status/2041303457554940336"},{"title":"2026 Conference","url":"https://neurips.cc/"},{"title":"NeurIPS Newsletter – April 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/"},{"title":"NeurIPS 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=neurips26"}]

Based on the search results, the abstract submission deadline for NeurIPS 2026 is May 4, 2026 (AOE). This is confirmed across multiple official sources from NeurIPS, including their Call for Papers page and recent newsletters.

So to answer your question: the exact date is **May 4, 2026**, not May 11.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d1f858b-38a2-49c3-900a-d165b8d6ffe2",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "da1ac7e0-10d4-4360-b699-5a6d3285b511",
  "sourceToolAssistantUUID": "3d1f858b-38a2-49c3-900a-d165b8d6ffe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T18:19:03.070Z_

<details><summary>↩ Tool result · `toolu_01NvLPUz3ye1UyYzKfWEDqPB`</summary>

```text
Web search results for query: "ICML 2027 submission deadline date"

Links: [{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"Conferences Future Meetings","url":"https://icml.cc/Conferences/FutureMeetings"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICML 2027","url":"https://icml2027.eurac.edu/en"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"ICML 2026","url":"https://icml.cc/"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"ICML: International Conference on Machine Learning 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1421"}]

Based on the search results, I found information about ICML 2027, but the specific submission deadline for the machine learning conference has not yet been officially announced.

ICML 2027 is scheduled for July 2027 with details marked as TBA (To Be Announced), with the deadline predicted based on historical patterns. However, the official submission deadline date has not yet been released.

For the most current and accurate information about ICML 2027 submission deadlines, I recommend checking the official ICML website at icml.cc, as they typically announce detailed deadlines and dates closer to the actual submission period.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5c17967-7acf-4d26-b92b-d15a981c8f56",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "fb1fce51-c98b-421e-92ef-b6f4f356e552",
  "sourceToolAssistantUUID": "e5c17967-7acf-4d26-b92b-d15a981c8f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T18:19:03.593Z_

<details><summary>↩ Tool result · `toolu_01VtK7Lzhb3nEqhqnD5yd3MS`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline August 2026"

Links: [{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AAAI Conference on Artificial Intelligence","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"}]

Based on the search results, I found the AAAI 2027 submission deadline information:

The AAAI-27 submission deadlines are July 21, 2026 for abstracts at 11:59 PM UTC-12, and July 28, 2026 for full papers at 11:59 PM UTC-12. Supplementary material and code are due by July 31, 2026 at 11:59 PM UTC-12.

These deadlines fall slightly before August 2026 rather than in August. The Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7dec152-8d39-4987-8a5e-6b1bdb4c34e3",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "31a6198e-d6fe-4d49-a34c-73a7465b0936",
  "sourceToolAssistantUUID": "a7dec152-8d39-4987-8a5e-6b1bdb4c34e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T18:19:04.253Z_

<details><summary>↩ Tool result · `toolu_011K4n7sbAQxsffbCkLza3qM`</summary>

```text
Web search results for query: "CVPR 2027 paper submission deadline November 2026"

Links: [{"title":"CVPR 2026 - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/"},{"title":"CVPR: Computer Vision and Pattern Recognition 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=628"},{"title":"Important Dates and Deadlines - CVPR 2026","url":"https://cvpr.thecvf.com/Conferences/2026/Dates"},{"title":"2025 Dates and Deadlines - CVPR 2026","url":"https://cvpr.thecvf.com/Conferences/2025/Dates"},{"title":"CVPR 2026 Call for Papers - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/Conferences/2026/CallForPapers"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"CVPR 2026 Guide: Dates, Deadlines, Topics & Tips for Denver","url":"https://conferenceinc.net/post/cvpr-2026/"},{"title":"One Year Calendar of Computer Image Analysis, Computer Vision Conferences","url":"http://conferences.visionbib.com/Browse-data.php?order=Due&ascdsc=DESC&year=2027"},{"title":"Conference Calendar for Computer Vision, Image Analysis and Related Topics","url":"http://conferences.visionbib.com/Iris-Conferences.html"}]

Based on the search results, I found information about CVPR 2026 but not specific details about CVPR 2027's paper submission deadline in November 2026. The search results primarily contain information about CVPR 2026, which had a submission deadline of November 13, 2025.

The results did not include detailed information about CVPR 2027's submission schedule. To get accurate information about CVPR 2027's paper submission deadline, I would recommend:

1. Visiting the official CVPR website (cvpr.thecvf.com) directly once the call for papers is announced
2. Checking conference announcement databases like WikiCFP or the Computer Vision Foundation's official pages
3. Monitoring the official CVPR social media accounts for announcements about CVPR 2027

Typically, major conference deadlines are announced several months in advance, so the official CVPR 2027 deadline information may not yet be publicly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05f2aef2-0b3d-4b45-9749-dde44a253535",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "b4a09bad-407b-465d-a5ee-4bcf2e283f17",
  "sourceToolAssistantUUID": "05f2aef2-0b3d-4b45-9749-dde44a253535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T18:19:04.867Z_

<details><summary>↩ Tool result · `toolu_01XYztr8tGTQmPcHgLeS4FWk`</summary>

```text
Web search results for query: "CoRL 2026 abstract deadline May 26 paper deadline May 28"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"AI Conference Deadlines","url":"https://mldeadlines.com/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"}]

Based on the search results, here's what I found about CoRL 2026 deadlines:

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC. However, there's a slight discrepancy regarding the paper deadline—the paper submission deadline is Thursday (5/28) EOD rather than Friday, according to the official CoRL website instructions for authors.

CoRL 2026 will be held November 9-12, 2026 in Austin, Texas, US.

For submissions, papers may be submitted through OpenReview, and the deadlines are final, and accommodations cannot be made for missing the abstract deadline or paper deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9af60dd7-1181-4bf8-8cae-604599625347",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "fca1dfe9-4050-4727-a272-3124456d2dcb",
  "sourceToolAssistantUUID": "9af60dd7-1181-4bf8-8cae-604599625347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-18T18:19:08.071Z_

Now let me get a few more details on conferences with upcoming deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fca1dfe9-4050-4727-a272-3124456d2dcb",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVggnn4V9yJm8Qf13kf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9627b1f-51b2-4c62-b8ba-512537cdc71b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZWT5xAANXKBoQ9x7yJgyN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3482,
      "cache_read_input_tokens": 16651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3482,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 39 · 2026-05-18T18:19:08.614Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HxLJH6pregECBS9vNxprBv`</summary>

```json
{
  "query": "NeurIPS 2026 full paper submission deadline May 6 AOE exact"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9627b1f-51b2-4c62-b8ba-512537cdc71b",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVggnn4V9yJm8Qf13kf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f8a4173-dbb1-4951-9cbc-27f138b58629",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZWT5xAANXKBoQ9x7yJgyN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3482,
      "cache_read_input_tokens": 16651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3482,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 40 · 2026-05-18T18:19:09.023Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WBKp3pzVo1YUH3Wj4rhWtZ`</summary>

```json
{
  "query": "ICLR 2027 call for papers submission deadline announcement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f8a4173-dbb1-4951-9cbc-27f138b58629",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVggnn4V9yJm8Qf13kf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "022bfca3-fffb-48c1-aa8a-2b2f1fd9019b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZWT5xAANXKBoQ9x7yJgyN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3482,
      "cache_read_input_tokens": 16651,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3482
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 16651,
          "cache_creation_input_tokens": 3482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3482,
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

_source line 41 · 2026-05-18T18:19:11.793Z_

<details><summary>↩ Tool result · `toolu_01HxLJH6pregECBS9vNxprBv`</summary>

```text
Web search results for query: "NeurIPS 2026 full paper submission deadline May 6 AOE exact"

Links: [{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026 Evaluations & Datasets FAQ","url":"https://neurips.cc/Conferences/2026/EvaluationsDatasetsFAQ"},{"title":"NeurIPS Newsletter – April 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/"},{"title":"research/docs/submission-guides/neurips-2026.md at main · serre-ai/research","url":"https://github.com/serre-ai/research/blob/main/docs/submission-guides/neurips-2026.md"},{"title":"General – NeurIPS Blog","url":"https://blog.neurips.cc/category/general/"},{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"NeurIPS 2026 LaTeX Template | Download & Formatting Guide | Underleaf","url":"https://www.underleaf.ai/templates/neurips"}]

Based on the search results, I can confirm the information you requested:

The full paper submission deadline for NeurIPS 2026, including all supplementary materials, is May 6, 2026 AOE (Anywhere On Earth).

This deadline applies to the main track and other submission tracks. The abstract submission deadline is May 4, 2026 (AOE), which comes two days before the full paper deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f8a4173-dbb1-4951-9cbc-27f138b58629",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "fbc0b3e6-9f00-483c-bd89-8857f2a7cc6b",
  "sourceToolAssistantUUID": "1f8a4173-dbb1-4951-9cbc-27f138b58629",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T18:19:13.615Z_

<details><summary>↩ Tool result · `toolu_01WBKp3pzVo1YUH3Wj4rhWtZ`</summary>

```text
Web search results for query: "ICLR 2027 call for papers submission deadline announcement"

Links: [{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"}]

Based on the search results, I found information about ICLR conferences, but the official announcement specifically for ICLR 2027's call for papers and submission deadline does not appear to be available yet in the search results.

Here's what I found:

- The most recent official ICLR information in the search results is for ICLR 2026, which is currently in progress.
- One source indicates ICLR 2027 is predicted to be April 24-28, 2027, based on previous year schedule, though it notes "Please verify on the official conference website."

For the official ICLR 2027 Call for Papers announcement and submission deadline, I recommend checking the official ICLR website at **iclr.cc** directly, as they typically release detailed CFP information several months in advance of the conference. The search results suggest that ICLR 2027 may be scheduled for April 2027, but the specific submission deadline announcement does not appear to have been published yet as of May 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "022bfca3-fffb-48c1-aa8a-2b2f1fd9019b",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "afa08300d4c78e69b",
  "type": "user",
  "uuid": "659f4735-c41e-4fe6-8e9d-ab0212c845cf",
  "sourceToolAssistantUUID": "022bfca3-fffb-48c1-aa8a-2b2f1fd9019b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-18T18:19:40.085Z_

Here is a comprehensive summary of upcoming top-tier AI/ML/robotics conference submission deadlines relative to today (2026-05-18):

---

## Conferences with Deadlines STILL OPEN (After 2026-05-18)

### 1. CoRL 2026 (Conference on Robot Learning)
- **Tier:** Solid (top venue for robot learning)
- **Abstract deadline:** May 26, 2026, 11:59 UTC
- **Full paper deadline:** May 28/29, 2026, 11:59 UTC (sources show slight discrepancy between May 28 and May 29)
- **Conference dates:** November 9-12, 2026, Austin, TX
- **Status: OPEN -- about 10 days remaining**
- Sources: [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers), [CoRL 2026 Instructions for Authors](https://www.corl.org/contributions/instruction-for-authors)

### 2. AAAI 2027 (AAAI Conference on Artificial Intelligence)
- **Tier:** Top-tier
- **Abstract deadline:** July 21, 2026, 11:59 PM UTC-12
- **Full paper deadline:** July 28, 2026, 11:59 PM UTC-12
- **Supplementary material/code:** July 31, 2026, 11:59 PM UTC-12
- **Conference dates:** February 16-23, 2027, Montreal, Canada
- **Status: OPEN -- about 2 months away**
- Sources: [AAAI-27 Official Page](https://aaai.org/conference/aaai/aaai-27/), [AI Deadlines - AAAI 2027](http://aideadlines.org/conference/?id=aaai27)

---

## Conferences with Deadlines NOT YET ANNOUNCED (Expected After 2026-05-18)

### 3. ICLR 2027
- **Tier:** Top-tier
- **Submission deadline:** Not yet announced. Based on ICLR 2026 patterns (deadline was September 2025), expect around **September-October 2026**.
- **Conference dates:** Predicted April 2027 (not officially confirmed)
- Sources: [ICLR Official](https://iclr.cc/), [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)

### 4. CVPR 2027
- **Tier:** Top-tier (computer vision)
- **Submission deadline:** Not yet announced. Based on CVPR 2026 patterns (deadline was November 2025), expect around **November 2026**.
- **Conference dates:** June 19-26, 2027, Seattle
- Sources: [CVPR Official](https://cvpr.thecvf.com/), [WikiCFP - CVPR](http://www.wikicfp.com/cfp/program?id=628)

### 5. ICML 2027
- **Tier:** Top-tier
- **Submission deadline:** Not yet announced. Based on ICML 2026 patterns (deadline was January 2026), expect around **January 2027**.
- **Conference dates:** July 2027 (likely Toronto, Canada)
- Sources: [ICML Future Meetings](https://icml.cc/Conferences/FutureMeetings), [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)

---

## Conferences with Deadlines ALREADY PASSED (Before 2026-05-18)

| Conference | Deadline | Status |
|---|---|---|
| **NeurIPS 2026** (Top-tier) | Abstract: May 4, 2026; Paper: May 6, 2026 AOE | **PASSED** (12-14 days ago) |
| **ICML 2026** (Top-tier) | January 28, 2026 | **PASSED** |
| **ICLR 2026** (Top-tier) | September 20, 2025 | **PASSED** |
| **ECCV 2026** (Top-tier, vision) | Registration: Feb 26; Paper: March 5, 2026 | **PASSED** |
| **CVPR 2026** (Top-tier, vision) | November 13, 2025 | **PASSED** |
| **RSS 2026** (Solid, robotics) | Late January 2026 | **PASSED** |
| **IROS 2026** (Solid, robotics) | March 2, 2026 | **PASSED** |

---

## Key Takeaways

**Immediate opportunity:** CoRL 2026 has a deadline in ~10 days (May 26/28-29). This is the most urgent open deadline.

**Near-term opportunity:** AAAI 2027 abstracts are due July 21, 2026, giving you about 2 months to prepare.

**NeurIPS 2026 just closed:** The deadline passed on May 6, so you narrowly missed it.

**Plan ahead for fall/winter 2026:** ICLR 2027 (~Sep/Oct 2026), CVPR 2027 (~Nov 2026), and ICML 2027 (~Jan 2027) deadlines have not been announced yet but are expected based on historical patterns. Monitor [AI Deadlines](http://aideadlines.org/) and [Hugging Face AI Deadlines](https://huggingface.co/spaces/huggingface/ai-deadlines) for announcements.

Sources:
- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)
- [NeurIPS 2026 Call for Papers](https://neurips.cc/Conferences/2026/CallForPapers)
- [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates)
- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instructions for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [ECCV 2026 Dates](https://eccv.ecva.net/Conferences/2026/Dates)
- [AAAI-27 Official Page](https://aaai.org/conference/aaai/aaai-27/)
- [CVPR Official](https://cvpr.thecvf.com/)
- [IROS 2026 Important Dates](https://2026.ieee-iros.org/about/important-dates/)
- [RSS 2026 Call for Papers](https://roboticsconference.org/information/cfp/)
- [AI Deadlines](http://aideadlines.org/)
- [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)
- [Hugging Face AI Deadlines](https://huggingface.co/spaces/huggingface/ai-deadlines)
- [MLciv AI Deadlines](https://mlciv.com/ai-deadlines/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "659f4735-c41e-4fe6-8e9d-ab0212c845cf",
  "isSidechain": true,
  "agentId": "afa08300d4c78e69b",
  "requestId": "req_011CbAVhKryCtc1s4LS8xGnD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fb7556b-12f9-4ee4-a47d-e513afe52433",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNhXpwUpD5aNWaqxmoJ2m3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1383,
      "cache_read_input_tokens": 20133,
      "output_tokens": 1813,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1383
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1813,
          "cache_read_input_tokens": 20133,
          "cache_creation_input_tokens": 1383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1383,
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
