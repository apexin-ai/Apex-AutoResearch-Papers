# Research conversation: Search for and verify these two papers on difficulty-proportional budget allocation: 1. CoBA-RL (arXiv:2602.03048) - "Ca

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5df4a77f21f8f7cb.jsonl`
- **Structured JSON:** [`0467a4e044386e0de0f8.json`](../../sessions/04/0467a4e044386e0de0f8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-12T00:01:47.198Z_

Search for and verify these two papers on difficulty-proportional budget allocation:

1. CoBA-RL (arXiv:2602.03048) - "Capability-Oriented Budget Allocation for RL in LLMs"
   - Does it exist? What does it do exactly?
   - What improvements does it achieve?

2. BranPO (arXiv:2602.03719) - "Training Multi-Turn Search Agent via Contrastive Dynamic Branch Sampling"
   - Does it exist? What does it do exactly?
   - Is code available at github.com/YubaoZhao/BranPO?
   - What improvements does it achieve?

Use WebSearch queries:
- "CoBA-RL capability oriented budget allocation arXiv 2602.03048"
- "BranPO contrastive dynamic branch sampling arXiv 2602.03719"
- "difficulty-aware budget allocation GRPO reinforcement learning"

Use WebFetch on any arXiv pages found. Report all findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "af9703b4-3bac-42ce-9cff-b8fc02975f65",
  "agentId": "a5df4a77f21f8f7cb",
  "type": "user",
  "uuid": "c59f9d34-4352-4a19-9913-fd5c585b0675",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-12T00:01:49.717Z_

I'll search for these two papers and verify their details using the specific queries you provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c59f9d34-4352-4a19-9913-fd5c585b0675",
  "isSidechain": true,
  "agentId": "a5df4a77f21f8f7cb",
  "requestId": "req_011CawhA1bMXTHQ4DX6y64UU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "21ee37f0-3eed-4ec5-953a-4184c6edb17c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014mx195nvt1iTNsPgxLN4Z8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
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

_source line 3 · 2026-05-12T00:01:49.934Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016i3dsDdFaQPbETpysdTn7a`</summary>

```json
{
  "query": "CoBA-RL capability oriented budget allocation arXiv 2602.03048"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21ee37f0-3eed-4ec5-953a-4184c6edb17c",
  "isSidechain": true,
  "agentId": "a5df4a77f21f8f7cb",
  "requestId": "req_011CawhA1bMXTHQ4DX6y64UU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c23407a4-74f6-4949-aa67-64c053f9b6fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014mx195nvt1iTNsPgxLN4Z8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
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

_source line 4 · 2026-05-12T00:01:50.001Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015SrRWqwrJuebhqHLpH7i8J`</summary>

```json
{
  "query": "BranPO contrastive dynamic branch sampling arXiv 2602.03719"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c23407a4-74f6-4949-aa67-64c053f9b6fd",
  "isSidechain": true,
  "agentId": "a5df4a77f21f8f7cb",
  "requestId": "req_011CawhA1bMXTHQ4DX6y64UU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8949b1bd-8db2-43f7-a6ee-d40d8a21ce19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014mx195nvt1iTNsPgxLN4Z8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
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

_source line 5 · 2026-05-12T00:01:50.143Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015qURDNvFutXAt1djdtDjWB`</summary>

```json
{
  "query": "difficulty-aware budget allocation GRPO reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8949b1bd-8db2-43f7-a6ee-d40d8a21ce19",
  "isSidechain": true,
  "agentId": "a5df4a77f21f8f7cb",
  "requestId": "req_011CawhA1bMXTHQ4DX6y64UU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eccfa3e3-4668-45c7-9af1-aabd014d3f01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014mx195nvt1iTNsPgxLN4Z8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
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

_source line 6 · 2026-05-12T00:01:57.937Z_

<details><summary>↩ Tool result · `toolu_015qURDNvFutXAt1djdtDjWB`</summary>

```text
Web search results for query: "difficulty-aware budget allocation GRPO reinforcement learning"

