# Research conversation: Use WebSearch to find the current best open-source language models as of May 2026. I need to know what models are at the

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aaae29ef0dc1bbe1e.jsonl`
- **Structured JSON:** [`2044816cf9a246a2cb82.json`](../../sessions/20/2044816cf9a246a2cb82.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-14T14:33:12.741Z_

Use WebSearch to find the current best open-source language models as of May 2026. I need to know what models are at the frontier for use in a research project on retrieval-augmented reasoning.

Search for:
1. "best open source LLM 2026" 
2. "SOTA open source language model May 2026"
3. "top open source reasoning model 2026"
4. "Qwen3 model 2026" (check if Qwen3 exists and its specs)
5. "DeepSeek R2 model 2026" or "DeepSeek V3 2026"
6. "Llama 4 model 2026" or latest Meta open source LLM
7. "best open source model for reasoning 2026 benchmark"

Report the top 3-5 open-source models suitable for reasoning research, with their parameter counts and any relevant benchmark scores. Focus on models that would be good base models for RL training on reasoning tasks (7B-72B parameter range preferred for research feasibility).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "8be18c2b-9d61-4d0e-be9f-359c57a29892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T14:33:12.743Z_

```json
{
  "parentUuid": "8be18c2b-9d61-4d0e-be9f-359c57a29892",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
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
  "uuid": "7c62dd84-1866-4810-b1a2-070664f3d69d",
  "timestamp": "2026-05-14T14:33:12.743Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T14:33:19.288Z_



I'll start by loading the WebSearch tool schema, then run all the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c62dd84-1866-4810-b1a2-070664f3d69d",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dE2rvKWiHd8LMqbzBG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aac9f723-6ad6-45be-b068-70f1b0351279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YURrhiPZiXovKbzXtnSgr4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 8223,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 785,
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

_source line 4 · 2026-05-14T14:33:19.316Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Lg8XGnePm95djUrjbBxNPy`</summary>

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
  "parentUuid": "aac9f723-6ad6-45be-b068-70f1b0351279",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dE2rvKWiHd8LMqbzBG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd56774b-df3a-449f-9197-ab07babb3003",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YURrhiPZiXovKbzXtnSgr4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 8223,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 785,
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

_source line 5 · 2026-05-14T14:33:19.320Z_

<details><summary>↩ Tool result · `toolu_01Lg8XGnePm95djUrjbBxNPy`</summary>

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
  "parentUuid": "fd56774b-df3a-449f-9197-ab07babb3003",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "d9bc7548-02b4-4b3f-b923-10cd87375670",
  "sourceToolAssistantUUID": "fd56774b-df3a-449f-9197-ab07babb3003",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T14:33:25.554Z_



Now let me run all seven searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9bc7548-02b4-4b3f-b923-10cd87375670",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dEXB1L1PGGiRYxen71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d701b96a-a84b-4d14-94c4-9dfa111289ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHggukZtAYbhTnECiytgFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 7 · 2026-05-14T14:33:26.037Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MV1HE5vqsdbostKVTMU9nN`</summary>

```json
{
  "query": "best open source LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d701b96a-a84b-4d14-94c4-9dfa111289ef",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dEXB1L1PGGiRYxen71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97b579db-760e-4860-b9ff-2d7fc4fe31a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHggukZtAYbhTnECiytgFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 8 · 2026-05-14T14:33:26.509Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DNf9mEy3P6v7FKJNpWMCvy`</summary>

```json
{
  "query": "SOTA open source language model May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97b579db-760e-4860-b9ff-2d7fc4fe31a1",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dEXB1L1PGGiRYxen71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc7d3f7c-0b7e-4b45-83a1-6f471e64dd17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHggukZtAYbhTnECiytgFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 9 · 2026-05-14T14:33:26.520Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ABSN4NzTr7Yyi973Q2PvxK`</summary>

```json
{
  "query": "top open source reasoning model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc7d3f7c-0b7e-4b45-83a1-6f471e64dd17",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dEXB1L1PGGiRYxen71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2b048d3-2df0-44d6-95a2-258d76214fe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHggukZtAYbhTnECiytgFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 10 · 2026-05-14T14:33:27.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gbc3UdpXowrxQebmxiZ5o4`</summary>

```json
{
  "query": "Qwen3 model 2026 specs parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2b048d3-2df0-44d6-95a2-258d76214fe7",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dEXB1L1PGGiRYxen71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a38f2fa0-5ca1-47e3-8894-d5b3b067012f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHggukZtAYbhTnECiytgFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 11 · 2026-05-14T14:33:27.452Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016ggssEAwseLYnQCb5q8MnF`</summary>

```json
{
  "query": "DeepSeek R2 model 2026 OR DeepSeek V3 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a38f2fa0-5ca1-47e3-8894-d5b3b067012f",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dEXB1L1PGGiRYxen71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e0b3935-ddca-46aa-bdfc-396958d9abe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHggukZtAYbhTnECiytgFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 12 · 2026-05-14T14:33:27.888Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0177AABD7CdCsJinAcb4WoUg`</summary>

```json
{
  "query": "Llama 4 model 2026 Meta open source LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e0b3935-ddca-46aa-bdfc-396958d9abe1",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dEXB1L1PGGiRYxen71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "558d8180-252c-4d39-a2e2-4413250743c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHggukZtAYbhTnECiytgFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 13 · 2026-05-14T14:33:27.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FkK8nhcm3mUQGfz5vDCoe3`</summary>

```json
{
  "query": "best open source model for reasoning 2026 benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "558d8180-252c-4d39-a2e2-4413250743c7",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dEXB1L1PGGiRYxen71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56ab497a-1051-44d9-b83a-7fb95a088fca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHggukZtAYbhTnECiytgFt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 9008,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 9008,
          "cache_creation_input_tokens": 1404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1404,
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

_source line 14 · 2026-05-14T14:33:33.641Z_

<details><summary>↩ Tool result · `toolu_01DNf9mEy3P6v7FKJNpWMCvy`</summary>

```text
Web search results for query: "SOTA open source language model May 2026"

Links: [{"title":"The State-of-the-Art in Open-Source Large Language Models: A New Era of AI Innovation | by Frank Morales Aguilera | AI Simplified in Plain English | Medium","url":"https://medium.com/ai-simplified-in-plain-english/the-state-of-the-art-in-open-source-large-language-models-a-new-era-of-ai-innovation-9a379aad0a23"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"[AINews] Z.ai GLM-5: New SOTA Open Weights LLM","url":"https://www.latent.space/p/ainews-zai-glm-5-new-sota-open-weights"},{"title":"CodeSOTA — Open AI Benchmark Registry and SOTA API","url":"https://www.codesota.com/llm"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"},{"title":"What Are the SOTA AI Models? | Machine Learning Glossary","url":"https://maddevs.io/glossary/state-of-the-art-models/"},{"title":"Mixtral 8x22B: SOTA Open-Source LLM Capabilities at a Fraction of the Compute — Jon Krohn","url":"https://www.jonkrohn.com/posts/2024/4/26/mixtral-8x22b-sota-open-source-llm-capabilities-at-a-fraction-of-the-compute"},{"title":"State-of-the-Art (SOTA) AI Models: The Complete Guide","url":"https://acecloud.ai/blog/state-of-the-art-models/"},{"title":"Introducing Ettin Suite: the SoTA open recipe to outperform existing Generative & Retrieval Models - LightOn","url":"https://lighton.ai/lighton-blogs/introducing-ettin-suite-the-sota-open-recipe-to-outperform-existing-generative-retrieval-models"}]

Based on the web search results, here's what's current in the state-of-the-art (SOTA) for open-source language models as of May 2026:

## Leading Open-Source Models

The best open-source LLMs in 2026 are Meta Llama 4 for general reasoning, Mistral Large for speed and efficiency, and Qwen 2.5 for multilingual tasks, with other top models including DeepSeek for coding and Microsoft Phi-4 for high-performance reasoning in small-scale deployments.

## Recent Notable Developments

Recent AIME 2026 results show Kimi and DeepSeek are among the best open-source AI models. Additionally, GLM-5 scales from 355B parameters (32B active) to 744B parameters (40B active), and integrates DeepSeek Sparse Attention (DSA), significantly reducing deployment cost while preserving long-context capacity.

## Performance Trends

Open-weight models now trail the SOTA proprietary models by only about three months on average. Several open source reasoning models now reach near-SOTA benchmark performance (MMLU, reasoning evals) at a fraction of the cost of proprietary providers.

## Key Capabilities

DeepSeek-R1 leverages sophisticated reinforcement learning techniques to develop a "thinking" process that allows it to break down complex problems and derive logical, step-by-step solutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc7d3f7c-0b7e-4b45-83a1-6f471e64dd17",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "2d54505d-77fe-4812-a336-d123fd5bf77f",
  "sourceToolAssistantUUID": "bc7d3f7c-0b7e-4b45-83a1-6f471e64dd17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T14:33:33.882Z_

<details><summary>↩ Tool result · `toolu_016ggssEAwseLYnQCb5q8MnF`</summary>

```text
Web search results for query: "DeepSeek R2 model 2026 OR DeepSeek V3 2026"

Links: [{"title":"The Ultimate DeepSeek Guide 2026 | Master AI with DeepSeek-V3.2 & R2","url":"https://deepseek.ai/blog/deepseek-guide-2026"},{"title":"Ultimate Guide - The Best DeepSeek-AI Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-deepseek-ai-models-in-2025"},{"title":"Will DeepSeek’s new model spark another global AI shake-up in 2026?","url":"https://restofworld.org/2025/deepseek-china-r2-ai-model-us-rivalry/"},{"title":"DeepSeek V4 and R2 Deep Dive | Meta Intelligence","url":"https://www.meta-intelligence.tech/en/insight-deepseek-v4-r2"},{"title":"DeepSeek - Wikipedia","url":"https://en.wikipedia.org/wiki/DeepSeek"},{"title":"DeepSeek","url":"https://www.deepseek.com/en/"},{"title":"DeepSeek AI training breakthrough in 2026: New method for scaling large language models | by Rysysth Insights | Medium","url":"https://medium.com/@rysysth-insights/deepseek-ai-training-breakthrough-in-2026-new-method-for-scaling-large-language-models-059b87d78104"},{"title":"DeepSeek V3.2 Guide (Updated March 2026): V4, R1/R2, Antigravity Integration | Antigravity.codes","url":"https://antigravity.codes/blog/deepseek-v3-2-guide"},{"title":"DeepSeek Official Models List 2026 (V4, Flash, Pro) | DeepSeek V4 Network","url":"https://deepseekv4.network/models"},{"title":"GitHub - deepseek-ai/DeepSeek-V3 · GitHub","url":"https://github.com/deepseek-ai/deepseek-v3"}]

Based on the search results, here's what I found about DeepSeek R2 and DeepSeek V3 in 2026:

## DeepSeek V3 in 2026

DeepSeek-V3.2 is a general-purpose model optimized for speed and daily tasks. A new version of DeepSeek-V3 (DeepSeek-V3-0324) was released with improvements to post-training methods, incorporating reinforcement learning techniques that significantly enhanced its performance on reasoning tasks.

Additionally, on April 24, 2026, DeepSeek released a preview of its V4 series, including the 1.6-trillion parameter DeepSeek-V4-Pro and the 284-billion parameter DeepSeek-V4-Flash, both featuring a 1-million token context window.

## DeepSeek R2 in 2026

DeepSeek R2 (successor to R1) is a specialized reasoning model designed for deep logic, complex coding, and multilingual reasoning. However, in late February 2026, multiple sources confirmed that DeepSeek was preparing to release two new models: DeepSeek V4 and DeepSeek R2. 

Yet as of March 2026, DeepSeek-R2 is the anticipated successor to R1, but as of March 2026, it has not been officially announced or released.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e0b3935-ddca-46aa-bdfc-396958d9abe1",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "724ff753-d6f1-45ab-a9bb-17cce3195105",
  "sourceToolAssistantUUID": "2e0b3935-ddca-46aa-bdfc-396958d9abe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T14:33:34.329Z_

<details><summary>↩ Tool result · `toolu_01MV1HE5vqsdbostKVTMU9nN`</summary>

```text
Web search results for query: "best open source LLM 2026"

Links: [{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"Open Source LLM Platforms in 2026: Ollama, OpenRouter, Groq, NVIDIA NIM — Which One Should You Use? | by Developer Awam | CodeX | May, 2026 | Medium","url":"https://medium.com/codex/open-source-llm-platforms-in-2026-ollama-openrouter-groq-nvidia-nim-which-one-should-you-use-2f11c7ba60bc"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Best Open Source LLMs in 2026: We Reviewed 7 Models","url":"https://fireworks.ai/blog/best-open-source-llms"}]

Based on the search results, here's an overview of the best open source LLMs in 2026:

## Top Open Source LLMs in 2026

Kimi K2.6 is the strongest open-weight pick in the live ranking with the best overall quality, and Kimi K2.6 Thinking leads with 78.57 Coding Average and 58.33 Agentic Coding Average.

Other leading models include:

- **DeepSeek V4**: DeepSeek-V4 is designed for long-context reasoning, coding, and agentic workflows, with DeepSeek-V4-Pro (1.6T total, 49B active) as the flagship model for maximum reasoning, coding, and agentic performance.

- **GLM-5**: On coding benchmarks, GLM-5 scores 90% on HumanEval and 77.8% on SWE-bench Verified according to Zhipu AI's official reports.

- **MiMo-V2.5**: MiMo-V2.5-Pro (1.02T total, 42B active) is the flagship LLM for coding agents, complex software engineering, and long-horizon tool use.

- **Qwen and Llama**: Models from Google (Gemma 4), Meta (Llama 4), Alibaba (Qwen3), and Microsoft (Phi 4) now match or exceed proprietary models for most practical tasks.

## Key Insight

The best open source LLM doesn't exist. Llama 4 excels at general tasks. Mistral AI optimizes for mobile. DeepSeek maximizes efficiency. Qwen 3 handles multilingual coding. StarCoder focuses on programming. The choice depends on your specific use case and requirements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97b579db-760e-4860-b9ff-2d7fc4fe31a1",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "1eba52a7-9a18-441b-9bcb-1288230cd6cb",
  "sourceToolAssistantUUID": "97b579db-760e-4860-b9ff-2d7fc4fe31a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T14:33:34.792Z_

<details><summary>↩ Tool result · `toolu_01Gbc3UdpXowrxQebmxiZ5o4`</summary>

```text
Web search results for query: "Qwen3 model 2026 specs parameters"

Links: [{"title":"Qwen3.6-Max-Preview: Benchmarks, API & Review (2026)","url":"https://www.buildfastwithai.com/blogs/qwen3-6-max-preview-review-2026"},{"title":"Qwen/Qwen3-Coder-Next · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Coder-Next"},{"title":"Qwen3.5","url":"https://qwen.ai/research"},{"title":"Ultimate Guide - The Best Qwen3 Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-qwen3-models-in-2025"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen/Qwen3.6-35B-A3B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-35B-A3B"},{"title":"Qwen 3.6 Plus Preview: 1M Context, Speed & Benchmarks 2026","url":"https://www.buildfastwithai.com/blogs/qwen-3-6-plus-preview-review"},{"title":"Qwen 3 GPU Requirements — Original Family (0.6B–235B) VRAM Guide (2026) | Will It Run AI Blog","url":"https://willitrunai.com/blog/qwen-3-gpu-requirements"},{"title":"Qwen - Wikipedia","url":"https://en.wikipedia.org/wiki/Qwen"},{"title":"qwen3","url":"https://ollama.com/library/qwen3"}]

Based on the search results, here's an overview of Qwen3 models and their specifications in 2026:

## Qwen3.6 Series (Latest - April 2026)

Qwen3.6-Max-Preview is Alibaba's most capable language model to date — a proprietary, hosted flagship model available via Alibaba Cloud Model Studio and Qwen Studio, released on April 20, 2026. Key specifications include:

- The model supports a 260,000 token context window and is compatible with both OpenAI and Anthropic API specifications
- Qwen3.6-Max-Preview claims the top position on six major coding benchmarks as of its April 20, 2026 release

Qwen3.6-Plus launched three weeks earlier, with a 1,000,000-token (1M) context window, equivalent to approximately 2,000 pages of text.

## Qwen3.6 Open-Weight Models

Qwen3.6-35B-A3B was released under Apache 2.0 on April 16, 2026, scores 73.4% on SWE-bench Verified, and is available via HuggingFace, Ollama, and vLLM. This is a mixture-of-experts model with 3B activated parameters (80B total parameters) in some versions.

## Qwen3 Original Family

The flagship model, Qwen3-235B-A22B, achieves competitive results in benchmark evaluations of coding, math, general capabilities, etc., when compared to other top-tier models such as DeepSeek-R1, o1, o3-mini, Grok-3, and Gemini-2.5-Pro.

Top three picks for 2026 are Qwen3-235B-A22B, Qwen3-30B-A3B, and Qwen3-14B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a38f2fa0-5ca1-47e3-8894-d5b3b067012f",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "ee4c2964-bc1a-41d7-97a9-f470e3243fe5",
  "sourceToolAssistantUUID": "a38f2fa0-5ca1-47e3-8894-d5b3b067012f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T14:33:35.433Z_

<details><summary>↩ Tool result · `toolu_01ABSN4NzTr7Yyi973Q2PvxK`</summary>

```text
Web search results for query: "top open source reasoning model 2026"

Links: [{"title":"Top 10 Open-source Reasoning Models in 2026","url":"https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026"},{"title":"Ultimate Guide - The Best Open Source LLMs for Reasoning in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-reasoning"},{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source LLMs in 2026: Ranked by Coding, Reasoning & Cost | WhatLLM.org","url":"https://whatllm.org/best-open-source-llm"},{"title":"Best Open Source LLMs in 2026: We Reviewed 7 Models","url":"https://fireworks.ai/blog/best-open-source-llms"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Best Open Source Reasoning Model in 2026 - Ertas AI","url":"https://www.ertas.ai/best/best-open-source-reasoning-model"},{"title":"5 Best AI Reasoning Models of 2026: Ranked!","url":"https://www.labellerr.com/blog/compare-reasoning-models/"},{"title":"Top 10 Best AI Reasoning Models in 2026 - TechNow","url":"https://tech-now.io/en/blogs/top-10-best-ai-reasoning-models-in-2026"}]

Based on the search results, here are the top open source reasoning models in 2026:

## Leading Open Source Reasoning Models

The top open-source reasoning models of 2026 include DeepSeek-R1, Qwen3, and Kimi K2.

**Top Recommendations:**

DeepSeek-R1, MiniMax-M1-80k, and Kimi-Dev-72B are the top three recommendations for 2026, each chosen for their exceptional reasoning abilities, innovative architectures, and ability to tackle challenging logical problems.

**By Use Case:**

- **General Reasoning**: For general reasoning tasks, DeepSeek-R1 offers OpenAI-o1 comparable performance
- **Long-Context Reasoning**: MiniMax-M1-80k provides exceptional computational savings for efficiency and long-context reasoning
- **Coding & Software Engineering**: Kimi-Dev-72B delivers state-of-the-art results at the best value for software engineering and coding reasoning

**Overall Performance:**

Benchmarks of 2025 show that specialized reasoning models now rival proprietary systems on math, logic, and tool-using tasks. Kimi K2.6 leads the live open-source ranking with a Quality Index of 53.905.

Additionally, DeepSeek V4 is the strongest open-weight choice for general reasoning workloads in 2026, with unified thinking-mode models like Qwen 3+, DeepSeek V3.2/V4, and Hermes 4 integrating reasoning capability into a standard chat checkpoint being the better operational choice for most production deployments in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2b048d3-2df0-44d6-95a2-258d76214fe7",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "4fa594a5-749a-4898-bfcb-6bed5275ba4d",
  "sourceToolAssistantUUID": "a2b048d3-2df0-44d6-95a2-258d76214fe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T14:33:36.010Z_

<details><summary>↩ Tool result · `toolu_0177AABD7CdCsJinAcb4WoUg`</summary>

```text
Web search results for query: "Llama 4 model 2026 Meta open source LLM"

Links: [{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Industry Leading, Open-Source AI | Llama","url":"https://www.llama.com/"},{"title":"Llama (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Llama_(language_model)"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"GitHub - meta-llama/llama-models: Utilities intended for use with Llama models. · GitHub","url":"https://github.com/meta-llama/llama-models"},{"title":"Open-Source LLM Landscape 2026: DeepSeek V4 vs Llama 4 vs Qwen 3.5 vs Gemma 4","url":"https://codersera.com/blog/open-source-llms-landscape-2026/"},{"title":"Report: Meta developing open-source versions of upcoming AI models - SiliconANGLE","url":"https://siliconangle.com/2026/04/06/report-meta-developing-open-source-versions-upcoming-ai-models/"},{"title":"Llama 4 Variants: How to Pick the Right Open Source Model Without Regret","url":"https://ajianaz.dev/llama-4-variants-how-to-pick-the-right-open-source-model-without-regret/"},{"title":"Best Llama Models in 2026 — Meta's Open-Source AI Dominance | Remote OpenClaw","url":"https://www.remoteopenclaw.com/blog/best-llama-models-2026"},{"title":"llama4","url":"https://ollama.com/library/llama4"}]

Based on the web search results, here's what I found about Llama 4 and Meta's open-source LLM:

## Llama 4 Overview

Llama 4 Scout and Llama 4 Maverick are the first open-weight natively multimodal models with unprecedented context length support and the first built using a mixture-of-experts (MoE) architecture.

## Model Variants

Llama 4 Scout is a 17 billion active parameter model with 16 experts, and Llama 4 Maverick is a 17 billion active parameter model with 128 experts. Llama 4 Maverick contains 17 billion active parameters, 128 experts, and 400 billion total parameters, offering high quality at a lower price compared to Llama 3.3 70B.

## Key Features

Llama 4 models are designed with native multimodality, incorporating early fusion to seamlessly integrate text and vision tokens into a unified model backbone. Meta's Llama 4 brought a 10M-token context window into the open.

## Performance

Llama 4 Behemoth outperforms GPT-4.5, Claude Sonnet 3.7, and Gemini 2.0 Pro on several STEM benchmarks. However, Llama 4 Behemoth is still training, and the company continues to share more details about it while it's still in development.

## Availability

Llama 4 is Meta's first model family to use a Mixture-of-Experts architecture, and as of April 2026, it is the most widely deployed open-weight AI model ecosystem in the world.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "558d8180-252c-4d39-a2e2-4413250743c7",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "e637a198-d8a3-494b-a88e-e42c5bc5c4e6",
  "sourceToolAssistantUUID": "558d8180-252c-4d39-a2e2-4413250743c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T14:33:36.742Z_

<details><summary>↩ Tool result · `toolu_01FkK8nhcm3mUQGfz5vDCoe3`</summary>

```text
Web search results for query: "best open source model for reasoning 2026 benchmark"

Links: [{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Ultimate Guide - The Best Open Source LLMs for Reasoning in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-reasoning"},{"title":"Top 10 Open-source Reasoning Models in 2026","url":"https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source LLMs in 2026: Ranked by Coding, Reasoning & Cost | WhatLLM.org","url":"https://whatllm.org/best-open-source-llm"},{"title":"Comparison of Open Source AI Models across Intelligence, Performance, Price, Context Window, and more | Artificial Analysis","url":"https://artificialanalysis.ai/models/open-source"},{"title":"Best Open Source LLMs in 2026: We Reviewed 7 Models","url":"https://fireworks.ai/blog/best-open-source-llms"},{"title":"Open Source LLM Leaderboard 2026: Rankings, Benchmarks & the Best Models Right Now &#045; VERTU® Official Site","url":"https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"}]

Based on the search results, here are the best open-source models for reasoning according to 2026 benchmarks:

## Top Reasoning Models

The top three picks for 2026 are DeepSeek-R1, MiniMax-M1-80k, and Kimi-Dev-72B.

### DeepSeek-R1
DeepSeek-R1 achieves performance comparable to OpenAI-o1 across math, code, and reasoning tasks. With 671B parameters using MoE architecture and 164K context length, it represents the pinnacle of open-source reasoning capabilities.

### MiniMax-M1
MiniMax-M1 is an open-weight, large-scale hybrid-attention reasoning model with 456 B parameters and 45.9 B activated per token. It natively supports 1 M-token context, lightning attention enabling 75% FLOPs savings vs DeepSeek R1 at 100 K tokens, and leverages a MoE architecture.

### Other Frontier Models

S-tier models like GLM-4.7, Kimi K2.5, and MiniMax M2.5 are matching or exceeding proprietary model performance on specific benchmarks. Kimi K2.5 posts remarkable benchmark numbers with a HumanEval score of 99.0 (the highest of any model tracked), leads in MMLU (92.0), IFEval (94.0), MATH-500 (98.0), and GPQA Diamond (87.6), while maintaining a Chatbot Arena rating of 1447.

DeepSeek-V4-Pro is one of the strongest open-source models for reasoning-heavy and coding-heavy workloads, showing competitive results across major reasoning and agentic benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56ab497a-1051-44d9-b83a-7fb95a088fca",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "0d31d16a-7ef4-4bb2-81ef-f45ba1b2b9f3",
  "sourceToolAssistantUUID": "56ab497a-1051-44d9-b83a-7fb95a088fca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-14T14:33:41.106Z_

Let me get a few more targeted searches for the specific parameter ranges you care about (7B-72B) and for RL training suitability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d31d16a-7ef4-4bb2-81ef-f45ba1b2b9f3",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dFoUZgP8jspceiSzBZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c681c2a-de8c-4786-8e04-c1ef749ca7d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V99xT8Y3ZGzcBeQXJbCjJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7062,
      "cache_read_input_tokens": 10412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7062,
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

_source line 22 · 2026-05-14T14:33:41.955Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CXc8Bdnk4PzxQWEbbrQR96`</summary>

```json
{
  "query": "Qwen3-30B-A3B Qwen3-14B reasoning benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c681c2a-de8c-4786-8e04-c1ef749ca7d1",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dFoUZgP8jspceiSzBZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aceef624-9e38-4b72-bc14-6eb84f211a72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V99xT8Y3ZGzcBeQXJbCjJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7062,
      "cache_read_input_tokens": 10412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7062,
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

_source line 23 · 2026-05-14T14:33:42.434Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015J3vW9wcCnCFA7x9KjLgUJ`</summary>

```json
{
  "query": "DeepSeek-R1 distilled 7B 14B 32B 70B reasoning benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aceef624-9e38-4b72-bc14-6eb84f211a72",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dFoUZgP8jspceiSzBZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dad33482-8653-40a7-9ff9-8260ec78f506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V99xT8Y3ZGzcBeQXJbCjJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7062,
      "cache_read_input_tokens": 10412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7062,
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

_source line 24 · 2026-05-14T14:33:42.840Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UVec2AbcE8QNCYYf2HHgZV`</summary>

```json
{
  "query": "Kimi-Dev-72B benchmark specs parameters 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dad33482-8653-40a7-9ff9-8260ec78f506",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dFoUZgP8jspceiSzBZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4705fcc3-5002-4161-850d-f769f8a1fc46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V99xT8Y3ZGzcBeQXJbCjJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7062,
      "cache_read_input_tokens": 10412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7062,
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

_source line 25 · 2026-05-14T14:33:49.770Z_

<details><summary>↩ Tool result · `toolu_015J3vW9wcCnCFA7x9KjLgUJ`</summary>

```text
Web search results for query: "DeepSeek-R1 distilled 7B 14B 32B 70B reasoning benchmark 2026"

Links: [{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/deepseek-r1"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"DeepSeek-R1: The Open-Source Reasoning Model","url":"https://www.sitepoint.com/deepseek-r1-open-source-reasoning/"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-14B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"},{"title":"Run DeepSeek R1 Locally — Setup Guide & GPU Needs 2026 | Compute Market","url":"https://www.compute-market.com/blog/deepseek-r1-local-setup-guide-2026"},{"title":"DeepSeek R1 Guide: Architecture, Benchmarks, and Practical Usage in 2026 - DEV Community","url":"https://dev.to/lemondata_dev/deepseek-r1-guide-architecture-benchmarks-and-practical-usage-in-2026-m8f"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-32B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"},{"title":"DeepSeek V4 Review 2026: Open-Source Coding AI vs GitHub Copilot","url":"https://computertech.co/deepseek-v4-review/"},{"title":"Running DeepSeek R1 Locally: Your Complete Setup Guide (2026)","url":"https://www.sitepoint.com/running-deepseek-r1-locally-your-complete-setup-guide-2026/"}]

Based on the search results, here's what I found about DeepSeek-R1 distilled models and their reasoning benchmarks:

## DeepSeek-R1 Distilled Variants

DeepSeek has open-sourced distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series.

## Model Architecture

The 1.5B, 7B, 14B and 32B models are derived from Qwen-2.5 series and finetuned with 800k samples curated with DeepSeek-R1, while the 70B model is derived from Llama3.3-70B-Instruct.

## Reasoning Benchmark Performance

The evaluation results demonstrate that the distilled smaller dense models perform exceptionally well on benchmarks. Specifically:

- DeepSeek-R1-Distill-Qwen-32B outperforms OpenAI-o1-mini across various benchmarks, achieving new state-of-the-art results for dense models

- The 32B distill scored 79.8% on MATH-500

- The 32B distill scored 72.6% on LiveCodeBench

DeepSeek-R1 achieves performance comparable to OpenAI-o1 across math, code, and reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dad33482-8653-40a7-9ff9-8260ec78f506",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "9694b63d-cb6f-4a82-82a9-90e67970e21b",
  "sourceToolAssistantUUID": "dad33482-8653-40a7-9ff9-8260ec78f506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T14:33:49.899Z_

<details><summary>↩ Tool result · `toolu_01UVec2AbcE8QNCYYf2HHgZV`</summary>

```text
Web search results for query: "Kimi-Dev-72B benchmark specs parameters 2026"

Links: [{"title":"Kimi-Dev-72B - Model Info, Parameters, Benchmarks - SiliconFlow\"","url":"https://www.siliconflow.com/models/kimi-dev-72b"},{"title":"Kimi-Dev-72B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/kimi-dev-72b"},{"title":"GitHub - MoonshotAI/Kimi-Dev: open-source coding LLM for software engineering tasks · GitHub","url":"https://github.com/MoonshotAI/Kimi-Dev"},{"title":"moonshotai/Kimi-Dev-72B · Hugging Face","url":"https://huggingface.co/moonshotai/Kimi-Dev-72B"},{"title":"Kimi Dev 72B - API, Specs, Playground & Pricing - Puter Developer","url":"https://developer.puter.com/ai/moonshotai/kimi-dev-72b/"},{"title":"ubergarm/Kimi-Dev-72B-GGUF · Hugging Face","url":"https://huggingface.co/ubergarm/Kimi-Dev-72B-GGUF"},{"title":"Kimi-Dev-72B","url":"https://moonshotai.github.io/Kimi-Dev/"},{"title":"Kimmy K2.6 and Qwen 3.6: The Open-Source Models Closing the Frontier Gap | MindStudio","url":"https://www.mindstudio.ai/blog/kimmy-k2-6-qwen-3-6-open-source-frontier-models"},{"title":"MoonshotAI: Kimi Dev 72B Free Chat Online - Skywork ai","url":"https://skywork.ai/blog/models/moonshotai-kimi-dev-72b-free-chat-online/"},{"title":"Kimi Dev 72B - API Pricing & Providers | OpenRouter","url":"https://openrouter.ai/moonshotai/kimi-dev-72b"}]

Based on the search results, here are the key specifications and benchmark details for Kimi-Dev-72B:

## Model Specifications

Kimi-Dev-72B has a dense 72-billion-parameter architecture with a 131,072-token context window. More specifically:

- The model uses Qwen2 Transformer architecture with FP8 precision and a context length of 131K tokens
- It was built upon the Qwen2.5-72B foundational architecture
- The model underwent a large-scale mid-training phase using approximately 150 billion tokens of high-quality data from GitHub issues and pull request commits

## Benchmark Performance

Kimi-Dev-72B achieves 60.4% performance on SWE-bench Verified, surpassing the runner-up and setting a new state-of-the-art result among open-source models.

## Key Features

The model's core innovation lies in its duo-stage framework, comprising specialized "BugFixer" and "TestWriter" behaviors. Kimi-Dev-72B is a 72-billion-parameter coding model by Moonshot AI, purpose-built for software engineering tasks like bug fixing, code generation, and unit test creation.

The model was released in May/June 2025 and is available as an open-source project under the MIT license.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4705fcc3-5002-4161-850d-f769f8a1fc46",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "443114ac-46cd-4ecf-8848-d758b3c9841e",
  "sourceToolAssistantUUID": "4705fcc3-5002-4161-850d-f769f8a1fc46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T14:33:50.557Z_

<details><summary>↩ Tool result · `toolu_01CXc8Bdnk4PzxQWEbbrQR96`</summary>

```text
Web search results for query: "Qwen3-30B-A3B Qwen3-14B reasoning benchmark 2026"

Links: [{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Ultimate Guide - The Best Qwen3 Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-qwen3-models-in-2025"},{"title":"Qwen/Qwen3.6-35B-A3B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-35B-A3B"},{"title":"Qwen/Qwen3-30B-A3B-Thinking-2507 · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507"},{"title":"Speed Benchmark - Qwen","url":"https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen/Qwen3.5-35B-A3B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-35B-A3B"},{"title":"Qwen 3 Benchmarks, Comparisons, Model Specifications, and More - DEV Community","url":"https://dev.to/best_codes/qwen-3-benchmarks-comparisons-model-specifications-and-more-4hoa"},{"title":"Qwen: Qwen3 30B A3B Review | Pricing, Benchmarks & Capabilities (2026) | Design for Online","url":"https://designforonline.com/ai-models/qwen-qwen3-30b-a3b/"},{"title":"Qwen3 14B vs Qwen3 Coder 30B A3B Instruct (Comparative Analysis) | Galaxy.ai","url":"https://blog.galaxy.ai/compare/qwen3-14b-vs-qwen3-coder-30b-a3b-instruct"}]

Based on the web search results, here's what I found about Qwen3-30B-A3B and Qwen3-14B reasoning benchmarks:

## Model Architecture and Parameters

Qwen3-30B-A3B is a smaller MoE model with 30 billion total parameters and 3 billion activated parameters, while Qwen3-14B is a dense model that was open-weighted under Apache 2.0 license.

## Reasoning Performance Comparison

Qwen3-30B-A3B provides excellent reasoning with efficient resource usage, while Qwen3-14B delivers strong reasoning performance in a compact form factor. The search results reference Table 15 which provides comparison among Qwen3-30B-A3B / Qwen3-14B (Thinking) and other reasoning baselines, though the specific benchmark scores from that table were not included in the search results.

## Dual-Mode Reasoning

Both models support seamless switching between thinking mode (for complex logical reasoning, math, and coding) and non-thinking mode (for efficient, general-purpose dialogue).

For more detailed benchmark comparisons and specific performance metrics, you may want to consult the full Qwen3 Technical Report or the official benchmark tables mentioned in the documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aceef624-9e38-4b72-bc14-6eb84f211a72",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "aaae29ef0dc1bbe1e",
  "type": "user",
  "uuid": "8f46db0c-a7fc-4ecf-93db-03c260102f42",
  "sourceToolAssistantUUID": "aceef624-9e38-4b72-bc14-6eb84f211a72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-14T14:34:35.156Z_

Here is my consolidated report on the current frontier of open-source language models for reasoning research as of May 2026.

---

## Top Open-Source Models for Reasoning Research (May 2026)

### 1. Qwen3 Series (Alibaba) -- Best Range of Research-Friendly Sizes

The Qwen3 family offers the widest range of sizes practical for RL-based reasoning research:

- **Qwen3-14B** (dense, 14B params): Strong reasoning in a compact form factor. Supports dual-mode operation (thinking/non-thinking). Apache 2.0 license. A very practical choice for single-GPU RL training experiments.
- **Qwen3-30B-A3B** (MoE, 30B total / 3B active): Excellent reasoning at extremely efficient inference cost. The low active parameter count makes it feasible for RL training with limited compute, while the MoE architecture provides capacity.
- **Qwen3-235B-A22B** (MoE, 235B total / 22B active): The flagship; competitive with DeepSeek-R1, o1, o3-mini, and Gemini-2.5-Pro on reasoning benchmarks. Too large for most research RL setups, but useful as a reference/teacher model.

The Qwen3 line has since been followed by Qwen3.5 and Qwen3.6 releases (with Qwen3.6-35B-A3B scoring 73.4% on SWE-bench Verified), but the Qwen3 base models remain the most well-studied for RL fine-tuning.

### 2. DeepSeek-R1 Distilled Models (DeepSeek) -- Proven RL-Trained Reasoning Models

DeepSeek-R1 was the breakthrough that demonstrated pure RL can produce strong reasoning in open-source models. The distilled checkpoints are the most directly relevant for your work:

- **DeepSeek-R1-Distill-Qwen-7B** (7B, dense): Smallest practical reasoning distill. Good starting point for RL experiments with limited compute.
- **DeepSeek-R1-Distill-Qwen-14B** (14B, dense): Sweet spot of capability vs. trainability.
- **DeepSeek-R1-Distill-Qwen-32B** (32B, dense): Outperforms OpenAI o1-mini on multiple benchmarks. Scored 79.8% on MATH-500 and 72.6% on LiveCodeBench. State-of-the-art for dense models in this size class.
- **DeepSeek-R1-Distill-Llama-70B** (70B, dense, based on Llama 3.3 70B): Top of the distill line, strong across math/code/reasoning.

These models were trained with 800K curated reasoning samples and are explicitly designed as starting points for further RL training. The full DeepSeek-R1 (671B MoE, 164K context) and the newer DeepSeek-V4-Pro (1.6T total, 49B active) are the reference frontier but too large for research RL.

### 3. Kimi-Dev-72B (Moonshot AI) -- Best Open-Source Coding/SE Reasoning

- **72B dense parameters**, 131K context window, built on Qwen2.5-72B architecture
- **60.4% on SWE-bench Verified** -- state-of-the-art among open-source models for software engineering
- Trained with 150B tokens of GitHub issues/PR data; MIT licensed
- Duo-stage framework (BugFixer + TestWriter) makes it uniquely suited for agentic coding and retrieval-augmented SE reasoning

At 72B dense parameters, this sits at the upper edge of your feasibility range but is the strongest open model specifically for code reasoning tasks.

### 4. MiniMax-M1-80K (MiniMax) -- Best for Long-Context Reasoning

- **456B total params / 45.9B active** (MoE), natively supports 1M-token context
- Uses lightning attention, achieving 75% FLOPs savings vs. DeepSeek-R1 at 100K tokens
- Strong on reasoning benchmarks; the efficient architecture makes it more practical than its total parameter count suggests

Relevant if your retrieval-augmented reasoning research involves very long contexts, though the total parameter count makes full RL training challenging.

### 5. Llama 4 Maverick (Meta) -- Best Multimodal + Reasoning Baseline

- **17B active params / 400B total** (MoE, 128 experts), 10M-token context window
- Natively multimodal (text + vision early fusion)
- Outperforms Llama 3.3 70B at lower inference cost
- Meta's community license (most permissive of the large-company models)

The 17B active parameter count is very research-friendly, though the 400B total model weight may require significant memory for RL training. The MoE architecture with many experts is architecturally interesting for reasoning research.

---

## Recommendation for RL Training on Reasoning Tasks

Given your 7B-72B constraint and focus on retrieval-augmented reasoning, my ranked recommendations:

| Priority | Model | Params | Why |
|----------|-------|--------|-----|
| 1 | **DeepSeek-R1-Distill-Qwen-32B** | 32B dense | Already RL-trained for reasoning; proven MATH/code benchmarks; manageable for RL on 4-8 GPUs |
| 2 | **Qwen3-14B** | 14B dense | Excellent reasoning base; dual-mode thinking; Apache 2.0; very trainable on 2-4 GPUs |
| 3 | **Qwen3-30B-A3B** | 30B total / 3B active | MoE efficiency makes RL feasible; strong reasoning despite low active params |
| 4 | **DeepSeek-R1-Distill-Qwen-14B** | 14B dense | Smaller reasoning distill; fastest iteration cycle for RL experiments |
| 5 | **Kimi-Dev-72B** | 72B dense | Best if your RAG research targets code/SE tasks specifically; needs 4+ A100s for RL |

The DeepSeek-R1-Distill-Qwen-32B is likely your best starting point -- it is already trained with RL for reasoning, has excellent benchmark results, and at 32B dense parameters is feasible for RL fine-tuning on a modest multi-GPU setup.

---

Sources:
- [Top 10 Open-source Reasoning Models in 2026 (Clarifai)](https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026)
- [Best Open Source LLMs for Reasoning in 2026 (SiliconFlow)](https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-reasoning)
- [Best Open Source LLM Leaderboard 2026 (Onyx)](https://onyx.app/open-llm-leaderboard)
- [The Best Open-Source LLMs in 2026 (BentoML)](https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models)
- [Best Qwen3 Models in 2026 (SiliconFlow)](https://www.siliconflow.com/articles/en/the-best-qwen3-models-in-2025)
- [Qwen3.6-35B-A3B (Hugging Face)](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- [DeepSeek R1 Guide: Architecture, Benchmarks, and Practical Usage in 2026](https://dev.to/lemondata_dev/deepseek-r1-guide-architecture-benchmarks-and-practical-usage-in-2026-m8f)
- [DeepSeek-R1 (Hugging Face)](https://huggingface.co/deepseek-ai/DeepSeek-R1)
- [DeepSeek V4 and R2 Deep Dive (Meta Intelligence)](https://www.meta-intelligence.tech/en/insight-deepseek-v4-r2)
- [Kimi-Dev-72B (SiliconFlow)](https://www.siliconflow.com/models/kimi-dev-72b)
- [Kimi-Dev-72B (Hugging Face)](https://huggingface.co/moonshotai/Kimi-Dev-72B)
- [Llama 4 Herd (Meta AI)](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [Open-Source LLM Landscape 2026: DeepSeek V4 vs Llama 4 vs Qwen 3.5 vs Gemma 4](https://codersera.com/blog/open-source-llms-landscape-2026/)
- [Open LLM Leaderboard 2026 (Vellum)](https://www.vellum.ai/open-llm-leaderboard)
- [GLM-5: New SOTA Open Weights LLM (Latent Space)](https://www.latent.space/p/ainews-zai-glm-5-new-sota-open-weights)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f46db0c-a7fc-4ecf-93db-03c260102f42",
  "isSidechain": true,
  "agentId": "aaae29ef0dc1bbe1e",
  "requestId": "req_011Cb2dGpZ5Y5Dr4qAasXK1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28e9aba3-17d2-4fde-acc9-526c31a320b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qchc7Hdh1EG7n92kFSfoxq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1882,
      "cache_creation_input_tokens": 1150,
      "cache_read_input_tokens": 17474,
      "output_tokens": 2343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1150
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1882,
          "output_tokens": 2343,
          "cache_read_input_tokens": 17474,
          "cache_creation_input_tokens": 1150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1150,
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
