# Research conversation: I'm researching the current state of demonstration curation methods for robot learning. Search for and read: 1. SCIZOR (

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6aedbc70f4ed94ec.jsonl`
- **Structured JSON:** [`1b92a945681fc721f037.json`](../../sessions/1b/1b92a945681fc721f037.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

66 recorded events

### User

_source line 1 · 2026-05-13T10:03:41.514Z_

I'm researching the current state of demonstration curation methods for robot learning. Search for and read:

1. SCIZOR (ICRA 2026) - "A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning". What are their specific results on Sirius-Fleet? How does their method work in detail? What are their baselines?

2. DemInf (RSS 2025) - "Robot Data Curation with Mutual Information Estimators". What exactly are their results on RoboMimic? What are their failure modes?

3. Search for any new demonstration curation papers from 2026 (Jan-May 2026) that I might have missed. Search "demonstration curation 2026", "data quality robot learning 2026", "imitation learning data selection 2026".

4. Search for "importance weighted behavioral cloning" or "weighted imitation learning" - I want to understand if using quality scores as sample weights (soft filtering) has been explored.

Use WebSearch and WebFetch. Report detailed findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "d41deb50-bbfa-4aa5-ba05-e604a303100a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T10:03:41.517Z_

```json
{
  "parentUuid": "d41deb50-bbfa-4aa5-ba05-e604a303100a",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
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
  "uuid": "518283ed-fc10-4e44-9be2-a8781e938b85",
  "timestamp": "2026-05-13T10:03:41.517Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T10:03:43.871Z_



I'll start by loading the WebSearch and WebFetch tools, then conduct the research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "518283ed-fc10-4e44-9be2-a8781e938b85",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNs4vxtW9QvWqYPZtaU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53107fde-4e0d-4343-9211-58327ff56def",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165duH1faVaWYfWCq9iBp7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 784,
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

_source line 4 · 2026-05-13T10:03:44.480Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WmStA7ryfUKPKWz83ii2ND`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53107fde-4e0d-4343-9211-58327ff56def",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNs4vxtW9QvWqYPZtaU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29a2898c-5bfd-435e-be2c-9ceabfef1163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165duH1faVaWYfWCq9iBp7W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 8223,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 784,
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

_source line 5 · 2026-05-13T10:03:44.507Z_

<details><summary>↩ Tool result · `toolu_01WmStA7ryfUKPKWz83ii2ND`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29a2898c-5bfd-435e-be2c-9ceabfef1163",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "43c0f7fa-9aa2-47ac-ac76-484fcaf78699",
  "sourceToolAssistantUUID": "29a2898c-5bfd-435e-be2c-9ceabfef1163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T10:03:46.749Z_



Now let me launch all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43c0f7fa-9aa2-47ac-ac76-484fcaf78699",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNsHt5VNvHPrmCJCjKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77a27642-902e-4d12-87de-a466587e9a34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiwstdZsXNaucTnn53SZNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 7 · 2026-05-13T10:03:47.662Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LB5aJwDXq57uFzRcZDcrbc`</summary>

```json
{
  "query": "SCIZOR ICRA 2026 \"Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77a27642-902e-4d12-87de-a466587e9a34",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNsHt5VNvHPrmCJCjKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0072508c-f460-4040-ae59-66ae35c20032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiwstdZsXNaucTnn53SZNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 8 · 2026-05-13T10:03:47.798Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Js87mJMTKcQ35xYyB1kG9U`</summary>

```json
{
  "query": "DemInf RSS 2025 \"Robot Data Curation with Mutual Information Estimators\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0072508c-f460-4040-ae59-66ae35c20032",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNsHt5VNvHPrmCJCjKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a0406c6-d5c2-4fbb-b201-6e7051ed5fd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiwstdZsXNaucTnn53SZNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 9 · 2026-05-13T10:03:48.169Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LGAvVQRNdzjoUCsi5kdADv`</summary>

```json
{
  "query": "demonstration curation robot learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a0406c6-d5c2-4fbb-b201-6e7051ed5fd6",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNsHt5VNvHPrmCJCjKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "785598a2-d367-4f39-814b-22e1718465a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiwstdZsXNaucTnn53SZNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 10 · 2026-05-13T10:03:48.616Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HwVJncU61vjbN9buWL9keh`</summary>

```json
{
  "query": "data quality robot learning imitation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "785598a2-d367-4f39-814b-22e1718465a3",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNsHt5VNvHPrmCJCjKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd01e4f1-6786-41de-8dba-cc46c778adbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiwstdZsXNaucTnn53SZNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 11 · 2026-05-13T10:03:49.164Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J4NfHXZEvAnuHXN6gLz6PH`</summary>

```json
{
  "query": "imitation learning data selection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd01e4f1-6786-41de-8dba-cc46c778adbb",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNsHt5VNvHPrmCJCjKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a77d3beb-3521-444d-aa61-8a92cc1b8985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiwstdZsXNaucTnn53SZNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 12 · 2026-05-13T10:03:49.173Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014hBBTHaWhbpdMFZq2V4GVg`</summary>

```json
{
  "query": "\"importance weighted behavioral cloning\" robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a77d3beb-3521-444d-aa61-8a92cc1b8985",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNsHt5VNvHPrmCJCjKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ceeaefcb-6f5e-4603-910a-06afd6ac48c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiwstdZsXNaucTnn53SZNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 13 · 2026-05-13T10:03:49.642Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Axts3Vvz1nKYnKxydf5J1Q`</summary>

```json
{
  "query": "\"weighted imitation learning\" sample weights quality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceeaefcb-6f5e-4603-910a-06afd6ac48c1",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNsHt5VNvHPrmCJCjKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59206698-008b-4c16-af95-86df387a070f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiwstdZsXNaucTnn53SZNf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9007,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 364,
          "cache_read_input_tokens": 9007,
          "cache_creation_input_tokens": 1909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1909,
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

_source line 14 · 2026-05-13T10:03:55.707Z_

<details><summary>↩ Tool result · `toolu_01Js87mJMTKcQ35xYyB1kG9U`</summary>

```text
Web search results for query: "DemInf RSS 2025 "Robot Data Curation with Mutual Information Estimators""

Links: [{"title":"Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/html/2502.08623v2"},{"title":"Robot Data Curation with Mutual Information Estimators | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.08623v3"},{"title":"[2502.08623] Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/abs/2502.08623"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"[PDF] Robot Data Curation with Mutual Information Estimators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Robot-Data-Curation-with-Mutual-Information-Hejna-Mirchandani/37cb83dc757f483cfd389c8709b4aee389da8dc6"},{"title":"Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/html/2505.22626v1"},{"title":"GitHub - jhejna/demonstration-information: Code for the paper Robot Data Curation with Mutual Information Estimators","url":"https://github.com/jhejna/demonstration-information"},{"title":"Robot Data Curation with Mutual Information Estimators · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/23/"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"DataMIL : Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/html/2505.09603"}]

I found the paper and information about DemInf. Here's what the search results show:

## "Robot Data Curation with Mutual Information Estimators"

DemInf is an unsupervised, offline method developed by researchers from Google DeepMind Robotics and Stanford University that estimates mutual information between states and actions to curate robot demonstration datasets.

**Key Methodology:**
DemInf proposes the Demonstration Information Estimation method for computationally estimating mutual information. The method estimates the average contribution of a trajectory towards the mutual information between states and actions in the entire dataset, which captures both the entropy of the marginal action distribution and the state-conditioned action entropy.

**Performance Results:**
On RoboMimic tasks, DemInf-filtered data results in 5-10% improvements in success rates compared to training on all available data, and real-world experiments on ALOHA and Franka systems confirm these improvements translate to physical robot performance.

**Paper Details:**
The paper is authored by Joey Hejna, Suvir Mirchandani, Ashwin Balakrishna, Annie Xie, Ayzaan Wahid, Jonathan Tompson, Pannag Sanketi, Dhruv Shah, Coline Devin, and Dorsa Sadigh. The paper was accepted to the Robotics: Science and Systems (RSS) conference.

The paper is available on arXiv (2502.08623) and has open-source code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a0406c6-d5c2-4fbb-b201-6e7051ed5fd6",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "a20e0423-b2fb-483a-8c13-cbd39a195863",
  "sourceToolAssistantUUID": "4a0406c6-d5c2-4fbb-b201-6e7051ed5fd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T10:03:55.885Z_

<details><summary>↩ Tool result · `toolu_01LGAvVQRNdzjoUCsi5kdADv`</summary>

```text
Web search results for query: "demonstration curation robot learning 2026"

Links: [{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"Towards Demonstration-Efficient Robot Learning - King's College London","url":"https://kclpure.kcl.ac.uk/portal/en/studentTheses/towards-demonstration-efficient-robot-learning/"},{"title":"Robot Data Curation with Mutual Information Estimators · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/23/"},{"title":"Learning a thousand tasks in a day | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.adv7594"},{"title":"Curating Demonstrations using Online Experience","url":"https://arxiv.org/html/2503.03707"},{"title":"Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions","url":"https://arxiv.org/html/2604.15395v1"},{"title":"State of Robot Learning, Q1 2026: What Shipped, What Stalled | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/state-of-robot-learning-q1-2026"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"}]

Based on the search results, I found several relevant recent publications and developments in demonstration curation for robot learning in 2026:

## Key Research in Demonstration Curation for Robot Learning

**Quality over Quantity (QoQ) Approach**

A recent paper submitted in March 2026 addresses how learning from demonstrations has emerged as a promising paradigm for end-to-end robot control, while the quality of demonstration data remains a critical bottleneck for effective data-driven robot learning. The QoQ method selects trajectories based on their direct contribution to policy performance using influence functions, measuring similarity between gradients of validation and training data—where higher similarity indicates that including a particular state-action pair will effectively reduce validation loss.

Experiments demonstrate that QoQ effectively identifies high-quality robotic trajectories, resulting in significantly improved policy success rates compared to baseline curation algorithms across both simulation and real-world robot experiments.

**Self-Curation Approach**

Another approach proposes for robots to self-curate based on online robot experience through Demo-SCORE. Demo-SCORE can effectively identify suboptimal demonstrations without manual curation, achieving over 15-35% higher absolute success rate compared to policies trained with all original demonstrations.

**Industry Perspective**

According to Q1 2026 industry analysis, a lab with an open stack and 2,000 well-curated demos is considered competitive. Additionally, upcoming workshop efforts at ICRA 2026 emphasize best practices for data curation, preprocessing, and annotation as key components of vision-language-action (VLA) pipelines for robotics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "785598a2-d367-4f39-814b-22e1718465a3",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "b6b8bb08-e177-4e3a-9a89-18479a392c3e",
  "sourceToolAssistantUUID": "785598a2-d367-4f39-814b-22e1718465a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T10:03:56.404Z_

<details><summary>↩ Tool result · `toolu_014hBBTHaWhbpdMFZq2V4GVg`</summary>

```text
Web search results for query: ""importance weighted behavioral cloning" robot"

Links: [{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=advantage-weighted+behavioral+cloning"},{"title":"Reward-Aligned Behavior Cloning","url":"https://www.emergentmind.com/topics/reward-aligned-behavior-cloning-ra-bc"},{"title":"BEHAVIORAL CLONING FROM NOISY DEMONSTRA","url":"https://openreview.net/pdf?id=zrT3HcsWSAt"},{"title":"Density-Ratio Weighted Behavioral Cloning:","url":"https://arxiv.org/pdf/2510.01479"},{"title":"Why Behaviour Cloning?","url":"http://www.imgeorgiev.com/2025-01-31-why-bc-not-rl/"},{"title":"Constrained Behavior Cloning for Robotic Learning","url":"https://arxiv.org/html/2408.10568v1"},{"title":"Density-Ratio Weighted Behavioral Cloning: Learning Control Policies from Corrupted Datasets","url":"https://arxiv.org/html/2510.01479"},{"title":"10 Imitation Learning","url":"https://web.stanford.edu/class/cs237b/pdfs/lecture/lecture_10111213.pdf"},{"title":"Towards balanced behavior cloning from imbalanced datasets | Autonomous Robots | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10514-025-10237-0"},{"title":"Fine-tuning Behavioral Cloning Policies with Preference-Based Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=vWqkLA0uzm"}]

I found relevant search results about importance-weighted behavioral cloning and related weighted approaches in robotics. Here's what the search revealed:

## Overview

A small modification to supervised fine-tuning (SFT) leads to an importance weighted variant that behaves closer to training with reinforcement learning, referred to as importance weighted supervised fine-tuning (iw-SFT).

## Key Applications

**Robustness to Contaminated Data:** A weighted behavioral cloning framework for robust policy imitation from contaminated offline datasets uses a small, vetted reference set of clean trajectories to train a binary discriminator, comparing the reference set against the potentially corrupted training set, then using its confidence scores to weight the BC objective.

**Handling Imbalanced Demonstrations:** Recent work suggests that common, repetitive behaviors in large datasets dominate the learning process, indicating that the relative proportion of data points representing distinct behaviors is an important aspect of training data.

## Performance Benefits

Weighted BC maintains near-optimal performance even at high contamination ratios, outperforming baselines such as traditional BC, batch-constrained Q-learning (BCQ) and behavior regularized actor-critic (BRAC).

## Related Approaches

Advantage-weighted behavioral cloning is used in implicit Q-learning (IQL), which extracts policies through this method, and IQL demonstrates state-of-the-art performance on D4RL, a standard benchmark for offline reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceeaefcb-6f5e-4603-910a-06afd6ac48c1",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "ea4f66d1-5ab7-4cdf-8eed-bd8f98fa822d",
  "sourceToolAssistantUUID": "ceeaefcb-6f5e-4603-910a-06afd6ac48c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T10:03:56.470Z_

<details><summary>↩ Tool result · `toolu_01HwVJncU61vjbN9buWL9keh`</summary>

```text
Web search results for query: "data quality robot learning imitation 2026"

Links: [{"title":"AGIBOT WORLD 2026 dataset is open-source to accelerate embodied AI development - The Robot Report","url":"https://www.therobotreport.com/agibot-world-2026-dataset-open-source-accelerate-embodied-ai-development/"},{"title":"AGIBOT Open-AGIBOT Innovation (Shanghai) Technology Co., Ltd.","url":"https://www.agibot.com/article/231/detail/54.html"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"Universal Robots and Scale AI launch imitation learning system to accelerate AI model training, bridging the 'lab-to-factory' gap","url":"https://www.universal-robots.com/news-and-media/news-center/universal-robots-scale-ai-launch-imitation-learning-system-accelerate-ai-training-lab-to-factory/"},{"title":"Best Robot Learning Datasets 2026 | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/best-2026"},{"title":"Data Quality in Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=FwmvbuDiMk"},{"title":"[2306.02437] Data Quality in Imitation Learning","url":"https://arxiv.org/abs/2306.02437"},{"title":"NVIDIA GTC 2026: Universal Robots, Scale AI launch imitation learning system to accelerate AI model training - Robotics 24/7","url":"https://www.robotics247.com/article/nvidia-gtc-2026-universal-robots-scale-ailaunch-imitation-learning-system-to-accelerate-ai-model-training"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels | OpenReview","url":"https://openreview.net/forum?id=AcTsKglDdh"},{"title":"Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions","url":"https://arxiv.org/html/2604.15395v1"}]

Based on the search results, here's what I found about data quality, robot learning, and imitation learning in 2026:

## Key Developments in 2026

**AGIBOT WORLD 2026 Dataset**: AGIBOT released an open-source heterogeneous dataset designed to systematically support five key research pathways in embodied intelligence, featuring structured, high-quality, and precisely annotated real-world robot data. The first release focuses on imitation learning, a key paradigm that enables robots to acquire complex physical skills from expert demonstrations, including hundreds of hours of real-world data collected primarily in commercial and service environments.

**Data Quality as Critical Infrastructure**: Data infrastructure is the defining story of 2026, with the underlying economics of robot training data shifting more than any other segment of the stack. The Open-X Embodiment quality rubric has become the most widely cited framework, covering trajectory smoothness, demonstration diversity, and labeling confidence.

**UR AI Trainer**: Universal Robots and Scale AI's AI Trainer represents a tectonic shift as robots move from pre-programmed applications to fully AI-driven tasks, powered by robust data generated in AI training cells where robots imitate humans.

**Data Curation Research**: Researchers have developed DataMIL, a data selection framework that learns to estimate each data-point's effect on imitation learning performance via Datamodels to select high-quality samples that maximize downstream policy success.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd01e4f1-6786-41de-8dba-cc46c778adbb",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "ae44093b-9ae6-45c1-922e-701a63f34ebf",
  "sourceToolAssistantUUID": "bd01e4f1-6786-41de-8dba-cc46c778adbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T10:03:56.609Z_

<details><summary>↩ Tool result · `toolu_01J4NfHXZEvAnuHXN6gLz6PH`</summary>

```text
Web search results for query: "imitation learning data selection 2026"

Links: [{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://robin-lab.cs.utexas.edu/datamodels4imitation/"},{"title":"Imitation Learning from Imperfection: Theoretical Justifications and Algorithms | OpenReview","url":"https://openreview.net/forum?id=vO04AzsB49"},{"title":"GitHub - FocasLab/ICRA-IL-2026: Beyond the Expert: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning · GitHub","url":"https://github.com/FocasLab/ICRA-IL-2026"},{"title":"ICLR 2026: 12 papers on making AI systems reliable, efficient, and secure","url":"https://lambda.ai/blog/iclr-2026-12-papers"},{"title":"ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=fIj88Tn3fc"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with ...","url":"https://arxiv.org/pdf/2505.09603"},{"title":"Rethinking imitation learning with Predictive Inverse Dynamics Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/blog/rethinking-imitation-learning-with-predictive-inverse-dynamics-models/"},{"title":"[2505.09603] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/abs/2505.09603"},{"title":"Data Quality in Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=FwmvbuDiMk&noteId=yRiDkOIoZK"},{"title":"Universal Robots and Scale AI Launch Imitation Learning System for Physical AI Model Training","url":"https://theaiinsider.tech/2026/03/17/universal-robots-and-scale-ai-launch-imitation-learning-system-for-ai-model-training/"}]

Here are the key findings on imitation learning data selection research in 2026:

## Recent Methods and Approaches

DataMIL is a novel data selection method that leverages datamodels to select high-quality task-aware datasets for imitation learning, estimating how each training sample influences policy performance on a given task and selecting samples that lead to maximum improvement. DataMIL demonstrates effectiveness on 60+ simulation and real world tasks, showing significant improvements in performance compared to existing data selection methods, even for novel embodiments not present in the prior data.

ReMix investigates how to weigh different subsets or "domains" of robotics datasets during pre-training to maximize worst-case performance across all possible downstream domains using distributionally robust optimization (DRO). Domain weights learned by ReMix outperform uniform weights by over 40% on average and human-selected weights by over 20% on datasets used to train the RT-X models.

## Data Quality Framework

Fundamental properties necessary for high quality datasets include action divergence—the mismatch between the expert and learned policy at certain states—and transition diversity, the noise present in the system for a given state and action.

## Industry Applications

Universal Robots introduced the UR AI Trainer at GTC 2026, an imitation learning system that records multimodal data including physical interaction forces to create structured datasets used to train vision-language-action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a77d3beb-3521-444d-aa61-8a92cc1b8985",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "39b88754-7931-4c88-8680-4d258c72eaf6",
  "sourceToolAssistantUUID": "a77d3beb-3521-444d-aa61-8a92cc1b8985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T10:03:56.763Z_

<details><summary>↩ Tool result · `toolu_01LB5aJwDXq57uFzRcZDcrbc`</summary>

```text
Web search results for query: "SCIZOR ICRA 2026 "Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning""

Links: [{"title":"[2505.22626] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/abs/2505.22626"},{"title":"SCIZOR: Self-Supervised Data Curation for Large-Scale Imitation Learning","url":"https://ut-austin-rpl.github.io/SCIZOR/"},{"title":"Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/html/2505.22626v2"},{"title":"Huihan Liu on X: \"Our data curation work SCIZOR is accepted to ICRA 2026! Check out this self-supervised data curation approach that removes suboptimal and duplicated data for large-scale imitation learning, led by @YZ_Franklin @yuqi_xie5\" / X","url":"https://x.com/huihan_liu/status/2017698931493195899"},{"title":"SCIZOR: A Self-Supervised Approach to Data Curation for ...","url":"https://openreview.net/pdf?id=Wo8eEdFUDF"},{"title":"(PDF) SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.researchgate.net/publication/392167457_SCIZOR_A_Self-Supervised_Approach_to_Data_Curation_for_Large-Scale_Imitation_Learning"},{"title":"Copyright by Yuqi Xie 2025 1","url":"https://repositories.lib.utexas.edu/bitstreams/d8256e22-405e-4881-87d8-ca3f8008345e/download"},{"title":"GitHub - UT-Austin-RPL/SCIZOR · GitHub","url":"https://github.com/UT-Austin-RPL/SCIZOR"},{"title":"[Literature Review] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.themoonlight.io/en/review/scizor-a-self-supervised-approach-to-data-curation-for-large-scale-imitation-learning"},{"title":"Huihan Liu","url":"https://huihanl.github.io/"}]

I found comprehensive information about SCIZOR and its acceptance at ICRA 2026. Here's a summary of the search results:

## SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning

SCIZOR is a self-supervised data curation framework that filters out low-quality state-action pairs to improve the performance of imitation learning policies.

### Key Problem and Approach

Large-scale datasets used for policy training often introduce substantial variability in quality, which can negatively impact performance. Automatically curating datasets by filtering low-quality samples becomes essential. Existing robotic curation approaches rely on costly manual annotations and perform curation at a coarse granularity, such as the dataset or trajectory level, failing to account for the quality of individual state-action pairs.

### Core Components

SCIZOR targets two complementary sources of low-quality data: suboptimal data, which hinder learning with undesirable actions, and redundant data, which dilute training with repetitive patterns.

The framework has two main components:

1. **Suboptimal Data Removal**: A progress-prediction model flags and removes frames that fail to make meaningful task progress, without needing reward signals.

2. **Redundancy Detection**: Joint visual-action embeddings are clustered to detect and discard look-alike segments, ensuring diversity.

### Results and Impact

SCIZOR consistently improved policy performance, achieving an average success rate increase of 15.4% compared to training on the full dataset. Specifically, SCIZOR yielded absolute gains of 5.4% on RoboMimic, 8.1% on OXEMagic, and 32.9% on Sirius-Fleet.

### Publication

The paper is part of the 2026 IEEE International Conference on Robotics and Automation (ICRA). The authors are Zhang, Yu and Xie, Yuqi and Liu, Huihan and Shah, Rutav and Wan, Michael and Fan, Linxi and Zhu, Yuke.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0072508c-f460-4040-ae59-66ae35c20032",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "6395a59e-9fce-4742-a67b-d7b7f1ca97be",
  "sourceToolAssistantUUID": "0072508c-f460-4040-ae59-66ae35c20032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T10:03:57.225Z_

<details><summary>↩ Tool result · `toolu_01Axts3Vvz1nKYnKxydf5J1Q`</summary>

```text
Web search results for query: ""weighted imitation learning" sample weights quality"

Links: [{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/html/2509.01657"},{"title":"What is the Effect of Importance Weighting in Deep Learning?","url":"http://proceedings.mlr.press/v97/byrd19a/byrd19a.pdf"},{"title":"Imitation Learning from Suboptimal Demonstrations via Meta-Learning An Action Ranker","url":"https://arxiv.org/html/2412.20193v1"},{"title":"Weighted quality estimates in machine learning | Bioinformatics | Oxford Academic","url":"https://academic.oup.com/bioinformatics/article/22/21/2597/252278"},{"title":"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning","url":"https://arxiv.org/html/2604.23000"},{"title":"10 Imitation Learning","url":"https://web.stanford.edu/class/cs237b/pdfs/lecture/lecture_10111213.pdf"},{"title":"Machine Learning 101: The What, Why, and How of Weighting - KDnuggets","url":"https://www.kdnuggets.com/2019/11/machine-learning-what-why-how-weighting.html"},{"title":"(PDF) Weighted Machine Learning","url":"https://www.researchgate.net/publication/328731166_Weighted_Machine_Learning"},{"title":"Learning Fast Sample Re-weighting Without Reward Data","url":"https://arxiv.org/pdf/2109.03216"},{"title":"LOW: Training deep neural networks by learning optimal sample weights - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320320303885"}]

Based on the search results, here's what I found about weighted imitation learning and sample quality:

## Key Concepts

Importance Weighted Retrieval (IWR) is an importance sampling-inspired method for retrieval in few-shot imitation learning. This approach addresses limitations in how training data is selected and weighted.

## Weighted Imitation Learning from Suboptimal Demonstrations

Recent research has focused on using weights to assess demonstration quality. Weighted behavior cloning approaches involve training a discriminator to assess demonstration quality, applying weights based on the advantage function relative to the learned policy to ensure high-quality demonstrations are retained.

Standard imitation learning algorithms, which process expert and non-expert demonstrations indiscriminately, may inadvertently learn the deficiencies inherent in suboptimal demonstrations. To address this, weights can be applied based on the advantage function relative to the learned policy to ensure that high-quality demonstrations outside the expert distributions are retained.

## Data Quality Assessment Through Weighting

Another approach uses smoothness-based metrics for quality assessment. RINSE uses two complementary metrics: Spectral Arc Length (SAL) for spectral frequency-domain regularity and Trajectory-Envelope Distance (TED) for spatial geometric deviation. These weights can then be applied within training frameworks to prioritize higher-quality demonstrations.

## General Principles

Sample weights are useful when some training samples are measured by more accurate devices, come from different sources with different reliabilities, or some samples are more relevant than others—all considerations relevant to imitation learning quality assessment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59206698-008b-4c16-af95-86df387a070f",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "63866eba-ae03-4c30-b288-0f5a64b35df2",
  "sourceToolAssistantUUID": "59206698-008b-4c16-af95-86df387a070f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T10:04:00.561Z_

Now let me fetch the detailed papers for SCIZOR, DemInf, and the new papers I found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63866eba-ae03-4c30-b288-0f5a64b35df2",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNtE4B2uBeb7fU62jhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "473ba167-30d7-4038-b09a-c420a8254bef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhzMYW7MCaTk88apNEzCkW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6739,
      "cache_read_input_tokens": 10916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6739,
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

_source line 22 · 2026-05-13T10:04:03.054Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XPe75hb83athVJzpFSJzi3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.22626",
  "prompt": "Extract all details about SCIZOR: the full method description, all experimental results (especially on Sirius-Fleet with exact numbers), all baselines compared against, and any ablation studies. Include success rate numbers for all tasks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "473ba167-30d7-4038-b09a-c420a8254bef",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNtE4B2uBeb7fU62jhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e458d4a2-addf-46d3-ac03-78b093298c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhzMYW7MCaTk88apNEzCkW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6739,
      "cache_read_input_tokens": 10916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6739,
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

_source line 23 · 2026-05-13T10:04:04.510Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0186FCbYvosB6X6Nkxdg8CwT`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.08623",
  "prompt": "Extract all details about DemInf: the full method description, all experimental results on RoboMimic with exact numbers for each task, all baselines, failure modes, and limitations discussed by the authors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e458d4a2-addf-46d3-ac03-78b093298c41",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNtE4B2uBeb7fU62jhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07ed8c27-cf14-454c-a5ab-bad9c7983ca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhzMYW7MCaTk88apNEzCkW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6739,
      "cache_read_input_tokens": 10916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6739,
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

_source line 24 · 2026-05-13T10:04:05.810Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VhpjbGq9kUGBCooL22L5XV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.09056",
  "prompt": "Extract all details about this paper: the full method description (CUPID / influence functions), all experimental results with exact numbers, baselines, and how it compares to DemInf and SCIZOR."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07ed8c27-cf14-454c-a5ab-bad9c7983ca7",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNtE4B2uBeb7fU62jhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3049939f-64c2-4468-af52-037cf5e105d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhzMYW7MCaTk88apNEzCkW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6739,
      "cache_read_input_tokens": 10916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6739,
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

_source line 25 · 2026-05-13T10:04:06.734Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KSHzRZ7cxgCmCxGyCEFzoi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.09603",
  "prompt": "Extract all details about DataMIL: the method description, experimental results with exact numbers, baselines, and how it differs from other curation methods like DemInf and SCIZOR."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3049939f-64c2-4468-af52-037cf5e105d8",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNtE4B2uBeb7fU62jhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e460025b-bd93-4c1c-af6d-a6b3ff8a868b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhzMYW7MCaTk88apNEzCkW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6739,
      "cache_read_input_tokens": 10916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6739,
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

_source line 26 · 2026-05-13T10:04:07.278Z_

<details><summary>↩ Tool result · `toolu_01XPe75hb83athVJzpFSJzi3`</summary>

```text
# SCIZOR: Data Curation for Imitation Learning

## Method Overview

SCIZOR is described as "a self-supervised data curation framework that filters out low-quality state-action pairs to improve the performance of imitation learning policies."

The approach targets two types of problematic data:
1. **Suboptimal data** - removes samples that lack task progression using a self-supervised task progress predictor
2. **Redundant data** - eliminates repetitive patterns through a deduplication module operating on joint state-action representations

## Experimental Results

The document provides limited quantitative details. The abstract states: "SCIZOR enables imitation learning policies to achieve higher performance with less data, yielding an average improvement of 15.4% across multiple benchmarks."

However, the provided content **does not include**:
- Specific results for Sirius-Fleet or any individual benchmark with exact success rates
- Detailed baseline comparisons
- Ablation study results
- Task-specific performance numbers

## Missing Information

The abstract references a project website ("this https URL") for additional details, but the actual paper content needed to extract comprehensive experimental results, specific baseline comparisons, and ablation studies is not included in the provided webpage excerpt. Access to the full PDF or HTML version would be necessary to provide the detailed quantitative analysis requested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e458d4a2-addf-46d3-ac03-78b093298c41",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "4426f7f3-2c8b-413e-91f8-46675cf971c9",
  "sourceToolAssistantUUID": "e458d4a2-addf-46d3-ac03-78b093298c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T10:04:08.158Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ByV8LFui7AVa3hc5UQjEuS`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.01479",
  "prompt": "Extract all details about Density-Ratio Weighted Behavioral Cloning: the method, how sample weights are computed, experimental results, and how it handles corrupted/low-quality demonstrations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4426f7f3-2c8b-413e-91f8-46675cf971c9",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNtE4B2uBeb7fU62jhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08c3e234-c748-4358-a4dc-22eb8f86afb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhzMYW7MCaTk88apNEzCkW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6739,
      "cache_read_input_tokens": 10916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6739,
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

_source line 28 · 2026-05-13T10:04:08.960Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NhFEo9KAMsbiTQQhLA8SR3`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.03707",
  "prompt": "Extract all details about Demo-SCORE: the method for curating demonstrations using online experience, results, baselines, and how it self-curates data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08c3e234-c748-4358-a4dc-22eb8f86afb2",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNtE4B2uBeb7fU62jhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6d45e5a-a090-4716-88e8-bbd11fad709d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhzMYW7MCaTk88apNEzCkW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6739,
      "cache_read_input_tokens": 10916,
      "output_tokens": 682,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6739
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 682,
          "cache_read_input_tokens": 10916,
          "cache_creation_input_tokens": 6739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6739,
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

_source line 29 · 2026-05-13T10:04:09.164Z_

<details><summary>↩ Tool result · `toolu_0186FCbYvosB6X6Nkxdg8CwT`</summary>

```text
# Analysis of arXiv:2502.08623

I cannot provide the specific details you requested because the webpage content provided contains only the **abstract and metadata** of the paper, not the full paper itself.

## What's Available:

The abstract mentions the core approach: "estimate the average contribution of a trajectory towards the mutual information between states and actions" using "k-nearest neighbor estimates of mutual information on top of simple VAE embeddings."

The abstract reports results generally: "training policies based on data filtered by our method leads to a 5-10% improvement in RoboMimic and better performance on real ALOHA and Franka setups."

## What's Not Available in This Source:

- **Detailed DemInf method description** (full algorithm, mathematical formulations, implementation specifics)
- **RoboMimic task-by-task results with exact numbers** for each benchmark
- **Complete baseline comparisons** 
- **Failure modes and limitations** discussed by authors
- **Experimental protocols and hyperparameters**

## To Obtain This Information:

You would need to access the full paper via:
- The PDF link provided: `/pdf/2502.08623`
- The HTML version: `arxiv.org/html/2502.08623v3`
- The project website referenced: `jhejna.github.io/demonstration-info`

The webpage itself only summarizes the work at a high level.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07ed8c27-cf14-454c-a5ab-bad9c7983ca7",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "125b2a27-f0b3-4008-acaa-1aa74b77ce6c",
  "sourceToolAssistantUUID": "07ed8c27-cf14-454c-a5ab-bad9c7983ca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T10:04:09.802Z_

<details><summary>↩ Tool result · `toolu_01VhpjbGq9kUGBCooL22L5XV`</summary>

```text
# Paper Analysis: Quality over Quantity (QoQ)

## Overview
Based on the arXiv page content provided, I can only offer limited details, as the full paper text isn't included in the excerpt.

## Method Description
The paper proposes **Quality over Quantity (QoQ)**, which defines data quality as "the contribution of each training sample to reducing loss on validation demonstrations." The approach leverages **influence functions** to quantify impact of individual training samples on model performance.

Two key adaptations for robot demonstrations are mentioned:
1. Using maximum influence across validation samples for relevant state-action pairs
2. Aggregating influence scores within trajectories to reduce noise

## Experimental Results
The abstract states that "Experiments in both simulated and real-world settings show that QoQ consistently improves policy performances over prior data selection methods," but **no specific numerical results, baselines, or comparisons to DemInf and SCIZOR are provided** in the available content.

## Limitations
The webpage excerpt contains only the abstract and metadata. To access:
- Detailed experimental numbers
- Specific baseline comparisons
- Performance metrics against competing methods
- Full methodology details

You would need to view the full PDF or HTML paper version linked on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3049939f-64c2-4468-af52-037cf5e105d8",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "326a6cc1-ad97-4f4a-a589-85e37991de56",
  "sourceToolAssistantUUID": "3049939f-64c2-4468-af52-037cf5e105d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T10:04:11.569Z_

<details><summary>↩ Tool result · `toolu_01KSHzRZ7cxgCmCxGyCEFzoi`</summary>

```text
# DataMIL: Data Selection for Robot Imitation Learning

## Method Description

DataMIL is a policy-driven data selection framework based on datamodels that addresses a key challenge in robot learning: while large datasets produce strong average performance, they often underperform on specialized tasks. The approach differs fundamentally from traditional filtering methods.

The framework "directly optimizes data selection for task success, allowing us to select data that" enhance policies while removing harmful data, rather than relying on human-defined quality metrics like visual or semantic similarity.

To make the approach practical for real-world deployment, researchers developed "a novel surrogate loss function on task-specific data, allowing us to use DataMIL in the real world without" requiring expensive environmental rollouts during selection.

## Experimental Results

The paper validates DataMIL across "more than 60 simulation and real-world manipulation tasks," including successful data selection from Open X-Embodiment datasets. Results demonstrate "consistent gains in success rates and superior performance" compared to baseline approaches.

## Comparative Analysis

The abstract does not provide specific details about baseline methods, numerical comparisons, or mentions of competing approaches like DemInf or SCIZOR. The content focuses on distinguishing DataMIL's "end-to-end, performance-aware data selection" philosophy rather than detailed quantitative comparisons with named alternatives.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e460025b-bd93-4c1c-af6d-a6b3ff8a868b",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "9950d805-0c74-4e1d-a79b-22e49f2d2709",
  "sourceToolAssistantUUID": "e460025b-bd93-4c1c-af6d-a6b3ff8a868b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T10:04:15.658Z_

<details><summary>↩ Tool result · `toolu_01ByV8LFui7AVa3hc5UQjEuS`</summary>

```text
# Density-Ratio Weighted Behavioral Cloning: Summary

## Core Method

The approach learns robust control policies from contaminated offline datasets using a three-stage process. As the paper states, the method "uses a small, verified clean reference set to estimate trajectory-level density ratios via a binary discriminator."

**Key Innovation**: Rather than treating all trajectories equally, the system identifies and downweights corrupted data without knowing the contamination mechanism.

## Sample Weight Computation

Weights are calculated through these steps:

1. **Discriminator Training**: A binary classifier distinguishes between clean reference trajectories and potentially corrupted main dataset samples using balanced logistic regression.

2. **Density Ratio Extraction**: The discriminator output is converted to density ratios using the formula: r(τ) = d_φ(τ)/(1-d_φ(τ))

3. **Clipping**: Ratios are clipped to [ε, C] where ε=10⁻³ and C=2.0 to ensure numerical stability and prevent extreme weights.

4. **Policy Training**: The behavioral cloning objective is weighted by these computed values, prioritizing expert-like behaviors.

## Experimental Results

Testing on D4RL benchmarks (HalfCheetah, Ant, Walker2d, Hopper) with contamination from α ∈ {0.2, 0.4, 0.6, 0.8, 1.0}:

- **Superior Performance**: "Weighted BC maintains near-optimal performance even at high contamination ratios outperforming baselines such as traditional BC, BCQ and BRAC"
- **Retention**: Maintains over 80% performance retention up to 60% contamination
- **Relative Gains**: Shows positive improvement in 93% of test scenarios, with up to 200% improvement under extreme contamination
- **Computational Efficiency**: Only 1.04× overhead compared to standard behavioral cloning

## Handling Corrupted Demonstrations

The method addresses four poisoning types:

- **Reward poisoning**: Inverting positive rewards
- **State poisoning**: Adding Gaussian noise to observations
- **Transition poisoning**: Shuffling next-state observations
- **Action poisoning**: Perturbing actions with noise

Performance remains robust across all contamination types without requiring prior knowledge of which corruption mechanism was applied.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08c3e234-c748-4358-a4dc-22eb8f86afb2",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "f468e0d6-7778-4833-ba2d-e07bb5fa9b52",
  "sourceToolAssistantUUID": "08c3e234-c748-4358-a4dc-22eb8f86afb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-13T10:04:19.159Z_

<details><summary>↩ Tool result · `toolu_01NhFEo9KAMsbiTQQhLA8SR3`</summary>

```text
# Demo-SCORE: Demonstration Curation via Online Experience

## Core Method

Demo-SCORE automatically curates robot demonstration datasets by identifying and removing unreliable demonstrations based on policy performance. The approach leverages the key insight that "when a policy is trained on heterogeneous demonstrations, its performance during rollouts can reveal which demonstrated strategies are most reliable."

### Four-Step Process

1. **Initial Policy Training**: Train a policy on the full demonstration set to learn all demonstrated behaviors

2. **Rollout Collection**: Generate rollouts at multiple checkpoints (C checkpoints, typically 4-5) during training to capture varying policy distributions

3. **Classifier Training & Cross-Validation**: Train C-1 classifiers on rollouts from early checkpoints to distinguish successful from failed trajectories. Cross-validate using rollouts from the final checkpoint to prevent overfitting to any single policy state

4. **Demonstration Filtering**: Apply the best-performing classifier to filter the original dataset, keeping only demonstrations where the average success probability exceeds a threshold γ (computed as the mean classifier confidence on successful rollouts)

## Key Technical Insight

The method addresses distribution shift between rollouts and demonstrations through cross-validation across multiple policy checkpoints. This prevents the classifier from overfitting to rollouts from a single checkpoint while still generalizing to the original demonstration distribution.

## Results Summary

**Simulated Tasks** (Peg insertion, Square peg):
- Demo-SCORE achieves 15-35% absolute improvement in success rate over baseline
- Reduces failure rates by 2× compared to Autonomous Imitation Learning
- Filters 16-67% of demonstrations depending on data composition

**Real-World ALOHA Tasks** (Spoon, Chocolate, Sharpie, Strawberry, Jellybean):
- Approximately 30% average success rate improvement
- Jellybean task: increases full-task success from 0% to 20%
- Identifies strategy-specific failures humans find difficult to discern

## Baseline Comparisons

1. **Base Policy**: Trains on all original demonstrations
2. **Training Loss Weighting**: Weights demos inversely proportional to policy loss
3. **Autonomous Imitation Learning (Auto-IL)**: Combines original demos with successful rollout episodes
4. **Return-Conditioned Policies (RCP)**: Trains with success/failure return signals

Demo-SCORE consistently outperforms all baselines across tasks and data mixtures.

## Design Robustness

Ablation studies demonstrate:
- Effective with as few as 10 rollouts per checkpoint (100 total)
- Works with chunk-level or episode-level filtering
- Performs comparably with trajectory classifiers or single-step classifiers
- Cross-validation is critical; without it, performance drops significantly

## Limitations

- Assumes policy rollouts represent the original demonstration distribution
- May struggle when all demonstrations are too low-quality for initial policy learning
- Can reduce state coverage compared to training on full datasets
- Recommended for final policy training rather than pre-training stages
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6d45e5a-a090-4716-88e8-bbd11fad709d",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "29b89eed-dc09-4e3f-83e8-a9c6dbac16c1",
  "sourceToolAssistantUUID": "f6d45e5a-a090-4716-88e8-bbd11fad709d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-13T10:04:22.356Z_

Let me now fetch the full HTML versions of the SCIZOR and DemInf papers for detailed results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29b89eed-dc09-4e3f-83e8-a9c6dbac16c1",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNuqrFDywTAornwiEq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "520daa49-bc3d-49b1-bf88-89120566ba8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sTP78vbwGY7uyTeLTz9JE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3252,
      "cache_read_input_tokens": 17655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3252,
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

_source line 35 · 2026-05-13T10:04:25.081Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015SdCEFHUsjsGfQrcPmayHf`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.22626v2",
  "prompt": "Extract ALL experimental results, especially: 1) Sirius-Fleet results with exact success rate numbers for each task, 2) RoboMimic results with exact numbers, 3) OXEMagic results, 4) All baselines listed and their performance numbers, 5) Ablation study results showing contribution of suboptimal removal vs deduplication, 6) How many demonstrations were filtered out. Report every number you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "520daa49-bc3d-49b1-bf88-89120566ba8f",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNuqrFDywTAornwiEq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f62bb027-c3ec-4c25-b44f-7d47bcae252e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sTP78vbwGY7uyTeLTz9JE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3252,
      "cache_read_input_tokens": 17655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3252,
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

_source line 36 · 2026-05-13T10:04:28.732Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VVYzoDimGQ6ySxiXAyYf2H`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.08623v2",
  "prompt": "Extract ALL experimental results and details: 1) RoboMimic results with exact success rate numbers for EVERY task (Lift, Can, Square, Transport, etc.), 2) All baselines and their exact numbers, 3) The mathematical formulation of the mutual information estimation, 4) Failure modes and limitations section, 5) How the method handles different types of demonstrations, 6) Real robot results. Report every number you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f62bb027-c3ec-4c25-b44f-7d47bcae252e",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNuqrFDywTAornwiEq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74e67e3d-fc8b-4188-8957-9c96905b6046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sTP78vbwGY7uyTeLTz9JE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3252,
      "cache_read_input_tokens": 17655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3252,
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

_source line 37 · 2026-05-13T10:04:29.111Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013MXern8WysMMCGEDeGf9vR`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.09056",
  "prompt": "Extract ALL details about CUPID/QoQ: the method, influence function formulation, all experimental results with exact numbers, baselines including DemInf and SCIZOR comparisons, ablations, and failure modes. Report every number you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74e67e3d-fc8b-4188-8957-9c96905b6046",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNuqrFDywTAornwiEq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed336253-9b2e-429f-8e45-055123eb58ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sTP78vbwGY7uyTeLTz9JE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3252,
      "cache_read_input_tokens": 17655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3252,
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

_source line 38 · 2026-05-13T10:04:30.415Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WMYnda99aKSkCTHufqyqpZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.23000",
  "prompt": "Extract all details about RINSE / smoothness-driven metrics for data quality in imitation learning: the method, metrics used, experimental results with numbers, and how quality scores are used as weights."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed336253-9b2e-429f-8e45-055123eb58ff",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNuqrFDywTAornwiEq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca3d1753-2135-45bc-a130-ee00f0528e8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sTP78vbwGY7uyTeLTz9JE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3252,
      "cache_read_input_tokens": 17655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3252,
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

_source line 39 · 2026-05-13T10:04:32.506Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019iJnAchnGfF55Yi3ZSFL5c`</summary>

```json
{
  "url": "https://openreview.net/forum?id=fIj88Tn3fc",
  "prompt": "Extract all details about ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning. Method, results, how it weights different data subsets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca3d1753-2135-45bc-a130-ee00f0528e8a",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNuqrFDywTAornwiEq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f75c5e7-748a-4098-857b-d77c547fbc61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sTP78vbwGY7uyTeLTz9JE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3252,
      "cache_read_input_tokens": 17655,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3252
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 702,
          "cache_read_input_tokens": 17655,
          "cache_creation_input_tokens": 3252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3252,
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

_source line 40 · 2026-05-13T10:04:35.575Z_

<details><summary>↩ Tool result · `toolu_015SdCEFHUsjsGfQrcPmayHf`</summary>

```text
# Scizor Experimental Results Summary

## Overall Performance Improvements
Scizor achieved "absolute gains of 5.4% on RoboMimic, 8.1% on OXEMagic, and 32.9% on the Sirius-Fleet real-robot tasks" with "an average improvement of 15.4% across multiple benchmarks."

## Sirius-Fleet Results (Real Robot)
Task-by-task success rates with Scizor vs. baselines:

| Task | No Deletion | Suboptimal Only | Dedup Only | DemInf | Scizor |
|------|------------|-----------------|-----------|--------|--------|
| Book→Caddy | 40.0% | 65.0% | 45.0% | 66.7% | **66.7%** |
| Cup→Caddy | 65.0% | 75.0% | 75.0% | 53.3% | **73.3%** |
| Bowl→Plate | 65.0% | 70.0% | 80.0% | 60.0% | **93.3%** |
| Mug→Plate | 35.0% | 60.0% | 70.0% | 50.0% | **83.3%** |
| Mug→Basket | 35.0% | 35.0% | 65.0% | 50.0% | **66.7%** |
| Bowl→Basket | 60.0% | 90.0% | 70.0% | 76.7% | **96.7%** |
| Mug→Tray | 35.0% | 50.0% | 60.0% | 53.3% | **66.7%** |
| Bread→Plate | 50.0% | 60.0% | 60.0% | 63.3% | **90.0%** |

## RoboMimic Results

| Method | Can | Square |
|--------|-----|--------|
| Suboptimal Only | 84.0% | 37.8% |
| Dedup Only | 74.3% | 22.4% |
| Random Deletion | 78.0% | 32.2% |
| DemInf | 88.9% | 41.4% |
| **Scizor** | **87.3%±0.7** | **37.2%±2.5** |

## OXE Results

**OXEMagic Mixture:**
- No Deletion: Pick Can 27.0%, Move Near 13.1%
- Suboptimal Only: Pick Can 33.7%, Move Near 16.9%
- Dedup Only: Pick Can 31.8%, Move Near 12.3%
- **Scizor: Pick Can 39.5%, Move Near 16.7%**

**OXERT-X Mixture:**
- Re-Mix: Pick Can 40.5%, Move Near 15.0%
- **Scizor: Pick Can 43.3%, Move Near 19.2%**

## Ablation Study Results (Table 1)

| Component | RoboMimic | Sirius-Fleet | OXEMagic |
|-----------|-----------|--------------|----------|
| Suboptimal Only | 60.9±1.8 | 64.2±2.6 | 25.3±2.9 |
| Dedup Only | 48.3±0.8 | 63.3±6.9 | 22.1±0.9 |
| **Full Scizor** | **62.3±1.6** | **79.6±1.4** | **28.1±3.3** |

## Data Filtering Rates (Table 3)

Deletion ratios using unified thresholds (ε_s=0.58, ε_d=0.99):

| Dataset | Suboptimal | Dedup | Total |
|---------|-----------|-------|-------|
| RoboMimic | 29.3% | 0.3% | 29.6% |
| Sirius-Fleet | 4.7% | 3.2% | 7.9% |
| OXEMagic | 11.9% | 4.5% | 15.8% |
| OXERT-X | 15.0% | 0.8% | 15.8% |
| OXERT-1 | 9.2% | 0.5% | 9.7% |

## Baseline Comparisons
Scizor outperformed "Re-Mix by 3.5% on average" and significantly outperformed DemInf by "19.2% on the Sirius-Fleet dataset."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f62bb027-c3ec-4c25-b44f-7d47bcae252e",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "c0ba3685-eb71-4d22-b3fa-2e5f39fbc574",
  "sourceToolAssistantUUID": "f62bb027-c3ec-4c25-b44f-7d47bcae252e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-13T10:04:36.046Z_

<details><summary>↩ Tool result · `toolu_019iJnAchnGfF55Yi3ZSFL5c`</summary>

```text
# ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning

## Overview
ReMix is a method for optimizing how different data subsets are weighted when training robotics foundation models. The approach addresses a gap in robotics research, as "data selection has been of utmost importance to scaling in vision and natural language processing (NLP)" yet received limited attention in robotics.

## Methodology
ReMix employs **distributionally robust optimization (DRO)** techniques to learn data mixture weights. The method aims to "maximize worst-case performance across all possible downstream domains." 

To make DRO practical for robotics datasets with varying action spaces and dynamics, ReMix incorporates:
- Early stopping mechanisms
- Action normalization and discretization strategies

## Key Results
The technique demonstrated substantial improvements across robotics datasets:
- **40% performance gains** compared to uniform weighting on average
- **20% improvement** over human-selected weights on datasets used for RT-X model training

## Application
ReMix was validated extensively on two major robotics datasets: Bridge and OpenX (used in RT-X development). The research suggests that "data curation can have an outsized impact on downstream performance" in robotics foundation models.

**Code availability:** https://github.com/jhejna/remix
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f75c5e7-748a-4098-857b-d77c547fbc61",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "7300e536-ac8e-46e1-9d09-783dd0b78cad",
  "sourceToolAssistantUUID": "9f75c5e7-748a-4098-857b-d77c547fbc61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T10:04:40.693Z_

<details><summary>↩ Tool result · `toolu_01WMYnda99aKSkCTHufqyqpZ`</summary>

```text
# RINSE: Smoothness-Driven Metrics for Data Quality in Imitation Learning

## Overview
RINSE (Ranking and INdexing Smooth Examples) is a lightweight framework that evaluates demonstration quality based on trajectory smoothness, operating without policy training or rollouts.

## Core Metrics

**Spectral Arc Length (SAL)**
SAL measures frequency-domain smoothness by analyzing the Fast Fourier Transform of velocity signals. The metric quantifies "the arc length along the log-spectrum curve; a short arc length forces steep spectral decay, penalizing high-frequency energy." Lower (more negative) SAL scores indicate smoother trajectories, with computation in O(T log T) time.

**Trajectory-Envelope Distance (TED)**
TED captures spatial smoothness through contact-aware geometric deviation. The approach:
- Partitions trajectories by gripper contact status
- Fits low-degree Bézier curves to each phase
- Measures DTW distance between raw and smoothed trajectories
- Operates in O(KT) time, typically tens of milliseconds per trajectory

## Theoretical Foundation

The authors decompose behavioral cloning loss into two components: policy error and an irreducible "noise floor" representing conditional action variance. They demonstrate that "filtering to retain only smooth, high-quality demonstrations reduces conditional action variance of the retained data distribution," improving the learning signal while maintaining task coverage.

## Experimental Results

**RoboMimic Benchmarks:**
- Transport task: "SAL filtering achieves 16% higher success using one-sixth of the data"
- Tool Hang: 8% improvement with 50% of demonstrations
- Convergence: 10× speedup on filtered subsets

**Real-World Manipulation:**
- Push Block: "20% improvement with half the data" using TED filtering
- Outperforms random subsets by 8–32 percentage points

**Quality Diagnostics:**
- RTIS modality ranking: Consistently orders kinesthetic > VR > spacemouse
- Re-Mix domain reweighting: "Spearman ρ ≥ 0.89" correlation with learned allocations

**Retrieval Integration:**
LIBERO-10 (STRAP framework): "5.6% improvement" in mean success by re-ranking retrieved sub-trajectories

## Quality Score Application

In Re-Mix domain reweighting, trajectories receive exponential weights based on normalized quality scores: w(τ) = exp(−λq(τ)). This weighting adjusts per-domain loss contributions, allowing smoother demonstrations to carry greater influence during training without explicit filtering.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca3d1753-2135-45bc-a130-ee00f0528e8a",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "cc8c0e90-ddbd-48bc-8bf2-f084f4e924e4",
  "sourceToolAssistantUUID": "ca3d1753-2135-45bc-a130-ee00f0528e8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-13T10:04:42.778Z_

<details><summary>↩ Tool result · `toolu_013MXern8WysMMCGEDeGf9vR`</summary>

````text
# Analysis of QoQ Method and Experimental Results

## Method Overview

QoQ (Quality over Quantity) defines data quality as "direct performance contribution to the learned policy" using influence functions. The approach comprises two key steps:

**Step 1 - Contribution Estimation:**
Computes QoQ-score for each state-action pair as: maximum gradient similarity across validation samples rather than averaging. This "maximum influence scoring" focuses on the most relevant validation state-action pair.

**Step 2 - Trajectory-wise Curation:**
Aggregates influence scores within trajectories using mean, then selects top N trajectories. This prevents redundant state-action selection while maintaining diverse state coverage.

## Influence Function Formulation

QoQ uses normalized gradient dot products (Equation 6):
```
QoQ-score(s,a) = max gradient_similarity(validation, training pairs)
```

This approximates influence functions via "normalized gradients" without computing inverse Hessians, addressing computational constraints with large models.

## Experimental Results - Exact Numbers

**Simulation (Robomimic Can-placement):**
- QoQ success rate: 99.2%
- Flow Retrieval (best baseline): 76.0%
- All data baseline: 55.4% curation accuracy

**Real Robot - Banana Grasping:**
- QoQ curation accuracy: 83.6 ± 0.8%
- QoQ success rate: 86.7% ± 8.9
- Behavior Retrieval: 67.3 ± 0.7% curation accuracy, 56.7% success
- Flow Retrieval: 57.7 ± 0.1% curation accuracy
- All data: 58.7% baseline success

**Multi-object Pick-and-place:**
- QoQ success: 93.3%
- Behavior Retrieval: 20% (nearly failed)
- Flow Retrieval: substantially better but below QoQ

**DROID Dataset (In-the-wild):**
- QoQ maintained highest curation accuracy across domains with heterogeneous visual inputs

**Cabinet Opening (Policy Rollout Validation):**
- Curated dataset improved success rate versus all-data baseline

## Ablation Study Results

**Maximum Influence Scoring:**
Significantly improved curation accuracy and success rates versus averaging approach across metrics.

**Trajectory-wise Curation:**
Substantially outperformed state-action-wise curation, preventing distributional bias that degraded behavior cloning performance.

**Gradient Computation Layers:**
- Action Head only: 83.6 ± 1.3% curation accuracy
- Backbone (Vision/VLM): 82.7 ± 0.6%
- All parameters: 82.1 ± 1.2%
Results show comparable performance without full model gradient computation.

**Curation Budget Variation:**
- Budget 10: 36.7 ± 17.6% success
- Budget 20: 63.3 ± 17.6%
- Budget 40: 60.0 ± 10.0%
- Budget 60: 86.7 ± 8.9%
QoQ consistently outperformed Behavior Retrieval across all budgets.

## Baseline Comparisons

**Methods Evaluated:**
1. Behavior Retrieval (VAE-based latent space similarity)
2. Flow Retrieval (optical flow in VAE latent space)
3. All data (no curation)

**Notable:** The paper mentions related work CUPID and DataMIL also use influence functions, but differs by using maximum influence versus averaging/summing across validation transitions. Paper claims this improves stability through "noisy signal" reduction.

## Limitations Acknowledged

- Cannot selectively use high-quality segments within trajectories (trajectory-level only)
- Influence computation remains costly despite layer restrictions and OPORP compression
- Assumes shared embodiments between training/validation
- Demonstrated only with behavior cloning (not offline RL)

## Data Selection Consistency

Kendall's W correlation across seeds:
- QoQ: 0.7713 (most consistent)
- Flow Retrieval: 0.7026
- Behavior Retrieval: 0.3287

Higher consistency indicates more reliable trajectory scoring across random seeds.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed336253-9b2e-429f-8e45-055123eb58ff",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "d93a257a-5d58-41f4-9495-b7c958b82ba9",
  "sourceToolAssistantUUID": "ed336253-9b2e-429f-8e45-055123eb58ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-13T10:04:46.723Z_

<details><summary>↩ Tool result · `toolu_01VVYzoDimGQ6ySxiXAyYf2H`</summary>

```text
# Experimental Results and Technical Details from DemInf Paper

## Mathematical Formulation

The core mutual information estimation uses the KSG estimator:

**Mutual Information Decomposition:**
"I(S;A) = H(S) − H(A|S)" where S represents states and A represents actions.

**Sample-wise MI Contribution:**
The method decomposes dataset-level MI into individual contributions: "Î(S;A) = 1/|𝒟_N| ∑ Î(s_i, a_i; 𝒟_N)"

**KSG Estimator Formula:**
"Î(s_i, a_i; 𝒟_N) ∝ −ψ(n(z_s,i)+1) − ψ(n(z_a,i)+1)" where ψ is the digamma function.

---

## RoboMimic Results

The paper does NOT provide explicit success rate percentages for individual tasks. Instead, results are presented as quality filtering curves comparing average expert quality scores. Key findings:

- **Image-based performance:** DemInf "surpasses all methods on both RoboMimic" tasks
- **State-based performance:** DemInf performs "as well or better than baselines in all environments"
- **Policy performance gains:** Training on DemInf-filtered data yields "5-10% improvement in RoboMimic"
- Figure 8 shows "over 10% in Can and is the only method to improve upon training on all of the data in Square"

Tasks evaluated: Lift, Can, Square (multi-human variants with state and image inputs)

---

## Baseline Comparisons

Baselines include:

1. **Uncertainty:** Ensemble of 5 policies predicting data uncertainty
2. **Compatibility:** Gandhi et al. method combining novelty and likelihood
3. **VIP (Value Implicit Pre-training):** Action-free goal-conditioned RL approach
4. **InfoNCE (MI):** Symmetric InfoNCE contrastive learning
5. **MINE (MI):** Dual-form KL divergence mutual information estimator

**Key Finding:** "InfoNCE and MINE perform acceptably in state-based settings" but "perform significantly worse in image based settings as dimensionality increases."

---

## Real Robot Results

### RoboCrowd (ALOHA Platform)
- Tasks: HiChew, TootsieRoll, HersheyKiss candy bin-picking
- Dataset sizes: 40-100 demonstrations per task
- Policy trained: ACT (Action Chunking with Transformers)
- Result: DemInf-filtered policies show "better performance on real ALOHA"
- Human eval shows DemInf policy "more commonly successfully completes the task"

### Franka Panda Robot
- Tasks: PenInCup, DishRack
- Dataset: 60-80 demonstrations (50% expert, 50% intentionally poor quality)
- Policy trained: Diffusion Policy
- Result: "DemInf always outperforms the random subset"
- Note: "Training on all data does slightly better than filtering with DemInf on PenInCup" (harder task requiring more training data despite quality issues)

---

## Method: Handling Different Demonstrations

**VAE Representation Learning:** Separate VAEs embed states and actions into low-dimensional representations suitable for k-NN estimation.

**Scoring Function:**
"S(τ) = 1/T ∑_{t=1}^T Î(s_t, a_t; 𝒟_N)" (average MI contribution across trajectory timesteps)

**Why Not Timestep-Level Filtering:** The method deliberately averages across time because "filtering data by mutual information at the state-action level might drop data for crucial parts of a task that inherently have lower mutual information."

Example shown in Figure 2: Grasping phases exhibit low MI compared to free motion, yet grasping is task-critical.

---

## Failure Modes and Limitations

1. **Action Entropy Over-indexing:** The method may "over-index on H(A|S)" since action entropy directly determines state entropy temporally in sequential settings.

2. **State Entropy Outliers:** "DemInf could prefer outlier trajectories that visit a new part of the state space" if actions remain consistent.

3. **Pauses/Predictable Inaction:** Method is "susceptible to preferring data that is predictable, but might not make progress towards completing the task" (e.g., extended pauses).

4. **Greedy Procedure:** "DemInf's curation procedure is greedy and not globally optimal—once we remove an episode we have changed the data distribution."

---

## Ablation Studies

**k-NN Parameter Sensitivity (Figure 10):** "DemInf's performance is generally robust to this parameter, with no substantial change" across tested values.

**MI Estimator Comparison (Figure 11):** KSG estimator "superior to both the BiKSG estimator...and the naïve application of the differential entropy estimator."

**Variance Analysis:** DemInf exhibits "far lower variance across seeds" compared to InfoNCE and MINE, which showed "one or two runs that performed far worse than the others."

---

## Data Efficiency

The method works effectively with robotics dataset sizes of "50-300 demonstrations commonly used in robotics," where parametric estimators like InfoNCE require "hundreds of millions of training examples."

Human annotation labels used for evaluation ranged from 0-3 quality scores across datasets, enabling quantitative assessment against ground truth.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74e67e3d-fc8b-4188-8957-9c96905b6046",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "d5269223-a207-467d-9814-cdf3e604955d",
  "sourceToolAssistantUUID": "74e67e3d-fc8b-4188-8957-9c96905b6046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-13T10:04:49.468Z_

Now let me get more details on the weighted imitation learning approaches and fetch the SCIZOR project page for any additional details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5269223-a207-467d-9814-cdf3e604955d",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNwseh8ds4K9mbW6Cio",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a566c4aa-2754-4484-b0d4-dde973c1cd43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012phkrTPbALfeeK7TP3kQCi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 3256,
      "cache_read_input_tokens": 20907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3256,
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

_source line 46 · 2026-05-13T10:04:51.463Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WsMjYG3fo6Cdj65mru2mRU`</summary>

```json
{
  "url": "https://ut-austin-rpl.github.io/SCIZOR/",
  "prompt": "Extract all details about SCIZOR's method: how the progress prediction model works, how redundancy detection works, the clustering approach, threshold selection, and any details not in the arxiv paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a566c4aa-2754-4484-b0d4-dde973c1cd43",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNwseh8ds4K9mbW6Cio",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e96fdd0f-c72d-4334-9fc0-0e70046b1c0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012phkrTPbALfeeK7TP3kQCi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 3256,
      "cache_read_input_tokens": 20907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3256,
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

_source line 47 · 2026-05-13T10:04:52.271Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017vQ8HvsP5vgMMXCQNpoHrs`</summary>

```json
{
  "query": "\"advantage weighted regression\" \"behavioral cloning\" imitation learning soft filtering quality scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e96fdd0f-c72d-4334-9fc0-0e70046b1c0d",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNwseh8ds4K9mbW6Cio",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d189469-a1f7-4259-98c9-fe32c9f18580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012phkrTPbALfeeK7TP3kQCi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 3256,
      "cache_read_input_tokens": 20907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3256,
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

_source line 48 · 2026-05-13T10:04:52.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014w4Z8Tx7u5Hnfng962vvNU`</summary>

```json
{
  "query": "CUPID demonstration curation influence functions 2026 robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d189469-a1f7-4259-98c9-fe32c9f18580",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNwseh8ds4K9mbW6Cio",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f855fb5a-c811-4fbf-b5a3-66f051a9ecc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012phkrTPbALfeeK7TP3kQCi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 3256,
      "cache_read_input_tokens": 20907,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3256
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1976,
          "output_tokens": 253,
          "cache_read_input_tokens": 20907,
          "cache_creation_input_tokens": 3256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3256,
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

_source line 49 · 2026-05-13T10:04:56.162Z_

<details><summary>↩ Tool result · `toolu_01WsMjYG3fo6Cdj65mru2mRU`</summary>

```text
# SCIZOR Method Details

## Progress Prediction Model

The framework employs "a self-supervised progress estimator that predicts how much progress a robot makes over short intervals." Transitions exhibiting significantly diminished predicted progress relative to elapsed time are identified as suboptimal and subsequently removed. Notably, this approach operates without requiring reward annotations or manual labeling.

## Redundancy Detection & Clustering

The deduplication process encodes fixed-duration segments into joint visual-action embeddings. The system then applies K-means clustering to group analogous samples. Within resulting clusters, samples demonstrating high similarity scores are pruned to eliminate overrepresented patterns while retaining uncommon variations.

## Key Design Principles

The dual-filter approach targets "two complementary sources of low-quality data: suboptimal data, which hinder learning with undesirable actions, and redundant data, which dilute training with repetitive patterns."

## Limitations in Available Information

The webpage does not specify threshold values for progress prediction, clustering hyperparameters, or other implementation details. For comprehensive technical specifications—including threshold selection methodology, embedding architecture details, or additional ablation studies—consultation of the arxiv paper is necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e96fdd0f-c72d-4334-9fc0-0e70046b1c0d",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "46422bb8-096a-4913-81c1-c2b2c69f26d9",
  "sourceToolAssistantUUID": "e96fdd0f-c72d-4334-9fc0-0e70046b1c0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-13T10:04:59.315Z_

<details><summary>↩ Tool result · `toolu_014w4Z8Tx7u5Hnfng962vvNU`</summary>

```text
Web search results for query: "CUPID demonstration curation influence functions 2026 robot learning"

Links: [{"title":"[2506.19121] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions | OpenReview","url":"https://openreview.net/forum?id=TqevdDMqrK"},{"title":"[2506.19121v2] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121v2"},{"title":"CUPID: Robot Data Curation via Influence Functions","url":"https://www.emergentmind.com/papers/2506.19121"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://proceedings.mlr.press/v305/agia25a.html"},{"title":"[Literature Review] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://www.themoonlight.io/en/review/cupid-curating-data-your-robot-loves-with-influence-functions"}]

Based on the search results, here's what I found about CUPID:

## Overview

CUPID is a robot data curation method based on a novel influence function-theoretic formulation for imitation learning policies.

## Key Concept

Given a set of evaluation rollouts, CUPID estimates the influence of each training demonstration on the policy's expected return, enabling ranking and selection of demonstrations according to their impact on the policy's closed-loop performance.

## Applications

CUPID curates data by 1) filtering out training demonstrations that harm policy performance and 2) subselecting newly collected trajectories that will most improve the policy.

## Results

Training with less than 33% of curated data can yield state-of-the-art diffusion policies on the simulated RoboMimic benchmark, with similar gains observed in hardware. Additionally, hardware experiments show that the method can identify robust strategies under distribution shift, isolate spurious correlations, and even enhance the post-training of generalist robot policies.

## Technical Approach

A demonstration's influence on expected return decomposes into a tractable sum over its state-action transitions and can be efficiently approximated using a REINFORCE-style estimator given a set of policy rollouts.

The CUPID paper was published in 2025 and appears to be part of the recent advances in robot learning and data curation techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f855fb5a-c811-4fbf-b5a3-66f051a9ecc7",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "3d97be0a-27aa-495e-a82f-80650347a6d6",
  "sourceToolAssistantUUID": "f855fb5a-c811-4fbf-b5a3-66f051a9ecc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-13T10:05:00.600Z_

<details><summary>↩ Tool result · `toolu_017vQ8HvsP5vgMMXCQNpoHrs`</summary>

```text
Web search results for query: ""advantage weighted regression" "behavioral cloning" imitation learning soft filtering quality scores"

Links: [{"title":"ADR-BC: Adversarial Density Weighted Regression Behavior Cloning","url":"https://arxiv.org/html/2405.20351v1"},{"title":"Discriminator-Weighted Offline Imitation Learning from ...","url":"https://proceedings.mlr.press/v162/xu22l/xu22l.pdf"},{"title":"VALUE-ALIGNED BEHAVIOR CLONING FOR OFFLINE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/17ab5964d90f38b174a068646c958789-Paper-Conference.pdf"},{"title":"Behavioral Cloning in Imitation Learning","url":"https://www.emergentmind.com/topics/behavioral-cloning-bc"},{"title":"Behavior Cloning (BC)","url":"https://stevengong.co/notes/Behavior-Cloning"},{"title":"10 Imitation Learning","url":"https://web.stanford.edu/class/cs237b/pdfs/lecture/lecture_10111213.pdf"},{"title":"Reward-Aligned Behavior Cloning","url":"https://www.emergentmind.com/topics/reward-aligned-behavior-cloning-ra-bc"},{"title":"Behavioral Cloning (BC) - imitation","url":"https://imitation.readthedocs.io/en/latest/algorithms/bc.html"},{"title":"SelfBC: Self Behavior Cloning for Ofﬂine Reinforcement Learning","url":"https://hajim.rochester.edu/ece/sites/gsharma/papers/LiuSelfBehavCloneRL_ECAI2024.pdf"},{"title":"[2405.20351] Imitating from auxiliary imperfect demonstrations via Adversarial Density Weighted Regression","url":"https://arxiv.org/abs/2405.20351"}]

I've found relevant research on these topics. Here are the key findings:

## Advantage-Weighted Regression and Behavioral Cloning

Advantage-weighted regression (AWR) is used with pairs in imitation learning approaches, and it's referenced as a related method to behavior cloning.

## Quality-Based Weighting and Filtering

Several recent approaches address the problem of handling variable quality data in behavioral cloning:

1. **Density-Weighted Approaches**: A one-step imitation learning algorithm leverages estimated behavior density to optimize the empirical policy using a density-weighted behavior cloning objective. Adversarial Density Weighted Regression (ADR-BC) weights the BC loss at each state-action pair by a ratio of learned densities (expert vs. suboptimal), resulting in a single-step regression that actively avoids suboptimal data regions.

2. **Discriminator-Weighted Approaches**: An approach uses discriminator outputs directly as weights to reduce training time and avoid overestimation issues in estimating value functions offline.

3. **Meta-Learning Scoring Networks**: The Value-aligned Behavior Cloning via Bi-level Optimization (VACO) framework integrates a simple multi-layer perception meta-scoring network to assign differential importance weights to various state-action sample pairs, transforming the conventional BC loss function into a weighted summation of individual sample losses.

## Key Problem Being Addressed

Behavioral cloning lacks the capability to discern between high-quality and low-quality data, which typically results in competitive performance only with expert offline datasets and leads to failure within poor/sub-optimal offline datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d189469-a1f7-4259-98c9-fe32c9f18580",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "4fee8c83-3ef2-420d-a988-8400b93f36be",
  "sourceToolAssistantUUID": "6d189469-a1f7-4259-98c9-fe32c9f18580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-13T10:05:04.293Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018g4C47QAeUbJWC16mkm7iF`</summary>

```json
{
  "url": "https://cupid-curation.github.io/",
  "prompt": "Extract all details about CUPID: method, experimental results with exact numbers, baselines, comparisons to DemInf, and key findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fee8c83-3ef2-420d-a988-8400b93f36be",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNxuCEzfxPQFbWBJgeP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d5d3b69-627d-449f-a1c5-feef1e0ddf24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JEGCi1i1Lz31dvqx8z4a8D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 826,
      "cache_creation_input_tokens": 3400,
      "cache_read_input_tokens": 24163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3400,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 53 · 2026-05-13T10:05:05.820Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013vFNiapNUFmeS8Kxk6VDkJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.19121v1",
  "prompt": "Extract ALL experimental results with exact numbers: RoboMimic task-by-task success rates, all baselines compared, hardware experiment results, and how CUPID compares to DemInf. Also extract failure modes and limitations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d5d3b69-627d-449f-a1c5-feef1e0ddf24",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNxuCEzfxPQFbWBJgeP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74f91a26-0b2a-4032-9fc4-567909a064f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JEGCi1i1Lz31dvqx8z4a8D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 826,
      "cache_creation_input_tokens": 3400,
      "cache_read_input_tokens": 24163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3400,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 54 · 2026-05-13T10:05:07.418Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01T8KDupLyCaGStXBoh7PY32`</summary>

```json
{
  "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/17ab5964d90f38b174a068646c958789-Paper-Conference.pdf",
  "prompt": "Extract all details about VACO (Value-aligned Behavior Cloning via Bi-level Optimization): how it uses a meta-scoring network to assign importance weights to state-action pairs, experimental results, and how it converts BC into weighted learning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74f91a26-0b2a-4032-9fc4-567909a064f3",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNxuCEzfxPQFbWBJgeP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ccdb0671-11cd-4195-a93e-b40e4c4f650d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JEGCi1i1Lz31dvqx8z4a8D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 826,
      "cache_creation_input_tokens": 3400,
      "cache_read_input_tokens": 24163,
      "output_tokens": 374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3400
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 826,
          "output_tokens": 374,
          "cache_read_input_tokens": 24163,
          "cache_creation_input_tokens": 3400,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3400,
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

_source line 55 · 2026-05-13T10:05:09.991Z_

<details><summary>↩ Tool result · `toolu_018g4C47QAeUbJWC16mkm7iF`</summary>

```text
# CUPID: Data Curation for Robot Imitation Learning

## Method Overview

CUPID uses influence functions to estimate how individual training demonstrations affect a policy's closed-loop performance. The approach enables two key capabilities: filtering harmful demonstrations from existing datasets and selecting the most beneficial trajectories from newly collected data.

The method employs a REINFORCE-style estimator to compute performance influence scores, then ranks and selects top-k demonstrations based on their measured impact on policy success.

## Experimental Results

**Simulated Tasks (RoboMimic):**
- Achieved state-of-the-art diffusion policies using less than 33% of curated data
- Demonstration ranking stabilized with approximately 25-50 rollouts on "Lift MH" and "Square MH" tasks
- Required 50-100 rollouts on "Transport MH"

**Hardware Experiments (Franka Robot):**
- Improved success rates on mixed-quality datasets
- Used only 25 policy rollouts for real-world curation
- Successfully identified robust strategies and isolated spurious correlations

## Baseline Comparisons

CUPID was compared against:
- **DemInf**: Performed well in mixed-quality settings but degraded performance when high-quality demonstrations induced brittle test-time strategies
- **Demo-SCORE**: Another curation baseline evaluated across tasks
- **CUPID-Quality**: A quality-based variant that underperformed on tasks where quality wasn't the primary performance factor

## Key Findings

- Performance-based curation (CUPID) maintained robustness across diverse task settings where quality-based measures failed
- Data curated for single-task policies improved Vision-Language-Action (VLA) model post-training
- CUPID identified demonstrations causing distribution shifts and identified brittle strategies that harmed generalization
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d5d3b69-627d-449f-a1c5-feef1e0ddf24",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "0fa911a2-a2b0-4c7a-ae16-ae28a332a3af",
  "sourceToolAssistantUUID": "8d5d3b69-627d-449f-a1c5-feef1e0ddf24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-13T10:05:14.027Z_

<details><summary>↩ Tool result · `toolu_01T8KDupLyCaGStXBoh7PY32`</summary>

```text
I appreciate your request, but I must be honest: the content provided appears to be raw PDF binary data rather than readable text about VACO (Value-aligned Behavior Cloning via Bi-level Optimization).

The document shows PDF stream objects with compressed/encoded content that hasn't been properly extracted into human-readable format. The garbled text includes PDF metadata, compression filters, and binary information rather than actual article content discussing VACO's methodology.

To help you effectively, I would need:

1. **Properly extracted text** from the PDF (using tools like pdftotext or similar)
2. **Direct access** to the research paper or article discussing VACO
3. **Readable passages** describing the meta-scoring network, weighting mechanism, and experimental results

**What I can tell you generally about VACO-type approaches:**

Behavior cloning with importance weighting typically involves assigning higher weights to state-action pairs deemed more valuable, often through auxiliary networks that predict relevance scores. This converts standard BC into a weighted supervised learning problem.

**Could you provide:**
- The actual text content from the document?
- A link to the research paper?
- Specific passages you'd like analyzed?

This would allow me to extract the precise details about VACO's meta-scoring network, experimental findings, and technical methodology while respecting your 125-character quote limit and attribution requirements.

[Binary content (application/pdf, 5.4MB) also saved to /home/ubuntu/.claude-account-2/projects/-/b77d0efd-01f4-43f8-a3fe-0f8c4682d142/tool-results/webfetch-1778666709154-l5t52f.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccdb0671-11cd-4195-a93e-b40e4c4f650d",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "441c0f40-33e1-445c-b1e5-74eb333ffd97",
  "sourceToolAssistantUUID": "ccdb0671-11cd-4195-a93e-b40e4c4f650d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-13T10:05:17.162Z_

<details><summary>↩ Tool result · `toolu_013vFNiapNUFmeS8Kxk6VDkJ`</summary>

```text
# CUPID Experimental Results Summary

## RoboMimic Benchmark Results

### Mixed-Quality Setting (Figure 3)
The paper evaluates three tasks with ground-truth quality labels:

**Lift Task**: Cupid achieves comparable or superior performance to DemInf despite selecting demonstrations rated lower in quality. The baseline prioritizes "high-quality" examples, yet Cupid's selections prove more effective for downstream policy success.

**Square Task**: Similar pattern emerges where Cupid-matched or exceeded DemInf performance while curating lower-perceived-quality data.

**Transport Task (Most Complex)**: The authors note that "Cupid-Quality...achieving an even higher success rate than the official diffusion policy while using fewer than (i) 33% of the original 300 demonstrations and (ii) 10% of the model parameters."

Success rates aren't provided with exact numbers in the main text, but Figure 3 shows qualitative performance trends across filtering and selection tasks at varying k values.

## Hardware Experiments (Franka FR3 Robot)

### Figure-8 Task (Mixed-Quality)
- "Cupid improves over the base policy's success rate by 38% (averaged over filtering and selection)"
- Cupid-Quality further strengthened performance

### TuckBox Task (Distribution Shift Robustness)
- Base policy: 0% success under distribution shift
- Cupid performance: "84%-88% success rate" compared to Oracle
- Baselines (DemInf, Cupid-Quality) failed to identify robust strategies

### Bookshelf Task (Spurious Correlation Disentanglement)
- Base policy: 44% success rate
- Cupid achieved: 84% success rate
- Baselines misidentified spurious correlations as causal factors

## Baseline Comparisons

The study compared Cupid against:
- **DemInf**: Offline mutual-information-based curation
- **Demo-SCORE**: Binary classifier distinguishing successful/failed states
- **Success Similarity**: Custom state-similarity heuristic
- **Random Selection**: Uniform random baseline
- **Oracle**: Privileged access to ground-truth labels

Key finding: "Cupid consistently match[es] or outperform[s] those of DemInf" despite DemInf curating "datasets of the highest overall quality."

## Limitations and Failure Modes

### Data Efficiency Limitations
The method requires policy rollout evaluation. The authors note variance challenges, stating: "as we reduce the number of rollouts m to evaluate the policy—akin to the high variance problem of the REINFORCE algorithm."

### Task-Dependent Effectiveness
- **Square MH Task**: "removing almost any demonstration degrades performance" indicating limited curation benefit when all data proves valuable
- **Lift MH Task**: Only approximately 15% of demonstrations were necessary, suggesting extreme redundancy in some datasets

### Quality Metric Trade-offs
The integration of quality metrics (Cupid-Quality) helps in mixed-quality settings but "degrade[s] performance in other settings" where quality doesn't correlate with performance.

### Methodological Assumptions
Proposition 1 requires "Hessian of BC objective...is positive definite," potentially limiting applicability if optimization reaches saddle points rather than minima.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74f91a26-0b2a-4032-9fc4-567909a064f3",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "163cbb28-cf34-4a7f-bc64-fffb8f3acc15",
  "sourceToolAssistantUUID": "74f91a26-0b2a-4032-9fc4-567909a064f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-13T10:05:20.480Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019e6yuAyxYrNxYFj85ben9E`</summary>

```json
{
  "url": "https://arxiv.org/html/2405.20351v1",
  "prompt": "Extract details about ADR-BC (Adversarial Density Weighted Regression Behavior Cloning): how it weights BC loss using density ratios, how it handles suboptimal demonstrations, and experimental results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "163cbb28-cf34-4a7f-bc64-fffb8f3acc15",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNz7xyD8U2awvpCTtiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "750b4694-829a-449e-89b7-2f8132e47ee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWxxh6BBvtKPYmqTp5LQyb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 418,
      "cache_creation_input_tokens": 2416,
      "cache_read_input_tokens": 27563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2416,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 59 · 2026-05-13T10:05:21.434Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011TR22pjQ7U2N3oq1j3WQBU`</summary>

```json
{
  "query": "DataMIL datamodels robot imitation learning data selection results baselines 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "750b4694-829a-449e-89b7-2f8132e47ee0",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazNz7xyD8U2awvpCTtiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "679a0278-de22-4851-b881-ae30b53e67d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWxxh6BBvtKPYmqTp5LQyb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 418,
      "cache_creation_input_tokens": 2416,
      "cache_read_input_tokens": 27563,
      "output_tokens": 182,
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
          "input_tokens": 418,
          "output_tokens": 182,
          "cache_read_input_tokens": 27563,
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

### Tool result

_source line 60 · 2026-05-13T10:05:27.270Z_

<details><summary>↩ Tool result · `toolu_019e6yuAyxYrNxYFj85ben9E`</summary>

```text
# ADR-BC: Adversarial Density Weighted Regression Behavior Cloning

## Core Mechanism

ADR-BC enhances behavior cloning by weighting the loss using density ratios. The method introduces a **density weight** defined as:

λ(P̂,P*) = log[P̂(a|s)/P*(a|s)]

This weight scales the regression loss, emphasizing state-action pairs where the expert density exceeds suboptimal density. As the paper states, the objective is "matching expert distribution while diverging the sub-optimal distribution."

## Handling Suboptimal Data

The approach uses two VAEs to separately estimate expert and suboptimal behavior densities. Through **Adversarial Density Estimation (ADE)**, the expert density estimator is trained to maximize likelihood on expert samples while minimizing it on suboptimal ones. This leverages suboptimal demonstrations as negative samples to improve expert density estimation robustness.

The suboptimal VAE requires simpler training—the paper notes that "λ₂=0 is sufficient to obtain good performance," meaning adversarial training isn't necessary for non-expert data.

## Key Advantages

- **Single-step optimization**: Avoids cumulative bias from multi-step RL frameworks
- **Computational efficiency**: O(bm) complexity versus O(2(b+1)·bm) for KL divergence methods

## Experimental Results

| Domain | Performance |
|--------|-------------|
| **Gym-Mujoco** | 1008.6 total score; 10.5% improvement over prior SOTA (CEIL) |
| **Kitchen+Adroit** | 526.6 combined score; 89.5% improvement over IQL with ground-truth rewards |

The method demonstrates particular strength in long-horizon tasks, suggesting the density-weighted approach effectively handles distribution shift despite limited demonstrations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "750b4694-829a-449e-89b7-2f8132e47ee0",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "50ca0e87-8772-458c-8e52-b0f38f1589a2",
  "sourceToolAssistantUUID": "750b4694-829a-449e-89b7-2f8132e47ee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-13T10:05:30.521Z_

<details><summary>↩ Tool result · `toolu_011TR22pjQ7U2N3oq1j3WQBU`</summary>

```text
Web search results for query: "DataMIL datamodels robot imitation learning data selection results baselines 2025"

Links: [{"title":"[2505.09603] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/abs/2505.09603"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://robin-lab.cs.utexas.edu/datamodels4imitation/"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with ...","url":"https://arxiv.org/pdf/2505.09603"},{"title":"DataMIL : Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/html/2505.09603"},{"title":"GitHub - UT-Austin-RobIn/datamil: Code release for -- DataMIL: Selecting Data for Robot Imitation Learning with Datamodels · GitHub","url":"https://github.com/UT-Austin-RobIn/datamil"},{"title":"DATAMIL: SELECTING DATA FOR ROBOT IMITATION ...","url":"https://openreview.net/pdf/82e6c304571ad1e85b44780f29e82e7042b2743f.pdf"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels | OpenReview","url":"https://openreview.net/forum?id=AcTsKglDdh"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://openreview.net/pdf/d1836285b655f13b1f86918922a074b725fa137b.pdf"},{"title":"[Literature Review] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://www.themoonlight.io/en/review/datamil-selecting-data-for-robot-imitation-learning-with-datamodels"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

Based on the web search results, here's what I found about DataMIL:

## Overview

DataMIL is a policy-driven data selection framework built on the datamodels paradigm that reasons about data selection in an end-to-end manner, using the policy itself to identify which data points will most improve performance. Unlike standard practices that filter data using human notions of quality (e.g., based on semantic or visual similarity), DataMIL directly optimizes data selection for task success, allowing us to select data that enhance the policy while dropping data that degrade it.

## Key Technical Approach

To avoid performing expensive rollouts in the environment during selection, DataMIL uses a novel surrogate loss function on task-specific data, allowing it to be used in the real world without degrading performance.

## Results and Validation

The approach was validated on a suite of more than 60 simulation and real-world manipulation tasks - most notably showing successful data selection from the Open X-Embodiment datasets-demonstrating consistent gains in success rates and superior performance over multiple baselines.

## Performance on Specific Benchmarks

- **MetaWorld**: Across 50 tasks in MetaWorld, DataMIL shows a 10% performance boost compared to the state-of-the-art baselines.

- **Open X-Embodiment (OXE)**: Data selected using DataMIL achieves the highest performance across all tasks, highlighting the need for end-end policy-aware data selection techniques.

- **LIBERO**: DataMIL consistently performs well across all tasks, achieving the highest average performance overall.

## Baselines Compared

Similarity-based baselines perform poorly: state-only retrieval (SR) fails to reject poor actions, action-only retrieval (AR) selects irrelevant tasks with similar action distributions, and state-action retrieval (BR) gives equal weight to both modalities, which may not be the appropriate recipe for all tasks.

The paper was published on arXiv on May 14, 2025 (arXiv:2505.09603).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "679a0278-de22-4851-b881-ae30b53e67d3",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "092a8557-69b8-4117-96a6-dcaa5929747b",
  "sourceToolAssistantUUID": "679a0278-de22-4851-b881-ae30b53e67d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-13T10:05:33.933Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X5FEPtWornccdVeGZnSMhd`</summary>

```json
{
  "url": "https://robin-lab.cs.utexas.edu/datamodels4imitation/",
  "prompt": "Extract all details about DataMIL: method description, how datamodels work for data selection, experimental results with exact numbers across all benchmarks, baselines compared, and key findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "092a8557-69b8-4117-96a6-dcaa5929747b",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazP16vVQsgBPAVdswEdN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d10211d-c85f-47d6-aebd-af20693da7b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8GwvqahUa2QsTwiN44e7y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2179,
      "cache_read_input_tokens": 29979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 63 · 2026-05-13T10:05:34.753Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RGdx6nqmvPnu8W7giFY87S`</summary>

```json
{
  "query": "ICRA 2026 \"Beyond the Expert\" mixed-skill demonstrations imitation learning FocasLab"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d10211d-c85f-47d6-aebd-af20693da7b6",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazP16vVQsgBPAVdswEdN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "075b14cf-10f6-43e2-9347-5ad442844df0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8GwvqahUa2QsTwiN44e7y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2179,
      "cache_read_input_tokens": 29979,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2179
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 29979,
          "cache_creation_input_tokens": 2179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2179,
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

_source line 64 · 2026-05-13T10:05:40.172Z_

<details><summary>↩ Tool result · `toolu_01RGdx6nqmvPnu8W7giFY87S`</summary>

```text
Web search results for query: "ICRA 2026 "Beyond the Expert" mixed-skill demonstrations imitation learning FocasLab"

Links: [{"title":"GitHub - FocasLab/ICRA-IL-2026: Beyond the Expert: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning · GitHub","url":"https://github.com/FocasLab/ICRA-IL-2026"},{"title":"GitHub - amathislab/Kinesis: [ICRA 2026] The official implementation of the paper \"Reinforcement Learning-Based Motion Imitation for Physiologically Plausible Musculoskeletal Motor Control\" · GitHub","url":"https://github.com/amathislab/Kinesis"},{"title":"Competitions - IEEE ICRA 2026","url":"https://2026.ieee-icra.org/program/competitions/"},{"title":"Contributions | Future Roadmap for Manipulation Skills","url":"https://icra-manipulation-skill.github.io/contributions/"},{"title":"Interactive Perception and Robot Learning Lab - Publications","url":"https://iprl.stanford.edu/publications"},{"title":"ICRA 2026 Beyond Teleoperation Workshop","url":"https://icra-beyond-teleop.github.io/"},{"title":"2025 IEEE International Conference on Robotics ... - ICRA 2026","url":"https://2025.ieee-icra.org/"},{"title":"Dinesh Jayaraman","url":"https://www.seas.upenn.edu/~dineshj/bibbase/"},{"title":"IROSA: Interactive Robot Skill Adaptation using Natural Language","url":"https://arxiv.org/html/2603.03897"},{"title":"Publications","url":"https://core-robotics.gatech.edu/publications/"}]

Based on the search results, I found relevant information about your query:

The project "Beyond the Expert: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning" is associated with FocasLab at ICRA 2026. The repository contains the code, datasets, experiments, and evaluations for the proposed method.

The key components of this work include:
- A core Jupyter notebook for demo utility scoring and demo cleaning pipeline
- Implementation of the Pick-and-Place task, including datasets, models, and scoring notebooks (evaluation scripts)
- Demo Utility Scoring – Quantitative evaluation of dataset usefulness for model training

The GitHub repository for this project is available at: https://github.com/FocasLab/ICRA-IL-2026

This work appears to focus on leveraging demonstrations from demonstrators of varying skill levels for imitation learning, rather than relying solely on expert demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "075b14cf-10f6-43e2-9347-5ad442844df0",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "154dba0b-6c2b-4262-b788-c8b1a07af0d8",
  "sourceToolAssistantUUID": "075b14cf-10f6-43e2-9347-5ad442844df0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-13T10:05:41.470Z_

<details><summary>↩ Tool result · `toolu_01X5FEPtWornccdVeGZnSMhd`</summary>

```text
# DataMIL: Data Selection for Robot Imitation Learning

## Method Overview

DataMIL adapts datamodels—a framework for measuring how training samples influence model outputs—to robotics imitation learning. The system performs two-stage data selection: first estimating datamodels with influence scores for each sample, then selecting top-performing samples for policy training.

## How Datamodels Enable Data Selection

Datamodels answer the question: "how would the output of a model change if we had trained on a different dataset?" Rather than retraining, they assign influence scores to samples. DataMIL implements this through "regression and metagradient-based datamodels" without requiring costly full rollouts.

## Three Key Technical Modifications

1. **Proxy Metric**: Uses validation loss on target task demonstrations instead of expensive rollouts
2. **Clustering**: Applies temporal clustering to reduce estimation noise in trajectories
3. **Co-training**: Minimizes distribution shift by training jointly with target task data

## Experimental Results

The authors evaluated DataMIL across "60+ simulation and real world tasks" using Open X-Embodiment datasets. Key findings include:

- **Novel embodiments**: Successfully selected data for Tiago robot (not in prior datasets) by identifying relevant samples from Google Robot and WidowX data
- **Multitask performance**: Extended evaluation showed effectiveness across multiple target tasks simultaneously
- **Consistent improvements**: Outperformed existing dataset selection baselines across diverse task characteristics

## Baselines Compared

- Action Retrieval
- Behavior Retrieval
- Flow Retrieval
- Similarity-based methods

## Notable Insights

1. Selected data spans multiple datasets rather than concentrating on single sources, preventing overfitting
2. DataMIL identifies correct embodiments when available in prior data
3. Top-ranked and lowest-ranked samples appear visually similar, suggesting useful and harmful data share common characteristics—aligning with computer vision observations
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d10211d-c85f-47d6-aebd-af20693da7b6",
  "isSidechain": true,
  "promptId": "589b8077-6001-4cc4-b3e0-8c25e8a1e296",
  "agentId": "a6aedbc70f4ed94ec",
  "type": "user",
  "uuid": "159e7a09-6633-492a-a0ad-fa2682beb6f3",
  "sourceToolAssistantUUID": "9d10211d-c85f-47d6-aebd-af20693da7b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-13T10:07:28.089Z_

Now I have comprehensive information. Let me compile the detailed findings.

---

## Detailed Research Report: Demonstration Curation Methods for Robot Learning (2025-2026)

---

### 1. SCIZOR (ICRA 2026) -- "A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning"

**Authors:** Yu Zhang, Yuqi Xie, Huihan Liu, Rutav Shah, Michael Wan, Linxi Fan, Yuke Zhu (UT Austin RPL / NVIDIA)

**Method in Detail:**

SCIZOR targets two complementary sources of low-quality data with a dual-filter pipeline:

**(A) Suboptimal Data Removal** -- A self-supervised progress estimator predicts how much task progress the robot makes over short time intervals. Transitions exhibiting significantly diminished predicted progress relative to elapsed time are flagged as suboptimal and removed. This operates without reward annotations or manual labels -- purely self-supervised from the demonstration data itself.

**(B) Redundancy/Deduplication** -- Fixed-duration segments are encoded into joint visual-action embeddings. K-means clustering groups analogous samples. Within clusters, samples with high similarity scores are pruned to eliminate overrepresented patterns while retaining uncommon variations.

Unified thresholds are used: epsilon_s = 0.58 (suboptimal), epsilon_d = 0.99 (deduplication).

**Sirius-Fleet Results (Real Robot, detailed task-by-task):**

| Task | No Deletion | Suboptimal Only | Dedup Only | DemInf | SCIZOR |
|------|------------|-----------------|-----------|--------|--------|
| Book->Caddy | 40.0% | 65.0% | 45.0% | 66.7% | **66.7%** |
| Cup->Caddy | 65.0% | 75.0% | 75.0% | 53.3% | **73.3%** |
| Bowl->Plate | 65.0% | 70.0% | 80.0% | 60.0% | **93.3%** |
| Mug->Plate | 35.0% | 60.0% | 70.0% | 50.0% | **83.3%** |
| Mug->Basket | 35.0% | 35.0% | 65.0% | 50.0% | **66.7%** |
| Bowl->Basket | 60.0% | 90.0% | 70.0% | 76.7% | **96.7%** |
| Mug->Tray | 35.0% | 50.0% | 60.0% | 53.3% | **66.7%** |
| Bread->Plate | 50.0% | 60.0% | 60.0% | 63.3% | **90.0%** |

Average absolute gain on Sirius-Fleet: **+32.9%** over no deletion. SCIZOR outperformed DemInf by **19.2%** on this benchmark.

**RoboMimic Results:**

| Method | Can | Square |
|--------|-----|--------|
| Suboptimal Only | 84.0% | 37.8% |
| Dedup Only | 74.3% | 22.4% |
| Random Deletion | 78.0% | 32.2% |
| DemInf | 88.9% | 41.4% |
| SCIZOR | 87.3% +/- 0.7 | 37.2% +/- 2.5 |

Average RoboMimic gain: +5.4%. Note: DemInf actually beats SCIZOR on RoboMimic (88.9% vs 87.3% on Can; 41.4% vs 37.2% on Square).

**OXEMagic Results:**

| Method | Pick Can | Move Near |
|--------|----------|-----------|
| No Deletion | 27.0% | 13.1% |
| Suboptimal Only | 33.7% | 16.9% |
| Dedup Only | 31.8% | 12.3% |
| SCIZOR | 39.5% | 16.7% |
| ReMix | 40.5% | 15.0% |
| SCIZOR (OXERT-X) | 43.3% | 19.2% |

SCIZOR outperformed ReMix by 3.5% on average.

**Ablation (averaged across benchmarks):**

| Component | RoboMimic | Sirius-Fleet | OXEMagic |
|-----------|-----------|--------------|----------|
| Suboptimal Only | 60.9 +/- 1.8 | 64.2 +/- 2.6 | 25.3 +/- 2.9 |
| Dedup Only | 48.3 +/- 0.8 | 63.3 +/- 6.9 | 22.1 +/- 0.9 |
| Full SCIZOR | 62.3 +/- 1.6 | 79.6 +/- 1.4 | 28.1 +/- 3.3 |

Suboptimal removal contributes more than deduplication, but both together are best.

**Data Filtering Rates:**
- RoboMimic: 29.6% total removed (29.3% suboptimal, 0.3% dedup)
- Sirius-Fleet: 7.9% total (4.7% suboptimal, 3.2% dedup)
- OXEMagic: 15.8% total (11.9% suboptimal, 4.5% dedup)

**Baselines:** No Deletion, Suboptimal Only, Dedup Only, Random Deletion, DemInf, ReMix

---

### 2. DemInf (RSS 2025) -- "Robot Data Curation with Mutual Information Estimators"

**Authors:** Joey Hejna, Suvir Mirchandani, Ashwin Balakrishna, Annie Xie, Ayzaan Wahid, Jonathan Tompson, Pannag Sanketi, Dhruv Shah, Coline Devin, Dorsa Sadigh (Google DeepMind / Stanford)

**Method in Detail:**

DemInf estimates the mutual information I(S;A) between states and actions across the dataset using k-nearest neighbor (KSG) estimators. Separate VAEs embed states and actions into low-dimensional representations. The per-sample MI contribution is:

I_hat(s_i, a_i; D_N) is proportional to -psi(n(z_s,i)+1) - psi(n(z_a,i)+1)

where psi is the digamma function and n(z) counts k-nearest neighbors in the respective marginal spaces.

Trajectory-level scoring: S(tau) = (1/T) * sum_{t=1}^{T} I_hat(s_t, a_t; D_N)

Critically, filtering is done at the trajectory level (not timestep level) because task-critical phases like grasping inherently exhibit low MI -- filtering at the timestep level would discard these essential segments.

**RoboMimic Results:**
- Tasks evaluated: Lift, Can, Square (multi-human variants, both state and image inputs)
- Overall: 5-10% improvement over training on all data
- Can task: Over 10% improvement; "the only method to improve upon training on all data in Square"
- Image-based: DemInf surpasses all methods on both RoboMimic tasks
- State-based: Matches or exceeds all baselines

**Real Robot Results:**
- ALOHA (RoboCrowd): Tasks -- HiChew, TootsieRoll, HersheyKiss candy bin-picking (40-100 demos per task, ACT policy). DemInf-filtered policies more commonly complete tasks successfully.
- Franka Panda: PenInCup, DishRack tasks (60-80 demos, 50% expert / 50% intentionally poor, Diffusion Policy). DemInf always outperforms random subset. However: "Training on all data does slightly better than filtering with DemInf on PenInCup" -- suggesting that harder tasks requiring more training data may not benefit from aggressive filtering.

**Baselines:** Uncertainty (ensemble of 5 policies), Compatibility (Gandhi et al.), VIP (Value Implicit Pre-training), InfoNCE (MI), MINE (MI). InfoNCE and MINE perform acceptably in state-based settings but "perform significantly worse in image-based settings as dimensionality increases."

**Failure Modes (explicitly discussed by authors):**

1. **Action entropy over-indexing** -- May over-index on H(A|S) since action entropy directly determines state entropy temporally in sequential settings
2. **State entropy outliers** -- Could prefer outlier trajectories visiting new state space regions if actions remain consistent
3. **Pauses/predictable inaction** -- Susceptible to preferring predictable but non-progressive data (e.g., extended pauses)
4. **Greedy procedure** -- Curation is greedy and not globally optimal; removing an episode changes the data distribution for subsequent decisions

**Ablations:**
- k-NN parameter: Robust across tested values, no substantial change
- KSG estimator superior to BiKSG and naive differential entropy
- DemInf exhibits far lower variance across seeds compared to InfoNCE and MINE

---

### 3. New Demonstration Curation Papers (Jan-May 2026)

**(A) QoQ -- "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning" (arXiv March 2026, arXiv:2603.09056)**

Uses influence functions with two key innovations: (1) maximum influence scoring across validation samples (not averaging), and (2) trajectory-wise aggregation to reduce noise. Results: 99.2% success on RoboMimic Can-placement (vs 76% for best baseline); 86.7% on real banana grasping (vs 56.7% for Behavior Retrieval); 93.3% on multi-object pick-and-place. Kendall's W consistency: 0.7713 (highest among methods).

**(B) CUPID -- "Curating Data your Robot Loves with Influence Functions" (CoRL 2025, arXiv:2506.19121)**

Uses REINFORCE-style influence function estimator requiring policy rollouts. Key result: state-of-the-art diffusion policies using less than 33% of curated data on RoboMimic. Hardware results on Franka: +38% success rate averaged across tasks; 84-88% success on TuckBox task where DemInf failed (0% under distribution shift). Baselines: DemInf, Demo-SCORE, Random, Oracle.

**(C) Demo-SCORE -- "Curating Demonstrations using Online Experience" (arXiv March 2025, arXiv:2503.03707)**

Four-step self-curation: train initial policy, collect rollouts at multiple checkpoints, train classifiers to distinguish success/failure, filter demonstrations. Achieves 15-35% absolute improvement. Requires rollout access but only ~100 rollouts total. Limitations: struggles when all demonstrations are low-quality; may reduce state coverage.

**(D) DataMIL -- "Selecting Data for Robot Imitation Learning with Datamodels" (arXiv May 2025, arXiv:2505.09603, from UT Austin RobIn lab)**

Uses datamodels framework to estimate how each training sample influences policy output. Novel surrogate loss avoids expensive rollouts. Validated on 60+ simulation and real tasks including Open X-Embodiment. 10% performance boost over SOTA on MetaWorld (50 tasks). Works for novel embodiments not in training data (e.g., selecting data for Tiago robot from Google Robot and WidowX datasets).

**(E) RINSE -- "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning" (arXiv April 2026, arXiv:2604.23000)**

Lightweight, training-free approach using two metrics: Spectral Arc Length (SAL, O(T log T)) for frequency-domain smoothness and Trajectory-Envelope Distance (TED) for spatial geometric deviation. RoboMimic Transport: 16% higher success using 1/6 of data; 10x convergence speedup. Critically, this paper also explores using quality scores as exponential weights: w(tau) = exp(-lambda * q(tau)) for soft weighting in ReMix-style domain reweighting.

**(F) ReMix -- "Optimizing Data Mixtures for Large Scale Imitation Learning" (2025)**

Uses distributionally robust optimization (DRO) to learn data mixture weights maximizing worst-case performance across downstream domains. 40% improvement over uniform weighting, 20% over human-selected weights on RT-X datasets.

**(G) "Beyond the Expert: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning" (ICRA 2026, FocasLab)**

Focuses on leveraging demonstrations from varying skill levels with a demo utility scoring pipeline. GitHub: https://github.com/FocasLab/ICRA-IL-2026

---

### 4. Importance-Weighted / Soft Filtering in Behavioral Cloning

Yes, using quality scores as sample weights (soft filtering rather than hard thresholding) has been explored through several lines of work:

**(A) Density-Ratio Weighted BC (arXiv:2510.01479)** -- Uses a small clean reference set to train a binary discriminator. Density ratios r(tau) = d(tau)/(1-d(tau)) are clipped to [epsilon, C] and used as BC loss weights. Maintains 80%+ performance retention up to 60% data contamination. Only 1.04x computational overhead vs standard BC. Tested on D4RL (HalfCheetah, Ant, Walker2d, Hopper) with four contamination types (reward, state, transition, action poisoning).

**(B) ADR-BC -- Adversarial Density Weighted Regression BC (arXiv:2405.20351)** -- Weights BC loss by lambda = log[P_hat(a|s) / P*(a|s)] using two VAEs for expert vs. suboptimal density estimation. Adversarial training uses suboptimal demos as negative samples. 10.5% improvement over prior SOTA on Gym-MuJoCo; 89.5% improvement over IQL on Kitchen+Adroit.

**(C) DWBC -- Discriminator-Weighted Offline Imitation Learning (ICML 2022, Xu et al.)** -- Uses discriminator outputs directly as per-sample weights in the BC loss, avoiding value function estimation entirely.

**(D) VACO -- Value-Aligned Behavior Cloning via Bi-level Optimization (ICLR 2025)** -- Integrates a meta-scoring MLP network trained via bi-level optimization to assign importance weights to individual state-action pairs, transforming standard BC into a weighted sum of sample losses. The meta-network learns weights that align with downstream value.

**(E) RINSE's exponential weighting** -- As mentioned above, RINSE (2026) explicitly uses smoothness-based quality scores as exponential weights w(tau) = exp(-lambda * q(tau)) in domain reweighting frameworks, demonstrating Spearman rho >= 0.89 correlation with learned ReMix allocations.

**(F) IQL / Advantage-Weighted Regression** -- Implicit Q-Learning extracts policies through advantage-weighted behavioral cloning, which is soft filtering in value-function space. This is the most well-known instance of the idea in offline RL.

**Key takeaway on soft vs. hard filtering:** Hard filtering (DemInf, SCIZOR, CUPID) is dominant in the robotics curation literature as of 2026. Soft weighting approaches exist but are more common in the offline RL literature (D4RL benchmarks). RINSE is a notable bridge -- it proposes quality metrics that can be used either for hard filtering or as soft weights. The density-ratio weighted BC paper explicitly shows that soft weighting via density ratios is more robust than hard filtering at high contamination levels, since hard thresholds discard borderline-useful data.

---

Sources:
- [SCIZOR paper (arXiv)](https://arxiv.org/abs/2505.22626)
- [SCIZOR HTML](https://arxiv.org/html/2505.22626v2)
- [SCIZOR project page](https://ut-austin-rpl.github.io/SCIZOR/)
- [DemInf paper (arXiv)](https://arxiv.org/abs/2502.08623)
- [DemInf HTML](https://arxiv.org/html/2502.08623v2)
- [DemInf at RSS](https://roboticsconference.org/program/papers/23/)
- [QoQ paper (arXiv)](https://arxiv.org/abs/2603.09056)
- [CUPID paper (arXiv)](https://arxiv.org/abs/2506.19121)
- [CUPID project page](https://cupid-curation.github.io/)
- [Demo-SCORE (arXiv)](https://arxiv.org/html/2503.03707)
- [DataMIL (arXiv)](https://arxiv.org/abs/2505.09603)
- [DataMIL project page](https://robin-lab.cs.utexas.edu/datamodels4imitation/)
- [RINSE (arXiv)](https://arxiv.org/html/2604.23000)
- [ReMix (OpenReview)](https://openreview.net/forum?id=fIj88Tn3fc)
- [Density-Ratio Weighted BC](https://arxiv.org/html/2510.01479)
- [ADR-BC](https://arxiv.org/html/2405.20351v1)
- [DWBC (ICML 2022)](https://proceedings.mlr.press/v162/xu22l/xu22l.pdf)
- [VACO (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/17ab5964d90f38b174a068646c958789-Paper-Conference.pdf)
- [Beyond the Expert (ICRA 2026)](https://github.com/FocasLab/ICRA-IL-2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "159e7a09-6633-492a-a0ad-fa2682beb6f3",
  "isSidechain": true,
  "agentId": "a6aedbc70f4ed94ec",
  "requestId": "req_011CazP1umJnaJqEeqJZLb4i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0397ec1f-974e-4248-bee6-fa5fd442f924",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b77d0efd-01f4-43f8-a3fe-0f8c4682d142",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017r8QXRww422GHzooYopF3b",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 686,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 32158,
      "output_tokens": 4604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 651
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 686,
          "output_tokens": 4604,
          "cache_read_input_tokens": 32158,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 651,
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
