# Research conversation: I'm reviewing an ML paper proposal about "Structure-Guided Draft Training for Reasoning Speculative Decoding" and need t

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aef1d7efc87249487.jsonl`
- **Structured JSON:** [`6d7c6bc8d1d614a9e4e6.json`](../../sessions/6d/6d7c6bc8d1d614a9e4e6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-09T18:43:44.620Z_

I'm reviewing an ML paper proposal about "Structure-Guided Draft Training for Reasoning Speculative Decoding" and need to independently verify several claims. Please search for:

1. ThinKV paper (arXiv:2510.01290) - verify it exists, is ICLR 2026 Oral, and what its R/E/T classification granularity actually is (segment-level vs token-level)
2. CoT-Aware speculative decoding paper (OpenReview bKau2NNrji) - verify it exists and what it actually does
3. EAGLE-3 (NeurIPS 2025) - verify it exists
4. SCoT arXiv:2504.19095 - verify it exists and its actual reported speedups
5. Search for any NEW competing work (2025-2026) on structural/semantic-aware draft training for speculative decoding
6. Search for any work combining Markov chain models with speculative decoding draft training
7. Search for "thought segment speculative decoding" or "reasoning trace structure speculative decoding"

For each search, use WebSearch. Report what you find - whether papers exist, what they actually claim, and any competing work that might challenge the novelty of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "21f1ba23-a54b-44e3-b9d4-ab02d23e19b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-09T18:43:47.294Z_

I'll systematically search for information about each of these papers and claims. Let me start with parallel searches for the main papers mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21f1ba23-a54b-44e3-b9d4-ab02d23e19b6",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVHX9tBxGqHyrDLeUZK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1597f0ab-323a-4577-8ffe-ae710f8e3c7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DKeoTKmfq8qaMAzdDXFh1V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16867,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16867,
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

_source line 3 · 2026-05-09T18:43:47.297Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CitM8THRNiHswXfDCKWXoN`</summary>

```json
{
  "query": "ThinKV arXiv:2510.01290 ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1597f0ab-323a-4577-8ffe-ae710f8e3c7b",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVHX9tBxGqHyrDLeUZK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "643425ea-598a-4ed7-9e4e-0374f0d9eebf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DKeoTKmfq8qaMAzdDXFh1V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16867,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16867,
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

_source line 4 · 2026-05-09T18:43:47.419Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W486jqSxZ8pGMPkZzf5TjX`</summary>

```json
{
  "query": "CoT-Aware speculative decoding OpenReview bKau2NNrji"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "643425ea-598a-4ed7-9e4e-0374f0d9eebf",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVHX9tBxGqHyrDLeUZK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2badc9b1-4385-4c67-ac8e-85c54d6c1ae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DKeoTKmfq8qaMAzdDXFh1V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16867,
      "cache_read_input_tokens": 0,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16867
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 254,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16867,
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

_source line 5 · 2026-05-09T18:43:47.424Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QR1EFJT56b92hBxGTD2BNv`</summary>

```json
{
  "query": "EAGLE-3 NeurIPS 2025 speculative decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2badc9b1-4385-4c67-ac8e-85c54d6c1ae9",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVHX9tBxGqHyrDLeUZK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8ede91fc-0b58-47d1-9e4f-f51f98c581a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DKeoTKmfq8qaMAzdDXFh1V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16867,
      "cache_read_input_tokens": 0,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16867
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 254,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16867,
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

_source line 6 · 2026-05-09T18:43:47.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KQaC6pvamVKbL5YiiUoagp`</summary>

```json
{
  "query": "SCoT arXiv:2504.19095 speedup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ede91fc-0b58-47d1-9e4f-f51f98c581a7",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVHX9tBxGqHyrDLeUZK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "53df8f6e-8521-4307-89f8-ee0a071a5cc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DKeoTKmfq8qaMAzdDXFh1V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16867,
      "cache_read_input_tokens": 0,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16867
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 254,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16867,
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

_source line 7 · 2026-05-09T18:43:53.408Z_

<details><summary>↩ Tool result · `toolu_01KQaC6pvamVKbL5YiiUoagp`</summary>

```text
Web search results for query: "SCoT arXiv:2504.19095 speedup"

