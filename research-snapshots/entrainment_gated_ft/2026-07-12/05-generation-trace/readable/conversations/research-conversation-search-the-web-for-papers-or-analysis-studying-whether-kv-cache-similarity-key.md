# Research conversation: Search the web for papers or analysis studying whether KV cache similarity (key-value vector similarity between tokens) 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa1543551dfcb7eca.jsonl`
- **Structured JSON:** [`af884ae7386704bbf96d.json`](../../sessions/af/af884ae7386704bbf96d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-10T18:21:27.475Z_

Search the web for papers or analysis studying whether KV cache similarity (key-value vector similarity between tokens) correlates with MLP activation sparsity or activation magnitude patterns in LLMs. I want to know if there's any evidence that tokens with similar keys also have more compressible/sparse MLP activations.

Search queries:
1. "KV similarity activation sparsity correlation LLM"
2. "token redundancy MLP computation skip LLM inference"
3. "key vector similarity predict activation magnitude transformer"
4. "redundant token MLP sparsity reasoning LLM"
5. "token importance MLP attention correlation transformer inference"

Also search for papers on KV cache "insertion filtering" — methods that decide whether to add a token to the KV cache at the time of generation (as opposed to periodic eviction of cached entries):
6. "KV cache insertion filtering LLM inference"
7. "selective KV cache storage token generation"
8. "token importance recurrence KV eviction reasoning"

Report what you find. This is important for assessing whether a KV-similarity-based signal can validly drive MLP sparsity decisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "f8b003e1-e68e-43e8-8a25-27fcd82ad168",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:21:27.479Z_

```json
{
  "parentUuid": "f8b003e1-e68e-43e8-8a25-27fcd82ad168",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
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
  "uuid": "fd7b0bb4-6990-44b5-96e9-87651b6efe57",
  "timestamp": "2026-05-10T18:21:27.479Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:21:29.673Z_



I'll search the web for all these queries in parallel. Let me first load the WebSearch tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd7b0bb4-6990-44b5-96e9-87651b6efe57",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMPsMoksC6o1zbQBc9L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bff2de3-6620-4eb1-a4fd-7874ff324fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yM16pxUKDpRr8NB7SoQHz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 808,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T18:21:30.084Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BTYo6zVSNAe2pHwf46XCwB`</summary>

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
  "parentUuid": "2bff2de3-6620-4eb1-a4fd-7874ff324fad",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMPsMoksC6o1zbQBc9L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c29d5716-159e-4283-b116-9528e610a545",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yM16pxUKDpRr8NB7SoQHz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 8223,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 808
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 808,
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

_source line 5 · 2026-05-10T18:21:30.087Z_

<details><summary>↩ Tool result · `toolu_01BTYo6zVSNAe2pHwf46XCwB`</summary>

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
  "parentUuid": "c29d5716-159e-4283-b116-9528e610a545",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "1db0715b-81b7-42e5-bf08-543eaf8197f0",
  "sourceToolAssistantUUID": "c29d5716-159e-4283-b116-9528e610a545",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:21:32.518Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1db0715b-81b7-42e5-bf08-543eaf8197f0",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMQ4iRrviB7uKH7GTZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b50e0b55-870e-4824-bb46-1253a2ac8806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdGWeZ1L5zKMSxYxqyV7j4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 7 · 2026-05-10T18:21:32.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W1Nm8PbQRyaZCRkKi5nqGo`</summary>

```json
{
  "query": "KV similarity activation sparsity correlation LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b50e0b55-870e-4824-bb46-1253a2ac8806",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMQ4iRrviB7uKH7GTZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdfa2fcd-65b5-49a7-9a7b-ad1e1a1b2b00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdGWeZ1L5zKMSxYxqyV7j4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 8 · 2026-05-10T18:21:33.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LBufifya4kduky8iQjTJWH`</summary>

```json
{
  "query": "token redundancy MLP computation skip LLM inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdfa2fcd-65b5-49a7-9a7b-ad1e1a1b2b00",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMQ4iRrviB7uKH7GTZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96ef48d7-5f75-4cb1-8ee0-750513f8e437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdGWeZ1L5zKMSxYxqyV7j4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 9 · 2026-05-10T18:21:34.414Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BdQ3QT82UN1wnEct94DDCL`</summary>

```json
{
  "query": "key vector similarity predict activation magnitude transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96ef48d7-5f75-4cb1-8ee0-750513f8e437",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMQ4iRrviB7uKH7GTZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "977a54bc-f305-46f5-a4d8-a94d2af906e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdGWeZ1L5zKMSxYxqyV7j4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 10 · 2026-05-10T18:21:34.892Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q24p2XW8LwEvg2qtj1KHP9`</summary>

```json
{
  "query": "redundant token MLP sparsity reasoning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "977a54bc-f305-46f5-a4d8-a94d2af906e3",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMQ4iRrviB7uKH7GTZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cc73cb3-e1f6-4632-8741-e0a060e5d9ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdGWeZ1L5zKMSxYxqyV7j4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 11 · 2026-05-10T18:21:35.833Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014WBTKLC37jYkzoLsJnHkoQ`</summary>

```json
{
  "query": "token importance MLP attention correlation transformer inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc73cb3-e1f6-4632-8741-e0a060e5d9ce",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMQ4iRrviB7uKH7GTZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4e7a642-4a9e-4b1c-800e-a3582f2d75d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdGWeZ1L5zKMSxYxqyV7j4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 12 · 2026-05-10T18:21:36.300Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PNVfL2WezihidmKEGNu1Uy`</summary>

```json
{
  "query": "KV cache insertion filtering LLM inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4e7a642-4a9e-4b1c-800e-a3582f2d75d9",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMQ4iRrviB7uKH7GTZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad6cdca6-c045-48e5-a726-2ff82794c337",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdGWeZ1L5zKMSxYxqyV7j4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 13 · 2026-05-10T18:21:36.913Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Mcwp2CBNtTRF6eRz6zXLZ`</summary>

```json
{
  "query": "selective KV cache storage token generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad6cdca6-c045-48e5-a726-2ff82794c337",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMQ4iRrviB7uKH7GTZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e0a3a66-9aa4-48e9-b626-3be3d01e88ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdGWeZ1L5zKMSxYxqyV7j4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 14 · 2026-05-10T18:21:37.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W3wcXygLhW7skAAHiEXcBD`</summary>

```json
{
  "query": "token importance recurrence KV eviction reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e0a3a66-9aa4-48e9-b626-3be3d01e88ec",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMQ4iRrviB7uKH7GTZb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83c30901-ae91-483a-bf37-bbd4015d0786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdGWeZ1L5zKMSxYxqyV7j4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9031,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 377,
          "cache_read_input_tokens": 9031,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1415,
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

_source line 15 · 2026-05-10T18:21:40.268Z_

<details><summary>↩ Tool result · `toolu_01W1Nm8PbQRyaZCRkKi5nqGo`</summary>

```text
Web search results for query: "KV similarity activation sparsity correlation LLM"

Links: [{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/html/2512.07090"},{"title":"Track: Session 7: Quantization and Sparsity","url":"https://mlsys.org/virtual/2025/session/3153"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"Efficient Long-Context LLM Inference via KV Cache Clustering","url":"https://arxiv.org/html/2506.11418"},{"title":"SmallKV: Small Model Assisted Compensation of KV ...","url":"https://openreview.net/pdf?id=0BVrpXMr5Y"},{"title":"A Systematic Characterization of LLM Inference on GPUs","url":"https://www.arxiv.org/pdf/2512.01644"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/html/2504.15364"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884"}]

I found comprehensive research on KV similarity, activation sparsity, and correlation in LLMs. Here's a summary of the key findings:

## KV Similarity and Attention Correlation

Research has demonstrated a correlation between the cosine similarity among keys and their corresponding attention scores. More specifically, there is a consistently high correlation (ρ≈0.94 on average) across all layers, indicating that geometrically distinctive keys (those with low pairwise cosine similarity) are strongly aligned with tokens receiving higher attention scores.

## KV Similarity-Based Pruning Methods

Recent methods use lightweight KV-similarity–based selection that jointly considers key and value to identify highly redundant tokens and prune them in real time. Cosine similarity is computed between the key/value and the anchor key/value, where the anchor key/value represents the average of previous keys and values.

## Activation Sparsity Patterns

As token distance increases, the cosine similarity of key states generally decreases monotonically and follows a convex trend. Additionally, initial layers exhibit lower similarity compared to subsequent layers.

## Online Structured Pruning

Token Filtering is a lightweight online structured pruning technique that makes pruning decisions directly during inference without any calibration data, using KV similarity as the core mechanism for identifying redundant tokens.

These findings have led to practical optimization techniques for efficient LLM inference that leverage the strong correlation between key similarity and token importance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdfa2fcd-65b5-49a7-9a7b-ad1e1a1b2b00",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "90471b35-c0a6-4c43-ba51-de6f6955d087",
  "sourceToolAssistantUUID": "cdfa2fcd-65b5-49a7-9a7b-ad1e1a1b2b00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:21:41.529Z_

<details><summary>↩ Tool result · `toolu_01LBufifya4kduky8iQjTJWH`</summary>

```text
Web search results for query: "token redundancy MLP computation skip LLM inference"

Links: [{"title":"Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM","url":"https://arxiv.org/html/2505.15816"},{"title":"SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling","url":"https://arxiv.org/html/2506.04179v1"},{"title":"SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and","url":"https://arxiv.org/pdf/2506.04179"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.13155"},{"title":"[2601.13155] Probe and Skip: Self-Predictive Token Skipping for Efficient Long-Context LLM Inference","url":"https://arxiv.org/abs/2601.13155"},{"title":"DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding","url":"https://arxiv.org/html/2504.19327"},{"title":"Probe and Skip: Self-Predictive Token Skipping","url":"https://www.arxiv.org/pdf/2601.13155"},{"title":"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?","url":"https://arxiv.org/html/2502.11501"},{"title":"Skipping Computations in Multimodal LLMs","url":"https://arxiv.org/html/2410.09454"},{"title":"Accelerating Streaming Video Large Language Models via Hierarchical Token Compression","url":"https://arxiv.org/html/2512.00891"}]

Based on the search results, I found several recent research papers addressing token redundancy and MLP computation skipping in LLM inference. Here are the key findings:

## Key Research Areas

**SkipGPT: Dynamic Layer Pruning**

SkipGPT addresses two critical dynamics in LLM inference: horizontal dynamics where token-level heterogeneity demands context-aware pruning decisions, and vertical dynamics where the distinct functional roles of MLP and self-attention layers necessitate component-specific pruning policies. The framework uses global token-aware routing to prioritize critical tokens and decoupled pruning policies for MLP and self-attention components.

Notably, research reveals that attention modules exhibit greater redundancy than MLP modules, suggesting that while MLPs can be optimized, they are less redundant than attention mechanisms.

**Self-Predictive Token Skipping (SPTS)**

A novel training-free framework called Self-Predictive Token Skipping (SPTS) addresses efficient long-context LLM inference through selective token skipping strategies, including Partial Attention Probing (PAP) for multi-head attention and Low-rank Transformation Probing (LTP) for feed forward networks.

**ProxyV for Vision Tokens**

ProxyV introduces a group of proxy vision tokens to relieve full vision tokens from heavy computation burden, as an improvement over directly skipping heavy attention and FFN operations.

These approaches collectively demonstrate methods to identify and skip redundant computations while maintaining model performance, with SkipGPT reducing over 40% model parameters while matching or exceeding the performance of the original dense model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96ef48d7-5f75-4cb1-8ee0-750513f8e437",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "1a8dbc9e-08fa-400b-96b8-75bdc1a45f88",
  "sourceToolAssistantUUID": "96ef48d7-5f75-4cb1-8ee0-750513f8e437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T18:21:42.091Z_

<details><summary>↩ Tool result · `toolu_01BdQ3QT82UN1wnEct94DDCL`</summary>

```text
Web search results for query: "key vector similarity predict activation magnitude transformer"

Links: [{"title":"Query, Key, Value: The Foundation of Transformer Attention - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/query-key-value-attention-mechanism"},{"title":"Transformer Architecture Explained With Self-Attention Mechanism | Codecademy","url":"https://www.codecademy.com/article/transformer-architecture-self-attention-mechanism"},{"title":"Tutorial 6 (JAX): Transformers and Multi-Head Attention — UvA DL Notebooks v1.2 documentation","url":"https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/JAX/tutorial6/Transformers_and_MHAttention.html"},{"title":"billparker.ai: Transformer Attention: A Guide to the Q, K, and V Matrices","url":"https://www.billparker.ai/2024/10/transformer-attention-simple-guide-to-q.html"},{"title":"Tutorial 6: Transformers and Multi-Head Attention — UvA DL Notebooks v1.2 documentation","url":"https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial6/Transformers_and_MHAttention.html"},{"title":"To Understand Transformers, Focus on Attention – Scott H. Hawley","url":"https://drscotthawley.github.io/blog/posts/Transformers1-Attention.html"},{"title":"Transformer Explainer: LLM Transformer Model Visually Explained","url":"https://poloclub.github.io/transformer-explainer/"},{"title":"What are the query, key, and value vectors? | by RAHULRAJ P V | Medium","url":"https://rahulrajpvr7d.medium.com/what-are-the-query-key-and-value-vectors-5656b8ca5fa0"},{"title":"Query-Key Normalization in Transformers","url":"https://www.emergentmind.com/topics/query-key-normalization-qk-norm"},{"title":"Understanding Q,K,V In Transformer( Self Attention) | by mustafac | Analytics Vidhya | Medium","url":"https://medium.com/analytics-vidhya/understanding-q-k-v-in-transformer-self-attention-9a5eddaa5960"}]

Based on the search results, here's information about key vector similarity, activation magnitude, and transformers:

## Key Vector Similarity in Transformers

The dot product of the query vector of a token with the key vector of another token gives us a similarity score showing the relevance of the tokens to each other. The dot product between Qi and Kj measures the similarity between Qi and Kj, and a higher dot product indicates a higher relevance or alignment between what token i is seeking and what token j offers.

## The Activation Magnitude Problem

An important consideration in transformer architectures is how activation magnitudes change with dimensionality. As the dimension grows, dot products tend to become larger in magnitude, not because the vectors are more aligned, but simply because we're summing more terms. In high-dimensional vector spaces, which is the norm in transformer models, the dot product of two random vectors tends to have a larger magnitude because each dimension contributes to the total. This can result in attention scores that are large, pushing the softmax function into regions where it outputs very small gradients.

## Solution: Scaled Dot-Product Attention

The scaling factor √d effectively controls the variance of the dot product by scaling the dot product by the square root of the dimensionality of the Key vectors. This keeps the attention scores at a scale where the softmax function operates optimally, and the gradients remain at a magnitude conducive to learning.

Additionally, Query-Key Normalization (QK-Norm) encompasses a set of normalization techniques designed to improve the stability, expressivity, and controllability of attention-based neural architectures. QK-Norm methods intervene in the attention mechanism by explicitly normalizing, scaling, or otherwise regularizing the query and key vectors prior to the computation of attention logits, constraining the magnitude of attention scores and mitigating gradient instabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "977a54bc-f305-46f5-a4d8-a94d2af906e3",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "1b3f3a72-1ddc-4b03-a554-96b3450bd608",
  "sourceToolAssistantUUID": "977a54bc-f305-46f5-a4d8-a94d2af906e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T18:21:43.158Z_

<details><summary>↩ Tool result · `toolu_014WBTKLC37jYkzoLsJnHkoQ`</summary>

```text
Web search results for query: "token importance MLP attention correlation transformer inference"

Links: [{"title":"Learning to Explain: Supervised Token Attribution from Transformer Attention Patterns","url":"https://arxiv.org/html/2601.14112"},{"title":"Linear Predictability of Attention Heads in Large Language Models","url":"https://arxiv.org/html/2603.13314"},{"title":"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions","url":"https://arxiv.org/html/2402.15055v2"},{"title":"Transformers 101: Tokens, Attention, and Beyond! | by Mayank Sultania | Medium","url":"https://medium.com/@mayanksultania/transformers-101-tokens-attention-and-beyond-b080a900ca6c"},{"title":"Is Attention Required for Transformer Inference? Explore Function-preserving Attention Replacement","url":"https://arxiv.org/html/2505.21535v2"},{"title":"Representation Shift: Unifying Token Compression with FlashAttention","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Choi_Representation_Shift_Unifying_Token_Compression_with_FlashAttention_ICCV_2025_paper.pdf"},{"title":"MLP Can Be A Good Transformer Learner","url":"https://arxiv.org/html/2404.05657v1"},{"title":"What Matters in Transformers? Not All Attention is Needed","url":"https://arxiv.org/html/2406.15786v6"},{"title":"Filtering with Self-Attention and Storing with MLP: One-Layer Transformers Can Provably Acquire and Extract Knowledge","url":"https://arxiv.org/html/2508.00901"},{"title":"Rethinking Transformer Connectivity: TLinFormer, A Path","url":"https://arxiv.org/pdf/2508.20407"}]

Here are the search results for your query on token importance, MLP, attention correlation, and transformer inference:

## Key Findings

**Token Importance and Attention Patterns:**
Attention-based explanation methods treat token importance extraction as a supervised learning problem, training on human-annotated rationales to discover which attention configurations correlate with human-judged token importance.

**Attention-MLP Interactions:**
Some attention heads recognize specific contexts relevant to predicting a token and activate downstream token-predicting neurons accordingly, providing a deeper understanding of how attention heads work with MLP neurons to perform next-token prediction.

**Linear Correlations in Attention Heads:**
Pretrained Transformers exhibit a pervasive inter-head linear structure where for a given token, the Query, Key, and Value vectors of an attention head can often be reconstructed as a linear combination of a small number of peer heads—typically within the same layer.

**MLP's Role in Knowledge Storage:**
The MLP is the primary component for knowledge storage in transformer-based language models.

**Efficiency Analysis:**
Jointly dropping low-importance Attention and MLP layers yields better performance under high sparsity conditions compared to pruning only one type of layer. Additionally, ExpNet requires only a single forward pass of a lightweight MLP over pre-computed attention features, with no gradients, sampling, or perturbations at inference time.

These results cover recent research on understanding token importance through attention patterns, the interaction between attention and MLP components, and practical implications for transformer inference optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4e7a642-4a9e-4b1c-800e-a3582f2d75d9",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "11267e83-1b2a-4c8c-b73c-a2fdb74c98da",
  "sourceToolAssistantUUID": "d4e7a642-4a9e-4b1c-800e-a3582f2d75d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T18:21:43.493Z_

<details><summary>↩ Tool result · `toolu_01Q24p2XW8LwEvg2qtj1KHP9`</summary>

```text
Web search results for query: "redundant token MLP sparsity reasoning LLM"

Links: [{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v1"},{"title":"METEOR: Multi-Encoder Collaborative Token Pruning for Efficient","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_METEOR_Multi-Encoder_Collaborative_Token_Pruning_for_Efficient_Vision_Language_Models_ICCV_2025_paper.pdf"},{"title":"Sparsity Forcing: Reinforcing Token Sparsity of MLLMs","url":"https://arxiv.org/html/2504.18579v4"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/html/2403.15388"},{"title":"Jenga: Enhancing LLM Long-Context Fine-tuning with ...","url":"https://www.usenix.org/system/files/atc25-wang-tuowei.pdf"},{"title":"preprint INFORMED ROUTING IN LLMS: SMARTER TOKEN-","url":"https://arxiv.org/pdf/2510.13831"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"},{"title":"Sparsity Meets Similarity: Leveraging Long-Tail Distribution for Dynamic Optimized Token Representation in Multimodal Large Language Models","url":"https://arxiv.org/html/2409.01162"},{"title":"SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and","url":"https://arxiv.org/pdf/2506.04179"},{"title":"Think Clearly: Improving Reasoning via Redundant Token Pruning","url":"https://arxiv.org/html/2507.08806v1"}]

Based on the search results, I found relevant research on redundant token pruning, MLP sparsity, and reasoning in large language models. Here's what the literature reveals:

## Token Redundancy in LLM Reasoning

Recent language models tend to include substantial redundancy in reasoning paths, with attention scores widely scattered. Deliberately removing this redundancy in the reasoning process significantly improves performance through clear thinking.

Researchers identify reasoning redundancy by measuring token-level attention scores to a special end-of-thinking token, and propose structure-aware pruning that prioritizes removing tokens in low-contributing reasoning chunks over individual tokens.

## MLP vs. Attention Module Sparsity

The MLP module has higher redundancy during the decoding phase compared to the pre-filling phase, while attention redundancy remains nearly the same in both phases. Additionally, self-attention is more redundant than FFN blocks, and many token transformations in self-attention are approximable by simple linear operations.

## Token Reduction Strategies

TokenSkip enables LLMs to skip less important tokens within chain-of-thought sequences and learn shortcuts between critical reasoning steps, allowing for controllable compression with adjustable compression ratios to automatically trim redundant tokens during reasoning.

Information-driven token elimination utilizes a score-based algorithm that dynamically identifies and eliminates redundant tokens within attention blocks, and extends this approach to the MLP block, ensuring consistency across various components of the model.

The research indicates that token pruning is an effective approach for improving both efficiency and reasoning performance in LLMs by identifying and removing redundant computations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cc73cb3-e1f6-4632-8741-e0a060e5d9ce",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "62eca011-efb4-4f34-9dc5-44a1b4e45461",
  "sourceToolAssistantUUID": "0cc73cb3-e1f6-4632-8741-e0a060e5d9ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T18:21:44.038Z_

<details><summary>↩ Tool result · `toolu_01W3wcXygLhW7skAAHiEXcBD`</summary>

```text
Web search results for query: "token importance recurrence KV eviction reasoning"

Links: [{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning","url":"https://arxiv.org/html/2506.15969v1"},{"title":"Published as preprint paper G-KV: DECODING-TIME KV CACHE EVICTION WITH","url":"https://arxiv.org/pdf/2512.00504"},{"title":"[2506.15969] LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning","url":"https://arxiv.org/abs/2506.15969"},{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for","url":"https://www.arxiv.org/pdf/2506.15969v3"},{"title":"Token Eviction Mechanism","url":"https://www.emergentmind.com/topics/token-eviction-mechanism"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v2"},{"title":"CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based","url":"https://arxiv.org/pdf/2504.14051"},{"title":"KV Cache Eviction in Transformer LLMs","url":"https://www.emergentmind.com/topics/kv-cache-eviction"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"NACL: A General and Effective KV Cache Eviction ...","url":"https://aclanthology.org/2024.acl-long.428.pdf"}]

Based on the search results, here's what I found about token importance recurrence and KV eviction in reasoning tasks:

## Token Importance Recurrence Phenomenon

A Token Importance Recurrence phenomenon has been identified where a large proportion of tokens in reasoning tasks receive renewed attention after multiple decoding steps. These "recurring tokens" may have low attention scores within an interval while suddenly increasing in the future.

## Why This Matters for KV Eviction

Empirical analysis demonstrates that these tokens often contain information vital for later reasoning stages, and premature eviction of recurring tokens leads to catastrophic performance degradation. Existing KV compression methods usually fail to identify such tokens due to inherent limitations.

## The LazyEviction Solution

LazyEviction is an Observation Window-based Lagged Eviction Mechanism retaining latent recurring tokens by performing lagged evictions across decoding steps, which contains two key components: (1) Recurrence Interval Tracking for capturing temporal variations in token importance, and (2) an Maximum Recurrence Interval-Centric Eviction Policy that prioritizes eviction based on tokens' recurrence patterns.

## Performance Impact

LazyEviction reduces KV cache size by 50% while maintaining comparable accuracy on mathematics reasoning datasets, outperforming state-of-the-art methods. The findings highlight the importance of preserving recurring tokens, which are critical for maintaining knowledge continuity in multi-step reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83c30901-ae91-483a-bf37-bbd4015d0786",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "904711de-ec5c-419c-bd51-799d0caf876b",
  "sourceToolAssistantUUID": "83c30901-ae91-483a-bf37-bbd4015d0786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T18:21:44.477Z_

<details><summary>↩ Tool result · `toolu_01PNVfL2WezihidmKEGNu1Uy`</summary>

```text
Web search results for query: "KV cache insertion filtering LLM inference"

Links: [{"title":"KV Caching Explained: Optimizing Transformer Inference Efficiency","url":"https://huggingface.co/blog/not-lain/kv-caching"},{"title":"Understanding and Coding the KV Cache in LLMs from Scratch","url":"https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms"},{"title":"LLM Inference Series: 4. KV caching, a deeper look | by Pierre Lienhart | Medium","url":"https://medium.com/@plienhar/llm-inference-series-4-kv-caching-a-deeper-look-4ba9a77746c8"},{"title":"Master KV cache aware routing with llm-d for efficient AI inference | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/10/07/master-kv-cache-aware-routing-llm-d-efficient-ai-inference"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"[2603.20397] KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/abs/2603.20397"},{"title":"Selective KV-Cache Sharing to Mitigate Timing Side-Channels in LLM Inference","url":"https://arxiv.org/pdf/2508.08438"},{"title":"How to Cut LLM Inference Costs with KV Caching | Everpure Blog","url":"https://blog.everpuredata.com/purely-technical/cut-llm-inference-costs-with-kv-caching/"},{"title":"KV Caching in LLM Inference A Comprehensive Review","url":"https://www.rohan-paul.com/p/kv-caching-in-llm-inference-a-comprehensive"},{"title":"[2511.01815] KV Cache Transform Coding for Compact Storage in LLM Inference","url":"https://arxiv.org/abs/2511.01815"}]

Based on the search results, here's what I found about KV cache insertion filtering in LLM inference:

## KV Cache Basics

A KV cache stores intermediate key (K) and value (V) computations for reuse during inference, which results in a substantial speed-up when generating text. The key-value (KV) cache is a foundational optimization in Transformer-based large language models (LLMs), eliminating redundant recomputation of past token representations during autoregressive generation.

## KV Cache Insertion and Filtering Techniques

The search results reveal several advanced techniques for managing KV cache insertion and filtering:

**SafeKV - Privacy-Based Filtering**: When a KV-cache block is created, the system immediately inserts it as Private and continues serving the request without waiting for any detector, then the block is upgraded to shareable only after background verification completes. This uses a Hybrid Detector with tier-1 rule-based filters, tier-2 lightweight transformer classifiers, and tier-3 large-model validation.

**StreamingLLM and Token Filtering**: The StreamingLLM framework builds on the observation that the initial tokens collect a large amount of attention, and therefore builds a sliding window by only keeping the very first positional tokens ("sink tokens") and the last neighboring tokens (local attention) in the cache.

**RocketKV - Two-Stage Selection**: RocketKV combines coarse eviction with dynamic sparse selection to accelerate long-context inference, using SnapKV for coarse-grain KV cache eviction in the first stage and Hybrid Sparse Attention (HAS) to select relevant tokens dynamically in the second stage.

These techniques address the core challenge that the KV cache's memory footprint scales linearly with context length, imposing critical bottlenecks on GPU memory capacity, memory bandwidth, and inference throughput.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad6cdca6-c045-48e5-a726-2ff82794c337",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "5954ec8f-19eb-441b-bc8e-040139bd1cbe",
  "sourceToolAssistantUUID": "ad6cdca6-c045-48e5-a726-2ff82794c337",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T18:21:47.058Z_

<details><summary>↩ Tool result · `toolu_011Mcwp2CBNtTRF6eRz6zXLZ`</summary>

```text
Web search results for query: "selective KV cache storage token generation"

Links: [{"title":"Transformers KV Caching Explained | by João Lages | Medium","url":"https://medium.com/@joaolages/kv-caching-explained-276520203249"},{"title":"[2602.02579] ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2602.02579"},{"title":"ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2602.02579"},{"title":"Understanding and Coding the KV Cache in LLMs from Scratch","url":"https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v2"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"},{"title":"Unlocking Longer Generation with Key-Value Cache Quantization","url":"https://huggingface.co/blog/kv-cache-quantization"},{"title":"(PDF) SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models","url":"https://www.researchgate.net/publication/398513412_SkipKV_Selective_Skipping_of_KV_Generation_and_Storage_for_Efficient_Inference_with_Large_Reasoning_Models"},{"title":"Techniques for KV Cache Optimization in Large Language Models","url":"https://www.omrimallis.com/posts/techniques-for-kv-cache-optimization/"},{"title":"LLM Inference and KV Cache Complete Guide [2026]: How Token Generation Works | QubitTool","url":"https://qubittool.com/blog/llm-inference-kv-cache-guide"}]

Based on the search results, here's what I found about selective KV cache storage token generation:

## Overview

A KV cache stores intermediate key (K) and value (V) computations for reuse during inference (after training), which results in a substantial speed-up when generating text. By caching the previous Keys and Values, we can focus on only calculating the attention for the new token.

## Selective Storage Approaches

Recent research has developed several selective storage methods to optimize KV cache memory usage:

**ProphetKV**: ProphetKV is a user-query-driven KV Cache reuse method for RAG scenarios that dynamically prioritizes tokens based on their semantic relevance to the user query and employs a dual-stage recomputation pipeline to fuse layer-wise attention metrics into a high-utility set.

**TRIM-KV**: Each gate predicts a scalar retention score that decays over time, reflecting the long-term utility of the token for a specific layer and head. Tokens with low scores are evicted when the memory budget is exceeded, ensuring that the cache always contains the most critical tokens.

**SkipKV**: It selectively skips KV-cache storage and generation by leveraging sentence-level redundancy detection.

## Common Selection Criteria

Most KV compression approaches use importance-based selection, relying on explicit token-wise criteria such as attention-weight accumulators (heavy-hitter tracking), with attention-accumulation tracking cumulative attention received by each token and retaining top-K (heavy hitters) plus a recency buffer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e0a3a66-9aa4-48e9-b626-3be3d01e88ec",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "2cc52ac5-549e-4692-92f1-70edc344579a",
  "sourceToolAssistantUUID": "2e0a3a66-9aa4-48e9-b626-3be3d01e88ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T18:21:49.521Z_

Let me do a few more targeted searches to dig deeper into the most relevant findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cc52ac5-549e-4692-92f1-70edc344579a",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMRK2RwYwCU6stJq1Wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "307c49b2-9ee8-4361-9168-a9b224c12f0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ff5zBifP4uLFp1HhqDJuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 6931,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6931,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T18:21:50.472Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QVCatwHzH3rXY6X26pWj5V`</summary>

```json
{
  "query": "SkipKV selective skipping KV generation storage reasoning models paper 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "307c49b2-9ee8-4361-9168-a9b224c12f0f",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMRK2RwYwCU6stJq1Wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2c8ebc1-f037-4ee7-9103-170596cfd91b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ff5zBifP4uLFp1HhqDJuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 6931,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6931,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T18:21:51.412Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LNLQpYafNfnhuMYB5Gj7BH`</summary>

```json
{
  "query": "\"Polar Sparsity\" contextual sparsity MLP activation prediction LLM batched inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2c8ebc1-f037-4ee7-9103-170596cfd91b",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMRK2RwYwCU6stJq1Wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7793f3b9-90f5-4746-8d82-0fa5aa3b9ff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ff5zBifP4uLFp1HhqDJuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 6931,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6931,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T18:21:51.902Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UGC5tJvUrGptcHgjdL5HC8`</summary>

```json
{
  "query": "attention score predict MLP neuron activation sparsity transformer layer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7793f3b9-90f5-4746-8d82-0fa5aa3b9ff1",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMRK2RwYwCU6stJq1Wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf3877e4-d88c-4b5d-8608-9e377d15d1ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ff5zBifP4uLFp1HhqDJuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 6931,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6931,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T18:21:52.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CJLF4qWq2Bic8NwkTjdMF7`</summary>

```json
{
  "query": "\"token filtering\" KV similarity online pruning LLM arxiv 2512.07090"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf3877e4-d88c-4b5d-8608-9e377d15d1ff",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMRK2RwYwCU6stJq1Wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b45ae94d-082a-4aaa-b2d1-26cd2103b472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ff5zBifP4uLFp1HhqDJuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 6931,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6931,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-10T18:21:53.400Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AUvnmNiTmaRwonjdWsKRrf`</summary>

```json
{
  "query": "LazyEviction recurring token attention KV cache eviction reasoning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b45ae94d-082a-4aaa-b2d1-26cd2103b472",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMRK2RwYwCU6stJq1Wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fde10ad-a8d7-4c9c-8cf7-31e8895c205f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ff5zBifP4uLFp1HhqDJuE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 6931,
      "cache_read_input_tokens": 10446,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6931
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 845,
          "output_tokens": 296,
          "cache_read_input_tokens": 10446,
          "cache_creation_input_tokens": 6931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6931,
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

_source line 29 · 2026-05-10T18:21:58.708Z_

<details><summary>↩ Tool result · `toolu_01QVCatwHzH3rXY6X26pWj5V`</summary>

```text
Web search results for query: "SkipKV selective skipping KV generation storage reasoning models paper 2025"

Links: [{"title":"[2512.07993] SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models","url":"https://arxiv.org/abs/2512.07993"},{"title":"(PDF) SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models","url":"https://www.researchgate.net/publication/398513412_SkipKV_Selective_Skipping_of_KV_Generation_and_Storage_for_Efficient_Inference_with_Large_Reasoning_Models"},{"title":"1 Introduction","url":"https://arxiv.org/html/2512.07993"},{"title":"Improving Model Representation and Reducing KV Cache via Skip Connections with First Value Heads","url":"https://arxiv.org/html/2510.16807v1"},{"title":"SwiftKV: Fast Prefill-Optimized Inference with Knowledge- ...","url":"https://aclanthology.org/2025.emnlp-main.1306.pdf"},{"title":"[2510.16807] Improving Model Representation and Reducing KV Cache via Skip Connections with First Value Heads","url":"https://arxiv.org/abs/2510.16807"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"Self-Predictive Token Skipping for Efficient Long-Context ...","url":"https://www.arxiv.org/pdf/2601.13155"},{"title":"ATTENTION IS ALL YOU NEED FOR KV CACHE IN DIFFUSION LLMS","url":"https://arxiv.org/pdf/2510.14973"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"}]

Based on the web search results, I found detailed information about the SkipKV paper:

## SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models

Large reasoning models (LRMs) often cost significant key-value (KV) cache overhead due to their linear growth with the verbose chain-of-thought (CoT) reasoning process, creating both memory and throughput bottlenecks that limit their efficient deployment.

### Key Approach

SkipKV is a sentence-aware selective KV eviction and generation framework designed for efficient CoT reasoning, featuring two key methods: the sentence-primary scoring method and the adaptive steering method to efficiently skip token storage and generation, respectively.

The method introduces a sentence-scoring metric to identify and remove highly similar sentences while maintaining semantic coherence. To suppress redundant generation, SkipKV dynamically adjusts a steering vector to update the hidden activation states during inference enforcing the LRM to generate concise response.

### Performance Results

Extensive evaluations on multiple reasoning benchmarks demonstrate SkipKV maintains up to 26.7% improved accuracy compared to alternatives at a similar compression budget, and compared to state-of-the-art methods, SkipKV yields up to 1.6× fewer generation length while improving throughput up to 1.7×.

The paper conducts comprehensive evaluations on DeepSeek-R1-Qwen-7B, R1-Qwen-14B, and R1-Llama-8B LRMs across four reasoning benchmarks: AIME-24, LiveCodeBench, MATH-500, and GSM8K.

The paper was published on December 8, 2025, with authors led by Jiayi Tian.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2c8ebc1-f037-4ee7-9103-170596cfd91b",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "510a857f-9487-4ec3-abfd-f1b2d56abefe",
  "sourceToolAssistantUUID": "c2c8ebc1-f037-4ee7-9103-170596cfd91b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T18:21:58.896Z_

<details><summary>↩ Tool result · `toolu_01CJLF4qWq2Bic8NwkTjdMF7`</summary>

```text
Web search results for query: ""token filtering" KV similarity online pruning LLM arxiv 2512.07090"

Links: [{"title":"[2512.07090] Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/abs/2512.07090"},{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://www.arxiv.org/pdf/2512.07090"},{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/html/2512.07090"},{"title":"(PDF) Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://www.researchgate.net/publication/398476553_Leveraging_KV_Similarity_for_Online_Structured_Pruning_in_LLMs"},{"title":"Similarity-Aware Token Pruning: Your VLM but Faster","url":"https://arxiv.org/html/2503.11549"},{"title":"ASAP: Attention-Shift-Aware Pruning for Efficient LVLM Inference","url":"https://arxiv.org/html/2603.14549v2"},{"title":"LazyLLM: Dynamic Token Pruning for Efficient Long Context LLM Inference","url":"https://arxiv.org/html/2407.14057v1"},{"title":"TopV: Compatible Token Pruning with Inference Time Optimization for Fast","url":"https://arxiv.org/pdf/2503.18278v2"},{"title":"(PDF) Similarity-Aware Token Pruning: Your VLM but Faster","url":"https://www.researchgate.net/publication/389894457_Similarity-Aware_Token_Pruning_Your_VLM_but_Faster"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"}]

Based on the search results, I found detailed information about the paper you're looking for:

## Token Filtering: Leveraging KV Similarity for Online Structured Pruning in LLMs (arXiv 2512.07090)

Token Filtering is a lightweight online structured pruning technique that makes pruning decisions directly during inference without any calibration data.

### Key Innovation

The key idea is to measure token redundancy via joint key-value similarity and skip redundant attention computations, thereby reducing inference cost while preserving critical information.

### Technical Approach

The method uses a variance-aware fusion strategy that adaptively weights key and value similarity across heads, ensuring that informative tokens are retained even under high pruning ratios. This design introduces no additional memory overhead.

### Performance Results

Extensive experiments on LLaMA-2 (7B/13B), LLaMA-3 (8B), and Mistral (7B) demonstrate that Token Filtering consistently outperforms prior structured pruning methods, preserving accuracy on commonsense reasoning benchmarks and maintaining strong performance on challenging tasks such as MMLU, even with 50% pruning.

The paper was posted on arXiv on December 8, 2025, and addresses the limitation of existing pruning approaches that rely on offline calibration data which may not generalize well across different inputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b45ae94d-082a-4aaa-b2d1-26cd2103b472",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "f578f30b-6aca-4b1a-af34-c04efbb30fa6",
  "sourceToolAssistantUUID": "b45ae94d-082a-4aaa-b2d1-26cd2103b472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T18:21:59.846Z_

<details><summary>↩ Tool result · `toolu_01AUvnmNiTmaRwonjdWsKRrf`</summary>

```text
Web search results for query: "LazyEviction recurring token attention KV cache eviction reasoning LLM"

Links: [{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning","url":"https://arxiv.org/html/2506.15969v1"},{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250615969Z/abstract"},{"title":"[2506.15969] LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning","url":"https://arxiv.org/abs/2506.15969"},{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for","url":"https://www.arxiv.org/pdf/2506.15969v2"},{"title":"NACL: A General and Effective KV Cache Eviction Framework for LLM at Inference Time | Request PDF","url":"https://www.researchgate.net/publication/384207931_NACL_A_General_and_Effective_KV_Cache_Eviction_Framework_for_LLM_at_Inference_Time"},{"title":"KV Cache Eviction in Transformer LLMs","url":"https://www.emergentmind.com/topics/kv-cache-eviction"},{"title":"[2410.12876] In-context KV-Cache Eviction for LLMs via Attention-Gate","url":"https://arxiv.org/abs/2410.12876"},{"title":"CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based","url":"https://arxiv.org/pdf/2504.14051"},{"title":"[2503.08879] LLMs Know What to Drop: Self-Attention Guided KV Cache Eviction for Efficient Long-Context Inference","url":"https://arxiv.org/abs/2503.08879"},{"title":"SAGE-KV: Self-Attention Guided KV Cache Eviction","url":"https://www.emergentmind.com/papers/2503.08879"}]

## Summary of LazyEviction

LazyEviction addresses the KV cache efficiency problem in LLMs by identifying a "Token Importance Recurrence phenomenon" where certain tokens receive renewed attention after multiple decoding steps. The method implements an observation window-based lagged eviction framework that retains recurring tokens through recurrence interval tracking and a maximum recurrence interval-centric eviction policy.

### Key Features

The research reveals that a large proportion of tokens regain high attention after multiple decoding steps, which existing methods fail to capture and may lead to unpredictable eviction of these periodically critical tokens. LazyEviction's framework enables prediction of future token importance, thereby preventing premature eviction of recurring tokens.

### Performance Results

LazyEviction reduces KV cache size by 50% while maintaining comparable accuracy on mathematics reasoning datasets, outperforming state-of-the-art methods. The findings highlight the importance of preserving recurring tokens, which are critical for maintaining knowledge continuity in multi-step reasoning tasks.

The method has been implemented on large reasoning models such as DeepSeek-R1-Distill-Qwen and DeepSeek-R1-Distill-Llama, achieving 50% KV budget reduction while maintaining comparable performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fde10ad-a8d7-4c9c-8cf7-31e8895c205f",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "019fef3f-5014-48c0-bf28-6b5a7ade8b0c",
  "sourceToolAssistantUUID": "4fde10ad-a8d7-4c9c-8cf7-31e8895c205f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T18:22:01.262Z_

<details><summary>↩ Tool result · `toolu_01UGC5tJvUrGptcHgjdL5HC8`</summary>

```text
Web search results for query: "attention score predict MLP neuron activation sparsity transformer layer"

Links: [{"title":"Crisp Attention: Regularizing Transformers via Structured Sparsity","url":"https://arxiv.org/html/2508.06016v1"},{"title":"Uncovering Layer-Dependent Activation Sparsity Patterns in ReLU Transformers","url":"https://arxiv.org/html/2407.07848v1"},{"title":"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models","url":"https://arxiv.org/html/2512.12744"},{"title":"Predicting Attention Sparsity in Transformers","url":"https://aclanthology.org/2022.spnlp-1.7.pdf"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"The Lazy Neuron Phenomenon: On Emergence of Activation Sparsity in Transformers | OpenReview","url":"https://openreview.net/forum?id=TJ2nxciYCk-"},{"title":"TRANSFORMER ACCELERATION WITH DYNAMIC SPARSE ATTENTION","url":"https://arxiv.org/pdf/2110.11299"},{"title":"Sparse attention cuts transformer O(n²) complexity | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/sparse-attention-cuts-transformer-on%C2%B2-complexity/"},{"title":"THE LAZY NEURON PHENOMENON: ON EMERGENCE ...","url":"https://openreview.net/pdf?id=TJ2nxciYCk-"},{"title":"MLP-ATTENTION: IMPROVING TRANSFORMER ARCHI","url":"https://openreview.net/pdf?id=99XvUeDFYTD"}]

Based on the search results, here's what I found about the relationship between attention scores, MLP neuron activation, and sparsity in transformer layers:

## Key Findings

**Attention Sparsity and MLP Activations:**
In the context of Transformers, enforcing sparsity in MLP activations has been shown to improve model robustness and calibration. Additionally, structured attention sparsity can serve as a primary regularization technique to significantly increase model accuracy, challenging the conventional view that sparsity is merely a tool for compression.

**Predicting Attention Sparsity:**
Research specifically addresses predicting sparse attention patterns. An approximation of attention scores with low computational costs is first obtained, then the sparse attention patterns are predicted using the approximate attention scores.

**Layer-Dependent Sparsity Patterns:**
The extent of sparsity, and also its evolution over the course of training, follow dramatically different patterns based on layer index, with the first layer and final layer in the network occupying distinct and opposing niches in terms of their sparsity behavior.

**MLP Neuron Activation Sparsity:**
Previous work has demonstrated that MLPs within ReLU Transformers exhibit high levels of sparsity, with many of their activations equal to zero for any given token.

**Combined Sparsity Strategy:**
Recent work has explored using both attention and MLP sparsity together. A method computes an importance index for each attention head before the attention module processes it, and this approach further applies sparsification to feed-forward neurons, creating a two-level sparsity strategy across both the attention and MLP sublayers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf3877e4-d88c-4b5d-8608-9e377d15d1ff",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "00b1df90-4f0b-45bf-8473-a1ed8728b048",
  "sourceToolAssistantUUID": "bf3877e4-d88c-4b5d-8608-9e377d15d1ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T18:22:04.455Z_

<details><summary>↩ Tool result · `toolu_01LNLQpYafNfnhuMYB5Gj7BH`</summary>

```text
Web search results for query: ""Polar Sparsity" contextual sparsity MLP activation prediction LLM batched inference"

Links: [{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884v1"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://arxiv.org/pdf/2505.14884"},{"title":"[2505.14884] Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/abs/2505.14884"},{"title":"Polar Sparsity: High Throughput Batched LLM","url":"https://openreview.net/pdf?id=cg2S1qqNSq"},{"title":"Paper page - Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://huggingface.co/papers/2505.14884"},{"title":"NeurIPS Poster Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://neurips.cc/virtual/2025/poster/117070"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://openreview.net/pdf/43bf702e03ce0cb3a890cf8a35f3ded98d30b94d.pdf"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity | OpenReview","url":"https://openreview.net/forum?id=cg2S1qqNSq"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with ...","url":"https://susavlsh10.github.io/files/Polar_Sparsity_NeurIPS_2025_CameraReady.pdf"},{"title":"[PDF] Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Polar-Sparsity:-High-Throughput-Batched-LLM-with-Shrestha-Settlemyer/328fcf757fa9647ea5eb96d37ee735e52a43df43"}]

Here are the search results for "Polar Sparsity":

## Overview

Polar Sparsity highlights a key shift in sparsity importance from MLP to Attention layers as batch size and sequence length scale. Contextual sparsity, where each token dynamically activates only a small subset of the model parameters, shows promise but does not scale to large batch sizes due to union of active neurons quickly approaching dense computation.

## Key Insights

While MLP layers become more compute-efficient under batching, their sparsity vanishes. In contrast, attention becomes increasingly more expensive at scale, while their head sparsity remains stable and batch-invariant.

In large-batch inference, the cost of accessing model parameters is largely amortized, since the entire batch utilizes the same model weights. In contrast, each batch has a unique key-value (KV) cache, making attention layers memory I/O expensive.

## Technical Approach

The MLP router follows the design used in prior contextual sparsity work. Each router is a two-layer feedforward network with a hidden dimension of 1024, trained independently for each transformer layer. It is trained using supervised learning with ground-truth neuron activations derived from dense MLP outputs. At inference time, the router produces scalar logits for each neuron, which are used to rank and select the top-k neurons for activation.

## Performance Results

The work develops hardware-efficient, sparsity-aware GPU kernels for selective MLP and Attention computations, delivering up to 2.2 × end-to-end speedups for models like OPT, LLaMA-2 & 3, across various batch sizes and sequence lengths without compromising accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7793f3b9-90f5-4746-8d82-0fa5aa3b9ff1",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "ebf4edbc-2e0b-45f6-a2b9-40288b9e4c66",
  "sourceToolAssistantUUID": "7793f3b9-90f5-4746-8d82-0fa5aa3b9ff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T18:22:08.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018HknLyzXiME1q1txgxRdFt`</summary>

```json
{
  "query": "DEJA VU contextual sparsity predict MLP attention head activation similarity LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf4edbc-2e0b-45f6-a2b9-40288b9e4c66",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMSbTvHP6iM1SNL4ag8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4eb72bc7-39f9-446d-9836-9b35a21d048e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YVA7Sji2v2xXW6kw1hA73",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2625,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 17377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3173,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-10T18:22:09.333Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RDXRxoRn1Tg7ZN1RoRnGwh`</summary>

```json
{
  "query": "\"attention-MLP interaction\" token representation predict neuron firing transformer mechanistic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eb72bc7-39f9-446d-9836-9b35a21d048e",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMSbTvHP6iM1SNL4ag8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0215bff-52b0-4291-a333-67a96650d3ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YVA7Sji2v2xXW6kw1hA73",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2625,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 17377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3173,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-10T18:22:09.680Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ApQeKrWFQgYZ8PY8QSrnK7`</summary>

```json
{
  "query": "KV cache filtering insertion time decide whether store token generation autoregressive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0215bff-52b0-4291-a333-67a96650d3ce",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMSbTvHP6iM1SNL4ag8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de2d7100-0512-4e60-b318-aaaeb3541327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YVA7Sji2v2xXW6kw1hA73",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2625,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 17377,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3173
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2625,
          "output_tokens": 169,
          "cache_read_input_tokens": 17377,
          "cache_creation_input_tokens": 3173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3173,
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

_source line 37 · 2026-05-10T18:22:13.895Z_

<details><summary>↩ Tool result · `toolu_018HknLyzXiME1q1txgxRdFt`</summary>

```text
Web search results for query: "DEJA VU contextual sparsity predict MLP attention head activation similarity LLM"

Links: [{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"},{"title":"[2310.17157] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/abs/2310.17157"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMS at Inference Time","url":"https://minjiazhang.github.io/courses/sp24-resource/DejaVu-pre.pdf"},{"title":"GitHub - FMInference/DejaVu · GitHub","url":"https://github.com/FMInference/DejaVu"},{"title":"[PDF] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deja-Vu:-Contextual-Sparsity-for-Efficient-LLMs-at-Liu-Wang/95240dda409e28acccdc5cf619ad0c036cf4292d"},{"title":"Deja Vu: contextual sparsity for efficient LLMs at inference ...","url":"https://dl.acm.org/doi/10.5555/3618408.3619327"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time | OpenReview","url":"https://openreview.net/forum?id=wIPIhHd00i"},{"title":"Deja Vu vs Not All Attention is Needed: Two Paths to LLM Efficiency | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/deja-vu-vs-not-all-attention-is-needed-two-paths-to-llm-efficiency-ec58748e983f"},{"title":"Deja Vu: Efficient Contextual Sparsity in LLMs","url":"https://www.emergentmind.com/papers/2310.17157"},{"title":"Paper page - Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://huggingface.co/papers/2310.17157"}]

I found relevant research on DEJA VU. Here's what the search revealed:

## Overview

DEJA VU is based on the hypothesis that contextual sparsity—small, input-dependent sets of attention heads and MLP parameters that yield approximately the same output as the dense model for a given input—can address computational efficiency issues in LLMs.

## Key Findings on Activation Similarity

The research demonstrates substantial sparsity opportunities in LLM components:

- Over 80% of attention heads can be silenced for a given token
- Over 95% of MLP parameters can be zeroed out for a given token

## Prediction Mechanism

A low-cost small trainable MLP (two-layer fully connected network) is used to predict contextual sparsity on the fly. The validation accuracy for attention sparse predictors is around 93% in the middle layers and near 99% in the shallow and deep layers.

## Understanding Contextual Sparsity

The system exploits the properties of residual connections in LLMs, noting that token embeddings change gradually across layers—a phenomenon allowing predictions to be made one layer ahead, thus parallelizing predictions with ongoing computations.

## Performance Results

DEJA VU speeds up generation by 1.8-2× compared to state-of-the-art methods and by 4.8-6× compared to widely used implementations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eb72bc7-39f9-446d-9836-9b35a21d048e",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "4781cf18-d0ec-4133-9843-cbe34742b6ca",
  "sourceToolAssistantUUID": "4eb72bc7-39f9-446d-9836-9b35a21d048e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T18:22:16.144Z_

<details><summary>↩ Tool result · `toolu_01RDXRxoRn1Tg7ZN1RoRnGwh`</summary>

```text
Web search results for query: ""attention-MLP interaction" token representation predict neuron firing transformer mechanistic"

Links: [{"title":"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions","url":"https://arxiv.org/html/2402.15055v1"},{"title":"[2402.15055] Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions","url":"https://arxiv.org/abs/2402.15055"},{"title":"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.930/"},{"title":"Interpreting Context Look-ups in Transformers","url":"https://aclanthology.org/2024.emnlp-main.930.pdf"},{"title":"[2309.08593] Attention-Only Transformers and Implementing MLPs with Attention Heads","url":"https://ar5iv.labs.arxiv.org/html/2309.08593"},{"title":"Patterns and Messages: A New Framing of Transformer Attention · Chris McCormick","url":"https://mccormickml.com/2025/02/18/patterns-and-messages-intro/"},{"title":"Analyzing Feed-Forward Blocks in Transformers through the Lens of Attention Maps","url":"https://arxiv.org/html/2302.00456"},{"title":"Transformer Dynamics: A neuroscientific approach to interpretability of large language models","url":"https://arxiv.org/html/2502.12131"},{"title":"Mechanistic Interpretability: Peeking Inside an LLM | Towards Data Science","url":"https://towardsdatascience.com/mechanistic-interpretability-peeking-inside-an-llm/"},{"title":"Transformers 101: Tokens, Attention, and Beyond! | by Mayank Sultania | Medium","url":"https://medium.com/@mayanksultania/transformers-101-tokens-attention-and-beyond-b080a900ca6c"}]

Based on the web search results, I found highly relevant research on attention-MLP interactions in transformers. Here are the key findings:

## Main Research on Attention-MLP Interactions

A major study investigates the interplay between attention heads and specialized "next-token" neurons in the Multilayer Perceptron that predict specific tokens. The analysis identifies attention heads that recognize contexts relevant to predicting a particular token, activating the associated neuron through the residual connection.

## Mechanistic Understanding

The research proposes a methodology to identify next-token neurons, find prompts that highly activate them, and determine the upstream attention heads responsible, then generate and evaluate explanations for the activity of these attention heads in an automated manner.

## Token Prediction Mechanism

Findings reveal that some attention heads recognize specific contexts relevant to predicting a token and activate a downstream token-predicting neuron accordingly, providing a deeper understanding of how attention heads work with MLP neurons to perform next-token prediction.

## Broader Context on Transformer Architecture

All components of a transformer (the token embedding, attention heads, MLP layers, and unembedding) communicate with each other by reading and writing to different subspaces of the residual stream. MLP networks store much of the knowledge, with later layers tending to contain more semantic and less shallow knowledge.

The research demonstrates how transformer models use coordinated interactions between attention and MLP components to achieve context-dependent token prediction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0215bff-52b0-4291-a333-67a96650d3ce",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "ac561fe3-5e5c-40ee-aace-5137c7c5bf99",
  "sourceToolAssistantUUID": "e0215bff-52b0-4291-a333-67a96650d3ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T18:22:18.138Z_

<details><summary>↩ Tool result · `toolu_01ApQeKrWFQgYZ8PY8QSrnK7`</summary>

```text
Web search results for query: "KV cache filtering insertion time decide whether store token generation autoregressive"

Links: [{"title":"[2603.20397] KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/abs/2603.20397"},{"title":"What is a KV cache, and why does it make LLM inference faster? | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/faq/docs/kv-cache.html"},{"title":"KV Caching Explained: Optimizing Transformer Inference Efficiency","url":"https://huggingface.co/blog/not-lain/kv-caching"},{"title":"KV Cache - AI Pocket Reference: NLP","url":"https://vectorinstitute.github.io/ai-pocket-reference/nlp/llms/efficient_inference/kv_cache.html"},{"title":"KV Prediction for Improved Time to First Token","url":"https://arxiv.org/html/2410.08391v1"},{"title":"Past- and Future-Informed KV Cache Policy with Salience Estimation in Autoregressive Video Diffusion","url":"https://arxiv.org/html/2601.21896"},{"title":"LLM Inference and KV Cache Complete Guide [2026]: How Token Generation Works | QubitTool","url":"https://qubittool.com/blog/llm-inference-kv-cache-guide"},{"title":"How KV caches impact time to first token for LLMs","url":"https://www.glean.com/blog/glean-kv-caches-llm-latency"},{"title":"Transformers KV Caching Explained | by João Lages | Medium","url":"https://medium.com/@joaolages/kv-caching-explained-276520203249"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"}]

Based on the search results, I found several relevant papers and resources addressing KV cache management and token generation decisions:

## KV Cache Fundamentals

The key-value (KV) cache is a foundational optimization in Transformer-based large language models (LLMs), eliminating redundant recomputation of past token representations during autoregressive generation. A KV cache stores past key and value tensors so an LLM can reuse them during autoregressive decoding, which speeds up inference by avoiding repeated attention computation over the same prefix.

## Filtering and Selective Retention

Your query touches on the challenge of deciding which tokens to store in the KV cache. Recent research has addressed this:

One approach observes that token contributions to generation are highly time-heterogeneous and proposes a Past- and Future-Informed KV Cache Policy (PaFu-KV) that introduces a lightweight Salience Estimation Head distilled from a bidirectional teacher to estimate salience scores, allowing the KV cache to retain informative tokens while discarding less relevant ones.

## Insertion Timing Decisions

The challenge of estimating how future queries will attend to each token in the context requires accessing attention scores from the past and from future tokens that are not available at the time of compression. Expected Attention estimates the importance that each token in the context has for queries that have not been generated and accordingly prunes the KV cache up to 60% while preserving performance quality.

During standard autoregressive generation, new KV cache entries are added as new tokens are processed.

The research indicates that deciding whether and when to store tokens in the KV cache is an active area of optimization, with methods focusing on estimating token importance and salience to make intelligent filtering decisions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de2d7100-0512-4e60-b318-aaaeb3541327",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "e091ae6f-78e5-440e-99c0-296b9104dd12",
  "sourceToolAssistantUUID": "de2d7100-0512-4e60-b318-aaaeb3541327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-10T18:22:21.162Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018zBW3NysCvrnR9D9K7A5Zy`</summary>

```json
{
  "query": "KeyDiff key similarity KV cache eviction cosine distance token importance 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e091ae6f-78e5-440e-99c0-296b9104dd12",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMTbzSjq3YCQKxZo5pA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f96fce8-b80f-4d1a-a545-3f09b1f3e2f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoGMTSVQQ55SUaaQSkhfXt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5569,
      "cache_read_input_tokens": 20550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5569,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-10T18:22:21.932Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019e1pk4afYFz7vQWDcM1LZJ`</summary>

```json
{
  "query": "\"Probe and Skip\" self-predictive token skipping MLP FFN probing LLM inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f96fce8-b80f-4d1a-a545-3f09b1f3e2f1",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMTbzSjq3YCQKxZo5pA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7520c1c1-8154-4c45-b514-bb3b91fbffcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoGMTSVQQ55SUaaQSkhfXt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5569,
      "cache_read_input_tokens": 20550,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5569
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 20550,
          "cache_creation_input_tokens": 5569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5569,
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

_source line 42 · 2026-05-10T18:22:29.106Z_

<details><summary>↩ Tool result · `toolu_018zBW3NysCvrnR9D9K7A5Zy`</summary>

```text
Web search results for query: "KeyDiff key similarity KV cache eviction cosine distance token importance 2025"

Links: [{"title":"[2504.15364] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/abs/2504.15364"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/html/2504.15364"},{"title":"KEYDIFF: Key Similarity-Based KV Cache Eviction for Long ...","url":"https://openreview.net/pdf/461c983f15c05127a5a4f31daa7628230411afbb.pdf"},{"title":"(PDF) KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://www.researchgate.net/publication/391020426_KeDiff_Key_Similarity-Based_KV_Cache_Eviction_for_Long-Context_LLM_Inference_in_Resource-Constrained_Environments"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250415364P/abstract"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"NeurIPS Poster KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://neurips.cc/virtual/2025/poster/115521"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/keydiff-key-similarity-based-kv-cache-eviction"},{"title":"HashEvict: A Pre-Attention KV Cache Eviction Strategy using Locality-Sensitive Hashing","url":"https://arxiv.org/html/2412.16187v3"}]

I've successfully performed a web search for your query. The results provide comprehensive information about KeyDiff and related KV cache eviction methods. Here are the key findings:

## KeyDiff Overview

KeyDiff is a training-free KV cache eviction method based solely on key similarity. Lower pairwise cosine similarity among keys correlates with higher attention scores, suggesting its utility as a proxy for token importance.

## Key Mechanism

Keys with lower average pairwise cosine similarity tend to receive higher attention scores across a variety of inputs. This suggests that key diversity serves as a strong proxy for global token importance, even without access to future tokens. KeyDiff introduces an eviction strategy that selects keys based on their similarity to other cached entries without relying on attention scores.

## Performance Benefits

KeyDiff demonstrates a performance gap of less than 0.04% with 8K cache budget (approximately 23% KV cache reduction) from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B. The method also achieves near baseline performance for Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark and decreases end-to-end inference latency by up to 30% compared to other token-eviction methods.

## Key Advantage

KeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention.

The research on KeyDiff was published in 2025, with the most recent version available on arXiv as of January 20, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f96fce8-b80f-4d1a-a545-3f09b1f3e2f1",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "5eab6597-8918-4b16-968e-b57ecb3c9ea1",
  "sourceToolAssistantUUID": "8f96fce8-b80f-4d1a-a545-3f09b1f3e2f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T18:22:32.242Z_

<details><summary>↩ Tool result · `toolu_019e1pk4afYFz7vQWDcM1LZJ`</summary>

```text
Web search results for query: ""Probe and Skip" self-predictive token skipping MLP FFN probing LLM inference"

Links: [{"title":"Probe and Skip: Self-Predictive Token Skipping","url":"https://www.arxiv.org/pdf/2601.13155"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.13155"},{"title":"[2601.13155] Probe and Skip: Self-Predictive Token Skipping for Efficient Long-Context LLM Inference","url":"https://arxiv.org/abs/2601.13155"},{"title":"LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding","url":"https://arxiv.org/pdf/2404.16710"},{"title":"Skip-Vision: Efficient and Scalable Acceleration of Vision-Language Models via Adaptive Token Skipping","url":"https://arxiv.org/html/2503.21817"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs Xuan Luo, Weizhi Wang, Xifeng Yan","url":"https://arxiv.org/pdf/2503.23798"},{"title":"What Layers When: Learning to Skip Compute in LLMs with Residual Gates","url":"https://arxiv.org/html/2510.13876"},{"title":"Skipping Computations in Multimodal LLMs","url":"https://arxiv.org/html/2410.09454"},{"title":"LayerSkip: faster LLM Inference with Early Exit and Self-speculative decoding | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/layerskip-faster-llm-inference-with-early-exit-and-self-speculative-decoding-3110cb93c94e"},{"title":"TokenSkip: Efficient Token and Module Skipping","url":"https://www.emergentmind.com/topics/tokenskip"}]

Based on the search results, here's what I found about "Probe and Skip" and Self-Predictive Token Skipping:

## Overview

"Probe and Skip" proposes a novel training-free framework dubbed Self-Predictive Token Skipping (SPTS), for efficient long-context LLM inference.

## Core Principle

The core principle of self-predictive token skipping is that a token's eligibility for skipping is determined by its potential impact within the target layer.

## Key Techniques

The framework introduces two main probing strategies:

**For Multi-Head Attention (MHA):**
For MHA, Partial Attention Probing (PAP) is introduced, which evaluates token importance by probing a small portion of attention score.

**For Feed-Forward Networks (FFN):**
For FFN, Low-rank Transformation Probing (LTP) is proposed, where a low-rank proxy network is pre-constructed to approximate the original FFN, and token selection is then guided by a combination of token-level proxy changes and attention scores.

## Performance Results

The method achieves up to 2.46× speedups on LLaMA-3.1-8B-Instruct for prefilling and end-to-end generation, respectively, with minimal performance degradation.

The paper was published on arXiv on February 2, 2026, and represents a training-free approach to improving LLM inference efficiency for long-context scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7520c1c1-8154-4c45-b514-bb3b91fbffcf",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "aa1543551dfcb7eca",
  "type": "user",
  "uuid": "76e17403-abad-4e15-818c-69f54e76ea40",
  "sourceToolAssistantUUID": "7520c1c1-8154-4c45-b514-bb3b91fbffcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-10T18:23:55.119Z_

Here is a comprehensive report of what the literature says across your two main lines of inquiry.

---

## Part 1: Does KV Cache Similarity Correlate with MLP Activation Sparsity?

### Direct evidence linking key similarity to MLP sparsity

No paper was found that directly studies the correlation "tokens with similar keys also have more compressible/sparse MLP activations." The two phenomena -- KV redundancy and MLP activation sparsity -- are well-studied individually, and a few papers come close to bridging them, but the explicit causal or correlational link you are asking about remains largely unestablished in the literature. Here is what exists:

### 1. KeyDiff (arXiv 2504.15364, NeurIPS 2025)

This is the strongest result connecting key similarity to token importance. KeyDiff demonstrates that **keys with lower average pairwise cosine similarity tend to receive higher attention scores**, with a correlation of rho ~0.94 across layers. This means geometrically distinctive keys (low cosine similarity to neighbors) are strongly aligned with tokens that matter more for attention computation. KeyDiff uses this as an eviction signal: tokens whose keys are very similar to other cached keys are treated as redundant and evicted. Critically, this works **without computing attention scores at all**, enabling compatibility with FlashAttention. However, KeyDiff says nothing about what happens in the MLP layers for those redundant tokens.

### 2. Deja Vu: Contextual Sparsity (arXiv 2310.17157, ICML 2024)

Deja Vu is the foundational paper on contextual sparsity. It shows that for any given input token, **over 80% of attention heads and over 95% of MLP neurons can be zeroed out** with minimal accuracy loss. It trains small two-layer MLP "routers" to predict which neurons/heads to activate, and these routers achieve ~93-99% accuracy. The key insight is that the **residual stream representation changes slowly across layers**, enabling predictions one layer ahead. However, Deja Vu does not use KV similarity as a predictor -- it uses separate trained routers per layer. The prediction is from the hidden state, not from key vectors specifically.

### 3. Polar Sparsity (arXiv 2505.14884, NeurIPS 2025)

Polar Sparsity extends Deja Vu to batched inference and makes an important observation: **MLP sparsity does not scale well to large batches** (the union of active neurons across a batch quickly approaches dense computation), while **attention head sparsity remains batch-invariant**. It also uses trained MLP routers to predict neuron activations. Again, the router predicts from hidden states, not from key similarity. But the observation that attention-level sparsity is more stable than MLP-level sparsity is relevant to your question -- it suggests that signals derived from the attention mechanism (like KV similarity) might be a more reliable basis for optimization than MLP-internal signals.

### 4. Token Filtering via KV Similarity (arXiv 2512.07090)

This paper uses **joint key-value similarity** with a variance-aware fusion strategy to perform online structured pruning -- deciding to skip entire attention computations for redundant tokens during inference. It achieves 50% pruning with minimal accuracy loss on LLaMA-2/3 and Mistral. Importantly, this is **structured pruning of the token dimension** (skipping a token's participation in attention), not MLP sparsity. But it validates that KV similarity is a strong signal for identifying tokens that contribute little to computation.

### 5. Attention-MLP Interaction (arXiv 2402.15055, EMNLP 2024)

This mechanistic interpretability paper shows that **specific attention heads recognize contexts and activate downstream "next-token neurons" in the MLP** through the residual stream. This demonstrates a functional coupling between attention patterns and MLP neuron firing, but the relationship is mediated by the residual stream, not by key similarity per se.

### 6. Probe and Skip / SPTS (arXiv 2601.13155)

This training-free framework uses **Partial Attention Probing (PAP)** for attention and **Low-rank Transformation Probing (LTP)** for FFN layers. For FFN token skipping, it constructs a low-rank proxy of the FFN and uses a combination of proxy output magnitude and attention scores to decide which tokens to skip. This is the closest to using an attention-derived signal to drive MLP-level decisions, but it still relies on a proxy computation rather than raw KV similarity.

### 7. SkipGPT (arXiv 2506.04179)

SkipGPT performs **decoupled pruning of MLP and attention modules**, finding that attention modules exhibit greater redundancy than MLP modules. It uses global token-aware routing to prioritize critical tokens, but the MLP and attention pruning decisions are made by separate policies, not coupled through KV similarity.

### Assessment for your question

The gap in the literature is clear: **no one has explicitly tested whether tokens with high pairwise key similarity also exhibit sparser/more compressible MLP activations**. The building blocks exist -- KeyDiff shows key similarity predicts token importance for attention, Deja Vu/Polar Sparsity show MLP activations are highly sparse and predictable from hidden states, and the attention-MLP interaction work shows functional coupling. But the specific hypothesis that KV similarity could serve as a valid signal for MLP sparsity decisions has not been validated.

There is an indirect reason to think it might work: if two tokens have very similar keys, they will receive similar attention patterns and thus produce similar post-attention residual stream updates. Since the MLP takes the residual stream as input, similar post-attention representations would likely produce similar MLP activation patterns (and thus similar sparsity patterns). But "similar sparsity patterns" is not the same as "higher sparsity." For the signal to validly drive MLP sparsity, you would need to show that **redundant tokens (high key similarity to neighbors) tend to have higher MLP activation sparsity**, not just similar sparsity to their neighbors.

---

## Part 2: KV Cache Insertion Filtering (Deciding at Generation Time Whether to Cache)

### Papers that address filtering at insertion time (as opposed to periodic eviction)

### 1. SkipKV (arXiv 2512.07993)

This is the most directly relevant paper. SkipKV is a **sentence-aware selective KV eviction and generation framework** for reasoning models. It has two components:
- A **sentence-primary scoring method** that identifies and removes highly similar sentences (not just tokens) while maintaining semantic coherence
- An **adaptive steering method** that dynamically adjusts hidden activation states to suppress redundant generation entirely

SkipKV skips both the **storage** and **generation** of KV pairs for redundant tokens. It maintains up to 26.7% improved accuracy vs. alternatives at similar compression budgets and achieves 1.6x fewer generated tokens with 1.7x throughput improvement. Evaluated on DeepSeek-R1 variants.

### 2. LazyEviction (arXiv 2506.15969)

LazyEviction identifies a **"Token Importance Recurrence" phenomenon** in reasoning tasks: tokens that appear unimportant (low attention) in a local window can suddenly become critical many steps later. It introduces:
- **Recurrence Interval Tracking** to capture temporal variation in token importance
- A **Maximum Recurrence Interval-Centric Eviction Policy** that avoids evicting tokens with long recurrence patterns

This achieves 50% KV cache reduction while maintaining accuracy on math reasoning. The key insight for your work: **any insertion-filtering approach must account for the fact that token importance is non-monotonic in reasoning tasks** -- a token that looks redundant now may be critical 100 steps later.

### 3. TRIM-KV / Cache What Lasts (arXiv 2512.03324)

Each gate predicts a scalar **retention score** that decays over time, reflecting the long-term utility of a token for a specific layer and head. Tokens with low scores are evicted when the memory budget is exceeded. This is closer to a continuous scoring mechanism than a binary insertion filter.

### 4. Expected Attention (arXiv 2510.00636)

This paper tackles the fundamental challenge of insertion-time filtering: you need to estimate importance for **future queries that haven't been generated yet**. Expected Attention estimates future attention distributions and uses them to prune up to 60% of the KV cache while preserving quality.

### 5. PaFu-KV (Past and Future-Informed KV Cache Policy)

Uses a lightweight **Salience Estimation Head** distilled from a bidirectional teacher to estimate token salience, combining past and future importance signals. This enables more informed retention decisions.

### 6. Attention-Gate (arXiv 2410.12876)

In-context KV cache eviction using learned attention gates that modulate which tokens to retain.

### 7. StreamingLLM

Retains only "sink tokens" (initial tokens that accumulate disproportionate attention) and a local sliding window. This is a simple insertion-time heuristic: keep the first few tokens always, keep recent tokens, discard everything else.

### Assessment for insertion filtering

The literature shows a clear progression:
- Early methods (StreamingLLM) use static rules
- Middle-generation methods (H2O, SnapKV) use attention-score accumulators to evict periodically
- Recent methods (SkipKV, LazyEviction, Expected Attention) try to make proactive decisions at or near insertion time, incorporating future-importance estimation

The major caveat from LazyEviction is that **insertion-time filtering is dangerous for reasoning tasks** because of token importance recurrence. Any viable approach would need a mechanism to either (a) defer final eviction decisions, or (b) recompute evicted entries when they become important again.

---

## Summary Assessment

**Can KV-similarity-based signal validly drive MLP sparsity decisions?** The literature provides indirect support but no direct validation:

1. Key similarity is a validated proxy for **attention-level token importance** (KeyDiff, rho ~0.94).
2. MLP activations are highly sparse and predictable from **hidden states** (Deja Vu, Polar Sparsity).
3. Attention patterns functionally couple to MLP neuron activation through the **residual stream** (attention-MLP interaction work).
4. The missing link is empirical evidence that tokens flagged as redundant by KV similarity also have higher/more predictable MLP sparsity.
5. The theoretical argument (similar keys -> similar attention -> similar residual -> similar MLP behavior) is plausible but does not directly imply *higher* sparsity for redundant tokens.

**For insertion filtering:** SkipKV is the closest existing work, operating at sentence level with both storage and generation skipping. LazyEviction's finding on token importance recurrence is a critical caveat: naive insertion filtering will fail on reasoning tasks.

Sources:
- [KeyDiff: Key Similarity-Based KV Cache Eviction](https://arxiv.org/abs/2504.15364)
- [Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time](https://arxiv.org/abs/2310.17157)
- [Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity](https://arxiv.org/abs/2505.14884)
- [Token Filtering: Leveraging KV Similarity for Online Structured Pruning in LLMs](https://arxiv.org/abs/2512.07090)
- [Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions](https://arxiv.org/abs/2402.15055)
- [Probe and Skip: Self-Predictive Token Skipping for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2601.13155)
- [SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling](https://arxiv.org/abs/2506.04179)
- [SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models](https://arxiv.org/abs/2512.07993)
- [LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning](https://arxiv.org/abs/2506.15969)
- [Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs](https://arxiv.org/abs/2512.03324)
- [Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution](https://arxiv.org/abs/2510.00636)
- [KV Cache Optimization Strategies for Scalable and Efficient LLM Inference](https://arxiv.org/abs/2603.20397)
- [Think Clearly: Improving Reasoning via Redundant Token Pruning](https://arxiv.org/html/2507.08806v1)
- [The Lazy Neuron Phenomenon: On Emergence of Activation Sparsity in Transformers](https://openreview.net/forum?id=TJ2nxciYCk-)
- [Uncovering Layer-Dependent Activation Sparsity Patterns in ReLU Transformers](https://arxiv.org/abs/2407.07848)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76e17403-abad-4e15-818c-69f54e76ea40",
  "isSidechain": true,
  "agentId": "aa1543551dfcb7eca",
  "requestId": "req_011CauMUeDBFrTiT4mUMTG5E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f68fda2e-cd9f-422a-9e58-47a8b1d99312",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kc6DtZPtW3H5nYnqp3YVAc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2140,
      "cache_read_input_tokens": 26119,
      "output_tokens": 3238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2140
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3238,
          "cache_read_input_tokens": 26119,
          "cache_creation_input_tokens": 2140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2140,
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
