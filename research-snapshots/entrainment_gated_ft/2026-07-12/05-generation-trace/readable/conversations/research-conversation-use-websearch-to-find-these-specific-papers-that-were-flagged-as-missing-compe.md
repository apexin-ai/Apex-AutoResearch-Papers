# Research conversation: Use WebSearch to find these specific papers that were flagged as missing competitors in Round 2 review. For each, verify

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a13838bea955ec79f.jsonl`
- **Structured JSON:** [`9812c3636ed55fd1b650.json`](../../sessions/98/9812c3636ed55fd1b650.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-11T23:38:06.969Z_

Use WebSearch to find these specific papers that were flagged as missing competitors in Round 2 review. For each, verify existence and get key details:

1. "TTKV" OR "Temporal-Tiered KV Cache" 2026 — temporal tier based compression
2. "TRIM-KV" OR "Cache What Lasts" KV cache retention 2025 2026
3. "EpiCache" Apple episodic KV cache 2025
4. "RateQuant" rate-distortion KV cache quantization 2026
5. "Transactional Attention" structural anchor KV cache 2026
6. "Agent Memory Below the Prompt" persistent Q4 KV cache 2026

For each paper found, report: title, date, venue, whether it's real, and its key contribution. If a paper doesn't exist, say so clearly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "a13838bea955ec79f",
  "type": "user",
  "uuid": "a1368c14-5e21-48da-b2b7-241a5db5a792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-11T23:38:08.489Z_

I'll search for each of these papers to verify their existence and gather key details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1368c14-5e21-48da-b2b7-241a5db5a792",
  "isSidechain": true,
  "agentId": "a13838bea955ec79f",
  "requestId": "req_011CawfMKTiPbnUDf8dgaCH4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e95282a7-c610-4f1d-9364-6e0f41640df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M1JYMCiY5sF9m8z1W5Xrw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 629,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-11T23:38:08.740Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0194szyfWC3fhtaXzQQsPqAm`</summary>

```json
{
  "query": "TTKV Temporal-Tiered KV Cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e95282a7-c610-4f1d-9364-6e0f41640df3",
  "isSidechain": true,
  "agentId": "a13838bea955ec79f",
  "requestId": "req_011CawfMKTiPbnUDf8dgaCH4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bee86f98-97c6-48e5-96d1-4d46d50ee75e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M1JYMCiY5sF9m8z1W5Xrw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 629,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:38:08.925Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HPcXiKpg5RcTsm5egmmnbx`</summary>

```json
{
  "query": "TRIM-KV Cache What Lasts KV cache retention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bee86f98-97c6-48e5-96d1-4d46d50ee75e",
  "isSidechain": true,
  "agentId": "a13838bea955ec79f",
  "requestId": "req_011CawfMKTiPbnUDf8dgaCH4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "26805be3-3dd0-4a33-83ca-6fccfb731828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M1JYMCiY5sF9m8z1W5Xrw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 629,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-11T23:38:09.126Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ii3YtqhZUmrn5v6kMTQZX`</summary>

```json
{
  "query": "EpiCache Apple episodic KV cache 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26805be3-3dd0-4a33-83ca-6fccfb731828",
  "isSidechain": true,
  "agentId": "a13838bea955ec79f",
  "requestId": "req_011CawfMKTiPbnUDf8dgaCH4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a358003d-493f-4452-ad2e-85d2cc54db41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M1JYMCiY5sF9m8z1W5Xrw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 629,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-11T23:38:09.132Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WfY5Ajf2taf8hUsqnY8xEj`</summary>

```json
{
  "query": "RateQuant rate-distortion KV cache quantization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a358003d-493f-4452-ad2e-85d2cc54db41",
  "isSidechain": true,
  "agentId": "a13838bea955ec79f",
  "requestId": "req_011CawfMKTiPbnUDf8dgaCH4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3971585e-ee22-4c55-9b91-a5cba87a0f0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M1JYMCiY5sF9m8z1W5Xrw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 629,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-11T23:38:09.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XbvPmm39ecLPhi2aoexS4w`</summary>

