# Research conversation: I need to deeply research the paper "Stratified GRPO" (arXiv:2510.06214). This is claimed to be titled "Stratified GRPO:

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9e76bf4de50fb468.jsonl`
- **Structured JSON:** [`267e0106bdaa0c6433ef.json`](../../sessions/26/267e0106bdaa0c6433ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-11T23:28:59.349Z_

I need to deeply research the paper "Stratified GRPO" (arXiv:2510.06214). This is claimed to be titled "Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents" proposing Stratified Advantage Normalization (SAN).

Please:
1. Use WebSearch to find this paper with queries like "Stratified GRPO arXiv 2510.06214", "stratified advantage normalization GRPO", "structural heterogeneity reinforcement learning LLM"
2. Use WebFetch to read the actual paper abstract and method sections from arxiv.org
3. Search for follow-up work or related papers on stratified normalization in GRPO

I need to understand:
- What are the "strata" they use? How do they partition trajectories?
- What is SAN (Stratified Advantage Normalization) exactly?
- What problem does it solve? Why is within-group normalization insufficient?
- What benchmarks/tasks do they evaluate on?
- How is this different from standard GRPO group normalization?
- Is this published at a venue or just arXiv?

Report all findings in detail. If the paper doesn't exist at that arXiv ID, report that clearly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "7b9a442b-6d31-4a3b-b50b-5f6845e6c47c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:28:59.351Z_

```json
{
  "parentUuid": "7b9a442b-6d31-4a3b-b50b-5f6845e6c47c",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
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
  "uuid": "50cdbb8f-47f7-44b2-8adb-81ffd79834f2",
  "timestamp": "2026-05-11T23:28:59.351Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:29:01.985Z_



I'll research this paper systematically. Let me start by loading the necessary tools and searching for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50cdbb8f-47f7-44b2-8adb-81ffd79834f2",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011Caweex8hooAo1Wf9H9wEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "313c3e81-4930-40b3-91f5-8d8262b8e0ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8x9neQCtAZ1sHHHE5US3H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 846,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 846,
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

_source line 4 · 2026-05-11T23:29:02.256Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NcMgEaW85H2aMf1rj81x6G`</summary>

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
  "parentUuid": "313c3e81-4930-40b3-91f5-8d8262b8e0ba",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011Caweex8hooAo1Wf9H9wEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bd7c6f7-c7bf-493f-81b8-8a00c0cf1d5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8x9neQCtAZ1sHHHE5US3H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 846,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 846,
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

_source line 5 · 2026-05-11T23:29:02.258Z_

<details><summary>↩ Tool result · `toolu_01NcMgEaW85H2aMf1rj81x6G`</summary>

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
  "parentUuid": "4bd7c6f7-c7bf-493f-81b8-8a00c0cf1d5e",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "8678807c-014a-4068-bba7-966b2c38a69c",
  "sourceToolAssistantUUID": "4bd7c6f7-c7bf-493f-81b8-8a00c0cf1d5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:29:04.839Z_



Now let me search for this paper using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8678807c-014a-4068-bba7-966b2c38a69c",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawefBAXbwqkHkKBh2wMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10d20ac8-d388-4021-ae9d-b60d57a3802a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAX3BU6SW1J1ebtE29fayj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 7 · 2026-05-11T23:29:05.917Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0127VDThZYV6kr7ps3MjrpBd`</summary>

```json
{
  "query": "Stratified GRPO arXiv 2510.06214"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10d20ac8-d388-4021-ae9d-b60d57a3802a",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawefBAXbwqkHkKBh2wMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4658a32-ec48-4103-b178-83dcf36a2087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAX3BU6SW1J1ebtE29fayj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 8 · 2026-05-11T23:29:06.379Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D1bEhR7cx7ai5rtpFCPHAB`</summary>

```json
{
  "query": "stratified advantage normalization GRPO reinforcement learning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4658a32-ec48-4103-b178-83dcf36a2087",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawefBAXbwqkHkKBh2wMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbbb72e8-fab4-4037-b286-17b6f78a21a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAX3BU6SW1J1ebtE29fayj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 9 · 2026-05-11T23:29:06.907Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XEkBgd446wpM8wSPp7fLdc`</summary>

```json
{
  "query": "\"structural heterogeneity\" \"reinforcement learning\" LLM search agents stratified normalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbbb72e8-fab4-4037-b286-17b6f78a21a2",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawefBAXbwqkHkKBh2wMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d40178c6-e167-4de2-8e67-52506d337f82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAX3BU6SW1J1ebtE29fayj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9069,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1912
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 184,
          "cache_read_input_tokens": 9069,
          "cache_creation_input_tokens": 1912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1912,
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

_source line 10 · 2026-05-11T23:29:12.963Z_

<details><summary>↩ Tool result · `toolu_01D1bEhR7cx7ai5rtpFCPHAB`</summary>

```text
Web search results for query: "stratified advantage normalization GRPO reinforcement learning LLM"

Links: [{"title":"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://arxiv.org/html/2510.06214"},{"title":"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents | OpenReview","url":"https://openreview.net/forum?id=hqnGfzQQfa"},{"title":"[2510.06214] Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://arxiv.org/abs/2510.06214"},{"title":"(PDF) Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://www.researchgate.net/publication/396292051_Stratified_GRPO_Handling_Structural_Heterogeneity_in_Reinforcement_Learning_of_LLM_Search_Agents"},{"title":"Blockwise Advantage Estimation for Multi-Objective RL with Verifiable Rewards","url":"https://arxiv.org/html/2602.10231"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"From REINFORCE to Dr. GRPO","url":"https://lancelqf.github.io/note/llm_post_training/"},{"title":"Understanding GRPO and how GRPO is changing LLM Training | Adaline","url":"https://www.adaline.ai/blog/understanding-grpo"},{"title":"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients","url":"https://arxiv.org/html/2601.23135"},{"title":"GDPO Explained: How NVIDIA Fixes GRPO for Multi-Reward LLM Reinforcement Learning - AI Papers Academy","url":"https://aipapersacademy.com/gdpo/"}]

I found comprehensive information about stratified advantage normalization and GRPO. Here's what the search reveals:

## Overview

Stratified GRPO addresses structural heterogeneity by using Stratified Advantage Normalization (SAN), a principled advantage estimator designed for heterogeneous action spaces.

## The Problem It Addresses

The trajectories of search agents are structurally heterogeneous, where variations in the number, placement, and outcomes of search calls lead to fundamentally different answer directions and reward distributions. Standard policy gradient methods, which use a single global baseline, suffer from cross-stratum bias—an "apples-to-oranges" comparison of heterogeneous trajectories.

## The Solution: Stratified Advantage Normalization

The core idea partitions trajectories into homogeneous strata based on their structural properties (e.g., the number of search calls), and then computes advantages within each stratum. By construction, SAN is free from cross-stratum bias, ensuring that each trajectory is evaluated only against its true peers.

## Theoretical Properties

SAN eliminates cross-stratum bias and is conditionally unbiased and has unit variance within each stratum. Crucially, SAN achieves these superior conditional properties while preserving the global unbiasedness and unit variance of standard normalization, yielding a more pure and scale-stable learning signal.

## Empirical Results

Stratified GRPO substantially outperforms GRPO by up to 11.3 points on diverse single-hop and multi-hop question-answering benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbbb72e8-fab4-4037-b286-17b6f78a21a2",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "b84a7761-dbe6-4134-ac55-145dd82fd665",
  "sourceToolAssistantUUID": "cbbb72e8-fab4-4037-b286-17b6f78a21a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-11T23:29:13.225Z_

<details><summary>↩ Tool result · `toolu_0127VDThZYV6kr7ps3MjrpBd`</summary>

```text
Web search results for query: "Stratified GRPO arXiv 2510.06214"

Links: [{"title":"[2510.06214] Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://arxiv.org/abs/2510.06214"},{"title":"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://arxiv.org/html/2510.06214"},{"title":"Preprint. STRATIFIED GRPO: HANDLING STRUCTURAL HET-","url":"https://arxiv.org/pdf/2510.06214"},{"title":"Hybrid Reinforcement:When Reward Is Sparse, It’s Better to Be Dense","url":"https://arxiv.org/html/2510.07242v1"},{"title":"Training-Free Group Relative Policy Optimization","url":"https://arxiv.org/html/2510.08191v1"},{"title":"(PDF) Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://www.researchgate.net/publication/396292051_Stratified_GRPO_Handling_Structural_Heterogeneity_in_Reinforcement_Learning_of_LLM_Search_Agents"},{"title":"[2510.01982v1] $\\text{G}^2$RPO: Granular GRPO for Precise Reward in Flow Models","url":"https://arxiv.org/abs/2510.01982v1"},{"title":"[2510.02654] Smart-GRPO: Smartly Sampling Noise for Efficient RL of Flow-Matching Models","url":"https://arxiv.org/abs/2510.02654"},{"title":"𝜆-GRPO: Unifying the GRPO Frameworks with Learnable Token Preferences","url":"https://arxiv.org/html/2510.06870v2"},{"title":"It Takes Two: Your GRPO Is Secretly DPO","url":"https://arxiv.org/pdf/2510.00977"}]

I found comprehensive information about the paper. Here are the key details about Stratified GRPO (arXiv 2510.06214):

## Overview

Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents is a research paper that addresses a fundamental problem in training LLM search agents.

## The Problem

Large language model (LLM) agents increasingly rely on external tools such as search engines to solve complex, multi-step problems, and reinforcement learning (RL) has become a key paradigm for training them. However, the trajectories of search agents are structurally heterogeneous, where variations in the number, placement, and outcomes of search calls lead to fundamentally different answer directions and reward distributions.

Standard policy gradient methods, which use a single global baseline, suffer from what we identify and formalize as cross-stratum bias—an "apples-to-oranges" comparison of heterogeneous trajectories. This cross-stratum bias distorts credit assignment and hinders exploration of complex, multi-step search strategies.

## The Solution

To address this, we propose Stratified GRPO, whose central component, Stratified Advantage Normalization (SAN), partitions trajectories into homogeneous strata based on their structural properties and computes advantages locally within each stratum. This ensures that trajectories are evaluated only against their true peers.

## Results

Extensive experiments on diverse single-hop and multi-hop question-answering benchmarks demonstrate that Stratified GRPO consistently and substantially outperforms GRPO by up to 11.3 points, achieving higher training rewards, greater training stability


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4658a32-ec48-4103-b178-83dcf36a2087",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "ead7e191-9074-449f-ba95-6a3f52250807",
  "sourceToolAssistantUUID": "d4658a32-ec48-4103-b178-83dcf36a2087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:29:14.384Z_

<details><summary>↩ Tool result · `toolu_01XEkBgd446wpM8wSPp7fLdc`</summary>

```text
Web search results for query: ""structural heterogeneity" "reinforcement learning" LLM search agents stratified normalization"

Links: [{"title":"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://arxiv.org/html/2510.06214"},{"title":"[2510.06214] Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://arxiv.org/abs/2510.06214"},{"title":"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents | OpenReview","url":"https://openreview.net/forum?id=hqnGfzQQfa"},{"title":"(PDF) Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://www.researchgate.net/publication/396292051_Stratified_GRPO_Handling_Structural_Heterogeneity_in_Reinforcement_Learning_of_LLM_Search_Agents"},{"title":"Preprint. STRATIFIED GRPO: HANDLING STRUCTURAL HET-","url":"https://arxiv.org/pdf/2510.06214"},{"title":"GitHub - PKU-MARL/HARL: Official implementation of HARL algorithms based on PyTorch. · GitHub","url":"https://github.com/PKU-MARL/HARL"},{"title":"Heterogeneous Group-Based Reinforcement Learning for LLM-based Multi-Agent Systems","url":"https://arxiv.org/html/2506.02718v1"},{"title":"GitHub - TsinghuaC3I/MARTI: A Framework for LLM-based Multi-Agent Reinforced Training and Inference · GitHub","url":"https://github.com/TsinghuaC3I/MARTI"},{"title":"[2506.02718] End-to-End Optimization of LLM-Driven Multi-Agent Search Systems via Heterogeneous-Group-Based Reinforcement Learning","url":"https://arxiv.org/abs/2506.02718"},{"title":"[2512.18892] Structural Reinforcement Learning for Heterogeneous Agent Macroeconomics","url":"https://arxiv.org/abs/2512.18892"}]

I found highly relevant research on your search topic. The results center on a recent paper titled "Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents," which directly addresses all the key concepts you mentioned.

## Key Findings

Large language model (LLM) agents increasingly rely on external tools such as search engines to solve complex, multi-step problems, and reinforcement learning (RL) has become a key paradigm for training them. However, the trajectories of search agents are structurally heterogeneous, where variations in the number, placement, and outcomes of search calls lead to fundamentally different answer directions and reward distributions.

Standard policy gradient methods, which use a single global baseline, suffer from what researchers identify and formalize as cross-stratum bias—an "apples-to-oranges" comparison of heterogeneous trajectories. This cross-stratum bias distorts credit assignment and hinders exploration of complex, multi-step search strategies.

## The Proposed Solution

To address this, researchers propose Stratified GRPO, whose central component, Stratified Advantage Normalization (SAN), partitions trajectories into homogeneous strata based on their structural properties and computes advantages locally within each stratum.

Extensive experiments on diverse single-hop and multi-hop question-answering benchmarks demonstrate that Stratified GRPO consistently and substantially outperforms GRPO by up to 11.3 points, achieving higher training rewards, greater training stability, and more effective search policies.

The paper was published in October 2025 and represents a significant advancement in addressing structural heterogeneity challenges in reinforcement learning for LLM-based search agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d40178c6-e167-4de2-8e67-52506d337f82",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "fdf52149-62f9-4b93-9260-36b45a8796f3",
  "sourceToolAssistantUUID": "d40178c6-e167-4de2-8e67-52506d337f82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-11T23:29:17.972Z_

The paper exists and is confirmed at arXiv:2510.06214. I also see it has an OpenReview page. Let me now fetch the detailed content from multiple sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdf52149-62f9-4b93-9260-36b45a8796f3",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011Caweg4QWP2s7b7syTexNv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4230d185-3977-4c3f-ac9d-3b6127bba1a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaQpiGoe3M5kufw6Zhq2fG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3084,
      "cache_read_input_tokens": 10981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3084,
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

_source line 14 · 2026-05-11T23:29:19.937Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KjexkpGKpB3sHFU7jVaF8v`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.06214",
  "prompt": "Extract ALL information from this page: full title, all authors, submission date, abstract in full, any comments about venue/publication, categories, and any other metadata."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4230d185-3977-4c3f-ac9d-3b6127bba1a5",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011Caweg4QWP2s7b7syTexNv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17c30c35-7d30-4537-9827-908784610c25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaQpiGoe3M5kufw6Zhq2fG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3084,
      "cache_read_input_tokens": 10981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3084,
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

_source line 15 · 2026-05-11T23:29:24.484Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TYL57B763wjSYwwpJNiYXu`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.06214",
  "prompt": "Extract the FULL content of the paper, focusing on: 1) The complete abstract, 2) The Introduction section explaining the motivation and problem, 3) The Method/Approach section explaining Stratified GRPO and SAN (Stratified Advantage Normalization) in detail - especially how strata are defined, the mathematical formulation, and how advantages are computed within strata, 4) What is \"cross-stratum bias\" exactly and how is it formalized, 5) How does SAN differ from standard GRPO normalization, 6) The experimental setup - what benchmarks, what base models, what baselines, 7) Key results and ablations, 8) Any theoretical properties proved about SAN. Extract as much technical detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17c30c35-7d30-4537-9827-908784610c25",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011Caweg4QWP2s7b7syTexNv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8a9c52d-8196-40a9-af32-2b8eef197444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaQpiGoe3M5kufw6Zhq2fG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3084,
      "cache_read_input_tokens": 10981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3084,
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

_source line 16 · 2026-05-11T23:29:25.162Z_

<details><summary>↩ Tool result · `toolu_01KjexkpGKpB3sHFU7jVaF8v`</summary>

```text
# Research Paper Metadata Summary

**Full Title:**
"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents"

**Authors:**
- Mingkang Zhu
- Xi Chen
- Bei Yu
- Hengshuang Zhao
- Jiaya Jia

**Submission Date:**
October 7, 2025

**arXiv Identifier:**
2510.06214 (cs.LG)

**Categories:**
Machine Learning (cs.LG), Artificial Intelligence (cs.AI), Computation and Language (cs.CL)

**Abstract Summary:**
The paper addresses training challenges for LLM agents using external search tools. The core issue identified is "cross-stratum bias"—when standard policy gradient methods compare structurally different trajectories using a single baseline. The authors propose Stratified GRPO with Stratified Advantage Normalization (SAN), which groups trajectories by structural properties and evaluates each group independently. They report improvements of up to 11.3 points over standard GRPO on question-answering benchmarks.

**Publication Status:**
Preprint (no venue/publication information listed)

**DOI:**
https://doi.org/10.48550/arXiv.2510.06214

**License:**
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17c30c35-7d30-4537-9827-908784610c25",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "81c4090e-6cb8-4ba0-ae90-e375368a7cb1",
  "sourceToolAssistantUUID": "17c30c35-7d30-4537-9827-908784610c25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-11T23:29:25.797Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UuV46Vws4mRY2iXahVmFkR`</summary>

```json
{
  "url": "https://openreview.net/forum?id=hqnGfzQQfa",
  "prompt": "Extract all information about this paper submission: what venue/conference is it submitted to, what is the status (accepted/rejected/under review), reviewer scores, any reviewer comments or discussion, decision, and any other metadata about the submission."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81c4090e-6cb8-4ba0-ae90-e375368a7cb1",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011Caweg4QWP2s7b7syTexNv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05e9c968-1376-4244-8c42-eba4a23565a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaQpiGoe3M5kufw6Zhq2fG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3084,
      "cache_read_input_tokens": 10981,
      "output_tokens": 505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3084
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 505,
          "cache_read_input_tokens": 10981,
          "cache_creation_input_tokens": 3084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3084,
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

_source line 18 · 2026-05-11T23:29:29.420Z_

<details><summary>↩ Tool result · `toolu_01UuV46Vws4mRY2iXahVmFkR`</summary>

```text
# Paper Submission Information

**Venue:** ICLR 2026 Conference

**Submission Status:** Under review (submitted September 1, 2025; modified February 11, 2026)

**Submission Number:** 431

**Title:** "Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents"

**Authors:** Mingkang Zhu, Xi Chen, Bei Yu, Hengshuang Zhao, Jiaya Jia

**Primary Area:** Foundation or frontier models, including LLMs

**Keywords:** LLM Agent, Search Agent, Reasoning, Reinforcement Learning

**License:** CC BY 4.0

---

**Reviewer Scores:** Not provided in the available content

**Reviewer Comments:** Not available in the provided material

**Decision:** Not yet rendered

**Other Metadata:** The page includes links to download the PDF and access author profiles, but no acceptance/rejection decision, reviewer feedback, or scoring information is visible in the supplied content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05e9c968-1376-4244-8c42-eba4a23565a1",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "5f792cc6-170f-45e9-ae49-8a114883b8ac",
  "sourceToolAssistantUUID": "05e9c968-1376-4244-8c42-eba4a23565a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T23:29:45.276Z_

<details><summary>↩ Tool result · `toolu_01TYL57B763wjSYwwpJNiYXu`</summary>

```text
# Stratified GRPO: Comprehensive Technical Summary

## Abstract Overview

The paper addresses a fundamental challenge in training Large Language Model (LLM) search agents using reinforcement learning. The authors identify and formalize "cross-stratum bias"—an inherent flaw when using standard policy gradient methods on trajectories with structurally different properties (varying numbers of search calls, different answer paths, etc.). They propose Stratified GRPO with its core innovation: Stratified Advantage Normalization (SAN), which partitions trajectories into homogeneous groups and computes advantages locally within each group rather than globally.

## The Core Problem: Cross-Stratum Bias

**What it is:** The researchers identify that search agent trajectories are structurally heterogeneous. A trajectory with zero search calls differs fundamentally from one with multiple searches—they exhibit "different answer directions and reward distributions." Standard methods using a single global baseline implicitly assume all trajectories are comparable, creating an "apples-to-oranges" comparison.

**Mathematical Formalization:** According to Proposition 1 in the paper, the global advantage decomposes as:

The global advantage = stratified advantage + (stratum mean - global mean)

This cross-stratum offset uniformly penalizes low-reward strata while favoring high-reward ones, distorting credit assignment. Theorem 1 proves this offset is "precisely the source of the excess variance" in standard approaches.

## Stratified Advantage Normalization (SAN)

**Core Concept:** Rather than computing:
- Standard GRPO: A_G(τ) = (R(τ) - global_mean) / global_std

**SAN computes:**
- A_SAN(τ) = (R(τ) - stratum_mean) / stratum_std

Where trajectories are partitioned into strata based on structural properties (e.g., number of search calls).

**Strata Definition:** The paper partitions trajectories by "a chosen partitioning function (e.g., the search count for search agents)." Each stratum B_k contains trajectories with identical structural properties.

**Key Mathematical Properties:**

1. **Invariance (Proposition 2):** SAN is invariant under positive affine reward transformations—multiplying all rewards by a positive constant and adding any value doesn't change the advantage estimates.

2. **Conditional Properties (Theorem 4):** In the population limit:
   - SAN is conditionally unbiased within each stratum: E[A_SAN | stratum k] = 0
   - SAN has unit conditional variance: Var(A_SAN | stratum k) = 1
   - Global Normalization (GN) is conditionally biased: E[A_GN | k] = (stratum_mean - global_mean) / global_std

3. **Global Properties (Theorem 5):** Despite different mechanisms, both SAN and GN are globally unbiased (mean zero) and achieve identical unit global variance when ε=0.

4. **Variance Decomposition (Theorem 2):** The variance reduction from global to SAN advantages splits into two components:
   - Between-stratum variance (removed by stratification)
   - Normalization effect (stabilizes within-stratum scales)

## How SAN Improves Learning

The paper proves in Theorem 3 that SAN's population gradient exactly targets a weighted sum of within-stratum policy gradients, with weights determined by stratum probabilities scaled by inverse standard deviations. This ensures the gradient updates benefit from heterogeneous trajectory information without bias.

**Practical Implementation - Blended Advantage:** For finite-sample stability when strata contain few trajectories, the authors introduce a convex blend:

A_blend = α·A_SAN + (1-α)·A_GN

This preserves SAN's local purity while borrowing global signal for stabilization.

## Experimental Setup

**Models:** Qwen-2.5-3B Base and Instruct models

**Benchmarks:** Seven question-answering datasets:
- Single-hop: Natural Questions (NQ), TriviaQA, PopQA
- Multi-hop: HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle

**Training Data:** Merged training splits from NQ and HotpotQA with Exact Match as reward

**Baselines Compared:**
- Non-RL: Direct Generation, SFT, RAG, Search-o1, IRCoT
- RL methods: Search-R1, R1, ReSearch, GRPO

**Retrieval Setup:** Wikipedia 2018 dump with E5 retriever (top-3 passages per query)

## Key Results

**Main Performance Gains:**
- Stratified GRPO improves over GRPO by up to 11.3 points averaged across benchmarks
- Particularly pronounced on multi-hop tasks (up to 14.5 point improvement over strongest baseline)
- Outperforms best baseline by up to 8.3 points overall

**Ablation Study (Table 2):** 
- SAN alone shows significant gains
- Blended advantage (adding α parameter) further enhances performance
- Full Stratified GRPO consistently outperforms both components individually

**Training Dynamics (Figure 1):**
- Stratified GRPO maintains stable, monotonically increasing rewards
- Standard GRPO suffers training collapse on Instruct model
- Stratified GRPO learns policies converging to ~2.5 search calls (effective multi-hop reasoning)
- GRPO stagnates at ~1 search call, indicating inability to explore multi-step strategies

**Stability Improvement:** The paper documents that GRPO experiences "training collapse—a known instability issue," while Stratified GRPO maintains stable learning curves.

## Key Theoretical Contributions

1. **Bias Characterization:** Exact decomposition showing GN advantage = (scaled SAN) + cross-stratum offset
2. **Conditional Analysis:** Proof that SAN delivers zero-mean, unit-variance signals within each stratum while GN is conditionally biased and inconsistently scaled
3. **Gradient Bias Proof:** Demonstration that cross-stratum bias directly translates to gradient bias affecting exploration
4. **Signal Purity:** Theorem establishing SAN as a "pure and scale-stable signal carrier" versus GN's flawed mechanism

## Why This Matters

The research reveals that structural heterogeneity in search agent trajectories isn't merely a practical concern but a fundamental theoretical problem. Standard advantage normalization conflates information across qualitatively different trajectory types, injecting systematic bias that harms both credit assignment and exploration. SAN's stratified approach restores fairness by ensuring each trajectory competes only against true peers, yielding provably superior learning signals with both theoretical guarantees and substantial empirical improvements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8a9c52d-8196-40a9-af32-2b8eef197444",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "63fd2d96-1e0b-4171-8b6e-11ce4199908e",
  "sourceToolAssistantUUID": "a8a9c52d-8196-40a9-af32-2b8eef197444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-11T23:29:48.307Z_

Excellent -- I have rich detail from the paper itself. Let me now search for follow-up work and related papers citing or building on this.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63fd2d96-1e0b-4171-8b6e-11ce4199908e",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CaweiLUxCFRHU5snjDGf5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "187c47ee-b45a-4015-87fe-474ae115e1b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sgTKRUsDmdCUehFLXDPgx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 266,
      "cache_creation_input_tokens": 2574,
      "cache_read_input_tokens": 14065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2574,
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

_source line 21 · 2026-05-11T23:29:48.848Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JwerNGmjSkSCM1ZBqvX6th`</summary>

```json
{
  "query": "\"Stratified GRPO\" citation follow-up work 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "187c47ee-b45a-4015-87fe-474ae115e1b1",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CaweiLUxCFRHU5snjDGf5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc84ea6f-5dde-4c4f-842a-dc3d19a659f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sgTKRUsDmdCUehFLXDPgx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 266,
      "cache_creation_input_tokens": 2574,
      "cache_read_input_tokens": 14065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2574,
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

_source line 22 · 2026-05-11T23:29:49.526Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FrfnU3jFd2XHBfbqkssGq8`</summary>

```json
{
  "query": "stratified normalization GRPO variants advantage estimation heterogeneous trajectories LLM agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc84ea6f-5dde-4c4f-842a-dc3d19a659f2",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CaweiLUxCFRHU5snjDGf5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "752b7597-b294-4c8d-a2fd-edded1575e8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sgTKRUsDmdCUehFLXDPgx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 266,
      "cache_creation_input_tokens": 2574,
      "cache_read_input_tokens": 14065,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2574
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 266,
          "output_tokens": 154,
          "cache_read_input_tokens": 14065,
          "cache_creation_input_tokens": 2574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2574,
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

_source line 23 · 2026-05-11T23:29:56.342Z_

<details><summary>↩ Tool result · `toolu_01JwerNGmjSkSCM1ZBqvX6th`</summary>

```text
Web search results for query: ""Stratified GRPO" citation follow-up work 2025 2026"

Links: [{"title":"Preprint. STRATIFIED GRPO: HANDLING STRUCTURAL HET-","url":"https://arxiv.org/pdf/2510.06214"},{"title":"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://arxiv.org/html/2510.06214v1"},{"title":"S-GRPO: Unified Post-Training for Large Vision-Language Models","url":"https://arxiv.org/html/2604.16557v1"},{"title":"Turn-Level Advantage Estimation with PPO for Improved ...","url":"https://aclanthology.org/2026.findings-eacl.328.pdf"},{"title":"Step-GRPO: Internalizing Dynamic Early Exit for Efficient Reasoning","url":"https://arxiv.org/html/2604.16890v1"},{"title":"STAGE: Stable and Generalizable GRPO for Autoregressive Image Generation","url":"https://arxiv.org/html/2509.25027v1"},{"title":"[2603.01162] Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic","url":"https://arxiv.org/abs/2603.01162"},{"title":"Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic","url":"https://arxiv.org/html/2603.01162v3"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Reinforcement Learning (RL) Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"}]

Based on the search results, here's what I found about "Stratified GRPO" and follow-up work in 2025-2026:

## Primary Work: Stratified GRPO

Stratified GRPO is a principled RL algorithm that eliminates cross-stratum bias through its core component, Stratified Advantage Normalization (SAN), which partitions trajectories into homogeneous strata and computes advantages locally.

The work addresses reinforcement learning for multi-turn search agents, where trajectories from different strategies are not directly comparable, and shows that structural heterogeneity of trajectories induces cross-stratum bias.

## Performance Results

The method improves upon GRPO by up to 11.3 points and surpasses the best-performing baseline by up to 8.3 points on average across seven QA benchmarks. On multi-hop benchmarks, Stratified GRPO achieves an average performance gain of up to 14.5 points over the strongest baseline.

## Follow-Up Work and Related Research (2025-2026)

The search results reveal a broader ecosystem of GRPO improvements and extensions:

- Step-GRPO proposes a novel post-training framework addressing efficient reasoning through semantic steps rather than tokens

- Recent theoretical work by Liu et al. (2025c) and Yang et al. (2026) studied the biases of GRPO's policy gradient and advantage function

- Research also provides a unified framework to understand GRPO through the lens of classical U-statistics to characterize its theoretical properties


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc84ea6f-5dde-4c4f-842a-dc3d19a659f2",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "f452a156-ad05-4238-b222-ceb22d34e1ed",
  "sourceToolAssistantUUID": "dc84ea6f-5dde-4c4f-842a-dc3d19a659f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-11T23:29:57.243Z_

<details><summary>↩ Tool result · `toolu_01FrfnU3jFd2XHBfbqkssGq8`</summary>

```text
Web search results for query: "stratified normalization GRPO variants advantage estimation heterogeneous trajectories LLM agents"

Links: [{"title":"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://arxiv.org/html/2510.06214"},{"title":"[2510.06214] Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://arxiv.org/abs/2510.06214"},{"title":"(PDF) Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://www.researchgate.net/publication/396292051_Stratified_GRPO_Handling_Structural_Heterogeneity_in_Reinforcement_Learning_of_LLM_Search_Agents"},{"title":"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents | OpenReview","url":"https://openreview.net/forum?id=hqnGfzQQfa"},{"title":"Preprint. STRATIFIED GRPO: HANDLING STRUCTURAL HET-","url":"https://arxiv.org/pdf/2510.06214"},{"title":"Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment","url":"https://arxiv.org/html/2603.10009"},{"title":"M-GRPO: Multi-Agent Group Relative Policy Optimization","url":"https://www.emergentmind.com/topics/multi-agent-group-relative-policy-optimization-m-grpo"},{"title":"Stratified Normalization Methods","url":"https://www.emergentmind.com/topics/stratified-normalization"},{"title":"Kernelized Advantage Estimation: From Nonparametric Statistics to LLM Reasoning","url":"https://arxiv.org/html/2604.28005"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Multi-Turn+Group+Relative+Policy+Optimization"}]

I found comprehensive information about your search query. Here are the key findings:

## Stratified GRPO: Handling Structural Heterogeneity

Large language model (LLM) agents increasingly rely on external tools such as search engines to solve complex, multi-step problems. However, the trajectories of search agents are structurally heterogeneous, where variations in the number, placement, and outcomes of search calls lead to fundamentally different answer directions and reward distributions.

### The Core Problem: Cross-Stratum Bias

Standard policy gradient methods, which use a single global baseline, suffer from cross-stratum bias—an "apples-to-oranges" comparison of heterogeneous trajectories. This cross-stratum bias distorts credit assignment and hinders exploration of complex, multi-step search strategies.

### The Solution: Stratified Advantage Normalization (SAN)

Stratified GRPO's central component, Stratified Advantage Normalization (SAN), partitions trajectories into homogeneous strata based on their structural properties and computes advantages locally within each stratum. SAN eliminates cross-stratum bias, yields conditionally unbiased unit-variance estimates inside each stratum, and retains the global unbiasedness and unit-variance properties enjoyed by standard normalization, resulting in a more pure and scale-stable learning signal.

### Empirical Results

Extensive experiments on diverse single-hop and multi-hop question-answering benchmarks demonstrate that Stratified GRPO consistently and substantially outperforms GRPO by up to 11.3 points, achieving higher training rewards, greater training stability, and more effective search policies.

To improve practical stability under finite-sample regimes, Stratified GRPO further linearly blends SAN with the global estimator.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "752b7597-b294-4c8d-a2fd-edded1575e8e",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "da503381-f112-4611-8925-2e8cf7cf983c",
  "sourceToolAssistantUUID": "752b7597-b294-4c8d-a2fd-edded1575e8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-11T23:30:01.172Z_

Let me fetch a few more relevant pages for additional detail -- the S-GRPO follow-up, the Emergent Mind stratified normalization topic page, and the blockwise advantage estimation paper that cites it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da503381-f112-4611-8925-2e8cf7cf983c",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawejDivcWg9Uz6mHfBWw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e84f092-a0ce-4fb7-93bf-84aaa463b6e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqazF9scxhp1TK8PPXsyWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2262,
      "cache_read_input_tokens": 16639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2262,
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

_source line 26 · 2026-05-11T23:30:02.593Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013JJi3sAtxDex7CGVCz7Jof`</summary>

```json
{
  "url": "https://www.emergentmind.com/topics/stratified-normalization",
  "prompt": "Extract all information about stratified normalization methods, what papers use it, how it relates to Stratified GRPO, and any follow-up or related work mentioned on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e84f092-a0ce-4fb7-93bf-84aaa463b6e5",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawejDivcWg9Uz6mHfBWw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35d9696f-5768-4c8a-9684-bba34ca01818",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqazF9scxhp1TK8PPXsyWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2262,
      "cache_read_input_tokens": 16639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2262,
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

_source line 27 · 2026-05-11T23:30:04.593Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ab1Biw4ZGzoDDMu5npUJpN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.10231",
  "prompt": "Extract the full abstract, title, authors, and how this paper relates to stratified normalization or GRPO. Does it cite Stratified GRPO? What is its contribution to advantage estimation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35d9696f-5768-4c8a-9684-bba34ca01818",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawejDivcWg9Uz6mHfBWw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "567f9e19-28bf-4f7f-90e8-30310d3eb91c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqazF9scxhp1TK8PPXsyWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2262,
      "cache_read_input_tokens": 16639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2262,
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

_source line 28 · 2026-05-11T23:30:05.406Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LCKfSqSS9oUtHmWoeAShKf`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.16557v1",
  "prompt": "Extract the full abstract and key details of S-GRPO. How does it relate to Stratified GRPO? Does it cite Stratified GRPO? What is its contribution?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "567f9e19-28bf-4f7f-90e8-30310d3eb91c",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawejDivcWg9Uz6mHfBWw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63325f53-ee8c-488a-b746-53a4f6a29443",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqazF9scxhp1TK8PPXsyWb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2262,
      "cache_read_input_tokens": 16639,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2262
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 386,
          "cache_read_input_tokens": 16639,
          "cache_creation_input_tokens": 2262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2262,
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

_source line 29 · 2026-05-11T23:30:09.702Z_

<details><summary>↩ Tool result · `toolu_013JJi3sAtxDex7CGVCz7Jof`</summary>

```text
# Stratified Normalization Methods: Summary

## Core Definition
Stratified normalization applies localized normalization within partitioned subsets defined by categorical or structural properties, addressing heterogeneity that would compromise accuracy if treated globally.

## Key Application Domains

**Algebraic Geometry**: Computes normalization of reduced affine algebras by partitioning singular locus into strata, enabling parallelizable computation through iterative test pair procedures.

**Logic & Type Theory**: Employs level-indexed stratification to regulate cut-elimination and ensure strong normalization, with rewrite rules controlled via index-based recursion guarantees.

**Machine Learning**: "Batch Normalization stratifies the normalization of activations per channel via L2, L1, or L∞ metrics" and eigen-stratified models reduce parameters for categorical variables.

**Particle Filtering**: Uses stratified resampling to partition normalized weights, proving asymptotic normality and enabling variance decomposition for error control.

**Reinforcement Learning**: Stratified Advantage Normalization (SAN) partitions heterogeneous trajectories into homogeneous strata, computing per-stratum advantage to eliminate cross-stratum bias in policy gradient methods.

## Connection to Stratified GRPO
The page lists "Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents" (2025) as a key reference, indicating SAN principles extend to gradient-based policy optimization for heterogeneous agent environments.

## Related Work
Ten primary papers referenced span algebraic algorithms (2011), logical systems (2012-2023), deep learning normalization (2018-2020), and recent RL applications (2023-2025).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35d9696f-5768-4c8a-9684-bba34ca01818",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "3ff43625-c8df-4138-86fa-57c8f2296cd9",
  "sourceToolAssistantUUID": "35d9696f-5768-4c8a-9684-bba34ca01818",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-11T23:30:10.494Z_

<details><summary>↩ Tool result · `toolu_01LCKfSqSS9oUtHmWoeAShKf`</summary>

```text
# S-GRPO: Key Details and Analysis

## Full Abstract

S-GRPO proposes a unified post-training framework for Large Vision-Language Models that integrates supervised fine-tuning with reinforcement learning. The method addresses two critical problems: SFT's catastrophic forgetting and pure RL's "cold-start" optimization collapse in sparse-reward visual tasks.

The core innovation is **Conditional Ground-Truth Trajectory Injection (CGI)**, which dynamically injects verified expert trajectories into the candidate pool only when the model fails to generate any valid responses. This ensures positive advantage signals during early training while allowing the model to transition to autonomous exploration as capabilities improve.

## Key Contributions

- **Unified Framework**: Seamlessly bridges SFT and RL within a single stage, eliminating the traditional two-stage pipeline
- **CGI Mechanism**: Dynamically solves exploration cold-start problems by guaranteeing non-zero gradients when all generated samples fail
- **Empirical Results**: Achieves domain-specific performance comparable to full fine-tuning while preserving general-purpose capabilities far better

## Relation to Stratified GRPO

**There is no mention of "Stratified GRPO" anywhere in this document.** The paper does not cite or reference any work by that name. S-GRPO builds upon Group Relative Policy Optimization (GRPO) and related methods like GCPO and RCPA, but does not discuss Stratified GRPO specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63325f53-ee8c-488a-b746-53a4f6a29443",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "d1e1ff44-c028-4d4a-b1b3-761adb4b6fd1",
  "sourceToolAssistantUUID": "63325f53-ee8c-488a-b746-53a4f6a29443",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-11T23:30:12.531Z_

<details><summary>↩ Tool result · `toolu_01Ab1Biw4ZGzoDDMu5npUJpN`</summary>

```text
# Paper Analysis: Blockwise Advantage Estimation for Multi-Objective RL

## Title and Authors
**Title:** "Blockwise Advantage Estimation for Multi-Objective RL with Verifiable Rewards"

**Authors:** Kirill Pavlenko, Alexander Golubev, Simon Karasik, Boris Yangel

## Full Abstract
"Group Relative Policy Optimization (GRPO) assigns a single scalar advantage to all tokens in a completion. For structured generations with explicit segments and objectives, this couples unrelated reward signals across segments, leading to objective interference and misattributed credit. We propose Blockwise Advantage Estimation, a family of GRPO-compatible methods that assigns each objective its own advantage and applies it only to the tokens in the corresponding text block, reducing reliance on hand-designed scalar rewards and scaling naturally to additional objectives. A key challenge is estimating advantages for later blocks whose rewards are conditioned on sampled prefixes; standard unbiased approaches require expensive nested rollouts from intermediate states. Concretely, we introduce an Outcome-Conditioned Baseline that approximates intermediate state values using only within-group statistics by stratifying samples according to a prefix-derived intermediate outcome. On math tasks with uncertainty estimation, our method mitigates reward interference, is competitive with a state-of-the-art reward-designed approach, and preserves test-time gains from confidence-weighted ensembling. More broadly, it provides a modular recipe for optimizing sequential objectives in structured generations without additional rollouts."

## Relationship to GRPO and Stratified Approaches

The paper builds directly on GRPO but does **not appear to cite "Stratified GRPO"** by name in the visible content. However, it employs stratification methodology: the "Outcome-Conditioned Baseline" stratifies samples "according to a prefix-derived intermediate outcome."

## Key Contribution to Advantage Estimation

The paper's primary contribution is introducing **Blockwise Advantage Estimation**, which decouples advantage signals by assigning separate advantages to individual objectives within text blocks rather than applying a single scalar to entire completions, addressing credit attribution in multi-objective sequential generation tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "567f9e19-28bf-4f7f-90e8-30310d3eb91c",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "fb9481b2-7b73-4138-b415-cc4d6f1fed62",
  "sourceToolAssistantUUID": "567f9e19-28bf-4f7f-90e8-30310d3eb91c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-11T23:30:15.455Z_

Now let me get one more piece of detail -- the ICLR 2026 review status and the paper's specific mathematical formulation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb9481b2-7b73-4138-b415-cc4d6f1fed62",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawekM2FL9ztD8eB7UmnP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c69d3734-751e-4c98-af2f-c544c69fd7d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZUQRirmxfKj8vaSBzbnS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 362,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 18901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1308,
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

_source line 33 · 2026-05-11T23:30:15.942Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RxHVXez1V7zDiiDysJ8Vca`</summary>

```json
{
  "query": "ICLR 2026 \"Stratified GRPO\" accepted rejected decision review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c69d3734-751e-4c98-af2f-c544c69fd7d8",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawekM2FL9ztD8eB7UmnP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "990b1d66-043a-435a-8cd5-f9bd867a6ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZUQRirmxfKj8vaSBzbnS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 362,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 18901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1308,
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

_source line 34 · 2026-05-11T23:30:20.141Z_

<details><summary>↩ Tool result · `toolu_01RxHVXez1V7zDiiDysJ8Vca`</summary>

```text
Web search results for query: "ICLR 2026 "Stratified GRPO" accepted rejected decision review"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=y5fpdBhhdM"},{"title":"ICLR 2026 Acceptance Prediction: Tabular ML Approach","url":"https://s-marton.github.io/TabICLR/"},{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"},{"title":"ICLR 2026 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/iclr-statistics/iclr-2026-statistics/"},{"title":"ICLR 2026 Area Chair Guide","url":"https://iclr.cc/Conferences/2026/AreaChairGuide"},{"title":"ICLR 2026 | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026"},{"title":"A Retrospective on the ICLR 2026 Review Process – ICLR Blog","url":"https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"}]

The search results don't contain any information about a paper titled "Stratified GRPO" or its acceptance/rejection status at ICLR 2026. The results show general information about the ICLR 2026 review process and conference, but no specific information about that particular paper.

One of the results does mention GRPO (Group-Relative Policy Optimization) briefly in the context of defense mechanisms, but it's not related to a paper called "Stratified GRPO."

To find information about this specific paper's decision status, you might try:
- Searching directly on OpenReview.net for ICLR 2026 submissions
- Looking at the ICLR 2026 accepted papers list at papercopilot.com
- Checking the OpenReview ICLR 2026 forum directly

Would you like me to search with different terms or try a more specific query?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "990b1d66-043a-435a-8cd5-f9bd867a6ec4",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "51f7b8c1-5f60-4d5b-ae74-4cb9dc291199",
  "sourceToolAssistantUUID": "990b1d66-043a-435a-8cd5-f9bd867a6ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-11T23:30:20.751Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012gmRCYMaCwaXMhjGMWMx5K`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.06214",
  "prompt": "Focus specifically on: 1) The exact definition of strata - how are trajectories partitioned? What is the partitioning function? Give specific examples mentioned in the paper. 2) The exact mathematical formula for SAN vs standard GRPO advantage. 3) The blended advantage formula with alpha. 4) The training algorithm pseudocode if available. 5) Any analysis of how many strata are used and what happens with different numbers of strata. 6) The specific datasets and their sizes used for training and evaluation. 7) Any limitations section. 8) Related work - what prior methods does this paper compare against and how does it position itself?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51f7b8c1-5f60-4d5b-ae74-4cb9dc291199",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawekM2FL9ztD8eB7UmnP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85468850-89e2-4dda-a06e-5f9054881c43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZUQRirmxfKj8vaSBzbnS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 362,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 18901,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1308
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 362,
          "output_tokens": 309,
          "cache_read_input_tokens": 18901,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1308,
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

_source line 36 · 2026-05-11T23:30:33.431Z_

<details><summary>↩ Tool result · `toolu_012gmRCYMaCwaXMhjGMWMx5K`</summary>

````text
# Stratified GRPO: Key Technical Details

## 1. Definition of Strata and Partitioning

Trajectories are partitioned based on **structural properties**, with the primary example being the **number of search calls**. The paper states: "partition trajectories into homogeneous strata based on their structural properties (e.g., the number of search calls)."

The partitioning function S(τ;θ) assigns each trajectory to a discrete stratum k ∈ {0,...,I-1}. In search agents, this typically means:
- Stratum 0: trajectories with zero searches
- Stratum 1: trajectories with one search
- Stratum 2: trajectories with two searches, etc.

No specific maximum number of strata is discussed; it depends on observed trajectory diversity in practice.

## 2. Mathematical Formulas

**Standard GRPO (Global Normalization):**
```
A_GN(τ_i) = (R(τ_i) - R̄_global) / (σ̂_global + ε)
```

**Stratified Advantage Normalization (SAN):**
```
A_SAN(τ_i) = (R(τ_i) - μ̂_k(x)) / (σ̂_k(x) + ε)
```
where μ̂_k and σ̂_k are empirical mean and standard deviation within stratum k.

**Blended Advantage:**
```
A_blend(τ) = α·A_SAN(τ) + (1-α)·A_GN(τ),  α ∈ [0,1]
```
The paper uses blending to improve finite-sample stability when some strata contain few trajectories.

## 3. Training Algorithm

Algorithm 1 provides the complete pseudocode:
1. Compute global reward statistics (mean and variance across entire batch)
2. Partition batch by stratum (e.g., search count)
3. For each stratum, compute local statistics
4. Calculate SAN advantage within each stratum
5. Blend with global advantage
6. Return gradient estimate using blended advantages

No specific α value is specified; it's a hyperparameter.

## 4. Strata Analysis

The paper lacks explicit discussion of optimal stratum numbers or sensitivity analysis. However, the ablation study (Table 2) shows:
- "GRPO w/ SAN" (stratified only) improves significantly
- Adding blending further enhances performance

This suggests the method works across configurations, but specific guidance on choosing stratum boundaries isn't provided.

## 5. Datasets and Training

**Training Data:**
- Natural Questions (NQ) training split
- HotpotQA training split
- Combined dataset size not explicitly stated
- E5 retriever with 2018 Wikipedia dump
- Top-3 passages per query

**Evaluation Benchmarks (7 datasets):**
- Single-hop: NQ, TriviaQA, PopQA
- Multi-hop: HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle
- Metric: Exact Match (EM)

**Models Tested:**
- Qwen-2.5-3B Base
- Qwen-2.5-3B Instruct

No explicit discussion of dataset sizes provided.

## 6. Limitations Section

The paper contains no dedicated limitations section. However, implicit limitations include:

- Assumes discrete stratum structure; applicability to continuous action spaces unclear
- Small regularization constant ε breaks perfect invariance property
- "When some strata contain very few trajectories," SAN may produce noisy estimates (addressed via blending)
- Stratum definition requires domain knowledge (e.g., search count is problem-specific)

## 7. Related Work and Positioning

**Prior Methods:**
- GRPO (Shao et al., 2024) - baseline being improved
- PPO and Search-R1 - actor-critic alternatives
- RLOO (Ahmadian et al., 2024) - policy gradient with global baseline
- RAG, IRCoT - non-RL retrieval methods

**Key Differentiation:**
The paper positions itself as addressing a "fundamental challenge" overlooked by prior work. It states: "systematic study of RL algorithms for LLM agents...remains underexplored," positioning Stratified GRPO as the first method to formally identify and address cross-stratum bias in search agents.

The method is specifically designed for **heterogeneous trajectory structures** rather than general RL, making it distinct from off-the-shelf policy gradient methods applied to this setting.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85468850-89e2-4dda-a06e-5f9054881c43",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "94148586-87e6-40fa-bca1-61fe00ad0fa7",
  "sourceToolAssistantUUID": "85468850-89e2-4dda-a06e-5f9054881c43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-11T23:30:36.234Z_

Let me check the ICLR 2026 accepted paper list to see if this paper was accepted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94148586-87e6-40fa-bca1-61fe00ad0fa7",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawemtNg5WLRek25bA2wa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3909372-a1ae-41a7-a603-b4fe52dc5748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsQdSB3Jd1qGHbY3g1fFqz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2647,
      "cache_read_input_tokens": 20209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2647,
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

_source line 38 · 2026-05-11T23:30:38.982Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018wp8bEPMraJbPgSpkk4nGY`</summary>

```json
{
  "url": "https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/",
  "prompt": "Search this page for \"Stratified GRPO\" or \"stratified advantage normalization\" or authors \"Mingkang Zhu\" or \"Jiaya Jia\". Is this paper in the ICLR 2026 accepted paper list? Report whether it was accepted or not, and if so, as poster/spotlight/oral."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3909372-a1ae-41a7-a603-b4fe52dc5748",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawemtNg5WLRek25bA2wa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dc15adb-23ba-43e0-becb-9054c79128cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsQdSB3Jd1qGHbY3g1fFqz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2647,
      "cache_read_input_tokens": 20209,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2647
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 20209,
          "cache_creation_input_tokens": 2647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2647,
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

_source line 39 · 2026-05-11T23:30:41.188Z_

<details><summary>↩ Tool result · `toolu_018wp8bEPMraJbPgSpkk4nGY`</summary>

```text
Based on the web page content provided, I cannot find any paper titled "Stratified GRPO" or "stratified advantage normalization" by authors Mingkang Zhu or Jiaya Jia in the ICLR 2026 accepted paper list.

The page shows that the Paper Copilot database contains 5,343 accepted papers for ICLR 2026, but the actual paper list content has not loaded. The interface displays "Visible rows 0 / ..." indicating the detailed paper records are not displayed in the provided content. Therefore, I cannot confirm whether this paper appears in the accepted list or not based on the information available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dc15adb-23ba-43e0-becb-9054c79128cd",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "32108eb0-a855-45e8-ad3a-fc3207677941",
  "sourceToolAssistantUUID": "2dc15adb-23ba-43e0-becb-9054c79128cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-11T23:30:47.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0128j3qTcSzjKK7kk9GssbHm`</summary>

```json
{
  "query": "site:iclr.cc \"Stratified GRPO\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32108eb0-a855-45e8-ad3a-fc3207677941",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawenTYxfkG7eatkc4vF4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d38fa2d-c7d5-423c-a3fe-f6f00210d3e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LM2E7KGpGYGXfK6Y7zouji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 22856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 356,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-11T23:30:47.461Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QAYzEKDk6B6jHNe5UCwJhG`</summary>

```json
{
  "query": "openreview.net \"hqnGfzQQfa\" ICLR 2026 decision accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d38fa2d-c7d5-423c-a3fe-f6f00210d3e4",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CawenTYxfkG7eatkc4vF4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b28726d4-d966-4b6b-aa3e-d38e0641f2af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LM2E7KGpGYGXfK6Y7zouji",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 22856,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 356
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 22856,
          "cache_creation_input_tokens": 356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 356,
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

_source line 42 · 2026-05-11T23:30:50.760Z_

<details><summary>↩ Tool result · `toolu_0128j3qTcSzjKK7kk9GssbHm`</summary>

```text
Web search results for query: "site:iclr.cc "Stratified GRPO" 2026"

No links found.

The search didn't return any results. This could mean that:

1. There is no content matching "Stratified GRPO" on the ICLR website (iclr.cc)
2. The paper or content may not be publicly available on that domain yet
3. The exact phrase "Stratified GRPO" may not appear in that format on the site

If you're looking for a specific paper or research, you might want to try:
- Searching for just "Stratified GRPO" without the site restriction
- Searching for related terms or authors
- Checking if the content is on other academic databases like arXiv, Papers with Code, or Google Scholar

Would you like me to help with any of these alternative searches?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d38fa2d-c7d5-423c-a3fe-f6f00210d3e4",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "360c7156-0ac5-43c3-883a-82717ab7efe2",
  "sourceToolAssistantUUID": "8d38fa2d-c7d5-423c-a3fe-f6f00210d3e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-11T23:30:51.684Z_

<details><summary>↩ Tool result · `toolu_01QAYzEKDk6B6jHNe5UCwJhG`</summary>

```text
Web search results for query: "openreview.net "hqnGfzQQfa" ICLR 2026 decision accepted"

Links: [{"title":"ICLR 2026 | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"A Retrospective on the ICLR 2026 Review Process – ICLR Blog","url":"https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/"},{"title":"ICLR 2026 Conference Submissions","url":"https://openreview.net/submissions?venue=ICLR.cc/2026/Conference"},{"title":"ICLR 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"PaperDecision | Modeling the Complete Peer Review Process","url":"https://paperdecision.netlify.app/"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"}]

I searched for the specific query you requested, but the search results don't contain information about the specific OpenReview submission ID "hqnGfzQQfa" or its acceptance decision for ICLR 2026. 

The search returned general information about ICLR 2026, including that 5,355 papers were accepted out of 13,763 submissions that received a decision, representing an acceptance rate of 27.4%, but it did not include details about this particular submission.

To find information about a specific submission, you would need to visit the OpenReview page directly using the submission ID in the URL, or check the ICLR 2026 submissions list on OpenReview directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b28726d4-d966-4b6b-aa3e-d38e0641f2af",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "b0f980f2-b05a-4386-aa0a-faaf7cc5b339",
  "sourceToolAssistantUUID": "b28726d4-d966-4b6b-aa3e-d38e0641f2af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-11T23:30:56.474Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MQYJk9pUzpomATWvkwzxBN`</summary>

```json
{
  "url": "https://openreview.net/forum?id=hqnGfzQQfa",
  "prompt": "Look for the acceptance decision for this paper. Is there a \"Decision\" section? Has this paper been accepted or rejected from ICLR 2026? What are the reviewer ratings/scores? Look for any text mentioning \"accept\", \"reject\", \"poster\", \"spotlight\", \"oral\", \"withdrawn\", or any final decision. Also extract any reviewer scores or ratings visible on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0f980f2-b05a-4386-aa0a-faaf7cc5b339",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CaweoETCP3LSHBQW43MHT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07ef4eba-d422-4f89-89c1-d0eac334ed11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Dn6b7C5mg45iRKxSjTqUY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1027,
      "cache_read_input_tokens": 23212,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1027
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 23212,
          "cache_creation_input_tokens": 1027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1027,
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

_source line 45 · 2026-05-11T23:30:58.680Z_

<details><summary>↩ Tool result · `toolu_01MQYJk9pUzpomATWvkwzxBN`</summary>

```text
Based on the provided web page content, there is **no Decision section visible**. The page does not display:

- Any acceptance or rejection decision
- Reviewer ratings or scores
- Status indicators such as "accept," "reject," "poster," "spotlight," "oral," or "withdrawn"

The document appears to be a submission to ICLR 2026 (dated 01 Sept 2025, modified 11 Feb 2026) on OpenReview, but the decision status and reviewer evaluations are not included in the content provided. To find this information, you would need to access the full paper page on OpenReview, which may contain additional sections below the abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07ef4eba-d422-4f89-89c1-d0eac334ed11",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a9e76bf4de50fb468",
  "type": "user",
  "uuid": "9ea0de68-ca33-4e5a-8b2e-f4e6a837ab3d",
  "sourceToolAssistantUUID": "07ef4eba-d422-4f89-89c1-d0eac334ed11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-11T23:32:08.867Z_

I now have comprehensive information. Here is the full research report.

---

## Research Report: Stratified GRPO (arXiv:2510.06214)

### Confirmation

The paper **does exist** at arXiv:2510.06214. It is real and substantive.

**Full Title:** "Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents"

**Authors:** Mingkang Zhu, Xi Chen, Bei Yu, Hengshuang Zhao, Jiaya Jia

**Submitted:** October 7, 2025

**Categories:** cs.LG, cs.AI, cs.CL

---

### Publication Venue Status

The paper was **submitted to ICLR 2026** (OpenReview ID: `hqnGfzQQfa`, submission #431, primary area: "Foundation or frontier models, including LLMs"). The submission was dated September 1, 2025 and last modified February 11, 2026. As of my research, **no public decision (accept/reject) is visible on the OpenReview page**, and the paper does not appear to be findable on the ICLR 2026 virtual site. The arXiv version is labeled "Preprint." The decision status remains unclear -- it may still be under review, or the decision may not be publicly visible yet.

---

### What Problem Does It Solve?

When training LLM search agents (models that call external search/retrieval tools), the generated trajectories are **structurally heterogeneous**: some trajectories use zero search calls, some use one, some use two or more. These different trajectory structures lead to fundamentally different reward distributions -- a trajectory that uses no search operates in a different "regime" than one that performs multi-hop retrieval.

Standard GRPO computes a **single global baseline** (mean and standard deviation across all trajectories in a group) and normalizes advantages against it. The authors identify that this creates **cross-stratum bias** -- an "apples-to-oranges" comparison where trajectories from different structural categories are compared against a shared baseline that is appropriate for none of them.

Concretely, this bias:
- Uniformly penalizes trajectories from low-reward strata while favoring high-reward ones, regardless of the quality of individual trajectories within their stratum
- Distorts credit assignment
- Hinders exploration of complex multi-step search strategies (the model learns to avoid multi-hop search because it is penalized relative to simpler strategies)

---

### What Are the "Strata"?

Strata are defined by a **partitioning function** S(tau; theta) that assigns each trajectory to a discrete stratum k in {0, ..., I-1}. The primary partitioning variable used in the paper is the **number of search calls** in a trajectory:

- **Stratum 0:** Trajectories with zero search calls (direct answer)
- **Stratum 1:** Trajectories with one search call
- **Stratum 2:** Trajectories with two search calls
- And so on...

The paper frames this generally -- "a chosen partitioning function (e.g., the search count for search agents)" -- so the strata definition is domain-dependent. For search agents, search count is the natural choice because it determines the trajectory's structural character.

---

### What Is SAN (Stratified Advantage Normalization) Exactly?

**Standard GRPO (Global Normalization):**
```
A_GN(tau_i) = (R(tau_i) - R_global_mean) / (sigma_global + epsilon)
```

**SAN:**
```
A_SAN(tau_i) = (R(tau_i) - mu_k(x)) / (sigma_k(x) + epsilon)
```

Where mu_k and sigma_k are the empirical mean and standard deviation computed **only within stratum k** -- the stratum to which trajectory tau_i belongs.

The key decomposition (Proposition 1) shows:
```
A_GN = (scaled A_SAN) + cross-stratum offset
```
where the cross-stratum offset = (stratum_mean - global_mean) / global_std. This offset is the bias term: it uniformly shifts all trajectories in a stratum up or down regardless of their individual quality.

**Blended Advantage** (for finite-sample stability):
```
A_blend(tau) = alpha * A_SAN(tau) + (1 - alpha) * A_GN(tau),    alpha in [0, 1]
```

This convex blend handles edge cases where some strata contain very few trajectories (making within-stratum statistics noisy) by borrowing signal from the global estimate.

---

### Why Is Within-Group (Standard GRPO) Normalization Insufficient?

Standard GRPO's "group" is all trajectories for a given prompt -- it is **not** stratified by structural properties. The paper proves several formal results:

1. **Theorem 1:** The cross-stratum offset is precisely the source of excess variance in global normalization.

2. **Theorem 4 (Conditional Properties):** In the population limit:
   - SAN is conditionally unbiased: E[A_SAN | stratum k] = 0 for every k
   - SAN has unit conditional variance: Var(A_SAN | stratum k) = 1
   - Global Normalization is **conditionally biased**: E[A_GN | k] = (stratum_mean - global_mean) / global_std (nonzero whenever strata have different reward distributions)

3. **Theorem 5 (Global Properties):** Both SAN and GN are globally unbiased (mean zero) and have identical unit global variance when epsilon = 0 -- so SAN gives you strictly better conditional properties without sacrificing anything globally.

4. **Theorem 3 (Gradient):** SAN's population gradient exactly targets a weighted sum of within-stratum policy gradients, with weights proportional to stratum probabilities scaled by inverse standard deviations. This means exploration of multi-step strategies is not suppressed.

In short: standard GRPO's normalization across all trajectories **conflates signal from structurally different trajectory types**, injecting systematic bias that specifically punishes complex multi-hop strategies (which tend to have lower average reward) and rewards simple strategies, regardless of whether an individual complex trajectory was actually good.

---

### How Is This Different from Standard GRPO Group Normalization?

| Property | Standard GRPO | Stratified GRPO (SAN) |
|---|---|---|
| Advantage baseline | Single global mean/std across all trajectories for a prompt | Per-stratum mean/std within each structural category |
| Cross-stratum bias | Present -- conflates different trajectory types | Eliminated by construction |
| Conditional unbiasedness | No (biased within each stratum) | Yes (zero-mean within each stratum) |
| Conditional variance | Inconsistent across strata | Unit variance within each stratum |
| Global unbiasedness | Yes | Yes (preserved) |
| Effect on exploration | Suppresses multi-step strategies | Encourages exploration of complex strategies |
| Training stability | Subject to training collapse (especially on Instruct models) | Stable, monotonically increasing rewards |

---

### Benchmarks and Evaluation

**Base Models:** Qwen-2.5-3B (both Base and Instruct variants)

**Training Data:** Merged training splits from Natural Questions (NQ) and HotpotQA. Reward: Exact Match.

**Retrieval Setup:** Wikipedia 2018 dump with E5 retriever, top-3 passages per query.

**Evaluation Benchmarks (7 QA datasets):**
- **Single-hop:** Natural Questions (NQ), TriviaQA, PopQA
- **Multi-hop:** HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle

**Baselines:**
- Non-RL: Direct Generation, SFT, RAG, Search-o1, IRCoT
- RL methods: GRPO, Search-R1, R1, ReSearch

**Key Results:**
- Stratified GRPO improves over GRPO by **up to 11.3 points** averaged across benchmarks
- Up to **14.5 points** improvement over the strongest baseline on multi-hop tasks
- Outperforms best baseline by up to **8.3 points** overall
- Standard GRPO suffers training collapse on Instruct models; Stratified GRPO remains stable
- Stratified GRPO learns policies that converge to ~2.5 search calls (effective multi-hop reasoning), while GRPO stagnates at ~1 search call

---

### Follow-up and Related Work

The paper is relatively recent (October 2025), but the broader GRPO ecosystem has been active:

- **Blockwise Advantage Estimation** (arXiv:2602.10231, Pavlenko et al.) independently uses stratification in advantage estimation for multi-objective RL, stratifying by prefix-derived intermediate outcomes -- a conceptually related approach though not directly citing Stratified GRPO.
- **S-GRPO** (arXiv:2604.16557) is a different paper (unified post-training for vision-language models) that does **not** cite or build on Stratified GRPO.
- **Demystifying GRPO** (arXiv:2603.01162) analyzes GRPO's policy gradient as a U-statistic, providing complementary theoretical understanding.
- The Emergent Mind topic page on "Stratified Normalization" lists the paper as a key reference for stratified normalization in RL.

---

### Limitations (Implicit -- No Dedicated Section)

- Requires **domain knowledge** to define strata (search count is specific to search agents; other agent types would need different partitioning functions)
- When strata contain **very few trajectories**, SAN estimates become noisy (addressed via blending)
- The small regularization constant epsilon technically breaks the perfect affine invariance property
- Only evaluated on **Qwen-2.5-3B** -- unknown how well it scales to larger models
- Only tested on **QA tasks with search** -- generalization to other agentic settings (code, tool use, etc.) is unverified
- **Applicability to continuous action spaces** is unclear

Sources:
- [Stratified GRPO - arXiv Abstract](https://arxiv.org/abs/2510.06214)
- [Stratified GRPO - Full HTML Paper](https://arxiv.org/html/2510.06214)
- [Stratified GRPO - OpenReview (ICLR 2026 Submission)](https://openreview.net/forum?id=hqnGfzQQfa)
- [Stratified GRPO - ResearchGate](https://www.researchgate.net/publication/396292051_Stratified_GRPO_Handling_Structural_Heterogeneity_in_Reinforcement_Learning_of_LLM_Search_Agents)
- [Blockwise Advantage Estimation (related work)](https://arxiv.org/abs/2602.10231)
- [S-GRPO (unrelated despite similar name)](https://arxiv.org/html/2604.16557v1)
- [Demystifying GRPO as U-Statistic](https://arxiv.org/abs/2603.01162)
- [Emergent Mind - Stratified Normalization Methods](https://www.emergentmind.com/topics/stratified-normalization)
- [ICLR 2026 Accepted Paper List (Paper Copilot)](https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ea0de68-ca33-4e5a-8b2e-f4e6a837ab3d",
  "isSidechain": true,
  "agentId": "a9e76bf4de50fb468",
  "requestId": "req_011CaweokGZvs42zapAdYooy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "794b15d4-cf89-4552-a401-09d26a9d0b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01639dX7Bj3ugs5NgYrveweF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 24239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 328,
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
