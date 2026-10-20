# Research conversation: Search for the current best open-source language models as of May 2026 that would be suitable for code generation and co

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a640b56e22515d6fa.jsonl`
- **Structured JSON:** [`70d06620817745050279.json`](../../sessions/70/70d06620817745050279.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-16T05:29:11.949Z_

Search for the current best open-source language models as of May 2026 that would be suitable for code generation and code repair tasks. Use WebSearch:

1. "best open source code LLM 2026" 
2. "SOTA open source language model code generation May 2026"
3. "Qwen3 Coder 2026" or "Qwen 3 code model"
4. "DeepSeek Coder V3 2026" or "DeepSeek V3 code"
5. "open source LLM leaderboard code 2026"
6. "best 7B 14B code model 2026 open source"
7. "StarCoder 3 2026" or latest StarCoder
8. "CodeLlama successor 2026" or "Llama 4 code"
9. Search HuggingFace open LLM leaderboard for top code models

Report the top 3-5 open-source models suitable for fine-tuning for code repair, including:
- Model name and size variants
- Release date
- Key benchmarks (HumanEval, MBPP, SWE-bench if available)
- Whether they support RL fine-tuning (important for this project)
- License

Focus on models in the 7B-32B parameter range that are practical for RL training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "1c2598c6-5525-4273-85cf-ae7fc615e41f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T05:29:11.953Z_

```json
{
  "parentUuid": "1c2598c6-5525-4273-85cf-ae7fc615e41f",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
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
  "uuid": "1460759c-9638-4be5-9b1f-eeedcaa8d409",
  "timestamp": "2026-05-16T05:29:11.953Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T05:29:14.731Z_



I'll search for the latest open-source code LLMs. Let me first load the WebSearch tool, then run all the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1460759c-9638-4be5-9b1f-eeedcaa8d409",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMmj32u6xHpbJTpSkq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "214a0d28-927a-4086-b4b4-82120fee7d66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137BvBuWZ7aQqJG1Luw6Jj9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 848,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 4 · 2026-05-16T05:29:14.901Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RG18Abag3EUdKj7yuaEiGb`</summary>

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
  "parentUuid": "214a0d28-927a-4086-b4b4-82120fee7d66",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMmj32u6xHpbJTpSkq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74c703c4-783d-4614-b4c5-6b2c55cfd308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137BvBuWZ7aQqJG1Luw6Jj9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 7304,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 848,
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

_source line 5 · 2026-05-16T05:29:14.904Z_

<details><summary>↩ Tool result · `toolu_01RG18Abag3EUdKj7yuaEiGb`</summary>

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
  "parentUuid": "74c703c4-783d-4614-b4c5-6b2c55cfd308",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "c3668b9b-fe44-4e58-ad4b-3095258a75a6",
  "sourceToolAssistantUUID": "74c703c4-783d-4614-b4c5-6b2c55cfd308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T05:29:17.245Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3668b9b-fe44-4e58-ad4b-3095258a75a6",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMzYTrPM5SNfVJCwHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a15fa0c2-c3ba-43e3-bd5d-364787889dfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JscMn46wGXjgATA7MVoT74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 7 · 2026-05-16T05:29:17.725Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YXnuZcjUsqjrvz79cFK4Q3`</summary>

```json
{
  "query": "best open source code LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a15fa0c2-c3ba-43e3-bd5d-364787889dfc",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMzYTrPM5SNfVJCwHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb8e430b-e66f-4bbf-a4ff-d078c3a41b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JscMn46wGXjgATA7MVoT74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 8 · 2026-05-16T05:29:17.862Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014VJAPpvjyjv9S6YsGbsVWx`</summary>

```json
{
  "query": "SOTA open source language model code generation May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb8e430b-e66f-4bbf-a4ff-d078c3a41b39",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMzYTrPM5SNfVJCwHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d08d1f51-89a6-410d-acdf-b1e5e68ff72f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JscMn46wGXjgATA7MVoT74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 9 · 2026-05-16T05:29:18.231Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PTHhPNAMp2jEYqWbgEUDaP`</summary>

```json
{
  "query": "Qwen3 Coder 2026 code model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d08d1f51-89a6-410d-acdf-b1e5e68ff72f",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMzYTrPM5SNfVJCwHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2aeee6c-2a87-4222-ac5c-e0b9158647a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JscMn46wGXjgATA7MVoT74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 10 · 2026-05-16T05:29:18.671Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MxSkVQFd5L8B9tpgNVNuvB`</summary>

```json
{
  "query": "DeepSeek Coder V3 2026 code generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2aeee6c-2a87-4222-ac5c-e0b9158647a4",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMzYTrPM5SNfVJCwHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8007916f-6069-4d3a-b36a-cc1fea6b0b97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JscMn46wGXjgATA7MVoT74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 11 · 2026-05-16T05:29:19.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AWdQUtX6f3sihZ1GiUc5VE`</summary>

```json
{
  "query": "open source LLM leaderboard code 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8007916f-6069-4d3a-b36a-cc1fea6b0b97",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMzYTrPM5SNfVJCwHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fe01012-af8c-4366-a942-66f7ada1ac17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JscMn46wGXjgATA7MVoT74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 12 · 2026-05-16T05:29:19.168Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D4T74W62WnHh9nrCApjBr7`</summary>

```json
{
  "query": "best 7B 14B code model 2026 open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fe01012-af8c-4366-a942-66f7ada1ac17",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMzYTrPM5SNfVJCwHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a63e0598-fee3-40dc-a7fd-e121bef9dcf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JscMn46wGXjgATA7MVoT74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 13 · 2026-05-16T05:29:19.642Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RtP1BbEQZHCCkAc6ESPNHx`</summary>

```json
{
  "query": "StarCoder 3 2026 latest StarCoder model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a63e0598-fee3-40dc-a7fd-e121bef9dcf4",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMzYTrPM5SNfVJCwHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff1e0a26-4fa0-472c-a2e2-ca53dad7a051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JscMn46wGXjgATA7MVoT74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 14 · 2026-05-16T05:29:20.114Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JXHp8vFCV2RwappnhzdLWo`</summary>

```json
{
  "query": "CodeLlama successor 2026 Llama 4 code model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff1e0a26-4fa0-472c-a2e2-ca53dad7a051",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMzYTrPM5SNfVJCwHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f916f508-9ad0-40ad-81fb-9a5895a02f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JscMn46wGXjgATA7MVoT74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 15 · 2026-05-16T05:29:20.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014tTeRnLpKgRkQZVUn2tJbr`</summary>

```json
{
  "query": "HuggingFace open LLM leaderboard top code models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f916f508-9ad0-40ad-81fb-9a5895a02f56",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hMzYTrPM5SNfVJCwHu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2648c1e6-689b-4dab-8de7-f6c567f40be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JscMn46wGXjgATA7MVoT74",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8152,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1423
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 463,
          "cache_read_input_tokens": 8152,
          "cache_creation_input_tokens": 1423,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1423,
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

_source line 16 · 2026-05-16T05:29:24.665Z_

<details><summary>↩ Tool result · `toolu_01YXnuZcjUsqjrvz79cFK4Q3`</summary>

```text
Web search results for query: "best open source code LLM 2026"

Links: [{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Best Open Source LLM February 2026 | Benchmarks + Self-Hosting Guide","url":"https://whatllm.org/blog/best-open-source-models-february-2026"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Ultimate Guide - Best Open Source LLM for Software Development in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLM-for-software-development"},{"title":"Best Open-Source LLMs in 2026 - Ranked | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"The Best Open Source LLMs for Coding in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-coding"}]

Based on the search results, here are the best open source code LLMs in 2026:

## Top Picks for Coding

Kimi K2.6 Thinking currently leads on both Coding (78.57) and Agentic Coding (58.33), making it one of the strongest options for code-related tasks.

The top three recommendations for 2026 are moonshotai/Kimi-Dev-72B, Qwen/Qwen3-Coder-480B-A35B-Instruct, and zai-org/GLM-4.5-Air for software development specifically.

## Other Notable Models

Qwen 3 235B-A22B currently leads on the broadest range of benchmarks, combining top-tier reasoning, coding, and multilingual capabilities under an Apache 2.0 license.

Qwen3.5-397B-A17B is the latest flagship model from the Qwen family, combining a large MoE architecture with multimodal reasoning and ultra-long context support.

GLM-5 and GLM-5.1 remain strong open-source options for long-context coding and agentic tasks, both scoring 55.00 on Agentic Coding.

## Key Consideration

There is no single best open-source LLM for everyone—the best model depends on what you need: coding accuracy, local hardware, license freedom, API cost, context length, or tool-use ability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb8e430b-e66f-4bbf-a4ff-d078c3a41b39",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "676d9843-a4c0-4e96-8a44-0798cd229a60",
  "sourceToolAssistantUUID": "bb8e430b-e66f-4bbf-a4ff-d078c3a41b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T05:29:25.035Z_

<details><summary>↩ Tool result · `toolu_01PTHhPNAMp2jEYqWbgEUDaP`</summary>

```text
Web search results for query: "Qwen3 Coder 2026 code model"

Links: [{"title":"GitHub - QwenLM/Qwen3-Coder: Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. · GitHub","url":"https://github.com/QwenLM/Qwen3-Coder"},{"title":"Qwen/Qwen3-Coder-Next · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Coder-Next"},{"title":"qwen3-coder","url":"https://ollama.com/library/qwen3-coder"},{"title":"Alibaba Cloud Model Studio:Code capabilities (Qwen-Coder)","url":"https://www.alibabacloud.com/help/en/model-studio/qwen-coder"},{"title":"Qwen3-Coder-Next: Pushing Small Hybrid Models","url":"https://qwen.ai/blog?id=qwen3-coder-next"},{"title":"Qwen3-Coder-Next Local Deployment: A Complete Developer Guide (2026)","url":"https://www.sitepoint.com/qwen3codernext-local-deployment-a-complete-developer-guide-2026/"},{"title":"Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model","url":"https://qwen.ai/blog?id=qwen3.6-27b"},{"title":"qwen3-coder-next","url":"https://www.ollama.com/library/qwen3-coder-next"},{"title":"Model Providers | Qwen Code Docs","url":"https://qwenlm.github.io/qwen-code-docs/en/users/configuration/model-providers/"},{"title":"GitHub - QwenLM/qwen-code: An open-source AI agent that lives in your terminal. · GitHub","url":"https://github.com/QwenLM/qwen-code"}]

Based on the search results, here's what I found about Qwen3 Coder 2026:

## Overview

Qwen3-Coder is described as "our most agentic code model to date." Qwen3-Coder is available in multiple sizes, including Qwen3-Coder-480B-A35B-Instruct, Qwen3-Coder-30B-A3B-Instruct, and Qwen3-Coder-Next, offering exceptional performance in both coding and agentic tasks.

## Qwen3-Coder-Next (Key Model)

Qwen3-Coder-Next is an open-weight language model designed specifically for coding agents and local development, built on top of Qwen3-Next-80B-A3B-Base with a hybrid attention and MoE architecture, trained at scale on large-scale executable task synthesis, environment interaction, and reinforcement learning.

### Key Features

- **Efficiency**: With only 3B activated parameters (80B total parameters), it achieves performance comparable to models with 10–20x more active parameters, making it highly cost-effective for agent deployment.

- **Context Length**: Long context support with 256K tokens natively and up to 1M tokens using extrapolation methods, optimized for repository-scale understanding.

- **Performance**: Qwen3-Coder-Next achieves over 70% on SWE-Bench Verified using the SWE-Agent scaffold.

The model is available through platforms like Hugging Face, ModelScope, and Ollama for deployment and local use.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2aeee6c-2a87-4222-ac5c-e0b9158647a4",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "3169ccea-e236-4c82-bffc-f548c20a6a45",
  "sourceToolAssistantUUID": "e2aeee6c-2a87-4222-ac5c-e0b9158647a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T05:29:25.084Z_

<details><summary>↩ Tool result · `toolu_014VJAPpvjyjv9S6YsGbsVWx`</summary>

```text
Web search results for query: "SOTA open source language model code generation May 2026"

Links: [{"title":"Code Generation Benchmarks 2026: SOTA LLMs ...","url":"https://www.codesota.com/code-generation"},{"title":"GitHub - BudEcosystem/code-millenials: SOTA OpenSource code generation model on par with GPT-4 & Beating Google Gemini Ultra, Claude -2 etc. · GitHub","url":"https://github.com/BudEcosystem/code-millenials"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"GitHub - rafska/awesome-local-llm: A curated list of awesome platforms, tools, practices and resources that helps run LLMs locally · GitHub","url":"https://github.com/rafska/awesome-local-llm"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"GLM-4.5 Now Available on SiliconFlow: Open-Source SOTA Model for Reasoning, Code, and Agentic Applications","url":"https://www.siliconflow.com/blog/glm-4-5-now-available-on-siliconflow-open-source-sota-model-for-reasoning-code-and-agentic-applications"},{"title":"The State-of-the-Art in Open-Source Large Language Models: A New Era of AI Innovation | by Frank Morales Aguilera | AI Simplified in Plain English | Medium","url":"https://medium.com/ai-simplified-in-plain-english/the-state-of-the-art-in-open-source-large-language-models-a-new-era-of-ai-innovation-9a379aad0a23"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"},{"title":"Kilo - Best AI Coding Models 2026","url":"https://kilo.ai/leaderboard"},{"title":"Top 6 SOTA LLMs for Code, Web search, Research and More - Analytics Vidhya","url":"https://www.analyticsvidhya.com/blog/2025/03/top-sota-llms/"}]

Based on the web search results, here's what's currently state-of-the-art for open-source language models in code generation as of May 2026:

## Top Open-Source Models for Code Generation

Claude Opus 4.7 shipped on 2026-04-16 and leads SWE-bench Verified at 87.6% under the Claude Code harness.

For open-source options specifically, the best open-source LLMs in 2026 are Meta Llama 4 for general reasoning, Mistral Large for speed and efficiency, and Qwen 2.5 for multilingual tasks.

### Notable Open-Source Code Models

GLM-4.5 delivers state-of-the-art results among open-source models in reasoning, code generation and agentic capabilities, with industry-leading performance in real-world code agent evaluations.

Qwen3-Coder-480B-A35B-Instruct is a Mixture-of-Experts (MoE) code generation model optimized for agentic coding tasks, while Qwen3-Coder-Next is an open-weight causal language model optimized for coding agents and local development workflows.

Additional specialized coding models mentioned include OmniCoder-9B, NousCoder-14B, and FrogBoss-32B-2510 & FrogMini-14B-2510 coding agents.

### General Performance Gap

Open-weight models now trail the SOTA proprietary models by only about three months on average.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d08d1f51-89a6-410d-acdf-b1e5e68ff72f",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "a00278ed-4635-481f-ab3c-516133d166fa",
  "sourceToolAssistantUUID": "d08d1f51-89a6-410d-acdf-b1e5e68ff72f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T05:29:25.481Z_

<details><summary>↩ Tool result · `toolu_01MxSkVQFd5L8B9tpgNVNuvB`</summary>

```text
Web search results for query: "DeepSeek Coder V3 2026 code generation"

Links: [{"title":"DeepSeek Coder","url":"https://deepseekcoder.github.io/"},{"title":"DeepSeek V3 - DeepSeek","url":"https://deepseak.org/deepseek-v3/"},{"title":"DeepSeek","url":"https://www.deepseek.com/en/"},{"title":"Explore Code Generation Using DeepSeek Coder Models · Cloudflare Workers AI docs","url":"https://developers.cloudflare.com/workers-ai/guides/tutorials/explore-code-generation-using-deepseek-coder-models/"},{"title":"DeepSeek Coder - DeepSeek","url":"https://deepseak.org/deepseek-coder/"},{"title":"DeepSeek for Coding Review: Coding, Features & Use Cases | Second Talent","url":"https://www.secondtalent.com/resources/deepseek-for-coding/"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder: DeepSeek Coder: Let the Code Write Itself · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder"},{"title":"DeepSeek-V3.2 Release | DeepSeek API Docs","url":"https://api-docs.deepseek.com/news/news251201"},{"title":"deepseek-coder","url":"https://ollama.com/library/deepseek-coder"},{"title":"GitHub - deepseek-ai/DeepSeek-V3 · GitHub","url":"https://github.com/deepseek-ai/deepseek-v3"}]

Based on the search results, here's what I found about DeepSeek Coder and code generation capabilities:

## DeepSeek Coder Overview

DeepSeek Coder comprises a series of code language models trained from scratch on both 87% code and 13% natural language in English and Chinese, with each model pre-trained on 2T tokens. DeepSeek Coder is an AI model built for fast and accurate code generation and debugging.

## DeepSeek Coder V2 & V3 Capabilities

With 236 billion total parameters but only 21 billion activated during inference, DeepSeek Coder V2 achieves performance comparable to GPT-4 Turbo on coding benchmarks while supporting an expanded set of 338 programming languages.

DeepSeek Coder-V3 extends context to 128K tokens, making it suitable for large codebases, multi-file projects, and extended workflows.

## Performance on Benchmarks

Compared with CodeLLama-34B, it leads by 7.9%, 9.3%, 10.8% and 5.9% respectively on HumanEval Python, HumanEval Multilingual, MBPP and DS-1000. DeepSeek-Coder-Instruct-33B model after instruction tuning outperforms GPT-3.5-turbo on HumanEval and achieves comparable result with GPT-3.5-turbo on MBPP.

## Availability

DeepSeek is fully open source and released under the MIT license. Developers can download the model weights from GitHub or Hugging Face and use them for both research and commercial projects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8007916f-6069-4d3a-b36a-cc1fea6b0b97",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "80d2390e-e2cd-40f0-9100-15c99788cd7c",
  "sourceToolAssistantUUID": "8007916f-6069-4d3a-b36a-cc1fea6b0b97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T05:29:25.502Z_

<details><summary>↩ Tool result · `toolu_01RtP1BbEQZHCCkAc6ESPNHx`</summary>

```text
Web search results for query: "StarCoder 3 2026 latest StarCoder model"

Links: [{"title":"What is StarCoder? Key Features & Pricing - Milestone","url":"https://mstone.ai/tools-wizard/starcoder/"},{"title":"StarCoder — NeMo-AutoModel","url":"https://docs.nvidia.com/nemo/automodel/latest/model-coverage/llm/bigcode/starcoder.html"},{"title":"GitHub - bigcode-project/starcoder2: Home of StarCoder2! · GitHub","url":"https://github.com/bigcode-project/starcoder2"},{"title":"GitHub - bigcode-project/starcoder: Home of StarCoder: fine-tuning & inference! · GitHub","url":"https://github.com/bigcode-project/starcoder"},{"title":"starcoder:3b","url":"https://ollama.com/library/starcoder:3b"},{"title":"Best AI Coding Tools 2026: 7 Tested [Ranked] - Tech Insider","url":"https://tech-insider.org/ai-coding-tools-2026-transforming-software-development/"},{"title":"starcoder","url":"https://ollama.com/library/starcoder"},{"title":"bigcode/starcoder2-3b · Hugging Face","url":"https://huggingface.co/bigcode/starcoder2-3b"},{"title":"ServiceNow and Hugging Face Release StarCoder - ServiceNow Press","url":"https://www.servicenow.com/uk/company/investor-relations/financials/starcoder.html"},{"title":"StarCoder Reviews in 2026","url":"https://sourceforge.net/software/product/StarCoder/"}]

Based on the search results, here's what I found about StarCoder 3 and the latest StarCoder models in 2026:

## StarCoder 3

StarCoder 3, developed by the BigCode project with contributions from over 600 researchers, pushed the frontier on repository-level code understanding. StarCoder 3 is available as an open source option that developers can run locally using tools like Continue, Tabby, and Ollama-based coding setups.

## Recent StarCoder Versions

The most well-documented recent version is StarCoder2, which was released in 2024 and comes in three sizes: 3B, 7B, and 15B, trained on The Stack v2 with support for 600+ languages and featuring a 16K context window.

StarCoder2 is a family of code generation models trained on 600+ programming languages from The Stack v2 and some natural language text such as Wikipedia, Arxiv, and GitHub issues.

## Availability

Open source StarCoder models provide complete data privacy and zero ongoing cost — a critical advantage for security-conscious organizations and independent developers. These models can be deployed through various platforms including Hugging Face, Ollama, and other local deployment options.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff1e0a26-4fa0-472c-a2e2-ca53dad7a051",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "0d33dad8-57fb-4a95-909e-c612711495ff",
  "sourceToolAssistantUUID": "ff1e0a26-4fa0-472c-a2e2-ca53dad7a051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T05:29:25.955Z_

<details><summary>↩ Tool result · `toolu_01D4T74W62WnHh9nrCApjBr7`</summary>

```text
Web search results for query: "best 7B 14B code model 2026 open source"

Links: [{"title":"The Best Open Source and Open-Weight LLM Models to Run Locally in 2026","url":"https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally"},{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Best Local Coding Models Ranked: Every VRAM Tier, Every Benchmark (2026) | InsiderLLM","url":"https://insiderllm.com/guides/best-local-coding-models-2026/"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"5 Open-Source Coding LLMs You Can Run Locally in 2026","url":"https://www.labellerr.com/blog/best-coding-llms/"},{"title":"Best Open-Source LLMs in 2026: A Practical Guide by Use Case - ML Journey","url":"https://mljourney.com/best-open-source-llms-in-2026-a-practical-guide-by-use-case/"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"qwen2.5-coder:14b","url":"https://ollama.com/library/qwen2.5-coder:14b"},{"title":"The Complete Guide to Open-Source AI Models in 2026 | ClawBench","url":"https://www.clawbench.com/articles/best-open-source-ai-models-2026"},{"title":"Best Coding LLMs to Run Locally in 2026 - ML Journey","url":"https://mljourney.com/best-coding-llms-to-run-locally-in-2026/"}]

Based on the search results, here are the best 7B and 14B open-source code models for 2026:

## Top Recommendations

**For 7B models:**

Qwen2.5-Coder from Alibaba is the strongest coding model family available for local use in 2026, with the 7B variant fitting comfortably on 8GB VRAM and producing code quality that rivals models twice its size.

**For 14B models:**

Qwen2.5-Coder 14B is recommended if you have 16GB+ VRAM. For tab-complete/FIM (Fill-in-the-Middle), Qwen 2.5-Coder (7B/14B/32B) is still unmatched at every tier.

## Key Features of Qwen2.5-Coder

Alibaba's Qwen2.5-Coder family dominates coding benchmarks at every size tier in 2026, with the 7B variant outperforming general-purpose models twice its size on code generation, debugging, and refactoring.

Qwen 2.5 Coder 32B performs excellent across more than 40 programming languages, scoring 65.9 on McEval.

## Alternative Options

If you need faster inference with MoE (Mixture of Experts) architecture, DeepSeek-Coder-V2 16B provides similar quality at higher token throughput.

## Hardware Requirements

For 8GB VRAM, Qwen2.5-Coder 7B covers 90% of everyday use cases well. For 16GB VRAM, Qwen2.5-Coder 14B provides noticeably better quality and handles longer contexts reliably.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a63e0598-fee3-40dc-a7fd-e121bef9dcf4",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "10f9b58a-d3ad-437a-b54c-167fcd0a690b",
  "sourceToolAssistantUUID": "a63e0598-fee3-40dc-a7fd-e121bef9dcf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T05:29:26.371Z_

<details><summary>↩ Tool result · `toolu_01JXHp8vFCV2RwappnhzdLWo`</summary>

```text
Web search results for query: "CodeLlama successor 2026 Llama 4 code model"

Links: [{"title":"Llama 4 Coder: How to Run Meta","url":"https://ai-coding-flow.com/blog/llama-4-coder-local-coding-assistant-2026/"},{"title":"GitHub - meta-llama/codellama: Inference code for CodeLlama models · GitHub","url":"https://github.com/meta-llama/codellama"},{"title":"Ollama Models Cheat Sheet 2026 | ComputingForGeeks","url":"https://computingforgeeks.com/ollama-models-cheat-sheet/"},{"title":"CodeLlama (Meta) - Wiki | clawbot","url":"https://clawbot.ai/wiki/voice-memory/codellama.html"},{"title":"codellama","url":"https://ollama.com/library/codellama"},{"title":"Meta Code Llama","url":"https://www.llama.com/code-llama/"},{"title":"llama.cpp Code Generation Tutorial: Build a Local Coding Assistant [2026] | Markaicode","url":"https://markaicode.com/tutorial/llamacpp-code-generation-tutorial/"},{"title":"GitHub - ex3ndr/llama-coder: Replace Copilot local AI · GitHub","url":"https://github.com/ex3ndr/llama-coder"},{"title":"Best Ollama Models: 12 Models Ranked for Coding, RAG & Agents (2026) | Morph","url":"https://www.morphllm.com/best-ollama-models"},{"title":"Llama 4 Complete Developer Guide (2026): Variants, Benchmarks, License, Hosting","url":"https://codersera.com/blog/llama-4-complete-guide-2026/"}]

Based on the web search results, here's what I found about CodeLlama's successor and Llama 4 code models in 2026:

## Llama 4 Coder - CodeLlama's Successor

In 2026, Meta released Llama 4 Coder, a new generation of open-source large models specifically designed for code generation and understanding. Llama 4 Coder represents a significant leap forward compared to Llama 3 and the previous CodeLlama models.

While Llama 3 is a general-purpose LLM, Llama 4 Coder is laser-focused on coding tasks. Unlike its predecessors, Llama 4 Coder focuses exclusively on coding tasks, leading to significant performance gains in code generation, completion, and debugging.

## Performance and Variants

The 70B model provides a strong balance of performance and resource requirements, while the 8B model offers accessibility for those with limited hardware. While GPT-4o and Claude Opus still hold a slight edge, Llama 4 Coder's open-source nature and local execution capabilities make it a highly attractive option for many developers.

## Competitive Landscape

It's worth noting that while Llama 4 Coder is a capable successor to CodeLlama, qwen2.5-coder:32b is the strongest local coding model in 2026, scoring within a few points of GPT-4o on Aider's pass-rate benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f916f508-9ad0-40ad-81fb-9a5895a02f56",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "d19547ea-398d-46a5-a33c-9329fc36b855",
  "sourceToolAssistantUUID": "f916f508-9ad0-40ad-81fb-9a5895a02f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T05:29:27.096Z_

<details><summary>↩ Tool result · `toolu_01AWdQUtX6f3sihZ1GiUc5VE`</summary>

```text
Web search results for query: "open source LLM leaderboard code 2026"

Links: [{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Open Source LLM Leaderboard 2026: Rankings, Benchmarks & the Best Models Right Now &#045; VERTU® Official Site","url":"https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now"},{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Best LLM for Coding - Vellum","url":"https://www.vellum.ai/best-llm-for-coding"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Open-Source LLM Leaderboard: February 2026 | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/open-source-llm-leaderboard/"},{"title":"open-llm-leaderboard (Open LLM Leaderboard)","url":"https://huggingface.co/open-llm-leaderboard"},{"title":"Open Source LLM Leaderboard 2025–2026: Llama, Mistral, DeepSeek, Qwen | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm/open-models"}]

Based on the web search results, here are the key open source LLM leaderboards and code resources for 2026:

## Major Open Source LLM Leaderboards

The Open LLM Leaderboard compares the best open source LLMs with rankings, pricing, speed, and benchmark scores. It provides an independent ranking of open-weight large language models — Llama, Qwen, GLM, DeepSeek, Mistral, Kimi and more — by coding-arena score, GPQA Diamond, throughput, latency, and per-token pricing, and is updated continuously from provider APIs and verified benchmarks.

The Vellum open source LLM leaderboard displays the latest public benchmark performance for open-weight and open-source models released after April 2024, with data coming from model providers as well as independently run evaluations by Vellum or the open-source community.

The Vellum coding LLM leaderboard compares the latest models on engineering-specific benchmarks including SWE-Bench, LiveCodeBench, Aider Polyglot, BFCL tool use, and more.

The Awesome Agents open-source LLM leaderboard ranks open-weight and open-source models exclusively, covering models whose weights are publicly available for download, fine-tuning, and self-hosting.

## Key Resources

The Open LLM Leaderboard organization on Hugging Face maintains the leaderboard, with the hub containing the dataset with detailed results and queries for the models, score results, and current state of requests.

CodeSOTA provides a leaderboard with benchmark comparisons across open-weight models including DeepSeek-R1, Llama 3, Qwen 2.5, Mistral, and Gemma 3, updated April 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fe01012-af8c-4366-a942-66f7ada1ac17",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "d6e91c62-2e08-4031-b6ab-86b16a9f29d4",
  "sourceToolAssistantUUID": "3fe01012-af8c-4366-a942-66f7ada1ac17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T05:29:30.343Z_

<details><summary>↩ Tool result · `toolu_014tTeRnLpKgRkQZVUn2tJbr`</summary>

```text
Web search results for query: "HuggingFace open LLM leaderboard top code models 2026"

Links: [{"title":"Open LLM Leaderboard best models ❤️‍🔥 - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-best-models"},{"title":"open-llm-leaderboard (Open LLM Leaderboard)","url":"https://huggingface.co/open-llm-leaderboard"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Show HN: How I topped the HuggingFace open LLM leaderboard on two gaming GPUs | Hacker News","url":"https://news.ycombinator.com/item?id=47322887"},{"title":"Hugging Face Open LLM Leaderboard 2026: How Anti-Contamination Controls Reshuffled the Rankings | AgentMarketCap","url":"https://agentmarketcap.ai/blog/2026/04/10/huggingface-open-llm-leaderboard-v3-2026"},{"title":"Official Benchmarks Leaderboard 2026 - a Hugging Face Space by OpenEvals","url":"https://huggingface.co/spaces/OpenEvals/every-leaderboards"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"blog/open-llm-leaderboard-mmlu.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/open-llm-leaderboard-mmlu.md"},{"title":"LLM Performance Leaderboard - a Hugging Face Space by ArtificialAnalysis","url":"https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard"}]

Based on the search results, here's what I found about the HuggingFace Open LLM Leaderboard and top code models in 2026:

## Top Models for Coding

For the best coding models, test Kimi K2.6 and GLM-5.1. Kimi K2.6 and GLM-5.1 are recommended as the top coding models.

## Overall Leaderboard Leaders

GLM-5 leads the 2026 open-weight leaderboard at 85 while Llama 4 Scout sits at 24. Chinese research labs—primarily Zhipu AI (Z.AI), Alibaba, Moonshot AI, and DeepSeek—hold the majority of top positions across multiple independent leaderboards.

GLM-5's architecture represents a significant scaling step from its predecessor: 744B total parameters (40B active per forward pass), with a substantially expanded pretraining dataset versus the prior-generation 355B/32B design.

## Key 2026 Models by Use Case

- For clean commercial licensing, start with Qwen3 or Gemma 4
- For local deployment, start with Gemma 4 26B A4B or Phi-4
- DeepSeek V3.2 wins on reasoning and coding quality

## Important Note on Rankings

When Hugging Face launched Open LLM Leaderboard v2 in late 2024, the goal was to solve benchmark contamination by replacing saturated tests with six harder ones, which significantly reshuffled the rankings in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2648c1e6-689b-4dab-8de7-f6c567f40be5",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "34ad201b-09c5-4c5e-840b-efa6906deff7",
  "sourceToolAssistantUUID": "2648c1e6-689b-4dab-8de7-f6c567f40be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-16T05:29:33.055Z_

Now let me get more specific details on benchmarks and fine-tuning suitability for the top candidates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34ad201b-09c5-4c5e-840b-efa6906deff7",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hP8N34bSqGbuvs3ctX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dd3ec52-1ac5-4150-bda2-68570d8e5d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVWTTNuUzV86CxHUJYYNnC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8859,
      "cache_read_input_tokens": 9575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8859,
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

_source line 26 · 2026-05-16T05:29:33.548Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Q1LAhDJou9sQTkL6ouSde`</summary>

```json
{
  "query": "Qwen3-Coder-Next benchmarks HumanEval MBPP SWE-bench parameters fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dd3ec52-1ac5-4150-bda2-68570d8e5d67",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hP8N34bSqGbuvs3ctX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "565f53da-f0e2-43f9-8db1-7e976757cae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVWTTNuUzV86CxHUJYYNnC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8859,
      "cache_read_input_tokens": 9575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8859,
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

_source line 27 · 2026-05-16T05:29:34.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YCWPzdDy9zTFyrjQE1XEeC`</summary>

```json
{
  "query": "Qwen 2.5 Coder 32B benchmarks HumanEval MBPP RL fine-tuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "565f53da-f0e2-43f9-8db1-7e976757cae6",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hP8N34bSqGbuvs3ctX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3503daa-fbef-4e0a-8198-78ff955e93d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVWTTNuUzV86CxHUJYYNnC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8859,
      "cache_read_input_tokens": 9575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8859,
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

_source line 28 · 2026-05-16T05:29:35.469Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YBqsb54Wd27gvcoSXqtdMM`</summary>

```json
{
  "query": "Qwen3.6-27B code benchmarks release date license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3503daa-fbef-4e0a-8198-78ff955e93d5",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hP8N34bSqGbuvs3ctX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b940975f-a60b-4552-846a-8de17e09190c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVWTTNuUzV86CxHUJYYNnC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8859,
      "cache_read_input_tokens": 9575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8859,
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

_source line 29 · 2026-05-16T05:29:36.151Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ME89pJmxAEk6noxEB7RSS2`</summary>

```json
{
  "query": "Llama 4 Coder 8B benchmarks HumanEval release date license 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b940975f-a60b-4552-846a-8de17e09190c",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hP8N34bSqGbuvs3ctX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5701054-dbbb-4992-98b1-48980d81870b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVWTTNuUzV86CxHUJYYNnC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8859,
      "cache_read_input_tokens": 9575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8859,
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

_source line 30 · 2026-05-16T05:29:36.486Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016iAyu4Yj1DmL2pk6uUBJ2K`</summary>

```json
{
  "query": "NousCoder-14B benchmarks release date license fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5701054-dbbb-4992-98b1-48980d81870b",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hP8N34bSqGbuvs3ctX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8182335-4c88-48d7-9065-406398c49e3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVWTTNuUzV86CxHUJYYNnC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8859,
      "cache_read_input_tokens": 9575,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8859
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 330,
          "cache_read_input_tokens": 9575,
          "cache_creation_input_tokens": 8859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8859,
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

_source line 31 · 2026-05-16T05:29:40.877Z_

<details><summary>↩ Tool result · `toolu_01YBqsb54Wd27gvcoSXqtdMM`</summary>

```text
Web search results for query: "Qwen3.6-27B code benchmarks release date license"

Links: [{"title":"Qwen3.6-27B: 27B Model Beats 397B on Coding (2026)","url":"https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026"},{"title":"Qwen3.6-27B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen3.6-27b"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model","url":"https://qwen.ai/blog?id=qwen3.6-27b"},{"title":"Qwen3.6 27B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/qwen3-6-27b"},{"title":"Qwen: Qwen3.6 27B Review | Pricing, Benchmarks & Capabilities (2026) | Design for Online","url":"https://designforonline.com/ai-models/alibaba-qwen3-6-27b-reasoning/"},{"title":"Qwen3.6-27B: Dense 27B That Beats 397B MoE on Agentic Coding","url":"https://localaimaster.com/models/qwen-3-6-27b"},{"title":"Qwen3.6–27B Is The New King (April 2026) | by Andrew Zhu | Apr, 2026 | Medium","url":"https://xhinker.medium.com/qwen3-6-27b-is-the-new-king-april-2026-09467b6c6335"},{"title":"How to Use Qwen3.6-27B: Complete Guide to Alibaba's New Open-Weight Coding Model | Tosea.ai","url":"https://tosea.ai/blog/qwen-3-6-27b-complete-guide"},{"title":"Qwen3.6 27B - API Pricing & Providers | OpenRouter","url":"https://openrouter.ai/qwen/qwen3.6-27b"}]

Based on the search results, here's information about Qwen3.6-27B:

**Release Date:** Qwen3.6-27B was released by Alibaba on April 22, 2026 (though one source indicates April 21, 2026).

**License:** The model is released under the Apache 2.0 license, which is an open-source/open-weight license.

**Code Benchmarks:** The model demonstrates strong coding performance across multiple benchmarks:
- SWE-bench Verified: 77.2, SWE-bench Pro: 53.5, Terminal-Bench 2.0: 59.3, and SkillsBench: 48.2
- On reasoning tasks, Qwen3.6-27B achieves 87.8 on GPQA Diamond

**Key Achievement:** The 27-billion-parameter model outperformed a 397-billion-parameter model on agentic coding benchmarks, specifically surpassing the previous-generation open-source flagship Qwen3.5-397B-A17B (397B total / 17B active MoE) across all major coding benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b940975f-a60b-4552-846a-8de17e09190c",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "9c1ce8ba-9954-4bc7-b171-8d998d3713ac",
  "sourceToolAssistantUUID": "b940975f-a60b-4552-846a-8de17e09190c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T05:29:41.593Z_

<details><summary>↩ Tool result · `toolu_01YCWPzdDy9zTFyrjQE1XEeC`</summary>

```text
Web search results for query: "Qwen 2.5 Coder 32B benchmarks HumanEval MBPP RL fine-tuning 2026"

Links: [{"title":"Qwen2.5-Coder Series: Powerful, Diverse, Practical. | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-coder-family/"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v3"},{"title":"Qwen 2.5 Coder 32B Hardware Requirements: Running a 32B Coding Model Locally | CraftRigs","url":"https://craftrigs.com/guides/qwen-2-5-coder-32b-hardware-guide/"},{"title":"Technical Report Qwen2.5-Coder Technical Report Binyuan Hui* Jian Yang*","url":"https://arxiv.org/pdf/2409.12186"},{"title":"Qwen 2.5 Coder 32B | Open Laboratory","url":"https://openlaboratory.ai/models/qwen-2_5-coder-32b"},{"title":"Qwen2.5-LLM: Extending the boundary of LLMs | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-llm/"},{"title":"Qwen2.5-Coder Series: Powerful, Diverse, Practical - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/qwen2-5-coder-series-powerful-diverse-practical_601765"},{"title":"Qwen2.5-Coder 32B Instruct vs Qwen3 32B Comparison","url":"https://llm-stats.com/models/compare/qwen-2.5-coder-32b-instruct-vs-qwen3-32b"},{"title":"Qwen AI for Coding: Reviews, Usage and Performance in 2026 | Second Talent","url":"https://www.secondtalent.com/resources/qwen-ai-for-coding-reviews-usage-and-performance/"},{"title":"qwen2.5-coder-32b-instruct Model by Qwen | NVIDIA NIM","url":"https://build.nvidia.com/qwen/qwen2_5-coder-32b-instruct/modelcard"}]

Based on the search results, here's comprehensive information about Qwen2.5-Coder-32B benchmarks:

## HumanEval and MBPP Performance

Qwen2.5-Coder-32B-Instruct scores 92.7% on HumanEval and 90.2% on MBPP. Through 4-stage filtering with high-quality Text-Code Grounding Data, average scores on HumanEval and MBPP increased from 41.6% to 46.8% compared to the baseline.

## Overall Benchmark Performance

Qwen2.5-Coder-32B has demonstrated strong code completion capabilities on pre-trained models, achieving SOTA (state-of-the-art) performance on a total of 5 benchmarks: Humaneval-Infilling, CrossCodeEval, CrossCodeLongEval, RepoEval, and SAFIM.

Qwen2.5-Coder-32B-Instruct has achieved the best performance among open-source models on multiple popular code generation benchmarks (EvalPlus, LiveCodeBench, BigCodeBench), and has competitive performance with GPT-4o.

## Training and Fine-tuning

Qwen2.5-Coder-32B was trained on an extensive dataset comprising approximately 5.5 trillion tokens that include a blend of source code, instructional text-code samples, and synthetic data, curated to cover programming languages and task diversity. Training strategies, such as instruction tuning and alignment, support capabilities in creative task following, role-playing, and multi-turn dialogue, which are relevant for code assistant applications.

The model represents significant advances in code generation performance through careful data curation, filtering strategies, and instruction alignment techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3503daa-fbef-4e0a-8198-78ff955e93d5",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "1e5ac2db-3fbd-4aef-a5a8-a08120393973",
  "sourceToolAssistantUUID": "a3503daa-fbef-4e0a-8198-78ff955e93d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T05:29:41.745Z_

<details><summary>↩ Tool result · `toolu_011Q1LAhDJou9sQTkL6ouSde`</summary>

```text
Web search results for query: "Qwen3-Coder-Next benchmarks HumanEval MBPP SWE-bench parameters fine-tuning"

Links: [{"title":"Qwen3-Coder-Next: Pushing Small Hybrid Models","url":"https://qwen.ai/blog?id=qwen3-coder-next"},{"title":"Qwen3-Coder-Next Technical Report","url":"https://arxiv.org/html/2603.00729v1"},{"title":"2026-03-03 Qwen3-Coder-Next Technical Report Qwen Team","url":"https://arxiv.org/pdf/2603.00729"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3-Coder-Next: How to Run Locally | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3-coder-next"},{"title":"Evaluating Large Language Models on Self-invoking Code ...","url":"https://aclanthology.org/2025.findings-acl.686.pdf"},{"title":"Technical Report Qwen2.5-Coder Technical Report Binyuan Hui* Jian Yang*","url":"https://arxiv.org/pdf/2409.12186"},{"title":"Qwen3-Coder-Next Hardware Guide — GPU, VRAM & RAM (2026) | Compute Market","url":"https://www.compute-market.com/blog/qwen-3-coder-next-local-hardware-guide-2026"},{"title":"Qwen3-Coder-Next: Local Coding AI, 70% SWE-Bench (2026) | Local AI Master","url":"https://localaimaster.com/models/qwen-3-coder-next"},{"title":"Qwen3-Coder-Next: The Complete 2026 Guide to Running Powerful AI Coding Agents Locally - DEV Community","url":"https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95"}]

Based on the search results, here's comprehensive information about Qwen3-Coder-Next benchmarks, parameters, and fine-tuning:

## Model Parameters

Qwen3-Coder-Next is an 80-billion-parameter model that activates only 3 billion parameters during inference, enabling strong coding capability with efficient inference. The model is built on top of Qwen3-Next-80B-A3B-Base, which adopts a novel architecture with hybrid attention and MoE.

## Benchmark Performance

**SWE-Bench Results:**
- Qwen3-Coder-Next achieves scores of 70.6% with SWE-Agent, 71.1% with MiniSWE-Agent, and 71.3% with OpenHands on SWE-Bench Verified.
- Qwen3-Coder-Next achieves over 70% on SWE-Bench Verified using the SWE-Agent scaffold.
- Qwen3-Coder-Next (3B active) achieves SWE-Bench-Pro performance comparable to models with 10×–20× more active parameters.

## Training Approach

Rather than focusing on traditional supervised fine-tuning on HumanEval and MBPP alone, the model uses a more sophisticated training pipeline:

The model uses a staged pipeline that progressively builds agentic capabilities. Starting from the pretrained base of Qwen3-Next, they first shift representations toward code- and agent-centric domains via continued pretraining, then apply supervised fine-tuning on high-quality agentic coding data.

From this checkpoint, they specialize multiple expert models, covering software engineering workflows, QA, web development, and user experience (UX) focused coding, and then distill their capabilities back into a single unified model.

The model performs agentic training through large-scale synthesis of verifiable coding tasks paired with executable environments, allowing learning directly from environment feedback via mid-training and reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "565f53da-f0e2-43f9-8db1-7e976757cae6",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "275d6a57-e9da-468c-8fa1-75b2b4c67089",
  "sourceToolAssistantUUID": "565f53da-f0e2-43f9-8db1-7e976757cae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T05:29:41.842Z_

<details><summary>↩ Tool result · `toolu_01ME89pJmxAEk6noxEB7RSS2`</summary>

```text
Web search results for query: "Llama 4 Coder 8B benchmarks HumanEval release date license 2026"

Links: [{"title":"New Ollama Models May 2026: Latest Releases & Updates","url":"https://www.promptquorum.com/local-llms/top-open-source-models-ollama"},{"title":"HumanEval Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/humaneval"},{"title":"Best Local LLM Models 2026 | Developer Comparison","url":"https://www.sitepoint.com/best-local-llm-models-2026/"},{"title":"Best Open Source LLM in 2026: Rankings, Benchmarks, and the Models Worth Running | BenchLM.ai","url":"https://benchlm.ai/blog/posts/best-open-source-llm"},{"title":"Best Open-Source LLMs in 2026 - Ranked | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"Best LLM Models for 8GB VRAM in 2026 (Tested and Ranked)","url":"https://inferencerig.com/models/best-llm-models-for-8gb-vram-in-2026-tested-and-ranked/"},{"title":"Home GPU LLM Leaderboard: Best Open Source Models by VRAM Tier with Token/s Benchmarks | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/home-gpu-llm-leaderboard/"},{"title":"Llama-3.1-FoundationAI-SecurityLLM-Reasoning-8B Technical Report","url":"https://arxiv.org/pdf/2601.21051"},{"title":"Best Ollama Models (March 2026): Top 15 Ranked by Task | Local AI Master","url":"https://localaimaster.com/blog/best-ollama-models"},{"title":"Best Open Source LLMs in 2026: Ranked by Coding, Reasoning & Cost | WhatLLM.org","url":"https://whatllm.org/best-open-source-llm"}]

Based on the web search results, I found relevant information about Llama models and HumanEval benchmarks in 2026, though I could not locate specific information about a "Llama 4 Coder 8B" model with the exact details you requested.

Here's what I found about Llama models in 2026:

**Llama 4 Models Available:**
The top open source models in May 2026 include Llama 4 Scout (best overall), which is described as having the best overall quality with a MoE architecture. Llama 4 Scout's 10M token context is unmatched.

**HumanEval Performance:**
The search results show HumanEval benchmarks for various models, but I did not find specific benchmark data for a "Llama 4 Coder 8B" model. Llama 3.3's 8B variant achieves a HumanEval score of 72.6 at Q4_K_M quantization.

**Release Date and License:**
I was unable to find specific information about a "Llama 4 Coder 8B" release date or license from the search results provided.

It's possible that a specific "Llama 4 Coder 8B" model may not yet be released, or may be announced under a different name. The search results predominantly feature Llama 4 Scout as the primary Llama 4 release in 2026, along with other coding-focused models like Qwen series for code generation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5701054-dbbb-4992-98b1-48980d81870b",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "72a26170-fd56-4774-9ca6-abb832398585",
  "sourceToolAssistantUUID": "d5701054-dbbb-4992-98b1-48980d81870b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T05:29:44.900Z_

<details><summary>↩ Tool result · `toolu_016iAyu4Yj1DmL2pk6uUBJ2K`</summary>

```text
Web search results for query: "NousCoder-14B benchmarks release date license fine-tuning"

Links: [{"title":"NousResearch/NousCoder-14B · Hugging Face","url":"https://huggingface.co/NousResearch/NousCoder-14B"},{"title":"NousCoder-14B: Competitive Programming AI Model Explained - SuperGok","url":"https://supergok.com/nouscoder-14b-competitive-programming-ai-model/"},{"title":"Nous Research's NousCoder-14B is an open-source coding model landing right in the Claude Code moment | VentureBeat","url":"https://venturebeat.com/technology/nous-researchs-nouscoder-14b-is-an-open-source-coding-model-landing-right-in"},{"title":"NousCoder-14B: A Competitive Olympiad Programming Model - NOUS RESEARCH","url":"https://nousresearch.com/nouscoder-14b-a-competitive-olympiad-programming-model"},{"title":"Nous Research Releases NousCoder-14B: A Competitive Olympiad Programming Model Post-Trained on Qwen3-14B via Reinforcement Learning - MarkTechPost","url":"https://www.marktechpost.com/2026/01/18/nous-research-releases-nouscoder-14b-a-competitive-olympiad-programming-model-post-trained-on-qwen3-14b-via-reinforcement-learning/"},{"title":"NousCoder-14B: The AI Model Crushing Competitive Programming","url":"https://aicosoft.com/artificial-intelligence/this-new-ai-can-ace-coding-competitions-meet-nouscoder-14b"},{"title":"Nous Research's NousCoder-14B is an open-source coding model landing right in the Claude Code moment · AmericaBots","url":"https://americabots.com/ai-news/nous-researchs-nouscoder-14b-is-an-open-source-coding-model-landing-right-in-the-claude-code-moment/"},{"title":"Inside NousCoder-14B: Open-Source RL Beats Its Base Model as AI Coding Hits a Data Wall - techbuddies.io","url":"https://www.techbuddies.io/2026/01/10/inside-nouscoder-14b-open-source-rl-beats-its-base-model-as-ai-coding-hits-a-data-wall/"},{"title":"Startup News: Key Reasons NousCoder-14B Steps Up Open-Source AI Coding Revolution in 2026","url":"https://launch.femaleswitch.com/startup-news-nouscoder-14b-open-source-ai-coding-revolution-2026/"},{"title":"Nous Research’s NousCoder-14B is an open-source coding model landing right in the Claude Code moment - Boulder Bubble","url":"https://boulderbubble.com/nous-researchs-nouscoder-14b-is-an-open-source-coding-model-landing-right-in-the-claude-code-moment-44/"}]

Based on the search results, here's what I found about NousCoder-14B:

## Release Date

NousCoder-14B was released on January 6, 2026, as announced by Nous Research.

## Benchmarks

On LiveCodeBench v6 (08/01/2024 - 05/01/2025), NousCoder-14B achieves a Pass@1 accuracy of 67.87%, a 7.08% improvement from the baseline Pass@1 accuracy of 60.79% of Qwen3-14B.

## License

The model weights are released with an Apache 2.0 license on Hugging Face.

## Fine-tuning Approach

NousCoder-14B enhances performance by using reinforcement learning (RL) post-training, taking Qwen3-14B as a solid base and re-adapting it to competitive programming with feedback that rewards correct answers and penalizes incorrect or excessively resource-intensive ones.

The model was trained on 24k verifiable coding problems using 48 B200s over the course of four days.

Additionally, Nous Research published the complete reinforcement learning environment, benchmark suite, and training harness — built on the company's Atropos framework — enabling any researcher with sufficient compute to reproduce or extend the work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8182335-4c88-48d7-9065-406398c49e3d",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "abc90864-29a7-4b6b-bd7e-606f4be12cfb",
  "sourceToolAssistantUUID": "f8182335-4c88-48d7-9065-406398c49e3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-16T05:29:47.626Z_

Let me get a few more details on the remaining top candidates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abc90864-29a7-4b6b-bd7e-606f4be12cfb",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hQCZaPrqkH8kUpdeML",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1144d81c-84a9-4517-9509-13cef0e639b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAeeNDR8xmPy8ASApb21yy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5399,
      "cache_read_input_tokens": 18434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5399,
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

_source line 37 · 2026-05-16T05:29:48.110Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A6XbHDQxcXqwUjFLi8gvxn`</summary>

```json
{
  "query": "Qwen3-Coder 30B-A3B benchmarks license release date 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1144d81c-84a9-4517-9509-13cef0e639b0",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hQCZaPrqkH8kUpdeML",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3e3db8a-af9e-450a-b2ed-68d4dc9e168c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAeeNDR8xmPy8ASApb21yy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5399,
      "cache_read_input_tokens": 18434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5399,
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

_source line 38 · 2026-05-16T05:29:49.044Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AYTkJoYKERK45YaJvWyWsw`</summary>

```json
{
  "query": "Qwen2.5-Coder 7B 14B 32B license RL reinforcement learning fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3e3db8a-af9e-450a-b2ed-68d4dc9e168c",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hQCZaPrqkH8kUpdeML",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15fa6c7a-e766-467d-807a-55b929559b03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAeeNDR8xmPy8ASApb21yy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5399,
      "cache_read_input_tokens": 18434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5399,
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

_source line 39 · 2026-05-16T05:29:49.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GJ91AsCoraFHJTLAimjFQT`</summary>

```json
{
  "query": "Qwen3.6-27B HumanEval MBPP LiveCodeBench fine-tuning RL training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15fa6c7a-e766-467d-807a-55b929559b03",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hQCZaPrqkH8kUpdeML",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aafb858b-3b9c-4d5b-9954-f034ce001dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAeeNDR8xmPy8ASApb21yy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5399,
      "cache_read_input_tokens": 18434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5399,
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

_source line 40 · 2026-05-16T05:29:52.812Z_

<details><summary>↩ Tool result · `toolu_01A6XbHDQxcXqwUjFLi8gvxn`</summary>

```text
Web search results for query: "Qwen3-Coder 30B-A3B benchmarks license release date 2026"

Links: [{"title":"Qwen3 Coder 30B A3B Instruct Model Specs, Costs & Benchmarks (April 2026) | Galaxy.ai","url":"https://blog.galaxy.ai/model/qwen3-coder-30b-a3b-instruct"},{"title":"Qwen3 Coder 30B A3B Instruct - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/qwen/qwen3-coder-30b-a3b-instruct"},{"title":"Qwen3 30B A3B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen3-30b-a3b"},{"title":"Qwen3 Coder 30B A3B Instruct API Pricing 2026 - Costs, Performance & Providers","url":"https://pricepertoken.com/pricing-page/model/qwen-qwen3-coder-30b-a3b-instruct"},{"title":"Qwen3-Coder-30B-A3B - Specs & Pricing [2026]","url":"https://getdeploying.com/llms/qwen3-coder-30b-a3b"},{"title":"Qwen3.5 Plus 2026-04-20 vs Qwen3 Coder 30B A3B Instruct (Comparative Analysis) | Galaxy.ai","url":"https://blog.galaxy.ai/compare/qwen3-5-plus-20260420-vs-qwen3-coder-30b-a3b-instruct"},{"title":"Qwen/Qwen3-Coder-30B-A3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct"},{"title":"Qwen3 30B A3B API Pricing 2026 - Costs, Performance & Providers","url":"https://pricepertoken.com/pricing-page/model/qwen-qwen3-30b-a3b"},{"title":"Qwen: Qwen3 30B A3B Review | Pricing, Benchmarks & Capabilities (2026) | Design for Online","url":"https://designforonline.com/ai-models/qwen-qwen3-30b-a3b/"},{"title":"Qwen: Qwen3 Coder 30B A3B Instruct Review — Pricing, Benchmarks & Capabilities (2026) — Design for Online","url":"https://designforonline.com/ai-models/qwen-qwen3-coder-30b-a3b-instruct/"}]

Based on the search results, here's the information about Qwen3-Coder-30B-A3B:

**Release Date:** Qwen3 Coder 30B A3B Instruct was released on July 31, 2025.

**License:** Qwen3 30B A3B is released under the Apache 2.0 license.

**Model Architecture:** Qwen3-Coder-30B-A3B-Instruct is a 30.5B parameter Mixture-of-Experts (MoE) model with 128 experts (8 active per forward pass), designed for advanced code generation, repository-scale understanding, and agentic tool use.

**Context Window:** 160,000 token context window, maximum output of 32,768 tokens.

**Performance:** It has achieved impressive scores in various benchmarks. The search results reference benchmarks but don't provide specific benchmark scores in the detailed content available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3e3db8a-af9e-450a-b2ed-68d4dc9e168c",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "79ae0f4d-abb9-43c4-8c8e-31a7f73b08bf",
  "sourceToolAssistantUUID": "c3e3db8a-af9e-450a-b2ed-68d4dc9e168c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T05:29:56.315Z_

<details><summary>↩ Tool result · `toolu_01GJ91AsCoraFHJTLAimjFQT`</summary>

```text
Web search results for query: "Qwen3.6-27B HumanEval MBPP LiveCodeBench fine-tuning RL training"

Links: [{"title":"Qwen/Qwen3.5-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-27B"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Technical Report Qwen2.5-Coder Technical Report Binyuan Hui* Jian Yang*","url":"https://arxiv.org/pdf/2409.12186"},{"title":"Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model","url":"https://qwen.ai/blog?id=qwen3.6-27b"},{"title":"Evaluating Large Language Models on Self-invoking Code ...","url":"https://aclanthology.org/2025.findings-acl.686.pdf"},{"title":"qwen3.5:27b-q4_K_M","url":"https://ollama.com/library/qwen3.5:27b-q4_K_M"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"What Is Qwen 3.6 Plus? Alibaba's 1M Token Agentic Coding Model Explained | MindStudio","url":"https://www.mindstudio.ai/blog/what-is-qwen-3-6-plus-agentic-coding-model"},{"title":"Qwen3.5-27B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen3.5-27b"},{"title":"How to Use Qwen3.6-27B: Complete Guide to Alibaba's New Open-Weight Coding Model | Tosea.ai","url":"https://tosea.ai/blog/qwen-3-6-27b-complete-guide"}]

Based on the web search results, here's what I found about Qwen3.6-27B and its evaluation on the benchmarks you mentioned:

## Qwen3.6-27B Overview

Qwen3.6 is the first open-weight variant built on direct feedback from the community, prioritizing stability and real-world utility. It's a dense 27-billion-parameter multimodal model.

## Performance on Key Benchmarks

The Qwen3 family performs competitively on standard coding evaluations including HumanEval, MBPP, and LiveCodeBench. With only 27B parameters, it outperforms the Qwen3.5-397B-A17B on every major coding benchmark, though the specific benchmark scores aren't detailed for HumanEval, MBPP, and LiveCodeBench in the search results.

## Training Approach

Qwen3.5 (the predecessor generation) features scalable RL generalization with reinforcement learning scaled across million-agent environments with progressively complex task distributions. While the search results don't explicitly detail Qwen3.6-27B's specific RL training methodology or fine-tuning details for these exact benchmarks, they indicate that RL training is a key component of the Qwen3 series' training pipeline.

The search results focus more on the model's capabilities and deployment rather than detailed technical specifications about fine-tuning procedures for the specific benchmarks you mentioned. For more technical details on the fine-tuning and RL training specifics, you may want to consult the official Qwen3.6 technical report or blog post.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aafb858b-3b9c-4d5b-9954-f034ce001dba",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "66ca2ad5-bdea-4c15-b9f4-aaa064d5eb55",
  "sourceToolAssistantUUID": "aafb858b-3b9c-4d5b-9954-f034ce001dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T05:29:57.305Z_

<details><summary>↩ Tool result · `toolu_01AYTkJoYKERK45YaJvWyWsw`</summary>

```text
Web search results for query: "Qwen2.5-Coder 7B 14B 32B license RL reinforcement learning fine-tuning"

Links: [{"title":"Fine-Tune and Deploy Qwen2.5 - Coder with SFT & DPO on PAI - Alibaba Cloud","url":"https://www.alibabacloud.com/help/en/pai/use-cases/training-evaluation-compression-and-deployment-of-qwen2-5-coder-model"},{"title":"Qwen2.5-Coder-7B Instruct: Precision Code LLM","url":"https://www.emergentmind.com/topics/qwen2-5-coder-7b-instruct"},{"title":"Fine Tune Qwen2.5-VL-32B in 3 Days Complete Hands On Tutorial - Skywork ai","url":"https://skywork.ai/blog/llm/fine-tune-qwen2-5-vl-32b-in-3-days-complete-hands-on-tutorial/"},{"title":"Technical Report: Full-Stack Fine-Tuning for the Q Programming Language","url":"https://arxiv.org/pdf/2508.06813"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v2"},{"title":"[2412.15115] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen 2.5 Coder Fine-tuning with Unsloth","url":"https://unsloth.ai/blog/qwen-coder"},{"title":"Qwen Models: Alibaba’s Next-Generation AI Family for Text, Vision, and Beyond","url":"https://www.inferless.com/learn/the-ultimate-guide-to-qwen-model"},{"title":"Fine-Tuning the Qwen2.5-7B-VL-Instruct Model: A Comprehensive Guide","url":"https://connectaman.hashnode.dev/fine-tuning-the-qwen25-7b-vl-instruct-model-a-comprehensive-guide"}]

Based on the search results, here's what I found about Qwen2.5-Coder models:

## Model Sizes and Architecture

The Qwen2.5-Coder series includes six models: Qwen2.5-Coder-(0.5B/1.5B/3B/7B/14B/32B).

## Licensing

The series has permissive licensing and supports wider adoption by developers, indicating that these models are released under open-source licenses.

## Training and Fine-tuning

Qwen2.5-Coder is built upon the Qwen2.5 architecture and continues pretrained on a vast corpus of over 5.5 trillion tokens. Coder specialization is realized via subsequent post-training optimization and reinforcement learning.

## Reinforcement Learning

Regarding RL fine-tuning specifically, RL-hardened models further improve best-of-N accuracy and agentic reasoning. Qwen2.5-Coder-7B-Instruct serves as a backbone for advanced RL pipelines and agentic coders. RL methods demonstrate label-free reward model training, best-of-N selection, and step-level reward shaping using program execution or visual/GUI-agent scores.

The search results show that Qwen2.5-Coder models support both supervised fine-tuning and reinforcement learning approaches for customization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15fa6c7a-e766-467d-807a-55b929559b03",
  "isSidechain": true,
  "promptId": "0c67e942-8282-4425-bfec-54e2039b6227",
  "agentId": "a640b56e22515d6fa",
  "type": "user",
  "uuid": "67154c58-1201-441f-81fb-d1fcec7315dc",
  "sourceToolAssistantUUID": "15fa6c7a-e766-467d-807a-55b929559b03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T05:30:46.911Z_

Here is my comprehensive report on the top open-source models suitable for fine-tuning for code repair as of May 2026.

---

## Top Open-Source Models for Code Generation / Code Repair (May 2026)

### 1. Qwen3.6-27B (Dense) -- TOP RECOMMENDATION

- **Developer:** Alibaba (Qwen team)
- **Parameters:** 27B dense (all parameters active)
- **Release Date:** April 22, 2026
- **License:** Apache 2.0
- **Key Benchmarks:**
  - SWE-bench Verified: 77.2
  - SWE-bench Pro: 53.5
  - Terminal-Bench 2.0: 59.3
  - GPQA Diamond: 87.8
  - Outperforms the 397B MoE Qwen3.5 flagship on all major coding benchmarks
- **RL Fine-tuning:** Yes. The Qwen3.x family uses scalable RL generalization trained across million-agent environments. The architecture is well-suited for RL post-training. Dense architecture makes gradient computation straightforward compared to MoE models.
- **Why it fits:** At 27B dense parameters, this is the sweet spot -- large enough for strong code understanding and repair, small enough for practical RL training on a moderate GPU cluster. The Apache 2.0 license is fully permissive. It is the current open-source SOTA for agentic coding at this parameter scale.

### 2. NousCoder-14B -- BEST RL-TRAINED PRECEDENT

- **Developer:** Nous Research
- **Base Model:** Qwen3-14B, post-trained with RL
- **Parameters:** 14B dense
- **Release Date:** January 6, 2026
- **License:** Apache 2.0
- **Key Benchmarks:**
  - LiveCodeBench v6 Pass@1: 67.87% (7.08% improvement over Qwen3-14B baseline of 60.79%)
- **RL Fine-tuning:** This model IS the product of RL fine-tuning. Nous Research trained it on 24k verifiable coding problems using 48 B200 GPUs over 4 days. They published the complete RL training environment, benchmark suite, and training harness (built on their Atropos framework), making it directly reproducible.
- **Why it fits:** This is the single most relevant model for your project. It demonstrates exactly the workflow you want: taking a strong base code model and improving it with RL using verifiable coding rewards. The published Atropos training harness can likely be adapted for code repair tasks. At 14B parameters, RL training is highly practical.

### 3. Qwen2.5-Coder-32B-Instruct -- PROVEN WORKHORSE

- **Developer:** Alibaba (Qwen team)
- **Parameters:** 32B dense
- **Release Date:** November 2024 (but remains competitive in 2026)
- **License:** Apache 2.0
- **Key Benchmarks:**
  - HumanEval: 92.7%
  - MBPP: 90.2%
  - SOTA on HumanEval-Infilling, CrossCodeEval, CrossCodeLongEval, RepoEval, SAFIM
  - Competitive with GPT-4o on EvalPlus, LiveCodeBench, BigCodeBench
- **RL Fine-tuning:** Yes. The model's post-training already includes RL optimization. It is widely used as a backbone for RL pipelines, and Unsloth has published guides for fine-tuning it. The 7B and 14B variants in this family are also strong options if compute is limited.
- **Why it fits:** Most battle-tested open-source code model available. Massive community ecosystem, extensive fine-tuning documentation, and multiple size variants (7B/14B/32B) for experimentation. The 32B variant is at the upper boundary of practical RL training; the 14B variant may be the better choice for iterative RL experiments.

### 4. Qwen3-Coder-Next (80B total, 3B active MoE) -- EFFICIENCY PICK

- **Developer:** Alibaba (Qwen team)
- **Parameters:** 80B total, 3B active (MoE with hybrid attention)
- **Release Date:** March 2026
- **License:** Apache 2.0
- **Key Benchmarks:**
  - SWE-bench Verified: 70.6% (SWE-Agent), 71.1% (MiniSWE-Agent), 71.3% (OpenHands)
  - Performance comparable to models with 10-20x more active parameters
  - 256K native context, up to 1M with extrapolation
- **RL Fine-tuning:** Yes -- the model was explicitly trained via environment interaction and reinforcement learning on executable coding tasks. However, MoE architectures are more complex to RL fine-tune than dense models due to load-balancing and routing considerations.
- **Why it fits:** Exceptional inference efficiency (only 3B active params for 70%+ SWE-bench). However, MoE fine-tuning is more complex than dense model fine-tuning, so this is better suited if you need fast inference in production but can invest in the MoE training infrastructure.

### 5. Qwen3-Coder-30B-A3B-Instruct -- COMPACT MoE OPTION

- **Developer:** Alibaba (Qwen team)
- **Parameters:** 30.5B total, ~3B active (128 experts, 8 active per forward pass)
- **Release Date:** July 31, 2025
- **License:** Apache 2.0
- **Context Window:** 160K tokens, 32K max output
- **RL Fine-tuning:** Same MoE caveats as Qwen3-Coder-Next. The smaller total parameter count makes it more manageable for fine-tuning than the 80B variant.
- **Why it fits:** Repository-scale context understanding at efficient inference cost. Good middle ground if you want MoE efficiency but the 80B total params of Coder-Next is too large for your cluster.

---

## Practical Recommendation for Code Repair RL Fine-Tuning

**Start with NousCoder-14B or Qwen3-14B as your base.** Here is why:

1. **NousCoder-14B already proves the RL-for-code pipeline works** at this scale. Nous Research published their entire Atropos training framework, so you have a reference implementation.
2. **14B is the practical sweet spot** for iterative RL experiments -- large enough for strong code understanding, small enough to run many training iterations on a reasonable GPU budget (Nous did it on 48 B200s in 4 days).
3. **Apache 2.0 license** on both NousCoder-14B and its Qwen3-14B base means no restrictions on commercial use or derivative models.
4. **If you need higher ceiling performance**, move to Qwen3.6-27B or Qwen2.5-Coder-32B after validating your RL reward design at 14B scale.

The dominant trend in 2026 is clear: the Qwen model family (Alibaba) holds the top positions across virtually every open-source code benchmark, at every size tier, under the Apache 2.0 license. Chinese research labs collectively hold the majority of top positions on independent leaderboards.

---

Sources:
- [Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model](https://qwen.ai/blog?id=qwen3.6-27b)
- [Qwen/Qwen3.6-27B on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)
- [NousCoder-14B: A Competitive Olympiad Programming Model](https://nousresearch.com/nouscoder-14b-a-competitive-olympiad-programming-model)
- [NousResearch/NousCoder-14B on Hugging Face](https://huggingface.co/NousResearch/NousCoder-14B)
- [Nous Research Releases NousCoder-14B (MarkTechPost)](https://www.marktechpost.com/2026/01/18/nous-research-releases-nouscoder-14b-a-competitive-olympiad-programming-model-post-trained-on-qwen3-14b-via-reinforcement-learning/)
- [Inside NousCoder-14B: Open-Source RL Beats Its Base Model](https://www.techbuddies.io/2026/01/10/inside-nouscoder-14b-open-source-rl-beats-its-base-model-as-ai-coding-hits-a-data-wall/)
- [Qwen2.5-Coder Series: Powerful, Diverse, Practical](https://qwenlm.github.io/blog/qwen2.5-coder-family/)
- [Qwen2.5-Coder Technical Report (arXiv)](https://arxiv.org/html/2409.12186v3)
- [Qwen3-Coder-Next: Pushing Small Hybrid Models](https://qwen.ai/blog?id=qwen3-coder-next)
- [Qwen3-Coder-Next Technical Report (arXiv)](https://arxiv.org/html/2603.00729v1)
- [Qwen/Qwen3-Coder-30B-A3B-Instruct on Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
- [Best Open-Source LLMs in 2026 (BentoML)](https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models)
- [Open Source LLM Leaderboard 2026 (Vellum)](https://www.vellum.ai/open-llm-leaderboard)
- [Best LLM for Coding (Vellum)](https://www.vellum.ai/best-llm-for-coding)
- [Best Open Source Self-Hosted LLMs for Coding in 2026 (Pinggy)](https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/)
- [Qwen 2.5 Coder Fine-tuning with Unsloth](https://unsloth.ai/blog/qwen-coder)
- [HuggingFace Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67154c58-1201-441f-81fb-d1fcec7315dc",
  "isSidechain": true,
  "agentId": "a640b56e22515d6fa",
  "requestId": "req_011Cb5hR7chQJq23LBwpz8D6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd7d25a7-20a7-499a-b207-67b736f96377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e3ca133-70f3-4b03-a31a-714b1591fe65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pZQwzCy4byjy7UKDT7sWs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 962,
      "cache_creation_input_tokens": 2251,
      "cache_read_input_tokens": 23833,
      "output_tokens": 2648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2251
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 962,
          "output_tokens": 2648,
          "cache_read_input_tokens": 23833,
          "cache_creation_input_tokens": 2251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2251,
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