```json
{
  "query": "Transactional Attention structural anchor KV cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3971585e-ee22-4c55-9b91-a5cba87a0f0c",
  "isSidechain": true,
  "agentId": "a13838bea955ec79f",
  "requestId": "req_011CawfMKTiPbnUDf8dgaCH4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e60955f1-6f97-45bb-8423-7bc744d9434a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M1JYMCiY5sF9m8z1W5Xrw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 629,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-11T23:38:09.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017xiGH4gsrbW74Uy7TiofkD`</summary>

```json
{
  "query": "Agent Memory Below the Prompt persistent Q4 KV cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e60955f1-6f97-45bb-8423-7bc744d9434a",
  "isSidechain": true,
  "agentId": "a13838bea955ec79f",
  "requestId": "req_011CawfMKTiPbnUDf8dgaCH4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9a1eadc2-9fe0-4589-96a9-a2eb513545e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M1JYMCiY5sF9m8z1W5Xrw5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 16153,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 629
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 629,
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

_source line 9 · 2026-05-11T23:38:17.380Z_

<details><summary>↩ Tool result · `toolu_0194szyfWC3fhtaXzQQsPqAm`</summary>

```text
Web search results for query: "TTKV Temporal-Tiered KV Cache 2026"

Links: [{"title":"TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference","url":"https://arxiv.org/html/2604.19769"},{"title":"[2604.19769] TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference","url":"https://arxiv.org/abs/2604.19769"},{"title":"Boosting LLM Performance with Tiered KV Cache on Google Kubernetes Engine | Google Cloud Blog","url":"https://cloud.google.com/blog/topics/developers-practitioners/boosting-llm-performance-with-tiered-kv-cache-on-google-kubernetes-engine"},{"title":"What is KV Cache? Efficient LLM Inference | Ultralytics","url":"https://www.ultralytics.com/glossary/kv-cache"},{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Modular: The Five Eras of KVCache","url":"https://www.modular.com/blog/the-five-eras-of-kvcache"},{"title":"KV-Cache in Transformer Models","url":"https://www.emergentmind.com/topics/kv-cache"},{"title":"🔥 Introducing TriAttention: A New KV Cache Compression Technique | by Mayur Jain | MLWorks | Apr, 2026 | Medium","url":"https://medium.com/mlworks/introducing-triattention-a-new-kv-cache-compression-technique-60d1215f5af2"},{"title":"Google’s TurboQuant Compression May Support Faster Inference, Same Accuracy on Less Capable Hardware - InfoQ","url":"https://www.infoq.com/news/2026/04/turboquant-compression-kv-cache/"}]

Based on the search results, here's what I found about TTKV (Temporal-Tiered KV Cache):

## Overview

TTKV is a new perspective on KV cache management inspired by human memory mechanisms. TTKV partitions the KV cache into temporal tiers with heterogeneous capacity and precision, and is realized through tier layout, tier content, and tier interaction.

## Key Design Features

Unlike existing approaches that treat all KV states as equally important over time, TTKV observes that recent context requires fast and precise access, while older context can be stored more compactly and retrieved with lower fidelity.

The framework addresses three core aspects:

Tier Layout decouples fast and slow memory using HBM and DRAM; Tier Content assigns more recent KV states to faster, higher-precision tiers based on temporal proximity; and Tier Interaction employs block-wise streaming attention to overlap communication and computation when accessing slow tiers.

## Performance Results

Experiments show that TTKV reduces cross-tier traffic by 5.94x on 128K-context tasks, achieving up to 76% latency reduction and 2x throughput improvement over strong baselines.

The paper was submitted on March 27, 2026 and is available on arXiv with authors including Gradwell Dzikanyanga and Weihao Yang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bee86f98-97c6-48e5-96d1-4d46d50ee75e",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "a13838bea955ec79f",
  "type": "user",
  "uuid": "452089f3-f876-4ba7-97aa-b607573bcfeb",
  "sourceToolAssistantUUID": "bee86f98-97c6-48e5-96d1-4d46d50ee75e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-11T23:38:17.729Z_

<details><summary>↩ Tool result · `toolu_01WfY5Ajf2taf8hUsqnY8xEj`</summary>

```text
Web search results for query: "RateQuant rate-distortion KV cache quantization 2026"

Links: [{"title":"[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/abs/2605.06675"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"Towards 10 Million Context Length LLM Inference with KV ...","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf"},{"title":"KV Cache Is Eating Your VRAM. Here’s How Google Fixed It With TurboQuant. | Towards Data Science","url":"https://towardsdatascience.com/kv-cache-is-eating-your-vram-heres-how-google-fixed-it-with-turboquant/"},{"title":"TurboQuant Explained: 3-Bit KV Cache at 6× Compression","url":"https://decodethefuture.org/en/turboquant-vector-quantization-kv-cache/"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"[Feature]: Add TurboQuant Support for KV Cache Quantization · Issue #38171 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/38171"},{"title":"TurboQuant: Redefining AI efficiency with extreme compression","url":"https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"},{"title":"Quantized KV Cache - vLLM","url":"https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/"}]

Based on the search results, here's what I found about RateQuant and KV cache quantization:

## RateQuant Overview

RateQuant fits a per-quantizer distortion model from a small calibration set, then solves the resulting bit-allocation problem in closed form via reverse waterfilling from rate-distortion theory.

## The Problem It Solves

Large language models cache all previously computed key-value (KV) pairs during generation, and this KV cache grows linearly with sequence length, making it a primary memory bottleneck for serving. Quantizing the KV cache to fewer bits reduces this cost, yet all current quantizers assign the same bit-width to every attention head, ignoring the large variation in head importance.

## Distortion Model Mismatch Challenge

A key innovation of RateQuant addresses a critical issue in mixed-precision KV cache quantization: Each quantizer follows a different distortion curve D(b)=alpha*beta^{-b}, and the decay rate beta varies from 3.6 to 5.3 across quantizer designs. Applying one quantizer's distortion model to another inverts the allocation order and makes performance worse than uniform quantization. This failure mode is called distortion model mismatch and RateQuant proposes to resolve it.

## Technical Approach

RateQuant operates at per-head granularity with closed-form allocation and supports arbitrary base quantizers through calibration.

The paper appears to be recent, with the arXiv preprint dated to about 3 weeks before today (May 2026), making it a 2026 contribution to the field of efficient LLM inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3971585e-ee22-4c55-9b91-a5cba87a0f0c",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "a13838bea955ec79f",
  "type": "user",
  "uuid": "37daaf26-0ccf-4cc9-96a2-626b843eb0db",
  "sourceToolAssistantUUID": "3971585e-ee22-4c55-9b91-a5cba87a0f0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-11T23:38:18.090Z_

<details><summary>↩ Tool result · `toolu_015ii3YtqhZUmrn5v6kMTQZX`</summary>

```text
Web search results for query: "EpiCache Apple episodic KV cache 2025"

Links: [{"title":"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/epicache"},{"title":"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://arxiv.org/html/2509.17396"},{"title":"GitHub - apple/ml-epicache","url":"https://github.com/apple/ml-epicache"},{"title":"EpiCache: Episodic KV Cache Management for Long ...","url":"https://arxiv.org/pdf/2509.17396"},{"title":"Paper page - EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://huggingface.co/papers/2509.17396"},{"title":"[2509.17396] EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://arxiv.org/abs/2509.17396"},{"title":"EpiCache: Episodic KV Cache for LongConvQA","url":"https://www.emergentmind.com/topics/epicache"},{"title":"Apple’s memory-saving AI breakthrough could save enterprises millions | VentureBeat","url":"https://venturebeat.com/ai/apples-memory-saving-ai-breakthrough-could-save-enterprises-millions"},{"title":"[Literature Review] EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://www.themoonlight.io/en/review/epicache-episodic-kv-cache-management-for-long-conversational-question-answering"},{"title":"(PDF) EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://www.researchgate.net/publication/395724682_EpiCache_Episodic_KV_Cache_Management_for_Long_Conversational_Question_Answering"}]

Based on the search results, here's what I found about EpiCache:

## Overview

EpiCache is a training-free KV cache management framework for long conversational question answering (LongConvQA) under fixed memory budgets. The research was published in February 2026 and focuses on addressing memory demands of the autoregressive Key-Value (KV) cache in Large Language Models.

## How It Works

EpiCache bounds cache growth through block-wise prefill and preserves topic-relevant context via episodic KV compression, which clusters conversation history into coherent episodes and applies episode-specific KV cache eviction. The framework further designs an adaptive layer-wise budget allocation strategy that measures each layer's sensitivity to eviction and distributes the memory budget across layers accordingly.

## Performance Results

Across three LongConvQA benchmarks, EpiCache improves accuracy by up to 40% over recent baselines, sustains near-full KV accuracy under 4-6x compression, and reduces latency and memory by up to 2.4x and 3.5x.

## Key Features

The framework is "training-free," meaning it can be applied to existing AI models without requiring them to be retrained — a significant advantage for practical deployment. The code is available at https://github.com/apple/ml-epicache.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a358003d-493f-4452-ad2e-85d2cc54db41",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "a13838bea955ec79f",
  "type": "user",
  "uuid": "ccff84ed-3d10-49c4-9c60-6616241b1fc4",
  "sourceToolAssistantUUID": "a358003d-493f-4452-ad2e-85d2cc54db41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:38:19.374Z_

<details><summary>↩ Tool result · `toolu_01XbvPmm39ecLPhi2aoexS4w`</summary>

```text
Web search results for query: "Transactional Attention structural anchor KV cache 2026"

Links: [{"title":"Transactional Attention: Semantic Sponsorship for KV-Cache Retention","url":"https://arxiv.org/html/2604.11288"},{"title":"[2604.11288] Transactional Attention: Semantic Sponsorship for KV-Cache Retention","url":"https://arxiv.org/abs/2604.11288"},{"title":"billparker.ai","url":"https://www.billparker.ai/2026/04/the-cache-is-thought-what-kv-caching.html"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"KV Caching & Attention Optimization: From O(n²) to O(n) | by pdawg | Medium","url":"https://medium.com/@prathamgrover777/kv-caching-attention-optimization-from-o-n%C2%B2-to-o-n-8b605f0d4072"},{"title":"The State of FP8 KV-Cache and Attention Quantization in vLLM | vLLM Blog","url":"https://vllm-project.github.io/2026/04/22/fp8-kvcache.html"},{"title":"Introduction to KV Cache Optimization Using Grouped Query Attention - PyImageSearch","url":"https://pyimagesearch.com/2025/10/06/introduction-to-kv-cache-optimization-using-grouped-query-attention/"},{"title":"DepCache: A KV Cache Management Framework for GraphRAG with Dependency Attention | Proceedings of the ACM on Management of Data","url":"https://dl.acm.org/doi/10.1145/3769778"},{"title":"KV Cache Explained: Efficient Attention for LLM Generation - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/kv-cache-transformer-attention-optimization"}]

Based on the search results, here's what I found about Transactional Attention, structural anchors, and KV cache:

## Transactional Attention Overview

Transactional Attention (TA) is a sponsorship mechanism in which structural anchor patterns (e.g., "key:", "password:"[REDACTED] protect adjacent value-bearing tokens from eviction.

## The Problem It Solves

The failure mode it addresses is dormant tokens: credentials, API keys, and configuration values that receive near-zero attention but become essential at generation time. Because these tokens lack the statistical signals that eviction policies rely on, no method based on attention scores, reconstruction loss, or learned retention gates retains them.

## Key Performance Results

TA achieves 100% credential retrieval at K=16 where six baselines (H2O, TOVA, SnapKV, StreamingLLM, PyramidKV, DynamicKV) achieve 0%, and sustains 100% accuracy across 200 function-calling trials.

## Efficient Variants

TA-Fast, an attention-free variant, reduces memory overhead by 52% and is compatible with SDPA and FlashAttention. TA is orthogonal to existing compression methods and adds less than 1% latency overhead.

## Distinction from Related Work

StructKV (Chen et al., 2026) is the closest concurrent work. It addresses tokens that appear "temporarily dormant" at one layer but serve as global information hubs across network depth, using Global In-Degree Centrality to aggregate cross-layer attention patterns. However, TA targets a fundamentally different dormancy: tokens that receive near-zero attention at all layers because nothing queries them yet. TA's structural sponsorship is the only mechanism that protects such tokens, because it operates on semantic patterns rather than attention signals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e60955f1-6f97-45bb-8423-7bc744d9434a",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "a13838bea955ec79f",
  "type": "user",
  "uuid": "7c11c5e9-1b5a-4432-8d9e-310c8a4a413d",
  "sourceToolAssistantUUID": "e60955f1-6f97-45bb-8423-7bc744d9434a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-11T23:38:21.117Z_

<details><summary>↩ Tool result · `toolu_01HPcXiKpg5RcTsm5egmmnbx`</summary>

```text
Web search results for query: "TRIM-KV Cache What Lasts KV cache retention 2025 2026"

Links: [{"title":"[2512.03324] Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/abs/2512.03324"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs | OpenReview","url":"https://openreview.net/forum?id=qCaq3jGb0S"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v2"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.03324v1"},{"title":"(PDF) Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://www.researchgate.net/publication/398312974_Cache_What_Lasts_Token_Retention_for_Memory-Bounded_KV_Cache_in_LLMs"},{"title":"TRIM-KV Cache Accepted to ICLR 2026","url":"https://www.linkedin.com/posts/shubham-sharma-8271b312a_cache-what-lasts-token-retention-for-memory-bounded-activity-7422296801816252417-0nQX"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"},{"title":"Caching and Reuse Optimizations","url":"https://www.aussieai.com/research/caching"},{"title":"GitHub - jjiantong/Awesome-KV-Cache-Optimization: [ACL 2026] Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization · GitHub","url":"https://github.com/jjiantong/Awesome-KV-Cache-Optimization"},{"title":"Introducing New KV Cache Reuse Optimizations in NVIDIA TensorRT-LLM | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/"}]

Based on the search results, here's what I found about TRIM-KV cache and KV cache retention:

## TRIM-KV: Cache What Lasts

TRIM-KV is a novel approach that learns each token's intrinsic importance at creation time via a lightweight retention gate. Each gate predicts a scalar retention score that decays over time, reflecting the long-term utility of the token for a specific layer and head. Tokens with low scores are evicted when the memory budget is exceeded, ensuring that the cache always contains the most critical tokens.

## The Problem It Addresses

Memory and computation remain core bottlenecks in long-horizon LLM inference due to the quadratic cost of self-attention and the ever-growing key-value (KV) cache. Existing strategies for memory-bounded inference, such as quantization, offloading, or heuristic KV eviction, either incur high orchestration costs or rely on unreliable attention-based proxies of importance.

## Training and Implementation

TRIM-KV is trained efficiently through distillation from a frozen LLM combined with a capacity loss, requiring only gate fine-tuning and adding negligible inference overhead.

## Performance Results

Across mathematical reasoning (GSM8K, MATH-500, AIME24), procedural generation (LongProc), conversational long-memory benchmarks (LongMemEval), and long-context understanding (LongBench and SCBench), TRIM-KV consistently outperforms strong eviction and learnable retrieval baselines, especially in low-memory regimes. Remarkably, it even surpasses full-cache models in some settings, showing that selective retention can serve as a form of regularization, suppressing noise from uninformative tokens.

Qualitative analyses further reveal that learned retention scores align with human intuition, naturally recovering heuristics such as sink tokens, sliding windows, and gist compression without explicit design.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26805be3-3dd0-4a33-83ca-6fccfb731828",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "a13838bea955ec79f",
  "type": "user",
  "uuid": "abad031f-07ea-4acd-b67d-49f8d70765e9",
  "sourceToolAssistantUUID": "26805be3-3dd0-4a33-83ca-6fccfb731828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T23:38:21.993Z_

<details><summary>↩ Tool result · `toolu_017xiGH4gsrbW74Uy7TiofkD`</summary>

```text
Web search results for query: "Agent Memory Below the Prompt persistent Q4 KV cache 2026"

Links: [{"title":"[2603.04428] Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/abs/2603.04428"},{"title":"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/html/2603.04428v1"},{"title":"GitHub - yshk-mxim/agent-memory: Persistent KV cache for multi-agent LLM systems on Apple Silicon · GitHub","url":"https://github.com/yshk-mxim/agent-memory"},{"title":"Persistent Q4 KV Cache for Multi-Agent LLM Inference on ...","url":"https://arxiv.org/pdf/2603.04428"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"Accelerating Inference - VAST Data","url":"https://www.vastdata.com/blog/accelerating-inference"},{"title":"Don’t Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks","url":"https://arxiv.org/html/2601.06007v1"},{"title":"How to save GPU memory in LLM serving: Principles and operating conditions of KV cache offloading","url":"https://www.backend.ai/blog/2026-04-how-to-save-gpu-memory-in-llm-serving-kv-cache-offloading"},{"title":"KVCache-Centric Memory for LLM Agents | OpenReview","url":"https://openreview.net/forum?id=YolJOZOGhI"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"}]

Based on the search results, here's what I found about "Agent Memory Below the Prompt: Persistent Q4 KV Cache 2026":

## Overview

This is a research paper titled "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices" that addresses a memory management problem in multi-agent LLM systems on edge devices, where device RAM is too small to hold every agent's KV cache simultaneously.

## The Problem

On Apple M4 Pro with 10.2 GB of cache budget, only 3 agents fit at 8K context in FP16. A 10-agent workflow must constantly evict and reload caches. Without persistence, every eviction forces a full re-prefill through the model—15.7 seconds per agent at 4K context.

## The Solution

The paper addresses this by persisting each agent's KV cache to disk in 4-bit quantized format and reloading it directly into the attention layer, eliminating redundant O(n) prefill computation via direct cache restoration.

## Performance Results

Cache restoration reduces time-to-first-token by up to 136x (Gemma: 22–136x at 4K–32K; DeepSeek: 11–76x at 4K–32K; Llama: 24–111x at 4K–16K; 3–10x at 1K). Additionally, Q4 quantization fits 4x more agent contexts into fixed device memory than FP16.

## Quality Impact

Perplexity measured with actual Q4 KV caches shows -0.7% for Gemma, +2.8% for Llama, and +3.0% for DeepSeek.

The paper was submitted on February 17, 2026 and is available as open-source on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a1eadc2-9fe0-4589-96a9-a2eb513545e2",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "a13838bea955ec79f",
  "type": "user",
  "uuid": "99325d71-0113-4407-a849-ea85dc3c7bd3",
  "sourceToolAssistantUUID": "9a1eadc2-9fe0-4589-96a9-a2eb513545e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-11T23:38:38.789Z_

Based on my comprehensive web search, here are the findings for each of the six papers flagged as missing competitors:

## Paper Verification Results

### 1. TTKV - Temporal-Tiered KV Cache
**Status: REAL** ✓
- **Title:** TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference
- **Date:** March 27, 2026 (arXiv submission)
- **Venue:** arXiv (2604.19769)
- **Key Contribution:** Partitions KV cache into temporal tiers with heterogeneous capacity and precision. Uses tier layout (HBM/DRAM separation), tier content (recent tokens in faster tiers), and tier interaction (block-wise streaming attention). Achieves 76% latency reduction and 2x throughput improvement over baselines on 128K contexts.
- **Source:** [arXiv abstract](https://arxiv.org/abs/2604.19769)

### 2. TRIM-KV - Cache What Lasts
**Status: REAL** ✓
- **Title:** Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs
- **Date:** December 2025 (arXiv 2512.03324) / Accepted to ICLR 2026
- **Venue:** arXiv, ICLR 2026
- **Key Contribution:** Learns each token's intrinsic importance via lightweight retention gates that predict scalar decay scores. Tokens with low scores are evicted when memory budgets are exceeded. Trained via distillation with negligible overhead. Outperforms baselines on mathematical reasoning, procedural generation, and long-context benchmarks.
- **Source:** [arXiv abstract](https://arxiv.org/abs/2512.03324)

### 3. EpiCache - Apple Episodic KV Cache
**Status: REAL** ✓
- **Title:** EpiCache: Episodic KV Cache Management for Long Conversational Question Answering
- **Date:** September 2025 (arXiv 2509.17396) / Published February 2026
- **Venue:** arXiv, Apple Machine Learning Research
- **Key Contribution:** Training-free framework that uses episodic KV compression (clustering conversation history into coherent episodes) and adaptive layer-wise budget allocation. Improves accuracy by up to 40% over baselines, sustains near-full KV accuracy under 4-6x compression, reduces latency/memory by up to 2.4x/3.5x.
- **Source:** [Apple ML Research](https://machinelearning.apple.com/research/epicache)

### 4. RateQuant - Rate-Distortion KV Cache Quantization
**Status: REAL** ✓
- **Title:** RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory
- **Date:** May 2026 (arXiv 2605.06675)
- **Venue:** arXiv
- **Key Contribution:** Applies rate-distortion theory with reverse waterfilling for optimal bit-allocation across attention heads. Addresses distortion model mismatch problem where different quantizers have different decay rates (β: 3.6-5.3). Operates at per-head granularity with closed-form allocation and calibration support for arbitrary base quantizers.
- **Source:** [arXiv abstract](https://arxiv.org/abs/2605.06675)

### 5. Transactional Attention - Structural Anchor KV Cache
**Status: REAL** ✓
- **Title:** Transactional Attention: Semantic Sponsorship for KV-Cache Retention
- **Date:** April 2026 (arXiv 2604.11288)
- **Venue:** arXiv
- **Key Contribution:** Sponsorship mechanism where structural anchor patterns (e.g., "key:", "password:"[REDACTED] protect dormant value-bearing tokens from eviction. Achieves 100% credential retrieval at K=16 where baselines (H2O, TOVA, SnapKV, StreamingLLM, PyramidKV, DynamicKV) achieve 0%. TA-Fast variant adds <1% latency overhead and is orthogonal to other compression methods.
- **Source:** [arXiv abstract](https://arxiv.org/abs/2604.11288)

### 6. Agent Memory Below the Prompt - Persistent Q4 KV Cache
**Status: REAL** ✓
- **Title:** Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices
- **Date:** February 17, 2026 (arXiv 2603.04428)
- **Venue:** arXiv
- **Key Contribution:** Persists quantized KV caches to disk and restores them directly into attention layers, eliminating redundant prefill computation. Reduces time-to-first-token by up to 136x (Gemma: 22-136x; DeepSeek: 11-76x; Llama: 24-111x depending on context length). Q4 quantization fits 4x more agent contexts into fixed device memory. Solves the constraint where only 3 agents fit simultaneously on M4 Pro.
- **Source:** [arXiv abstract](https://arxiv.org/abs/2603.04428)

## Summary

**All six papers are confirmed real and published in 2025-2026.** They address distinct KV cache challenges:
- **TTKV** → temporal tiering architecture
- **TRIM-KV** → learned token retention gates
- **EpiCache** → episodic compression for conversations
- **RateQuant** → mixed-precision quantization via rate-distortion
- **Transactional Attention** → structural anchor sponsorship for dormant tokens
- **Agent Memory Below the Prompt** → persistent Q4 quantized caching for edge multi-agent systems

All appear in top venues or high-quality preprint servers and represent substantive technical contributions to KV cache optimization, making them legitimate competitors for a Round 2 review context.

Sources:
- [TTKV arXiv](https://arxiv.org/abs/2604.19769)
- [TRIM-KV arXiv](https://arxiv.org/abs/2512.03324)
- [EpiCache Apple ML](https://machinelearning.apple.com/research/epicache)
- [RateQuant arXiv](https://arxiv.org/abs/2605.06675)
- [Transactional Attention arXiv](https://arxiv.org/abs/2604.11288)
- [Agent Memory Below the Prompt arXiv](https://arxiv.org/abs/2603.04428)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99325d71-0113-4407-a849-ea85dc3c7bd3",
  "isSidechain": true,
  "agentId": "a13838bea955ec79f",
  "requestId": "req_011CawfNRg3j2oZMdg1suc2b",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e16934db-ba48-42b3-bc17-1572a8b46191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WJXB8nSgTdk3xbuvgzEPLE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7246,
      "cache_read_input_tokens": 16782,
      "output_tokens": 1636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7246
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1636,
          "cache_read_input_tokens": 16782,
          "cache_creation_input_tokens": 7246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7246,
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
