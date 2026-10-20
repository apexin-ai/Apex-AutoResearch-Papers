# Research conversation: I'm researching feasibility for a project on self-supervised affordance grounding using instruction invariance in Vision

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a359a0270b1b532f7.jsonl`
- **Structured JSON:** [`3495e7aba8a1f0417009.json`](../../sessions/34/3495e7aba8a1f0417009.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-18T18:44:52.227Z_

I'm researching feasibility for a project on self-supervised affordance grounding using instruction invariance in Vision-Language-Action models. Search for:

1. WebSearch: "github.com affordance grounding VLA implementation"
2. WebSearch: "github.com OpenVLA affordance"
3. WebSearch: "github.com UAD affordance distillation code"
4. WebSearch: "github.com AGD20K affordance grounding"
5. WebSearch: "huggingface.co/datasets affordance grounding"
6. WebSearch: "paperswithcode.com affordance detection datasets"
7. WebSearch: "paperswithcode.com affordance grounding benchmark"
8. WebSearch: "VLA training cost GPU hours A100 2025 2026"
9. WebSearch: "OpenVLA training compute requirements"
10. WebSearch: "affordance detection benchmark SOTA results 2026"

For each search, report:
- What repositories/datasets/benchmarks exist
- Whether code is publicly available
- Specific numbers: training cost, dataset sizes, baseline performance metrics
- Any practical issues noted (data quality, compute requirements, etc.)

This is for grounding resource estimates in real data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "936c487d-ae34-413f-a49b-5146a3cdfd40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T18:44:52.231Z_

```json
{
  "parentUuid": "936c487d-ae34-413f-a49b-5146a3cdfd40",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
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
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "68da9a12-9d1d-43bc-a20f-6083a0ab19ca",
  "timestamp": "2026-05-18T18:44:52.231Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T18:44:54.754Z_



I'll conduct all 10 searches in parallel to gather the information you need. Let me first load the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68da9a12-9d1d-43bc-a20f-6083a0ab19ca",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXekKHM1RsUP6Tt2ZqM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d3e0bed-1d60-4895-a00e-1589473aed7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01St9TH1uoB4HryskMPpXXrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 804,
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

_source line 4 · 2026-05-18T18:44:55.215Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CUd6f4ANTv8xAKw4rRK3gZ`</summary>

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
  "parentUuid": "5d3e0bed-1d60-4895-a00e-1589473aed7f",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXekKHM1RsUP6Tt2ZqM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1b1b5a0-d6fb-4799-b95f-16dc26b86765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01St9TH1uoB4HryskMPpXXrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 7304,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 804
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 804,
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

_source line 5 · 2026-05-18T18:44:55.218Z_

<details><summary>↩ Tool result · `toolu_01CUd6f4ANTv8xAKw4rRK3gZ`</summary>

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
  "parentUuid": "b1b1b5a0-d6fb-4799-b95f-16dc26b86765",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "545973a1-be44-4268-8afa-46408579c062",
  "sourceToolAssistantUUID": "b1b1b5a0-d6fb-4799-b95f-16dc26b86765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T18:45:01.012Z_



Now let me run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "545973a1-be44-4268-8afa-46408579c062",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12d61112-857c-4594-85d3-4d88bba0d2c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 7 · 2026-05-18T18:45:01.651Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CeVHqQtwFpTpUGLqmHCy92`</summary>

```json
{
  "query": "github.com affordance grounding VLA implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12d61112-857c-4594-85d3-4d88bba0d2c1",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9831a69-208a-4514-a647-e2688604c440",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 8 · 2026-05-18T18:45:02.103Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TwGQu6gjtntm3SzxETgFVe`</summary>

```json
{
  "query": "github.com OpenVLA affordance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9831a69-208a-4514-a647-e2688604c440",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4ea59c7-81da-4206-a564-ed6915d65cf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 9 · 2026-05-18T18:45:02.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RDtiBsnGYbkS9jydSjCY5d`</summary>

```json
{
  "query": "github.com UAD affordance distillation code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4ea59c7-81da-4206-a564-ed6915d65cf8",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbd6ab0a-9aab-4db2-a433-6b9e0776f3c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 10 · 2026-05-18T18:45:03.439Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NHTUukASqhMvvvnmofj35e`</summary>

```json
{
  "query": "github.com AGD20K affordance grounding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbd6ab0a-9aab-4db2-a433-6b9e0776f3c3",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ed120da-0064-495d-a949-d267e78701aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 11 · 2026-05-18T18:45:03.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FkEJk5YEmiTSCEGHTzygBU`</summary>

```json
{
  "query": "huggingface.co/datasets affordance grounding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ed120da-0064-495d-a949-d267e78701aa",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "263aea75-d75f-4067-98cd-34ba0a76382b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 12 · 2026-05-18T18:45:03.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AjZ7R4fienD23ETjMj5hnd`</summary>

```json
{
  "query": "paperswithcode.com affordance detection datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "263aea75-d75f-4067-98cd-34ba0a76382b",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2344c1f9-f2a3-4956-b939-ef3eeb14e1ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 13 · 2026-05-18T18:45:04.318Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A9V2pDxqKTeFgagYkMKx8U`</summary>

```json
{
  "query": "paperswithcode.com affordance grounding benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2344c1f9-f2a3-4956-b939-ef3eeb14e1ef",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86ed5e68-4201-4f6b-94be-b2fa158117bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 14 · 2026-05-18T18:45:05.271Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NK5krkGQX5BJv5GWPvpC8v`</summary>

```json
{
  "query": "VLA training cost GPU hours A100 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86ed5e68-4201-4f6b-94be-b2fa158117bd",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "faead405-8f2d-40d7-b391-03b872de5a22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 15 · 2026-05-18T18:45:05.814Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SN4x4UagXGyMDFsfCbnyqw`</summary>

```json
{
  "query": "OpenVLA training compute requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faead405-8f2d-40d7-b391-03b872de5a22",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6f48d99-31d4-4439-9b9a-d0a850b7cb1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 16 · 2026-05-18T18:45:06.255Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015UYmGd29eB91uoBfpxsK6P`</summary>

```json
{
  "query": "affordance detection benchmark SOTA results 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6f48d99-31d4-4439-9b9a-d0a850b7cb1d",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXey6jGDEMcZmqqxQjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c749bd2a-aff5-4505-9330-14beae47c450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtxKJB7JWbGwokp9j29WoJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8108,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 474,
          "cache_read_input_tokens": 8108,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1421,
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

_source line 17 · 2026-05-18T18:45:08.434Z_

<details><summary>↩ Tool result · `toolu_01RDtiBsnGYbkS9jydSjCY5d`</summary>

```text
Web search results for query: "github.com UAD affordance distillation code"

Links: [{"title":"Github","url":"https://unsup-affordance.github.io/uad.pdf"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=an953WOpo2"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/html/2506.09284v1"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://www.researchgate.net/publication/392597063_UAD_Unsupervised_Affordance_Distillation_for_Generalization_in_Robotic_Manipulation"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | Request PDF","url":"https://www.researchgate.net/publication/395210639_UAD_Unsupervised_Affordance_Distillation_for_Generalization_in_Robotic_Manipulation"},{"title":"UAD: Unsupervised Affordance Distillation","url":"https://openreview.net/pdf?id=an953WOpo2"},{"title":"[2506.09284] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/abs/2506.09284"},{"title":"GitHub - hq-King/Awesome-Affordance-Learning · GitHub","url":"https://github.com/hq-King/Awesome-Affordance-Learning"},{"title":"UAD","url":"https://gpt-affordance.github.io/"}]

Based on the search results, I found information about UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation.

UAD is a method for distilling affordance knowledge from foundation models into a task-conditioned affordance model without any manual annotations. By leveraging the complementary strengths of large vision models and vision-language models, UAD automatically annotates a large-scale dataset with detailed pairs, and trains a lightweight task-conditioned decoder atop frozen features that exhibits notable generalization to in-the-wild robotic scenes.

The project has a website at unsup-affordance.github.io, which should have links to the code repository. The work was authored by Yihe Tang and others, and was published at ICRA 2025.

While the search results reference the project's GitHub and website, they don't provide a direct GitHub repository URL in the snippets shown. You may want to visit the project website (unsup-affordance.github.io) to find the direct link to the code repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbd6ab0a-9aab-4db2-a433-6b9e0776f3c3",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "c485f24b-3f1c-4728-a0f3-e15437544eb5",
  "sourceToolAssistantUUID": "bbd6ab0a-9aab-4db2-a433-6b9e0776f3c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T18:45:09.268Z_

<details><summary>↩ Tool result · `toolu_01FkEJk5YEmiTSCEGHTzygBU`</summary>

```text
Web search results for query: "huggingface.co/datasets affordance grounding"

Links: [{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Affordance+grounding"},{"title":"Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale","url":"https://arxiv.org/html/2506.12009v1"},{"title":"Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale","url":"https://arxiv.org/pdf/2506.12009"},{"title":"junhalee/Mosaic3D · Datasets at Hugging Face","url":"https://huggingface.co/datasets/junhalee/Mosaic3D"},{"title":"qualifire/grounding-benchmark · Datasets at Hugging Face","url":"https://huggingface.co/datasets/qualifire/grounding-benchmark"},{"title":"Learning Affordance Grounding from Exocentric Images","url":"https://arxiv.org/pdf/2203.09905"},{"title":"google/FACTS-grounding-public · Datasets at Hugging Face","url":"https://huggingface.co/datasets/google/FACTS-grounding-public"},{"title":"WorldAfford: Affordance Grounding based on Natural Language Instructions","url":"https://arxiv.org/pdf/2405.12461"}]

Based on the search results, here's what I found:

## Affordance Grounding on Hugging Face

Affordance grounding refers to the task of finding the area of an object with which one can interact.

### Affogato Dataset

The most prominent affordance grounding dataset on Hugging Face is **Affogato**. It is a large-scale benchmark comprising 150K instances, annotated with open-vocabulary text descriptions and corresponding 3D affordance heatmaps across a diverse set of objects and interactions. It is the largest 3D affordance grounding dataset to date.

The dataset is publicly available at: https://huggingface.co/datasets/project-affogato/affogato

Affordance grounding—localizing object regions based on natural language descriptions of interactions—is a critical challenge for enabling intelligent agents to understand and interact with their environments.

### Other Related Datasets

Additionally, there's Mosaic3D, a large-scale dataset designed for open-vocabulary segmentation and affordance grounding in 3D scenes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "263aea75-d75f-4067-98cd-34ba0a76382b",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "87cab4b4-8617-4254-9dcb-ceb18c700743",
  "sourceToolAssistantUUID": "263aea75-d75f-4067-98cd-34ba0a76382b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T18:45:09.886Z_

<details><summary>↩ Tool result · `toolu_01NHTUukASqhMvvvnmofj35e`</summary>

```text
Web search results for query: "github.com AGD20K affordance grounding"

Links: [{"title":"Learning Affordance Grounding from Exocentric Images Hongchen Luo1‡* Wei Zhai1‡","url":"https://arxiv.org/pdf/2203.09905"},{"title":"GitHub - lhc1224/Cross-View-AG: Official PyTorch Implementation of Learning Affordance Grounding from Exocentric Images, CVPR 2022","url":"https://github.com/lhc1224/Cross-View-AG"},{"title":"Learning Affordance Grounding from Exocentric Images Hongchen Luo1‡* Wei Zhai1‡","url":"https://openaccess.thecvf.com/content/CVPR2022/papers/Luo_Learning_Affordance_Grounding_From_Exocentric_Images_CVPR_2022_paper.pdf"},{"title":"Grounded Affordance from Exocentric View","url":"https://arxiv.org/pdf/2208.13196"},{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://arxiv.org/pdf/2401.06341"},{"title":"Weakly-Supervised Affordance Grounding Guided by Part-Level Semantic Priors","url":"https://arxiv.org/html/2505.24103v1"},{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://jasonqsy.github.io/AffordanceLLM/"},{"title":"Resource-Efficient Affordance Grounding with Complementary Depth","url":"https://arxiv.org/pdf/2503.02600"},{"title":"Cross-View-AG/README.md at main · lhc1224/Cross-View-AG","url":"https://github.com/lhc1224/Cross-View-AG/blob/main/README.md"},{"title":"AffoGato: Learning Open-Vocabulary Affordance Grounding with Foundation Models","url":"https://junha-l.github.io/affogato/"}]

Based on the search results, here's what I found about AGD20K and affordance grounding:

## AGD20K Dataset

AGD20K is an affordance grounding dataset constructed by collecting and labeling over 20K images from 36 affordance categories. Affordance grounding aims to locate an object's region of "action possibilities".

## GitHub Repository

The code is available at github.com/lhc1224/Cross-View-AG, which is the official PyTorch implementation of a paper presented at CVPR 2022 on "Learning Affordance Grounding from Exocentric Images."

## Research Applications

The AGD20K dataset has become a benchmark used in multiple research projects. Under the AGD20K benchmark, various methods have demonstrated performance gains, and it is noted as the only large-scale affordance grounding dataset with accurate action and object labels. Recent methods continue to use this dataset to evaluate affordance grounding algorithms, including approaches that incorporate vision-language models and depth information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ed120da-0064-495d-a949-d267e78701aa",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "db1449d7-3439-461d-8e93-c57540db6ffc",
  "sourceToolAssistantUUID": "8ed120da-0064-495d-a949-d267e78701aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T18:45:09.904Z_

<details><summary>↩ Tool result · `toolu_01AjZ7R4fienD23ETjMj5hnd`</summary>

```text
Web search results for query: "paperswithcode.com affordance detection datasets"

Links: [{"title":"Papers with Code - Affordance Detection","url":"https://paperswithcode.com/task/affordance-detection/codeless"},{"title":"Papers with Code - Affordance Recognition","url":"https://paperswithcode.com/task/affordance-recognition"},{"title":"Papers with Code - ADE-Affordance Dataset","url":"https://paperswithcode.com/dataset/ade-affordance"},{"title":"Visual Affordance Learning Dataset | Papers With Code","url":"https://paperswithcode.com/dataset/visual-affordance-learning"},{"title":"Machine Learning Datasets - Affordance Detection","url":"https://paperswithcode.com/datasets?q=Walker2d&task=affordance-detection&mod=3d"},{"title":"GitHub - Nir3usHaHaHa/Papers-with-Code: https://paperswithcode.com/ · GitHub","url":"https://github.com/Nir3usHaHaHa/Papers-with-Code"},{"title":"One-Shot Affordance Detection","url":"https://arxiv.org/pdf/2106.14747"},{"title":"One-Shot Object Affordance Detection in the Wild","url":"https://arxiv.org/pdf/2108.03658"},{"title":"Phrase-Based Affordance Detection via Cyclic Bilateral Interaction","url":"https://arxiv.org/pdf/2202.12076"}]

Based on the search results from Papers with Code, here are the main affordance detection datasets available:

## Key Affordance Detection Datasets

**3D AffordanceNet** - A dataset of 23k shapes containing 56,307 affordance annotations for 22,949 shapes covering 18 affordance classes and 23 semantic object categories.

**ADE-Affordance** - A dataset built upon ADE20k with annotations enabling rich visual reasoning.

**Visual Affordance Learning Dataset** - A large-scale multi-view RGBD dataset with a benchmark of 47,210 RGBD images from 37 object categories, annotated with 15 visual affordance categories and 35 cluttered/complex scenes.

**Purpose-driven Affordance Dataset v2 (PADv2)** - A large-scale dataset with 30k images from 39 affordance and 103 object categories, featuring complex scenes and rich annotations for benchmarking affordance detection methods.

These datasets are commonly used benchmarks on Papers with Code for affordance detection research, with varying scales and annotation types ranging from 2D segmentation masks to 3D shape data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2344c1f9-f2a3-4956-b939-ef3eeb14e1ef",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "3dadeca0-e526-4c41-b4ee-402693cccdba",
  "sourceToolAssistantUUID": "2344c1f9-f2a3-4956-b939-ef3eeb14e1ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T18:45:11.123Z_

<details><summary>↩ Tool result · `toolu_01A9V2pDxqKTeFgagYkMKx8U`</summary>

```text
Web search results for query: "paperswithcode.com affordance grounding benchmark"

Links: [{"title":"Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions","url":"https://arxiv.org/html/2504.04744v1"},{"title":"Papers with Code - Learning 2D Invariant Affordance Knowledge for 3D Affordance Grounding","url":"https://paperswithcode.com/paper/learning-2d-invariant-affordance-knowledge"},{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://arxiv.org/pdf/2401.06341"},{"title":"Papers with Code - Paper tables with annotated results for WorldAfford: Affordance Grounding based on Natural Language Instructions","url":"https://paperswithcode.com/paper/worldafford-affordance-grounding-based-on/review/"},{"title":"Affordance Grounding from Demonstration Video to Target Image","url":"https://arxiv.org/pdf/2303.14644"},{"title":"Learning Affordance Grounding from Exocentric Images","url":"https://arxiv.org/pdf/2203.09905"},{"title":"Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale","url":"https://arxiv.org/pdf/2506.12009"},{"title":"LOCATE: Localize and Transfer Object Parts for Weakly Supervised   Affordance Grounding","url":"https://arxiv.org/pdf/2303.09665"},{"title":"WorldAfford: Affordance Grounding based on Natural Language Instructions","url":"https://arxiv.org/pdf/2405.12461"},{"title":"Affordance-R1: Reinforcement Learning for Generalizable Affordance Reasoning in Multimodal Large Language Model","url":"https://arxiv.org/pdf/2508.06206"}]

Based on the search results, here's what I found regarding affordance grounding benchmarks on Papers with Code:

The search reveals several key affordance grounding benchmarks and datasets:

1. **AGD20K**: An affordance grounding dataset constructed by collecting and labeling over 20K images from 36 affordance categories.

2. **Affogato**: A large-scale benchmark comprising 150K instances, annotated with open-vocabulary text descriptions and corresponding 3D affordance heatmaps across a diverse set of objects and interactions.

3. **LLMaFF**: A dataset containing 550 test images with natural language instructions and manually labeled affordance maps.

4. **AGPIL**: Composed of 30972 point-image-text pairs, covering 17 affordance categories and 23 object classes.

5. **Video-to-Image Affordance Benchmarks**: Three video-to-image affordance benchmarks, namely OPRA, EPIC-Hotspot, and AssistQ.

These benchmarks represent different approaches to affordance grounding, ranging from 2D image analysis to 3D object understanding, and from simple action labels to complex natural language instructions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86ed5e68-4201-4f6b-94be-b2fa158117bd",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "ec1cdaff-ec8e-4fd3-884d-a75f9335d609",
  "sourceToolAssistantUUID": "86ed5e68-4201-4f6b-94be-b2fa158117bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T18:45:12.808Z_

<details><summary>↩ Tool result · `toolu_015UYmGd29eB91uoBfpxsK6P`</summary>

```text
Web search results for query: "affordance detection benchmark SOTA results 2026"

Links: [{"title":"RoboAfford: A Dataset and Benchmark for Enhancing Object and Spatial Affordance Learning in Robot Manipulation | Request PDF","url":"https://www.researchgate.net/publication/396941670_RoboAfford_A_Dataset_and_Benchmark_for_Enhancing_Object_and_Spatial_Affordance_Learning_in_Robot_Manipulation"},{"title":"One-Shot Affordance Detection","url":"https://arxiv.org/pdf/2106.14747"},{"title":"One-Shot Object Affordance Detection in the Wild","url":"https://arxiv.org/pdf/2108.03658"},{"title":"AffordanceSAM: Segment Anything Once More in Affordance Grounding","url":"https://arxiv.org/pdf/2504.15650"},{"title":"AffordanceNet: An End-to-End Deep Learning Approach for Object   Affordance Detection","url":"https://arxiv.org/pdf/1709.07326"},{"title":"Capturing Fine-Grained Alignments Improves 3D Affordance Detection","url":"https://arxiv.org/pdf/2506.19312"},{"title":"AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"}]

Based on the search results, here are some key findings on affordance detection benchmark SOTA results:

**Recent State-of-the-Art Results:**

AffordanceSAM achieves state-of-the-art performance under the AGD20K benchmark, and shows evidence to generalize well to novel actions and objects. This paper was published in April 2026 (arxiv ID 2504.15650).

**3D Point Cloud Affordance Detection:**

Existing methods often fail to adequately capture fine-grained alignment, resulting in accuracy below 50% on standard benchmarks. A recent paper (arxiv ID 2506.19312) proposes LM-AD, a method that leverages a pretrained language model to improve fine-grained alignment for 3D point cloud affordance detection.

**Affordance Detection Benchmarks:**

The Purpose-driven Affordance Dataset v2 (PADv2) contains 30k images from 39 affordance and 103 object categories, and can be used as a test bed to benchmark affordance detection methods.

The search results show recent advances in affordance detection with methods like AffordanceSAM achieving SOTA performance in 2026, particularly for affordance grounding tasks on the AGD20K benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c749bd2a-aff5-4505-9330-14beae47c450",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "d558753e-309a-4aec-aff5-556f09604b0e",
  "sourceToolAssistantUUID": "c749bd2a-aff5-4505-9330-14beae47c450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T18:45:13.354Z_

<details><summary>↩ Tool result · `toolu_01NK5krkGQX5BJv5GWPvpC8v`</summary>

```text
Web search results for query: "VLA training cost GPU hours A100 2025 2026"

Links: [{"title":"NVIDIA A100 GPU Price in 2026: Cost Per Hour, Cloud ...","url":"https://jarvislabs.ai/blog/a100-price"},{"title":"A100 Cloud Pricing: Compare 38+ Providers (2026)","url":"https://getdeploying.com/gpus/nvidia-a100"},{"title":"GPU Cloud Pricing 2026: H100 from $1.03/hr, B200 from $2.12/hr (15+ providers) | Spheron Blog","url":"https://www.spheron.network/blog/gpu-cloud-pricing-comparison-2026/"},{"title":"How much does an NVIDIA A100 GPU cost? | Blog — Northflank","url":"https://northflank.com/blog/nvidia-a100-gpu-cost"},{"title":"H100 Cloud Pricing: Compare 41+ Providers (2026)","url":"https://getdeploying.com/gpus/nvidia-h100"},{"title":"NVIDIA A100 GPU: $10K Workhorse That Still Trains AI in 2026","url":"https://www.aitooldiscovery.com/ai-infra/nvidia-a100-specs-price"},{"title":"GPU Cloud Pricing 2026: H100 From $2.21/hr — AWS vs Azure vs GCP Compared","url":"https://spendark.com/blog/machine-learning-cloud-cost/"},{"title":"NVIDIA A100 Pricing (May 2026): Cheapest On-demand GPU Instances","url":"https://www.thundercompute.com/blog/nvidia-a100-pricing"},{"title":"Scaling VLA Model Training on a Budget: Lessons From 100+ Fine-Tunes | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/scaling-vla-training-on-a-budget"},{"title":"Cloud GPU Pricing Comparison India [2026]: A100, H200 & More","url":"https://acecloud.ai/blog/cloud-gpu-pricing-comparison/"}]

Based on the search results, here's what I found regarding VLA (Vision Language Action) model training costs on A100 GPUs in 2025-2026:

## A100 GPU Hourly Costs (2025-2026)

Cloud rental ranges from $1.49 to $3.43 per GPU hour (March 2026). More specifically, on-demand pricing has decreased by about 13% since May 2025, dropping from $2.39 to $2.09/hr per GPU.

A100 80G SXM4 on-demand is at $1.07/hr (as of Q2 2026 from a different provider).

## VLA Training Specifics

For Vision Language Action model fine-tuning, the results provide practical guidance: The 7B-parameter base means you will want at least a 40GB A100 or, ideally, an 80GB H100 for comfortable batch sizes with LoRA.

QLoRA is what makes OpenVLA fine-tuning feasible on a single A100 40GB or a consumer card with 24-32GB.

For cost calculation context: Training a 7B parameter language model on a 128-GPU cluster on A100 at $2/hour per GPU: 128 GPUs x 168 hours (7 days) x $2 = $43,008 total.

The search results don't contain specific information about total GPU-hours required for full VLA training from scratch in 2025-2026, but they indicate that A100s remain a viable option for VLA fine-tuning and training, especially when using parameter-efficient methods like LoRA or QLoRA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faead405-8f2d-40d7-b391-03b872de5a22",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "a6cd1fc4-a3f4-40a3-be92-786c00592e09",
  "sourceToolAssistantUUID": "faead405-8f2d-40d7-b391-03b872de5a22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T18:45:16.782Z_

<details><summary>↩ Tool result · `toolu_01SN4x4UagXGyMDFsfCbnyqw`</summary>

```text
Web search results for query: "OpenVLA training compute requirements"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v2"},{"title":"Understanding OpenVLA: A Simple Guide - Hankyu Kim","url":"https://hankyukim.com/openvla/"},{"title":"OpenVLA: Training Robot Policies by Treating Actions as Language Tokens | Starlog","url":"https://starlog.is/articles/llm-engineering/openvla-openvla/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Scaling VLA Model Training on a Budget: Lessons From 100+ Fine-Tunes | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/scaling-vla-training-on-a-budget"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"}]

Based on the search results, here are the key training compute requirements for OpenVLA:

## Original Training

The final OpenVLA model was trained on a cluster of 64 A100 GPUs for 14 days, totaling 21,500 A100-hours, using a batch size of 2048.

## Fine-tuning Requirements

For those looking to fine-tune OpenVLA:

- **LoRA Fine-tuning**: You will want at least a 40GB A100 or, ideally, an 80GB H100 for comfortable batch sizes with LoRA.

- **Full Fine-tuning**: Full fine-tuning is only recommended if you have sufficient compute (e.g., a full node of 8 A100 GPUs).

- **OFT Fine-tuning**: OpenVLA-OFT training jobs were run with 8 A100 or H100 GPUs with 80 GB memory and trained for 50K to 150K gradient steps, depending on the fine-tuning dataset size, which took 1-2 days.

## Inference Requirements

During inference, OpenVLA requires 15GB of GPU memory when loaded in bfloat16 precision and runs at approximately 6Hz on one NVIDIA RTX 4090 GPU.

## Key Considerations

The resolution of input images has significant impact on the computational requirements of VLA training, since higher-resolution images result in more image patch tokens and thus longer context lengths that quadratically increase training compute.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6f48d99-31d4-4439-9b9a-d0a850b7cb1d",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "19213a62-2c2e-46d4-9c3c-779544902f68",
  "sourceToolAssistantUUID": "c6f48d99-31d4-4439-9b9a-d0a850b7cb1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T18:45:17.193Z_

<details><summary>↩ Tool result · `toolu_01TwGQu6gjtntm3SzxETgFVe`</summary>

```text
Web search results for query: "github.com OpenVLA affordance"

Links: [{"title":"GitHub - yueen-ma/Awesome-VLA · GitHub","url":"https://github.com/yueen-ma/awesome-vla"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"},{"title":"Open-Vocabulary Affordance Detection in 3D Point Clouds","url":"https://arxiv.org/pdf/2303.02401"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary   Task-Oriented Grasping in Clutter","url":"https://arxiv.org/pdf/2503.00778"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"GitHub - dusty-nv/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation.","url":"https://github.com/dusty-nv/openvla"}]

Based on the search results, here's what I found:

## OpenVLA Overview

OpenVLA is a 7B-parameter open-source vision-language-action model trained on 970k robot episodes from the Open X-Embodiment dataset. OpenVLA sets a new state of the art for generalist robot manipulation policies and supports controlling multiple robots out of the box while being quickly adaptable to new robot domains via parameter-efficient fine-tuning.

## GitHub Repository

The main OpenVLA GitHub repository is at **github.com/reazon-research/openvla**. The OpenVLA checkpoints and PyTorch training pipeline are fully open-source and models can be downloaded and fine-tuned from HuggingFace.

## Related Work on Affordances

The search results also show related research on affordances for robotics. RT-A (RT-Affordance) presents "Affordances are Versatile Intermediate Representations for Robot Manipulation" published at ICRA 2025, which explores the use of affordances in conjunction with vision-language-action models for robot manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4ea59c7-81da-4206-a564-ed6915d65cf8",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "1d06f680-709b-4f52-a997-751e85da4516",
  "sourceToolAssistantUUID": "b4ea59c7-81da-4206-a564-ed6915d65cf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T18:45:21.599Z_

<details><summary>↩ Tool result · `toolu_01CeVHqQtwFpTpUGLqmHCy92`</summary>

```text
Web search results for query: "github.com affordance grounding VLA implementation"

Links: [{"title":"Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions | Request PDF","url":"https://www.researchgate.net/publication/394512560_Grounding_3D_Object_Affordance_with_Language_Instructions_Visual_Observations_and_Interactions"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"GitHub - JasonQSY/AffordanceLLM: Code for \"AffordanceLLM: Grounding Affordance from Vision Language Models\"","url":"https://github.com/JasonQSY/AffordanceLLM"},{"title":"GitHub - lhc1224/Cross-View-AG: Official PyTorch Implementation of Learning Affordance Grounding from Exocentric Images, CVPR 2022","url":"https://github.com/lhc1224/Cross-View-AG"},{"title":"GitHub - yyvhang/IAGNet: The Pytorch implementation of Grounding 3D Object Affordance from 2D Interactios in Images. · GitHub","url":"https://github.com/yyvhang/IAGNet"}]

Based on the search results, I found several relevant GitHub repositories and research projects related to affordance grounding and VLA (Vision-Language-Action) implementations:

## Key GitHub Repositories Found:

1. **AffordanceLLM** (github.com/JasonQSY/AffordanceLLM): Code for "AffordanceLLM: Grounding Affordance from Vision Language Models".

2. **Cross-View-AG** (github.com/lhc1224/Cross-View-AG): Official PyTorch Implementation of Learning Affordance Grounding from Exocentric Images, CVPR 2022.

3. **IAGNet** (github.com/yyvhang/IAGNet): The Pytorch implementation of Grounding 3D Object Affordance from 2D Interactions in Images.

## Recent Research Directions:

The search also reveals several cutting-edge approaches to affordance grounding in VLAs:

- VEGA (Visual Encoder Grounding Alignment) directly aligns the output of the VLA's visual encoder with spatially-aware features, grounding spatial awareness before any linguistic entanglement occurs.

- A framework with a module designed to strategically infuse affordance knowledge into policy learning, enabling robots to better ground actions in physical and contextual understanding.

These repositories and approaches represent the intersection of affordance understanding, language grounding, and robotic control in modern Vision-Language-Action systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9831a69-208a-4514-a647-e2688604c440",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "927fc20f-0c09-4cf4-b92b-3c202979129f",
  "sourceToolAssistantUUID": "e9831a69-208a-4514-a647-e2688604c440",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-18T18:45:24.173Z_

Let me run a few follow-up searches to fill in specific gaps on metrics, dataset sizes, and code availability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "927fc20f-0c09-4cf4-b92b-3c202979129f",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXgugeohMcQyNf5Modb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9960eccf-9347-4531-a296-796a4670a980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQER36VGuYb6YMMcbBrRve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6570,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 9529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1274,
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

_source line 28 · 2026-05-18T18:45:25.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JosT193wsduDjob2twgqGv`</summary>

```json
{
  "query": "AffordanceLLM github code dataset performance metrics KLD SIM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9960eccf-9347-4531-a296-796a4670a980",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXgugeohMcQyNf5Modb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fe3846e-66e6-4907-be8b-5194929c68c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQER36VGuYb6YMMcbBrRve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6570,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 9529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1274,
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

_source line 29 · 2026-05-18T18:45:26.150Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V3PJcyUzkNNuLxuPiM5rHP`</summary>

```json
{
  "query": "AGD20K benchmark results KLD SIM NSS affordance grounding leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fe3846e-66e6-4907-be8b-5194929c68c8",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXgugeohMcQyNf5Modb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1704bb8-fe22-4b5e-9605-b7cce8e9e5ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQER36VGuYb6YMMcbBrRve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6570,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 9529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1274,
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

_source line 30 · 2026-05-18T18:45:27.078Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P5H7ruB8bB5MKz2vHFXrZL`</summary>

```json
{
  "query": "OpenVLA 7B training 21500 GPU hours dataset size Open X-Embodiment 970k episodes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1704bb8-fe22-4b5e-9605-b7cce8e9e5ac",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXgugeohMcQyNf5Modb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "528c5f98-9c3c-46de-8c13-1bbf0f788fcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQER36VGuYb6YMMcbBrRve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6570,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 9529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1274,
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

_source line 31 · 2026-05-18T18:45:27.532Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rr6HTW7eZTExr1uoQXtTeA`</summary>

```json
{
  "query": "AffordanceSAM AGD20K results metrics 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "528c5f98-9c3c-46de-8c13-1bbf0f788fcd",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXgugeohMcQyNf5Modb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f760fa8e-edab-42cb-a021-2c577c7580d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQER36VGuYb6YMMcbBrRve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6570,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 9529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1274,
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

_source line 32 · 2026-05-18T18:45:28.209Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VVRwQKuT1xmmFDAmsLfyM3`</summary>

```json
{
  "query": "CoA-VLA chain of affordance VLA code github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f760fa8e-edab-42cb-a021-2c577c7580d8",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXgugeohMcQyNf5Modb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cd3b77c-9f1e-48dd-b385-a928e98d0c83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQER36VGuYb6YMMcbBrRve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6570,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 9529,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1274
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6570,
          "output_tokens": 299,
          "cache_read_input_tokens": 9529,
          "cache_creation_input_tokens": 1274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1274,
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

_source line 33 · 2026-05-18T18:45:33.763Z_

<details><summary>↩ Tool result · `toolu_01P5H7ruB8bB5MKz2vHFXrZL`</summary>

```text
Web search results for query: "OpenVLA 7B training 21500 GPU hours dataset size Open X-Embodiment 970k episodes"

Links: [{"title":"openvla/openvla-7b · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v2"},{"title":"openvla/README.md at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/README.md"},{"title":"Understanding OpenVLA: A Simple Guide - Hankyu Kim","url":"https://hankyukim.com/openvla/"},{"title":"Deploy OpenVLA on GPU Cloud: Self-Host the Open Vision-Language-Action Robotics Foundation Model (2026 Setup Guide) | Spheron Blog","url":"https://www.spheron.network/blog/deploy-openvla-gpu-cloud/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"OpenVLA is an open-source generalist robotics model | VentureBeat","url":"https://venturebeat.com/ai/openvla-is-an-open-source-generalist-robotics-model"}]

Based on the search results, here's what I found about OpenVLA 7B:

## Dataset and Training Information

OpenVLA 7B is trained on 970K robot manipulation episodes from the Open X-Embodiment dataset. The dataset consists of 970k robot manipulation trajectories from the Open X-Embodiment (OpenX) dataset.

## Training Compute

OpenVLA was trained on a cluster of 64 A100 GPUs for 15 days. However, I should note that the specific figure of 21,500 GPU hours you mentioned in your query does not appear in these search results. Based on the information that 64 A100 GPUs were used for 15 days, this would roughly correspond to approximately 23,040 GPU hours (64 × 24 × 15), which is close to but not exactly 21,500.

## Model Architecture

OpenVLA was created by fine-tuning a pretrained Prismatic-7B VLM, which consists of a fused visual encoder with SigLIP and DinoV2 backbones, a projector, and a Llama 2 7B language model backbone that predicts tokenized output actions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "528c5f98-9c3c-46de-8c13-1bbf0f788fcd",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "f53baaf1-ccd3-4509-b99a-909a53f40b96",
  "sourceToolAssistantUUID": "528c5f98-9c3c-46de-8c13-1bbf0f788fcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T18:45:40.554Z_

<details><summary>↩ Tool result · `toolu_01JosT193wsduDjob2twgqGv`</summary>

```text
Web search results for query: "AffordanceLLM github code dataset performance metrics KLD SIM"

Links: [{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://jasonqsy.github.io/AffordanceLLM/"},{"title":"GitHub - JasonQSY/AffordanceLLM: Code for \"AffordanceLLM: Grounding Affordance from Vision Language Models\"","url":"https://github.com/JasonQSY/AffordanceLLM"},{"title":"StatLLM: A Dataset for Evaluating the Performance of Large Language   Models in Statistical Analysis","url":"https://arxiv.org/pdf/2502.17657"},{"title":"Can Large Language Models Simulate Symbolic Execution Output Like KLEE?","url":"https://arxiv.org/pdf/2511.08530"},{"title":"Benchmarking Large Language Models for Predictive Modeling in Biomedical Research With a Focus on Reproductive Health","url":"https://www.biorxiv.org/content/10.1101/2025.07.07.663529.full.pdf"},{"title":"Large language models for frontline healthcare support in low-resource settings","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12880909/"},{"title":"How Good Are Large Language Models at Supporting Frontline Healthcare Workers in Low-Resource Settings – A Benchmarking Study & Dataset","url":"https://www.medrxiv.org/content/10.1101/2025.08.26.25333975.full.pdf"}]

Based on the search results, I found information about AffordanceLLM:

AffordanceLLM is about grounding affordance from vision language models, where affordance grounding refers to the task of finding the area of an object with which one can interact. The GitHub repository contains data processing code for "AffordanceLLM: Grounding Affordance from Vision Language Models".

Under the AGD20K benchmark, the proposed model demonstrates a significant performance gain over competing methods for in-the-wild object affordance grounding.

However, the search results did not provide specific information about the performance metrics you mentioned (KLD and SIM) or detailed dataset statistics. To get more specific information about those metrics and other technical details, you may want to visit the GitHub repository directly at https://github.com/JasonQSY/AffordanceLLM or the project website at https://jasonqsy.github.io/AffordanceLLM/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fe3846e-66e6-4907-be8b-5194929c68c8",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "52d84bff-8bd1-41a4-9253-e7d6c0fdc29a",
  "sourceToolAssistantUUID": "4fe3846e-66e6-4907-be8b-5194929c68c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T18:45:42.612Z_

<details><summary>↩ Tool result · `toolu_01Rr6HTW7eZTExr1uoQXtTeA`</summary>

```text
Web search results for query: "AffordanceSAM AGD20K results metrics 2026"

Links: [{"title":"[Literature Review] AffordanceSAM: Segment Anything Once More in Affordance Grounding","url":"https://www.themoonlight.io/en/review/affordancesam-segment-anything-once-more-in-affordance-grounding"},{"title":"AffordanceSAM: Segment Anything Once More in Affordance Grounding","url":"https://arxiv.org/pdf/2504.15650"},{"title":"The results of the different methods on the AGD20K for each affordance... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-results-of-the-different-methods-on-the-AGD20K-for-each-affordance-category-We_fig8_376833041"},{"title":"[2203.09905] Learning Affordance Grounding from Exocentric Images","url":"https://arxiv.org/abs/2203.09905"},{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://arxiv.org/html/2401.06341v2"},{"title":"Learning Affordance Grounding from Exocentric Images","url":"https://arxiv.org/pdf/2203.09905"},{"title":"GitHub - lhc1224/Cross-View-AG: Official PyTorch Implementation of Learning Affordance Grounding from Exocentric Images, CVPR 2022","url":"https://github.com/lhc1224/Cross-View-AG"},{"title":"Unsupervised Affordance Distillation for Generalization in ...","url":"https://openreview.net/pdf?id=an953WOpo2"}]

Based on the search results, I found information about AffordanceSAM and its performance on the AGD20K benchmark:

AffordanceSAM achieves state-of-the-art performance on the AGD20K benchmark and generalizes well to novel objects and affordance functions. The model surpasses previous methods under the AGD20K benchmark and shows evidence to handle the task with novel objects and affordance functions.

However, the search results don't contain specific numerical metrics or results from 2026. The papers found appear to be from earlier timeframes (2022-2024), as this research is relatively recent. To find more specific quantitative metrics from AffordanceSAM's AGD20K results, you may want to consult the full ArXiv paper or check academic databases directly for the detailed performance numbers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f760fa8e-edab-42cb-a021-2c577c7580d8",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "45377056-691f-4a0c-a459-629443681c08",
  "sourceToolAssistantUUID": "f760fa8e-edab-42cb-a021-2c577c7580d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T18:45:44.461Z_

<details><summary>↩ Tool result · `toolu_01VVRwQKuT1xmmFDAmsLfyM3`</summary>

```text
Web search results for query: "CoA-VLA chain of affordance VLA code github"

Links: [{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"Add CoA-VLA (Chain-of-Affordance) · Issue #5 · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/issues/5"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"}]

Based on the search results, here's what I found about CoA-VLA:

CoA-VLA (Chain-of-Affordance) is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion. 

The model prompts the system to consider four types of affordances before taking action: (1) object affordance — what object to manipulate and where it is; (2) grasp affordance — the specific object part to grasp; (3) spatial affordance — the optimal space to place the object; and (4) movement affordance — the collision-free path for movement.

CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks.

**Project Resources:**
- Project website: https://chain-of-affordance.github.io/
- ArXiv paper: https://arxiv.org/abs/2412.20451

The search results show the paper and project website, but I did not find a specific GitHub repository link with the code in these results. You may want to check the project website (chain-of-affordance.github.io) directly, as it likely contains links to the code repository or you can search for the authors' GitHub profiles for the implementation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cd3b77c-9f1e-48dd-b385-a928e98d0c83",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "9303638a-d0f9-4ce5-a415-5bb6b7f927b5",
  "sourceToolAssistantUUID": "7cd3b77c-9f1e-48dd-b385-a928e98d0c83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T18:45:51.298Z_

<details><summary>↩ Tool result · `toolu_01V3PJcyUzkNNuLxuPiM5rHP`</summary>

```text
Web search results for query: "AGD20K benchmark results KLD SIM NSS affordance grounding leaderboard"

Links: [{"title":"AffordanceSAM: Segment Anything Once More in Affordance Grounding","url":"https://arxiv.org/html/2504.15650v1"},{"title":"PanoAffordanceNet: Towards Holistic Affordance Grounding in 360° Indoor Environments","url":"https://arxiv.org/html/2603.09760"},{"title":"Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale","url":"https://arxiv.org/html/2506.12009v1"},{"title":"Weakly-Supervised Affordance Grounding Guided by Part-Level Semantic Priors","url":"https://arxiv.org/html/2505.24103v1"},{"title":"[Literature Review] WorldAfford: Affordance Grounding based on Natural Language Instructions","url":"https://www.themoonlight.io/en/review/worldafford-affordance-grounding-based-on-natural-language-instructions"},{"title":"The results of the different methods on the AGD20K for each affordance... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-results-of-the-different-methods-on-the-AGD20K-for-each-affordance-category-We_fig8_376833041"},{"title":"[2503.02600] Resource-Efficient Affordance Grounding with Complementary Depth and Semantic Prompts","url":"https://arxiv.org/abs/2503.02600"},{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://arxiv.org/html/2401.06341v2"},{"title":"2D affordance grounding on the AGD20K [33] | Download Scientific Diagram","url":"https://www.researchgate.net/figure/2D-affordance-grounding-on-the-AGD20K-33_tbl2_392716806"}]

Based on the search results, here's what I found about AGD20K benchmark results using the KLD, SIM, and NSS metrics:

## Evaluation Metrics

KLD quantifies the distributional difference between the predicted and ground-truth heatmaps (lower is better). SIM measures their histogram intersection, and NSS calculates the normalized prediction score at ground-truth keypoint locations. For both SIM and NSS, higher values indicate better performance.

## Notable Results

**AffordanceSAM**: On the easy split, it achieves the highest scores in SIM (0.543) and NSS (1.800). On the hard split, this method reduces the KLD by 17.4%, while simultaneously increasing the SIM and NSS scores by 10.4% and 64.2% respectively when compared to the previous best performing method OOAL.

**BiT-Align (Resource-Efficient Affordance Grounding)**: Compared with the current state-of-the-art method, it achieves a 6.0% improvement in the KLD metric, while reducing model parameters by 88.8%.

**WorldAfford**: Performance is evaluated on both the existing AGD20K dataset and the new LLMaFF dataset using metrics like KLD (Kullback-Leibler Divergence), SIM (Similarity), and NSS (Normalized Scanpath Saliency) to measure the correspondence between the predicted affordance map and the ground truth.

The search results provide various benchmark results, but do not show a comprehensive leaderboard table with all methods ranked side-by-side.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1704bb8-fe22-4b5e-9605-b7cce8e9e5ac",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "3bf1bece-c800-4cc8-857b-e7a1f3bb56bf",
  "sourceToolAssistantUUID": "e1704bb8-fe22-4b5e-9605-b7cce8e9e5ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T18:45:54.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CHEVYBSiLdN7TD1hYcTrqX`</summary>

```json
{
  "query": "Affordance-R1 reinforcement learning affordance reasoning MLLM github 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bf1bece-c800-4cc8-857b-e7a1f3bb56bf",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXj6dmUgzfQYt8Gahiz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fc81fe5-1bcf-4644-b1f6-f8b6be5adafe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KWDaDCHhj9f7WR8vQvyY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2154,
      "cache_creation_input_tokens": 8430,
      "cache_read_input_tokens": 10803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8430,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 39 · 2026-05-18T18:45:55.695Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RbbVQxAuoVHtrc47H51Ayd`</summary>

```json
{
  "query": "3D AffordanceNet dataset size benchmark results github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fc81fe5-1bcf-4644-b1f6-f8b6be5adafe",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXj6dmUgzfQYt8Gahiz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7a48f29-cb91-4af6-be74-8bc2dc5f6074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KWDaDCHhj9f7WR8vQvyY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2154,
      "cache_creation_input_tokens": 8430,
      "cache_read_input_tokens": 10803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8430,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 40 · 2026-05-18T18:45:56.075Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JXT85Hfhud7vpwZWAMAczh`</summary>

```json
{
  "query": "PADv2 purpose driven affordance dataset benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7a48f29-cb91-4af6-be74-8bc2dc5f6074",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXj6dmUgzfQYt8Gahiz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77011be2-7e65-4fe0-be09-61a120241492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KWDaDCHhj9f7WR8vQvyY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2154,
      "cache_creation_input_tokens": 8430,
      "cache_read_input_tokens": 10803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8430,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 41 · 2026-05-18T18:46:02.430Z_

<details><summary>↩ Tool result · `toolu_01CHEVYBSiLdN7TD1hYcTrqX`</summary>

```text
Web search results for query: "Affordance-R1 reinforcement learning affordance reasoning MLLM github 2025"

Links: [{"title":"Affordance-R1: Reinforcement Learning for Generalizable Affordance Reasoning in Multimodal Large Language Model","url":"https://arxiv.org/html/2508.06206"},{"title":"GitHub - hq-King/Affordance-R1: code for affordance-r1","url":"https://github.com/hq-King/Affordance-R1"},{"title":"Affordance-R1: Reinforcement Learning for Generalizable Affordance Reasoning","url":"https://arxiv.org/pdf/2508.06206"},{"title":"GitHub - hq-King/Awesome-Affordance-Learning · GitHub","url":"https://github.com/hq-King/Awesome-Affordance-Learning"},{"title":"Affordance-R1: Reinforcement Learning for Generalizable Affordance Reasoning in Multimodal Large Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250806206W/abstract"},{"title":"AffordanceGrasp-R1: Leveraging Reasoning-Based Affordance Segmentation with Reinforcement Learning for Robotic Grasping","url":"https://arxiv.org/html/2602.03547"},{"title":"GitHub - Jiaaqiliu/Awesome-RL-Reasoning-LMs: A comprehensive collection of research papers on RL(especially various R1-related paper) techniques for enhancing reasoning capabilities in LLMs, VLMs, and MLLMs. · GitHub","url":"https://github.com/Jiaaqiliu/Awesome-RL-Reasoning-LMs"}]

Based on the web search results, here's what I found about Affordance-R1:

## Overview

Affordance-R1 is a reinforcement learning framework that enhances affordance grounding models with deep reasoning capabilities. It employs GRPO to fine-tune MLLMs without supervised training, investigating their self-evolution potential to develop reasoning abilities rather than relying on explicitly annotated processes.

## Key Features

The model processes queries through policy-based reasoning with &lt;think> and &lt;rethink> stages to generate affordance predictions. The policy optimization uses a sophisticated reward system comprising format rewards for reasoning structure, perception rewards for spatial accuracy (Box-Num, IOU, L1), and recognition rewards for semantic similarity.

The researchers constructed a high-quality affordance dataset ReasonAff for MLLM-based instruction-tuning, which is crucial for embodied perception and reasoning.

## Training and Results

Trained exclusively via reinforcement learning with GRPO and without explicit reasoning data, Affordance-R1 achieves robust zero-shot generalization and exhibits emergent test-time reasoning capabilities. Affordance-R1 is the first to integrate GRPO-based RL with reasoning into affordance reasoning.

## GitHub Repository

The code of the method and dataset is released on https://github.com/hq-King/Affordance-R1. The code was released on August 11th, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fc81fe5-1bcf-4644-b1f6-f8b6be5adafe",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "959bf879-2214-46b6-80b7-dbf7ecb0a405",
  "sourceToolAssistantUUID": "9fc81fe5-1bcf-4644-b1f6-f8b6be5adafe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T18:46:03.163Z_

<details><summary>↩ Tool result · `toolu_01JXT85Hfhud7vpwZWAMAczh`</summary>

```text
Web search results for query: "PADv2 purpose driven affordance dataset benchmark results"

Links: [{"title":"[2108.03658] One-Shot Object Affordance Detection in the Wild","url":"https://arxiv.org/abs/2108.03658"},{"title":"RoboAfford: A Dataset and Benchmark for Enhancing Object and Spatial Affordance Learning in Robot Manipulation | Request PDF","url":"https://www.researchgate.net/publication/396941670_RoboAfford_A_Dataset_and_Benchmark_for_Enhancing_Object_and_Spatial_Affordance_Learning_in_Robot_Manipulation"},{"title":"One-Shot Object Affordance Detection in the Wild","url":"https://arxiv.org/pdf/2108.03658"},{"title":"One-Shot Object Affordance Detection in the Wild | International Journal of Computer Vision | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11263-022-01642-4"},{"title":"One-Shot Object Affordance Detection in the Wild | DeepAI","url":"https://deepai.org/publication/one-shot-object-affordance-detection-in-the-wild"},{"title":"Visual affordance maps obtained by different methods on the PADv2 | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Visual-affordance-maps-obtained-by-different-methods-on-the-PADv2_fig11_362557495"},{"title":"Papers with Code - PADv2 Dataset","url":"https://paperswithcode.com/dataset/padv2"},{"title":"One-Shot Affordance Detection","url":"https://arxiv.org/pdf/2106.14747"}]

Based on the search results, here's what I found about PADv2 (Purpose-driven Affordance Dataset v2) and its benchmark results:

## Dataset Overview
PADv2 is a large-scale Purpose-driven Affordance Dataset v2 built by collecting and labeling 30k images from 39 affordance and 103 object categories. It provides rich affordance mask annotations, depth information annotations, bounding boxes annotations of humans/objects, and human pose annotations in support images.

## Purpose and Benchmarking
With complex scenes and rich annotations, PADv2 can be used as a test bed to benchmark affordance detection methods and may also facilitate downstream vision tasks, such as scene understanding, action recognition, and robot manipulation.

## Benchmark Experiments
Comprehensive experiments on PADv2 dataset were conducted by including 11 advanced models from several related research fields. Experimental results demonstrate the superiority of the OSAD-Net model over previous representative ones in terms of both objective metrics and visual quality.

The dataset was introduced in a paper on one-shot object affordance detection, which addresses the problem of detecting objects with common affordances given a support image depicting an action purpose. The benchmark suite is available on GitHub for researchers to use.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77011be2-7e65-4fe0-be09-61a120241492",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "97b47e8e-a86c-415e-8824-5077f5b0d4d9",
  "sourceToolAssistantUUID": "77011be2-7e65-4fe0-be09-61a120241492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-18T18:46:04.174Z_

<details><summary>↩ Tool result · `toolu_01RbbVQxAuoVHtrc47H51Ayd`</summary>

```text
Web search results for query: "3D AffordanceNet dataset size benchmark results github"

Links: [{"title":"[PDF] 3D AffordanceNet: A Benchmark for Visual Object Affordance Understanding | Semantic Scholar","url":"https://www.semanticscholar.org/paper/3D-AffordanceNet:-A-Benchmark-for-Visual-Object-Deng-Xu/63508e386705e1340944db73e4d690dbc7febb37"},{"title":"3D AffordanceNet: A Benchmark for Visual Object Affordance Understanding | Request PDF","url":"https://www.researchgate.net/publication/350512270_3D_AffordanceNet_A_Benchmark_for_Visual_Object_Affordance_Understanding"},{"title":"[2103.16397] 3D AffordanceNet: A Benchmark for Visual Object Affordance Understanding","url":"https://arxiv.org/abs/2103.16397"},{"title":"3D AffordanceNet: A Benchmark for Visual Object Affordance Understanding - A*STAR OAR","url":"https://oar.a-star.edu.sg/communities-collections/articles/18009?collectionId=20"},{"title":"3D AffordanceNet: A Benchmark for Visual Object Affordance Understanding | DeepAI","url":"https://deepai.org/publication/3d-affordancenet-a-benchmark-for-visual-object-affordance-understanding"},{"title":"GitHub - Gorilla-Lab-SCUT/AffordanceNet · GitHub","url":"https://github.com/Gorilla-Lab-SCUT/AffordanceNet"},{"title":"3D AffordanceNet: A Benchmark for Visual Object Affordance Understanding","url":"https://arxiv.org/pdf/2103.16397"},{"title":"3D AffordanceNet: A Benchmark for Visual Object Affordance Understanding","url":"https://openaccess.thecvf.com/content/CVPR2021/papers/Deng_3D_AffordanceNet_A_Benchmark_for_Visual_Object_Affordance_Understanding_CVPR_2021_paper.pdf"}]

Based on the search results, here's what I found about the 3D AffordanceNet dataset:

**Dataset Size:**
3D AffordanceNet is a 3D point cloud benchmark consisting of 23k shapes from 23 semantic object categories, annotated with 56k affordance annotations and covering 18 visual affordance categories.

**Benchmarking Tasks:**
The dataset provides three benchmarking tasks for evaluating visual affordance understanding, including full-shape, partial-view and rotation-invariant affordance estimations.

**Benchmark Methods:**
The GitHub repository implements two baseline methods: PointNet++ and DGCNN on four proposed affordance understanding tasks: Full-Shape, Partial-View, Rotation-Invariant, Semi-Supervised Affordance Estimation.

**GitHub Repository:**
The official GitHub repository is available at https://github.com/Gorilla-Lab-SCUT/AffordanceNet, which contains implementation of the baseline methods and allows you to reproduce the performance results from the original paper.

The dataset was published as a CVPR 2021 paper and represents a significant benchmark for 3D visual affordance understanding in robotics and computer vision applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7a48f29-cb91-4af6-be74-8bc2dc5f6074",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a359a0270b1b532f7",
  "type": "user",
  "uuid": "0ef04fbe-8101-4853-9689-74d6d25788dc",
  "sourceToolAssistantUUID": "b7a48f29-cb91-4af6-be74-8bc2dc5f6074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-18T18:47:30.941Z_

Here is the consolidated research report across all 10 searches.

---

## 1. Affordance Grounding + VLA Implementations (GitHub)

**Repositories found:**

- **AffordanceLLM** ([github.com/JasonQSY/AffordanceLLM](https://github.com/JasonQSY/AffordanceLLM)) -- Grounding affordance from Vision-Language Models. Code is public. Evaluated on AGD20K; significant performance gains reported over prior methods.
- **Cross-View-AG** ([github.com/lhc1224/Cross-View-AG](https://github.com/lhc1224/Cross-View-AG)) -- Official PyTorch implementation for "Learning Affordance Grounding from Exocentric Images" (CVPR 2022). Introduced the AGD20K dataset. Code is public.
- **IAGNet** ([github.com/yyvhang/IAGNet](https://github.com/yyvhang/IAGNet)) -- Grounding 3D Object Affordance from 2D Interactions. PyTorch, code public.
- **Affordance-R1** ([github.com/hq-King/Affordance-R1](https://github.com/hq-King/Affordance-R1)) -- RL-based (GRPO) affordance reasoning in MLLMs. Code and dataset (ReasonAff) released August 2025. First to integrate GRPO-based RL with reasoning for affordance tasks.
- **Awesome-Affordance-Learning** ([github.com/hq-King/Awesome-Affordance-Learning](https://github.com/hq-King/Awesome-Affordance-Learning)) -- Curated list of affordance learning papers/repos.

**VLA-specific affordance papers (code status unclear):**
- **CoA-VLA** (Chain-of-Affordance, ICCV 2025) -- Decomposes affordance into object/grasp/spatial/movement affordances before action prediction. Outperforms OpenVLA and Octo. Project site: chain-of-affordance.github.io. No public GitHub repo found in search results; check the project page.
- **Affordance Field Intervention** (arXiv 2512.07472) -- Enables VLAs to escape "memory traps." Paper only, no public code found.

---

## 2. OpenVLA

**Repository:** [github.com/openvla/openvla](https://github.com/openvla/openvla) -- fully open-source, weights on HuggingFace at `openvla/openvla-7b`.

**Architecture:** Prismatic-7B VLM backbone (SigLIP + DinoV2 fused visual encoder, Llama 2 7B LM), actions tokenized as language tokens.

**Training data:** 970K robot manipulation episodes from Open X-Embodiment.

**Training compute:**
- 64 A100 GPUs for ~14-15 days
- Approximately **23,000 A100-GPU-hours** (some sources round to 21,500)
- Batch size 2048

**Fine-tuning compute:**
- LoRA/QLoRA: feasible on a single A100 40GB or even a 24-32GB consumer GPU
- Full fine-tune: recommended 8x A100 node minimum
- OpenVLA-OFT: 8x A100/H100 80GB, 50K-150K gradient steps, 1-2 days

**Inference:** ~15GB VRAM in bfloat16, ~6 Hz on RTX 4090.

**Practical note:** Input image resolution has quadratic impact on compute due to patch token count.

---

## 3. UAD (Unsupervised Affordance Distillation)

**Paper:** "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation" (ICRA 2025, arXiv 2506.09284).

**Method:** Distills affordance knowledge from foundation models (large vision models + VLMs) into a lightweight task-conditioned decoder on top of frozen features. No manual annotations required -- automatically generates large-scale paired data.

**Code availability:** Project website at unsup-affordance.github.io (and also gpt-affordance.github.io). The paper references a GitHub link, but no direct public repo URL was confirmed in search results. The PDF is hosted at a GitHub Pages site, suggesting code release is intended/partial.

**Practical note:** The "no annotation" aspect is compelling for scaling, but the reliance on foundation model quality for pseudo-labels introduces a data quality dependency.

---

## 4. AGD20K Dataset/Benchmark

**Repository:** [github.com/lhc1224/Cross-View-AG](https://github.com/lhc1224/Cross-View-AG) (CVPR 2022).

**Dataset size:** 20,000+ images across 36 affordance categories. It is the only large-scale affordance grounding dataset with accurate action and object labels.

**Evaluation metrics:** KLD (lower is better), SIM (higher is better), NSS (higher is better).

**Current SOTA results on AGD20K (as of early 2026):**

| Method | Key Result |
|--------|-----------|
| **AffordanceSAM** (Apr 2026) | Easy split: SIM=0.543, NSS=1.800 (best). Hard split: KLD reduced 17.4%, SIM +10.4%, NSS +64.2% vs. previous SOTA (OOAL) |
| **BiT-Align** | KLD improved 6.0% over prior SOTA, with 88.8% fewer parameters |
| **AffordanceLLM** | Significant gains over competing methods (specific numbers require paper) |
| **Cross-View-AG** (baseline) | Original benchmark baseline |

---

## 5. HuggingFace Datasets

**Available datasets:**
- **Affogato** ([huggingface.co/datasets/project-affogato/affogato](https://huggingface.co/datasets/project-affogato/affogato)) -- 150K instances with open-vocabulary text descriptions + 3D affordance heatmaps. Largest 3D affordance grounding dataset to date. Associated paper: arXiv 2506.12009.
- **Mosaic3D** ([huggingface.co/datasets/junhalee/Mosaic3D](https://huggingface.co/datasets/junhalee/Mosaic3D)) -- Large-scale dataset for open-vocabulary segmentation and affordance grounding in 3D scenes.

---

## 6. Papers with Code: Affordance Detection Datasets

| Dataset | Size | Categories | Type |
|---------|------|-----------|------|
| **3D AffordanceNet** | 23K shapes, 56K annotations | 18 affordance classes, 23 object categories | 3D point clouds |
| **ADE-Affordance** | Built on ADE20K | Rich visual reasoning annotations | 2D images |
| **Visual Affordance Learning** | 47,210 RGBD images | 15 affordance categories, 37 object categories | Multi-view RGBD |
| **PADv2** | 30K images | 39 affordance categories, 103 object categories | 2D with depth, pose, bbox |

**3D AffordanceNet GitHub:** [github.com/Gorilla-Lab-SCUT/AffordanceNet](https://github.com/Gorilla-Lab-SCUT/AffordanceNet) -- Baselines: PointNet++, DGCNN on four tasks. CVPR 2021.

**PADv2:** Benchmarked with 11 models; OSAD-Net showed best results. Supports one-shot affordance detection.

---

## 7. Papers with Code: Affordance Grounding Benchmarks

Key benchmarks beyond AGD20K:
- **LLMaFF** -- 550 test images with natural language instructions + manually labeled affordance maps
- **AGPIL** -- 30,972 point-image-text pairs, 17 affordance categories, 23 object classes
- **Video-to-image benchmarks:** OPRA, EPIC-Hotspot, AssistQ
- **Affogato** -- 150K instances (3D, open-vocabulary)
- **RoboAfford** -- Newer benchmark for object and spatial affordance in robot manipulation

---

## 8. VLA Training Cost (GPU Hours, A100, 2025-2026)

**A100 cloud pricing (Q2 2026):**
- Range: $1.07/hr to $3.43/hr depending on provider and configuration
- On-demand average ~$2.09/hr (down ~13% since May 2025)
- Cheapest spot: ~$1.07/hr for A100 80G SXM4

**VLA training cost estimates:**
- OpenVLA full training: ~23,000 A100-hours x $2/hr = **~$46,000** at mid-range pricing
- 128-GPU cluster for 7 days (hypothetical 7B model): ~$43,000
- Fine-tuning (LoRA): single GPU, hours to a day -- **$2-50** depending on dataset
- Fine-tuning (full, OFT): 8 GPUs for 1-2 days -- **$400-800**

**Practical notes:** QLoRA makes single-GPU fine-tuning feasible. H100s increasingly preferred for new training runs but A100s remain viable and cheaper.

---

## 9. OpenVLA Training Compute (Detailed)

- **Full pre-training:** 64 A100 GPUs, ~15 days, ~23,000 GPU-hours, batch size 2048
- **Fine-tuning (LoRA):** 1x A100 40GB minimum (QLoRA enables 24-32GB consumer GPUs)
- **Fine-tuning (full):** 8x A100 recommended minimum
- **OpenVLA-OFT:** 8x A100/H100 80GB, 50K-150K gradient steps, 1-2 days
- **Inference:** 15GB VRAM (bfloat16), ~6 Hz on RTX 4090
- **Image resolution caveat:** Higher resolution = quadratically more compute (more patch tokens = longer context)

---

## 10. Affordance Detection SOTA (2026)

**Current SOTA methods:**
- **AffordanceSAM** (April 2026) -- SOTA on AGD20K. Builds on SAM for affordance grounding. Generalizes to novel actions and objects.
- **Affordance-R1** (August 2025) -- First RL-based (GRPO) affordance reasoning in MLLMs. Zero-shot generalization with emergent test-time reasoning.
- **LM-AD** -- Uses pretrained language models for fine-grained 3D point cloud affordance detection. Addresses the problem that existing 3D methods have accuracy below 50% on standard benchmarks.
- **PanoAffordanceNet** -- Holistic affordance grounding in 360-degree indoor environments.
- **AffordanceGrasp-R1** -- Extends R1-style reasoning to robotic grasping via affordance segmentation.

**Key gap:** 3D affordance detection accuracy remains below 50% on standard benchmarks, indicating significant room for improvement.

---

## Summary for Resource Planning

| Item | Key Number |
|------|-----------|
| Full VLA training (OpenVLA-scale) | ~23,000 A100-hours (~$46K at $2/hr) |
| VLA LoRA fine-tuning | 1 GPU, hours, ~$2-50 |
| VLA full fine-tuning | 8 GPUs, 1-2 days, ~$400-800 |
| AGD20K dataset | 20K+ images, 36 affordance categories |
| Affogato dataset | 150K instances (largest 3D affordance) |
| PADv2 dataset | 30K images, 39 affordance / 103 object categories |
| 3D AffordanceNet | 23K shapes, 56K annotations |
| Open X-Embodiment (for VLA) | 970K robot manipulation episodes |
| SOTA AGD20K (AffordanceSAM) | SIM=0.543, NSS=1.800 (easy split) |
| 3D affordance accuracy | <50% on standard benchmarks |
| A100 cloud cost (2026) | $1.07-$3.43/hr |

**Practical issues to note:**
1. No single repository combines affordance grounding with VLA training end-to-end -- you would need to integrate components.
2. CoA-VLA is the closest to "affordance + VLA" but code availability is uncertain.
3. UAD's unsupervised approach is attractive for scaling but depends on foundation model quality for pseudo-labels.
4. 3D affordance accuracy is still low (<50%), suggesting the field is far from saturated.
5. Image resolution has quadratic compute impact in VLA training -- a critical design choice.
6. The Affogato 150K dataset and Affordance-R1's ReasonAff dataset are the newest large-scale resources.

Sources:
- [AffordanceLLM GitHub](https://github.com/JasonQSY/AffordanceLLM)
- [Cross-View-AG / AGD20K GitHub](https://github.com/lhc1224/Cross-View-AG)
- [IAGNet GitHub](https://github.com/yyvhang/IAGNet)
- [OpenVLA GitHub](https://github.com/openvla/openvla)
- [OpenVLA Paper](https://arxiv.org/pdf/2406.09246)
- [OpenVLA HuggingFace](https://huggingface.co/openvla/openvla-7b)
- [UAD Paper](https://arxiv.org/abs/2506.09284)
- [UAD Project Site](https://unsup-affordance.github.io/)
- [CoA-VLA Paper](https://arxiv.org/abs/2412.20451)
- [Affordance-R1 GitHub](https://github.com/hq-King/Affordance-R1)
- [Awesome-Affordance-Learning](https://github.com/hq-King/Awesome-Affordance-Learning)
- [Affogato Dataset (HuggingFace)](https://huggingface.co/datasets/project-affogato/affogato)
- [Affogato Paper](https://arxiv.org/pdf/2506.12009)
- [3D AffordanceNet GitHub](https://github.com/Gorilla-Lab-SCUT/AffordanceNet)
- [3D AffordanceNet Paper](https://arxiv.org/abs/2103.16397)
- [AffordanceSAM Paper](https://arxiv.org/pdf/2504.15650)
- [Papers with Code - Affordance Detection](https://paperswithcode.com/task/affordance-detection/codeless)
- [Papers with Code - ADE-Affordance](https://paperswithcode.com/dataset/ade-affordance)
- [A100 Cloud Pricing 2026](https://getdeploying.com/gpus/nvidia-a100)
- [VLA Training on a Budget](https://www.roboticscenter.ai/blog/scaling-vla-training-on-a-budget)
- [OpenVLA-OFT Project](https://openvla-oft.github.io/)
- [PADv2 on Papers with Code](https://paperswithcode.com/dataset/padv2)
- [Mosaic3D HuggingFace](https://huggingface.co/datasets/junhalee/Mosaic3D)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ef04fbe-8101-4853-9689-74d6d25788dc",
  "isSidechain": true,
  "agentId": "a359a0270b1b532f7",
  "requestId": "req_011CbAXk3kAn8xZ188DvWfyt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d39d24a8-7b27-44c8-822c-08bb9158eed8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lg9wLS3xsxnSu8CikSVsaM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 746,
      "cache_creation_input_tokens": 3936,
      "cache_read_input_tokens": 19233,
      "output_tokens": 3920,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 746,
          "output_tokens": 3920,
          "cache_read_input_tokens": 19233,
          "cache_creation_input_tokens": 3936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3936,
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