Links: [{"title":"CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs","url":"https://arxiv.org/html/2602.03048"},{"title":"Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/html/2602.01601"},{"title":"Hard Examples Are All You Need: Maximizing GRPO Post-Training Under Annotation BudgetsCode available at https://github.com/Pikus16/grpo_difficulty","url":"https://arxiv.org/html/2508.14094v1"},{"title":"Hard Examples Are All You Need: Maximizing GRPO Post-Training Under Annotation Budgets","url":"https://arxiv.org/html/2508.14094v2"},{"title":"Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://arxiv.org/html/2509.25849v1"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for","url":"https://arxiv.org/pdf/2504.09696"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning ...","url":"https://aclanthology.org/2025.emnlp-main.287.pdf"},{"title":"Budget-Aware GRPO Optimization","url":"https://www.emergentmind.com/topics/budget-aware-training-objectives-grpo"},{"title":"Maximizing Rollout Informativeness under a Fixed Budget: A Submodular View of Tree Search for Tool-Use Agentic Reinforcement Learning","url":"https://arxiv.org/html/2605.05262"},{"title":"Boosting Accuracy and Efficiency of Budget Forcing in LLMs via Reinforcement Learning for Mathematical Reasoning","url":"https://arxiv.org/html/2510.21398"}]

I found several highly relevant papers on difficulty-aware budget allocation in GRPO reinforcement learning. Here are the key findings:

## Overview

Vanilla GRPO overlooks the critical impact of sample difficulty on training value and the corresponding rollout budget. This is a significant problem because complex samples often harbor higher training value and demand extensive exploration, whereas simple instances require minimal resources.

## Key Research Areas

**CoBA-RL (Capability-Oriented Budget Allocation)**: CoBA-RL is a reinforcement learning algorithm designed to adaptively allocate rollout budgets based on the model's evolving capability, utilizing a Capability-Oriented Value function to map tasks to their potential training gains and employing a heap-based greedy strategy to efficiently self-calibrate the distribution of computational resources.

**Knapsack-RL**: This approach views each task's exploration as an "item" with a distinct "value" and "cost", establishing a connection to the classical knapsack problem, which allows deriving an optimal assignment rule that adaptively distributes resources based on the model's current learning status.

**VIP (Variance-Informed Predictive Allocation)**: VIP is a principled training framework for efficient and adaptive rollout allocation in group-based policy optimization, providing theoretical analysis of gradient variance for prominent RL algorithms and establishing the relationship between the gradient variance contributed by a prompt and the probability that it is solved by the current model.

## Effectiveness of Hard Examples

Research shows that selection strategy effectiveness depends critically on task type, with reasoning tasks benefiting from hard examples while knowledge tasks show no such preference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eccfa3e3-4668-45c7-9af1-aabd014d3f01",
  "isSidechain": true,
  "promptId": "af9703b4-3bac-42ce-9cff-b8fc02975f65",
  "agentId": "a5df4a77f21f8f7cb",
  "type": "user",
  "uuid": "9de4640c-e3d1-409a-bd81-778d8f8b0814",
  "sourceToolAssistantUUID": "eccfa3e3-4668-45c7-9af1-aabd014d3f01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-12T00:01:58.051Z_

<details><summary>↩ Tool result · `toolu_015SrRWqwrJuebhqHLpH7i8J`</summary>

```text
Web search results for query: "BranPO contrastive dynamic branch sampling arXiv 2602.03719"

Links: [{"title":"[2602.03719] Training Multi-Turn Search Agent via Contrastive Dynamic Branch Sampling","url":"https://arxiv.org/abs/2602.03719"},{"title":"Training Multi-Turn Search Agent via Contrastive Dynamic Branch Sampling","url":"https://arxiv.org/html/2602.03719"},{"title":"BranchGRPO: Stable and Efficient GRPO with Structured Branching in Diffusion Models","url":"https://arxiv.org/html/2509.06040v1"},{"title":"CLDG: Contrastive Learning on Dynamic Graphs","url":"https://arxiv.org/html/2412.14451v1"},{"title":"Machine Learning","url":"https://web3.arxiv.org/list/cs.LG/recent?skip=65&show=1000"},{"title":"BranchGRPO: Stable and Efficient GRPO with Structured Branching in Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=T2nP2IQasd"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=675&show=2000"},{"title":"Computer Science Aug 2024","url":"https://arxiv.org/list/cs/2024-08?skip=625&show=2000"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=771&show=2000"},{"title":"Machine Learning Jan 2025","url":"https://www.arxiv.org/list/cs.LG/2025-01?skip=850&show=2000"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

## BranPO: Branching Relative Policy Optimization

The paper is titled "Training Multi-Turn Search Agent via Contrastive Dynamic Branch Sampling" by Yubao Zhao and 6 other authors, published in February 2026.

### Key Overview

Agentic reinforcement learning has enabled large language models to perform complex multi-turn planning and tool use, but learning in long-horizon settings remains challenging due to sparse, trajectory-level outcome rewards.

### The BranPO Method

The paper proposes Branching Relative Policy Optimization (BranPO), a value-free method that provides step-level contrastive supervision without dense rewards. Through empirical analysis of search agents, the authors identify a common pattern: performance diverges mainly due to decisions near the tail.

BranPO targets the most critical decision points by recursively truncating and resampling trajectories from the tail, focusing on branches with contrastive outcomes rather than indiscriminately exploring all continuations.

### Additional Features

To further boost efficiency and stabilize training, the method introduces difficulty-aware branch sampling to adapt branching frequency across tasks, and redundant step masking to suppress uninformative actions.

### Results

Extensive experiments on various question answering benchmarks demonstrate that BranPO consistently outperforms strong baselines, achieving significant accuracy gains on long-horizon tasks without increasing the overall training budget.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8949b1bd-8db2-43f7-a6ee-d40d8a21ce19",
  "isSidechain": true,
  "promptId": "af9703b4-3bac-42ce-9cff-b8fc02975f65",
  "agentId": "a5df4a77f21f8f7cb",
  "type": "user",
  "uuid": "b2a087fc-e8ac-4c5e-a287-23862cd837a1",
  "sourceToolAssistantUUID": "8949b1bd-8db2-43f7-a6ee-d40d8a21ce19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-12T00:02:01.504Z_

<details><summary>↩ Tool result · `toolu_016i3dsDdFaQPbETpysdTn7a`</summary>

```text
Web search results for query: "CoBA-RL capability oriented budget allocation arXiv 2602.03048"

Links: [{"title":"[2602.03048] CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs","url":"https://arxiv.org/abs/2602.03048"},{"title":"CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs","url":"https://arxiv.org/html/2602.03048"},{"title":"GitHub - Within-yao/CoBA-RL: CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs · GitHub","url":"https://github.com/Within-yao/CoBA-RL"},{"title":"A Relative-Budget Theory for Reinforcement Learning with Verifiable Rewards in Large Language Model Reasoning","url":"https://arxiv.org/html/2602.01523"},{"title":"𝑉₀: A Generalist Value Model for Any Policy at State Zero","url":"https://arxiv.org/html/2602.03584"},{"title":"[2509.25849v1] Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://arxiv.org/abs/2509.25849v1"},{"title":"CoBA Model: Multi-Domain Algorithmic Innovations","url":"https://www.emergentmind.com/topics/coba-model"},{"title":"DARA: Few-shot Budget Allocation in Online Advertising via In-Context Decision Making with RL-Finetuned LLMs","url":"https://arxiv.org/html/2601.14711v1"},{"title":"Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://arxiv.org/html/2509.25849v1"},{"title":"LLM-as-Judge on a Budget","url":"https://arxiv.org/html/2602.15481v1"}]

I found the paper you're looking for! Here's what the search results show:

CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs (arXiv:2602.03048) was submitted on February 3, 2026, with the latest version (v3) on February 6, 2026.

**Overview:**
The paper addresses Reinforcement Learning with Verifiable Rewards (RLVR) for enhancing LLM reasoning, noting that standard frameworks like Group Relative Policy Optimization (GRPO) typically employ uniform rollout budgets, leading to resource inefficiency.

**Key Contribution:**
CoBA-RL is a reinforcement learning algorithm designed to adaptively allocate rollout budgets based on the model's evolving capability. Specifically, it utilizes a Capability-Oriented Value function to map tasks to their potential training gains and employs a heap-based greedy strategy to efficiently self-calibrate the distribution of computational resources to samples with high training value.

**Authors:**
The paper is authored by Zhiyuan Yao, Yi-Kai Zhang, Yuxin Chen, Yueqing Sun, Zishan Xu, Yu Yang, Tianhao Hu, Qi Gu, Hui Su, and Xunliang Cai.

You can access the paper directly at https://arxiv.org/abs/2602.03048.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c23407a4-74f6-4949-aa67-64c053f9b6fd",
  "isSidechain": true,
  "promptId": "af9703b4-3bac-42ce-9cff-b8fc02975f65",
  "agentId": "a5df4a77f21f8f7cb",
  "type": "user",
  "uuid": "208c6d95-1618-4bda-affd-e5091cf38062",
  "sourceToolAssistantUUID": "c23407a4-74f6-4949-aa67-64c053f9b6fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-12T00:02:03.130Z_

Now let me fetch the arXiv pages for both papers to get more detailed information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "208c6d95-1618-4bda-affd-e5091cf38062",
  "isSidechain": true,
  "agentId": "a5df4a77f21f8f7cb",
  "requestId": "req_011CawhB4jPx8bNDuVAetES4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a64de329-0aaa-4daf-bb5e-c4c612dd324b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019K2h68yF85181B1tTrzRdo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1710,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 16815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1852,
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

_source line 10 · 2026-05-12T00:02:03.712Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GVp6h796siV3Z8goLPYD9y`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03048",
  "prompt": "What are the key improvements and results achieved by CoBA-RL? What are the main experimental findings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a64de329-0aaa-4daf-bb5e-c4c612dd324b",
  "isSidechain": true,
  "agentId": "a5df4a77f21f8f7cb",
  "requestId": "req_011CawhB4jPx8bNDuVAetES4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98b8cb2e-c9fb-433a-b687-5c7dc4970be7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019K2h68yF85181B1tTrzRdo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1710,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 16815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1852,
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

_source line 11 · 2026-05-12T00:02:03.840Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DH8WgRssEaBfFW4hEo7kmn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03719",
  "prompt": "What are the key improvements and results achieved by BranPO? Is code available? What benchmarks were tested?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98b8cb2e-c9fb-433a-b687-5c7dc4970be7",
  "isSidechain": true,
  "agentId": "a5df4a77f21f8f7cb",
  "requestId": "req_011CawhB4jPx8bNDuVAetES4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "857dd437-be2b-4231-9b48-a8d94e93685e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019K2h68yF85181B1tTrzRdo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1710,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 16815,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1710,
          "output_tokens": 212,
          "cache_read_input_tokens": 16815,
          "cache_creation_input_tokens": 1852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1852,
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

_source line 12 · 2026-05-12T00:02:08.009Z_

<details><summary>↩ Tool result · `toolu_01GVp6h796siV3Z8goLPYD9y`</summary>

```text
# CoBA-RL Key Improvements and Results

## Main Improvements

CoBA-RL addresses inefficiencies in standard reinforcement learning frameworks by introducing adaptive budget allocation. Rather than using uniform rollout budgets like Group Relative Policy Optimization (GRPO), this approach dynamically allocates computational resources based on the model's evolving capabilities.

The method employs two key innovations:
1. A Capability-Oriented Value function that maps tasks to their potential training value
2. A heap-based greedy strategy for efficiently distributing resources to high-value samples

## Experimental Findings

According to the abstract, the research demonstrates that CoBA-RL achieves:

> "consistent generalization improvements across multiple challenging benchmarks"

The authors emphasize that their findings reveal that "quantifying sample training value and optimizing budget allocation are pivotal for advancing LLM post-training efficiency."

The algorithm successfully orchestrates the balance between exploration and exploitation, moving beyond instance-level metrics like task pass rates to better capture the model's dynamic learning state—a limitation of previous adaptive methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98b8cb2e-c9fb-433a-b687-5c7dc4970be7",
  "isSidechain": true,
  "promptId": "af9703b4-3bac-42ce-9cff-b8fc02975f65",
  "agentId": "a5df4a77f21f8f7cb",
  "type": "user",
  "uuid": "d0dec2eb-adad-4896-abe6-d150519e9adf",
  "sourceToolAssistantUUID": "98b8cb2e-c9fb-433a-b687-5c7dc4970be7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:02:08.199Z_

<details><summary>↩ Tool result · `toolu_01DH8WgRssEaBfFW4hEo7kmn`</summary>

```text
# BranPO: Key Improvements and Results

## Core Improvements

BranPO addresses long-horizon training challenges through several innovations:

- **Contrastive Learning**: The method "truncates trajectories near the tail and resamples alternative continuations" to create contrasting suffixes over shared prefixes
- **Efficiency Enhancements**: Introduces difficulty-aware branch sampling and redundant step masking to stabilize training without increasing computational costs
- **Value-Free Approach**: Provides step-level supervision without requiring dense rewards

## Results

The research demonstrates that BranPO achieves "significant accuracy gains on long-horizon tasks" across question-answering benchmarks, consistently outperforming baseline methods.

## Code Availability

**Yes**, code is available. The authors state: "Our code is available at" a GitHub repository (YubaoZhao/BranPO).

## Benchmarks Tested

The paper evaluates performance on "various question answering benchmarks," though the specific benchmark names are not detailed in the abstract provided. The abstract emphasizes that improvements occur "without increasing the overall training budget."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "857dd437-be2b-4231-9b48-a8d94e93685e",
  "isSidechain": true,
  "promptId": "af9703b4-3bac-42ce-9cff-b8fc02975f65",
  "agentId": "a5df4a77f21f8f7cb",
  "type": "user",
  "uuid": "f4366fb9-9b18-461c-9ed8-ebb8f97347fe",
  "sourceToolAssistantUUID": "857dd437-be2b-4231-9b48-a8d94e93685e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-12T00:02:09.418Z_

Let me verify the GitHub repository for BranPO:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4366fb9-9b18-461c-9ed8-ebb8f97347fe",
  "isSidechain": true,
  "agentId": "a5df4a77f21f8f7cb",
  "requestId": "req_011CawhBZK6yzKrSuCiYipBJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "916acbd5-b140-4e75-88f0-f40bca95d510",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MPFaykHcDwcM3kr8Pnpdva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2457,
      "cache_read_input_tokens": 18667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2457,
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

_source line 15 · 2026-05-12T00:02:09.587Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FWeB2TRn9XGUcAR4Lg5BZL`</summary>

```json
{
  "query": "github.com/YubaoZhao/BranPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "916acbd5-b140-4e75-88f0-f40bca95d510",
  "isSidechain": true,
  "agentId": "a5df4a77f21f8f7cb",
  "requestId": "req_011CawhBZK6yzKrSuCiYipBJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "448f308d-7fa6-44d3-bc91-c9f31bef82d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MPFaykHcDwcM3kr8Pnpdva",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2457,
      "cache_read_input_tokens": 18667,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2457
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 79,
          "cache_read_input_tokens": 18667,
          "cache_creation_input_tokens": 2457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2457,
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

_source line 16 · 2026-05-12T00:02:14.944Z_

<details><summary>↩ Tool result · `toolu_01FWeB2TRn9XGUcAR4Lg5BZL`</summary>

```text
Web search results for query: "github.com/YubaoZhao/BranPO"

Links: [{"title":"GitHub - YubaoZhao/BranPO: Training Multi-Turn Search Agent via Contrastive Branch Sampling","url":"https://github.com/YubaoZhao/BranPO"},{"title":"GitHub - YubaoZhao/ECG-Chat: A Large ECG-Language Model for Cardiac Disease Diagnosis","url":"https://github.com/YubaoZhao/ECG-Chat"},{"title":"Ghostty Is Leaving GitHub – Mitchell Hashimoto","url":"https://mitchellh.com/writing/ghostty-leaving-github"},{"title":"A mudança é constante. O GitHub mantém você à frente.","url":"https://github.com/"},{"title":"Explore GitHub · GitHub","url":"https://github.com/explore?imz_s=hkm8trci1g55pa4ukqg1c67866"},{"title":"GitHub RCE Vulnerability: CVE-2026-3854 Breakdown | Wiz Blog","url":"https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854"},{"title":"Home | B00MERANG","url":"https://b00merang-project.github.io/"},{"title":"banghuazhao (Banghua Zhao) · GitHub","url":"https://github.com/banghuazhao"},{"title":"yubozhao (Bozhao) · GitHub","url":"https://github.com/yubozhao"},{"title":"zhuang2002 (Junhao Zhuang (庄俊豪)) · GitHub","url":"https://github.com/zhuang2002"}]

Based on the search results, here's what I found about the BranPO repository:

BranPO provides scripts for both GRPO and BranPO in ./train_grpo.sh and ./train_branpo.sh, respectively. The repository is titled "Training Multi-Turn Search Agent via Contrastive Branch Sampling."

The codebase is built upon rLLM and veRL, with the search workflow and training data based on Search-R1 and ASearcher.

The repository includes setup instructions for working with retrieval and training environments. To evaluate the model, you can run run_eval.sh to test against the local retrieval server, and then execute run_llm_as_a_judge.sh to perform the LLM-as-a-Judge evaluation.

The project appears to focus on training multi-turn search agents with specific emphasis on contrastive branch sampling techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "448f308d-7fa6-44d3-bc91-c9f31bef82d6",
  "isSidechain": true,
  "promptId": "af9703b4-3bac-42ce-9cff-b8fc02975f65",
  "agentId": "a5df4a77f21f8f7cb",
  "type": "user",
  "uuid": "cb3f85ed-3a76-44c1-89ad-a5447df76fd7",
  "sourceToolAssistantUUID": "448f308d-7fa6-44d3-bc91-c9f31bef82d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-12T00:02:25.712Z_

## Findings Report

### Paper 1: CoBA-RL (arXiv:2602.03048)

**Status: CONFIRMED - Paper exists**

**Full Title:** "Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs"

**What it does:**
- Addresses inefficiency in standard GRPO (Group Relative Policy Optimization) which uses uniform rollout budgets
- Introduces an adaptive budget allocation algorithm that dynamically allocates computational resources based on the model's evolving capabilities
- Uses a Capability-Oriented Value function to map tasks to their potential training value
- Employs a heap-based greedy strategy to efficiently distribute resources to high-value samples

**Key Improvements Achieved:**
- Consistent generalization improvements across multiple challenging benchmarks
- Moves beyond instance-level metrics (like task pass rates) to better capture the model's dynamic learning state
- Quantifies sample training value and optimizes budget allocation for improved LLM post-training efficiency
- Successfully balances exploration and exploitation in resource allocation

**Authors:** Zhiyuan Yao, Yi-Kai Zhang, Yuxin Chen, Yueqing Sun, Zishan Xu, Yu Yang, Tianhao Hu, Qi Gu, Hui Su, and Xunliang Cai

**Code availability:** Yes - Available at [GitHub - Within-yao/CoBA-RL](https://github.com/Within-yao/CoBA-RL)

---

### Paper 2: BranPO (arXiv:2602.03719)

**Status: CONFIRMED - Paper exists**

**Full Title:** "Training Multi-Turn Search Agent via Contrastive Dynamic Branch Sampling"

**What it does:**
- Proposes Branching Relative Policy Optimization (BranPO), a value-free method for long-horizon reinforcement learning in LLMs
- Provides step-level contrastive supervision without requiring dense rewards
- Uses trajectory truncation and resampling near the tail to create contrasting suffixes over shared prefixes
- Focuses training on the most critical decision points by recursively truncating and resampling trajectories
- Incorporates difficulty-aware branch sampling to adapt branching frequency across tasks
- Uses redundant step masking to suppress uninformative actions and stabilize training

**Key Improvements Achieved:**
- Significant accuracy gains on long-horizon question-answering tasks
- Consistently outperforms strong baselines
- Achieves improvements without increasing overall training budget
- Addresses the sparse, trajectory-level reward problem in agentic RL

**Code Availability:** YES - Confirmed available at [GitHub - YubaoZhao/BranPO](https://github.com/YubaoZhao/BranPO)

**Implementation Details:**
- Built upon rLLM and veRL frameworks
- Training workflow and data based on Search-R1 and ASearcher
- Provides ./train_grpo.sh and ./train_branpo.sh scripts
- Includes evaluation scripts (run_eval.sh and run_llm_as_a_judge.sh)

---

## Connection to Difficulty-Proportional Budget Allocation

Both papers are part of a broader research trend in difficulty-aware resource allocation for GRPO-based RL:
- **CoBA-RL** focuses on capability-oriented budget allocation at the instance level
- **BranPO** incorporates difficulty-aware branch sampling within its trajectory resampling strategy

Other related work in this area includes Knapsack-RL and VIP (Variance-Informed Predictive Allocation), which also address adaptive rollout allocation based on task characteristics.

---

**Sources:**
- [CoBA-RL arXiv Abstract](https://arxiv.org/abs/2602.03048)
- [CoBA-RL arXiv HTML](https://arxiv.org/html/2602.03048)
- [CoBA-RL GitHub](https://github.com/Within-yao/CoBA-RL)
- [BranPO arXiv Abstract](https://arxiv.org/abs/2602.03719)
- [BranPO arXiv HTML](https://arxiv.org/html/2602.03719)
- [BranPO GitHub](https://github.com/YubaoZhao/BranPO)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb3f85ed-3a76-44c1-89ad-a5447df76fd7",
  "isSidechain": true,
  "agentId": "a5df4a77f21f8f7cb",
  "requestId": "req_011CawhC49SsztV34iWHULJm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "19b6ccc6-9d6f-4680-b645-957c0bbe3fd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "74f7aea8-32c7-4108-99f3-3a636c0291d1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJ8RR7nfsb8Pb9kAJnJxT1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 21124,
      "output_tokens": 1014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 741
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1014,
          "cache_read_input_tokens": 21124,
          "cache_creation_input_tokens": 741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 741,
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
