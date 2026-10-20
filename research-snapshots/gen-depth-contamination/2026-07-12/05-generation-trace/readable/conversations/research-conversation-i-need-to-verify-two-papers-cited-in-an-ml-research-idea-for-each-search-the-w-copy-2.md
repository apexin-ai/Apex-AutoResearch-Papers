# Research conversation: I need to verify two papers cited in an ML research idea. For each, search the web to confirm they exist, find their act

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af13040affcd79259.jsonl`
- **Structured JSON:** [`420aa1cf6f4afb5a4f5a.json`](../../sessions/42/420aa1cf6f4afb5a4f5a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-12T01:40:58.736Z_

I need to verify two papers cited in an ML research idea. For each, search the web to confirm they exist, find their actual claims, and report what they do.

1. **BEACON** (arXiv 2605.06078, May 2026) — claimed to detect milestones from environment state changes and apply dual-scale (trajectory + segment) advantage estimation, achieving 92.9% on long-horizon ALFWorld.

2. **Spark** (arXiv 2601.20209, January 2026) — claimed to do "Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning" — adaptively branching at critical decision states using intrinsic policy signals (entropy, value uncertainty).

For each paper:
- Use WebSearch to find it (try "BEACON milestone policy learning arXiv 2026", "Spark dynamic branching agentic learning arXiv 2026", etc.)
- If found, use WebFetch to read the abstract and key methodology
- Report: Does the paper exist? What does it actually do? Do the claims in the idea match? 
- Specifically for Spark: does it use checkpoint-and-branch similar to what STAG proposes?

Be thorough — try multiple search queries if the first doesn't work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "af13040affcd79259",
  "type": "user",
  "uuid": "7d5d0b90-e9aa-4c51-8ff6-9fb631ec1d5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T01:40:58.738Z_

```json
{
  "parentUuid": "7d5d0b90-e9aa-4c51-8ff6-9fb631ec1d5e",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "116a4d25-91ba-4aae-9869-3b8d7dcd75ac",
  "timestamp": "2026-05-12T01:40:58.738Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T01:41:03.644Z_



I'll start by loading the WebSearch and WebFetch tools, then search for both papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "116a4d25-91ba-4aae-9869-3b8d7dcd75ac",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011Cawpiixidjdq43hgtw1nw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a8b2a69-67e6-4cf1-a025-d796056ce76f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FBfg8uqH3d2SaUrBPD8b9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 820,
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

_source line 4 · 2026-05-12T01:41:03.797Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014fhNpfNCXe6daLzj5ui5Eo`</summary>

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
  "parentUuid": "7a8b2a69-67e6-4cf1-a025-d796056ce76f",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011Cawpiixidjdq43hgtw1nw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f493f515-da38-4d5c-8520-a8b73b3f86f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FBfg8uqH3d2SaUrBPD8b9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 820,
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

_source line 5 · 2026-05-12T01:41:03.801Z_

<details><summary>↩ Tool result · `toolu_014fhNpfNCXe6daLzj5ui5Eo`</summary>

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
  "parentUuid": "f493f515-da38-4d5c-8520-a8b73b3f86f7",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "af13040affcd79259",
  "type": "user",
  "uuid": "439b3cce-8219-4632-a519-f7baa38b9439",
  "sourceToolAssistantUUID": "f493f515-da38-4d5c-8520-a8b73b3f86f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T01:41:06.190Z_



Now let me search for both papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "439b3cce-8219-4632-a519-f7baa38b9439",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011Cawpj7KseMYwQ1Wgy8wzv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfec796c-a161-47c7-a72e-c7818c510617",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018v4hx8bCCxcPUq4aVAN5Rm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-12T01:41:07.139Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PgzcTFoQJaFxpbLNHNZxvm`</summary>

```json
{
  "query": "BEACON milestone policy learning arXiv 2605.06078 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfec796c-a161-47c7-a72e-c7818c510617",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011Cawpj7KseMYwQ1Wgy8wzv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3e18373-7240-4227-8e32-5deab171efa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018v4hx8bCCxcPUq4aVAN5Rm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-12T01:41:07.526Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ga68vg7hbKDTJLdbKHEdgV`</summary>

```json
{
  "query": "Spark dynamic branching agentic learning arXiv 2601.20209 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3e18373-7240-4227-8e32-5deab171efa0",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011Cawpj7KseMYwQ1Wgy8wzv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "227166b9-57db-44d9-9cc1-068f64be2aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018v4hx8bCCxcPUq4aVAN5Rm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8124,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 135,
          "cache_read_input_tokens": 8124,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-12T01:41:13.727Z_

<details><summary>↩ Tool result · `toolu_01PgzcTFoQJaFxpbLNHNZxvm`</summary>

```text
Web search results for query: "BEACON milestone policy learning arXiv 2605.06078 2026"

Links: [{"title":"Milestone-Guided Policy Learning for Long-Horizon Language Agents","url":"https://arxiv.org/html/2605.06078"},{"title":"[2605.06078] Milestone-Guided Policy Learning for Long-Horizon Language Agents","url":"https://arxiv.org/abs/2605.06078"},{"title":"[2605.07579] Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor's Internal States","url":"https://arxiv.org/abs/2605.07579"},{"title":"BEACON: A Bayesian Optimization Inspired Strategy for Efficient Novelty Search","url":"https://arxiv.org/html/2406.03616v4"},{"title":"[2509.14519] BEACON: Behavioral Malware Classification with Large Language Model Embeddings and Deep Learning","url":"https://arxiv.org/abs/2509.14519"},{"title":"[2605.07101] Decentralized Diffusion Policy Learning for Enhanced Exploration in Cooperative Multi-agent Reinforcement Learning","url":"https://arxiv.org/abs/2605.07101"},{"title":"[2605.06448] Performance guaranteed MPC Policy Approximation via Cost Guided Learning","url":"https://arxiv.org/abs/2605.06448"},{"title":"[2605.05755] Transformers Provably Implement In-Context Reinforcement Learning with Policy Improvement","url":"https://arxiv.org/abs/2605.05755"},{"title":"[2605.07501] ExpThink: Experience-Guided Reinforcement Learning for Adaptive Chain-of-Thought Compression","url":"https://arxiv.org/abs/2605.07501"},{"title":"[2605.07701] Guidance Is Not a Hyperparameter: Learning Dynamic Control in Diffusion Language Models","url":"https://arxiv.org/abs/2605.07701"}]

Based on the search results, here's what I found about the BEACON milestone policy learning paper (arXiv 2605.06078):

## Overview

BEACON is a milestone-guided policy learning framework that leverages the compositional structure of long-horizon tasks to ensure precise credit assignment.

## Problem and Solution

The paper addresses challenges in training language agents with reinforcement learning on long-horizon agentic tasks, identifying two root causes: credit misattribution (where correct early actions are penalized due to terminal failures) and sample inefficiency (where scarce successful trajectories result in near-total loss of learning signal).

BEACON partitions trajectories at milestone boundaries, applies temporal reward shaping within segments to credit partial progress, and estimates advantages at dual scales to prevent distant failures from corrupting the evaluation of local actions.

## Performance Results

On ALFWorld, WebShop, and ScienceWorld, BEACON consistently outperforms GRPO and GiGPO. On long-horizon ALFWorld tasks, BEACON achieves 92.9% success rate, nearly doubling GRPO's 53.5%, while improving effective sample utilization from 23.7% to 82.0%.

The paper was submitted to arXiv on May 7, 2026, and code is available at https://github.com/ZJU-REAL/BEACON.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3e18373-7240-4227-8e32-5deab171efa0",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "af13040affcd79259",
  "type": "user",
  "uuid": "34c74d56-bb22-4cbf-98fd-7c7e886a2e9e",
  "sourceToolAssistantUUID": "a3e18373-7240-4227-8e32-5deab171efa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T01:41:14.229Z_

<details><summary>↩ Tool result · `toolu_01Ga68vg7hbKDTJLdbKHEdgV`</summary>

```text
Web search results for query: "Spark dynamic branching agentic learning arXiv 2601.20209 2026"

Links: [{"title":"[2601.20209] Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning","url":"https://arxiv.org/abs/2601.20209"},{"title":"Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning","url":"https://arxiv.org/html/2601.20209"},{"title":"Training Multi-Turn Search Agent via Contrastive Dynamic Branch Sampling","url":"https://arxiv.org/html/2602.03719"},{"title":"TreePS-RAG: Tree-based Process Supervision for Reinforcement Learning in Agentic RAG","url":"https://arxiv.org/html/2601.06922"},{"title":"AgentVNE: LLM-Augmented Graph Reinforcement Learning for Affinity-Aware Multi-Agent Placement in Edge Agentic AI","url":"https://arxiv.org/html/2601.02021"},{"title":"[2507.17365v1] DynaSearcher: Dynamic Knowledge Graph Augmented Search Agent via Multi-Reward Reinforcement Learning","url":"https://arxiv.org/abs/2507.17365v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.04426v1"},{"title":"SPARK: Synergistic Policy And Reward co-evolving framework","url":"https://arxiv.org/html/2509.22624v1"},{"title":"[2601.13247] Aligning Agentic World Models via Knowledgeable Experience Learning","url":"https://arxiv.org/abs/2601.13247"},{"title":"[2601.00868] SmartFlow Reinforcement Learning and Agentic AI for Bike-Sharing Optimisation","url":"https://arxiv.org/abs/2601.00868"}]

I found the paper! Here are the key details about the Spark paper from arXiv 2601.20209:

## Paper Overview

**Spark** (**S**trategic **P**olicy-**A**ware explo**R**ation via **K**ey-state dynamic branching) is a novel framework that selectively branches at critical decision states for resource-efficient exploration.

## Problem It Addresses

The paper addresses the challenge of training large language models as intelligent agents for long-horizon tasks, which remains difficult due to the scarcity of high-quality trajectories, especially under limited resources. Existing methods typically scale up rollout sizes and indiscriminately allocate computational resources among intermediate steps, which inherently wastes substantial computation budget on trivial steps while failing to guarantee sample quality.

## Key Innovation

The key insight is to activate adaptive branching exploration at critical decision points to probe promising trajectories, thereby achieving precise resource allocation that prioritizes sampling quality over blind coverage.

## Results

Experiments across diverse tasks (e.g., embodied planning) demonstrate that Spark achieves superior success rates with significantly fewer training samples, exhibiting robust generalization even in unseen scenarios.

The paper was submitted on January 28, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "227166b9-57db-44d9-9cc1-068f64be2aff",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "af13040affcd79259",
  "type": "user",
  "uuid": "e66b0642-4a3e-40d4-b567-aaea1afcdfd1",
  "sourceToolAssistantUUID": "227166b9-57db-44d9-9cc1-068f64be2aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-12T01:41:17.742Z_

Both papers exist. Let me now fetch the actual abstracts and detailed methodology from each paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e66b0642-4a3e-40d4-b567-aaea1afcdfd1",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011CawpjsMGYQbzoHNV2nFpF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc6aa0d2-a897-4672-9585-e84a36fc2bff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVrPu5ak9mQaSmtjyVEDTg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 10034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1790,
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

_source line 12 · 2026-05-12T01:41:20.109Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EwgUdc4Wi2CHGj8G4MmM2h`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06078",
  "prompt": "Extract the full abstract, the list of authors, the submission date, and any key methodology details (milestone detection, dual-scale advantage estimation, reward shaping, benchmarks, and results). Also note the exact name/acronym of the method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc6aa0d2-a897-4672-9585-e84a36fc2bff",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011CawpjsMGYQbzoHNV2nFpF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6758e59f-332a-4f5e-9056-210d8ff47b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVrPu5ak9mQaSmtjyVEDTg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 10034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1790,
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

_source line 13 · 2026-05-12T01:41:22.126Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0125KHifd2U2RN15duk2cGYD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.20209",
  "prompt": "Extract the full abstract, the list of authors, the submission date, and any key methodology details. Specifically: (1) How does it identify critical decision states? Does it use entropy or value uncertainty? (2) Does it do checkpoint-and-branch / branching from saved states? (3) What intrinsic policy signals does it use? (4) What benchmarks and results are reported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6758e59f-332a-4f5e-9056-210d8ff47b84",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011CawpjsMGYQbzoHNV2nFpF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73bb6cf7-8837-4232-bf96-db7bb95939d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVrPu5ak9mQaSmtjyVEDTg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 10034,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1790
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 301,
          "cache_read_input_tokens": 10034,
          "cache_creation_input_tokens": 1790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1790,
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

_source line 14 · 2026-05-12T01:41:26.248Z_

<details><summary>↩ Tool result · `toolu_01EwgUdc4Wi2CHGj8G4MmM2h`</summary>

```text
# BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents

**Method Name:** BEACON

**Authors:** Zixuan Wang, Yuchen Yan, Hongxing Li, Teng Pan, Dingming Li, Ruiqing Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

**Submission Date:** May 7, 2026

**Full Abstract:**
"While long-horizon agentic tasks require language agents to perform dozens of sequential decisions, training such agents with reinforcement learning remains challenging. We identify two root causes: credit misattribution, where correct early actions are penalized due to terminal failures, and sample inefficiency, where scarce successful trajectories result in near-total loss of learning signal. We introduce a milestone-guided policy learning framework, BEACON, that leverages the compositional structure of long-horizon tasks to ensure precise credit assignment. BEACON partitions trajectories at milestone boundaries, applies temporal reward shaping within segments to credit partial progress, and estimates advantages at dual scales to prevent distant failures from corrupting the evaluation of local actions."

**Key Methodology Details:**

- **Milestone Detection:** Partitions trajectories at milestone boundaries to leverage task compositional structure
- **Reward Shaping:** Applies temporal reward shaping within segments to credit partial progress
- **Dual-Scale Advantage Estimation:** Estimates advantages at dual scales to prevent distant failures from affecting local action evaluation
- **Benchmarks:** ALFWorld, WebShop, ScienceWorld
- **Key Results:** On ALFWorld, achieved 92.9% success rate versus GRPO's 53.5%; improved sample utilization from 23.7% to 82.0%

**Code Availability:** Available on GitHub (ZJU-REAL/BEACON)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6758e59f-332a-4f5e-9056-210d8ff47b84",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "af13040affcd79259",
  "type": "user",
  "uuid": "dcf24c2b-a560-4d40-bd94-e74ffd6abac9",
  "sourceToolAssistantUUID": "6758e59f-332a-4f5e-9056-210d8ff47b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T01:41:29.255Z_

<details><summary>↩ Tool result · `toolu_0125KHifd2U2RN15duk2cGYD`</summary>

```text
# Spark Paper Summary

**Full Abstract:**
"Reinforcement learning has empowered large language models to act as intelligent agents, yet training them for long-horizon tasks remains challenging due to the scarcity of high-quality trajectories, especially under limited resources. Existing methods typically scale up rollout sizes and indiscriminately allocate computational resources among intermediate steps. Such attempts inherently waste substantial computation budget on trivial steps while failing to guarantee sample quality. To address this, we propose Spark (Strategic Policy-Aware exploration via Key-state dynamic branching), a novel framework that selectively branches at critical decision states for resource-efficient exploration. Our key insight is to activate adaptive branching exploration at critical decision points to probe promising trajectories, thereby achieving precise resource allocation that prioritizes sampling quality over blind coverage. This design leverages the agent's intrinsic decision-making signals to reduce dependence on human priors, enabling the agent to autonomously expand exploration and achieve stronger generalization. Experiments across diverse tasks (e.g., embodied planning), demonstrate that Spark achieves superior success rates with significantly fewer training samples, exhibiting robust generalization even in unseen scenarios."

**Authors:**
Jinyang Wu, Shuo Yang, Changpeng Yang, Yuhao Shen, Shuai Zhang, Zhengqi Wen, Jianhua Tao

**Submission Date:**
January 28, 2026

**Methodology Details:**

1. **Critical State Identification:** The abstract does not specify whether entropy or value uncertainty is employed; only that it "activate[s] adaptive branching exploration at critical decision points."

2. **Branching Mechanism:** The methodology involves "selectively branches at critical decision states," but the provided content lacks technical details about checkpoint-and-branch implementation.

3. **Policy Signals:** The framework "leverage[s] the agent's intrinsic decision-making signals to reduce dependence on human priors."

4. **Benchmarks & Results:** Claims "superior success rates with significantly fewer training samples" and "robust generalization even in unseen scenarios," though specific numerical results are absent from this abstract page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73bb6cf7-8837-4232-bf96-db7bb95939d0",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "af13040affcd79259",
  "type": "user",
  "uuid": "431eca04-a8e6-4a0d-97b8-bf3628c227d4",
  "sourceToolAssistantUUID": "73bb6cf7-8837-4232-bf96-db7bb95939d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-12T01:41:34.446Z_

Good. I have the abstracts. Now let me fetch the full HTML versions of both papers to get deeper methodology details, especially for Spark where I need to check for entropy/value uncertainty signals and checkpoint-and-branch mechanics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "431eca04-a8e6-4a0d-97b8-bf3628c227d4",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011CawpkyKiTrbSZkNjZCpit",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "374b16f2-9ebf-4fbd-945a-ce534d38f8dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZZBWhgxejP2tJbKDRYRXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1247,
      "cache_read_input_tokens": 11824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1247,
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

_source line 17 · 2026-05-12T01:41:38.351Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X4WttSokmTsPWmQVqfop7v`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.20209",
  "prompt": "I need detailed methodology information about Spark. Specifically extract: (1) How does it identify critical decision states / key states? Does it use policy entropy, value uncertainty, or other signals? (2) How does the dynamic branching work mechanically? Does it checkpoint environment states and branch from them (rollback and re-explore)? Or does it branch from a saved trajectory? (3) What intrinsic policy signals does it use? (4) Any comparison to other branching or tree-search methods? (5) Does it mention anything about segment-level or trajectory-level credit assignment? (6) Specific benchmark results and numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "374b16f2-9ebf-4fbd-945a-ce534d38f8dc",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011CawpkyKiTrbSZkNjZCpit",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cb5a10c-6e37-43fb-b37a-7e68e603e05b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZZBWhgxejP2tJbKDRYRXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1247,
      "cache_read_input_tokens": 11824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1247,
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

_source line 18 · 2026-05-12T01:41:40.617Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Eh3t9wF98XLveMGvbtMnXG`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06078",
  "prompt": "Extract detailed methodology information about BEACON. Specifically: (1) How are milestones detected - from environment state changes or something else? (2) How does dual-scale advantage estimation work (trajectory-level vs segment-level)? (3) What is the temporal reward shaping mechanism? (4) Detailed benchmark results on ALFWorld, WebShop, ScienceWorld. (5) Any comparison to Spark or other branching methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cb5a10c-6e37-43fb-b37a-7e68e603e05b",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011CawpkyKiTrbSZkNjZCpit",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91095057-17b5-4e83-b99b-f69494147f4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZZBWhgxejP2tJbKDRYRXH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1247,
      "cache_read_input_tokens": 11824,
      "output_tokens": 428,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1247
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 428,
          "cache_read_input_tokens": 11824,
          "cache_creation_input_tokens": 1247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1247,
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

_source line 19 · 2026-05-12T01:41:47.857Z_

<details><summary>↩ Tool result · `toolu_01Eh3t9wF98XLveMGvbtMnXG`</summary>

```text
# BEACON Methodology Analysis

## 1. Milestone Detection

Milestones are detected from **observable environment state changes**, not learned models. The paper states: "Φ does not require learned models or manual annotation—it detects observable state changes from environment feedback." Examples include object state transitions in ALFWorld (successful pick-up, heating completion) and page transitions in WebShop advancing toward target products.

## 2. Dual-Scale Advantage Estimation

BEACON combines two advantage types:

**Trajectory-level:** Standard normalized advantage comparing terminal rewards across sampled trajectories, following GRPO's approach.

**Segment-level:** Compares segment performance only among trajectories reaching the same milestone. This isolation prevents "correct actions in early segments from being penalized by failures in later segments."

The combined advantage is: final_advantage = trajectory_advantage + λ × segment_advantage, where λ balances global and local performance.

## 3. Temporal Reward Shaping

Within completed segments, rewards decay exponentially: actions closer to milestone completion receive higher credit through the formula r_t = R_ms × γ^(t_k - t), where γ is the decay factor. Only segments ending with completed milestones receive positive reward, ensuring partial progress generates learning signal.

## 4. Benchmark Results

**ALFWorld (1.5B model):**
- Short: 96.8% | Medium: 87.0% | Long: 92.9%
- Outperforms GRPO by +73.6% on long tasks

**WebShop:** 75.6% success versus GRPO's 56.8%

**ScienceWorld:** 45.3% success versus GRPO's 21.1%

Sample efficiency improved from 23.7% to 82.0% effective utilization.

## 5. Comparison to Other Methods

The paper doesn't mention Spark or branching methods. It compares primarily against GRPO, GiGPO (state-based grouping), PPO, and process reward model approaches, positioning itself as superior because it "avoids expensive annotation, sampling overhead, or reliance on emergent trajectory patterns."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91095057-17b5-4e83-b99b-f69494147f4e",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "af13040affcd79259",
  "type": "user",
  "uuid": "78b4fc42-3fb1-4677-a922-eb99beefa1c7",
  "sourceToolAssistantUUID": "91095057-17b5-4e83-b99b-f69494147f4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T01:41:49.667Z_

<details><summary>↩ Tool result · `toolu_01X4WttSokmTsPWmQVqfop7v`</summary>

```text
# Spark Framework: Detailed Methodology Analysis

## 1. Critical Decision State Identification

Spark identifies critical states through **intrinsic policy signals** rather than external metrics. The mechanism is elegantly simple:

> "the agent selectively initiates additional exploration; otherwise, it proceeds linearly through routine decisions"

Specifically, the branching criterion ℬ detects an explicit `&lt;explore>` tag in the reasoning trace:

> "identifies states where exploration is valuable by detecting signals of epistemic uncertainty in the reasoning trace, which is explicitly manifested as a dedicated &lt;explore> tag"

This represents the agent's **self-awareness** of decision uncertainty, not computed entropy or value estimates.

## 2. Dynamic Branching Mechanics

The branching operates on **trajectory continuations**, not environment checkpointing:

- **Stage 1 (Root Init)**: Creates M parallel trajectory roots from initial state (typically M=3-5)
- **Stage 2 (Autonomous Branching)**: At each step, when `&lt;explore>` appears, samples B alternative continuations from the same history context
- **Stage 3 (Budget Enforcement)**: Dynamically adjusts branching factor via: `b_eff = min(b, N - N_current + 1)`

The method constructs a tree of trajectory paths sharing common prefixes, avoiding redundant re-execution of routine steps.

## 3. Intrinsic Policy Signals

The framework uses a **supervised fine-tuning (SFT) phase** to enable initial signal generation:

> "A cold-start SFT with 300 trajectories enables initial &lt;explore> tag generation in RL"

This creates the capability for reasoning traces to include uncertainty markers, enabling autonomous branching without external heuristics.

## 4. Comparison to Tree-Search Methods

Appendix E.1 discusses tree-based baselines but the document notes a limitation in the main text regarding low-capability models:

> "may not fully exploit exploration opportunities in extremely low-capability base models where the agent's self-awareness is limited"

Existing uniform branching methods waste resources on trivial steps, whereas Spark concentrates budget strategically.

## 5. Credit Assignment Mechanism

The approach uses **group-normalized advantages**:

> "Shared prefixes induce comparable alternatives, enabling relative credit assignment via group-normalized advantages"

Trajectories sharing common origins receive comparative reward signals, allowing the policy to learn which branches lead to superior outcomes.

## 6. Benchmark Results Summary

**ALFWorld Performance (7B model)**:
- Look: 100.0% (vs GRPO 76.7%)
- Clean: 92.5% (vs GRPO 86.0%)
- Pick2: 95.8% (vs GRPO 56.4%)

**ScienceWorld L2 (hardest, out-of-domain)**:
- Spark-1.5B: 49.2% (exceeding GPT-5 at 33.6%)

**Sample Efficiency**: Achieves 84.4% success on ALFWorld using only 20% training data (GRPO requires full data for 76.6%)

**Token Reduction**: 6.9% (ALFWorld), 47.0% (ScienceWorld), 11.2% (WebShop) versus baseline chain methods
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cb5a10c-6e37-43fb-b37a-7e68e603e05b",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "af13040affcd79259",
  "type": "user",
  "uuid": "4208f974-c68f-462e-919e-7720a86b35b2",
  "sourceToolAssistantUUID": "1cb5a10c-6e37-43fb-b37a-7e68e603e05b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-12T01:42:29.942Z_

Excellent. I now have thorough information on both papers. Here is my report.

---

## Paper 1: BEACON (arXiv 2605.06078, May 2026)

**Status: EXISTS and is confirmed.**

**Full title:** "Milestone-Guided Policy Learning for Long-Horizon Language Agents"

**Authors:** Zixuan Wang, Yuchen Yan, Hongxing Li, Teng Pan, Dingming Li, Ruiqing Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen (Zhejiang University)

**What it actually does:**
- **Milestone detection:** Milestones are detected from **observable environment state changes** (e.g., object state transitions in ALFWorld, page transitions in WebShop). No learned models or manual annotation required.
- **Temporal reward shaping:** Within completed segments, rewards decay exponentially -- actions closer to a milestone completion receive higher credit via `r_t = R_ms * gamma^(t_k - t)`.
- **Dual-scale advantage estimation:** Combines (1) a trajectory-level advantage (standard GRPO-style normalized advantage across full trajectories) with (2) a segment-level advantage (comparing segment performance only among trajectories that reached the same milestone). Combined as: `final_advantage = trajectory_advantage + lambda * segment_advantage`.

**Key results:**
- ALFWorld Long-horizon: **92.9%** (vs. GRPO 53.5%), a +73.6% improvement
- WebShop: 75.6% (vs. GRPO 56.8%)
- ScienceWorld: 45.3% (vs. GRPO 21.1%)
- Effective sample utilization improved from 23.7% to 82.0%

**Do the cited claims match?** **Yes, accurately.** The claim of detecting milestones from environment state changes, applying dual-scale (trajectory + segment) advantage estimation, and achieving 92.9% on long-horizon ALFWorld are all confirmed verbatim from the paper.

---

## Paper 2: Spark (arXiv 2601.20209, January 2026)

**Status: EXISTS and is confirmed.**

**Full title:** "Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning"

**Authors:** Jinyang Wu, Shuo Yang, Changpeng Yang, Yuhao Shen, Shuai Zhang, Zhengqi Wen, Jianhua Tao

**What it actually does:**
- **Critical state identification:** Spark does NOT use computed entropy or value uncertainty estimates. Instead, it uses a learned `&lt;explore>` tag in the reasoning trace -- the agent's own self-awareness of decision uncertainty. This is bootstrapped via an SFT cold-start phase with ~300 trajectories.
- **Dynamic branching mechanism:** At each step where `&lt;explore>` appears, Spark samples B alternative continuations from the same history context (trajectory continuations sharing common prefixes). It does NOT checkpoint environment states in the traditional sense -- it constructs a tree of trajectory paths sharing common prefixes, avoiding redundant re-execution of routine steps.
- **Credit assignment:** Uses group-normalized advantages -- trajectories sharing common origins (prefixes) receive comparative reward signals.
- **Stage structure:** (1) Root Init -- create M parallel trajectory roots; (2) Autonomous Branching -- branch when `&lt;explore>` detected; (3) Budget Enforcement -- dynamically adjust branching factor.

**Key results:**
- ALFWorld (7B): Look 100%, Clean 92.5%, Pick2 95.8% (vs. GRPO 76.7%, 86.0%, 56.4%)
- ScienceWorld L2 (1.5B): 49.2% (exceeding GPT-5 at 33.6%)
- Achieves 84.4% on ALFWorld with only 20% training data (GRPO needs full data for 76.6%)

**Do the cited claims match? Partially -- with important nuances:**
- The claim that Spark does "adaptive branching at critical decision states" is **correct**.
- The claim that it uses "intrinsic policy signals (entropy, value uncertainty)" is **inaccurate**. Spark does NOT use entropy or value uncertainty. It uses a self-generated `&lt;explore>` tag in the reasoning trace, which is a qualitatively different mechanism -- it's a learned token/tag, not a computed statistical measure.
- The subtitle/full title match is **exact**.

**Does Spark use checkpoint-and-branch similar to what STAG proposes?**
Spark does branch from shared trajectory prefixes (common history contexts), which is conceptually related to checkpoint-and-branch. However, it operates at the **trajectory/text level** (sharing common prefix tokens and branching continuations) rather than checkpointing full environment states and rolling back the simulator. The branching is driven by the agent's own `&lt;explore>` signal rather than external policy statistics. So while there is a structural similarity (branch at critical points, compare outcomes), the mechanism is quite different from a traditional checkpoint-and-rollback approach.

---

## Summary

| Aspect | BEACON | Spark |
|--------|--------|-------|
| Exists? | Yes | Yes |
| Claims accurate? | Yes, fully | Partially -- branching claim correct, but entropy/value uncertainty claim is wrong |
| Key mechanism | Milestone-based segmentation + dual-scale advantages | Self-signaled branching via `&lt;explore>` tag |
| Branching? | No (linear trajectories, segmented) | Yes (tree of continuations) |

The most important discrepancy: whoever cited Spark as using "entropy, value uncertainty" for branching decisions was incorrect. Spark's branching criterion is a learned `&lt;explore>` tag emitted by the model itself during reasoning, which is a fundamentally different (and arguably more novel) approach than using computed entropy or value uncertainty.

Sources:
- [BEACON - arXiv abstract](https://arxiv.org/abs/2605.06078)
- [BEACON - full HTML](https://arxiv.org/html/2605.06078)
- [Spark - arXiv abstract](https://arxiv.org/abs/2601.20209)
- [Spark - full HTML](https://arxiv.org/html/2601.20209)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4208f974-c68f-462e-919e-7720a86b35b2",
  "isSidechain": true,
  "agentId": "af13040affcd79259",
  "requestId": "req_011CawpnUbdbpqSEE2g7p8vm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3674fbb9-040c-4338-a6e6-ff80332ed89e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JypVnHGRX6nag61ZqkNNH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 522,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 13071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1324,
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
