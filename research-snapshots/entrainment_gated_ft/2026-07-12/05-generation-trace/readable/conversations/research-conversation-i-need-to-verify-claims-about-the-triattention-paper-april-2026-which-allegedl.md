# Research conversation: I need to verify claims about the "TriAttention" paper (April 2026) which allegedly proposes trigonometric KV compressio

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-adac2c0f526a268f5.jsonl`
- **Structured JSON:** [`96696074e9300c78b0ac.json`](../../sessions/96/96696074e9300c78b0ac.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-10T18:20:22.294Z_

I need to verify claims about the "TriAttention" paper (April 2026) which allegedly proposes trigonometric KV compression using pre-RoPE Q/K center norms and mean resultant length (MRL). Key claims to verify:
1. Does the paper exist? Search for "TriAttention trigonometric KV compression" and "TriAttention long reasoning"
2. Does it report ~90% of heads have MRL R > 0.95?
3. Does it achieve 2.5x throughput?
4. Is there an open-source implementation at github.com/WeianMao/triattention?
5. Does the scoring formula use precomputed E[q_f] centers (query-agnostic)?

Use WebSearch to find this paper. Try multiple queries:
- "TriAttention trigonometric KV compression 2026"
- "TriAttention efficient long reasoning"
- "site:arxiv.org TriAttention trigonometric attention"
- "WeianMao triattention github"

For any papers found, use WebFetch to read the abstract and key sections. Report exactly what you find - don't speculate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adac2c0f526a268f5",
  "type": "user",
  "uuid": "f31a8832-d009-4f6d-ab2b-37b6288f8cde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:20:22.298Z_

```json
{
  "parentUuid": "f31a8832-d009-4f6d-ab2b-37b6288f8cde",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
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
  "uuid": "7839250b-8e48-4fee-968e-2235db4e6f05",
  "timestamp": "2026-05-10T18:20:22.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:20:25.280Z_



I'll search for the "TriAttention" paper using multiple queries. Let me first load the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7839250b-8e48-4fee-968e-2235db4e6f05",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMK4d5crWehCo9C3vGk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4ec11a6-d439-420a-8847-08082e9e229f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8BZ5zeu75rvVxhWFvCzXJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 819,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 819,
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

_source line 4 · 2026-05-10T18:20:25.857Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WXDqb69Tf8jRnMFnsfewof`</summary>

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
  "parentUuid": "b4ec11a6-d439-420a-8847-08082e9e229f",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMK4d5crWehCo9C3vGk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54ddadc7-2110-4a6c-8db3-eeb51d16b061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8BZ5zeu75rvVxhWFvCzXJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 819,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 819,
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

_source line 5 · 2026-05-10T18:20:25.862Z_

<details><summary>↩ Tool result · `toolu_01WXDqb69Tf8jRnMFnsfewof`</summary>

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
  "parentUuid": "54ddadc7-2110-4a6c-8db3-eeb51d16b061",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adac2c0f526a268f5",
  "type": "user",
  "uuid": "0cd0631c-e59b-42e6-af21-f5ddf474e32d",
  "sourceToolAssistantUUID": "54ddadc7-2110-4a6c-8db3-eeb51d16b061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:20:28.749Z_



Now let me run all four search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cd0631c-e59b-42e6-af21-f5ddf474e32d",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMKLs8xW5g4GjYDnpC3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79e81682-f4ea-42cd-9d2f-26865faf3d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdaPEr3kv78RUgLJaJ3HpH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 7 · 2026-05-10T18:20:29.760Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uey1avbammQXd6wpzvhqmW`</summary>

```json
{
  "query": "TriAttention trigonometric KV compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79e81682-f4ea-42cd-9d2f-26865faf3d84",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMKLs8xW5g4GjYDnpC3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a18c636-d4f2-458c-9890-8a6bcedabc86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdaPEr3kv78RUgLJaJ3HpH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 8 · 2026-05-10T18:20:30.178Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NqoPFU5MckqHRzuEkei6JR`</summary>

```json
{
  "query": "TriAttention efficient long reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a18c636-d4f2-458c-9890-8a6bcedabc86",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMKLs8xW5g4GjYDnpC3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14c9d070-b57e-4d02-bca6-f224ae4ac40e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdaPEr3kv78RUgLJaJ3HpH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 9 · 2026-05-10T18:20:30.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018JYnmXW47T9zrS7bTmwVEC`</summary>

```json
{
  "query": "site:arxiv.org TriAttention trigonometric attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14c9d070-b57e-4d02-bca6-f224ae4ac40e",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMKLs8xW5g4GjYDnpC3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "484a4cd4-7329-4db2-8bd2-d278d286d05c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdaPEr3kv78RUgLJaJ3HpH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 10 · 2026-05-10T18:20:31.023Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RqaYGZ7wLdrZ7TyCfoafnM`</summary>

```json
{
  "query": "WeianMao triattention github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "484a4cd4-7329-4db2-8bd2-d278d286d05c",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMKLs8xW5g4GjYDnpC3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d830f252-199a-4544-8c6a-3457e285d991",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdaPEr3kv78RUgLJaJ3HpH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9042,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 9042,
          "cache_creation_input_tokens": 1919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1919,
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

_source line 11 · 2026-05-10T18:20:37.365Z_

<details><summary>↩ Tool result · `toolu_01Uey1avbammQXd6wpzvhqmW`</summary>

```text
Web search results for query: "TriAttention trigonometric KV compression 2026"

Links: [{"title":"GitHub - WeianMao/triattention: TriAttention — Efficient long reasoning with trigonometric KV cache compression. Enables OpenClaw local deployment on memory-constrained GPUs.","url":"https://github.com/WeianMao/triattention"},{"title":"[2604.04921] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921"},{"title":"Researchers from MIT, NVIDIA, and Zhejiang University Propose TriAttention: A KV Cache Compression Method That Matches Full Attention at 2.5× Higher Throughput - MarkTechPost","url":"https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/"},{"title":"Paper page - TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://huggingface.co/papers/2604.04921"},{"title":"🔥 Introducing TriAttention: A New KV Cache Compression Technique | by Mayur Jain | MLWorks | Apr, 2026 | Medium","url":"https://medium.com/mlworks/introducing-triattention-a-new-kv-cache-compression-technique-60d1215f5af2"},{"title":"TriAttention | Efficient KV Cache Compression for Long-Context Reasoning","url":"https://weianmao.github.io/tri-attention-project-page/"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV","url":"https://www.opentrain.ai/papers/triattention-efficient-long-reasoning-with-trigonometric-kv-compression--arxiv-2604.04921/"},{"title":"[2604.04921v1] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921v1"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/html/2604.04921v1"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression | alphaXiv","url":"https://www.alphaxiv.org/overview/2604.04921"}]

Based on the search results, here's information about TriAttention and trigonometric KV compression:

## Overview

TriAttention is a method for efficient long reasoning with trigonometric KV cache compression, addressing the severe KV cache memory bottlenecks that arise from extended reasoning in large language models.

## The Problem

Leading KV cache compression methods estimate KV importance using attention scores from recent post-RoPE queries, but queries rotate with position during RoPE, making representative queries very few and leading to poor top-key selection and unstable reasoning.

## The Solution

To avoid this issue, the approach turns to the pre-RoPE space, where Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions. This concentration causes queries to preferentially attend to keys at specific distances, with the centers determining which distances are preferred via a trigonometric series.

## Performance Results

TriAttention achieves 2.5x higher throughput on AIME25 long reasoning while matching Full Attention accuracy and 10.7x KV memory reduction with trigonometric frequency-domain compression. On MATH 500, it achieves 1,405 tokens per second against Full Attention's 223 tokens per second (6.3× speedup), and on AIME25 it achieves 563.5 tokens per second against 222.8 (2.5× speedup at matched accuracy).

## Recent Updates

As of April 2026, TriAttention now supports AR video generation with KV cache compression, has a community C/ggml port for llama.cpp (HIP/ROCm) for AMD GPUs, and experimental MLX and TurboQuant support for Apple Silicon.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a18c636-d4f2-458c-9890-8a6bcedabc86",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adac2c0f526a268f5",
  "type": "user",
  "uuid": "4998ae81-66f3-4b54-a8fb-a1e9bde58ab0",
  "sourceToolAssistantUUID": "4a18c636-d4f2-458c-9890-8a6bcedabc86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:20:38.277Z_

<details><summary>↩ Tool result · `toolu_01RqaYGZ7wLdrZ7TyCfoafnM`</summary>

```text
Web search results for query: "WeianMao triattention github"

Links: [{"title":"GitHub - WeianMao/triattention: TriAttention — Efficient long reasoning with trigonometric KV cache compression. Enables OpenClaw local deployment on memory-constrained GPUs.","url":"https://github.com/WeianMao/triattention"},{"title":"TriAttention | Efficient KV Cache Compression for Long-Context Reasoning","url":"https://weianmao.github.io/tri-attention-project-page/"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/html/2604.04921v1"},{"title":"triattention/docs/reproduction.md at main · WeianMao/triattention","url":"https://github.com/WeianMao/triattention/blob/main/docs/reproduction.md"},{"title":"triattention/docs/mlx.md at main · WeianMao/triattention","url":"https://github.com/WeianMao/triattention/blob/main/docs/mlx.md"},{"title":"triattention/setup.py at main · WeianMao/triattention","url":"https://github.com/WeianMao/triattention/blob/main/setup.py"},{"title":"WeianMao (WeianMao) · GitHub","url":"https://github.com/WeianMao"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV","url":"https://www.opentrain.ai/papers/triattention-efficient-long-reasoning-with-trigonometric-kv-compression--arxiv-2604.04921/"},{"title":"WeianMao (mao)","url":"https://huggingface.co/WeianMao"},{"title":"WeianMao/triattention — GitHub trending stats & insights","url":"https://trendshift.io/repositories/25771"}]

Based on the search results, here's what I found about WeianMao's TriAttention GitHub repository:

## TriAttention Overview

TriAttention achieves 2.5x higher throughput and 10.7x KV memory reduction on AIME25 while matching Full Attention accuracy. It is an efficient long reasoning method with trigonometric KV cache compression that enables OpenClaw local deployment on memory-constrained GPUs.

## Technical Approach

Pre-RoPE Q/K vectors in long reasoning models concentrate around fixed centers that determine distance preferences via a trigonometric series, and TriAttention scores keys using these centers and norms instead of requiring representative query selection, enabling accurate KV cache compression without the overhead of existing attention-based methods.

## Repository Details

The repository is located at: https://github.com/WeianMao/triattention

You can clone it with: `git clone https://github.com/WeianMao/triattention.git`

## Features

As of April 21, 2026, SGLang backend support was added — TriAttention now runs on SGLang in addition to vLLM. Additionally, experimental MLX and TurboQuant support for Apple Silicon (M1/M2/M3/M4) is available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d830f252-199a-4544-8c6a-3457e285d991",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adac2c0f526a268f5",
  "type": "user",
  "uuid": "97668a8a-b777-4dc8-8217-77101a6945ca",
  "sourceToolAssistantUUID": "d830f252-199a-4544-8c6a-3457e285d991",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:20:40.343Z_

<details><summary>↩ Tool result · `toolu_018JYnmXW47T9zrS7bTmwVEC`</summary>

```text
Web search results for query: "site:arxiv.org TriAttention trigonometric attention"

Links: [{"title":"[2604.04921] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/html/2604.04921v1"},{"title":"[2604.04921v1] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921v1"},{"title":"[2211.02899] Tri-Attention: Explicit Context-Aware Attention Mechanism for Natural Language Processing","url":"https://arxiv.org/abs/2211.02899"},{"title":"[2010.03045] Rotate to Attend: Convolutional Triplet Attention Module","url":"https://arxiv.org/abs/2010.03045"},{"title":"[2204.13767] Triformer: Triangular, Variable-Specific Attentions for Long Sequence Multivariate Time Series Forecasting--Full Version","url":"https://arxiv.org/abs/2204.13767"},{"title":"Achieving 3D Attention via Triplet Squeeze and Excitation Block","url":"https://arxiv.org/html/2505.05943v1"},{"title":"[2507.02754] Fast and Simplex: 2-Simplicial Attention in Triton","url":"https://arxiv.org/abs/2507.02754"},{"title":"Triangle Multiplication is All You Need for Biomolecular Structure Representations","url":"https://arxiv.org/html/2510.18870v1"},{"title":"[2505.05943] Achieving 3D Attention via Triplet Squeeze and Excitation Block","url":"https://arxiv.org/abs/2505.05943"}]

I found search results for TriAttention with trigonometric attention. Here's what I found:

## TriAttention: Efficient Long Reasoning with Trigonometric KV Compression

Extended reasoning in large language models (LLMs) creates severe KV cache memory bottlenecks. The research observes that Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions, and this concentration causes queries to preferentially attend to keys at specific distances, with the centers determining which distances are preferred via a trigonometric series.

Based on this, TriAttention is proposed to estimate key importance by leveraging these centers. Via the trigonometric series, the method uses the distance preference characterized by these centers to score keys according to their positions, and also leverages Q/K norms as an additional signal for importance estimation.

### Performance Results

On AIME25 with 32K-token generation, TriAttention matches Full Attention reasoning accuracy while achieving 2.5x higher throughput or 10.7x KV memory reduction, whereas leading baselines achieve only about half the accuracy at the same efficiency. TriAttention enables OpenClaw deployment on a single consumer GPU, where long context would otherwise cause out-of-memory with Full Attention.

The paper was published on arXiv on April 6, 2026, by Weian Mao and 7 other authors (arXiv ID: 2604.04921).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "484a4cd4-7329-4db2-8bd2-d278d286d05c",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adac2c0f526a268f5",
  "type": "user",
  "uuid": "4d87d9e7-ed05-409e-8a06-5759f683b200",
  "sourceToolAssistantUUID": "484a4cd4-7329-4db2-8bd2-d278d286d05c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:20:46.462Z_

<details><summary>↩ Tool result · `toolu_01NqoPFU5MckqHRzuEkei6JR`</summary>

```text
Web search results for query: "TriAttention efficient long reasoning"

Links: [{"title":"[2604.04921] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921"},{"title":"GitHub - WeianMao/triattention: TriAttention — Efficient long reasoning with trigonometric KV cache compression. Enables OpenClaw local deployment on memory-constrained GPUs.","url":"https://github.com/WeianMao/triattention"},{"title":"Paper page - TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://huggingface.co/papers/2604.04921"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/html/2604.04921v1"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV","url":"https://www.opentrain.ai/papers/triattention-efficient-long-reasoning-with-trigonometric-kv-compression--arxiv-2604.04921/"},{"title":"[2604.04921v1] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921v1"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression | alphaXiv","url":"https://www.alphaxiv.org/overview/2604.04921"},{"title":"TriAttention | Efficient KV Cache Compression for Long-Context Reasoning","url":"https://weianmao.github.io/tri-attention-project-page/"},{"title":"🔥 Introducing TriAttention: A New KV Cache Compression Technique | by Mayur Jain | MLWorks | Apr, 2026 | Medium","url":"https://medium.com/mlworks/introducing-triattention-a-new-kv-cache-compression-technique-60d1215f5af2"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression | Request PDF","url":"https://www.researchgate.net/publication/403562159_TriAttention_Efficient_Long_Reasoning_with_Trigonometric_KV_Compression"}]

Based on the search results, here's what I found about TriAttention:

## Overview

Extended reasoning in large language models (LLMs) creates severe KV cache memory bottlenecks. Leading KV cache compression methods estimate KV importance using attention scores from recent post-RoPE queries. However, queries rotate with position during RoPE, making representative queries very few, leading to poor top-key selection and unstable reasoning.

## The Core Innovation

TriAttention observes that Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions in the pre-RoPE space. This concentration causes queries to preferentially attend to keys at specific distances (e.g., nearest keys), with the centers determining which distances are preferred via a trigonometric series.

## Performance Results

On AIME25 with 32K-token generation, TriAttention matches Full Attention reasoning accuracy while achieving 2.5x higher throughput or 10.7x KV memory reduction, whereas leading baselines achieve only about half the accuracy at the same efficiency.

Additionally, at fixed memory budget, TriAttention nearly doubles the accuracy of R-KV on AIME25 (32.9% vs. 17.5%) and AIME24 (42.1% vs. 25.4%).

## Practical Applications

TriAttention enables OpenClaw deployment on a single consumer GPU, where long context would otherwise cause out-of-memory with Full Attention.

The paper was released in April 2026 and is available on arXiv, with an open-source implementation provided on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14c9d070-b57e-4d02-bca6-f224ae4ac40e",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adac2c0f526a268f5",
  "type": "user",
  "uuid": "bb43c661-39b6-4e78-95eb-1c25aa708868",
  "sourceToolAssistantUUID": "14c9d070-b57e-4d02-bca6-f224ae4ac40e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T18:20:49.925Z_

The paper clearly exists across multiple sources. Now let me fetch the arxiv abstract and the GitHub repo for more specific details about the claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb43c661-39b6-4e78-95eb-1c25aa708868",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMLrD1ypJEMj71uZPGN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8172dea1-a61c-474a-b215-abdc226fd8d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pqGwjyMF6p6mu9dexvnfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1684,
      "cache_creation_input_tokens": 2281,
      "cache_read_input_tokens": 10961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2281,
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

_source line 16 · 2026-05-10T18:20:53.360Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XsBErEu1bFDbmxMTadvcp9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.04921",
  "prompt": "Extract the full abstract, the list of authors, the submission date, and any mentions of: (1) mean resultant length (MRL) or R > 0.95, (2) 2.5x throughput, (3) pre-RoPE Q/K center norms, (4) E[q_f] or query-agnostic precomputed centers, (5) scoring formula details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8172dea1-a61c-474a-b215-abdc226fd8d3",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMLrD1ypJEMj71uZPGN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a41f98de-12cc-4359-935f-d2f07ce85e58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pqGwjyMF6p6mu9dexvnfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1684,
      "cache_creation_input_tokens": 2281,
      "cache_read_input_tokens": 10961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2281,
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

_source line 17 · 2026-05-10T18:20:55.676Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M812RctnVPJqMKSDC4pq5m`</summary>

```json
{
  "url": "https://github.com/WeianMao/triattention",
  "prompt": "Extract the full README content, including: repository description, installation instructions, key features listed, any mentions of MRL or mean resultant length, throughput numbers, and the scoring formula if described. Also note the number of stars, forks, and latest commit date if visible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a41f98de-12cc-4359-935f-d2f07ce85e58",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMLrD1ypJEMj71uZPGN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "539af0d7-5877-4fc6-9743-dcc6d2a837c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pqGwjyMF6p6mu9dexvnfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1684,
      "cache_creation_input_tokens": 2281,
      "cache_read_input_tokens": 10961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2281,
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

_source line 18 · 2026-05-10T18:20:58.917Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011uJ3YKP8kPw6TRDjbq5vhv`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.04921v1",
  "prompt": "Search this full paper for: (1) any mention of 'mean resultant length' or 'MRL' or 'R > 0.95' or 'R>0.95' or concentration statistics about heads, (2) the exact scoring formula used for key importance, (3) any mention of E[q_f] or precomputed query centers or query-agnostic scoring, (4) the 2.5x throughput claim and the exact experimental setup, (5) the ~90% of heads statistic. Extract exact quotes for each if found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "539af0d7-5877-4fc6-9743-dcc6d2a837c6",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMLrD1ypJEMj71uZPGN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b202345a-d3c0-4911-83be-48aa43050867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015pqGwjyMF6p6mu9dexvnfS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1684,
      "cache_creation_input_tokens": 2281,
      "cache_read_input_tokens": 10961,
      "output_tokens": 514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2281
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1684,
          "output_tokens": 514,
          "cache_read_input_tokens": 10961,
          "cache_creation_input_tokens": 2281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2281,
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

_source line 19 · 2026-05-10T18:21:01.216Z_

<details><summary>↩ Tool result · `toolu_01XsBErEu1bFDbmxMTadvcp9`</summary>

```text
# TriAttention Paper Extract

## Full Abstract
"Extended reasoning in large language models (LLMs) creates severe KV cache memory bottlenecks. Leading KV cache compression methods estimate KV importance using attention scores from recent post-RoPE queries. However, queries rotate with position during RoPE, making representative queries very few, leading to poor top-key selection and unstable reasoning. To avoid this issue, we turn to the pre-RoPE space, where we observe that Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions -- Q/K concentration. We show that this concentration causes queries to preferentially attend to keys at specific distances (e.g., nearest keys), with the centers determining which distances are preferred via a trigonometric series. Based on this, we propose TriAttention to estimate key importance by leveraging these centers. Via the trigonometric series, we use the distance preference characterized by these centers to score keys according to their positions, and also leverage Q/K norms as an additional signal for importance estimation. On AIME25 with 32K-token generation, TriAttention matches Full Attention reasoning accuracy while achieving 2.5x higher throughput or 10.7x KV memory reduction, whereas leading baselines achieve only about half the accuracy at the same efficiency. TriAttention enables OpenClaw deployment on a single consumer GPU, where long context would otherwise cause out-of-memory with Full Attention."

## Authors
Weian Mao, Xi Lin, Wei Huang, Yuxin Xie, Tianfu Fu, Bohan Zhuang, Song Han, Yukang Chen

## Submission Date
April 6, 2026

## Specific Mentions Found
1. **2.5x throughput**: Confirmed in abstract—"achieving 2.5x higher throughput"
2. **Pre-RoPE Q/K centers**: Confirmed—"highly concentrated around fixed non-zero centers"
3. **Trigonometric series**: Mentioned as mechanism for determining distance preferences

## Not Found in Provided Content
- Mean resultant length (MRL) or R > 0.95
- E[q_f] or query-agnostic precomputed centers
- Detailed scoring formula specifications
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a41f98de-12cc-4359-935f-d2f07ce85e58",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adac2c0f526a268f5",
  "type": "user",
  "uuid": "6aff80f8-d353-4142-abfa-0daf5d853cfc",
  "sourceToolAssistantUUID": "a41f98de-12cc-4359-935f-d2f07ce85e58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T18:21:05.647Z_

<details><summary>↩ Tool result · `toolu_01M812RctnVPJqMKSDC4pq5m`</summary>

````text
# TriAttention Repository Summary

## Repository Stats
- **Stars:** 703
- **Forks:** 57
- **License:** Apache 2.0

## Description
TriAttention enables efficient long reasoning through trigonometric KV cache compression, achieving "10.7x KV memory reduction" while maintaining accuracy on extended reasoning tasks.

## Key Features
- 2.5x throughput improvement on AIME25 benchmarks
- 10.7x KV cache compression ratio
- Compatible with OpenClaw for local GPU deployment
- Support for multiple inference backends (vLLM, SGLang)

## Installation
```bash
git clone https://github.com/WeianMao/triattention.git
cd triattention
pip install -e .
pip install flash-attn --no-build-isolation
```

## Supported Models
- Qwen3-8B
- DeepSeek-R1-Distill-Llama-8B
- DeepSeek-R1-Distill-Qwen-7B
- GPT-OSS-20B

## Performance Results (AIME25, KV Budget=2048)
| Model | Full Attention | TriAttention |
|-------|---|---|
| Qwen3-8B | 40.8% | 40.8% |
| DS-Llama-8B | 31.4% | 19.6% |

Throughput on MATH-500: "222.8 to 1405.2 tokens/sec (6.3x speedup)"

## Technical Approach
The method leverages pre-RoPE Q/K vector concentrations around fixed centers using trigonometric series for scoring, eliminating expensive representative query selection.

## Notable Updates
- SGLang backend integration (April 2026)
- MLX support for Apple Silicon (M1-M4)
- Community ports for AMD GPUs via llama.cpp
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "539af0d7-5877-4fc6-9743-dcc6d2a837c6",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adac2c0f526a268f5",
  "type": "user",
  "uuid": "8309b5a6-63dc-4f45-b954-e05972da5e7a",
  "sourceToolAssistantUUID": "539af0d7-5877-4fc6-9743-dcc6d2a837c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T18:21:06.345Z_

<details><summary>↩ Tool result · `toolu_011uJ3YKP8kPw6TRDjbq5vhv`</summary>

```text
# TriAttention Key Findings

## (1) Mean Resultant Length and Concentration Statistics

**MRL Definition & Prevalence:**
- "Mean Resultant Length R=‖𝔼[q]‖/𝔼[‖q‖], which measures how tightly vectors concentrate"
- "across all heads in Qwen3-8B, the vast majority exhibit R values approaching 1.0"
- "~90% of heads exhibiting R>0.95" appears in Section 3.3

**Architecture Validation:**
- For MLA architecture: "96.6% of MLA heads achieve R>0.95 (vs. 84.7% for GQA)" (Appendix I)

## (2) Key Importance Scoring Formula

The exact scoring function combines two components:

**Trigonometric Series Score:**
"S_trig(k,Δ)=∑_f ‖𝔼[q_f]‖⋅‖k_f‖⋅cos(ω_f Δ+ϕ_f)"

**Norm-Based Score:**
"S_norm(k)=∑_f(1−R_f)⋅𝔼[‖q_f‖]⋅‖k_f‖"

**Final Combined Score:**
"S(k,Δ)=S_trig(k,Δ)+S_norm(k)" with importance averaged as "S̃(k)=1/|𝒟| ∑_δ∈𝒟 S(k,Δ+δ)"

## (3) Query-Agnostic Scoring Using Precomputed Centers

The method uses "mean Q and K vectors from a calibration dataset in the pre-RoPE space" to compute 𝔼[q_f] offline, enabling scoring without actual query observation.

## (4) Throughput Claims & Experimental Setup

**2.5× Throughput Claim:**
"At equivalent accuracy to Full Attention (40.8%), TriAttention achieves 2.5× higher throughput" on AIME25 (Table 4)

**Setup:** Single A100 80GB GPU, bfloat16 precision, maximum 16K decoding length, default KV budget 2048 tokens

## (5) Head Concentration Statistics

The paper states concentration "remains stable across positions and contexts" with approximately 90% of heads showing R>0.95 across multiple models (Qwen3, Qwen2.5, Llama3).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b202345a-d3c0-4911-83be-48aa43050867",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adac2c0f526a268f5",
  "type": "user",
  "uuid": "30e806b0-c061-43f9-af49-daff10d76a9b",
  "sourceToolAssistantUUID": "b202345a-d3c0-4911-83be-48aa43050867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T18:21:09.516Z_

Now let me also fetch the project page to see if there are any additional details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30e806b0-c061-43f9-af49-daff10d76a9b",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMNKiWo4XyW2efYMfAj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17dbaa1c-129a-4946-8107-666cce0dd27e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNUrX9Vmm6dR1atnDPLy15",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3963,
      "cache_read_input_tokens": 13242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3963,
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

_source line 23 · 2026-05-10T18:21:11.361Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XrJSEdFMZhcca5v6Kt58gc`</summary>

```json
{
  "url": "https://weianmao.github.io/tri-attention-project-page/",
  "prompt": "Extract any details about: the scoring formula, MRL statistics, throughput benchmarks, and the list of authors/affiliations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17dbaa1c-129a-4946-8107-666cce0dd27e",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMNKiWo4XyW2efYMfAj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7deaf3f1-5383-45af-8e19-541caeb0c70f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNUrX9Vmm6dR1atnDPLy15",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3963,
      "cache_read_input_tokens": 13242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3963,
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

_source line 24 · 2026-05-10T18:21:15.432Z_

<details><summary>↩ Tool result · `toolu_01XrJSEdFMZhcca5v6Kt58gc`</summary>

```text
# TriAttention: Key Details Summary

## Scoring Formula
TriAttention combines two components: a trigonometric series score (capturing distance preferences from Q/K centers) and a norm-based score (for heads with lower concentration). These are "balanced by Q/K concentration" using Mean Resultant Length (MRL) as the weighting mechanism.

## MRL Statistics
The paper shows "right-skewed distributions with means above 0.5" across attention heads in Qwen3, Qwen2.5, and Llama3 models, indicating consistent Q/K concentration. Additionally, "attention logits can be accurately reconstructed using a trigonometric series (Pearson r = 0.72)."

## Throughput Benchmarks
- AIME25: "2.5× higher throughput than Full Attention" at matched 40.8% accuracy
- MATH 500: "1,405 tokens/s vs. 223 tokens/s for Full Attention"
- Memory reduction: "10.7× KV cache memory reduction while matching Full Attention reasoning accuracy"

## Authors & Affiliations
**Authors:** Weian Mao, Xi Lin, Wei Huang, Yuxin Xie, Tianfu Fu, Bohan Zhuang, Song Han, Yukang Chen

**Affiliations:** MIT, NVIDIA, and Zhejiang University (ZJU)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7deaf3f1-5383-45af-8e19-541caeb0c70f",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adac2c0f526a268f5",
  "type": "user",
  "uuid": "94bda5f5-8fdd-4186-85dd-d6bbc0cd170b",
  "sourceToolAssistantUUID": "7deaf3f1-5383-45af-8e19-541caeb0c70f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-10T18:21:40.110Z_

I now have comprehensive information to verify all five claims. Here is my report:

---

## Verification Results for "TriAttention" Paper Claims

### Claim 1: Does the paper exist?
**CONFIRMED.** The paper exists and is published on arXiv as **arXiv:2604.04921**, submitted April 6, 2026. The full title is *"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression."* Authors are Weian Mao, Xi Lin, Wei Huang, Yuxin Xie, Tianfu Fu, Bohan Zhuang, Song Han, and Yukang Chen, affiliated with MIT, NVIDIA, and Zhejiang University. It has been covered by MarkTechPost, appeared on HuggingFace papers, alphaXiv, and ResearchGate.

### Claim 2: Does it report ~90% of heads have MRL R > 0.95?
**CONFIRMED.** The full HTML paper (Section 3.3) states that "~90% of heads exhibiting R > 0.95" across multiple models (Qwen3, Qwen2.5, Llama3). The MRL is defined as R = ||E[q]|| / E[||q||], measuring how tightly vectors concentrate. Appendix I further reports that for MLA architecture, 96.6% of MLA heads achieve R > 0.95 (vs. 84.7% for GQA).

### Claim 3: Does it achieve 2.5x throughput?
**CONFIRMED.** The abstract and Table 4 state: "At equivalent accuracy to Full Attention (40.8%), TriAttention achieves 2.5x higher throughput" on AIME25 with 32K-token generation. The experimental setup uses a single A100 80GB GPU with bfloat16 precision. On MATH-500, the speedup is even larger: 1,405 tokens/s vs. 223 tokens/s (6.3x). The paper also reports 10.7x KV memory reduction.

### Claim 4: Is there an open-source implementation at github.com/WeianMao/triattention?
**CONFIRMED.** The repository exists at [github.com/WeianMao/triattention](https://github.com/WeianMao/triattention) with 703 stars and 57 forks, Apache 2.0 license. It supports models including Qwen3-8B, DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-7B, and GPT-OSS-20B. It has vLLM and SGLang backend support, plus experimental MLX support for Apple Silicon and community ports for AMD GPUs via llama.cpp.

### Claim 5: Does the scoring formula use precomputed E[q_f] centers (query-agnostic)?
**CONFIRMED.** The paper explicitly describes using "mean Q and K vectors from a calibration dataset in the pre-RoPE space" to compute E[q_f] offline, enabling scoring without actual query observation (query-agnostic). The scoring formula has two components:

- **Trigonometric series score:** S_trig(k, Delta) = sum_f ||E[q_f]|| * ||k_f|| * cos(omega_f * Delta + phi_f)
- **Norm-based score:** S_norm(k) = sum_f (1 - R_f) * E[||q_f||] * ||k_f||
- **Combined:** S(k, Delta) = S_trig(k, Delta) + S_norm(k), with importance averaged over a set of offsets.

The E[q_f] centers are precomputed and fixed, making the scoring query-agnostic -- no representative query selection is needed at inference time.

---

**Summary: All five claims are verified as accurate** based on the arxiv paper, its full HTML version, the GitHub repository, and the project page.

Sources:
- [arXiv: TriAttention (2604.04921)](https://arxiv.org/abs/2604.04921)
- [Full HTML paper](https://arxiv.org/html/2604.04921v1)
- [GitHub: WeianMao/triattention](https://github.com/WeianMao/triattention)
- [Project Page](https://weianmao.github.io/tri-attention-project-page/)
- [HuggingFace Papers](https://huggingface.co/papers/2604.04921)
- [MarkTechPost Coverage](https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94bda5f5-8fdd-4186-85dd-d6bbc0cd170b",
  "isSidechain": true,
  "agentId": "adac2c0f526a268f5",
  "requestId": "req_011CauMNypiPcGobPvbxyAmy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44cdeacc-8331-436e-994b-f3c9f27418e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwCkj15wcxKj7iVYzBydyn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 17205,
      "output_tokens": 1192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 464
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1192,
          "cache_read_input_tokens": 17205,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 464,
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
