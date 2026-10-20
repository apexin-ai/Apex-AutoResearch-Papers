# Research conversation: Use WebSearch to find the current best open-source large language models as of mid-2026. I need to know what models woul

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 2
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a773a7bcb28c1b47d.jsonl`
- **Structured JSON:** [`1b7d064b9d91fdb5c9e6.json`](../../sessions/1b/1b7d064b9d91fdb5c9e6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-15T13:20:50.947Z_

Use WebSearch to find the current best open-source large language models as of mid-2026. I need to know what models would be appropriate for safety fine-tuning research. Search for:

1. "best open source LLM 2026"
2. "top open source language model 2026 leaderboard"
3. "Llama 4 release 2026" or latest Meta LLM
4. "Qwen 3 model 2026" or latest Alibaba LLM
5. "Mistral latest model 2026"
6. "open source LLM SOTA 2026"
7. "huggingface open LLM leaderboard 2026"

Report: model name, parameter sizes available, release date, and whether it's a good candidate for safety fine-tuning research (i.e., has safety training already applied, open weights, reasonable size for academic compute). I specifically need to know if Llama-3 is still frontier or if newer models have superseded it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "f88718c0-e7ef-4527-bae3-5be2d4dd76f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T13:20:50.950Z_

```json
{
  "parentUuid": "f88718c0-e7ef-4527-bae3-5be2d4dd76f8",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
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
  "uuid": "2c0d056c-a088-4bbf-8f57-876416a525fb",
  "timestamp": "2026-05-15T13:20:50.950Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T13:20:53.799Z_



I'll search for all of these queries in parallel to gather comprehensive information about the current state of open-source LLMs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c0d056c-a088-4bbf-8f57-876416a525fb",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RWtzEW4HUB3iJjbVgG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4357a81-b71c-4753-97dc-4dd28d4b250c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013QYai3yj2Rjg8otr33gZ2H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 757,
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

_source line 4 · 2026-05-15T13:20:54.091Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JDTthDSL2KjzFuB5YTxoXL`</summary>

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
  "parentUuid": "c4357a81-b71c-4753-97dc-4dd28d4b250c",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RWtzEW4HUB3iJjbVgG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "791a3edb-8a17-4bd5-99de-5f2c6e0f1081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013QYai3yj2Rjg8otr33gZ2H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 7304,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 757
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 757,
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

_source line 5 · 2026-05-15T13:20:54.093Z_

<details><summary>↩ Tool result · `toolu_01JDTthDSL2KjzFuB5YTxoXL`</summary>

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
  "parentUuid": "791a3edb-8a17-4bd5-99de-5f2c6e0f1081",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "ade922f3-628f-47ac-9040-9fc5a208ce7b",
  "sourceToolAssistantUUID": "791a3edb-8a17-4bd5-99de-5f2c6e0f1081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T13:20:57.304Z_



Now let me run all 7 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ade922f3-628f-47ac-9040-9fc5a208ce7b",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RX8eGQ2YA6PuSrYZQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89b58c3d-d22f-449b-b286-d1cc8eac6a6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UhuwSEnb33nsn1TuPBWJU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8061,
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

_source line 7 · 2026-05-15T13:20:57.843Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VXjxzWq5EepKgBeX5GeLty`</summary>

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
  "parentUuid": "89b58c3d-d22f-449b-b286-d1cc8eac6a6b",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RX8eGQ2YA6PuSrYZQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7772c20-8109-41d8-82df-3505f52e8705",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UhuwSEnb33nsn1TuPBWJU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8061,
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

_source line 8 · 2026-05-15T13:20:58.316Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G9MEUPPJGwVz8UUWd56PcQ`</summary>

```json
{
  "query": "top open source language model 2026 leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7772c20-8109-41d8-82df-3505f52e8705",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RX8eGQ2YA6PuSrYZQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1382138-2eb6-472b-aaf0-d0e1e0feb35b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UhuwSEnb33nsn1TuPBWJU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8061,
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

_source line 9 · 2026-05-15T13:20:59.296Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CqFN2ie36QYeMqiRJrcX7q`</summary>

```json
{
  "query": "Llama 4 release 2026 Meta latest LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1382138-2eb6-472b-aaf0-d0e1e0feb35b",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RX8eGQ2YA6PuSrYZQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8fa7d09-9de1-4652-9f6a-64e1fcd7d35a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UhuwSEnb33nsn1TuPBWJU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8061,
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

_source line 10 · 2026-05-15T13:20:59.727Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hi86PdQfMdwg3zXmZmDsqS`</summary>

```json
{
  "query": "Qwen 3 model 2026 Alibaba latest LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8fa7d09-9de1-4652-9f6a-64e1fcd7d35a",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RX8eGQ2YA6PuSrYZQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8d63b3e-43f7-4163-b047-6b5278f79662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UhuwSEnb33nsn1TuPBWJU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8061,
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

_source line 11 · 2026-05-15T13:21:00.199Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E2KM3WMdE683JsvwHXnB42`</summary>

```json
{
  "query": "Mistral latest model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8d63b3e-43f7-4163-b047-6b5278f79662",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RX8eGQ2YA6PuSrYZQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b22fea12-06eb-45f6-977b-b60e85e70fbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UhuwSEnb33nsn1TuPBWJU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8061,
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

_source line 12 · 2026-05-15T13:21:00.672Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FRarPZF5u4gKfvPbreT2DB`</summary>

```json
{
  "query": "open source LLM SOTA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b22fea12-06eb-45f6-977b-b60e85e70fbd",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RX8eGQ2YA6PuSrYZQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eab162e7-b932-46eb-bd64-152119cd8f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UhuwSEnb33nsn1TuPBWJU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8061,
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

_source line 13 · 2026-05-15T13:21:01.017Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E25SREfL4ZeGxNwBFu2WEt`</summary>

```json
{
  "query": "huggingface open LLM leaderboard 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eab162e7-b932-46eb-bd64-152119cd8f17",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RX8eGQ2YA6PuSrYZQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67b1c012-ebd1-4c99-b93c-2626f0305ee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UhuwSEnb33nsn1TuPBWJU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8061,
      "output_tokens": 356,
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
          "output_tokens": 356,
          "cache_read_input_tokens": 8061,
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

_source line 14 · 2026-05-15T13:21:04.437Z_

<details><summary>↩ Tool result · `toolu_01VXjxzWq5EepKgBeX5GeLty`</summary>

```text
Web search results for query: "best open source LLM 2026"

Links: [{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"11 Top Open-Source LLMs for 2026 and Their Uses | DataCamp","url":"https://www.datacamp.com/blog/top-open-source-llms"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"Open Source LLM Platforms in 2026: Ollama, OpenRouter, Groq, NVIDIA NIM — Which One Should You Use? | by Developer Awam | CodeX | May, 2026 | Medium","url":"https://medium.com/codex/open-source-llm-platforms-in-2026-ollama-openrouter-groq-nvidia-nim-which-one-should-you-use-2f11c7ba60bc"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Best Open-Source LLMs in 2026 - Ranked | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"}]

Based on the search results, here are the best open-source LLMs in 2026:

## Top Overall Models

GLM 5.1 is a 744B-parameter MoE with a 200K token context, positioned as a flagship release for coding, reasoning, and agentic workflows — currently the leading open-weights model on Artificial Analysis's Intelligence Index.

Qwen 3 235B-A22B currently leads on the broadest range of benchmarks, combining top-tier reasoning, coding, and multilingual capabilities under an Apache 2.0 license.

## Specialized Leaders

**For Coding:** Kimi K2.6 Thinking is the strongest open-source entry across both key coding metrics on May 12, 2026: 78.57 Coding Avg and 58.33 Agentic Coding Avg.

**For Long Context:** Meta's Llama 4 Scout brought a 10 million token context window. You can feed it an entire codebase, a shelf of research papers, or 20 hours of video transcription in a single prompt.

**For Reasoning:** DeepSeek came to the spotlight in early 2025, when R1 demonstrated ChatGPT-level reasoning at significantly lower training costs. The latest release DeepSeek-V4 is designed for long-context reasoning, coding, and agentic workflows, with two large MoE models.

## Performance Comparison

On coding and math benchmarks, the best open-source models match or beat GPT-4.5 and approach Claude Sonnet 4.5 performance. The gap is narrowest in structured tasks (code, math, reasoning) and widest in creative writing and nuanced instruction following.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7772c20-8109-41d8-82df-3505f52e8705",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "92d50c77-542e-4370-807f-a78c95ad1c45",
  "sourceToolAssistantUUID": "c7772c20-8109-41d8-82df-3505f52e8705",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T13:21:06.216Z_

<details><summary>↩ Tool result · `toolu_01CqFN2ie36QYeMqiRJrcX7q`</summary>

```text
Web search results for query: "Llama 4 release 2026 Meta latest LLM"

Links: [{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Llama (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Llama_(language_model)"},{"title":"Best Llama Models in 2026 — Meta's Open-Source AI Dominance | Remote OpenClaw","url":"https://www.remoteopenclaw.com/blog/best-llama-models-2026"},{"title":"AI Updates Today (May 2026) – Latest AI Model Releases","url":"https://llm-stats.com/llm-updates"},{"title":"Meta is back in the LLM game after a year-long break","url":"https://www.understandingai.org/p/meta-is-back-in-the-llm-game-after"},{"title":"Industry Leading, Open-Source AI | Llama","url":"https://www.llama.com/"},{"title":"Meta AI All Models Available: Llama‑4, Llama‑3, and Deployment Options","url":"https://www.datastudios.org/post/meta-ai-all-models-available-llama-4-llama-3-and-deployment-options"},{"title":"Goodbye, Llama? Meta launches new proprietary AI model Muse Spark — first since Superintelligence Labs' formation | VentureBeat","url":"https://venturebeat.com/technology/goodbye-llama-meta-launches-new-proprietary-ai-model-muse-spark-first-since"},{"title":"April 2026 AI Models: Every Major Release Reviewed | by Sanjeev Patel | Apr, 2026 | Medium","url":"https://medium.com/@sanjeevpatel3007/april-2026-ai-models-every-major-release-reviewed-6ea03d7bc0b7"},{"title":"Llama 4 Complete Developer Guide (2026): Variants, Benchmarks, License, Hosting","url":"https://codersera.com/blog/llama-4-complete-guide-2026/"}]

Based on the search results, here's what I found about Llama 4 and Meta's latest LLM developments in 2026:

## Llama 4 Release

Llama 4 was released in April 2025, making it Meta's current generation LLM as of 2026. The release introduced Llama 4 Scout and Llama 4 Maverick, the first open-weight natively multimodal models with unprecedented context length support and the first built using a mixture-of-experts (MoE) architecture.

### Key Llama 4 Models

Llama 4 Scout is a 17 billion active parameter model with 16 experts, and Llama 4 Maverick is a 17 billion active parameter model with 128 experts. Llama 4 Scout offers a 10M token context window — the largest of any open-weight model as of April 2026.

These models are the best yet thanks to distillation from Llama 4 Behemoth, a 288 billion active parameter model with 16 experts. However, Llama 4 Behemoth, Meta's largest model, was still in training at last public update and has not been released as of April 2026.

## Meta's Newest Model: Muse Spark (April 2026)

More recently, on April 8, Meta Superintelligence Labs launched Muse Spark — Meta's first proprietary, closed-weight AI model. This marks a significant shift in Meta's strategy, as while the Llama series was famously accessible to developers, Muse Spark is launching as a proprietary model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8fa7d09-9de1-4652-9f6a-64e1fcd7d35a",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "f2d52ab5-c221-448b-834d-6f47121f283f",
  "sourceToolAssistantUUID": "b8fa7d09-9de1-4652-9f6a-64e1fcd7d35a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:21:06.730Z_

<details><summary>↩ Tool result · `toolu_01G9MEUPPJGwVz8UUWd56PcQ`</summary>

```text
Web search results for query: "top open source language model 2026 leaderboard"

Links: [{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Best Open Source LLMs in 2026: Ranked by Coding, Reasoning & Cost | WhatLLM.org","url":"https://whatllm.org/best-open-source-llm"},{"title":"Open Source LLM Leaderboard 2026: Rankings, Benchmarks & the Best Models Right Now &#045; VERTU® Official Site","url":"https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Open Source LLM Leaderboard 2026: Rankings, Benchmarks & the Best Models Right Now - VERTU® Official Site","url":"https://legacy.vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now/"},{"title":"Best Open Source LLMs in 2026","url":"https://onyx.app/insights/best-open-source-llms-2026"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"}]

Based on the search results, here's what the 2026 open source language model leaderboards show:

## Top Performing Models

S-tier models like GLM-4.7, Kimi K2.5, and MiniMax M2.5 are matching or exceeding proprietary model performance on specific benchmarks.

### Top Individual Models:

**Kimi K2.5**: Kimi K2.5 posts some of the most remarkable benchmark numbers on the entire leaderboard. Its HumanEval score of 99.0 is the highest of any model tracked — essentially near-perfect on standard coding evaluation. It also leads in MMLU (92.0), IFEval (94.0), MATH-500 (98.0), and GPQA Diamond (87.6), while maintaining a Chatbot Arena rating of 1447.

**GLM-5**: GLM-5 is Zhipu AI's larger successor to GLM-4.7, and it currently holds the highest Chatbot Arena rating on the leaderboard at 1451 — making it the top-ranked model by human preference.

**GLM-4.7**: With a 200K context window and strong instruction-following (IFEval: 88.0), GLM-4.7 is arguably the most well-rounded open-source model available as of early 2026.

**MiniMax M2.5**: MiniMax M2.5 earns its S-tier placement primarily on the strength of its SWE-bench Verified score of 80.2 — the highest of any model on the leaderboard for real-world software engineering tasks.

## Leaderboard Tiers

The leaderboard organizes open-source models into four tiers — S, A, B, and C/D — based on aggregate performance across reasoning, coding, math, chat, and instruction following benchmarks.

## Market Maturity

With over a dozen frontier-class models now publicly available, the gap between open-source and proprietary AI has narrowed to near parity in many domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1382138-2eb6-472b-aaf0-d0e1e0feb35b",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "e80b3d3b-7162-4766-8473-a0d1a9fea636",
  "sourceToolAssistantUUID": "c1382138-2eb6-472b-aaf0-d0e1e0feb35b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T13:21:07.274Z_

<details><summary>↩ Tool result · `toolu_01Hi86PdQfMdwg3zXmZmDsqS`</summary>

```text
Web search results for query: "Qwen 3 model 2026 Alibaba latest LLM"

Links: [{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen 3 Release Date: AI Performance Analysis and Model Timeline - H3sync","url":"https://h3sync.com/blog/qwen-3-release-date/"},{"title":"Qwen - Wikipedia","url":"https://en.wikipedia.org/wiki/Qwen"},{"title":"Qwen 3.6 Series: Alibaba's Open-Source LLM Revolution in 2026 — AI/ML API Blog","url":"https://aimlapi.com/blog/qwen-3-6-series-alibabas-open-source-llm-revolution-in-2026"},{"title":"Supported Models and Capabilities Overview - Model Studio - Alibaba Cloud - Alibaba Cloud Model Studio - Alibaba Cloud Documentation Center","url":"https://www.alibabacloud.com/help/en/model-studio/models"},{"title":"Qwen Studio","url":"https://qwen.ai/"},{"title":"Qwen","url":"https://qwenlm.github.io/"},{"title":"All Qwen Models by Alibaba (2026) | LM Market Cap","url":"https://lmmarketcap.com/qwen-models"},{"title":"Alibaba's Qwen launches new flagship LLM with Qwen 3.6-Plus | Constellation Research","url":"https://www.constellationr.com/insights/news/alibabas-qwen-launches-new-flagship-llm-qwen-36-plus"},{"title":"Qwen - Alibaba Cloud","url":"https://www.alibabacloud.com/en/solutions/generative-ai/qwen?_p_lc=1"}]

Based on the search results, here's what's currently happening with Alibaba's latest Qwen models in 2026:

## Recent Qwen Releases in 2026

On February 16, 2026, Qwen3.5 and Qwen3.5-Plus were released, with Qwen3.5 being open-weights. Qwen3.5-Omni and Qwen3.6-Plus were released in April 2026 as proprietary models, with access limited to the chatbots' websites and the Alibaba cloud platform.

## Qwen 3.6 Series

Qwen 3.6 is Alibaba's latest generation of multimodal, open-source large language models. The series genuinely handles text, structured code, vision (via the Qwen 3.6-VL variants), and in select builds, audio and video processing. The models support 201 languages and dialects, enabling inclusive, worldwide deployment with nuanced cultural and regional understanding.

## Key Technical Features

The headline architectural change in Qwen 3.6 is a mature implementation of Mixture-of-Experts (MoE) sparse activation, where MoE routing dynamically selects the most relevant expert sub-networks per token. Extended context is handled via YaRN (Yet another RoPE extensioN), which supports sequences up to 128K tokens.

## Model Variants Available

Qwen3.5 was released on February 16, 2026, with the first release including a 397B-A17B MoE model. Released under the Apache 2.0 license, all weights are free for commercial deployment without royalties or usage fees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8d63b3e-43f7-4163-b047-6b5278f79662",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "a716414c-070c-4f72-a906-4ac7f4f162d9",
  "sourceToolAssistantUUID": "a8d63b3e-43f7-4163-b047-6b5278f79662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T13:21:07.541Z_

<details><summary>↩ Tool result · `toolu_01E25SREfL4ZeGxNwBFu2WEt`</summary>

```text
Web search results for query: "huggingface open LLM leaderboard 2026"

Links: [{"title":"open-llm-leaderboard (Open LLM Leaderboard)","url":"https://huggingface.co/open-llm-leaderboard"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"Open LLM Leaderboard best models ❤️‍🔥 - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-best-models"},{"title":"LLM Performance Leaderboard - a Hugging Face Space by ArtificialAnalysis","url":"https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard"},{"title":"Show HN: How I topped the HuggingFace open LLM leaderboard on two gaming GPUs | Hacker News","url":"https://news.ycombinator.com/item?id=47322887"},{"title":"Hugging Face Open LLM Leaderboard 2026: How Anti-Contamination Controls Reshuffled the Rankings | AgentMarketCap","url":"https://agentmarketcap.ai/blog/2026/04/10/huggingface-open-llm-leaderboard-v3-2026"},{"title":"Official Benchmarks Leaderboard 2026 - a Hugging Face Space by OpenEvals","url":"https://huggingface.co/spaces/OpenEvals/every-leaderboards"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"Leaderboards and Evaluations · Hugging Face","url":"https://huggingface.co/docs/leaderboards/index"},{"title":"Find a leaderboard - a Hugging Face Space by OpenEvals","url":"https://huggingface.co/spaces/OpenEvals/find-a-leaderboard"}]

Based on the search results, here's what I found about the Hugging Face Open LLM Leaderboard in 2026:

## Current Status

The Open LLM Leaderboard is maintained by Hugging Face, where you can find the dataset with detailed results and queries for models on the leaderboard.

## 2026 Rankings and Changes

GLM-5 leads the 2026 open-weight leaderboard while Llama 4 Scout sits at 24. This represents a significant shift in the landscape due to methodology changes. Hugging Face launched Open LLM Leaderboard v2 in late 2024 to solve benchmark contamination issues by replacing saturated tests with six harder ones.

## Key 2026 Insights

A new class of open-weight models—led almost entirely by Chinese labs—now occupies the top tiers of every major leaderboard by margin in early 2026. Chinese research labs—primarily Zhipu AI, Alibaba, Moonshot AI, and DeepSeek—hold the majority of top positions across multiple independent leaderboards.

GPQA Diamond, Humanity's Last Exam, SWE-Bench Verified, and LiveCodeBench are the four tests that actually separate frontier models from each other because they resist data contamination and reward genuine reasoning over pattern recall.

You can access the leaderboard directly at the Hugging Face spaces linked in the search results for up-to-date rankings and evaluations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67b1c012-ebd1-4c99-b93c-2626f0305ee1",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "405b633f-eb18-4b41-bf9c-a47223cba9f6",
  "sourceToolAssistantUUID": "67b1c012-ebd1-4c99-b93c-2626f0305ee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T13:21:08.495Z_

<details><summary>↩ Tool result · `toolu_01E2KM3WMdE683JsvwHXnB42`</summary>

```text
Web search results for query: "Mistral latest model 2026"

Links: [{"title":"Mistral AI Latest Models 2026: The Powerful Breakthroughs (and Hidden Limitations)","url":"https://aizolo.com/blog/mistral-ai-latest-models-2026/"},{"title":"Mistral Docs","url":"https://docs.mistral.ai/models/overview"},{"title":"Mistral AI Models 2026: Small 4, Large 3, Voxtral TTS, Forge — Complete Guide | Serenities AI","url":"https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide"},{"title":"Latest news | Mistral AI","url":"https://mistral.ai/news"},{"title":"Mistral’s Model Lets You Vibe Long-Running Code in the Cloud","url":"https://aibusiness.com/agentic-ai/mistral-s-model-vibe-long-running-code-in-the-cloud"},{"title":"Mistral releases a new open source model for speech generation | TechCrunch","url":"https://techcrunch.com/2026/03/26/mistral-releases-a-new-open-source-model-for-speech-generation/"},{"title":"Mistral AI Models 2026: A Powerful Complete Guide for Builders (With Some Limitations)","url":"https://aizolo.com/blog/mistral-ai-models-2026/"},{"title":"Mistral Medium 3.5: 128B Open-Weight Model Replaces Devstral 2 and Magistral | Let's Data Science","url":"https://letsdatascience.com/blog/mistral-medium-3-5-128b-open-weight-merged-model"},{"title":"Mistral 3 AI Explained - Open-Source Models Guide 2026 — Shawn Kanungo","url":"https://shawnkanungo.com/blog/what-is-mistral-3-ai-open-source-models-guide-2026"},{"title":"Models - from cloud to edge | Mistral AI","url":"https://mistral.ai/models"}]

Based on the search results, here are Mistral's latest models in 2026:

## Latest Mistral Models (2026)

**Mistral Medium 3.5** (April 2026)
On April 30, 2026, Mistral released Medium 3.5, a 128B dense merged model under a modified MIT license. This is "our first flagship merged model" that combines the dedicated reasoning model (Magistral) and the dedicated coding model (Devstral 2) into a single set of weights. It has 128B parameters with a 256K context window, which allows it to manage instruction-following, reasoning and coding.

**Mistral Small 4** (March 2026)
Released March 16, 2026, Mistral Small 4 merges three previously separate products into a single model: Magistral (reasoning), Pixtral (multimodal vision), and Devstral (agentic coding). Despite having 5x more total parameters than Small 3, only 6B are active per token — making it dramatically cheaper to run, with a 40% reduction in end-to-end completion time and 3x more requests per second compared to Small 3.

**Mistral Large 3** (December 2025)
Released in December 2025, Mistral Large 3 remains the crown jewel of the Mistral AI latest models 2026 lineup. Mistral Large 3 is our largest model to date, featuring 41B active parameters and 675B total parameters, with a large 256k context window, and offers powerful agentic capabilities.

**Voxtral TTS** (March 2026)
Released March 23, 2026, Voxtral TTS is Mistral's first audio model — and a direct shot at ElevenLabs. The new model, called Voxtral TTS, supports nine languages, including English, French, German, Spanish, Dutch, Portuguese, Italian, Hindi, and Arabic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b22fea12-06eb-45f6-977b-b60e85e70fbd",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "aeeee83c-d898-4372-a029-8f03b67be8cb",
  "sourceToolAssistantUUID": "b22fea12-06eb-45f6-977b-b60e85e70fbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T13:21:08.834Z_

<details><summary>↩ Tool result · `toolu_01FRarPZF5u4gKfvPbreT2DB`</summary>

```text
Web search results for query: "open source LLM SOTA 2026"

Links: [{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"CodeSOTA — Open AI Benchmark Registry and SOTA API","url":"https://www.codesota.com/code-generation"}]

Based on the web search results, here's what the current state-of-the-art (SOTA) looks like for open-source LLMs in 2026:

## Current Performance Gap

According to Epoch AI, open-weight models now trail the SOTA proprietary models by only about three months on average. 2025 was the year open-source LLMs closed the gap with proprietary models, and in 2026, they're on par in many areas – or better.

## Top Open-Source Models

**For General Reasoning and Performance:**
The best open-source LLMs in 2026 are Meta Llama 4 for general reasoning, Mistral Large for speed and efficiency, and Qwen 2.5 for multilingual tasks, with other top models including DeepSeek for coding and Microsoft Phi-4 for high-performance reasoning in small-scale deployments.

**For Coding Tasks:**
Kimi K2.6 Thinking currently leads on both Coding (78.57) and Agentic Coding (58.33) scores, with GLM 5.1 and DeepSeek V4 Pro close behind on agentic work. Kimi K2.6 is one of the strongest open-weight models for developers in 2026, with about 1.1T parameters listed under a Modified MIT license.

## Key Capabilities

Open-source AI in 2026 is no longer just the cheaper alternative to closed models; for coding, reasoning, agentic workflows, long-context analysis, and local deployment, open-weight models are now good enough for serious production use.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eab162e7-b932-46eb-bd64-152119cd8f17",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "d4e6e34d-6805-4293-b054-565ba1bea65a",
  "sourceToolAssistantUUID": "eab162e7-b932-46eb-bd64-152119cd8f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-15T13:21:12.568Z_

Let me do a couple of follow-up searches to get more specific details on parameter sizes and safety training for the top candidates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4e6e34d-6805-4293-b054-565ba1bea65a",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RYDP3ipDxiWQjaCXEo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abeb90d2-c4de-4d29-b751-fc91467a9b86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFj32PCK7gXjtJ8m2Eq5T8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 952,
      "cache_creation_input_tokens": 6376,
      "cache_read_input_tokens": 9481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6376,
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

_source line 22 · 2026-05-15T13:21:13.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R3biATLTKpwxUrrr5UDhNy`</summary>

```json
{
  "query": "Qwen 3 parameter sizes safety training RLHF open weights 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abeb90d2-c4de-4d29-b751-fc91467a9b86",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RYDP3ipDxiWQjaCXEo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fc3c0eb-ece4-46f9-a4f7-81a3e45ede12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFj32PCK7gXjtJ8m2Eq5T8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 952,
      "cache_creation_input_tokens": 6376,
      "cache_read_input_tokens": 9481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6376,
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

_source line 23 · 2026-05-15T13:21:14.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012HjHDW26SyT6D9y7hydrvK`</summary>

```json
{
  "query": "DeepSeek V4 model sizes parameters open source 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fc3c0eb-ece4-46f9-a4f7-81a3e45ede12",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RYDP3ipDxiWQjaCXEo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dc74be9-1710-4d14-8c76-c7ad9ebe69b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFj32PCK7gXjtJ8m2Eq5T8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 952,
      "cache_creation_input_tokens": 6376,
      "cache_read_input_tokens": 9481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6376,
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

_source line 24 · 2026-05-15T13:21:14.677Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EzSnjuAGcHimCPaBAmEdRR`</summary>

```json
{
  "query": "GLM 5 Zhipu AI parameter sizes open weights license 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dc74be9-1710-4d14-8c76-c7ad9ebe69b3",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RYDP3ipDxiWQjaCXEo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a074c29a-19ae-4dee-9868-321b145d6345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFj32PCK7gXjtJ8m2Eq5T8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 952,
      "cache_creation_input_tokens": 6376,
      "cache_read_input_tokens": 9481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6376,
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

_source line 25 · 2026-05-15T13:21:15.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BFmtFSF9QWjkwPcYzQrxvY`</summary>

```json
{
  "query": "Llama 4 Scout Maverick safety training RLHF fine-tuning research 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a074c29a-19ae-4dee-9868-321b145d6345",
  "isSidechain": true,
  "agentId": "a773a7bcb28c1b47d",
  "requestId": "req_011Cb4RYDP3ipDxiWQjaCXEo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d84b58d3-bd64-4fe1-9f29-9d2ac6707ee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFj32PCK7gXjtJ8m2Eq5T8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 952,
      "cache_creation_input_tokens": 6376,
      "cache_read_input_tokens": 9481,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6376
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 952,
          "output_tokens": 258,
          "cache_read_input_tokens": 9481,
          "cache_creation_input_tokens": 6376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6376,
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

_source line 26 · 2026-05-15T13:21:19.884Z_

<details><summary>↩ Tool result · `toolu_01R3biATLTKpwxUrrr5UDhNy`</summary>

```text
Web search results for query: "Qwen 3 parameter sizes safety training RLHF open weights 2026"

Links: [{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/qwen3"},{"title":"Qwen 3 Release Date: AI Performance Analysis and Model Timeline - H3sync","url":"https://h3sync.com/blog/qwen-3-release-date/"},{"title":"Qwen 3.6: The Frontier Open Foundation Model","url":"https://qwen3lm.com/qwen3.6/"},{"title":"Qwen","url":"https://qwenlm.github.io/"},{"title":"Qwen Models Guide: 600M to 1 Trillion Parameters","url":"https://www.digitalapplied.com/blog/qwen-models-complete-guide"},{"title":"What Is Qwen 3.5? Alibaba's Open-Weight Model That Runs on Your Phone | MindStudio","url":"https://www.mindstudio.ai/blog/what-is-qwen-3-5-alibaba-open-weight-model"},{"title":"MS-SWIFT - Qwen","url":"https://qwen.readthedocs.io/en/latest/training/ms_swift.html"},{"title":"How to Use Qwen3.6-27B: Complete Guide to Alibaba's New Open-Weight Coding Model | Tosea.ai","url":"https://tosea.ai/blog/qwen-3-6-27b-complete-guide"},{"title":"Understanding and Implementing Qwen3 From Scratch","url":"https://magazine.sebastianraschka.com/p/qwen3-from-scratch"},{"title":"Abliterated Models Guide — Qwen 3.6, Gemma 4 Heretic, Llama 3.1 Uncensored Download Links","url":"https://locallyuncensored.com/blog/abliterated-models-guide.html"}]

Based on the search results, here's what I found about Qwen 3 parameter sizes, safety training, RLHF, and open weights in 2026:

## Parameter Sizes

Qwen3 is available in dense and Mixture-of-Experts (MoE) models of various sizes: 0.6B, 1.7B, 4B, 8B, 14B, 32B and 30B-A3B, 235B-A22B. In September 2025, Alibaba's Qwen team released a comprehensive model family spanning from 600M to over 1 trillion parameters.

## Safety Training and RLHF

Qwen 3 uses RLHF (Reinforcement Learning from Human Feedback) with a global pool of diverse annotators to ensure cultural sensitivity. It also utilizes RLAIF (Reinforcement Learning from AI Feedback), where a "Constitution Model" evaluates Qwen 3's outputs for safety and logic.

For Qwen 3.6, the model incorporates multi-stage reinforcement learning from human feedback (RLHF), constitutional AI principles, and red-teaming feedback across 40+ geographic regions.

## Open Weights

Alibaba is making the weights of Qwen3 available to the public, including both dense and Mixture-of-Expert (MoE) models. All open-weights models are released under Apache 2.0 license, support 119 languages, and have native context windows up to 262K tokens (extendable to 1M).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fc3c0eb-ece4-46f9-a4f7-81a3e45ede12",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "58d0d94d-808e-4182-bbde-f2e689ac70a4",
  "sourceToolAssistantUUID": "6fc3c0eb-ece4-46f9-a4f7-81a3e45ede12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T13:21:20.189Z_

<details><summary>↩ Tool result · reported error · `toolu_012HjHDW26SyT6D9y7hydrvK`</summary>

```text
The user doesn't want to proceed with this tool use. The tool use was rejected (eg. if it was a file edit, the new_string was NOT written to the file). STOP what you are doing and wait for the user to tell you how to proceed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dc74be9-1710-4d14-8c76-c7ad9ebe69b3",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "6fe99f79-36b6-4157-a2e5-a69e6def6842",
  "toolUseResult": "User rejected tool use",
  "sourceToolAssistantUUID": "0dc74be9-1710-4d14-8c76-c7ad9ebe69b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T13:21:20.189Z_

<details><summary>↩ Tool result · reported error · `toolu_01EzSnjuAGcHimCPaBAmEdRR`</summary>

```text
The user doesn't want to proceed with this tool use. The tool use was rejected (eg. if it was a file edit, the new_string was NOT written to the file). STOP what you are doing and wait for the user to tell you how to proceed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a074c29a-19ae-4dee-9868-321b145d6345",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "350b41e6-a614-48fb-8c89-086ba9645869",
  "toolUseResult": "User rejected tool use",
  "sourceToolAssistantUUID": "a074c29a-19ae-4dee-9868-321b145d6345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T13:21:20.192Z_

<details><summary>↩ Tool result · reported error · `toolu_01BFmtFSF9QWjkwPcYzQrxvY`</summary>

```text
The user doesn't want to proceed with this tool use. The tool use was rejected (eg. if it was a file edit, the new_string was NOT written to the file). STOP what you are doing and wait for the user to tell you how to proceed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d84b58d3-bd64-4fe1-9f29-9d2ac6707ee6",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "0ce9831e-dcce-4be6-ac65-de9b1d00a2fe",
  "toolUseResult": "User rejected tool use",
  "sourceToolAssistantUUID": "d84b58d3-bd64-4fe1-9f29-9d2ac6707ee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

1 recorded events

### User

_source line 30 · 2026-05-15T13:21:20.192Z_

[Request interrupted by user for tool use]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ce9831e-dcce-4be6-ac65-de9b1d00a2fe",
  "isSidechain": true,
  "promptId": "6432ccac-aeb9-4c9a-96ee-cc32326ed532",
  "agentId": "a773a7bcb28c1b47d",
  "type": "user",
  "uuid": "a867fdeb-f008-4995-9a49-fcbc8a329774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8a782dd9-76fe-4641-9686-c8ac4ddb8016",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
