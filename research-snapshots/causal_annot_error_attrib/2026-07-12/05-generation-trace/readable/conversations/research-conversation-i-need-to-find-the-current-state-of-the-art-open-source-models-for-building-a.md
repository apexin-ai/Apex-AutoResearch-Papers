# Research conversation: I need to find the current state-of-the-art open-source models for building a Vision-Language-Action (VLA) system in 202

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a85bd974213dd0e1a.jsonl`
- **Structured JSON:** [`babb2e1bc579f52179b8.json`](../../sessions/ba/babb2e1bc579f52179b8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-18T18:44:30.581Z_

I need to find the current state-of-the-art open-source models for building a Vision-Language-Action (VLA) system in 2026. Search for:

1. WebSearch: "best open source VLA model 2026 robot manipulation"
2. WebSearch: "SOTA open source vision language action model 2026"
3. WebSearch: "open source VLA robot 2026 OpenVLA pi0"
4. WebSearch: "best open source LLM 2026 May"
5. WebSearch: "best open source vision language model 2026"
6. WebSearch: "open source multimodal LLM 2026 SOTA"
7. WebSearch: "OpenVLA 2 2026" or similar next-gen VLA models

For each category, report:
- Model name, organization, date released
- Key capabilities and benchmarks
- Whether it's suitable as a backbone for affordance-aware VLA research
- Model size variants available
- License

I need the CURRENT frontier models, not older ones from 2024. Focus on what's available NOW (May 2026).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "17979ae4-0c3f-4632-b9f0-f6240772ae82",
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

_source line 2 · 2026-05-18T18:44:30.588Z_

```json
{
  "parentUuid": "17979ae4-0c3f-4632-b9f0-f6240772ae82",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
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
  "uuid": "aed6820d-f26b-4895-87b1-fa0841a3a053",
  "timestamp": "2026-05-18T18:44:30.588Z",
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

_source line 3 · 2026-05-18T18:44:32.982Z_



I'll search for all of these topics in parallel. Let me first load the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aed6820d-f26b-4895-87b1-fa0841a3a053",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXd9bhhn9xjXCtmSVVZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5922b7be-c3de-419a-9d0b-daf9b28d647f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YPit8KBNQAyrCDU6a7Cg9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 782,
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

_source line 4 · 2026-05-18T18:44:33.454Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01V9ei1w2MG9J12MNLFLm7AA`</summary>

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
  "parentUuid": "5922b7be-c3de-419a-9d0b-daf9b28d647f",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXd9bhhn9xjXCtmSVVZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9272d5b6-afe0-429e-b83a-cc592f67795f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YPit8KBNQAyrCDU6a7Cg9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 7304,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 782
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 782,
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

_source line 5 · 2026-05-18T18:44:33.457Z_

<details><summary>↩ Tool result · `toolu_01V9ei1w2MG9J12MNLFLm7AA`</summary>

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
  "parentUuid": "9272d5b6-afe0-429e-b83a-cc592f67795f",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "f0dad409-32d6-4b41-bc81-d650ee2bd8da",
  "sourceToolAssistantUUID": "9272d5b6-afe0-429e-b83a-cc592f67795f",
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

_source line 6 · 2026-05-18T18:44:35.936Z_



Now let me run all 7 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0dad409-32d6-4b41-bc81-d650ee2bd8da",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXdNTrNjgACo5i1cpcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca9acc7f-08e4-4f0d-9803-20dc226f5be8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FWCGDuLeh8xXQi97BpwRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 7 · 2026-05-18T18:44:36.882Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EnfK6R6CfNMkENES9ZbLYs`</summary>

```json
{
  "query": "best open source VLA model 2026 robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca9acc7f-08e4-4f0d-9803-20dc226f5be8",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXdNTrNjgACo5i1cpcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ff05a7d-c1ff-445b-a72b-15b66445bfe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FWCGDuLeh8xXQi97BpwRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 8 · 2026-05-18T18:44:37.357Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V91DKX7jrKxzg3wnbkPNqd`</summary>

```json
{
  "query": "SOTA open source vision language action model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ff05a7d-c1ff-445b-a72b-15b66445bfe1",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXdNTrNjgACo5i1cpcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0621a474-af50-45b0-9ac8-17ad2a50891a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FWCGDuLeh8xXQi97BpwRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 9 · 2026-05-18T18:44:38.370Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B21yZVcEXDEcR4gnXNYxTq`</summary>

```json
{
  "query": "open source VLA robot 2026 OpenVLA pi0 successor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0621a474-af50-45b0-9ac8-17ad2a50891a",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXdNTrNjgACo5i1cpcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a5a3191-b73c-4843-a317-9ce8aa21fe82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FWCGDuLeh8xXQi97BpwRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 10 · 2026-05-18T18:44:38.373Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Asrd5bF7rxTvRijNVqEzwr`</summary>

```json
{
  "query": "best open source LLM 2026 May"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a5a3191-b73c-4843-a317-9ce8aa21fe82",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXdNTrNjgACo5i1cpcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e4b485b-fcbe-4529-b282-7cc3e3d4dc8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FWCGDuLeh8xXQi97BpwRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 11 · 2026-05-18T18:44:38.837Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HLzLz8h3F6mHw1WDp8Z9ZR`</summary>

```json
{
  "query": "best open source vision language model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e4b485b-fcbe-4529-b282-7cc3e3d4dc8f",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXdNTrNjgACo5i1cpcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fcf4ef1-6ef2-499d-945d-9f4f75459e7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FWCGDuLeh8xXQi97BpwRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 12 · 2026-05-18T18:44:39.306Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012P4XFrwPdePU5G2dng37WV`</summary>

```json
{
  "query": "open source multimodal LLM 2026 SOTA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fcf4ef1-6ef2-499d-945d-9f4f75459e7d",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXdNTrNjgACo5i1cpcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "027dd873-61d5-4dae-ad31-63ca4df95116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FWCGDuLeh8xXQi97BpwRi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 13 · 2026-05-18T18:44:39.882Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ljxk3fd3M3LDhYbpVSrwky`</summary>

```json
{
  "query": "OpenVLA 2 2026 next generation VLA model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "027dd873-61d5-4dae-ad31-63ca4df95116",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXdNTrNjgACo5i1cpcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b0711e0-8f8e-4a24-9fb0-ca3bdca968be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FWCGDuLeh8xXQi97BpwRi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8086,
      "output_tokens": 356,
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
          "output_tokens": 356,
          "cache_read_input_tokens": 8086,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1415,
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

_source line 14 · 2026-05-18T18:44:46.324Z_

<details><summary>↩ Tool result · `toolu_01EnfK6R6CfNMkENES9ZbLYs`</summary>

```text
Web search results for query: "best open source VLA model 2026 robot manipulation"

Links: [{"title":"Top 10 Physical AI Models Powering Real-World Robots in 2026 - MarkTechPost","url":"https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/"},{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/learn/vla-models-comparison"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Robbyant Open-Sources LingBot-VLA as a “Universal Brain” for Robots | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/26071/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"}]

Based on the search results, here are the leading open-source VLA (Vision-Language-Action) models for robot manipulation in 2026:

## Top Open-Source Models

**OpenVLA** is a prominent choice: OpenVLA is a 7B-parameter open-source VLA trained on a diverse collection of 970,000 real-world robot demonstrations. Despite being 7× smaller, OpenVLA outperforms the closed RT-2-X (55B parameters) by 16.5 percentage points in absolute task success rate across 29 tasks and multiple robot embodiments.

**SmolVLA** offers another strong open-source option: On the LIBERO benchmark, SmolVLA achieves 82–90% success — within 5% of OpenVLA despite having 16x fewer parameters. On real-robot evaluations, fine-tuned SmolVLA matches OpenVLA on simple tasks and slightly underperforms on complex multi-step tasks. The key advantage is inference speed: SmolVLA runs at 15–30 Hz on a single RTX 4090, fast enough for reactive manipulation.

**LingBot-VLA** is another recent open-source release: Robbyant announced the open-source release of LingBot-VLA, a vision-language-action (VLA) model designed to serve as a "universal brain" for real-world robotics. In tests conducted across three distinct physical robot platforms, LingBot-VLA achieved higher task success rates than other evaluated models.

**A1** is an emerging option focused on efficiency: A1 is a fully open-source and transparent VLA framework designed for low-cost, high-throughput inference without sacrificing manipulation success, and releases the full training stack to enable end-to-end reproducibility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ff05a7d-c1ff-445b-a72b-15b66445bfe1",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "8d2401db-eecb-4616-b3da-1aa3db71d897",
  "sourceToolAssistantUUID": "4ff05a7d-c1ff-445b-a72b-15b66445bfe1",
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

_source line 15 · 2026-05-18T18:44:46.668Z_

<details><summary>↩ Tool result · `toolu_01B21yZVcEXDEcR4gnXNYxTq`</summary>

```text
Web search results for query: "open source VLA robot 2026 OpenVLA pi0 successor"

Links: [{"title":"Physical Intelligence π0 vs OpenVLA: Best VLA Model for Robot Learning 2026 | SVRC","url":"https://www.roboticscenter.ai/physical-intelligence-pi0-vs-openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/learn/vla-models-comparison"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"Vision-Language-Action (VLA) Models: LLMs for robots | by Gaurav Gupta | Black Coffee Robotics | Medium","url":"https://medium.com/black-coffee-robotics/vision-language-action-vla-models-llms-for-robots-f60ba0b79579"},{"title":"A Comprehensive Overview of Vision-Language-Action Models | DigitalOcean","url":"https://www.digitalocean.com/community/conceptual-articles/vision-language-action-models"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"}]

Based on the search results, here's what I found about open source VLA robot models in 2026:

## OpenVLA: The Open-Source Standard

OpenVLA is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA is a 7B parameter model that can be fine-tuned on a single consumer GPU (e.g., RTX 4090) using LoRA or QLoRA, with inference running comfortably on similar hardware.

OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks and multiple robot embodiments, with 7x fewer parameters.

## Recent Improvements in 2025-2026

OFT (Optimized Fine-Tuning recipe for VLAs) was recently released, which compared to vanilla OpenVLA fine-tuning, enables 25-50x faster inference speed, higher task success rates, multiple input images, and high-frequency bimanual robot control.

## Comparison with π0 (Pi-Zero)

For context on π0 (which appears to be a successor/alternative rather than a successor to OpenVLA): π0 (Pi-Zero) from Physical Intelligence delivers state-of-the-art dexterity performance — but requires partnership access and cannot be self-hosted. In contrast, for most researchers, OpenVLA is the recommended starting point as it is open-weight, fine-tunable on consumer hardware, and has an active community.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a5a3191-b73c-4843-a317-9ce8aa21fe82",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "19e531f7-cf0a-4f72-a590-2351e2a00511",
  "sourceToolAssistantUUID": "7a5a3191-b73c-4843-a317-9ce8aa21fe82",
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

_source line 16 · 2026-05-18T18:44:47.385Z_

<details><summary>↩ Tool result · `toolu_01Ljxk3fd3M3LDhYbpVSrwky`</summary>

```text
Web search results for query: "OpenVLA 2 2026 next generation VLA model"

Links: [{"title":"Vision language Action (VLA) Models | by chidubem ndukwe | Mar, 2026 | Medium","url":"https://medium.com/@chidubemndukwe/vision-language-action-vla-models-91795fa227c6"},{"title":"Vision-Language-Action (VLA) Models 2026 - Robotics Foundation Models & General-Purpose Robot AI | Internet Pros","url":"https://internet-pros.com/blog/vision-language-action-models-robotics-2026/"},{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/learn/vla-models-comparison"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"Vision-Language-Action (VLA) Models: LLMs for robots | by Gaurav Gupta | Black Coffee Robotics | Medium","url":"https://medium.com/black-coffee-robotics/vision-language-action-vla-models-llms-for-robots-f60ba0b79579"}]

Based on the search results, here's what I found about OpenVLA and VLA models in 2026:

## OpenVLA Overview

OpenVLA is a high-performance, open-source VLA model designed to be accessible and fine-tunable for a wide variety of robotic platforms. OpenVLA is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.

## Performance

OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks and multiple robot embodiments, with 7x fewer parameters.

## 2026 Context

In 2024, OpenVLA put a 7B foundation model in every academic lab. In 2025, π0, GR00T N1, Gemini Robotics, and Helix turned VLAs into production systems running humanoid bodies. The search results don't specifically mention an "OpenVLA 2" next-generation model announced for 2026, but they do discuss the broader evolution of VLA models and competing systems in the robotics field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b0711e0-8f8e-4a24-9fb0-ca3bdca968be",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "87e67c90-f192-4c53-b98c-b212e351617e",
  "sourceToolAssistantUUID": "4b0711e0-8f8e-4a24-9fb0-ca3bdca968be",
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

_source line 17 · 2026-05-18T18:44:47.464Z_

<details><summary>↩ Tool result · `toolu_012P4XFrwPdePU5G2dng37WV`</summary>

```text
Web search results for query: "open source multimodal LLM 2026 SOTA"

Links: [{"title":"Multimodal AI: The Best Open-Source Vision Language Models in 2026","url":"https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models"},{"title":"11 Top Open-Source LLMs for 2026 and Their Uses | DataCamp","url":"https://www.datacamp.com/blog/top-open-source-llms"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"The Best Open-Source LLMs in 2026: A Complete Guide for AI Developers - VERTU® Official Site","url":"https://vertu.com/lifestyle/the-best-open-source-llms-in-2026-a-complete-guide-for-ai-developers"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Best Open Source Multimodal LLMs: Top Choices in 2026","url":"https://okara.ai/blog/best-open-source-multimodal-llms"},{"title":"Ultimate Guide - The Best Open Source Multimodal Models in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-multimodal-models-2025"}]

Based on the search results, here are the leading open-source multimodal LLMs at the state-of-the-art (SOTA) in 2026:

## Top Multimodal Models

The top three recommendations for 2026 are GLM-4.5V, GLM-4.1V-9B-Thinking, and Qwen2.5-VL-32B-Instruct.

**GLM-4.5V and GLM-4.6V**: GLM-4.6V is the latest open-source multimodal model developed by Z.ai, featuring native multimodal tool use, stronger visual reasoning, and a 128K context window. It introduces end-to-end vision-driven tool use where images, UI screenshots, document pages, and visual snippets can be provided directly as tool parameters.

**GLM-4.7**: From the Zhipu AI team, GLM-4.7 is designed around three pillars: agentic abilities, complex reasoning, and advanced coding, representing a meaningful step forward in production-grade coding agents.

**MiMo-V2.5**: MiMo-V2.5 is the native multimodal agent model from Xiaomi, supporting text, image, video, and audio inputs.

**Apriel-1.5-15B-Thinker**: This is a multimodal (text+image) reasoning model from ServiceNow delivering frontier-level results on a single GPU.

## Performance Context

According to research from Epoch AI, open-weight models now trail the state-of-the-art proprietary models by only about three months on average, with open-source models being competitive with or superior to GPT-5 and Claude Sonnet 4 in coding agents, mathematical reasoning, and general chat.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "027dd873-61d5-4dae-ad31-63ca4df95116",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "65a6beb7-2baf-481b-8c45-4434718d85f1",
  "sourceToolAssistantUUID": "027dd873-61d5-4dae-ad31-63ca4df95116",
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

_source line 18 · 2026-05-18T18:44:47.677Z_

<details><summary>↩ Tool result · `toolu_01HLzLz8h3F6mHw1WDp8Z9ZR`</summary>

```text
Web search results for query: "best open source vision language model 2026"

Links: [{"title":"Ultimate Guide - The Best Open Source Multimodal Models in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-multimodal-models-2025"},{"title":"Ultimate Guide - The Best Open Source LLM for Document Screening in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLM-for-Document-screening"},{"title":"The Fastest Open Source Multimodal Models in 2026","url":"https://www.siliconflow.com/articles/en/fastest-open-source-multimodal-models"},{"title":"Best Open-Source Vision Language Models of 2026","url":"https://www.labellerr.com/blog/top-open-source-vision-language-models/"},{"title":"Top 10 Vision Language Models in 2026 | Benchmark, Use Cases","url":"https://dextralabs.com/blog/top-10-vision-language-models/"},{"title":"Multimodal AI: The Best Open-Source Vision Language Models in 2026","url":"https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models"},{"title":"Top 10 Vision Language Models in 2026 | DataCamp","url":"https://www.datacamp.com/blog/top-vision-language-models"}]

Based on the search results, here are the best open-source vision language models in 2026:

## Top Models

The top three recommendations for 2026 are GLM-4.5V, GLM-4.1V-9B-Thinking, and Qwen2.5-VL-32B-Instruct.

**GLM-4.5V** stands out as a leader. It's the latest generation vision-language model released by Zhipu AI with 106B total parameters and 12B active parameters, utilizing a Mixture-of-Experts (MoE) architecture for superior performance at lower inference cost. The model achieves state-of-the-art performance among open-source models on 41 public multimodal benchmarks.

**Additional Strong Performers:**

- Qwen 2.5-VL-72B and Gemma 3 are top performers in the open-source ecosystem
- GLM-4.6V features native multimodal tool use, stronger visual reasoning, and a 128K context window
- InternVL3-78B has achieved a score of 72.2 on the MMMU benchmark, establishing a new state-of-the-art record among open-source MLLMs

## Use Case-Specific Recommendations

For scalable workflows with documents, OCR, or VQA solutions, both Gemma 3 and LLaMA 3.2 Vision are the best options for accuracy and flexibility. For lightweight, resource-efficient deployments, DeepSeek-VL2, Phi-4, and Pixtral run well on edge devices.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fcf4ef1-6ef2-499d-945d-9f4f75459e7d",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "592c1b89-abf2-4aad-9a10-0576d457e0ae",
  "sourceToolAssistantUUID": "8fcf4ef1-6ef2-499d-945d-9f4f75459e7d",
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

_source line 19 · 2026-05-18T18:44:47.732Z_

<details><summary>↩ Tool result · `toolu_01V91DKX7jrKxzg3wnbkPNqd`</summary>

```text
Web search results for query: "SOTA open source vision language action model 2026"

Links: [{"title":"GitHub - starVLA/starVLA: StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing · GitHub","url":"https://github.com/starVLA/starVLA"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Meet dots.ocr: A New 1.7B Vision-Language Model that Achieves SOTA Performance on Multilingual Document Parsing - MarkTechPost","url":"https://www.marktechpost.com/2025/08/16/meet-dots-ocr-a-new-1-7b-vision-language-model-that-achieves-sota-performance-on-multilingual-document-parsing/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"MoTVLA: A Vision-Language-Action Model with Unified Fast-Slow Reasoning","url":"https://arxiv.org/pdf/2510.18337"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks","url":"https://arxiv.org/pdf/2504.19854"}]

Based on the search results, here are some of the state-of-the-art open-source vision-language-action models in 2026:

## Key Models:

**StarVLA**: This model recently achieved SOTA performance on RoboCasa evaluation when trained without pretraining. StarVLA now supports DOMINO, a dynamic manipulation benchmark for moving objects.

**OpenVLA**: A 7B-parameter open-source vision-language-action model trained on 970k robot episodes, which sets a new state of the art for generalist robot manipulation policies. OpenVLA outperforms closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks with 7x fewer parameters.

**MoTVLA**: This model shows superiority over state-of-the-art baselines in both reasoning and manipulation tasks, with capabilities across VQA, text and mathematics tasks, and robotic manipulation like stacking, tool usage, and pick-and-place.

**NORA**: A small open-sourced model that outperforms existing large-scale VLA models while achieving better task performance with significantly reduced computational overhead.

These models represent the cutting-edge of open-source VLA development in 2026, with varying trade-offs between scale, performance, and computational efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0621a474-af50-45b0-9ac8-17ad2a50891a",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "63e4a1b3-de15-40af-92de-516372f7c731",
  "sourceToolAssistantUUID": "0621a474-af50-45b0-9ac8-17ad2a50891a",
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

_source line 20 · 2026-05-18T18:44:48.172Z_

<details><summary>↩ Tool result · `toolu_01Asrd5bF7rxTvRijNVqEzwr`</summary>

```text
Web search results for query: "best open source LLM 2026 May"

Links: [{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"11 Top Open-Source LLMs for 2026 and Their Uses | DataCamp","url":"https://www.datacamp.com/blog/top-open-source-llms"},{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"The Best Open Source and Open-Weight LLM Models to Run Locally in 2026","url":"https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally"},{"title":"Open Source LLM Platforms in 2026: Ollama, OpenRouter, Groq, NVIDIA NIM — Which One Should You Use? | by Developer Awam | CodeX | May, 2026 | Medium","url":"https://medium.com/codex/open-source-llm-platforms-in-2026-ollama-openrouter-groq-nvidia-nim-which-one-should-you-use-2f11c7ba60bc"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"}]

Based on the search results, here are the best open source LLMs as of May 2026:

## Top Performers Overall

Qwen 3 235B-A22B currently leads on the broadest range of benchmarks, combining top-tier reasoning, coding, and multilingual capabilities under an Apache 2.0 license. For specific use cases, DeepSeek R1 (reasoning) and Llama 4 Scout (long context) may be better picks.

## By Specific Use Cases

**For Coding:**
On the May 12, 2026 snapshot, Kimi K2.6 Thinking is the strongest open-source entry across both key coding metrics: 78.57 Coding Avg and 58.33 Agentic Coding Avg.

**For Long Context:**
Meta's Llama 4 Scout brought something genuinely new to the open-source world: a 10 million token context window.

**For Budget/Local Deployment:**
If someone told you one year ago that Alibaba would ship the best default local LLM of 2026, you would have laughed. The Qwen models are noted as excellent for local deployment.

## Notable Models

GLM 5.1: 744B-parameter MoE (40B active) with a 200K token context, positioned as a flagship release for coding, reasoning, and agentic workflows — currently the leading open-weights model on Artificial Analysis's Intelligence Index.

DeepSeek-V4 offers both variants: V4-Pro (1.6T total / 49B active) and V4-Flash (284B total / 13B active), both with 1M context and MIT licensing.

## Overall Landscape

In 2026, open-source models have caught up with GPT-4 on most tasks. On coding and math benchmarks, the best open-source models match or beat GPT-4.5 and approach Claude Sonnet 4.5 performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e4b485b-fcbe-4529-b282-7cc3e3d4dc8f",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "8f0489d1-f055-4942-9fb3-a659a37166a8",
  "sourceToolAssistantUUID": "0e4b485b-fcbe-4529-b282-7cc3e3d4dc8f",
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

_source line 21 · 2026-05-18T18:44:51.187Z_

Let me do a few more targeted searches to fill in gaps on specific models that appeared.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f0489d1-f055-4942-9fb3-a659a37166a8",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXeSnq65b7SWThYNHoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5375b7d4-1970-451d-93b0-8073978f858d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j8Mw3vyRmvrepF7cJf3xV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2418,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 9501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 22 · 2026-05-18T18:44:52.212Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TG6MpTPBMRGBZQo9a3yWsZ`</summary>

```json
{
  "query": "SmolVLA model 2025 2026 Hugging Face parameters license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5375b7d4-1970-451d-93b0-8073978f858d",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXeSnq65b7SWThYNHoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40bce11b-e7f0-46f6-b56c-a4e2edb366e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j8Mw3vyRmvrepF7cJf3xV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2418,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 9501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 23 · 2026-05-18T18:44:52.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JVU2uy2ZRJqC1NXWcDUrMf`</summary>

```json
{
  "query": "StarVLA ICLR 2026 benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40bce11b-e7f0-46f6-b56c-a4e2edb366e1",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXeSnq65b7SWThYNHoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10a47b6d-348a-483a-b296-b440820fc6bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j8Mw3vyRmvrepF7cJf3xV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2418,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 9501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 24 · 2026-05-18T18:44:53.135Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016EShpNeVfDu11tTfEGHo9B`</summary>

```json
{
  "query": "NORA VLA model 2025 2026 small open source embodied"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10a47b6d-348a-483a-b296-b440820fc6bf",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXeSnq65b7SWThYNHoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f4d824c-f672-4cc2-9c17-80c91b4917e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j8Mw3vyRmvrepF7cJf3xV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2418,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 9501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 25 · 2026-05-18T18:44:53.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TobEFWmPALFgf6ksffT1Bg`</summary>

```json
{
  "query": "SimpleVLA-RL ICLR 2026 reinforcement learning VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f4d824c-f672-4cc2-9c17-80c91b4917e9",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXeSnq65b7SWThYNHoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ce7dae5-d28c-439d-b27c-0ac0fccad874",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j8Mw3vyRmvrepF7cJf3xV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2418,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 9501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 26 · 2026-05-18T18:44:54.544Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0182wu4feQi5TJC18g6a6eUL`</summary>

```json
{
  "query": "A1 VLA model 2026 transparent open source adaptive truncated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ce7dae5-d28c-439d-b27c-0ac0fccad874",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXeSnq65b7SWThYNHoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a23fce5-3eb7-49ff-974d-6839358521f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j8Mw3vyRmvrepF7cJf3xV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2418,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 9501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 27 · 2026-05-18T18:44:55.016Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012iXrhY21u9Bd5oPTVkXMDZ`</summary>

```json
{
  "query": "Qwen3 235B vision multimodal capabilities 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a23fce5-3eb7-49ff-974d-6839358521f5",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXeSnq65b7SWThYNHoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54376389-bb2b-42da-90e9-dc3b24038340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j8Mw3vyRmvrepF7cJf3xV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2418,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 9501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 28 · 2026-05-18T18:44:55.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UfH464pFAofRNCqvumujWq`</summary>

```json
{
  "query": "InternVL3 2026 open source vision language model sizes license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54376389-bb2b-42da-90e9-dc3b24038340",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXeSnq65b7SWThYNHoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffb265d6-a50a-441f-921c-3f630a876806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j8Mw3vyRmvrepF7cJf3xV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2418,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 9501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 29 · 2026-05-18T18:44:58.989Z_

<details><summary>↩ Tool result · `toolu_01JVU2uy2ZRJqC1NXWcDUrMf`</summary>

```text
Web search results for query: "StarVLA ICLR 2026 benchmark results"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=eKhOrQWAVJ"},{"title":"StarVLA-𝜶: Reducing Complexity in Vision-Language-Action Systems","url":"https://arxiv.org/html/2604.11757v1"},{"title":"GitHub - starVLA/starVLA: StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing · GitHub","url":"https://github.com/starVLA/starVLA"},{"title":"ICLR.2026 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"},{"title":"ICLR 2026 Scores Released: Reviewers Call It \"Crazy\", DeepMind Researchers Show Comeback from Desperate Situation","url":"https://eu.36kr.com/en/p/3551362253731718"},{"title":"StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing","url":"https://arxiv.org/pdf/2604.05014"}]

Based on the search results, I found information about StarVLA and ICLR 2026. Here's what I found:

StarVLA is a unified codebase for Vision-Language-Action (VLA) model development that addresses fragmentation in VLA research by providing diverse action-decoding designs, decoupled system components for reuse, and consistent evaluation protocols across benchmarks.

Regarding benchmark results, the search results show that StarVLA reached state-of-the-art performance on RoboCasa evaluation without pretraining, and pipelines have been established for Behavior-1K, RoboTwin 2.0, and CALVIN benchmarks.

Additionally, related work published at ICLR 2026 includes ST4VLA achieving state-of-the-art results on SimplerEnv benchmarks, improving large-scale simulation tasks by over 6% on average, and reaching 92% success on real-world long-horizon manipulation under distribution shifts.

If you're looking for more specific benchmark result numbers or comparisons across different benchmarks, the full papers (particularly the StarVLA codebase paper on arxiv.org) would contain more detailed performance metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10a47b6d-348a-483a-b296-b440820fc6bf",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "f81b3c13-a9d4-4f89-af99-b73ef2cd42b3",
  "sourceToolAssistantUUID": "10a47b6d-348a-483a-b296-b440820fc6bf",
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

_source line 30 · 2026-05-18T18:44:59.965Z_

<details><summary>↩ Tool result · `toolu_01TobEFWmPALFgf6ksffT1Bg`</summary>

```text
Web search results for query: "SimpleVLA-RL ICLR 2026 reinforcement learning VLA"

Links: [{"title":"Activity · PRIME-RL/SimpleVLA-RL","url":"https://github.com/PRIME-RL/SimpleVLA-RL/activity"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"Issues · PRIME-RL/SimpleVLA-RL","url":"https://github.com/PRIME-RL/SimpleVLA-RL/issues"},{"title":"SIMPLEVLA-RL: SCALING VLA TRAINING VIA RE","url":"https://openreview.net/pdf/04ee56414bb3cef5c18010f6993f98e74dbcd5aa.pdf"},{"title":"ICLR Poster SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://iclr.cc/virtual/2026/poster/10009314"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"PRIME-RL · GitHub","url":"https://github.com/PRIME-RL"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"GitHub - thegovind/simplevla-rl: SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://github.com/thegovind/simplevla-rl"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"}]

Based on the search results, here's what I found about SimpleVLA-RL:

## Overview

SimpleVLA-RL is an efficient RL framework tailored for VLA models that introduces VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, and optimized loss computation.

## Problem It Addresses

Vision-Language-Action (VLA) models face two fundamental challenges: (i) the scarcity and high cost of large-scale human-operated robotic trajectories required for SFT scaling, and (ii) limited generalization to tasks involving distribution shift.

## Key Features

SimpleVLA-RL is an efficient RL framework for VLA that improves long-horizon planning under data scarcity, outperforms SFT in simulation and real-world tasks, reveals a "pushcut" new-action phenomenon, and strengthens spatial/object/goal generalization.

## Performance Results

SimpleVLA-RL improves the performance of OpenVLA-OFT to 97.6 points on LIBERO-Long and sets a new state-of-the-art. Remarkably, using only one trajectory per task for cold-start SFT, SimpleVLA-RL raises the performance of OpenVLA-OFT from 17.3 to 91.7, yielding an improvement of 74.4 points (430.1%).

The paper was accepted to ICLR 2026, and the project code is available on GitHub under the PRIME-RL organization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ce7dae5-d28c-439d-b27c-0ac0fccad874",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "9d58eef0-fe2c-4bd0-9793-52a89244e4af",
  "sourceToolAssistantUUID": "9ce7dae5-d28c-439d-b27c-0ac0fccad874",
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

_source line 31 · 2026-05-18T18:45:01.961Z_

<details><summary>↩ Tool result · `toolu_012iXrhY21u9Bd5oPTVkXMDZ`</summary>

```text
Web search results for query: "Qwen3 235B vision multimodal capabilities 2026"

Links: [{"title":"Qwen: Qwen3 VL 235B A22B Thinking Review | Pricing, Benchmarks & Capabilities (2026) | Design for Online","url":"https://designforonline.com/ai-models/qwen-qwen3-vl-235b-a22b-thinking/"},{"title":"Multimodal AI: The Best Open-Source Vision Language Models in 2026","url":"https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models"},{"title":"Qwen3 VL 235B vs GPT-5 Vision: Multimodal AI Comparison 2026 - Crazyrouter","url":"https://crazyrouter.com/en/blog/qwen3-vl-235b-vs-gpt-5-vision-multimodal-comparison-2026"},{"title":"GitHub - QwenLM/Qwen3-VL: Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3-VL"},{"title":"Qwen3-VL Technical Report","url":"https://arxiv.org/pdf/2511.21631"},{"title":"Qwen","url":"https://qwen.readthedocs.io/"},{"title":"[2511.21631] Qwen3-VL Technical Report","url":"https://arxiv.org/abs/2511.21631"},{"title":"Qwen/Qwen3.5-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-27B"},{"title":"qwen3-vl","url":"https://ollama.com/library/qwen3-vl"}]

Based on the search results, here's what I found about Qwen3 VL 235B's vision multimodal capabilities in 2026:

## Model Overview

Qwen3-VL-235B-A22B is a multimodal model that unifies strong text generation with visual understanding across images and video. The flagship model, Qwen3-VL-235B-A22B, has 235B total parameters with 22B activated per token.

## Key Multimodal Capabilities

The model natively supports interleaved contexts of up to 256K tokens, seamlessly integrating text, images, and video. The model demonstrates significantly stronger multimodal reasoning capabilities, achieving superior performance on complex reasoning tasks.

The model includes both non-thinking and thinking variants, with the Thinking model optimized for multimodal reasoning in STEM and math.

## Performance Strengths

The flagship Qwen3-VL-235B-A22B-Instruct rivals top-tier proprietary models such as Gemini-2.5-Pro and GPT-5 across multimodal benchmarks covering general Q&A, 2D/3D grounding, video understanding, OCR, and document comprehension.

Qwen3-VL can operate graphical interfaces (PC/mobile), recognizes UI elements, understands functions, and performs real-world tasks through tool invocation.

It can generate code from images or videos — for example, turning a design mockup into Draw.io, HTML, CSS, or JavaScript code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54376389-bb2b-42da-90e9-dc3b24038340",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "ccb0e86f-74f8-49c4-b8d3-95741a8b589e",
  "sourceToolAssistantUUID": "54376389-bb2b-42da-90e9-dc3b24038340",
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

_source line 32 · 2026-05-18T18:45:02.241Z_

<details><summary>↩ Tool result · `toolu_0182wu4feQi5TJC18g6a6eUL`</summary>

```text
Web search results for query: "A1 VLA model 2026 transparent open source adaptive truncated"

Links: [{"title":"[2604.05672] A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/abs/2604.05672"},{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"},{"title":"𝐴₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/html/2604.05672"},{"title":"Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision–Language–Action Models via Latent Iterative Reasoning | OpenReview","url":"https://openreview.net/forum?id=p1UF73ZvE0"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"}]

Based on the search results, I found detailed information about the A1 model you're looking for:

## A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model

A1 is a fully open-source and transparent VLA framework designed for low-cost, high-throughput inference without sacrificing manipulation success, leveraging pretrained VLMs that provide implicit affordance priors for action generation.

### Key Features:

**Transparency and Reproducibility:** The full training stack is released (training code, data/data-processing pipeline, intermediate checkpoints, and evaluation scripts) to enable end-to-end reproducibility.

**Adaptive Inference:** A1 targets the full inference pipeline by introducing a budget-aware adaptive inference scheme that jointly accelerates the backbone and the action head. It monitors action consistency across intermediate VLM layers to trigger early termination, and proposes Inter-Layer Truncated Flow Matching that warm-starts denoising across layers, enabling accurate actions with substantially fewer effective denoising iterations.

### Performance:

Across simulation benchmarks (LIBERO, VLABench) and real robots (Franka, AgiBot), A1 achieves state-of-the-art success rates while significantly reducing inference cost (e.g., up to 72% lower per-episode latency for flow-matching inference and up to 76.6% backbone computation reduction with minor performance degradation).

The paper was posted on arXiv in April 2026 and is available with code and project page according to the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a23fce5-3eb7-49ff-974d-6839358521f5",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "c2f8db32-e063-4418-8be4-d83ec7206fc6",
  "sourceToolAssistantUUID": "9a23fce5-3eb7-49ff-974d-6839358521f5",
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

_source line 33 · 2026-05-18T18:45:09.278Z_

<details><summary>↩ Tool result · `toolu_016EShpNeVfDu11tTfEGHo9B`</summary>

```text
Web search results for query: "NORA VLA model 2025 2026 small open source embodied"

Links: [{"title":"[PDF] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NORA:-A-Small-Open-Sourced-Generalist-Vision-Action-Hung-Sun/0801ed93c26dcb72e2bddf756f971e10357942a2"},{"title":"[2504.19854] NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/abs/2504.19854"},{"title":"Paper page - NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://huggingface.co/papers/2504.19854"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://arxiv.org/html/2504.19854v1"},{"title":"NORA: A Small Open-Sourced Generalist Vision Language Action Model for   Embodied Tasks","url":"https://arxiv.org/pdf/2504.19854"},{"title":"GitHub - ehaller00/NORA-VLA: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub","url":"https://github.com/ehaller00/NORA-VLA"},{"title":"(PDF) NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks","url":"https://www.researchgate.net/publication/391247234_NORA_A_Small_Open-Sourced_Generalist_Vision_Language_Action_Model_for_Embodied_Tasks"},{"title":"GitHub - declare-lab/nora: NORA: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks · GitHub","url":"https://github.com/declare-lab/nora"}]

Based on the search results, here's what I found about NORA:

## NORA VLA Model Overview

NORA is a 3B-parameter VLA model using Qwen-2.5-VL-3B for efficient visual reasoning and action grounding, outperforming larger models with reduced computational overhead.

Experimental results demonstrate that NORA outperforms existing large-scale VLA models, achieving better task performance with significantly reduced computational overhead, making it a more practical solution for real-time robotic autonomy.

### Key Features

The model introduces Ego3D Position Encoding to inject 3D information into the input observations of the visual-language-action model, and Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids.

By leveraging the state-of-the-art open-source multimodal model Qwen-2.5-VL-3B, NORA achieves a balance between performance and efficiency, enabling more scalable and practical deployment in robotic systems.

### Publication and Availability

The paper was published on April 28, 2025. The model is open-sourced, with code available on GitHub at the declare-lab/nora repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f4d824c-f672-4cc2-9c17-80c91b4917e9",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "459bcfdb-1ae9-4668-b9fc-9c42250719a8",
  "sourceToolAssistantUUID": "7f4d824c-f672-4cc2-9c17-80c91b4917e9",
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

_source line 34 · 2026-05-18T18:45:11.688Z_

<details><summary>↩ Tool result · `toolu_01TG6MpTPBMRGBZQo9a3yWsZ`</summary>

```text
Web search results for query: "SmolVLA model 2025 2026 Hugging Face parameters license"

Links: [{"title":"Hugging Face says its new robotics model is so efficient it can run on a MacBook | TechCrunch","url":"https://techcrunch.com/2025/06/04/hugging-face-says-its-new-robotics-model-is-so-efficient-it-can-run-on-a-macbook/"},{"title":"Hugging Face Releases SmolVLA, a Compact Open-Source Robotics Model -- Pure AI","url":"https://pureai.com/articles/2025/06/10/hugging-face-releases-smolvla.aspx"},{"title":"Hugging Face releases Smolvla: a compact model on visual action for affordable and effective robotics","url":"https://learnopoly.com/hugging-face-releases-smolvla-a-compact-model-on-visual-action-for-affordable-and-effective-robotics/"},{"title":"Hugging Face Unveils SmolVLA: Efficient and Affordable Vision-Language-Action Model for Robotics | Timekeeper","url":"https://kiadev.net/news/2025-06-03-hugging-face-smolvla-efficient-affordable-robotics/"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model For Affordable And Efficient Robotics — Meta Ai Labs™","url":"https://metaailabs.com/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"}]

Based on the search results, here's what I found about SmolVLA:

## Model Size and Parameters
SmolVLA has 450 million parameters and aims to offer efficient, reproducible performance for robotic tasks without reliance on proprietary datasets or expensive infrastructure.

## License
The model is released under an open license, complete with code, training data, and deployment tools. More specifically, it was trained on "compatibly licensed," community-shared datasets.

## Release and Availability
Hugging Face released SmolVLA, an open AI model for robotics. The model is available on Hugging Face's platform, as indicated by references to the official model repository.

## Training Data
SmolVLA is pretrained on 10 million frames curated from 487 community datasets tagged under "lerobot" on Hugging Face.

## Architecture
Unlike traditional VLAs, SmolVLA is trained exclusively on community-collected datasets and is optimized to operate on single-GPU or CPU systems. Its architecture combines a trimmed pretrained vision-language model (SmolVLM-2) with a transformer-based action expert.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40bce11b-e7f0-46f6-b56c-a4e2edb366e1",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "49293f7c-5e28-46c7-8179-5b6bb6ac09d3",
  "sourceToolAssistantUUID": "40bce11b-e7f0-46f6-b56c-a4e2edb366e1",
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

_source line 35 · 2026-05-18T18:45:12.484Z_

<details><summary>↩ Tool result · `toolu_01UfH464pFAofRNCqvumujWq`</summary>

```text
Web search results for query: "InternVL3 2026 open source vision language model sizes license"

Links: [{"title":"InternVL","url":"https://internvl.github.io/"},{"title":"Advanced Visual Reasoning with DeepSeek-VL2 and InternVL3","url":"https://getstream.io/blog/deepseekvl-internvl3-visual-reasoning/"},{"title":"GitHub - OpenGVLab/InternVL: [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative to GPT-4o. 近GPT-4o表现的开源多模态对话模型 · GitHub","url":"https://github.com/opengvlab/internvl"},{"title":"InternVL 3.5 : Best open-sourced Multi-Modal LLM | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/internvl-3-5-best-open-sourced-multi-modal-llm-bc929e2b6338"},{"title":"InternVL3: Open-Source Multimodal LLM","url":"https://www.emergentmind.com/topics/internvl3"},{"title":"Top 10 Vision Language Models in 2026 | DataCamp","url":"https://www.datacamp.com/blog/top-vision-language-models"},{"title":"Deploy Vision Language Models on GPU Cloud: Qwen3-VL, Llama 4 Scout, and InternVL3 Guide (2026) | Spheron Blog","url":"https://www.spheron.network/blog/deploy-vision-language-models-gpu-cloud/"},{"title":"Top 10 Vision Language Models in 2026 | Benchmark, Use Cases","url":"https://dextralabs.com/blog/top-10-vision-language-models/"},{"title":"OpenGVLab/InternVL3_5-8B · Hugging Face","url":"https://huggingface.co/OpenGVLab/InternVL3_5-8B"},{"title":"Survey of Open-Source Vision Language Models (2026) | Hacker News","url":"https://news.ycombinator.com/item?id=47247663"}]

Based on the web search results, here's the information about InternVL3 as a 2026 open-source vision-language model:

## Model Sizes

InternVL3 models are available on Hugging Face in sizes ranging from 1B to 78B parameters. More specifically, InternVL3 is an advanced multimodal large language model (MLLM) series with InternVL3-78B achieving state-of-the-art performance in both perception and reasoning performance among open-source MLLMs.

Additionally, there's a newer version: InternVL3.5, released in August 2025, is a new family of open-source multimodal models with the largest model, InternVL3.5-241B-A28B, attaining state-of-the-art results among open-source MLLMs.

## License

Both InternVL3 and related models are released with licenses that allow commercial usage, making them viable alternatives to proprietary vision APIs for production applications. More broadly, these models come with licensing that permits commercial use.

## Architecture

The flagship 78B model pairs a 6B-parameter vision encoder (InternViT) with a 72.7B Qwen2.5 language model. InternVL3 uses what the team calls "Native Multimodal Pre-Training," where vision and language are learned together from the start.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffb265d6-a50a-441f-921c-3f630a876806",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "f519c728-e88a-4b08-b706-c3db69c4f4ec",
  "sourceToolAssistantUUID": "ffb265d6-a50a-441f-921c-3f630a876806",
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

_source line 36 · 2026-05-18T18:45:15.707Z_

Let me get a few more details on key models and licenses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f519c728-e88a-4b08-b706-c3db69c4f4ec",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXgEh7rVyyssRpvsuvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "460b25a5-e1a5-4834-8a3e-bbbc319aa521",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qiqa6sDiP5dUuJnZ56cj5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8520,
      "cache_read_input_tokens": 13477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8520,
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

_source line 37 · 2026-05-18T18:45:16.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PqT5jdFRNRE3pWoeUfzeUc`</summary>

```json
{
  "query": "OpenVLA license MIT Apache model weights 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "460b25a5-e1a5-4834-8a3e-bbbc319aa521",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXgEh7rVyyssRpvsuvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18217120-236a-4d26-adb9-aafe8f298a3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qiqa6sDiP5dUuJnZ56cj5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8520,
      "cache_read_input_tokens": 13477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8520,
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

_source line 38 · 2026-05-18T18:45:17.120Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D5o2xQX1PVshEZ9WAkXV6J`</summary>

```json
{
  "query": "OpenVLA-OFT 2025 optimized fine-tuning VLA improvements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18217120-236a-4d26-adb9-aafe8f298a3c",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXgEh7rVyyssRpvsuvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c34e8814-f19a-462c-8538-6d1ecdb436a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qiqa6sDiP5dUuJnZ56cj5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8520,
      "cache_read_input_tokens": 13477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8520,
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

_source line 39 · 2026-05-18T18:45:18.118Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019PmZGGyKTWHa5pVmUiAJg4`</summary>

```json
{
  "query": "LingBot-VLA Robbyant 2026 model size license open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c34e8814-f19a-462c-8538-6d1ecdb436a8",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXgEh7rVyyssRpvsuvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddcca4fb-9505-4731-a91b-83ef339902cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qiqa6sDiP5dUuJnZ56cj5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8520,
      "cache_read_input_tokens": 13477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8520,
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

_source line 40 · 2026-05-18T18:45:19.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013M8wMN8dqdSkJHdURdpCbQ`</summary>

```json
{
  "query": "MoTVLA fast slow reasoning VLA 2025 2026 open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddcca4fb-9505-4731-a91b-83ef339902cd",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXgEh7rVyyssRpvsuvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74edc3bd-5662-409f-a851-e1dc98aadc8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qiqa6sDiP5dUuJnZ56cj5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8520,
      "cache_read_input_tokens": 13477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8520,
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

_source line 41 · 2026-05-18T18:45:19.649Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RXeVYqzfJUk7W1UxhbKCCr`</summary>

```json
{
  "query": "GLM-4.6V Zhipu 2026 open source license size parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74edc3bd-5662-409f-a851-e1dc98aadc8d",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXgEh7rVyyssRpvsuvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "096b9576-793a-4bd1-8b91-ebe53dd92d03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qiqa6sDiP5dUuJnZ56cj5p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8520,
      "cache_read_input_tokens": 13477,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8520
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 290,
          "cache_read_input_tokens": 13477,
          "cache_creation_input_tokens": 8520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8520,
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

_source line 42 · 2026-05-18T18:45:21.537Z_

<details><summary>↩ Tool result · `toolu_01PqT5jdFRNRE3pWoeUfzeUc`</summary>

```text
Web search results for query: "OpenVLA license MIT Apache model weights 2024"

Links: [{"title":"Open-Weight Foundation Models for Robotics (2025 Guide) | RoboCloud Hub","url":"https://robocloud-dashboard.vercel.app/learn/blog/open-weight-robot-models"},{"title":"OpenVLA - AI Agent Index - MIT","url":"https://aiagentindex.mit.edu/openvla/"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"openvla/openvla-7b · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b"},{"title":"GitHub - xiaoxiao0406/VQ-VLA: The offical repo for paper \"VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers\" (ICCV 2025)","url":"https://github.com/xiaoxiao0406/VQ-VLA"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"}]

Based on the search results, here's what I found about OpenVLA's licensing:

**Code License:**
All OpenVLA checkpoints, as well as the training codebase are released under an MIT License.

**Model Weights License:**
However, there's an important distinction regarding the model weights. While all code in the repository is released under an MIT License, the pretrained models may inherit restrictions from the underlying base models. Specifically, both the models are derived from Llama-2, and as such are subject to the Llama Community License.

So while the Apache 2.0 license you mentioned doesn't appear in the official documentation, the code is under MIT, and the model weights have more complex licensing due to their Llama-2 foundation.

**Model Details:**
OpenVLA is a 7 billion parameter open-source Vision Language-Action (VLA) model. The first paper release was June 13, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18217120-236a-4d26-adb9-aafe8f298a3c",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "1e7bb0a6-e049-462a-8c5d-514cd15bf420",
  "sourceToolAssistantUUID": "18217120-236a-4d26-adb9-aafe8f298a3c",
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

_source line 43 · 2026-05-18T18:45:24.312Z_

<details><summary>↩ Tool result · `toolu_013M8wMN8dqdSkJHdURdpCbQ`</summary>

```text
Web search results for query: "MoTVLA fast slow reasoning VLA 2025 2026 open source"

Links: [{"title":"MoTVLA: A Vision-Language-Action Model with Unified Fast-Slow Reasoning | OpenReview","url":"https://openreview.net/forum?id=bjApyTEoRf"},{"title":"MoTVLA: A Vision-Language-Action Model with Unified Fast-Slow Reasoning","url":"https://arxiv.org/html/2510.18337v3"},{"title":"MoTVLA: A Vision-Language-Action Model with Unified Fast-Slow Reasoning | Request PDF","url":"https://www.researchgate.net/publication/396747355_MoTVLA_A_Vision-Language-Action_Model_with_Unified_Fast-Slow_Reasoning"},{"title":"MoTVLA: A Vision-Language-Action Model with Unified Fast-Slow Reasoning","url":"https://arxiv.org/pdf/2510.18337"},{"title":"[2510.18337] MoTVLA: A Vision-Language-Action Model with Unified Fast-Slow Reasoning","url":"https://arxiv.org/abs/2510.18337"}]

Based on the search results, here's what I found about MoTVLA:

## MoTVLA Overview

MoTVLA is a mixture-of-transformers (MoT)–based vision–language–action (VLA) model that integrates fast–slow unified reasoning with behavior policy learning.

## Problem It Addresses

Existing approaches face two challenges: limited language steerability when no generated reasoning is used as a condition, or significant inference latency when reasoning is incorporated.

## Key Features

MoTVLA preserves the general intelligence of pre-trained VLMs (serving as the generalist) for tasks such as perception, scene understanding, and semantic planning, while incorporating a domain expert, a second transformer that shares knowledge with the pretrained VLM, to generate domain-specific fast reasoning (e.g., robot motion decomposition).

## Performance

Extensive evaluations across natural language processing benchmarks, robotic simulation environments, and real-world experiments confirm the superiority of MoTVLA in both language reasoning and manipulation task performance.

## Academic Status

The paper was submitted to ICLR 2026 on September 17, 2025 (modified February 11, 2026). However, I did not find specific information in the search results about whether MoTVLA is available as open-source software.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74edc3bd-5662-409f-a851-e1dc98aadc8d",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "4a539171-2d15-49c7-9a8e-80832c699be3",
  "sourceToolAssistantUUID": "74edc3bd-5662-409f-a851-e1dc98aadc8d",
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

_source line 44 · 2026-05-18T18:45:24.507Z_

<details><summary>↩ Tool result · `toolu_01D5o2xQX1PVshEZ9WAkXV6J`</summary>

```text
Web search results for query: "OpenVLA-OFT 2025 optimized fine-tuning VLA improvements"

Links: [{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"The OpenVLA-OFT Vision-Language-Action Model is open-sourced! Fine-tuning optimization enhances speed and success rate.","url":"https://model.aibase.com/models/details/1935154868167905280"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"OpenVLA-OFT+ on the bimanual ALOHA robot. Our Optimized Fine-Tuning... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/OpenVLA-OFT-on-the-bimanual-ALOHA-robot-Our-Optimized-Fine-Tuning-OFT-recipe-enhances_fig1_389399234"},{"title":"Open-source OpenVLA-OFT Model - Finetune and Optimize Visual-Language-Action Abilities, Improve Performance and Speed","url":"https://model.aibase.com/models/details/1935154868096602112"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"[Literature Review] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.themoonlight.io/en/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"}]

Based on the search results, here's what I found about OpenVLA-OFT 2025:

## Overview

OpenVLA-OFT significantly boosts OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×.

## Key Components

The Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications.

## VLA Improvements

The improvements are significant across multiple dimensions:

- **Speed**: Through parallel decoding and action chunking, OpenVLA-OFT obtains 26x faster action generation speed and 3x lower latency than the base OpenVLA model.

- **Real-world Performance**: In real-world evaluations, the fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs (π0 and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch by up to 15% (absolute) in average success rate.

- **Language Grounding**: The OFT+ variant integrates feature-wise linear modulation (FiLM), which strengthens language grounding in tasks where accurate language understanding is critical for success.

The research was published in April 2025 and represents a significant advancement in efficiently fine-tuning vision-language-action models for robotics applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c34e8814-f19a-462c-8538-6d1ecdb436a8",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "97d14795-424b-4f9e-bae7-143005947cb1",
  "sourceToolAssistantUUID": "c34e8814-f19a-462c-8538-6d1ecdb436a8",
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

_source line 45 · 2026-05-18T18:45:26.344Z_

<details><summary>↩ Tool result · `toolu_01RXeVYqzfJUk7W1UxhbKCCr`</summary>

```text
Web search results for query: "GLM-4.6V Zhipu 2026 open source license size parameters"

Links: [{"title":"Zhipu GLM 4.6: The Open-Source Frontier AI Model Guide | CodeGPT","url":"https://www.codegpt.co/blog/zhipu-glm-4-6-open-source-ai"},{"title":"Zhipu AI Releases GLM-4.6V: A 128K Context Vision Language Model with Native Tool Calling - MarkTechPost","url":"https://www.marktechpost.com/2025/12/09/zhipu-ai-releases-glm-4-6v-a-128k-context-vision-language-model-with-native-tool-calling/"},{"title":"Z.ai debuts open source GLM-4.6V, a native tool-calling vision model for multimodal reasoning | VentureBeat","url":"https://venturebeat.com/ai/z-ai-debuts-open-source-glm-4-6v-a-native-tool-calling-vision-model-for"},{"title":"Zhipu Open-Source GLM-4.6V Series: 106B Native Support for Function Call Lightweight Version 9B Free for Commercial Use","url":"https://news.aibase.com/news/23480"},{"title":"glm-4.1v-9b-thinking & glm-4.5-flash: Zhipu Model Roundup (2026) - TokenMix Blog","url":"https://tokenmix.ai/blog/glm-models-zhipu-roundup-4-1v-4-5-flash-2026"},{"title":"GLM-4.6V - Overview - Z.AI DEVELOPER DOCUMENT","url":"https://docs.z.ai/guides/vlm/glm-4.6v"},{"title":"Zhipu GLM 4.6 vs Claude Sonnet: Coding Model Guide","url":"https://www.digitalapplied.com/blog/zhipu-ai-glm-4-6-vs-claude-sonnet"},{"title":"GLM-5.1: #1 Open Source AI Model? Full Review (2026)","url":"https://www.buildfastwithai.com/blogs/glm-5-1-open-source-review-2026"},{"title":"Z.ai - Wikipedia","url":"https://en.wikipedia.org/wiki/Z.ai"},{"title":"Zhipu Open-Source GLM-4.6V Series: 106B Native Support for Function Call Lightweight Version 9B Free for Commercial Use","url":"https://www.aibase.com/news/23480"}]

Based on the search results, here's the information about GLM-4.6V from Zhipu AI:

## Model Parameters and Architecture

GLM-4.6V is a 106B parameter foundation model for cloud and high performance cluster workloads, while GLM-4.6V-Flash is a 9B parameter variant tuned for local deployment and low latency use. More specifically, the base version GLM-4.6V has total parameters of 106B with 12B activated parameters.

## Open Source License

GLM-4.6V-Flash is completely free and allows developers to commercialize at zero cost. While the search results show information about the original GLM-4.6 text model having an MIT license, the specific open-source license details for the GLM-4.6V vision-language variant are referenced as being available on GitHub and Hugging Face, but the exact license type for GLM-4.6V isn't explicitly stated in the results.

## Context Window

GLM-4.6V extends the training context window to 128K tokens.

## Release Information

Zhipu AI open sourced the GLM-4.6V series as a pair of vision language models that treat images, video and tools as first class inputs for agents. The model was released in December 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "096b9576-793a-4bd1-8b91-ebe53dd92d03",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "90498861-543f-437d-b197-dd6da7a357a0",
  "sourceToolAssistantUUID": "096b9576-793a-4bd1-8b91-ebe53dd92d03",
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

_source line 46 · 2026-05-18T18:45:39.590Z_

<details><summary>↩ Tool result · `toolu_019PmZGGyKTWHa5pVmUiAJg4`</summary>

```text
Web search results for query: "LingBot-VLA Robbyant 2026 model size license open source"

Links: [{"title":"GitHub - Robbyant/lingbot-vla: A Pragmatic VLA Foundation Model · GitHub","url":"https://github.com/robbyant/lingbot-vla"},{"title":"Robbyant open-sources LingBot-VLA ‘universal brain’ model for embodied AI robots","url":"https://roboticsandautomationnews.com/2026/03/13/robbyant-open-sources-lingbot-vla-model-as-a-universal-brain-for-robots/99640/"},{"title":"Robbyant Open-Sources LingBot-VLA as a “Universal Brain” for Robots | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/26071/"},{"title":"robbyant/lingbot-vla-4b · Hugging Face","url":"https://huggingface.co/robbyant/lingbot-vla-4b"},{"title":"Robbyant Open-Sources LingBot-VLA as a “Universal Brain” for Robots","url":"https://theaiinsider.tech/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/"},{"title":"GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/robbyant/lingbot-va"},{"title":"Robbyant Open-Sources LingBot-World, a World Model for Millisecond-Level Real-Time Interaction","url":"https://www.businesswire.com/news/home/20260128459962/en/Robbyant-Open-Sources-LingBot-World-a-World-Model-for-Millisecond-Level-Real-Time-Interaction"},{"title":"GitHub - Robbyant/lingbot-world: Advancing Open-source World Models · GitHub","url":"https://github.com/robbyant/lingbot-world"},{"title":"LingBot-World | Open Source AI World Model","url":"https://www.lingbot-world.pro/"},{"title":"Robbyant Open-Sources LingBot-VLA as a “Universal Brain” for Robots","url":"https://www.businesswire.com/news/home/20260127455032/en/Robbyant-Open-Sources-LingBot-VLA-as-a-Universal-Brain-for-Robots"}]

Based on the search results, here's what I found about LingBot-VLA:

## Model Size
LingBot-VLA is available as a 4B (4 billion parameter) model, with two configurations: a depth-free version and a depth-distilled version.

## License
This project is licensed under the Apache-2.0 License.

## Open Source Status
Robbyant has open-sourced LingBot-VLA, a vision-language-action model designed as a universal brain for robots. The open-source release includes not only the model weights but also a complete, production-ready codebase, featuring tools for data processing, efficient fine-tuning, and automated evaluation.

## Additional Details
The model was pre-trained on more than 20,000 hours of real-world interaction data, and delivers 1.5x to 2.8x faster training than comparable frameworks. The LingBot-VLA Technical Report is available on Arxiv, released on January 27, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddcca4fb-9505-4731-a91b-83ef339902cd",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a85bd974213dd0e1a",
  "type": "user",
  "uuid": "331210d8-b57b-4349-ab6c-19cf09be25f0",
  "sourceToolAssistantUUID": "ddcca4fb-9505-4731-a91b-83ef339902cd",
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

_source line 47 · 2026-05-18T18:47:09.804Z_

Now I have comprehensive data. Here is the full report.

---

## Frontier Open-Source Models for Building a VLA System (May 2026)

I searched across all seven queries. Below is a structured report covering three categories: (1) dedicated VLA models, (2) general-purpose open-source LLMs (text backbones), and (3) open-source Vision-Language Models (VLMs) suitable as VLA backbones.

---

### CATEGORY 1: Dedicated Vision-Language-Action (VLA) Models

#### 1. OpenVLA + OpenVLA-OFT
- **Organization:** Stanford / UC Berkeley / Toyota Research Institute / Google DeepMind
- **Released:** OpenVLA June 2024; OpenVLA-OFT April 2025
- **Parameters:** 7B (based on Llama-2 + DINOv2 + SigLIP vision encoders)
- **License:** Code = MIT; Weights = Llama Community License (inherited from Llama-2)
- **Key results:** Outperforms RT-2-X (55B) by 16.5% absolute success rate across 29 tasks with 7x fewer parameters. OFT recipe boosts average success from 76.5% to 97.1% on LIBERO and gives 26x faster inference. Supports bimanual ALOHA control and outperforms pi0 and RDT-1B in real-world fine-tuning evaluations.
- **VLA backbone suitability:** **Excellent.** The most established open-source VLA with the largest community. Fine-tunable on a single RTX 4090 via LoRA/QLoRA. OFT adds action chunking, continuous action representation, and parallel decoding. The best starting point for affordance-aware VLA research.

#### 2. SmolVLA
- **Organization:** Hugging Face (LeRobot team)
- **Released:** June 2025
- **Parameters:** 450M (based on SmolVLM-2 + transformer action expert)
- **License:** Open (community-compatible); trained exclusively on openly-licensed datasets
- **Key results:** 82-90% success on LIBERO (within 5% of OpenVLA). Runs at 15-30 Hz on a single RTX 4090. Pretrained on 10M frames from 487 community datasets.
- **VLA backbone suitability:** **Good for edge/real-time deployment.** 16x fewer parameters than OpenVLA with competitive performance. Ideal if you need high-frequency reactive control on consumer hardware, but may lack capacity for complex affordance reasoning due to small backbone.

#### 3. LingBot-VLA
- **Organization:** Robbyant
- **Released:** January 2026
- **Parameters:** 4B (depth-free and depth-distilled variants)
- **License:** Apache-2.0
- **Key results:** Tested across 3 physical robot platforms with higher success rates than evaluated baselines. Pre-trained on 20,000+ hours of real-world interaction data. 1.5x-2.8x faster training than comparable frameworks.
- **VLA backbone suitability:** **Good.** Apache-2.0 is the most permissive license among VLA models. The 4B size hits a sweet spot between SmolVLA (too small) and OpenVLA (larger). Full production-ready codebase with data processing, fine-tuning, and evaluation tools included.

#### 4. A1 (Truncated VLA)
- **Organization:** Academic (arXiv April 2026)
- **Released:** April 2026
- **Parameters:** Not explicitly stated; uses pretrained VLM backbone with flow-matching action head
- **License:** Fully open-source (code, data pipeline, intermediate checkpoints, eval scripts)
- **Key results:** SOTA success rates on LIBERO, VLABench, and real robots (Franka, AgiBot). Up to 72% lower per-episode latency for flow-matching inference. Up to 76.6% backbone computation reduction with minor performance degradation. Leverages "implicit affordance priors" from pretrained VLMs.
- **VLA backbone suitability:** **Very promising for affordance research.** Explicitly designed around the idea that pretrained VLMs contain implicit affordance priors. Budget-aware adaptive inference and inter-layer truncated flow matching are novel and directly relevant to affordance-aware systems.

#### 5. SimpleVLA-RL
- **Organization:** PRIME-RL (ICLR 2026)
- **Released:** 2025 (paper); ICLR 2026 acceptance
- **Parameters:** Built on OpenVLA-OFT
- **License:** Open-source (GitHub)
- **Key results:** SOTA on LIBERO-Long at 97.6. From just 1 trajectory per task for cold-start SFT, raises OpenVLA-OFT from 17.3 to 91.7 (430% improvement). RL-based training for VLAs addressing data scarcity.
- **VLA backbone suitability:** **Critical for data-efficient training.** If your affordance research involves limited demonstration data, SimpleVLA-RL's RL framework is the current best approach for VLA training under data scarcity.

#### 6. NORA
- **Organization:** DeCLaRe Lab (academic)
- **Released:** April 2025
- **Parameters:** 3B (based on Qwen-2.5-VL-3B)
- **License:** Open-source (GitHub)
- **Key results:** Outperforms larger VLA models with lower computational overhead. Introduces Ego3D Position Encoding for 3D awareness and Adaptive Action Grids for spatial actions.
- **VLA backbone suitability:** **Good for 3D-aware manipulation.** The Ego3D encoding is directly relevant to affordance-aware systems that need spatial reasoning.

#### 7. StarVLA
- **Organization:** Academic (2026)
- **Released:** April 2026
- **Parameters:** Framework/codebase, not a single model
- **License:** Open-source (GitHub)
- **Key results:** SOTA on RoboCasa without pretraining. Supports DOMINO benchmark for dynamic manipulation. Unified codebase with diverse action-decoding designs.
- **VLA backbone suitability:** **Best as a research platform.** Lego-like modular codebase lets you swap action decoders, VLM backbones, and evaluation protocols. Ideal for systematic affordance research across architectures.

#### 8. MoTVLA
- **Organization:** Academic (ICLR 2026 submission)
- **Released:** October 2025
- **Parameters:** Mixture-of-Transformers architecture (sizes not specified)
- **License:** Unclear if open-sourced
- **Key results:** Superior on both language reasoning and manipulation benchmarks. Fast-slow dual reasoning where a generalist VLM handles perception/planning and a domain expert handles motion decomposition.
- **VLA backbone suitability:** **Architecturally interesting** for affordance research (fast-slow reasoning mirrors affordance detection vs. action execution), but availability is uncertain.

---

### CATEGORY 2: Frontier Open-Source LLMs (Potential Text Backbones)

| Model | Org | Parameters | Key Strength | License |
|---|---|---|---|---|
| **Qwen 3 235B-A22B** | Alibaba | 235B total / 22B active (MoE) | Best overall across benchmarks; reasoning + coding + multilingual | Apache 2.0 |
| **GLM-5.1** | Zhipu AI (Z.ai) | 744B total / 40B active (MoE) | #1 on Artificial Analysis Intelligence Index; 200K context | Open-source |
| **DeepSeek-V4-Pro** | DeepSeek | 1.6T total / 49B active | 1M context; MIT license | MIT |
| **DeepSeek-V4-Flash** | DeepSeek | 284B total / 13B active | 1M context; efficient variant | MIT |
| **Kimi K2.6 Thinking** | Moonshot AI | Not specified | #1 open-source coding (78.57 Coding Avg, 58.33 Agentic Coding) | Not specified |
| **Llama 4 Scout** | Meta | MoE | 10M token context window | Llama license |

---

### CATEGORY 3: Frontier Open-Source Vision-Language Models (VLM Backbones for VLA)

| Model | Org | Parameters | Key Strength | License |
|---|---|---|---|---|
| **Qwen3-VL-235B-A22B** | Alibaba | 235B total / 22B active | Rivals GPT-5 and Gemini-2.5-Pro on multimodal benchmarks; 256K context; thinking variants; UI/agent grounding | Apache 2.0 |
| **GLM-4.6V** | Zhipu AI | 106B total / 12B active (MoE) | Native tool calling; 128K context; first-class image/video/tool input | Open-source (9B Flash variant free for commercial use) |
| **InternVL3-78B** | OpenGVLab (Shanghai AI Lab) | 78B (6B InternViT + 72.7B Qwen2.5 LM) | 72.2 MMMU (SOTA open-source); native multimodal pre-training | Commercial use permitted |
| **InternVL3.5-241B-A28B** | OpenGVLab | 241B total / 28B active | Latest SOTA among open-source MLLMs | Commercial use permitted |
| **GLM-4.5V** | Zhipu AI | 106B total / 12B active | SOTA on 41 public multimodal benchmarks | Open-source |

**Model sizes available for InternVL3:** 1B, 2B, 8B, 14B, 38B, 78B (and 241B MoE for v3.5).
**Model sizes available for Qwen3-VL:** Multiple sizes up to 235B-A22B, including smaller variants runnable locally.

---

### RECOMMENDATIONS FOR AFFORDANCE-AWARE VLA RESEARCH

**Best overall starting point:** **OpenVLA + OFT + SimpleVLA-RL stack.** This gives you the most mature VLA (OpenVLA-7B), the best fine-tuning recipe (OFT for 26x faster inference and 97.1% success), and RL-based training (SimpleVLA-RL for data-efficient learning). MIT code license, Llama weights license.

**Best for full openness and permissive licensing:** **LingBot-VLA** (Apache-2.0, 4B, production-ready) or **A1** (fully transparent with all artifacts released).

**Best VLM backbone if building a custom VLA:** **Qwen3-VL-235B-A22B** (Apache 2.0, rivals proprietary frontier models) or **InternVL3.5** (commercial-friendly, native multimodal pre-training, multiple size variants from 1B to 241B for scaling experiments).

**Best for affordance-specific research:** **A1** -- it explicitly models "implicit affordance priors" from pretrained VLMs and provides budget-aware adaptive inference. Combined with **NORA's** Ego3D Position Encoding for 3D spatial affordance grounding, these two provide the most directly relevant architectures.

**Best research platform for systematic experiments:** **StarVLA** -- modular codebase letting you swap VLM backbones, action decoders, and benchmarks.

---

Sources:
- [Top 10 Physical AI Models Powering Real-World Robots in 2026](https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/)
- [VLA Models Compared: OpenVLA vs pi0 vs SmolVLA vs RT-2 (2026 Guide)](https://www.roboticscenter.ai/learn/vla-models-comparison)
- [A1: A Fully Transparent Open-Source VLA Model](https://arxiv.org/abs/2604.05672)
- [StarVLA GitHub](https://github.com/starVLA/starVLA)
- [SimpleVLA-RL: Scaling VLA Training via RL (ICLR 2026)](https://github.com/PRIME-RL/SimpleVLA-RL)
- [NORA: A Small Open-Sourced Generalist VLA Model](https://arxiv.org/abs/2504.19854)
- [LingBot-VLA GitHub](https://github.com/robbyant/lingbot-vla)
- [Robbyant Open-Sources LingBot-VLA](https://www.roboticstomorrow.com/news/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/26071/)
- [SmolVLA - Hugging Face](https://techcrunch.com/2025/06/04/hugging-face-says-its-new-robotics-model-is-so-efficient-it-can-run-on-a-macbook/)
- [OpenVLA-OFT: Fine-Tuning VLAs](https://arxiv.org/abs/2502.19645)
- [OpenVLA GitHub](https://github.com/openvla/openvla)
- [MoTVLA: Fast-Slow Reasoning VLA](https://arxiv.org/abs/2510.18337)
- [Best Open-Source LLMs in 2026 - BentoML](https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models)
- [Top Open-Source LLMs 2026 - DataCamp](https://www.datacamp.com/blog/top-open-source-llms)
- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)
- [Qwen3-VL GitHub](https://github.com/QwenLM/Qwen3-VL)
- [GLM-4.6V Release - MarkTechPost](https://www.marktechpost.com/2025/12/09/zhipu-ai-releases-glm-4-6v-a-128k-context-vision-language-model-with-native-tool-calling/)
- [InternVL3 - OpenGVLab](https://internvl.github.io/)
- [InternVL3.5-8B on Hugging Face](https://huggingface.co/OpenGVLab/InternVL3_5-8B)
- [Best Open-Source VLMs 2026 - Labellerr](https://www.labellerr.com/blog/top-open-source-vision-language-models/)
- [Best Open-Source Multimodal Models 2026 - SiliconFlow](https://www.siliconflow.com/articles/en/best-open-source-multimodal-models-2025)
- [GLM-5.1 Review 2026](https://www.buildfastwithai.com/blogs/glm-5-1-open-source-review-2026)
- [Physical Intelligence pi0 vs OpenVLA](https://www.roboticscenter.ai/physical-intelligence-pi0-vs-openvla)
- [WholebodyVLA (ICLR 2026)](https://github.com/OpenDriveLab/WholebodyVLA)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "331210d8-b57b-4349-ab6c-19cf09be25f0",
  "isSidechain": true,
  "agentId": "a85bd974213dd0e1a",
  "requestId": "req_011CbAXiEaUbP4foeQCTc8Xm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28e195bf-150c-410a-9b73-343f4fb36565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STfmps1cWxYg5rUo56xxZb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1631,
      "cache_creation_input_tokens": 2862,
      "cache_read_input_tokens": 21997,
      "output_tokens": 3857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2862
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1631,
          "output_tokens": 3857,
          "cache_read_input_tokens": 21997,
          "cache_creation_input_tokens": 2862,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2862,
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
