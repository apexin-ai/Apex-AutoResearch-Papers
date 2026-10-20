# Research conversation: Search for recent (2025-2026) papers that might compete with or overlap with "ExeSpec" — a training-free method that use

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 91
- **Recorded user turns:** 1
- **Tool calls:** 40
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9b53bfb6b47df469.jsonl`
- **Structured JSON:** [`75a894e626dba5d43ab4.json`](../../sessions/75/75a894e626dba5d43ab4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

91 recorded events

### User

_source line 1 · 2026-05-12T02:30:18.244Z_

Search for recent (2025-2026) papers that might compete with or overlap with "ExeSpec" — a training-free method that uses execution-grounded behavioral specifications (preconditions, postconditions, invariants) as intermediate reasoning for LLM code tasks. I need to find works the proposal might have missed.

Use WebSearch with these queries:
1. "execution grounded specification code generation LLM 2025 2026" 
2. "property-based testing LLM code refinement inference time 2025 2026"
3. "behavioral specification code debugging LLM 2025 2026"
4. "structured intermediate representation code generation 2025 2026"
5. "contract-guided code generation LLM 2025 2026"
6. "specification verification code repair LLM 2026"
7. "site:arxiv.org code specification execution grounding 2026"

For any highly relevant papers you find, use WebFetch to read their abstracts. I'm looking for papers that:
- Use specifications/properties/contracts as intermediate reasoning for code LLMs
- Apply execution-based verification of LLM-generated specifications
- Are training-free inference-time methods for code tasks
- Were published in 2025-2026

Report all findings with titles, venues, dates, and how they relate to ExeSpec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "3d92c4eb-40f8-4484-a5d4-1528da1581ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T02:30:18.247Z_

```json
{
  "parentUuid": "3d92c4eb-40f8-4484-a5d4-1528da1581ad",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
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
  "uuid": "44c11313-2ca1-4007-a9f7-db7ecd2f85a2",
  "timestamp": "2026-05-12T02:30:18.247Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T02:30:22.111Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44c11313-2ca1-4007-a9f7-db7ecd2f85a2",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtUtH8Y3qA5QJSGbNtD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9db0b89-44a9-4167-be0d-b67bdc368e1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184zjVsm8iGYS8RNq7HEWt2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 852,
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

_source line 4 · 2026-05-12T02:30:22.264Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qgr39kdDEnpPyK8rxPeB6q`</summary>

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
  "parentUuid": "b9db0b89-44a9-4167-be0d-b67bdc368e1d",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtUtH8Y3qA5QJSGbNtD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12de88f8-b7a3-4ee7-92fc-406923caab8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184zjVsm8iGYS8RNq7HEWt2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 8223,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 852,
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

_source line 5 · 2026-05-12T02:30:22.269Z_

<details><summary>↩ Tool result · `toolu_01Qgr39kdDEnpPyK8rxPeB6q`</summary>

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
  "parentUuid": "12de88f8-b7a3-4ee7-92fc-406923caab8f",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "8c83bc21-f040-45ec-8a62-485590af38cc",
  "sourceToolAssistantUUID": "12de88f8-b7a3-4ee7-92fc-406923caab8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T02:30:26.614Z_



Now let me run all seven searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c83bc21-f040-45ec-8a62-485590af38cc",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtVHi2pAhj4nYZiivSS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1eda2794-abcd-42a4-9bf5-4888129a14ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XosEAMCt6TQmXfzrWq43uR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 7 · 2026-05-12T02:30:27.624Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P5NCPf4TFWywD2G1QCYKXY`</summary>

```json
{
  "query": "execution grounded specification code generation LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eda2794-abcd-42a4-9bf5-4888129a14ba",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtVHi2pAhj4nYZiivSS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0c47756-8067-4d8d-818d-f80559e3141c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XosEAMCt6TQmXfzrWq43uR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 8 · 2026-05-12T02:30:28.101Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QCffuij9HSehcgtQsoftjk`</summary>

```json
{
  "query": "property-based testing LLM code refinement inference time 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0c47756-8067-4d8d-818d-f80559e3141c",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtVHi2pAhj4nYZiivSS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b260bb5-d9e7-4c4a-b054-18da80161adb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XosEAMCt6TQmXfzrWq43uR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 9 · 2026-05-12T02:30:28.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MvLt6qbw4wYHsT8EAwcFSJ`</summary>

```json
{
  "query": "behavioral specification code debugging LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b260bb5-d9e7-4c4a-b054-18da80161adb",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtVHi2pAhj4nYZiivSS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41c6353e-8996-4ca6-8d43-fd59eafeb359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XosEAMCt6TQmXfzrWq43uR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 10 · 2026-05-12T02:30:29.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RWn5mSN3rEbkik6e4E3bBd`</summary>

```json
{
  "query": "structured intermediate representation code generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41c6353e-8996-4ca6-8d43-fd59eafeb359",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtVHi2pAhj4nYZiivSS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45b5148b-d486-480a-b74d-28c615f22452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XosEAMCt6TQmXfzrWq43uR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 11 · 2026-05-12T02:30:29.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P5334dzaMH2jMXpXAn5Ves`</summary>

```json
{
  "query": "contract-guided code generation LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45b5148b-d486-480a-b74d-28c615f22452",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtVHi2pAhj4nYZiivSS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3eabecca-3cb3-4e67-ba12-6e3567d4e00d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XosEAMCt6TQmXfzrWq43uR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 12 · 2026-05-12T02:30:29.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R7FReUbNmN3HuRjRh89U1G`</summary>

```json
{
  "query": "specification verification code repair LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eabecca-3cb3-4e67-ba12-6e3567d4e00d",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtVHi2pAhj4nYZiivSS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a7fe747-54a0-4b80-99ba-96c9284f9459",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XosEAMCt6TQmXfzrWq43uR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 13 · 2026-05-12T02:30:30.625Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BMu6GFUfqAGccHTd1Hzz6W`</summary>

```json
{
  "query": "site:arxiv.org code specification execution grounding 2026",
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
  "parentUuid": "7a7fe747-54a0-4b80-99ba-96c9284f9459",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtVHi2pAhj4nYZiivSS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "182f4d7f-f542-44ac-aec2-a549c21e679c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XosEAMCt6TQmXfzrWq43uR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9075,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 386,
          "cache_read_input_tokens": 9075,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 14 · 2026-05-12T02:30:35.892Z_

<details><summary>↩ Tool result · `toolu_01QCffuij9HSehcgtQsoftjk`</summary>

```text
Web search results for query: "property-based testing LLM code refinement inference time 2025 2026"

Links: [{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"From Exploration to Specification: LLM-Based Property Generation for Mobile App Testing","url":"https://arxiv.org/html/2604.13463v1"},{"title":"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing | Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/3696630.3728702"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"[2506.18315] Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/abs/2506.18315"},{"title":"FMI_SU_Yotkova_Kastreva at SemEval-2026 Task 13: Lightweight Detection of LLM-Generated Code via Stylometric Signals","url":"https://arxiv.org/html/2605.04157"},{"title":"LLM Testing in 2026: Top Methods and Strategies - Confident AI","url":"https://www.confident-ai.com/blog/llm-testing-in-2024-top-methods-and-strategies"},{"title":"LLM-Based Property-Based Test Generation for Guardrailing Cyber-Physical Systems | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-032-07132-3_3"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"LLM Developments 2025: How Efficiency and RLVR Broke the Scaling Obsession | Efficient Coder","url":"https://www.xugj520.cn/en/archives/llm-2025-developments-rlvr-efficiency.html"}]

Based on the search results, here are the key findings on property-based testing, LLM code refinement, and inference time:

## Property-Based Testing & LLM Code Refinement

Property-Based Testing (PBT) validates high-level program properties or invariants instead of relying on specific input-output examples, and these properties are often simpler to define and verify than directly predicting exhaustive test oracles.

Property-Generated Solver employs two collaborative LLM-based agents: a Generator dedicated to code generation and iterative refinement, and a Tester that manages the PBT life-cycle and formulates semantically rich feedback from property violations, providing a robust mechanism for steering LLMs towards more correct and generalizable code.

Experimental results demonstrate that Property-Generated Solver achieves substantial pass@1 improvements, ranging from 23.1% to 37.3% relative gains over established TDD methods.

## LLM Property Generation for Mobile Apps

PropGen is an automated approach for constructing properties of mobile apps that reduces the need for manual property specification by exploring app functionalities and deriving properties from behavioral evidence, with a feedback-driven refinement technique to refine imprecise properties exposed during testing.

## Inference-Time Scaling in 2025-2026

There will be more focus on inference-time scaling in 2026, which means spending more time and money after training when letting the LLM generate the answer.

Progress stems from inference-time scaling that lets models think longer, with DeepSeekMath-V2 achieving IMO gold medal performance by generating extensive reasoning chains during inference, allowing models to explore multiple solution paths, self-critique, and refine answers before delivering the final result.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b260bb5-d9e7-4c4a-b054-18da80161adb",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "292d9da0-f8f7-45ba-9f41-155c5de1d058",
  "sourceToolAssistantUUID": "1b260bb5-d9e7-4c4a-b054-18da80161adb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T02:30:35.941Z_

<details><summary>↩ Tool result · `toolu_01MvLt6qbw4wYHsT8EAwcFSJ`</summary>

```text
Web search results for query: "behavioral specification code debugging LLM 2025 2026"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"HWE-Bench: Benchmarking LLM Agents on Real-World Hardware Bug Repair Tasks","url":"https://arxiv.org/html/2604.14709v1"},{"title":"Best LLM for Coding in 2026: Ranked by Real Benchmarks | WhatLLM.org","url":"https://whatllm.org/best-llm-for-coding"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"LLM-based Behaviour Driven Development for Hardware Design","url":"https://arxiv.org/html/2512.17814"},{"title":"Spec-driven development. Unpacking one of 2025’s key new… | by Thoughtworks | Medium","url":"https://thoughtworks.medium.com/spec-driven-development-d85995a81387"},{"title":"Bridging the Gap between User Intent and LLM: A Requirement Alignment Approach for Code Generation","url":"https://arxiv.org/html/2604.16198v1"},{"title":"My LLM coding workflow going into 2026 | by Addy Osmani | Medium","url":"https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Proceedings of Machine Learning Research vol vvv:1–34, 2025","url":"https://arxiv.org/pdf/2602.12083"}]

Based on the search results, here's what I found on behavioral specification code debugging and LLMs in 2025-2026:

## Behavioral Specifications for LLMs

The ability of LLMs to generate executable behavioral specifications remains underexplored, and generating executable behavioral specifications is substantially more challenging for LLMs than generating code solutions. Executable behavioral specifications characterize program behavior through preconditions and postconditions, collectively constituting an explicit, executable interface for representing program semantics.

## Recent Benchmarks and Approaches

Recent approaches like FormalBench and VERINA (both from 2025) rely on deductive verification and exclude repository-level tasks. A new benchmark called CodeSpecBench has been developed to address these limitations by evaluating LLMs' ability to generate executable behavioral specifications from natural-language descriptions.

## LLM Performance on Debugging Tasks

In hardware debugging specifically, recent evaluations include proprietary models like GPT-5.4 and Claude Opus 4.6/Sonnet 4.6, along with open-source models like DeepSeek V3.2.

## Spec-Driven Development Trends

Spec-driven development remains an emerging practice as 2025 draws to a close. Best practices involve brainstorming a detailed specification with the AI and outlining a step-by-step plan before writing code, compiling comprehensive specifications containing requirements, architecture decisions, data models, and testing strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41c6353e-8996-4ca6-8d43-fd59eafeb359",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "1520518d-97ee-4a61-bcbf-f8d10fdf8611",
  "sourceToolAssistantUUID": "41c6353e-8996-4ca6-8d43-fd59eafeb359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T02:30:36.521Z_

<details><summary>↩ Tool result · `toolu_01P5334dzaMH2jMXpXAn5Ves`</summary>

```text
Web search results for query: "contract-guided code generation LLM 2025 2026"

Links: [{"title":"Light and shadows of smart contract development with LLMs - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425026284"},{"title":"2026 LLM x Law Hackathon #6 Winners - CodeX - Stanford Law School","url":"https://law.stanford.edu/2026/04/27/2026-llm-x-law-hackathon-6-winners/"},{"title":"2025: The year in LLMs","url":"https://simonwillison.net/2025/Dec/31/the-year-in-llms/"},{"title":"LLM-Generated Code in 2025: Trends and Predictions - Revelo","url":"https://www.revelo.com/blog/llm-code-generation-2025-trends-predictions-human-data"},{"title":"My LLM coding workflow going into 2026 | by Addy Osmani | Medium","url":"https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"5 Open-Source Coding LLMs You Can Run Locally in 2026","url":"https://www.labellerr.com/blog/best-coding-llms/"},{"title":"Best LLM for Coding - Vellum","url":"https://www.vellum.ai/best-llm-for-coding"},{"title":"Home | LLM4Code 2026","url":"https://llm4code.github.io/"}]

Based on the web search results, here's what I found about contract-guided code generation with LLMs in 2025-2026:

## Smart Contract Generation from Legal Agreements

A recent study evaluates the potential of Large Language Models (LLMs) for automated smart contract generation from legal agreements. The work systematically assesses the capabilities of four leading commercial LLMs – gpt-4-turbo (OpenAI), claude-3.5-sonnet (Anthropic), mistral-large (MistralAI), and gemini-1.5-pro (Google) – across a diverse range of legal agreements with varying complexity.

### Key Findings

The results reveal a performance hierarchy with claude-3.5-sonnet and gpt-4-turbo consistently outperforming mistral-large and gemini-1.5-pro, particularly when handling complex agreements such as mortgage note agreement and property sales agreement. However, a nonlinear relationship has been observed between contract complexity and model performance, with even top-performing models showing significant degradation when processing intricate legal structures.

### Challenges and Limitations

Although achieving syntactic correctness has become increasingly feasible, ensuring functional completeness and security remains challenging, as evidenced by high-impact vulnerabilities detected across all generated smart contracts.

## 2026 Practical Applications

In a 2026 hackathon context, ClauseWise is a logic-based middleware designed to bridge the gap between static legal text and active financial systems. It transforms contracts from passive documents into executable code, allowing for automated enforcement and "what-if" scenario modeling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3eabecca-3cb3-4e67-ba12-6e3567d4e00d",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "a44af80c-705b-422d-be90-3b35929d8003",
  "sourceToolAssistantUUID": "3eabecca-3cb3-4e67-ba12-6e3567d4e00d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T02:30:38.135Z_

<details><summary>↩ Tool result · `toolu_01RWn5mSN3rEbkik6e4E3bBd`</summary>

```text
Web search results for query: "structured intermediate representation code generation 2025 2026"

Links: [{"title":"Intermediate representation - Wikipedia","url":"https://en.wikipedia.org/wiki/Intermediate_representation"},{"title":"CS143 Handout 22 Summer 2010 July 23rd, 2010 Intermediate Representation","url":"https://web.stanford.edu/class/archive/cs/cs143/cs143.1128/handouts/230%20Intermediate%20Rep.pdf"},{"title":"Structured Chain-of-Thought Prompting for Code Generation","url":"https://ligechina.github.io/My%20Papers/2025%20-%20TOSEM%20-%20Structured%20Chain-of-Thought%20Prompting%20for%20Code%20Generation.pdf"},{"title":"Intermediate Representation (IR)","url":"https://www.emergentmind.com/topics/intermediate-representation-ir"},{"title":"Intermediate Representations (IRs)","url":"https://www.emergentmind.com/topics/intermediate-representations-irs"},{"title":"Representation of Intermediate Code Generation- a Compiler","url":"https://www.jetir.org/papers/JETIR1806056.pdf"},{"title":"Intermediate Code Generation in Compiler Design - GeeksforGeeks","url":"https://www.geeksforgeeks.org/compiler-design/intermediate-code-generation-in-compiler-design/"},{"title":"The Graph’s Apprentice: Teaching an LLM Low-Level Knowledge for Circuit","url":"https://www.ijcai.org/proceedings/2025/1033.pdf"},{"title":"Vol.:(0123456789) The Journal of Supercomputing (2025) 81:418","url":"https://inspirehep.net/files/81c0d5c771823878cea10c3f74f9d81a"},{"title":"Intermediate Representation - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/computer-science/intermediate-representation"}]

Based on the search results, here's what I found regarding structured intermediate representation code generation in 2025-2026:

## Recent Developments in Structured Intermediate Representation

### Structured Chain-of-Thought for Code Generation (2025)

A recent approach uses Structured Chain-of-Thought (SCoT), which denotes several intermediate reasoning steps constructed by programming structures. SCoT prompting asks LLMs first to generate an SCoT and then output the final code. The motivation is that human developers benefit from structured programming in coding, relying on three programming structures (sequential, branch, and loop structures) to design and implement high-quality programs.

### Modern IR Advances and Applications

Intermediate representations form the core abstraction layer of modern compilation, transformation, and analysis ecosystems, enabling both generic and specialized optimizations, efficient static analysis, and portable code generation.

### Emerging Focus Areas for 2025-2026

Several key research directions are active:

- **LLM Reasoning with IRs**: Current LLMs can parse IR syntax and extract high-level structure but fail at fine-grained reasoning required for control flow, loop semantics, and dynamic execution in IRs, necessitating IR-specific pre-training, control-flow-sensitive neural architectures, and curated benchmarks.

- **Multi-level and Domain-Specific IRs**: Multi-level IRs (e.g., OpenQASM3→MLIR→QIR) support the full quantum-classical hybrid programming abstraction with value-semantics, structured control, and retargetable lowering. Specialized IRs such as Ensemble-IR encode entire families of circuits using symbolic and distributional gate constructs.

- **Multilingual Code Generation**: Aligning source code with language-independent IRs during LLM training yields better multilingual code generation and prompt consistency, outperforming models trained solely on source code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45b5148b-d486-480a-b74d-28c615f22452",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "8844a5ab-aa93-4f36-af25-20252521fffd",
  "sourceToolAssistantUUID": "45b5148b-d486-480a-b74d-28c615f22452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T02:30:38.843Z_

<details><summary>↩ Tool result · `toolu_01R7FReUbNmN3HuRjRh89U1G`</summary>

```text
Web search results for query: "specification verification code repair LLM 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"[2603.00897] Detect Repair Verify for Securing LLM Generated Code: A Multi-Language Empirical Study","url":"https://arxiv.org/abs/2603.00897"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=svyjoTT47M"},{"title":"CktFormalizer: Autoformalization of Natural Language into Circuit Representations","url":"https://arxiv.org/html/2605.07782"},{"title":"Verifying LLM-Generated Code in the Context of Software Verification with Ada/SPARK","url":"https://arxiv.org/html/2502.07728v1"},{"title":"Automatic Program Repair Using Large Language Models in Model-Based Development","url":"https://www.scitepress.org/Papers/2026/144911/144911.pdf"},{"title":"Detect–Repair–Verify for Securing LLM-Generated Code: A Multi-Language Empirical Study","url":"https://arxiv.org/html/2603.00897"},{"title":"AutoVerus: Automated Proof Generation for Rust Code","url":"https://arxiv.org/pdf/2409.13082"},{"title":"Lemur: Integrating Large Language Models in Automated Program Verification","url":"https://mathai2023.github.io/papers/28.pdf"},{"title":"Code Repair with LLMs gives an Exploration-Exploitation Tradeoff Hao Tang","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d5c56ec4f69c9a473089b16000d3f8cd-Paper-Conference.pdf"}]

Based on the search results, here are key findings on specification, verification, code repair, and LLMs in 2026:

## Recent Research Overview

Recent work in this area includes "A Systematic Literature Review on Large Language Models for Automated Program Repair" published in TOSEM 2026, which indicates this is an active research area.

## Key 2026 Work

A March 2026 paper titled "Detect Repair Verify for Securing LLM Generated Code: A Multi-Language Empirical Study" addresses a Detect–Repair–Verify (DRV) loop workflow that detects issues, applies fixes, and verifies the result, studying this workflow for project-level artifacts and addressing gaps including the lack of project-level benchmarks, limited evidence on pipeline-level effectiveness, unclear reliability of detection reports as repair guidance, and uncertain repair trustworthiness.

SimLLMRepair is an LLM-based APR system designed for Simulink models that converts Simulink models into structured JSON format and employs design intent-driven Retrieval-Augmented Generation, demonstrating 88.8% fault localization and 50.0% repair success rates.

## Related Areas

CktFormalizer is a framework that redirects LLM-driven hardware generation through a dependently-typed HDL embedded in Lean 4, where dependent types encode constraints and turn hardware defects into compile-time errors that guide iterative repair.

Research explores using formal software verification, specifically the SPARK framework for Ada, to ensure reliability of LLM-generated code, with Marmaragan being a tool that leverages LLMs to generate SPARK annotations for existing programs enabling formal verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a7fe747-54a0-4b80-99ba-96c9284f9459",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "32055ce5-c672-4900-aaaa-21eb90ebd721",
  "sourceToolAssistantUUID": "7a7fe747-54a0-4b80-99ba-96c9284f9459",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T02:30:39.241Z_

<details><summary>↩ Tool result · `toolu_01BMu6GFUfqAGccHTd1Hzz6W`</summary>

```text
Web search results for query: "site:arxiv.org code specification execution grounding 2026"

Links: [{"title":"Spec Kit Agents: Context-Grounded Agentic Workflows","url":"https://arxiv.org/html/2604.05278"},{"title":"[2402.08073] Grounding Data Science Code Generation with Input-Output Specifications","url":"https://arxiv.org/abs/2402.08073"},{"title":"Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis","url":"https://arxiv.org/html/2604.10800v1"},{"title":"Understanding Specification-Driven Code Generation with ...","url":"https://arxiv.org/pdf/2601.03878"},{"title":"Grounding Data Science Code Generation with Input-Output Specifications","url":"https://arxiv.org/html/2402.08073v2"},{"title":"[2410.02089] RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning","url":"https://arxiv.org/abs/2410.02089"},{"title":"Agentic Scientific Simulation: Execution-Grounded Model Construction and Reconstruction","url":"https://arxiv.org/html/2603.00214v1"},{"title":"[2604.10800v1] Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis","url":"https://arxiv.org/abs/2604.10800v1"},{"title":"Execution Guided Line-by-Line Code Generation Boaz Lavon Shahar Katz Lior Wolf","url":"https://arxiv.org/pdf/2506.10948"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"}]

I've performed the web search for your query on arXiv. Here are the key results found:

## Recent Papers on Code Specification, Execution, and Grounding (2026)

Several recent papers address the intersection of code specification, execution, and grounding:

1. **Spec Kit Agents: Context-Grounded Agentic Workflows** - GitHub's Spec Kit operationalizes a staged workflow (Specify → Implement), optionally gated by plan review. This validates intermediate artifacts (SPEC/PLAN/TASKS) before code generation, catching hallucinated APIs, invalid paths, and architectural mismatches early.

2. **Verify Before You Fix: Agentic Execution Grounding for Cross-Language Code Analysis** - A unified cross-language vulnerability lifecycle framework built around three LLM-driven reasoning stages—hybrid structural-semantic detection, execution-grounded agentic validation, and validation-aware iterative repair—governed by a strict invariant: no repair action is taken without execution-based confirmation of exploitability.

3. **Agentic Scientific Simulation: Execution-Grounded Model Construction** - An LLM embedded within a structured interpret–act–validate loop around a simulator allows enforcement capability to be exploited directly: the agent mediates between high-level modelling intent and executable specifications.

4. **Understanding Specification-Driven Code Generation with LLMs** - A three-phase TDD workflow where the user inputs the specification, guides the LLM in generating test cases, and the final code generation phase is delegated entirely to the LLM, which generates the code and verifies its execution results against the test suite.

These papers collectively demonstrate an emerging focus on grounding code generation in execution feedback and specification validation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "182f4d7f-f542-44ac-aec2-a549c21e679c",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "949ad089-5adf-4396-9570-10336d1f0558",
  "sourceToolAssistantUUID": "182f4d7f-f542-44ac-aec2-a549c21e679c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T02:30:43.087Z_

<details><summary>↩ Tool result · `toolu_01P5NCPf4TFWywD2G1QCYKXY`</summary>

```text
Web search results for query: "execution grounded specification code generation LLM 2025 2026"

Links: [{"title":"RLEF: GROUNDING CODE LLMS IN EXECUTION FEEDBACK WITH REINFORCEMENT LEARNING","url":"https://www.arxiv.org/pdf/2410.02089"},{"title":"RLEF: GROUNDING CODE LLMS IN EXECUTION ...","url":"https://openreview.net/pdf?id=zPPy79qKWe"},{"title":"GitHub - luka-group/Execution-Grounded-Reasoning: [EMNLP 2025] Code Execution as Grounded Supervision for LLM Reasoning","url":"https://github.com/luka-group/Execution-Grounded-Reasoning"},{"title":"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=PzSG5nKe1q"},{"title":"Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis","url":"https://arxiv.org/html/2604.10800v1"},{"title":"Code Execution as Grounded Supervision for LLM Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1260/"},{"title":"Grounding Code Generation with Input-Output Specifications | OpenReview","url":"https://openreview.net/forum?id=rO8QOHrCeA"},{"title":"Code Execution as Grounded Supervision for LLM ...","url":"https://aclanthology.org/2025.emnlp-main.1260.pdf"},{"title":"AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering","url":"https://arxiv.org/html/2604.13120v1"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"}]

Here are the search results for "execution grounded specification code generation LLM 2025 2026":

## Recent Research (2025-2026)

Several significant papers have emerged recently on execution-grounded approaches to code generation and LLM reasoning:

### 1. **RLEF: Grounding Code LLMs in Execution Feedback**
Published at ICML 2025, this work proposes an end-to-end reinforcement learning method for teaching models to leverage execution feedback in code synthesis, benchmarking on competitive programming tasks and achieving large performance gains with both small (8B parameters) and large (70B) models.

### 2. **Code Execution as Grounded Supervision for LLM Reasoning**
This EMNLP 2025 paper proposes a scalable method for generating verifiable CoT data to supervise the reasoning process of LLMs by leveraging the determinism of program execution, extracting verifiable, step-by-step reasoning traces from code execution and transforming them into natural language CoT reasoning.

### 3. **Verify Before You Fix: Agentic Execution Grounding**
This recent work presents a unified cross-language vulnerability lifecycle framework built around three LLM-driven reasoning stages: hybrid structural-semantic detection, execution-grounded agentic validation, and validation-aware iterative repair, with the governing principle that no repair action is taken without execution-based confirmation, constituting a general principle for trustworthy agentic AI.

### 4. **AgentForge: Execution-Grounded Multi-Agent Framework**
This framework introduces execution-grounded verification as a first-class principle where every code change must survive sandboxed execution before propagation, achieved 40.0% resolution on SWE-bench Lite, outperforming single-agent baselines by 26–28 points.

### 5. **Self-Spec: Model-Authored Specifications**
This approach demonstrates that introducing a specification intermediate makes assumptions explicit, reduces drift, and materially improves outcomes in code generation from natural language instructions.

These papers collectively show a strong trend toward grounding LLM code generation in execution feedback and formal specifications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0c47756-8067-4d8d-818d-f80559e3141c",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "0e521dbb-1754-4004-bc60-e73c677ff5f0",
  "sourceToolAssistantUUID": "c0c47756-8067-4d8d-818d-f80559e3141c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-12T02:30:46.151Z_

Excellent results. I found several highly relevant papers. Let me now fetch the abstracts/details of the most relevant ones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e521dbb-1754-4004-bc60-e73c677ff5f0",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtWiKA4VgNDjDpRVoV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c9633b2-469f-41b3-8c01-0035dccd5bb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXxu3HPyEUXNExzeQYCwQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5660,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 10988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
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

_source line 22 · 2026-05-12T02:30:49.123Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015ySs5gZAichDGcWqbeHA6K`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=6pr7BUGkLp",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description of Self-Spec. Focus on: does it use specifications as intermediate reasoning? Is it training-free? Does it use execution-based verification?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c9633b2-469f-41b3-8c01-0035dccd5bb4",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtWiKA4VgNDjDpRVoV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdffc8d2-bafd-4a32-811d-ddd326aed8f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXxu3HPyEUXNExzeQYCwQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5660,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 10988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
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

_source line 23 · 2026-05-12T02:30:50.970Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0164A1u6mpj71VzT9eEMF9Rf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.12268",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key contributions of CodeSpecBench. Focus on: what are executable behavioral specifications, how are they evaluated, and what is the relationship to preconditions/postconditions/invariants?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdffc8d2-bafd-4a32-811d-ddd326aed8f7",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtWiKA4VgNDjDpRVoV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b8a0778-6c8b-421b-99e5-7f60f91c3919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXxu3HPyEUXNExzeQYCwQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5660,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 10988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
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

_source line 24 · 2026-05-12T02:30:52.431Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QZeuv5gcS6N5qUgqRfQ5vu`</summary>

```json
{
  "url": "https://dl.acm.org/doi/10.1145/3696630.3728702",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description of this paper on property-based testing for LLM code generation. Is it training-free? Does it use properties as intermediate reasoning? How does it refine code?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b8a0778-6c8b-421b-99e5-7f60f91c3919",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtWiKA4VgNDjDpRVoV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c41b61a7-a95a-4f18-8bc4-f3d202ef96a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXxu3HPyEUXNExzeQYCwQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5660,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 10988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
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

### Tool result

_source line 25 · 2026-05-12T02:30:52.658Z_

<details><summary>↩ Tool result · reported error · `toolu_01QZeuv5gcS6N5qUgqRfQ5vu`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c41b61a7-a95a-4f18-8bc4-f3d202ef96a6",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "87dea396-34e9-4231-9831-649835d30671",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "c41b61a7-a95a-4f18-8bc4-f3d202ef96a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T02:30:53.129Z_

<details><summary>↩ Tool result · `toolu_015ySs5gZAichDGcWqbeHA6K`</summary>

```text
I appreciate your request, but I need to be transparent: the content you've provided appears to be a PDF file encoded in binary/compressed format, not readable text. The streams contain FlateDecode-compressed data that I cannot directly parse or extract information from.

To properly answer your questions about Self-Spec's:
- Full title, authors, abstract
- Venue and date
- Whether it uses specifications as intermediate reasoning
- Training-free status
- Execution-based verification approach

I would need either:
1. A plain text version of the paper
2. The paper's URL or DOI
3. Decompressed, readable content

If you can provide the paper in a readable format, I'd be happy to extract the specific information you're seeking while adhering to the 125-character quote limit and proper attribution guidelines you've outlined.

[Binary content (application/pdf, 413.5KB) also saved to /home/ubuntu/.claude-account-3/projects/-/f798b600-6634-458d-b3ae-c38ff9f70c19/tool-results/webfetch-1778553049660-knnhpe.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdffc8d2-bafd-4a32-811d-ddd326aed8f7",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "0350a883-d583-4dac-974a-08bd132e889e",
  "sourceToolAssistantUUID": "fdffc8d2-bafd-4a32-811d-ddd326aed8f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-12T02:30:53.843Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011VQrt5ZFk5eKRBKKQGktkb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.18315",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description. Focus on: does it use property-based testing to bridge code generation and validation? Is it training-free? How does it use properties?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0350a883-d583-4dac-974a-08bd132e889e",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtWiKA4VgNDjDpRVoV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fcb7888-90d3-4ccc-bddc-6dca2ebc6b6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXxu3HPyEUXNExzeQYCwQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5660,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 10988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
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

_source line 28 · 2026-05-12T02:30:55.257Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HJMjFmStqad3ZDREehFizS`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.16198v1",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description of this paper about requirement alignment for code generation. Does it use specifications or contracts as intermediates? Is it training-free?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fcb7888-90d3-4ccc-bddc-6dca2ebc6b6b",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtWiKA4VgNDjDpRVoV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fda3ec85-e3f8-4839-abdc-5a1d43a59c7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXxu3HPyEUXNExzeQYCwQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5660,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 10988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
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

### Tool result

_source line 29 · 2026-05-12T02:30:56.002Z_

<details><summary>↩ Tool result · `toolu_0164A1u6mpj71VzT9eEMF9Rf`</summary>

```text
# CodeSpecBench: Research Overview

## Full Title
CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation

## Authors
Zaoyu Chen, Jianbo Dai, Boyu Zhu, Jingdong Wang, Huiming Wang, Xin Xu, Haoyang Yuan, Zhijiang Guo, Xiao-Ming Wu

## Venue & Date
arXiv Computer Science (Software Engineering), submitted April 14, 2026

## What Are Executable Behavioral Specifications?
According to the abstract, "Executable behavioral specifications, defined via preconditions and postconditions, provide a concrete means to assess" whether LLMs understand intended program behavior. The benchmark encodes these specifications as executable Python functions, enabling evaluation of both correctness and completeness.

## Evaluation Methodology
The research introduces an "execution-based evaluation protocol" supporting both function-level and repository-level tasks. This approach measures two key dimensions:
- **Correctness**: accepting valid behaviors
- **Completeness**: rejecting invalid behaviors

## Key Findings & Contributions
The study reveals critical gaps in LLM capabilities. Testing 15 state-of-the-art models showed "sharp performance degradation on repository-level tasks, where the best model attains only a 20.2% pass rate." Notably, "specification generation is substantially more challenging than code generation," suggesting strong coding ability doesn't guarantee deep semantic understanding.

The benchmark dataset and implementation are publicly available to enable further research in this domain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b8a0778-6c8b-421b-99e5-7f60f91c3919",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "9fe2e9ab-2c1c-47ff-b299-fd5167e52ef1",
  "sourceToolAssistantUUID": "1b8a0778-6c8b-421b-99e5-7f60f91c3919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-12T02:30:56.990Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U25KrqqQLpN91ab3CkrMAJ`</summary>

```json
{
  "url": "https://openreview.net/forum?id=rO8QOHrCeA",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description. Does it use input-output specifications? Is it training-free? What is the approach?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fe2e9ab-2c1c-47ff-b299-fd5167e52ef1",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtWiKA4VgNDjDpRVoV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c80ddd9-e0b8-4674-90d2-f850dc7da73c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXxu3HPyEUXNExzeQYCwQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5660,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 10988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
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

_source line 31 · 2026-05-12T02:30:57.802Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JEWJANNfKHLcwkJbqYZGff`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.03878v1",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key contributions. Focus on: what is spec-driven code generation? Is it about using specifications as intermediate reasoning? What LLM workflow is studied?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c80ddd9-e0b8-4674-90d2-f850dc7da73c",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtWiKA4VgNDjDpRVoV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61e40c55-a271-41a0-923d-a467538fbb99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXxu3HPyEUXNExzeQYCwQq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5660,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 10988,
      "output_tokens": 853,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5660,
          "output_tokens": 853,
          "cache_read_input_tokens": 10988,
          "cache_creation_input_tokens": 1452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1452,
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

_source line 32 · 2026-05-12T02:30:59.907Z_

<details><summary>↩ Tool result · `toolu_011VQrt5ZFk5eKRBKKQGktkb`</summary>

```text
# Paper Summary: Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback

**Full Title:** Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback

**Authors:** Lehan He, Zeren Chen, Zhe Zhang, Xiang Gao, Lu Sheng

**Venue/Date:** arXiv:2506.18315 (cs.SE); Submitted June 23, 2025; Revised May 1, 2026

---

## Abstract Summary
The paper addresses functional correctness challenges in LLM-generated code. Rather than relying on Test-Driven Development methods hampered by poor feedback quality, the authors introduce the Property-Generated Solver (PGS) that prioritizes feedback caliber over test quantity.

---

## Key Method: Property-Based Feedback

**Does it use property-based testing?** Yes, fundamentally.

**Training-free approach?** The paper indicates PGS operates through validation rather than model retraining, suggesting a training-free methodology.

**How properties are utilized:**
- Checks "high-level program properties" (e.g., sorting functions producing non-decreasing sequences)
- Provides "the simplest failing counterexample to the LLM"
- Operates via two core principles: *property-oriented* (semantic guidance beyond I/O mismatches) and *structurally minimal* (reduces cognitive load, isolates root causes)

**Performance Results:**
- 13.4% improvement over other TDD methods (pass@1)
- 64% fix rate on initially-failed problems
- 1.4x-1.6x higher bug fix rate versus debugging-based approaches

The approach bridges code generation and validation by using semantic property specifications rather than conventional test cases.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fcb7888-90d3-4ccc-bddc-6dca2ebc6b6b",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "ac47a385-c3f5-4e5b-b04b-fc38658cfa78",
  "sourceToolAssistantUUID": "5fcb7888-90d3-4ccc-bddc-6dca2ebc6b6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-12T02:31:00.965Z_

<details><summary>↩ Tool result · `toolu_01U25KrqqQLpN91ab3CkrMAJ`</summary>

```text
# Paper Summary

**Full Title:** Grounding Code Generation with Input-Output Specifications

**Authors:** Yeming Wen, Pengcheng Yin, Kensen Shi, Henryk Michalewski, Swarat Chaudhuri, Alex Polozov

**Venue & Date:** ICLR 2024 Conference (submitted 23 Sept 2023, modified 11 Feb 2024)

**Abstract:** The paper addresses the problem of LLMs generating executable but incorrect code. The researchers introduce GIFT4Code, which uses "execution-derived feedback as a key learning signal" in the form of input-output specifications to fine-tune code generation models on synthetic data the LLM itself produces.

---

## Key Questions Answered

**Does it use input-output specifications?**
Yes. The method explicitly leverages "program input-output specifications" as feedback to guide the fine-tuning process.

**Is it training-free?**
No. This is an instruction fine-tuning approach requiring training on synthetic data with execution-based feedback.

**The Approach:**
GIFT4Code is an instruction fine-tuning framework that:
1. Generates synthetic training data using the LLM itself
2. Uses execution-derived I/O specifications as learning signals
3. Fine-tunes the model to align with user intentions
4. Tests on data science benchmarks (Arcade, DS-1000)

The core innovation involves grounding code generation in concrete input-output behavior rather than relying solely on text-based training signals.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c80ddd9-e0b8-4674-90d2-f850dc7da73c",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "4910c25e-52cd-4fab-ba6b-5f737eeaafc6",
  "sourceToolAssistantUUID": "5c80ddd9-e0b8-4674-90d2-f850dc7da73c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T02:31:01.671Z_

<details><summary>↩ Tool result · `toolu_01HJMjFmStqad3ZDREehFizS`</summary>

```text
# Paper Summary: REA-Coder

**Full Title:**
"Bridging the Gap between User Intent and LLM: A Requirement Alignment Approach for Code Generation"

**Authors:**
Jia Li, Ruiqi Bai, Yangkang Luo, Yiran Zhang, Wentao Yang, Zeyu Sun, Tiankuo Zhao, Dongming Jin, Lei Li, and Zhi Jin

**Venue/Date:**
arXiv:2604.16198v1 [cs.SE], April 17, 2026

**Abstract Summary:**
The paper proposes REA-Coder, which addresses the limitation that "the LLM can correctly understand the given requirement" doesn't always hold. The approach identifies misaligned requirements through question-answer checklists, aligns them before code generation, and verifies alignment through masked-requirement recovery.

**Key Method Description:**
REA-Coder operates in three stages: (1) requirement alignment using QA-based verification against core dimensions (Purpose, Inputs, Outputs, Constraints, Examples); (2) code generation from aligned requirements; (3) verification through masking semantic spans and recovering them from generated code to detect remaining misalignments. The process iterates until code passes tests or reaches 10 iterations.

**Specifications/Contracts:**
The approach does not use formal specifications or contracts as intermediates. Instead, it uses natural language requirement dimensions and QA checklists.

**Training-Free:**
Yes, REA-Coder is completely training-free, operating solely through prompting and iterative refinement with existing LLMs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fda3ec85-e3f8-4839-abdc-5a1d43a59c7e",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "e8840351-6b08-415c-b3fe-a3326692fc30",
  "sourceToolAssistantUUID": "fda3ec85-e3f8-4839-abdc-5a1d43a59c7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-12T02:31:05.582Z_

<details><summary>↩ Tool result · `toolu_01JEWJANNfKHLcwkJbqYZGff`</summary>

```text
# Study on Specification-Driven Code Generation with LLMs

## Title & Metadata
**"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design"**

**Authors:** Giovanni Rosa, David Moreno-Lumbreras, Gregorio Robles, Jesús M. González-Barahona

**Venue:** SANER 2026 (Stage 1 Registered Report with Continuity Acceptance)

## Abstract
The research examines how large language models perform when integrated into structured, specification-first development processes. Participants use CURRANTE—a VS Code extension—to solve medium-difficulty programming challenges by defining requirements, generating test suites, and producing functions that satisfy those tests. The study captures interaction logs and effectiveness metrics to understand how human involvement in test refinement influences code quality.

## What is Spec-Driven Code Generation?

Specification-driven development represents a shift from traditional code-centric approaches. Rather than writing code directly, developers express intent through formal specifications (here, test cases in Python's unittest format). The LLM then generates implementations matching those specifications. The authors note this differs from code completion tools by emphasizing "a more abstract specification-driven process" centered on requirements definition upfront.

## The LLM Workflow Studied

CURRANTE implements a three-phase workflow:

1. **Specification Phase:** Users define problem requirements in structured TOML format
2. **Test Refinement:** LLM generates initial tests; developers iteratively improve them through explanations, regenerations, and deletions
3. **Function Generation:** LLM produces code validated against the refined test suite

The intermediate reasoning occurs through test case curation—developers refine formal specifications before code generation proceeds, enabling human oversight of the problem decomposition.

## Key Contributions

- Reproducible TDD-based protocol using LiveCodeBench dataset
- Fine-grained telemetry capturing 10+ interaction and outcome metrics
- Empirical evidence on human-AI collaboration in structured development workflows
- Reusable methodology for evaluating LLM coding tools

Human involvement in test specification acts as the critical intermediate reasoning step.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61e40c55-a271-41a0-923d-a467538fbb99",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "f6a07380-9be2-4699-b029-9d6060201aa4",
  "sourceToolAssistantUUID": "61e40c55-a271-41a0-923d-a467538fbb99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-12T02:31:08.041Z_

Now let me fetch the remaining highly relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6a07380-9be2-4699-b029-9d6060201aa4",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtYNU7V4CFryCBNn6fW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6be0a8e3-360d-4b4b-b5c3-4e423d16e2e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v1C91CdoQZhtuHm31LJbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8923,
      "cache_read_input_tokens": 12440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8923,
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

_source line 37 · 2026-05-12T02:31:10.446Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G3X3iuRCexteRWJL3ZSQHE`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.05278",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description of Spec Kit Agents. Does it use specifications as intermediate artifacts before code generation? Is it training-free? How does it validate specifications?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6be0a8e3-360d-4b4b-b5c3-4e423d16e2e2",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtYNU7V4CFryCBNn6fW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0290b7a6-8a40-4cc8-a46b-bf025575c68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v1C91CdoQZhtuHm31LJbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8923,
      "cache_read_input_tokens": 12440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8923,
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

_source line 38 · 2026-05-12T02:31:12.401Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014CKKH2tDJgkoANUzoZ17G4`</summary>

```json
{
  "url": "https://ligechina.github.io/My%20Papers/2025%20-%20TOSEM%20-%20Structured%20Chain-of-Thought%20Prompting%20for%20Code%20Generation.pdf",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description of this Structured Chain-of-Thought paper. Is it training-free? Does it use specifications or structured intermediates for code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0290b7a6-8a40-4cc8-a46b-bf025575c68a",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtYNU7V4CFryCBNn6fW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75da943f-721e-4b8a-837d-391ca2f99931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v1C91CdoQZhtuHm31LJbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8923,
      "cache_read_input_tokens": 12440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8923,
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

_source line 39 · 2026-05-12T02:31:13.825Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018G9zq2mPiEAB2RER5KkUrB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.12083",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description of this paper. Does it use specifications, contracts, or execution-based verification for LLM code generation or reasoning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75da943f-721e-4b8a-837d-391ca2f99931",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtYNU7V4CFryCBNn6fW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3ad87c0-e6f5-4880-85ff-1138319f09d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v1C91CdoQZhtuHm31LJbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8923,
      "cache_read_input_tokens": 12440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8923,
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

_source line 40 · 2026-05-12T02:31:14.757Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WRPKCC9KfTzyf5Sj1WpYZg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.13463",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description of PropGen. Does it use property-based specifications? Is it training-free? How does it generate and refine properties?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3ad87c0-e6f5-4880-85ff-1138319f09d6",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtYNU7V4CFryCBNn6fW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b455af60-20b2-4641-98f4-d4d771863192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v1C91CdoQZhtuHm31LJbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8923,
      "cache_read_input_tokens": 12440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8923,
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

### Tool result

_source line 41 · 2026-05-12T02:31:17.635Z_

<details><summary>↩ Tool result · `toolu_01G3X3iuRCexteRWJL3ZSQHE`</summary>

```text
# Spec Kit Agents: Key Details

**Full Title:** "Spec Kit Agents: Context-Grounded Agentic Workflows"

**Authors:** Pardis Taghavi, Santosh Bhavani

**Venue/Date:** arXiv:2604.05278v1 [cs.SE], April 7, 2026

## Abstract Summary
The paper presents a multi-agent spec-driven development pipeline addressing "context blindness" in LLM-based coding agents. It reports quality improvements of +0.15 on a composite 1–5 score across 128 runs, while maintaining 99.7–100% test compatibility.

## Core Method: Yes to Both Questions

**Specifications as Intermediate Artifacts:**
Yes. The system generates three intermediate documents before implementation: SPEC.md (requirements), PLAN.md (implementation plan), and TASKS.md (executable checklist). The authors note this "externalizes intermediate artifacts" and provides "structured audit trail."

**Training-Free:**
Yes. The approach uses existing LLMs (MiniMax-M2.5 for generation, Claude Opus 4.6 for evaluation) without fine-tuning.

## Validation Strategy

The system employs a two-hook context-grounding layer:

1. **Discovery hooks** (pre-phase): "Read-only prober gathers evidence about the codebase using repository inspection tools" like globbing and grep to surface conventions and APIs

2. **Validation hooks** (post-phase): Check artifacts for "structural and referential constraints" (e.g., whether file paths exist, required libraries present), then execute repository checks like tests and linters after implementation

This front-loads error detection before code generation compounds mistakes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0290b7a6-8a40-4cc8-a46b-bf025575c68a",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "8114e3dd-2f1c-473c-97e9-51410f1ff6c3",
  "sourceToolAssistantUUID": "0290b7a6-8a40-4cc8-a46b-bf025575c68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T02:31:17.437Z_

<details><summary>↩ Tool result · `toolu_014CKKH2tDJgkoANUzoZ17G4`</summary>

```text
I appreciate your request, but I need to be transparent: the content provided is a PDF file in binary/encoded format that hasn't been properly decoded into readable text. While I can see metadata indicating this is an ACM paper (DOI: 10.1145/3690635), the actual document content is compressed and not legible in the format provided.

To accurately extract the title, authors, abstract, venue, methods, and answer your specific questions about training-free approaches and structured intermediates for code generation, I would need:

1. A properly decoded text version of the PDF, or
2. The HTML/text source of the paper, or
3. A direct link to the paper

**What I can confirm from metadata:**
- Publisher: ACM (Association for Computing Machinery)
- DOI: 10.1145/3690635
- Date stamp: January 21, 2025

**Recommendation:** Please provide the paper in one of these formats:
- Plain text extraction
- Markdown version
- HTML content
- Direct URL to the published paper

Once you share a readable version, I'll be happy to provide the detailed extraction you've requested, adhering to your character limits and citation requirements.

[Binary content (application/pdf, 5.6MB) also saved to /home/ubuntu/.claude-account-3/projects/-/f798b600-6634-458d-b3ae-c38ff9f70c19/tool-results/webfetch-1778553072829-zy9wq0.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75da943f-721e-4b8a-837d-391ca2f99931",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "278c5919-28d2-4597-94cb-a859087df2af",
  "sourceToolAssistantUUID": "75da943f-721e-4b8a-837d-391ca2f99931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-12T02:31:18.404Z_

<details><summary>↩ Tool result · `toolu_018G9zq2mPiEAB2RER5KkUrB`</summary>

```text
# Paper Summary

**Full Title:** Differentiable Modal Logic for Multi-Agent Diagnosis, Orchestration and Communication

**Author:** Antonin Sulc

**Submission Date:** February 12, 2026

**Venue:** Tutorial at 3rd International Conference on Neuro-Symbolic Systems (NeuS)

## Abstract Summary

The paper presents a neurosymbolic framework using Modal Logical Neural Networks (MLNNs) to debug multi-agent AI systems. It addresses reasoning about "knowledge, belief, causality, and obligation" through four modal types: epistemic, temporal, deontic, and doxastic. Applications include discovering deceptive alliances in games and detecting LLM hallucinations.

## Key Method Description

The approach enables systems to "learn trust networks, causal chains, and regulatory boundaries from behavioral data alone" rather than requiring manual specification. It converts logical contradictions into learnable optimization objectives, providing interpretable learned structures where trust and causality remain explicit parameters.

## Verification Approach

**No.** This paper does not employ specifications, contracts, or execution-based verification for LLM code generation. Instead, it uses differentiable modal logic and neural networks to learn semantic relationships from behavioral data, focusing on multi-agent system debugging through logical reasoning rather than formal verification techniques.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3ad87c0-e6f5-4880-85ff-1138319f09d6",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "0b34df9a-c460-45de-8168-1bce93f453b7",
  "sourceToolAssistantUUID": "c3ad87c0-e6f5-4880-85ff-1138319f09d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-12T02:31:20.493Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UWsYR7BiAWzT19LQS7k28g`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.00897",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method. Does it use specification-based verification? Is it training-free? How does the detect-repair-verify loop work?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b34df9a-c460-45de-8168-1bce93f453b7",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtYNU7V4CFryCBNn6fW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c77ef31b-ef90-4231-b3d6-f27563883a66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v1C91CdoQZhtuHm31LJbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8923,
      "cache_read_input_tokens": 12440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8923,
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

_source line 45 · 2026-05-12T02:31:20.596Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GhN7TsbWDZ1v665bs6H3uj`</summary>

```json
{
  "url": "https://thoughtworks.medium.com/spec-driven-development-d85995a81387",
  "prompt": "Extract key points about spec-driven development. Is this about an academic paper? What does it say about using specifications as intermediates for LLM-based code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c77ef31b-ef90-4231-b3d6-f27563883a66",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtYNU7V4CFryCBNn6fW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fec293e-0e09-4e1b-95c2-015a00a4fae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v1C91CdoQZhtuHm31LJbY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8923,
      "cache_read_input_tokens": 12440,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8923
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 722,
          "cache_read_input_tokens": 12440,
          "cache_creation_input_tokens": 8923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8923,
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

_source line 46 · 2026-05-12T02:31:25.545Z_

<details><summary>↩ Tool result · `toolu_01WRPKCC9KfTzyf5Sj1WpYZg`</summary>

```text
# PropGen: LLM-Based Property Generation for Mobile App Testing

**Full Title:** "From Exploration to Specification: LLM-Based Property Generation for Mobile App Testing"

**Authors:** Yiheng Xiong, Shiwen Song, Bo Ma, Ting Su, Xiaofei Xie

**Venue/Date:** arXiv:2604.13463 [cs.SE], submitted April 15, 2026

## Abstract Summary
The system addresses functional bugs in Android apps that lack explicit test oracles. It employs "property-based testing" to detect behavioral issues under diverse user interactions, automating what typically requires manual property construction.

## Key Method Description
PropGen operates through three phases:

1. **Exploration:** Performs "functionality-guided exploration to collect behavioral evidence from app executions"
2. **Synthesis:** Generates properties from collected evidence
3. **Refinement:** "Refines imprecise properties based on testing feedback"

## Key Questions Answered

**Does it use property-based specifications?** Yes. The approach explicitly leverages property-based testing methodology to verify intended behavioral properties.

**Is it training-free?** The document does not specify whether the LLM component requires fine-tuning, so this cannot be definitively answered from the provided content.

**Property Generation & Refinement:** The system synthesizes properties from observed behavioral evidence during app execution, then repairs inaccurate properties identified during subsequent testing cycles.

**Results:** Identified 1,210 valid functionalities, generated 985 properties (912 valid), and discovered 25 previously unknown bugs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b455af60-20b2-4641-98f4-d4d771863192",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "40dcca37-da56-4e8b-97ba-16615d676a1a",
  "sourceToolAssistantUUID": "b455af60-20b2-4641-98f4-d4d771863192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-12T02:31:26.775Z_

<details><summary>↩ Tool result · `toolu_01GhN7TsbWDZ1v665bs6H3uj`</summary>

```text
# Spec-Driven Development: Key Points

**Not an Academic Paper**
This is a practitioner's blog post by Liu Shangqi, Technology Director at Thoughtworks, published on Medium in December 2025—not an academic paper.

## Key Points on Specifications as Code Generation Intermediates

**Core Concept**
The article defines spec-driven development as "a development paradigm that uses well-crafted software requirement specifications as prompts, aided by AI coding agents, to generate executable code."

**Specifications as Intermediates**
There's significant industry debate about whether specs are:
- **Disposable process artifacts** (some argue code should be generated from specs, then specs discarded)
- **Persistent sources of truth** (the author's view—specs drive generation but executable code remains the maintained artifact)

**Technical Specifications Matter**
The author emphasizes that "providing the model with semi-structured input prompts or forcing it to output in a structured manner can significantly improve reasoning performance and reduce hallucinations."

**Workflow Structure**
The practice separates planning (requirements analysis → specification creation) from implementation (AI agents generate code from finalized specs), compressing contextual information into specifications.

**Not Waterfall**
The author argues this differs from waterfall because it maintains shorter feedback cycles through human-in-the-loop validation rather than creating lengthy upfront design phases.

**Remaining Challenges**
Code generation from specifications remains non-deterministic, requiring robust CI/CD practices to manage spec drift and hallucinations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fec293e-0e09-4e1b-95c2-015a00a4fae6",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "0a0739d0-e6a4-4687-96d5-7d3130fb2297",
  "sourceToolAssistantUUID": "3fec293e-0e09-4e1b-95c2-015a00a4fae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-12T02:31:31.352Z_

<details><summary>↩ Tool result · `toolu_01UWsYR7BiAWzT19LQS7k28g`</summary>

```text
# Paper Summary

**Full Title:** "Detect Repair Verify for Securing LLM Generated Code: A Multi-Language Empirical Study"

**Author:** Cheng Cheng

**Venue/Date:** arXiv:2603.00897 (cs.SE), submitted March 1, 2026

**Abstract Summary:**
The paper investigates a "Detect--Repair--Verify (DRV) loop" workflow for securing LLM-generated code. It addresses four research gaps: lack of project-level benchmarks with executable tests, limited evidence of pipeline-level effectiveness, unclear reliability of detection reports as repair guidance, and uncertain repair trustworthiness.

**Key Method:**
The authors introduce a benchmark dataset of "runnable web-application projects paired with functional tests and targeted security tests." They evaluate three approaches: generation-only, single-pass DRV, and bounded iterative DRV variants, measuring outcomes through test-grounded verification and analyzing failure modes like regressions and semantic drift.

**Specification-Based Verification?**
No explicit mention of formal specifications. Instead, the work uses "functional tests and targeted security tests" for verification.

**Training-Free?**
Yes, this appears to be a training-free empirical evaluation study using existing LLMs within a DRV workflow.

**DRV Loop Operation:**
Detection identifies security issues → Repair applies fixes → Verification tests the results against functional and security test suites, with potential iteration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c77ef31b-ef90-4231-b3d6-f27563883a66",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "a53eb4bd-c97d-4d11-848d-49fd95515186",
  "sourceToolAssistantUUID": "c77ef31b-ef90-4231-b3d6-f27563883a66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-12T02:31:36.094Z_

Let me now search for a few more specific papers that are closely related to ExeSpec's approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a53eb4bd-c97d-4d11-848d-49fd95515186",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtaGeRdqam9pnjhJJ94",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a53ae5d1-f627-4f86-93ae-142cdfe93f13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJW4TMek7vSQuXm9q2nxMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 366,
      "cache_creation_input_tokens": 2562,
      "cache_read_input_tokens": 21363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2562,
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

_source line 50 · 2026-05-12T02:31:36.641Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KZkaSZW3dGYNWaMqJEMLKZ`</summary>

```json
{
  "query": "Self-Spec model-authored specifications LLM code generation training-free 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a53ae5d1-f627-4f86-93ae-142cdfe93f13",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtaGeRdqam9pnjhJJ94",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "542a0efa-c27c-4766-a849-96d1cdb216a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJW4TMek7vSQuXm9q2nxMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 366,
      "cache_creation_input_tokens": 2562,
      "cache_read_input_tokens": 21363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2562,
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

_source line 51 · 2026-05-12T02:31:37.745Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V78oLVUqFpxRz9zW2uLrzW`</summary>

```json
{
  "query": "\"precondition postcondition\" LLM code generation inference 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "542a0efa-c27c-4766-a849-96d1cdb216a5",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtaGeRdqam9pnjhJJ94",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd498d37-3049-48cf-84ae-eec61860d46d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJW4TMek7vSQuXm9q2nxMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 366,
      "cache_creation_input_tokens": 2562,
      "cache_read_input_tokens": 21363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2562,
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

_source line 52 · 2026-05-12T02:31:38.092Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Qd54uRn1Jhvr3VTjfBRWK`</summary>

```json
{
  "query": "LLM self-generated tests specifications code refinement iterative 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd498d37-3049-48cf-84ae-eec61860d46d",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtaGeRdqam9pnjhJJ94",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98181d51-3223-44a9-9b01-dc9e47c7a237",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJW4TMek7vSQuXm9q2nxMy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 366,
      "cache_creation_input_tokens": 2562,
      "cache_read_input_tokens": 21363,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2562
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 366,
          "output_tokens": 202,
          "cache_read_input_tokens": 21363,
          "cache_creation_input_tokens": 2562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2562,
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

_source line 53 · 2026-05-12T02:31:44.341Z_

<details><summary>↩ Tool result · `toolu_01KZkaSZW3dGYNWaMqJEMLKZ`</summary>

```text
Web search results for query: "Self-Spec model-authored specifications LLM code generation training-free 2025"

Links: [{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation | OpenReview","url":"https://openreview.net/forum?id=6pr7BUGkLp"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/html/2605.02455"},{"title":"SpecGen: Automated Generation of Formal Program Specifications via Large Language Models","url":"https://arxiv.org/html/2401.08807v1"},{"title":"The Spec-to-Code Workflow: Building Software Using Only LLMs | by Mattia D'Argenio | Medium","url":"https://medium.com/@mattia.darge/the-spec-to-code-workflow-building-software-using-only-llms-5e025cd28de0"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Self-planning Code Generation with Large Language Models","url":"https://arxiv.org/pdf/2303.06689"},{"title":"Leveraging LLMs for Formal Software Requirements: Challenges and Prospects","url":"https://ceur-ws.org/Vol-4142/paper11.pdf"},{"title":"[2401.08807] SpecGen: Automated Generation of Formal Program Specifications via Large Language Models","url":"https://arxiv.org/abs/2401.08807"},{"title":"SpecGen: Automated Generation of Formal Program ...","url":"https://arxiv.org/pdf/2401.08807"}]

Based on the search results, here's what I found about Self-Spec:

## Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation

Self-Spec is a lightweight, deterministic (T=0) orchestration that prompts a model to design a compact spec schema it prefers, instantiate that schema from a problem's docstring and signature, resolve ambiguities via a minimal Q&A loop, and generate code only from the confirmed spec.

### Key Features

The method is simple (no finetuning), model-agnostic (each model chooses its spec shape), and practical (assumptions are made explicit). A self-authored spec better aligns with a model's internal representational bias, reducing docstring drift and format/edge-case mistakes.

### Performance Results

On HumanEval (pass@1, single sample), Self-Spec improves over direct NL→code for stronger models: GPT-4o 87%→92% (+5) and Claude 3.7 92%→94% (+2); Claude 3.5 dips 90%→89% (-1), which returns to baseline once we remove over-defensive guards in generated code.

### Significance

This is the first systematic study that lets an LLM design its own spec language for coding. Self-Spec works in practice and offers strong potential as a general path to more reliable LLM coding via self-authored specifications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "542a0efa-c27c-4766-a849-96d1cdb216a5",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "58050d89-fbb7-4dff-87d1-7167659e2942",
  "sourceToolAssistantUUID": "542a0efa-c27c-4766-a849-96d1cdb216a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-12T02:31:46.765Z_

<details><summary>↩ Tool result · `toolu_01V78oLVUqFpxRz9zW2uLrzW`</summary>

```text
Web search results for query: ""precondition postcondition" LLM code generation inference 2025 2026 arxiv"

Links: [{"title":"Beyond Postconditions: Can Large Language Models infer Formal Contracts for","url":"https://arxiv.org/pdf/2510.12702"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"Beyond Code Generation: Assessing Code LLM Maturity with Postconditions","url":"https://arxiv.org/html/2407.14118v1"},{"title":"An Automatic Approach to Weakest Precondition ...","url":"https://arxiv.org/pdf/2507.05272"},{"title":"FormalSpecCpp: A Dataset of C++ Formal Specifications created using LLMs","url":"https://arxiv.org/pdf/2502.15217"},{"title":"LLMs and Fuzzing in Tandem: A New Approach to Automatically Generating Weakest Preconditions","url":"https://arxiv.org/html/2507.05272"},{"title":"FuzzFeed: An Automatic Approach to Weakest Precondition Generation using LLMs and Fuzzing This work was conducted with the financial support of the Research Ireland Centre for Research Training in Digitally-Enhanced Reality (d-real) under Grant No. 18/CRT/6224, Taighde Éireann – Research Ireland under Grant number 13/RC/2094/\\_2, and the ERC Consolidator Grant ARTIST 101002685. For the purpose of Open Access, the author has applied a CC BY public copyright licence to any Author Accepted Manuscript versio","url":"https://arxiv.org/html/2507.05272v1"},{"title":"Preconditions and Postconditions as Design Constraints ...","url":"https://ieeexplore.ieee.org/iel8/6287639/10820123/11218044.pdf"},{"title":"arXiv:2404.00762v2 [cs.SE] 2 Apr 2024","url":"https://arxiv.org/pdf/2404.00762"},{"title":"Automatic Generation of Formal Specification and Verification Annotations Using LLMs and Test Oracles1footnote 11footnote 1Preprint. Intended for submission to Science of Computer Programming.","url":"https://arxiv.org/html/2601.12845v1"}]

I found several relevant arxiv papers on precondition and postcondition inference using LLMs for code generation. Here are the key findings:

## Recent Research Papers (2025-2026)

**NL2Contract (October 2025)**: A paper titled "Beyond Postconditions: Can Large Language Models infer Formal Contracts for Automatic Software Verification?" introduces NL2Contract, the task of employing LLMs to translate informal natural language into formal functional contracts, consisting of postconditions as well as preconditions. The evaluation shows that LLMs are generally effective at generating functional contracts sound for all possible inputs, and verifiers supplied with LLM inferred functional contracts produce fewer false alarms than when provided with postconditions alone.

**Automatic Generation of Formal Specification and Verification Annotations (January 2026)**: This paper investigates how LLMs can automatically generate formal specification and verification constructs (preconditions, postconditions, loop invariants, and proof helpers) for programs written in Dafny, with a multimodel approach combining Claude Opus 4.5 and GPT-5.2 generating correct annotations for 98.2% of the programs within at most 8 repair iterations.

**FormalSpecCpp Dataset (February 2026)**: A dataset paper on C++ formal specifications created using LLMs, noting that preconditions and postconditions serve as formal specifications that define the expected state of a program before and after code execution, ensuring software correctness and formal verification.

## Earlier Work (2024-2025)

**FuzzFeed (July 2025)**: A paper proposing the combination of Large Language Models and fuzz testing for generating weakest preconditions, introducing Fuzzing Guidance (FG) which acts as a means of directing LLMs towards correct WPs using program execution feedback and context refinement.

**AutoSpec (April 2024)**: AutoSpec is driven by static analysis and program verification, empowered by LLMs, and can synthesize different types of specifications (e.g., invariants, preconditions, postconditions) for programs with various structures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd498d37-3049-48cf-84ae-eec61860d46d",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "490d714d-7c03-40ea-bbec-94448c475be8",
  "sourceToolAssistantUUID": "cd498d37-3049-48cf-84ae-eec61860d46d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-12T02:31:49.285Z_

<details><summary>↩ Tool result · `toolu_011Qd54uRn1Jhvr3VTjfBRWK`</summary>

```text
Web search results for query: "LLM self-generated tests specifications code refinement iterative 2025 2026"

Links: [{"title":"Self-Refining LLM Unit Testers: Iterative Generation and Repair via Error-Guided Feedback | by Floralan | Dec, 2025 | Medium","url":"https://medium.com/@floralan212/self-refining-llm-unit-testers-iterative-generation-and-repair-via-error-guided-feedback-7c4afd7f5f55"},{"title":"LLMLOOP: Improving LLM-Generated Code and Tests ...","url":"https://valerio-terragni.github.io/assets/pdf/ravi-icsme-2025.pdf"},{"title":"How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks","url":"https://arxiv.org/html/2604.10508"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"},{"title":"Self-Execution Simulation Improves Coding Models","url":"https://arxiv.org/html/2604.03253"},{"title":"LLMLOOP: Improving LLM-Generated Code and Tests through Automated Iterative Feedback Loops (ICSME 2025 - Tool Demonstration Track) - ICSME 2025 - International Conference on Software Maintenance and Evolution","url":"https://conf.researchr.org/details/icsme-2025/icsme-2025-tool-demonstration/8/LLMLOOP-Improving-LLM-Generated-Code-and-Tests-through-Automated-Iterative-Feedback-"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"LLM-Powered Test Case Generation: Enhancing Coverage and Efficiency","url":"https://www.frugaltesting.com/blog/llm-powered-test-case-generation-enhancing-coverage-and-efficiency"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"}]

I found several relevant research results on LLM self-generated tests, specifications, code refinement, and iterative approaches in 2025-2026. Here's what the search revealed:

## Key Research Areas

**Iterative Self-Refinement for Test Generation**

LLM-generated unit tests undergo error detection for compilation, runtime, and assertion failures, with iterative refinement loops using compiler errors and runtime feedback to automatically repair faulty tests. GPT-4o-mini improved assertion correctness by 21.76 percentage points, while Gemini-2.0-flash gained 32 points.

**Iterative Code and Test Improvement**

LLMLOOP employs five iterative loops: resolving compilation errors, addressing static analysis issues, fixing test case failures, and improving test quality through mutation analysis. When tests fail, details are sent back to the LLM for refinement through an iterative process that continues until test suites pass, with LLMs able to change either generated source code, test code, or both.

**Self-Repair in Code Generation**

Research on iterative self-repair across seven models found that on HumanEval and MBPP with up to five attempts, self-repair universally improves pass rates from +4.9 to +17.1 pp on HumanEval and +16.0 to +30.0 pp on MBPP.

**Specification-Driven Development**

CURRANTE, a Visual Studio Code extension, enables a human-in-the-loop workflow guiding developers through three sequential stages—Specification, Tests, and Function—allowing them to define requirements, generate and refine test suites, and produce functions that satisfy those tests.

**Executable Behavioral Specifications**

While LLMs have become integral to modern software development for generating code from natural-language descriptions, executable behavioral specifications provide a concrete and expressive way to evaluate program behavior understanding.

These studies represent active research directions in 2025-2026 focusing on how iterative feedback loops and specifications can improve LLM-generated code quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98181d51-3223-44a9-9b01-dc9e47c7a237",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "1293e5ad-28a2-494d-ab30-1ad0083bef78",
  "sourceToolAssistantUUID": "98181d51-3223-44a9-9b01-dc9e47c7a237",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-12T02:31:52.514Z_

Let me fetch a few more highly relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1293e5ad-28a2-494d-ab30-1ad0083bef78",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtbbQZkEX776wvgpJmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dbf0841-cbe8-4ed7-a896-b55adbd20e4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWAbBgbMCa2BuKh5qC4kAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 23925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3736,
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

_source line 57 · 2026-05-12T02:31:55.371Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011SsZfKuvzeswoJHRTk8hv5`</summary>

```json
{
  "url": "https://openreview.net/forum?id=6pr7BUGkLp",
  "prompt": "Extract full title, authors, abstract, venue, submission date, and method description for Self-Spec. Is it training-free? Does it use execution-based verification? What kind of specifications does the model generate? How does it compare to direct code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dbf0841-cbe8-4ed7-a896-b55adbd20e4b",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtbbQZkEX776wvgpJmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a87d186c-502c-424f-9818-e5b580ad0063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWAbBgbMCa2BuKh5qC4kAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 23925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3736,
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

_source line 58 · 2026-05-12T02:31:57.903Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NyBSGKe8Z7cYoapHRsu8Tz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.02455",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description of this paper on LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering. Does it use specifications as intermediates? Is it training-free? How does it work?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a87d186c-502c-424f-9818-e5b580ad0063",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtbbQZkEX776wvgpJmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be091704-f26a-485e-9f57-78da1e1a15ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWAbBgbMCa2BuKh5qC4kAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 23925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3736,
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

_source line 59 · 2026-05-12T02:31:58.846Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018b1UNjo4KxKJaVFgqDDZ4i`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03253",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description. Does it use self-execution simulation? Is it training-free? How does it improve code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be091704-f26a-485e-9f57-78da1e1a15ca",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtbbQZkEX776wvgpJmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f49d86b5-bd53-4900-884b-37623180eb0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWAbBgbMCa2BuKh5qC4kAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 23925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3736,
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

_source line 60 · 2026-05-12T02:31:59.697Z_

<details><summary>↩ Tool result · `toolu_011SsZfKuvzeswoJHRTk8hv5`</summary>

```text
# Self-Spec Research Paper Summary

**Full Title:** Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation

**Authors:** Zihao Xu, Xiao Cheng, Jingling Xue, Yuekang Li

**Venue:** Agents4Science 2025 Conference

**Publication Date:** October 8, 2025

## Abstract Summary

The research investigates whether language models generate code more dependably by "first author a task-specific specification language and then implement strictly from that spec."

## Method Description

The approach uses a four-stage process:
1. Design a compact specification schema aligned with the model's preferences
2. Create instances of that schema from problem documentation
3. Resolve unclear elements through minimal question-and-answer interaction
4. Produce code exclusively from the validated specification

The intuition centers on reducing "docstring drift and format/edge-case mistakes" by matching specifications to the model's internal biases.

## Key Characteristics

**Training-Free:** Yes—the method uses deterministic settings (T=0) without fine-tuning.

**Execution-Based Verification:** No explicit mention of testing or execution-based validation in the abstract.

**Specification Type:** Models generate their own compact specification schemas tailored to their representational preferences, rather than using predefined formats.

## Performance Comparison

Self-Spec versus direct code generation shows mixed results:
- GPT-4o: 87% → 92% (+5 percentage points)
- Claude 3.5: 90% → 89% (-1 percentage point)
- Claude 3.7: 92% → 94% (+2 percentage points)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a87d186c-502c-424f-9818-e5b580ad0063",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "54a14f4d-254c-40aa-a596-52d06925db03",
  "sourceToolAssistantUUID": "a87d186c-502c-424f-9818-e5b580ad0063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-12T02:32:00.113Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EdeK9jmBUnxiNUM2D19Pkg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.12845",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description. Does it generate preconditions, postconditions, invariants? Is it training-free or fine-tuned? How does it use execution feedback?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54a14f4d-254c-40aa-a596-52d06925db03",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtbbQZkEX776wvgpJmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "408fe69e-069f-42b1-8bdd-bd93daf3eeb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWAbBgbMCa2BuKh5qC4kAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 23925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3736,
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

_source line 62 · 2026-05-12T02:32:01.528Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WR76sXuxLEPFjo9sGpuhMM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.12702",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description of NL2Contract. Does it use preconditions and postconditions? Is it training-free? How does it relate to code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "408fe69e-069f-42b1-8bdd-bd93daf3eeb0",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtbbQZkEX776wvgpJmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8263e09-9e11-44c2-99e9-1ccdd56ccd2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWAbBgbMCa2BuKh5qC4kAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 23925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3736,
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

_source line 63 · 2026-05-12T02:32:02.219Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RMuGenGXmDNrGHLhaLAUZQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.10508",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description. Is it about iterative self-repair? Is it training-free? How does it use tests or specifications?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8263e09-9e11-44c2-99e9-1ccdd56ccd2b",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtbbQZkEX776wvgpJmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "211581db-ce63-4117-8294-2dadd9d37b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWAbBgbMCa2BuKh5qC4kAr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 23925,
      "output_tokens": 717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3736
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 717,
          "cache_read_input_tokens": 23925,
          "cache_creation_input_tokens": 3736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3736,
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

_source line 64 · 2026-05-12T02:32:02.685Z_

<details><summary>↩ Tool result · `toolu_01NyBSGKe8Z7cYoapHRsu8Tz`</summary>

```text
# LLM-Assisted Repository-Level Generation Paper Summary

**Full Title:** LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering

**Authors:** Shuzhao Feng, Boqi Chen, Brett H Meyer, Gunter Mussbacher

**Venue/Date:** Accepted to the 34th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (FSE Companion '26), submitted May 4, 2026

**Abstract:** The paper addresses limitations in LLM code generation at repository scale. The authors propose that "structured specifications as LLM inputs make high-quality, repository-level code generation a tangible goal, while at the same time offering superior verifiability." They conducted a pilot study generating Model-View-Controller business logic across three systems using five different LLMs.

---

## Key Questions Answered

**Does it use specifications as intermediates?** Yes. The core contribution is structured spec-driven engineering (SSDE), which explicitly leverages structured artifacts to guide LLM generation rather than relying solely on natural language prompts.

**Is it training-free?** The paper doesn't explicitly state training requirements, but the approach appears to be a prompting methodology applied to existing LLMs rather than a fine-tuning approach.

**How does it work?** The method replaces ambiguous natural language prompts with structured specifications to improve code generation quality, verifiability, and scalability at the repository level—demonstrated through MVC business logic generation experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be091704-f26a-485e-9f57-78da1e1a15ca",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "a4b4b995-c286-4d3e-a53f-aa3dc1503db4",
  "sourceToolAssistantUUID": "be091704-f26a-485e-9f57-78da1e1a15ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-12T02:32:03.633Z_

<details><summary>↩ Tool result · `toolu_018b1UNjo4KxKJaVFgqDDZ4i`</summary>

```text
# Paper Summary: Self-Execution Simulation Improves Coding Models

**Full Title:** Self-Execution Simulation Improves Coding Models

**Authors:** Gallil Maimon, Ori Yoran, Felix Kreuk, Michael Hassid, Gal Cohen, Pierre Chambon, Yossi Adi

**Venue/Date:** arXiv:2604.03253 (cs.CL), submitted March 11, 2026

**Key Abstract Points:**
The research addresses how LLMs struggle with "properly estimate program execution, particularly for code they generate." The team demonstrates that Code LLMs can learn to simulate execution step-by-step.

---

## Method Description

The approach combines three training strategies:

1. **Supervised fine-tuning** using natural language execution traces
2. **Reinforcement learning** with verifiable rewards
3. **Dual objectives**: predicting outputs from code/inputs, and solving competitive programming tasks

The model performs "self-verification over multiple candidate solutions, and iterative self-fixing by simulating test execution."

---

## Key Questions

**Does it use self-execution simulation?** Yes, this is the core contribution.

**Is it training-free?** No. It requires supervised fine-tuning and reinforcement learning.

**How does it improve code generation?** By enabling models to verify solutions and iteratively fix errors through simulated execution feedback across multiple benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f49d86b5-bd53-4900-884b-37623180eb0e",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "5b7cbd01-a928-47dc-a501-7bf75c54770a",
  "sourceToolAssistantUUID": "f49d86b5-bd53-4900-884b-37623180eb0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-12T02:32:05.642Z_

<details><summary>↩ Tool result · `toolu_01EdeK9jmBUnxiNUM2D19Pkg`</summary>

```text
# Paper Summary: Automatic Generation of Formal Specification and Verification Annotations

**Full Title:** Automatic Generation of Formal Specification and Verification Annotations Using LLMs and Test Oracles

**Authors:** João Pascoal Faria, Emanuel Trigo, Vinicius Honorato, Rui Abreu

**Venue/Date:** arXiv:2601.12845 (cs.SE), submitted January 19, 2026

---

## Abstract Summary

The research explores leveraging large language models to automatically generate formal verification constructs for programs written in Dafny. The system accepts conventional code with natural language specifications and test cases as input.

---

## Key Findings

**What It Generates:** The system produces preconditions, postconditions, loop invariants, auxiliary predicates/functions, and proof helpers.

**Performance:** Across 110 Dafny programs, the multimodel approach (combining Claude Opus 4.5 and GPT-5.2) achieved "correct annotations for 98.2% of the programs within at most 8 repair iterations."

**Training Approach:** This is training-free—the work employs existing off-the-shelf LLMs rather than fine-tuned models.

**Execution Feedback Mechanism:** The approach uses "verifier feedback" to iteratively repair incorrect annotations. Additionally, "assertions in the test cases served as static oracles to automatically validate the generated pre/postconditions," providing a validation mechanism without requiring human review.

---

## Notable Finding

Analysis revealed that proof-helper annotations disproportionately contribute to difficulty for current LLMs, suggesting this category represents the primary challenge in automation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "408fe69e-069f-42b1-8bdd-bd93daf3eeb0",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "dd6cbbb5-4374-45f6-9b61-4941ea6c4ab4",
  "sourceToolAssistantUUID": "408fe69e-069f-42b1-8bdd-bd93daf3eeb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-12T02:32:06.181Z_

<details><summary>↩ Tool result · `toolu_01WR76sXuxLEPFjo9sGpuhMM`</summary>

```text
# NL2Contract Research Summary

**Full Title:** "Beyond Postconditions: Can Large Language Models infer Formal Contracts for Automatic Software Verification?"

**Authors:** Cedric Richter and Heike Wehrheim

**Venue/Date:** arXiv:2510.12702 (submitted October 14, 2025); Computer Science > Software Engineering

**Abstract Overview:**
The research addresses a critical gap in software verification—the lack of formal specifications in real-world code. The authors introduce NL2Contract, which translates "informal natural language into formal functional contracts" with both preconditions and postconditions. They demonstrate that LLM-generated contracts reduce false alarms in verification compared to postconditions alone.

**Preconditions and Postconditions:**
Yes, NL2Contract explicitly generates both components. The abstract states the approach focuses on "functional contracts, consisting of postconditions as well as preconditions," marking a departure from prior work limited to postconditions only.

**Training-Free Status:**
The document does not specify whether the approach is training-free. It evaluates "different LLMs" without clarifying whether fine-tuning occurred.

**Relation to Code Generation:**
NL2Contract operates within automatic software verification, not code generation. It infers formal specifications from natural language to enable verifiers to detect bugs more accurately, representing a specification-generation task rather than code synthesis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8263e09-9e11-44c2-99e9-1ccdd56ccd2b",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "97bd6961-8d3d-4fe1-b17b-24416a7e7035",
  "sourceToolAssistantUUID": "b8263e09-9e11-44c2-99e9-1ccdd56ccd2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-12T02:32:07.356Z_

<details><summary>↩ Tool result · `toolu_01RMuGenGXmDNrGHLhaLAUZQ`</summary>

```text
# Paper Summary

**Full Title:** "How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks"

**Author:** Johin Johny Arimbur

**Venue/Date:** arXiv:2604.10508 (cs.SE), submitted April 12, 2026

**Is it about iterative self-repair?** Yes. The core focus examines how models improve through multiple correction attempts.

**Is it training-free?** Yes. The paper emphasizes that "modern instruction-tuned models succeed with prompting alone," without requiring fine-tuning.

**How it uses tests/specifications:** The approach feeds execution errors back to the model iteratively. The error-type analysis reveals that "assertion errors (logical mistakes) are the hardest to repair at ~45%, while syntax and name errors are repaired at substantially higher rates."

**Key Method:** The technique involves providing execution feedback across up to five attempts on two benchmarks (HumanEval and MBPP Sanitized). A prompt ablation shows that chain-of-thought reasoning yields additional gains of up to 5.5 percentage points over minimal prompting.

**Key Finding:** Self-repair universally improved pass rates by 4.9-17.1 pp on HumanEval and 16.0-30.0 pp on MBPP, with most gains concentrated in the first two attempts across seven tested models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "211581db-ce63-4117-8294-2dadd9d37b49",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "4f236d26-d35d-4133-8fbe-5fccf61940e6",
  "sourceToolAssistantUUID": "211581db-ce63-4117-8294-2dadd9d37b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-12T02:32:10.958Z_

Let me do a few more targeted searches for papers that are most directly competitive with ExeSpec's core ideas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f236d26-d35d-4133-8fbe-5fccf61940e6",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtcvcF8Pee3qY7ebxUw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb54d32c-c48b-40d8-8f5b-ce6a1660a5ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1BTaitaXptoW2TYYgu17o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 27661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2936,
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

_source line 70 · 2026-05-12T02:32:11.996Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RDyzjcAn8v7gDfan9qDV3G`</summary>

```json
{
  "query": "LLM generate assert precondition postcondition invariant code debugging repair training-free 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb54d32c-c48b-40d8-8f5b-ce6a1660a5ae",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtcvcF8Pee3qY7ebxUw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28c65403-8bfc-4d2d-89d3-505f770241b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1BTaitaXptoW2TYYgu17o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 27661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2936,
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

_source line 71 · 2026-05-12T02:32:12.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011F9RSumVZJn986mzoYmfEe`</summary>

```json
{
  "query": "\"intermediate reasoning\" \"code generation\" specification property verification LLM inference-time 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28c65403-8bfc-4d2d-89d3-505f770241b5",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtcvcF8Pee3qY7ebxUw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4961707-7f29-4c9e-97f2-576faaba2516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1BTaitaXptoW2TYYgu17o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 27661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2936,
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

_source line 72 · 2026-05-12T02:32:13.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BBVin5WiidfD2mcJ2iEiLi`</summary>

```json
{
  "query": "CodeSpecBench executable behavioral specification precondition postcondition benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4961707-7f29-4c9e-97f2-576faaba2516",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtcvcF8Pee3qY7ebxUw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed1d265f-2107-4ac0-bed8-66b6424b2ec5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1BTaitaXptoW2TYYgu17o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 27661,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 27661,
          "cache_creation_input_tokens": 2936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2936,
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

_source line 73 · 2026-05-12T02:32:20.306Z_

<details><summary>↩ Tool result · `toolu_01RDyzjcAn8v7gDfan9qDV3G`</summary>

```text
Web search results for query: "LLM generate assert precondition postcondition invariant code debugging repair training-free 2025 2026"

Links: [{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"Beyond Postconditions: Can Large Language Models infer Formal Contracts for","url":"https://arxiv.org/pdf/2510.12702"},{"title":"Automatic Generation of Formal Specification and Verification Annotations Using LLMs and Test Oracles1footnote 11footnote 1Preprint. Intended for submission to Science of Computer Programming.","url":"https://arxiv.org/html/2601.12845v1"},{"title":"LLM For Loop Invariant Generation and Fixing","url":"https://arxiv.org/pdf/2511.06552"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"Clover: Closed-Loop Verifiable Code Generation Chuyue Sun1⋆ Ying Sheng1∗","url":"https://theory.stanford.edu/~barrett/pubs/SSP+24.pdf"},{"title":"DafnyBench: A Benchmark for Formal Software Verification Chloe Loughridge∗","url":"https://namin.seas.harvard.edu/pubs/dafnybench.pdf"},{"title":"Verifying LLM-Generated Code in the Context of Software Verification with Ada/SPARK","url":"https://arxiv.org/html/2502.07728v1"},{"title":"Published in Transactions on Machine Learning Research (01/2025)","url":"https://openreview.net/pdf?id=yBgTVWccIx"},{"title":"An Automatic Approach to Weakest Precondition ...","url":"https://arxiv.org/pdf/2507.05272"}]

Based on the search results, I found several recent research papers (2025-2026) on LLMs generating formal specifications and code debugging/repair. Here are the key findings:

## Recent Research (2025-2026)

**Automatic Generation of Formal Specifications** (January 2026):
Research investigates how LLMs can automatically generate formal annotations for programs written in Dafny, starting from conventional code accompanied by natural language specifications and test code. A multimodel approach combining Claude Opus 4.5 and GPT-5.2 generated correct annotations for 98.2% of the programs within at most 8 repair iterations, using verifier feedback.

**Loop Invariant Generation and Fixing**:
Studies examine the effectiveness of LLMs to create and repair loop invariants, investigating research questions including how good LLMs are at generating loop invariants and whether LLMs can repair incorrect loop invariants.

**NL2Contract - Inferring Formal Contracts**:
NL2Contract infers preconditions and postconditions from the function's signature, documentation and possible imports. It evaluates the quality of such inferred contracts by supplying them to an automatic verifier which should then generate bug triggering inputs on buggy implementations.

**Weakest Precondition Generation**:
Research explores if LLMs can generate sensible weakest precondition (WP) candidates and whether fuzzing guidance can aid them in doing so by enabling iterative phases of context refinement.

**Self-Spec Framework**:
Questions target precise pre-/post-conditions and type/refinement invariants, with user responses simulated by a second LLM, so each question receives a consistent, model-generated answer.

These papers demonstrate training-free or few-shot approaches using verifier feedback and iterative refinement rather than extensive fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28c65403-8bfc-4d2d-89d3-505f770241b5",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "dd9d62a2-c1b5-49d5-b031-67085debd444",
  "sourceToolAssistantUUID": "28c65403-8bfc-4d2d-89d3-505f770241b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-12T02:32:20.690Z_

<details><summary>↩ Tool result · `toolu_01BBVin5WiidfD2mcJ2iEiLi`</summary>

```text
Web search results for query: "CodeSpecBench executable behavioral specification precondition postcondition benchmark 2026"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268"},{"title":"[2604.12268] CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/abs/2604.12268"},{"title":"FormalSpecCpp: A Dataset of C++ Formal Specifications created using LLMs","url":"https://arxiv.org/pdf/2502.15217"},{"title":"FormalSpecCpp: A Dataset of C++ Formal Specifications created using LLMs | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/11025548/11025536/11025772.pdf"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=Z7TUUQPSzY"},{"title":"FormalSpecCpp: A Dataset of C++ Formal Specifications created using LLMs","url":"https://www.osti.gov/servlets/purl/2564074"},{"title":"Enchanting Program Specification Synthesis by","url":"https://arxiv.org/pdf/2404.00762"},{"title":"DafnyBench: A Benchmark for Formal Software Verification Chloe Loughridge∗","url":"https://namin.seas.harvard.edu/pubs/dafnybench.pdf"},{"title":"Preconditions and Postconditions as Design Constraints ...","url":"https://ieeexplore.ieee.org/iel8/6287639/10820123/11218044.pdf"},{"title":"DafnyBench: A Benchmark for Formal Software Verifi- cation","url":"https://openreview.net/pdf?id=yBgTVWccIx"}]

Based on the search results, here's what I found about CodeSpecBench:

## CodeSpecBench Overview

CodeSpecBench is a benchmark for executable behavioral specification generation. It provides an execution-based evaluation protocol and represents a recent development in evaluating Large Language Models' ability to understand program behavior.

## Key Features

CodeSpecBench includes both preconditions and postconditions, expressed as executable Python functions, allowing flexible and expressive behavioral constraints. It adopts an execution-based evaluation protocol and covers both function-level and repository-level tasks, rather than isolated functions.

It is built from a larger and more diverse set of real-world codebases, yielding more complex and realistic scenarios than prior small-scale or simplified datasets.

## Evaluation Methodology

It evaluates both correctness (accepting valid behaviors) and completeness (rejecting invalid behaviors), enabling a more comprehensive assessment of LLMs' ability to generate executable behavioral specifications.

## Research Findings

15 state-of-the-art LLMs were evaluated on CodeSpecBench, and although models attain moderate performance on self-contained, function-level tasks, a sharp performance degradation occurs on repository-level tasks, where the best model attains only a 20.2% pass rate. Specification generation is substantially more challenging than code generation, indicating that strong coding performance does not necessarily reflect deep understanding of intended program semantics.

The data and code are available at https://github.com/SparksofAGI/CodeSpecBench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed1d265f-2107-4ac0-bed8-66b6424b2ec5",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "3e54b072-7279-4cfa-a041-7f0e56744366",
  "sourceToolAssistantUUID": "ed1d265f-2107-4ac0-bed8-66b6424b2ec5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-12T02:32:21.960Z_

<details><summary>↩ Tool result · `toolu_011F9RSumVZJn986mzoYmfEe`</summary>

```text
Web search results for query: ""intermediate reasoning" "code generation" specification property verification LLM inference-time 2025 2026"

Links: [{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Towards Formal Verification of LLM-Generated Code from Natural Language Prompts","url":"https://arxiv.org/pdf/2507.13290"},{"title":"LLM-Based Code Translation Needs Formal Compositional Reasoning Alvin Cheung","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-174.pdf"},{"title":"Bridging Natural Language and Formal Specification– Automated Translation of Software Requirements to LTL via Hierarchical Semantics Decomposition Using LLMs","url":"https://arxiv.org/html/2512.17334v1"},{"title":"Bridging the Gap between User Intent and LLM: A Requirement Alignment Approach for Code Generation","url":"https://arxiv.org/html/2604.16198v1"},{"title":"2025: The year in LLMs","url":"https://simonwillison.net/2025/Dec/31/the-year-in-llms/"},{"title":"A Survey on Code Generation with LLM-based Agents","url":"https://arxiv.org/html/2508.00083v1"},{"title":"Correctness assessment of code generated by Large Language Models using internal representations - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0164121225002390"},{"title":"The Year in AI - Best of 2025, Part I: Reasoning Models, LLM Agents and More | Apolo AI Launchpad - Secure, Industry-Tailored AI Tools for Regulated Enterprises","url":"https://www.apolo.us/blog-posts/the-year-in-ai-best-of-2025-part-i-reasoning-models-llm-agents-and-more"},{"title":"Correctness Assessment of Code Generated by Large Language Models Using Internal Representations","url":"https://arxiv.org/html/2501.12934v1"}]

I've completed the web search for your query about intermediate reasoning, code generation, specification property verification, and LLM inference-time developments in 2025-2026. Here are the key findings:

## Key Results:

**Inference-Time Scaling and Reasoning:** There is expected to be more focus on inference-time scaling in 2026, which means spending more time and money after training when the LLM generates the answer. OpenAI initiated the "reasoning" aka inference-scaling revolution in September 2024 with o1 and o1-mini, and doubled down on that with o3, o3-mini and o4-mini in the opening months of 2025, making reasoning a signature feature of models from nearly every major AI lab.

**Intermediate Reasoning in Code Generation:** Reasoning-based generation aims to improve code quality by enhancing the intermediate reasoning process before code is produced, with a representative direction being to design better prompting strategies for structured reasoning. LLMs spontaneously develop strategies that look like "reasoning" to humans—they learn to break down problem solving into intermediate calculations and develop problem solving strategies for iterating back and forth to figure things out.

**Specification and Property Verification:** Intermediate contract or test checking involves validating a function or module against unit tests or pre/post-conditions once it is complete, with passing such checks implying behavioral equivalence with respect to the chosen test suite. A broad goal is to provide formal guarantees that code generated by an LLM from a natural language prompt has the user's desired functionality.

**Internal Representations for Code Verification:** By analyzing the intermediate states of the LLM during code generation, approaches can assess code correctness based on a comprehensive set of signals derived from these states.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4961707-7f29-4c9e-97f2-576faaba2516",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "bfe8270a-0b47-4602-95be-46df0c4ca75c",
  "sourceToolAssistantUUID": "c4961707-7f29-4c9e-97f2-576faaba2516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-12T02:32:26.424Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014mTDRNqvtaYvbDKufF1ZGi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.06552",
  "prompt": "Extract the full title, authors, abstract, venue/date, and key method description for this paper on LLM loop invariant generation. Is it training-free? Does it use execution feedback?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfe8270a-0b47-4602-95be-46df0c4ca75c",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011Cawte13BEze7n5aiPs84Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fe0f87f-7a02-4ac3-828e-cffe39662d6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsFLwymKvZEoTSb6ArBcEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 30597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2144,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-12T02:32:28.779Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0192VdFyao8XRZ4nrLswf8Tk`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.12268v1",
  "prompt": "Extract the full abstract of CodeSpecBench. What specific types of behavioral specifications does it cover? How does it evaluate correctness and completeness? What models were tested and what were the key results? Does it propose any methods for using specs to improve code generation, or is it purely a benchmark?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fe0f87f-7a02-4ac3-828e-cffe39662d6a",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011Cawte13BEze7n5aiPs84Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2524e5a6-ad1b-40bb-b3a0-734c2a8fe342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsFLwymKvZEoTSb6ArBcEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 30597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2144,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-12T02:32:29.386Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NBYkGuvDbdehhCLzrf3qFL`</summary>

```json
{
  "query": "Clover closed-loop verifiable code generation postcondition LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2524e5a6-ad1b-40bb-b3a0-734c2a8fe342",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011Cawte13BEze7n5aiPs84Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4158bb23-aa4c-4111-a298-3a182a785e42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsFLwymKvZEoTSb6ArBcEz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 30597,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2144
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 900,
          "output_tokens": 307,
          "cache_read_input_tokens": 30597,
          "cache_creation_input_tokens": 2144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2144,
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

_source line 79 · 2026-05-12T02:32:30.717Z_

<details><summary>↩ Tool result · `toolu_014mTDRNqvtaYvbDKufF1ZGi`</summary>

```text
# Paper Summary: LLM For Loop Invariant Generation and Fixing

**Full Title:** "LLM For Loop Invariant Generation and Fixing: How Far Are We?"

**Authors:** Mostafijur Rahman Akhond, Saikat Chakraborty, Gias Uddin

**Venue/Date:** Submitted to IEEE for possible publication; arXiv submission November 9, 2025

**Abstract Summary:**
The research evaluates both open and closed-source LLMs of varying scales on their capability to infer inductive loop invariants and repair incorrect ones. Key findings indicate that "LLMs achieve a maximum success rate of 78% in generating, but are limited to 16% in repairing the invariant." Performance improves substantially when models receive "auxiliary information such as domain knowledge and illustrative examples."

**Method Description:**
The paper presents an empirical study assessing LLM proficiency in loop invariant inference and correction. While specific implementation details aren't provided in the abstract, the approach examines how supplementary context enhances model performance on formal verification tasks.

**Training-Free Status:** Not specified in the provided content.

**Execution Feedback:** Not mentioned in the available materials.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fe0f87f-7a02-4ac3-828e-cffe39662d6a",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "cb5e5413-88e9-4984-b362-8ff27786c23b",
  "sourceToolAssistantUUID": "3fe0f87f-7a02-4ac3-828e-cffe39662d6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-12T02:32:35.174Z_

<details><summary>↩ Tool result · `toolu_0192VdFyao8XRZ4nrLswf8Tk`</summary>

```text
# CodeSpecBench Overview

## Full Abstract

CodeSpecBench is a benchmark for evaluating large language models' ability to generate executable behavioral specifications from natural language descriptions. It uses an execution-based evaluation protocol covering both function-level and repository-level tasks, with specifications encoded as executable Python functions representing preconditions and postconditions. The benchmark was constructed from diverse real-world codebases and evaluated 15 state-of-the-art LLMs, revealing that specification generation is substantially more challenging than code generation, with the best model achieving only 20.2% pass rate on repository-level tasks.

## Specification Coverage

The benchmark includes both **preconditions** (constraints on valid inputs and program state before execution) and **postconditions** (properties that must hold after execution). These are represented as executable Python functions rather than formal assertions, enabling flexible and expressive behavioral constraints.

## Evaluation Approach

CodeSpecBench evaluates specifications along two complementary dimensions:

- **Correctness**: Whether specifications accept valid test cases that satisfy the problem requirements
- **Completeness**: Whether specifications reject invalid test cases that violate expected behavior

Pass rate combines both criteria—specifications must satisfy both to pass.

## Models Tested & Key Results

The evaluation covered 15 LLMs including open-weight (Qwen3, DeepSeek) and proprietary models (Claude, GPT-5, Gemini). Results showed:

- Function-level: best pass rate of 47.0% (GPT-5-mini)
- Repository-level: best pass rate of 20.2% (Claude-4.5-Sonnet)
- Specification generation significantly outperformed code generation in difficulty

## Practical Application

Beyond benchmarking, the work demonstrates that generated specifications can improve code generation through semantic re-ranking, improving pass@1 rates by 2-3 percentage points on function-level tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2524e5a6-ad1b-40bb-b3a0-734c2a8fe342",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "ffe3cc81-76d8-4132-8b66-028a70d460c0",
  "sourceToolAssistantUUID": "2524e5a6-ad1b-40bb-b3a0-734c2a8fe342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-12T02:32:37.979Z_

<details><summary>↩ Tool result · `toolu_01NBYkGuvDbdehhCLzrf3qFL`</summary>

```text
Web search results for query: "Clover closed-loop verifiable code generation postcondition LLM 2024 2025"

Links: [{"title":"Clover: Closed-Loop Verifiable Code Generation Chuyue Sun1⋆ Ying Sheng1∗","url":"https://theory.stanford.edu/~barrett/pubs/SSP+24.pdf"},{"title":"[2310.17807] Clover: Closed-Loop Verifiable Code Generation","url":"https://arxiv.org/abs/2310.17807"},{"title":"Clover: Closed-Loop Verifiable Code Generation","url":"https://arxiv.org/pdf/2310.17807"},{"title":"CLOVER: CLOSED-LOOP VERIFIABLE CODE GENERATION Anonymous authors","url":"https://openreview.net/pdf?id=oSuVEv4X7w"},{"title":"Clover: Closed-Loop Verifiable Code Generation | OpenReview","url":"https://openreview.net/forum?id=oSuVEv4X7w"},{"title":"GitHub - ChuyueSun/Clover: Clover: Closed-Loop Verifiable Code Generation · GitHub","url":"https://github.com/ChuyueSun/Clover"},{"title":"Clover: Closed-Loop Verifiable Code Generation | AI Verification","url":"https://dl.acm.org/doi/10.1007/978-3-031-65112-0_7"},{"title":"Clover: Closed-Loop Verifiable Code Generation | SAIL Blog","url":"http://ai.stanford.edu/blog/clover/"},{"title":"CLOVER: Closed-Loop Verifiable Code Generation (Dafny 2024) - POPL 2024","url":"https://popl24.sigplan.org/details/dafny-2024-papers/1/CLOVER-Closed-Loop-Verifiable-Code-Generation"},{"title":"Clover: Closed-Loop Verifiable Code Generation","url":"https://www.wisdom.weizmann.ac.il/~padon/clover-saiv2024.pdf"}]

I've found comprehensive information about Clover. Here's a summary of the search results:

## Clover: Closed-Loop Verifiable Code Generation

Clover is an approach that uses consistency checking to provide a strong filter for incorrect code, addressing the challenge of ensuring correctness in AI-generated code.

### Core Concept

At the core of Clover lies a checker that performs consistency checks among code, docstrings, and formal annotations, implemented using a novel integration of formal verification tools and large language models. The paradigm reduces correctness checking to the more accessible problem of consistency checking.

### Key Findings

The research investigates performance on a hand-designed dataset (CloverBench) featuring annotated Dafny programs at a textbook level of difficulty. Experimental results show that LLMs are reasonably successful at automatically generating formal specifications, and the consistency checker achieves a promising acceptance rate (up to 87%) for correct instances while maintaining zero tolerance for adversarial incorrect ones (no false positives).

### Research Timeline

The paper was initially submitted in October 2023, with subsequent versions in January 2024, June 2024, and November 2024, indicating active development and refinement of the approach through 2024-2025.

### Application Areas

Clover also discovered 6 incorrect programs in the existing human-written dataset MBPP-DFY-50, demonstrating its utility in catching errors in existing code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4158bb23-aa4c-4111-a298-3a182a785e42",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "44b84b26-6e86-4f7d-8456-a67624838676",
  "sourceToolAssistantUUID": "4158bb23-aa4c-4111-a298-3a182a785e42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-12T02:32:41.715Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XmV9jTCms71sifQaPVtkgq`</summary>

```json
{
  "query": "\"From Prompts to Properties\" property-based testing LLM code generation FSE 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44b84b26-6e86-4f7d-8456-a67624838676",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtfBWzYfyLS4ZmUaY7d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af2c2cde-775e-4ebe-8e92-105e9101dec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1PDnMFYi33GuUznadJeSz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2843,
      "cache_read_input_tokens": 32741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2843,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-12T02:32:42.080Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015thRBdTYGrX8EU4zSo3AdQ`</summary>

```json
{
  "query": "LLMLOOP iterative code test feedback loop specification 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af2c2cde-775e-4ebe-8e92-105e9101dec9",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011CawtfBWzYfyLS4ZmUaY7d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a77fca83-71a5-43de-9bbb-c1e40506223e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1PDnMFYi33GuUznadJeSz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2843,
      "cache_read_input_tokens": 32741,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2843
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 32741,
          "cache_creation_input_tokens": 2843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2843,
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

_source line 84 · 2026-05-12T02:32:47.575Z_

<details><summary>↩ Tool result · `toolu_01XmV9jTCms71sifQaPVtkgq`</summary>

```text
Web search results for query: ""From Prompts to Properties" property-based testing LLM code generation FSE 2025"

Links: [{"title":"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing | Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/3696630.3728702"},{"title":"From Prompts to Properties: Rethinking LLM Code Generation","url":"https://dl.acm.org/doi/pdf/10.1145/3696630.3728702"},{"title":"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing (LLanMER 2025) - LLanMER 2025","url":"https://conf.researchr.org/details/llanmer-2025/llanmer-2025-papers/7/From-Prompts-to-Properties-Rethinking-LLM-Code-Generation-with-Property-Based-Testin"},{"title":"Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/html/2506.18315v1"},{"title":"Understanding the Characteristics of LLM-Generated Property-Based Tests in Exploring Edge Cases","url":"https://arxiv.org/html/2510.25297v1"},{"title":"From Exploration to Specification: LLM-Based Property Generation for Mobile App Testing","url":"https://arxiv.org/html/2604.13463"},{"title":"[2506.18315] Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/abs/2506.18315"},{"title":"Can Large Language Models Write Good Property-Based Tests? Vasudev Vikram","url":"https://arxiv.org/pdf/2307.04346"},{"title":"Enhancing LLM-Based Test Generation by Eliminating Covered Code","url":"https://arxiv.org/html/2602.21997"},{"title":"Enhanced LLM code generation with property-based testing! New Framework PGS to Break Self-Deception | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/llm-paper/property-generated-solver"}]

Based on the search results, I found information about the paper "From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing" from FSE 2025.

## Summary

"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing" was presented at the 33rd ACM International Conference on the Foundations of Software Engineering (FSE Companion '25) in June 2025.

## Key Contributions

The paper addresses how ensuring correctness in LLM code generation remains a significant challenge, with traditional unit testing failing to capture deeper logical constraints. The authors apply Property-Based Testing (PBT) as an alternative evaluation strategy to StarCoder and CodeLlama on MBPP and HumanEval.

## Findings

The results reveal that while pass@k evaluation shows moderate success, PBT exposes additional correctness gaps, with a significant portion of generated solutions only partially adhering to correctness properties (30–32%), while 18–23% fail outright.

The paper demonstrates how property-based testing can be more effective than traditional unit testing at evaluating the correctness of LLM-generated code by focusing on abstract logical properties rather than specific input-output examples.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af2c2cde-775e-4ebe-8e92-105e9101dec9",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "0c36697e-3f73-48b7-9f4b-cfc841a84a2a",
  "sourceToolAssistantUUID": "af2c2cde-775e-4ebe-8e92-105e9101dec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-12T02:32:49.922Z_

<details><summary>↩ Tool result · `toolu_015thRBdTYGrX8EU4zSo3AdQ`</summary>

```text
Web search results for query: "LLMLOOP iterative code test feedback loop specification 2025"

Links: [{"title":"LLMLOOP: Improving LLM-Generated Code and Tests ...","url":"https://valerio-terragni.github.io/assets/pdf/ravi-icsme-2025.pdf"},{"title":"LLMLOOP: Improving LLM-Generated Code and Tests through Automated Iterative Feedback Loops (ICSME 2025 - Tool Demonstration Track) - ICSME 2025 - International Conference on Software Maintenance and Evolution","url":"https://conf.researchr.org/details/icsme-2025/icsme-2025-tool-demonstration/8/LLMLOOP-Improving-LLM-Generated-Code-and-Tests-through-Automated-Iterative-Feedback-"},{"title":"LLMLOOP: Improving LLM-Generated Code and","url":"https://arxiv.org/pdf/2603.23613"},{"title":"(PDF) LLMLOOP: Improving LLM-Generated Code and Tests through Automated Iterative Feedback Loops","url":"https://www.researchgate.net/publication/394085087_LLMLOOP_Improving_LLM-Generated_Code_and_Tests_through_Automated_Iterative_Feedback_Loops"},{"title":"LLMLOOP: Improving LLM-Generated Code and Tests Through Automated Iterative Feedback Loops | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11185878/"},{"title":"LLMloop: Improving LLM-Generated Code and Tests through Automated Iterative Feedback Loops","url":"https://arxiv.org/html/2603.23613v1"},{"title":"[PDF] LLM LOOP : Improving LLM-Generated Code and Tests through Automated Iterative Feedback Loops | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLM-LOOP-:-Improving-LLM-Generated-Code-and-Tests-Ravi-Bradshaw/a7da0a5b7331a5e4a97fc944d2a8e84bafc42179"},{"title":"CodeContests-O: Powering LLMs via Feedback-Driven Iterative Test Case Generation","url":"https://arxiv.org/html/2601.13682"},{"title":"Improve Code Generation with Feedback | OpenReview","url":"https://openreview.net/forum?id=CscKx97jBi"},{"title":"Helping LLMs Improve Code Generation Using Feedback from Testing and Static Analysis","url":"https://arxiv.org/html/2412.14841v1"}]

Based on the search results, I found comprehensive information about LLMLOOP. Here's what I discovered:

## LLMLOOP Overview

LLMLOOP is a framework that automates the refinement of both source code and test cases produced by LLMs. It leverages iterative feedback loops and multiple analysis methods to enhance LLM-generated JAVA code.

## The Five Iterative Feedback Loops

LLMLOOP employs five iterative loops: resolving compilation errors, addressing static analysis issues, fixing test case failures, and improving test quality through mutation analysis.

More specifically:

1. **Loop 1 - Compilation Errors**: The first feedback loop ensures all generated or modified code is compilable, with the process beginning with an initial prompt to the LLM, supplemented with comments to direct it to produce JAVA 11-compliant code.

2. **Loop 3 - Static Analysis**: When all given tests pass or the budget is reached, the framework performs static analysis using the PMD MAVEN plugin, which is an extensible multilanguage static code analysis tool that detects common programming flaws like unused variables, empty catch blocks, unnecessary object creation, etc.

3. **Test Validation**: If failures occur for the LLM-generated tests, the details are sent back to the LLM for refinement, and this iterative process continues until the test suite passes all tests.

## Performance Results

LLMLOOP improves the quality of LLM-generated code with a pass@10 of 90.24% versus pass@10 of 76.22% for the baseline.

The framework was presented at the 41st IEEE International Conference on Software Maintenance and Evolution (ICSME 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a77fca83-71a5-43de-9bbb-c1e40506223e",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "af9c297b-34c7-4e29-964e-ebba17c240d4",
  "sourceToolAssistantUUID": "a77fca83-71a5-43de-9bbb-c1e40506223e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-12T02:32:52.664Z_

Now let me look for a couple more papers that might be very close competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af9c297b-34c7-4e29-964e-ebba17c240d4",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011Cawtg4b3zgsL5gyKi4z3m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5b188c4-1139-4d52-b7a5-6e63cd50c520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADtsFLxXfLAaHanAm7TRiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2122,
      "cache_read_input_tokens": 35584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2122,
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

_source line 87 · 2026-05-12T02:32:53.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VLB9qExJx9MiXaiFh8kqN4`</summary>

```json
{
  "query": "SpecGen automated generation formal program specification LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5b188c4-1139-4d52-b7a5-6e63cd50c520",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011Cawtg4b3zgsL5gyKi4z3m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6ee9587-5c4e-4cf2-8f8e-d9a5ae04ed2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADtsFLxXfLAaHanAm7TRiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2122,
      "cache_read_input_tokens": 35584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2122,
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

_source line 88 · 2026-05-12T02:32:53.742Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014H6SDihubXZ6Gdp7VE3jxE`</summary>

```json
{
  "query": "\"semantic re-ranking\" specification code generation LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6ee9587-5c4e-4cf2-8f8e-d9a5ae04ed2d",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011Cawtg4b3zgsL5gyKi4z3m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5ae02f7-e06f-4af6-b9e7-656267a577c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADtsFLxXfLAaHanAm7TRiU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2122,
      "cache_read_input_tokens": 35584,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 35584,
          "cache_creation_input_tokens": 2122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2122,
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

_source line 89 · 2026-05-12T02:33:01.461Z_

<details><summary>↩ Tool result · `toolu_01VLB9qExJx9MiXaiFh8kqN4`</summary>

```text
Web search results for query: "SpecGen automated generation formal program specification LLM 2024 2025"

Links: [{"title":"[2401.08807] SpecGen: Automated Generation of Formal Program Specifications via Large Language Models","url":"https://arxiv.org/abs/2401.08807"},{"title":"SpecGen: Automated Generation of Formal Program Specifications via Large Language Models | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00129"},{"title":"SpecGen: Automated Generation of Formal Program Specifications via Large Language Models","url":"https://arxiv.org/html/2401.08807v1"},{"title":"SpecGen: Automated Generation of Formal Program ...","url":"https://arxiv.org/pdf/2401.08807"},{"title":"[2401.08807v1] SpecGen: Automated Generation of Formal Program Specifications via Large Language Models","url":"https://arxiv.org/abs/2401.08807v1"},{"title":"SpecGen: Automated Generation of Formal Program Specifications via Large Language Models | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/11029684/11029718/11029962.pdf"},{"title":"SpecGen: Automated Generation of Formal Program Specifications via Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/392965895_SpecGen_Automated_Generation_of_Formal_Program_Specifications_via_Large_Language_Models"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"SpecGen: Automated Generation of Formal Program Specifications via Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2401.08807v5"},{"title":"dblp: SpecGen: Automated Generation of Formal Program Specifications via Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2401-08807.html"}]

I found comprehensive information about SpecGen. Here are the key findings from the search results:

## Overview

SpecGen is a novel technique for formal program specification generation based on Large Language Models. Formal program specifications play a crucial role in various stages of software development, but manually crafting formal program specifications is rather difficult, making the job time-consuming and labor-intensive.

## Approach

SpecGen's workflow comes in two phases: in the first phase, conversation-driven specification generation, it aims to query output specifications by conducting a conversation with the LLM. The second phase, designed for where the LLM fails to generate correct specifications, applies four mutation operators to the model-generated specifications and selects verifiable specifications from the mutated ones through a novel heuristic selection strategy.

## Performance Results

SpecGen was evaluated on two datasets, including the SV-COMP Java category benchmark and a manually constructed dataset, with experimental results demonstrating that SpecGen succeeds in generating verifiable specifications for 279 out of 385 programs, outperforming the existing purely LLM-based approaches and conventional specification generation tools like Houdini and Daikon.

## Publication Status

The paper was first submitted on January 16, 2024, with subsequent versions released through 2025, with the latest version dated February 25, 2025. SpecGen was published at the IEEE/ACM 47th International Conference on Software Engineering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6ee9587-5c4e-4cf2-8f8e-d9a5ae04ed2d",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "77bf5a2b-b049-4288-9851-91d26ad8c2fa",
  "sourceToolAssistantUUID": "d6ee9587-5c4e-4cf2-8f8e-d9a5ae04ed2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-12T02:33:01.730Z_

<details><summary>↩ Tool result · `toolu_014H6SDihubXZ6Gdp7VE3jxE`</summary>

```text
Web search results for query: ""semantic re-ranking" specification code generation LLM 2025 2026"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"Bridging the Gap between User Intent and LLM: A Requirement Alignment Approach for Code Generation","url":"https://arxiv.org/html/2604.16198v1"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Evaluating LLMs for Source Code Generation and Summarization Using Machine Learning Classification and Ranking","url":"https://www.mdpi.com/2073-431X/15/2/119"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation | OpenReview","url":"https://openreview.net/forum?id=6pr7BUGkLp"},{"title":"Semantic Operators and Their Optimization: Enabling","url":"https://www.vldb.org/pvldb/vol18/p4171-patel.pdf"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"The 2026 LLM Landscape: A Strategic Guide to Semantic Authority","url":"https://aunimeda.com/blog/llm-landscape-2026-guide-for-ctos"},{"title":"Ultimate Guide - The Best Open Source LLMs for Information Retrieval & Semantic Search in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-llm-for-information-retrieval-and-semantic-search"}]

Based on the search results, I found relevant research related to semantic re-ranking, specification-based approaches, and code generation with LLMs in 2025-2026. Here are the key findings:

## Recent Research on Specifications and Code Generation

Despite rapid advances in large language models for code generation from natural-language descriptions, a critical question remains: whether LLMs truly understand the intended program behavior. Executable behavioral specifications provide a concrete and expressive way to evaluate this form of understanding.

Executable behavioral specification generation is significantly harder than code generation, suggesting that strong solution-generation ability does not necessarily imply a deep understanding of intended program semantics.

## Self-Authored Specification Approach

A particularly relevant methodology is the Self-Spec approach: Self-Spec prompts a model to (i) design a compact spec schema it prefers, (ii) instantiate that schema from a problem's docstring and signature, (iii) resolve ambiguities via a minimal Q&A loop, and (iv) generate code only from the confirmed spec.

Self-Spec improves code generation for stronger models: GPT-4o 87%→92% (+5) and Claude 3.7 92%→94% (+2) on HumanEval (pass@1, single sample).

## LLM Selection for Code Tasks

Research investigates the use of machine learning classification and ranking methods to select the best-suited open-source LLMs for code generation and code summarization tasks.

The search results indicate active research in 2025-2026 on improving code generation reliability through specification-based approaches and better ranking/selection methods for LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5ae02f7-e06f-4af6-b9e7-656267a577c0",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a9b53bfb6b47df469",
  "type": "user",
  "uuid": "db816d95-e019-4cee-8054-93d9521326a1",
  "sourceToolAssistantUUID": "c5ae02f7-e06f-4af6-b9e7-656267a577c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 91 · 2026-05-12T02:34:22.787Z_

I now have a comprehensive picture. Here is my full report.

---

## Competitive Landscape Analysis for ExeSpec (2024--2026)

I searched across seven queries and fetched abstracts for 15+ papers. Below are the most relevant works organized by degree of overlap with ExeSpec's core ideas (specifications as intermediate reasoning, execution-based verification, training-free inference-time methods for code tasks).

---

### TIER 1: DIRECTLY COMPETING / HIGHLY OVERLAPPING

These papers share the most DNA with ExeSpec and should be cited or distinguished in the proposal.

**1. Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation**
- Authors: Zihao Xu, Xiao Cheng, Jingling Xue, Yuekang Li
- Venue: Agents4Science 2025 (October 2025)
- URL: [OpenReview](https://openreview.net/forum?id=6pr7BUGkLp)
- Overlap: Very high. Self-Spec prompts an LLM to (i) design its own specification schema, (ii) instantiate it from a docstring, (iii) resolve ambiguities via Q&A, (iv) generate code only from the confirmed spec. It is training-free, uses specifications as an explicit intermediate, and targets code generation. Results: +5 pp on HumanEval for GPT-4o.
- Key difference from ExeSpec: Self-Spec lets the model choose its own spec format (not necessarily pre/postconditions/invariants), does NOT use execution-based verification of the specifications, and lacks the behavioral grounding loop. ExeSpec's emphasis on *execution-grounded* specs (actually running preconditions/postconditions against test cases) is a distinguishing feature.

**2. CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation**
- Authors: Zaoyu Chen, Jianbo Dai, Boyu Zhu, et al.
- Date: April 14, 2026 (arXiv)
- URL: [arXiv:2604.12268](https://arxiv.org/abs/2604.12268)
- Overlap: Very high. CodeSpecBench is a benchmark specifically for LLM generation of *executable behavioral specifications defined via preconditions and postconditions* -- exactly ExeSpec's intermediate representation. It evaluates 15 LLMs on correctness (accepting valid behaviors) and completeness (rejecting invalid behaviors). It also shows that generated specs can improve code generation via semantic re-ranking (+2-3 pp pass@1).
- Key difference from ExeSpec: CodeSpecBench is primarily a benchmark, not a method. Its downstream application (semantic re-ranking) is simpler than ExeSpec's full specification-guided reasoning pipeline. However, it directly validates the premise that executable behavioral specs are useful for code generation.

**3. Property-Generated Solver (PGS): Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback**
- Authors: Lehan He, Zeren Chen, Zhe Zhang, Xiang Gao, Lu Sheng
- Date: June 2025 (arXiv:2506.18315), revised May 2026
- URL: [arXiv:2506.18315](https://arxiv.org/abs/2506.18315)
- Overlap: High. PGS uses two LLM agents -- a Generator and a Tester -- where the Tester formulates property-based tests (high-level behavioral properties like "sorting produces non-decreasing sequences") and feeds the simplest failing counterexample back to the Generator. Training-free, uses properties as intermediate reasoning, and execution-grounded via PBT. Results: +23-37% relative gains over TDD methods.
- Key difference from ExeSpec: PGS uses properties for *refinement feedback* (post-hoc correction), while ExeSpec uses specifications as *upfront intermediate reasoning* (preconditions, postconditions, invariants generated before code). PGS focuses on minimal counterexamples rather than full behavioral specification.

**4. SpecGen: Automated Generation of Formal Program Specifications via Large Language Models**
- Authors: SpecGen team
- Venue: ICSE 2025
- URL: [arXiv:2401.08807](https://arxiv.org/abs/2401.08807)
- Overlap: High. SpecGen uses conversation-driven LLM prompting to generate formal specifications (JML annotations including preconditions, postconditions, loop invariants), then applies mutation operators and heuristic selection when LLM-generated specs fail verification. Succeeds on 279/385 programs.
- Key difference from ExeSpec: SpecGen targets formal verification (generating specs for existing code), not code generation. It generates specs *for* code rather than using specs *to generate* code. It also targets JML/Java rather than Python and uses static verification rather than execution-based checking.

**5. Clover: Closed-Loop Verifiable Code Generation**
- Authors: Chuyue Sun, Ying Sheng, et al. (Stanford)
- Venue: CAV/SAIV 2024, with versions through late 2024
- URL: [arXiv:2310.17807](https://arxiv.org/abs/2310.17807)
- Overlap: High. Clover generates code, docstrings, and formal annotations (postconditions) together, then runs consistency checking among them using formal verification tools + LLMs. Achieves up to 87% acceptance for correct instances with zero false positives. Uses Dafny.
- Key difference from ExeSpec: Clover uses *formal* (deductive) verification rather than *execution-based* checking. It generates code and specs jointly for consistency checking, whereas ExeSpec generates specs first as intermediate reasoning. Clover requires Dafny, limiting practical applicability.

---

### TIER 2: SIGNIFICANTLY RELATED

**6. Automatic Generation of Formal Specification and Verification Annotations Using LLMs and Test Oracles**
- Authors: Joao Pascoal Faria, Emanuel Trigo, Vinicius Honorato, Rui Abreu
- Date: January 2026 (arXiv:2601.12845)
- URL: [arXiv:2601.12845](https://arxiv.org/abs/2601.12845)
- Relevance: Generates preconditions, postconditions, loop invariants, and proof helpers for Dafny programs using LLMs (Claude Opus 4.5 + GPT-5.2), with iterative repair via verifier feedback. Training-free. 98.2% success within 8 iterations. Uses test assertions as static oracles to validate pre/postconditions.
- Difference: Targets formal verification annotation of existing code (Dafny), not code generation from NL descriptions.

**7. NL2Contract: Beyond Postconditions -- Can LLMs Infer Formal Contracts for Automatic Software Verification?**
- Authors: Cedric Richter, Heike Wehrheim
- Date: October 2025 (arXiv:2510.12702)
- URL: [arXiv:2510.12702](https://arxiv.org/abs/2510.12702)
- Relevance: Translates NL to formal functional contracts (preconditions + postconditions). Shows contracts reduce false alarms in automatic verification vs. postconditions alone.
- Difference: Targets verification (finding bugs in existing code), not code generation. Does not use specs as intermediate reasoning for generating code.

**8. From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing**
- Venue: FSE Companion 2025
- URL: [ACM DL](https://dl.acm.org/doi/10.1145/3696630.3728702)
- Relevance: Applies PBT to evaluate LLM-generated code, finding that 30-32% of solutions only partially adhere to properties and 18-23% fail outright, exposing correctness gaps missed by unit tests.
- Difference: Uses properties for *evaluation*, not as intermediate reasoning for generation.

**9. LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering (SSDE)**
- Authors: Shuzhao Feng, Boqi Chen, Brett H Meyer, Gunter Mussbacher
- Venue: FSE Companion 2026 (accepted May 2026)
- URL: [arXiv:2605.02455](https://arxiv.org/abs/2605.02455)
- Relevance: Uses structured specifications as LLM inputs for repository-level code generation, arguing they provide superior verifiability. Training-free prompting approach.
- Difference: Focuses on repository-level MVC generation with structured NL specs, not executable behavioral specifications with pre/postconditions.

**10. Spec Kit Agents: Context-Grounded Agentic Workflows**
- Authors: Pardis Taghavi, Santosh Bhavani (GitHub)
- Date: April 2026 (arXiv:2604.05278)
- URL: [arXiv:2604.05278](https://arxiv.org/abs/2604.05278)
- Relevance: Multi-agent pipeline that generates SPEC.md/PLAN.md/TASKS.md as intermediate artifacts before code, with validation hooks that check structural/referential constraints. Training-free.
- Difference: Uses NL-level specs and structural validation (file paths exist, libs present), not executable behavioral specifications with execution-based checking.

---

### TIER 3: RELATED BUT LESS DIRECTLY COMPETITIVE

**11. RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning**
- Venue: ICML 2025
- URL: [arXiv:2410.02089](https://arxiv.org/abs/2410.02089)
- Relevance: Uses execution feedback for code LLMs, but via RL training (not training-free).

**12. Code Execution as Grounded Supervision for LLM Reasoning**
- Venue: EMNLP 2025
- URL: [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1260/)
- Relevance: Extracts verifiable CoT from code execution traces. Training-based (supervision).

**13. Self-Execution Simulation Improves Coding Models**
- Authors: Gallil Maimon et al.
- Date: March 2026 (arXiv:2604.03253)
- Relevance: Models learn to simulate execution step-by-step for self-verification and self-fixing. Requires fine-tuning + RL (not training-free).

**14. LLMLOOP: Improving LLM-Generated Code and Tests through Automated Iterative Feedback Loops**
- Venue: ICSME 2025
- Relevance: Five iterative loops (compilation, static analysis, test failures, mutation analysis) for code+test co-refinement. Training-free but uses test-pass feedback, not behavioral specifications.

**15. Understanding Specification-Driven Code Generation with LLMs (CURRANTE)**
- Venue: SANER 2026 (Registered Report)
- URL: [arXiv:2601.03878](https://arxiv.org/abs/2601.03878)
- Relevance: Empirical study of spec-first TDD workflow (Specification -> Tests -> Function). Human-in-the-loop; studies how test refinement affects code quality.

**16. FuzzFeed: Weakest Precondition Generation using LLMs and Fuzzing**
- Date: July 2025 (arXiv:2507.05272)
- Relevance: Combines LLMs + fuzz testing to generate weakest preconditions, using execution feedback for iterative context refinement.

**17. REA-Coder: Requirement Alignment for Code Generation**
- Date: April 2026 (arXiv:2604.16198)
- Relevance: Training-free iterative requirement alignment via QA checklists before code generation. Uses NL requirements, not formal specs.

**18. Structured Chain-of-Thought Prompting for Code Generation (SCoT)**
- Venue: TOSEM 2025
- Relevance: Uses programming structures (sequential, branch, loop) as structured intermediate reasoning for code generation. Training-free prompting.
- Difference: Uses algorithmic/structural intermediates, not behavioral specifications.

---

### SUMMARY OF KEY GAPS AND POSITIONING

The most important papers ExeSpec should address are:

1. **Self-Spec** -- the closest competitor using specs-as-intermediate-reasoning. ExeSpec's differentiator is execution-based grounding of specifications.
2. **CodeSpecBench** -- validates the premise that executable behavioral specs (preconditions/postconditions) can improve code generation. ExeSpec could use this benchmark.
3. **PGS** -- closest in using execution-grounded properties, but for refinement rather than upfront reasoning.
4. **SpecGen/Clover** -- use formal specifications but for verification, not as intermediate reasoning for generation, and rely on deductive (not execution-based) checking.

ExeSpec's unique combination of (a) pre/postconditions/invariants as intermediate reasoning, (b) execution-based verification of those specifications, and (c) training-free inference-time application appears to be a genuine gap in the literature, though Self-Spec and PGS each capture parts of this combination.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db816d95-e019-4cee-8054-93d9521326a1",
  "isSidechain": true,
  "agentId": "a9b53bfb6b47df469",
  "requestId": "req_011Cawtgw5e1FjWUPRfGgVhb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e47b3f52-30ce-4fc4-80e7-002b73a09070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9hidHv3ecFGCzoYFVEnX7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 37706,
      "output_tokens": 3267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1986
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3267,
          "cache_read_input_tokens": 37706,
          "cache_creation_input_tokens": 1986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1986,
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
