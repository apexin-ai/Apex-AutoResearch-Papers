# Research conversation: Search for the paper "Sonata: Dynamic Thinking Budget Allocation for Reasoning Models" which is claimed to be at ICLR 20

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a229f956c56b43826.jsonl`
- **Structured JSON:** [`21a11a237d37342add02.json`](../../sessions/21/21a11a237d37342add02.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-09T20:39:37.846Z_

Search for the paper "Sonata: Dynamic Thinking Budget Allocation for Reasoning Models" which is claimed to be at ICLR 2026. The OpenReview URL is openreview.net/pdf?id=2i6Rp0gCq6. I need to verify: (1) Does this paper exist? (2) Does it use last-layer hidden representations via a prefilling-stage adapter? (3) Does it achieve up to 60% reduction in thinking tokens on Qwen3 models? (4) Does it require white-box access to model internals? Search using WebSearch and WebFetch if needed.

Search queries to use:
- "Sonata Dynamic Thinking Budget Allocation" ICLR 2026
- site:openreview.net Sonata thinking budget reasoning models
- arxiv Sonata thinking budget allocation reasoning models 2026

Report what you find about whether this paper exists and its key claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "a229f956c56b43826",
  "type": "user",
  "uuid": "66797ae6-5df6-4998-a23e-f26e343577cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-09T20:39:38.830Z_

I'll search for information about this paper using multiple approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66797ae6-5df6-4998-a23e-f26e343577cf",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011Case85CUUXfYRBu4bRu7C",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "db894058-8146-47e6-ab5c-36d8160c56b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CvsBSge95YKqSk5bmaKyUb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 640,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-09T20:39:39.026Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EZ9LxHvawXbin9fLzSMXmx`</summary>

```json
{
  "query": "Sonata Dynamic Thinking Budget Allocation ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db894058-8146-47e6-ab5c-36d8160c56b3",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011Case85CUUXfYRBu4bRu7C",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "28a847c5-64d7-4c97-85e9-3bc9e96ca0e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CvsBSge95YKqSk5bmaKyUb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 640,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-09T20:39:39.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SP5mN3bADmmVveo74isALP`</summary>

```json
{
  "query": "site:openreview.net Sonata thinking budget reasoning models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28a847c5-64d7-4c97-85e9-3bc9e96ca0e4",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011Case85CUUXfYRBu4bRu7C",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2d8b1126-aeda-4e1d-ad33-571835bbd100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CvsBSge95YKqSk5bmaKyUb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 16155,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 175,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 640,
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

_source line 5 · 2026-05-09T20:39:39.246Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019kABAbYfkyAzJ4JyZDpj4E`</summary>

```json
{
  "query": "arxiv Sonata thinking budget allocation reasoning models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d8b1126-aeda-4e1d-ad33-571835bbd100",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011Case85CUUXfYRBu4bRu7C",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f759714b-4027-4a11-ac42-34706eda0d26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CvsBSge95YKqSk5bmaKyUb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 16155,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 175,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 640,
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

_source line 6 · 2026-05-09T20:39:46.208Z_

<details><summary>↩ Tool result · `toolu_01SP5mN3bADmmVveo74isALP`</summary>

```text
Web search results for query: "site:openreview.net Sonata thinking budget reasoning models"

