# Research conversation: I need you to do two tasks: TASK 1: Find the current best open-source LLMs for multilingual instruction tuning in 2026. 

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a23571b3019c9aac5.jsonl`
- **Structured JSON:** [`a49b5437de7191d64c83.json`](../../sessions/a4/a49b5437de7191d64c83.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-10T06:21:20.986Z_

I need you to do two tasks:

TASK 1: Find the current best open-source LLMs for multilingual instruction tuning in 2026. Search:
- "best open source multilingual LLM 2026"
- "SOTA open source language model multilingual 2026"
- "Llama 4 vs Gemma vs Qwen multilingual 2026"
Report model names, sizes, and what makes them good for multilingual tasks.

TASK 2: Verify these paper references are real (search for each):
1. "Left Behind arXiv 2603.21036" - paper about cross-lingual transfer gaps for Kazakh and Mongolian
2. "CLO arXiv 2505.14297" - paper about cross-lingual optimization with 3200 samples
3. "PLUG ACL 2024 cross-lingual instruction generation"
4. "Family Matters arXiv 2510.00810 Nordic languages Faroese"
5. "Cross-Linguistic Transfer in Multilingual NLP arXiv 2505.13908"
6. "Multi-Linguistic LoRA Merging NeurIPS 2025"

For each paper: confirm title, venue/arXiv ID, and whether it's real. Report exact titles as they appear.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d908c3c3-c203-4310-b121-66c8213aac0a",
  "agentId": "a23571b3019c9aac5",
  "type": "user",
  "uuid": "6095f0e4-9193-422e-8407-84ef743e0d26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T06:21:22.175Z_

I'll help you with both tasks. Let me start by searching for information about current best open-source LLMs for multilingual instruction tuning, and then verify those paper references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6095f0e4-9193-422e-8407-84ef743e0d26",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQUw4nSEUuCSKon5dZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "250dd31b-2190-4b4b-b71f-d7f2fce96f01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D3CiiYhxcSQVNZRRSeTSVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
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

_source line 3 · 2026-05-10T06:21:22.405Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QM3gRc3uLmwTr327N1k2qj`</summary>

```json
{
  "query": "best open source multilingual LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "250dd31b-2190-4b4b-b71f-d7f2fce96f01",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQUw4nSEUuCSKon5dZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c9f5d9f-2d59-44ef-a855-33d901de85fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D3CiiYhxcSQVNZRRSeTSVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
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

_source line 4 · 2026-05-10T06:21:22.619Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KnX7mupa6r4QBVTMPAqqE3`</summary>

```json
{
  "query": "SOTA open source language model multilingual 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c9f5d9f-2d59-44ef-a855-33d901de85fa",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQUw4nSEUuCSKon5dZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4baba7ea-bb32-4101-a862-f923ae71f458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D3CiiYhxcSQVNZRRSeTSVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
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

_source line 5 · 2026-05-10T06:21:22.623Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LJLihMXn5QDBU5t9wWBK1N`</summary>

```json
{
  "query": "Llama 4 vs Gemma vs Qwen multilingual 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4baba7ea-bb32-4101-a862-f923ae71f458",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQUw4nSEUuCSKon5dZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "418e9f1c-d5ab-4cff-9922-732418bf5758",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D3CiiYhxcSQVNZRRSeTSVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
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

_source line 6 · 2026-05-10T06:21:22.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KMFwJFwbNz6DckjiXh9BPi`</summary>

```json
{
  "query": "Left Behind arXiv 2603.21036 Kazakh Mongolian cross-lingual transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "418e9f1c-d5ab-4cff-9922-732418bf5758",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQUw4nSEUuCSKon5dZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "783f1e76-ab48-471a-b853-190f9d12447b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D3CiiYhxcSQVNZRRSeTSVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
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

_source line 7 · 2026-05-10T06:21:23.067Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VpbtBi3M8aHSc4Q7p4cGQX`</summary>

```json
{
  "query": "CLO arXiv 2505.14297 cross-lingual optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "783f1e76-ab48-471a-b853-190f9d12447b",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQUw4nSEUuCSKon5dZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7feed60-d30d-4b6c-b0ad-03f64c7085db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D3CiiYhxcSQVNZRRSeTSVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
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

_source line 8 · 2026-05-10T06:21:23.278Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ig3arNzKqS74zqFjD6LDw`</summary>

```json
{
  "query": "PLUG ACL 2024 cross-lingual instruction generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7feed60-d30d-4b6c-b0ad-03f64c7085db",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQUw4nSEUuCSKon5dZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "10e6b4c6-145f-46b8-ae88-92590716c178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D3CiiYhxcSQVNZRRSeTSVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
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

_source line 9 · 2026-05-10T06:21:23.486Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011z8R4YPnUhYGr5SEp23kkd`</summary>

```json
{
  "query": "Family Matters arXiv 2510.00810 Nordic Faroese languages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10e6b4c6-145f-46b8-ae88-92590716c178",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQUw4nSEUuCSKon5dZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c19a856-c3c1-4c1a-bb7e-ed7023c179e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D3CiiYhxcSQVNZRRSeTSVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 736,
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

_source line 10 · 2026-05-10T06:21:23.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BXefwbvJfUqD7tZvYUL3KG`</summary>

