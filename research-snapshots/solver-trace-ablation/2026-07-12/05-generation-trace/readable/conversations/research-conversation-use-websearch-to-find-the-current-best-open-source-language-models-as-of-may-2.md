# Research conversation: Use WebSearch to find the current best open-source language models as of May 2026. The research direction needs models g

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa4be14f0866b19d4.jsonl`
- **Structured JSON:** [`c47f882f57aee932a5a3.json`](../../sessions/c4/c47f882f57aee932a5a3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-11T20:39:44.640Z_

Use WebSearch to find the current best open-source language models as of May 2026. The research direction needs models good at logical/mathematical reasoning that can be used for inference (not fine-tuning).

Search for:
1. "best open source LLM 2026 reasoning"
2. "top open source language model May 2026"
3. "SOTA open source reasoning model 2026"
4. "Qwen3 model release 2026" — check if Qwen3 exists and what sizes are available
5. "DeepSeek R1 distill 2026" — check current status
6. "open source LLM benchmark leaderboard 2026"
7. "best open weight model for mathematical reasoning 2026"

Report which models are currently at the frontier for open-source reasoning, their sizes, and availability. The user's seed mentions Qwen3 and DeepSeek-R1-distill — verify these are still frontier or if newer models have surpassed them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "22a965bc-9deb-46d8-b3f6-4db7e84a7404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T20:39:44.645Z_

```json
{
  "parentUuid": "22a965bc-9deb-46d8-b3f6-4db7e84a7404",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
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
  "uuid": "8d85e226-e5f1-4fd3-907f-6057d1d85d3e",
  "timestamp": "2026-05-11T20:39:44.645Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T20:39:47.413Z_



I'll start by loading the WebSearch tool schema, then run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d85e226-e5f1-4fd3-907f-6057d1d85d3e",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRkQQPDPN8tB6o2tLxP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ed09da8-4db7-436b-b88b-af5ceb24859e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016it2NDjEad6MnhmWuVt3sn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 776,
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

_source line 4 · 2026-05-11T20:39:47.552Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qom28gusDf3g3TTxrUVULt`</summary>

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
  "parentUuid": "8ed09da8-4db7-436b-b88b-af5ceb24859e",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRkQQPDPN8tB6o2tLxP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7685d631-9ef4-487f-b623-2aed4ec9a912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016it2NDjEad6MnhmWuVt3sn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 8223,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 776,
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

_source line 5 · 2026-05-11T20:39:47.555Z_

<details><summary>↩ Tool result · `toolu_01Qom28gusDf3g3TTxrUVULt`</summary>

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
  "parentUuid": "7685d631-9ef4-487f-b623-2aed4ec9a912",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "2b65f5dc-ed03-46ee-9a8b-eca5dff34934",
  "sourceToolAssistantUUID": "7685d631-9ef4-487f-b623-2aed4ec9a912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T20:39:50.428Z_



Now let me run all 7 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b65f5dc-ed03-46ee-9a8b-eca5dff34934",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRkdBq3g4N44dc4gLn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c77fefd0-739c-4a22-aeff-49b49cfb91cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A87Yojx6EqskanA7ArebYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 7 · 2026-05-11T20:39:50.937Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NydjcNFuhskJXaZsLSBjX6`</summary>

```json
{
  "query": "best open source LLM 2026 reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c77fefd0-739c-4a22-aeff-49b49cfb91cc",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRkdBq3g4N44dc4gLn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c09690f1-66a2-4d53-a1ce-d29a653ea20c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A87Yojx6EqskanA7ArebYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 8 · 2026-05-11T20:39:51.384Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Tkcip9P4uXPCnKowVLk1R`</summary>

```json
{
  "query": "top open source language model May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c09690f1-66a2-4d53-a1ce-d29a653ea20c",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRkdBq3g4N44dc4gLn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40b21352-9db7-494f-906a-894dcff8c686",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A87Yojx6EqskanA7ArebYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 9 · 2026-05-11T20:39:51.425Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ed7r8md9ug9vq8zN4prwxa`</summary>

```json
{
  "query": "SOTA open source reasoning model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40b21352-9db7-494f-906a-894dcff8c686",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRkdBq3g4N44dc4gLn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0eb73c66-a802-43b7-a75d-3197c718c0f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A87Yojx6EqskanA7ArebYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 10 · 2026-05-11T20:39:51.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011LexmkktstmjwckhWHpGAR`</summary>

```json
{
  "query": "Qwen3 model release 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eb73c66-a802-43b7-a75d-3197c718c0f7",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRkdBq3g4N44dc4gLn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1af1ea3-a386-4081-b5d2-8b66d8530824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A87Yojx6EqskanA7ArebYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 11 · 2026-05-11T20:39:52.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XdYC4fgkxLbvJVYtMev2hK`</summary>

```json
{
  "query": "DeepSeek R1 distill 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1af1ea3-a386-4081-b5d2-8b66d8530824",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRkdBq3g4N44dc4gLn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df2fc337-e914-4ca8-8eba-390d789a55a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A87Yojx6EqskanA7ArebYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 12 · 2026-05-11T20:39:52.335Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CL5YKj8Qmy7ChjHM3xWbxv`</summary>

```json
{
  "query": "open source LLM benchmark leaderboard 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df2fc337-e914-4ca8-8eba-390d789a55a9",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRkdBq3g4N44dc4gLn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8906fd08-4272-4018-9389-cc0952d42d35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A87Yojx6EqskanA7ArebYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 13 · 2026-05-11T20:39:52.607Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HyekyecexCPNvDLkoLkyEz`</summary>

```json
{
  "query": "best open weight model for mathematical reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8906fd08-4272-4018-9389-cc0952d42d35",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRkdBq3g4N44dc4gLn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e8924df-3f4b-4b3a-b629-5f24f47a0c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A87Yojx6EqskanA7ArebYS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8999,
      "output_tokens": 342,
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
          "output_tokens": 342,
          "cache_read_input_tokens": 8999,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1413,
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

_source line 14 · 2026-05-11T20:39:58.174Z_

<details><summary>↩ Tool result · `toolu_01NydjcNFuhskJXaZsLSBjX6`</summary>

```text
Web search results for query: "best open source LLM 2026 reasoning"

Links: [{"title":"Best Open Source LLM Leaderboard 2026 | Open Source Model Rankings and Tier List | Onyx AI","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Ultimate Guide - The Best Open Source LLMs for Reasoning in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-reasoning"},{"title":"Best Open Source LLMs in 2026: Ranked by Coding, Reasoning & Cost | WhatLLM.org","url":"https://whatllm.org/best-open-source-llm"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"11 Top Open-Source LLMs for 2026 and Their Uses | DataCamp","url":"https://www.datacamp.com/blog/top-open-source-llms"},{"title":"Best Open-Source LLMs in 2026 - Ranked | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"}]

Based on the web search results, here are the best open source LLMs for reasoning in 2026:

## Top Reasoning Models

The top recommendations for 2026 are DeepSeek-R1, MiniMax-M1-80k, and Kimi-Dev-72B—each chosen for their exceptional reasoning abilities, innovative architectures, and ability to tackle challenging logical problems.

### DeepSeek-R1
DeepSeek-R1 offers OpenAI-o1 comparable performance for general reasoning tasks. DeepSeek came to the spotlight during the "DeepSeek moment" in early 2025, when R1 demonstrated ChatGPT-level reasoning at significantly lower training costs.

### MiniMax-M1-80k
MiniMax-M1-80k provides exceptional computational savings for efficiency and long-context reasoning.

### Kimi-Dev-72B
Kimi-Dev-72B is unmatched for coding and software engineering reasoning with its 60.4% SWE-bench Verified score.

## Other Notable Models

GLM 5.1 is a 744B-parameter MoE (40B active) with a 200K token context, positioned as a flagship release for coding, reasoning, and agentic workflows — currently the leading open-weights model on Artificial Analysis's Intelligence Index.

Qwen 3 235B-A22B currently leads on the broadest range of benchmarks, combining top-tier reasoning, coding, and multilingual capabilities under an Apache 2.0 license.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c09690f1-66a2-4d53-a1ce-d29a653ea20c",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "92363127-be9a-4e17-a59d-25471a555396",
  "sourceToolAssistantUUID": "c09690f1-66a2-4d53-a1ce-d29a653ea20c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T20:39:58.464Z_

<details><summary>↩ Tool result · `toolu_011LexmkktstmjwckhWHpGAR`</summary>

```text
Web search results for query: "Qwen3 model release 2026"

Links: [{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen - Wikipedia","url":"https://en.wikipedia.org/wiki/Qwen"},{"title":"Qwen 3 Release Date: AI Performance Analysis and Model Timeline - H3sync","url":"https://h3sync.com/blog/qwen-3-release-date/"},{"title":"Qwen3.6-Max-Preview: Benchmarks, API & Review (2026)","url":"https://www.buildfastwithai.com/blogs/qwen3-6-max-preview-review-2026"},{"title":"Qwen3.5","url":"https://qwen.ai/research/"},{"title":"Qwen3-Coder-Next: Pushing Small Hybrid Models","url":"https://qwen.ai/blog?id=qwen3-coder-next"},{"title":"Qwen3-Coder-Next: The Complete 2026 Guide to Running Powerful AI Coding Agents Locally - DEV Community","url":"https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95"},{"title":"Qwen3 Coder Next Model Specs, Costs & Benchmarks (April 2026) | Galaxy.ai","url":"https://blog.galaxy.ai/model/qwen3-coder-next"},{"title":"Alibaba Qwen Team Releases Qwen3.6-27B: A Dense Open-Weight Model Outperforming 397B MoE on Agentic Coding Benchmarks - MarkTechPost","url":"https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/"},{"title":"Qwen3-Coder-Next Local Deployment: A Complete Developer Guide (2026)","url":"https://www.sitepoint.com/qwen3codernext-local-deployment-a-complete-developer-guide-2026/"}]

Based on the search results, here's what I found about Qwen3 model releases in 2026:

## Recent Qwen3 Releases in 2026

The Qwen3 model family was released on April 28, 2025, with several subsequent releases throughout 2026:

**Qwen3.5 Series:**
- On February 16, 2026, Qwen3.5 and Qwen3.5-Plus were released
- On February 24, 2026, Qwen3.5-122B-A10B, Qwen3.5-35B-A3B, and Qwen3.5-27B were released

**Qwen3.6 Series:**
- Qwen3.6-Max-Preview was released on April 20, 2026
- Qwen3.6-35B-A3B was released on February 24, 2026
- Qwen3.6-27B was released as the first dense open-weight model in the Qwen3.6 family

**Specialized Models:**
- Qwen3-Coder-Next was released in February 2026, specifically designed for coding agents and local development environments

One source also mentions that the primary Qwen 3 release date for the core LLM models is projected for early Q4 2026, specifically late September to early October, suggesting there may be additional major releases coming later in the year.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1af1ea3-a386-4081-b5d2-8b66d8530824",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "5e0477a9-8da7-49dd-a507-d6807bd16540",
  "sourceToolAssistantUUID": "e1af1ea3-a386-4081-b5d2-8b66d8530824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T20:39:59.156Z_

<details><summary>↩ Tool result · `toolu_01CL5YKj8Qmy7ChjHM3xWbxv`</summary>

```text
Web search results for query: "open source LLM benchmark leaderboard 2026"

Links: [{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"Open Source LLM Leaderboard 2026: Rankings, Benchmarks & the Best Models Right Now &#045; VERTU® Official Site","url":"https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now"},{"title":"Best Open Source LLM Leaderboard 2026 | Open Source Model Rankings and Tier List | Onyx AI","url":"https://onyx.app/open-llm-leaderboard"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"Best Open Source LLM in 2026: Rankings, Benchmarks, and the Models Worth Running | BenchLM.ai","url":"https://benchlm.ai/blog/posts/best-open-source-llm"},{"title":"Best Open Source LLMs in 2026: Rankings and Licensing Comparison | Onyx AI","url":"https://onyx.app/insights/best-open-source-llms-2026"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"open-llm-leaderboard (Open LLM Leaderboard)","url":"https://huggingface.co/open-llm-leaderboard"}]

Based on the search results, here's an overview of open source LLM benchmark leaderboards in 2026:

## Key Leaderboard Platforms

The Vellum Open Source LLM Leaderboard displays the latest public benchmark performance for open-weight and open-source models released after April 2024. It allows you to compare open-source and open-weight LLM benchmarks for models like Llama, DeepSeek, Qwen, and Kimi, with updated rankings across reasoning, coding, math, and multilingual tasks.

Other major leaderboard resources include:
- LLM Stats Open LLM Leaderboard, which compares the best open source LLMs with rankings, pricing, and benchmark scores, providing independent ranking of open-weight models like Llama, Qwen, GLM, DeepSeek, Mistral, and Kimi
- The Hugging Face Open LLM Leaderboard, which lets you explore and compare the performance of open-source large language models on tests such as IFEval, BBH, MATH, GPQA, MUSR, and MMLU-PRO

## Top-Performing Models

DeepSeek V4 Pro (Max) leads BenchLM.ai's open weight leaderboard at 87 overall, followed by Kimi K2.6 at 84, GLM-5 (Reasoning) and GLM-5.1 at 83, and Qwen3.5 397B (Reasoning) at 79.

Among these models, Kimi K2.5 leads HumanEval (99%) and AIME (96.1%), GLM-5 has the strongest SWE-bench result among open models (77.8%), and Qwen 3.5 has the highest GPQA Diamond score among the open-source models listed (88.4%).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8906fd08-4272-4018-9389-cc0952d42d35",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "bf09734c-4a29-49e3-a269-b2fad67768cf",
  "sourceToolAssistantUUID": "8906fd08-4272-4018-9389-cc0952d42d35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T20:39:59.306Z_

<details><summary>↩ Tool result · `toolu_016Tkcip9P4uXPCnKowVLk1R`</summary>

```text
Web search results for query: "top open source language model May 2026"

Links: [{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Best Open Source LLM Leaderboard 2026 | Open Source Model Rankings and Tier List | Onyx AI","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Open-Source LLMs in 2026: Best AI Models | Medium","url":"https://medium.com/@servifyspheresolutions/the-free-models-running-the-world-af6a3d2e8758"},{"title":"The Best Open-Source Small Language Models (SLMs) in 2026","url":"https://www.bentoml.com/blog/the-best-open-source-small-language-models"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Top 35+ Uncensored Open-Source AI Models [Updated May 2026]","url":"https://www.decodesfuture.com/articles/top-uncensored-open-source-ai-models-2026-list"},{"title":"LLM News Today (May 2026) – AI Model Releases","url":"https://llm-stats.com/ai-news"},{"title":"10 Best Open Source LLMs to Evaluate in 2026","url":"https://kanerika.com/blogs/open-source-llms-models/"}]

Based on the search results for top open source language models in May 2026, here are the leading models:

## Frontier-Grade Models

Kimi-K2.6 sets a new open-source bar on complex, end-to-end coding, with benchmark results competitive with top closed-source models like GPT-5.4 and Claude Opus 4.6. Kimi-K2.6 can dynamically decompose complex tasks into parallel subtasks with up to 300 sub-agents across 4,000 coordinated steps simultaneously.

Google's Gemma 3 27B model beats Llama-405B, DeepSeek-V3, and o3-mini on LMArena benchmarks—a 27 billion parameter model outperforming something fifteen times its size.

The top open-source LLMs of 2026 include DeepSeek, Llama 4, Qwen, Kimi, and Gemma.

## Specialized Models

MiMo-V2.5 is the latest open-source model family from Xiaomi for agentic coding, long-horizon reasoning, and multimodal workflows, with MiMo-V2.5-Pro (1.02T total, 42B active) as the flagship LLM for coding agents.

## Market Context

By May 2026, developers worldwide can download frontier-grade models, run them on their own hardware, and deploy them without paying per token. Over half the LLM market runs on-premises, with more organizations trusting open source language models they can own, modify, and control than proprietary APIs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40b21352-9db7-494f-906a-894dcff8c686",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "864719f4-186c-4691-9070-513e82655d5a",
  "sourceToolAssistantUUID": "40b21352-9db7-494f-906a-894dcff8c686",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T20:39:59.824Z_

<details><summary>↩ Tool result · `toolu_01Ed7r8md9ug9vq8zN4prwxa`</summary>

```text
Web search results for query: "SOTA open source reasoning model 2026"

Links: [{"title":"What Are the SOTA AI Models? | Machine Learning Glossary","url":"https://maddevs.io/glossary/state-of-the-art-models/"},{"title":"GitHub - OpenPipe/deductive-reasoning: Train your own SOTA deductive reasoning model · GitHub","url":"https://github.com/openpipe/deductive-reasoning"},{"title":"Gemma 4 Open Models Launched: Google’s Latest SOTA Reasoning From 2B to Edge-Ready Multimodal – Analysis and 2026 Opportunities | AI News Detail","url":"https://blockchain.news/ainews/gemma-4-open-models-launched-google-s-latest-sota-reasoning-from-2b-to-edge-ready-multimodal-analysis-and-2026-opportunities"},{"title":"The State-of-the-Art in Open-Source Large Language Models: A New Era of AI Innovation | by Frank Morales Aguilera | AI Simplified in Plain English | Medium","url":"https://medium.com/ai-simplified-in-plain-english/the-state-of-the-art-in-open-source-large-language-models-a-new-era-of-ai-innovation-9a379aad0a23"},{"title":"Reasoning — SOTA Benchmarks for Math, Science & Code Reasoning | CodeSOTA","url":"https://www.codesota.com/browse/reasoning"},{"title":"SOTA AI Models: Benchmarks, Metrics & Deployment Guide","url":"https://huggingface.co/blog/daya-shankar/sota-ai-models"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"SoTA with Less: MCTS-Guided Sample Selection for Data-Efficient Visual Reasoning Self-Improvement | OpenReview","url":"https://openreview.net/forum?id=PHu9xJeAum"},{"title":"Best Open Source LLM Leaderboard 2026 | Open Source Model Rankings and Tier List | Onyx AI","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Switching from SOTA to Local OSS LLMs: A Practical Guide","url":"https://enji.ai/tech-articles/how-to-switch-from-sota-llms-to-local-oss-llms/"}]

Based on the search results, here are the leading open-source reasoning models in 2026:

## Top Open-Source Reasoning Models

**Google Gemma 4**
Google released Gemma 4, a new family of open foundation models built on the same research and technology as the Gemini 3 series, featuring state-of-the-art reasoning and multimodal capabilities from edge-scale 2B and 4B variants with vision and audio support. Released on April 2, 2026, this new family of foundation models introduces state-of-the-art reasoning capabilities across various scales, starting from edge-friendly 2B and 4B parameter models that incorporate vision and audio modalities.

**DeepSeek-R1**
DeepSeek-R1, with its impressive 671 billion total parameters and efficient Mixture-of-Experts (MoE) architecture, has carved out a niche for its exceptional reasoning and mathematical prowess, often outperforming even some closed-source models on specialized benchmarks.

**Meta Llama 3.1**
The Llama 3.1 405B is a massive and highly performant "dense" model, excelling in general knowledge, reasoning, and coding, with extensive multilingual support and long context windows.

**Qwen3**
Qwen3 comes in three versions: 4b, 8b, and 32b (the 32b version even has reasoning capabilities for complex tasks).

## Key Trends in 2026
AI reasoning has transformed in 2025 with test-time compute scaling rivaling traditional training approaches. Leading models now solve graduate-level problems through extended thinking, but cost and instruction-following trade-offs remain critical deployment considerations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0eb73c66-a802-43b7-a75d-3197c718c0f7",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "297b224a-2b01-42bc-9f0d-e20ce5511615",
  "sourceToolAssistantUUID": "0eb73c66-a802-43b7-a75d-3197c718c0f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T20:40:01.315Z_

<details><summary>↩ Tool result · `toolu_01HyekyecexCPNvDLkoLkyEz`</summary>

```text
Web search results for query: "best open weight model for mathematical reasoning 2026"

Links: [{"title":"Top 10 Open-source Reasoning Models in 2026","url":"https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026"},{"title":"Ultimate Guide - The Best Open Source LLMs for Reasoning in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-reasoning"},{"title":"Best Open Source LLM For Math In 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math"},{"title":"Best Open Source Reasoning Model in 2026 - Ertas AI","url":"https://www.ertas.ai/best/best-open-source-reasoning-model"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Best LLM for Math 2026 - AI Model Benchmark Comparison","url":"https://pricepertoken.com/leaderboards/math"},{"title":"Ultimate Guide - The Best QwQ & Alternative Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-qwq-models-in-2025"},{"title":"Best AI for Math 2026 - Top Mathematical Models","url":"https://llm-stats.com/leaderboards/best-ai-for-math"},{"title":"Best Open Source LLMs in 2026: Ranked by Coding, Reasoning & Cost | WhatLLM.org","url":"https://whatllm.org/best-open-source-llm"},{"title":"Best Reasoning AI Models (2026) — Ranked by Benchmark Data | BenchLM.ai","url":"https://benchlm.ai/best/reasoning-models"}]

Based on the search results, here are the top open-weight models for mathematical reasoning in 2026:

## Top Recommendations

**DeepSeek-R1** is widely recognized as the leading open-weight model for mathematical reasoning. It achieves performance comparable to OpenAI-o1 across math, code, and reasoning tasks, and through carefully designed training methods, it has enhanced overall effectiveness. The full 671B-parameter MoE flagship matches or exceeds OpenAI's o1 on AIME 2024 (math competitions), Codeforces, and GPQA Diamond.

**DeepSeek V4** is recommended for production deployments. DeepSeek V4 is the strongest open-weight choice for general reasoning workloads in 2026, incorporating a unified thinking mode toggle within a single chat checkpoint — fast direct responses for routine queries, extended reasoning when explicitly enabled or when the model detects benefit. The V4 Pro variant currently leads the BenchLM aggregate intelligence index at 87 with strong scores on AIME, GPQA Diamond, and complex code reasoning.

## Alternative Options

**Qwen/QwQ-32B** offers a good balance. DeepSeek-R1 offers elite-level performance comparable to OpenAI-o1, QwQ-32B provides the best balance of capability and efficiency, while GLM-Z1-9B-0414 delivers surprising mathematical prowess in a lightweight package.

**Ministerial 14B** is ideal for resource-constrained environments. Ministerial 14B achieves approximately 85% accuracy on AIME 2025, a leading result for any model under 30B parameters and competitive with models several times larger.

The choice depends on your specific requirements: DeepSeek-R1 for maximum mathematical reasoning power, DeepSeek V4 for practical production deployment, QwQ-32B for efficiency, or smaller models like Ministerial 14B if you have hardware constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e8924df-3f4b-4b3a-b629-5f24f47a0c3d",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "d56c489b-5a8d-4841-9efe-149c2162354a",
  "sourceToolAssistantUUID": "9e8924df-3f4b-4b3a-b629-5f24f47a0c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-11T20:40:07.284Z_

<details><summary>↩ Tool result · `toolu_01XdYC4fgkxLbvJVYtMev2hK`</summary>

```text
Web search results for query: "DeepSeek R1 distill 2026"

Links: [{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/deepseek-r1"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"},{"title":"deepseek-r1","url":"https://lmstudio.ai/models/deepseek-r1"},{"title":"DeepSeek R1 Local Deployment: Complete Guide 2026 | SitePoint","url":"https://www.sitepoint.com/deepseek-r1-local-deployment-guide-2026/"},{"title":"DeepSeek R1 1.5B Review: Run Reasoning on Your Laptop - TokenMix Blog","url":"https://tokenmix.ai/blog/deepseek-r1-1-5b-laptop-reasoning-review-2026"},{"title":"DeepSeek-R1 Distilled Models Overview","url":"https://www.emergentmind.com/topics/deepseek-r1-distilled-models"},{"title":"unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF"},{"title":"What are DeepSeek-R1 distilled models? | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d"},{"title":"DeepSeek-R1 Release | DeepSeek API Docs","url":"https://api-docs.deepseek.com/news/news250120"}]

Here's what I found about DeepSeek R1 distill models in 2026:

## Overview

DeepSeek has open-sourced six dense models distilled from DeepSeek-R1 based on Llama and Qwen. DeepSeek R1 Distilled 1.5B is the smallest member of DeepSeek's R1 reasoning family — distilled from the full 671B model into a 1.5 billion parameter dense architecture that runs on any laptop with 4GB+ free RAM.

## Model Sizes and Performance

The open-sourced distilled models include 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series. DeepSeek-R1-Distill-Qwen-32B outperforms OpenAI-o1-mini across various benchmarks, achieving new state-of-the-art results for dense models.

## Distillation Approach

DeepSeek took a smart shortcut: Started with 6 open-source models from Llama 3.1/3.3 and Qwen 2.5 · Generated 800,000 high-quality reasoning samples using R1 · Fine-tuned the smaller models on these synthetic reasoning data · Unlike R1, these distilled models rely solely on SFT and they do not include an RL stage.

## Key Capabilities

These models balance reasoning accuracy with efficiency, performing robustly across domains like mathematical reasoning, coding, biomedical analysis, and financial evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df2fc337-e914-4ca8-8eba-390d789a55a9",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "717a138a-56a8-4d97-85be-986e8c0d0240",
  "sourceToolAssistantUUID": "df2fc337-e914-4ca8-8eba-390d789a55a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-11T20:40:11.374Z_

Let me run a few more targeted searches to fill in gaps, particularly on DeepSeek V4 and GLM-5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "717a138a-56a8-4d97-85be-986e8c0d0240",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRn5AZ1yJZm4i6wFpBx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c15cc856-dc41-4eef-90d4-0754aec4498d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014An5kA4ynF5Lhu7ZATQnWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1992,
      "cache_creation_input_tokens": 5234,
      "cache_read_input_tokens": 10412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5234,
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

_source line 22 · 2026-05-11T20:40:11.849Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019yaULZpMfye5xevP6wk5AQ`</summary>

```json
{
  "query": "DeepSeek V4 model parameters release date 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c15cc856-dc41-4eef-90d4-0754aec4498d",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRn5AZ1yJZm4i6wFpBx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "372ef08b-fb83-4b97-8f10-b48d71718596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014An5kA4ynF5Lhu7ZATQnWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1992,
      "cache_creation_input_tokens": 5234,
      "cache_read_input_tokens": 10412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5234,
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

_source line 23 · 2026-05-11T20:40:12.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B2mnwAFHvZRS6htyN9EcsC`</summary>

```json
{
  "query": "GLM 5.1 open source model 2026 parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "372ef08b-fb83-4b97-8f10-b48d71718596",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRn5AZ1yJZm4i6wFpBx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e07389fb-475d-4633-90ef-9106b77a74be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014An5kA4ynF5Lhu7ZATQnWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1992,
      "cache_creation_input_tokens": 5234,
      "cache_read_input_tokens": 10412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5234,
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

_source line 24 · 2026-05-11T20:40:12.985Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Cu6ec2cZdPnsoGmuF6Vb6`</summary>

```json
{
  "query": "Qwen3 235B-A22B model sizes available reasoning benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e07389fb-475d-4633-90ef-9106b77a74be",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRn5AZ1yJZm4i6wFpBx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dff59a4e-edc0-4ad1-a11f-0a583d6bfae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014An5kA4ynF5Lhu7ZATQnWR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1992,
      "cache_creation_input_tokens": 5234,
      "cache_read_input_tokens": 10412,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5234
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1992,
          "output_tokens": 193,
          "cache_read_input_tokens": 10412,
          "cache_creation_input_tokens": 5234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5234,
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

_source line 25 · 2026-05-11T20:40:16.971Z_

<details><summary>↩ Tool result · `toolu_019yaULZpMfye5xevP6wk5AQ`</summary>

```text
Web search results for query: "DeepSeek V4 model parameters release date 2026"

Links: [{"title":"DeepSeek V4 Preview Release | DeepSeek API Docs","url":"https://api-docs.deepseek.com/news/news260424"},{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"},{"title":"DeepSeek V4 Pro 2026: 80.6% SWE-Bench, $3.48/M Output (List)","url":"https://codersera.com/blog/deepseek-v4-pro-review-benchmarks-pricing-2026/"},{"title":"DeepSeek V4 (1.6T MoE, Multimodal) | Guides | Clore.ai","url":"https://docs.clore.ai/guides/language-models/deepseek-v4"},{"title":"DeepSeek V4 (2026): 1T Parameters, 81% SWE-bench, $0.30/MTok — Full Specs | NxCode","url":"https://www.nxcode.io/resources/news/deepseek-v4-release-specs-benchmarks-2026"},{"title":"DeepSeek V4 Targets Coding Dominance with Mid-February | Introl Blog","url":"https://introl.com/blog/deepseek-v4-february-2026-coding-model-release"},{"title":"DeepSeek V4: 1T Parameter AI Model Guide | Independent DeepSeek Resource Hub","url":"https://deepseek.ai/deepseek-v4"},{"title":"DeepSeek V4's 1-Trillion Parameter Architecture Targets | Introl Blog","url":"https://introl.com/blog/deepseek-v4-trillion-parameter-coding-model-february-2026"},{"title":"DeepSeek V4 slated for late April: Trillion parameters, million context length, and deep optimization with Huawei Ascend. | DeepSeek v4 - The Next Gen Coding AI Release Date & Features","url":"https://deepseekv4.app/news/2026-04-14-deepseek-v4-release-window"},{"title":"DeepSeek V4 Review. DeepSeek released V4 as a public… | by Barnacle Goose | Apr, 2026 | Medium","url":"https://medium.com/@leucopsis/deepseek-v4-review-a23ce940151c"}]

Based on the search results, here's what I found about DeepSeek V4's model parameters and release date:

## Release Date

DeepSeek V4 Pro was released April 24, 2026, though some sources indicate the release occurred on April 22, 2026 with full open weights under MIT license.

## Model Parameters

DeepSeek V4 comes in two variants with different parameter counts:

1. **DeepSeek-V4-Pro**: A Mixture-of-Experts (MoE) language model with 1.6 trillion parameters (49 billion activated)

2. **DeepSeek-V4-Flash**: A MoE model with 284 billion parameters (13 billion activated), both supporting a context length of one million tokens

## Key Architectural Features

DeepSeek-V4 incorporates a hybrid attention mechanism combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) to dramatically improve long-context efficiency. Additionally, in the 1M-token context setting, DeepSeek-V4-Pro requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "372ef08b-fb83-4b97-8f10-b48d71718596",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "12661689-a167-4c79-bb1a-8ce5eaa41de0",
  "sourceToolAssistantUUID": "372ef08b-fb83-4b97-8f10-b48d71718596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T20:40:19.197Z_

<details><summary>↩ Tool result · `toolu_01B2mnwAFHvZRS6htyN9EcsC`</summary>

```text
Web search results for query: "GLM 5.1 open source model 2026 parameters"

Links: [{"title":"GLM-5.1: #1 Open Source AI Model? Full Review (2026)","url":"https://www.buildfastwithai.com/blogs/glm-5-1-open-source-review-2026"},{"title":"GLM-5.1 - Overview - Z.AI DEVELOPER DOCUMENT","url":"https://docs.z.ai/guides/llm/glm-5.1"},{"title":"GLM 5.1: The Open-Source Model That Matches GPT and Claude on Coding | MindStudio","url":"https://www.mindstudio.ai/blog/glm-5-1-open-source-coding-model"},{"title":"GitHub - zai-org/GLM-5: GLM-5: From Vibe Coding to Agentic Engineering · GitHub","url":"https://github.com/zai-org/GLM-5"},{"title":"zai-org/GLM-5.1 · Hugging Face","url":"https://huggingface.co/zai-org/GLM-5.1"},{"title":"GLM-5.1: The Open-Source Model That Beat GPT-5.4 | Nerd Level Tech","url":"https://nerdleveltech.com/glm-5-1-open-source-beats-gpt-coding-benchmarks"},{"title":"zai-org/GLM-5 · Hugging Face","url":"https://huggingface.co/zai-org/GLM-5"},{"title":"GLM 5 - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/z-ai/glm-5"},{"title":"GLM-5.1 Open Source: #1 on SWE-Bench Pro (What to Know)","url":"https://www.modemguides.com/blogs/ai-news/glm-5-1-open-source-benchmarks-local-ai"},{"title":"glm-5.1","url":"https://ollama.com/library/glm-5.1"}]

Based on the search results, here's information about GLM-5.1, the open-source model released in 2026:

## Model Parameters and Architecture

GLM-5.1 is built on a 754-billion parameter Mixture-of-Experts (MoE) architecture with 40 billion active parameters per token, a 200,000 token context window, and the ability to generate up to 128,000 output tokens in a single response.

The MoE design means the full 754B parameters are never activated simultaneously. Only the most relevant 40B are engaged per token, which keeps inference costs manageable for a model of this scale.

## Release and Developer

GLM-5.1 is Z.ai's flagship open-source AI model, released on April 7, 2026, built specifically for agentic engineering and long-horizon software development tasks.

## Performance Highlights

GLM-5.1 scores 58.4 on SWE-Bench Pro, edging past Claude Opus 4.6's 57.3 on that specific benchmark. It scored 58.4% on SWE-bench Pro, making it the first open-source model to ever lead that leaderboard.

## Licensing and Availability

GLM-5.1 weights are available on Hugging Face under the MIT license, one of the most permissive open-source licenses available. You can download, modify, fine-tune, and deploy it commercially with no usage restrictions or royalty fees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e07389fb-475d-4633-90ef-9106b77a74be",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "c3edeca9-240a-400a-9500-b7ca10684603",
  "sourceToolAssistantUUID": "e07389fb-475d-4633-90ef-9106b77a74be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-11T20:40:19.757Z_

<details><summary>↩ Tool result · `toolu_013Cu6ec2cZdPnsoGmuF6Vb6`</summary>

```text
Web search results for query: "Qwen3 235B-A22B model sizes available reasoning benchmark"

Links: [{"title":"Qwen/Qwen3-235B-A22B-Thinking-2507 · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507"},{"title":"Qwen/Qwen3-235B-A22B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-235B-A22B"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Artificial Analysis on X: \"Qwen3 model family overview: full benchmarks for all 8 Qwen3 models in both reasoning and non-reasoning modes Key results: ➤ Qwen3 235B-A22B (Reasoning): The largest Qwen3 model scores 62 on the Artificial Analysis Intelligence Index, becoming the most intelligent open weights https://t.co/AjmJVVrJLj\" / X","url":"https://x.com/ArtificialAnlys/status/1922317655643717887"},{"title":"Qwen3 235B A22B Thinking 2507 - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/qwen/qwen3-235b-a22b-thinking-2507"},{"title":"Qwen 3 Benchmarks, Comparisons, Model Specifications, and More - DEV Community","url":"https://dev.to/best_codes/qwen-3-benchmarks-comparisons-model-specifications-and-more-4hoa"},{"title":"2025 Complete Guide: Qwen3-235B-A22B-Thinking-2507 - The New Benchmark for Open-Source Thinking Models - DEV Community","url":"https://dev.to/czmilo/2025-complete-guide-qwen3-235b-a22b-thinking-2507-the-new-benchmark-for-open-source-thinking-419d"},{"title":"Qwen: Qwen3 235B A22B Review | Pricing, Benchmarks & Capabilities (2026) | Design for Online","url":"https://designforonline.com/ai-models/qwen-qwen3-235b-a22b/"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"}]

Based on the search results, here's what I found about Qwen3-235B-A22B model sizes and reasoning benchmarks:

## Model Sizes Available

The Qwen3 family includes dense and Mixture-of-Experts (MoE) models of various sizes, available in 0.6B, 1.7B, 4B, 8B, 14B, 32B and 30B-A3B, 235B-A22B. Qwen3-235B-A22B is a large model with 235 billion total parameters and 22 billion activated parameters.

## Reasoning Benchmark Performance

The flagship model, Qwen3-235B-A22B, achieves competitive results in benchmark evaluations of coding, math, general capabilities, etc., when compared to other top-tier models such as DeepSeek-R1, o1, o3-mini, Grok-3, and Gemini-2.5-Pro.

Qwen3 235B-A22B (Reasoning) scores 62 on the Artificial Analysis Intelligence Index, becoming the most intelligent open weights model ever. The thinking-only variant enhances structured logical reasoning, mathematics, science, and long-form generation, showing strong benchmark performance across AIME, SuperGPQA, LiveCodeBench, and MMLU-Redux.

Additionally, the AIME'24 score of the Qwen3-235B-A22B model increases from 70.1 to 85.1 over a total of 170 RL training steps.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dff59a4e-edc0-4ad1-a11f-0a583d6bfae3",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "aa4be14f0866b19d4",
  "type": "user",
  "uuid": "2461ed0e-a632-4053-baa2-2fec0d8a25ea",
  "sourceToolAssistantUUID": "dff59a4e-edc0-4ad1-a11f-0a583d6bfae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-11T20:41:08.647Z_

Here is a comprehensive report on the current frontier of open-source/open-weight language models for logical and mathematical reasoning as of May 2026.

---

## Tier 1: Frontier Open-Weight Reasoning Models

### DeepSeek V4 Pro (released April 24, 2026)
- **Parameters:** 1.6T total / 49B active (MoE)
- **Context:** 1M tokens
- **License:** MIT
- **Status:** Currently the **#1 open-weight model** on BenchLM's aggregate intelligence index (score: 87). Incorporates a unified "thinking mode toggle" -- fast direct responses for routine queries, extended reasoning when needed. Strong on AIME, GPQA Diamond, and complex code reasoning. The lighter **DeepSeek-V4-Flash** variant (284B total / 13B active) is also available for cost-sensitive deployments.

### GLM-5.1 (released April 7, 2026)
- **Parameters:** 754B total / 40B active (MoE)
- **Context:** 200K tokens, up to 128K output tokens
- **License:** MIT
- **Status:** First open-source model to lead SWE-Bench Pro (58.4%, edging Claude Opus 4.6's 57.3). Strong on agentic engineering and long-horizon software tasks. From Z.ai (formerly Zhipu AI).

### Kimi-K2.6
- **Status:** Scored 84 on BenchLM aggregate, leads HumanEval (99%) and AIME (96.1%). Competitive with GPT-5.4 and Claude Opus 4.6 on complex end-to-end coding. Can decompose tasks into parallel sub-agents.

---

## Tier 2: Strong Reasoning Models (Excellent and Widely Deployed)

### Qwen3 family (original release April 28, 2025; successors through 2026)
- **Qwen3-235B-A22B:** 235B total / 22B active (MoE). Scored 62 on Artificial Analysis Intelligence Index. Strong on AIME'24 (85.1 after RL), SuperGPQA, LiveCodeBench. Apache 2.0 license. Leads on broadest range of benchmarks combining reasoning, coding, and multilingual.
- **Available sizes:** 0.6B, 1.7B, 4B, 8B, 14B, 32B (dense); 30B-A3B, 235B-A22B (MoE).
- **Newer successors:** Qwen3.5 (Feb 2026) with 122B-A10B, 35B-A3B, 27B variants; Qwen3.6 (April 2026) with 27B dense model and Qwen3.6-Max-Preview; Qwen3-Coder-Next for coding agents.
- **Verdict:** Qwen3 is **not obsolete** -- it remains strong, and its successors (3.5, 3.6) extend the family further. The 235B-A22B remains a top-tier reasoning model, though DeepSeek V4 Pro and Kimi-K2.6 now score higher on aggregate leaderboards.

### DeepSeek-R1 (released January 2025)
- **Parameters:** 671B total (MoE)
- **Status:** Still an excellent reasoning model that matches or exceeds OpenAI o1 on AIME 2024, Codeforces, and GPQA Diamond. However, it has been **superseded by DeepSeek V4** as the flagship. R1 remains highly relevant for mathematical reasoning workloads.
- **Distilled variants (DeepSeek-R1-Distill):** Available in 1.5B, 7B, 8B, 14B, 32B, and 70B sizes (based on Qwen2.5 and Llama3). The 32B distill outperforms OpenAI o1-mini. These are **still excellent** for resource-constrained deployments and remain among the best small reasoning models, though newer alternatives now exist.

### Google Gemma 4 (released April 2, 2026)
- Edge-friendly models at 2B and 4B parameters with vision and audio. SOTA reasoning at small scale.

### Gemma 3 27B
- Beats Llama-405B, DeepSeek-V3, and o3-mini on LMArena benchmarks despite being only 27B parameters.

---

## Tier 3: Efficient / Specialized Reasoning Models

| Model | Size | Strength |
|---|---|---|
| **QwQ-32B** (Qwen) | 32B dense | Best balance of capability and efficiency for reasoning |
| **MiniMax-M1-80k** | -- | Long-context reasoning with computational savings |
| **GLM-Z1-9B** | 9B | Surprisingly strong math for its size |
| **Ministerial 14B** | 14B | ~85% on AIME 2025; competitive with much larger models |
| **MiMo-V2.5-Pro** (Xiaomi) | 1.02T total / 42B active | Agentic coding and long-horizon reasoning |
| **Kimi-Dev-72B** | 72B | 60.4% SWE-bench Verified for software engineering |

---

## Verdict on User's Seed Models

**Qwen3:** Still frontier-class. The 235B-A22B is a top-5 open reasoning model. The family has expanded with Qwen3.5 and Qwen3.6 variants. For inference-only use, the 32B dense or 235B-A22B MoE are excellent choices depending on hardware budget.

**DeepSeek-R1-Distill:** Still very good, especially the 32B and 70B distills for cost-effective reasoning. However, they have been **partially surpassed** by:
- DeepSeek V4 Flash (284B/13B active) for similar cost with better performance
- Qwen3.5/3.6 dense models at similar sizes
- GLM-Z1-9B and Ministerial 14B at the small-model end

**What has surpassed them both:** DeepSeek V4 Pro (87 on BenchLM), Kimi-K2.6 (84), and GLM-5.1 (83) now represent the true frontier for open-weight reasoning.

---

## Recommendation for Inference (Not Fine-Tuning)

- **Maximum reasoning power, ample hardware:** DeepSeek V4 Pro (1.6T/49B active, MIT license)
- **Strong reasoning, moderate hardware:** Qwen3-235B-A22B or GLM-5.1 (both ~40B active parameters)
- **Single-GPU reasoning:** QwQ-32B, Qwen3-32B, or DeepSeek-R1-Distill-32B
- **Laptop/edge:** Gemma 4 (2B/4B) or DeepSeek-R1-Distill-1.5B/7B

Sources:
- [Best Open Source LLMs for Reasoning in 2026 - SiliconFlow](https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-reasoning)
- [Best Open Source LLM Leaderboard 2026 - Onyx AI](https://onyx.app/open-llm-leaderboard)
- [Open Source LLM Leaderboard 2026 - Vellum](https://www.vellum.ai/open-llm-leaderboard)
- [Best Open Source LLM for Math in 2026 - SiliconFlow](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-math)
- [LLM Benchmark Leaderboard 2026 - CodeSOTA](https://www.codesota.com/llm)
- [Best Open Source LLM 2026 - BenchLM](https://benchlm.ai/blog/posts/best-open-source-llm)
- [DeepSeek V4 Pro - Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [DeepSeek V4 Preview Release - DeepSeek API Docs](https://api-docs.deepseek.com/news/news260424)
- [GLM-5.1 Full Review 2026 - BuildFastWithAI](https://www.buildfastwithai.com/blogs/glm-5-1-open-source-review-2026)
- [GLM-5.1 - Hugging Face](https://huggingface.co/zai-org/GLM-5.1)
- [Qwen3-235B-A22B - Hugging Face](https://huggingface.co/Qwen/Qwen3-235B-A22B)
- [Qwen3.6 - GitHub](https://github.com/QwenLM/Qwen3.6)
- [Alibaba Qwen3.6-27B Release - MarkTechPost](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)
- [DeepSeek-R1 - GitHub](https://github.com/deepseek-ai/deepseek-r1)
- [Gemma 4 Open Models Launched - Blockchain News](https://blockchain.news/ainews/gemma-4-open-models-launched-google-s-latest-sota-reasoning-from-2b-to-edge-ready-multimodal-analysis-and-2026-opportunities)
- [Top 10 Open-Source Reasoning Models 2026 - Clarifai](https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026)
- [Best Reasoning AI Models 2026 - BenchLM](https://benchlm.ai/best/reasoning-models)
- [Best AI for Math 2026 - LLM Stats](https://llm-stats.com/leaderboards/best-ai-for-math)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2461ed0e-a632-4053-baa2-2fec0d8a25ea",
  "isSidechain": true,
  "agentId": "aa4be14f0866b19d4",
  "requestId": "req_011CawRnzXmyyVXAUqCTNZww",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "023ad401-4abe-462f-91b4-64c5c68d226f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9Q4dzpBHXhrgEDZK1nHgU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5193,
      "cache_read_input_tokens": 15646,
      "output_tokens": 2581,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5193
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2581,
          "cache_read_input_tokens": 15646,
          "cache_creation_input_tokens": 5193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5193,
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