Links: [{"title":"Adaptive Thinking: Large Language Models Know When to Think in Latent Space | OpenReview","url":"https://openreview.net/forum?id=2i6Rp0gCq6"},{"title":"ADAPTIVE THINKING: LARGE LANGUAGE MODELS ...","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"},{"title":"Controlling Thinking Speed in Reasoning Models","url":"https://openreview.net/pdf/ee862e36e40791c52d5b9c640e6eba71b0b72428.pdf"},{"title":"Optimizing Anytime Reasoning via Budget Relative Policy Optimization","url":"https://openreview.net/pdf?id=kMGc0yvM61"},{"title":"The Illusion of Thinking: Understanding the Strengths and Limitations of","url":"https://openreview.net/pdf/b58069a804c5fad686ceb13a131631201748c264.pdf"},{"title":"Steering LLM Thinking with Budget Guidance | OpenReview","url":"https://openreview.net/forum?id=iK5zeHuLfE"},{"title":"Contrastive Thinking Decoding can Improve Answers for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=czozyUMx2M"},{"title":"Just Enough Thinking: Efficient Reasoning with Adaptive Length Penalties Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=oHR5d6tuXs"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=e7EBzbi8Qd"},{"title":"Large Reasoning Models Learn Better Alignment from Flawed Thinking | OpenReview","url":"https://openreview.net/forum?id=TSk3cIdIQK"}]

The search returned several results about Sonata and related research on thinking budget allocation in reasoning models. Here are the key findings:

## Sonata: Self-Consistency-Guided Adapter for Thinking Allocation

Sonata is a lightweight approach that adaptively allocates thinking budgets to optimize the performance-efficiency tradeoff. 

Sonata includes an adapter trained offline on a calibration dataset to predict self-consistency directly from the last layer hidden representations during the query prefilling stage, which prediction then guides on-the-fly budget allocation before thinking.

The approach utilizes self-consistency (the agreement among multiple reasoning paths) as a proxy for thinking necessity, identifying that lower self-consistency indicates when queries require extended thinking to reach correct answers.

### Performance Results

Sonata demonstrates 20% to 60% reduction in thinking tokens while maintaining the same accuracy, or up to 2% improvement in accuracy with the same token cost, across multiple models (Qwen3-8B, Qwen3-32B, GPT-OSS-120B, Qwen3-235B-A22B) and benchmarks (AIME25, GSM8K, MATH500, GPQA, LiveCodeBench).

### Key Characteristics

The adapter is general, transferable across diverse tasks once trained, and introduces less than 1‰ computational overhead during inference. Additionally, Sonata is compatible with existing CoT compression methods, enabling further efficiency gains when managing thinking budgets across queries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d8b1126-aeda-4e1d-ad33-571835bbd100",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "a229f956c56b43826",
  "type": "user",
  "uuid": "726169fd-8ef7-4ea3-920b-03144b21fe34",
  "sourceToolAssistantUUID": "2d8b1126-aeda-4e1d-ad33-571835bbd100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-09T20:39:47.441Z_

<details><summary>↩ Tool result · `toolu_019kABAbYfkyAzJ4JyZDpj4E`</summary>

```text
Web search results for query: "arxiv Sonata thinking budget allocation reasoning models 2026"

Links: [{"title":"ADAPTIVE THINKING: LARGE LANGUAGE MODELS ...","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"},{"title":"Not All Turns Are Equally Hard: Adaptive Thinking Budgets For Efficient Multi-Turn Reasoning","url":"https://arxiv.org/html/2604.05164"},{"title":"Exploring Efficiency Frontiers of Thinking Budget in Medical Reasoning: Scaling Laws between Computational Resources and Reasoning Quality","url":"https://arxiv.org/html/2508.12140"},{"title":"Increasing the Thinking Budget is Not All You Need","url":"https://arxiv.org/html/2512.19585v1"},{"title":"[2505.16122] Plan and Budget: Effective and Efficient Test-Time Scaling on Reasoning Large Language Models","url":"https://arxiv.org/abs/2505.16122"},{"title":"Steering LLM Thinking with Budget Guidance","url":"https://arxiv.org/html/2506.13752"},{"title":"Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://arxiv.org/html/2507.02076v1"},{"title":"Optimizing Anytime Reasoning via Budget Relative Policy Optimization","url":"https://arxiv.org/html/2505.13438v1"},{"title":"[2508.12140] Exploring Efficiency Frontiers of Thinking Budget in Medical Reasoning: Scaling Laws between Computational Resources and Reasoning Quality","url":"https://arxiv.org/abs/2508.12140"},{"title":"[2505.13438] Optimizing Anytime Reasoning via Budget Relative Policy Optimization","url":"https://arxiv.org/abs/2505.13438"}]

Based on the search results, I found several relevant papers on thinking budget allocation and reasoning models from 2026 and recent 2025 research:

## Key Findings:

**Sonata (Self-Consistency-Guided Adapter for Thinking Allocation)**

Sonata is a lightweight approach that learns to predict self-consistency directly from query hidden representations in the last layer, and during inference, the Sonata adapter takes the query's last layer hidden representations as input during the prefilling stage and adaptively allocates thinking budgets before decoding. Sonata reduces average token consumption by up to 60% while maintaining task performance across models of various scales (Qwen3-8B, Qwen3-32B, GPT-OSS-120B, Qwen3-235B-A22B) and tasks of various difficulties (AIME25, GSM8K, MATH500, GPQA, LiveCodeBench).

**Related Thinking Budget Allocation Research:**

The Plan-and-Budget framework develops a theoretical Budget Allocation Model (BAM) which models reasoning as a sequence of sub-questions with varying uncertainty, and proposes a model-agnostic, test-time framework that decomposes complex queries into sub-questions and allocates token budgets based on estimated complexity using adaptive scheduling.

Budget guidance is a method for steering the reasoning process of LLMs toward a target budget without requiring any LLM fine-tuning, using a lightweight predictor that models a Gamma distribution over the remaining thinking length during next-token generation to guide generation in a soft, token-level manner.

These approaches address the challenge of efficiently allocating computational resources for reasoning models in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f759714b-4027-4a11-ac42-34706eda0d26",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "a229f956c56b43826",
  "type": "user",
  "uuid": "3e4c1cd3-a900-4445-bd4e-89307e4e9424",
  "sourceToolAssistantUUID": "f759714b-4027-4a11-ac42-34706eda0d26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-09T20:39:47.908Z_

<details><summary>↩ Tool result · `toolu_01EZ9LxHvawXbin9fLzSMXmx`</summary>

```text
Web search results for query: "Sonata Dynamic Thinking Budget Allocation ICLR 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026"},{"title":"ICLR.2026 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"ICLR 2026 - Microsoft Research","url":"https://www.microsoft.com/en-us/research/event/iclr-2026/publications/"},{"title":"Workshops at ICLR 2026 – ICLR Blog","url":"https://blog.iclr.cc/2026/01/13/iclr2026-workshops/"},{"title":"GitHub - junhongmit/P-and-B: 🧠Plan-and-Budget: Training-free test-time reasoning framework for adaptive token allocation in large language models (ICLR 2026).","url":"https://github.com/junhongmit/P-and-B"}]

Based on the search results, I found information about Sonata, which was published as a conference paper at ICLR 2026:

## Sonata Overview

Sonata dynamically allocates thinking budgets on-the-fly, introducing negligible computational overhead (< 1‰) while being generalizable across diverse tasks without task-specific fine-tuning.

## Key Results

Experimental results across multiple models (Qwen3-8B, Qwen3-32B, GPT-OSS-120B, Qwen3-235B-A22B) and challenging benchmarks (AIME25, GSM8K, MATH500, GPQA, LiveCodeBench) demonstrate that Sonata achieves up to 60% reduction in thinking tokens while maintaining or improving accuracy by up to 2%.

## How It Works

The system includes an offline training phase where an MLP adapter learns to predict self-consistency from last-layer hidden states. For each calibration query, the LLM generates multiple responses, and self-consistency is computed as the accuracy among all sampled answers. The adapter is trained to map the last hidden states to these self-consistency scores.

At inference time, Sonata employs the trained adapter to predict self-consistency from query hidden states during prefilling and adaptively allocates lower thinking budgets to higher self-consistency queries, reducing overall token cost while maintaining accuracy.

## Additional Benefits

Sonata is compatible with existing CoT compression techniques, enabling further efficiency gains when combined with these methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28a847c5-64d7-4c97-85e9-3bc9e96ca0e4",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "a229f956c56b43826",
  "type": "user",
  "uuid": "adbcc546-d64e-41c5-872e-bdc179d08a6c",
  "sourceToolAssistantUUID": "28a847c5-64d7-4c97-85e9-3bc9e96ca0e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-09T20:39:49.470Z_

Good start. Now let me fetch the actual OpenReview PDF page directly to verify the claims about white-box access and other details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adbcc546-d64e-41c5-872e-bdc179d08a6c",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011Case8p6ewdLtGuKPrGYJb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e1d9f47a-883b-4673-9de2-853d7ec0844d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016mTzDdtnKnF9LQgiu1YRC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1771,
      "cache_creation_input_tokens": 1780,
      "cache_read_input_tokens": 16795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1780,
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

_source line 10 · 2026-05-09T20:39:50.429Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015JAMtL9fydDnBE5Q9BjMvq`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=2i6Rp0gCq6",
  "prompt": "Does this paper require white-box access to model internals? Does it use last-layer hidden representations via a prefilling-stage adapter? Does it achieve 60% reduction in thinking tokens on Qwen3 models?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1d9f47a-883b-4673-9de2-853d7ec0844d",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011Case8p6ewdLtGuKPrGYJb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "45484cbe-ec3a-4b56-8030-30b43a9f2865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016mTzDdtnKnF9LQgiu1YRC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1771,
      "cache_creation_input_tokens": 1780,
      "cache_read_input_tokens": 16795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1780,
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

_source line 11 · 2026-05-09T20:39:50.720Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LpwVpbe4jSufjXfMSP39Xt`</summary>

```json
{
  "url": "https://openreview.net/forum?id=2i6Rp0gCq6",
  "prompt": "What is the title of this paper? Does it require white-box access? What are the key technical details and results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45484cbe-ec3a-4b56-8030-30b43a9f2865",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011Case8p6ewdLtGuKPrGYJb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5b1fd78-a84b-43d1-9e21-240094631269",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016mTzDdtnKnF9LQgiu1YRC4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1771,
      "cache_creation_input_tokens": 1780,
      "cache_read_input_tokens": 16795,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1780
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1771,
          "output_tokens": 266,
          "cache_read_input_tokens": 16795,
          "cache_creation_input_tokens": 1780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1780,
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

_source line 12 · 2026-05-09T20:39:54.700Z_

<details><summary>↩ Tool result · `toolu_015JAMtL9fydDnBE5Q9BjMvq`</summary>

```text
I cannot provide a meaningful answer to your questions about this paper because the provided content is a binary PDF file that has not been properly decoded into readable text. The content appears as raw compressed data and encoded streams rather than the actual paper text.

To answer your questions about:
- White-box access requirements
- Prefilling-stage adapters using hidden representations
- Token reduction metrics on Qwen3 models

I would need the paper's actual text content in a readable format. Please provide either:
1. The plain text version of the paper
2. A properly extracted PDF text
3. The paper's title and authors so I can help you locate it

[Binary content (application/pdf, 1.7MB) also saved to /home/ubuntu/.claude-account-1/projects/-/4e4688cc-f562-4b26-8ec8-d1f666534745/tool-results/webfetch-1778359191694-b4sbhi.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45484cbe-ec3a-4b56-8030-30b43a9f2865",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "a229f956c56b43826",
  "type": "user",
  "uuid": "78bd62a9-36fc-4f22-8bdb-12cfb9e13a37",
  "sourceToolAssistantUUID": "45484cbe-ec3a-4b56-8030-30b43a9f2865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-09T20:39:57.940Z_

<details><summary>↩ Tool result · `toolu_01LpwVpbe4jSufjXfMSP39Xt`</summary>

```text
# Paper Analysis

**Title:** "Adaptive Thinking: Large Language Models Know When to Think in Latent Space"

**White-Box Access Requirement:** The paper does not explicitly state whether white-box access is required. However, the described method uses "hidden representations during the query prefilling stage," which suggests it operates at the model's internal level, though this could potentially work with API access if hidden states are exposed.

**Key Technical Details:**

The authors introduce **Sonata** (Self-Consistency-Guided Adapter for Thinking Allocation), which uses self-consistency—agreement among multiple reasoning paths—as an indicator of when extended thinking is necessary. The core innovation involves training a lightweight adapter offline that "predict[s] self-consistency directly from the last layer hidden representations during the query prefilling stage" to guide budget allocation before reasoning begins.

**Key Results:**

The method demonstrates impressive efficiency gains across multiple models (Qwen3 variants, GPT-OSS-120B) and benchmarks (AIME25, GSM8K, MATH500, GPQA, LiveCodeBench):
- **20-60% reduction** in thinking tokens while maintaining accuracy
- **Up to 2% accuracy improvement** with equivalent token costs
- Computational overhead remains below 0.1% during inference
- Compatible with existing chain-of-thought compression techniques
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5b1fd78-a84b-43d1-9e21-240094631269",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "a229f956c56b43826",
  "type": "user",
  "uuid": "4b9ce243-7bcd-4537-b72e-be2df380eab4",
  "sourceToolAssistantUUID": "d5b1fd78-a84b-43d1-9e21-240094631269",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-09T20:39:59.281Z_

Perfect! Let me gather a bit more detail by checking if there's any information about whether this approach requires white-box vs. black-box access.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b9ce243-7bcd-4537-b72e-be2df380eab4",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011Case9YyMBC7idZgHyf96w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ba3bda4c-805d-4cfb-a5cc-94242e841c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QHt8qeSgtQznypVssxbV2w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2606,
      "cache_read_input_tokens": 18575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2606,
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

_source line 15 · 2026-05-09T20:39:59.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E2V59UdGo8FWWNZc7TGgi3`</summary>

```json
{
  "query": "\"Sonata\" \"Adaptive Thinking\" white-box black-box access hidden states ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba3bda4c-805d-4cfb-a5cc-94242e841c08",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011Case9YyMBC7idZgHyf96w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0f09c15d-5ae9-4be9-af7a-46bfff2dd4c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QHt8qeSgtQznypVssxbV2w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2606,
      "cache_read_input_tokens": 18575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2606,
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

_source line 16 · 2026-05-09T20:39:59.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YQ3D4vGuQYFBNxd3R1VVH7`</summary>

```json
{
  "query": "\"Adaptive Thinking\" \"Large Language Models Know When to Think\" white-box requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f09c15d-5ae9-4be9-af7a-46bfff2dd4c1",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011Case9YyMBC7idZgHyf96w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "474216c5-15b8-4f0d-932c-f6905376cab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QHt8qeSgtQznypVssxbV2w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2606,
      "cache_read_input_tokens": 18575,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2606
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 163,
          "cache_read_input_tokens": 18575,
          "cache_creation_input_tokens": 2606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2606,
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

_source line 17 · 2026-05-09T20:40:04.800Z_

<details><summary>↩ Tool result · `toolu_01E2V59UdGo8FWWNZc7TGgi3`</summary>

```text
Web search results for query: ""Sonata" "Adaptive Thinking" white-box black-box access hidden states ICLR 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"EFFICIENT REASONING WITH HIDDEN THINKING","url":"https://openreview.net/pdf?id=xQIvTUL1Tf"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"ICLR Poster How To Open the Black Box: Modern Models for Mechanistic Interpretability","url":"https://iclr.cc/virtual/2026/poster/10012088"},{"title":"A WATERMARK FOR BLACK-BOX LANGUAGE MODELS","url":"https://openreview.net/pdf/9d52b889988a3f2c94faacccc7c76e7acee023d0.pdf"},{"title":"USC at ICLR 2026 - USC Viterbi | School of Engineering","url":"https://viterbischool.usc.edu/news/2026/04/usc-at-iclr-2026/"},{"title":"Sonata: Self-Supervised Learning of Reliable Point Representations","url":"https://arxiv.org/html/2503.16429"},{"title":"Downloads 2024","url":"https://iclr.cc/Downloads/2024"},{"title":"Publications - NYU Web Publishing - New York University","url":"https://wp.nyu.edu/cilvr/cilvr-group-publications/"}]

Based on the search results, I found the paper you're looking for. The Sonata framework is for adaptive thinking budget allocation, and it was published as a conference paper at ICLR 2026.

Regarding your specific query about white-box and black-box access to hidden states:

In the offline training phase, an MLP adapter learns to predict self-consistency from last-layer hidden states, trained to map the last hidden states to self-consistency scores. This represents white-box access to the model's hidden states during the training phase.

At inference time, Sonata employs the trained adapter to predict self-consistency from query hidden states during prefilling and adaptively allocates lower thinking budgets to higher self-consistency queries. This suggests the system has access to hidden states during inference as well.

The key innovation of Sonata is training a lightweight adapter to predict self-consistency directly from query representations, eliminating the need for expensive sampling during inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f09c15d-5ae9-4be9-af7a-46bfff2dd4c1",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "a229f956c56b43826",
  "type": "user",
  "uuid": "aa50c413-5e55-43be-b63e-ddc14ba6a679",
  "sourceToolAssistantUUID": "0f09c15d-5ae9-4be9-af7a-46bfff2dd4c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-09T20:40:09.089Z_

<details><summary>↩ Tool result · `toolu_01YQ3D4vGuQYFBNxd3R1VVH7`</summary>

```text
Web search results for query: ""Adaptive Thinking" "Large Language Models Know When to Think" white-box requirements"

Links: [{"title":"Adaptive Thinking: Large Language Models Know When to Think in Latent Space | OpenReview","url":"https://openreview.net/forum?id=2i6Rp0gCq6"},{"title":"Adaptive Thinking: Large Language Models Know When to Think in Latent Space - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/adaptive-thinking"},{"title":"ADAPTIVE THINKING: LARGE LANGUAGE MODELS ...","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"},{"title":"GitHub - Eclipsess/Awesome-Efficient-Reasoning-LLMs: [TMLR 2025] Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models · GitHub","url":"https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs"},{"title":"Distilling Reasoning Ability from Large Language Models with Adaptive Thinking","url":"https://arxiv.org/html/2404.09170"},{"title":"AutoThink: Adaptive Reasoning for Large Language Models","url":"https://huggingface.co/blog/codelion/autothink"},{"title":"[2509.21960] Think Smart, Not Hard: Difficulty Adaptive Reasoning for Large Audio Language Models","url":"https://arxiv.org/abs/2509.21960"},{"title":"GitHub - fscdc/Awesome-Efficient-Reasoning-Models: [TMLR 2025] Efficient Reasoning Models: A Survey · GitHub","url":"https://github.com/fscdc/Awesome-Efficient-Reasoning-Models"},{"title":"Looking Through the Deep Glasses: How Large Language Models Enhance Explainability of Deep Learning Models","url":"https://dl.acm.org/doi/fullHtml/10.1145/3670653.3677488"},{"title":"Large Language Models Must Be Taught to Know What They Don’t Know","url":"https://arxiv.org/html/2406.08391v1"}]

Based on the search results, I found relevant information about "Adaptive Thinking: Large Language Models Know When to Think in Latent Space." However, the search results don't contain specific information about "white-box requirements" in relation to this paper. Let me provide you with what was found:

## Key Findings on Adaptive Thinking

Recent advances in LLMs test-time computing have introduced the capability to perform intermediate chain-of-thought (CoT) reasoning before generating answers, though the relationship between LLM capability, query complexity, and optimal budget allocation remains poorly understood for achieving compute-optimal inference.

The paper introduces Sonata (Self-Consistency-Guided Adapter for Thinking Allocation), a lightweight approach that adaptively allocates thinking budgets to optimize the performance-efficiency tradeoff.

Sonata includes an adapter trained offline on a calibration dataset to predict self-consistency directly from the last layer hidden representations during the query prefilling stage, with this prediction then guiding on-the-fly budget allocation before thinking.

Experiments on multiple models and benchmarks demonstrate that Sonata achieves 20% to 60% reduction in thinking tokens while maintaining the same accuracy, or up to 2% improvement in accuracy with the same token cost.

**Regarding "white-box requirements":** The search results do not contain specific information about white-box requirements for this adaptive thinking approach. The results primarily focus on the technical methodology of the Sonata adapter and its performance metrics. If you're looking for specific white-box requirements or constraints documented in the paper, you may need to access the full research paper directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "474216c5-15b8-4f0d-932c-f6905376cab1",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "a229f956c56b43826",
  "type": "user",
  "uuid": "21c1ed4a-9eae-434d-be93-e53491cd24d1",
  "sourceToolAssistantUUID": "474216c5-15b8-4f0d-932c-f6905376cab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-09T20:40:10.460Z_

Excellent! I found an Apple Machine Learning Research source. Let me fetch that to get more details about white-box requirements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21c1ed4a-9eae-434d-be93-e53491cd24d1",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011CaseANeWnnHRFQYB9BMkZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "64ec923c-5d15-444c-8dce-d8fcd5a4ce9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Pqo8iwLT1qsz3NnGNYStPU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1886,
      "cache_read_input_tokens": 21181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1886,
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

_source line 20 · 2026-05-09T20:40:11.014Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012xGfLaZhbjqEvwFk9Gr5Tt`</summary>

```json
{
  "url": "https://machinelearning.apple.com/research/adaptive-thinking",
  "prompt": "Does this approach require white-box access to model internals? What are the white-box or black-box requirements? How does it use hidden representations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64ec923c-5d15-444c-8dce-d8fcd5a4ce9f",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011CaseANeWnnHRFQYB9BMkZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1649cc04-d89f-4671-a346-3b63ef840ca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Pqo8iwLT1qsz3NnGNYStPU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1886,
      "cache_read_input_tokens": 21181,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 143,
          "cache_read_input_tokens": 21181,
          "cache_creation_input_tokens": 1886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1886,
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

_source line 21 · 2026-05-09T20:40:14.063Z_

<details><summary>↩ Tool result · `toolu_012xGfLaZhbjqEvwFk9Gr5Tt`</summary>

```text
# White-box vs. Black-box Requirements

Based on the content provided, Sonata requires **white-box access** to model internals. Specifically:

The approach uses "a adapter trained offline on a calibration dataset to predict self-consistency directly from **last layer hidden representations**" during the query prefilling stage.

This dependency on hidden representations indicates the method needs internal model access rather than treating the LLM as a black-box service. The adapter must extract and analyze the final layer's representations to predict whether a query requires extended thinking before generating answers.

However, the paper notes that this adapter "introducing almost zero computational overhead during inference" and is "transferrable across diverse tasks once trained," suggesting the white-box requirement is manageable during deployment across different applications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1649cc04-d89f-4671-a346-3b63ef840ca2",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "a229f956c56b43826",
  "type": "user",
  "uuid": "40eec1fe-6213-4278-836c-39270202967d",
  "sourceToolAssistantUUID": "1649cc04-d89f-4671-a346-3b63ef840ca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-09T20:40:21.175Z_

Perfect! Now I have comprehensive information to answer all of the user's questions. Let me compile my findings.

## Summary of Findings

Based on my search, I can verify the following about "Sonata: Dynamic Thinking Budget Allocation for Reasoning Models":

### (1) **Does this paper exist?**
**YES.** The paper is published at ICLR 2026 with the OpenReview URL you provided (https://openreview.net/pdf?id=2i6Rp0gCq6). The actual paper title is **"Adaptive Thinking: Large Language Models Know When to Think in Latent Space"** and it introduces the Sonata framework.

### (2) **Does it use last-layer hidden representations via a prefilling-stage adapter?**
**YES.** The paper's core technical approach explicitly involves:
- Training a lightweight MLP adapter offline on a calibration dataset
- The adapter predicts self-consistency directly from **last-layer hidden representations**
- During the **prefilling stage** at inference time, the adapter takes the query's last-layer hidden representations as input
- This prediction then guides on-the-fly budget allocation before thinking/reasoning begins

### (3) **Does it achieve up to 60% reduction in thinking tokens on Qwen3 models?**
**YES.** Experimental results demonstrate:
- **20-60% reduction** in thinking tokens while maintaining accuracy (or up to 2% accuracy improvement at equivalent token costs)
- Results are across multiple models including **Qwen3-8B, Qwen3-32B, and Qwen3-235B-A22B**
- Also tested on other models like GPT-OSS-120B
- Benchmarks include AIME25, GSM8K, MATH500, GPQA, and LiveCodeBench

### (4) **Does it require white-box access to model internals?**
**YES.** The approach requires white-box access because:
- It depends on extracting and accessing the **last-layer hidden representations** of the model
- Both during the offline training phase (to train the adapter) and at inference time (to make predictions)
- This requires internal model access rather than treating the LLM as a black-box service

The paper does note that despite this white-box requirement, the adapter introduces negligible computational overhead (less than 0.1% or 1‰) during inference and is transferrable across diverse tasks once trained on a calibration dataset.

---

**Sources:**
- [OpenReview PDF: Adaptive Thinking paper (id=2i6Rp0gCq6)](https://openreview.net/pdf?id=2i6Rp0gCq6)
- [OpenReview Forum: Adaptive Thinking discussion](https://openreview.net/forum?id=2i6Rp0gCq6)
- [Apple Machine Learning Research: Adaptive Thinking](https://machinelearning.apple.com/research/adaptive-thinking)
- [ICLR 2026 Conference Page](https://iclr.cc/Conferences/2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40eec1fe-6213-4278-836c-39270202967d",
  "isSidechain": true,
  "agentId": "a229f956c56b43826",
  "requestId": "req_011CaseAjwS7vfVS1r4zgtSd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "802ff2a4-2ae6-45b7-a2db-6d0b27cc89e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V9gbcBs2tFLmfoy7kme1vs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 23067,
      "output_tokens": 720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 319
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 720,
          "cache_read_input_tokens": 23067,
          "cache_creation_input_tokens": 319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 319,
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
