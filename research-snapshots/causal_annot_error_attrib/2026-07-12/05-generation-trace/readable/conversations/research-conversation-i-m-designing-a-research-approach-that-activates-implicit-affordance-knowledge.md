# Research conversation: I'm designing a research approach that activates implicit affordance knowledge in VLMs for VLA (Vision-Language-Action) 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a464db43d225e4e3c.jsonl`
- **Structured JSON:** [`fefa620db49f4c7c27ee.json`](../../sessions/fe/fefa620db49f4c7c27ee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-18T18:19:08.775Z_

I'm designing a research approach that activates implicit affordance knowledge in VLMs for VLA (Vision-Language-Action) robot manipulation. I need to understand the technical building blocks. Search for:

1. WebSearch: "cross-attention affordance features robot manipulation transformer"
2. WebSearch: "DINO feature extraction affordance part segmentation 2025 2026"
3. WebSearch: "language-conditioned attention mechanism manipulation policy"
4. WebSearch: "VLM internal representations affordance probing 2026"
5. WebSearch: "adapter module VLA fine-tuning efficient 2025 2026"
6. WebSearch: "LoRA VLA fine-tuning robot manipulation"
7. WebSearch: "SIMPLER benchmark VLA evaluation 2026"
8. WebSearch: "LIBERO benchmark robot manipulation evaluation"

Report:
- How DINO features have been used for affordance estimation (specific layers, techniques)
- What attention mechanisms have been used to inject affordance info into policies
- What evaluation benchmarks are standard for VLA models (SIMPLER, LIBERO, real-world)
- What efficient fine-tuning approaches exist for VLA models
- Technical details on how to extract and use intermediate VLM features for affordance

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "58dadf3e-e669-42df-b07b-dde3fb841523",
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

_source line 2 · 2026-05-18T18:19:08.799Z_

```json
{
  "parentUuid": "58dadf3e-e669-42df-b07b-dde3fb841523",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
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
  "uuid": "5f0b5a1c-a163-43ce-b69a-b86def2d6a09",
  "timestamp": "2026-05-18T18:19:08.799Z",
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

_source line 3 · 2026-05-18T18:19:11.903Z_



I'll search for all these topics in parallel to gather comprehensive information on the technical building blocks for your research approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f0b5a1c-a163-43ce-b69a-b86def2d6a09",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVgyLSEz6UDHDsKoeTe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54a90044-d01d-4a2a-aa5b-8c45cd571ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGyGYWYmF7L3GzUjKH1Lgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 817,
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

_source line 4 · 2026-05-18T18:19:11.975Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GQVipkCKjZVgNm92YcgBtS`</summary>

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
  "parentUuid": "54a90044-d01d-4a2a-aa5b-8c45cd571ff3",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVgyLSEz6UDHDsKoeTe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8924a863-9941-48c6-b8fd-6680c326c58b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGyGYWYmF7L3GzUjKH1Lgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 817,
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

_source line 5 · 2026-05-18T18:19:11.978Z_

<details><summary>↩ Tool result · `toolu_01GQVipkCKjZVgNm92YcgBtS`</summary>

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
  "parentUuid": "8924a863-9941-48c6-b8fd-6680c326c58b",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "edde6368-bc0c-494f-a7cf-eb921af08bb3",
  "sourceToolAssistantUUID": "8924a863-9941-48c6-b8fd-6680c326c58b",
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

_source line 6 · 2026-05-18T18:19:14.755Z_



Now let me launch all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edde6368-bc0c-494f-a7cf-eb921af08bb3",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVhD99Qg8XM5sYLxsbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "015fe8ee-1842-466b-919b-fb9220c9499a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyamUq8QmhYf888BuGBrtw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 7 · 2026-05-18T18:19:14.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A21bigomaWa1gA8L7WEVjt`</summary>

```json
{
  "query": "cross-attention affordance features robot manipulation transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "015fe8ee-1842-466b-919b-fb9220c9499a",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVhD99Qg8XM5sYLxsbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7ee71f5-a014-4be9-8559-ce07ce14ccc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyamUq8QmhYf888BuGBrtw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 8 · 2026-05-18T18:19:15.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HhsKoQL1RLhtHJyKgxAd1m`</summary>

```json
{
  "query": "DINO feature extraction affordance part segmentation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7ee71f5-a014-4be9-8559-ce07ce14ccc8",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVhD99Qg8XM5sYLxsbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "731d6436-748f-48cc-b6b3-c41866f4a96f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyamUq8QmhYf888BuGBrtw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 9 · 2026-05-18T18:19:15.706Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LvuH3dD5xkvGKYDuG4SYMV`</summary>

```json
{
  "query": "language-conditioned attention mechanism manipulation policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "731d6436-748f-48cc-b6b3-c41866f4a96f",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVhD99Qg8XM5sYLxsbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cde5b01-aa61-491c-9e4a-6d7a80f2557b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyamUq8QmhYf888BuGBrtw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 10 · 2026-05-18T18:19:15.711Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014WyutUdaGCZ831JQdCb7Ha`</summary>

```json
{
  "query": "VLM internal representations affordance probing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cde5b01-aa61-491c-9e4a-6d7a80f2557b",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVhD99Qg8XM5sYLxsbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da11c248-73cb-4eb0-942b-a24df96c87b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyamUq8QmhYf888BuGBrtw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 11 · 2026-05-18T18:19:16.178Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BgxHdyTDbMxRGTFutv6URq`</summary>

```json
{
  "query": "adapter module VLA fine-tuning efficient 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da11c248-73cb-4eb0-942b-a24df96c87b9",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVhD99Qg8XM5sYLxsbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab3a61e1-54d7-4dbd-af21-bb9640ab9c25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyamUq8QmhYf888BuGBrtw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 12 · 2026-05-18T18:19:16.647Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017FHWcrGoFWGjaN9m1UVJtx`</summary>

```json
{
  "query": "LoRA VLA fine-tuning robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab3a61e1-54d7-4dbd-af21-bb9640ab9c25",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVhD99Qg8XM5sYLxsbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b859184e-cd41-4772-806e-8b9a133cb831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyamUq8QmhYf888BuGBrtw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 13 · 2026-05-18T18:19:17.009Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wigf82VJGRnDEPPC34oGBs`</summary>

```json
{
  "query": "SIMPLER benchmark VLA evaluation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b859184e-cd41-4772-806e-8b9a133cb831",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVhD99Qg8XM5sYLxsbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba3ee5ca-b2fe-43f6-9ee4-11d91f3d1f62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyamUq8QmhYf888BuGBrtw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8121,
      "output_tokens": 391,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 391,
          "cache_read_input_tokens": 8121,
          "cache_creation_input_tokens": 1417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1417,
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

_source line 14 · 2026-05-18T18:19:17.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0113EahY3FPm4sNtZRjNLbY5`</summary>

```json
{
  "query": "LIBERO benchmark robot manipulation evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba3ee5ca-b2fe-43f6-9ee4-11d91f3d1f62",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVhD99Qg8XM5sYLxsbs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbb9c72c-9385-4abf-862a-434525c3a4dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyamUq8QmhYf888BuGBrtw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8121,
      "output_tokens": 391,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 391,
          "cache_read_input_tokens": 8121,
          "cache_creation_input_tokens": 1417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1417,
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

_source line 15 · 2026-05-18T18:19:21.040Z_

<details><summary>↩ Tool result · `toolu_01LvuH3dD5xkvGKYDuG4SYMV`</summary>

```text
Web search results for query: "language-conditioned attention mechanism manipulation policy"

Links: [{"title":"Modularity through Attention: Efficient Training and Transfer of   Language-Conditioned Policies for Robot Manipulation","url":"https://arxiv.org/pdf/2212.04573"},{"title":"Modularity through Attention: Efficient Training and Transfer of Language-Conditioned Policies for Robot Manipulation","url":"https://languageforrobots.com/"},{"title":"Modularity through Attention: Efficient Training and Transfer of Language-Conditioned Policies for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=uCaNr6_dQB0"},{"title":"[2212.04573] Modularity through Attention: Efficient Training and Transfer of Language-Conditioned Policies for Robot Manipulation","url":"https://arxiv.org/abs/2212.04573"},{"title":"(PDF) Learning Modular Language-Conditioned Robot Policies through Attention","url":"https://www.researchgate.net/publication/373752641_Learning_Modular_Language-Conditioned_Robot_Policies_through_Attention"},{"title":"Spatial-Language Attention Policies for Efficient Robot Learning","url":"https://arxiv.org/pdf/2304.11235"},{"title":"Learning modular language-conditioned robot policies through attention | Autonomous Robots | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10514-023-10129-1"},{"title":"CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity","url":"https://arxiv.org/pdf/2506.16652"}]

Based on the search results, here's what I found about language-conditioned attention mechanism manipulation policy:

## Key Research

Language-conditioned policies allow robots to interpret and execute human instructions, and researchers have proposed sample-efficient approaches for training language-conditioned manipulation policies that allow for rapid transfer across different types of robots.

## Hierarchical Modularity Approach

A novel method called Hierarchical Modularity uses supervised attention across multiple sub-modules to bridge the divide between modular and end-to-end learning and enable the reuse of functional building blocks. This method outperforms current state-of-the-art methods and can transfer policies across 4 different robots in a sample-efficient manner.

## Related Approaches

Additional research in this area includes Spatial-Language Attention Policies (SLAP), which uses three-dimensional tokens as the input representation to train a single multi-task, language-conditioned action prediction policy.

More recent work addresses language ambiguity, where natural language instructions for robotic manipulation tasks often exhibit ambiguity and vagueness, such as "Hang a mug on the mug tree" which may involve multiple valid actions if there are several mugs and branches to choose from.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cde5b01-aa61-491c-9e4a-6d7a80f2557b",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "b0522da1-b4d2-492e-a286-c713aa1f945d",
  "sourceToolAssistantUUID": "5cde5b01-aa61-491c-9e4a-6d7a80f2557b",
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

_source line 16 · 2026-05-18T18:19:21.501Z_

<details><summary>↩ Tool result · `toolu_01A21bigomaWa1gA8L7WEVjt`</summary>

```text
Web search results for query: "cross-attention affordance features robot manipulation transformer"

Links: [{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/html/2409.01083v4"},{"title":"Learning Precise Affordances from Egocentric Videos for Robotic Manipulation","url":"https://arxiv.org/html/2408.10123v2"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.researchgate.net/publication/385560182_RT-Affordance_Affordances_are_Versatile_Intermediate_Representations_for_Robot_Manipulation"},{"title":"AFFORD2ACT: Affordance-Guided Automatic Keypoint Selection for Generalizable and Lightweight Robotic Manipulation","url":"https://arxiv.org/pdf/2510.01433"},{"title":"Cross-Embodiment Robotic Manipulation Synthesis via Guided Demonstrations through CycleVAE and Human Behavior Transformer","url":"https://arxiv.org/html/2503.08622"},{"title":"CroSTAta: Cross-State Transition Attention Transformer for Robotic Manipulation","url":"https://arxiv.org/html/2510.00726v1"}]

The search results reveal several recent research papers on robot manipulation using transformers and affordances:

One framework unifies affordance map learning and action generation for robot manipulation, where the model first extracts instruction-relevant manipulation affordances through a prompt tuning method that prepends learnable text-conditioned prompts in a frozen vision foundation model, then uses a flow matching policy to transform random waypoints to desired action trajectories guided by task-relevant affordance maps.

The Geometry-guided Affordance Transformer (GAT) incorporates shape and geometric priors to learn affordances, and its design contains several cross-attention layers followed by residual connections.

AFFORD2ACT follows a three-stage pipeline involving affordance filtering, category-level keypoint construction, and transformer-based policy learning with embedded gating to reason about relevant keypoints.

Another approach proposes cross-attention mechanisms with contrastive losses to enable robots to complete manipulation tasks by observing human demonstrations and learning unified representations using paired human video and robot trajectory datasets.

A Cross-State Transition Attention Transformer employs a novel State Transition Attention mechanism to modulate standard attention weights based on learned state evolution patterns, enabling policies to better adapt their behavior based on execution history.

These approaches demonstrate the integration of cross-attention mechanisms, affordance representations, and transformer architectures as key components in modern robot manipulation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7ee71f5-a014-4be9-8559-ce07ce14ccc8",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "6f5c54e5-1308-4eaa-9530-3f0fdb033dba",
  "sourceToolAssistantUUID": "d7ee71f5-a014-4be9-8559-ce07ce14ccc8",
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

_source line 17 · 2026-05-18T18:19:21.705Z_

<details><summary>↩ Tool result · `toolu_017FHWcrGoFWGjaN9m1UVJtx`</summary>

```text
Web search results for query: "LoRA VLA fine-tuning robot manipulation"

Links: [{"title":"[2512.11921] Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/abs/2512.11921"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251211921Y/abstract"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"(PDF) Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://www.researchgate.net/publication/398721162_Towards_Accessible_Physical_AI_LoRA-Based_Fine-Tuning_of_VLA_Models_for_Real-World_Robot_Control"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.11921v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=real-world+episodes"}]

Here are the search results for "LoRA VLA fine-tuning robot manipulation":

The search found a recently published research paper titled "Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control" which focuses on Vision-Language-Action (VLA) models that enable robots to execute natural language commands through end-to-end learning from visual observations.

**Key findings from the research:**

The paper proposes a resource-efficient fine-tuning strategy using Low-Rank Adaptation (LoRA) and quantization techniques that enable multi-billion parameter VLA models (3.1B parameters) to run on consumer-grade GPUs with 8GB VRAM.

The methodology addresses the critical challenge of adapting pre-trained VLA models to new robot embodiments with limited demonstration data, focusing on the trade-offs between frozen and unfrozen vision encoders.

**Real-World Deployment:**

The approach was demonstrated through real-world deployment on the SO101 robotic arm for a button-pressing manipulation task, and achieved a 74-76% success rate with 200 demonstration episodes, operating at 20 Hz control frequency.

The results show that with proper fine-tuning methodology, VLA models can be successfully deployed on affordable robotic platforms, making advanced manipulation capabilities accessible beyond expensive research robots.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b859184e-cd41-4772-806e-8b9a133cb831",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "cd5396a8-bd65-4935-8e35-3a5eadef265d",
  "sourceToolAssistantUUID": "b859184e-cd41-4772-806e-8b9a133cb831",
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

_source line 18 · 2026-05-18T18:19:22.227Z_

<details><summary>↩ Tool result · `toolu_01Wigf82VJGRnDEPPC34oGBs`</summary>

```text
Web search results for query: "SIMPLER benchmark VLA evaluation 2026"

Links: [{"title":"[2603.13966] vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.13966"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"VLA-Arena: Benchmark for VLA Models","url":"https://www.emergentmind.com/papers/2512.22539"},{"title":"VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness | OpenReview","url":"https://openreview.net/forum?id=31EjDFwFEe"},{"title":"vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.13966"},{"title":"GitHub - OpenMOSS/VLABench: Official repo of VLABench, a large scale benchmark designed for fairly evaluating VLA, Embodied Agent, and VLMs. · GitHub","url":"https://github.com/OpenMOSS/VLABench"},{"title":"GitHub - PKU-Alignment/VLA-Arena: VLA-Arena is an open-source benchmark for systematic evaluation of Vision-Language-Action (VLA) models. · GitHub","url":"https://github.com/PKU-Alignment/VLA-Arena"},{"title":"VLANeXt: Recipes for Building Strong VLA Models","url":"https://arxiv.org/pdf/2602.18532"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"}]

Based on the search results, here's what I found about SIMPLER benchmark VLA evaluation in 2026:

SIMPLER is one of the benchmarks being used to evaluate Vision-Language-Action models, alongside LIBERO and CALVIN. The search results indicate that SIMPLER (also referred to as SimplerEnv) is being incorporated into VLA evaluation frameworks.

The vla-eval framework supports 13 simulation benchmarks including SimplerEnv, and parallel evaluation via episode sharding and batch inference achieves a 47× throughput improvement, completing 2,000 LIBERO episodes in ~18 minutes.

Additionally, VLA models have delivered over 50% performance gains in SimplerEnv, demonstrating significant progress on this benchmark.

The vla-eval harness appears to be a major infrastructure development in 2026 for unified VLA evaluation across multiple benchmarks including SIMPLER, addressing challenges with inconsistent evaluation protocols and benchmark integration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba3ee5ca-b2fe-43f6-9ee4-11d91f3d1f62",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "54795df6-560e-4ae1-8e26-b1b12a1a4134",
  "sourceToolAssistantUUID": "ba3ee5ca-b2fe-43f6-9ee4-11d91f3d1f62",
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

_source line 19 · 2026-05-18T18:19:23.126Z_

<details><summary>↩ Tool result · `toolu_01BgxHdyTDbMxRGTFutv6URq`</summary>

```text
Web search results for query: "adapter module VLA fine-tuning efficient 2025 2026"

Links: [{"title":"[Quick Review] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action\\n Model","url":"https://liner.com/review/vlaadapter-effective-paradigm-for-tinyscale-visionlanguageaction-model"},{"title":"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/html/2605.06175v1"},{"title":"VLA-ADAPTER: AN EFFECTIVE PARADIGM FOR TINY-SCALE VISION-LANGUAGE-ACTION MODEL","url":"https://arxiv.org/pdf/2509.09372"},{"title":"Adapter-Based Fine-Tuning","url":"https://www.emergentmind.com/topics/adapter-based-fine-tuning"},{"title":"Adapter Modules for LLM Fine-tuning","url":"https://apxml.com/courses/fine-tuning-adapting-large-language-models/chapter-4-parameter-efficient-fine-tuning/adapter-modules"},{"title":"Towards Efficient Post-Training via Fourier-Driven Adapter Architectures","url":"https://arxiv.org/pdf/2512.22378"}]

Based on the search results, here's what I found about adapter modules for VLA (Vision-Language-Action) fine-tuning efficiency in 2025-2026:

## VLA-Adapter Paradigm

Current VLA models incur significant training costs due to reliance on large-scale Vision-Language Models (VLMs) and extensive pre-training, facing bottlenecks including high GPU memory consumption, slow fine-tuning speeds, and low inference efficiency, particularly in high-dimensional control environments.

VLA-Adapter facilitates efficient fine-tuning of VLMs without robotic pre-training, achieving performance that surpasses baselines using a tiny backbone. VLA-Adapter improvement is obvious when VLMs lack robotic pre-training, as relying solely on last-layer latents without pre-training is insufficient for effective action mapping, making VLA-Adapter crucial to achieve efficient fine-tuning.

## Parameter-Efficient Fine-Tuning (PEFT) in VLA

Since full fine-tuning methods are memory consuming, LoRA is explored in VLA fine-tuning works, with OpenVLA being among the earliest VLA works to adopt LoRA for lower training memory consumption.

Adapters introduce only a small number of new parameters, drastically reducing computational cost and storage needs compared to full fine-tuning, allowing a single base model to be adapted for many tasks by storing only small, task-specific adapter weights.

The research shows active development in 2025-2026 around making VLA models more efficient through adapter-based approaches and parameter-efficient fine-tuning methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab3a61e1-54d7-4dbd-af21-bb9640ab9c25",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "c86ae4f8-e317-4398-bb96-0a2d4bc26eb8",
  "sourceToolAssistantUUID": "ab3a61e1-54d7-4dbd-af21-bb9640ab9c25",
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

_source line 20 · 2026-05-18T18:19:24.594Z_

<details><summary>↩ Tool result · `toolu_01HhsKoQL1RLhtHJyKgxAd1m`</summary>

```text
Web search results for query: "DINO feature extraction affordance part segmentation 2025 2026"

Links: [{"title":"One-Shot Transfer of Affordance Regions? AffCorrs!","url":"https://arxiv.org/pdf/2209.07147"},{"title":"OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance","url":"https://arxiv.org/html/2604.08461v1"},{"title":"Upsampling DINOv2 Features for Unsupervised Vision Tasks and Weakly Supervised Materials Segmentation - Docherty - 2026 - Advanced Intelligent Systems - Wiley Online Library","url":"https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202501094"},{"title":"A Deep Learning Approach to Object Affordance Segmentation","url":"https://arxiv.org/pdf/2004.08644"},{"title":"Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models","url":"https://arxiv.org/pdf/2602.20501"}]

Based on the search results, I found several relevant papers on DINO feature extraction and affordance part segmentation:

## Key Findings

**One-Shot Affordance Part Segmentation (OSAPS):**
The pre-trained DINO-ViT model can be used for part querying and finding semantically corresponding parts in one-shot, addressing a novel formulation of One-Shot Affordance Part Segmentation (OSAPS). This work is one of the first to extend one-shot instance segmentation to part masks, and affordance parts in particular.

**DINO Feature Extraction for Segmentation:**
DINO exhibits strong object contour awareness as early as its initial layers, indicating that structural information is captured during the early stages of feature extraction. DINO, as a self-supervised visual backbone, exhibits strong fine-grained representation capability and maintains notable consistency with the CLIP text embedding space.

**Recent Developments (2025-2026):**
DINOv2 is noted as learning robust visual features without supervision, and there have been recent applications like OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with language guidance (published April 2026).

**Affordance Reasoning in Vision Foundation Models:**
Models best at affordance segmentation organize visual features into part-level structures, revealing object geometry as the foundation of actionable perception.

These papers demonstrate the growing interest in using DINO-based approaches for fine-grained affordance and part segmentation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "731d6436-748f-48cc-b6b3-c41866f4a96f",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "269ade43-64e5-4dd8-b681-01cca024cac5",
  "sourceToolAssistantUUID": "731d6436-748f-48cc-b6b3-c41866f4a96f",
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

_source line 21 · 2026-05-18T18:19:26.490Z_

<details><summary>↩ Tool result · `toolu_014WyutUdaGCZ831JQdCb7Ha`</summary>

```text
Web search results for query: "VLM internal representations affordance probing 2026"

Links: [{"title":"Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models","url":"https://arxiv.org/pdf/2602.20501"},{"title":"Reading Between the Lines: Abstaining from VLM-Generated OCR Errors via Latent Representation Probes","url":"https://arxiv.org/pdf/2511.19806"},{"title":"Context-Dependent Affordance Computation in Vision-Language Models","url":"https://arxiv.org/pdf/2603.04419"},{"title":"[Literature Review] Hidden in plain sight: VLMs overlook their visual representations","url":"https://www.themoonlight.io/en/review/hidden-in-plain-sight-vlms-overlook-their-visual-representations"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/pdf/2603.05465"},{"title":"Responses Fall Short of Understanding: Revealing the Gap between Internal Representations and Responses in Visual Document Understanding","url":"https://arxiv.org/pdf/2604.04411"}]

I found several relevant research papers on VLM internal representations and affordance probing from 2026 (and late 2025):

## Key Findings:

**Affordance Reasoning in Vision Foundation Models:**
Geometric and interaction perception are the fundamental building blocks of affordance understanding in VFMs, providing a mechanistic account of how perception grounds action. By simply fusing DINO's geometric prototypes with Flux's interaction maps in a training-free and zeroshot manner, researchers achieved affordance estimation competitive with weakly-supervised methods.

**Representation Probing Techniques:**
Representation probing is a diagnostic approach where lightweight classifiers or regressors are trained on internal model activations to assess the encoding of specific properties. Recent work has extended this to Vision Transformers, where intermediate layers encode rich class-specific and scene-level semantics.

**Probing Internal Representations:**
Multiple recent studies employ probing to analyze VLM internals. There is a clear gap between internal representations and generated responses, and information required to solve the task is often encoded more linearly from intermediate layers than from the final layer. Additionally, affordance-related tasks involve computing cosine similarity between patch features of reference points and candidate points.

These papers demonstrate active research into understanding how VLMs internally represent affordances through probing methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da11c248-73cb-4eb0-942b-a24df96c87b9",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "871b3ab3-4e2e-429f-bbff-0d5bdb2b013c",
  "sourceToolAssistantUUID": "da11c248-73cb-4eb0-942b-a24df96c87b9",
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

_source line 22 · 2026-05-18T18:19:27.315Z_

<details><summary>↩ Tool result · `toolu_0113EahY3FPm4sNtZRjNLbY5`</summary>

```text
Web search results for query: "LIBERO benchmark robot manipulation evaluation"

Links: [{"title":"LIBERO Benchmark: Lifelong Robot Learning","url":"https://www.emergentmind.com/topics/libero-benchmark"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"Libero-Object Benchmark","url":"https://www.emergentmind.com/topics/libero-object-benchmark"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"RoboEval: Where Robotic Manipulation Meets Structured and Scalable Evaluation","url":"https://arxiv.org/pdf/2507.00435"}]

Based on the search results, here's what I found about the LIBERO benchmark:

## Overview

LIBERO benchmark is a standardized platform for evaluating sequential knowledge transfer in robotic manipulation tasks across diverse settings. It is a standardized and extensible benchmarking suite for assessing multi-modal, vision-language-action (VLA) models in robot manipulation, with a particular emphasis on lifelong, multi-task, and knowledge-transfer learning across diverse and procedurally generated environments.

## Key Features

It employs a modular procedural generation pipeline, comprehensive evaluation protocols, and high-quality human demonstrations to assess both declarative and procedural knowledge. It employs a procedural generation pipeline and curated simulation/annotation infrastructure to create varied tasks that test generalization, robustness, and transfer capabilities.

## Task Organization

The LIBERO benchmark is a simulation-only (MuJoCo-based) scalable benchmark, currently with 130 language-conditioned manipulation tasks organized into 4 groups: Tasks with distribution shifts in object types (LIBERO-OBJECT), Tasks with distribution shifts in the spatial arrangement of objects (LIBERO-SPATIAL), Tasks with distribution shifts in the task goals (LIBERO-GOAL), and Tasks with a combination of the above three.

## Findings

Empirical findings show high success rates under clean conditions yet reveal model brittleness under perturbations, highlighting challenges in lifelong, compositional learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbb9c72c-9385-4abf-862a-434525c3a4dc",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "8fcd1530-656d-4f62-92e7-3957a806f843",
  "sourceToolAssistantUUID": "fbb9c72c-9385-4abf-862a-434525c3a4dc",
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

_source line 23 · 2026-05-18T18:19:31.247Z_

Let me search for a few more specific topics to fill in technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fcd1530-656d-4f62-92e7-3957a806f843",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAViLQjMpHUQQGwGtm1E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf0887b9-b11f-4d41-8e0f-b2787870cdcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B94jnhNN4eMvsQ7YCabtpd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6015,
      "cache_read_input_tokens": 9538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6015,
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

_source line 24 · 2026-05-18T18:19:31.894Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013YtHtF6bfhK5ue316ALnz8`</summary>

```json
{
  "query": "RT-Affordance intermediate representations VLA robot manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf0887b9-b11f-4d41-8e0f-b2787870cdcf",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAViLQjMpHUQQGwGtm1E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "389fb7cf-96fc-4f3b-9ac9-fdabfd45cb08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B94jnhNN4eMvsQ7YCabtpd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6015,
      "cache_read_input_tokens": 9538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6015,
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

_source line 25 · 2026-05-18T18:19:32.760Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PyqzChpNvcB5zCaGQukFiG`</summary>

```json
{
  "query": "DINOv2 layer features affordance estimation robot grasping specific layers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "389fb7cf-96fc-4f3b-9ac9-fdabfd45cb08",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAViLQjMpHUQQGwGtm1E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce4d2e9b-4523-4948-86d4-858ab0394a65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B94jnhNN4eMvsQ7YCabtpd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6015,
      "cache_read_input_tokens": 9538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6015,
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

_source line 26 · 2026-05-18T18:19:34.651Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K4rVpUYoJrngQsUG4QxR4e`</summary>

```json
{
  "query": "VLA-Adapter architecture details multi-layer feature extraction action prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce4d2e9b-4523-4948-86d4-858ab0394a65",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAViLQjMpHUQQGwGtm1E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac9a70e5-be54-4896-8ee6-1cd68cf3c09f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B94jnhNN4eMvsQ7YCabtpd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6015,
      "cache_read_input_tokens": 9538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6015,
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

_source line 27 · 2026-05-18T18:19:36.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019xAz43JqxXndMbJ1CBE1x8`</summary>

```json
{
  "query": "VLA-GSE generalized specialized experts parameter efficient fine-tuning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac9a70e5-be54-4896-8ee6-1cd68cf3c09f",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAViLQjMpHUQQGwGtm1E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ac53fa7-4315-4c28-9ddf-bea8024cc62f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B94jnhNN4eMvsQ7YCabtpd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6015,
      "cache_read_input_tokens": 9538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6015,
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

_source line 28 · 2026-05-18T18:19:37.185Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013jfqNTrVgAwzeFae4V9vMk`</summary>

```json
{
  "query": "OpenVLA LoRA fine-tuning architecture details vision encoder"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ac53fa7-4315-4c28-9ddf-bea8024cc62f",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAViLQjMpHUQQGwGtm1E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ff85906-b7c9-45dd-ad0e-b019740a6855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B94jnhNN4eMvsQ7YCabtpd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6015,
      "cache_read_input_tokens": 9538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6015,
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

_source line 29 · 2026-05-18T18:19:37.861Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FPorkM7oe1q9utA5tEnY9J`</summary>

```json
{
  "query": "CALVIN benchmark robot manipulation evaluation VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ff85906-b7c9-45dd-ad0e-b019740a6855",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAViLQjMpHUQQGwGtm1E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16e6e05d-9307-4014-9f63-e1f0061f86a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B94jnhNN4eMvsQ7YCabtpd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6015,
      "cache_read_input_tokens": 9538,
      "output_tokens": 331,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6015
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 331,
          "cache_read_input_tokens": 9538,
          "cache_creation_input_tokens": 6015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6015,
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

_source line 30 · 2026-05-18T18:19:40.497Z_

<details><summary>↩ Tool result · `toolu_01PyqzChpNvcB5zCaGQukFiG`</summary>

```text
Web search results for query: "DINOv2 layer features affordance estimation robot grasping specific layers"

Links: [{"title":"Learning Precise Affordances from Egocentric Videos for Robotic Manipulation","url":"https://arxiv.org/html/2408.10123v1"},{"title":"Kaixin Bai1, Lei Zhang1, Yiwen Liu1, Zhaopeng Chen1, and Jianwei ...","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/256652/preprint_pdf/8ad986002b4280e0e40d019b71802be3.pdf"},{"title":"Learning Precise Affordances from Egocentric Videos for Robotic Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Learning_Precise_Affordances_from_Egocentric_Videos_for_Robotic_Manipulation_ICCV_2025_paper.pdf"},{"title":"OptiGrasp: Optimized Grasp Pose Detection Using RGB Images for Warehouse Picking Robots","url":"https://arxiv.org/html/2409.19494"},{"title":"Aff-Grasp","url":"https://reagan1311.github.io/affgrasp/"},{"title":"Spatial RoboGrasp: Generalized Robotic Grasping Control Policy","url":"https://arxiv.org/html/2505.20814v1"},{"title":"Grasping affordance for use in a robot system","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11565429"}]

I've found relevant research on using DINOv2 layer features for affordance estimation in robot grasping. Here are the key findings:

## DINOv2 Architecture and Layer-Specific Features

DINOv2 transformer layers have layer-specific characteristics: those closer to the output capture task-specific high-level features, while those near the input focus on generic low-level features. This characteristic is important for affordance estimation tasks.

## Applications in Robot Grasping

Several recent systems leverage DINOv2 features for affordance-based robotic manipulation:

1. **Geometry-guided Affordance Transformer (GAT)**: This architecture includes a DINOv2 image encoder as a feature extractor, along with a novel Depth Feature Injector and LoRA layers for effective fine-tuning. The system uses DINOv2 as the visual foundation model image encoder, keeps it frozen, and employs Low-Rank Adaptation (LoRA) for fine-tuning to enhance generalization ability and prevent overfitting.

2. **OptiGrasp**: This grasp pose detection system integrates a pre-trained DINOv2 from the Depth Anything model using a ViT-base architecture. The network takes an RGB image and object mask as inputs and predicts dense prediction maps including affordance grasp scores, pitch angle, and yaw angle at each pixel.

The research indicates that leveraging specific DINOv2 layers—where deeper layers provide task-specific features and earlier layers provide generic low-level features—is effective for precise affordance estimation in robotic grasping tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce4d2e9b-4523-4948-86d4-858ab0394a65",
  "isSidechain": true,
  "promptId": "b2a6c99e-672f-4efc-a8d3-ec260de2c298",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "12f25ba4-5244-47a2-9d27-4a76180e8ffb",
  "sourceToolAssistantUUID": "ce4d2e9b-4523-4948-86d4-858ab0394a65",
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

_source line 31 · 2026-05-18T18:19:41.454Z_

<details><summary>↩ Tool result · `toolu_013YtHtF6bfhK5ue316ALnz8`</summary>

```text
Web search results for query: "RT-Affordance intermediate representations VLA robot manipulation 2024 2025"

Links: [{"title":"[Literature Review] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.themoonlight.io/en/review/rt-affordance-affordances-are-versatile-intermediate-representations-for-robot-manipulation"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.researchgate.net/publication/395222047_RT-Affordance_Affordances_are_Versatile_Intermediate_Representations_for_Robot_Manipulation"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"[2411.02704] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/abs/2411.02704"},{"title":"RT-Affordance: Reasoning about Robotic Manipulation with Affordances","url":"https://openreview.net/pdf?id=s8VMLXKH1X"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/html/2411.02704v1"}]

Based on the search results, here's what I found about RT-Affordance:

## Overview

RT-Affordance is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation.

## Problem It Addresses

Vision-language-action (VLA) models, pretrained with large-scale robot data, promise generalization to new objects, scenes, and tasks, but VLAs are not yet reliable enough to be deployed outside of narrow lab settings where they are trained. Existing representations such as language, goal images, and trajectory sketches have been shown to be helpful, but these representations either do not provide enough context or provide over-specified context that yields less robust policies.

## Key Approach

The proposed method employs a hierarchical model architecture that consists of two primary components: an affordance generator and an affordance-conditioned policy. The model can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories, and can be trained on cheap-to-collect in-domain affordance images, allowing learning of new tasks without collecting additional costly robot trajectories.

## Performance

RT-Affordance exceeds the performance of existing methods by over 50%, and affordances are shown to be robust to novel settings.

The paper was submitted to CoRL 2024 and made public in November 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "389fb7cf-96fc-4f3b-9ac9-fdabfd45cb08",
  "isSidechain": true,
  "promptId": "b2a6c99e-672f-4efc-a8d3-ec260de2c298",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "f7f363dd-4237-42d4-9a7e-a3cac66a31d8",
  "sourceToolAssistantUUID": "389fb7cf-96fc-4f3b-9ac9-fdabfd45cb08",
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

_source line 32 · 2026-05-18T18:19:42.487Z_

<details><summary>↩ Tool result · `toolu_01K4rVpUYoJrngQsUG4QxR4e`</summary>

```text
Web search results for query: "VLA-Adapter architecture details multi-layer feature extraction action prediction"

Links: [{"title":"VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/vla-adapter-effective-paradigm-tiny-scale-vision"},{"title":"VLA-ADAPTER: AN EFFECTIVE PARADIGM FOR TINY-SCALE VISION-LANGUAGE-ACTION MODEL","url":"https://arxiv.org/pdf/2509.09372"},{"title":"VLA-Adapter","url":"https://vla-adapter.github.io/"},{"title":"VLA-MP: A Vision-Language-Action Framework for Multimodal Perception and Physics-Constrained Action Generation in Autonomous Driving","url":"https://www.mdpi.com/1424-8220/25/19/6163"},{"title":"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.10698v1"},{"title":"VLA-MP: A Vision-Language-Action Framework for Multimodal Perception and Physics-Constrained Action Generation in Autonomous Driving - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12526522/"}]

Based on the search results, here are the key architecture details of VLA-Adapter:

## Architecture Overview

VLA-Adapter follows the Prismatic-VLMs architecture with M layers. The framework investigates how to effectively bridge vision-language representations to the action space.

## Multi-Layer Feature Extraction

A key finding is that multi-layer features consistently outperform single-layer approaches, improving performance while eliminating the need for manual layer selection during design. The architecture employs two types of features:

- Raw features (vision and language representations in VLM) and ActionQuery (additional learnable tokens)
- Middle-layer latent performs better than deep-layer latent, as deep-layer Raw features is biased towards semantic information and less effective in action generation.

## Bridge Attention Mechanism for Action Prediction

VLA-Adapter introduces Bridge Attention, a novel mechanism designed to optimally inject conditions into the action space. 

The mechanism works as follows:
- The Policy network uses an L1-based architecture where action latents undergo cross-attention with conditions and self-attention iteratively across layers.
- Bridge Attention consists of three attention components: two cross-attentions and one self-attention. The first cross-attention processes Raw features through an MLP to obtain key-value pairs, using action latent as queries.

## Final Output Processing

The attention outputs are concatenated to form the layer output, which passes through a residual feedforward network. This process repeats across layers, ultimately generating the action chunk through final LayerNorm and MLP layers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac9a70e5-be54-4896-8ee6-1cd68cf3c09f",
  "isSidechain": true,
  "promptId": "b2a6c99e-672f-4efc-a8d3-ec260de2c298",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "6e4009ff-cdfa-43f0-bfc6-2c32cf212bba",
  "sourceToolAssistantUUID": "ac9a70e5-be54-4896-8ee6-1cd68cf3c09f",
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

_source line 33 · 2026-05-18T18:19:42.709Z_

<details><summary>↩ Tool result · `toolu_019xAz43JqxXndMbJ1CBE1x8`</summary>

```text
Web search results for query: "VLA-GSE generalized specialized experts parameter efficient fine-tuning 2025"

Links: [{"title":"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/html/2605.06175v1"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/html/2603.16044v1"},{"title":"Let the Expert Stick to His Last: Expert-Specialized Fine-Tuning for   Sparse Architectural Large Language Models","url":"https://arxiv.org/pdf/2407.01906"},{"title":"MLAE: Masked LoRA Experts for Visual Parameter-Efficient Fine-Tuning","url":"https://arxiv.org/pdf/2405.18897"},{"title":"Learning to Route Among Specialized Experts for Zero-Shot Generalization","url":"https://arxiv.org/pdf/2402.05859"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"}]

Based on the search results, here's what I found about VLA-GSE:

## VLA-GSE: Generalized and Specialized Experts for Vision-Language-Action Models

VLA-GSE (Generalized and Specialized Experts) is initialized by spectrally decomposing the frozen backbone, assigning leading singular components to generalized experts (shared experts) and disjoint residual components to specialized experts (routed experts).

### Key Features and Performance

This decomposition improves adaptation capacity under a fixed trainable-parameter budget. VLA-GSE updates only 2.51% of full model parameters and consistently outperforms strong FFT and PEFT baselines.

### Problem It Addresses

Parameter-efficient fine-tuning (PEFT), such as low-rank adaptation (LoRA), is more stable in preserving pre-trained capability, yet existing PEFT approaches frequently under-adapt when precise control is required.

### Results

It achieves 81.2% average zero-shot success on LIBERO-Plus, preserves pre-trained VLM capability comparably to LoRA on multimodal understanding benchmarks, and improves real-world manipulation success under multiple distribution shifts.

Code is available at https://github.com/YuhuaJiang2002/VLA-GSE.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ac53fa7-4315-4c28-9ddf-bea8024cc62f",
  "isSidechain": true,
  "promptId": "b2a6c99e-672f-4efc-a8d3-ec260de2c298",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "3d051364-6538-4fe9-9b8a-9417ac3ba939",
  "sourceToolAssistantUUID": "0ac53fa7-4315-4c28-9ddf-bea8024cc62f",
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

_source line 34 · 2026-05-18T18:19:44.498Z_

<details><summary>↩ Tool result · `toolu_013jfqNTrVgAwzeFae4V9vMk`</summary>

```text
Web search results for query: "OpenVLA LoRA fine-tuning architecture details vision encoder"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/html/2603.16044v1"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"Fine-Tuning Vision-Language-Action Models | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/vision-language-action-finetuning-robotics"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"}]

Based on the search results, here's a comprehensive overview of OpenVLA's LoRA fine-tuning architecture and vision encoder details:

## Vision Encoder Architecture

OpenVLA's model consists of a fused visual encoder combining a SigLIP and a DinoV2 backbone that maps image inputs to image patch embeddings. The dual vision encoder extracts 256 patch embeddings per view, which are projected into the language embedding space with a shared projector network.

## Complete Model Architecture

The model includes three key elements: (1) a fused visual encoder (SigLIP and DinoV2), (2) a projector that maps visual encoder outputs into a language model's input space, and (3) a Llama 2 7B language model backbone that predicts tokenized output actions. These tokens are decoded into continuous output actions that can be directly executed on the robot.

## Input Processing Pipeline

All input embeddings—visual features, robot state, and language tokens—are concatenated along the sequence dimension before being passed to the decoder, enabling the model to attend to all available information when generating actions.

## LoRA Fine-Tuning Details

With LoRA (Low-Rank Adaptation), fine-tuning takes 10-15 hours on a single A100 GPU. OpenVLA was the first to demonstrate the effectiveness of compute-efficient fine-tuning methods leveraging low-rank adaptation and model quantization to facilitate adapting OpenVLA models on consumer-grade GPUs. The model was fine-tuned on nearly 1 million robot trajectories across 70+ domains using discrete action tokenization and efficient LoRA updates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ff85906-b7c9-45dd-ad0e-b019740a6855",
  "isSidechain": true,
  "promptId": "b2a6c99e-672f-4efc-a8d3-ec260de2c298",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "b84a7703-d66c-4815-86cd-8276dc193b8e",
  "sourceToolAssistantUUID": "8ff85906-b7c9-45dd-ad0e-b019740a6855",
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

_source line 35 · 2026-05-18T18:19:44.808Z_

<details><summary>↩ Tool result · `toolu_01FPorkM7oe1q9utA5tEnY9J`</summary>

```text
Web search results for query: "CALVIN benchmark robot manipulation evaluation VLA 2025 2026"

Links: [{"title":"LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"},{"title":"CALVIN Dataset: Language & Vision Robotics","url":"https://www.emergentmind.com/topics/calvin-dataset"},{"title":"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel7/7083369/9750005/09788026.pdf"},{"title":"CALVIN: A Benchmark for Language-Conditioned Policy Learning for   Long-Horizon Robot Manipulation Tasks","url":"https://arxiv.org/pdf/2112.03227"},{"title":"[2112.03227] CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks","url":"https://arxiv.org/abs/2112.03227"},{"title":"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks | Request PDF","url":"https://www.researchgate.net/publication/361082731_CALVIN_A_Benchmark_for_Language-Conditioned_Policy_Learning_for_Long-Horizon_Robot_Manipulation_Tasks"},{"title":"GitHub - mees/calvin: CALVIN - A benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks · GitHub","url":"https://github.com/mees/calvin"},{"title":"Robot Learning Benchmarks: CALVIN, LIBERO, RLBench, Google-Robot | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/benchmarks"},{"title":"Experiences from Benchmarking Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/pdf/2511.11298"}]

Based on the search results, here's what I found about the CALVIN benchmark for robot manipulation evaluation:

## CALVIN Benchmark Overview

CALVIN (Composing Actions from Language and Vision) is an open-source simulated benchmark to learn long-horizon language-conditioned tasks. It is designed to learn many long-horizon language-conditioned tasks over a range of four manipulation environments with diverse yet shared structure, from multimodal onboard sensor observations.

## VLA Evaluation Performance (2025-2026)

CALVIN was designed for long-horizon chains of skills in a shared tabletop environment, targeting language-conditioned manipulation. For Vision-Language-Action (VLA) models:

- Strong 2025 models reach roughly 3.5-4.0 on the easier A-to-A evaluation and drop to 2.0-3.0 on the zero-shot D evaluation, with anything above 4.0 on zero-shot D considered state-of-the-art as of early 2026.

## Key Characteristics

CALVIN tasks are more complex in terms of sequence length, action space, and language than existing vision-and-language task datasets and supports flexible specification of sensor suites. In the most difficult evaluation, methods must generalize to unseen entities by training on a large interaction corpora covering many rooms and testing on an unseen environment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16e6e05d-9307-4014-9f63-e1f0061f86a3",
  "isSidechain": true,
  "promptId": "b2a6c99e-672f-4efc-a8d3-ec260de2c298",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "9934c4af-30cc-4d7f-b164-4018f0740499",
  "sourceToolAssistantUUID": "16e6e05d-9307-4014-9f63-e1f0061f86a3",
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

_source line 36 · 2026-05-18T18:19:49.620Z_

Let me gather a few more technical details on specific architectural components.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9934c4af-30cc-4d7f-b164-4018f0740499",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVjdF3Cj1zLE2reTwoG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fada625-0994-492f-96a0-313a623269cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JL2tZqb5G7ic3GRxzjiAMr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4903,
      "cache_read_input_tokens": 15553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4903,
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

_source line 37 · 2026-05-18T18:19:50.529Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EoiwWm6KsjxYnbKcM8CsN8`</summary>

```json
{
  "query": "DINO ViT intermediate layer features cosine similarity affordance correspondence part segmentation technique"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fada625-0994-492f-96a0-313a623269cc",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVjdF3Cj1zLE2reTwoG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "995efac5-5d90-4a8c-9125-84735a59bb41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JL2tZqb5G7ic3GRxzjiAMr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4903,
      "cache_read_input_tokens": 15553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4903,
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

_source line 38 · 2026-05-18T18:19:51.480Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LfRhd2BzcwSYBAiB1C4mzB`</summary>

```json
{
  "query": "probing geometry interaction affordance vision foundation models DINO Flux fusing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "995efac5-5d90-4a8c-9125-84735a59bb41",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVjdF3Cj1zLE2reTwoG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ebacb47-1f4b-4b27-8d35-3f78e6c58008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JL2tZqb5G7ic3GRxzjiAMr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4903,
      "cache_read_input_tokens": 15553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4903,
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

_source line 39 · 2026-05-18T18:19:52.323Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GNesAKXvXxdo61APSY4c8m`</summary>

```json
{
  "query": "context-dependent affordance computation vision language models 2026 architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ebacb47-1f4b-4b27-8d35-3f78e6c58008",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVjdF3Cj1zLE2reTwoG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "410cb8e7-1d0e-43a9-8138-5d8cd8d8dc19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JL2tZqb5G7ic3GRxzjiAMr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4903,
      "cache_read_input_tokens": 15553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4903,
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

_source line 40 · 2026-05-18T18:19:52.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N2MCePPWBq6G24t7KfPFPM`</summary>

```json
{
  "query": "affordance map flow matching robot manipulation policy architecture 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "410cb8e7-1d0e-43a9-8138-5d8cd8d8dc19",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVjdF3Cj1zLE2reTwoG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d8c3885-bca1-4c63-8438-16751fb14014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JL2tZqb5G7ic3GRxzjiAMr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4903,
      "cache_read_input_tokens": 15553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4903,
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

_source line 41 · 2026-05-18T18:19:56.796Z_

<details><summary>↩ Tool result · `toolu_01EoiwWm6KsjxYnbKcM8CsN8`</summary>

```text
Web search results for query: "DINO ViT intermediate layer features cosine similarity affordance correspondence part segmentation technique"

Links: [{"title":"dino-vit-features/correspondences.py at main · ShirAmir/dino-vit-features","url":"https://github.com/ShirAmir/dino-vit-features/blob/main/correspondences.py"},{"title":"dino-vit-features/inspect_similarity.py at main · ShirAmir/dino-vit-features","url":"https://github.com/ShirAmir/dino-vit-features/blob/main/inspect_similarity.py"},{"title":"dino-vit-features/cosegmentation.py at main · ShirAmir/dino-vit-features","url":"https://github.com/ShirAmir/dino-vit-features/blob/main/cosegmentation.py"},{"title":"Deep ViT Features as Dense Visual Descriptors","url":"https://dino-vit-features.github.io/paper.pdf"},{"title":"Understanding contrastive versus reconstructive ...","url":"https://sslneurips22.github.io/paper_pdfs/paper_50.pdf"},{"title":"DINO-based Perceptual Loss Overview","url":"https://www.emergentmind.com/topics/dino-based-perceptual-loss"},{"title":"Finding Distributed Object-Centric Properties in Self-Supervised Transformers","url":"https://arxiv.org/pdf/2603.26127"},{"title":"GitHub - facebookresearch/dinov3: Reference PyTorch implementation and models for DINOv3 · GitHub","url":"https://github.com/facebookresearch/dinov3"},{"title":"One-Shot Transfer of Affordance Regions? AffCorrs!","url":"https://arxiv.org/pdf/2209.07147"}]

Based on the search results, I found relevant information about DINO ViT intermediate layer features and their application to correspondence and affordance tasks. Here's what the research shows:

## DINO ViT Intermediate Features

Intermediate ViT features contain both positional and semantic information, which makes them particularly useful for various computer vision tasks. Research demonstrates the use of intermediate features (compared to features from the last layer) and different facets of DINO-ViT as features including tokens, queries, values and keys.

## Cosine Similarity and Correspondence

The keys facet has cleaner similarity maps compared to other facets. The technique uses cosine similarity to measure correspondence between patches, with cosine similarity maps obtained between patches marked with a reference point and all other patches.

## Affordance and Part Correspondence

The pre-trained DINO-ViT model can be used for part querying and finding semantically corresponding parts in one-shot. Affordances are representations of how a part of the environment can be used, and part-based affordance representations can be efficiently used as an intermediate representation that reduces the dimensionality of many robot learning problems.

Additionally, numerous object-centric heads exist in intermediate layers (Layers 8-10), containing valuable information, demonstrating that object discovery is not confined to the final layer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "995efac5-5d90-4a8c-9125-84735a59bb41",
  "isSidechain": true,
  "promptId": "b2a6c99e-672f-4efc-a8d3-ec260de2c298",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "a4e11a26-65c2-4574-8dbc-8b35b5ce74ae",
  "sourceToolAssistantUUID": "995efac5-5d90-4a8c-9125-84735a59bb41",
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

_source line 42 · 2026-05-18T18:19:58.191Z_

<details><summary>↩ Tool result · `toolu_01LfRhd2BzcwSYBAiB1C4mzB`</summary>

```text
Web search results for query: "probing geometry interaction affordance vision foundation models DINO Flux fusing 2026"

Links: [{"title":"[2602.20501] Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models","url":"https://arxiv.org/abs/2602.20501"},{"title":"Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models","url":"https://arxiv.org/pdf/2602.20501"},{"title":"Probing and Bridging Geometry–Interaction Cues for Affordance Reasoning in Vision Foundation Models","url":"https://arxiv.org/html/2602.20501"},{"title":"Demo2Vec: Reasoning Object Affordances from Online Videos | Request PDF","url":"https://www.researchgate.net/publication/329741279_Demo2Vec_Reasoning_Object_Affordances_from_Online_Videos"},{"title":"Reasoning Mamba: Hypergraph-Guided Region Relation Calculating for Weakly Supervised Affordance Grounding | Request PDF","url":"https://www.researchgate.net/publication/394663626_Reasoning_Mamba_Hypergraph-Guided_Region_Relation_Calculating_for_Weakly_Supervised_Affordance_Grounding"}]

Based on the search results, I found a research paper that directly matches your query:

## Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models

The research conducts a systematic probing of Visual Foundation Models (VFMs), finding that models like DINO inherently encode part-level geometric structures, while generative models like Flux contain rich, verb-conditioned spatial attention maps that serve as implicit interaction priors.

The work argues that understanding affordance hinges on two complementary capacities: geometric perception, which identifies the structural parts of objects that enable interaction, and interaction perception, which models how an agent's actions engage with those parts.

By simply fusing DINO's geometric prototypes with Flux's interaction maps in a training-free and zero-shot manner, the researchers achieve affordance estimation competitive with weakly-supervised methods.

The paper was published on arXiv in February-March 2026 and is authored by Qing Zhang, Xuesong Li, and Jing Zhang from the Australian National University and CSIRO. The fusion experiment confirms that geometric and interaction perception are the fundamental building blocks of affordance understanding in VFMs, providing a mechanistic account of how perception grounds action.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ebacb47-1f4b-4b27-8d35-3f78e6c58008",
  "isSidechain": true,
  "promptId": "b2a6c99e-672f-4efc-a8d3-ec260de2c298",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "8b04e08f-2119-47a7-b19b-f106f62320db",
  "sourceToolAssistantUUID": "4ebacb47-1f4b-4b27-8d35-3f78e6c58008",
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

_source line 43 · 2026-05-18T18:19:59.858Z_

<details><summary>↩ Tool result · `toolu_01N2MCePPWBq6G24t7KfPFPM`</summary>

```text
Web search results for query: "affordance map flow matching robot manipulation policy architecture 2024 2025"

Links: [{"title":"[2409.01083] Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/abs/2409.01083"},{"title":"Affordance-based Robot Manipulation with Flow Matching | alphaXiv","url":"https://www.alphaxiv.org/overview/2409.01083v5"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/pdf/2409.01083"},{"title":"Affordance-based Robot Manipulation with Flow Matching | Request PDF","url":"https://www.researchgate.net/publication/383702331_Affordance-based_Robot_Manipulation_with_Flow_Matching"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/html/2409.01083v4"},{"title":"Paper page - Affordance-based Robot Manipulation with Flow Matching","url":"https://huggingface.co/papers/2409.01083"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://hri-eu.github.io/flow-matching-policy/"}]

I found relevant research on this topic! Here are the search results:

## Key Research: Affordance-based Robot Manipulation with Flow Matching

A framework for assistive robot manipulation addresses two fundamental challenges: efficiently adapting large-scale models to downstream scene affordance understanding tasks, especially in daily living scenarios, and effectively learning robot trajectories by grounding the visual affordance model.

**Architecture Overview:**

The first component employs a parameter-efficient prompt tuning method that prepends learnable text prompts to the frozen vision model to predict manipulation affordances in multi-task scenarios. The proposed framework processes natural language instructions through a frozen pretrained vision model with learnable prompts to generate affordance maps, which then guide a flow matching policy to transform random waypoints into goal trajectories for robot execution.

**Flow Matching Policy:**

Flow matching represents a robot visuomotor policy as a conditional process of flowing random waypoints to desired robot trajectories. Flow matching exhibits more stable training and evaluation, and noticeably faster inference, while maintaining comparable generalization performance to diffusion policy.

**Performance:**

The method achieves an 85% reduction in inference time compared to diffusion models while maintaining trajectory prediction accuracy across diverse robotic tasks and demonstrating robust performance in real-world Activities of Daily Living. The framework was evaluated on a real-world dataset with 10 tasks across Activities of Daily Living.

The paper (arXiv:2409.01083) was authored by Fan Zhang and Michael Gienger from Honda Research Institute EU and was first submitted in September 2024, with updates through February 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d8c3885-bca1-4c63-8438-16751fb14014",
  "isSidechain": true,
  "promptId": "b2a6c99e-672f-4efc-a8d3-ec260de2c298",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "f51c7c13-1660-4ac8-bcf1-ecba8f42d45e",
  "sourceToolAssistantUUID": "3d8c3885-bca1-4c63-8438-16751fb14014",
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

_source line 44 · 2026-05-18T18:20:00.591Z_

<details><summary>↩ Tool result · `toolu_01GNesAKXvXxdo61APSY4c8m`</summary>

```text
Web search results for query: "context-dependent affordance computation vision language models 2026 architecture"

Links: [{"title":"Acknowledgements","url":"https://arxiv.org/html/2603.04419"},{"title":"Context-Dependent Affordance Computation in Vision-Language Models","url":"https://arxiv.org/pdf/2603.04419"},{"title":"GitHub - studiofarzulla/semantic-vision: Context-Dependent Affordance Computation in Vision-Language Models (DP-2505) · GitHub","url":"https://github.com/studiofarzulla/semantic-vision"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"}]

Based on the search results, I found a highly relevant 2026 research paper on this exact topic:

## Context-Dependent Affordance Computation in Vision-Language Models

A research paper from January 2026 by Murad Farzulla characterizes the phenomenon of context-dependent affordance computation in vision-language models (VLMs).

### Key Findings

Through a large-scale computational study of 3,213 scene-context pairs from COCO-2017 using Qwen-VL 30B and LLaVA-1.5-13B with systematic context priming across 7 agentic personas, the research demonstrates massive affordance drift, with mean Jaccard similarity between context conditions of 0.095, indicating that over 90% of lexical scene description is context-dependent.

Sentence-level cosine similarity confirms substantial drift at the semantic level (mean = 0.415, 58.5% context-dependent).

### Architectural Implications

The research reframes a classical perceptual limitation as an architectural feature: efficient spatial cognition requires not representing everything, but dynamically projecting the environment onto task-relevant affordance dimensions. The results suggest that the 90% context-dependent signal could be computed first, with geometric features emerging as the residual context-invariant component.

### Proposed Direction

The findings suggest a direction for robotics research: dynamic, query-dependent ontological projection (JIT Ontology) rather than static world modeling.

The paper is available on arXiv (2603.04419) and includes code on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "410cb8e7-1d0e-43a9-8138-5d8cd8d8dc19",
  "isSidechain": true,
  "promptId": "b2a6c99e-672f-4efc-a8d3-ec260de2c298",
  "agentId": "a464db43d225e4e3c",
  "type": "user",
  "uuid": "b379dc82-1527-44d1-b39f-c0bf21e8f142",
  "sourceToolAssistantUUID": "410cb8e7-1d0e-43a9-8138-5d8cd8d8dc19",
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

_source line 45 · 2026-05-18T18:21:27.674Z_

Here is a comprehensive technical report covering the building blocks you need for your research on activating implicit affordance knowledge in VLMs for VLA robot manipulation.

---

## 1. How DINO Features Have Been Used for Affordance Estimation

**Layer-Specific Properties:**
- DINOv2 transformer layers have distinct roles: layers closer to the output capture task-specific high-level (semantic) features, while layers near the input focus on generic low-level (geometric/spatial) features.
- Intermediate layers (particularly layers 8-10 in standard ViT architectures) contain rich object-centric information -- object discovery is not confined to the final layer.
- The **keys facet** of DINO-ViT attention produces the cleanest similarity maps compared to queries, values, and tokens. Cosine similarity between patch-level key features is the standard technique for computing correspondence between reference affordance points and candidate points.

**Specific Techniques:**
- **AffCorrs (One-Shot Affordance Part Segmentation):** Uses frozen DINO-ViT features for one-shot part querying -- given a single reference image with annotated affordance regions, it finds semantically corresponding parts on novel objects by computing cosine similarity between patch features. This was one of the first to extend one-shot instance segmentation to part-level affordance masks.
- **Geometry-guided Affordance Transformer (GAT):** Uses DINOv2 as a frozen image encoder with LoRA layers for fine-tuning. It includes a Depth Feature Injector module and cross-attention layers with residual connections to learn affordances combining shape and geometric priors.
- **Probing and Bridging (Zhang et al., Feb 2026, ANU/CSIRO):** A landmark 2026 paper that systematically probes VFMs and finds that DINO inherently encodes **part-level geometric structures** (geometric prototypes), while generative models like Flux contain **verb-conditioned spatial attention maps** serving as implicit interaction priors. By simply fusing DINO's geometric prototypes with Flux's interaction maps in a **training-free, zero-shot** manner, they achieve affordance estimation competitive with weakly-supervised methods. This confirms that geometric perception (from DINO) and interaction perception (from generative models) are the two fundamental building blocks of affordance understanding.
- **OptiGrasp:** Uses DINOv2 with ViT-base architecture from Depth Anything, taking RGB image + object mask and predicting dense affordance grasp scores, pitch angle, and yaw angle per pixel.

---

## 2. Attention Mechanisms for Injecting Affordance Info into Policies

**Cross-Attention-Based Approaches:**

- **VLA-Adapter Bridge Attention:** The most architecturally detailed mechanism found. It introduces a three-component attention block per layer: (1) cross-attention where action latent queries attend to Raw features (vision + language representations) processed through an MLP to get key-value pairs; (2) a second cross-attention component; (3) self-attention over action latents. Outputs are concatenated, passed through a residual feedforward network, and repeated across layers to generate action chunks. Crucially, **middle-layer latents outperform deep-layer latents** for action generation, because deep-layer features are biased toward semantic information and less effective for precise control.

- **RT-Affordance Hierarchical Architecture:** Uses a two-stage design -- an **affordance generator** first proposes an affordance plan (image-based) given language, then an **affordance-conditioned policy** conditions on this plan to execute manipulation. This decoupled approach exceeds existing methods by over 50% and bridges heterogeneous supervision (web datasets + robot trajectories).

- **Affordance-based Flow Matching:** Prepends **learnable text-conditioned prompts** to a frozen vision foundation model to predict manipulation affordance maps. These maps then condition a flow matching policy that transforms random waypoints into desired robot trajectories. The flow matching policy achieves 85% reduction in inference time compared to diffusion models.

- **Hierarchical Modularity (Stengel-Eskin et al.):** Uses supervised attention across multiple sub-modules to bridge modular and end-to-end learning. Language conditioning is injected via attention to enable transfer across 4 different robot embodiments.

- **Spatial-Language Attention Policies (SLAP):** Uses 3D tokens as input representation, with language-conditioned attention for multi-task action prediction.

- **AFFORD2ACT:** Three-stage pipeline with affordance filtering, category-level keypoint construction, and a transformer-based policy with **embedded gating** to reason about task-relevant keypoints.

---

## 3. Evaluation Benchmarks for VLA Models

**LIBERO (Simulation - MuJoCo):**
- 130 language-conditioned manipulation tasks in 4 groups: LIBERO-OBJECT (object type shifts), LIBERO-SPATIAL (spatial arrangement shifts), LIBERO-GOAL (task goal shifts), and LIBERO-LONG (combinations).
- Tests lifelong, multi-task, and knowledge-transfer learning. Uses procedural generation pipeline with high-quality human demonstrations.
- LIBERO-PRO extends it for more robust/fair evaluation. LIBERO-Plus is used for zero-shot evaluation.
- Standard for evaluating VLA generalization and compositional learning.

**SIMPLER / SimplerEnv (Simulation):**
- Used for evaluating VLA models; strong 2025-era models showed over 50% performance gains on this benchmark.
- Integrated into unified evaluation frameworks like vla-eval.

**CALVIN (Simulation):**
- Focuses on **long-horizon language-conditioned manipulation** -- chains of skills in a shared tabletop environment.
- State-of-the-art performance (early 2026): ~3.5-4.0 on A-to-A evaluation; 2.0-3.0 on zero-shot D evaluation; anything above 4.0 on zero-shot D is SOTA.
- Tests generalization to unseen environments and entities.

**vla-eval (Unified Harness, 2026):**
- Supports 13 simulation benchmarks including SimplerEnv, LIBERO, and CALVIN.
- Parallel evaluation via episode sharding and batch inference achieves 47x throughput improvement (2,000 LIBERO episodes in ~18 minutes).
- Addresses the critical problem of inconsistent evaluation protocols across the field.

**VLA-Arena and VLABench:**
- Additional benchmarks for systematic VLA evaluation emerging in 2025-2026.

**Real-World Evaluation:**
- RT-Affordance was validated in real-world settings. The LoRA-based VLA fine-tuning work demonstrated 74-76% success rate on an SO101 robotic arm for button-pressing with only 200 demonstrations.

---

## 4. Efficient Fine-Tuning Approaches for VLA Models

**LoRA (Low-Rank Adaptation):**
- **OpenVLA** was the first major VLA to adopt LoRA, demonstrating effective fine-tuning of its 7B parameter model (Llama 2 backbone + SigLIP + DINOv2 dual vision encoder) on a single A100 GPU in 10-15 hours.
- With quantization (QLoRA), 3.1B parameter VLA models can run on **consumer-grade 8GB VRAM GPUs** at 20Hz control frequency.
- Key design choice: whether to freeze or unfreeze the vision encoder during LoRA fine-tuning significantly affects performance, especially with limited demonstration data.

**VLA-Adapter:**
- Achieves efficient fine-tuning **without robotic pre-training** using Bridge Attention to connect VLM representations to action space.
- Multi-layer feature extraction (from middle layers, not just final layer) consistently outperforms single-layer approaches, eliminating the need for manual layer selection.
- Designed for "tiny-scale" VLMs, making it practical for resource-constrained settings.

**VLA-GSE (Generalized and Specialized Experts, May 2025):**
- Initializes experts by **spectrally decomposing the frozen backbone**: leading singular components become shared/generalized experts, disjoint residual components become routed/specialized experts.
- Updates only **2.51% of full model parameters** while consistently outperforming both full fine-tuning and standard PEFT baselines.
- Achieves 81.2% average zero-shot success on LIBERO-Plus while preserving pre-trained VLM capability comparably to LoRA.
- Code: https://github.com/YuhuaJiang2002/VLA-GSE

**Prompt Tuning for Affordance:**
- Learnable text-conditioned prompts prepended to frozen vision foundation models (as in the flow matching work) offer a lightweight way to adapt models for affordance prediction without modifying backbone weights.

---

## 5. Extracting and Using Intermediate VLM Features for Affordance

**OpenVLA's Dual Encoder as a Blueprint:**
OpenVLA's architecture is directly relevant -- it fuses **SigLIP** (semantic/language-aligned features) and **DINOv2** (geometric/spatial features) through a shared projector into the language model's embedding space. All embeddings (visual, robot state, language) are concatenated along the sequence dimension before the Llama 2 decoder attends to them jointly. This dual-encoder design already separates the two types of information your approach would need: semantic affordance knowledge (SigLIP/CLIP-aligned) and geometric structure (DINOv2).

**Middle-Layer Extraction is Critical:**
VLA-Adapter's key finding is that **middle-layer features outperform final-layer features** for action generation. Deep-layer features are biased toward high-level semantics and lose the spatial precision needed for manipulation. The recommendation is to use multi-layer feature extraction (aggregating across layers) rather than relying on any single layer.

**Context-Dependent Affordance Computation (Farzulla, Jan 2026):**
A study of 3,213 scene-context pairs using Qwen-VL 30B and LLaVA-1.5-13B found that **over 90% of VLM scene description is context-dependent** (mean Jaccard similarity between context conditions = 0.095). This means VLM internal representations are already performing massive affordance-like filtering -- dynamically projecting scenes onto task-relevant dimensions depending on the language prompt. The implication for your work: VLM intermediate features are not static scene descriptions but are already affordance-conditioned by the language input.

**Probing Methodology:**
- Train lightweight classifiers/regressors on internal model activations to assess encoding of specific properties (linear probing).
- Information required for affordance tasks is often encoded **more linearly in intermediate layers** than in the final layer.
- Cosine similarity between patch features at reference affordance points and candidate points is the standard technique for computing affordance correspondence.

**Practical Architecture Suggestions from the Literature:**
1. Extract patch-level features from multiple intermediate layers of the VLM's vision encoder (especially DINO-family components).
2. Use cross-attention (as in VLA-Adapter's Bridge Attention) to let action queries attend to these multi-layer features.
3. Consider a hierarchical approach (as in RT-Affordance) where affordance maps are generated first, then used to condition the policy.
4. The DINO geometric prototypes + interaction maps fusion approach (training-free, zero-shot) from the 2026 ANU/CSIRO paper provides a baseline for what is extractable without any fine-tuning.

---

Sources:
- [Affordance-based Robot Manipulation with Flow Matching](https://arxiv.org/html/2409.01083v4)
- [Learning Precise Affordances from Egocentric Videos for Robotic Manipulation](https://arxiv.org/html/2408.10123v2)
- [RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation](https://arxiv.org/abs/2411.02704)
- [AFFORD2ACT: Affordance-Guided Automatic Keypoint Selection](https://arxiv.org/pdf/2510.01433)
- [CroSTAta: Cross-State Transition Attention Transformer](https://arxiv.org/html/2510.00726v1)
- [One-Shot Transfer of Affordance Regions? AffCorrs!](https://arxiv.org/pdf/2209.07147)
- [Upsampling DINOv2 Features for Unsupervised Vision Tasks (2026)](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202501094)
- [Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models](https://arxiv.org/abs/2602.20501)
- [Modularity through Attention: Efficient Training and Transfer of Language-Conditioned Policies](https://arxiv.org/abs/2212.04573)
- [Spatial-Language Attention Policies for Efficient Robot Learning](https://arxiv.org/pdf/2304.11235)
- [Context-Dependent Affordance Computation in Vision-Language Models](https://arxiv.org/pdf/2603.04419)
- [VLA-Adapter: An Effective Paradigm for Tiny-Scale VLA Model](https://arxiv.org/pdf/2509.09372)
- [VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA](https://arxiv.org/html/2605.06175v1)
- [Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models](https://arxiv.org/abs/2512.11921)
- [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/pdf/2406.09246)
- [vla-eval: A Unified Evaluation Harness for VLA Models](https://arxiv.org/abs/2603.13966)
- [LIBERO Benchmark](https://www.emergentmind.com/topics/libero-benchmark)
- [LIBERO-PRO: Towards Robust and Fair Evaluation](https://arxiv.org/pdf/2510.03827)
- [CALVIN Benchmark](https://arxiv.org/abs/2112.03227)
- [State of VLA Research at ICLR 2026](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
- [Deep ViT Features as Dense Visual Descriptors (dino-vit-features)](https://dino-vit-features.github.io/paper.pdf)
- [VLA-Arena Benchmark](https://github.com/PKU-Alignment/VLA-Arena)
- [Fine-Tuning VLA Models: Optimizing Speed and Success](https://arxiv.org/html/2502.19645v1)
- [GitHub: dino-vit-features correspondences](https://github.com/ShirAmir/dino-vit-features)
- [GitHub: VLA-GSE](https://github.com/YuhuaJiang2002/VLA-GSE)
- [GitHub: semantic-vision (Context-Dependent Affordance)](https://github.com/studiofarzulla/semantic-vision)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b379dc82-1527-44d1-b39f-c0bf21e8f142",
  "isSidechain": true,
  "agentId": "a464db43d225e4e3c",
  "requestId": "req_011CbAVknkZWHRjn9T3kbhyv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adfe4073-a53d-4aab-91d2-57c75d399cb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtFwDdTP9Wd2ZQw19hYsB7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 703,
      "cache_creation_input_tokens": 2416,
      "cache_read_input_tokens": 20456,
      "output_tokens": 3701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2416
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 703,
          "output_tokens": 3701,
          "cache_read_input_tokens": 20456,
          "cache_creation_input_tokens": 2416,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2416,
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
