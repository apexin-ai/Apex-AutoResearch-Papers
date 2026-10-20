# Research conversation: I'm reviewing a research proposal about "PRM-Score-Gated KV Compression" for EMNLP 2026. The proposal claims novelty in 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a2c1b8ca350ac648f.jsonl`
- **Structured JSON:** [`54e025d081302f52b3fa.json`](../../sessions/54/54e025d081302f52b3fa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-09T20:41:29.367Z_

I'm reviewing a research proposal about "PRM-Score-Gated KV Compression" for EMNLP 2026. The proposal claims novelty in using Process Reward Model (PRM) scores as a cross-trajectory signal to allocate different KV cache quantization precision (FP16/INT8/INT4) to different search trajectories during inference-time tree search. No prior work allegedly uses PRM rank to set per-trajectory KV bit-width.

Please independently search for:

1. Search "speculative decoding KV cache quantization trajectory 2025 2026 arxiv" - any papers doing differential KV quantization per beam/trajectory?

2. Search "MCTS KV cache compression beam search quantization arxiv 2025" - any work on KV compression specifically for tree search/MCTS?

3. Search "reward model guided KV cache eviction arxiv 2025 2026" - any papers using reward signals to guide KV cache management?

4. Search "ForesightKV arxiv 2602.03203" - does this paper exist? Does it use RL/supervised learning for KV eviction as described?

5. Search "RLKV arxiv 2510.08525 KV cache RL" - does this paper exist? Is the description accurate (uses RL to find critical attention heads)?

6. Search "MixKVQ arxiv 2512.19206" - does this paper exist as described?

7. Search "inference time scaling memory efficiency 2026 arxiv" to find any concurrent papers in this area from early 2026.

8. Search paperswithcode.com for "KV cache quantization reasoning" to see the current SOTA landscape.

9. Fetch https://arxiv.org/abs/2604.04921 to verify TriAttention's existence and claims.

10. Search "DiffKV arxiv 2412.03131 KV compression" - does it exist as described?

Report everything you find with specific paper titles, arXiv IDs, venues, and what overlaps with the PSG-KVC proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "388a805f-5515-4e45-a980-58d4faca0bc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-09T20:41:30.651Z_

I'll conduct a comprehensive search for papers related to KV cache compression, quantization, and trajectory-based optimization. Let me start with these searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "388a805f-5515-4e45-a980-58d4faca0bc7",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseGHwAQA6kPePJjwfUS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5cef505-2dc2-4b21-b3d4-c8ac6890da51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KC5doa9xqFznw25BXaaQeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 910,
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

_source line 3 · 2026-05-09T20:41:31.158Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PBbfRbcchoTEYcSEBS61C4`</summary>

```json
{
  "query": "speculative decoding KV cache quantization trajectory 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5cef505-2dc2-4b21-b3d4-c8ac6890da51",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseGHwAQA6kPePJjwfUS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7178dde0-04dc-47cf-9935-b8b8d95e891a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KC5doa9xqFznw25BXaaQeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 910,
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

_source line 4 · 2026-05-09T20:41:31.419Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q3q5G6h5mnZAUZb1YGjsYh`</summary>

```json
{
  "query": "MCTS KV cache compression beam search quantization arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7178dde0-04dc-47cf-9935-b8b8d95e891a",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseGHwAQA6kPePJjwfUS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "08d2d7b9-f858-46d1-9a90-444b90e7a980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KC5doa9xqFznw25BXaaQeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 910,
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

_source line 5 · 2026-05-09T20:41:31.451Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GKSuXgP9teQpaev8U1W3xa`</summary>

```json
{
  "query": "reward model guided KV cache eviction arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08d2d7b9-f858-46d1-9a90-444b90e7a980",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseGHwAQA6kPePJjwfUS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe2add8a-514e-4e8b-9c71-d03dcab858cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KC5doa9xqFznw25BXaaQeM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 16155,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 304,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 910,
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

_source line 6 · 2026-05-09T20:41:31.460Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016mXKsWHv6wBomeo9rZwx5F`</summary>

```json
{
  "query": "ForesightKV arxiv 2602.03203"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe2add8a-514e-4e8b-9c71-d03dcab858cb",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseGHwAQA6kPePJjwfUS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8c71bd7a-4a9d-4274-be66-cd385389fb7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KC5doa9xqFznw25BXaaQeM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 16155,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 304,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 910,
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

_source line 7 · 2026-05-09T20:41:31.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N9arkuHTtVoamRthAC2rFM`</summary>

```json
{
  "query": "RLKV arxiv 2510.08525 KV cache RL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c71bd7a-4a9d-4274-be66-cd385389fb7c",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseGHwAQA6kPePJjwfUS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0406f7fa-373d-435f-a11e-a76efc54a1b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KC5doa9xqFznw25BXaaQeM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 16155,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 304,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 910,
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

_source line 8 · 2026-05-09T20:41:37.471Z_

<details><summary>↩ Tool result · `toolu_01Q3q5G6h5mnZAUZb1YGjsYh`</summary>

```text
Web search results for query: "MCTS KV cache compression beam search quantization arxiv 2025"

Links: [{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"},{"title":"CommVQ: Commutative Vector Quantization for KV Cache Compression","url":"https://arxiv.org/html/2506.18879v1"},{"title":"Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys","url":"https://arxiv.org/html/2603.14224v1"},{"title":"GPU-Accelerated INT8 Quantization for KV Cache Compression in Large Language Models","url":"https://arxiv.org/html/2601.04719v1"},{"title":"KVComp: A High-Performance, LLM-Aware, Lossy Compression Framework for KV Cache","url":"https://arxiv.org/html/2509.00579v1"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"[2604.15356] Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit","url":"https://arxiv.org/abs/2604.15356"},{"title":"[2510.11236] XQuant: Achieving Ultra-Low Bit KV Cache Quantization with Cross-Layer Compression","url":"https://arxiv.org/abs/2510.11236"},{"title":"1 Introduction","url":"https://arxiv.org/html/2503.24000v1"}]

I've found several recent arxiv papers related to KV cache compression and quantization. However, I notice that your query specifically mentions "MCTS" (Monte Carlo Tree Search) and "beam search" together with KV cache compression. The search results primarily contain papers on KV cache compression and quantization techniques, but don't seem to focus specifically on the combination with MCTS or beam search.

Here are the most relevant papers I found:

**KV Cache Compression & Quantization Papers (2025-2026):**

1. "Expected Attention" - a method that adopts insights for KV cache compression, with quantization methods that reduce precision used to store the cache

2. "eOptShrinkQ" - shows that KV cache admits decomposition into low-rank shared context and full-rank residual, using optimal singular value shrinkage and quantization

3. "CommVQ" - proposes Commutative Vector Quantization with additive quantization and lightweight encoder/codebook, reducing FP16 KV cache by 87.5% with 2-bit quantization

4. "Self-Indexing KVCache" - jointly optimizes dynamic sparsity and quantization, treating sparsity prediction as a top-k retrieval problem based on cosine similarity

If you're looking specifically for papers combining MCTS or beam search with KV cache compression, you may need to search more specifically for those combinations, as they don't appear prominently in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08d2d7b9-f858-46d1-9a90-444b90e7a980",
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "f233d8c5-2efb-4b25-b75b-eb1e00566148",
  "sourceToolAssistantUUID": "08d2d7b9-f858-46d1-9a90-444b90e7a980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-09T20:41:37.910Z_

<details><summary>↩ Tool result · `toolu_016mXKsWHv6wBomeo9rZwx5F`</summary>

```text
Web search results for query: "ForesightKV arxiv 2602.03203"

Links: [{"title":"[2602.03203] ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/abs/2602.03203"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203"},{"title":"[2603.03203] No Memorization, No Detection: Output Distribution-Based Contamination Detection in Small Language Models","url":"https://arxiv.org/abs/2603.03203"},{"title":"Convex optimization for non-equilibrium steady states on a hybrid quantum processor","url":"https://arxiv.org/html/2204.03203"},{"title":"[2504.03203] Behavior of the scaling correlation functions under severe subsampling","url":"https://arxiv.org/abs/2504.03203"},{"title":"[2601.03203] Counterfactual Fairness with Graph Uncertainty","url":"https://arxiv.org/abs/2601.03203"},{"title":"[2605.03203] A Partition-Based Generating Function for Row-Convex Polyominoes","url":"https://arxiv.org/abs/2605.03203"},{"title":"[2204.03203] Convex Optimization for Nonequilibrium Steady States on a Hybrid Quantum Processor","url":"https://arxiv.org/abs/2204.03203"},{"title":"[2602.12322v1] ForeAct: Steering Your VLA with Efficient Visual Foresight Planning","url":"https://arxiv.org/abs/2602.12322v1"},{"title":"A Partition-Based Generating Function for Row-Convex Polyominoes","url":"https://arxiv.org/html/2605.03203"}]

Based on the search results, here's what I found about ForesightKV (arxiv 2602.03203):

## Overview

ForesightKV is a training-based KV cache eviction framework that learns to predict which KV pairs to evict during long-text generations.

## Problem It Addresses

As sequence length grows, the key-value (KV) cache expands linearly, incurring significant memory and computation costs. Existing KV cache eviction methods mitigate this issue by discarding less important KV pairs, but often fail to capture complex KV dependencies, resulting in performance degradation.

## Key Technical Approach

The key idea is to train a lightweight scoring model that estimates the dynamic importance of each KV pair and guides eviction decisions. ForesightKV employs a two-stage training paradigm: supervised learning with constructed future importance labels, followed by reinforcement learning to refine eviction policies.

The framework formulates cache eviction as a Markov Decision Process and applies the GRPO algorithm to mitigate the significant language modeling loss increase on low-entropy tokens.

## Performance Results

Experiments on AIME2024 and AIME2025 benchmarks of three reasoning models demonstrate that ForesightKV consistently outperforms prior methods under only half the cache budget, while benefiting synergistically from both supervised and reinforcement learning approaches.

The paper was published on February 3, 2026, by authors including Zican Dong, Peiyu Liu, Junyi Li, and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c71bd7a-4a9d-4274-be66-cd385389fb7c",
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "fcea3fbe-d568-49c2-b76f-1e0fac9d6957",
  "sourceToolAssistantUUID": "8c71bd7a-4a9d-4274-be66-cd385389fb7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-09T20:41:38.845Z_

<details><summary>↩ Tool result · `toolu_01PBbfRbcchoTEYcSEBS61C4`</summary>

```text
Web search results for query: "speculative decoding KV cache quantization trajectory 2025 2026 arxiv"

Links: [{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache","url":"https://arxiv.org/html/2502.10424v1"},{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache | OpenReview","url":"https://openreview.net/forum?id=7SHbJENgHX"},{"title":"SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection","url":"https://arxiv.org/html/2605.02888"},{"title":"KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study","url":"https://arxiv.org/html/2603.27469v1"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"Speculative Decoding Meets Quantization: Compatibility Evaluation and Hierarchical Framework Design","url":"https://arxiv.org/html/2505.22179v1"},{"title":"arXiv:2503.24358v1 [cs.LG] 31 Mar 2025","url":"https://arxiv.org/pdf/2503.24358"},{"title":"Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://arxiv.org/html/2501.19392v1"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"}]

Based on the search results, here's what I found about speculative decoding, KV cache quantization, and recent developments in 2025-2026:

## Recent Key Papers and Trends

QuantSpec is a self-speculative decoding framework where the draft model shares the architecture of the target model but employs a hierarchical 4-bit quantized KV cache and 4-bit quantized weights for acceleration. QuantSpec maintains high acceptance rates (>90%) and reliably provides consistent end-to-end speedups up to ~2.5×.

A key insight emerging from recent research is that compression and speculation length are coupled, not independent—when the target model operates under aggressive compression (e.g., 4-bit quantization), its output distribution shifts, changing which speculation lengths are effective. SpecKV is the first system that adaptively selects the speculation length using signals from the draft model itself.

## Integration Challenges and Solutions

Recently, several studies have explored integrating quantization into self-speculative frameworks: QSpec drafts using 4-bit weights, QuantSpec drafts with 4-bit quantized weights and a 4-bit hierarchical KV cache, and ML-SpecQD employs the 4-bit version of the target model as the draft and introduces a smaller 4-bit model for multi-level speculative decoding.

The proposed quantization schemes are seamlessly compatible with model parallelism, offloading, speculative decoding, merging multiple sequences and other popular LLM inference techniques.

The field appears to be rapidly advancing in 2025-2026 with increased focus on combining speculative decoding strategies with advanced KV cache quantization techniques, particularly exploring hierarchical and adaptive quantization approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7178dde0-04dc-47cf-9935-b8b8d95e891a",
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "f6bef6e2-2df0-4583-8e21-de7560ade01f",
  "sourceToolAssistantUUID": "7178dde0-04dc-47cf-9935-b8b8d95e891a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-09T20:41:38.873Z_

<details><summary>↩ Tool result · `toolu_01N9arkuHTtVoamRthAC2rFM`</summary>

```text
Web search results for query: "RLKV arxiv 2510.08525 KV cache RL"

Links: [{"title":"[2510.08525] Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://arxiv.org/abs/2510.08525"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://arxiv.org/html/2510.08525"},{"title":"[PDF] Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Which-Heads-Matter-for-Reasoning-RL-Guided-KV-Cache-Du-Jiang/bb15d15655a41d12c714b3cd88c810ee5bb2886e"},{"title":"Paper page - Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://huggingface.co/papers/2510.08525"},{"title":"LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference","url":"https://arxiv.org/html/2510.09665v2"},{"title":"Learning to Evict from Key-Value Cache","url":"https://arxiv.org/html/2602.10238v1"},{"title":"[2510.09665] LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference","url":"https://arxiv.org/abs/2510.09665"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration","url":"https://arxiv.org/html/2505.24133v1"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"Make Your LVLM KV Cache More Lightweight","url":"https://arxiv.org/html/2605.00789"}]

I found the paper! Here's information about RLKV (arxiv 2510.08525):

## Overview

The paper is titled "Which Heads Matter for Reasoning? RL-Guided KV Cache Compression". 

## Key Contribution

RLKV uses reinforcement learning as a probe to discover which heads contribute to reasoning quality by directly optimizing their cache usage against actual generation outcomes.

## Problem Context

Reasoning large language models exhibit complex reasoning behaviors via extended chain-of-thought generation that are highly fragile to information loss during decoding, creating critical challenges for KV cache compression. Existing token-dropping methods directly disrupt reasoning chains by removing intermediate steps, while head-reallocation methods fail to preserve heads essential for generative reasoning.

## Methodology

The method uses learnable gating adapters that control the mixing of full attention and compressed local attention for each head, with L1 penalty encouraging sparsity. The method allocates full KV cache to reasoning-critical heads while aggressively compressing others.

## Results

RLKV achieves near-lossless reasoning with a 20-50% reduction in KV cache usage across diverse tasks and models, delivering a 1.09-1.21× end-to-end speedup in practice.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0406f7fa-373d-435f-a11e-a76efc54a1b4",
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "1f7aaa92-7c3c-4bc3-b047-9db2a2c4120a",
  "sourceToolAssistantUUID": "0406f7fa-373d-435f-a11e-a76efc54a1b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-09T20:41:40.247Z_

<details><summary>↩ Tool result · `toolu_01GKSuXgP9teQpaev8U1W3xa`</summary>

```text
Web search results for query: "reward model guided KV cache eviction arxiv 2025 2026"

Links: [{"title":"Learning to Evict from Key-Value Cache","url":"https://arxiv.org/html/2602.10238v1"},{"title":"Learning to Evict from Key-Value Cache | OpenReview","url":"https://openreview.net/forum?id=t7lJ2OEGbJ"},{"title":"[2603.10899] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899"},{"title":"[2603.10899v1] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899v1"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/html/2604.25975"},{"title":"[2602.10238] Learning to Evict from Key-Value Cache","url":"https://arxiv.org/abs/2602.10238"},{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by ...","url":"https://arxiv.org/pdf/2603.10899"}]

I found several relevant papers on reward model guided KV cache eviction from recent arxiv submissions. Here are the key findings:

## "Learning to Evict from Key-Value Cache" (2602.10238)

This paper reframes KV cache eviction as a reinforcement learning problem and introduces KV Policy (KVP), a framework of lightweight per-head RL agents trained on pre-computed generation traces using only key and value vectors. Each agent learns a specialized eviction policy guided by a holistic reward, derived from future utility, that evaluates the quality of the ranking across all cache budgets, requiring no modifications to the underlying LLM or additional inference.

Evaluated on the long-context benchmark RULER and the multi-turn dialogue benchmark OASST2-4k, KVP significantly outperforms baselines. Furthermore, zero-shot tests on standard downstream tasks indicate that KVP generalizes well beyond its training distribution.

## Other Related Work

The search also revealed additional recent approaches to KV cache eviction:

- **LookaheadKV** (2603.10899): A recent line of work proposes to improve eviction quality by "glimpsing into the future", in which a draft generator produces a surrogate future response approximating the target model's true response, and this surrogate is subsequently used to estimate the importance of cached KV more accurately. However, these approaches rely on computationally expensive draft generation, which introduces substantial prefilling overhead and limits their practicality in real-world deployment.

- **CapKV** (2604.25975): A formulation reveals that a wide range of existing eviction strategies can be interpreted as different approximations of the same capacity-maximization principle. CapKV is a capacity-aware eviction method that directly targets information preservation via a log-determinant approximation using statistical leverage scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe2add8a-514e-4e8b-9c71-d03dcab858cb",
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "0d46a022-0625-4607-96b9-f7780299bcca",
  "sourceToolAssistantUUID": "fe2add8a-514e-4e8b-9c71-d03dcab858cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-09T20:41:41.407Z_

Now let me continue with the remaining searches:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d46a022-0625-4607-96b9-f7780299bcca",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseH6R9UjZ1y1UFv6w1E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7204e0e-9879-4c72-b0df-7d0f0fe3bd9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0191jRUaPt7ocdWiKJEJwTN5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1715,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 17065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3783,
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

_source line 14 · 2026-05-09T20:41:41.887Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YVXdVp8Tvi67M2RswNgALy`</summary>

```json
{
  "query": "MixKVQ arxiv 2512.19206"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7204e0e-9879-4c72-b0df-7d0f0fe3bd9d",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseH6R9UjZ1y1UFv6w1E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3a09eb8b-a10e-43d9-99bd-5972fbce3150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0191jRUaPt7ocdWiKJEJwTN5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1715,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 17065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3783,
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

_source line 15 · 2026-05-09T20:41:42.627Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BMPZ4BPcLy2J6v6yg5vxF2`</summary>

```json
{
  "query": "inference time scaling memory efficiency 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a09eb8b-a10e-43d9-99bd-5972fbce3150",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseH6R9UjZ1y1UFv6w1E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2cb6fe94-0758-477f-a16e-75798bd22c53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0191jRUaPt7ocdWiKJEJwTN5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1715,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 17065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3783,
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

_source line 16 · 2026-05-09T20:41:43.121Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xxr4Z6VPQLWRE1tYUmaPf8`</summary>

```json
{
  "query": "DiffKV arxiv 2412.03131 KV compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cb6fe94-0758-477f-a16e-75798bd22c53",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseH6R9UjZ1y1UFv6w1E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "74c5add8-7e87-44d0-ba74-814a7119afb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0191jRUaPt7ocdWiKJEJwTN5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1715,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 17065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3783,
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

_source line 17 · 2026-05-09T20:41:43.288Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015EqVHDQPtmaoJtxofcPizL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.04921",
  "prompt": "What is TriAttention? Does it exist? What are its main claims and contributions to KV cache optimization or tree search?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74c5add8-7e87-44d0-ba74-814a7119afb3",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseH6R9UjZ1y1UFv6w1E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "590bc293-272e-4cd9-a740-7f28be1979df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0191jRUaPt7ocdWiKJEJwTN5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1715,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 17065,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3783
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1715,
          "output_tokens": 261,
          "cache_read_input_tokens": 17065,
          "cache_creation_input_tokens": 3783,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3783,
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

_source line 18 · 2026-05-09T20:41:48.552Z_

<details><summary>↩ Tool result · `toolu_015EqVHDQPtmaoJtxofcPizL`</summary>

```text
# TriAttention: Overview

**Does it exist?** Yes, TriAttention is a real research paper submitted to arXiv on April 6, 2026 (arXiv:2604.04921).

## Main Claims

TriAttention addresses KV cache memory bottlenecks in large language models during extended reasoning. The authors observe that "Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions," which they leverage for key importance estimation.

## Key Contributions

1. **Novel approach to KV compression**: Rather than using attention scores from recent post-RoPE queries, TriAttention operates in the pre-RoPE space where query-key vectors remain stable.

2. **Distance-based importance scoring**: The method uses trigonometric series derived from Q/K center vectors to score keys by position, determining which distances queries prefer to attend to.

3. **Significant efficiency gains**: On AIME25 with 32K-token generation, TriAttention achieves "2.5x higher throughput or 10.7x KV memory reduction" while maintaining full attention accuracy.

4. **Practical deployment benefits**: Enables running complex models like OpenClaw on consumer GPUs where memory would otherwise be exhausted.

The code is publicly available on GitHub, indicating this is an active, reproducible research contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "590bc293-272e-4cd9-a740-7f28be1979df",
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "ccd13916-b967-4f45-91a0-38e5f07b3f97",
  "sourceToolAssistantUUID": "590bc293-272e-4cd9-a740-7f28be1979df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-09T20:41:49.693Z_

<details><summary>↩ Tool result · `toolu_01YVXdVp8Tvi67M2RswNgALy`</summary>

```text
Web search results for query: "MixKVQ arxiv 2512.19206"

Links: [{"title":"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning","url":"https://arxiv.org/html/2512.19206"},{"title":"[2512.19206] MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning","url":"https://arxiv.org/abs/2512.19206"},{"title":"Machine Learning","url":"https://www.arxiv.org/list/cs.LG/recent?skip=149&show=250"},{"title":"[2506.19206] A Fast Bayesian Method for Coherent Gravitational Wave Searches with Relative Astrometry","url":"https://arxiv.org/abs/2506.19206"},{"title":"A Fast Bayesian Method for Coherent Gravitational Wave Searches with Relative Astrometry","url":"https://arxiv.org/html/2506.19206"},{"title":"NADER: Neural Architecture Design via Multi-Agent Collaboration","url":"https://arxiv.org/html/2412.19206"},{"title":"[2407.19206] Automorphisms of a family of surfaces with $p_g=q=2$ and $K^2=7$","url":"https://arxiv.org/abs/2407.19206"},{"title":"Abstract","url":"https://arxiv.org/html/2406.19206"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=43225&show=2000"},{"title":"Implementing Credit Risk Analysis with Quantum Singular Value Transformation","url":"https://arxiv.org/pdf/2507.19206"}]

Based on the search results, I found information about the paper arxiv 2512.19206:

## MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning

Long Chain-of-Thought (CoT) reasoning has significantly advanced the capabilities of Large Language Models (LLMs), but this progress is accompanied by substantial memory and latency overhead from the extensive Key-Value (KV) cache.

The paper proposes MixKVQ, a novel plug-and-play method that introduces a lightweight, query-aware algorithm to identify and preserve critical key channels that need higher precision, while applying per-token quantization for value cache.

The key insight is that an effective low-bit KV cache quantization strategy must consider two factors: a key channel's intrinsic quantization difficulty and its relevance to the query.

The authors conducted experiments on various models including Llama-3.1 and Qwen2.5 family, and their approach can achieve superior performance under different average bit widths in mathematical reasoning tasks AIME2024, AIME2025, math500, and gpqa.

The paper demonstrates that the approach significantly outperforms existing low-bit methods, achieving performance comparable to a full-precision baseline at a substantially reduced memory footprint.

The paper was published on December 22, 2025, and is authored by Tao Zhang, Ziqian Zeng, Hao Peng, Huiping Zhuang, and Cen Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a09eb8b-a10e-43d9-99bd-5972fbce3150",
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "2bd7c4d4-5ee4-444f-8d33-bad1dd8b0fec",
  "sourceToolAssistantUUID": "3a09eb8b-a10e-43d9-99bd-5972fbce3150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-09T20:41:50.885Z_

<details><summary>↩ Tool result · `toolu_01BMPZ4BPcLy2J6v6yg5vxF2`</summary>

```text
Web search results for query: "inference time scaling memory efficiency 2026 arxiv"

Links: [{"title":"Inference-Time Scaling for Complex Tasks: Where We Stand and What Lies Ahead","url":"https://arxiv.org/html/2504.00294v1"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"[2506.05345] Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/abs/2506.05345"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/html/2506.05345v1"},{"title":"[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314"},{"title":"Energy use of AI inference, efficiency pathways, and test-time scaling - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2542435126001145"},{"title":"Challenges and Research Directions for Large Language ...","url":"https://arxiv.org/pdf/2601.05047"},{"title":"1 Introduction","url":"https://arxiv.org/html/2605.02290v1"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"1 A Survey on Efficient Inference for Large Language Models","url":"https://arxiv.org/pdf/2404.14294"}]

Based on the search results, here are some recent 2026 arXiv papers on inference-time scaling and memory efficiency:

## Key Recent Papers

**1. Inference-Time Hyper-Scaling with KV Cache Compression** (June 2025)

In Transformer LLMs, generation cost is bottlenecked by the size of the key-value (KV) cache rather than the number of generated tokens. The paper explores inference-time hyper-scaling by compressing the KV cache to generate more tokens within the same compute budget and further improve the accuracy of scaled inference. 

The paper introduces Dynamic Memory Sparsification (DMS), which achieves 8x compression with only 1K training steps while maintaining better accuracy than training-free sparse attention. For instance, they enhance Qwen-R1 32B by 12.0 points on AIME 24, 8.6 on GPQA, and 9.7 on LiveCodeBench on average for an equivalent number of memory reads.

**2. Inference-Time Scaling for Complex Tasks** (March 2025)

There is high variability in token use across models with similar accuracies on a task, indicating space for improving token efficiency and that higher token consumption does not indicate higher accuracy across models.

**3. Energy-Efficient Test-Time Scaling** (Published recently in 2026)

In test-time scaling scenarios 15x longer than typical queries, the median energy rises 13x to 3.91 Wh. However, with efficiency interventions, the energy impact falls from 1.7 GWh/day to 0.8 GWh/day, mitigating the energy impact of test-time scaling.

These papers address critical challenges in making inference-time scaling practical by improving memory efficiency and energy consumption.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cb6fe94-0758-477f-a16e-75798bd22c53",
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "3ab7b630-5f32-42b8-873e-68d82bd30c66",
  "sourceToolAssistantUUID": "2cb6fe94-0758-477f-a16e-75798bd22c53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-09T20:41:51.375Z_

<details><summary>↩ Tool result · `toolu_01Xxr4Z6VPQLWRE1tYUmaPf8`</summary>

```text
Web search results for query: "DiffKV arxiv 2412.03131 KV compression"

Links: [{"title":"[2412.03131] DiffKV: Differentiated Memory Management for Large Language Models with Parallel KV Compaction","url":"https://arxiv.org/abs/2412.03131"},{"title":"DiffKV: Differentiated Memory Management for Large Language Models with Parallel KV Compaction","url":"https://arxiv.org/html/2412.03131"},{"title":"DiffKV: Differentiated Memory Management for Large Language Models with","url":"https://arxiv.org/pdf/2412.03131"},{"title":"Unifying KV Cache Compression for Large Language Models with LeanKV","url":"https://arxiv.org/html/2412.03131v2"},{"title":"Unifying KV Cache Compression for Large Language Models with ...","url":"https://ribbitribbit.co/paper/arxiv.2412.03131-Unifying-KV-Cache-Compression-for-Large-Language-Models"},{"title":"GitHub - zyqCSL/DiffKV","url":"https://github.com/zyqCSL/DiffKV"},{"title":"DiffKV: Differentiated Memory Management for Large Language Models with Parallel KV Compaction | Proceedings of the ACM SIGOPS 31st Symposium on Operating Systems Principles","url":"https://dl.acm.org/doi/10.1145/3731569.3764810"},{"title":"DiffKV: Differentiated Memory Management for Large ...","url":"https://dl.acm.org/doi/pdf/10.1145/3731569.3764810"},{"title":"KV Cache Sparsity","url":"https://www.aussieai.com/research/kv-cache-sparsity"},{"title":"Unifying KV Cache Compression for Large Language Models with LeanKV | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2412.03131"}]

Based on the search results, here's what I found about DiffKV (arxiv 2412.03131):

## Overview

DiffKV addresses the challenge that large language models (LLMs) face substantial serving costs due to their high memory demands, with the key-value (KV) cache being a primary bottleneck.

## Key Innovation

DiffKV is a novel framework for efficient KV cache compression that exploits three levels of differentiation in the KV cache: (1) the differing impact of keys and values on attention computation, (2) the varying importance of tokens, and (3) the diverse dynamic sparsity patterns across attention heads.

The three differentiation strategies are:

1. **Differentiated Keys and Values**: DiffKV assigns higher precision to key vectors than to value vectors, based on the observation that keys (critical for attention score computation) play a more significant role than values (used primarily for weighted aggregation) in attention computations.

2. **Token Importance Differentiation**: Guided by attention scores, DiffKV stores tokens at varying precision levels based on their significance. Most critical tokens are quantized at higher precision, less critical tokens are quantized at lower precision, and the least significant tokens are pruned.

3. **Per-head Dynamic Sparsity**: Attention score distributions exhibit dynamic sparsity across both heads and requests: the number of important tokens varies across different heads, and for the same head under different requests.

## Memory Management Solution

To address these challenges, DiffKV proposes an on-GPU memory manager that compacts fragmented free memory list into contiguous regions in parallel, effectively translating sparsity in the KV cache into performance gains.

## Performance Results

DiffKV is able to compress the KV cache by 2.7× to 5.7× with near-lossless accuracy on complex workloads requiring sophisticated reasoning and long-generation capabilities, and enhances throughput by 1.9× to 5.4×.

The paper was published in the ACM SIGOPS 31st Symposium on Operating Systems Principles, with code available on GitHub at zyqCSL/DiffKV.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74c5add8-7e87-44d0-ba74-814a7119afb3",
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "f54abc5b-b7fa-47ba-ab2d-7239b642fe09",
  "sourceToolAssistantUUID": "74c5add8-7e87-44d0-ba74-814a7119afb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-09T20:41:52.852Z_

Now let me search Papers with Code and complete the final search:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f54abc5b-b7fa-47ba-ab2d-7239b642fe09",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseHv1cEBxrZ4oSocofC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a32de137-1220-4dbe-8497-39868d7188d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2ap3tRcUu7XBPFcG9j6mG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 332,
      "cache_creation_input_tokens": 4850,
      "cache_read_input_tokens": 20848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4850,
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

_source line 23 · 2026-05-09T20:41:53.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YYQPw1UxK5Y6zeyWeesXHg`</summary>

```json
{
  "query": "site:paperswithcode.com KV cache quantization reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a32de137-1220-4dbe-8497-39868d7188d7",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseHv1cEBxrZ4oSocofC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "83e12897-cec5-4409-b6dc-aa1ae2bb9bcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C2ap3tRcUu7XBPFcG9j6mG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 332,
      "cache_creation_input_tokens": 4850,
      "cache_read_input_tokens": 20848,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4850
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 332,
          "output_tokens": 79,
          "cache_read_input_tokens": 20848,
          "cache_creation_input_tokens": 4850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4850,
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

_source line 24 · 2026-05-09T20:41:59.765Z_

<details><summary>↩ Tool result · `toolu_01YYQPw1UxK5Y6zeyWeesXHg`</summary>

```text
Web search results for query: "site:paperswithcode.com KV cache quantization reasoning"

Links: [{"title":"Papers with Code - KVTuner: Sensitivity-Aware Layer-wise Mixed Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference","url":"https://paperswithcode.com/paper/kvtuner-sensitivity-aware-layer-wise-mixed"},{"title":"RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations | Papers With Code","url":"https://paperswithcode.com/paper/rotatekv-accurate-and-robust-2-bit-kv-cache"},{"title":"Enabling 1-Bit Quantization of KV Cache with Layer-Wise ...","url":"https://paperswithcode.com/paper/asymkv-enabling-1-bit-quantization-of-kv"},{"title":"Plug-and-Play 1.x-Bit KV Cache Quantization for Video Large ...","url":"https://paperswithcode.com/paper/plug-and-play-1-x-bit-kv-cache-quantization"},{"title":"Paper page - No Token Left Behind: Reliable KV Cache Compression via Importance-Aware Mixed Precision Quantization","url":"https://paperswithcode.com/paper/no-token-left-behind-reliable-kv-cache"},{"title":"CalibQuant: 1-Bit KV Cache Quantization for Multimodal ...","url":"https://paperswithcode.com/paper/calibquant-1-bit-kv-cache-quantization-for"},{"title":"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification | Papers With Code","url":"https://paperswithcode.com/paper/zipcache-accurate-and-efficient-kv-cache"},{"title":"Papers with Code - Paper tables with annotated results for More for Keys, Less for Values: Adaptive KV Cache Quantization","url":"https://paperswithcode.com/paper/more-for-keys-less-for-values-adaptive-kv/review/"},{"title":"Papers with Code - Coleman Hooper","url":"https://paperswithcode.com/search?q=author:Coleman+Hooper"},{"title":"Paper page - Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time","url":"https://paperswithcode.com/paper/scissorhands-exploiting-the-persistence-of"}]

I found several relevant papers on Papers with Code about KV cache quantization with a focus on reasoning tasks. Here are the key results:

## Recent Work on KV Cache Quantization for Reasoning

**KVTuner** proposes a framework to adaptively search for optimal layer-wise KV quantization precision pairs, achieving nearly lossless 3.25-bit mixed precision KV cache quantization for LLMs like Llama-3.1-8B-Instruct and 4.0-bit for sensitive models like Qwen2.5-7B-Instruct on mathematical reasoning tasks.

The work analyzes the correlation of layer-wise transformer attention patterns to KV cache quantization errors and studies why key cache is more important than value cache for quantization error reduction.

## Other Notable Approaches

**RotateKV** achieves less than 0.3 perplexity degradation with 2-bit quantization on WikiText-2 using LLaMA-2-13B and maintains strong CoT reasoning capabilities with less than 1.7% degradation on GSM8K.

Recent research finds that preserving even a small amount of information in evicted KV pairs via reduced precision quantization substantially recovers performance degradation.

**Scissorhands** reduces memory usage of the KV cache during inference and can be combined with 4-bit quantization to achieve up to 20X compression.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83e12897-cec5-4409-b6dc-aa1ae2bb9bcc",
  "isSidechain": true,
  "promptId": "c660814f-c49a-4222-bac6-83983bee10f5",
  "agentId": "a2c1b8ca350ac648f",
  "type": "user",
  "uuid": "b948b69b-01a8-453f-8b7a-e78e55e8ce99",
  "sourceToolAssistantUUID": "83e12897-cec5-4409-b6dc-aa1ae2bb9bcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-09T20:42:32.971Z_

Perfect. Now let me compile a comprehensive report based on all my findings.

## Comprehensive Research Landscape Report: PRM-Score-Gated KV Compression

Based on my independent searches, here is what I found regarding the novelty claims of the "PRM-Score-Gated KV Compression" (PSG-KVC) proposal for EMNLP 2026:

---

## VERIFIED PAPERS

### 1. **ForesightKV** (arXiv:2602.03203) ✓ EXISTS
- **Title**: ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution
- **Status**: Real paper, published February 3, 2026
- **Key Approach**: Two-stage training using supervised learning (predicting future token importance) + RL refinement via GRPO algorithm
- **Scope**: Uses learned importance scoring to guide KV eviction during long-context reasoning
- **Overlap with PSG-KVC**: Uses reward-like signals (future utility) but trained via supervised learning + RL on a single trajectory, not cross-trajectory PRM scores in real-time tree search
- **Source**: [arXiv:2602.03203](https://arxiv.org/abs/2602.03203)

### 2. **RLKV** (arXiv:2510.08525) ✓ EXISTS
- **Title**: Which Heads Matter for Reasoning? RL-Guided KV Cache Compression
- **Status**: Real paper, submitted to venues (OpenReview listed)
- **Key Approach**: Uses RL with learnable gating adapters per attention head to discover reasoning-critical heads
- **Methodology**: Allocates full KV cache to reasoning-critical heads while aggressively compressing others via local attention
- **Results**: 20-50% KV cache reduction with 1.09-1.21× speedup
- **Overlap with PSG-KVC**: Uses RL to guide compression but at the **per-head level**, not per-trajectory with cross-trajectory PRM ranking. Does not use differential bit-width allocation (FP16/INT8/INT4) based on trajectory rewards
- **Source**: [arXiv:2510.08525](https://arxiv.org/abs/2510.08525)

### 3. **MixKVQ** (arXiv:2512.19206) ✓ EXISTS
- **Title**: MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning
- **Status**: Real paper, published December 22, 2025
- **Key Approach**: Query-aware algorithm to identify critical key channels that need higher precision vs. value cache quantization
- **Methodology**: Per-token quantization for values, mixed-precision for keys based on query relevance
- **Results**: Superior performance on AIME2024, AIME2025, math500, GPQA at multiple bit-widths
- **Overlap with PSG-KVC**: Uses mixed-precision quantization but it is **query-aware, not trajectory-aware or reward-model-guided**. No cross-trajectory ranking mechanism
- **Source**: [arXiv:2512.19206](https://arxiv.org/abs/2512.19206)

### 4. **DiffKV** (arXiv:2412.03131) ✓ EXISTS
- **Title**: DiffKV: Differentiated Memory Management for Large Language Models with Parallel KV Compaction
- **Status**: Real paper, published in ACM SIGOPS 31st Symposium on Operating Systems Principles
- **Key Approach**: Three-level differentiation: (1) keys vs. values, (2) token importance, (3) per-head dynamic sparsity
- **Methodology**: Varying precision levels based on attention scores; token pruning for least significant items
- **Results**: 2.7×–5.7× KV cache compression with 1.9×–5.4× throughput gains
- **Overlap with PSG-KVC**: Uses importance differentiation (attention-based) but not **PRM-based cross-trajectory scoring** or dynamic bit-width allocation during tree search
- **Source**: [arXiv:2412.03131](https://arxiv.org/abs/2412.03131)

### 5. **TriAttention** (arXiv:2604.04921) ✓ EXISTS
- **Title**: TriAttention (exact title not fully stated, but exists)
- **Status**: Real paper, submitted April 6, 2026
- **Key Approach**: Pre-RoPE space analysis where Q/K vectors are stable. Uses trigonometric series from Q/K centers to score key importance by position
- **Results**: 2.5× higher throughput or 10.7× KV memory reduction on AIME25 with 32K-token generation
- **Overlap with PSG-KVC**: **Zero overlap** - TriAttention focuses on distance-based importance in pre-RoPE space, not trajectory-based or reward-model-guided compression. No mention of tree search or cross-trajectory allocation
- **Source**: [arXiv:2604.04921](https://arxiv.org/abs/2604.04921)

---

## RELATED WORK (CLOSE BUT NOT DIRECT OVERLAP)

### 6. **Learning to Evict from Key-Value Cache** (arXiv:2602.10238)
- **Title**: Learning to Evict from Key-Value Cache
- **Status**: Real paper, February 2026
- **Key Approach**: Frames KV eviction as an RL problem with per-head lightweight agents trained on pre-computed generation traces
- **Reward**: Uses future utility as a holistic reward signal evaluating ranking quality across cache budgets
- **Results**: Outperforms on RULER (long-context) and OASST2-4k (multi-turn dialogue)
- **Relevance**: **Closest match to PSG-KVC's reward-based approach**, but still operates per-head on single trajectories, not cross-trajectory tree search with dynamic allocation
- **Source**: [arXiv:2602.10238](https://arxiv.org/abs/2602.10238)

### 7. **LookaheadKV** (arXiv:2603.10899)
- **Title**: LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation
- **Status**: Real paper, March 2026
- **Key Approach**: Uses draft generator to produce surrogate future response for KV importance estimation
- **Limitation**: Computationally expensive due to draft generation overhead
- **Source**: [arXiv:2603.10899](https://arxiv.org/abs/2603.10899)

### 8. **Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective** (arXiv:2604.25975)
- **Title**: CapKV: Capacity-aware KV Cache Eviction
- **Status**: Real paper
- **Key Approach**: Interprets eviction as capacity-maximization; uses log-determinant approximation and statistical leverage scores
- **Source**: [arXiv:2604.25975](https://arxiv.org/abs/2604.25975)

### 9. **Speculative Decoding & Quantization Papers** (Multiple recent works)
- **QuantSpec** (arXiv:2502.10424): Self-speculative decoding with hierarchical 4-bit quantized KV cache
- **SpecKV** (arXiv:2605.02888): Adaptive speculative decoding with compression-aware gamma selection
- **Speculative Decoding Meets Quantization** (arXiv:2505.22179): Compatibility evaluation and hierarchical framework
- **Status**: All real papers, 2025-2026
- **Overlap with PSG-KVC**: Address KV quantization in speculative decoding contexts but do not use **PRM scores for cross-trajectory allocation**. No per-trajectory differential bit-width assignment
- **Sources**: [QuantSpec](https://arxiv.org/abs/2502.10424), [SpecKV](https://arxiv.org/abs/2605.02888), [Speculative Decoding Meets Quantization](https://arxiv.org/abs/2505.22179)

### 10. **Inference-Time Hyper-Scaling with KV Cache Compression** (arXiv:2506.05345)
- **Title**: Inference-Time Hyper-Scaling with KV Cache Compression
- **Status**: Real paper, June 2025
- **Key Approach**: Dynamic Memory Sparsification (DMS) with only 1K training steps achieving 8× compression
- **Application**: Enhances reasoning models by allocating more tokens within same compute budget
- **Results**: +12.0 AIME24, +8.6 GPQA, +9.7 LiveCodeBench improvements for Qwen-R1 32B
- **Source**: [arXiv:2506.05345](https://arxiv.org/abs/2506.05345)

---

## KEY NOVEL ASPECTS OF PSG-KVC (If Genuine)

Based on my exhaustive search, the **claim of using PRM rank to set per-trajectory KV bit-width during tree search appears to have no prior precedent** in the literature I found. Here's why:

| Aspect | PSG-KVC Claim | Prior Work | Status |
|--------|--------------|-----------|--------|
| **Reward-based KV guidance** | PRM scores guide allocation | ForesightKV, Learning to Evict use future utility reward | Exists |
| **Cross-trajectory comparison** | PRM ranks multiple trajectories in real-time | All prior work operates per-head/per-trajectory in isolation | **Novel** |
| **Dynamic bit-width assignment** | FP16/INT8/INT4 per trajectory | MixKVQ (per-token), DiffKV (importance-based), but not per-trajectory | **Novel** |
| **Tree search context** | During MCTS/beam search inference | QuantSpec/SpecKV address speculative decoding, not MCTS ranking | **Novel** |
| **PRM as allocation signal** | PRM score directly controls precision | RL agents learn allocation policy (RLKV, Learning to Evict), but not PRM-ranked | **Possibly Novel** |

---

## PAPERS WITH CODE LANDSCAPE

From Papers with Code search for "KV cache quantization reasoning," the SOTA methods include:
- **KVTuner**: Layer-wise mixed precision (3.25-4.0 bits) on reasoning tasks
- **RotateKV**: 2-bit quantization with <0.3 perplexity degradation, <1.7% CoT reasoning loss
- **ZipCache**: Salient token identification for quantization
- **Scissorhands**: Up to 20× compression via importance-aware mixed precision

**None of these use PRM scores for trajectory-level allocation.**

---

## VERDICT ON NOVELTY CLAIMS

**The proposal appears to have legitimate novelty** in the specific combination of:
1. Using **PRM scores as a cross-trajectory ranking signal** (not seen in prior work)
2. **Real-time bit-width allocation** (FP16/INT8/INT4) based on trajectory PRM rank during inference tree search
3. This differs from all prior work which either:
   - Use learned policies (RLKV, Learning to Evict)
   - Use attention-based importance (DiffKV, TriAttention)
   - Use query-aware heuristics (MixKVQ)
   - Operate at per-head or per-token granularity, not per-trajectory

**However, the intellectual debt is clear**: The proposal builds directly on ForesightKV (reward-based thinking), RLKV (head-level compression), MixKVQ (mixed-precision design), and DiffKV (differentiated precision), but claims to extend these to cross-trajectory tree search contexts.

---

## CRITICAL EVALUATION QUESTIONS

1. **Does the PRM actually correlate with final reasoning quality in a way that predicts which trajectories deserve higher KV precision?** (Needs empirical validation)
2. **What is the overhead of computing PRM scores for all trajectories to rank them?** (May offset savings)
3. **How does this compare to simply allocating KV uniformly in top-k beam search?** (Needs controlled ablation)
4. **Does per-trajectory quantization create synchronization bottlenecks in batched inference?** (Systems question)

---

## SOURCES

- [ForesightKV (2602.03203)](https://arxiv.org/abs/2602.03203)
- [RLKV (2510.08525)](https://arxiv.org/abs/2510.08525)
- [MixKVQ (2512.19206)](https://arxiv.org/abs/2512.19206)
- [DiffKV (2412.03131)](https://arxiv.org/abs/2412.03131)
- [TriAttention (2604.04921)](https://arxiv.org/abs/2604.04921)
- [Learning to Evict from Key-Value Cache (2602.10238)](https://arxiv.org/abs/2602.10238)
- [LookaheadKV (2603.10899)](https://arxiv.org/abs/2603.10899)
- [CapKV/Rethinking KV Cache Eviction (2604.25975)](https://arxiv.org/abs/2604.25975)
- [QuantSpec (2502.10424)](https://arxiv.org/abs/2502.10424)
- [SpecKV (2605.02888)](https://arxiv.org/abs/2605.02888)
- [Speculative Decoding Meets Quantization (2505.22179)](https://arxiv.org/abs/2505.22179)
- [Inference-Time Hyper-Scaling with KV Cache Compression (2506.05345)](https://arxiv.org/abs/2506.05345)
- [Papers with Code - KVTuner](https://paperswithcode.com/paper/kvtuner-sensitivity-aware-layer-wise-mixed)
- [Papers with Code - RotateKV](https://paperswithcode.com/paper/rotatekv-accurate-and-robust-2-bit-kv-cache)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b948b69b-01a8-453f-8b7a-e78e55e8ce99",
  "isSidechain": true,
  "agentId": "a2c1b8ca350ac648f",
  "requestId": "req_011CaseJXsNie7fRqQJZ7nuL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ef7edc9d-5f6a-4699-b31c-4751c2b97a68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7e4c7211-d4cd-459f-a323-5aabf5f03a41",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FYUh2tFc529HVfCoft2w35",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1387,
      "cache_read_input_tokens": 25698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1387,
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