Links: [{"title":"Efficient Reasoning for LLMs through Speculative Chain-of-Thought Jikai Wang","url":"https://arxiv.org/pdf/2504.19095"},{"title":"[2504.19095] Efficient Reasoning for LLMs through Speculative Chain-of-Thought","url":"https://arxiv.org/abs/2504.19095"},{"title":"Efficient Reasoning for LLMs through Speculative Chain-of-Thought","url":"https://arxiv.org/html/2504.19095"},{"title":"[2504.06254v1] Fixing non-blocking data structures for better compatibility with memory reclamation schemes","url":"https://arxiv.org/abs/2504.06254v1"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=9800&show=50"},{"title":"[2504.14841] (Sub)Exponential Quantum Speedup for Optimization","url":"https://arxiv.org/abs/2504.14841"},{"title":"Exponential Quantum Speedup for Simulating Classical Lattice Dynamics","url":"https://arxiv.org/html/2504.05453"},{"title":"[2504.05453] Exponential Quantum Speedup for Simulating Classical Lattice Dynamics","url":"https://arxiv.org/abs/2504.05453"},{"title":"[2601.19095] Dual Analysis of Continuous-time Economic Dispatch and Its Price Implications","url":"https://arxiv.org/abs/2601.19095"},{"title":"[2504.13613] Speedup Chip Yield Analysis by Improved Quantum Bayesian Inference","url":"https://arxiv.org/abs/2504.13613"}]

Based on the search results, here's what I found about SCoT (Speculative Chain-of-Thought) and its speedup metrics from arXiv:2504.19095:

## Overview
SCoT reduces reasoning latency by accelerating average reasoning speed through large and small model collaboration. The core idea of SCoT is to use a lightweight model to efficiently generate multiple CoT drafts which are then picked and used by the target model.

## Speedup Results
SCoT demonstrates an average speed-up ratio of 2.3× and 1.6× for the two target models on reasoning latency. More specifically, SCoT reduces reasoning latency by 48%–66% and 21%–49% for Deepseek-R1-Distill-Qwen-32B and Deepseek-R1-Distill-Llama-70B while achieving near-target-model-level performance.

## Key Innovation
SCoT is inspired by speculative decoding, which performs token-level speculation, whereas SCoT conducts thought-level speculation. Unlike shortening the length of CoT, SCoT accelerates the thinking process by increasing the speed of CoT generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53df8f6e-8521-4307-89f8-ee0a071a5cc4",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "2e4fe6a7-e22d-445f-9719-997d5aa69254",
  "sourceToolAssistantUUID": "53df8f6e-8521-4307-89f8-ee0a071a5cc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-09T18:43:53.900Z_

<details><summary>↩ Tool result · `toolu_01CitM8THRNiHswXfDCKWXoN`</summary>

```text
Web search results for query: "ThinKV arXiv:2510.01290 ICLR 2026"

Links: [{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.01290"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"Paper Digest: ICLR 2026 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2026/02/iclr-2026-papers-highlights/"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"ICLR Workshop 2026","url":"https://sites.google.com/view/icbinb-2026/home"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.02282"},{"title":"Publications - NYU Web Publishing - New York University","url":"https://wp.nyu.edu/cilvr/cilvr-group-publications/"},{"title":"Under review as a conference submission to ICLR 2026","url":"https://arxiv.org/pdf/2510.03361"}]

Based on the search results, here's what I found about ThinKV (arXiv:2510.01290):

## Overview

ThinKV is a thought-adaptive KV cache compression framework designed to address memory challenges in large reasoning models.

## Problem It Solves

The long-output context generation of large reasoning models enables extended chain of thought (CoT) but also drives rapid growth of the key-value (KV) cache, quickly overwhelming GPU memory.

## Key Approach

ThinKV is based on the observation that attention sparsity reveals distinct thought types with varying importance within the CoT. It applies a hybrid quantization-eviction strategy, assigning token precision by thought importance and progressively evicting tokens from less critical thoughts as reasoning trajectories evolve.

## Implementation Details

To implement ThinKV, they design a kernel that extends PagedAttention to enable efficient reuse of evicted tokens' memory slots, eliminating compaction overheads.

## Results

Extensive experiments on DeepSeek-R1-Distill, GPT-OSS, and NVIDIA AceReason across mathematics and coding benchmarks show that ThinKV achieves near-lossless accuracy with less than 5% of the original KV cache.

The paper was submitted to arXiv on October 1, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "643425ea-598a-4ed7-9e4e-0374f0d9eebf",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "48650879-a854-4552-87f9-5fbd1cc961a1",
  "sourceToolAssistantUUID": "643425ea-598a-4ed7-9e4e-0374f0d9eebf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-09T18:43:53.924Z_

<details><summary>↩ Tool result · `toolu_01W486jqSxZ8pGMPkZzf5TjX`</summary>

```text
Web search results for query: "CoT-Aware speculative decoding OpenReview bKau2NNrji"

Links: [{"title":"Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework | OpenReview","url":"https://openreview.net/forum?id=bKau2NNrji"},{"title":"ALIGNING DRAFT AND TARGET IN SPECULATIVE DE- CODING","url":"https://openreview.net/pdf?id=bKau2NNrji"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=h1t9kRSbLb"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"},{"title":"ALIGNING DRAFT AND TARGET IN SPECULATIVE DE","url":"https://openreview.net/pdf/d5ffb8b564b55ef1fb2b46c0c4b4efdbb74366e1.pdf"},{"title":"DISTILLSPEC: IMPROVING SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=rsY6J3ZaTF"},{"title":"SpecCoT: Accelerating Chain-of-Thought Reasoning through Speculative Exploration | OpenReview","url":"https://openreview.net/forum?id=mOR17THWTB"},{"title":"Online Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=Km3Kprwyua"},{"title":"SpecBranch: Speculative Decoding via Hybrid Drafting and Rollback-Aware Branch Parallelism | OpenReview","url":"https://openreview.net/forum?id=BrnlCSqO6n"},{"title":"Speculative Verification: Exploiting Information Gain to Refine Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=tPXtIMagQX"}]

I found the paper you're looking for! Here are the key details about the work:

## Title and Overview
The paper is titled "Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework". Chain-of-thought (CoT) prompting enhances the reasoning of large language models (LLMs) but increases autoregressive latency; speculative decoding (SD) mitigates this via a small-drafter--large-verifier pipeline whose efficiency hinges on drafted-token acceptance.

## Key Problem and Solution
The researchers show that training-based SD methods (e.g., EAGLE) suffer from catastrophic forgetting and distribution shift under naïve CoT supervision, and propose a CoT-aware mixed training framework that raises acceptance without altering decoding hyperparameters by combining process-level CoT distillation with feature regression to reduce forward KL divergence and improve step-wise acceptance, and SurpriseRatio (SR), a data-selection metric that anchors the distribution and prevents forgetting using minimal open-domain samples.

## Performance Results
Experiments on two target models show that their methods achieve wall-clock speedups of 3.04×–4.55×.

The paper is hosted on OpenReview at: https://openreview.net/forum?id=bKau2NNrji


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2badc9b1-4385-4c67-ac8e-85c54d6c1ae9",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "93923b6d-7830-4e98-8b0c-805feb0c099e",
  "sourceToolAssistantUUID": "2badc9b1-4385-4c67-ac8e-85c54d6c1ae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-09T18:43:53.993Z_

<details><summary>↩ Tool result · `toolu_01QR1EFJT56b92hBxGTD2BNv`</summary>

```text
Web search results for query: "EAGLE-3 NeurIPS 2025 speculative decoding"

Links: [{"title":"GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub","url":"https://github.com/SafeAILab/EAGLE"},{"title":"EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test | OpenReview","url":"https://openreview.net/forum?id=4exx1hUffq"},{"title":"Speculative Decoding in Practice: How EAGLE3 Makes LLMs Faster Without Changing Their Outputs","url":"https://huggingface.co/blog/lujangusface/tw-eagle3-gpu"},{"title":"EAGLE-3: Scaling up Inference Acceleration of Large ...","url":"https://openreview.net/pdf?id=4exx1hUffq"},{"title":"SuffixDecoding: Extreme Speculative Decoding for Emerging AI Applications | NeurIPS 2025 Spotlight","url":"https://suffix-decoding.github.io/"},{"title":"NeurIPS Poster EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119930"},{"title":"[2503.01840] EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test","url":"https://arxiv.org/abs/2503.01840"},{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"SuffixDecoding: Extreme Speculative Decoding for Emerging AI Applications","url":"https://arxiv.org/pdf/2411.04975"},{"title":"P-EAGLE: Faster LLM inference with Parallel Speculative Decoding in vLLM | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/"}]

Based on the search results, here's what I found about EAGLE-3 at NeurIPS 2025:

## Overview

EAGLE-3 was accepted to NeurIPS'25, and the poster was presented on Wednesday, December 3, 2025.

## What is EAGLE-3?

EAGLE (Extrapolation Algorithm for Greater Language-model Efficiency) is a new baseline for fast decoding of Large Language Models (LLMs) with provable performance maintenance through extrapolating the second-top-layer contextual feature vectors of LLMs.

## Key Innovations

EAGLE-3 abandons feature prediction in favor of direct token prediction and replaces reliance on top-layer features with multi-layer feature fusion via a technique named training-time test. More specifically, EAGLE-3 removes the feature prediction constraint in EAGLE and simulates this process during training using training-time testing, while replacing top-layer features with a fusion of low-, mid-, and high-level semantic features.

## Performance Results

EAGLE-3 achieves a speedup ratio up to 6.5x, with about 1.4x improvement over EAGLE-2, and in the SGLang framework, EAGLE-3 achieves a 1.38x throughput improvement at a batch size of 64.

## Code and Implementation

EAGLE has been merged in mainstream LLM serving frameworks including vLLM, SGLang, and others, making it accessible for practical deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ede91fc-0b58-47d1-9e4f-f51f98c581a7",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "74e2cda6-ec63-4f80-ba80-46f7c30c4d37",
  "sourceToolAssistantUUID": "8ede91fc-0b58-47d1-9e4f-f51f98c581a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-09T18:43:55.536Z_

Good progress. Now let me search for more information about ThinKV's specific classification granularity, and then search for competing and related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74e2cda6-ec63-4f80-ba80-46f7c30c4d37",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVJDBB8iLFkxR6s3Y3S",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3e76bd76-f581-4129-beda-cb8e1348f3a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VetK5pPprwEtdJLwRFGRRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 3709,
      "cache_read_input_tokens": 16867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3709,
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

_source line 12 · 2026-05-09T18:43:55.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RMoyLSbGYTRWsSBL2UtXeq`</summary>

```json
{
  "query": "ThinKV segment-level token-level thought type classification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e76bd76-f581-4129-beda-cb8e1348f3a6",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVJDBB8iLFkxR6s3Y3S",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "346dfebe-c145-4511-bf3d-3fa462e5b9de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VetK5pPprwEtdJLwRFGRRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 3709,
      "cache_read_input_tokens": 16867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3709,
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

_source line 13 · 2026-05-09T18:43:56.317Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kt2KX1oDNHwZV6gys7kguP`</summary>

```json
{
  "query": "structural semantic-aware draft training speculative decoding 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "346dfebe-c145-4511-bf3d-3fa462e5b9de",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVJDBB8iLFkxR6s3Y3S",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b06af5b2-290c-4fbe-a26d-d5c97a313a82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VetK5pPprwEtdJLwRFGRRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 3709,
      "cache_read_input_tokens": 16867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3709,
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

_source line 14 · 2026-05-09T18:43:56.503Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G97dXVt6QGPFLudsVZeVhR`</summary>

```json
{
  "query": "Markov chain speculative decoding draft training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b06af5b2-290c-4fbe-a26d-d5c97a313a82",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVJDBB8iLFkxR6s3Y3S",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2e97e9ac-de7b-4813-8c99-482241de707c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VetK5pPprwEtdJLwRFGRRy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 3709,
      "cache_read_input_tokens": 16867,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3709
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 781,
          "output_tokens": 232,
          "cache_read_input_tokens": 16867,
          "cache_creation_input_tokens": 3709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3709,
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

_source line 15 · 2026-05-09T18:43:56.548Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XjLBB9rbVeCGUwRqc1Nk96`</summary>

```json
{
  "query": "thought segment speculative decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e97e9ac-de7b-4813-8c99-482241de707c",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVJDBB8iLFkxR6s3Y3S",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04562be6-36ba-4177-b447-539900b60249",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VetK5pPprwEtdJLwRFGRRy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 781,
      "cache_creation_input_tokens": 3709,
      "cache_read_input_tokens": 16867,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3709
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 781,
          "output_tokens": 232,
          "cache_read_input_tokens": 16867,
          "cache_creation_input_tokens": 3709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3709,
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

_source line 16 · 2026-05-09T18:44:02.660Z_

<details><summary>↩ Tool result · `toolu_01G97dXVt6QGPFLudsVZeVhR`</summary>

```text
Web search results for query: "Markov chain speculative decoding draft training"

Links: [{"title":"Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework | OpenReview","url":"https://openreview.net/forum?id=bKau2NNrji"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"SPECDEC++: BOOSTING SPECULATIVE DECODING VIA ...","url":"https://openreview.net/pdf?id=NnExMNiTHw"},{"title":"Get 3× Faster LLM Inference with Speculative Decoding Using the Right Draft Model","url":"https://www.bentoml.com/blog/3x-faster-llm-inference-with-speculative-decoding"},{"title":"SpecDec++: Boosting Speculative Decoding via Adaptive Candidate Lengths","url":"https://openreview.net/pdf?id=ZwwY5UgNGh"},{"title":"When Drafts Evolve: Speculative Decoding Meets Online Learning","url":"https://arxiv.org/html/2603.12617"},{"title":"Speculative Decoding with CTC-based Draft Model for LLM Inference Acceleration","url":"https://arxiv.org/html/2412.00061v1"},{"title":"Training Domain Draft Models for Speculative Decoding: Best Practices and Insights","url":"https://arxiv.org/html/2503.07807v1"},{"title":"MIXTURE OF ATTENTIONS FOR SPECULATIVE DECODING","url":"https://discovery.ucl.ac.uk/id/eprint/10212512/1/11328_Mixture_of_Attentions_Fo.pdf"},{"title":"Preprint. SELF SPECULATIVE DECODING FOR DIFFUSION LARGE LANGUAGE MODELS","url":"https://arxiv.org/pdf/2510.04147"}]

Based on the search results, here's what I found about Markov chain speculative decoding draft training:

## Markov Decision Process Framework in Speculative Decoding

Speculative decoding can be formulated into a Markov Decision Process (MDP) framework. The optimal policy of this Markov decision process takes the form of a threshold policy, where the current speculation should stop and be verified when the probability of getting a rejection exceeds a threshold value.

## Key Applications

One notable application is **SpecDec++**, an enhanced version of speculative decoding that adaptively determines the candidate length on the fly. SpecDec++ augments the draft model with a trained acceptance prediction head to predict the conditional acceptance probability of the candidate tokens, and will stop the current speculation when the predicted probability that at least one token gets rejected exceeds a threshold.

## Broader Context on Draft Training

Beyond the Markov chain approach, speculative decoding is an effective method for accelerating inference of large language models (LLMs) by employing a small draft model to predict the output of a target model. Variational Speculative Decoding (VSD) formulates draft training as variational inference over latent proposals (draft paths), maximizing the marginal probability of target-model acceptance while minimizing divergence from the target distribution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e97e9ac-de7b-4813-8c99-482241de707c",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "6a2079fa-6aa0-4891-b3a1-602206933980",
  "sourceToolAssistantUUID": "2e97e9ac-de7b-4813-8c99-482241de707c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-09T18:44:02.778Z_

<details><summary>↩ Tool result · `toolu_01RMoyLSbGYTRWsSBL2UtXeq`</summary>

```text
Web search results for query: "ThinKV segment-level token-level thought type classification"

Links: [{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Think Before You Segment: High-Quality Reasoning Segmentation with GPT Chain of Thoughts","url":"https://arxiv.org/html/2503.07503v2"},{"title":"Chain-of-Visual-Thought: Teaching VLMs to See and Think Better with Continuous Visual Tokens","url":"https://arxiv.org/html/2511.19418v2"},{"title":"Thought-Adaptive KV Cache Compression","url":"https://www.emergentmind.com/topics/thought-adaptive-kv-cache-compression"},{"title":"Segment-Level Attribution for Selective Learning of Long Reasoning Traces","url":"https://arxiv.org/html/2602.00425"},{"title":"Token Classification in Natural Language Processing - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/token-classification-in-natural-language-processing/"},{"title":"1 The Type-Token Distinction and the Mind and Brain Sciences","url":"https://philsci-archive.pitt.edu/3860/1/The_Type-Token_Distinction_and_the_Mind_and_Brain_Sciences.pdf"},{"title":"Modeling Language as a Sequence of Thoughts","url":"https://arxiv.org/html/2512.25026v2"},{"title":"Token Classification","url":"https://colab.research.google.com/github/huggingface/notebooks/blob/master/examples/token_classification.ipynb"},{"title":"Types and Tokens (Stanford Encyclopedia of Philosophy)","url":"https://plato.stanford.edu/entries/types-tokens/"}]

Based on the search results, here's what I found about ThinKV and its segment-level token-level thought type classification approach:

## ThinKV Overview

ThinKV is a thought-adaptive hybrid quantization–eviction framework designed for efficient reasoning models. It addresses the challenge of compressing key-value (KV) cache while preserving reasoning-critical information.

## Thought Type Classification

ThinKV categorizes generation into "Reasoning," "Execution," and "Transition" types based on attention sparsity statistics measured via kernel density estimates, dynamically assigning compression fidelity to each.

More specifically, the chain of thought in Large Reasoning Models (LRMs) can be decomposed into distinct thought types, with their differentiation enabled by degree of sparsity in attention weights.

## Key Components

The framework operates through two main mechanisms:

1. **Think Before You Quantize (TBQ)**: A KV cache quantization scheme that assigns precision to tokens based on the importance of their associated thought type.

2. **Think Before You Evict (TBE)**: A thought-adaptive eviction scheme that leverages inter-thought dynamics to progressively evict tokens.

## Performance

ThinKV (TBQ+TBE) yields substantial compression at the cost of only a marginal accuracy reduction, demonstrating the effectiveness of combining thought-aware quantization with adaptive eviction strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "346dfebe-c145-4511-bf3d-3fa462e5b9de",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "5fb6f6b2-e0af-4842-8aac-16d46e62c5d0",
  "sourceToolAssistantUUID": "346dfebe-c145-4511-bf3d-3fa462e5b9de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-09T18:44:04.136Z_

<details><summary>↩ Tool result · `toolu_01XjLBB9rbVeCGUwRqc1Nk96`</summary>

```text
Web search results for query: "thought segment speculative decoding"

Links: [{"title":"A Hitchhiker’s Guide to Speculative Decoding – PyTorch","url":"https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/"},{"title":"Looking back at speculative decoding","url":"https://research.google/blog/looking-back-at-speculative-decoding/"},{"title":"Efficient Reasoning for LLMs through Speculative Chain-of-Thought","url":"https://arxiv.org/html/2504.19095v2"},{"title":"Generation at the Speed of Thought: Speculative Decoding","url":"https://bittere.substack.com/p/generation-at-the-speed-of-thought"},{"title":"Speculative decoding strips thinking tokens · Issue #866 · jundot/omlx","url":"https://github.com/jundot/omlx/issues/866"},{"title":"Speculative Decoding: A Guide With Implementation Examples | DataCamp","url":"https://www.datacamp.com/tutorial/speculative-decoding"},{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"},{"title":"In the Fast Lane! Speculative Decoding — 10x Larger Model, No Extra Cost | by TitanML | Medium","url":"https://medium.com/@TitanML/in-the-fast-lane-speculative-decoding-10x-larger-model-no-extra-cost-f33ea39d065a"},{"title":"The Magic of “Thinking Ahead”: How Speculative Decoding Makes AI Faster | by Kyush | Medium","url":"https://mkyush.medium.com/the-magic-of-thinking-ahead-how-speculative-decoding-makes-ai-faster-7cca5e1e3c45"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"}]

Based on the search results, here's what I found about thought segment speculative decoding:

## Speculative Chain-of-Thought (SCoT)

The search results reveal a technique called Speculative Chain-of-Thought (SCoT), which is inspired by speculative decoding but performs thought-level speculation rather than token-level speculation. 

This represents an evolution in how speculative decoding is being applied to reasoning tasks. Rather than speculating at the individual token level (as traditional speculative decoding does), thought chains are mostly generated by the draft model for simple tasks, while more thought chains are allocated to the target model for complex problems, achieving a speed-up ratio of up to 2.92× for the reasoning process.

## Overview of Speculative Decoding Context

For context, speculative decoding is an inference optimization technique that pairs a target model with a lightweight draft mechanism that quickly proposes several next tokens, which the target model then verifies in a single forward pass and accepts the longest prefix that matches its own predictions.

The thought segment approach appears to be a higher-level application of this same principle, operating at the level of reasoning "thoughts" or segments rather than individual tokens, making it particularly useful for tasks that require chain-of-thought reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04562be6-36ba-4177-b447-539900b60249",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "a498550e-4eff-428b-8612-223338782b36",
  "sourceToolAssistantUUID": "04562be6-36ba-4177-b447-539900b60249",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-09T18:44:04.187Z_

<details><summary>↩ Tool result · `toolu_01Kt2KX1oDNHwZV6gys7kguP`</summary>

```text
Web search results for query: "structural semantic-aware draft training speculative decoding 2025 2026"

Links: [{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"Draft, Verify, & Improve Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/html/2510.05421v1"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"ConFu: Contemplate the Future for Better Speculative Sampling","url":"https://arxiv.org/html/2603.08899v1"},{"title":"ENTROPY-AWARE SPECULATIVE DECODING TOWARD ...","url":"https://openreview.net/pdf/8873a72aa9dd1126e677275974d787218c03b614.pdf"},{"title":"[2510.05421] Draft, Verify, and Improve: Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/abs/2510.05421"},{"title":"Recurrent Drafter for Fast Speculative Decoding in Large Language Models - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/recurrent-drafter"},{"title":"Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/mirror"},{"title":"DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference","url":"https://arxiv.org/html/2601.19278v1"}]

Based on the search results, I found several relevant research papers from 2025-2026 on speculative decoding with draft training improvements. Here are the key findings:

## Recent Advances in Speculative Decoding (2025-2026)

Recent work has improved speculative decoding by refining draft model training. Several notable approaches have emerged:

**Draft Model Training Improvements:**
- HASS (Zhang et al., 2024) enforces feature consistency to reduce hidden-state mismatches, GRIFFIN (Hu et al., 2025b) resolves token-level misalignment, and EAGLE-3 (Li et al., 2025) incorporates training-time rollouts to better mimic decoding.

**Semantic and Structural Awareness:**
- A constraint effectively filters out semantically implausible combinations that arise from independently predicted positions, while retaining high-quality candidates.
- DVI is particularly effective for workloads with strong local lexical structure and retrieval grounding (assistant-style tasks), whereas deep tree drafting is more beneficial for long-range reasoning and structured planning.

**Training-Decoding Distribution Alignment:**
A fundamental limitation remains: a training-decoding distributional discrepancy. The draft model is trained to favor a deterministic distribution (a single greedy path), while decoding operates over a stochastic distribution induced by ranked multi-path sampling.

**Advanced Architectures:**
- ConFu provides a new direction for improving draft generation by additionally conditioning the draft model with contemplate token and future token, and views this as an important step toward integrating speculative decoding with latent reasoning paradigms.

The research demonstrates significant progress in making speculative decoding more semantically aware through better training objectives and structural constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b06af5b2-290c-4fbe-a26d-d5c97a313a82",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "76c98cc0-f13d-4f7d-b521-f07fe947ad53",
  "sourceToolAssistantUUID": "b06af5b2-290c-4fbe-a26d-d5c97a313a82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-09T18:44:05.765Z_

Let me do one more search to look specifically for "reasoning trace structure speculative decoding" and other competing approaches that directly combine reasoning structure with draft training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76c98cc0-f13d-4f7d-b521-f07fe947ad53",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVJxiZ3qPFxK2Bo9EAA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "65590988-84b4-48aa-bb41-4e548de5a869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QCQuWaRiQVsFTGpxFA282o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1712,
      "cache_creation_input_tokens": 2852,
      "cache_read_input_tokens": 20576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2852,
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

_source line 21 · 2026-05-09T18:44:05.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KTmh8k89J8bUpRGerA3eSV`</summary>

```json
{
  "query": "\"reasoning trace structure\" speculative decoding draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65590988-84b4-48aa-bb41-4e548de5a869",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVJxiZ3qPFxK2Bo9EAA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2567fae6-b3b0-4907-8971-88d96fa30500",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QCQuWaRiQVsFTGpxFA282o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1712,
      "cache_creation_input_tokens": 2852,
      "cache_read_input_tokens": 20576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2852,
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

_source line 22 · 2026-05-09T18:44:06.386Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016ABJ6Sfko4gpdmo3S21EXh`</summary>

```json
{
  "query": "draft model reasoning path structure CoT 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2567fae6-b3b0-4907-8971-88d96fa30500",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVJxiZ3qPFxK2Bo9EAA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2b4f4c0a-b8a2-4753-8bdd-ecfa97645fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QCQuWaRiQVsFTGpxFA282o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1712,
      "cache_creation_input_tokens": 2852,
      "cache_read_input_tokens": 20576,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1712,
          "output_tokens": 182,
          "cache_read_input_tokens": 20576,
          "cache_creation_input_tokens": 2852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2852,
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

_source line 23 · 2026-05-09T18:44:06.456Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XAWErbQAjQBggcH7uu4zHc`</summary>

```json
{
  "query": "semantic draft speculative decoding reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b4f4c0a-b8a2-4753-8bdd-ecfa97645fe3",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVJxiZ3qPFxK2Bo9EAA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "49ec4eac-bb00-4ea2-9c4a-bb087aafe8db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QCQuWaRiQVsFTGpxFA282o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1712,
      "cache_creation_input_tokens": 2852,
      "cache_read_input_tokens": 20576,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1712,
          "output_tokens": 182,
          "cache_read_input_tokens": 20576,
          "cache_creation_input_tokens": 2852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2852,
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

_source line 24 · 2026-05-09T18:44:12.514Z_

<details><summary>↩ Tool result · `toolu_01KTmh8k89J8bUpRGerA3eSV`</summary>

```text
Web search results for query: ""reasoning trace structure" speculative decoding draft"

Links: [{"title":"Speculative Decoding: A Guide With Implementation Examples | DataCamp","url":"https://www.datacamp.com/tutorial/speculative-decoding"},{"title":"ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification","url":"https://arxiv.org/html/2602.18447"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure","url":"https://aclanthology.org/2025.tacl-1.8.pdf"},{"title":"Adaptive Speculative Decoding","url":"https://www.emergentmind.com/topics/adaptive-speculative-decoding"},{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"},{"title":"Faster Speculative Decoding via Effective Draft ...","url":"https://aclanthology.org/2025.acl-long.486.pdf"},{"title":"Offloaded Reasoning: Efficient Inference for Large ...","url":"https://aclanthology.org/2025.findings-emnlp.393.pdf"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00735/128189/OPT-Tree-Speculative-Decoding-with-Adaptive-Draft"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning | Hao AI Lab @ UCSD","url":"https://haoailab.com/blogs/lookaheadreasoning/"}]

Based on the web search results, here's what I found about reasoning trace structure in the context of speculative decoding and draft models:

## Reasoning Trace Structure in Speculative Decoding

Although reasoning traces are generated token by token, their semantic structure is natural, which has important implications for how speculative decoding can be optimized.

### Step-Level Reasoning Structure

Recent research shows that reasoning is inherently hierarchical: a chain-of-thought naturally decomposes into discrete steps, each representing a semantically meaningful unit of progress. A step might consist of a subgoal, a case split, or a logical transformation.

This hierarchical structure is significant because a step only needs to be semantically correct to advance the proof or derivation; it need not match the target model token-for-token, to contribute validly to the overall reasoning trace.

### Practical Implementation with Draft Models

The smaller model, often called the "draft" model, generates a batch of tokens that the main, more powerful LLM can either confirm or refine. The draft model acts as a first pass, producing multiple tokens that speed up the generation process. Instead of the main LLM generating tokens sequentially, the draft model provides a set of likely candidates, and the main model evaluates them in parallel.

### Advanced Approaches

Step-level speculative reasoning extends speculative decoding by operating on entire reasoning steps. By allowing verification based on semantic equivalence rather than exact token matching, step-level speculation better aligns with the structure of CoT reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2567fae6-b3b0-4907-8971-88d96fa30500",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "e8413cf1-7b74-4c2a-9176-99ad59eca814",
  "sourceToolAssistantUUID": "2567fae6-b3b0-4907-8971-88d96fa30500",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-09T18:44:14.744Z_

<details><summary>↩ Tool result · `toolu_01XAWErbQAjQBggcH7uu4zHc`</summary>

```text
Web search results for query: "semantic draft speculative decoding reasoning 2026"

Links: [{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/pdf/2506.19830"},{"title":"[2604.15244] From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning","url":"https://arxiv.org/abs/2604.15244"},{"title":"Beyond Tokens: Semantic-Aware Speculative Decoding for Efficient Inference by Probing Internal States","url":"https://arxiv.org/html/2602.03708"},{"title":"Speculative decoding: how it works & when to use it","url":"https://redis.io/blog/speculative-decoding-llm/"},{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Calibrated Speculative Decoding: Frequency-Guided Candidate Selection for Efficient Inference","url":"https://arxiv.org/html/2604.13634"},{"title":"Speculative decoding | LLM Inference Handbook","url":"https://bentoml.com/llm/inference-optimization/speculative-decoding"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=speculative+decoding"},{"title":"Speculative Speculative Decoding Tanishq Kumar1,* Tri Dao2,3 Avner May3","url":"https://arxiv.org/pdf/2603.03251"}]

Based on the search results, here's what I found about semantic draft speculative decoding and reasoning in 2026:

## Key Developments in 2026

Several important papers and approaches have emerged in 2026 addressing semantic-aware speculative decoding for reasoning:

### SemanticSpec Framework
SemanticSpec is a semantic-aware speculative decoding framework that verifies entire semantic sequences instead of tokens, introducing a semantic probability estimation mechanism that probes the model's internal hidden states to assess the likelihood of generating sequences with specific meanings. This approach achieves up to 2.7× speedup on DeepSeekR1-32B and 2.1× on QwQ-32B, addressing the limitation that existing token-level methods ignore semantic equivalence (i.e., different token sequences expressing the same meaning), leading to inefficient rejections.

### Lookahead Reasoning
Entire reasoning steps can be speculatively proposed by a draft model, with a small 1.5B draft model able to generate speculative steps that semantically align with over 50% of ground-truth steps from a much larger 32B target model. Methods like SpecReason and Lookahead Reasoning address limitations by drafting entire reasoning steps rather than individual tokens, then verifying them for semantic correctness rather than exact token match.

### Verification-Aware Approaches
SpecGuard is a verification-aware speculative decoding framework that performs step-level verification using model-internal signals, sampling multiple draft candidates and selecting the most consistent step validated using an ensemble of attention-based grounding scores and log-probability-based scores.

### Speculative Speculative Decoding
Speculative speculative decoding (SSD) is a unifying framework for parallelizing drafting and verification, where the draft model predicts what verification outcomes are most likely and prepares speculations for all of them in parallel to verification.

These approaches represent a shift toward understanding and leveraging semantic meaning rather than strict token matching in speculative decoding for reasoning models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49ec4eac-bb00-4ea2-9c4a-bb087aafe8db",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "666b2477-c9bb-4f50-a679-2e29922d354c",
  "sourceToolAssistantUUID": "49ec4eac-bb00-4ea2-9c4a-bb087aafe8db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-09T18:44:15.054Z_

<details><summary>↩ Tool result · `toolu_016ABJ6Sfko4gpdmo3S21EXh`</summary>

```text
Web search results for query: "draft model reasoning path structure CoT 2025"

Links: [{"title":"Draft-Thinking: Learning Efficient Reasoning in Long Chain-of-Thought LLMs","url":"https://arxiv.org/html/2603.00578"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://aclanthology.org/2025.emnlp-main.504.pdf"},{"title":"Published in Transactions on Machine Learning Research (08/2025)","url":"https://openreview.net/pdf?id=HvoG8SxggZ"},{"title":"LLaVA-CoT: Let Vision Language Models Reason Step-by-Step Guowei Xu♣*","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_LLaVA-CoT_Let_Vision_Language_Models_Reason_Step-by-Step_ICCV_2025_paper.pdf"},{"title":"A Survey of Chain-of-X Paradigms for LLMs","url":"https://aclanthology.org/2025.coling-main.719.pdf"},{"title":"Chain of Draft: Concise Prompting Reduces LLM Costs by 90% - Ajith Vallath Prabhakar","url":"https://ajithp.com/2025/03/02/chain-of-draft-llm-prompting/"},{"title":"Sketch-of-Thought: Efficient LLM Reasoning with Adaptive ...","url":"https://aclanthology.org/2025.emnlp-main.1236.pdf"},{"title":"Chain of Draft for Software Engineering: Challenges in Applying Concise Reasoning to Code Tasks","url":"https://arxiv.org/html/2506.10987"},{"title":"DR-CoT: dynamic recursive chain of thought with meta reasoning for parameter efficient models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-18622-6"},{"title":"CoT-RAG: Integrating Chain of Thought and Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.168.pdf"}]

Based on the search results, I found relevant information about draft model reasoning and Chain-of-Thought (CoT) structures in 2025. Here are the key findings:

## Draft-Thinking and Reasoning Path Structure

Draft-Thinking internalizes the selection of high-value steps as an endogenous capability of large reasoning models, maintaining the original long-CoT capability while substantially boosting its token efficiency.

The reasoning behavior differs between the original model and Draft-Thinking's three reasoning modes, with analysis examining the reasoning behavior differences through distinct phases across predefined categories.

## Chain of Draft (CoD) - A Key 2025 Development

Chain of Draft (CoD), as introduced by Xu et al. (2025), is a prompting strategy that encourages language models to generate extremely concise intermediate reasoning steps. CoD encourages models to produce extremely concise intermediate reasoning steps—limited to just 5 words per step, with research demonstrating remarkable efficiency gains in mathematical reasoning tasks, reducing token usage to merely 7.6% of CoT while maintaining comparable accuracy.

## CoT Variants and Structured Reasoning

Self-Consistency CoT replaces the standard greedy decoding approach by sampling diverse reasoning paths and selecting the most consistent answer through marginalization and aggregation. Tree-of-Thought (ToT) prompting further structures the reasoning process as a tree with backtracking, significantly improving efficiency in solving parallelizable subtasks.

## Sketch-of-Thought (SoT)

Sketch-of-Thought (SoT) introduces paradigm-guided sketching, yielding more compact yet structured intermediate steps via dynamic routing, in contrast to CoT which produces verbose natural language traces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b4f4c0a-b8a2-4753-8bdd-ecfa97645fe3",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "326f5b5a-7505-43fc-b355-fead316c3007",
  "sourceToolAssistantUUID": "2b4f4c0a-b8a2-4753-8bdd-ecfa97645fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-09T18:44:17.252Z_

Excellent. Now let me search more specifically for verification-aware and step-level speculative decoding papers to get complete information on competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "326f5b5a-7505-43fc-b355-fead316c3007",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVKpSkQ4rECHMC5bQVZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "478941d7-b635-40af-8782-4ed3732e8877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0182Vc7bN1fwUPXeB3mFwHzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 982,
      "cache_creation_input_tokens": 3785,
      "cache_read_input_tokens": 23428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3785,
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

_source line 28 · 2026-05-09T18:44:17.474Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LBraJdYGenUnLsq2Q7ynyt`</summary>

```json
{
  "query": "\"From Tokens to Steps\" verification-aware speculative decoding arXiv 2604.15244"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "478941d7-b635-40af-8782-4ed3732e8877",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVKpSkQ4rECHMC5bQVZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b3432e1c-f11d-4948-8e1f-97ffa39409c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0182Vc7bN1fwUPXeB3mFwHzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 982,
      "cache_creation_input_tokens": 3785,
      "cache_read_input_tokens": 23428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3785,
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

_source line 29 · 2026-05-09T18:44:17.919Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N3n5598Xv9CqsaJ1Q67suU`</summary>

```json
{
  "query": "ConfSpec step-level speculative reasoning confidence arXiv 2602.18447"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3432e1c-f11d-4948-8e1f-97ffa39409c8",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVKpSkQ4rECHMC5bQVZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4b1ab403-fad6-4de0-9463-66c8b563feef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0182Vc7bN1fwUPXeB3mFwHzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 982,
      "cache_creation_input_tokens": 3785,
      "cache_read_input_tokens": 23428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3785,
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

_source line 30 · 2026-05-09T18:44:18.209Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012aTUCT9rYdeopJq7SQvuEh`</summary>

```json
{
  "query": "OPT-Tree adaptive draft tree structure speculative decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b1ab403-fad6-4de0-9463-66c8b563feef",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVKpSkQ4rECHMC5bQVZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f1d33f85-3101-4df9-adcd-f9a84ea29e1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0182Vc7bN1fwUPXeB3mFwHzv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 982,
      "cache_creation_input_tokens": 3785,
      "cache_read_input_tokens": 23428,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 982,
          "output_tokens": 205,
          "cache_read_input_tokens": 23428,
          "cache_creation_input_tokens": 3785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3785,
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

_source line 31 · 2026-05-09T18:44:22.774Z_

<details><summary>↩ Tool result · `toolu_01LBraJdYGenUnLsq2Q7ynyt`</summary>

```text
Web search results for query: ""From Tokens to Steps" verification-aware speculative decoding arXiv 2604.15244"

Links: [{"title":"[2604.15244] From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning","url":"https://arxiv.org/abs/2604.15244"},{"title":"From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning","url":"https://arxiv.org/html/2604.15244"},{"title":"ELMoE-3D: Leveraging Intrinsic Elasticity of MoE for Hybrid-Bonding-Enabled Self-Speculative Decoding in On-Premises Serving","url":"https://arxiv.org/html/2604.14626"},{"title":"[2604.14682] Acceptance Dynamics Across Cognitive Domains in Speculative Decoding","url":"https://arxiv.org/abs/2604.14682"},{"title":"See the Forest for the Trees See the Forest for the Trees: Loosely Speculative Decoding via Visual-Semantic Guidance for Efficient Inference of Video LLMs","url":"https://arxiv.org/html/2604.05650v1"},{"title":"Speeding up Speculative Decoding via Approximate Verification","url":"https://arxiv.org/html/2502.04557v1"},{"title":"Beyond Tokens: Semantic-Aware Speculative Decoding for Efficient Inference by Probing Internal States","url":"https://arxiv.org/html/2602.03708"},{"title":"A Comprehensive Survey of Speculative Decoding","url":"https://aclanthology.org/2024.findings-acl.456.pdf"},{"title":"SpecInfer: Accelerating Generative LLM Serving with ...","url":"https://www.cs.cmu.edu/~zhihaoj2/papers/specinfer.pdf"},{"title":"Calibrated Speculative Decoding: Frequency-Guided Candidate Selection for Efficient Inference","url":"https://arxiv.org/html/2604.13634"}]

I found the paper! Here's what I discovered:

"From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning" was submitted to arXiv on April 16, 2026 by authors Kiran Purohit, Ramasuri Narayanam, and Soumyabrata Pal.

The paper addresses speculative decoding, which accelerates large language model inference by allowing a lightweight draft model to propose outputs that a stronger target model verifies, but its token-centric nature allows erroneous steps to propagate.

The authors propose SpecGuard, a verification-aware speculative decoding framework that performs step-level verification using only model-internal signals. At each step, SpecGuard samples multiple draft candidates and selects the most consistent step, which is then validated using an ensemble of lightweight models.

The full paper is available on arXiv at https://arxiv.org/abs/2604.15244.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3432e1c-f11d-4948-8e1f-97ffa39409c8",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "2d06f684-8166-4253-8554-9d361282c769",
  "sourceToolAssistantUUID": "b3432e1c-f11d-4948-8e1f-97ffa39409c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-09T18:44:23.387Z_

<details><summary>↩ Tool result · `toolu_01N3n5598Xv9CqsaJ1Q67suU`</summary>

```text
Web search results for query: "ConfSpec step-level speculative reasoning confidence arXiv 2602.18447"

Links: [{"title":"[2602.18447] ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification","url":"https://arxiv.org/abs/2602.18447"},{"title":"ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification","url":"https://arxiv.org/html/2602.18447"},{"title":"SpecReason: Fast and Accurate Inference-Time Compute via Speculative Reasoning","url":"https://arxiv.org/html/2504.07891v1"},{"title":"Accelerating Large Language Model Reasoning via Speculative Search","url":"https://arxiv.org/html/2505.02865v1"},{"title":"Beyond Tokens: Semantic-Aware Speculative Decoding for Efficient Inference by Probing Internal States","url":"https://arxiv.org/html/2602.03708"},{"title":"ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning","url":"https://arxiv.org/html/2505.04881v1"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"[2504.07891] SpecReason: Fast and Accurate Inference-Time Compute via Speculative Reasoning","url":"https://arxiv.org/abs/2504.07891"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/html/2506.19830v1"},{"title":"Speculative Thinking: Enhancing Small-Model Reasoning with Large Model Guidance at Inference Time","url":"https://arxiv.org/html/2504.12329v1"}]

Based on the search results, I found information about the paper you're looking for:

ConfSpec is a confidence-gated cascaded verification framework for efficient step-level speculative reasoning via confidence-gated verification. The paper addresses how chain-of-thought reasoning significantly improves the performance of large language models on complex tasks, but incurs high inference latency due to long generation traces.

Step-level speculative reasoning aims to mitigate this cost, yet existing approaches face a long-standing trade-off among accuracy, inference speed, and resource efficiency. The key insight is an asymmetry between generation and verification: while generating a correct reasoning step requires substantial model capacity, step-level verification is a constrained discriminative task for which small draft models are well-calibrated.

The paper was submitted to arXiv on January 28, 2026, and is authored by Siran Liu and Cyril Y. He. You can access the full paper and additional details at https://arxiv.org/abs/2602.18447.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b1ab403-fad6-4de0-9463-66c8b563feef",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "afedf0d3-7e26-4c36-b215-2663f87c3eb7",
  "sourceToolAssistantUUID": "4b1ab403-fad6-4de0-9463-66c8b563feef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-09T18:44:23.547Z_

<details><summary>↩ Tool result · `toolu_012aTUCT9rYdeopJq7SQvuEh`</summary>

```text
Web search results for query: "OPT-Tree adaptive draft tree structure speculative decoding"

Links: [{"title":"[2406.17276] OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure","url":"https://arxiv.org/abs/2406.17276"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure - ACL Anthology","url":"https://aclanthology.org/2025.tacl-1.8/"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00735/128189/OPT-Tree-Speculative-Decoding-with-Adaptive-Draft"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure","url":"https://arxiv.org/html/2406.17276"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/article/view/6873"},{"title":"Paper page - OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure","url":"https://huggingface.co/papers/2406.17276"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure","url":"https://aclanthology.org/2025.tacl-1.8.pdf"},{"title":"GitHub - Jikai0Wang/OPT-Tree","url":"https://github.com/Jikai0Wang/OPT-Tree"},{"title":"OPT-Tree/README.md at main · Jikai0Wang/OPT-Tree","url":"https://github.com/Jikai0Wang/OPT-Tree/blob/main/README.md"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/opt-tree-speculative-decoding-adaptive-draft-tree"}]

Based on the search results, here's what I found about OPT-Tree:

## Overview

OPT-Tree is an algorithm to construct adaptive and scalable draft trees designed for speculative decoding, which employs a "draft and then verify" mechanism to allow multiple tokens to be generated in one step, realizing lossless acceleration.

## Key Innovation

Existing methods mainly adopt fixed heuristic draft structures, which fail to adapt to different situations to maximize the acceptance length during verification. OPT-Tree addresses this limitation by searching the optimal tree structure that maximizes the mathematical expectation of the acceptance length in each decoding step.

## Performance

The experimental results are impressive: OPT-Tree outperforms the existing draft structures and achieves a speed-up ratio of up to 3.2 compared with autoregressive decoding. Additionally, if the draft model is powerful enough and the node budget is sufficient, it can generate more than ten tokens in a single step.

## Publication

The work was published in 2025 in Transactions of the Association for Computational Linguistics, volume 13, pages 188–199. The code is available at https://github.com/Jikai0Wang/OPT-Tree.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1d33f85-3101-4df9-adcd-f9a84ea29e1f",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "a1cfaa5e-afd1-44ee-8ad9-c02f5571db61",
  "sourceToolAssistantUUID": "f1d33f85-3101-4df9-adcd-f9a84ea29e1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-09T18:44:24.933Z_

Let me do one more search to look for any papers specifically about ICLR 2026 acceptance on this topic and to verify ThinKV's ICLR status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1cfaa5e-afd1-44ee-8ad9-c02f5571db61",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVLPY5SUJeCUFv4VBtW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f45d975c-e538-4ecd-bf7d-f62f03b0aa5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AyzLZ33gFEH1uvB8G7KZ7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 27213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3600,
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

_source line 35 · 2026-05-09T18:44:25.150Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BMqM6H39g96Ug7kkKjSbfy`</summary>

```json
{
  "query": "ThinKV ICLR 2026 oral poster acceptance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f45d975c-e538-4ecd-bf7d-f62f03b0aa5b",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVLPY5SUJeCUFv4VBtW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eb2a3d3c-f283-4fd1-9196-6af05ad8c0f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AyzLZ33gFEH1uvB8G7KZ7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 27213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3600,
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

_source line 36 · 2026-05-09T18:44:25.289Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RgsongYw4LvszG96UAVLN2`</summary>

```json
{
  "query": "draft model training speculative decoding ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb2a3d3c-f283-4fd1-9196-6af05ad8c0f9",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVLPY5SUJeCUFv4VBtW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf44ce7f-0afb-4abb-b353-29fc832173ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AyzLZ33gFEH1uvB8G7KZ7K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 27213,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3600
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 154,
          "cache_read_input_tokens": 27213,
          "cache_creation_input_tokens": 3600,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3600,
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

_source line 37 · 2026-05-09T18:44:30.345Z_

<details><summary>↩ Tool result · `toolu_01BMqM6H39g96Ug7kkKjSbfy`</summary>

```text
Web search results for query: "ThinKV ICLR 2026 oral poster acceptance"

Links: [{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"2026 Poster Instructions","url":"https://iclr.cc/Conferences/2026/PosterInstructions"},{"title":"ICLR 2026 Accepted Papers: Oral Papers, Research Trends & Top Highlights","url":"https://www.bohrium.com/en/blog/research-notes/iclr-2026-accepted-papers-highlights/"},{"title":"ICLR Oral ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://iclr.cc/virtual/2026/oral/10009981"},{"title":"ICLR.2026 - Oral | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026?group=Oral"},{"title":"ICLR 2026 on X: \"ICLR 2025 decisions and meta-reviews are now available on OpenReview. We reviewed 11,565 submissions, with an overall acceptance rate of 32.08%. Oral/poster decisions will be announced at a later date. Camera ready deadline is March 1st.\" / X","url":"https://x.com/iclr_conf/status/1882140455825297580?lang=en"},{"title":"ICLR 2026 Acceptance Prediction: Tabular ML Approach","url":"https://s-marton.github.io/TabICLR/"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"}]

Based on the search results, I found information about ThinKV at ICLR 2026:

ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models has been accepted as an Oral presentation at ICLR 2026, scheduled for Friday, April 24, 2026 from 11:15 AM – 11:25 AM PDT in the Amphitheater. The paper will also have a poster presentation during Poster Session 3 in Pavilion 3.

The paper is authored by Akshat Ramachandran, Marina Neseem, Charbel Sakr, Rangharajan Venkatesan, Brucek Khailany, and Tushar Krishna. ThinKV is a thought-adaptive KV cache compression framework based on the observation that attention sparsity reveals distinct thought types with varying importance within chain of thought reasoning, and it applies a hybrid quantization–eviction strategy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb2a3d3c-f283-4fd1-9196-6af05ad8c0f9",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "9ffd70d0-6277-4baf-a281-5bf9a4471777",
  "sourceToolAssistantUUID": "eb2a3d3c-f283-4fd1-9196-6af05ad8c0f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-09T18:44:33.050Z_

<details><summary>↩ Tool result · `toolu_01RgsongYw4LvszG96UAVLN2`</summary>

```text
Web search results for query: "draft model training speculative decoding ICLR 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"ICLR Poster Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning","url":"https://iclr.cc/virtual/2026/poster/10010314"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/56d5c6f1a93a7b0590cb4e1c32762d84e42428ae.pdf"},{"title":"Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=IK9cbzzXLt"},{"title":"ICLR Poster Speculative Speculative Decoding","url":"https://iclr.cc/virtual/2026/poster/10008711"},{"title":"Training Domain Draft Models for Speculative Decoding: Best Practices and Insights | OpenReview","url":"https://openreview.net/forum?id=7FBJIxYXxd"},{"title":"SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf/20f1f3685b9fff60c510b3f327fbbde9d5584379.pdf"},{"title":"Published as a workshop paper at SCOPE - ICLR 2025","url":"https://arxiv.org/pdf/2503.07807"},{"title":"TRAINING-FREE LOOSELY SPECULATIVE DECODING","url":"https://openreview.net/pdf/80207abf423159aa729279976811c32dd2f2ea23.pdf"},{"title":"Draft, Verify, \\& Improve: Toward Training-Aware Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=CwvY6TXLxr"}]

Based on the search results, I found several papers related to draft model training and speculative decoding presented at ICLR 2026:

## Key Papers on Draft Model Training and Speculative Decoding at ICLR 2026

**1. Speculative Speculative Decoding (SSD)**
The paper introduces speculative speculative decoding (SSD) to parallelize drafting and verification operations. While a verification is ongoing, the draft model predicts likely verification outcomes and prepares speculations pre-emptively for them. If the actual verification outcome is in the predicted set, a speculation can be returned immediately, eliminating drafting overhead entirely.

**2. Learning To Draft (LTD): Adaptive Speculative Decoding with Reinforcement Learning**
This paper formulates speculative decoding as a reinforcement learning environment and trains two co-adaptive policies to dynamically coordinate the draft and verification phases, encouraging the policies to adapt to each other and explicitly maximize decoding efficiency. The results show that LTD achieves speedup ratios ranging from 2.24x to 4.32x, outperforming the state-of-the-art method Eagle3 up to 36.4%.

**3. Position Specialist Generates Better Draft for Speculative Decoding (POSS)**
The paper proposes Position Specialists (POSS), which consist of multiple position-specialized draft layers to generate tokens at assigned position(s), substantially improving token acceptance rate at later positions within each drafting round.

**4. Draft, Verify, & Improve (DVI)**
DVI is a training-aware self-speculative framework that combines inference with continual online learning. It partitions an LLM into a drafter and a verifier, and during generation, verifier accept/reject decisions are converted into supervision signals and used to update the drafter head.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf44ce7f-0afb-4abb-b353-29fc832173ca",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "8bb61b32-38ff-4bde-a88d-bcffacaec4af",
  "sourceToolAssistantUUID": "bf44ce7f-0afb-4abb-b353-29fc832173ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-09T18:44:34.415Z_

Perfect. Now let me search for one final confirmation on whether any papers specifically address "structure-guided" or "structure-aware" draft training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bb61b32-38ff-4bde-a88d-bcffacaec4af",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVM686n3818L5iC5ojw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "38304f6c-46b9-49b6-847b-7cd50cb3f9b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PZV9h8EWB3eynHoeVNoyQn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 30813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2064,
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

_source line 40 · 2026-05-09T18:44:34.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KH7v6WX2dhB4uCMLqMjxwT`</summary>

```json
{
  "query": "\"structure-guided\" draft speculative decoding reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38304f6c-46b9-49b6-847b-7cd50cb3f9b0",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVM686n3818L5iC5ojw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "be16f054-0c09-4b72-90de-5acd98947803",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PZV9h8EWB3eynHoeVNoyQn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 30813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2064,
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

_source line 41 · 2026-05-09T18:44:34.791Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016uVBbNy7zgnNSzxH7Cn1Ez`</summary>

```json
{
  "query": "\"structure-aware\" draft training speculative 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be16f054-0c09-4b72-90de-5acd98947803",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVM686n3818L5iC5ojw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8fa9bda3-b426-4ffe-bfd9-376fcb02bb93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PZV9h8EWB3eynHoeVNoyQn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 30813,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2064
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 142,
          "cache_read_input_tokens": 30813,
          "cache_creation_input_tokens": 2064,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2064,
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

_source line 42 · 2026-05-09T18:44:41.269Z_

<details><summary>↩ Tool result · `toolu_01KH7v6WX2dhB4uCMLqMjxwT`</summary>

```text
Web search results for query: ""structure-guided" draft speculative decoding reasoning"

Links: [{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00735/128189/OPT-Tree-Speculative-Decoding-with-Adaptive-Draft"},{"title":"Reward-Guided Speculative Decoding for Efficient LLM ...","url":"https://arxiv.org/pdf/2501.19324"},{"title":"ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification","url":"https://arxiv.org/html/2602.18447"},{"title":"Speculative Decoding: A Guide With Implementation Examples | DataCamp","url":"https://www.datacamp.com/tutorial/speculative-decoding"},{"title":"Faster Speculative Decoding via Effective Draft ...","url":"https://aclanthology.org/2025.acl-long.486.pdf"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/pdf/2506.19830"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure - ACL Anthology","url":"https://aclanthology.org/2025.tacl-1.8/"},{"title":"From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning","url":"https://arxiv.org/html/2604.15244"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure","url":"https://arxiv.org/html/2406.17276"}]

Based on the search results, here's what I found about structure-guided draft speculative decoding for reasoning:

## Overview

Speculative decoding employs a "draft and then verify" mechanism to allow multiple tokens to be generated in one step, realizing lossless acceleration.

## Structure-Guided Approaches

Several recent works explore structure-guided approaches to speculative decoding:

### OPT-Tree
OPT-Tree is an algorithm to construct adaptive and scalable draft trees that searches the optimal tree structure which maximizes the mathematical expectation of the acceptance length in each decoding step. Experimental results reveal that OPT-Tree outperforms the existing draft structures and achieves a speed-up ratio of up to 3.2 compared with autoregressive decoding.

### Step-Level Reasoning for Speculative Decoding

Step-level speculative reasoning extends speculative decoding by operating on entire reasoning steps by allowing verification based on semantic equivalence rather than exact token matching, which better aligns with the structure of CoT reasoning.

### Lookahead Reasoning

Reasoning is naturally hierarchical: a full chain-of-thought breaks into discrete steps, and each step unrolls tokens by token, where a reasoning step requires only semantic correctness but not exact token matches.

These structure-guided approaches leverage the inherent structure of reasoning tasks to improve efficiency while maintaining or improving quality compared to token-level speculative decoding alone.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be16f054-0c09-4b72-90de-5acd98947803",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "f6ee9ef1-48a3-412d-a865-0b98241cb0a8",
  "sourceToolAssistantUUID": "be16f054-0c09-4b72-90de-5acd98947803",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-09T18:44:43.358Z_

<details><summary>↩ Tool result · `toolu_016uVBbNy7zgnNSzxH7Cn1Ez`</summary>

```text
Web search results for query: ""structure-aware" draft training speculative 2025 2026"

Links: [{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework | OpenReview","url":"https://openreview.net/forum?id=bKau2NNrji"},{"title":"Draft, Verify, & Improve Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/html/2510.05421v1"},{"title":"[2510.05421] Draft, Verify, and Improve: Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/abs/2510.05421"},{"title":"Recurrent Drafter for Fast Speculative Decoding in Large Language Models - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/recurrent-drafter"},{"title":"Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning","url":"https://arxiv.org/html/2603.01639"},{"title":"GitHub - smart-lty/ParallelSpeculativeDecoding: [ICLR 2025] PEARL: Parallel Speculative Decoding with Adaptive Draft Length · GitHub","url":"https://github.com/smart-lty/parallelspeculativedecoding"},{"title":"Adaptive Speculative Inference","url":"https://www.emergentmind.com/topics/adaptive-speculative-inference"},{"title":"Adaptive Speculative Decoding with Reinforcement Learning","url":"https://arxiv.org/pdf/2603.01639"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.06932v3"}]

I found several recent research papers and systems related to structure-aware draft training in speculative decoding. Here are the key findings from 2025-2026:

## Key Approaches

**Variational Speculative Decoding (VSD)**: Recent work has improved speculative decoding by refining draft model training. For instance, HASS enforces feature consistency to reduce hidden-state mismatches, GRIFFIN resolves token-level misalignment, and EAGLE-3 incorporates training-time rollouts to better mimic decoding.

**CoT-Aware Mixed Framework**: A CoT-aware mixed training framework raises acceptance without altering decoding hyperparameters by combining process-level CoT distillation with feature regression to reduce forward KL divergence and improve step-wise acceptance, and SurpriseRatio (SR), a data-selection metric that anchors the distribution and prevents forgetting.

**Training-Aware Self-Speculation (DVI)**: Draft, Verify, & Improve (DVI), a training-aware self-speculative framework combines inference with continual online learning. It partitions an LLM into a drafter and a verifier, and during generation, verifier accept/reject decisions are converted into supervision signals and used to update the drafter head.

**Adaptive Draft Structure**: Draft structure adaptation adjusts not only the number, but the organizational structure (e.g., tree depth, width, multi-level cascades) of speculative drafts according to context.

**Learning to Draft with RL**: Recent work focuses on dynamically adjusting the size of the draft tree, with approaches that typically rely on simple heuristics or train models to optimize for the metric of acceptance length.

These approaches represent the current frontier of structure-aware training methods for speculative decoding in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fa9bda3-b426-4ffe-bfd9-376fcb02bb93",
  "isSidechain": true,
  "promptId": "f2bd8137-ca32-49e6-98db-d57123b728e0",
  "agentId": "aef1d7efc87249487",
  "type": "user",
  "uuid": "224db0db-e683-4b17-9be0-edef9795a309",
  "sourceToolAssistantUUID": "8fa9bda3-b426-4ffe-bfd9-376fcb02bb93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-09T18:45:10.926Z_

Now I have comprehensive information. Let me compile my findings into a clear report for the user.

## VERIFICATION REPORT: ML PAPER PROPOSAL ON STRUCTURE-GUIDED DRAFT TRAINING

I've completed a thorough search of the literature. Here are my findings on each claim:

### 1. ThinKV (arXiv:2510.01290) - ICLR 2026 Oral

**STATUS: VERIFIED**
- **Existence**: Confirmed. Paper exists on arXiv and is published.
- **ICLR 2026 Oral**: CONFIRMED. Paper accepted as Oral presentation at ICLR 2026 (scheduled Friday, April 24, 2026, 11:15-11:25 AM PDT).
- **Classification Granularity - IMPORTANT FINDING**: ThinKV uses **segment-level** (specifically, "thought-level") classification, NOT token-level. The paper categorizes CoT into three distinct thought types ("Reasoning," "Execution," and "Transition") based on **attention sparsity patterns** measured via kernel density estimates. The compression is applied at the thought/segment level with hybrid quantization-eviction strategies, not at individual token granularity.
- **Key approach**: Applies differential KV cache compression based on thought importance within the CoT, achieving near-lossless compression to <5% of original KV cache size.

Source: [ThinKV arXiv paper](https://arxiv.org/abs/2510.01290), [ICLR 2026 Oral listing](https://iclr.cc/virtual/2026/oral/10009981)

---

### 2. CoT-Aware Speculative Decoding (OpenReview bKau2NNrji)

**STATUS: VERIFIED**
- **Existence**: Confirmed. Paper exists on OpenReview.
- **Full title**: "Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework"
- **What it actually does**: 
  - Shows that training-based SD methods (like EAGLE) suffer from **catastrophic forgetting and distribution shift** under naive CoT supervision
  - Proposes a CoT-aware mixed training framework combining:
    - **Process-level CoT distillation** with feature regression to reduce forward KL divergence
    - **SurpriseRatio (SR)**: A data-selection metric that prevents forgetting using minimal open-domain samples
  - Achieves wall-clock speedups of 3.04× to 4.55× without altering decoding hyperparameters

Source: [OpenReview paper](https://openreview.net/forum?id=bKau2NNrji)

---

### 3. EAGLE-3 (NeurIPS 2025)

**STATUS: VERIFIED**
- **Existence**: Confirmed. Official implementation exists on GitHub.
- **Conference**: Published at NeurIPS 2025 (poster presentation).
- **Key innovation**: 
  - Abandons feature prediction in favor of direct token prediction
  - Replaces top-layer features with **multi-layer feature fusion** ("training-time test")
  - Achieves up to 6.5× speedup (1.4× improvement over EAGLE-2)
  - 1.38× throughput improvement in SGLang framework at batch size 64
  - Merged into mainstream frameworks (vLLM, SGLang)

Source: [GitHub official implementation](https://github.com/SafeAILab/EAGLE), [NeurIPS 2025 poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/119930)

---

### 4. SCoT (arXiv:2504.19095) - Speedups

**STATUS: VERIFIED**
- **Existence**: Confirmed. Paper exists on arXiv.
- **Full title**: "Efficient Reasoning for LLMs through Speculative Chain-of-Thought"
- **Actual reported speedups**:
  - **Average 2.3× and 1.6×** for two target models on reasoning latency
  - More specifically: **48-66% latency reduction** for Deepseek-R1-Distill-Qwen-32B and **21-49% reduction** for Deepseek-R1-Distill-Llama-70B
  - **Key distinction**: SCoT performs **thought-level** (not token-level) speculation, using a lightweight model to generate multiple CoT drafts

Source: [SCoT arXiv paper](https://arxiv.org/abs/2504.19095)

---

### 5. NEW Competing Work on Structural/Semantic-Aware Draft Training (2025-2026)

**IMPORTANT: Multiple competing approaches exist:**

**a) From Tokens to Steps: Verification-Aware Speculative Decoding (arXiv:2604.15244)**
- Introduces **SpecGuard**, a verification-aware framework for **step-level verification**
- Samples multiple draft candidates and selects most consistent step using lightweight ensemble models
- Addresses token-centric limitations where erroneous steps can propagate
- Submitted April 2026

**b) ConfSpec: Efficient Step-Level Speculative Reasoning (arXiv:2602.18447)**
- Confidence-gated cascaded verification framework for **step-level** speculative reasoning
- Key insight: Generation requires substantial capacity, but **step verification is discriminative** task
- Submitted January 2026

**c) OPT-Tree: Adaptive Draft Tree Structure (TACL 2025)**
- Searches optimal tree structure maximizing acceptance length in each step
- Up to 3.2× speedup with adaptive branching factors
- Can generate 10+ tokens per step with sufficient compute budget
- Published in Transactions of the Association for Computational Linguistics

**d) Learning To Draft (LTD): Reinforcement Learning Approach (ICLR 2026 Poster)**
- Formulates speculative decoding as RL with co-adaptive draft/verify policies
- Achieves 2.24-4.32× speedup, outperforms EAGLE-3 by up to 36.4%

**e) Beyond Tokens: Semantic-Aware Speculative Decoding (arXiv:2602.03708)**
- Probes internal model states for semantic probability estimation
- Accepts semantic sequence equivalence instead of token matching
- Up to 2.7× speedup on DeepSeekR1-32B, 2.1× on QwQ-32B

**f) Speculative Speculative Decoding (ICLR 2026 Poster)**
- Parallelizes drafting and verification by predicting verification outcomes
- Draft model pre-emptively generates speculations for predicted outcomes
- Eliminates drafting overhead when predictions match actual outcomes

**g) Draft, Verify, & Improve (DVI): Training-Aware Self-Speculation**
- Uses verifier accept/reject decisions as supervision for continuous drafter updates
- Combines inference with online learning

---

### 6. Markov Chain Models with Speculative Decoding

**FOUND:**
- **SpecDec++**: Formulates speculative decoding as an **MDP framework**
  - Optimal policy takes form of **threshold policy** for stopping speculation
  - Augments draft model with acceptance prediction head
  - Stops speculation when rejection probability exceeds threshold
  
- **Variational Speculative Decoding (VSD)**: Formulates draft training as **variational inference** over latent proposals, maximizing marginal target acceptance probability

Source: [SpecDec++ OpenReview](https://openreview.net/pdf?id=NnExMNiTHw)

---

### 7. "Thought Segment Speculative Decoding"

**FOUND:**
- **SCoT (already mentioned)** performs thought-level speculation
- **Step-level approaches** (ConfSpec, From Tokens to Steps) operate on semantic reasoning steps
- **Lookahead Reasoning**: Entire reasoning steps proposed speculatively with >50% semantic alignment with target model
- Multiple papers reference **hierarchical structure** of CoT (steps→tokens) but distinction between token-level and step-level verification is well-established

---

## CRITICAL ASSESSMENT FOR PROPOSAL NOVELTY

**Key Competing Areas:**

1. **Step-Level/Thought-Level Speculation**: Well-established (SCoT, ConfSpec, SpecGuard) - multiple papers from 2025-2026
2. **Semantic Awareness**: Multiple approaches exist (SemanticSpec, Beyond Tokens, Lookahead Reasoning)
3. **Structure-Guided/Adaptive Structures**: OPT-Tree, Learning To Draft with RL already address draft tree/structure optimization
4. **Training-Aware Draft Models**: CoT-Aware, DVI, VSD all improve draft training with semantic/structural awareness
5. **Step-Level Verification with Internal Signals**: ConfSpec, SpecGuard already implement this

**Potential Novelty Gap:**
The proposal's claimed novelty of "Structure-Guided **Draft Training**" (emphasis on training) may be differentiated if it:
- Specifically optimizes **draft model training** (not just verification) using reasoning structure
- Differs from existing CoT-aware training or RL-based approaches
- Proposes a novel training objective or supervision signal

However, several papers already combine structure-awareness with draft training optimization (DVI, CoT-Aware framework, Learning To Draft).

---

**Sources cited in this report:**
- [ThinKV arXiv](https://arxiv.org/abs/2510.01290)
- [ICLR 2026 Oral ThinKV](https://iclr.cc/virtual/2026/oral/10009981)
- [CoT-Aware Speculative Decoding OpenReview](https://openreview.net/forum?id=bKau2NNrji)
- [EAGLE-3 GitHub](https://github.com/SafeAILab/EAGLE)
- [EAGLE-3 NeurIPS 2025](https://neurips.cc/virtual/2025/loc/san-diego/poster/119930)
- [SCoT arXiv](https://arxiv.org/abs/2504.19095)
- [From Tokens to Steps (SpecGuard) arXiv](https://arxiv.org/abs/2604.15244)
- [ConfSpec arXiv](https://arxiv.org/abs/2602.18447)
- [OPT-Tree TACL](https://aclanthology.org/2025.tacl-1.8/)
- [Learning To Draft ICLR 2026](https://openreview.net/forum?id=IK9cbzzXLt)
- [Beyond Tokens: Semantic-Aware arXiv](https://arxiv.org/html/2602.03708)
- [Speculative Speculative Decoding OpenReview](https://openreview.net/pdf?id=aL1Wnml9Ef)
- [Variational Speculative Decoding arXiv](https://arxiv.org/html/2602.05774v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "224db0db-e683-4b17-9be0-edef9795a309",
  "isSidechain": true,
  "agentId": "aef1d7efc87249487",
  "requestId": "req_011CasVMrCUYRBMam2fdpYLK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8095c274-f812-44c0-a77c-8282cd510698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d544b854-21de-43ec-9cff-7fdef77ddc21",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014G4dnY5TdkqnGqqwQLMMdb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 32877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1951,
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
