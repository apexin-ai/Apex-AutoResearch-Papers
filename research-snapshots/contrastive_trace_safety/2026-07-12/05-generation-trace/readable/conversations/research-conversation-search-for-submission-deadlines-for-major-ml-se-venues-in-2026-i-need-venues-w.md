# Research conversation: Search for submission deadlines for major ML/SE venues in 2026. I need venues whose submission deadline is AFTER 2026-05

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a1d4f585bf67d390d.jsonl`
- **Structured JSON:** [`ddcf43ae5b534e32288f.json`](../../sessions/dd/ddcf43ae5b534e32288f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-11T20:39:17.690Z_

Search for submission deadlines for major ML/SE venues in 2026. I need venues whose submission deadline is AFTER 2026-05-11. Search for:

1. WebSearch: "NeurIPS 2026 submission deadline"
2. WebSearch: "ICLR 2027 submission deadline"
3. WebSearch: "EMNLP 2026 submission deadline"
4. WebSearch: "AAAI 2027 submission deadline"
5. WebSearch: "ASE 2026 submission deadline"
6. WebSearch: "ISSTA 2027 submission deadline"
7. WebSearch: "FSE 2027 submission deadline"
8. WebSearch: "ICML 2026 submission deadline"
9. WebSearch: "ACL 2026 submission deadline"
10. WebSearch: "COLM 2026 submission deadline"

For each venue, report the exact submission deadline date if found. I need to filter out any venue whose deadline has already passed as of 2026-05-11.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "8e2e2f6e-8a7d-47c0-a5be-819f456c7997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T20:39:17.694Z_

```json
{
  "parentUuid": "8e2e2f6e-8a7d-47c0-a5be-819f456c7997",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
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
  "uuid": "01af7e41-7de3-4db9-b837-e48540d442fd",
  "timestamp": "2026-05-11T20:39:17.694Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T20:39:20.007Z_



I'll start by loading the WebSearch tool schema, then run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01af7e41-7de3-4db9-b837-e48540d442fd",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRiRCTJAwwrqY7VoGGw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2446e70a-cbbe-4fdf-970b-4d7915e35d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBqBjkDPrXmWuToGGzMKim",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 766,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T20:39:20.552Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0178A9zHb4D85ZerxCZBgobN`</summary>

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
  "parentUuid": "2446e70a-cbbe-4fdf-970b-4d7915e35d0e",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRiRCTJAwwrqY7VoGGw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4e67c0a-8394-4e41-a25d-3ccef432540e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBqBjkDPrXmWuToGGzMKim",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 7304,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 766
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 766,
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

_source line 5 · 2026-05-11T20:39:20.554Z_

<details><summary>↩ Tool result · `toolu_0178A9zHb4D85ZerxCZBgobN`</summary>

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
  "parentUuid": "e4e67c0a-8394-4e41-a25d-3ccef432540e",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "a63f7943-0efc-4318-8334-f8a02456418e",
  "sourceToolAssistantUUID": "e4e67c0a-8394-4e41-a25d-3ccef432540e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T20:39:24.893Z_



Now let me run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a63f7943-0efc-4318-8334-f8a02456418e",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cf4b0df-236e-449f-8e9a-77a1954d211f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

_source line 7 · 2026-05-11T20:39:25.388Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017yzPfFsipCJc33THoQPcWt`</summary>

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
  "parentUuid": "4cf4b0df-236e-449f-8e9a-77a1954d211f",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2010e99-0c75-489a-b8c4-85d59d00a61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

_source line 8 · 2026-05-11T20:39:25.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FwN1a1yhKY3ze7WqtcY28x`</summary>

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
  "parentUuid": "a2010e99-0c75-489a-b8c4-85d59d00a61d",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6a4e959-7cf8-45ff-9943-203fbbb73a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

_source line 9 · 2026-05-11T20:39:25.864Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UedY4DbCoNLhKMNgucChgF`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6a4e959-7cf8-45ff-9943-203fbbb73a64",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cce9cc5d-14bc-4117-937c-68a36fd2da8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

_source line 10 · 2026-05-11T20:39:26.343Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Smr5DFEVaiemPCEWxn3EBT`</summary>

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
  "parentUuid": "cce9cc5d-14bc-4117-937c-68a36fd2da8a",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bcbd974-5163-407a-84aa-275acecf2c58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

_source line 11 · 2026-05-11T20:39:26.786Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012oy5Wy2sqg1LDVLDrwYxrr`</summary>

```json
{
  "query": "ASE 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bcbd974-5163-407a-84aa-275acecf2c58",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e97e97cb-3fb2-4214-832f-e10a106c9ae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

_source line 12 · 2026-05-11T20:39:27.308Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014c9TcXfCzS1fdsUAuwUrGj`</summary>

```json
{
  "query": "ISSTA 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e97e97cb-3fb2-4214-832f-e10a106c9ae9",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "280f843e-a744-4135-bf3c-344ba92e1596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

_source line 13 · 2026-05-11T20:39:27.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FVZ3zsV3JmEwupS9hfsaFn`</summary>

```json
{
  "query": "FSE 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "280f843e-a744-4135-bf3c-344ba92e1596",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fd081cc-5b72-42ed-9a62-a4a25c88af5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

_source line 14 · 2026-05-11T20:39:27.728Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R8vmqLb2fvqZc8NrmnyaSo`</summary>

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
  "parentUuid": "8fd081cc-5b72-42ed-9a62-a4a25c88af5e",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c150fa7-f425-4112-aee5-2128f17ed9ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

_source line 15 · 2026-05-11T20:39:28.200Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DNi2KGw5wYAQgTo2aNcv4P`</summary>

```json
{
  "query": "ACL 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c150fa7-f425-4112-aee5-2128f17ed9ce",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "444e69c2-5c99-46a1-ab13-923c6bea3772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

_source line 16 · 2026-05-11T20:39:28.263Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VimA5oxy8SRJrbWk4eVQQa`</summary>

```json
{
  "query": "COLM 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "444e69c2-5c99-46a1-ab13-923c6bea3772",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRidaqAFkczoQpUM75o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb617cd8-8dae-4c5f-9255-7720a7f4c45f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRT1AmnVJzXMUX1Pur2Tfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8070,
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

### Tool result

_source line 17 · 2026-05-11T20:39:28.940Z_

<details><summary>↩ Tool result · `toolu_01FwN1a1yhKY3ze7WqtcY28x`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"}]

Based on the search results, I was unable to find specific information about the ICLR 2027 submission deadline. The search results primarily contained information about ICLR 2026 (which already occurred) and general information about the conference.

The search results show that ICLR is typically held in late April or early May each year, but the specific submission deadline for ICLR 2027 has not yet been announced or is not readily available online.

For the most accurate and up-to-date information about ICLR 2027 submission deadlines, I recommend checking the official ICLR website at iclr.cc directly, as they will publish the call for papers and submission deadlines when they become available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6a4e959-7cf8-45ff-9943-203fbbb73a64",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "deb9fed8-5c76-41a0-9ab0-224e4e8f2918",
  "sourceToolAssistantUUID": "a6a4e959-7cf8-45ff-9943-203fbbb73a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T20:39:29.189Z_

<details><summary>↩ Tool result · `toolu_017yzPfFsipCJc33THoQPcWt`</summary>

```text
Web search results for query: "NeurIPS 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FConference"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"2026 Conference","url":"https://neurips.cc/Conferences/2026"},{"title":"NeurIPS Conference (@NeurIPSConf) / X","url":"https://x.com/NeurIPSConf"},{"title":"NeurIPS: Neural Information Processing Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2212"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"}]

Based on the search results, here is the NeurIPS 2026 submission deadline information:

The abstract submission deadline is May 4, 2026 (AOE - Anywhere on Earth), and the full paper submission deadline, including all supplementary materials, is May 6, 2026 AOE.

Note that the different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines.

Additionally, the conference is held December 6th through the 12th, 2026, and author notification is September 24, 2026 (AoE).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2010e99-0c75-489a-b8c4-85d59d00a61d",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "e6b2c299-f49d-4a90-819e-bea55195f934",
  "sourceToolAssistantUUID": "a2010e99-0c75-489a-b8c4-85d59d00a61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T20:39:30.349Z_

<details><summary>↩ Tool result · `toolu_01UedY4DbCoNLhKMNgucChgF`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here's the information about EMNLP 2026 submission deadlines:

The ARR submission deadline for long and short papers is May 25, 2026. Additionally, the reviewer registration deadline for all authors is May 27, 2026.

The conference itself will be held in Budapest, Hungary from October 24th to October 29th, 2026.

Other important dates for EMNLP 2026 include:
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026
- Camera-ready papers due: September 20, 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cce9cc5d-14bc-4117-937c-68a36fd2da8a",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "a1c100f1-dc33-428a-bdaf-2c9a7b1aa48c",
  "sourceToolAssistantUUID": "cce9cc5d-14bc-4117-937c-68a36fd2da8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-11T20:39:30.460Z_

<details><summary>↩ Tool result · `toolu_01Smr5DFEVaiemPCEWxn3EBT`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's what I found regarding the AAAI 2027 submission deadline:

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027. However, the AAAI 2027 paper submission deadline is TBD (to be determined).

While the exact deadline hasn't been officially announced yet, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns. For the most current information, you can check the official AAAI call for papers at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bcbd974-5163-407a-84aa-275acecf2c58",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "953177fc-2f9c-4cfa-9035-edd981381e38",
  "sourceToolAssistantUUID": "2bcbd974-5163-407a-84aa-275acecf2c58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-11T20:39:30.892Z_

<details><summary>↩ Tool result · `toolu_01FVZ3zsV3JmEwupS9hfsaFn`</summary>

```text
Web search results for query: "FSE 2027 submission deadline"

Links: [{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"Call for Papers | IACR Transactions on Symmetric Cryptology","url":"https://tosc.iacr.org/index.php/ToSC/Call"},{"title":"FSE: Foundations of Software Engineering 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1093"},{"title":"FSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/fse-2026"},{"title":"FSE 2027 - Research Papers - FSE 2027","url":"https://conf.researchr.org/track/fse-2027/fse-2027-papers"},{"title":"Upcoming Events | FSE","url":"http://www.esec-fse.org/upcoming_events"},{"title":"FSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/home/fse-2027"},{"title":"Home | FSE","url":"https://www.esec-fse.org/"},{"title":"The deadline for FSE 2026 Research Paper submission is ...","url":"https://www.facebook.com/fseconference/posts/the-deadline-for-fse-2026-research-paper-submission-is-approaching-in-three-week/782885284237049/"},{"title":"Important Dates - FSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/dates/fse-2027"}]

Based on the search results, I found information about FSE 2027. In 2027, the conference will be held in Shenzhen, China, and it will take place from July 12-16, 2027.

However, the search results don't contain a specific submission deadline date for FSE 2027. Papers must be submitted electronically through the FSE 2027 submission site, and the link will be posted when closer to the deadline. For the most current and detailed deadline information, I recommend checking the official FSE 2027 website at https://conf.researchr.org/home/fse-2027 or the Important Dates page at https://conf.researchr.org/dates/fse-2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fd081cc-5b72-42ed-9a62-a4a25c88af5e",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "bce1146c-8ab0-4fb5-af59-7ac897d3b379",
  "sourceToolAssistantUUID": "8fd081cc-5b72-42ed-9a62-a4a25c88af5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-11T20:39:31.980Z_

<details><summary>↩ Tool result · `toolu_01R8vmqLb2fvqZc8NrmnyaSo`</summary>

```text
Web search results for query: "ICML 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected","url":"https://eu.36kr.com/en/p/3540848514510723"},{"title":"ICML 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=icml26"},{"title":"ICML 2026 Call for Post-Conference Workshops","url":"https://icml.cc/Conferences/2026/CallForWorkshops"},{"title":"ICML 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FConference"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"ICML 2026 Call For Position Papers","url":"https://icml.cc/Conferences/2026/CallForPositionPapers"},{"title":"Update ICML 2025 and 2026 conference data · huggingface/ai-deadlines at 55d2124","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/55d21240bacc3ac62397280592b3dd5ded9e5683"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"}]

Based on the search results, here is the information about ICML 2026 submission deadlines:

The ICML 2026 paper submission deadline is January 28, 2026.

Additionally, there are specific deadlines for different components:

- **Abstract submission deadline:** Abstract and paper submission deadlines are strict with no extensions given.
- **Position papers:** Position papers have an abstract submission deadline of January 24, 2026 (AoE) and a full paper submission deadline of January 29, 2026 (AoE).

The Forty-Third annual ICML conference is held from July 6th through July 11th, 2026 at the Coex Convention & Exhibition Center.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c150fa7-f425-4112-aee5-2128f17ed9ce",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "8253ec62-e13e-4cd9-bafa-004800373857",
  "sourceToolAssistantUUID": "4c150fa7-f425-4112-aee5-2128f17ed9ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-11T20:39:32.017Z_

<details><summary>↩ Tool result · `toolu_014c9TcXfCzS1fdsUAuwUrGj`</summary>

```text
Web search results for query: "ISSTA 2027 submission deadline"

Links: [{"title":"ISSTA 2026","url":"https://issta2026.hotcrp.com/"},{"title":"ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA) | ISSTA","url":"http://www.issta.org/"},{"title":"ISSTA 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/issta-2026"},{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"ISSTA: International Symposium on Software Testing and Analysis 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1760"},{"title":"ISSTA 2024 - Technical Papers - ISSTA 2024","url":"https://2024.issta.org/track/issta-2024-papers"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ISSTA 2025 - conf.researchr.org","url":"https://conf.researchr.org/home/issta-2025"},{"title":"ISSTA 2023 - Technical Papers - ISSTA 2023","url":"https://2023.issta.org/track/issta-2023-technical-papers"},{"title":"International Symposium on Software Testing and Analysis - Accepted Papers, Deadline, Impact Factor & Score 2026 | Research.com","url":"https://research.com/conference/international-symposium-on-software-testing-and-analysis"}]

Based on the search results, I was unable to find specific submission deadline information for ISSTA 2027. The search results show information about ISSTA 2026 (which has already passed its submission deadline) and earlier years, but ISSTA 2027 will be held in Singapore with chairs Jun Sun, Dan Hao, and Jacques Klein.

However, the specific submission deadline dates for ISSTA 2027 do not appear to be available yet in the search results. I recommend:

1. Visiting the official ISSTA website at https://issta.org/ for the latest announcements
2. Checking the ResearchR conference page once it's set up for ISSTA 2027
3. Monitoring the official ISSTA social media channels for deadline announcements

Typically, ISSTA announces its submission deadlines several months in advance, so checking back periodically on their official channels would be your best approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "280f843e-a744-4135-bf3c-344ba92e1596",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "c7b131e6-50be-4cfc-8ff6-3d5282ccc21a",
  "sourceToolAssistantUUID": "280f843e-a744-4135-bf3c-344ba92e1596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-11T20:39:32.345Z_

<details><summary>↩ Tool result · `toolu_01VimA5oxy8SRJrbWk4eVQQa`</summary>

```text
Web search results for query: "COLM 2026 submission deadline"

Links: [{"title":"COLM 2026: Key Dates","url":"https://colmweb.org/dates.html"},{"title":"COLM 2026: Call for Papers","url":"https://colmweb.org/cfp.html"},{"title":"Conference on Language Modeling on X: \"COLM 2026 is just around the corner! Mark your calendars for: 💡Abstract deadline: Thursday, March 26, 2026 📄Full paper submission deadline: Tuesday, March 31, 2026 Call for papers in thread (website coming soon). https://t.co/YfjLxzCqxO\" / X","url":"https://x.com/COLM_conf/status/2000952051212415394"},{"title":"COLM 2026","url":"https://colmweb.org/"},{"title":"Conference on Language Modeling (COLM), 2026 | ServiceNow AI Research","url":"https://www.servicenow.com/research/event/2026-colm.html"},{"title":"COLM 2026: Submission Instructions","url":"https://colmweb.org/submission-instructions.html"},{"title":"COLM 2026: Author Guide","url":"https://colmweb.org/AuthorGuide.html"},{"title":"When is COLM 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/colm"},{"title":"COLM 2026 Conference | OpenReview","url":"https://openreview.net/group?id=colmweb.org%2FCOLM%2F2026%2FConference"},{"title":"COLM 2026: Call for Workshops","url":"https://colmweb.org/cfw.html"}]

Based on the search results, here are the key submission deadlines for COLM 2026:

**Main Conference:**
- Abstract deadline: Thursday, March 26, 2026
- Full paper submission deadline: Tuesday, March 31, 2026

**Additional Key Dates:**
- Review release date: May 22, 2026
- Rebuttal deadline: June 8, 2026
- Final decision date: July 8, 2026

**Workshops:**
- Suggested submission deadline for workshop contributions: June 23, 2026

COLM 2026 will take place at the Hilton Union Square in San Francisco, USA from October 6-9, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb617cd8-8dae-4c5f-9255-7720a7f4c45f",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "0ffdef93-6ebf-4af8-8622-d4de7b8270c5",
  "sourceToolAssistantUUID": "cb617cd8-8dae-4c5f-9255-7720a7f4c45f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T20:39:32.635Z_

<details><summary>↩ Tool result · `toolu_012oy5Wy2sqg1LDVLDrwYxrr`</summary>

```text
Web search results for query: "ASE 2026 submission deadline"

Links: [{"title":"ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/ase-2026"},{"title":"ASE Call For Abstracts - The Association for Surgical Education","url":"https://www.surgicaleducation.com/call-for-abstracts/"},{"title":"Call for Papers","url":"https://www.asee.org/events/Conferences-and-Meetings/2026-Annual-Conference-Exposition/Paper-Management/Call-for-Papers"},{"title":"ASE 2026 - Research Papers - ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-research-track"},{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"ASE 2026","url":"https://ase26.hotcrp.com/"},{"title":"ASE: Automated Software Engineering 2027 2026 2025 .. ...","url":"http://www.wikicfp.com/cfp/program?id=233"},{"title":"ASE 2026 Call for Science","url":"https://www.asecho.org/education-events/scientific-sessions/call-for-science/"},{"title":"Guidelines For Abstract Preparation & Submission - ASE","url":"https://www.asescientificsessions.org/ase-call-for-abstracts-guidelines-for-abstract-preparation-and-submission/"},{"title":"Abstract FAQs - ASE","url":"https://www.asecho.org/education-events/scientific-sessions/call-for-science/abstract-faqs/"}]

Based on the search results, there are multiple organizations with "ASE 2026" conferences. Here are the submission deadlines for the major ones:

## IEEE/ACM ASE 2026 (Automated Software Engineering)

The 41st IEEE/ACM International Conference on Automated Software Engineering will take place in Munich, Germany during October 12–16, 2026. However, the deadline for registering submissions has passed for the research track.

## ASE 2026 (American Society of Echocardiography)

Abstract submission opens October 14, 2025, and the extended submission and editing deadline is 11:59 PM Eastern Time (ET) on Wednesday, January 21, 2026.

## ASE 2026 (Association for Surgical Education)

Abstract submissions are now closed with notifications of proposal acceptance sent mid-December 2025.

If you're looking for a specific ASE 2026 conference, please let me know which one and I can provide more detailed information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e97e97cb-3fb2-4214-832f-e10a106c9ae9",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "79330d34-0a4a-40c4-914f-a5e3d3001b16",
  "sourceToolAssistantUUID": "e97e97cb-3fb2-4214-832f-e10a106c9ae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T20:39:33.372Z_

<details><summary>↩ Tool result · `toolu_01DNi2KGw5wYAQgTo2aNcv4P`</summary>

```text
Web search results for query: "ACL 2026 submission deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL 2026","url":"http://aideadlines.org/conference/?id=acl26"},{"title":"ACL 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=acl26"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"LINGUIST List 37.181 Confs: 64th Annual Meeting of the Association for Computational Linguistics: Industry Track (USA)","url":"https://linguistlist.org/issues/37/181/"},{"title":"ACL 2026 in California: Dates, Deadline, Fees & Registration Steps - Conference Inc.","url":"https://conferenceinc.net/post/acl/"},{"title":"LINGUIST List 36.2630 Confs: Joint Call for Tutorial Proposals: EACL/ACL 2026 (Online)","url":"https://linguistlist.org/issues/36/2630/"}]

Based on the search results, here's what I found about ACL 2026 submission deadlines:

ACL 2026 uses ARR (ACL Rolling Review) exclusively for submissions. This means there isn't a single paper submission deadline. Instead, ARR switched from 8-week review cycles to 10-week cycles starting in May 2025.

However, for specific tracks, there are different deadlines:

**Industry Track**: The paper submission deadline for the ACL 2026 Industry Track is February 14, 2026.

For the main conference papers submitted through ARR, authors can submit to multiple ARR review cycles throughout the year. All deadlines are 11:59 pm UTC -12h (anywhere on earth).

For more specific information about exact ARR submission deadlines for papers you're planning to submit, I'd recommend checking the official ARR website or the ACL 2026 website directly, as the exact cycle dates would be listed there.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "444e69c2-5c99-46a1-ab13-923c6bea3772",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "2e6ce437-cdc9-4300-a142-d66b5338a561",
  "sourceToolAssistantUUID": "444e69c2-5c99-46a1-ab13-923c6bea3772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-11T20:39:37.027Z_

Let me get more details on a few venues where the deadlines were unclear or I need to confirm specific dates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e6ce437-cdc9-4300-a142-d66b5338a561",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRjaByCUXG77mMGStUC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4e82683-631d-4a3a-9c2b-29666f7cedda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6eyurVdEutVnnEUv9t1TZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 675,
      "cache_creation_input_tokens": 6565,
      "cache_read_input_tokens": 9485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6565,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-11T20:39:37.733Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018sM7YhWFuK8apUjTYNUXoR`</summary>

```json
{
  "query": "ASE 2026 Automated Software Engineering research track submission deadline date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4e82683-631d-4a3a-9c2b-29666f7cedda",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRjaByCUXG77mMGStUC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da1f039e-4308-4c53-b031-e352dba14aba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6eyurVdEutVnnEUv9t1TZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 675,
      "cache_creation_input_tokens": 6565,
      "cache_read_input_tokens": 9485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6565,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-11T20:39:38.370Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013XDyJuYQFXD21ruyVXZ6jF`</summary>

```json
{
  "query": "ACL 2026 ARR commitment deadline main conference papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da1f039e-4308-4c53-b031-e352dba14aba",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRjaByCUXG77mMGStUC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b36a71d-78b2-421a-8111-9b58f2e04016",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6eyurVdEutVnnEUv9t1TZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 675,
      "cache_creation_input_tokens": 6565,
      "cache_read_input_tokens": 9485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6565,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-11T20:39:38.868Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KsFDpc6r2dL2b3ViVFupUC`</summary>

```json
{
  "query": "AAAI 2027 call for papers submission deadline date August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b36a71d-78b2-421a-8111-9b58f2e04016",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRjaByCUXG77mMGStUC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63cfc2c8-7cbf-4504-b713-210ae39609f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6eyurVdEutVnnEUv9t1TZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 675,
      "cache_creation_input_tokens": 6565,
      "cache_read_input_tokens": 9485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6565,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-11T20:39:39.312Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UzJpXuZYaexuwzZhQ6ENDs`</summary>

```json
{
  "query": "FSE 2027 research papers submission deadline date 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63cfc2c8-7cbf-4504-b713-210ae39609f0",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRjaByCUXG77mMGStUC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "621f6cbf-5524-4320-9a58-632226988efb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6eyurVdEutVnnEUv9t1TZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 675,
      "cache_creation_input_tokens": 6565,
      "cache_read_input_tokens": 9485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6565,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-11T20:39:39.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AnXsZp6mXnszq6xcCgPUti`</summary>

```json
{
  "query": "ISSTA 2027 call for papers submission deadline date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "621f6cbf-5524-4320-9a58-632226988efb",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRjaByCUXG77mMGStUC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1df495a9-9047-4946-80f2-7acfc36e65f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6eyurVdEutVnnEUv9t1TZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 675,
      "cache_creation_input_tokens": 6565,
      "cache_read_input_tokens": 9485,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6565
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 675,
          "output_tokens": 284,
          "cache_read_input_tokens": 9485,
          "cache_creation_input_tokens": 6565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6565,
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

_source line 33 · 2026-05-11T20:39:42.917Z_

<details><summary>↩ Tool result · `toolu_013XDyJuYQFXD21ruyVXZ6jF`</summary>

```text
Web search results for query: "ACL 2026 ARR commitment deadline main conference papers"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"The 19th Conference of the European Chapter of the Association for Computational LinguisticsRabat, MoroccoMarch 24-29, 2026 -","url":"https://2026.eacl.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, I found information about ACL 2026 ARR commitment deadlines:

The commitment deadline for ACL 2026 is March 14, 2026. This deadline applies to authors who want to commit papers that have already been reviewed through the ACL Rolling Review (ARR) system to the ACL 2026 main conference.

Papers that have already received reviews and a meta-review from ARR from earlier cycles may be committed to ACL 2026 via the conference commitment site. Additionally, papers may be submitted to the ARR 2025 October cycle and ARR 2026 January cycle, with the submission deadline being January 5, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b36a71d-78b2-421a-8111-9b58f2e04016",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "d288b21e-a20e-496a-8d10-dae2d3555636",
  "sourceToolAssistantUUID": "4b36a71d-78b2-421a-8111-9b58f2e04016",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-11T20:39:43.180Z_

<details><summary>↩ Tool result · `toolu_01UzJpXuZYaexuwzZhQ6ENDs`</summary>

```text
Web search results for query: "FSE 2027 research papers submission deadline date 2026"

Links: [{"title":"FSE 2027 - Research Papers - FSE 2027","url":"https://conf.researchr.org/track/fse-2027/fse-2027-papers"},{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"Call for Papers | IACR Transactions on Symmetric Cryptology","url":"https://tosc.iacr.org/index.php/ToSC/Call"},{"title":"FSE: Foundations of Software Engineering 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1093"},{"title":"FSE 2026 - Research Papers - FSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/fse-2026/fse-2026-research-papers"},{"title":"Upcoming Events | FSE","url":"http://www.esec-fse.org/upcoming_events"},{"title":"The deadline for FSE 2026 Research Paper submission is ...","url":"https://www.facebook.com/fseconference/posts/the-deadline-for-fse-2026-research-paper-submission-is-approaching-in-three-week/782885284237049/"},{"title":"FSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/fse-2026"},{"title":"FSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/home/fse-2027"},{"title":"FSE 2026 - Industry Papers - FSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/fse-2026/fse-2026-industry-papers"}]

Based on the search results, I found information about FSE 2027. The official FSE 2027 Research Papers track page mentions that submission deadline details should be found "on the right panel," but the specific deadline date was not clearly visible in the search results provided.

However, I can see that in 2027, the conference will be held in Shenzhen, China.

To get the exact submission deadline for FSE 2027 research papers, you would need to visit the official FSE 2027 conference website at https://conf.researchr.org/track/fse-2027/fse-2027-papers, where the deadline information is displayed in the right panel of that page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "621f6cbf-5524-4320-9a58-632226988efb",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "f2b9e2af-89fb-418e-af65-f72dd3555120",
  "sourceToolAssistantUUID": "621f6cbf-5524-4320-9a58-632226988efb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-11T20:39:43.209Z_

<details><summary>↩ Tool result · `toolu_01AnXsZp6mXnszq6xcCgPUti`</summary>

```text
Web search results for query: "ISSTA 2027 call for papers submission deadline date"

Links: [{"title":"ISSTA 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/issta-2026"},{"title":"ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA) | ISSTA","url":"http://www.issta.org/"},{"title":"FAST '27 Call for Papers | USENIX","url":"https://www.usenix.org/conference/fast27/call-for-papers"},{"title":"ISSTA 2026","url":"https://issta2026.hotcrp.com/"},{"title":"ISSTA: International Symposium on Software Testing and Analysis 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1760"},{"title":"International Symposium on Software Testing and Analysis - Accepted Papers, Deadline, Impact Factor & Score 2026 | Research.com","url":"https://research.com/conference/international-symposium-on-software-testing-and-analysis"},{"title":"ISSTA 2023 - Technical Papers - ISSTA 2023","url":"https://2023.issta.org/track/issta-2023-technical-papers"},{"title":"ISSTA 2025 - conf.researchr.org","url":"https://conf.researchr.org/home/issta-2025"},{"title":"ISSTA 2024 - Technical Papers - ISSTA 2024","url":"https://2024.issta.org/track/issta-2024-papers"},{"title":"ISSTA Conference on X: \"📢 Call for Papers for ISSTA 2026 We invite high-quality submissions on software testing and analysis from industry and academia, incl. * Research papers * Experience papers, and * Replicability studies. 📆 29th January 2026 🖊️ https://t.co/WFeAOU3dZ0 🌐 https://t.co/lpXi9LuCQO\" / X","url":"https://x.com/issta_conf/status/2001208030235419096"}]

Based on the search results, I found information about ISSTA 2027. ISSTA 2027 will be held in Singapore with chairs Jun Sun, Dan Hao, and Jacques Klein. 

However, the search results do not contain the specific submission deadline date for ISSTA 2027's call for papers. The results show information about ISSTA 2026 (with a deadline of January 29, 2026) and earlier years, but the ISSTA 2027 call for papers details are not yet available in these search results. You may want to check the official ISSTA website (issta.org) or the conference's researchr page closer to when the call for papers is officially announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1df495a9-9047-4946-80f2-7acfc36e65f5",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "5fa4b713-d88c-4beb-844b-6695827dbb5a",
  "sourceToolAssistantUUID": "1df495a9-9047-4946-80f2-7acfc36e65f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-11T20:39:43.269Z_

<details><summary>↩ Tool result · `toolu_01KsFDpc6r2dL2b3ViVFupUC`</summary>

```text
Web search results for query: "AAAI 2027 call for papers submission deadline date August 2026"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, I found information about the AAAI 2027 submission deadline:

The Forty-first Conference on Artificial Intelligence (AAAI 2027) will be held in Montréal, Québec, Canada from February 16-23, 2027. 

Regarding the specific submission deadline date for August 2026:

The AAAI 2027 paper submission deadline is TBD (to be determined), though submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns. However, as of March 30, 2026, no deadlines have been officially announced yet.

The official call for papers information can be found at https://aaai.org/conference/aaai/aaai-27/, but based on the current search results, the exact submission deadline date has not yet been publicly announced by the conference organizers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63cfc2c8-7cbf-4504-b713-210ae39609f0",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "039e1fd6-e87f-472a-886c-82d80389b58b",
  "sourceToolAssistantUUID": "63cfc2c8-7cbf-4504-b713-210ae39609f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-11T20:39:44.131Z_

<details><summary>↩ Tool result · `toolu_018sM7YhWFuK8apUjTYNUXoR`</summary>

```text
Web search results for query: "ASE 2026 Automated Software Engineering research track submission deadline date"

Links: [{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/ase-2026"},{"title":"ASE 2026","url":"https://ase26.hotcrp.com/"},{"title":"ASE: Automated Software Engineering 2027 2026 2025 .. ...","url":"http://www.wikicfp.com/cfp/program?id=233"},{"title":"ASE conference series - ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/series/ase"},{"title":"ASE 2026 - Research Papers - ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-research-track"},{"title":"Collections and calls for papers | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/journal/10515/collections"},{"title":"Home | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/journal/10515"},{"title":"ASE 2026 - Tools and Datasets - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-tools-and-data-sets"},{"title":"Automated Software Engineering Homepage | The Website of the Automated Software Engineering Conference","url":"https://ase-conferences.org/"}]

The search results show information about ASE 2026 but don't clearly display the research track submission deadline date. Let me search for more specific information.

Links: [{"title":"ASE Call For Abstracts - The Association for Surgical Education","url":"https://www.surgicaleducation.com/call-for-abstracts/"},{"title":"ASE 2026 - Research Papers - ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-research-track"},{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/ase-2026"},{"title":"Important Deadlines","url":"https://www.asee.org/events/Conferences-and-Meetings/2026-Annual-Conference-Exposition/Important-Deadlines"},{"title":"ASE 2026 - Tools and Datasets - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-tools-and-data-sets"},{"title":"Deadlines - IE 2026 - ASE","url":"https://www.conferenceie.ase.ro/index.php/deadlines/"},{"title":"ASE 2026","url":"https://ase26.hotcrp.com/"},{"title":"ASE 2026 - Industry Showcase - ASE 2026","url":"https://conf.researchr.org/track/ase-2026/ase-2026-industry-showcase"},{"title":"conf.researchr.org conference management system -","url":"https://conf.researchr.org/submissiondates"}]

Perfect! I found the information in the search results.

The ASE 2026 Research Paper Track submission deadline is March 26, 2026 at 23:59.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da1f039e-4308-4c53-b031-e352dba14aba",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "49109357-948a-465e-a653-5408eab32587",
  "sourceToolAssistantUUID": "da1f039e-4308-4c53-b031-e352dba14aba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-11T20:39:46.865Z_

Let me try to get the EMNLP 2026 ARR deadline details more precisely and check a couple more items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49109357-948a-465e-a653-5408eab32587",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRkNBSBrTNf8fjSAG8d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00c4e3df-2755-45f6-aa21-d23b0c9236ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Lcmz2AG5bSi3EFCziVDJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2847,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 16050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 39 · 2026-05-11T20:39:47.684Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WFnFyVN9HJFCXtqXx6rJwn`</summary>

```json
{
  "query": "EMNLP 2026 direct submission deadline ARR May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00c4e3df-2755-45f6-aa21-d23b0c9236ca",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRkNBSBrTNf8fjSAG8d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4369d801-0965-483e-843d-eb7185e34ed0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Lcmz2AG5bSi3EFCziVDJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2847,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 16050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 40 · 2026-05-11T20:39:47.886Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ro4N95YqRwYWN4urggLieq`</summary>

```json
{
  "query": "NeurIPS 2026 datasets benchmarks track submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4369d801-0965-483e-843d-eb7185e34ed0",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRkNBSBrTNf8fjSAG8d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51b76f1c-ab21-4291-862f-2c516354faf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Lcmz2AG5bSi3EFCziVDJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2847,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 16050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 41 · 2026-05-11T20:39:48.155Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Efvy35u3SUBaWiKNNHg9Vx`</summary>

```json
{
  "query": "ICLR 2027 call for papers deadline announcement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51b76f1c-ab21-4291-862f-2c516354faf9",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRkNBSBrTNf8fjSAG8d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e701e1a7-66d7-43f7-a5a3-700cb8a77c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Lcmz2AG5bSi3EFCziVDJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2847,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 16050,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2847,
          "output_tokens": 193,
          "cache_read_input_tokens": 16050,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
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

_source line 42 · 2026-05-11T20:39:51.927Z_

<details><summary>↩ Tool result · `toolu_01Efvy35u3SUBaWiKNNHg9Vx`</summary>

```text
Web search results for query: "ICLR 2027 call for papers deadline announcement"

Links: [{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"}]

Based on the search results, I found that the official ICLR website does not yet have information about ICLR 2027 posted. The Fourteenth annual conference (ICLR 2026) is the most recent one with announced details, with location and dates for the fifteenth annual conference (ICLR 2027) still to be announced.

The search results indicate that while there are general conferences on learning representations scheduled for August 2027 (like the one in Sydney), the official ICLR 2027 call for papers deadline has not yet been announced. For the most current information about ICLR 2027's call for papers and submission deadlines, I recommend checking the official ICLR website at iclr.cc directly or monitoring their OpenReview page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e701e1a7-66d7-43f7-a5a3-700cb8a77c41",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "e3cba213-2e52-4673-afb4-62ecd2c55d78",
  "sourceToolAssistantUUID": "e701e1a7-66d7-43f7-a5a3-700cb8a77c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-11T20:39:52.321Z_

<details><summary>↩ Tool result · `toolu_01Ro4N95YqRwYWN4urggLieq`</summary>

```text
Web search results for query: "NeurIPS 2026 datasets benchmarks track submission deadline"

Links: [{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026 Evaluations & Datasets FAQ","url":"https://neurips.cc/Conferences/2026/EvaluationsDatasetsFAQ"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"Call For Datasets & Benchmarks","url":"https://neurips.cc/Conferences/2023/CallForDatasetsBenchmarks"},{"title":"Introducing the Evaluations & Datasets Track at NeurIPS 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/03/23/introducing-the-evaluations-datasets-track-at-neurips-2026/"},{"title":"Datasets and Benchmarks Track: Call for Papers – KDD 2026","url":"https://kdd2026.kdd.org/datasets-and-benchmarks-track-call-for-papers/"},{"title":"NeurIPS 2025 Datasets & Benchmarks Track Call for Papers","url":"https://neurips.cc/Conferences/2025/CallForDatasetsBenchmarks"},{"title":"NeurIPS 2026 Evaluations and Datasets Track | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FEvaluations_and_Datasets_Track"},{"title":"NeurIPS Newsletter – April 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/"}]

Based on the search results, here's the information about NeurIPS 2026 Evaluations & Datasets Track submission deadlines:

The abstract submission deadline is May 4, 2026 (AoE), and the full paper submission deadline (including all supplementary materials) is May 6, 2026 (AoE). The submission portal opens on April 15, 2026 (at the same time as the main track).

For the ED track, the full paper — including all required materials — must be submitted by May 6, 2026 (AOE), and datasets and code are not considered supplementary materials.

It's worth noting that the Datasets & Benchmarks Track at NeurIPS 2026 has been officially renamed the Evaluations & Datasets (ED) Track, reflecting an expanded scope that now positions evaluation as a scientific object of study.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51b76f1c-ab21-4291-862f-2c516354faf9",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "33aae6d0-f571-4a2a-8f74-4cf4d0416867",
  "sourceToolAssistantUUID": "51b76f1c-ab21-4291-862f-2c516354faf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-11T20:39:53.075Z_

<details><summary>↩ Tool result · `toolu_01WFnFyVN9HJFCXtqXx6rJwn`</summary>

```text
Web search results for query: "EMNLP 2026 direct submission deadline ARR May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"}]

Based on the search results, here's the key information about EMNLP 2026 direct submission deadline through ARR in May 2026:

## Key Deadlines

The ARR submission deadline is May 25, 2026.

## Important Submission Details

For the May 2026 ARR cycle, there's a specific policy for EMNLP 2026:

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026—ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## Post-Submission Deadline

After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.

## Commitment and Acceptance Timeline

The EMNLP commitment deadline is August 2, 2026, with notification of acceptance on August 20, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4369d801-0965-483e-843d-eb7185e34ed0",
  "isSidechain": true,
  "promptId": "d582a416-cff8-421b-b114-b9bdd6cbe118",
  "agentId": "a1d4f585bf67d390d",
  "type": "user",
  "uuid": "4d0f3524-c3a1-4482-bcae-2e45582788c4",
  "sourceToolAssistantUUID": "4369d801-0965-483e-843d-eb7185e34ed0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-11T20:40:20.655Z_

Here is a comprehensive summary of the submission deadlines for all 10 venues, filtered against the cutoff date of 2026-05-11.

---

## Venues with Deadlines AFTER 2026-05-11 (Still Open)

### 1. EMNLP 2026
- **ARR Submission Deadline:** May 25, 2026
- **Commitment Deadline:** August 2, 2026
- **Conference:** October 24-29, 2026, Budapest, Hungary
- Note: Authors must select EMNLP 2026 as target conference at submission time (binding choice since the May ARR cycle is shared with AACL).

### 2. AAAI 2027
- **Submission Deadline:** TBD (expected July-August 2026 based on historical patterns)
- **Conference:** February 16-23, 2027, Montreal, Quebec, Canada
- The call for papers has not yet been officially released.

### 3. ISSTA 2027
- **Submission Deadline:** TBD (not yet announced)
- **Conference:** Singapore (exact dates TBD)
- Chairs: Jun Sun, Dan Hao, Jacques Klein. Based on past years, the deadline is likely late 2026 or early 2027.

### 4. FSE 2027
- **Submission Deadline:** TBD (not yet announced)
- **Conference:** July 12-16, 2027, Shenzhen, China
- Check the official page for updates: https://conf.researchr.org/track/fse-2027/fse-2027-papers

### 5. ICLR 2027
- **Submission Deadline:** TBD (not yet announced)
- **Conference:** Location and dates TBD
- Based on historical patterns (ICLR 2026 deadline was around October 2025), the submission deadline is expected around September-October 2026.

---

## Venues with Deadlines BEFORE 2026-05-11 (Already Passed)

### 6. NeurIPS 2026
- **Abstract Deadline:** May 4, 2026 (AoE) -- PASSED
- **Full Paper Deadline:** May 6, 2026 (AoE) -- PASSED
- **Conference:** December 6-12, 2026

### 7. ICML 2026
- **Submission Deadline:** January 28, 2026 -- PASSED
- **Conference:** July 6-11, 2026, Seoul (Coex Convention Center)

### 8. ACL 2026
- **ARR Commitment Deadline:** March 14, 2026 -- PASSED
- **Last eligible ARR submission cycle:** January 5, 2026 -- PASSED
- **Conference:** 2026 (location TBD)

### 9. COLM 2026
- **Abstract Deadline:** March 26, 2026 -- PASSED
- **Full Paper Deadline:** March 31, 2026 -- PASSED
- **Conference:** October 6-9, 2026, San Francisco, USA

### 10. ASE 2026 (Automated Software Engineering)
- **Submission Deadline:** March 26, 2026 -- PASSED
- **Conference:** October 12-16, 2026, Munich, Germany

---

## Summary Table

| Venue | Deadline | Status (as of 2026-05-11) |
|-------|----------|--------------------------|
| EMNLP 2026 | May 25, 2026 | **OPEN** |
| AAAI 2027 | TBD (~Jul-Aug 2026) | **OPEN (expected)** |
| ISSTA 2027 | TBD | **OPEN (expected)** |
| FSE 2027 | TBD | **OPEN (expected)** |
| ICLR 2027 | TBD (~Sep-Oct 2026) | **OPEN (expected)** |
| NeurIPS 2026 | May 6, 2026 | PASSED |
| ICML 2026 | Jan 28, 2026 | PASSED |
| ACL 2026 | Mar 14, 2026 (commit) | PASSED |
| COLM 2026 | Mar 31, 2026 | PASSED |
| ASE 2026 | Mar 26, 2026 | PASSED |

**Bottom line:** The only venue with a confirmed and still-open deadline is **EMNLP 2026 (May 25, 2026)**. Four other venues (AAAI 2027, ISSTA 2027, FSE 2027, ICLR 2027) have not yet announced deadlines but are expected to have them after 2026-05-11. The remaining five venues have deadlines that have already passed.

Sources:
- [NeurIPS 2026 Dates and Deadlines](https://neurips.cc/Conferences/2026/Dates)
- [ICLR 2026 Conference](https://iclr.cc/)
- [EMNLP 2026](https://2026.emnlp.org/)
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [AAAI Conference on Artificial Intelligence](https://aaai.org/conference/aaai/)
- [AAAI 2027 Deadline Tracker](https://www.getpaperpilot.com/deadlines/aaai-2027.html)
- [ASE 2026 - conf.researchr.org](https://conf.researchr.org/home/ase-2026)
- [ASE 2026 Research Papers Track](https://conf.researchr.org/track/ase-2026/ase-2026-research-track)
- [ISSTA - Official Website](http://www.issta.org/)
- [FSE 2027 - conf.researchr.org](https://conf.researchr.org/home/fse-2027)
- [FSE 2027 Research Papers](https://conf.researchr.org/track/fse-2027/fse-2027-papers)
- [ICML 2026 Dates and Deadlines](https://icml.cc/Conferences/2026/Dates)
- [ACL 2026 Main Conference Papers](https://2026.aclweb.org/calls/main_conference_papers/)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)
- [COLM 2026 Key Dates](https://colmweb.org/dates.html)
- [COLM 2026 Call for Papers](https://colmweb.org/cfp.html)
- [SE Deadlines](https://se-deadlines.github.io/)
- [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d0f3524-c3a1-4482-bcae-2e45582788c4",
  "isSidechain": true,
  "agentId": "a1d4f585bf67d390d",
  "requestId": "req_011CawRm2U3oDr37Y4eaGQmt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c49db15-f6f5-4525-8824-46d4470bd1cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5392b626-6c26-4ec2-bcc8-4f43aa7bd832",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dth9LEuuUBPwQt6nk3ynKu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1330,
      "cache_creation_input_tokens": 4083,
      "cache_read_input_tokens": 17960,
      "output_tokens": 1726,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1330,
          "output_tokens": 1726,
          "cache_read_input_tokens": 17960,
          "cache_creation_input_tokens": 4083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4083,
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
