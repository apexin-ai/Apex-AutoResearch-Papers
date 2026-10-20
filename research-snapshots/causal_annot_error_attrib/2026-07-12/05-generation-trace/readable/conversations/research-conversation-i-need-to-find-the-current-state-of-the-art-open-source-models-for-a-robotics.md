# Research conversation: I need to find the current state-of-the-art open-source models for a robotics VLA (Vision-Language-Action) research proj

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a67129ccf8a63acd8.jsonl`
- **Structured JSON:** [`92d848fa4e8ca5a4b99d.json`](../../sessions/92/92d848fa4e8ca5a4b99d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-18T18:18:28.692Z_

I need to find the current state-of-the-art open-source models for a robotics VLA (Vision-Language-Action) research project in May 2026. Perform these searches and report the top models with their key details:

1. WebSearch: "best open source VLA model 2026 robot manipulation"
2. WebSearch: "state of the art vision language action model 2026 open source"
3. WebSearch: "best open source VLM 2026 vision language model"
4. WebSearch: "OpenVLA successor 2026 open source robot foundation model"
5. WebSearch: "π0 pi-zero robot foundation model 2026"
6. WebSearch: "octo robot model successor 2026 open weights"

For each model found, report:
- Model name and version
- Parameter count
- Whether weights are publicly available
- Key benchmark results if available
- Whether it's suitable as a VLA backbone that could be modified for affordance-conditioned action generation

I need this to recommend the right backbone model for the research approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "b32457d9-fd8a-49d0-9be1-5d9ad2e25bb6",
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

_source line 2 · 2026-05-18T18:18:28.697Z_

```json
{
  "parentUuid": "b32457d9-fd8a-49d0-9be1-5d9ad2e25bb6",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
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
  "uuid": "766a1140-5886-45e4-a3b7-243180f584d7",
  "timestamp": "2026-05-18T18:18:28.697Z",
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

_source line 3 · 2026-05-18T18:18:33.513Z_



I'll perform all six searches in parallel to gather comprehensive information about the current state-of-the-art VLA models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "766a1140-5886-45e4-a3b7-243180f584d7",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVe1pRg83gABJH9M6Tj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70405284-4b18-479c-8d82-35ba9e8b6c8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XBMUiPsNQZTWBp1UVFAg5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 773,
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

_source line 4 · 2026-05-18T18:18:33.618Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01V8hYGhECHyT785sBV6E8Vc`</summary>

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
  "parentUuid": "70405284-4b18-479c-8d82-35ba9e8b6c8f",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVe1pRg83gABJH9M6Tj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6eea1fea-d9f2-40f8-bd3d-26f479266039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XBMUiPsNQZTWBp1UVFAg5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 7304,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 773
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 773,
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

_source line 5 · 2026-05-18T18:18:33.621Z_

<details><summary>↩ Tool result · `toolu_01V8hYGhECHyT785sBV6E8Vc`</summary>

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
  "parentUuid": "6eea1fea-d9f2-40f8-bd3d-26f479266039",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "cc33af80-19de-4c15-b4c9-a2b0a88efe3e",
  "sourceToolAssistantUUID": "6eea1fea-d9f2-40f8-bd3d-26f479266039",
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

_source line 6 · 2026-05-18T18:18:35.912Z_



Now let me run all six searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc33af80-19de-4c15-b4c9-a2b0a88efe3e",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVeP57g9NLkuxPU8UEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21329757-9393-41a8-81c4-320cc2b18f49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNRhYkGSvJNgL2tjMSWTZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8077,
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

_source line 7 · 2026-05-18T18:18:36.376Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PPBd6fe3GdXv5MQmdSHDAt`</summary>

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
  "parentUuid": "21329757-9393-41a8-81c4-320cc2b18f49",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVeP57g9NLkuxPU8UEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f30b0ab4-3808-4fd3-b3d8-f67b0e84e3e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNRhYkGSvJNgL2tjMSWTZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8077,
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

_source line 8 · 2026-05-18T18:18:36.900Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W3ZWdES3duztsigEUsrwWJ`</summary>

```json
{
  "query": "state of the art vision language action model 2026 open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f30b0ab4-3808-4fd3-b3d8-f67b0e84e3e5",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVeP57g9NLkuxPU8UEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de5726ff-ba40-423a-bc01-0789946455ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNRhYkGSvJNgL2tjMSWTZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8077,
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

_source line 9 · 2026-05-18T18:18:36.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QhGFzJ4qsWPtbzHboPsnFm`</summary>

```json
{
  "query": "best open source VLM 2026 vision language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de5726ff-ba40-423a-bc01-0789946455ce",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVeP57g9NLkuxPU8UEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8aaa32fe-afe0-4472-a59c-52f5d9a1242b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNRhYkGSvJNgL2tjMSWTZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8077,
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

_source line 10 · 2026-05-18T18:18:37.385Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L4NEY4tuQ3JheEmk9SQAFL`</summary>

```json
{
  "query": "OpenVLA successor 2026 open source robot foundation model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aaa32fe-afe0-4472-a59c-52f5d9a1242b",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVeP57g9NLkuxPU8UEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc2579a7-d0b7-4604-8b0d-dccc6db7c465",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNRhYkGSvJNgL2tjMSWTZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8077,
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

_source line 11 · 2026-05-18T18:18:37.837Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ETZ2scL5bqiYnwz34dQqXg`</summary>

```json
{
  "query": "π0 pi-zero robot foundation model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc2579a7-d0b7-4604-8b0d-dccc6db7c465",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVeP57g9NLkuxPU8UEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba91f0d8-2002-47d8-9073-f1555d6f7603",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNRhYkGSvJNgL2tjMSWTZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8077,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1420
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 308,
          "cache_read_input_tokens": 8077,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1420,
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

_source line 12 · 2026-05-18T18:18:37.879Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RpQiiSdFM99pe9UZNjrRKJ`</summary>

```json
{
  "query": "octo robot model successor 2026 open weights"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba91f0d8-2002-47d8-9073-f1555d6f7603",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVeP57g9NLkuxPU8UEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdc7ecaa-1b8e-416a-b2b6-fe7e5f6c0c91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNRhYkGSvJNgL2tjMSWTZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8077,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1420
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 308,
          "cache_read_input_tokens": 8077,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1420,
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

_source line 13 · 2026-05-18T18:18:43.565Z_

<details><summary>↩ Tool result · `toolu_01L4NEY4tuQ3JheEmk9SQAFL`</summary>

```text
Web search results for query: "OpenVLA successor 2026 open source robot foundation model"

Links: [{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/learn/vla-models-comparison"},{"title":"Generative AI in Industrial Robotics: 2026 Layers Guide","url":"https://www.evsint.com/generative-ai-industrial-robotics-foundation-models-code-generation-2026/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"OpenVLA | Open Source Robotics","url":"https://robotics.growbotics.ai/projects/foundation-models/openvla"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"},{"title":"Robbyant Open-Sources LingBot-VLA as a “Universal Brain” for Robots | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/26071/"}]

Based on the search results, here's what I found regarding OpenVLA successors and open-source robot foundation models in 2026:

## Key Open-Source Robot Foundation Models in 2026

OpenVLA (Stanford University, 2024) provided a fully open-weights alternative at 7 billion parameters with an Apache 2.0 license, making it the primary research and early-industrial-pilot baseline for labs without access to proprietary compute.

### Successors and Related Models:

**Physical Intelligence's π0**: π0 (2024–25) introduced a flow-matching action head in place of discrete token classification, producing smoother trajectories better suited to multi-stage dexterous tasks.

**NVIDIA's GR00T N1**: The publicly released GR00T-N1-2B model has 2.2B parameters in total, with 1.34B in the VLM. It designs a compositional model integrating Vision-Language Model-based reasoning and Diffusion Transformer-based action modules, supporting a wide range of robot embodiments and enabling rapid adaptation to new tasks.

**LingBot-VLA**: LingBot-VLA has been successfully adapted to robots from leading manufacturers and achieved higher task success rates than other evaluated models in tests across three distinct physical robot platforms.

These represent the current landscape of open-source robot foundation models available in 2026, with several alternatives to OpenVLA offering different architectural approaches and performance characteristics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc2579a7-d0b7-4604-8b0d-dccc6db7c465",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "145deb42-e877-450d-92dc-071dc54ba699",
  "sourceToolAssistantUUID": "dc2579a7-d0b7-4604-8b0d-dccc6db7c465",
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

_source line 14 · 2026-05-18T18:18:44.273Z_

<details><summary>↩ Tool result · `toolu_01PPBd6fe3GdXv5MQmdSHDAt`</summary>

```text
Web search results for query: "best open source VLA model 2026 robot manipulation"

Links: [{"title":"Top 10 Physical AI Models Powering Real-World Robots in 2026 - MarkTechPost","url":"https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/"},{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/learn/vla-models-comparison"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Robbyant Open-Sources LingBot-VLA as a “Universal Brain” for Robots | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/26071/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"}]

Based on the search results, here are the leading open-source VLA models for robot manipulation in 2026:

## Top Open-Source VLA Models

**OpenVLA** stands out as a highly effective option: OpenVLA is a 7B-parameter open-source VLA trained on a diverse collection of 970,000 real-world robot demonstrations. Despite being 7× smaller, OpenVLA outperforms the closed RT-2-X (55B parameters) by 16.5 percentage points in absolute task success rate across 29 tasks and multiple robot embodiments.

**SmolVLA** offers a practical alternative focused on efficiency: On the LIBERO benchmark, SmolVLA achieves 82–90% success — within 5% of OpenVLA despite having 16x fewer parameters. The key advantage is inference speed: SmolVLA runs at 15–30 Hz on a single RTX 4090, fast enough for reactive manipulation.

**LingBot-VLA** has recently gained prominence: Robbyant announced the open-source release of LingBot-VLA, a vision-language-action (VLA) model designed to serve as a "universal brain" for real-world robotics. In tests conducted across three distinct physical robot platforms, LingBot-VLA achieved higher task success rates than other evaluated models.

**A1** is another fully transparent option: A1 is a fully open-source and transparent VLA framework designed for low-cost, high-throughput inference without sacrificing manipulation success, with the full training stack released to enable end-to-end reproducibility.

The choice between these models depends on your priorities—whether you value raw performance (OpenVLA), inference speed (SmolVLA), cross-platform robustness (LingBot-VLA), or transparency and reproducibility (A1).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f30b0ab4-3808-4fd3-b3d8-f67b0e84e3e5",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "e3780a9c-2ae6-4cfa-a077-6ef8f8a46645",
  "sourceToolAssistantUUID": "f30b0ab4-3808-4fd3-b3d8-f67b0e84e3e5",
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

_source line 15 · 2026-05-18T18:18:44.741Z_

<details><summary>↩ Tool result · `toolu_01RpQiiSdFM99pe9UZNjrRKJ`</summary>

```text
Web search results for query: "octo robot model successor 2026 open weights"

Links: [{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/"},{"title":"An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/paper.pdf"},{"title":"GitHub - octo-models/octo: Octo is a transformer-based robot policy trained on a diverse mix of 800k robot trajectories. · GitHub","url":"https://github.com/octo-models/octo"},{"title":"[2405.12213] Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/abs/2405.12213"},{"title":"Top 10 Physical AI Models Powering Real-World Robots in 2026 - MarkTechPost","url":"https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/html/2405.12213v2"},{"title":"Foundation Models: The AI Revolution in Robotics 2026 | OnOff.gr","url":"https://www.onoff.gr/blog/en/robot/foundation-models-ai-robotics-2026/"},{"title":"Octo: An Open-Source Generalist Robot Policy | Request PDF","url":"https://www.researchgate.net/publication/383897130_Octo_An_Open-Source_Generalist_Robot_Policy"},{"title":"Open-Weight Foundation Models for Robotics (2025 Guide) | RoboCloud Hub","url":"https://robocloud-dashboard.vercel.app/learn/blog/open-weight-robot-models"},{"title":"GitHub - emb-ai/octo-pytorch: Octo manipulation policy in PyTorch · GitHub","url":"https://github.com/emb-ai/octo-pytorch"}]

Based on the search results, here's what I found about the Octo robot model and its successors in 2026:

## Octo Model Overview

Octo is a transformer-based diffusion policy pretrained on 800k robot episodes from the Open X-Embodiment dataset, with two initial versions available: Octo-Small (27M parameters) and Octo-Base (93M parameters).

## 2026 Context

Octo was designed specifically to support efficient finetuning to new robot setups, outperforming training from scratch by an average of 52% across six evaluation setups, performs comparably to RT-2-X (55B parameters) in zero-shot settings while being orders of magnitude smaller, and is primarily a research and developer tool serving as a strong lightweight starting point for labs needing to iterate quickly on new manipulation tasks with limited compute.

## Open-Weight Status

In the robotics AI landscape, Octo is part of the open-source community alongside OpenVLA and Llama-based robotics models, which are free, reproducible, and community-driven. Octo runs on consumer GPUs, making cutting-edge robotics AI accessible to small labs and startups worldwide.

As of May 2026, the search results don't indicate a specific successor model to Octo, but rather show it continuing to be used as a strong foundational open-weight model in the broader ecosystem of robot policies that includes models like OpenVLA and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdc7ecaa-1b8e-416a-b2b6-fe7e5f6c0c91",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "70b48527-d9e7-4150-9a57-1158e8ef6118",
  "sourceToolAssistantUUID": "bdc7ecaa-1b8e-416a-b2b6-fe7e5f6c0c91",
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

_source line 16 · 2026-05-18T18:18:45.631Z_

<details><summary>↩ Tool result · `toolu_01ETZ2scL5bqiYnwz34dQqXg`</summary>

```text
Web search results for query: "π0 pi-zero robot foundation model 2026"

Links: [{"title":"π 0 : Our First Generalist Policy","url":"https://www.pi.website/blog/pi0"},{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"},{"title":"Physical Intelligence (π)","url":"https://www.pi.website/"},{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"},{"title":"Physical Intelligence open-sources Pi0 robotics foundation model","url":"https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"},{"title":"Our First Generalist Policy","url":"https://physicalintelligence.company/blog/pi0"},{"title":"Physical Intelligence π0 vs OpenVLA: Best VLA Model for Robot Learning 2026 | SVRC","url":"https://www.roboticscenter.ai/physical-intelligence-pi0-vs-openvla"},{"title":"Physical Intelligence (Pi): Company Profile & Analysis 2026 | SVRC","url":"https://www.roboticscenter.ai/companies/physical-intelligence"}]

Based on the search results, here's what I found about π0 (pi-zero):

## Overview

π0 is a general-purpose robot foundation model developed by Physical Intelligence over eight months. Physical Intelligence is betting that the future of robotics is not better hardware but better brains — specifically, a single foundation model that can control any robot to perform any task.

## Technical Architecture

Unlike LLMs, it spans images, text, and actions and acquires physical intelligence by training on embodied experience from robots, learning to directly output low-level motor commands via a novel architecture. π0 uses a smaller 3 billion parameter VLM as a starting point, and dexterous robot manipulation requires π0 to output motor commands at a high frequency, up to 50 times per second.

## Capabilities

It can control a variety of different robots, and can either be prompted to carry out the desired task, or fine-tuned to specialize it to challenging application scenarios. The model was pre-trained on over 10,000 hours of robot data, and fine-tuned to dexterous tasks including laundry folding, clearing a table, putting dishes in a microwave, stacking eggs into a carton, assembling a box, and bagging groceries.

## Recent Developments in 2026

π0.7: a Steerable Model with Emergent Capabilities was announced April 16, 2026 as a steerable robotic foundation model that exhibits a step-change in generalization. Multi-Scale Embodied Memory (MEM) gives models both long-term and short-term memory, enabling complex tasks longer than ten minutes.

## Open Source Release

Physical Intelligence has released the code and weights for Pi0 as part of its experimental openpi repository on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba91f0d8-2002-47d8-9073-f1555d6f7603",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "2a77c379-d50b-42ea-96ba-eb246ffc1667",
  "sourceToolAssistantUUID": "ba91f0d8-2002-47d8-9073-f1555d6f7603",
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

_source line 17 · 2026-05-18T18:18:46.797Z_

<details><summary>↩ Tool result · `toolu_01W3ZWdES3duztsigEUsrwWJ`</summary>

```text
Web search results for query: "state of the art vision language action model 2026 open source"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | alphaXiv","url":"https://www.alphaxiv.org/overview/2406.09246v3"},{"title":"Multimodal AI: The Best Open-Source Vision Language Models in 2026","url":"https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"Survey of Open-Source Vision Language Models (2026) | Hacker News","url":"https://news.ycombinator.com/item?id=47247663"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Dexbotic: Open-Source Vision-Language-Action Toolbox","url":"https://arxiv.org/pdf/2510.23511"}]

Based on the search results, here are the state-of-the-art open-source vision-language-action models in 2026:

## Leading Models

**A1 (Most Recent - April 2026)**
A1 is a fully open-source and transparent VLA framework designed for low-cost, high-throughput inference that achieves state-of-the-art success rates while significantly reducing inference cost. On RoboChallenge, A1 achieves an average success rate of 29.00%, outperforming baselines including π₀ (28.33%), X-VLA (21.33%), and RDT-1B (15.00%). A1 releases the full training stack including training code, data/data-processing pipeline, intermediate checkpoints, and evaluation scripts.

**OpenVLA**
OpenVLA is a state-of-the-art, open-source 7B-parameter VLA model that obtains strong performance for cross-embodiment robot control out-of-the-box and can be easily adapted to new robot setups via parameter-efficient fine-tuning. OpenVLA is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations.

## Related Open-Source Tools

Dexbotic is an open-source Vision-Language-Action (VLA) model toolbox that provides a one-stop VLA research service for professionals in the field of embodied intelligence with support for multiple mainstream VLA policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de5726ff-ba40-423a-bc01-0789946455ce",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "d9c0df4d-02e3-4ba6-bad6-ce6d75094cde",
  "sourceToolAssistantUUID": "de5726ff-ba40-423a-bc01-0789946455ce",
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

_source line 18 · 2026-05-18T18:18:50.966Z_

<details><summary>↩ Tool result · `toolu_01QhGFzJ4qsWPtbzHboPsnFm`</summary>

```text
Web search results for query: "best open source VLM 2026 vision language model"

Links: [{"title":"Top 10 Vision Language Models in 2026 | Benchmark, Use Cases","url":"https://dextralabs.com/blog/top-10-vision-language-models/"},{"title":"Ultimate Guide - The Best Open Source LLM for Document Screening in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLM-for-Document-screening"},{"title":"Best Open-Source Vision Language Models of 2026","url":"https://www.labellerr.com/blog/top-open-source-vision-language-models/"},{"title":"Ultimate Guide - The Best Open Source Multimodal Models in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-multimodal-models-2025"},{"title":"Multimodal AI: The Best Open-Source Vision Language Models in 2026","url":"https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models"},{"title":"Top 10 Vision Language Models in 2026 | DataCamp","url":"https://www.datacamp.com/blog/top-vision-language-models"}]

Based on the search results, here are the best open-source Vision Language Models (VLMs) in 2026:

## Top Open-Source VLMs for 2026

The top three recommendations for 2026 are GLM-4.5V, GLM-4.1V-9B-Thinking, and Qwen2.5-VL-32B-Instruct.

**GLM-4.5V** stands out as a leading option. GLM-4.5V is the latest generation vision-language model released by Zhipu AI, built on a Mixture-of-Experts architecture with 106B total parameters and 12B active parameters, and excels at processing diverse visual content including images, videos, and long documents. It achieves state-of-the-art performance among open-source models of its scale on 41 public multimodal benchmarks.

Other notable open-source VLMs include:

- Gemma 3 – A strong open-source option with OCR and multilingual support for document analysis, medical imaging, and content moderation
- LLaMA 3.2 Vision – Structures data very well from images, excellent for ID verification, invoice processing, and parsing legal documents
- Molmo models, available in 1B, 7B, and 72B parameters, deliver state-of-the-art performance for their class and can perform on a par with proprietary models like GPT-4V, Gemini 1.5 Pro, and Claude 3.5 Sonnet

The latest wave, from Qwen3-VL to GLM-4.6V, pushes open-source multimodality into new territory once dominated by proprietary systems like GPT-5 and Gemini-2.5-Pro.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8aaa32fe-afe0-4472-a59c-52f5d9a1242b",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "3bbb6915-584d-4e20-a67f-9c34a73d31bb",
  "sourceToolAssistantUUID": "8aaa32fe-afe0-4472-a59c-52f5d9a1242b",
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

_source line 19 · 2026-05-18T18:18:54.055Z_

Let me do a few more targeted searches to fill in gaps on specific models and their suitability as VLA backbones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bbb6915-584d-4e20-a67f-9c34a73d31bb",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVff35eJmo9pTu5fEQn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11e6e17c-c812-42b2-aa47-e96d06faf986",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZm655evVNzzpFSTn1o3Jk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2457,
      "cache_creation_input_tokens": 2785,
      "cache_read_input_tokens": 9497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2785,
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

_source line 20 · 2026-05-18T18:18:55.164Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WySQagi3Qd4t8WwWcbAWJY`</summary>

```json
{
  "query": "OpenVLA-OFT OpenVLA v2 2025 2026 fine-tuning improvements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11e6e17c-c812-42b2-aa47-e96d06faf986",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVff35eJmo9pTu5fEQn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08cb00f4-3830-4819-9d04-89eba42a5f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZm655evVNzzpFSTn1o3Jk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2457,
      "cache_creation_input_tokens": 2785,
      "cache_read_input_tokens": 9497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2785,
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

_source line 21 · 2026-05-18T18:18:55.472Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T9v74pdkJDdigtvMnWPrXi`</summary>

```json
{
  "query": "SmolVLA parameters architecture 2025 2026 huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08cb00f4-3830-4819-9d04-89eba42a5f48",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVff35eJmo9pTu5fEQn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f8dfe41-78ad-40fd-8eab-2e3647a2ec91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZm655evVNzzpFSTn1o3Jk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2457,
      "cache_creation_input_tokens": 2785,
      "cache_read_input_tokens": 9497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2785,
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

_source line 22 · 2026-05-18T18:18:55.942Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y11LRTMKHWCfqGt7PSHnME`</summary>

```json
{
  "query": "pi0 open weights openpi download model size parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f8dfe41-78ad-40fd-8eab-2e3647a2ec91",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVff35eJmo9pTu5fEQn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b23ad614-2880-4146-929e-0a5460e7a323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZm655evVNzzpFSTn1o3Jk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2457,
      "cache_creation_input_tokens": 2785,
      "cache_read_input_tokens": 9497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2785,
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

_source line 23 · 2026-05-18T18:18:56.655Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QCZjB2iJm7kF4yG8kC69aH`</summary>

```json
{
  "query": "A1 VLA model 2026 parameters benchmark results architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b23ad614-2880-4146-929e-0a5460e7a323",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVff35eJmo9pTu5fEQn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e91e9955-1fff-47c8-8bc9-919b63158f83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZm655evVNzzpFSTn1o3Jk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2457,
      "cache_creation_input_tokens": 2785,
      "cache_read_input_tokens": 9497,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2457,
          "output_tokens": 247,
          "cache_read_input_tokens": 9497,
          "cache_creation_input_tokens": 2785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2785,
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

_source line 24 · 2026-05-18T18:19:02.023Z_

<details><summary>↩ Tool result · `toolu_01T9v74pdkJDdigtvMnWPrXi`</summary>

```text
Web search results for query: "SmolVLA parameters architecture 2025 2026 huggingface"

Links: [{"title":"Hugging Face Releases SmolVLA, a Compact Open-Source Robotics Model -- Pure AI","url":"https://pureai.com/articles/2025/06/10/hugging-face-releases-smolvla.aspx"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"AI and Robotics: With SmolVLA, Hugging Face Opens Vision-Language-Action Models to the Community","url":"https://www.actuia.com/en/news/ai-and-robotics-with-smolvla-hugging-face-opens-vision-language-action-models-to-the-community/"},{"title":"blog/smolvla.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/smolvla.md"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"}]

Based on the search results, here's what I found about SmolVLA's parameters and architecture:

## Parameters

SmolVLA is a 450 million parameter model, making it significantly more compact than existing VLA models. The architecture is modular, with an action expert comprising 100 million parameters that predicts robot actions.

## Architecture

SmolVLA consists of two core components: a Vision-Language Model (VLM) that processes multimodal inputs and an action expert that outputs robot control commands.

**Vision-Language Model Component:**
SmolVLA uses SmolVLM2 as its VLM backbone, which is optimized for multi-image inputs and consists of a SigLIP vision encoder and a SmolLM2 language decoder.

**Key Efficiency Features:**
SmolVLA applies three key techniques: reducing the number of visual tokens, skipping upper layers in the VLM, and interleaving cross- and self-attention layers in the action expert. Additionally, layer skipping allows for faster execution by bypassing certain model layers, and asynchronous inference allows action prediction during the execution of the previous one.

**Performance:**
Despite its relatively small size and modest training data—fewer than 30,000 episodes—SmolVLA matches or outperforms larger models like ACT on both simulated and real-world benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f8dfe41-78ad-40fd-8eab-2e3647a2ec91",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "0d9b8dd3-0507-4e48-9602-c1b4a078ae26",
  "sourceToolAssistantUUID": "3f8dfe41-78ad-40fd-8eab-2e3647a2ec91",
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

_source line 25 · 2026-05-18T18:19:02.266Z_

<details><summary>↩ Tool result · `toolu_01WySQagi3Qd4t8WwWcbAWJY`</summary>

```text
Web search results for query: "OpenVLA-OFT OpenVLA v2 2025 2026 fine-tuning improvements"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"[Literature Review] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.themoonlight.io/en/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"},{"title":"openvla/README.md at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/README.md"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/html/2603.16044v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"}]

Based on the search results, here's what I found about OpenVLA-OFT and OpenVLA v2 fine-tuning improvements:

## OpenVLA-OFT Overview

OpenVLA-OFT is an Optimized Fine-Tuning recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to improve inference efficiency, policy performance, and flexibility in the model's input-output specifications.

## Key Performance Improvements

OpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×.

Through parallel decoding and action chunking, OpenVLA-OFT obtains 26x faster action generation speed and 3x lower latency than the base OpenVLA model.

## Real-World Applications

The resulting OpenVLA-OFT+ policies execute diverse dexterous manipulation tasks on a real-world bimanual robot at high control frequencies (25 Hz). The "+" suffix indicates the integration of feature-wise linear modulation (FiLM), which strengthens language grounding in tasks where accurate language understanding is critical for success.

## OpenVLA v2 Updates

In the updated OpenVLA paper (v2), fine-tuning OpenVLA on a simulated benchmark, LIBERO, is discussed in Appendix E, including how demonstration datasets were modified to improve the overall performance of all methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08cb00f4-3830-4819-9d04-89eba42a5f48",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "59cb08fb-a999-4798-96a4-bebc3c585292",
  "sourceToolAssistantUUID": "08cb00f4-3830-4819-9d04-89eba42a5f48",
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

_source line 26 · 2026-05-18T18:19:03.328Z_

<details><summary>↩ Tool result · `toolu_01Y11LRTMKHWCfqGt7PSHnME`</summary>

```text
Web search results for query: "pi0 open weights openpi download model size parameters"

Links: [{"title":"openpi/src/openpi/training/config.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/src/openpi/training/config.py"},{"title":"Pi0 and Pi0.5 fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"Physical Intelligence open-sources Pi0 robotics foundation model","url":"https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"},{"title":"question about lora fine-tuning for pi0.5 · Issue #672 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/672"},{"title":"GitHub - allenzren/open-pi-zero: Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence · GitHub","url":"https://github.com/allenzren/open-pi-zero"},{"title":"openpi — Trossen Robotics Trossen Arm Documentation","url":"https://docs.trossenrobotics.com/trossen_arm/v1.9/tutorials/openpi.html"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"}]

Based on the search results, here's what I found about Pi0 open weights and the OpenPI model:

## Release and Availability

Physical Intelligence has released the code and weights for Pi0 as part of its experimental openpi repository on GitHub. It also provides checkpoints for a few "simple tasks" on available platforms such as ALOHA and DROID, example code to run inference on real-world and simulated robot platforms, and the code for fine-tuning the base π0 model for your own tasks and platforms.

## Model Architecture and Parameters

Based on a community implementation, the model adopts a MoE-like architecture and uses a pre-trained 3B PaliGemma VLM (2.291B to be fine-tuned) and a new set of action expert parameters (0.315B).

## Framework Support

HuggingFace has also prepared a PyTorch port of openpi for those developers who prefer PyTorch over JAX.

## Fine-tuning Capabilities

The company said between 1-20 hours of data was sufficient to tune Pi0 to a variety of tasks in its own experiments.

The official OpenPI repository on GitHub appears to be the primary source for accessing the open-weight model and code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b23ad614-2880-4146-929e-0a5460e7a323",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "2b67bab5-747b-4c14-9d3b-985e185202af",
  "sourceToolAssistantUUID": "b23ad614-2880-4146-929e-0a5460e7a323",
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

_source line 27 · 2026-05-18T18:19:04.245Z_

<details><summary>↩ Tool result · `toolu_01QCZjB2iJm7kF4yG8kC69aH`</summary>

```text
Web search results for query: "A1 VLA model 2026 parameters benchmark results architecture"

Links: [{"title":"Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline","url":"https://arxiv.org/pdf/2602.22663"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.19233"},{"title":"Experiences from Benchmarking Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/pdf/2511.11298"},{"title":"Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment","url":"https://arxiv.org/pdf/2511.04555"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Cross-Platform Scaling of Vision-Language-Action Models from Edge to Cloud GPUs","url":"https://arxiv.org/pdf/2509.11480"},{"title":"Cross-Platform Scaling of Vision-Language-Action Models from Edge to Cloud GPUs","url":"https://arxiv.org/html/2509.11480v1"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/pdf/2512.11891"},{"title":"vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.13966"}]

Based on the search results, I found comprehensive information about Vision-Language-Action (VLA) models and their benchmarks as of 2026. Here's what the research reveals:

## Key VLA Models and Parameters

Evo-1 is a lightweight VLA architecture with only 0.77B parameters, while OpenVLA is a 7B-parameter open-source model trained on 970K robot demonstrations from the Open X-Embodiment (OXE) dataset. Recent mechanistic studies have analyzed six models spanning 80M-7B parameters.

## Architecture Features

Modern VLA architectures integrate a compact VLM backbone with multi-view perception, proprioceptive tokenization, and action chunking. Hierarchical and late fusion architectures achieve the highest manipulation success and generalization, with diffusion-based decoders demonstrating superior cross-domain transfer and robustness compared to autoregressive heads.

## Benchmark Results

Evo-1 sets a new state-of-the-art on Meta-World (80.6%) and RoboTwin suite (37.8%), surpassing previous bests of 68.2% and 30.9%, respectively, and reaches 94.8% on LIBERO. OpenVLA-OFT achieves a 97.1% success rate on the LIBERO benchmark.

## Evaluation Framework

A unified evaluation framework supports 13 simulation benchmarks and achieves a 47× throughput improvement through parallel evaluation, completing 2,000 LIBERO episodes in approximately 18 minutes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e91e9955-1fff-47c8-8bc9-919b63158f83",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "3e43217a-479d-40ce-ae89-827e5f5f732d",
  "sourceToolAssistantUUID": "e91e9955-1fff-47c8-8bc9-919b63158f83",
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

### Tool call

_source line 28 · 2026-05-18T18:19:07.639Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MTfXHWE44kUHT1pPbWKaXt`</summary>

```json
{
  "query": "GR00T N1 NVIDIA open weights parameters download 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e43217a-479d-40ce-ae89-827e5f5f732d",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVgdpSFPXognzPetzVf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6be522c1-eaac-4cad-af97-3fa3390efbc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWcgPrdz4Qwnh11G5SeW6Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5909,
      "cache_read_input_tokens": 12282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5909,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 29 · 2026-05-18T18:19:08.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016h4kEt6K3wBzptKwu9QEEu`</summary>

```json
{
  "query": "LingBot-VLA Robbyant parameters architecture open source weights 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6be522c1-eaac-4cad-af97-3fa3390efbc0",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVgdpSFPXognzPetzVf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e38353b0-7ec7-4abd-8cff-ff7b24167131",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWcgPrdz4Qwnh11G5SeW6Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5909,
      "cache_read_input_tokens": 12282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5909,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 30 · 2026-05-18T18:19:09.209Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B4MjotYThZ7HZbHjYJdfFo`</summary>

```json
{
  "query": "pi0.7 open source weights release 2026 parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e38353b0-7ec7-4abd-8cff-ff7b24167131",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVgdpSFPXognzPetzVf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d12d3b32-acd8-4c28-b1f4-ceaefc2d68f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWcgPrdz4Qwnh11G5SeW6Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5909,
      "cache_read_input_tokens": 12282,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 12282,
          "cache_creation_input_tokens": 5909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5909,
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

_source line 31 · 2026-05-18T18:19:14.631Z_

<details><summary>↩ Tool result · `toolu_01MTfXHWE44kUHT1pPbWKaXt`</summary>

```text
Web search results for query: "GR00T N1 NVIDIA open weights parameters download 2025 2026"

Links: [{"title":"GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub","url":"https://github.com/NVIDIA/Isaac-GR00T"},{"title":"Isaac GR00T - Generalist Robot 00 Technology | NVIDIA Developer","url":"https://developer.nvidia.com/isaac/gr00t"},{"title":"NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots | Research","url":"https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots"},{"title":"GR00T N1.5","url":"https://research.nvidia.com/labs/gear/gr00t-n1_5/"},{"title":"Training Data for GR00T N1 | Data Requirements & Formats | Claru","url":"https://claru.ai/models/groot-n1"},{"title":"GitHub - NVIDIA-Medtech/GR00T-H: Gr00t-H · GitHub","url":"https://github.com/NVIDIA-Medtech/GR00T-H"},{"title":"GR00T N1.6","url":"https://research.nvidia.com/labs/gear/gr00t-n1_6/"},{"title":"Accelerate Generalist Humanoid Robot Development with NVIDIA Isaac GR00T N1 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1/"},{"title":"NVIDIA Announces Isaac GR00T N1 — the World’s First Open Humanoid Robot Foundation Model — and Simulation Frameworks to Speed Robot Development | NVIDIA Newsroom","url":"https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734v1"}]

Based on the search results, here's information about GR00T N1 NVIDIA open weights and parameters:

## Model Overview

GR00T N1 is an open foundation model for generalist humanoid robots, developed by NVIDIA and published in March 2025. The models are made open-weight with permissive licenses available via NVIDIA Isaac GR00T.

## Parameters and Architecture

The publicly released GR00T-N1-2B model contains 2.2 billion parameters in total, with 1.34 billion in the VLM backbone (NVIDIA Eagle-2, fine-tuned from SmolLM2 and SigLIP-2).

## Latest Versions and Downloads

GR00T N1.7 Early Access was just released, the latest version of GR00T N1 with a new VLM backbone (Cosmos-Reason2-2B / Qwen3-VL) and improved performance. You are welcome to download the model, explore the codebase, and begin building on the stack, with the understanding that support and stability guarantees are limited until the GA release.

The models are available on the official GitHub repository: **https://github.com/NVIDIA/Isaac-GR00T**

Additionally, [March 2026] — Released GR00T-H with pre-trained checkpoint and the Open-H dataset, which is a healthcare robotics variant of GR00T N1.6.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6be522c1-eaac-4cad-af97-3fa3390efbc0",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "7b2ae7ca-f956-444f-94ac-db15066fa5c1",
  "sourceToolAssistantUUID": "6be522c1-eaac-4cad-af97-3fa3390efbc0",
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

_source line 32 · 2026-05-18T18:19:15.620Z_

<details><summary>↩ Tool result · `toolu_01B4MjotYThZ7HZbHjYJdfFo`</summary>

```text
Web search results for query: "pi0.7 open source weights release 2026 parameters"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"Open Sourcing π0","url":"https://www.pi.website/blog/openpi"},{"title":"Physical Intelligence open-sources Pi0 robotics foundation model","url":"https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"},{"title":"Weights & Biases","url":"https://wandb.ai/wandb-smle/openpi-aloha-wandb-integration/reports/OpenPI-and-W-B-for-Physical-AI-Experiment-tracking-guide--VmlldzoxNjQyMzc4Mg"},{"title":"exla-ai/openpie-0.6 · Hugging Face","url":"https://huggingface.co/exla-ai/openpie-0.6"},{"title":"Peter Welinder on X: \"Pi0 seems like a great open source robotics model to build on.\" / X","url":"https://x.com/npew/status/1886824422163800188"},{"title":"Physical Intelligence (π)","url":"https://www.pi.website/"},{"title":"π0 and π0-FAST: Vision-Language-Action Models for General Robot Control","url":"https://huggingface.co/blog/pi0"},{"title":"OpenPi π₀.₅ on Jetson Thor | Jetson AI Lab","url":"https://www.jetson-ai-lab.com/tutorials/openpi_on_thor/"},{"title":"Rohan Paul on X: \"π0.5 weights + fine-tuning code are now open-source made by Physical-Intelligenc This is the open-sourced π0 from Physical Intelligence, its robotic foundation model, via the openpi repository. π0 is the most advanced Vision Language Action model. It takes natural language https://t.co/2W1YjMubTr\" / X","url":"https://x.com/rohanpaul_ai/status/1965269131827069377"}]

Based on the search results, here's what I found about pi0.7 and related releases:

## π0.7 Release Information

π0.7 is a steerable model with emergent capabilities and is described as a steerable robotic foundation model that exhibits a step-change in generalization. However, the search results indicate this is a recently announced model, and specific details about parameter counts for π0.7 specifically are not provided in the available sources.

## Related Open Source Releases

The search results show information about other open-source releases from Physical Intelligence:

- **π0 and π0-FAST**: Physical Intelligence released the code and weights for π0 as part of their experimental openpi repository, along with their new π0-FAST autoregressive model.

- **π0.5**: π0.5 was released in September 2025 as an upgraded version of π0 with better open-world generalization.

- **OpenPIE-0.6**: A third-party implementation is also available. The first fully open-source PyTorch implementation of Physical Intelligence's pi0.6 robot policy model, trained with RECAP, has a policy model of approximately 5.91B parameters and a value function of 1.31B parameters (7.22B total).

The search results don't contain specific parameter information for π0.7, suggesting it may be too recently announced for detailed specifications to be widely documented yet.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d12d3b32-acd8-4c28-b1f4-ceaefc2d68f8",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "48423951-679a-4aa0-bfc0-6679e87e44d7",
  "sourceToolAssistantUUID": "d12d3b32-acd8-4c28-b1f4-ceaefc2d68f8",
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

_source line 33 · 2026-05-18T18:19:17.312Z_

<details><summary>↩ Tool result · `toolu_016h4kEt6K3wBzptKwu9QEEu`</summary>

```text
Web search results for query: "LingBot-VLA Robbyant parameters architecture open source weights 2026"

Links: [{"title":"Robbyant Open-Sources LingBot-VLA as a \"Universal Brain\" for Robots","url":"https://finance.yahoo.com/news/robbyant-open-sources-lingbot-vla-081800694.html"},{"title":"Robbyant Open-Sources LingBot-VLA as a “Universal Brain” for Robots | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/26071/"},{"title":"Robbyant Open-Sources LingBot-VLA as a \"Universal Brain\" for Robots - Social News XYZ","url":"https://www.socialnews.xyz/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/"},{"title":"Robbyant Open-Sources LingBot-VLA as a “Universal Brain” for Robots","url":"https://www.businesswire.com/news/home/20260127455032/en/Robbyant-Open-Sources-LingBot-VLA-as-a-Universal-Brain-for-Robots"},{"title":"GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/robbyant/lingbot-va"},{"title":"GitHub - Robbyant/lingbot-vla: A Pragmatic VLA Foundation Model · GitHub","url":"https://github.com/Robbyant/lingbot-vla"},{"title":"Robbyant Open-Sources LingBot-VLA as a “Universal Brain” for Robots","url":"https://theaiinsider.tech/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/"},{"title":"Robbyant open-sources LingBot-VLA ‘universal brain’ model for embodied AI robots","url":"https://roboticsandautomationnews.com/2026/03/13/robbyant-open-sources-lingbot-vla-model-as-a-universal-brain-for-robots/99640/"}]

Based on the search results, here's what I found about LingBot-VLA:

## Overview
LingBot-VLA is a vision-language-action (VLA) model designed to serve as a "universal brain" for real-world robotics, which helps reduce post-training costs and accelerate the path to scalable deployment. Ant Group described LingBot-VLA as its first open-source embodied AI model.

## Architecture & Parameters
To train LingBot with their codebase, weights from Qwen2.5-VL-3B-Instruct, MoGe-2-vitb-normal, and LingBot-Depth are required. The search results indicate there are versions including LingBot-VLA-4B and LingBot-VLA-4B-Depth models.

## Open Source Release & Weights
The open-source release includes not only the model weights but also a complete, production-ready codebase, featuring tools for data processing, efficient fine-tuning, and automated evaluation.

## Performance & Training
The model was pre-trained on more than 20,000 hours of real-world interaction data and delivers 1.5x to 2.8x faster training than comparable frameworks. It has been successfully adapted to robots from Galaxea Dynamics and AgileX Robotics, and achieved higher task success rates than other evaluated models across three distinct physical robot platforms.

The announcement was made in January 2026, with technical documentation available on GitHub and a technical report on ArXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e38353b0-7ec7-4abd-8cff-ff7b24167131",
  "isSidechain": true,
  "promptId": "bc281d65-3388-4434-9d17-b49ef3cd6665",
  "agentId": "a67129ccf8a63acd8",
  "type": "user",
  "uuid": "f434b24e-7c30-4ed8-9d03-d46c60e97487",
  "sourceToolAssistantUUID": "e38353b0-7ec7-4abd-8cff-ff7b24167131",
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

_source line 34 · 2026-05-18T18:20:29.361Z_

Here is my comprehensive report on the current state-of-the-art open-source VLA and VLM models relevant to your robotics research project as of May 2026.

---

## Top VLA Models for Affordance-Conditioned Action Generation

### 1. OpenVLA + OpenVLA-OFT (Stanford / UC Berkeley)
- **Parameters:** 7B (based on a Prismatic VLM backbone with Llama 2 7B)
- **Weights:** Publicly available, Apache 2.0 license
- **Benchmarks:** 76.5% on LIBERO (base), **97.1% on LIBERO with OFT recipe**; outperforms RT-2-X (55B) by 16.5 percentage points across 29 tasks
- **Key details:** OpenVLA-OFT adds parallel decoding, action chunking, continuous action representation, and L1 regression loss -- yielding 26x faster action generation and 3x lower latency. The OFT+ variant adds FiLM conditioning for stronger language grounding. Runs bimanual dexterous manipulation at 25 Hz.
- **VLA backbone suitability:** **Excellent.** This is the most established open-source VLA with the largest research ecosystem. The 7B size is large but manageable, and OFT's modular improvements (especially swapping the action head) demonstrate that the architecture is amenable to modification. Strong candidate for adding an affordance-conditioned action head.

### 2. Pi-zero (Physical Intelligence) -- pi0 / pi0-FAST / pi0.5 / pi0.7
- **Parameters:** ~3B VLM backbone (PaliGemma, 2.29B fine-tuned) + 315M action expert parameters (~2.6B total for base pi0). Third-party pi0.6 reimplementation: ~5.91B policy + 1.31B value function.
- **Weights:** Open via the `openpi` GitHub repository. pi0, pi0-FAST, and pi0.5 weights available. pi0.7 announced April 2026 but open-weight availability unclear.
- **Benchmarks:** 28.33% on RoboChallenge; strong real-world results on laundry folding, table clearing, dish loading, box assembly, grocery bagging. pi0.7 claims a "step-change in generalization."
- **Key details:** Uses a **flow-matching (diffusion) action head** rather than discrete token classification, producing smoother trajectories for dexterous manipulation. Outputs motor commands at up to 50 Hz. Pre-trained on 10,000+ hours of robot data. Only 1-20 hours of data needed for fine-tuning to new tasks.
- **VLA backbone suitability:** **Very strong.** The flow-matching action head architecture is particularly relevant if your affordance-conditioned generation needs smooth, continuous action outputs. The modular VLM + action expert design makes it natural to intercept representations and inject affordance conditioning. The smaller base size (~2.6B) is also more compute-friendly than OpenVLA's 7B.

### 3. SmolVLA (Hugging Face)
- **Parameters:** **450M total** (VLM backbone from SmolVLM2 with SigLIP vision encoder + SmolLM2 language decoder; 100M action expert)
- **Weights:** Publicly available via Hugging Face
- **Benchmarks:** 82-90% on LIBERO (within 5% of OpenVLA); matches or outperforms ACT on real-world benchmarks
- **Key details:** Runs at **15-30 Hz on a single RTX 4090**. Uses layer skipping, reduced visual tokens, and interleaved cross/self-attention in the action expert. Trained on fewer than 30,000 episodes. Supports asynchronous inference.
- **VLA backbone suitability:** **Good for resource-constrained settings.** The small size makes rapid iteration easy, but the 450M parameter count may limit the richness of internal representations needed for affordance reasoning. Best if you want fast prototyping or plan to deploy on edge hardware. The modular VLM + action expert split is clean for architectural modifications.

### 4. A1 VLA (April 2026)
- **Parameters:** Not precisely specified in available sources, but described as designed for "low-cost, high-throughput inference"
- **Weights:** Fully open -- training code, data pipeline, intermediate checkpoints, and evaluation scripts all released
- **Benchmarks:** **29.00% on RoboChallenge** (outperforms pi0 at 28.33%, X-VLA at 21.33%, RDT-1B at 15.00%)
- **Key details:** Uses a truncated VLA architecture for efficiency. Full transparency -- the most reproducible option available. April 2026 release makes it the newest model on this list.
- **VLA backbone suitability:** **Strong.** The fully transparent training stack is a major advantage for a research project where you need to deeply modify the architecture. The truncated design suggests it's already optimized for the kind of efficiency/capability tradeoff you'd want when adding affordance conditioning.

### 5. NVIDIA GR00T N1 (now at N1.7)
- **Parameters:** 2.2B total (1.34B VLM backbone from Eagle-2, fine-tuned from SmolLM2 + SigLIP-2)
- **Weights:** Open-weight with permissive license via NVIDIA Isaac GR00T. N1.7 uses Cosmos-Reason2-2B / Qwen3-VL backbone.
- **Benchmarks:** Designed primarily for humanoid robots; strong cross-embodiment results but benchmarks are more humanoid-focused
- **Key details:** Compositional architecture with VLM-based reasoning + Diffusion Transformer action module. Broad embodiment support.
- **VLA backbone suitability:** **Moderate for manipulation.** Primarily designed for humanoid robots, so it may require more adaptation for tabletop/arm manipulation tasks. The diffusion transformer action module is architecturally interesting for affordance conditioning, but the humanoid focus could be a mismatch.

### 6. LingBot-VLA (Robbyant / Ant Group)
- **Parameters:** ~4B (LingBot-VLA-4B); uses Qwen2.5-VL-3B-Instruct as VLM backbone
- **Weights:** Open-source (weights + production codebase + fine-tuning tools + evaluation)
- **Benchmarks:** Higher task success rates than competitors across 3 physical robot platforms (specific numbers not published in available sources)
- **Key details:** Pre-trained on 20,000+ hours of real-world data. 1.5-2.8x faster training than comparable frameworks. Cross-platform (tested on Galaxea Dynamics and AgileX robots).
- **VLA backbone suitability:** **Good.** The Qwen2.5-VL backbone is a strong modern VLM. The production-ready codebase is appealing, but the model is newer with less community research built on top of it compared to OpenVLA or pi0.

### 7. Octo (UC Berkeley)
- **Parameters:** Octo-Small: 27M; Octo-Base: 93M
- **Weights:** Fully open
- **Benchmarks:** Comparable to RT-2-X (55B) in zero-shot; outperforms training-from-scratch by 52% average across 6 setups
- **Key details:** Transformer-based diffusion policy. Very lightweight -- runs on consumer GPUs. Trained on 800K episodes from Open X-Embodiment.
- **VLA backbone suitability:** **Limited as a VLA backbone for affordance conditioning.** The model is too small to serve as a rich representation backbone. However, it is excellent as a baseline or for lightweight deployment. No direct successor identified.

---

## Relevant VLM Backbones (if building a VLA from a VLM)

If you want to build your own VLA by starting from a pure VLM and adding action heads:

| Model | Parameters | Notes |
|---|---|---|
| **Qwen2.5-VL / Qwen3-VL** | 3B, 7B, 32B, 72B | Top-tier open VLM; already used as backbone by LingBot-VLA and GR00T N1.7 |
| **GLM-4.5V** | 106B total / 12B active (MoE) | SOTA on 41 multimodal benchmarks; overkill for most robotics but very capable |
| **SmolVLM2** | ~256M-500M | Already used as SmolVLA backbone; good for lightweight builds |
| **PaliGemma** | 3B | Used as pi0 backbone; proven in robotics context |
| **Molmo** | 1B, 7B, 72B | Strong multimodal performance, comparable to GPT-4V |

---

## Recommendation for Affordance-Conditioned Action Generation

For your specific use case of modifying a VLA backbone for affordance-conditioned action generation, I would rank the options:

1. **pi0 (via openpi)** -- Best architectural fit. The modular VLM + flow-matching action expert design is naturally suited to injecting affordance conditioning between the VLM representations and the action head. The ~2.6B size is manageable, and the diffusion-based action generation produces smooth trajectories. Strong community and Physical Intelligence support.

2. **OpenVLA-OFT** -- Best ecosystem and benchmarks. The 7B model has the most research built on it, the strongest benchmark results (97.1% LIBERO), and the OFT recipe already demonstrates how to swap/modify the action head. Larger compute footprint but more proven.

3. **A1** -- Best for full reproducibility. If your research requires complete transparency in the training pipeline (important for publishability), A1's fully open stack is unmatched. It also holds the current SOTA on RoboChallenge.

4. **SmolVLA** -- Best for rapid prototyping. At 450M parameters, you can iterate on architectural modifications quickly before scaling up.

The practical recommendation: **start prototyping with SmolVLA or pi0 for fast iteration, then scale to OpenVLA-OFT or A1 for final results.**

---

Sources:
- [Top 10 Physical AI Models Powering Real-World Robots in 2026](https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/)
- [VLA Models Compared: OpenVLA vs pi0 vs SmolVLA vs RT-2 (2026 Guide)](https://www.roboticscenter.ai/learn/vla-models-comparison)
- [A1: A Fully Transparent Open-Source VLA Model](https://arxiv.org/pdf/2604.05672)
- [OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models](https://arxiv.org/abs/2502.19645)
- [SmolVLA - Hugging Face Documentation](https://huggingface.co/docs/lerobot/smolvla)
- [Hugging Face Releases SmolVLA](https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/)
- [Physical Intelligence pi0 Blog](https://www.pi.website/blog/pi0)
- [OpenPI GitHub Repository](https://github.com/Physical-Intelligence/openpi)
- [Physical Intelligence pi0 vs OpenVLA](https://www.roboticscenter.ai/physical-intelligence-pi0-vs-openvla)
- [GR00T N1: Open Foundation Model for Humanoid Robots](https://arxiv.org/html/2503.14734v1)
- [NVIDIA Isaac GR00T N1.7 GitHub](https://github.com/NVIDIA/Isaac-GR00T)
- [Robbyant Open-Sources LingBot-VLA](https://www.roboticstomorrow.com/news/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/26071/)
- [LingBot-VLA GitHub](https://github.com/Robbyant/lingbot-vla)
- [Octo: An Open-Source Generalist Robot Policy](https://octo-models.github.io/)
- [OpenVLA GitHub](https://github.com/openvla/openvla)
- [Best Open-Source Vision Language Models in 2026](https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models)
- [Top 10 Vision Language Models in 2026](https://dextralabs.com/blog/top-10-vision-language-models/)
- [pi0 and pi0-FAST on Hugging Face](https://huggingface.co/blog/pi0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f434b24e-7c30-4ed8-9d03-d46c60e97487",
  "isSidechain": true,
  "agentId": "a67129ccf8a63acd8",
  "requestId": "req_011CbAVhbhTq9wVScLxirQ7H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfeaf184-8d06-4ac4-b6cf-fde2c0d45c22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fb106d55-093f-4dcf-9ad8-7293de92a994",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BqWLsMtWxUyJ3mSudWw2F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 2078,
      "cache_read_input_tokens": 18191,
      "output_tokens": 3197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2078
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 907,
          "output_tokens": 3197,
          "cache_read_input_tokens": 18191,
          "cache_creation_input_tokens": 2078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2078,
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
