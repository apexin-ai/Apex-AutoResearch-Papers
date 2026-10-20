# Research conversation: Search the web thoroughly for the paper "TriAttention" about trigonometric KV compression for reasoning models. The pape

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a84e2b000404b8c85.jsonl`
- **Structured JSON:** [`71c628240e3921d907df.json`](../../sessions/71/71c628240e3921d907df.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-10T18:57:40.663Z_

Search the web thoroughly for the paper "TriAttention" about trigonometric KV compression for reasoning models. The paper is from approximately April 2026. I need to verify specific throughput claims:
1. Does it achieve 6.3x throughput on MATH-500 (specifically 1,405 vs 223 tokens/s)?
2. Does it achieve 2.5x throughput on AIME25?
3. Does it achieve 10.7x memory reduction?

Search using:
- "TriAttention KV compression reasoning" 
- "TriAttention trigonometric KV" site:arxiv.org
- "TriAttention MATH-500 throughput"
- "pre-RoPE Q/K concentration KV compression"

Use WebSearch and if you find the paper, use WebFetch to read the abstract and results sections. Report exactly what numbers the paper claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "699dd0ec-bb74-4292-8d77-12e196fbe5e0",
  "agentId": "a84e2b000404b8c85",
  "type": "user",
  "uuid": "d515f269-dd6f-4acd-bb2a-adb77c2b1b75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:57:40.668Z_

```json
{
  "parentUuid": "d515f269-dd6f-4acd-bb2a-adb77c2b1b75",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
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
  "uuid": "43125108-b8f9-4e4b-86b2-b5f1a0106573",
  "timestamp": "2026-05-10T18:57:40.668Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:57:43.418Z_



I'll search for this paper using multiple queries. Let me first load the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43125108-b8f9-4e4b-86b2-b5f1a0106573",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQA4h9QZNpfkwnC2MWj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42e303ef-260f-462a-95f1-d2df6ac24216",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BAv9JvBgZd6wHdBmDot4Wc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8979,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8979,
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

_source line 4 · 2026-05-10T18:57:43.777Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YXdAnWpEfosGJV2iW4PkMA`</summary>

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
  "parentUuid": "42e303ef-260f-462a-95f1-d2df6ac24216",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQA4h9QZNpfkwnC2MWj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc5d8b20-74aa-49a9-b442-ce061809dabe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BAv9JvBgZd6wHdBmDot4Wc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8979,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8979,
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

### Tool result

_source line 5 · 2026-05-10T18:57:43.782Z_

<details><summary>↩ Tool result · `toolu_01YXdAnWpEfosGJV2iW4PkMA`</summary>

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
  "parentUuid": "fc5d8b20-74aa-49a9-b442-ce061809dabe",
  "isSidechain": true,
  "promptId": "699dd0ec-bb74-4292-8d77-12e196fbe5e0",
  "agentId": "a84e2b000404b8c85",
  "type": "user",
  "uuid": "d06afb28-e1ce-4427-8a14-126c029b2216",
  "sourceToolAssistantUUID": "fc5d8b20-74aa-49a9-b442-ce061809dabe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:57:46.489Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d06afb28-e1ce-4427-8a14-126c029b2216",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQAJgXFGDk7yMfUUBAA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9a90b49-a889-4878-9bca-7bd01c7c837e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8cCEF13nYp8pCcEH7i4yk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8979,
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

_source line 7 · 2026-05-10T18:57:47.027Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GwrFxkChzUnUNrcTLJwrtN`</summary>

```json
{
  "query": "TriAttention KV compression reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9a90b49-a889-4878-9bca-7bd01c7c837e",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQAJgXFGDk7yMfUUBAA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68611b81-c811-473e-91f1-92657bf60b53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8cCEF13nYp8pCcEH7i4yk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8979,
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

_source line 8 · 2026-05-10T18:57:48.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LUjgM3CViXSL5aaCt4EzLw`</summary>

```json
{
  "query": "TriAttention trigonometric KV site:arxiv.org",
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
  "parentUuid": "68611b81-c811-473e-91f1-92657bf60b53",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQAJgXFGDk7yMfUUBAA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed042b8b-e0d6-4900-9af3-8dd14fe6995d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8cCEF13nYp8pCcEH7i4yk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8979,
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

_source line 9 · 2026-05-10T18:57:48.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FUGPVmFWnREGwtDzw2bwpt`</summary>

```json
{
  "query": "TriAttention MATH-500 throughput tokens/s"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed042b8b-e0d6-4900-9af3-8dd14fe6995d",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQAJgXFGDk7yMfUUBAA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb76ca4b-3388-48f2-87ea-4e51a5762bb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8cCEF13nYp8pCcEH7i4yk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8979,
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

_source line 10 · 2026-05-10T18:57:49.156Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KUuQf4V7QzcWNXd6yqQi3Z`</summary>

```json
{
  "query": "pre-RoPE Q/K concentration KV compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb76ca4b-3388-48f2-87ea-4e51a5762bb9",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQAJgXFGDk7yMfUUBAA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50191b3b-2b6c-4ecc-b01b-3a18f88deaa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8cCEF13nYp8pCcEH7i4yk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8979,
      "output_tokens": 244,
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
          "output_tokens": 244,
          "cache_read_input_tokens": 8979,
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

_source line 11 · 2026-05-10T18:57:51.757Z_

<details><summary>↩ Tool result · `toolu_01FUGPVmFWnREGwtDzw2bwpt`</summary>

```text
Web search results for query: "TriAttention MATH-500 throughput tokens/s"

Links: [{"title":"Researchers from MIT, NVIDIA, and Zhejiang University Propose TriAttention: A KV Cache Compression Method That Matches Full Attention at 2.5× Higher Throughput - MarkTechPost","url":"https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/"},{"title":"triattention/docs/mlx.md at main · WeianMao/triattention","url":"https://github.com/WeianMao/triattention/blob/main/docs/mlx.md"},{"title":"MATH-500 Benchmark Leaderboard | Artificial Analysis","url":"https://artificialanalysis.ai/evaluations/math-500"},{"title":"TriAttention KV Cache Compression: How to Stop Long AI Chats from Slowing Down and Speed Up Long-Context Reasoning","url":"https://www.intelligentliving.co/triattention-kv-cache-compression/"},{"title":"GitHub - AmesianX/TurboQuant: TurboQuant KV Cache Compression for llama.cpp — 5.2x memory reduction with near-lossless quality | Implementation of Google DeepMind's TurboQuant (ICLR 2026)","url":"https://github.com/AmesianX/TurboQuant"},{"title":"InferenceMAX™: Open Source Inference Benchmarking","url":"https://newsletter.semianalysis.com/p/inferencemax-open-source-inference"},{"title":"Pricing 101: Token Math & Cost-Per-Completion Explained","url":"https://deepinfra.com/blog/pricing-101-token-math-cost-per-completion"},{"title":"MATH 500","url":"https://www.vals.ai/benchmarks/math500"},{"title":"Provisioned throughput Foundation Model APIs | Databricks on AWS","url":"https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/prov-throughput-tokens"},{"title":"Measuring AI Model Performance: Tokens per Second, Model Sizes, and Inferencing Tools | OpenMetal IaaS","url":"https://openmetal.io/resources/blog/ai-model-performance-tokens-per-second/"}]

Based on the search results, TriAttention achieves 1,405 tokens per second on MATH 500 against Full Attention's 223 tokens per second, a 6.3× speedup.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb76ca4b-3388-48f2-87ea-4e51a5762bb9",
  "isSidechain": true,
  "promptId": "699dd0ec-bb74-4292-8d77-12e196fbe5e0",
  "agentId": "a84e2b000404b8c85",
  "type": "user",
  "uuid": "63e99b29-e1ad-4212-8053-9cbee210bc4f",
  "sourceToolAssistantUUID": "eb76ca4b-3388-48f2-87ea-4e51a5762bb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:57:53.942Z_

<details><summary>↩ Tool result · `toolu_01GwrFxkChzUnUNrcTLJwrtN`</summary>

```text
Web search results for query: "TriAttention KV compression reasoning 2026"

Links: [{"title":"[2604.04921] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921"},{"title":"GitHub - WeianMao/triattention: TriAttention — Efficient long reasoning with trigonometric KV cache compression. Enables OpenClaw local deployment on memory-constrained GPUs.","url":"https://github.com/WeianMao/triattention"},{"title":"Paper page - TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://huggingface.co/papers/2604.04921"},{"title":"Researchers from MIT, NVIDIA, and Zhejiang University Propose TriAttention: A KV Cache Compression Method That Matches Full Attention at 2.5× Higher Throughput - MarkTechPost","url":"https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/"},{"title":"🔥 Introducing TriAttention: A New KV Cache Compression Technique | by Mayur Jain | MLWorks | Apr, 2026 | Medium","url":"https://medium.com/mlworks/introducing-triattention-a-new-kv-cache-compression-technique-60d1215f5af2"},{"title":"[2604.04921v1] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921v1"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/html/2604.04921v1"},{"title":"TriAttention | Efficient KV Cache Compression for Long-Context Reasoning","url":"https://weianmao.github.io/tri-attention-project-page/"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://papers.fzhiy.net/papers/2604-04921.html"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV","url":"https://www.opentrain.ai/papers/triattention-efficient-long-reasoning-with-trigonometric-kv-compression--arxiv-2604.04921/"}]

Based on the search results, here's what I found about TriAttention KV compression for reasoning:

## Overview

TriAttention is a method submitted on April 6, 2026, that addresses KV cache memory bottlenecks in large language models during extended reasoning.

## The Problem

When models like DeepSeek-R1 or Qwen3 work through complex math problems, they can generate tens of thousands of tokens, and every token must be stored in the KV cache. For many deployment scenarios, especially on consumer hardware, this growth eventually exhausts GPU memory entirely.

## Key Innovation

TriAttention observes that Query and Key vectors are highly concentrated around fixed non-zero centers in pre-RoPE space and remain stable across positions. This concentration causes queries to preferentially attend to keys at specific distances, with the centers determining which distances are preferred via a trigonometric series.

TriAttention scores keys using these centers and norms instead of requiring representative query selection, enabling accurate KV cache compression without the overhead of existing attention-based methods.

## Performance Results

On the AIME25 mathematical reasoning benchmark with 32K-token generation, TriAttention matches Full Attention accuracy while achieving 2.5× higher throughput or 10.7× KV memory reduction. On LongBench, a 16-subtask benchmark covering question answering, summarization, few-shot classification, retrieval, counting, and code tasks, TriAttention achieves the highest average score of 48.1 among all compression methods at a 50% KV budget on Qwen3-8B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68611b81-c811-473e-91f1-92657bf60b53",
  "isSidechain": true,
  "promptId": "699dd0ec-bb74-4292-8d77-12e196fbe5e0",
  "agentId": "a84e2b000404b8c85",
  "type": "user",
  "uuid": "c1bfab75-f512-4eb9-a32f-61e563527bfd",
  "sourceToolAssistantUUID": "68611b81-c811-473e-91f1-92657bf60b53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:57:55.815Z_

<details><summary>↩ Tool result · `toolu_01LUjgM3CViXSL5aaCt4EzLw`</summary>

```text
Web search results for query: "TriAttention trigonometric KV site:arxiv.org"

Links: [{"title":"[2604.04921] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/html/2604.04921v1"},{"title":"[2604.04921v1] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921v1"},{"title":"LoL: Longer than Longer, Scaling Video Generation to Hour","url":"https://arxiv.org/html/2601.16914"},{"title":"The Anatomy of a Triton Attention Kernel","url":"https://arxiv.org/html/2511.11581v1"},{"title":"A Trident Quaternion Framework for Inertial-based Navigation Part...","url":"https://arxiv.org/abs/2102.12220"},{"title":"[2102.12217] A Trident Quaternion Framework for Inertial-based Navigation Part I: Rigid Motion Representation and Computation","url":"https://arxiv.org/abs/2102.12217"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"[0806.3481] The ancient Greeks present: Rational Trigonometry","url":"https://arxiv.org/abs/0806.3481"},{"title":"Trigonometric polynomials with frequencies in the set of cubes","url":"https://arxiv.org/html/2311.14937v2"}]

I found the paper you're searching for! Here are the key results:

## TriAttention: Efficient Long Reasoning with Trigonometric KV Compression

The paper addresses the problem of KV cache memory bottlenecks in large language models during extended reasoning. Leading KV cache compression methods estimate KV importance using attention scores from recent post-RoPE queries, but queries rotate with position during RoPE, making representative queries very few and leading to poor top-key selection and unstable reasoning.

The authors observe that Q and K vectors are highly concentrated around fixed non-zero centers in the pre-RoPE space and remain stable across positions. This concentration causes queries to preferentially attend to keys at specific distances, with the centers determining which distances are preferred via a trigonometric series.

TriAttention estimates key importance by leveraging these centers, using the trigonometric series to score keys according to their positions while also leveraging Q/K norms as an additional signal for importance estimation.

**Performance Results:**

On AIME25 with 32K-token generation, TriAttention matches Full Attention reasoning accuracy while achieving 2.5x higher throughput or 10.7x KV memory reduction, whereas leading baselines achieve only about half the accuracy at the same efficiency.

The paper was published on arXiv on April 6, 2026, by Weian Mao and 7 other authors. The code is available at https://github.com/WeianMao/triattention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed042b8b-e0d6-4900-9af3-8dd14fe6995d",
  "isSidechain": true,
  "promptId": "699dd0ec-bb74-4292-8d77-12e196fbe5e0",
  "agentId": "a84e2b000404b8c85",
  "type": "user",
  "uuid": "52a3b7a9-3859-48c3-bbc0-2750f66bad5b",
  "sourceToolAssistantUUID": "ed042b8b-e0d6-4900-9af3-8dd14fe6995d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:57:57.648Z_

<details><summary>↩ Tool result · `toolu_01KUuQf4V7QzcWNXd6yqQi3Z`</summary>

```text
Web search results for query: "pre-RoPE Q/K concentration KV compression 2026"

Links: [{"title":"Researchers from MIT, NVIDIA, and Zhejiang University Propose TriAttention: A KV Cache Compression Method That Matches Full Attention at 2.5× Higher Throughput - MarkTechPost","url":"https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/"},{"title":"turboquant/LANDSCAPE_2026.md at master · OnlyTerp/turboquant","url":"https://github.com/OnlyTerp/turboquant/blob/master/LANDSCAPE_2026.md"},{"title":"GitHub - AmesianX/TurboQuant: TurboQuant KV Cache Compression for llama.cpp — 5.2x memory reduction with near-lossless quality | Implementation of Google DeepMind's TurboQuant (ICLR 2026)","url":"https://github.com/AmesianX/TurboQuant"},{"title":"TriAttention | Efficient KV Cache Compression for Long-Context Reasoning","url":"https://weianmao.github.io/tri-attention-project-page/"},{"title":"Paper page - TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://huggingface.co/papers/2604.04921"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression: Analysis, Review & Summary | Paperium","url":"https://paperium.net/article/article/16602/triattention-efficient-long-reasoning-with-trigonometric-kv-compression"},{"title":"TriAttention: MIT and NVIDIA's 10.7x KV Cache Compression for LLM Reasoning • Dev|Journal","url":"https://earezki.com/ai-news/2026-04-11-researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-25-higher-throughput/"},{"title":"EliteKV: Scalable KV Cache Compression via RoPE Frequency Selection and Joint Low-Rank Projection","url":"https://arxiv.org/html/2503.01586"},{"title":"What Is KV Cache in LLMs? A 2026 Guide.","url":"https://www.buildfastwithai.com/blogs/kv-cache-llms-explained"}]

Based on the search results, here's what I found about pre-RoPE Q/K concentration and KV compression in 2026:

## Key Research: TriAttention

The key insight comes from looking at Query and Key vectors before RoPE rotation is applied — the pre-RoPE space. When visualized in this space, Q and K vectors cluster tightly around fixed, non-zero center points across the vast majority of attention heads and multiple model architectures.

## Q/K Concentration Definition

Q/K concentration is measured using the Mean Resultant Length R — a standard directional statistics measure where R → 1 means tight clustering and R → 0 means dispersion in all directions. On Qwen3-8B, approximately 90% of attention heads exhibit R > 0.95, meaning their pre-RoPE Q/K vectors are nearly perfectly concentrated around their respective centers.

## KV Compression Results

TriAttention achieves the highest average score of 48.1 among all compression methods at a 50% KV budget on Qwen3-8B on LongBench, winning 11 out of 16 subtasks and surpassing the next best baseline, Ada-KV+SnapKV, by 2.5 points. On AIME25 with 32K-token generation, TriAttention matches Full Attention reasoning accuracy while achieving 2.5× higher throughput or 10.7× KV memory reduction.

## Why Pre-RoPE Space Matters

RoPE rotation disperses these concentrated vectors into arc patterns that vary with position, but in pre-RoPE space, the centers remain fixed. This stability allows the method to work effectively for KV cache compression without the limitations of post-RoPE approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50191b3b-2b6c-4ecc-b01b-3a18f88deaa4",
  "isSidechain": true,
  "promptId": "699dd0ec-bb74-4292-8d77-12e196fbe5e0",
  "agentId": "a84e2b000404b8c85",
  "type": "user",
  "uuid": "959ccd28-20f5-457a-8c69-24e27fa7fdb8",
  "sourceToolAssistantUUID": "50191b3b-2b6c-4ecc-b01b-3a18f88deaa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T18:58:01.683Z_

The paper is clearly identified. Let me now fetch the actual arxiv paper and the project page to get the exact numbers you need verified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "959ccd28-20f5-457a-8c69-24e27fa7fdb8",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQBKKFaxbDzBXFq1NQz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba3950a8-15df-4100-9091-cab856788a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xwSpfULTVeHQPgAnj6e1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4066,
      "cache_read_input_tokens": 10892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4066,
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

_source line 16 · 2026-05-10T18:58:04.582Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NFUKvbPsTDjyPcD3NxkJhG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.04921",
  "prompt": "Extract the full abstract and any specific throughput numbers mentioned. I need exact numbers for: 1) MATH-500 throughput (tokens/s for TriAttention vs Full Attention), 2) AIME25 throughput multiplier, 3) memory reduction factor. Also extract any tables or figures that mention these benchmarks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba3950a8-15df-4100-9091-cab856788a36",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQBKKFaxbDzBXFq1NQz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6587792-9be3-4f0a-84d9-9d38893176ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xwSpfULTVeHQPgAnj6e1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4066,
      "cache_read_input_tokens": 10892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4066,
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

_source line 17 · 2026-05-10T18:58:05.845Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xbk1n9Ud9jrSg3bLVWZKze`</summary>

```json
{
  "url": "https://weianmao.github.io/tri-attention-project-page/",
  "prompt": "Extract all specific performance numbers, throughput claims, memory reduction claims, and benchmark results. I need exact numbers for MATH-500 throughput (tokens/s), AIME25 throughput, and memory reduction factors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6587792-9be3-4f0a-84d9-9d38893176ea",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQBKKFaxbDzBXFq1NQz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92ad4ecd-144c-4b4c-92ca-62f30308c85f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xwSpfULTVeHQPgAnj6e1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4066,
      "cache_read_input_tokens": 10892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4066,
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

_source line 18 · 2026-05-10T18:58:07.481Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0123hszWPHQnYvbbQKPdMitT`</summary>

```json
{
  "url": "https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/",
  "prompt": "Extract all specific performance numbers for TriAttention, especially: 1) MATH-500 throughput in tokens/s (TriAttention vs Full Attention), 2) AIME25 throughput multiplier, 3) memory reduction factor, 4) any other specific benchmark numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92ad4ecd-144c-4b4c-92ca-62f30308c85f",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQBKKFaxbDzBXFq1NQz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cc52a25-986a-4889-aaba-cc95b497b9f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xwSpfULTVeHQPgAnj6e1T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4066,
      "cache_read_input_tokens": 10892,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4066
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 10892,
          "cache_creation_input_tokens": 4066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4066,
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

_source line 19 · 2026-05-10T18:58:09.543Z_

<details><summary>↩ Tool result · `toolu_01Xbk1n9Ud9jrSg3bLVWZKze`</summary>

```text
# TriAttention Performance Metrics

## Throughput Claims
- **MATH 500**: TriAttention achieves "1,405 tokens/s vs. 223 tokens/s for Full Attention"
- **AIME25**: "2.5× higher throughput than Full Attention" at matched accuracy (40.8%)

## Memory Reduction
- **AIME25**: "10.7× KV cache memory reduction while matching Full Attention reasoning accuracy"

## Benchmark Results (KV Budget = 2048)

**AIME25 Performance:**
| Method | Qwen3-8B | DS-Llama | DS-Qwen | GPT-OSS |
|--------|----------|----------|---------|---------|
| Full Attention | 40.8% | 31.4% | 34.2% | 60.0% |
| TriAttention | 32.9% | 19.6% | 30.0% | 49.2% |

**AIME24 Performance:**
| Method | Qwen3-8B | DS-Llama | DS-Qwen | GPT-OSS |
|--------|----------|----------|---------|---------|
| Full Attention | 57.1% | 50.4% | 43.8% | 69.2% |
| TriAttention | 42.1% | 33.8% | 42.5% | 59.2% |

## Real-World Deployment
Running a 32B model on 24GB GPU: TriAttention enables task completion where "Full Attention hits out-of-memory before the agent can even start."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92ad4ecd-144c-4b4c-92ca-62f30308c85f",
  "isSidechain": true,
  "promptId": "699dd0ec-bb74-4292-8d77-12e196fbe5e0",
  "agentId": "a84e2b000404b8c85",
  "type": "user",
  "uuid": "16077aeb-ab95-46aa-8682-00062ef8a652",
  "sourceToolAssistantUUID": "92ad4ecd-144c-4b4c-92ca-62f30308c85f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T18:58:11.233Z_

<details><summary>↩ Tool result · `toolu_01NFUKvbPsTDjyPcD3NxkJhG`</summary>

```text
# TriAttention Paper Summary

## Full Abstract
"Extended reasoning in large language models (LLMs) creates severe KV cache memory bottlenecks. Leading KV cache compression methods estimate KV importance using attention scores from recent post-RoPE queries. However, queries rotate with position during RoPE, making representative queries very few, leading to poor top-key selection and unstable reasoning. To avoid this issue, we turn to the pre-RoPE space, where we observe that Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions -- Q/K concentration. We show that this concentration causes queries to preferentially attend to keys at specific distances (e.g., nearest keys), with the centers determining which distances are preferred via a trigonometric series. Based on this, we propose TriAttention to estimate key importance by leveraging these centers. Via the trigonometric series, we use the distance preference characterized by these centers to score keys according to their positions, and also leverage Q/K norms as an additional signal for importance estimation. On AIME25 with 32K-token generation, TriAttention matches Full Attention reasoning accuracy while achieving 2.5x higher throughput or 10.7x KV memory reduction, whereas leading baselines achieve only about half the accuracy at the same efficiency. TriAttention enables OpenClaw deployment on a single consumer GPU, where long context would otherwise cause out-of-memory with Full Attention."

## Specific Numbers Extracted

**AIME25 Performance:**
- Throughput multiplier: **2.5x higher**
- Memory reduction: **10.7x KV memory reduction**
- Context length: 32K tokens

**Note:** The abstract does not contain MATH-500 throughput comparisons or individual tokens/second measurements for either method. No tables or figures are present in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6587792-9be3-4f0a-84d9-9d38893176ea",
  "isSidechain": true,
  "promptId": "699dd0ec-bb74-4292-8d77-12e196fbe5e0",
  "agentId": "a84e2b000404b8c85",
  "type": "user",
  "uuid": "9b28a7c8-06e5-468f-a59a-e4aee93cd9de",
  "sourceToolAssistantUUID": "f6587792-9be3-4f0a-84d9-9d38893176ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T18:58:13.039Z_

<details><summary>↩ Tool result · `toolu_0123hszWPHQnYvbbQKPdMitT`</summary>

```text
# TriAttention Performance Numbers

## Throughput Metrics

**MATH-500:**
- TriAttention: 1,405 tokens/second
- Full Attention: 223 tokens/second
- Improvement: "6.3× speedup"

**AIME25:**
- TriAttention: 563.5 tokens/second
- Full Attention: 222.8 tokens/second
- Improvement: "2.5× speedup at matched accuracy"

## Memory Efficiency

- KV cache reduction: "10.7× KV memory reduction"
- Context length: 32K-token generation tasks

## Accuracy Benchmarks

**AIME25:** TriAttention achieved 32.9% accuracy versus R-KV's 17.5%

**MATH 500:** TriAttention reached 68.4% accuracy against Full Attention's 69.6% with only 1,024 tokens in KV cache

**LongBench (50% KV budget):** Average score of 48.1, winning 11 of 16 subtasks

**RULER retrieval:** Score of 66.1, a 10.5-point advantage over SnapKV

The research team notes TriAttention enables "a 32B reasoning model to run on a single 24GB RTX 4090" without memory exhaustion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cc52a25-986a-4889-aaba-cc95b497b9f2",
  "isSidechain": true,
  "promptId": "699dd0ec-bb74-4292-8d77-12e196fbe5e0",
  "agentId": "a84e2b000404b8c85",
  "type": "user",
  "uuid": "e9ac6f08-9799-4653-9723-c99011449dff",
  "sourceToolAssistantUUID": "6cc52a25-986a-4889-aaba-cc95b497b9f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T18:58:16.303Z_

Now let me also fetch the full HTML version of the paper to confirm these numbers directly from the source.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9ac6f08-9799-4653-9723-c99011449dff",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQCT4rXxH8PbRqoT3qF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1780508-ed52-4b45-986f-432a218ab708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGmfCq2MyJruU62DXyFFxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1799,
      "cache_read_input_tokens": 14958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1799,
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

_source line 23 · 2026-05-10T18:58:19.595Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AynS4NARrzdMcQqAHKeMjd`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.04921v1",
  "prompt": "Find and extract the exact throughput numbers for MATH-500 and AIME25 benchmarks. Specifically look for: 1) tokens/s values for TriAttention vs Full Attention on MATH-500 (looking for 1,405 vs 223), 2) throughput multiplier on AIME25 (looking for 2.5x), 3) memory reduction factor (looking for 10.7x). Also look for any tables reporting these metrics. Report the exact text/sentences containing these numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1780508-ed52-4b45-986f-432a218ab708",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQCT4rXxH8PbRqoT3qF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b696c532-fbe2-4790-8558-5047a0f82a43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGmfCq2MyJruU62DXyFFxp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1799,
      "cache_read_input_tokens": 14958,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1799
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 14958,
          "cache_creation_input_tokens": 1799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1799,
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

_source line 24 · 2026-05-10T18:58:23.814Z_

<details><summary>↩ Tool result · `toolu_01AynS4NARrzdMcQqAHKeMjd`</summary>

```text
# Throughput and Efficiency Metrics from TriAttention Paper

## MATH-500 Benchmark
The paper reports: **"1405.2 tokens/s"** for TriAttention versus **"222.8 tokens/s"** for Full Attention, achieving a **"6.3×"** speedup with comparable accuracy (68.4% vs 69.6%).

## AIME25 Benchmark
For AIME25 at matching accuracy: **"2.5× higher throughput"** is achieved by TriAttention compared to Full Attention.

## Memory Reduction
The paper states: **"10.7× KV memory reduction"** while matching Full Attention accuracy on AIME25.

## Source Table Reference
Table 4 explicitly displays these metrics: "At KV budgets achieving comparable accuracy to Full Attention, TriAttention shows significant throughput gains," listing throughput values of 1405.2 (TriAttention) versus 222.8 (Full Attention) on MATH 500, with a 6.3× speedup notation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b696c532-fbe2-4790-8558-5047a0f82a43",
  "isSidechain": true,
  "promptId": "699dd0ec-bb74-4292-8d77-12e196fbe5e0",
  "agentId": "a84e2b000404b8c85",
  "type": "user",
  "uuid": "c775e6af-9113-477f-951f-5c7266794861",
  "sourceToolAssistantUUID": "b696c532-fbe2-4790-8558-5047a0f82a43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-10T18:58:40.830Z_

I now have all the information needed to give you a definitive answer. Here are my findings:

---

## Verification Results for TriAttention (arXiv: 2604.04921)

**Paper:** "TriAttention: Efficient Long Reasoning with Trigonometric KV Compression"
**Published:** April 6, 2026 on arXiv
**Authors:** Weian Mao et al. (MIT, NVIDIA, Zhejiang University)

### Claim 1: 6.3x throughput on MATH-500 (1,405 vs 223 tokens/s)

**CONFIRMED with minor precision difference.** The paper reports in Table 4:
- TriAttention: **1,405.2 tokens/s**
- Full Attention: **222.8 tokens/s**
- Speedup: **6.3x**

Your figure of "223 tokens/s" for Full Attention is a rounding of the actual 222.8. The TriAttention figure of 1,405 is a rounding of 1,405.2. The 6.3x claim is accurate. Accuracy was nearly preserved: 68.4% (TriAttention) vs 69.6% (Full Attention).

### Claim 2: 2.5x throughput on AIME25

**CONFIRMED.** The abstract explicitly states: "TriAttention matches Full Attention reasoning accuracy while achieving 2.5x higher throughput." The MarkTechPost article further specifies the raw numbers as 563.5 tokens/s (TriAttention) vs 222.8 tokens/s (Full Attention) on AIME25, at matched accuracy of 40.8%.

### Claim 3: 10.7x memory reduction

**CONFIRMED.** The abstract states: "10.7x KV memory reduction" on AIME25 with 32K-token generation, while matching Full Attention reasoning accuracy.

### Additional context
- The 2.5x throughput and 10.7x memory reduction are reported as alternative operating points on AIME25 (not simultaneous) -- you can trade off between throughput and memory savings.
- Leading baselines (e.g., R-KV) achieved only about half the accuracy at the same efficiency levels.
- On LongBench at 50% KV budget, TriAttention scored 48.1 average across 16 subtasks, winning 11 of them.

---

Sources:
- [TriAttention on arXiv (abstract)](https://arxiv.org/abs/2604.04921)
- [TriAttention full HTML paper](https://arxiv.org/html/2604.04921v1)
- [TriAttention project page](https://weianmao.github.io/tri-attention-project-page/)
- [MarkTechPost article](https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/)
- [GitHub repository](https://github.com/WeianMao/triattention)
- [Hugging Face paper page](https://huggingface.co/papers/2604.04921)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c775e6af-9113-477f-951f-5c7266794861",
  "isSidechain": true,
  "agentId": "a84e2b000404b8c85",
  "requestId": "req_011CauQDF7J27KXcrnodzbU3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a83f7b3e-0227-4247-bc89-99d9605b8c30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd76f103-f390-4bf4-86a9-6bb0d8c21c0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrBLrXzb24jSv2JmnCu7Gm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 16757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 484,
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
