# Research conversation: Search the web for concurrent and recent work (2025-2026) on open-vocabulary affordance reasoning in Vision-Language-Act

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a479979600018ba92.jsonl`
- **Structured JSON:** [`dcdbfaa853182cc88c7d.json`](../../sessions/dc/dcdbfaa853182cc88c7d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-18T18:26:54.760Z_

Search the web for concurrent and recent work (2025-2026) on open-vocabulary affordance reasoning in Vision-Language-Action models (VLAs). I need to know if anyone is already doing this or something very similar.

Perform these searches:
1. WebSearch: "open-vocabulary affordance reasoning VLA 2026"
2. WebSearch: "affordance tokens autoregressive VLA 2026"
3. WebSearch: "chain of affordance VLA open vocabulary 2025 2026"
4. WebSearch: "arXiv affordance VLA reasoning tokens 2025 2026"
5. WebSearch: "openreview affordance VLA reasoning ICML NeurIPS ICLR 2026"
6. WebSearch: "CoA-VLA open vocabulary affordance"
7. WebSearch: "CoT-VLA affordance reasoning extension 2025 2026"

For each result, note: title, authors, venue/date, and how it relates to "generating open-vocabulary affordance reasoning tokens before action tokens in a unified autoregressive VLA." Report any highly similar concurrent work clearly. Be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "1e1a478d-a250-4098-b426-b4d3b537c7d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T18:26:54.764Z_

```json
{
  "parentUuid": "1e1a478d-a250-4098-b426-b4d3b537c7d6",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
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
  "uuid": "4e7adc9c-1923-43ce-b774-e5d97bbf6648",
  "timestamp": "2026-05-18T18:26:54.764Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T18:26:57.604Z_



I'll start by loading the WebSearch tool schema, then run all the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e7adc9c-1923-43ce-b774-e5d97bbf6648",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWHKVbCuzS5uibCSs7C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bf803a7-5f8d-487f-ae1c-98f1802379b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BPuVRfGBC35Swdy3kLfrU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9035,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9035,
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

_source line 4 · 2026-05-18T18:26:57.759Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NGGVPfhwg4E1ZppXKT5jEZ`</summary>

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
  "parentUuid": "9bf803a7-5f8d-487f-ae1c-98f1802379b5",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWHKVbCuzS5uibCSs7C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eee1c200-54be-48de-86e9-ebb343b4fa04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BPuVRfGBC35Swdy3kLfrU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9035,
      "cache_read_input_tokens": 0,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9035
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9035,
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

_source line 5 · 2026-05-18T18:26:57.763Z_

<details><summary>↩ Tool result · `toolu_01NGGVPfhwg4E1ZppXKT5jEZ`</summary>

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
  "parentUuid": "eee1c200-54be-48de-86e9-ebb343b4fa04",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "b63ac59c-6625-4c45-9037-6538c665364b",
  "sourceToolAssistantUUID": "eee1c200-54be-48de-86e9-ebb343b4fa04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T18:27:00.355Z_



Now let me run all 7 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b63ac59c-6625-4c45-9037-6538c665364b",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWHYQE6PZPo932HMqND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7fb3ef8-2a50-44aa-8e26-5ff0fa14a9fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWkYsrfFCmfAfvnvCB5ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9035,
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

_source line 7 · 2026-05-18T18:27:00.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013PknV6D9x9x2ZBDFfmHZg5`</summary>

```json
{
  "query": "open-vocabulary affordance reasoning VLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7fb3ef8-2a50-44aa-8e26-5ff0fa14a9fe",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWHYQE6PZPo932HMqND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bca1dd02-f519-4dff-84f2-b49499f0c2fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWkYsrfFCmfAfvnvCB5ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9035,
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

_source line 8 · 2026-05-18T18:27:01.332Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MgmHZzL4PafBTVGsFPiA8w`</summary>

```json
{
  "query": "affordance tokens autoregressive VLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bca1dd02-f519-4dff-84f2-b49499f0c2fc",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWHYQE6PZPo932HMqND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84ddcca2-eacc-4232-9f8b-c54abce7590d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWkYsrfFCmfAfvnvCB5ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9035,
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

_source line 9 · 2026-05-18T18:27:01.478Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016YpY2FyWFp5weZKz1z15JY`</summary>

```json
{
  "query": "chain of affordance VLA open vocabulary 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84ddcca2-eacc-4232-9f8b-c54abce7590d",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWHYQE6PZPo932HMqND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06dc65f1-e6f4-43fd-a23c-2ae6354e70a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWkYsrfFCmfAfvnvCB5ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9035,
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

_source line 10 · 2026-05-18T18:27:01.791Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QedJ5RREy2C89ZybK9uk3S`</summary>

```json
{
  "query": "arXiv affordance VLA reasoning tokens 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06dc65f1-e6f4-43fd-a23c-2ae6354e70a4",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWHYQE6PZPo932HMqND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73621dc5-7b0d-46e7-bc71-1da4674fbb96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWkYsrfFCmfAfvnvCB5ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9035,
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

_source line 11 · 2026-05-18T18:27:02.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015PfKs4v5qDn2B391XmRHKZ`</summary>

```json
{
  "query": "openreview affordance VLA reasoning ICML NeurIPS ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73621dc5-7b0d-46e7-bc71-1da4674fbb96",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWHYQE6PZPo932HMqND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17210303-fd2f-463c-940e-baea92f77cf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWkYsrfFCmfAfvnvCB5ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9035,
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

_source line 12 · 2026-05-18T18:27:02.670Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012FD2tiqaCek3cxnScVgV3G`</summary>

```json
{
  "query": "CoA-VLA open vocabulary affordance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17210303-fd2f-463c-940e-baea92f77cf9",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWHYQE6PZPo932HMqND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "016cd98a-c8bf-4737-a97a-20ec3b0de444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWkYsrfFCmfAfvnvCB5ez",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9035,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 9035,
          "cache_creation_input_tokens": 1411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1411,
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

_source line 13 · 2026-05-18T18:27:02.676Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011nKkvhQ5qsqXAJrNxGSEMZ`</summary>

```json
{
  "query": "CoT-VLA affordance reasoning extension 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "016cd98a-c8bf-4737-a97a-20ec3b0de444",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWHYQE6PZPo932HMqND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16ad2787-2746-40ac-83b4-cb4a4e741070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWkYsrfFCmfAfvnvCB5ez",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 9035,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 9035,
          "cache_creation_input_tokens": 1411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1411,
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

_source line 14 · 2026-05-18T18:27:07.306Z_

<details><summary>↩ Tool result · `toolu_012FD2tiqaCek3cxnScVgV3G`</summary>

```text
Web search results for query: "CoA-VLA open vocabulary affordance"

Links: [{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"CoA-VLA","url":"https://chain-of-affordance.github.io/"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"},{"title":"Add CoA-VLA (Chain-of-Affordance) · Issue #5 · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/issues/5"}]

Based on the search results, here's what I found about CoA-VLA:

## CoA-VLA: Chain-of-Affordance Vision-Language-Action Models

CoA-VLA is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion.

### Key Components

The model considers four types of affordances before taking action: (1) object affordance — what object to manipulate and where it is; (2) grasp affordance — the specific object part to grasp; (3) spatial affordance — the optimal space to place the object; and (4) movement affordance — the collision-free path for movement.

Each affordance is transformed into two prompting formats: visual affordance and textual affordance, with a novel vision-language co-injection module that integrates this knowledge into the policy network.

### Performance

CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks. Furthermore, CoA-VLA exhibits strong generalization capabilities, including recognizing unseen object poses, identifying free space, and avoiding obstacles in novel environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "016cd98a-c8bf-4737-a97a-20ec3b0de444",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "8c8893f9-1f94-4e0d-9aa3-60931b02ecf0",
  "sourceToolAssistantUUID": "016cd98a-c8bf-4737-a97a-20ec3b0de444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T18:27:08.361Z_

<details><summary>↩ Tool result · `toolu_01MgmHZzL4PafBTVGsFPiA8w`</summary>

```text
Web search results for query: "affordance tokens autoregressive VLA 2026"

Links: [{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/394511717_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"arXiv:2503.10631v3 [cs.CV] 23 Jun 2025","url":"https://arxiv.org/pdf/2503.10631"},{"title":"FASTer: Toward Powerful and Efficient Autoregressive Vision–Language–Action Models with Learnable Action Tokenizer and Block-wise Decoding | OpenReview","url":"https://openreview.net/forum?id=k6nTUFoqeT"},{"title":"Think Twice, Act Once: Token-Aware Compression and Action Reuse for Efficient Inference in Vision-Language-Action Models","url":"https://arxiv.org/pdf/2505.21200"},{"title":"AR-VLA: True Autoregressive Action Expert for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.10126"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://arxiv.org/pdf/2507.22424"}]

Here are the search results for "affordance tokens autoregressive VLA 2026":

## Key Findings

**Autoregressive VLAs and Action Tokenization:**
Autoregressive VLAs use discrete action tokens within the vision-language model's vocabulary, enabling action generation similar to language modeling through next-token prediction.

**Affordance in VLA Systems:**
Language-based robot planners decompose instructions into executable subgoals, code, affordance-scored actions, or chain-of-thought rationales. Additionally, observations and task descriptions are used to inform affordance reasoning in natural language.

**Recent Developments (2025-2026):**
The search results show active research in this area, including:
- Recent approaches formulate future visual pixels and actions as autoregressive token sequences on a shared vocabulary.
- Autoregressive vision-language-action models have demonstrated strong capabilities in robotic manipulation, though action tokenization involves tradeoffs between reconstruction fidelity and inference efficiency. FASTer is a unified framework integrating a learnable tokenizer with an autoregressive policy.
- While recent VLA architectures are labeled "autoregressive," they utilize autoregression only to generate tokens within a single inference step and do not autoregress across time.

The research indicates ongoing work to improve efficiency and reasoning capabilities in autoregressive VLA systems for robotic control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84ddcca2-eacc-4232-9f8b-c54abce7590d",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "5156e1fd-7323-434e-a000-9662e491e878",
  "sourceToolAssistantUUID": "84ddcca2-eacc-4232-9f8b-c54abce7590d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T18:27:08.731Z_

<details><summary>↩ Tool result · `toolu_016YpY2FyWFp5weZKz1z15JY`</summary>

```text
Web search results for query: "chain of affordance VLA open vocabulary 2025 2026"

Links: [{"title":"Add CoA-VLA (Chain-of-Affordance) · Issue #5 · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/issues/5"},{"title":"(PDF) Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://www.researchgate.net/publication/387539786_Improving_Vision-Language-Action_Models_via_Chain-of-Affordance"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://chain-of-affordance.github.io/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation","url":"https://arxiv.org/pdf/2511.06240"}]

Here are the search results for "chain of affordance VLA open vocabulary 2025 2026":

## CoA-VLA: Chain-of-Affordance Vision-Language-Action Models

CoA-VLA (Chain-of-Affordance) was presented at ICCV 2025 and introduces Chain-of-Affordance reasoning for VLAs, prompting four types of affordances before acting: (1) object affordance — what to manipulate and where, (2) grasp affordance — which part to grasp, (3) spatial affordance — optimal placement space, (4) movement affordance — collision-free path.

Each affordance has visual and textual formats, injected via a novel vision-language co-injection module.

The approach outperforms OpenVLA and Octo with strong generalization to unseen poses, free space identification, and obstacle avoidance.

**Additional Context:**

Chain-of-Affordance (CoA-VLA) is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion. CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks and exhibits strong generalization capabilities, including recognizing unseen object poses, identifying free space, and avoiding obstacles in novel environments.

The official project page is available at https://chain-of-affordance.github.io/ and the paper is on arXiv at https://arxiv.org/abs/2412.20451


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06dc65f1-e6f4-43fd-a23c-2ae6354e70a4",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "c3c0aac5-d2ff-430e-9b77-3992229571c5",
  "sourceToolAssistantUUID": "06dc65f1-e6f4-43fd-a23c-2ae6354e70a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T18:27:09.129Z_

<details><summary>↩ Tool result · `toolu_01QedJ5RREy2C89ZybK9uk3S`</summary>

```text
Web search results for query: "arXiv affordance VLA reasoning tokens 2025 2026"

Links: [{"title":"Stable Language Guidance for Vision–Language–Action Models","url":"https://arxiv.org/html/2601.04052v2"},{"title":"[2510.01623] VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.01623"},{"title":"[2507.01925] A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/abs/2507.01925"},{"title":"Think Proprioceptively: Embodied Visual Reasoning for VLA Manipulation","url":"https://arxiv.org/pdf/2602.06575"},{"title":"GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.09079"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"}]

Based on the search results, here are relevant papers and research on arXiv involving affordance, VLA (Vision-Language-Action), reasoning, and tokens from 2025-2026:

1. **VLA-R1: Enhancing Reasoning in Vision-Language-Action Models** (October 2025)
   This work develops a high-quality dataset with chain-of-thought supervision aligned with affordance and trajectory annotations, achieving superior generalization and real-world performance.

2. **A Survey on Vision-Language-Action Models: An Action Tokenization Perspective** (July 2025)
   This comprehensive survey examines how VLA models formulate action tokens, categorizing them into language description, code, affordance, trajectory, goal state, latent representation, raw action, and reasoning.

3. **Think Proprioceptively: Embodied Visual Reasoning for VLA Manipulation** (February 2026)
   This work explores how embodied state can participate in visual reasoning and token selection, finding that text tokenization is more effective than learned projectors, and that retaining roughly 15% of visual tokens can match full token set performance.

4. **GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models** (2026)
   This model generates supervised Depth-Aware Chain-of-Thought intermediate reasoning over 3D object grounding, grasp affordance, metric spatial relations, and SE(3) motion plan waypoints.

5. **GTA-VLA (Guide, Think, Act)** (RSS 2026)
   This interactive framework enables spatially steerable embodied reasoning, allowing users to guide robot policies with explicit visual cues including affordance points, boxes, and traces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73621dc5-7b0d-46e7-bc71-1da4674fbb96",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "8b665492-1598-4909-9856-1da78cc00946",
  "sourceToolAssistantUUID": "73621dc5-7b0d-46e7-bc71-1da4674fbb96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T18:27:09.132Z_

<details><summary>↩ Tool result · `toolu_013PknV6D9x9x2ZBDFfmHZg5`</summary>

```text
Web search results for query: "open-vocabulary affordance reasoning VLA 2026"

Links: [{"title":"Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation","url":"https://arxiv.org/pdf/2511.06240"},{"title":"[Literature Review] GLOVER: Generalizable Open-Vocabulary Affordance Reasoning for Task-Oriented Grasping","url":"https://www.themoonlight.io/en/review/glover-generalizable-open-vocabulary-affordance-reasoning-for-task-oriented-grasping"},{"title":"3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary   Affordance Detection in 3D Worlds","url":"https://arxiv.org/pdf/2502.20041"},{"title":"AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary   Task-Oriented Grasping in Clutter","url":"https://arxiv.org/pdf/2503.00778"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

Based on the search results, here's what I found related to open-vocabulary affordance reasoning and VLAs in 2026:

## Key Research Areas

Affordance reasoning involves identifying specific regions of objects suitable for interaction, describing potential interactions between robots and their environment, such as using a knife's blade for cutting tasks.

## Recent Publications (2025-2026)

Several recent papers are advancing this field:

1. **3D-AffordanceLLM**: This work redefines 3D affordance detection as an Instruction Reasoning Affordance Segmentation task, equipping models with general recognition and segmentation knowledge through pretraining, then fine-tuning for context-aware reasoning and affordance region prediction.

2. **AffordGrasp**: This framework leverages vision-language models for in-context affordance reasoning, infers tasks from implicit user instructions, identifies task-relevant objects, and grounds their part-level affordances using visual grounding to generate task-oriented grasp poses within affordance regions.

3. **Mobile Manipulation**: Recent work leverages coarse semantic priors from VLMs to guide search toward task-relevant regions and refine placements with geometric constraints, achieving 85% success rate on diverse open-vocabulary mobile manipulation tasks.

The GitHub repository tracking this field lists multiple 2025-2026 publications including RoboReward, UAD, and other VLA-related works.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bca1dd02-f519-4dff-84f2-b49499f0c2fc",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "174c88ee-fbf9-4222-972e-4d74373f04aa",
  "sourceToolAssistantUUID": "bca1dd02-f519-4dff-84f2-b49499f0c2fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T18:27:11.028Z_

<details><summary>↩ Tool result · `toolu_015PfKs4v5qDn2B391XmRHKZ`</summary>

```text
Web search results for query: "openreview affordance VLA reasoning ICML NeurIPS ICLR 2026"

Links: [{"title":"ICLR 2026 Workshop Proposal ICLR 2026 Workshop on","url":"https://openreview.net/pdf/dbfd766aad3ada3875a0758013716727e704a7e3.pdf"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"ICLR 2026 Workshop LLM Reasoning | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FLLM_Reasoning"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.19752"},{"title":"Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning","url":"https://arxiv.org/pdf/2602.08167"}]

The search returned several relevant results on the topic of affordance, VLA (Vision-Language-Action) models, and reasoning. Here's what I found:

**Recent Research on Affordance and VLA Reasoning:**

Vision-Language-Action (VLA) models are robot foundation models that have garnered attention for enhancing robot policy learning, and researchers have introduced Chain-of-Affordance (CoA-VLA) approaches that incorporate reasoning in the format of sequential robot affordances to facilitate task completion.

The approach considers four types of affordances before taking action: object affordance (what object to manipulate and where), grasp affordance (the specific object part to grasp), spatial affordance (the optimal space to place the object), and movement affordance (the collision-free path for movement).

Additional work introduces Affordance Field Intervention (AFI), a lightweight hybrid framework that uses Spatial Affordance Fields as a plugin to guide VLA behavior, achieving an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios.

Other approaches enable VLAs to refine and bootstrap reasoning strategies based on their information benefit for action prediction, effectively filtering out distractor information while amplifying critical signals like structural affordances for legged robots.

The search also found references to ICLR 2026 Workshop on LLM Reasoning and other 2026 conference materials on OpenReview, though specific paper submissions combining all these exact topics weren't fully detailed in the results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17210303-fd2f-463c-940e-baea92f77cf9",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "08ad8091-645b-4c39-b3ba-597ef166f8a7",
  "sourceToolAssistantUUID": "17210303-fd2f-463c-940e-baea92f77cf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T18:27:15.095Z_

<details><summary>↩ Tool result · `toolu_011nKkvhQ5qsqXAJrNxGSEMZ`</summary>

```text
Web search results for query: "CoT-VLA affordance reasoning extension 2025 2026"

Links: [{"title":"[PDF] CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoT-VLA:-Visual-Chain-of-Thought-Reasoning-for-Zhao-Lu/2d7f3a99e916fc80ff890d109699f9682253e66d"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/394511717_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models"},{"title":"Add CoA-VLA (Chain-of-Affordance) · Issue #5 · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/issues/5"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action   Models","url":"https://arxiv.org/pdf/2503.22020"}]

Based on the search results, here's what I found about CoT-VLA and affordance reasoning extensions in 2025-2026:

## CoT-VLA (Visual Chain-of-Thought Reasoning)

CoT-VLA introduces explicit visual chain-of-thought reasoning into vision-language-action models by predicting future image frames autoregressively as visual goals before generating action sequences, with CoT-VLA being a state-of-the-art 7B VLA. CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks.

## CoA-VLA (Chain-of-Affordance Extension)

A related extension to this work is CoA-VLA, which extends the reasoning approach with affordances. CoA-VLA was presented at ICCV 2025 and introduces Chain-of-Affordance reasoning for VLAs, prompting four types of affordances before acting: (1) object affordance — what to manipulate and where, (2) grasp affordance — which part to grasp, (3) spatial affordance — optimal placement space, (4) movement affordance — collision-free path. Each affordance has visual and textual formats, injected via a novel vision-language co-injection module.

CoA-VLA outperforms OpenVLA and Octo with strong generalization to unseen poses, free space identification, and obstacle avoidance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16ad2787-2746-40ac-83b4-cb4a4e741070",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "c1aabf81-aa7c-47fd-b11e-48ef13c79fd2",
  "sourceToolAssistantUUID": "16ad2787-2746-40ac-83b4-cb4a4e741070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-18T18:27:18.044Z_

Let me run a few more targeted searches to fill in gaps on specific papers that appeared and to check for any additional very recent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1aabf81-aa7c-47fd-b11e-48ef13c79fd2",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWJpPvtShMmDGwJbd4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "593b0e7e-b131-4343-8ff3-f90a8922de95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUyqjcAGxKAbnS2Xm3hKys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5813,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5813,
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

_source line 22 · 2026-05-18T18:27:18.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C477WQSUcVHfbTUbgowGXc`</summary>

```json
{
  "query": "VLA-R1 enhancing reasoning vision language action model affordance 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "593b0e7e-b131-4343-8ff3-f90a8922de95",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWJpPvtShMmDGwJbd4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a705bdc-ab9f-481a-b96b-eff61819e76b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUyqjcAGxKAbnS2Xm3hKys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5813,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5813,
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

_source line 23 · 2026-05-18T18:27:19.405Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FfX9wQcJy5PmGkEsw4PBBt`</summary>

```json
{
  "query": "GST-VLA depth-aware chain-of-thought affordance spatial tokens 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a705bdc-ab9f-481a-b96b-eff61819e76b",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWJpPvtShMmDGwJbd4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d0f313e-30cd-4fbf-b2af-76f11cd1e532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUyqjcAGxKAbnS2Xm3hKys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5813,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5813,
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

_source line 24 · 2026-05-18T18:27:19.888Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ULfSZf89LtzLyjgXdWTLn3`</summary>

```json
{
  "query": "\"affordance field intervention\" VLA reasoning out-of-distribution 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d0f313e-30cd-4fbf-b2af-76f11cd1e532",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWJpPvtShMmDGwJbd4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dea0416-420f-4ec7-8782-9413e605d44e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUyqjcAGxKAbnS2Xm3hKys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5813,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5813,
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

_source line 25 · 2026-05-18T18:27:20.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NMgbwfdbNsELeCKcNqLmaL`</summary>

```json
{
  "query": "GTA-VLA guide think act spatially steerable affordance reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dea0416-420f-4ec7-8782-9413e605d44e",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWJpPvtShMmDGwJbd4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5844f682-9250-44f6-9600-b05127e1dd95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUyqjcAGxKAbnS2Xm3hKys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5813,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5813,
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

_source line 26 · 2026-05-18T18:27:20.814Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S8LRZAJZBSo2zzH7A5rE8Z`</summary>

```json
{
  "query": "\"learning affordances at inference-time\" VLA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5844f682-9250-44f6-9600-b05127e1dd95",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWJpPvtShMmDGwJbd4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c772204-5238-4e43-9821-eee31cfd7177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUyqjcAGxKAbnS2Xm3hKys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5813,
      "cache_read_input_tokens": 10446,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5813
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 10446,
          "cache_creation_input_tokens": 5813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5813,
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

_source line 27 · 2026-05-18T18:27:24.623Z_

<details><summary>↩ Tool result · `toolu_01C477WQSUcVHfbTUbgowGXc`</summary>

```text
Web search results for query: "VLA-R1 enhancing reasoning vision language action model affordance 2025"

Links: [{"title":"[2510.01623] VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.01623"},{"title":"Paper page - VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.01623"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.01623v1"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://gigaai-research.github.io/VLA-R1/"},{"title":"[Quick Review] VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://liner.com/review/vlar1-enhancing-reasoning-in-visionlanguageaction-models"},{"title":"[Literature Review] VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/vla-r1-enhancing-reasoning-in-vision-language-action-models"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01623v1"}]

Based on the search results, here's what I found about VLA-R1:

## Overview

VLA-R1 is a reasoning-enhanced VLA that integrates Reinforcement Learning from Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) to systematically optimize both reasoning and execution.

## Problem It Addresses

Current VLA models often lack explicit step-by-step reasoning, instead emitting final actions without considering affordance constraints or geometric relations. Their post-training pipelines also rarely reinforce reasoning quality, relying primarily on supervised fine-tuning with weak reward design.

## Key Technical Contributions

VLA-R1 designs an RLVR-based post-training strategy with verifiable rewards for region alignment, trajectory consistency, and output formatting, thereby strengthening reasoning robustness and execution accuracy. Additionally, the researchers develop VLA-CoT-13K, a high-quality dataset that provides chain-of-thought supervision explicitly aligned with affordance and trajectory annotations.

## Performance

Extensive evaluations on in-domain, out-of-domain, simulation, and real-robot platforms demonstrate that VLA-R1 achieves superior generalization and real-world performance compared to prior VLA methods. The results include achieving an IoU of 36.51 on the in-domain affordance benchmark (17.78% improvement over baselines).

The research was published on arXiv in October 2025, with code and resources available on GitHub and the project website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a705bdc-ab9f-481a-b96b-eff61819e76b",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "387f2c37-5cd1-47a3-92a9-d227e199590d",
  "sourceToolAssistantUUID": "9a705bdc-ab9f-481a-b96b-eff61819e76b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T18:27:27.007Z_

<details><summary>↩ Tool result · `toolu_01ULfSZf89LtzLyjgXdWTLn3`</summary>

```text
Web search results for query: ""affordance field intervention" VLA reasoning out-of-distribution 2025"

Links: [{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/html/2512.07472v1"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in","url":"https://www.arxiv.org/pdf/2512.07472"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01623v1"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

Based on the search results, I found a highly relevant paper matching your query:

## Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation

VLAs often reproduce memorized trajectories instead of adapting to the updated scene under distribution shifts, a failure mode referred to as the "Memory Trap". In out-of-distribution (OOD) scenarios, such as significant perturbations in object positions, these models tend to rigidly reproduce trajectories memorized from the training data.

To address this, the paper proposes Affordance Field Intervention (AFI), which augments VLA models with explicit 3D spatial reasoning via Spatial Affordance Fields. AFI is a lightweight hybrid framework that uses Spatial Affordance Fields (SAFs) as an on-demand plug-in to guide VLA behavior.

The system detects memory traps through proprioception, repositions the robot to recent high-affordance regions, and proposes affordance-driven waypoints that anchor VLA-generated actions.

The paper was published on arxiv in December 2025 and provides a solution to improve VLA robustness in out-of-distribution scenarios through spatial affordance field reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dea0416-420f-4ec7-8782-9413e605d44e",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "8fc413d3-0a91-43cd-bc61-6d67096d158d",
  "sourceToolAssistantUUID": "8dea0416-420f-4ec7-8782-9413e605d44e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T18:27:27.793Z_

<details><summary>↩ Tool result · `toolu_01FfX9wQcJy5PmGkEsw4PBBt`</summary>

```text
Web search results for query: "GST-VLA depth-aware chain-of-thought affordance spatial tokens 2026"

Links: [{"title":"[2603.09079] GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.09079"},{"title":"GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.09079"},{"title":"GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models – Own Your AI","url":"https://ownyourai.com/gst-vla-structured-gaussian-spatial-tokens-for-3d-depth-aware-vision-language-action-models/"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/394511717_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models"},{"title":"(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"}]

Based on the search results, here's what I found:

GST-VLA is a paper by Md Selim Sarowar, Omer Tariq, and Sungho Kim, published in March 2026 on arXiv.

**Key Components:**

1. **Gaussian Spatial Tokenizer (GST)**: The GST converts frozen dense depth and frozen semantic patch features into 128 anisotropic 3D Gaussian primitives, each parameterized by a metric residual mean, log-scale covariance, and learned opacity.

2. **Depth-Aware Chain-of-Thought (DA-CoT)**: DA-CoT introduces a supervised intermediate generation stage where the VLM explicitly produces four structured spatial thoughts: 3D object grounding, grasp affordance contact geometry, pairwise metric distances, and coarse SE(3) motion plan waypoints.

**Performance:**

GST-VLA achieves 96.4% on LIBERO (+2.0%), and 80.2% on SimplerEnv (+5.4%).

**Purpose:**

The model integrates structured 3D Gaussian Spatial Tokens and Depth-Aware Chain-of-Thought reasoning to improve geometric accuracy and task precision, addressing key limitations of traditional 2D patch-token VLA models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d0f313e-30cd-4fbf-b2af-76f11cd1e532",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "599133a9-ef1a-44ee-bdb8-95b02ff03e69",
  "sourceToolAssistantUUID": "2d0f313e-30cd-4fbf-b2af-76f11cd1e532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T18:27:27.891Z_

<details><summary>↩ Tool result · `toolu_01NMgbwfdbNsELeCKcNqLmaL`</summary>

```text
Web search results for query: "GTA-VLA guide think act spatially steerable affordance reasoning 2026"

Links: [{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.09079"},{"title":"ST4VLA: Spatially Guided Training for Vision-Language-Action Model","url":"https://arxiv.org/html/2602.10109"},{"title":"[2603.22760] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/abs/2603.22760"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/pdf/2603.22760"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning","url":"https://arxiv.org/pdf/2507.16815"}]

Based on the search results, I found several relevant papers on Vision-Language-Action (VLA) models with spatial reasoning and affordance concepts from 2026, though I didn't find a specific paper with that exact title combination. Here are the most relevant findings:

**ThinkAct: Vision-Language-Action Reasoning** - ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards, with reasoning plans compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments.

**ST4VLA: Spatially Guided Training** - A dual-system, end-to-end VLA framework based on Qwen2.5-VL that fosters alignment between the optimization dynamics of the spatial grounding objective and the action policy objective. The VLM planner is aligned with a broad range of spatial grounding data, both real and synthetic, covering tasks such as object detection, affordance recognition, and visual trajectory planning.

**SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models** - This model co-trains auxiliary decoders that reconstruct interpretable intermediate signals including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks from shared visual-language features to encourage spatially grounded, manipulation-aware latent representations.

These papers represent recent advances in combining spatial reasoning, affordance detection, and action planning in VLA models from early 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5844f682-9250-44f6-9600-b05127e1dd95",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "496adf15-334c-4055-9884-95e84cd2abc0",
  "sourceToolAssistantUUID": "5844f682-9250-44f6-9600-b05127e1dd95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T18:27:34.032Z_

<details><summary>↩ Tool result · `toolu_01S8LRZAJZBSo2zzH7A5rE8Z`</summary>

```text
Web search results for query: ""learning affordances at inference-time" VLA 2025"

Links: [{"title":"[2510.19752] Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.19752"},{"title":"LITEN: Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://liten-vla.github.io/"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251019752S/abstract"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.19752"},{"title":"[Literature Review] Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/learning-affordances-at-inference-time-for-vision-language-action-models"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"Quick and Accurate Affordance Learning","url":"https://arxiv.org/pdf/2405.07816"},{"title":"MAIN-VLA: Modeling Abstraction of Intention and eNvironment for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.02212"}]

I found results for your search! Here's what I found about "Learning Affordances at Inference-Time for Vision-Language-Action Models":

## Main Result

The paper introduces Learning from Inference-Time Execution (LITEN), which connects a VLA low-level policy to a high-level VLM that conditions on past experiences by including them in-context, allowing it to learn the affordances and capabilities of the low-level VLA.

## Key Features

The approach iterates between a reasoning phase that generates and executes plans for the low-level VLA, and an assessment phase that reflects on the resulting execution and draws useful conclusions to be included in future reasoning contexts, requiring structured guiderails when reflecting on unstructured real-world robot trajectories like raw videos.

Experimental results demonstrate LITEN is able to effectively learn from past experience to generate plans that use high-affordance instructions to accomplish long-horizon tasks.

## Background Problem

Vision-Language-Action models (VLAs) offer a promising path towards solving complex control tasks, but lack the ability to contextually and dynamically readjust behavior when they fail to accomplish a task.

The paper was published in October 2025 and comes from authors at UC Berkeley and Physical Intelligence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c772204-5238-4e43-9821-eee31cfd7177",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "d52fe91d-f468-4485-945d-932f2f52cd43",
  "sourceToolAssistantUUID": "7c772204-5238-4e43-9821-eee31cfd7177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-18T18:27:37.151Z_

Now let me search for a couple more specific items that appeared in earlier results and check for the most recent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d52fe91d-f468-4485-945d-932f2f52cd43",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWLDPosYFxftbViF9gR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d03708a5-18b5-4107-9eda-2490aac13969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVSBuPq1jZ32izFhxmeHe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3839,
      "cache_read_input_tokens": 16259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3839,
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

_source line 33 · 2026-05-18T18:27:37.704Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TKsQ3ZKv3LS3Puf1G9yG7J`</summary>

```json
{
  "query": "ACoT-VLA action chain-of-thought vision language action affordance 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d03708a5-18b5-4107-9eda-2490aac13969",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWLDPosYFxftbViF9gR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42b6579b-af7e-4a94-8bb1-ab4eb22fb3b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVSBuPq1jZ32izFhxmeHe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3839,
      "cache_read_input_tokens": 16259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3839,
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

_source line 34 · 2026-05-18T18:27:38.593Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QZCVziAK8YoeLNNJRbdpa8`</summary>

```json
{
  "query": "\"open vocabulary\" affordance autoregressive token generation robot policy 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42b6579b-af7e-4a94-8bb1-ab4eb22fb3b4",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWLDPosYFxftbViF9gR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3f9aced-fa37-45dd-9c5a-cc2f7d6dfe61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVSBuPq1jZ32izFhxmeHe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3839,
      "cache_read_input_tokens": 16259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3839,
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

_source line 35 · 2026-05-18T18:27:38.972Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GF8pM8sJTqKCW3Vb7mLKrh`</summary>

```json
{
  "query": "AR-VLA true autoregressive action expert vision language action 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f9aced-fa37-45dd-9c5a-cc2f7d6dfe61",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWLDPosYFxftbViF9gR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63056fdb-2090-456d-896c-d9d44578c442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVSBuPq1jZ32izFhxmeHe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3839,
      "cache_read_input_tokens": 16259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3839,
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

_source line 36 · 2026-05-18T18:27:47.264Z_

<details><summary>↩ Tool result · `toolu_01QZCVziAK8YoeLNNJRbdpa8`</summary>

```text
Web search results for query: ""open vocabulary" affordance autoregressive token generation robot policy 2025 2026"

Links: [{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"},{"title":"RoboAfford: A Dataset and Benchmark for Enhancing Object and Spatial Affordance Learning in Robot Manipulation | Request PDF","url":"https://www.researchgate.net/publication/396941670_RoboAfford_A_Dataset_and_Benchmark_for_Enhancing_Object_and_Spatial_Affordance_Learning_in_Robot_Manipulation"},{"title":"Autoregressive Action Sequence Learning for Robotic Manipulation","url":"https://arxiv.org/pdf/2410.03132"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"OAT: Ordered Action Tokenization","url":"https://arxiv.org/pdf/2602.04215"},{"title":"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot   Manipulation through LLM Affordance-Grounding","url":"https://arxiv.org/pdf/2404.11000"},{"title":"GLOVER: Generalizable Open-Vocabulary Affordance ...","url":"https://corl25-genpriors.github.io/Papers/22_GLOVER_Generalizable_Open_V.pdf"}]

Here are the search results for your query about open vocabulary affordance autoregressive token generation in robot policy research for 2025-2026:

The search returned several relevant papers and resources:

1. **VQ-VLA and Discrete Diffusion Models** - VQ-VLA: "Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers" was presented at ICCV 2025, and discrete diffusion models are being used for parallel action token generation instead of autoregressive decoding.

2. **FASTer Framework** - FASTer is a unified framework integrating a learnable tokenizer with an autoregressive policy, where FASTerVLA builds on this tokenizer with block-wise autoregressive decoding and achieves faster inference and higher task performance.

3. **OAT (Ordered Action Tokenization)** - OAT enables prefix-based detokenization where early tokens produce coarse action chunks, and additional autoregressive steps progressively refine actions.

4. **Open-Vocabulary Affordance Methods** - OVAL-Prompt is a prompt-based approach for open-vocabulary affordance localization that leverages a Vision Language Model for object part segmentation and an LLM to ground part-segment-affordance relationships.

5. **Affordance Learning** - Recent 2025 work includes "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation".

These papers represent current research directions combining open vocabulary understanding, affordance learning, and autoregressive token generation for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3f9aced-fa37-45dd-9c5a-cc2f7d6dfe61",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "ef9c5455-e3e3-4497-8994-058ad0232e6d",
  "sourceToolAssistantUUID": "d3f9aced-fa37-45dd-9c5a-cc2f7d6dfe61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T18:27:47.582Z_

<details><summary>↩ Tool result · `toolu_01TKsQ3ZKv3LS3Puf1G9yG7J`</summary>

```text
Web search results for query: "ACoT-VLA action chain-of-thought vision language action affordance 2026"

Links: [{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models (Jan 2026) - YouTube","url":"https://www.youtube.com/watch?v=43yUDoGKh9w"},{"title":"[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/abs/2601.11404"},{"title":"[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"},{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://huggingface.co/papers/2601.11404"},{"title":"(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2601.11404"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/html/2601.11404v2"}]

Based on the search results, here's what I found about ACoT-VLA:

## Overview

ACoT-VLA introduces Action Chain-of-Thought (ACoT), a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy.

## Architecture

ACoT-VLA is a novel architecture that materializes the ACoT paradigm through two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR). The former proposes coarse reference trajectories as explicit action-level reasoning steps, while the latter extracts latent action priors from internal representations of multimodal input, co-forming an ACoT that conditions the downstream action head to enable grounded policy learning.

## Performance

Extensive experiments in real-world and simulation environments demonstrate achievements of 98.5%, 84.1%, and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively. Additionally, ACoT-VLA demonstrates significant improvements, particularly in the LIBERO-Long suite, by reducing ambiguity in mapping observations to actions.

## Publication Status

This repository serves as the official baseline implementation for the AgiBot World Challenge @ ICRA 2026. The paper was submitted to arXiv in January 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42b6579b-af7e-4a94-8bb1-ab4eb22fb3b4",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "46d6ecfd-8c2d-49a4-919f-fd9cd2ab9755",
  "sourceToolAssistantUUID": "42b6579b-af7e-4a94-8bb1-ab4eb22fb3b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T18:27:48.960Z_

<details><summary>↩ Tool result · `toolu_01GF8pM8sJTqKCW3Vb7mLKrh`</summary>

```text
Web search results for query: "AR-VLA true autoregressive action expert vision language action 2026"

Links: [{"title":"AR-VLA: True Autoregressive Action Expert for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.10126"},{"title":"[2603.10126] AR-VLA: True Autoregressive Action Expert for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.10126"},{"title":"AR-VLA: True Autoregressive Action Expert for Vision–Language–Action Models","url":"https://arxiv.org/html/2603.10126v1"},{"title":"AR-VLA: Autoregressive Action Expert for Vision ...","url":"https://arxiv.org/html/2603.10126v2"},{"title":"FASTer: Toward Efficient Autoregressive Vision Language Action Modeling via neural Action Tokenization","url":"https://arxiv.org/html/2512.04952"}]

I found research on AR-VLA! Here's what the search results reveal:

AR-VLA: True Autoregressive Action Expert for Vision-Language-Action Models is a research paper by Yutong Hu, Jan-Nico Zaech, Nikolay Nikolov, Yuanqi Yao, and others from INSAIT at Sofia University and KU Leuven.

**Key Innovation:**

The research proposes a standalone autoregressive Action Expert that generates actions as a continuous causal sequence while conditioning on refreshable vision-language prefixes. In contrast to existing Vision-Language-Action (VLA) models and diffusion policies that reset temporal context with each new observation, this Action Expert maintains its own history through a long-lived memory and is inherently context-aware.

**Main Benefits:**

This structure addresses the frequency mismatch between fast control and slow reasoning, enabling efficient independent pretraining of kinematic syntax and modular integration with heavy perception backbones, naturally ensuring spatio-temporally consistent action generation across frames.

To synchronize these asynchronous hybrid V-L-A modalities, the researchers utilize a re-anchoring mechanism that mathematically accounts for perception staleness during both training and inference.

The paper was published on arXiv in March 2026 and demonstrates applications to both simulated and real-robot manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63056fdb-2090-456d-896c-d9d44578c442",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "42a03d4d-9c59-4ebf-b3f1-265e4c16db27",
  "sourceToolAssistantUUID": "63056fdb-2090-456d-896c-d9d44578c442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T18:27:52.090Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XSZDxfsjdad6swvytr8AKw`</summary>

```json
{
  "query": "CoA-VLA authors Jinming Li open vocabulary affordance types ICCV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42a03d4d-9c59-4ebf-b3f1-265e4c16db27",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWMKCLovhwSyd5tHppe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d58015a-f7ba-41ca-85fe-bdf717f971c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQKRwab4GT9UBFGihYnQBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 20098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2607,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 40 · 2026-05-18T18:27:52.523Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GANyuBkLfgcC493pdkUE13`</summary>

```json
{
  "query": "ST4VLA spatially guided training affordance recognition VLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d58015a-f7ba-41ca-85fe-bdf717f971c6",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWMKCLovhwSyd5tHppe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aefc29bf-a130-43f4-939c-60c2796877a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQKRwab4GT9UBFGihYnQBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 20098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2607,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 41 · 2026-05-18T18:27:53.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HfL5fFgQALEkKahKxxspyi`</summary>

```json
{
  "query": "ThinkAct VLA reasoning reinforced visual latent planning affordance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aefc29bf-a130-43f4-939c-60c2796877a9",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWMKCLovhwSyd5tHppe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fe6039e-8825-46ae-b32a-80b4cd155ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQKRwab4GT9UBFGihYnQBY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 20098,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 20098,
          "cache_creation_input_tokens": 2607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2607,
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

_source line 42 · 2026-05-18T18:27:58.236Z_

<details><summary>↩ Tool result · `toolu_01HfL5fFgQALEkKahKxxspyi`</summary>

```text
Web search results for query: "ThinkAct VLA reasoning reinforced visual latent planning affordance 2025 2026"

Links: [{"title":"ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning | Research","url":"https://research.nvidia.com/publication/2025-12_thinkact-vision-language-action-reasoning-reinforced-visual-latent-planning"},{"title":"ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning","url":"https://arxiv.org/pdf/2507.16815"},{"title":"ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning","url":"https://jasper0314-huang.github.io/thinkact-vla/"},{"title":"[2507.16815] ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning","url":"https://arxiv.org/abs/2507.16815"},{"title":"(PDF) ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning","url":"https://www.researchgate.net/publication/393923382_ThinkAct_Vision-Language-Action_Reasoning_via_Reinforced_Visual_Latent_Planning"},{"title":"Paper page - ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning","url":"https://huggingface.co/papers/2507.16815"},{"title":"NVIDIA AI Presents ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning - MarkTechPost","url":"https://www.marktechpost.com/2025/07/30/nvidia-ai-presents-thinkact-vision-language-action-reasoning-via-reinforced-visual-latent-planning/"}]

Based on the search results, here's what I found about ThinkAct:

## Overview

ThinkAct is a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning.

## How It Works

ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments.

## Problem It Addresses

Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations.

## Key Capabilities

Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

## Source Information

The research was conducted by researchers from Nvidia and National Taiwan University, with the paper published in July 2025 on arXiv (arxiv.org/pdf/2507.16815).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fe6039e-8825-46ae-b32a-80b4cd155ae0",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "55d30dff-a9ef-45be-8945-98afc8e8b6e6",
  "sourceToolAssistantUUID": "6fe6039e-8825-46ae-b32a-80b4cd155ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-18T18:27:58.590Z_

<details><summary>↩ Tool result · `toolu_01GANyuBkLfgcC493pdkUE13`</summary>

```text
Web search results for query: "ST4VLA spatially guided training affordance recognition VLA 2026"

Links: [{"title":"Robots Learn To Act On Instructions With Improved Spatial Awareness","url":"https://quantumzeitgeist.com/robots-learn-act-instructions-spatial/"},{"title":"(PDF) ST4VLA: Spatially Guided Training for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/400661387_ST4VLA_Spatially_Guided_Training_for_Vision-Language-Action_Models"},{"title":"ST4VLA: Spatially Guided Training for Vision-Language-Action Model","url":"https://arxiv.org/html/2602.10109"},{"title":"SP-VLA: SPATIALLY GUIDED TRAINING FOR VISION","url":"https://openreview.net/pdf?id=eKhOrQWAVJ"},{"title":"st4vla: spatially guided training for vision","url":"https://arxiv.org/pdf/2602.10109"},{"title":"[2602.10109] ST4VLA: Spatially Guided Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.10109"},{"title":"[Literature Review] ST4VLA: Spatially Guided Training for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/st4vla-spatially-guided-training-for-vision-language-action-models"}]

Based on the search results, here's what I found about ST4VLA:

## Overview

ST4VLA is a novel dual-system Vision-Language-Action framework presented by Jinhui Ye, Fangjing Wang from Southern University of Science and Technology, and Ning Gao from Shanghai AI Laboratory.

## Core Concept

ST4VLA leverages Spatial Guided Training to align action learning with spatial priors in VLMs. The work introduces Spatially Guided Training to better align action learning with spatial reasoning within vision-language models.

## Two-Stage Training Pipeline

The VLM planner acquires transferable spatial priors (point, box, trajectory) by unifying web-scale multimodal grounding data with robot-specific datasets, thereby equipping the model with affordance grounding, localization, and trajectory reasoning. In the second stage, the action expert is conditioned on these spatial priors through lightweight spatial prompting, aligning optimization between perception and control while preserving the VLM's grounding capacity.

## Performance

ST4VLA improves robotic performance on benchmarks such as Google Robot and WidowX Robot, achieving new state-of-the-art results and exhibiting enhanced generalisation and robustness in real-world scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aefc29bf-a130-43f4-939c-60c2796877a9",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "85309816-b8bd-4204-8fde-7d01b26372bd",
  "sourceToolAssistantUUID": "aefc29bf-a130-43f4-939c-60c2796877a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T18:27:58.651Z_

<details><summary>↩ Tool result · `toolu_01XSZDxfsjdad6swvytr8AKw`</summary>

```text
Web search results for query: "CoA-VLA authors Jinming Li open vocabulary affordance types ICCV 2025"

Links: [{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"},{"title":"CoA-VLA","url":"https://chain-of-affordance.github.io/"},{"title":"All Papers - ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/ICCV2025?day=all"},{"title":"bibtex - ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/ICCV2025?day=2025-10-21"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"[PDF] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoA-VLA:-Improving-Vision-Language-Action-Models-Li-Zhu/5760cc722b5eabc14487e9c497a78038ab46f37d"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"}]

Based on the search results, here's what I found about the CoA-VLA paper:

## Paper Information

The authors of CoA-VLA are Jinming Li, Yichen Zhu, Zhibin Tang, Junjie Wen, Minjie Zhu, Xiaoyu Liu, Chengmeng Li, Ran Cheng, Yaxin Peng, Yan Peng, and Feifei Feng. Jinming Li and Yichen Zhu are from Midea Group and Shanghai University, while Junjie Wen and Minjie Zhu are from East China Normal University.

## Research Focus

The paper introduces Chain-of-Affordance (CoA-VLA), a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances. The method involves designing four distinct types of affordance and introducing a novel visual-text co-injection method to integrate this knowledge into the decision-making process.

## Key Results

CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks, and exhibits strong generalization capabilities, including recognizing unseen object poses, identifying free space, and avoiding obstacles in novel environments.

The paper was accepted at ICCV 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d58015a-f7ba-41ca-85fe-bdf717f971c6",
  "isSidechain": true,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "agentId": "a479979600018ba92",
  "type": "user",
  "uuid": "d2a45aba-1251-46dd-b2c7-6ddac5590110",
  "sourceToolAssistantUUID": "4d58015a-f7ba-41ca-85fe-bdf717f971c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-18T18:29:03.648Z_

Here is my comprehensive report on concurrent and recent work (2025-2026) on open-vocabulary affordance reasoning in Vision-Language-Action models.

---

## Landscape Analysis: Open-Vocabulary Affordance Reasoning in VLAs (2025-2026)

### MOST CLOSELY RELATED WORK (Highest Overlap)

#### 1. CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance
- **Authors:** Jinming Li, Yichen Zhu, Zhibin Tang, Junjie Wen, Minjie Zhu, Xiaoyu Liu, Chengmeng Li, Ran Cheng, Yaxin Peng, Yan Peng, Feifei Feng (Midea Group, Shanghai University, East China Normal University)
- **Venue/Date:** ICCV 2025 (arXiv Dec 2024)
- **Relevance: HIGH -- this is the most directly comparable work.** CoA-VLA generates a structured "chain of affordance" before action prediction, covering four affordance types: (1) object affordance, (2) grasp affordance, (3) spatial affordance, (4) movement affordance. Each affordance is represented in both visual and textual form and injected via a co-injection module. However, the affordance vocabulary is structured around four predefined categories rather than being truly open-vocabulary/free-form. The affordances also do not appear to be generated as autoregressive tokens in a unified sequence with action tokens -- they are injected via a separate module. This is a key architectural difference from a unified autoregressive approach.

#### 2. VLA-R1: Enhancing Reasoning in Vision-Language-Action Models
- **Authors:** GigaAI Research (project page: gigaai-research.github.io/VLA-R1)
- **Venue/Date:** arXiv October 2025
- **Relevance: HIGH.** VLA-R1 creates VLA-CoT-13K, a dataset with chain-of-thought supervision explicitly aligned with affordance and trajectory annotations. It uses RLVR (Reinforcement Learning from Verifiable Rewards) with GRPO to optimize both reasoning and execution. The chain-of-thought includes affordance reasoning before actions. This is conceptually similar to generating affordance reasoning tokens before action tokens, though it uses RL-based post-training rather than a purely autoregressive generation approach, and its affordance reasoning is trained through supervised CoT + RL rather than emerging from a unified autoregressive objective.

#### 3. GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware VLA Models
- **Authors:** Md Selim Sarowar, Omer Tariq, Sungho Kim
- **Venue/Date:** arXiv March 2026
- **Relevance: HIGH.** GST-VLA introduces a "Depth-Aware Chain-of-Thought" (DA-CoT) where the model explicitly generates four structured spatial reasoning steps before action generation: 3D object grounding, grasp affordance contact geometry, pairwise metric distances, and SE(3) motion plan waypoints. This is very close to the idea of generating intermediate affordance reasoning tokens before action tokens in an autoregressive sequence, but is specifically structured around 3D geometric affordances (not open-vocabulary), and uses 3D Gaussian spatial tokens rather than language tokens.

#### 4. ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models
- **Authors:** AgibotTech
- **Venue/Date:** CVPR 2026 (arXiv January 2026)
- **Relevance: HIGH.** ACoT-VLA formulates reasoning as a structured sequence of coarse action intents (explicit action reasoning) that guide the final policy. It has two components: an Explicit Action Reasoner (EAR) that proposes coarse reference trajectories as reasoning steps, and an Implicit Action Reasoner (IAR) that extracts latent action priors. The "chain of thought" here is action-level rather than affordance-level, and it is not open-vocabulary text reasoning -- it is structured trajectory-level reasoning.

---

### MODERATELY RELATED WORK

#### 5. CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models
- **Authors:** Zhao, Lu et al.
- **Venue/Date:** arXiv March 2025
- **Relevance: MODERATE.** Predicts future image frames autoregressively as visual goals before generating action sequences. The "reasoning" is visual (future frames) rather than affordance-based or language-based. Not open-vocabulary affordance reasoning.

#### 6. ST4VLA: Spatially Guided Training for Vision-Language-Action Models
- **Authors:** Jinhui Ye, Fangjing Wang (SUSTech), Ning Gao (Shanghai AI Lab)
- **Venue/Date:** arXiv February 2026
- **Relevance: MODERATE.** Uses spatial priors (point, box, trajectory) including affordance grounding to align the VLM planner, then conditions the action expert on these spatial priors. The affordance component is part of spatial training rather than being open-vocabulary affordance tokens in the autoregressive stream.

#### 7. ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning
- **Authors:** NVIDIA, National Taiwan University
- **Venue/Date:** arXiv July 2025
- **Relevance: MODERATE.** Generates embodied reasoning plans that are compressed into a visual plan latent before action execution. The reasoning is visual/latent rather than explicit open-vocabulary affordance tokens.

#### 8. LITEN: Learning Affordances at Inference-Time for VLAs
- **Authors:** UC Berkeley, Physical Intelligence
- **Venue/Date:** arXiv October 2025
- **Relevance: MODERATE.** Uses a high-level VLM to learn affordances of a low-level VLA at inference time through in-context learning from past execution experiences. This is about learning which instructions are high-affordance (achievable) rather than generating affordance reasoning tokens in-line.

#### 9. Affordance Field Intervention (AFI)
- **Authors:** (arXiv December 2025)
- **Venue/Date:** arXiv December 2025
- **Relevance: MODERATE.** A plug-in module that uses 3D Spatial Affordance Fields to guide VLA behavior under distribution shift. Not about generating affordance tokens autoregressively.

#### 10. AR-VLA: True Autoregressive Action Expert for VLA Models
- **Authors:** INSAIT (Sofia University), KU Leuven (Yutong Hu, Jan-Nico Zaech, et al.)
- **Venue/Date:** arXiv March 2026
- **Relevance: LOW-MODERATE.** Focuses on making the action generation truly autoregressive with a standalone action expert maintaining temporal context. No affordance reasoning component -- the contribution is about temporal autoregressive action consistency.

---

### PERIPHERAL WORK (Lower Overlap but Relevant Context)

#### 11. SG-VLA: Spatially-Grounded VLA Models for Mobile Manipulation
- **Venue/Date:** arXiv March 2026
- Co-trains auxiliary decoders for grasp affordances, target-object pose, and segmentation from shared features. Not autoregressive affordance token generation.

#### 12. GLOVER: Generalizable Open-Vocabulary Affordance Reasoning for Task-Oriented Grasping
- **Venue/Date:** 2025
- Open-vocabulary affordance but for grasping only, not a VLA with autoregressive token generation.

#### 13. 3D-AffordanceLLM: Open-Vocabulary Affordance Detection in 3D Worlds
- **Venue/Date:** arXiv February 2025
- Uses LLMs for open-vocabulary 3D affordance segmentation. Not a VLA or action generation model.

#### 14. Survey: A Survey on VLA Models: An Action Tokenization Perspective (arXiv July 2025)
- Categorizes VLA action token types including "affordance" as one distinct token category alongside language, code, trajectory, goal state, latent, raw action, and reasoning tokens. Useful framing paper.

---

### KEY FINDINGS AND GAP ANALYSIS

**No one is doing exactly what you describe.** The specific idea of "generating open-vocabulary affordance reasoning tokens before action tokens in a unified autoregressive VLA" has no exact match in the literature. Here is why:

1. **CoA-VLA** (the closest) uses structured affordance reasoning but with (a) a fixed taxonomy of 4 affordance types rather than open-vocabulary, and (b) a separate co-injection module rather than a unified autoregressive token sequence.

2. **VLA-R1** uses affordance-aligned CoT supervision but trains with RL post-training, not a purely unified autoregressive objective.

3. **GST-VLA** generates structured spatial reasoning (including affordance) before actions, but the affordance types are fixed (3D geometric) and the tokens are spatial Gaussian tokens, not open-vocabulary language tokens.

4. **ACoT-VLA** generates reasoning before actions autoregressively, but the reasoning is coarse action trajectories, not open-vocabulary affordance descriptions.

5. **No paper combines all three of:** (a) open-vocabulary/free-form affordance descriptions, (b) generated as autoregressive tokens in the same sequence, (c) preceding action tokens in a unified VLA architecture.

**The gap your idea fills:** Existing work either uses fixed affordance taxonomies (CoA-VLA), or generates non-affordance reasoning (CoT-VLA generates future frames, ACoT-VLA generates coarse trajectories), or uses separate modules for affordance injection rather than unifying it in the autoregressive stream. A truly open-vocabulary, autoregressive, in-stream affordance reasoning approach before action token generation appears to be novel.

**Caution:** The field is moving extremely fast (multiple new *-VLA papers per month in early 2026). CoA-VLA at ICCV 2025 and ACoT-VLA at CVPR 2026 establish the "reason before acting" paradigm for VLAs, so the conceptual foundation is clearly in the air. Differentiating on the "open-vocabulary" and "unified autoregressive" aspects will be critical.

---

Sources:
- [CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance (ICCV 2025)](https://arxiv.org/abs/2412.20451)
- [CoA-VLA Project Page](https://chain-of-affordance.github.io/)
- [VLA-R1: Enhancing Reasoning in Vision-Language-Action Models](https://arxiv.org/abs/2510.01623)
- [GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware VLA Models](https://arxiv.org/abs/2603.09079)
- [ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models (CVPR 2026)](https://arxiv.org/abs/2601.11404)
- [CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models](https://arxiv.org/pdf/2503.22020)
- [ST4VLA: Spatially Guided Training for Vision-Language-Action Models](https://arxiv.org/abs/2602.10109)
- [ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (NVIDIA)](https://arxiv.org/abs/2507.16815)
- [LITEN: Learning Affordances at Inference-Time for VLA Models](https://arxiv.org/abs/2510.19752)
- [Affordance Field Intervention: Enabling VLAs to Escape Memory Traps](https://arxiv.org/pdf/2512.07472)
- [AR-VLA: True Autoregressive Action Expert for VLA Models](https://arxiv.org/abs/2603.10126)
- [SG-VLA: Learning Spatially-Grounded VLA Models for Mobile Manipulation](https://arxiv.org/abs/2603.22760)
- [A Survey on VLA Models: An Action Tokenization Perspective](https://arxiv.org/abs/2507.01925)
- [3D-AffordanceLLM: Open-Vocabulary Affordance Detection in 3D Worlds](https://arxiv.org/pdf/2502.20041)
- [FASTer: Toward Efficient Autoregressive VLA Models](https://openreview.net/forum?id=k6nTUFoqeT)
- [GLOVER: Generalizable Open-Vocabulary Affordance Reasoning for Task-Oriented Grasping](https://corl25-genpriors.github.io/Papers/22_GLOVER_Generalizable_Open_V.pdf)
- [Awesome Embodied VLA Collection (GitHub)](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2a45aba-1251-46dd-b2c7-6ddac5590110",
  "isSidechain": true,
  "agentId": "a479979600018ba92",
  "requestId": "req_011CbAWN36VbjYDhJvnuuGui",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c04faff3-cc22-4d27-8483-80ecf6464234",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVcpQc6QXBu9QN9REPMKWE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1484,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 22705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1111,
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