```json
{
  "query": "Cross-Linguistic Transfer Multilingual NLP arXiv 2505.13908"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c19a856-c3c1-4c1a-bb7e-ed7023c179e4",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQUw4nSEUuCSKon5dZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "054da52f-6ffe-4d01-a701-779703346d88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D3CiiYhxcSQVNZRRSeTSVL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 16155,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 736
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 512,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 736,
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

_source line 11 · 2026-05-10T06:21:23.754Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018X1LydBYgYUzGZmEHUCh2h`</summary>

```json
{
  "query": "Multi-Linguistic LoRA Merging NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "054da52f-6ffe-4d01-a701-779703346d88",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQUw4nSEUuCSKon5dZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0cdbb69d-a5ba-4dca-ab22-84760a57ecb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D3CiiYhxcSQVNZRRSeTSVL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 16155,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 736
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 512,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 736,
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

_source line 12 · 2026-05-10T06:21:28.619Z_

<details><summary>↩ Tool result · `toolu_01QM3gRc3uLmwTr327N1k2qj`</summary>

```text
Web search results for query: "best open source multilingual LLM 2026"

Links: [{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"},{"title":"The Best Open Source LLMs and Their Uses in 2026 | igmGuru","url":"https://www.igmguru.com/blog/top-open-source-llms"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"Ultimate Guide - The Best Open Source LLM For Spanish In 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-llm-for-spanish"},{"title":"Best Open Source LLM Leaderboard 2026 | Open Source Model Rankings and Tier List | Onyx AI","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"}]

Based on the search results, here are the best open-source multilingual LLMs in 2026:

## Top Multilingual Models

For multilingual tasks, Qwen 2.5 is recommended as one of the best open-source LLMs in 2026. Additionally, Qwen3-235B-A22B and Qwen3-14B are among the top recommendations for 2026, chosen for their outstanding multilingual language performance and ability to push the boundaries of open source multilingual LLMs.

Gemma 4 is pretrained on over 100+ languages and supports 30+ languages out of the box, making it well-suited for multilingual applications.

Meta Llama 4 is recommended for general reasoning and is highly performant on multilingual tasks.

## Other Strong Contenders

BLOOM, Llama 3.1, Mistral, MPT and Falcon are among the great multilingual LLMs available.

DeepSeek released powerful models like DeepSeek-MoE and DeepSeek-Coder that are optimized for multilingual and coding tasks and show promising results on recent benchmarks.

It's important to note that there is no single "best" open-source LLM, as the optimal choice depends on your specific use case, hardware constraints, and performance requirements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c9f5d9f-2d59-44ef-a855-33d901de85fa",
  "isSidechain": true,
  "promptId": "d908c3c3-c203-4310-b121-66c8213aac0a",
  "agentId": "a23571b3019c9aac5",
  "type": "user",
  "uuid": "406b39e1-bed4-4a35-bd33-b45f6fdd3222",
  "sourceToolAssistantUUID": "7c9f5d9f-2d59-44ef-a855-33d901de85fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T06:21:29.054Z_

<details><summary>↩ Tool result · `toolu_01BXefwbvJfUqD7tZvYUL3KG`</summary>

```text
Web search results for query: "Cross-Linguistic Transfer Multilingual NLP arXiv 2505.13908"

Links: [{"title":"[2505.13908] Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology","url":"https://arxiv.org/abs/2505.13908"},{"title":"Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Cross-Lingual Transfer in Sense-Aware Tasks","url":"https://arxiv.org/html/2505.24834"},{"title":"Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Transfer in Sense-Aware Tasks","url":"https://arxiv.org/html/2505.24834v1"},{"title":"Cross-Lingual Summarization for Low-Resource Languages Using Multilingual Retrieval-Based In-Context Learning","url":"https://www.mdpi.com/2076-3417/15/14/7800"},{"title":"Cross-Lingual Transfer Learning for Multilingual Task Oriented Dialog","url":"https://www-nlp.stanford.edu/pubs/schuster2019crosslingual.pdf"},{"title":"Cross-Lingual Transfer Learning","url":"https://www.emergentmind.com/topics/cross-lingual-transfer-learning"},{"title":"Cross-Lingual Knowledge Transfer","url":"https://www.emergentmind.com/topics/cross-lingual-knowledge-transfer"},{"title":"(PDF) Cross-Lingual Transfer Learning for Low-Resource NLP Tasks: Leveraging Multilingual Pretrained Models","url":"https://www.researchgate.net/publication/387003964_Cross-Lingual_Transfer_Learning_for_Low-Resource_NLP_Tasks_Leveraging_Multilingual_Pretrained_Models"},{"title":"Cross-Lingual Transfer: Language Selection","url":"https://www.emergentmind.com/topics/cross-lingual-transfer-language-selection"},{"title":"[2403.20056] Cross-Lingual Transfer Robustness to Lower-Resource Languages on Adversarial Datasets","url":"https://arxiv.org/abs/2403.20056"}]

Based on the search results, here's what I found about the paper with arXiv ID 2505.13908:

## Paper Overview

The paper "Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology" by Ajitesh Bankula and Praney Bankula was submitted on May 20, 2025.

## Research Focus

The paper investigates cross-linguistic transfer through the lens of language families and morphology, examining how language family proximity and morphological similarity affect performance across NLP tasks.

## Key Context

Cross-lingual transfer has become a crucial aspect of multilingual NLP, as it allows for models trained on resource-rich languages to be applied to low-resource languages more effectively. Recently massively multilingual pre-trained language models (e.g., mBERT, XLM-R) demonstrate strong zero-shot transfer capabilities.

## Research Methodology

The paper compares multilingual model performance and reviews how linguistic distance metrics correlate with transfer outcomes, and also looks into emerging approaches that integrate typological and morphological information into model pre-training to improve transfer to diverse languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "054da52f-6ffe-4d01-a701-779703346d88",
  "isSidechain": true,
  "promptId": "d908c3c3-c203-4310-b121-66c8213aac0a",
  "agentId": "a23571b3019c9aac5",
  "type": "user",
  "uuid": "5aa041e9-b8bc-41e3-af22-925f16b75760",
  "sourceToolAssistantUUID": "054da52f-6ffe-4d01-a701-779703346d88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T06:21:29.476Z_

<details><summary>↩ Tool result · `toolu_01VpbtBi3M8aHSc4Q7p4cGQX`</summary>

```text
Web search results for query: "CLO arXiv 2505.14297 cross-lingual optimization"

Links: [{"title":"[2505.14297] Cross-Lingual Optimization for Language Transfer in Large Language Models","url":"https://arxiv.org/abs/2505.14297"},{"title":"Cross-Lingual Optimization for Language Transfer in Large Language Models","url":"https://arxiv.org/html/2505.14297"},{"title":"Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models","url":"https://arxiv.org/html/2505.18673v1"},{"title":"The Unreasonable Effectiveness of Model Merging for Cross-Lingual Transfer in LLMs","url":"https://arxiv.org/html/2505.18356v1"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=800&show=500"},{"title":"Computation and Language May 2025","url":"http://arxiv.org/list/cs.CL/2025-05?skip=800&show=2000"},{"title":"Understanding Cross-Lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2505.13141v1"},{"title":"[2604.11096] Efficient Training for Cross-lingual Speech Language Models","url":"https://arxiv.org/abs/2604.11096"},{"title":"[2505.18673] Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models","url":"https://arxiv.org/abs/2505.18673"},{"title":"[2603.04678v1] Optimizing Language Models for Crosslingual Knowledge Consistency","url":"https://arxiv.org/abs/2603.04678v1"}]

Based on the search results, here's information about CLO (Cross-Lingual Optimization) from arXiv paper 2505.14297:

## Overview

Cross-Lingual Optimization (CLO) is a method that efficiently transfers an English-centric LLM to a target language while preserving its English capabilities.

## Problem Addressed

The paper addresses challenges in adapting large language models to other languages, noting that supervised fine-tuning (SFT) often suffers from an overemphasis on English performance, especially in data-constrained environments.

## Approach

CLO utilizes publicly available English SFT data and a translation model to enable cross-lingual transfer. More specifically, it modifies the Direct Preference Optimization (DPO) approach to increase preference for responding in the same language as the input, while reducing preference for responding in different languages, thereby facilitating knowledge acquisition in the target language.

## Key Results

CLO consistently outperforms SFT in both acquiring target language proficiency and maintaining English performance, and remarkably, in low-resource languages, CLO with only 3,200 samples surpasses SFT with 6,400 samples. Additionally, SFT is particularly sensitive to data quantity in medium and low-resource languages, whereas CLO remains robust.

The paper was accepted for publication at ACL 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7feed60-d30d-4b6c-b0ad-03f64c7085db",
  "isSidechain": true,
  "promptId": "d908c3c3-c203-4310-b121-66c8213aac0a",
  "agentId": "a23571b3019c9aac5",
  "type": "user",
  "uuid": "07ff675d-1de7-4f80-9c09-c25812e4b84e",
  "sourceToolAssistantUUID": "f7feed60-d30d-4b6c-b0ad-03f64c7085db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T06:21:29.601Z_

<details><summary>↩ Tool result · `toolu_01KMFwJFwbNz6DckjiXh9BPi`</summary>

```text
Web search results for query: "Left Behind arXiv 2603.21036 Kazakh Mongolian cross-lingual transfer"

Links: [{"title":"[2603.21036] Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models","url":"https://arxiv.org/abs/2603.21036"},{"title":"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource","url":"https://arxiv.org/pdf/2603.21036"},{"title":"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models","url":"https://arxiv.org/html/2603.21036"},{"title":"Left Behind: Cross-Lingual Transfer as a Bridge for Low- ...","url":"https://www.deepdyve.com/lp/arxiv/left-behind-cross-lingual-transfer-as-a-bridge-for-low-resource-lp4hAVwp8a"},{"title":"Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon","url":"https://arxiv.org/html/2506.01675"},{"title":"Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/html/2604.06202"},{"title":"Enhancing Cross-Lingual Transfer through Reversible","url":"https://arxiv.org/pdf/2509.17493"},{"title":"Shared Weights Pretraining for Extremely Low-Resource ...","url":"https://aclanthology.org/2025.acl-long.893.pdf"},{"title":"[2604.06202] Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/abs/2604.06202"},{"title":"Left Behind: Cross-Lingual Transfer as a Bridge for Low- ...","url":"https://www.researchgate.net/publication/403072467_Left_Behind_Cross-Lingual_Transfer_as_a_Bridge_for_Low-Resource_Languages_in_Large_Language_Models"}]

I found the paper! Here are the key details about arXiv 2603.21036:

## Paper Overview

The paper investigates how large language models perform on low-resource languages by benchmarking eight LLMs across five experimental conditions in English, Kazakh, and Mongolian. The paper is authored by Abdul-Salem Beibitkhan from North American University.

## Methodology

The research uses 50 hand-crafted questions spanning factual, reasoning, technical, and culturally grounded categories, evaluating 2,000 responses on accuracy, fluency, and completeness.

## Key Findings

The study found a consistent performance gap of 13.8-16.7 percentage points between English and low-resource language conditions, with models maintaining surface-level fluency while producing significantly less accurate content.

Regarding cross-lingual transfer specifically, cross-lingual transfer—prompting models to reason in English before translating back—yields selective gains for bilingual architectures (+2.2pp to +4.3pp) but provides no benefit to English-dominant models.

## Conclusion

The results demonstrate that current LLMs systematically underserve low-resource language communities, and that effective mitigation strategies are architecture-dependent rather than universal.

The paper was published on March 22, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "783f1e76-ab48-471a-b853-190f9d12447b",
  "isSidechain": true,
  "promptId": "d908c3c3-c203-4310-b121-66c8213aac0a",
  "agentId": "a23571b3019c9aac5",
  "type": "user",
  "uuid": "c5fef156-2851-4c19-81a8-e79026bf387b",
  "sourceToolAssistantUUID": "783f1e76-ab48-471a-b853-190f9d12447b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T06:21:29.947Z_

<details><summary>↩ Tool result · `toolu_01KnX7mupa6r4QBVTMPAqqE3`</summary>

```text
Web search results for query: "SOTA open source language model multilingual 2026"

Links: [{"title":"The State-of-the-Art in Open-Source Large Language Models: A New Era of AI Innovation | by Frank Morales Aguilera | AI Simplified in Plain English | Medium","url":"https://medium.com/ai-simplified-in-plain-english/the-state-of-the-art-in-open-source-large-language-models-a-new-era-of-ai-innovation-9a379aad0a23"},{"title":"Microsoft AI Releases Harrier-OSS-v1: A New Family of Multilingual Embedding Models Hitting SOTA on Multilingual MTEB v2 - MarkTechPost","url":"https://www.marktechpost.com/2026/03/30/microsoft-ai-releases-harrier-oss-v1-a-new-family-of-multilingual-embedding-models-hitting-sota-on-multilingual-mteb-v2/"},{"title":"Mixtral 8x22B: SOTA Open-Source LLM Capabilities at a Fraction of the Compute — Jon Krohn","url":"https://www.jonkrohn.com/posts/2024/4/26/mixtral-8x22b-sota-open-source-llm-capabilities-at-a-fraction-of-the-compute"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"What Are the SOTA AI Models? | Machine Learning Glossary","url":"https://maddevs.io/glossary/state-of-the-art-models/"},{"title":"Code Generation Benchmarks 2026: SOTA LLMs for Programming | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"},{"title":"Microsoft Harrier-OSS-v1: The Multilingual Embedding Model Built on Google's Own Architecture","url":"https://www.revolutioninai.com/2026/04/microsoft-harrier-oss-v1-multilingual-embedding-model-2026.html"},{"title":"The Best Open-Source Text-to-Speech Models in 2026","url":"https://www.bentoml.com/blog/exploring-the-world-of-open-source-text-to-speech-models"}]

Based on the search results, here's what's current for state-of-the-art (SOTA) open-source multilingual language models in 2026:

## Top SOTA Open-Source Multilingual Models

The best open-source LLMs in 2026 are Meta Llama 4 for general reasoning, Mistral Large for speed and efficiency, and Qwen 2.5 for multilingual tasks.

**Specific Multilingual Leaders:**

1. **Qwen 3.5** - Qwen3.5 expands multilingual coverage to over 200 languages and dialects. The model shows strong capabilities across instruction following, reasoning, coding, agentic, and multilingual tasks and in many benchmarks performs competitively with frontier closed-source models such as GPT-5.2 and Claude 4.5 Opus.

2. **Mistral Models** - Mistral AI's family of models (Mixtral, Pixtral) has gained significant traction for their remarkable efficiency, speed, and strong multilingual capabilities.

3. **Llama 4** - LLaMA 4 pushes language modeling further with versions ranging from 16*17B to 128*17B parameters and is highly performant on reasoning and multilingual tasks.

4. **Gemma 4** - Pretrained on over 100+ languages and supporting 30+ languages out of the box, Gemma 4 works well for multilingual applications.

## Multilingual Embeddings SOTA

Microsoft released Harrier-OSS-v1, a family of three multilingual text embedding models achieving state-of-the-art (SOTA) results on the Multilingual MTEB (Massive Text Embedding Benchmark) v2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4baba7ea-bb32-4101-a862-f923ae71f458",
  "isSidechain": true,
  "promptId": "d908c3c3-c203-4310-b121-66c8213aac0a",
  "agentId": "a23571b3019c9aac5",
  "type": "user",
  "uuid": "fec51bc5-04a0-4fdb-91f9-9b61deea14a8",
  "sourceToolAssistantUUID": "4baba7ea-bb32-4101-a862-f923ae71f458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T06:21:30.266Z_

<details><summary>↩ Tool result · `toolu_018ig3arNzKqS74zqFjD6LDw`</summary>

```text
Web search results for query: "PLUG ACL 2024 cross-lingual instruction generation"

Links: [{"title":"GitHub - ytyz1307zzh/PLUG: Code for the ACL 2024 paper \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning\"","url":"https://github.com/ytyz1307zzh/PLUG"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.379/"},{"title":"Leveraging Pivot Language in Cross-Lingual Instruction ...","url":"https://aclanthology.org/2024.acl-long.379.pdf"},{"title":"Accepted Main Conference Papers - ACL 2024","url":"https://2024.aclweb.org/program/main_conference_papers/"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | Underline","url":"https://underline.io/lecture/102322-plug-leveraging-pivot-language-in-cross-lingual-instruction-tuning"},{"title":"X-Instruction: Aligning Language Model in Low-resource ...","url":"https://nlpr-web.ia.ac.cn/cip/ZongPublications/2024/2024-LiChong-ACL.pdf"},{"title":"Empowering cross-lingual abilities of instruction-tuned large language models by translation-following demonstrations - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.473/"},{"title":"X-Instruction: Aligning Language Model in Low-resource Languages with Self-curated Cross-lingual Instructions - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.30/"},{"title":"Zero-shot cross-lingual transfer in instruction tuning of large language models - ACL Anthology","url":"https://aclanthology.org/2024.inlg-main.53/"},{"title":"Enhancing LLM Language Adaption through Cross-lingual ...","url":"https://aclanthology.org/2025.emnlp-main.1380.pdf"}]

Based on the web search results, here's what I found about PLUG and ACL 2024 cross-lingual instruction generation:

## PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning

PLUG (Pivot Language gUided Generation) is a method for cross-lingual instruction tuning of large language models (LLMs). The paper was published at the 62nd Annual Meeting of the Association for Computational Linguistics (ACL) in August 2024 in Bangkok, Thailand.

### How PLUG Works

PLUG utilizes a high-resource language as the pivot to enhance instruction tuning in low-resource languages by training the model to first process the instruction and draft a response in the pivot language, before producing the final response in the target language.

### Key Results

The approach demonstrates a significant improvement in the instruction-following abilities of LLMs by 29% on average, compared to directly responding in the target language alone. PLUG significantly improved the instruction-following abilities of LLMs in multiple target languages including Chinese, Korean, Italian, and Spanish.

### Authors and Resources

The paper was authored by Zhihan Zhang, Dong-Ho Lee, Yuwei Fang, Wenhao Yu, Mengzhao Jia, Meng Jiang, and Francesco Barbieri in 2024. Code and data are available at https://github.com/ytyz1307zzh/PLUG.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10e6b4c6-145f-46b8-ae88-92590716c178",
  "isSidechain": true,
  "promptId": "d908c3c3-c203-4310-b121-66c8213aac0a",
  "agentId": "a23571b3019c9aac5",
  "type": "user",
  "uuid": "707d8f36-a258-4a1b-bde3-0c8ac283b530",
  "sourceToolAssistantUUID": "10e6b4c6-145f-46b8-ae88-92590716c178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T06:21:30.755Z_

<details><summary>↩ Tool result · `toolu_01LJLihMXn5QDBU5t9wWBK1N`</summary>

```text
Web search results for query: "Llama 4 vs Gemma vs Qwen multilingual 2026"

Links: [{"title":"Best Open-Source LLM in May 2026: Llama 4 vs Qwen 3.5 vs DeepSeek V4 vs Gemma 4 vs Mistral Medium 3.5","url":"https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/"},{"title":"Gemma 4 vs Qwen 3.5 vs Llama 4: Updated Benchmarks, New Leader — ai.rs","url":"https://ai.rs/ai-developer/gemma-4-vs-qwen-3-5-vs-llama-4-compared"},{"title":"Gemma 4 vs Llama 4 vs Qwen 3.5: 2026 Comparison Guide | Lushbinary","url":"https://lushbinary.com/blog/gemma-4-vs-llama-4-vs-qwen-3-5-open-weight-model-comparison/"},{"title":"Llama 4 vs Qwen 3.5 vs Gemma 3: Which Open Model Should You Deploy? — ai.rs","url":"https://ai.rs/ai-developer/llama-4-vs-qwen-3-5-vs-gemma-3-compared"},{"title":"Open-Source LLM Landscape 2026: DeepSeek V4 vs Llama 4 vs Qwen 3.5 vs Gemma 4","url":"https://codersera.com/blog/open-source-llms-landscape-2026/"},{"title":"Open Source LLM Comparison Table (2026) | ComputingForGeeks","url":"https://computingforgeeks.com/open-source-llm-comparison/"},{"title":"Gemma 4 vs Qwen 3.5 vs Llama 4: Which Open Model Should You Actually Use? (2026) - Botmonster Tech","url":"https://botmonster.com/posts/gemma-4-vs-qwen-3-5-vs-llama-4-open-model-comparison-2026/"},{"title":"Qwen 3.6 vs Gemma 4 vs Llama 4 vs GLM-5.1 vs DeepSeek V4 Comparison | Lushbinary","url":"https://lushbinary.com/blog/qwen-3-6-vs-gemma-4-llama-4-glm-5-1-deepseek-v4-open-source-comparison/"},{"title":"Gemma 4 Complete Developer Guide (2026): Variants, Benchmarks, Apache 2.0, Deployment","url":"https://codersera.com/blog/gemma-4-complete-guide-2026/"},{"title":"10 Best Open-Source LLM Models (2025 Updated): Llama 4, Qwen 3 and DeepSeek R1","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"}]

Based on the search results, here's a comprehensive comparison of Llama 4, Gemma 4, and Qwen in terms of multilingual capabilities in 2026:

## Multilingual Performance

For multilingual capabilities, especially CJK (Chinese, Japanese, Korean), Qwen 3.5 is the clear leader. Qwen 3.5 dominates multilingual with its 250K vocabulary and 201-language training data, giving it a decisive edge on non-English tasks.

Qwen 3.5 still holds the multilingual crown, and Llama 4 Scout still has the unmatched 10M context window. In specific language performance, for CJK languages especially, the gap is massive (87.8 vs 76.2 on Japanese) when comparing Qwen to other models.

## Regional Language Strengths

Qwen and Hunyuan dominate Chinese, Mistral Large 3 is strongest on European languages, and Llama 4 covers ~30 languages well.

## Overall Ranking for Multimodal Multilingual

The Qwen 3.5-Omni variant (released March 30) adds multimodal input across text, image, audio, and video - and is the only model in this comparison that can produce real-time streaming speech output.

## Summary

If multilingual support is your primary concern, if you're building a product that could scale past 700M MAU, or if you need to redistribute modified model weights without attribution requirements, Gemma 4 and Qwen 3.5 are the only options. Qwen 3.5 is specifically the strongest choice for multilingual applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "418e9f1c-d5ab-4cff-9922-732418bf5758",
  "isSidechain": true,
  "promptId": "d908c3c3-c203-4310-b121-66c8213aac0a",
  "agentId": "a23571b3019c9aac5",
  "type": "user",
  "uuid": "ae5ad80e-0922-4f2c-8e15-0cd065a6b7e1",
  "sourceToolAssistantUUID": "418e9f1c-d5ab-4cff-9922-732418bf5758",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T06:21:30.764Z_

<details><summary>↩ Tool result · `toolu_018X1LydBYgYUzGZmEHUCh2h`</summary>

```text
Web search results for query: "Multi-Linguistic LoRA Merging NeurIPS 2025"

Links: [{"title":"NeurIPS MLM: Multi-linguistic LoRA Merging","url":"https://neurips.cc/virtual/2025/126638"},{"title":"MLM: Multi-linguistic LoRA Merging | OpenReview","url":"https://openreview.net/forum?id=VAnFWVbYxG"},{"title":"MLM: Multi-linguistic LoRA Merging Jung Lee∗ Sogang University","url":"https://openreview.net/pdf/04e3cf10a12c54ba61f81437fa90b856b50b30cd.pdf"},{"title":"Awesome-Model-Merging-Methods-Theories-Applications/README.md at main · EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications","url":"https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications/blob/main/README.md"},{"title":"GitHub - EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications: Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities. ACM Computing Surveys, 2026. · GitHub","url":"https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications"},{"title":"Adaptive LoRA Merge with Parameter Pruning for Low- ...","url":"https://aclanthology.org/2025.findings-acl.990.pdf"},{"title":"NeurIPS 2025 Accepted Papers Overview | 南京大学大模型研究协同创新中心","url":"https://jerry-terrasse.github.io/lm_center_homepage/en/post/2025-10-11-neurips-2025-accepted-papers/"},{"title":"GitHub - apanariello4/core-space-merging: Pytorch code for NeurIPS 2025 paper \"Accurate and Efficient Low-Rank Model Merging in Core Space\"","url":"https://github.com/apanariello4/core-space-merging"},{"title":"K-Merge: Online Continual Merging of Adapters for On-device Large Language Models","url":"https://arxiv.org/html/2510.13537v1"},{"title":"I-Lora: Iterative Merging of Routing-Tuned Low-Rank Adapters for Multi-task Learning | OpenReview","url":"https://openreview.net/forum?id=CRkoMdDlFh"}]

I found relevant information about Multi-Linguistic LoRA Merging (MLM) and NeurIPS 2025. Here's what the search results show:

## Multi-Linguistic LoRA Merging (MLM) - NeurIPS 2025

Large Language Models (LLMs) often struggle to generalize across languages, exhibiting strong task performance in high-resource settings but substantial degradation in low-resource ones. This performance gap arises not only from task-specific data scarcity, but also from the language imbalance embedded in pre-training.

The proposed Multi-Linguistic LoRA Merging (MLM) is a modular fine-tuning framework that decouples task and language adaptation into two independently trained LoRA-based adapters: a Task Adapter (TA) trained on a high-resource language, and a Language Adapter (LA) trained on the target low-resource language while keeping both the TA and base model frozen.

The LA serves as a linguistic bridge, aligning language-specific representations to the task logic encoded in the TA. The two adapters are then combined through simple parameter-space interpolation, followed by a lightweight post-merging alignment stage to refine their interaction.

The paper was published on October 16, 2025 and presented at the NeurIPS 2025 ER Workshop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cdbb69d-a5ba-4dca-ab22-84760a57ecb3",
  "isSidechain": true,
  "promptId": "d908c3c3-c203-4310-b121-66c8213aac0a",
  "agentId": "a23571b3019c9aac5",
  "type": "user",
  "uuid": "b2093294-ea48-451d-9b7d-2d60a4ae446c",
  "sourceToolAssistantUUID": "0cdbb69d-a5ba-4dca-ab22-84760a57ecb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T06:21:31.343Z_

<details><summary>↩ Tool result · `toolu_011z8R4YPnUhYGr5SEp23kkd`</summary>

```text
Web search results for query: "Family Matters arXiv 2510.00810 Nordic Faroese languages"

Links: [{"title":"[2510.00810] Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese","url":"https://arxiv.org/abs/2510.00810"},{"title":"Family Matters: Language Transfer and Merging","url":"https://arxiv.org/pdf/2510.00810"},{"title":"Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese","url":"https://arxiv.org/html/2510.00810"},{"title":"(PDF) Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese","url":"https://www.researchgate.net/publication/396094893_Family_Matters_Language_Transfer_and_Merging_for_Adapting_Small_LLMs_to_Faroese"},{"title":"Multi-label Scandinavian Language Identification (SLIDE)","url":"https://arxiv.org/html/2502.06692"},{"title":"[2012.06431] Discriminating Between Similar Nordic Languages","url":"https://arxiv.org/abs/2012.06431"},{"title":"Discriminating Between Similar Nordic Languages - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv201206431H/abstract"},{"title":"[2304.08823] Transfer to a Low-Resource Language via Close Relatives: The Case Study on Faroese","url":"https://arxiv.org/abs/2304.08823"},{"title":"Faroese Language Revitalization and Its Support for Nationhood","url":"https://opensiuc.lib.siu.edu/cgi/viewcontent.cgi?article=1384&context=gs_rp"},{"title":"arXiv:2304.08823v1 [cs.CL] 18 Apr 2023","url":"https://arxiv.org/pdf/2304.08823"}]

Based on the web search results, I found the paper you're looking for. Here are the key details about arXiv paper 2510.00810:

## "Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese"

The paper investigates strategies for adapting small, efficient language models to Faroese, a low-resource North Germanic language.

**Research Approach:**
Starting from English-pretrained models, the authors apply continued pre-training on related Scandinavian languages -- individually or combined via model merging -- before fine-tuning on Faroese. They compare full fine-tuning with parameter-efficient adaptation via LoRA, assessing their effects on general language modeling performance, linguistic accuracy, and text comprehension.

**Key Contributions:**
To address the lack of existing Faroese evaluation resources, they construct two new minimal-pair probing benchmarks, one for linguistic acceptability and one for text comprehension, and complement them with human evaluations conducted by native Faroese linguists.

**Main Findings:**
Their results show that transfer from related languages is essential, but the optimal source language is task-dependent: Icelandic improves linguistic accuracy, while Danish boosts reading comprehension.

**Authors:** Jenny Kunz, Iben Nyholm Debess, and Annika Simonsen


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c19a856-c3c1-4c1a-bb7e-ed7023c179e4",
  "isSidechain": true,
  "promptId": "d908c3c3-c203-4310-b121-66c8213aac0a",
  "agentId": "a23571b3019c9aac5",
  "type": "user",
  "uuid": "1f55541e-5cee-4dd5-a5bb-512dae533438",
  "sourceToolAssistantUUID": "9c19a856-c3c1-4c1a-bb7e-ed7023c179e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T06:21:52.349Z_

Excellent! I've completed both tasks. Here are my findings:

## TASK 1: Best Open-Source LLMs for Multilingual Instruction Tuning in 2026

### Top Models for Multilingual Tasks

**1. Qwen 3.5 (Clear Leader for Multilingual)**
- Covers 200+ languages and dialects
- Outstanding multilingual vocabulary (250K) with 201-language training data
- Particularly strong on CJK languages (87.8 on Japanese vs competitors at 76.2)
- Performs competitively with frontier closed-source models like GPT-5.2 and Claude 4.5 Opus
- Available as Qwen 3.5-Omni multimodal variant

**2. Llama 4**
- Versions range from 16B to 128B parameters
- Highly performant on reasoning and multilingual tasks
- Covers approximately 30 languages well
- Unmatched 10M context window in Llama 4 Scout variant

**3. Gemma 4**
- Pretrained on 100+ languages
- Supports 30+ languages out of the box
- Good for multilingual applications
- Apache 2.0 license for easier redistribution

**4. Mistral Models (Mistral Large, Mistral Medium 3.5, Mixtral)**
- Strongest on European languages
- Remarkable efficiency and speed
- Strong multilingual capabilities
- Known for practical performance-to-size ratio

**5. DeepSeek Models**
- DeepSeek V4 and DeepSeek-MoE optimized for multilingual tasks
- DeepSeek-Coder strong for coding tasks across languages
- Showing promising results on recent benchmarks

### What Makes Them Good for Multilingual Tasks
- Diverse language family coverage during pretraining
- Large vocabulary size (especially Qwen's 250K)
- Parameter efficiency for deploying in resource-constrained environments
- Performance on low-resource language benchmarks
- Specific optimization for non-English instruction following

---

## TASK 2: Paper Reference Verification Results

### VERIFIED PAPERS (All Real)

**1. "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models"**
- arXiv ID: 2603.21036 ✓ CONFIRMED
- Published: March 22, 2026
- Focus: Cross-lingual transfer gaps for Kazakh and Mongolian
- Key finding: Consistent performance gap of 13.8-16.7pp between English and low-resource languages
- Author: Abdul-Salem Beibitkhan (North American University)

**2. "Cross-Lingual Optimization for Language Transfer in Large Language Models"**
- arXiv ID: 2505.14297 ✓ CONFIRMED
- Accepted to: ACL 2025
- Acronym: CLO (as stated)
- Key finding: With only 3,200 samples, CLO surpasses supervised fine-tuning with 6,400 samples
- Methodology: Modified Direct Preference Optimization for language preference alignment

**3. "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning"**
- Venue: ACL 2024 ✓ CONFIRMED
- Published: August 2024, Bangkok, Thailand
- Acronym: PLUG = Pivot Language gUided Generation
- Authors: Zhihan Zhang, Dong-Ho Lee, Yuwei Fang, Wenhao Yu, Mengzhao Jia, Meng Jiang, Francesco Barbieri
- Key result: 29% average improvement in instruction-following abilities
- Code available at: github.com/ytyz1307zzh/PLUG

**4. "Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese"**
- arXiv ID: 2510.00810 ✓ CONFIRMED
- Focus: Nordic languages (specifically Faroese)
- Key contribution: Two new minimal-pair probing benchmarks + human evaluations by native linguists
- Findings: Icelandic helps linguistic accuracy, Danish boosts reading comprehension
- Authors: Jenny Kunz, Iben Nyholm Debess, Annika Simonsen

**5. "Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology"**
- arXiv ID: 2505.13908 ✓ CONFIRMED
- Submitted: May 20, 2025
- Authors: Ajitesh Bankula and Praney Bankula
- Focus: How language family proximity and morphological similarity affect cross-lingual transfer

**6. "Multi-Linguistic LoRA Merging" (MLM)**
- Venue: NeurIPS 2025 ✓ CONFIRMED
- Presented at: NeurIPS 2025 ER Workshop
- Published: October 16, 2025
- Framework: Decouples task and language adaptation into Task Adapter + Language Adapter
- Available: OpenReview (openreview.net/forum?id=VAnFWVbYxG)

---

### Summary
All six papers you referenced are real and verifiable. The papers represent current research (2024-2025) on multilingual instruction tuning, covering cross-lingual transfer optimization, language family effects, low-resource language adaptation, and advanced merging techniques.

Sources:
- [The Best Open-Source LLMs in 2026](https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models)
- [Top 7 open source LLMs for 2026](https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/)
- [Best Open Source LLMs: Complete 2026 Guide | Contabo Blog](https://contabo.com/blog/open-source-llms/)
- [Top Open-Source LLMs 2026: The Best Models & Comparison](https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/)
- [The State-of-the-Art in Open-Source Large Language Models](https://medium.com/ai-simplified-in-plain-english/the-state-of-the-art-in-open-source-large-language-models-a-new-era-of-ai-innovation-9a379aad0a23)
- [Microsoft AI Releases Harrier-OSS-v1](https://www.marktechpost.com/2026/03/30/microsoft-ai-releases-harrier-oss-v1-a-new-family-of-multilingual-embedding-models-hitting-sota-on-multilingual-mteb-v2/)
- [Best Open-Source LLM in May 2026: Llama 4 vs Qwen 3.5 vs DeepSeek V4 vs Gemma 4](https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/)
- [Gemma 4 vs Qwen 3.5 vs Llama 4: Updated Benchmarks](https://ai.rs/ai-developer/gemma-4-vs-qwen-3-5-llama-4-compared)
- [Gemma 4 vs Llama 4 vs Qwen 3.5: 2026 Comparison Guide](https://lushbinary.com/blog/gemma-4-vs-llama-4-vs-qwen-3-5-open-weight-model-comparison/)
- [Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages](https://arxiv.org/abs/2603.21036)
- [Cross-Lingual Optimization for Language Transfer in Large Language Models](https://arxiv.org/abs/2505.14297)
- [PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning](https://aclanthology.org/2024.acl-long.379/)
- [Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese](https://arxiv.org/abs/2510.00810)
- [Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology](https://arxiv.org/abs/2505.13908)
- [NeurIPS MLM: Multi-linguistic LoRA Merging](https://neurips.cc/virtual/2025/126638)
- [MLM: Multi-linguistic LoRA Merging | OpenReview](https://openreview.net/forum?id=VAnFWVbYxG)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f55541e-5cee-4dd5-a5bb-512dae533438",
  "isSidechain": true,
  "agentId": "a23571b3019c9aac5",
  "requestId": "req_011CatQVhGqzwfV4iaEprvCY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3f31f79a-5acd-4bcd-b0b8-8c14ea78b2c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "76fd9581-a5a6-4fd0-92ff-790f6bb3810e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DaGrPqnJXdEQJBgnqDy9rg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1831,
      "cache_creation_input_tokens": 8074,
      "cache_read_input_tokens": 16891,
      "output_tokens": 2143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1831,
          "output_tokens": 2143,
          "cache_read_input_tokens": 16891,
          "cache_creation_input_tokens": 8074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8074,
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
