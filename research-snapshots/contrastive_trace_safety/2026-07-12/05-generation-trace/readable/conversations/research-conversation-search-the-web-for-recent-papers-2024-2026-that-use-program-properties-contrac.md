# Research conversation: Search the web for recent papers (2024-2026) that use program properties, contracts, specifications, or formal constrain

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 83
- **Recorded user turns:** 1
- **Tool calls:** 36
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a082fc3bdac9c393e.jsonl`
- **Structured JSON:** [`2380ba9b57d6313c2268.json`](../../sessions/23/2380ba9b57d6313c2268.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

83 recorded events

### User

_source line 1 · 2026-05-12T01:17:35.315Z_

Search the web for recent papers (2024-2026) that use program properties, contracts, specifications, or formal constraints (NOT just test cases) to improve LLM code generation or repair at inference time. I need to find work that ExeSpec (a method using execution-grounded behavioral specifications like preconditions, postconditions, invariants) might be competing with.

Search queries to try:
1. "property-based testing LLM code generation 2025 2026"
2. "preconditions postconditions LLM code generation"
3. "From Prompts to Properties rethinking LLM code generation FSE 2025"
4. "ContractEval PACT LLM contract satisfaction arXiv 2510.12047"
5. "specification guided code generation LLM 2025 2026"
6. "StoryCoder arXiv 2604.14631"
7. "formal specification LLM program repair"
8. "design by contract LLM code"

For each paper found, report: title, venue/year, what it does, and how it relates to using execution-verified behavioral specs for code tasks. Focus on finding the closest competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "df10194f-ab46-44e1-881a-8fcfc2ac282d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T01:17:35.318Z_

```json
{
  "parentUuid": "df10194f-ab46-44e1-881a-8fcfc2ac282d",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
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
  "uuid": "942699d8-a0a5-4870-9844-7e5d4c6b213f",
  "timestamp": "2026-05-12T01:17:35.318Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T01:17:42.888Z_



I'll search for these papers systematically. Let me start by loading the WebSearch tool and then run the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "942699d8-a0a5-4870-9844-7e5d4c6b213f",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwGfoGbV1dYP7YG7rU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8664767b-a16a-409e-8498-4574e37284bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H96CuR834uP95Z29vP868N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 816,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T01:17:43.021Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018L6um8Xkd8dNzv3Z2bDEP3`</summary>

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
  "parentUuid": "8664767b-a16a-409e-8498-4574e37284bd",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwGfoGbV1dYP7YG7rU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4d2ac8e-f5c6-4d4b-b318-42d2c4924a9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H96CuR834uP95Z29vP868N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 8223,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 816
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 816,
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

_source line 5 · 2026-05-12T01:17:43.024Z_

<details><summary>↩ Tool result · `toolu_018L6um8Xkd8dNzv3Z2bDEP3`</summary>

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
  "parentUuid": "b4d2ac8e-f5c6-4d4b-b318-42d2c4924a9e",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "adbf26fa-24d4-4f2f-a90b-a901074ad5a4",
  "sourceToolAssistantUUID": "b4d2ac8e-f5c6-4d4b-b318-42d2c4924a9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T01:17:47.155Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adbf26fa-24d4-4f2f-a90b-a901074ad5a4",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwqvYXEygFznAM3Mnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcf4ddd2-c13b-4d19-81d7-22b62317e9d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS83U9E3pWFSTKWdFNrcQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 7 · 2026-05-12T01:17:48.360Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0176MPTNcNUZoSqbpgMRcJmd`</summary>

```json
{
  "query": "property-based testing LLM code generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcf4ddd2-c13b-4d19-81d7-22b62317e9d5",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwqvYXEygFznAM3Mnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38aaa67e-4dd4-4a9b-a873-7658dcfecc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS83U9E3pWFSTKWdFNrcQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 8 · 2026-05-12T01:17:48.646Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0113uF3kcYtqLGiAdFSVfkKC`</summary>

```json
{
  "query": "preconditions postconditions LLM code generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38aaa67e-4dd4-4a9b-a873-7658dcfecc6b",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwqvYXEygFznAM3Mnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba6f8e54-11ca-430c-bf5f-567fb8751ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS83U9E3pWFSTKWdFNrcQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 9 · 2026-05-12T01:17:49.512Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KEfDWetX74MtGxrvBrq8q2`</summary>

```json
{
  "query": "From Prompts to Properties rethinking LLM code generation FSE 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba6f8e54-11ca-430c-bf5f-567fb8751ae5",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwqvYXEygFznAM3Mnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82bb6727-c79a-4fee-a501-5f0a5a408cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS83U9E3pWFSTKWdFNrcQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 10 · 2026-05-12T01:17:50.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WUEqv7v4aY8o3JcTQPriBU`</summary>

```json
{
  "query": "ContractEval PACT LLM contract satisfaction arXiv 2510.12047"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82bb6727-c79a-4fee-a501-5f0a5a408cb0",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwqvYXEygFznAM3Mnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80feb0f8-01ad-4f42-82ec-f16f9a5b98c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS83U9E3pWFSTKWdFNrcQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 11 · 2026-05-12T01:17:51.106Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PgRae8fxsTMBRmB1LJGXuS`</summary>

```json
{
  "query": "specification guided code generation LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80feb0f8-01ad-4f42-82ec-f16f9a5b98c2",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwqvYXEygFznAM3Mnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25d53597-dab9-40a3-bb64-7a8a122f482f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS83U9E3pWFSTKWdFNrcQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 12 · 2026-05-12T01:17:51.366Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LLaS7j4Bs2mZHyzbLax5hk`</summary>

```json
{
  "query": "StoryCoder arXiv 2604.14631"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25d53597-dab9-40a3-bb64-7a8a122f482f",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwqvYXEygFznAM3Mnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8ef77e2-d344-4338-876c-a092e8873bc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS83U9E3pWFSTKWdFNrcQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 13 · 2026-05-12T01:17:52.307Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GS51MeV4h2A5odnXekPFme`</summary>

```json
{
  "query": "formal specification LLM program repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8ef77e2-d344-4338-876c-a092e8873bc6",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwqvYXEygFznAM3Mnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31ded941-ba4d-402c-b454-1390894fe9ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS83U9E3pWFSTKWdFNrcQc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9039,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1914
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 408,
          "cache_read_input_tokens": 9039,
          "cache_creation_input_tokens": 1914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1914,
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

### Tool call

_source line 14 · 2026-05-12T01:17:52.312Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GEvANApQrGWzsKMUAKSVsk`</summary>

```json
{
  "query": "design by contract LLM code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ded941-ba4d-402c-b454-1390894fe9ba",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnwqvYXEygFznAM3Mnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32241901-fd90-43b5-b513-59e75a730c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DS83U9E3pWFSTKWdFNrcQc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9039,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1914
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 408,
          "cache_read_input_tokens": 9039,
          "cache_creation_input_tokens": 1914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1914,
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

_source line 15 · 2026-05-12T01:17:55.408Z_

<details><summary>↩ Tool result · `toolu_01KEfDWetX74MtGxrvBrq8q2`</summary>

```text
Web search results for query: "From Prompts to Properties rethinking LLM code generation FSE 2025"

Links: [{"title":"From Prompts to Properties: Rethinking LLM Code Generation","url":"https://dl.acm.org/doi/pdf/10.1145/3696630.3728702"},{"title":"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing | Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/3696630.3728702"},{"title":"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing (LLanMER 2025) - LLanMER 2025","url":"https://conf.researchr.org/details/llanmer-2025/llanmer-2025-papers/7/From-Prompts-to-Properties-Rethinking-LLM-Code-Generation-with-Property-Based-Testin"},{"title":"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing","url":"https://vtechworks.lib.vt.edu/items/702015c7-5db2-4dfc-a098-a8333c50faf6"},{"title":"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/html/2605.02455v1"},{"title":"Rethinking the Evaluation of Secure Code Generation Shih-Chieh Dai","url":"https://arxiv.org/pdf/2503.15554"},{"title":"GSCE: A Prompt Framework with Enhanced Reasoning for ...","url":"https://arxiv.org/pdf/2502.12531"},{"title":"NeurIPS Poster Rethinking Verification for LLM Code Generation: From Generation to Testing","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118941"},{"title":"Beginners Struggle to Understand LLM-Generated Code","url":"https://dl.acm.org/doi/pdf/10.1145/3696630.3731663"},{"title":"The Ultimate Guide to Prompt Engineering in 2026 | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/prompt-engineering-guide"}]

I found detailed information about the paper "From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing."

## Summary

The paper "From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing" was presented at the 33rd ACM International Conference on the Foundations of Software Engineering (FSE Companion '25) in June 23–28, 2025, in Trondheim, Norway.

## Key Findings

The research addresses the challenge of ensuring correctness of code generated by Large Language Models (LLMs), noting that traditional unit testing evaluates functional correctness but often fails to capture deeper logical constraints.

The researchers applied Property-Based Testing (PBT) as an alternative evaluation strategy to StarCoder and CodeLlama on MBPP and HumanEval benchmarks. The results revealed that while pass@k evaluation shows moderate success, PBT exposes additional correctness gaps, with a significant portion of generated solutions only partially adhering to correctness properties (30–32%), while 18–23% fail outright.

This work highlights the importance of moving beyond traditional evaluation metrics to more rigorous property-based testing approaches for assessing the reliability of LLM-generated code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82bb6727-c79a-4fee-a501-5f0a5a408cb0",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "f2c046a4-bca3-4f27-aa6a-51878e14150b",
  "sourceToolAssistantUUID": "82bb6727-c79a-4fee-a501-5f0a5a408cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T01:17:55.858Z_

<details><summary>↩ Tool result · `toolu_0176MPTNcNUZoSqbpgMRcJmd`</summary>

```text
Web search results for query: "property-based testing LLM code generation 2025 2026"

Links: [{"title":"From Exploration to Specification: LLM-Based Property Generation for Mobile App Testing","url":"https://arxiv.org/html/2604.13463v1"},{"title":"[2506.18315] Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/abs/2506.18315"},{"title":"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing | Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/3696630.3728702"},{"title":"Rethinking LLM Code Generation with Property-Based ...","url":"https://dl.acm.org/doi/pdf/10.1145/3696630.3728702"},{"title":"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing (LLanMER 2025) - LLanMER 2025","url":"https://conf.researchr.org/details/llanmer-2025/llanmer-2025-papers/7/From-Prompts-to-Properties-Rethinking-LLM-Code-Generation-with-Property-Based-Testin"},{"title":"Enhanced LLM code generation with property-based testing! New Framework PGS to Break Self-Deception | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/llm-paper/property-generated-solver"},{"title":"LLM-Based Property-Based Test Generation for Guardrailing Cyber-Physical Systems | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-032-07132-3_3"},{"title":"Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/html/2506.18315v1"},{"title":"[2510.25297] Understanding the Characteristics of LLM-Generated Property-Based Tests in Exploring Edge Cases","url":"https://arxiv.org/abs/2510.25297"},{"title":"Can Large Language Models Write Good Property-Based Tests? Vasudev Vikram","url":"https://arxiv.org/pdf/2307.04346"}]

Based on the search results, here's what I found about property-based testing and LLM code generation in 2025-2026:

## Recent Research and Frameworks

Property-Generated Solver is a novel framework that leverages Property-Based Testing (PBT) to validate high-level program properties or invariants, instead of relying on specific input-output examples. Property-Generated Solver employs two collaborative LLM-based agents: a Generator dedicated to code generation and iterative refinement, and a Tester that manages the PBT life-cycle and formulate semantically rich feedback from property violations.

Property-Generated Solver achieves substantial pass@1 improvements, ranging from 23.1% to 37.3% relative gains over established TDD methods.

## Key Applications

Several recent studies have explored the use of LLMs in property-related testing tasks. A novel automated approach has been proposed for guardrailing cyber-physical systems using property-based tests (PBTs) generated by Large Language Models (LLMs).

## Recent Findings on LLM-Generated Property-Based Tests

Research investigates the characteristics of LLM-generated Property-based Testing (PBT) compared to Example-based Testing (EBT) for exploring edge cases. Experimental results reveal that while each method individually achieved a 68.75% bug detection rate, combining both approaches improved detection to 81.25%.

The field shows significant progress in using property-based testing to improve the reliability and correctness of LLM-generated code through 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38aaa67e-4dd4-4a9b-a873-7658dcfecc6b",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "7fe288e0-60a8-402a-bda2-456c07c18103",
  "sourceToolAssistantUUID": "38aaa67e-4dd4-4a9b-a873-7658dcfecc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T01:17:56.241Z_

<details><summary>↩ Tool result · `toolu_0113uF3kcYtqLGiAdFSVfkKC`</summary>

```text
Web search results for query: "preconditions postconditions LLM code generation"

Links: [{"title":"Preconditions and Postconditions as Design Constraints for LLM Code Generation | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11218044/"},{"title":"A Study of Preconditions and Postconditions as Design ...","url":"https://commons.erau.edu/cgi/viewcontent.cgi?article=1917&context=edt"},{"title":"Beyond Postconditions: Can Large Language Models infer Formal Contracts for","url":"https://arxiv.org/pdf/2510.12702"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"A Study of Preconditions and Postconditions as Design Constraints for LLM Code Generation","url":"https://commons.erau.edu/edt/927/"},{"title":"Preconditions and Postconditions as Design Constraints ...","url":"https://ieeexplore.ieee.org/iel8/6287639/10820123/11218044.pdf"},{"title":"Automated Generation of Code Contracts – Generative AI to the Rescue?","url":"https://scg.unibe.ch/archive/papers/Grei24a-CodeContracts.pdf"},{"title":"FormalSpecCpp: A Dataset of C++ Formal Specifications created using LLMs","url":"https://arxiv.org/pdf/2502.15217"},{"title":"LLMs as Code Generators for Model-Driven Development Yoonsik Cheon","url":"https://www.scitepress.org/Papers/2025/135803/135803.pdf"},{"title":"Potential Runtime Error-Guided Specification Synthesis for ...","url":"https://www.arxiv.org/pdf/2512.24594"}]

Based on the search results, here's what I found about preconditions and postconditions in LLM code generation:

## Overview

Large Language Models have significantly advanced automated code generation, but current methods predominantly rely on natural language descriptions, and encounter challenges when handling complex, class-level software generation tasks due to inherent ambiguity and under-specification.

## Research on Formal Constraints

Few studies have investigated how formal software engineering constraints, such as explicit preconditions and postconditions as part of the Design-by-Contract paradigm, influence class-level generation tasks. However, recent research is addressing this gap.

## Key Findings

Incorporating explicit design constraints during prompting significantly boosts initial generation accuracy (measured via the pass@k metric), particularly in Python but also in C++. Additionally, models with fewer parameters or weaker initial performance saw especially pronounced benefits.

## Related Approaches

Several methods have been developed to leverage preconditions and postconditions in code generation:

- NL2Contract translates natural-language docstrings into contracts expressed as executable Python assertions, with contract quality evaluated for soundness using CrossHair.

- AutoSpec is a combined approach that synthesizes pre/postconditions and loop invariants using LLMs and verifier feedback.

- Preconditions and postconditions serve as formal specifications that define the expected state of a program before and after code execution, ensuring software correctness, formal verification, and code reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba6f8e54-11ca-430c-bf5f-567fb8751ae5",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "8f8a5f78-d51c-460a-bcf6-ac1d3f07126b",
  "sourceToolAssistantUUID": "ba6f8e54-11ca-430c-bf5f-567fb8751ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T01:17:57.166Z_

<details><summary>↩ Tool result · `toolu_01LLaS7j4Bs2mZHyzbLax5hk`</summary>

```text
Web search results for query: "StoryCoder arXiv 2604.14631"

Links: [{"title":"[2604.14631] StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation","url":"https://arxiv.org/abs/2604.14631"},{"title":"StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation","url":"https://arxiv.org/html/2604.14631"},{"title":"StoryDrawer | Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3491102.3501914"},{"title":"Characterizing LLM-Empowered Personalized Story-Reading and Interaction for Children: Insights from Multi-Stakeholder Perspectives","url":"https://arxiv.org/html/2503.00590v1"},{"title":"(PDF) StoryCoder: Teaching Computational Thinking Concepts Through Storytelling in a Voice-Guided App for Children","url":"https://www.researchgate.net/publication/351418072_StoryCoder_Teaching_Computational_Thinking_Concepts_Through_Storytelling_in_a_Voice-Guided_App_for_Children"},{"title":"storycoder (Joseph Margolis) · GitHub","url":"https://github.com/storycoder"},{"title":"Masked Generative Story Transformer with Character Guidance and Caption Augmentation","url":"https://arxiv.org/html/2403.08502v1"},{"title":"MindScratch: A Visual Programming Support Tool for Classroom Learning Based on Multimodal Generative AI","url":"https://arxiv.org/html/2412.09001v1"},{"title":"[2404.05979] StoryImager: A Unified and Efficient Framework for Coherent Story Visualization and Completion","url":"https://arxiv.org/abs/2404.05979"},{"title":"arXiv:2505.14631v2 [cs.CL] 21 May 2025 Think Only When You Need","url":"https://arxiv.org/pdf/2505.14631"}]

Based on the search results, I found the paper you're looking for. Here's what the search reveals about StoryCoder arXiv 2604.14631:

StoryCoder is a narrative reformulation framework that transforms code generation questions into coherent natural language narratives, providing richer contextual structure than simple rephrasings.

Each narrative consists of three components: a task overview, constraints, and example test cases, guided by the selected algorithm and genre.

The framework is based on findings from cognitive science that humans comprehend and reason more effectively when organizing fragmented conditions into coherent mental models using analogical structures.

According to the paper, experiments across 11 models on HumanEval, LiveCodeBench, and CodeForces demonstrate consistent improvements, with an average gain of 18.7% in zero-shot pass@10.

The paper was authored by Geonhui Jang, Dongyoon Han, and YoungJoon Yoo from Chung-Ang University and NAVER AI Lab, and was submitted on April 16, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8ef77e2-d344-4338-876c-a092e8873bc6",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "88b2a014-9e0f-433a-9aae-6dd105eac54f",
  "sourceToolAssistantUUID": "c8ef77e2-d344-4338-876c-a092e8873bc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T01:17:58.148Z_

<details><summary>↩ Tool result · `toolu_01WUEqv7v4aY8o3JcTQPriBU`</summary>

```text
Web search results for query: "ContractEval PACT LLM contract satisfaction arXiv 2510.12047"

Links: [{"title":"[2510.12047] ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation","url":"https://arxiv.org/abs/2510.12047"},{"title":"ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation","url":"https://arxiv.org/html/2510.12047"},{"title":"Under review. DO LARGE LANGUAGE MODELS RESPECT CON-","url":"https://arxiv.org/pdf/2510.12047"},{"title":"Do Large Language Models Respect Contracts? Evaluating and Enforcing Contract-Adherence in Code Generation","url":"https://arxiv.org/html/2510.12047v2"},{"title":"ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts","url":"https://arxiv.org/html/2508.03080v1"},{"title":"ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in","url":"https://arxiv.org/pdf/2508.03080"},{"title":"PACT: A Contract-Theoretic Framework for Pricing Agentic AI Services Powered by Large Language Models","url":"https://arxiv.org/html/2505.21286v1"},{"title":"[2508.03080] ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts","url":"https://arxiv.org/abs/2508.03080"},{"title":"A Contract-Theoretic Framework for Pricing Agentic AI ...","url":"https://arxiv.org/pdf/2505.21286"},{"title":"ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts","url":"https://www.researchgate.net/publication/394322713_ContractEval_Benchmarking_LLMs_for_Clause-Level_Legal_Risk_Identification_in_Commercial_Contracts"}]

Based on the search results, I found relevant information about arXiv paper 2510.12047. It appears there are actually two different papers with similar titles related to contracts and LLMs:

## Paper 2510.12047: ContractEval - Code Generation Focus

ContractEval is a benchmark for evaluating contract-satisfying assertions in code generation, which assesses whether code rejects contract-violating inputs by triggering intended assertions.

Built on HumanEval+ and MBPP+, ContractEval augments each task with contract-violation tests derived from reference assertions, synthesized via a neuro-symbolic pipeline where an LLM converts assertion clauses into constraints, and an SMT solver enumerates satisfiable violation combinations to generate inputs that violate selected clauses while satisfying the rest.

### Key Findings

Across five code LLMs, standard prompting yields 0% contract satisfaction, while adding a few contract-violation examples boosts contract satisfaction to 49--53% while maintaining pass@1 by 92% of the original.

Even when contracts are explicitly stated in the prompt, the satisfaction rate reaches only 23–41%, but showing models a small set of CVT (contract-violation test) examples lifts contract satisfaction further to 49–53%, preserving 92% of the original pass@1.

## Related Framework: PACT

The paper also references PACT (Program Assessment and Contract-adherence Evaluation framework), which is the first framework designed to systematically evaluate and enhance contract-adherence in LLM-generated code snippets alongside functional correctness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80feb0f8-01ad-4f42-82ec-f16f9a5b98c2",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "3e75f002-5ba6-4f90-96ce-3d4a1b3f7825",
  "sourceToolAssistantUUID": "80feb0f8-01ad-4f42-82ec-f16f9a5b98c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T01:17:59.705Z_

<details><summary>↩ Tool result · `toolu_01PgRae8fxsTMBRmB1LJGXuS`</summary>

```text
Web search results for query: "specification guided code generation LLM 2025 2026"

Links: [{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"},{"title":"My LLM coding workflow going into 2026 | by Addy Osmani | Medium","url":"https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation | OpenReview","url":"https://openreview.net/forum?id=6pr7BUGkLp"},{"title":"Distilling Multi-Agent Coding into a Single Small LLM","url":"https://aclanthology.org/2026.findings-eacl.346.pdf"},{"title":"Requirements Development and Formalization for Reliable Code Generation: A Multi-Agent Vision (ASE 2025 - New Ideas and Emerging Results) - ASE 2025","url":"https://conf.researchr.org/details/ase-2025/ase-2025-nier-track/30/Requirements-Development-and-Formalization-for-Reliable-Code-Generation-A-Multi-Agen"},{"title":"LLM-Generated Code in 2025: Trends and Predictions - Revelo","url":"https://www.revelo.com/blog/llm-code-generation-2025-trends-predictions-human-data"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"5 Open-Source Coding LLMs You Can Run Locally in 2026","url":"https://www.labellerr.com/blog/best-coding-llms/"},{"title":"Usage of Large Language Model for Code Generation Tasks: A Review | SN Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s42979-025-04241-5"},{"title":"LLM Code Quality Becomes Undeniable in 2026, Willison Predicts | ASCII News","url":"https://ascii.co.uk/news/article/news-20260118-5300f989/llm-code-quality-becomes-undeniable-in-2026-willison-predict"}]

Based on the web search results, here's what I found about specification-guided code generation with LLMs in 2025-2026:

## Recent Research and Approaches

Large Language Models are increasingly integrated into software development workflows, with research exploring specification-driven processes. The CURRANTE tool is a Visual Studio Code extension that enables a human-in-the-loop workflow for LLM-assisted code generation, guiding developers through three sequential stages—Specification, Tests, and Function—allowing them to define requirements, generate and refine test suites, and produce functions that satisfy those tests.

Self-Spec is a lightweight approach that prompts a model to design a compact spec schema it prefers, instantiate that schema from a problem's docstring and signature, resolve ambiguities via a minimal Q&A loop, and generate code only from the confirmed spec. On HumanEval benchmarks, Self-Spec improves results for stronger models: GPT-4o improved from 87% to 92%, and Claude 3.7 from 92% to 94%.

## Emerging Framework

ReDeFo is a multi-agent framework for reliable code generation based on requirements development and formalization, incorporating three agents with knowledge of formal methods into the requirements-to-code generation pipeline. The core of ReDeFo is using formal specifications to bridge the gap between ambiguous natural language requirements and precise executable code.

## Broader Trends

In 2026, the recommended workflow involves brainstorming a detailed specification with the AI first, then outlining a step-by-step plan before writing actual code, compiling this into a comprehensive spec.md containing requirements, architecture decisions, data models, and testing strategy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25d53597-dab9-40a3-bb64-7a8a122f482f",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "4b5ac560-45a6-400e-a16d-f96ece60a45b",
  "sourceToolAssistantUUID": "25d53597-dab9-40a3-bb64-7a8a122f482f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T01:18:00.005Z_

<details><summary>↩ Tool result · `toolu_01GEvANApQrGWzsKMUAKSVsk`</summary>

```text
Web search results for query: "design by contract LLM code"

Links: [{"title":"A Study of Preconditions and Postconditions as Design ...","url":"https://commons.erau.edu/cgi/viewcontent.cgi?article=1917&context=edt"},{"title":"Preconditions and Postconditions as Design Constraints for LLM Code Generation | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11218044/"},{"title":"A DbC Inspired Neurosymbolic Layer for Trustworthy Agent Design","url":"https://arxiv.org/pdf/2508.03665"},{"title":"Design by contract - Wikipedia","url":"https://en.wikipedia.org/wiki/Design_by_contract"},{"title":"Light and shadows of smart contract development with LLMs - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425026284"},{"title":"Automated Generation of Code Contracts – Generative AI to the Rescue?","url":"https://scg.unibe.ch/archive/papers/Grei24a-CodeContracts.pdf"},{"title":"Design By Contract Deontic Design Language for Component-Based Systems","url":"https://icr.uni.lu/leonvandertorre/papers/bnaic03b.pdf"},{"title":"Contracts for Large Language Model APIs:","url":"https://tanzimhromel.com/assets/pdf/llm-api-contracts.pdf"},{"title":"ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation","url":"https://arxiv.org/html/2510.12047"},{"title":"Code Generation of Smart Contracts with LLMs:","url":"https://lucaneg.github.io/papers/ISSRE25.pdf"}]

I found relevant research on the intersection of Design by Contract (DbC) and LLM code generation. Here are the key findings:

## Design by Contract with LLMs

Few studies have investigated how formal software engineering constraints, such as explicit preconditions and postconditions as part of the Design-by-Contract paradigm, influence class-level generation tasks. However, recent research is addressing this gap.

### Key Benefits

Design-by-contract is determined to be the best approach for LLM code generation because design contracts are still written in natural language, the native operational mode of LLMs. Incorporating explicit design constraints during prompting significantly boosts initial generation accuracy, particularly in Python but also in C++.

The contract-based design philosophy enhances component modularity and cohesion by allowing each function to focus exclusively on its specific responsibilities rather than accommodating every conceivable input state.

### Contract Applications

Researchers have adapted Design by Contract and type-theoretic principles to introduce a contract layer that mediates every LLM call, with contracts stipulating semantic and type requirements on inputs and outputs, coupled with probabilistic remediation to steer generation toward compliance.

Additionally, the DbC paradigm has been integrated into LLM-based program synthesis, enabling automated contract inference, natural language-based formal contract synthesis, and test assertion generation, while utilizing explicit contracts as design constraints to improve accuracy.

### Code Contract Generation

Real-world contracts are suitable to fine-tune state-of-the-art LLMs pretrained on code-related tasks, with nearly 60% exact match rate achieved despite a comparatively small dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32241901-fd90-43b5-b513-59e75a730c06",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "936aeae9-75b4-4e31-a52b-d95161fe8db1",
  "sourceToolAssistantUUID": "32241901-fd90-43b5-b513-59e75a730c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T01:18:01.229Z_

<details><summary>↩ Tool result · `toolu_01GS51MeV4h2A5odnXekPFme`</summary>

```text
Web search results for query: "formal specification LLM program repair"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"An empirical evaluation of pre-trained large language models for repairing declarative formal specifications | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10687-1"},{"title":"Specification-Guided Repair of Arithmetic Errors in Dafny Programs using LLMs","url":"https://arxiv.org/pdf/2507.03659"},{"title":"Specification-Guided Repair of Arithmetic Errors in Dafny Programs Using LLMs | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-10444-1_16"},{"title":"Combining Logic and Large Language Models for Assisted ...","url":"https://www.ricardobrancas.com/files/formhe25.pdf"},{"title":"An Empirical Evaluation of Pre-trained Large Language ...","url":"https://arxiv.org/pdf/2404.11050"},{"title":"Code Repair with LLMs gives an Exploration-Exploitation Tradeoff Hao Tang","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d5c56ec4f69c9a473089b16000d3f8cd-Paper-Conference.pdf"},{"title":"Counterexample Guided Program Repair Using Zero-Shot Learning and","url":"https://ojs.aaai.org/index.php/AAAI/article/view/32046/34201"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"}]

Based on the web search results, here's what I found about formal specification and LLM program repair:

## Overview

The intersection of formal specifications and LLM-based program repair is an active research area. Large Language Models (LLMs) have been investigated for their capacity to repair declarative specifications in Alloy, a declarative formal language used for software specification.

## Key Research Areas

**Declarative Formal Specifications:**
While existing APR techniques primarily target imperative programming languages like C and Java, there is a growing need for effective solutions applicable to declarative software specification languages. Automatic Program Repair (APR) has garnered significant attention as a practical research domain focused on automatically fixing bugs in programs.

**Specification-Guided Repair:**
An APR tool for Dafny, a verification-aware programming language that uses formal specifications — including pre-conditions, post-conditions, and invariants — as oracles for fault localization and repair, localizes faults using Hoare logic to determine the state of each statement within the program, and applies Large Language Models (LLMs) to synthesize candidate fixes.

## Performance Results

An approach using formal specifications achieved 89.7% fault localization success rate and GPT-4o mini yielded the highest repair success rate of 74.18%.

## Feedback Mechanisms

Research has designed multiple repair settings, encompassing single-agent and dual-agent paradigms, utilizing various LLMs, and incorporating different levels of feedback, including an auto-prompting mechanism for generating prompts autonomously using LLMs.

The research demonstrates "the potential of combining formal reasoning with LLM-based program synthesis for automated program repair."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31ded941-ba4d-402c-b454-1390894fe9ba",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "1dc0ed05-27ed-4641-b4a3-72e4baa882ac",
  "sourceToolAssistantUUID": "31ded941-ba4d-402c-b454-1390894fe9ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-12T01:18:05.051Z_

Good, I have a strong set of initial results. Let me now fetch more details on the most relevant papers, and run a few more targeted searches for papers I haven't found yet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dc0ed05-27ed-4641-b4a3-72e4baa882ac",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnyBV4WsKdRrVxYieTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca94900f-e6e3-45ef-8b87-1ebfccb6ee7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuDwVXWCRCkJCdAEj6Xmbj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 7026,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7026,
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

_source line 24 · 2026-05-12T01:18:06.606Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MAnhZ2hgZunmr3FbUa9cPN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.18315",
  "prompt": "Extract the full title, authors, date, and abstract of this paper. What method does it propose? How does it use property-based testing for LLM code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca94900f-e6e3-45ef-8b87-1ebfccb6ee7b",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnyBV4WsKdRrVxYieTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cf2b834-d52b-4022-98ce-ad7b0aa92366",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuDwVXWCRCkJCdAEj6Xmbj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 7026,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7026,
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

_source line 25 · 2026-05-12T01:18:07.919Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019tFHR3YeeKDVL2Zxttj7tK`</summary>

```json
{
  "url": "https://openreview.net/forum?id=6pr7BUGkLp",
  "prompt": "Extract the full title, authors, venue, date, and abstract of this paper. What is Self-Spec? How does it work? What results does it achieve?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cf2b834-d52b-4022-98ce-ad7b0aa92366",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnyBV4WsKdRrVxYieTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c41ab00-1e13-4315-8ef9-8041d0cc0714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuDwVXWCRCkJCdAEj6Xmbj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 7026,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7026,
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

_source line 26 · 2026-05-12T01:18:09.365Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DTCKf3XgvQ462tKTsk6Xfz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.12047",
  "prompt": "Extract the full title, authors, date, and abstract of this paper. What is ContractEval? What is PACT? How do they evaluate and enforce contract adherence in LLM code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c41ab00-1e13-4315-8ef9-8041d0cc0714",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnyBV4WsKdRrVxYieTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c1f551a-1a37-4172-98e8-fdbbe2dd9c84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuDwVXWCRCkJCdAEj6Xmbj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 7026,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7026,
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

_source line 27 · 2026-05-12T01:18:10.848Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YbfjfQPJQket5FQ4iGdttX`</summary>

```json
{
  "url": "https://ieeexplore.ieee.org/document/11218044/",
  "prompt": "Extract the full title, authors, venue, year, and abstract. What does this paper study about preconditions and postconditions as design constraints for LLM code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c1f551a-1a37-4172-98e8-fdbbe2dd9c84",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnyBV4WsKdRrVxYieTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f855fef-660d-4872-bf07-cc165474fb59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuDwVXWCRCkJCdAEj6Xmbj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 7026,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7026,
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

### Tool result

_source line 28 · 2026-05-12T01:18:11.219Z_

<details><summary>↩ Tool result · reported error · `toolu_01YbfjfQPJQket5FQ4iGdttX`</summary>

```text
Request failed with status code 418
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f855fef-660d-4872-bf07-cc165474fb59",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "7a33889d-6b2c-48c2-be30-856ee14ab071",
  "toolUseResult": "Error: Request failed with status code 418",
  "sourceToolAssistantUUID": "2f855fef-660d-4872-bf07-cc165474fb59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T01:18:11.358Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Fw1iBmriXnRy4jwf1epGp`</summary>

```json
{
  "query": "Property-Generated Solver PGS property-based testing LLM code generation arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a33889d-6b2c-48c2-be30-856ee14ab071",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnyBV4WsKdRrVxYieTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c2e00f1-d7d5-44a5-a73e-5aad185205f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuDwVXWCRCkJCdAEj6Xmbj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 7026,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7026,
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

### Tool result

_source line 30 · 2026-05-12T01:18:12.077Z_

<details><summary>↩ Tool result · `toolu_01MAnhZ2hgZunmr3FbUa9cPN`</summary>

```text
# Paper Summary

**Full Title:** "Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback"

**Authors:** Lehan He, Zeren Chen, Zhe Zhang, Xiang Gao, Lu Sheng

**Submission Date:** June 23, 2025 (revised May 1, 2026)

**Abstract:**
The paper addresses functional correctness in LLM-generated code by introducing the Property-Generated Solver (PGS). Rather than relying on test quantity, the authors emphasize feedback caliber. Their system generates "highly effective feedback via two principles: it must be property-oriented, to provide semantic guidance beyond simple I/O mismatches, and structurally minimal, to reduce cognitive load and isolate root causes."

## Proposed Method

PGS operates by evaluating high-level program characteristics (such as sorting functions producing non-decreasing sequences) and delivering the simplest counterexample that fails these conditions back to the LLM. This targeted strategy yields substantial improvements: up to 13.4% gain over other Test-Driven Development methods and a 64%+ fix rate on initially failing problems.

## Property-Based Testing Application

Rather than generating numerous test cases, the system validates abstract program properties and provides minimal failing examples. This property-driven approach guides models toward "correct and generalizable solutions," achieving bug-fix rates 1.4x-1.6x higher than competing debugging strategies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cf2b834-d52b-4022-98ce-ad7b0aa92366",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "4d33c3f7-0c11-4e9a-a650-705d8bb43c9f",
  "sourceToolAssistantUUID": "2cf2b834-d52b-4022-98ce-ad7b0aa92366",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-12T01:18:11.915Z_

<details><summary>↩ Tool result · `toolu_019tFHR3YeeKDVL2Zxttj7tK`</summary>

```text
# Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation

**Full Title:** Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation

**Authors:** Zihao Xu, Xiao Cheng, Jingling Xue, Yuekang Li

**Venue:** Agents4Science 2025 Conference

**Date Published:** October 8, 2025

## What is Self-Spec?

Self-Spec is a lightweight approach that enables language models to generate more reliable code by first creating their own specification language. The authors describe it as "a lightweight, deterministic (T=0) orchestration" that guides models through a structured process before implementation.

## How It Works

The method follows four sequential steps:

1. The model designs a compact specification schema tailored to its preferences
2. It instantiates that schema using the problem's docstring and function signature
3. It resolves ambiguities through minimal question-and-answer exchanges
4. It generates code exclusively from the confirmed specification

The underlying rationale is that "a self-authored spec better aligns with a model's internal representational bias, reducing docstring drift and format/edge-case mistakes."

## Results Achieved

On HumanEval benchmarks (pass@1), Self-Spec demonstrated improvements for stronger models:
- GPT-4o: 87% → 92% (+5 percentage points)
- Claude 3.7: 92% → 94% (+2 percentage points)
- Claude 3.5: 90% → 89% (-1 percentage point), returning to baseline after removing overly defensive code guards
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c41ab00-1e13-4315-8ef9-8041d0cc0714",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "639403fb-a81c-48f2-8437-f04baed2f398",
  "sourceToolAssistantUUID": "0c41ab00-1e13-4315-8ef9-8041d0cc0714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-12T01:18:12.451Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019DzWddxJmDD7SuxFoH1Acd`</summary>

```json
{
  "query": "AutoSpec LLM precondition postcondition loop invariant synthesis verifier feedback"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "639403fb-a81c-48f2-8437-f04baed2f398",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnyBV4WsKdRrVxYieTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c549285e-d752-49ae-b3a0-54b3ae0064b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuDwVXWCRCkJCdAEj6Xmbj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 7026,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7026,
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

_source line 33 · 2026-05-12T01:18:13.239Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GWKwVfK8pWGYU3VusHQWA4`</summary>

```json
{
  "query": "counterexample guided program repair zero-shot LLM AAAI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c549285e-d752-49ae-b3a0-54b3ae0064b5",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnyBV4WsKdRrVxYieTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fccae15b-dd00-4fe2-adc3-71807493809d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuDwVXWCRCkJCdAEj6Xmbj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 7026,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7026,
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

_source line 34 · 2026-05-12T01:18:13.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FHQg5itVUBBYExmy366pUP`</summary>

```json
{
  "query": "ReDeFo requirements formalization multi-agent code generation formal specification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fccae15b-dd00-4fe2-adc3-71807493809d",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnyBV4WsKdRrVxYieTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a555b60e-f29f-4891-a6f5-a9bd9a1911a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuDwVXWCRCkJCdAEj6Xmbj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 852,
      "cache_creation_input_tokens": 7026,
      "cache_read_input_tokens": 10953,
      "output_tokens": 686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7026
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 852,
          "output_tokens": 686,
          "cache_read_input_tokens": 10953,
          "cache_creation_input_tokens": 7026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7026,
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

_source line 35 · 2026-05-12T01:18:14.825Z_

<details><summary>↩ Tool result · `toolu_01DTCKf3XgvQ462tKTsk6Xfz`</summary>

```text
# ContractEval Paper Summary

**Full Title:** ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation

**Authors:** Soohan Lim, Joonghyuk Hahn, Hyunwoo Park, Sang-Ki Ko, Yo-Sub Han

**Date:** Submitted October 14, 2025; Last revised April 20, 2026 (v4)

## What is ContractEval?

ContractEval is a benchmark designed to assess whether AI-generated code properly enforces input preconditions. The research reveals a critical gap: "current code generation evaluation measures functional correctness on well-formed inputs that satisfy all input preconditions," yet these requirements are often left implicit in task descriptions.

The benchmark contains 364 tasks built on HumanEval+ and MBPP+, each including: explicitly stated contracts, test cases from a neuro-symbolic pipeline combining LLMs with SMT solvers, and reference code with contracts.

## Key Finding on Contract Adherence

Testing five open-source code LLMs exposed a striking problem: models achieved pass@1 scores of 75-82% for functional correctness but demonstrated "0% contract satisfaction" under standard conditions. Even with explicit contract statements in prompts, satisfaction rates only reached 23-41%, demonstrating that contemporary language models struggle significantly with enforcing preconditions in generated code.

**Note:** The provided content contains no information about "PACT."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c1f551a-1a37-4172-98e8-fdbbe2dd9c84",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "93f9ddf5-41e0-41bb-8687-97ecb8444a43",
  "sourceToolAssistantUUID": "5c1f551a-1a37-4172-98e8-fdbbe2dd9c84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T01:18:18.899Z_

<details><summary>↩ Tool result · `toolu_01GWKwVfK8pWGYU3VusHQWA4`</summary>

```text
Web search results for query: "counterexample guided program repair zero-shot LLM AAAI 2025"

Links: [{"title":"GitHub - pmorvalho/LLM-CEGIS-Repair: AAAI 2025: Counterexample Guided Program Repair Using Zero-Shot Learning and MaxSAT-based Fault Localization","url":"https://github.com/pmorvalho/LLM-CEGIS-Repair"},{"title":"Counterexample Guided Program Repair Using Zero-Shot Learning and MaxSAT-based Fault Localization | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/32046"},{"title":"Counterexample Guided Program Repair Using Zero-Shot Learning and MaxSAT-based Fault Localization - University of Lisbon","url":"https://researchportal.ulisboa.pt/en/publications/counterexample-guided-program-repair-using-zero-shot-learning-and/"},{"title":"Counterexample Guided Program Repair Using Zero-Shot Learning and","url":"https://ojs.aaai.org/index.php/AAAI/article/view/32046/34201"},{"title":"Counterexample Guided Program Repair Using Zero-Shot Learning and","url":"https://pmorvalho.github.io/uploads/papers/aaai25-LLM-CEGIS-Repair.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Counterexample+Guided+Program+Repair+Using+Zero-Shot+Learning+and+MaxSAT-based+Fault+Localization."},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"[2502.07786] Counterexample Guided Program Repair Using Zero-Shot Learning and MaxSAT-based Fault Localization","url":"https://arxiv.org/abs/2502.07786"},{"title":"Counterexample Guided Program Repair Using Zero-Shot Learning and MaxSAT-based Fault Localization","url":"https://arxiv.org/html/2502.07786v1"},{"title":"Counterexample guided program repair using zero-shot ...","url":"https://dl.acm.org/doi/10.1609/aaai.v39i1.32046"}]

Based on the search results, I found comprehensive information about the paper on counterexample guided program repair:

## Paper Overview

"Counterexample Guided Program Repair Using Zero-Shot Learning and MaxSAT-based Fault Localization" was accepted at AAAI 2025. The paper is authored by P. Orvalho, M. Janota, and V. Manquinho and was presented at the 39th Annual AAAI Conference on Artificial Intelligence.

## Key Approach

The work combines the strengths of both Formal Methods (FM)-based fault localization and Large Language Models (LLMs), via zero-shot learning, to enhance Automated Program Repair (APR) for introductory programming assignments (IPAs).

The method operates as follows:
- MaxSAT-based fault localization identifies buggy parts of a program, then presents the LLM with a program sketch devoid of these buggy statements.
- This hybrid approach follows a Counterexample Guided Inductive Synthesis (CEGIS) loop to iteratively refine the program. The LLM synthesizes the missing parts, which are then checked against a test suite. If the suggested program is incorrect, a counterexample from the test suite is fed back to the LLM for revised synthesis.

## Experimental Results

Experiments on 1,431 incorrect student programs show that the counterexample guided approach, using MaxSAT-based bug-free program sketches, significantly improves the repair capabilities of all six evaluated LLMs. The method allows LLMs to repair more programs and produce smaller fixes, outperforming other configurations and state-of-the-art symbolic program repair tools.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fccae15b-dd00-4fe2-adc3-71807493809d",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "744a254b-f567-4f33-ad4b-ba151aae730f",
  "sourceToolAssistantUUID": "fccae15b-dd00-4fe2-adc3-71807493809d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-12T01:18:19.417Z_

<details><summary>↩ Tool result · `toolu_019DzWddxJmDD7SuxFoH1Acd`</summary>

```text
Web search results for query: "AutoSpec LLM precondition postcondition loop invariant synthesis verifier feedback"

Links: [{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"Enchanting Program Specification Synthesis by","url":"https://arxiv.org/pdf/2404.00762"},{"title":"Automatic Generation of Formal Specification and Verification Annotations Using LLMs and Test Oracles1footnote 11footnote 1Preprint. Intended for submission to Science of Computer Programming.","url":"https://arxiv.org/html/2601.12845v1"},{"title":"Uppsala University Department of Informatics and Media VeRefine:","url":"https://www.diva-portal.org/smash/get/diva2:2010654/FULLTEXT02.pdf"},{"title":"Enchanting Program Specification Synthesis by Large Language Models using Static Analysis and Program Verification","url":"https://arxiv.org/html/2404.00762v2"},{"title":"LLM For Loop Invariant Generation and Fixing","url":"https://arxiv.org/pdf/2511.06552"},{"title":"Effectiveness of AutoSpec in General Specification Generation | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Effectiveness-of-AutoSpec-in-General-Specification-Generation_tbl1_382545666"},{"title":"ClassInvGen: Class Invariant Synthesis using Large Language Models","url":"https://openreview.net/pdf?id=7iwJ2ZQS3s"},{"title":"VeriAct: Beyond Verifiability – Agentic Synthesis of Correct and Complete Formal Specifications","url":"https://arxiv.org/html/2604.00280"},{"title":"ClassInvGen: Class Invariant Synthesis using Large Language Models","url":"https://arxiv.org/html/2502.18917"}]

Based on the search results, I found comprehensive information about AutoSpec. Here's what the research shows:

## AutoSpec Overview

AutoSpec synthesizes specification in a bottom-up manner, generating versatile specifications including not only loop invariants, but also preconditions, postconditions, and assigned variables necessary for full proof.

## Key Features

AutoSpec is a combined approach that synthesizes pre/postconditions and loop invariants using LLMs and verifier feedback. AutoSpec employs the prompt engineering technique of few-shot prompting, with prompts designed to include relevant input-output examples, which can guide LLMs in generating desired outputs.

## Technical Approach

AutoSpec is driven by static analysis and program verification and empowered by large language models, addressing practical challenges by having LLMs serve as generators to produce candidate specifications, decomposing programs to direct attention of LLMs, and validating candidate specifications in each round to avoid error accumulation.

## Performance Results

AutoSpec successfully verifies 79% of programs through automatic specification synthesis, achieving a significant improvement of 1.592x over existing works. It can also be successfully applied to verify programs in a real-world X509-parser project.

## Comparison with Test-Based Approaches

AutoSpec relies on ACSL assertions encoding general correctness properties, making it property-driven rather than test-driven, distinguishing it from other recent LLM-based verification approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c549285e-d752-49ae-b3a0-54b3ae0064b5",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "f89e089a-e79f-46c5-9770-fbbdfc86d690",
  "sourceToolAssistantUUID": "c549285e-d752-49ae-b3a0-54b3ae0064b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T01:18:19.465Z_

<details><summary>↩ Tool result · `toolu_016Fw1iBmriXnRy4jwf1epGp`</summary>

```text
Web search results for query: "Property-Generated Solver PGS property-based testing LLM code generation arXiv"

Links: [{"title":"Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/html/2506.18315v1"},{"title":"[2506.18315] Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/abs/2506.18315"},{"title":"Enhanced LLM code generation with property-based testing! New Framework PGS to Break Self-Deception | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/llm-paper/property-generated-solver"},{"title":"Use Property-Based Testing to Bridge LLM Code Generation and Validation | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.18315v1"},{"title":"[Literature Review] Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://www.themoonlight.io/en/review/use-property-based-testing-to-bridge-llm-code-generation-and-validation"},{"title":"Paper page - Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://huggingface.co/papers/2506.18315"},{"title":"[PDF] Use Property-Based Testing to Bridge LLM Code Generation and Validation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Use-Property-Based-Testing-to-Bridge-LLM-Code-and-He-Chen/976a0c7318053c050609c4732729ef37eddc0199"},{"title":"Understanding the Characteristics of LLM-Generated Property-Based Tests in Exploring Edge Cases","url":"https://arxiv.org/html/2510.25297v1"},{"title":"From Exploration to Specification: LLM-Based Property Generation for Mobile App Testing","url":"https://arxiv.org/html/2604.13463"},{"title":"[2510.25297] Understanding the Characteristics of LLM-Generated Property-Based Tests in Exploring Edge Cases","url":"https://arxiv.org/abs/2510.25297"}]

I found comprehensive information about the Property-Generated Solver (PGS) framework. Here's a summary of the search results:

## Property-Generated Solver (PGS) Overview

PGS is a novel framework that embeds Property-Based Testing (PBT) as a core engine for an iterative, LLM-driven code generation and refinement process.

### Framework Architecture

PGS employs two key agents—a Generator and a Tester—that systematically decouple code generation from its validation. After the Generator produces initial candidate programs, these agents collaborate iteratively: the Tester rigorously validates them using defined properties, while the Generator refines the programs based on the feedback from validation results.

### How It Works

The Tester manages the PBT life-cycle: it defines high-level abstract properties (e.g., invariants, functional constraints) that serve as precise specifications. The Tester then translates them into corresponding executable property-checking code and generates diverse test inputs to instantiate these properties, against which the candidate programs are executed.

### Key Innovation

PGS leverages Property-Based Testing to validate high-level program properties or invariants, instead of relying on specific input-output examples. These properties are often simpler to define and verify than directly predicting exhaustive test oracles, breaking the "cycle of self-deception" where tests might share flaws with the code they are meant to validate.

### Performance Results

PGS achieves a 23.1%–37.3% relative improvement (pass@1) over previous TDD methods on problems that are challenging for direct prompting when evaluated across multiple code generation benchmarks including HumanEval, MBPP, and LiveCodeBench.

The paper was submitted to arXiv on June 23, 2025, with arxiv ID 2506.18315.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c2e00f1-d7d5-44a5-a73e-5aad185205f1",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "0d5befea-8b70-4fa1-86e3-12369267fa0e",
  "sourceToolAssistantUUID": "4c2e00f1-d7d5-44a5-a73e-5aad185205f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-12T01:18:20.731Z_

<details><summary>↩ Tool result · `toolu_01FHQg5itVUBBYExmy366pUP`</summary>

```text
Web search results for query: "ReDeFo requirements formalization multi-agent code generation formal specification"

Links: [{"title":"Requirements Development and Formalization for Reliable Code Generation: A Multi-Agent Vision *Weisong Sun is the corresponding author. This research is supported by the National Natural Science Foundation of China (62192734, 62192731, 62372347), the Fundamental Research Funds for the Central Universities (ZYTS25076), and the National Research Foundation, Singapore, and DSO National Laboratories under the AI Singapore Programme (AISG Award No: AISG2-GC-2023-008).","url":"https://arxiv.org/html/2508.18675"},{"title":"[2508.18675] Requirements Development and Formalization for Reliable Code Generation: A Multi-Agent Vision","url":"https://arxiv.org/abs/2508.18675"},{"title":"Requirements Development and Formalization for Reliable Code Generation: A Multi-Agent Vision (ASE 2025 - New Ideas and Emerging Results) - ASE 2025","url":"https://conf.researchr.org/details/ase-2025/ase-2025-nier-track/30/Requirements-Development-and-Formalization-for-Reliable-Code-Generation-A-Multi-Agen"},{"title":"Envisioning Intelligent Requirements Engineering via Knowledge-Guided Multi-Agent Collaboration | Request PDF","url":"https://www.researchgate.net/publication/400199860_Envisioning_Intelligent_Requirements_Engineering_via_Knowledge-Guided_Multi-Agent_Collaboration"},{"title":"AgentCoder: Multiagent-Code Generation with Iterative Testing and Optimisation","url":"https://arxiv.org/html/2312.13010v2"},{"title":"Requirements Development and Formalization for Reliable ...","url":"https://www.researchgate.net/publication/394978496_Requirements_Development_and_Formalization_for_Reliable_Code_Generation_A_Multi-Agent_Vision"},{"title":"GitHub - huangd1999/AgentCoder: AgentCoder: multi-agent code generation framework. · GitHub","url":"https://github.com/huangd1999/AgentCoder"},{"title":"Position: Trustworthy AI Agents Require the Integration of","url":"https://openreview.net/pdf?id=wkisIZbntD"},{"title":"[2312.13010] AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation","url":"https://arxiv.org/abs/2312.13010"},{"title":"AgentCoder: Multi-Agent Code Generation with Effective Testing and Self-optimisation","url":"https://arxiv.org/html/2312.13010v3"}]

Based on the search results, here's what I found about ReDeFo:

## Overview

ReDeFo is a multi-agent framework for requirements development and formalization designed to improve automated code generation. The core of ReDeFo is the use of formal specifications to bridge the gap between potentially ambiguous natural language requirements and precise executable code.

## Architecture

The overall process involves three functionally specialized agents, i.e., Analyst, Formalizer, and Coder who are responsible for completing the requirements development, formalization, and code generation tasks, respectively.

The workflow operates as follows:

- **Analyst Agent**: The Analyst autonomously analyzes the text to refine each functionality into more detailed sub-requirements and further extracts or infers system constraints and functional behaviors, identifies architectural components, and constructs an initial architecture model.

- **Formalizer Agent**: The Formalizer is responsible for translating the informal specifications into formal specifications using domain-specific logic, formal semantics, and modeling guidelines.

- **Coder Agent**: The Coder uses both the refined NLRs and formal specifications to generate code modules that meet the given requirements, synthesizing executable code from the formal models while retaining alignment with the original informal descriptions.

## Key Benefits

ReDeFo enables rigorous reasoning about correctness, uncovering hidden bugs, and enforcing critical properties throughout the development process. Additionally, ReDeFo advocates human-in-the-loop interaction by incorporating expert judgment at critical points and facilitating more active expert participation beyond post-hoc review.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a555b60e-f29f-4891-a6f5-a9bd9a1911a9",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "b6c1f55b-9587-4131-b0eb-f63280d6c8e9",
  "sourceToolAssistantUUID": "a555b60e-f29f-4891-a6f5-a9bd9a1911a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-12T01:18:26.103Z_

Let me now search for a few more closely related papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6c1f55b-9587-4131-b0eb-f63280d6c8e9",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnzcpqcwUR9HxTLoaBE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5341b56a-303b-48a1-b40e-a72bb7a5354f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3x7hvLC2b1bSwySNs1JQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6645,
      "cache_read_input_tokens": 17979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6645,
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

_source line 41 · 2026-05-12T01:18:26.791Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LKE2p7qCr7CVc1rZ6XvKcG`</summary>

```json
{
  "query": "NL2Contract natural language docstring contract assertion Python LLM arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5341b56a-303b-48a1-b40e-a72bb7a5354f",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnzcpqcwUR9HxTLoaBE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37d19366-c2bb-41ee-92f7-2334b7245069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3x7hvLC2b1bSwySNs1JQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6645,
      "cache_read_input_tokens": 17979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6645,
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

_source line 42 · 2026-05-12T01:18:27.849Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0146LQMsAoHWzcdBk8TwEA8i`</summary>

```json
{
  "query": "specification-guided code repair Dafny LLM Hoare logic preconditions postconditions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37d19366-c2bb-41ee-92f7-2334b7245069",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnzcpqcwUR9HxTLoaBE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81e57b3a-47b1-4717-8694-873d67c7a5be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3x7hvLC2b1bSwySNs1JQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6645,
      "cache_read_input_tokens": 17979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6645,
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

_source line 43 · 2026-05-12T01:18:28.818Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XpWaCoGsAoX4i8ag3n8TFW`</summary>

```json
{
  "query": "execution-guided code generation LLM behavioral specification invariant 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81e57b3a-47b1-4717-8694-873d67c7a5be",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnzcpqcwUR9HxTLoaBE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f320f97f-1449-4936-841c-b58cc8bbfca5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3x7hvLC2b1bSwySNs1JQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6645,
      "cache_read_input_tokens": 17979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6645,
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

_source line 44 · 2026-05-12T01:18:28.983Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JbxaFayp919iu6eHBhGnER`</summary>

```json
{
  "query": "LLM code generation assertion checking runtime verification contract 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f320f97f-1449-4936-841c-b58cc8bbfca5",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011CawnzcpqcwUR9HxTLoaBE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "502ed427-39de-48bf-854e-96ce5c6744cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3x7hvLC2b1bSwySNs1JQ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6645,
      "cache_read_input_tokens": 17979,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6645
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 17979,
          "cache_creation_input_tokens": 6645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6645,
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

_source line 45 · 2026-05-12T01:18:34.685Z_

<details><summary>↩ Tool result · `toolu_01LKE2p7qCr7CVc1rZ6XvKcG`</summary>

```text
Web search results for query: "NL2Contract natural language docstring contract assertion Python LLM arXiv"

Links: [{"title":"Beyond Postconditions: Can Large Language Models infer Formal Contracts for","url":"https://arxiv.org/pdf/2510.12702"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"[2510.12702] Beyond Postconditions: Can Large Language Models infer Formal Contracts for Automatic Software Verification?","url":"https://arxiv.org/abs/2510.12702"},{"title":"DocuMint: Docstring Generation for Python using Small Language Models","url":"https://arxiv.org/html/2405.10243v1"},{"title":"Can Large Language Models Transform Natural Language","url":"https://web.eecs.umich.edu/~weimerw/2025-590/reading/endres-llm-postconditions.pdf"},{"title":"ContractNLI | ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts","url":"https://stanfordnlp.github.io/contract-nli/"},{"title":"[2110.01799] ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts","url":"https://arxiv.org/abs/2110.01799"},{"title":"ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation","url":"https://arxiv.org/html/2510.12047"},{"title":"ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts - ACL Anthology","url":"https://aclanthology.org/2021.findings-emnlp.164/"},{"title":"[2110.01799v1] ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts","url":"https://arxiv.org/abs/2110.01799v1"}]

Based on the search results, here's what I found about NL2Contract:

## NL2Contract Overview

NL2Contract is the task of employing LLMs to translate informal natural language into formal functional contracts, consisting of postconditions as well as preconditions. It translates natural-language docstrings into contracts expressed as executable Python assertions.

## Problem Statement

Automatic software verifiers have become increasingly effective at checking software against formal specifications, yet their adoption in practice has been hampered by the lack of such specifications in real world code. Large Language Models have shown promise in inferring formal postconditions from natural language hints embedded in code such as function names, comments or documentation, but using the generated postconditions as specifications in verification often leads verifiers to suggest invalid inputs, hinting at potential issues that ultimately turn out to be false alarms.

## Approach and Evaluation

An NL2Contract task is a triple of natural language description, reference implementation, and reference precondition, the latter for instance given as assertions within programs.

The benchmark uses HumanEval+ which includes 164 Python problems, each consisting of a function stub, a natural language description encoded as a Python docstring, a reference implementation, and some validating tests, with reference preconditions implemented as Python asserts for each problem.

## Key Results

LLMs are generally effective at generating functional contracts sound for all possible inputs, the generated contracts are sufficiently expressive for discriminating buggy from correct behavior, and LLM inferred preconditions generally align well with developers intentions which allows automatic software verifiers to catch real-world bugs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37d19366-c2bb-41ee-92f7-2334b7245069",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "3b429d87-1ed3-4ec5-9ac4-83d8780f59eb",
  "sourceToolAssistantUUID": "37d19366-c2bb-41ee-92f7-2334b7245069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-12T01:18:34.698Z_

<details><summary>↩ Tool result · `toolu_0146LQMsAoHWzcdBk8TwEA8i`</summary>

```text
Web search results for query: "specification-guided code repair Dafny LLM Hoare logic preconditions postconditions"

Links: [{"title":"Specification-Guided Repair of Arithmetic Errors in Dafny Programs using LLMs","url":"https://www.arxiv.org/pdf/2507.03659v2"},{"title":"Specification-Guided Repair of Arithmetic Errors in Dafny Programs Using LLMs | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-10444-1_16"},{"title":"[2507.03659] Specification-Guided Repair of Arithmetic Errors in Dafny Programs using LLMs","url":"https://arxiv.org/abs/2507.03659"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"Published in Transactions on Machine Learning Research (01/2025)","url":"https://openreview.net/pdf?id=yBgTVWccIx"},{"title":"Your Code Already Has Preconditions - You Just Haven't Written Them Down","url":"https://buildwithaws.substack.com/p/hoare-logic-for-code-and-cloud-what"},{"title":"Hoare Logic for Code and Cloud: What 1969 Computer Science Offers 2026 Engineering","url":"https://zircon.tech/blog/hoare-logic-for-code-and-cloud-what-1969-computer-science-offers-2026-engineering/"},{"title":"Automatic Specification Repair in Contract Programming","url":"https://haslab.github.io/SpecRep/pubs/AAbreu23.pdf"},{"title":"GitHub - VeriFixer/APRepair-of-Arithmetic-Programs-in-Dafny-using-LLMs: Tool for fault localization and repair of arithmetic bugs in Dafny using LLMs","url":"https://github.com/VeriFixer/APRepair-of-Arithmetic-Programs-in-Dafny-using-LLMs"},{"title":"/ Hoare Triples and Dafny /","url":"https://www.cs.umd.edu/class/spring2025/cmsc433/code/HoareLogic.dfy"}]

I found comprehensive research on this topic. Here's a summary of the search results:

## Overview

The research presents an APR (Automated Program Repair) tool for Dafny that uses formal specifications—including pre-conditions, post-conditions, and invariants—as oracles for fault localization and repair.

## Key Components

**Dafny Language:** Dafny is a programming language designed for formal software verification, using constructs for program specifications that define expected behavior and allow mathematical proof of consistency.

**Hoare Logic:** Hoare logic is a formal system with a set of logical rules used to reason about the correctness of computer programs. It employs deductive reasoning to prove properties of programs using Hoare Triples, denoted as {P} Q {R}, where P represents pre-conditions, Q is a sequence of program statements, and R represents post-conditions.

## Repair Process

The repair process begins by passing a Dafny program as an argument. If the verifier detects specification violations, the tool triggers APR components, which perform fault localization, generate prompts for the LLM, and apply candidate fixes. Verification is re-run after each patch attempt.

## Bug Scope and Limitations

The approach focused exclusively on arithmetic errors and does not yet support other error classes (e.g., control flow, heap misuse). GPT-4o mini was the most effective in generating valid patches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81e57b3a-47b1-4717-8694-873d67c7a5be",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "0a847018-247c-4bf7-b759-d301a908131c",
  "sourceToolAssistantUUID": "81e57b3a-47b1-4717-8694-873d67c7a5be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-12T01:18:36.377Z_

<details><summary>↩ Tool result · `toolu_01JbxaFayp919iu6eHBhGnER`</summary>

```text
Web search results for query: "LLM code generation assertion checking runtime verification contract 2025"

Links: [{"title":"Beyond Postconditions: Can Large Language Models infer Formal Contracts for","url":"https://arxiv.org/pdf/2510.12702"},{"title":"ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation","url":"https://arxiv.org/html/2510.12047"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"PropertyGPT: LLM-driven Formal Verification of Smart ...","url":"https://arxiv.org/pdf/2405.02580"},{"title":"Leveraging LLMs for Formal Software Requirements: Challenges and Prospects","url":"https://ceur-ws.org/Vol-4142/paper11.pdf"},{"title":"[2507.13290] Towards Formal Verification of LLM-Generated Code from Natural Language Prompts","url":"https://arxiv.org/abs/2507.13290"},{"title":"Quokka: Accelerating Program Verification with LLMs via Invariant Synthesis","url":"https://arxiv.org/html/2509.21629"},{"title":"Towards Formal Verification of LLM-Generated Code from Natural Language Prompts","url":"https://arxiv.org/pdf/2507.13290"},{"title":"Frontiers | A dual perspective review on large language models and code verification","url":"https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1655469/full"},{"title":"LLM-driven verification assistance: Bridging code, coverage and collaboration","url":"https://ijsra.net/content/llm-driven-verification-assistance-bridging-code-coverage-and-collaboration"}]

I've completed the web search for your query. Here's a summary of what I found:

## Key Research Areas on LLM Code Generation with Assertion Checking and Runtime Verification

The search returned several recent 2025 papers addressing the intersection of LLMs, code generation, assertions, and contract-based verification:

**ContractEval Benchmark**: Design by Contract (DbC) treats preconditions, postconditions, and invariants as part of the specification, and emphasizes checking them in executable conditions such as assertions, with contracts most commonly appearing as assertion-level input validity checks. The DbC paradigm has been integrated into LLM-based program synthesis, enabling automated contract inference, natural language-based formal contract synthesis, and test assertion generation.

**Formal Contract Generation**: Pre- and postconditions are encoded as pure Python assertions which allows the use of software verifiers subsequently checking for assertion violations.

**Program Verification with LLMs**: An evaluation-centric design directly evaluates LLM-generated invariants by checking whether each invariant is valid and whether it helps prove the target assertion, eliminating most customized post-processing logic.

**Formal Verification of LLM-Generated Code**: To offer formal guarantees of correctness to LLM generated code, a Formal Query Language can represent a user's intent in a formally defined but natural language-like manner.

These papers represent emerging work in ensuring LLM-generated code meets formal specifications through assertions and runtime contract verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "502ed427-39de-48bf-854e-96ce5c6744cb",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "3542b2df-772c-443c-9ec7-24708e8e04af",
  "sourceToolAssistantUUID": "502ed427-39de-48bf-854e-96ce5c6744cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-12T01:18:37.759Z_

<details><summary>↩ Tool result · `toolu_01XpWaCoGsAoX4i8ag3n8TFW`</summary>

```text
Web search results for query: "execution-guided code generation LLM behavioral specification invariant 2024 2025"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268"},{"title":"LLM-Based Code Translation Needs Formal Compositional Reasoning Alvin Cheung","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-174.pdf"},{"title":"Bridging the Gap between User Intent and LLM: A Requirement Alignment Approach for Code Generation","url":"https://arxiv.org/html/2604.16198v1"},{"title":"Verified Code Transpilation with LLMs Sahil Bhatia1 Jie Qiu Niranjan Hasabnis2∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/48bb60a0c0aebb4142bf314bd1a5c6a0-Paper-Conference.pdf"},{"title":"Execution Guided Line-by-Line Code Generation Boaz Lavon Shahar Katz Lior Wolf","url":"https://arxiv.org/pdf/2506.10948"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"Understanding Specification-Driven Code Generation with ...","url":"https://arxiv.org/pdf/2601.03878"},{"title":"Towards LLM-Driven Code Generation: The Impact of Process ...","url":"https://spectrum.library.concordia.ca/id/eprint/995585/1/LIN_MA_S2025.pdf"},{"title":"Transactions on Artificial Intelligence https://www.sciltp.com/journals/tai","url":"https://media.sciltp.com/articles/2505000685/2505000685.pdf"}]

Based on the search results, I found several relevant papers and research on execution-guided code generation, LLM behavioral specifications, and invariants from 2024-2025:

## Key Findings:

**Execution-Guided Code Generation:**

A paper presented at NeurIPS 2025 on "Execution Guided Line-by-Line Code Generation" demonstrates that EG-CFG (with DeepSeek-V3) matches state-of-the-art on HumanEval and sets new benchmarks on HumanEval-ET. The method grounds coding decisions in observed execution behavior rather than relying purely on syntactic approaches, providing raw execution outcomes as soft guidance signals.

**Behavioral Specification Generation:**

A recent approach (nl2postcond from Endres et al., 2024) uses execution-based evaluation but is restricted to relatively simple datasets, supports only limited assertion forms, and does not consider preconditions. Research has found that generating executable behavioral specifications is substantially more challenging for LLMs than generating code solutions.

**Invariant Generation and Verification:**

LLMs can be used to produce proof artifacts to enable verification to scale, via compositional verification and invariant generation. Employing LLMs in zero-shot settings to generate loop invariants often led to numerous attempts before producing correct invariants; researchers introduced iRank, a re-ranking mechanism based on contrastive learning, which effectively distinguishes correct from incorrect invariants.

**Specification-Driven Code Generation:**

Research targets precise pre-/post-conditions and type/refinement invariants, input domain restrictions, corner cases and determinism, error/exception policy and stability under weak preconditions, resource/complexity constraints and tie-breaking rules, and I/O formatting and stateful side-effects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f320f97f-1449-4936-841c-b58cc8bbfca5",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "8e6c182c-0cff-4e0f-a195-4f83b51594e1",
  "sourceToolAssistantUUID": "f320f97f-1449-4936-841c-b58cc8bbfca5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-12T01:18:40.906Z_

Let me fetch details on two more critical papers that look very closely related to ExeSpec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e6c182c-0cff-4e0f-a195-4f83b51594e1",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo1sfLeWpQumsnSDWEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28c12e46-ef57-4eb8-aa07-fb5f2be0ac26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ST4AeDypR8YigEDHc34GLL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 833,
      "cache_creation_input_tokens": 3176,
      "cache_read_input_tokens": 24624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3176,
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

_source line 50 · 2026-05-12T01:18:42.391Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Nyokw4aR5An96RXkgzQS29`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.12268",
  "prompt": "Extract the full title, authors, date, and abstract of this paper. What is CodeSpecBench? How does it relate to executable behavioral specifications for LLM code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28c12e46-ef57-4eb8-aa07-fb5f2be0ac26",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo1sfLeWpQumsnSDWEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cd66786-3dbb-4a51-94b4-626f287d380f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ST4AeDypR8YigEDHc34GLL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 833,
      "cache_creation_input_tokens": 3176,
      "cache_read_input_tokens": 24624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3176,
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

_source line 51 · 2026-05-12T01:18:43.815Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JK4Yj9zDb2K8yfLLftrV4P`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.12702",
  "prompt": "Extract the full title, authors, date, and abstract. What is the NL2Contract task? How does it use preconditions and postconditions for LLM-based verification?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cd66786-3dbb-4a51-94b4-626f287d380f",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo1sfLeWpQumsnSDWEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95eb313c-a262-4752-895f-7973dac2d1a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ST4AeDypR8YigEDHc34GLL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 833,
      "cache_creation_input_tokens": 3176,
      "cache_read_input_tokens": 24624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3176,
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

_source line 52 · 2026-05-12T01:18:45.346Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WNP5UbAAVBPXKeXb1HLyG8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.03659",
  "prompt": "Extract the full title, authors, venue, date, and abstract. How does this paper use formal specifications (preconditions, postconditions, invariants) to guide LLM-based program repair in Dafny?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95eb313c-a262-4752-895f-7973dac2d1a4",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo1sfLeWpQumsnSDWEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1abbdfc6-69e8-4385-9950-df737ce81aa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ST4AeDypR8YigEDHc34GLL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 833,
      "cache_creation_input_tokens": 3176,
      "cache_read_input_tokens": 24624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3176,
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

_source line 53 · 2026-05-12T01:18:46.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Se4P69KKtqUjzwouGubbBA`</summary>

```json
{
  "query": "CodeSpecBench executable behavioral specification benchmark LLM precondition postcondition invariant 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1abbdfc6-69e8-4385-9950-df737ce81aa3",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo1sfLeWpQumsnSDWEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "579c4624-5f94-48d0-9495-a3651db94adf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ST4AeDypR8YigEDHc34GLL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 833,
      "cache_creation_input_tokens": 3176,
      "cache_read_input_tokens": 24624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3176,
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

_source line 54 · 2026-05-12T01:18:46.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tm1iQb7BuWiBZocGt4okxz`</summary>

```json
{
  "query": "ClassInvGen class invariant synthesis LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "579c4624-5f94-48d0-9495-a3651db94adf",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo1sfLeWpQumsnSDWEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b52e939e-a1da-412a-b6f2-615e6f990783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ST4AeDypR8YigEDHc34GLL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 833,
      "cache_creation_input_tokens": 3176,
      "cache_read_input_tokens": 24624,
      "output_tokens": 461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 833,
          "output_tokens": 461,
          "cache_read_input_tokens": 24624,
          "cache_creation_input_tokens": 3176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3176,
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

_source line 55 · 2026-05-12T01:18:46.988Z_

<details><summary>↩ Tool result · `toolu_01Nyokw4aR5An96RXkgzQS29`</summary>

```text
# CodeSpecBench Paper Summary

**Full Title:** CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation

**Authors:** Zaoyu Chen, Jianbo Dai, Boyu Zhu, Jingdong Wang, Huiming Wang, Xin Xu, Haoyang Yuan, Zhijiang Guo, Xiao-Ming Wu

**Submission Date:** April 14, 2026

**Abstract:**
"Large language models (LLMs) can generate code from natural language, but the extent to which they capture intended program behavior remains unclear." The research introduces CodeSpecBench as a benchmarking framework that evaluates LLMs through an execution-based protocol using preconditions and postconditions as specifications.

## What is CodeSpecBench?

CodeSpecBench is a benchmark designed to assess how well LLMs understand program semantics by measuring their ability to generate executable behavioral specifications. It supports both function-level and repository-level evaluation tasks, encoding specifications as executable Python functions drawn from real-world codebases.

## Connection to Executable Behavioral Specifications

The benchmark addresses a critical gap: while LLMs excel at code generation, "specification generation is substantially more challenging than code generation, indicating that strong coding performance does not necessarily reflect deep understanding of intended program semantics." The framework evaluates both correctness (accepting valid behaviors) and completeness (rejecting invalid behaviors), revealing that even top-performing models achieve only 20.2% accuracy on repository-level tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cd66786-3dbb-4a51-94b4-626f287d380f",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "fec9db2d-9502-42c4-9702-c98a5767a37e",
  "sourceToolAssistantUUID": "3cd66786-3dbb-4a51-94b4-626f287d380f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-12T01:18:48.849Z_

<details><summary>↩ Tool result · `toolu_01JK4Yj9zDb2K8yfLLftrV4P`</summary>

```text
# Paper Summary

**Title:** "Beyond Postconditions: Can Large Language Models infer Formal Contracts for Automatic Software Verification?"

**Authors:** Cedric Richter, Heike Wehrheim

**Date:** Submitted October 14, 2025

**Abstract:** The authors address a key challenge in software verification: the lack of formal specifications in real-world code. They propose using LLMs to generate these specifications, but note that relying only on postconditions often produces false alarms during verification.

## The NL2Contract Task

NL2Contract represents an evolution beyond existing approaches. Rather than generating postconditions alone, it involves "employing LLMs to translate informal natural language into formal functional contracts, consisting of postconditions as well as preconditions."

## How It Works

The approach enhances verification by addressing a gap in prior methods. While previous work focused solely on inferring postconditions from comments and documentation, NL2Contract adds precondition inference. This dual approach serves three functions:

1. **Soundness validation** — ensuring generated contracts are logically valid
2. **Bug detection** — contracts can distinguish between correct and buggy code behavior  
3. **False alarm reduction** — preconditions constrain the input space, reducing verification false positives

The evaluation demonstrates that "verifiers supplied with LLM inferred functional contracts produce fewer false alarms than when provided with postconditions alone," making this a more practical approach for real-world software verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95eb313c-a262-4752-895f-7973dac2d1a4",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "c3904d2b-6486-45fc-abfc-f317cfd35ea6",
  "sourceToolAssistantUUID": "95eb313c-a262-4752-895f-7973dac2d1a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-12T01:18:50.233Z_

<details><summary>↩ Tool result · `toolu_01WNP5UbAAVBPXKeXb1HLyG8`</summary>

```text
# Paper Summary

**Title:** Specification-Guided Repair of Arithmetic Errors in Dafny Programs using LLMs

**Authors:** Valentina Wu, Alexandra Mendes, Alexandre Abreu

**Venue:** arXiv (Computer Science > Software Engineering)

**Date:** Submitted July 4, 2025; Last revised September 8, 2025

**Abstract:** The paper addresses automated debugging of formally verified programs by leveraging specifications as repair oracles.

## Use of Formal Specifications

The approach treats preconditions, postconditions, and invariants as validation criteria rather than relying solely on test suites. The methodology operates through these key steps:

1. **Fault Localization**: Uses Hoare logic to determine program state at each statement, enabling precise identification of where arithmetic errors occur.

2. **LLM-Based Synthesis**: Applies large language models (GPT-4o mini, Llama 3, Mistral 7B, Llemma 7B) to generate candidate fixes informed by formal specifications.

3. **Specification-Guided Validation**: "Formal specifications provide strong correctness criteria, enabling more effective automated repair" compared to traditional test-based approaches.

## Results

Testing on DafnyBench achieved 89.6% fault localization coverage with GPT-4o mini reaching a 74.18% repair success rate, demonstrating the effectiveness of combining formal reasoning with LLM synthesis for automated program repair.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1abbdfc6-69e8-4385-9950-df737ce81aa3",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "698c71b6-6470-4364-b052-483f634648e5",
  "sourceToolAssistantUUID": "1abbdfc6-69e8-4385-9950-df737ce81aa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-12T01:18:52.977Z_

<details><summary>↩ Tool result · `toolu_01Se4P69KKtqUjzwouGubbBA`</summary>

```text
Web search results for query: "CodeSpecBench executable behavioral specification benchmark LLM precondition postcondition invariant 2025"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"[2604.12268] CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/abs/2604.12268"},{"title":"FormalSpecCpp: A Dataset of C++ Formal Specifications created using LLMs","url":"https://arxiv.org/pdf/2502.15217"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"Published in Transactions on Machine Learning Research (01/2025)","url":"https://openreview.net/pdf?id=yBgTVWccIx"},{"title":"Benchmarking Large Language Models for Compositional ...","url":"https://arxiv.org/pdf/2509.23061"},{"title":"Preconditions and Postconditions as Design Constraints ...","url":"https://ieeexplore.ieee.org/iel8/6287639/10820123/11218044.pdf"},{"title":"Transactions on Artificial Intelligence https://www.sciltp.com/journals/tai","url":"https://media.sciltp.com/articles/2505000685/2505000685.pdf"},{"title":"Beyond Postconditions: Can Large Language Models infer Formal Contracts for","url":"https://arxiv.org/pdf/2510.12702"}]

Based on the web search results, here's what I found about CodeSpecBench:

## CodeSpecBench Overview

CodeSpecBench is a benchmark for executable behavioral specification generation with an execution-based evaluation protocol. CodeSpecBench covers both function-level and repository-level tasks, represents specifications as executable Python preconditions and postconditions.

## Key Features

Preconditions formally delimit the set of admissible inputs and program states under which a function is intended to execute, whereas postconditions prescribe the properties that the outputs and resulting program states must satisfy upon termination.

CodeSpecBench covers both function-level and repository-level tasks, represents specifications as executable Python preconditions and postconditions, and evaluates them along the complementary dimensions of correctness and completeness.

## Evaluation and Findings

Experiments on 15 LLMs show that specification generation remains challenging, especially in repository-level settings, where performance drops substantially. 

While models achieve high pass rates in solution generation, their performance drops sharply for executable behavioral specification generation, indicating that solving tasks does not necessarily imply the ability to generate precise executable behavioral constraints.

## Relationship to Other Benchmarks

CodeSpecBench departs from solution generation and instead focuses on specification generation, requiring models to produce explicit, executable preconditions and postconditions that capture intended program behavior rather than directly implementing solutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "579c4624-5f94-48d0-9495-a3651db94adf",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "12751d65-1500-4eda-884d-53ae9b2ee895",
  "sourceToolAssistantUUID": "579c4624-5f94-48d0-9495-a3651db94adf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-12T01:18:54.374Z_

<details><summary>↩ Tool result · `toolu_01Tm1iQb7BuWiBZocGt4okxz`</summary>

```text
Web search results for query: "ClassInvGen class invariant synthesis LLM 2025"

Links: [{"title":"ClassInvGen: Class Invariant Synthesis Using Large Language Models | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99991-8_4"},{"title":"[2502.18917] ClassInvGen: Class Invariant Synthesis using Large Language Models","url":"https://arxiv.org/abs/2502.18917"},{"title":"ClassInvGen: Class Invariant Synthesis using Large Language Models","url":"https://arxiv.org/html/2502.18917"},{"title":"ClassInvGen: Class Invariant Synthesis using Large Language Models","url":"https://openreview.net/pdf?id=7iwJ2ZQS3s"},{"title":"[Literature Review] ClassInvGen: Class Invariant Synthesis using Large Language Models","url":"https://www.themoonlight.io/en/review/classinvgen-class-invariant-synthesis-using-large-language-models"},{"title":"Chuyue Sun's research works","url":"https://www.researchgate.net/scientific-contributions/Chuyue-Sun-2284340737"},{"title":"On the Generation of Invalid Objects for Inferring More Precise Class Invariants | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-10444-1_9"},{"title":"LLM Meets Bounded Model Checking: Neuro-symbolic Loop Invariant Inference","url":"https://www.researchgate.net/publication/385287335_LLM_Meets_Bounded_Model_Checking_Neuro-symbolic_Loop_Invariant_Inference"},{"title":"Programming Language Techniques for Bridging LLM ...","url":"https://dl.acm.org/doi/pdf/10.1145/3759425.3763383"},{"title":"Quokka: Accelerating Program Verification with LLMs via ...","url":"https://arxiv.org/pdf/2509.21629"}]

Based on the search results, here's what I found about ClassInvGen:

## Overview

ClassInvGen is a method for co-generating executable class invariants and test inputs to produce high-quality class invariants for a mainstream language such as C++, leveraging LLMs' ability to synthesize pure functions.

## Research Publication

ClassInvGen: Class Invariant Synthesis Using Large Language Models was published at SAIV 2025 (AI Verification conference), with the paper authored by Chuyue Sun and colleagues.

## Motivation and Context

Formal program specifications in the form of preconditions, postconditions, and class invariants have several benefits for the construction and maintenance of programs, aiding in program understanding due to their unambiguous semantics and allowing them to be enforced dynamically or statically. Prior work has demonstrated the potential of LLMs for synthesizing high-quality method pre/postconditions for Python and Java, but does not consider class invariants.

## Key Approach

When generating invariants in isolation, ClassInvGen produces an average of 25 unique invariants per benchmark with a 77% pass rate against unit tests, and with test co-generation, ClassInvGen successfully eliminates all incorrect invariants, achieving perfect accuracy.

## Evaluation Results

ClassInvGen outperforms a pure LLM-based technique for generating specifications from code as well as prior data-driven invariant inference techniques such as Daikon. The method demonstrates its applicability to real-world code by performing a case study on several classes within a widely used and high-integrity C++ codebase.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b52e939e-a1da-412a-b6f2-615e6f990783",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "1119a2a6-45c9-4174-a4d9-9bd62cf30b07",
  "sourceToolAssistantUUID": "b52e939e-a1da-412a-b6f2-615e6f990783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-12T01:18:57.356Z_

Let me do a few more targeted searches for the remaining important papers I may have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1119a2a6-45c9-4174-a4d9-9bd62cf30b07",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo36ivjzFp74cxHQ2FF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a9c2c78-74c1-4a7f-aab1-095ecbcfb2a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjJp5UeAPfv4zqky16nhoU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4094,
      "cache_read_input_tokens": 27800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4094,
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

_source line 61 · 2026-05-12T01:18:58.311Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017WyY3jyZi7AcAhJDxNmzBg`</summary>

```json
{
  "query": "VeriAct agentic synthesis correct complete formal specifications arXiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a9c2c78-74c1-4a7f-aab1-095ecbcfb2a8",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo36ivjzFp74cxHQ2FF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd653f0f-aa64-4081-9d88-35b1d2a0ff9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjJp5UeAPfv4zqky16nhoU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4094,
      "cache_read_input_tokens": 27800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4094,
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

_source line 62 · 2026-05-12T01:18:59.323Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UBzv98yWNQCq7YbEiECMEu`</summary>

```json
{
  "query": "Quokka accelerating program verification LLM invariant synthesis 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd653f0f-aa64-4081-9d88-35b1d2a0ff9b",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo36ivjzFp74cxHQ2FF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86f79e4e-dcf6-4bec-bf57-6853f27651c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjJp5UeAPfv4zqky16nhoU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4094,
      "cache_read_input_tokens": 27800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4094,
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

_source line 63 · 2026-05-12T01:19:00.197Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011L6JNRyK4o7BAgbfNz1ima`</summary>

```json
{
  "query": "LLM-assisted structured spec-driven engineering repository-level code generation arXiv 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86f79e4e-dcf6-4bec-bf57-6853f27651c0",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo36ivjzFp74cxHQ2FF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8811e04f-da69-4325-a979-744842f6eda8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjJp5UeAPfv4zqky16nhoU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4094,
      "cache_read_input_tokens": 27800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4094,
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

_source line 64 · 2026-05-12T01:19:00.954Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016uSdKtMMrViUREcx3kKTbe`</summary>

```json
{
  "query": "\"code repair\" OR \"code generation\" LLM postcondition precondition execution feedback iterative refinement 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8811e04f-da69-4325-a979-744842f6eda8",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo36ivjzFp74cxHQ2FF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb008515-d93e-447c-a6a7-6571ed4e9d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjJp5UeAPfv4zqky16nhoU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4094,
      "cache_read_input_tokens": 27800,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4094
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 27800,
          "cache_creation_input_tokens": 4094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4094,
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

_source line 65 · 2026-05-12T01:19:05.684Z_

<details><summary>↩ Tool result · `toolu_017WyY3jyZi7AcAhJDxNmzBg`</summary>

```text
Web search results for query: "VeriAct agentic synthesis correct complete formal specifications arXiv 2604"

Links: [{"title":"[2604.00280] VeriAct: Beyond Verifiability -- Agentic Synthesis of Correct and Complete Formal Specifications","url":"https://arxiv.org/abs/2604.00280"},{"title":"VeriAct: Beyond Verifiability – Agentic Synthesis of Correct and Complete Formal Specifications","url":"https://arxiv.org/html/2604.00280v1"},{"title":"VeriAct: Beyond Verifiability – Agentic Synthesis of Correct and","url":"https://arxiv.org/pdf/2604.00280"},{"title":"Towards an Agentic LLM-based Approach to Requirement Formalization from Unstructured Specifications","url":"https://arxiv.org/html/2604.18228v1"},{"title":"Formalizing the Safety, Security, and Functional Properties ...","url":"https://arxiv.org/pdf/2510.14133"},{"title":"VERI-SURE: A Contract-Aware Multi-Agent Framework with Temporal","url":"https://arxiv.org/pdf/2601.19747v1"},{"title":"Architect in the Loop Agentic Hardware Design and Verification","url":"https://arxiv.org/html/2512.00016v1"},{"title":"Agentic Program Verification","url":"https://arxiv.org/html/2511.17330v1"},{"title":"Exploring the Agentic Frontier of Verilog Code Generation","url":"https://arxiv.org/html/2603.19347"},{"title":"[2604.10392] Intent-aligned Formal Specification Synthesis via Traceable Refinement","url":"https://arxiv.org/abs/2604.10392"}]

I found the paper you're looking for! Here are the key details about the VeriAct paper from arXiv:

## VeriAct: Beyond Verifiability – Agentic Synthesis of Correct and Complete Formal Specifications

**Paper ID:** arXiv 2604.00280

**Authors:** Md Rakib Hossain Misu and 2 other authors

**Publication Date:** March 31, 2026

### Overview

Formal specifications play a central role in ensuring software reliability and correctness, but automatically synthesizing high-quality formal specifications remains a challenging task, often requiring domain expertise.

### Key Contributions

The paper addresses a critical gap in specification synthesis:

1. **Problem Identification:** Recent work has applied large language models to generate specifications in Java Modeling Language (JML), reporting high verification pass rates, but the question of whether passing a verifier means that the specification is actually correct and complete remains open.

2. **Spec-Harness Framework:** The authors propose Spec-Harness, an evaluation framework that measures specification correctness and completeness through symbolic verification, revealing that a large fraction of verifier-accepted specifications, including optimized ones, are in fact incorrect or incomplete.

3. **VeriAct Solution:** VeriAct is a verification-guided agentic framework that iteratively synthesizes and repairs specifications through a closed loop of LLM-driven planning, code execution, verification, and Spec-Harness feedback.

### Results

Experiments on two benchmark datasets show that VeriAct outperforms both prompt-based and prompt-optimized baselines, producing specifications that are not only verifiable but also correct and complete.

You can access the paper at: https://arxiv.org/abs/2604.00280


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd653f0f-aa64-4081-9d88-35b1d2a0ff9b",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "9dee45a9-a350-48fa-ae73-f06d18db01f2",
  "sourceToolAssistantUUID": "cd653f0f-aa64-4081-9d88-35b1d2a0ff9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-12T01:19:06.170Z_

<details><summary>↩ Tool result · `toolu_01UBzv98yWNQCq7YbEiECMEu`</summary>

```text
Web search results for query: "Quokka accelerating program verification LLM invariant synthesis 2025"

Links: [{"title":"Quokka: Accelerating Program Verification with LLMs via Invariant Synthesis","url":"https://arxiv.org/html/2509.21629v2"},{"title":"[2509.21629] Quokka: Accelerating Program Verification with LLMs via Invariant Synthesis","url":"https://arxiv.org/abs/2509.21629"},{"title":"Quokka: Accelerating Program Verification with LLMs via Invariant Synthesis | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.21629"},{"title":"Quokka: Accelerating Program Verification with LLMs via Invariant Synthesis | OpenReview","url":"https://openreview.net/forum?id=nq03VvBki2"},{"title":"Quokka: Accelerating Program Verification with LLMs via Invariant Synthesis | Gist.Science","url":"https://gist.science/paper/2509.21629"},{"title":"GitHub - Anjiang-Wei/Quokka · GitHub","url":"https://github.com/Anjiang-Wei/InvBench"},{"title":"Quokka: Accelerating Program Verification with LLMs via ...","url":"https://arxiv.org/pdf/2509.21629"},{"title":"Tarun Suresh","url":"https://tarsur909.github.io/"},{"title":"Accelerating Program Verification with LLMs via Invariant ...","url":"https://www.semanticscholar.org/paper/Quokka:-Accelerating-Program-Verification-with-LLMs-Wei-Suresh/0c8be4908bcdbe7b49a2d1ce7860eec6072a6516"},{"title":"InvBench: Can LLMs Accelerate Program Verification with Invariant Synthesis?","url":"https://arxiv.org/html/2509.21629v1"}]

Based on the search results, here's what I found about Quokka:

## Overview

Quokka is a first-order and effective framework for LLM-based invariant synthesis that provides sound evaluation while achieving state-of-the-art speedup results. The research investigates whether large language models (LLMs) can accelerate program verification by generating useful loop invariants.

## Key Approach

Quokka adopts a simpler and evaluation-centric design that directly validates whether each LLM-generated invariant helps prove the target assertion, rather than treating LLM outputs as noisy material requiring extensive post-processing. Unlike previous work that designs complex, highly customized algorithms, Quokka employs a simple and principled verification procedure.

## Evaluation and Results

A dataset of 866 instances derived from the most recent edition of the software verification competition SV-COMP (Beyer and Strejček, 2025) was constructed. The evaluation included 9 state-of-the-art LLMs across multiple model families, and Quokka consistently outperformed all prior LLM-based verifiers, achieving speedups of at least 1.2× on 81 instances compared to 39 instances for the previous best approach.

## Models Evaluated

The benchmarking included Claude models from Anthropic, GPT models from OpenAI, and models from the Qwen and LLaMA families.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86f79e4e-dcf6-4bec-bf57-6853f27651c0",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "c26849c6-5753-4b53-887a-1df91ae47141",
  "sourceToolAssistantUUID": "86f79e4e-dcf6-4bec-bf57-6853f27651c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-12T01:19:07.277Z_

<details><summary>↩ Tool result · `toolu_011L6JNRyK4o7BAgbfNz1ima`</summary>

```text
Web search results for query: "LLM-assisted structured spec-driven engineering repository-level code generation arXiv 2605"

Links: [{"title":"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/html/2605.02455"},{"title":"[2605.02455] LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/abs/2605.02455"},{"title":"[2605.02455v1] LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/abs/2605.02455v1"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"},{"title":"Towards Specification-Driven LLM-Based Generation of Embedded Automotive Software","url":"https://arxiv.org/html/2411.13269v1"},{"title":"Knowledge Graph Based Repository-Level Code Generation","url":"https://arxiv.org/html/2505.14394v1"},{"title":"Understanding Specification-Driven Code Generation with ...","url":"https://arxiv.org/pdf/2601.03878"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"SemanticForge: Repository-Level Code Generation through Semantic Knowledge Graphs and Constraint Satisfaction","url":"https://arxiv.org/html/2511.07584"}]

Based on the search results, I found the paper you're looking for:

## LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering

The paper presents a vision for moving from file-level Large Language Model (LLM) coding assistance to repository-level automation through structured spec-driven engineering (SSDE).

**Key Contributions:**

The paper proposes structured spec-driven engineering (SSDE), a paradigm that leverages structured artifacts to guide LLM generation, arguing that structured specifications as LLM inputs make high-quality, repository-level code generation a tangible goal, while at the same time offering superior verifiability.

**Motivation:**

While studies show LLMs perform well at generating isolated functions or files, their reliability declines for larger or repository-level systems, and natural language prompts commonly used in current SDE workflows are often found to be lossy in communication due to inherent ambiguity of natural language.

**Methodology:**

The paper investigates the feasibility of this vision through a pilot study generating Model-View-Controller (MVC) business logic for three software systems using five LLMs.

**Results:**

The pilot study shows that 70% of errors from the naïve approach can be detected to enable automated corrections.

The paper (arXiv 2605.02455) was recently published and will be presented at FSE 2026 in Montreal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8811e04f-da69-4325-a979-744842f6eda8",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "7d5901d9-fa93-4776-ba5e-f2c7f5cba41d",
  "sourceToolAssistantUUID": "8811e04f-da69-4325-a979-744842f6eda8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-12T01:19:09.690Z_

<details><summary>↩ Tool result · `toolu_016uSdKtMMrViUREcx3kKTbe`</summary>

```text
Web search results for query: ""code repair" OR "code generation" LLM postcondition precondition execution feedback iterative refinement 2025 2026"

Links: [{"title":"Code Repair with LLMs gives an Exploration-Exploitation Tradeoff | OpenReview","url":"https://openreview.net/forum?id=o863gX6DxA"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks","url":"https://arxiv.org/html/2604.10508"},{"title":"CYCLE: Learning to Self-Refine the Code Generation","url":"https://arxiv.org/html/2403.18746v1"},{"title":"Iterative Refinement of Project-Level Code Context for Precise Code Generation with Compiler Feedback","url":"https://arxiv.org/html/2403.16792v1"},{"title":"Code Repair with LLMs gives an Exploration-Exploitation Tradeoff Hao Tang","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d5c56ec4f69c9a473089b16000d3f8cd-Paper-Conference.pdf"},{"title":"LLMLOOP: Improving LLM-Generated Code and Tests ...","url":"https://valerio-terragni.github.io/assets/pdf/ravi-icsme-2025.pdf"},{"title":"FeedbackEval: A Benchmark for Evaluating Large Language","url":"https://arxiv.org/pdf/2504.06939"},{"title":"REX | Code Repair with LLMs gives an Exploration-Exploitation Tradeoff","url":"https://haotang1995.github.io/projects/rex"}]

I found comprehensive research on code repair and generation with LLMs involving preconditions, postconditions, execution feedback, and iterative refinement. Here are the key findings:

## Iterative Refinement and Execution Feedback

Iteratively improving and repairing source code with large language models (LLMs), known as refinement, has emerged as a popular way of generating programs that would be too complex to construct in one shot. Given a bank of test cases, together with a candidate program, an LLM can improve that program by being prompted with failed test cases.

## Preconditions and Postconditions

Using this approach on the 4 programs with overly weak preconditions or overly strong postconditions, Claude Opus 4.5 produced correct solutions for all of them. Recent research also shows an iterative feedback loop verifies 79% of 251 C programs within five attempts.

## Self-Repair Across Modern Models (2025-2026)

Recent work investigates iterative self-repair (feeding execution errors back to the model for correction) across seven models spanning three families and both open-weight and proprietary providers: Llama 3.1 8B, Llama 3.3 70B, Llama 4 Scout (MoE, 16 experts), Llama 4 Maverick (MoE, 128 experts), Qwen3 32B, Gemini 2.5 Flash, and Gemini 2.5 Pro. On HumanEval (164 problems) and MBPP Sanitized (257 problems) with up to five attempts, self-repair universally improves pass rates: +4.9 to +17.1 pp on HumanEval and +16.0 to +30.0 pp on MBPP.

## Exploration-Exploitation Tradeoff

Refinement exposes an explore-exploit tradeoff: exploit by refining the program that passes the most test cases, or explore by refining a lesser considered program. A smart algorithm (REx) saves 10-80% of LLM requests compared to baseline methods, depending on the domain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb008515-d93e-447c-a6a7-6571ed4e9d2b",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "03d40e52-69e6-4524-8c80-cf6d94addb3a",
  "sourceToolAssistantUUID": "fb008515-d93e-447c-a6a7-6571ed4e9d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-12T01:19:12.658Z_

Let me also fetch a couple more papers that seem highly relevant, and run a final round of searches to be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03d40e52-69e6-4524-8c80-cf6d94addb3a",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo4EBv6Z9VBr6wxaG8S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cb68df6-0052-4174-8024-8962c19d2d28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bS9xysptxof2gxFRNYhEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4059,
      "cache_read_input_tokens": 31894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4059,
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

_source line 70 · 2026-05-12T01:19:14.680Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012xSFSK1REBsGSLPHFvavFJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.00280",
  "prompt": "Extract the full title, authors, date, and abstract. What is VeriAct? What is Spec-Harness? How do they synthesize and evaluate formal specifications?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cb68df6-0052-4174-8024-8962c19d2d28",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo4EBv6Z9VBr6wxaG8S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8d9dd9b-8130-4e8c-bb21-ed6c9bdb59a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bS9xysptxof2gxFRNYhEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4059,
      "cache_read_input_tokens": 31894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4059,
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

_source line 71 · 2026-05-12T01:19:16.074Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NYbSCmq83PtTdt4d3MczHS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.14631",
  "prompt": "Extract the full title, authors, date, and abstract. How does StoryCoder work? Does it use formal specifications or just narrative reformulation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8d9dd9b-8130-4e8c-bb21-ed6c9bdb59a9",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo4EBv6Z9VBr6wxaG8S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13c18e7d-7019-49e2-be38-62e22e930586",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bS9xysptxof2gxFRNYhEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4059,
      "cache_read_input_tokens": 31894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4059,
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

_source line 72 · 2026-05-12T01:19:16.547Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01411ueEYjfWJBUz6J5fVYg5`</summary>

```json
{
  "query": "CURRANTE specification tests function LLM code generation tool 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13c18e7d-7019-49e2-be38-62e22e930586",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo4EBv6Z9VBr6wxaG8S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fe7ffc6-760a-4821-a073-00b0bad48213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bS9xysptxof2gxFRNYhEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4059,
      "cache_read_input_tokens": 31894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4059,
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

_source line 73 · 2026-05-12T01:19:17.134Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RWPoDYAPqXSKkvHYjWEgtP`</summary>

```json
{
  "query": "AgentCoder multi-agent iterative testing code generation specification 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fe7ffc6-760a-4821-a073-00b0bad48213",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo4EBv6Z9VBr6wxaG8S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a15634d-2d97-45f5-8bdb-b789a8fd5921",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bS9xysptxof2gxFRNYhEo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4059,
      "cache_read_input_tokens": 31894,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4059
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 31894,
          "cache_creation_input_tokens": 4059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4059,
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

_source line 74 · 2026-05-12T01:19:19.730Z_

<details><summary>↩ Tool result · `toolu_012xSFSK1REBsGSLPHFvavFJ`</summary>

```text
# VeriAct: Research Paper Summary

**Full Title:** VeriAct: Beyond Verifiability -- Agentic Synthesis of Correct and Complete Formal Specifications

**Authors:** Md Rakib Hossain Misu, Iris Ma, Cristina V. Lopes

**Submission Date:** March 31, 2026

**Abstract:** The paper addresses a critical gap in automated formal specification generation. While prior work reported high verification pass rates for JML specifications, the authors demonstrate that "a large fraction of verifier-accepted specifications...are in fact incorrect or incomplete." They propose two key contributions to address this problem.

## What is VeriAct?

VeriAct is "a verification-guided agentic framework that iteratively synthesizes and repairs specifications through a closed loop of LLM-driven planning, code execution, verification, and Spec-Harness feedback." It moves beyond simple verification acceptance by ensuring specifications are both correct and complete.

## What is Spec-Harness?

Spec-Harness functions as "an evaluation framework that measures specification correctness and completeness through symbolic verification." It detects constraints that under- or over-specify inputs and outputs in ways traditional verifiers miss.

## Synthesis and Evaluation Approach

The methodology combines prompt-based generation with iterative refinement. Rather than relying solely on verifier acceptance, they employ Spec-Harness feedback to guide continuous improvement, achieving specifications that satisfy both verifiability and correctness criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8d9dd9b-8130-4e8c-bb21-ed6c9bdb59a9",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "277afe4a-36c8-4f12-a9d4-61f3b0ab6f58",
  "sourceToolAssistantUUID": "f8d9dd9b-8130-4e8c-bb21-ed6c9bdb59a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-12T01:19:20.368Z_

<details><summary>↩ Tool result · `toolu_01NYbSCmq83PtTdt4d3MczHS`</summary>

```text
# StoryCoder Paper Details

**Full Title:** StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation

**Authors:** Geonhui Jang, Dongyoon Han, YoungJoon Yoo

**Date:** Submitted April 16, 2026

**Abstract:** The research presents a framework that converts programming challenges into coherent natural language narratives rather than leaving problem conditions scattered. According to the abstract, "Each narrative consists of three components: a task overview, constraints, and example test cases, guided by the selected algorithm and genre."

## How StoryCoder Works

StoryCoder employs **narrative reformulation rather than formal specifications**. The approach transforms code generation questions by organizing fragmented information into coherent natural language stories. Rather than injecting formal logic or structured symbolic representations, the method focuses on narrative coherence and genre alignment to guide models toward correct algorithmic strategies.

The framework demonstrated consistent improvements across 11 models, with "an average gain of 18.7% in zero-shot pass@10" on multiple benchmarks. The analyses indicate that benefits stem from narrative coherence itself, suggesting that improved problem representation through storytelling—not formal specifications—drives the performance gains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13c18e7d-7019-49e2-be38-62e22e930586",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "69112693-0afc-4375-8ba3-c12a7192173b",
  "sourceToolAssistantUUID": "13c18e7d-7019-49e2-be38-62e22e930586",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-12T01:19:23.639Z_

<details><summary>↩ Tool result · `toolu_01411ueEYjfWJBUz6J5fVYg5`</summary>

```text
Web search results for query: "CURRANTE specification tests function LLM code generation tool 2025"

Links: [{"title":"Understanding Specification-Driven Code Generation with ...","url":"https://arxiv.org/pdf/2601.03878"},{"title":"Specification-Driven Code Generation with LLMs — An Empirical Study on Telling AI What to Build","url":"https://codenote.net/en/posts/specification-driven-code-generation-llm-empirical-study/"},{"title":"[2601.03878] Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design","url":"https://arxiv.org/abs/2601.03878"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878"},{"title":"Multi-Step Generation of Test Specifications using Large ...","url":"https://aclanthology.org/2025.acl-industry.11.pdf"},{"title":"Quality Assurance of LLM-generated Code: Addressing Non-Functional Quality Characteristics","url":"https://arxiv.org/html/2511.10271v1"},{"title":"Automated Test Generation Using Large Language Models","url":"https://www.mdpi.com/2306-5729/10/10/156"},{"title":"LLM-Powered Test Case Generation: Enhancing Coverage and Efficiency","url":"https://www.frugaltesting.com/blog/llm-powered-test-case-generation-enhancing-coverage-and-efficiency"},{"title":"Enhancing LLM-Based Test Generation by Eliminating Covered Code","url":"https://arxiv.org/html/2602.21997"},{"title":"LLMs for Automated Unit Test Generation and Assessment ...","url":"https://arxiv.org/pdf/2511.20403"}]

Based on the search results, here's what I found about CURRANTE:

## CURRANTE Overview

CURRANTE is a Visual Studio Code (VS Code) plugin that implements a TDD workflow leveraging LLMs to generate code based on user-provided specifications formally defined through test cases.

## Three-Phase Workflow

The tool guides developers through three sequential stages—Specification, Tests, and Function—allowing them to define requirements, generate and refine test suites, and produce functions that satisfy those tests. More specifically:

1. **Specification Phase**: The user starts by defining the problem requirements in a structured way, via a TOML file, which is designed to be human-readable and easy to edit.

2. **Tests Phase**: Test suites are generated and refined based on the specification. The LLM proposes test cases, and developers review and modify them. This phase often reveals gaps in the specification.

3. **Code Generation Phase**: The final phase is delegated entirely to the LLM, which generates the code and verifies its execution results against the test suite.

## Research Study

The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2. 32 professional developers (2+ years of experience) solve medium-difficulty problems from LiveCodeBench, a continuously updated benchmark comprising real-world programming problems sourced from platforms like LeetCode and CodeForces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fe7ffc6-760a-4821-a073-00b0bad48213",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "f330e0cd-7670-470c-8552-dffce8b111e5",
  "sourceToolAssistantUUID": "9fe7ffc6-760a-4821-a073-00b0bad48213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-12T01:19:23.903Z_

<details><summary>↩ Tool result · `toolu_01RWPoDYAPqXSKkvHYjWEgtP`</summary>

```text
Web search results for query: "AgentCoder multi-agent iterative testing code generation specification 2024"

Links: [{"title":"[2312.13010] AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation","url":"https://arxiv.org/abs/2312.13010"},{"title":"AgentCoder: Multiagent-Code Generation with Iterative Testing and Optimisation","url":"https://arxiv.org/html/2312.13010v2"},{"title":"AgentCoder: Multi-Agent Code Generation with Effective Testing and Self-optimisation","url":"https://arxiv.org/html/2312.13010v3"},{"title":"AgentCoder: Multi-Agent Code Generation with Effective ...","url":"https://arxiv.org/pdf/2312.13010"},{"title":"GitHub - huangd1999/AgentCoder: AgentCoder: multi-agent code generation framework. · GitHub","url":"https://github.com/huangd1999/AgentCoder"},{"title":"AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation","url":"https://arxiv.org/html/2312.13010v1"},{"title":"[2312.13010v3] AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation","url":"https://arxiv.org/abs/2312.13010v3"},{"title":"Paper page - AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation","url":"https://huggingface.co/papers/2312.13010"},{"title":"AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AgentCoder:-Multi-Agent-based-Code-Generation-with-Huang-Bu/1db56be01aeb44ca0f3fcebb45180cab1e4cd82e"},{"title":"MapCoder: Multi-Agent Code Generation for Competitive ...","url":"https://aclanthology.org/2024.acl-long.269.pdf"}]

Based on the search results, here's what I found about AgentCoder:

## Overview

AgentCoder is a multi-agent framework comprising a programmer agent, test designer agent, and test executor agent that addresses challenges in balancing code generation with effective test case generation and execution.

## Framework Architecture

The agents collaborate to generate high-quality code snippets, design comprehensive test cases, and ensure the correctness of the generated code through an iterative feedback loop.

The framework operates through the following process:

1. **Programmer Agent**: The programmer agent focuses on code generation and refinement based on the test executor agent's feedback.

2. **Test Designer Agent**: The test designer agent is designed to generate basic test cases, cover edge test cases, and cover large scale inputs.

3. **Test Executor Agent**: The test executor agent collects code snippets and test cases, executes them in the local environment to obtain feedback about whether the code passes tests and any error messages.

## Iterative Testing and Refinement

The refinement process is iterative, with the programmer agent continuously enhancing the code based on feedback until the code successfully passes all test cases.

## Performance Results

AgentCoder achieves 77.4% and 89.1% pass@1 in HumanEval-ET and MBPP-ET with GPT-3.5, while SOTA baselines obtain only 69.5% and 63.0%.

The paper was initially published in December 2023 with updates through May 2024, and is available on arXiv and GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a15634d-2d97-45f5-8bdb-b789a8fd5921",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "56053199-9474-477a-a179-67f8058c7b66",
  "sourceToolAssistantUUID": "2a15634d-2d97-45f5-8bdb-b789a8fd5921",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-12T01:19:40.441Z_

Now let me do one final round of searches for a few more potential competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56053199-9474-477a-a179-67f8058c7b66",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo5HBHMyBNEWds8EKGU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "206d1cef-ac76-46d7-917c-639d6fb9d2bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXMN3sGUgFpckRr9nwmhdH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2773,
      "cache_read_input_tokens": 35953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2773,
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

_source line 79 · 2026-05-12T01:19:41.849Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FhpxdqwPKebjecoBcrKx2X`</summary>

```json
{
  "query": "VERI-SURE contract-aware multi-agent framework temporal LLM verification 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "206d1cef-ac76-46d7-917c-639d6fb9d2bb",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo5HBHMyBNEWds8EKGU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd7c2a51-e98c-4f98-95e2-377519da845f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXMN3sGUgFpckRr9nwmhdH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2773,
      "cache_read_input_tokens": 35953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2773,
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

_source line 80 · 2026-05-12T01:19:42.211Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014R7rYPWjEmW6ELm1BrZu1n`</summary>

```json
{
  "query": "LLM code generation refinement using formal contracts specifications not test cases 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd7c2a51-e98c-4f98-95e2-377519da845f",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo5HBHMyBNEWds8EKGU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7927242-ac9b-4000-8595-8cfa9204abc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXMN3sGUgFpckRr9nwmhdH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2773,
      "cache_read_input_tokens": 35953,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2773
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 35953,
          "cache_creation_input_tokens": 2773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2773,
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

_source line 81 · 2026-05-12T01:19:49.638Z_

<details><summary>↩ Tool result · `toolu_01FhpxdqwPKebjecoBcrKx2X`</summary>

```text
Web search results for query: "VERI-SURE contract-aware multi-agent framework temporal LLM verification 2025"

Links: [{"title":"[2601.19747] Veri-Sure: A Contract-Aware Multi-Agent Framework with Temporal Tracing and Formal Verification for Correct RTL Code Generation","url":"https://arxiv.org/abs/2601.19747"},{"title":"Veri-Sure: A Contract-Aware Multi-Agent Framework with Temporal Tracing and Formal Verification for Correct RTL Code Generation","url":"https://arxiv.org/html/2601.19747v1"},{"title":"(PDF) Veri-Sure: A Contract-Aware Multi-Agent Framework with Temporal Tracing and Formal Verification for Correct RTL Code Generation","url":"https://www.researchgate.net/publication/400119159_Veri-Sure_A_Contract-Aware_Multi-Agent_Framework_with_Temporal_Tracing_and_Formal_Verification_for_Correct_RTL_Code_Generation"},{"title":"VERI-SURE: A Contract-Aware Multi-Agent Framework with Temporal","url":"https://arxiv.org/pdf/2601.19747v1"},{"title":"[2601.19747v1] Veri-Sure: A Contract-Aware Multi-Agent Framework with Temporal Tracing and Formal Verification for Correct RTL Code Generation","url":"https://arxiv.org/abs/2601.19747v1"},{"title":"GitHub - xyjoey/Veri-Sure: Contract-Aware RTL Code Generation Agents with Temporal Tracing, Slicing and Formal Verification · GitHub","url":"https://github.com/xyjoey/Veri-Sure"},{"title":"Enforcing Temporal Constraints for LLM Agents | OpenReview","url":"https://openreview.net/forum?id=VeRehDnGJJ"},{"title":"Agent Contracts: A Formal Framework for Resource-Bounded Autonomous AI Systems (Full)","url":"https://arxiv.org/html/2601.08815v1"},{"title":"VeriPlan: Integrating Formal Verification and LLMs into End-User Planning | Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3706598.3714113"},{"title":"Verification-Aware Planning for Multi-Agent LLM Systems: Why Agent Coordination Fails and How VERIMAP Improves Reliability","url":"https://megagon.ai/verification-aware-planning-multi-agent-llm/"}]

I found detailed information about VERI-SURE. Here are the search results:

## VERI-SURE: Contract-Aware Multi-Agent Framework

VERI-SURE is a multi-agent framework that establishes a design contract to align agents' intent and uses a patching mechanism guided by static dependency slicing to perform precise, localized repairs.

### Purpose and Context

In the rapidly evolving field of Electronic Design Automation (EDA), the deployment of Large Language Models (LLMs) for Register-Transfer Level (RTL) design has emerged as a promising direction. However, silicon-grade correctness remains bottlenecked by: (i) limited test coverage and reliability of simulation-centric evaluation, (ii) regressions and repair hallucinations introduced by iterative debugging, and (iii) semantic drift as intent is reinterpreted across agent handoffs.

### Key Features

By integrating a multi-branch verification pipeline that combines trace-driven temporal analysis with formal verification consisting of assertion-based checking and boolean equivalence proofs, Veri-Sure enables functional correctness beyond pure simulations.

### Performance

VERI-SURE introduces VerilogEval-v2-EXT, extending the original benchmark with 53 more industrial-grade design tasks and stratified difficulty levels, and achieves state-of-the-art verified-correct RTL code generation performance, surpassing standalone LLMs and prior agentic systems.

The paper was published on arXiv on January 27, 2026, and is authored by Jiale Liu and two other authors. The framework combines temporal tracing with formal verification to generate correct hardware description language (RTL) code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd7c2a51-e98c-4f98-95e2-377519da845f",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "7796d7de-a284-4042-b156-ffbbb66dc558",
  "sourceToolAssistantUUID": "bd7c2a51-e98c-4f98-95e2-377519da845f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-12T01:19:50.579Z_

<details><summary>↩ Tool result · `toolu_014R7rYPWjEmW6ELm1BrZu1n`</summary>

```text
Web search results for query: "LLM code generation refinement using formal contracts specifications not test cases 2024 2025"

Links: [{"title":"Light and shadows of smart contract development with LLMs - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425026284"},{"title":"Guiding LLM-based Smart Contract Generation with Finite State Machine","url":"https://www.ijcai.org/proceedings/2025/0653.pdf"},{"title":"Contracts for Large Language Model APIs:","url":"https://tanzimhromel.com/assets/pdf/llm-api-contracts.pdf"},{"title":"LLM-Based Code Translation Needs Formal Compositional Reasoning Alvin Cheung","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-174.pdf"},{"title":"Leveraging LLMs for Formal Software Requirements: Challenges and Prospects","url":"https://ceur-ws.org/Vol-4142/paper11.pdf"},{"title":"Beyond Postconditions: Can Large Language Models infer Formal Contracts for","url":"https://arxiv.org/pdf/2510.12702"},{"title":"SolGen: Secure Smart Contract Code Generation Using Large Language Models Via Masked Prompting | Proceedings of the 18th Innovations in Software Engineering Conference","url":"https://dl.acm.org/doi/10.1145/3717383.3717394"},{"title":"Do Large Language Models Respect Contracts? ...","url":"https://arxiv.org/pdf/2510.12047"},{"title":"PropertyGPT: LLM-driven Formal Verification of Smart ...","url":"https://www.ndss-symposium.org/wp-content/uploads/2025-1357-paper.pdf"},{"title":"Automated Generation of Code Contracts – Generative AI to the Rescue?","url":"https://scg.unibe.ch/archive/papers/Grei24a-CodeContracts.pdf"}]

Based on the search results, here's what I found regarding LLM code generation refinement using formal contracts specifications rather than test cases:

## Key Research Areas

### 1. **Contract-Based Code Refinement vs. Test-Based Approaches**

Mainstream automated testing and existing test-generation benchmarks often overlook latent defects from missing contract checks. Recent research has begun addressing this gap by focusing on formal contracts (preconditions, postconditions, invariants) as primary specifications rather than test cases.

One framework generates code under contract specification prompts that include functional descriptions and natural language paraphrases of contracts, and generates contract-violating test cases to rigorously assess whether LLM-generated code snippets enforce both functional specifications and explicit contracts.

### 2. **Smart Contract Generation with Formal Methods**

Recent work investigates the effective integration of large language models (LLMs) with formal method based tools to automatically generate secure, non-vulnerable Solidity smart contract code based on given specifications.

### 3. **Formal Specification Inference**

NL2Contract evaluates the ability of LLMs to generate specifications consistent with a natural language description, modeling the LLM as a function that maps a natural language description to formal specifications.

### 4. **Contract Validation and Verification**

Intermediate contract or test checking approaches validate functions or modules against unit tests or pre/post-conditions once they are complete. Online strategies such as contract or test checking and verifier-in-the-loop pruning with symbolic execution or SMT solvers prevent partial outputs from violating local specifications.

### 5. **Automated Contract Generation**

Research examines how to fine-tune LLMs for contract generation and systematically evaluates model performances, achieving remarkably good results despite relatively small datasets for fine-tuning.

These studies from 2024-2025 show a growing research focus on using formal contracts as primary specifications for refining LLM-generated code, moving beyond traditional test-case-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7927242-ac9b-4000-8595-8cfa9204abc4",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a082fc3bdac9c393e",
  "type": "user",
  "uuid": "e418285a-fbcf-404e-9abb-917ebdc6249d",
  "sourceToolAssistantUUID": "d7927242-ac9b-4000-8595-8cfa9204abc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 83 · 2026-05-12T01:21:43.492Z_

I now have a comprehensive picture. Here is the consolidated report.

---

## Papers Using Program Properties/Contracts/Specifications (Not Just Tests) to Improve LLM Code Generation or Repair (2024--2026)

Below are the papers found, organized from most to least directly competitive with ExeSpec (a method using execution-grounded behavioral specifications like preconditions, postconditions, and invariants to improve LLM code tasks at inference time).

---

### TIER 1: Closest Competitors (directly use executable specs to guide/evaluate LLM code generation)

**1. CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation**
- Authors: Zaoyu Chen, Jianbo Dai, Boyu Zhu, et al.
- arXiv: [2604.12268](https://arxiv.org/abs/2604.12268), April 2026
- What it does: Introduces a benchmark that evaluates LLMs on generating *executable* preconditions and postconditions (as Python functions) for both function-level and repository-level tasks. Evaluates correctness (accepting valid behaviors) and completeness (rejecting invalid behaviors).
- Key finding: Specification generation is substantially harder than code generation -- even top models achieve only 20.2% accuracy on repository-level specification tasks. Strong coding performance does not imply deep understanding of intended program semantics.
- Relevance to ExeSpec: **Extremely high.** This is the benchmark side of exactly what ExeSpec does. If ExeSpec generates executable behavioral specs and uses them, CodeSpecBench measures how well LLMs can do this. A direct evaluation target.

**2. Property-Generated Solver (PGS) -- "Use Property-Based Testing to Bridge LLM Code Generation and Validation"**
- Authors: Lehan He, Zeren Chen, Zhe Zhang, Xiang Gao, Lu Sheng
- arXiv: [2506.18315](https://arxiv.org/abs/2506.18315), June 2025 (revised May 2026)
- What it does: Two-agent system (Generator + Tester). The Tester defines high-level abstract properties (invariants, functional constraints), translates them into executable property-checking code, generates diverse test inputs, and provides *structurally minimal* counterexamples as feedback to the Generator for iterative refinement.
- Results: 23.1--37.3% relative pass@1 improvement over TDD methods; 1.4--1.6x higher bug-fix rates; up to 13.4% absolute gain.
- Relevance to ExeSpec: **Very high -- probably the closest direct competitor.** PGS uses property-based testing (abstract properties/invariants, not I/O test cases) to iteratively refine LLM-generated code at inference time. The key difference from ExeSpec may be that PGS uses LLM-generated properties rather than execution-grounded behavioral specifications derived from program behavior.

**3. ContractEval + PACT -- "Do Large Language Models Respect Contracts?"**
- Authors: Soohan Lim, Joonghyuk Hahn, Hyunwoo Park, Sang-Ki Ko, Yo-Sub Han
- arXiv: [2510.12047](https://arxiv.org/abs/2510.12047), October 2025 (revised April 2026)
- What it does: Builds ContractEval benchmark (364 tasks on HumanEval+/MBPP+) that evaluates whether LLM-generated code enforces input preconditions via assertions. Uses a neuro-symbolic pipeline (LLM + SMT solver) to generate contract-violation test inputs. PACT is a framework to evaluate and enforce contract-adherence alongside functional correctness.
- Key finding: Standard prompting yields **0% contract satisfaction**. Even with explicit contracts in prompts, only 23--41%. Few-shot contract-violation examples raise it to 49--53%.
- Relevance to ExeSpec: **Very high.** ContractEval directly measures whether LLMs can generate code that satisfies formal contracts (pre/postconditions). The enforcement techniques (few-shot CVT examples) are inference-time interventions -- exactly the kind of thing ExeSpec competes with.

**4. Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation**
- Authors: Zihao Xu, Xiao Cheng, Jingling Xue, Yuekang Li
- Venue: Agents4Science 2025, [OpenReview](https://openreview.net/forum?id=6pr7BUGkLp)
- What it does: Lightweight, deterministic (T=0) orchestration where the LLM: (1) designs a compact spec schema, (2) instantiates it from the docstring, (3) resolves ambiguities via Q&A, (4) generates code only from the confirmed spec. The spec is *model-authored* -- the LLM creates its own preferred specification language.
- Results: GPT-4o 87% -> 92%, Claude 3.7 92% -> 94% on HumanEval pass@1.
- Relevance to ExeSpec: **High.** Self-Spec uses specifications at inference time to improve code generation, but the specs are *not execution-grounded* -- they are LLM-generated text specs. ExeSpec's advantage would be that its specs are executable and verified against actual program behavior.

**5. Preconditions and Postconditions as Design Constraints for LLM Code Generation**
- Authors: (Embry-Riddle Aeronautical University thesis + IEEE Access publication)
- Venue: IEEE Access 2025, [IEEE Xplore](https://ieeexplore.ieee.org/document/11218044/)
- What it does: Systematically studies how explicit preconditions and postconditions (Design-by-Contract paradigm) in prompts affect class-level code generation. Tests with Python and C++ across multiple LLMs.
- Key finding: Incorporating explicit design constraints during prompting *significantly* boosts initial generation accuracy (pass@k), especially for weaker/smaller models.
- Relevance to ExeSpec: **High.** Directly studies the value of DbC-style specs for LLM code generation. However, this is an empirical study of prompt-based specification rather than an inference-time refinement loop. ExeSpec goes further by using execution to validate spec adherence.

---

### TIER 2: Strong Related Work (use formal specs/contracts in the LLM pipeline, but different focus)

**6. Beyond Postconditions: NL2Contract -- "Can Large Language Models infer Formal Contracts for Automatic Software Verification?"**
- Authors: Cedric Richter, Heike Wehrheim
- arXiv: [2510.12702](https://arxiv.org/abs/2510.12702), October 2025
- What it does: Uses LLMs to translate NL docstrings into formal functional contracts (preconditions + postconditions as executable Python assertions). Evaluated for soundness, bug-detection power, and false-alarm reduction in software verifiers.
- Key finding: LLM-inferred contracts are generally sound; adding preconditions (not just postconditions) substantially reduces verifier false alarms.
- Relevance to ExeSpec: **Moderate-high.** NL2Contract generates executable contract specifications from NL, which is upstream of what ExeSpec does. If ExeSpec uses execution to ground specs, NL2Contract shows that LLM-generated contracts can be effective oracles. Complementary/competitive depending on how ExeSpec generates its specs.

**7. VeriAct: Beyond Verifiability -- Agentic Synthesis of Correct and Complete Formal Specifications**
- Authors: Md Rakib Hossain Misu, Iris Ma, Cristina V. Lopes
- arXiv: [2604.00280](https://arxiv.org/abs/2604.00280), March 2026
- What it does: Proposes Spec-Harness (evaluation framework measuring specification correctness and completeness via symbolic verification) and VeriAct (agentic framework that iteratively synthesizes and repairs JML specifications through a closed loop of LLM planning, code execution, verification, and Spec-Harness feedback).
- Key finding: A large fraction of verifier-accepted specifications are actually incorrect or incomplete. VeriAct outperforms prompt-based and prompt-optimized baselines.
- Relevance to ExeSpec: **Moderate-high.** VeriAct uses an execution-in-the-loop approach to iteratively refine formal specifications (not code), which is related but inverted -- ExeSpec uses specs to improve code, VeriAct uses execution to improve specs.

**8. AutoSpec -- "Enchanting Program Specification Synthesis by Large Language Models using Static Analysis and Program Verification"**
- Authors: (Multiple, from arXiv [2404.00762](https://arxiv.org/abs/2404.00762))
- arXiv: 2404.00762, 2024
- What it does: Bottom-up synthesis of preconditions, postconditions, loop invariants, and assigned variables using LLMs + verifier feedback. Uses program decomposition and few-shot prompting. Validates candidate specs each round to avoid error accumulation.
- Results: Verifies 79% of programs, 1.592x improvement over existing works. Successfully applied to real-world X509-parser project.
- Relevance to ExeSpec: **Moderate.** AutoSpec synthesizes formal specifications (the same kind ExeSpec uses), but the goal is program verification rather than code generation/repair. However, the spec synthesis approach could be combined with ExeSpec-style inference-time use.

**9. ClassInvGen: Class Invariant Synthesis using Large Language Models**
- Authors: Chuyue Sun et al.
- Venue: SAIV 2025, [Springer](https://link.springer.com/chapter/10.1007/978-3-031-99991-8_4)
- What it does: Co-generates executable class invariants and test inputs for C++ using LLMs. Test co-generation eliminates all incorrect invariants, achieving perfect accuracy. Outperforms Daikon (data-driven invariant inference).
- Relevance to ExeSpec: **Moderate.** Directly generates executable invariants (one of ExeSpec's spec types) and uses execution to validate them. Focused on class-level invariants rather than pre/postconditions for code generation.

**10. Counterexample Guided Program Repair Using Zero-Shot Learning and MaxSAT-based Fault Localization**
- Authors: P. Orvalho, M. Janota, V. Manquinho
- Venue: AAAI 2025, [Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/32046)
- What it does: Combines MaxSAT-based fault localization with LLM zero-shot learning in a CEGIS (counterexample-guided inductive synthesis) loop. Localizes faults, creates program sketches, LLM fills in missing parts, counterexamples guide iterative refinement.
- Results: Repairs more programs with smaller fixes than state-of-the-art symbolic repair tools across 1,431 incorrect student programs.
- Relevance to ExeSpec: **Moderate.** Uses formal counterexamples (not just test failures) as feedback for LLM repair -- related to ExeSpec's use of specification-based feedback. However, it uses test suites as the oracle rather than behavioral specifications.

**11. Specification-Guided Repair of Arithmetic Errors in Dafny Programs using LLMs**
- Authors: Valentina Wu, Alexandra Mendes, Alexandre Abreu
- arXiv: [2507.03659](https://arxiv.org/abs/2507.03659), July 2025
- What it does: Uses Dafny's formal specifications (preconditions, postconditions, invariants) as repair oracles. Hoare-logic-based fault localization identifies where arithmetic errors occur; LLMs synthesize candidate fixes.
- Results: 89.6% fault localization, 74.18% repair success (GPT-4o mini).
- Relevance to ExeSpec: **Moderate.** Directly uses pre/postconditions and invariants to guide LLM-based repair, but limited to Dafny (verification-aware language) and arithmetic errors only.

---

### TIER 3: Related but More Distant

**12. From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing**
- Venue: FSE Companion 2025 (LLanMER workshop), [ACM DL](https://dl.acm.org/doi/10.1145/3696630.3728702)
- What it does: Applies PBT as an *evaluation* strategy (not a generation improvement). Tests StarCoder and CodeLlama on MBPP/HumanEval. Finds that 30--32% of solutions only partially adhere to correctness properties, 18--23% fail outright.
- Relevance to ExeSpec: **Moderate.** Evaluation-only (does not use properties to improve generation). But establishes the case that PBT catches bugs that standard unit tests miss, motivating ExeSpec's approach.

**13. ReDeFo: Requirements Development and Formalization for Reliable Code Generation**
- Venue: ASE 2025 NIER track, arXiv: [2508.18675](https://arxiv.org/abs/2508.18675)
- What it does: Three-agent framework (Analyst, Formalizer, Coder) that formalizes NL requirements into formal specs before code generation. Bridges ambiguous NL and precise executable code.
- Relevance to ExeSpec: **Moderate.** Uses formal specifications in the generation pipeline but focuses on requirements engineering rather than execution-grounded behavioral specs.

**14. CURRANTE + Specification-Driven Code Generation Empirical Study**
- Venue: SANER 2026 (registered report), arXiv: [2601.03878](https://arxiv.org/abs/2601.03878)
- What it does: VS Code plugin implementing a three-stage workflow (Specification -> Tests -> Function) for LLM-assisted code generation. Studies 32 professional developers on LiveCodeBench.
- Relevance to ExeSpec: **Low-moderate.** Uses specs to structure the workflow but generates tests from specs, then generates code from tests -- not directly using executable behavioral specs as ExeSpec does.

**15. Structured Spec-Driven Engineering (SSDE) for Repository-Level Code Generation**
- arXiv: [2605.02455](https://arxiv.org/abs/2605.02455), May 2026 (FSE 2026)
- What it does: Proposes using structured specifications (not NL) as inputs for repository-level LLM code generation. Pilot study with MVC systems shows 70% of naive-approach errors can be detected for automated correction.
- Relevance to ExeSpec: **Low-moderate.** Advocates specs over NL for LLM generation but focuses on structured artifacts (schemas, models) rather than executable behavioral specifications.

**16. StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation**
- Authors: Geonhui Jang, Dongyoon Han, YoungJoon Yoo
- arXiv: [2604.14631](https://arxiv.org/abs/2604.14631), April 2026
- What it does: Converts code problems into coherent natural language narratives (task overview + constraints + examples). Average 18.7% gain in zero-shot pass@10 across 11 models.
- Relevance to ExeSpec: **Low.** Uses narrative reformulation, NOT formal specifications. Included because it was requested in the search queries. Not a competitor to ExeSpec.

**17. Quokka: Accelerating Program Verification with LLMs via Invariant Synthesis**
- arXiv: [2509.21629](https://arxiv.org/abs/2509.21629), September 2025
- What it does: Framework for LLM-based loop invariant synthesis to accelerate program verification. Evaluation-centric design that directly checks whether invariants help prove assertions.
- Relevance to ExeSpec: **Low-moderate.** Generates invariants (one of ExeSpec's spec types) but for verification acceleration, not code generation/repair.

**18. Veri-Sure: Contract-Aware Multi-Agent Framework for RTL Code Generation**
- arXiv: [2601.19747](https://arxiv.org/abs/2601.19747), January 2026
- What it does: Multi-agent framework using design contracts + formal verification (assertion-based checking, boolean equivalence proofs) for hardware RTL code generation. Uses temporal tracing and dependency slicing for precise repairs.
- Relevance to ExeSpec: **Low.** Contract-aware code generation but for hardware (Verilog), not software. Interesting architectural parallel but different domain.

---

### Summary of Closest Competitors to ExeSpec

The papers most directly competitive with ExeSpec's approach of using execution-grounded behavioral specifications (preconditions, postconditions, invariants) to improve LLM code generation/repair at inference time are:

1. **PGS (Property-Generated Solver)** -- Closest overall. Uses LLM-generated abstract properties (invariants, constraints) with execution-based validation and minimal counterexample feedback for iterative code refinement. The main differentiator for ExeSpec would be whether its specs are *execution-grounded* (derived from actual program behavior) vs. PGS's LLM-generated properties.

2. **ContractEval/PACT** -- Closest on the evaluation/enforcement side. Benchmarks contract satisfaction and shows few-shot contract-violation examples can boost enforcement at inference time.

3. **CodeSpecBench** -- Closest on the benchmark side. Directly evaluates LLMs on generating executable preconditions and postconditions, establishing that spec generation is much harder than code generation.

4. **Self-Spec** -- Closest lightweight competitor. Uses model-authored specifications at inference time but without execution grounding.

5. **NL2Contract / "Beyond Postconditions"** -- Generates executable contracts (pre+postconditions) from NL for verification, showing the pipeline from NL to executable specs is feasible.

Sources:
- [PGS / Property-Generated Solver](https://arxiv.org/abs/2506.18315)
- [ContractEval](https://arxiv.org/abs/2510.12047)
- [CodeSpecBench](https://arxiv.org/abs/2604.12268)
- [Self-Spec](https://openreview.net/forum?id=6pr7BUGkLp)
- [From Prompts to Properties (FSE 2025)](https://dl.acm.org/doi/10.1145/3696630.3728702)
- [Preconditions/Postconditions as Design Constraints (IEEE Access)](https://ieeexplore.ieee.org/document/11218044/)
- [NL2Contract / Beyond Postconditions](https://arxiv.org/abs/2510.12702)
- [VeriAct](https://arxiv.org/abs/2604.00280)
- [AutoSpec](https://arxiv.org/abs/2404.00762)
- [ClassInvGen (SAIV 2025)](https://arxiv.org/abs/2502.18917)
- [CEGIS Repair (AAAI 2025)](https://ojs.aaai.org/index.php/AAAI/article/view/32046)
- [Spec-Guided Dafny Repair](https://arxiv.org/abs/2507.03659)
- [ReDeFo (ASE 2025)](https://arxiv.org/abs/2508.18675)
- [CURRANTE / Spec-Driven Study (SANER 2026)](https://arxiv.org/abs/2601.03878)
- [SSDE (FSE 2026)](https://arxiv.org/abs/2605.02455)
- [StoryCoder](https://arxiv.org/abs/2604.14631)
- [Quokka](https://arxiv.org/abs/2509.21629)
- [Veri-Sure](https://arxiv.org/abs/2601.19747)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e418285a-fbcf-404e-9abb-917ebdc6249d",
  "isSidechain": true,
  "agentId": "a082fc3bdac9c393e",
  "requestId": "req_011Cawo7F2bvdoDfrt4DbQJv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88670a90-327a-479c-a96d-26ab37d9f047",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ef2g7MbAiKHTcnXLKDbGWF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2204,
      "cache_read_input_tokens": 38726,
      "output_tokens": 4963,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2204
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4963,
          "cache_read_input_tokens": 38726,
          "cache_creation_input_tokens": 2204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2204,
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
