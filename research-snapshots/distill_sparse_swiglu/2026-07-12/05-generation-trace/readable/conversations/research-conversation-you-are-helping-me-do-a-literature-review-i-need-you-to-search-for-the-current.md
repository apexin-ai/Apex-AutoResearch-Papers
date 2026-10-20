# Research conversation: You are helping me do a literature review. I need you to search for the current state-of-the-art in data curation and fi

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-acab4e3ce805ecb28.jsonl`
- **Structured JSON:** [`1c6dad081defd5e4702d.json`](../../sessions/1c/1c6dad081defd5e4702d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-13T05:41:49.361Z_

You are helping me do a literature review. I need you to search for the current state-of-the-art in data curation and filtering for Vision-Language-Action (VLA) model training in robotics. 

Specifically search for:
1. "VLA data curation 2025 2026" 
2. "demonstration filtering imitation learning robot 2026"
3. "data quality vision language action model"
4. "SCIZOR data curation imitation learning"
5. "adaptive data selection robot learning 2026"

For each search, use WebSearch and report the top results with titles, URLs, and brief descriptions. I need to know what the actual current SOTA methods are for filtering/curating robot demonstration data as of May 2026.

Also search for:
6. "site:arxiv.org VLA training data quality 2026"
7. "demonstration quality scoring robot manipulation 2026"

Report all findings comprehensively.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "f9bdfde1-7038-4ce0-af25-dd830760f03e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T05:41:49.366Z_

```json
{
  "parentUuid": "f9bdfde1-7038-4ce0-af25-dd830760f03e",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
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
  "uuid": "3a7824d8-98b5-444d-b6ba-6349b31655ea",
  "timestamp": "2026-05-13T05:41:49.366Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T05:41:52.039Z_



I'll start by loading the WebSearch tool schema, then run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a7824d8-98b5-444d-b6ba-6349b31655ea",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2trdWrmY1gosnirGzv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "831ee87b-2a3a-494f-9b47-8cbc2209362a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01625Yi2VhjZihWSJbbXAhSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8982,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8982,
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

_source line 4 · 2026-05-13T05:41:52.186Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011FfqbTQuHDzAWonJRKASdR`</summary>

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
  "parentUuid": "831ee87b-2a3a-494f-9b47-8cbc2209362a",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2trdWrmY1gosnirGzv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b7be769-01f8-4f42-a956-61fd7797227c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01625Yi2VhjZihWSJbbXAhSy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8982,
      "cache_read_input_tokens": 0,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8982
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8982,
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

_source line 5 · 2026-05-13T05:41:52.192Z_

<details><summary>↩ Tool result · `toolu_011FfqbTQuHDzAWonJRKASdR`</summary>

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
  "parentUuid": "0b7be769-01f8-4f42-a956-61fd7797227c",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "ca9dff00-ac75-4b26-8fdb-cc22aa98369a",
  "sourceToolAssistantUUID": "0b7be769-01f8-4f42-a956-61fd7797227c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T05:41:54.617Z_



Now let me run all 7 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca9dff00-ac75-4b26-8fdb-cc22aa98369a",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2u53PNeTac5C5cQEpP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d51fc9b-98d9-4043-8c7b-347af26b27cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DthJ6Jy1TcTRvC4WKuNw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 7 · 2026-05-13T05:41:55.083Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Pnbw66TXK9fbmWtaGABmL`</summary>

```json
{
  "query": "VLA data curation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d51fc9b-98d9-4043-8c7b-347af26b27cd",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2u53PNeTac5C5cQEpP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c44ba4f7-1817-44d7-a58b-238b13b1b211",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DthJ6Jy1TcTRvC4WKuNw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 8 · 2026-05-13T05:41:55.575Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012qJknD3bx8VZ6vX6ki4iLy`</summary>

```json
{
  "query": "demonstration filtering imitation learning robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c44ba4f7-1817-44d7-a58b-238b13b1b211",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2u53PNeTac5C5cQEpP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cf149ef-f5b0-4021-ba36-a763e61e883b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DthJ6Jy1TcTRvC4WKuNw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 9 · 2026-05-13T05:41:55.580Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016WD8W8Vjw3DJcNPr6zSj9S`</summary>

```json
{
  "query": "data quality vision language action model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cf149ef-f5b0-4021-ba36-a763e61e883b",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2u53PNeTac5C5cQEpP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "917f8377-fd11-45e0-8492-3effa0960fb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DthJ6Jy1TcTRvC4WKuNw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 10 · 2026-05-13T05:41:56.010Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FTeT18kbKs3o3SGmZ9tkZk`</summary>

```json
{
  "query": "SCIZOR data curation imitation learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "917f8377-fd11-45e0-8492-3effa0960fb8",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2u53PNeTac5C5cQEpP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f18edc63-f5ec-432b-a923-e875c84d0fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DthJ6Jy1TcTRvC4WKuNw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 11 · 2026-05-13T05:41:56.501Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TcrrAGHEMvBn1km2hd9BKn`</summary>

```json
{
  "query": "adaptive data selection robot learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f18edc63-f5ec-432b-a923-e875c84d0fe4",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2u53PNeTac5C5cQEpP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c69b3a9-9828-46e1-8a8e-924b6fa46d96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DthJ6Jy1TcTRvC4WKuNw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 12 · 2026-05-13T05:41:56.981Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ss3QneKxp8CuYRgMSV2yjg`</summary>

```json
{
  "query": "site:arxiv.org VLA training data quality 2026",
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
  "parentUuid": "4c69b3a9-9828-46e1-8a8e-924b6fa46d96",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2u53PNeTac5C5cQEpP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13232092-5bbc-4338-9a2d-cc7b588af496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DthJ6Jy1TcTRvC4WKuNw9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8982,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 359,
          "cache_read_input_tokens": 8982,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1413,
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

_source line 13 · 2026-05-13T05:41:56.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014argwb6oVvLuB5B4SqWX53`</summary>

```json
{
  "query": "demonstration quality scoring robot manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13232092-5bbc-4338-9a2d-cc7b588af496",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2u53PNeTac5C5cQEpP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86862dc5-7493-4626-914d-c4f745d1e54e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DthJ6Jy1TcTRvC4WKuNw9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8982,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 359,
          "cache_read_input_tokens": 8982,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1413,
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

_source line 14 · 2026-05-13T05:42:02.157Z_

<details><summary>↩ Tool result · `toolu_012qJknD3bx8VZ6vX6ki4iLy`</summary>

```text
Web search results for query: "demonstration filtering imitation learning robot 2026"

Links: [{"title":"Beyond the Teacher: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=7Ox8aKIFbA"},{"title":"Frontiers | Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1682437/full"},{"title":"Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12757213/"},{"title":"Frontiers | Imitation learning for legged robot locomotion: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/full"},{"title":"A survey on imitation learning for contact-rich tasks in robotics - Toshiaki Tsuji, Yasuhiro Kato, Gokhan Solak, Heng Zhang, Tadej Petrič, Francesco Nori, Arash Ajoudani, 2026","url":"https://journals.sagepub.com/doi/10.1177/02783649261417694"},{"title":"Visual imitation learning from one-shot demonstration for multi-step robot pick and place tasks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-30938-x"},{"title":"What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=JrsfBJtDFdI"},{"title":"[2602.19184] Human-to-Robot Interaction: Learning from Video Demonstration for Robot Imitation","url":"https://arxiv.org/abs/2602.19184"},{"title":"GitHub - ARISE-Initiative/robomimic: robomimic: A Modular Framework for Robot Learning from Demonstration · GitHub","url":"https://github.com/ARISE-Initiative/robomimic"},{"title":"Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration","url":"https://www.robot-learning.uk/coarse-to-fine-imitation-learning"}]

Based on the search results, here are the key findings related to demonstration filtering and imitation learning for robots in 2026:

## Recent Research on Demonstration Filtering and Imitation Learning

A recent framework enables robot learning from imperfect data by selecting a representative demonstration and using an LSTM network to refine the entire set of demonstrations with a multi-objective loss. This approach has been demonstrated on a Franka Emika robot performing phasic tasks such as wiping and stirring.

In the context of interactive imitation learning, MEGA-DAgger allows for several experts who may also be imperfect, with a built-in filter that resolves contrary corrections and removes unsafe demonstrations.

## Broader Context on Imitation Learning

Contact-rich tasks must be performed without damaging target objects, and data collection in robotic systems is both challenging and costly, with two primary approaches to extracting motion models from demonstration data being reinforcement learning and imitation learning.

Recent advances also include a one-shot visual imitation learning framework that allows robots to acquire multi-step pick & place tasks from a single video demonstration, integrating hand detection, object detection, trajectory segmentation, and skill learning through Dynamic Movement Primitives.

These developments highlight the ongoing importance of filtering and processing demonstration data effectively to enable more robust and practical robot learning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cf149ef-f5b0-4021-ba36-a763e61e883b",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "362effe4-56f7-42e9-9676-d977c6f39316",
  "sourceToolAssistantUUID": "7cf149ef-f5b0-4021-ba36-a763e61e883b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T05:42:02.250Z_

<details><summary>↩ Tool result · `toolu_01Ss3QneKxp8CuYRgMSV2yjg`</summary>

```text
Web search results for query: "site:arxiv.org VLA training data quality 2026"

Links: [{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines","url":"https://arxiv.org/html/2604.23001v1"},{"title":"Learning from Mistakes: Post-Training for Driving VLA with Takeover Data","url":"https://arxiv.org/html/2603.14972v1"},{"title":"[2510.24795] A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.24795"},{"title":"LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://arxiv.org/html/2601.15197"},{"title":"[2604.19728v1] VLA Foundry: A Unified Framework for Training Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.19728v1"},{"title":"VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models","url":"https://arxiv.org/html/2604.03956v2"},{"title":"10 Open Challenges Steering the Future of Vision-Language-Action Models","url":"https://arxiv.org/html/2511.05936v1"},{"title":"A tutorial note on collecting simulated data for vision-language-action models","url":"https://arxiv.org/html/2508.06547v1"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"}]

The search results show several recent arxiv papers about Vision-Language-Action (VLA) models from 2025-2026. The search query included "site:arxiv.org" but did not find papers specifically about "VLA training data quality" in the traditional sense - instead the results focus on Vision-Language-Action models in robotics.

Here are the key findings from the 2026 arxiv papers on VLA training data quality:

The development of vision language action (VLA) models in robotics relies heavily on high-quality datasets, with dataset collection and annotation playing a critical role in driving advancements in the field.

The success of VLA models critically depends on the quality and diversity of their training data—a challenge that distinguishes VLA research from traditional computer vision or natural language processing domains.

Mixed Data Co-training is a potent strategy for boosting VLA model efficiency and generalization by jointly training on heterogeneous datasets across varying quality and modality.

Effective VLA dataset construction requires careful consideration of three key dimensions: data quality, scale, and diversity.

If you're looking for information about a different type of VLA (such as Variable-Length Arrays or another acronym), please clarify and I can perform a more targeted search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13232092-5bbc-4338-9a2d-cc7b588af496",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "acab3783-9b24-45f6-8eb0-4d0c1ece5809",
  "sourceToolAssistantUUID": "13232092-5bbc-4338-9a2d-cc7b588af496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T05:42:02.934Z_

<details><summary>↩ Tool result · `toolu_012Pnbw66TXK9fbmWtaGABmL`</summary>

```text
Web search results for query: "VLA data curation 2025 2026"

Links: [{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"MolmoAct 2: An open foundation for robots that work in the real world | Ai2","url":"https://allenai.org/blog/molmoact2"},{"title":"Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future","url":"https://arxiv.org/html/2512.16760v2"}]

I found search results related to Vision-Language-Action (VLA) data curation in 2025-2026, though it appears the results focus on robotics VLA systems rather than the Very Large Array (astronomical VLA). Here are the key findings:

## VLA Data Curation Initiatives (Robotics Focus)

The AI Robotic Association (AIRoA) announced a workshop titled "From Data to Decisions: VLA Pipelines for Real Robots" at ICRA 2026, which will be held in Vienna, Austria, from June 1–5, 2026.

This workshop aims to examine the entire end-to-end VLA pipeline, from scalable data collection and systematic curation to training strategies and inference-time reasoning.

The workshop competition involves multimodal data including RGB-D video, joint states, force/torque signals, language annotations, and action trajectories, which will be organized in the LeRobot format and released via storage services such as Wasabi.

AI2 created the MolmoAct 2-Bimanual YAM dataset, a 700-hour collection of robot demonstrations with over 30x the robot data used for the original MolmoAct, making it the largest open-source bimanual robotics dataset ever released.

If you were looking for information about Very Large Array (astronomical) data curation instead, please let me know and I can search for that specific topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c44ba4f7-1817-44d7-a58b-238b13b1b211",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "8d1fab76-7363-493c-9fe0-04ba8bcbaa1a",
  "sourceToolAssistantUUID": "c44ba4f7-1817-44d7-a58b-238b13b1b211",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T05:42:03.075Z_

<details><summary>↩ Tool result · `toolu_01FTeT18kbKs3o3SGmZ9tkZk`</summary>

```text
Web search results for query: "SCIZOR data curation imitation learning"

Links: [{"title":"[2505.22626] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/abs/2505.22626"},{"title":"SCIZOR: Self-Supervised Data Curation for Large-Scale Imitation Learning","url":"https://ut-austin-rpl.github.io/SCIZOR/"},{"title":"Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/html/2505.22626v2"},{"title":"GitHub - UT-Austin-RPL/SCIZOR · GitHub","url":"https://github.com/UT-Austin-RPL/SCIZOR"},{"title":"SCIZOR: A Self-Supervised Approach to Data Curation for ...","url":"https://openreview.net/pdf?id=Wo8eEdFUDF"},{"title":"(PDF) SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.researchgate.net/publication/392167457_SCIZOR_A_Self-Supervised_Approach_to_Data_Curation_for_Large-Scale_Imitation_Learning"},{"title":"Copyright by Yuqi Xie 2025 1","url":"https://repositories.lib.utexas.edu/bitstreams/d8256e22-405e-4881-87d8-ca3f8008345e/download"},{"title":"[Literature Review] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.themoonlight.io/en/review/scizor-a-self-supervised-approach-to-data-curation-for-large-scale-imitation-learning"},{"title":"Huihan Liu on X: \"Our data curation work SCIZOR is accepted to ICRA 2026! Check out this self-supervised data curation approach that removes suboptimal and duplicated data for large-scale imitation learning, led by @YZ_Franklin @yuqi_xie5\" / X","url":"https://x.com/huihan_liu/status/2017698931493195899"},{"title":"[PDF] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SCIZOR:-A-Self-Supervised-Approach-to-Data-Curation-Zhang-Xie/1a601961be1a3facbacc68205b9279216e802c5c"}]

Based on the search results, here's what I found about SCIZOR:

## Overview

SCIZOR is a self-supervised data curation framework that filters out low-quality state-action pairs to improve the performance of imitation learning policies.

## Problem It Addresses

Large-scale datasets used for policy training often introduce substantial variability in quality, which can negatively impact performance, making it essential to automatically curate datasets by filtering low-quality samples. Existing robotic curation approaches rely on costly manual annotations and perform curation at a coarse granularity, such as the dataset or trajectory level, failing to account for the quality of individual state-action pairs.

## Key Components

SCIZOR targets two complementary sources of low-quality data: suboptimal data, which hinders learning with undesirable actions, and redundant data, which dilutes training with repetitive patterns. It leverages a self-supervised task progress predictor for suboptimal data to remove samples lacking task progression, and a deduplication module operating on joint state-action representation for samples with redundant patterns.

## Results

SCIZOR enables imitation learning policies to achieve higher performance with less data, yielding an average improvement of 15.4% across multiple benchmarks. Compared to training on the full dataset, SCIZOR delivers absolute gains of 5.4% on RoboMimic, 8.1% on OXE-Magic-Soup, and 32.9% on the Sirius-Fleet real-robot tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f18edc63-f5ec-432b-a923-e875c84d0fe4",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "c8c2d96f-2e58-4882-92b5-8b4f37cf8044",
  "sourceToolAssistantUUID": "f18edc63-f5ec-432b-a923-e875c84d0fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T05:42:03.372Z_

<details><summary>↩ Tool result · `toolu_016WD8W8Vjw3DJcNPr6zSj9S`</summary>

```text
Web search results for query: "data quality vision language action model"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Helix: A Vision-Language-Action Model for Generalist Humanoid Control","url":"https://www.figure.ai/news/helix"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Vision-Language-Action (VLA) Models for Robotics","url":"https://blog.roboflow.com/vision-language-action-models/"},{"title":"[2512.03913] Hierarchical Vision Language Action Model Using Success and Failure Demonstrations","url":"https://arxiv.org/abs/2512.03913"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Hierarchical Vision Language Action Model Using Success and Failure Demonstrations","url":"https://arxiv.org/html/2512.03913"}]

Based on the search results, here's what I found about data quality in vision language action models:

## Key Findings on Data Quality in VLAs

VLA models are only as good as the visual data they are trained on. The architecture can be elegant, the backbone pretrained on billions of images, and the action decoder carefully tuned, and the model will still fail in deployment if the training data did not represent the environments it will actually operate in.

### Data Collection Challenges

Collecting robot demonstration data is slow and expensive, and the quality of the annotations applied to that data determines whether the model learns something generalizable or something brittle.

VLA models rely on high-quality labeled datasets. The development of vision language action models in robotics relies heavily on high-quality datasets and realistic simulators capable of capturing the complexity of real-world scenarios.

### Data Quality Issues

Some datasets are collected in real-world settings, which requires substantial human effort and financial resources. Despite these efforts, data collection remains costly, annotations are labor-intensive, and long-tail corner cases are often underrepresented.

### Mixed-Quality Data Approaches

Recent research has also focused on leveraging both successful and failed demonstrations. Prior Vision-Language-Action models are typically trained on teleoperated successful demonstrations, while discarding numerous failed attempts that occur naturally during data collection. However, these failures encode where and how policies can be fragile, information that can be exploited to improve robustness. Addressing this involves leveraging mixed-quality datasets to learn failure-aware reasoning at planning time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "917f8377-fd11-45e0-8492-3effa0960fb8",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "5918350a-2117-458a-9202-6c132c6a2395",
  "sourceToolAssistantUUID": "917f8377-fd11-45e0-8492-3effa0960fb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T05:42:03.801Z_

<details><summary>↩ Tool result · `toolu_01TcrrAGHEMvBn1km2hd9BKn`</summary>

```text
Web search results for query: "adaptive data selection robot learning 2026"

Links: [{"title":"Frontiers | Editorial: Reinforcement learning for real-world robot navigation","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1861947/full"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"PADP: progressive and adaptive data pruning for efficient incremental learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-43959-x"},{"title":"Enhancing Human-Robot Collaborative Transportation of ...","url":"https://sites.gc.sjtu.edu.cn/youyibi/wp-content/uploads/sites/3/2025/09/AEI-2026.pdf"},{"title":"4 physical AI predictions for 2026 - and beyond, from UR - The Robot Report","url":"https://www.therobotreport.com/four-physical-ai-predictions-2026-beyond-universal-robots/"},{"title":"Frontiers | Editorial: AI for design and control of advanced robots","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1850311/full"},{"title":"AdaDS: Adaptive data selection for accelerating pre-trained language model knowledge distillation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666651023000074"},{"title":"Frontiers | Adaptive mapless mobile robot navigation using deep reinforcement learning based improved TD3 algorithm","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1625968/full"},{"title":"AI Adaptive Systems 2026: Smarter Self-Learning Intelligence","url":"https://www.aitechboss.com/ai-adaptive-systems-2026/"},{"title":"Frontiers | A survey of decision-making and planning methods for self-driving vehicles","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2025.1451923/full"}]

Based on the search results, here are key findings related to adaptive data selection in robot learning in 2026:

## Recent Research on Adaptive Data Selection for Robot Learning

An adaptive command sampling mechanism balances training across skills of varying difficulty and prevents catastrophic forgetting. This approach is part of the Seamless Multi-Skill Learning (SMSL) framework, which shows effectiveness through sim-to-real validation on Solo8 robots.

### Data Pruning and Incremental Learning

PADP (Progressive and Adaptive Data Pruning) dynamically evaluates sample difficulty and its difficulty changes during training to enable adaptive sample selection for each incremental learning task. The method proposes two metrics: the instant difficulty score (which evaluates the learning difficulty of a sample) and the difficulty variation score (which evaluates the variation in difficulty over a training interval), combined to guide pruning decisions.

### Broader Adaptive Systems Context

In the context of broader AI adaptive systems in 2026, AI Adaptive Systems are artificial intelligence frameworks capable of modifying their behavior based on new data and outcomes, and unlike traditional AI models that require manual retraining, adaptive systems learn incrementally.

### Robot Learning Applications

Reinforcement learning has emerged as a powerful paradigm for robot challenges, with RL providing unique advantages for dynamic and adaptive navigation by benefiting from trial-and-error interactions with the environments.

The search results indicate that 2026 research is focusing on making robot learning systems more efficient through intelligent data selection strategies that adapt to changing training conditions and task requirements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c69b3a9-9828-46e1-8a8e-924b6fa46d96",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "19730f54-7b8c-4726-be1f-03fcb1606a31",
  "sourceToolAssistantUUID": "4c69b3a9-9828-46e1-8a8e-924b6fa46d96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T05:42:04.506Z_

<details><summary>↩ Tool result · `toolu_014argwb6oVvLuB5B4SqWX53`</summary>

```text
Web search results for query: "demonstration quality scoring robot manipulation 2026"

Links: [{"title":"RoCo Challenge at AAAI 2026: Benchmarking Robotic Collaborative Manipulation for Assembly Towards Industrial Automation","url":"https://arxiv.org/html/2603.15469"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"Competitions - IEEE ICRA 2026","url":"https://2026.ieee-icra.org/program/competitions/"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/152/"},{"title":"[2603.15469] RoCo Challenge at AAAI 2026: Benchmarking Robotic Collaborative Manipulation for Assembly Towards Industrial Automation","url":"https://arxiv.org/abs/2603.15469"},{"title":"REGULAR PAPER 1 Trustworthy Evaluation of Robotic Manipulation: A New Benchmark","url":"https://arxiv.org/pdf/2601.18723"},{"title":"Trustworthy Evaluation of Robotic Manipulation: A New Benchmark and AutoEval Methods","url":"https://arxiv.org/html/2601.18723"},{"title":"RoCo Challenge at AAAI 2026: Benchmarking Robotic Collaborative Manipulation for Assembly Towards Industrial Automation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260315469L/abstract"},{"title":"Abstracting Robot Manipulation Skills via Mixture-of- ...","url":"https://arxiv.org/pdf/2601.21251"}]

I found several relevant results related to demonstration quality scoring and robot manipulation in 2026. Here are the key findings:

## Demonstration Quality Scoring in Robot Manipulation (2026)

There is significant interest in dataset curation tools, episode quality scoring, and demonstration filtering in the robotics field as of 2026.

### Key Developments:

**Quality Metrics Framework:**
Reproducibility failures have driven interest in standardized dataset quality scores, with the Open-X Embodiment quality rubric, extended by SVRC and several academic partners, becoming the most widely cited framework, covering trajectory smoothness, demonstration diversity, and labeling confidence.

**Benchmark Systems:**
Recent work has developed comprehensive evaluation systems. Domain experts provide numerical quality scores with detailed Chain-of-Thought reasoning, and datasets like Eval-Actions explicitly incorporate failure cases alongside Fine-Grained Action Quality scores.

**Data Curation Approaches:**
Quality over Quantity (QoQ) is a systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations, leveraging influence functions to quantify the impact of individual training samples on model performance.

**Real-World Challenge Results:**
In real-world robot challenges, participants were provided with a high-quality teleoperated dataset consisting of more than 300 demonstrations collected on the target hardware platform.

These developments reflect a major shift in robotics research toward treating data quality and curation as critical factors for successful robot manipulation systems in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86862dc5-7493-4626-914d-c4f745d1e54e",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "93ab00e9-a2d7-463d-a8eb-cbc32977b20a",
  "sourceToolAssistantUUID": "86862dc5-7493-4626-914d-c4f745d1e54e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T05:42:07.443Z_

Let me run a few more targeted searches to fill in gaps on specific methods mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93ab00e9-a2d7-463d-a8eb-cbc32977b20a",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2uyQaqK16tN7JgckeA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26abc91f-7c49-4b78-9052-b9338cca6d01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUa6otRvMuBa5astiFqqKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6630,
      "cache_read_input_tokens": 10395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6630,
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

_source line 22 · 2026-05-13T05:42:07.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016pWKSGrXSTJsNmo7StF2Hc`</summary>

```json
{
  "query": "Quality over Quantity influence functions demonstration curation robot learning arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26abc91f-7c49-4b78-9052-b9338cca6d01",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2uyQaqK16tN7JgckeA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fa08bc6-c4ff-4bef-98e3-840bb3899af5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUa6otRvMuBa5astiFqqKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6630,
      "cache_read_input_tokens": 10395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6630,
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

_source line 23 · 2026-05-13T05:42:08.984Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XiCNYag89PphQKjhifZ8Y8`</summary>

```json
{
  "query": "\"What Matters in Learning from Offline Human Demonstrations\" robot manipulation data filtering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fa08bc6-c4ff-4bef-98e3-840bb3899af5",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2uyQaqK16tN7JgckeA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "970cb697-883c-45de-bab3-04279d02acfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUa6otRvMuBa5astiFqqKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6630,
      "cache_read_input_tokens": 10395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6630,
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

_source line 24 · 2026-05-13T05:42:09.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JZYPmqfgpwpQBGcWdYZSM3`</summary>

```json
{
  "query": "VLA Foundry unified framework training vision language action data curation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "970cb697-883c-45de-bab3-04279d02acfa",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2uyQaqK16tN7JgckeA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91a9bed9-20c9-4229-a844-fe32ca4ea549",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUa6otRvMuBa5astiFqqKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6630,
      "cache_read_input_tokens": 10395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6630,
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

_source line 25 · 2026-05-13T05:42:10.411Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MQQufqpjuYjtxDNUXcAASD`</summary>

```json
{
  "query": "\"Beyond the Teacher\" mixed-skill demonstrations robust imitation learning filtering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91a9bed9-20c9-4229-a844-fe32ca4ea549",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2uyQaqK16tN7JgckeA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "889d53e8-c082-47f2-aaf6-6d2aa97d2bd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUa6otRvMuBa5astiFqqKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6630,
      "cache_read_input_tokens": 10395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6630,
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

_source line 26 · 2026-05-13T05:42:11.380Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RDsMhiE7Nuafv4nBBM4GJT`</summary>

```json
{
  "query": "arxiv \"Vision-Language-Action\" datasets benchmarks data engines survey 2026",
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
  "parentUuid": "889d53e8-c082-47f2-aaf6-6d2aa97d2bd0",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2uyQaqK16tN7JgckeA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98ac67ad-b3f1-4e0e-9c51-b233bc6a5466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUa6otRvMuBa5astiFqqKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6630,
      "cache_read_input_tokens": 10395,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6630
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 311,
          "cache_read_input_tokens": 10395,
          "cache_creation_input_tokens": 6630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6630,
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

_source line 27 · 2026-05-13T05:42:13.336Z_

<details><summary>↩ Tool result · `toolu_01MQQufqpjuYjtxDNUXcAASD`</summary>

```text
Web search results for query: ""Beyond the Teacher" mixed-skill demonstrations robust imitation learning filtering"

Links: [{"title":"Beyond the Teacher: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=7Ox8aKIFbA"},{"title":"GitHub - FocasLab/ICRA-IL-2026: Beyond the Expert: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning · GitHub","url":"https://github.com/FocasLab/ICRA-IL-2026"}]

Based on the search results, I found information about this research:

The work presents a novel learning framework that enables robots to perform complex periodic tasks with expert-like proficiency, even when learning from naive demonstrations.

The two-stage pipeline first selects a representative demonstration based on user-defined task intention scores. This single best demo is then used to extract a canonical motion shape via Periodic Dynamic Movement Primitives (DMPs). Finally, a Long Short-Term Memory (LSTM) network refines the entire set of demonstrations, leveraging a multi-objective loss that combines the canonical shape with other task quality metrics.

The proposed approach is demonstrated on a Franka Emika robot performing phasic tasks such as wiping and stirring.

The work addresses imitation learning from naive demonstrations through demonstration filtering to enable expert-like learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "889d53e8-c082-47f2-aaf6-6d2aa97d2bd0",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "84dfac27-8c92-430c-8012-4b9c650fe43e",
  "sourceToolAssistantUUID": "889d53e8-c082-47f2-aaf6-6d2aa97d2bd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T05:42:14.093Z_

<details><summary>↩ Tool result · `toolu_016pWKSGrXSTJsNmo7StF2Hc`</summary>

```text
Web search results for query: "Quality over Quantity influence functions demonstration curation robot learning arxiv 2025"

Links: [{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121"},{"title":"[2502.08211] Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation","url":"https://arxiv.org/abs/2502.08211"},{"title":"[2506.19121] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121"},{"title":"[2503.09205] Quality Over Quantity? LLM-Based Curation for a Data-Efficient Audio-Video Foundation Model","url":"https://arxiv.org/abs/2503.09205"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation","url":"https://arxiv.org/html/2502.08211"},{"title":"Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250208211X/abstract"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://arxiv.org/html/2506.13536v1"}]

Based on the search results, I found the paper you're looking for:

## Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning

The paper proposes Quality over Quantity (QoQ), a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations.

The research addresses learning from demonstrations for end-to-end robot control, with a focus on overcoming the critical bottleneck of demonstration data quality, which is often collected through human teleoperation. Human errors, operational constraints, and teleoperator variability introduce noise and suboptimal behaviors, making data curation essential yet largely manual and heuristic-driven.

The paper is available on arXiv as paper **2603.09056** and was published on March 10, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fa08bc6-c4ff-4bef-98e3-840bb3899af5",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "2c3bec5b-7155-4dfd-951e-1eed0faa280e",
  "sourceToolAssistantUUID": "4fa08bc6-c4ff-4bef-98e3-840bb3899af5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T05:42:16.589Z_

<details><summary>↩ Tool result · `toolu_01JZYPmqfgpwpQBGcWdYZSM3`</summary>

```text
Web search results for query: "VLA Foundry unified framework training vision language action data curation 2026"

Links: [{"title":"[2604.19728] VLA Foundry: A Unified Framework for Training Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.19728"},{"title":"[2604.19728v1] VLA Foundry: A Unified Framework for Training Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.19728v1"},{"title":"VLA Foundry - Vision-Language-Action Model Training Framework","url":"https://tri-ml.github.io/vla_foundry/"},{"title":"VLA Foundry: A Unified Framework for Training Vision-Language-Action Models","url":"https://arxiv.org/html/2604.19728.pdf"},{"title":"VLA Foundry: A Unified Framework for Training Vision-Language-Action Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2604.19728"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"},{"title":"GitHub - baaivision/UniVLA: [ICLR 2026] Unified Vision-Language-Action Model · GitHub","url":"https://github.com/baaivision/UniVLA"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"}]

Based on the search results, here's what I found about VLA Foundry:

## VLA Foundry Overview

VLA Foundry is an open-source framework that unifies LLM, VLM, and VLA training in a single codebase. Most open-source VLA efforts specialize on the action training stage, often stitching together incompatible pretraining pipelines.

## Key Features

VLA Foundry provides a shared training stack with end-to-end control, from language pretraining to action-expert fine-tuning. The framework is built on FSDP2 with WebDataset streaming, and multi-GPU training works locally with torchrun and on large clusters with AWS SageMaker.

## Data and Training Capabilities

You can train with text, image-captions, or robotics data, going from LLM to VLM to VLA using the same framework. VLA Foundry supports both from-scratch training and pretrained backbones from Hugging Face, with two types of models: the first trained fully from scratch through an LLM→VLM→VLA pipeline and the second built on the pretrained Qwen3-VL backbone.

## Evaluation and Release

The framework evaluates closed-loop policy performance on LBM Eval, an open-data, open-source simulator. The VLA Foundry codebase is available online and all multi-task model weights are released on Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91a9bed9-20c9-4229-a844-fe32ca4ea549",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "04e3f5f3-e039-459f-94d7-312abfe68391",
  "sourceToolAssistantUUID": "91a9bed9-20c9-4229-a844-fe32ca4ea549",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T05:42:18.538Z_

<details><summary>↩ Tool result · `toolu_01RDsMhiE7Nuafv4nBBM4GJT`</summary>

```text
Web search results for query: "arxiv "Vision-Language-Action" datasets benchmarks data engines survey 2026"

Links: [{"title":"[2604.23001] Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines","url":"https://arxiv.org/abs/2604.23001"},{"title":"Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines","url":"https://arxiv.org/html/2604.23001v1"},{"title":"[2510.24795] A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.24795"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[2405.14093] A Survey on Vision-Language-Action Models for Embodied AI","url":"https://arxiv.org/abs/2405.14093"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"[2506.24044] A Survey on Vision-Language-Action Models for Autonomous Driving","url":"https://arxiv.org/abs/2506.24044"},{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/html/2507.01925v1"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"[2512.16760] Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future","url":"https://arxiv.org/abs/2512.16760"}]

Your search found several highly relevant papers on Vision-Language-Action (VLA) models. Here are the key results:

## Primary Match

The most directly relevant paper is "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines" (arXiv 2604.23001), published on April 24, 2026. This survey argues that future advances in VLA will depend less on model architecture and more on the co-design of high-fidelity data engines and structured evaluation protocols.

## Related Surveys

Additional comprehensive surveys on VLAs include:

1. A Survey on Efficient Vision-Language-Action Models (arXiv 2510.24795), which presents the first comprehensive review of Efficient VLAs across the entire model-training-data pipeline

2. Pure Vision Language Action (VLA) Models: A Comprehensive Survey, which analyzes VLA applications across different scenarios and introduces foundational datasets, benchmarks, and simulation platforms

3. A Survey on Vision-Language-Action Models for Embodied AI (arXiv 2405.14093), addressing language-conditioned robotic tasks and presenting the first survey on VLAs for embodied AI

4. Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey, providing the first systematic review of large VLM-based VLA models, covering architectural paradigms, advanced integration techniques, and datasets/benchmarks

These papers comprehensively cover VLA datasets, benchmarks, and data engine methodologies as of 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98ac67ad-b3f1-4e0e-9c51-b233bc6a5466",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "aa3f211b-6a0f-4228-b2e1-1fe90aad5f68",
  "sourceToolAssistantUUID": "98ac67ad-b3f1-4e0e-9c51-b233bc6a5466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T05:42:20.029Z_

<details><summary>↩ Tool result · `toolu_01XiCNYag89PphQKjhifZ8Y8`</summary>

```text
Web search results for query: ""What Matters in Learning from Offline Human Demonstrations" robot manipulation data filtering"

Links: [{"title":"What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | robomimic","url":"https://robomimic.github.io/study/"},{"title":"What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | SAIL Blog","url":"https://ai.stanford.edu/blog/robomimic/"},{"title":"What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=JrsfBJtDFdI"},{"title":"[2108.03298] What Matters in Learning from Offline Human Demonstrations for Robot Manipulation","url":"https://arxiv.org/abs/2108.03298"},{"title":"[PDF] What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/What-Matters-in-Learning-from-Offline-Human-for-Mandlekar-Xu/3032844d6ac6882ccb03e7a2c22a0026b210ac05"},{"title":"[2108.03298v1] What Matters in Learning from Offline Human Demonstrations for Robot Manipulation","url":"https://arxiv.org/abs/2108.03298v1"},{"title":"What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | Request PDF","url":"https://www.researchgate.net/publication/353791375_What_Matters_in_Learning_from_Offline_Human_Demonstrations_for_Robot_Manipulation"},{"title":"What Matters in Learning from Offline Human Demonstrations ...","url":"https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf"},{"title":"What Matters in Learning from Offline Human Demonstrations for Robot Manipulation","url":"https://vitalab.github.io/article/2022/06/16/What_Matters_Robot_Manipulation.html"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://arxiv.org/html/2506.13536v1"}]

Based on the search results, I found detailed information about "What Matters in Learning from Offline Human Demonstrations for Robot Manipulation," a comprehensive research paper on robot manipulation and data filtering.

## Overview

The study conducts an extensive analysis of six offline learning algorithms for robot manipulation on five simulated and three real-world multi-stage manipulation tasks of varying complexity, and with datasets of varying quality.

## Key Challenges Identified

The research identifies several critical challenges when learning from offline human demonstration data:

1. **Non-Markovian Human Behavior**: Humans are non-markovian agents who act on more factors than just the information they have in front of them at each time, such as their memory and prior experience.

2. **Varying Trajectory Quality**: Different humans have different control skills for the task at hand.

3. **Dataset Size and Coverage**: Learning agents need sufficient coverage in the dataset to handle all the situations they might encounter.

4. **Objective Discrepancies**: Agents are trained to replicate behavior in the dataset, but this is a different objective from the underlying objective of being successful at the task.

## Key Findings

The study derives lessons including the sensitivity to different algorithmic design choices, the dependence on the quality of demonstrations, and the variability based on stopping criteria due to different objectives in training and evaluation.

The researchers have open-sourced their datasets and all algorithm implementations to facilitate future research and fair comparisons in learning from human demonstration data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "970cb697-883c-45de-bab3-04279d02acfa",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "43116c20-59bd-4453-99a4-0a09f279ffb6",
  "sourceToolAssistantUUID": "970cb697-883c-45de-bab3-04279d02acfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-13T05:42:22.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016WeNd6QPVvyqZ1DkwrMjsG`</summary>

```json
{
  "query": "CUPID curating data robot influence functions demonstration filtering 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43116c20-59bd-4453-99a4-0a09f279ffb6",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2w7jficWgVHygS22A8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cc9ab29-84c3-4ddf-b7f3-6dae92a60f98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DeEDpuMBqtMTC2riRgyTm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2084,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 17025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 33 · 2026-05-13T05:42:23.149Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D9bbur5Mps8E5dUaJxLiZV`</summary>

```json
{
  "query": "\"hierarchical vision language action\" success failure demonstrations data curation arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cc9ab29-84c3-4ddf-b7f3-6dae92a60f98",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2w7jficWgVHygS22A8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df80b0b9-8911-4336-bf2d-2dd725636276",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DeEDpuMBqtMTC2riRgyTm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2084,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 17025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 34 · 2026-05-13T05:42:23.715Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C7YGTPnr8gwqD8PzFPscmG`</summary>

```json
{
  "query": "\"What Matters in Learning from Large-Scale Datasets\" robot manipulation 2025 2026 data curation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df80b0b9-8911-4336-bf2d-2dd725636276",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2w7jficWgVHygS22A8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b79912fa-5a70-4612-8bbf-0c5311abc38b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DeEDpuMBqtMTC2riRgyTm7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2084,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 17025,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1939
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2084,
          "output_tokens": 173,
          "cache_read_input_tokens": 17025,
          "cache_creation_input_tokens": 1939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1939,
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

_source line 35 · 2026-05-13T05:42:29.171Z_

<details><summary>↩ Tool result · `toolu_016WeNd6QPVvyqZ1DkwrMjsG`</summary>

```text
Web search results for query: "CUPID curating data robot influence functions demonstration filtering 2025"

Links: [{"title":"[2506.19121] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121"},{"title":"GitHub - agiachris/cupid: Official repository for \"CUPID: Curating Data your Robot Loves with Influence Functions,\" accepted to CoRL 2025. · GitHub","url":"https://github.com/agiachris/cupid"},{"title":"[2506.19121v2] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121v2"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://proceedings.mlr.press/v305/agia25a.html"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions | OpenReview","url":"https://openreview.net/forum?id=TqevdDMqrK"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"CUPID: Robot Data Curation via Influence Functions","url":"https://www.emergentmind.com/papers/2506.19121"},{"title":"[PDF] CUPID: Curating Data your Robot Loves with Influence Functions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CUPID:-Curating-Data-your-Robot-Loves-with-Agia-Sinha/666481cd9e72de8e90e3dd12fb826338f5ce17f0"},{"title":"[Literature Review] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://www.themoonlight.io/en/review/cupid-curating-data-your-robot-loves-with-influence-functions"}]

I found comprehensive information about CUPID. Here's a summary of the search results:

## CUPID: Curating Data your Robot Loves with Influence Functions

CUPID (CUrating Performance-Influencing Demonstrations) is a data curation method for robot imitation learning that uses influence functions to estimate the causal impact of each demonstration on a policy's closed-loop performance.

### Key Features

CUPID is a robot data curation method based on a novel influence function-theoretic formulation for imitation learning policies. Given a set of evaluation rollouts, CUPID estimates the influence of each training demonstration on the policy's expected return.

CUPID provides a principled way to filter existing training sets and subselect helpful demos from new data.

### Applications

CUPID curates data by 1) filtering out training demonstrations that harm policy performance and 2) subselecting newly collected trajectories that will most improve the policy.

### Demonstrated Results

Training with less than 33% of curated data can yield state-of-the-art diffusion policies on the simulated RoboMimic benchmark, with similar gains observed in hardware. Additionally, hardware experiments show that the method can identify robust strategies under distribution shift, isolate spurious correlations, and even enhance the post-training of generalist robot policies.

### Publication Status

CUPID was accepted to CoRL 2025 and appears in Proceedings of The 9th Conference on Robot Learning, PMLR 305:2907-2932, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cc9ab29-84c3-4ddf-b7f3-6dae92a60f98",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "4fc21061-be88-4f36-806b-f57ef7adbbbb",
  "sourceToolAssistantUUID": "7cc9ab29-84c3-4ddf-b7f3-6dae92a60f98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T05:42:30.552Z_

<details><summary>↩ Tool result · `toolu_01D9bbur5Mps8E5dUaJxLiZV`</summary>

```text
Web search results for query: ""hierarchical vision language action" success failure demonstrations data curation arxiv"

Links: [{"title":"[2512.03913] Hierarchical Vision Language Action Model Using Success and Failure Demonstrations","url":"https://arxiv.org/abs/2512.03913"},{"title":"Hierarchical Vision Language Action Model Using Success and Failure Demonstrations","url":"https://arxiv.org/html/2512.03913v1"},{"title":"(PDF) Hierarchical Vision Language Action Model Using Success and Failure Demonstrations","url":"https://www.researchgate.net/publication/398313119_Hierarchical_Vision_Language_Action_Model_Using_Success_and_Failure_Demonstrations"},{"title":"A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://arxiv.org/html/2509.15937v1"},{"title":"AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation","url":"https://arxiv.org/html/2410.00371v1"},{"title":"Clutter-Robust Vision–Language–Action Models through Object-Centric and Geometry Grounding","url":"https://arxiv.org/html/2512.22519"},{"title":"Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines","url":"https://arxiv.org/html/2604.23001"},{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/html/2507.01925v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[Literature Review] Hierarchical Vision Language Action Model Using Success and Failure Demonstrations","url":"https://www.themoonlight.io/en/review/hierarchical-vision-language-action-model-using-success-and-failure-demonstrations"}]

I found several relevant research papers on arXiv related to hierarchical vision-language-action models that incorporate success and failure demonstrations for data curation. Here are the key findings:

## Primary Result: VINE Paper

The most directly relevant paper is **"Hierarchical Vision Language Action Model Using Success and Failure Demonstrations"** by Jeongeun Park and colleagues (arXiv:2512.03913).

### Key Contributions

Prior Vision-Language-Action (VLA) models are typically trained on teleoperated successful demonstrations, while discarding numerous failed attempts that occur naturally during data collection. However, these failures encode where and how policies can be fragile, information that can be exploited to improve robustness.

VINE is a hierarchical vision-language-action model that separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical reinforcement learning formalism, making failures usable as a structured learning signal rather than noisy supervision.

### System Architecture

System 2 performs feasibility-guided tree search over a 2D scene-graph abstraction: it proposes subgoal transitions, predicts success probabilities from both successes and failures, and prunes brittle branches before execution.

## Related Work

Other relevant papers on similar topics include:
- AHA, which systematically generates failure trajectories yielding a curated dataset of 49k failure-question pairs
- Papers addressing failure detection and reasoning in vision-language models for robotic manipulation

These papers emphasize the importance of data curation that incorporates both successful and failed demonstrations for building more robust robotic systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df80b0b9-8911-4336-bf2d-2dd725636276",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "16c45fcd-e7d2-4c54-9e8e-e0763b4d40e6",
  "sourceToolAssistantUUID": "df80b0b9-8911-4336-bf2d-2dd725636276",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-13T05:42:30.874Z_

<details><summary>↩ Tool result · `toolu_01C7YGTPnr8gwqD8PzFPscmG`</summary>

```text
Web search results for query: ""What Matters in Learning from Large-Scale Datasets" robot manipulation 2025 2026 data curation"

Links: [{"title":"[2506.13536] What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://arxiv.org/abs/2506.13536"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=LqhorpRLIm"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://arxiv.org/html/2506.13536v1"},{"title":"What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | robomimic","url":"https://robomimic.github.io/study/"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250613536S/abstract"},{"title":"(PDF) What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://www.researchgate.net/publication/392736873_What_Matters_in_Learning_from_Large-Scale_Datasets_for_Robot_Manipulation"},{"title":"What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | SAIL Blog","url":"https://ai.stanford.edu/blog/robomimic/"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://robo-mimiclabs.github.io/"},{"title":"[PDF] What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/What-Matters-in-Learning-from-Offline-Human-for-Mandlekar-Xu/3032844d6ac6882ccb03e7a2c22a0026b210ac05"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation | NVIDIA Seattle Robotics Lab","url":"https://research.nvidia.com/labs/srl/publication/saxena-2025-what/"}]

Based on the search results, I found relevant information about the research paper you're looking for:

## "What Matters in Learning from Large-Scale Datasets for Robot Manipulation"

This paper, by Vaibhav Saxena and 7 other authors, focuses on imitation learning from large multi-task demonstration datasets as a promising path for building generally-capable robots. Despite continuous growth in large-scale dataset efforts, there has been a lack of systematic understanding of what data should be collected to improve the utility of a robotics dataset and facilitate downstream policy learning.

### Research Approach

The researchers developed a data generation framework to procedurally emulate common sources of diversity in existing datasets (such as sensor placements and object types and arrangements), and use it to generate large-scale robot datasets with controlled compositions.

### Key Findings

The study found that camera poses and spatial arrangements are crucial dimensions for both diversity in collection and alignment in retrieval. 

In real-world robot learning settings, their retrieval strategies on existing datasets such as DROID allow them to consistently outperform existing training strategies by up to 70%.

### Practical Applications

The work focuses on two practical settings: (1) what types of diversity should be emphasized when future researchers collect large-scale datasets for robotics, and (2) how current practitioners should retrieve relevant demonstrations from existing datasets to maximize downstream policy performance on tasks of interest.

The paper was published in 2025 and represents recent work in robot learning and data curation strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b79912fa-5a70-4612-8bbf-0c5311abc38b",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "acab4e3ce805ecb28",
  "type": "user",
  "uuid": "766a549b-c9eb-41f1-87f1-75ab02282ccb",
  "sourceToolAssistantUUID": "b79912fa-5a70-4612-8bbf-0c5311abc38b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-13T05:43:23.933Z_

Here is a comprehensive report of findings across all seven search queries.

---

## Literature Review: Data Curation and Filtering for VLA Model Training in Robotics (as of May 2026)

### 1. SCIZOR -- The Leading Self-Supervised Data Curation Method

**SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning** (UT Austin RPL, accepted at ICRA 2026)

This is arguably the most prominent recent work directly targeting VLA/imitation learning data curation. SCIZOR addresses two complementary sources of low-quality data:

- **Suboptimal data**: Uses a self-supervised task progress predictor to remove state-action pairs that lack meaningful task progression.
- **Redundant data**: Applies a deduplication module operating on joint state-action representations to remove repetitive patterns.

Key results: Average improvement of 15.4% across benchmarks -- +5.4% on RoboMimic, +8.1% on OXE-Magic-Soup, and +32.9% on Sirius-Fleet real-robot tasks. Crucially, SCIZOR operates at the **state-action pair level** (fine-grained), not just trajectory-level, which is a key differentiator from prior work.

- Paper: [arXiv:2505.22626](https://arxiv.org/abs/2505.22626)
- Project page: [https://ut-austin-rpl.github.io/SCIZOR/](https://ut-austin-rpl.github.io/SCIZOR/)
- Code: [https://github.com/UT-Austin-RPL/SCIZOR](https://github.com/UT-Austin-RPL/SCIZOR)

---

### 2. CUPID -- Influence Function-Based Curation (CoRL 2025)

**CUPID: Curating Data your Robot Loves with Influence Functions**

Uses influence functions to estimate the causal impact of each demonstration on a policy's closed-loop performance. Two capabilities:
1. **Filtering**: Removes training demonstrations that harm policy performance.
2. **Subselection**: Identifies which newly collected trajectories will most improve the policy.

Key results: Training with less than 33% of curated data yields SOTA diffusion policies on RoboMimic. Hardware experiments show the method can identify robust strategies under distribution shift and isolate spurious correlations.

- Paper: [arXiv:2506.19121](https://arxiv.org/abs/2506.19121)
- Project page: [https://cupid-curation.github.io/](https://cupid-curation.github.io/)
- Published in: CoRL 2025, PMLR 305:2907-2932

---

### 3. Quality over Quantity (QoQ) -- Demonstration Curation via Influence Functions (March 2026)

**Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning**

Defines data quality as the contribution of each training sample to reducing loss on validation demonstrations, using influence functions. Addresses noise and suboptimal behaviors introduced by human teleoperation variability.

- Paper: [arXiv:2603.09056](https://arxiv.org/abs/2603.09056) (March 10, 2026)
- Extended HTML: [https://arxiv.org/html/2603.09056](https://arxiv.org/html/2603.09056)

---

### 4. VINE -- Hierarchical VLA Using Success AND Failure Demonstrations

**Hierarchical Vision Language Action Model Using Success and Failure Demonstrations** (December 2025)

Key insight: Prior VLAs discard failed demonstrations, but failures encode where and how policies can be fragile. VINE separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical RL formalism, making failures usable as a structured learning signal. System 2 performs feasibility-guided tree search, predicting success probabilities from both successes and failures and pruning brittle branches.

- Paper: [arXiv:2512.03913](https://arxiv.org/abs/2512.03913)

---

### 5. What Matters in Learning from Large-Scale Datasets for Robot Manipulation (NVIDIA, 2025)

Systematic study of what data diversity dimensions matter most. Developed a procedural data generation framework to emulate common sources of diversity (sensor placements, object types, spatial arrangements). Key finding: **camera poses and spatial arrangements are crucial dimensions** for both diversity in collection and alignment in retrieval. Their retrieval strategies on the DROID dataset outperform existing training strategies by up to 70%.

- Paper: [arXiv:2506.13536](https://arxiv.org/abs/2506.13536)
- NVIDIA project page: [https://research.nvidia.com/labs/srl/publication/saxena-2025-what/](https://research.nvidia.com/labs/srl/publication/saxena-2025-what/)

---

### 6. VLA Foundry -- Unified VLA Training Framework (April 2026)

**VLA Foundry: A Unified Framework for Training Vision-Language-Action Models** (Toyota Research Institute)

Open-source framework unifying LLM, VLM, and VLA training in a single codebase. Supports mixed-modality data (text, image-captions, robotics) and end-to-end training pipelines from LLM to VLM to VLA. Built on FSDP2 with WebDataset streaming.

- Paper: [arXiv:2604.19728](https://arxiv.org/abs/2604.19728)
- Project page: [https://tri-ml.github.io/vla_foundry/](https://tri-ml.github.io/vla_foundry/)

---

### 7. Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines (April 2026)

The most comprehensive and recent survey, arguing that **future VLA advances will depend less on model architecture and more on the co-design of high-fidelity data engines and structured evaluation protocols**. Covers dataset construction along three key dimensions: data quality, scale, and diversity. Discusses mixed data co-training as a strategy for boosting efficiency.

- Paper: [arXiv:2604.23001](https://arxiv.org/abs/2604.23001)

---

### 8. Additional Relevant Work

**Beyond the Teacher: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning** (ICRA 2026)
- Two-stage pipeline: selects a representative demonstration via user-defined task intention scores, extracts canonical motion shape via Periodic DMPs, then uses LSTM to refine the full demo set.
- [OpenReview](https://openreview.net/forum?id=7Ox8aKIFbA) | [GitHub](https://github.com/FocasLab/ICRA-IL-2026)

**ICRA 2026 Workshop: "From Data to Decisions: VLA Pipelines for Real Robots"**
- Dedicated workshop on the full VLA pipeline from data collection/curation to training and inference.
- Competition with 10,000 hours of real-world robot data in LeRobot format.
- [Workshop site](https://icra2026vlapipeline.github.io/) | [AIRoA announcement](https://www.airoa.org/updates/2026-02-10)

**MolmoAct 2 (AI2)**
- Released the YAM dataset: 700+ hours of bimanual robot demonstrations, the largest open-source bimanual robotics dataset.
- [Blog post](https://allenai.org/blog/molmoact2)

**SmolVLA (Hugging Face)**
- Efficient VLA model trained on LeRobot community data, demonstrating the viability of community-curated datasets.
- [Blog post](https://huggingface.co/blog/smolvla)

**State of VLA Research at ICLR 2026** -- A blog summary of VLA trends at ICLR 2026.
- [Blog post](https://mbreuss.github.io/blog_post_iclr_26_vla.html)

**A Survey on Efficient Vision-Language-Action Models** (arXiv:2510.24795)
- First comprehensive review of Efficient VLAs across the model-training-data pipeline.
- [Paper](https://arxiv.org/abs/2510.24795)

---

### Summary of SOTA Methods for Filtering/Curating Robot Demonstration Data (May 2026)

| Method | Approach | Granularity | Key Venue |
|--------|----------|-------------|-----------|
| **SCIZOR** | Self-supervised progress prediction + deduplication | State-action pair | ICRA 2026 |
| **CUPID** | Influence functions on closed-loop returns | Trajectory | CoRL 2025 |
| **QoQ** | Influence functions on validation loss | Sample | arXiv Mar 2026 |
| **VINE** | Hierarchical VLA with failure-aware tree search | Trajectory (success+failure) | arXiv Dec 2025 |
| **Beyond the Teacher** | Representative selection + LSTM refinement | Trajectory | ICRA 2026 |

The clear trend is a shift from manual/heuristic curation toward **automated, principled data quality estimation** -- with influence functions and self-supervised quality predictors as the two dominant paradigms. The field consensus, articulated most clearly in the April 2026 survey (arXiv:2604.23001), is that **data engine co-design will matter more than architecture** for the next generation of VLA models.

Sources:
- [SCIZOR (arXiv:2505.22626)](https://arxiv.org/abs/2505.22626)
- [SCIZOR Project Page](https://ut-austin-rpl.github.io/SCIZOR/)
- [CUPID (arXiv:2506.19121)](https://arxiv.org/abs/2506.19121)
- [CUPID Project Page](https://cupid-curation.github.io/)
- [Quality over Quantity (arXiv:2603.09056)](https://arxiv.org/abs/2603.09056)
- [VINE: Hierarchical VLA (arXiv:2512.03913)](https://arxiv.org/abs/2512.03913)
- [What Matters in Large-Scale Datasets (arXiv:2506.13536)](https://arxiv.org/abs/2506.13536)
- [VLA Foundry (arXiv:2604.19728)](https://arxiv.org/abs/2604.19728)
- [VLA Survey: Datasets, Benchmarks, Data Engines (arXiv:2604.23001)](https://arxiv.org/abs/2604.23001)
- [Beyond the Teacher (OpenReview)](https://openreview.net/forum?id=7Ox8aKIFbA)
- [ICRA 2026 VLA Pipelines Workshop](https://icra2026vlapipeline.github.io/)
- [AIRoA ICRA 2026 Announcement](https://www.airoa.org/updates/2026-02-10)
- [MolmoAct 2 (AI2)](https://allenai.org/blog/molmoact2)
- [SmolVLA (Hugging Face)](https://huggingface.co/blog/smolvla)
- [State of VLA at ICLR 2026](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
- [Efficient VLA Survey (arXiv:2510.24795)](https://arxiv.org/abs/2510.24795)
- [OpenVLA](https://openvla.github.io/)
- [State of Robotics 2026 Report](https://www.roboticscenter.ai/state-of-robotics-2026)
- [VLA Wikipedia](https://en.wikipedia.org/wiki/Vision-language-action_model)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "766a549b-c9eb-41f1-87f1-75ab02282ccb",
  "isSidechain": true,
  "agentId": "acab4e3ce805ecb28",
  "requestId": "req_011Caz2wv6hzSRguktX3iHE1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b33e227-692c-4ad2-9d6b-8a35a9025544",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HkcvADGq7KpyQP7eWn85t",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4982,
      "cache_read_input_tokens": 18964,
      "output_tokens": 2972,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4982
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2972,
          "cache_read_input_tokens": 18964,
          "cache_creation_input_tokens": 4982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4982,
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
