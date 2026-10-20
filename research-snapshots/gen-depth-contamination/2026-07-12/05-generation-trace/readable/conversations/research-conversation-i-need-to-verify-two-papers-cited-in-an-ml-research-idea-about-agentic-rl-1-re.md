# Research conversation: I need to verify two papers cited in an ML research idea about agentic RL: 1. **RewardFlow** (arXiv 2603.18859, March 20

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae39de92b4d475ccd.jsonl`
- **Structured JSON:** [`624972390960eabadb10.json`](../../sessions/62/624972390960eabadb10.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-12T01:41:26.232Z_

I need to verify two papers cited in an ML research idea about agentic RL:

1. **RewardFlow** (arXiv 2603.18859, March 2026) — claimed to construct state graphs across rollouts and backpropagate rewards through graph topology, achieving 12.3% relative gain on ALFWorld.

2. **RTMC** (arXiv 2604.11037, April 2026) — claimed to exploit "implicit rollout tree structure for unbiased per-step MC advantages."

For each paper:
- Use WebSearch to find it (try "RewardFlow state graph reward propagation arXiv 2026", "RTMC rollout tree credit assignment arXiv 2026", etc.)
- If found, use WebFetch to read the abstract
- Report: Does the paper exist? What does it actually do?
- For RewardFlow specifically: it builds state graphs similar to STAG — how similar is the graph construction? Does RewardFlow also use state hashing? Could RewardFlow's graph trivially be repurposed for rollout allocation (which would undermine STAG's novelty)?

Be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "21b0170f-f388-48ac-87fd-122c579c4163",
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

_source line 2 · 2026-05-12T01:41:26.236Z_

```json
{
  "parentUuid": "21b0170f-f388-48ac-87fd-122c579c4163",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
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
  "uuid": "92658657-f18c-4fdf-91af-73d6beaf9a2f",
  "timestamp": "2026-05-12T01:41:26.236Z",
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

_source line 3 · 2026-05-12T01:41:30.197Z_



I'll start by loading the WebSearch and WebFetch tools, then search for both papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92658657-f18c-4fdf-91af-73d6beaf9a2f",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011CawpkkX2jjf5rCCUiJyqR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73d9183c-0cfa-45ef-bc55-904bca106a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gy7t3GXYiygbSh9pgTQo1D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 788,
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

_source line 4 · 2026-05-12T01:41:30.430Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QLwaVb8VfqHMiZtk1p8GES`</summary>

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
  "parentUuid": "73d9183c-0cfa-45ef-bc55-904bca106a7f",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011CawpkkX2jjf5rCCUiJyqR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b910de6-9bca-4ec6-a8ff-613c9b33cd8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gy7t3GXYiygbSh9pgTQo1D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 788,
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

_source line 5 · 2026-05-12T01:41:30.436Z_

<details><summary>↩ Tool result · `toolu_01QLwaVb8VfqHMiZtk1p8GES`</summary>

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
  "parentUuid": "7b910de6-9bca-4ec6-a8ff-613c9b33cd8a",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "08422dab-9a8f-4655-ac29-a7e19e568780",
  "sourceToolAssistantUUID": "7b910de6-9bca-4ec6-a8ff-613c9b33cd8a",
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

_source line 6 · 2026-05-12T01:41:33.651Z_



Now let me search for both papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08422dab-9a8f-4655-ac29-a7e19e568780",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011Cawpm5SaAUb6KdFTEyJDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e7d1dea-69e7-4c36-ba49-0585a42ba196",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KFyTYLqf48EVrqhtUbPqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8092,
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

_source line 7 · 2026-05-12T01:41:34.289Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0172jZ2gDrgzXL9BNPZvQJ9r`</summary>

```json
{
  "query": "RewardFlow state graph reward propagation arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e7d1dea-69e7-4c36-ba49-0585a42ba196",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011Cawpm5SaAUb6KdFTEyJDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26eebfff-05e6-4686-9ffc-6da09db4b28a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KFyTYLqf48EVrqhtUbPqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8092,
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

_source line 8 · 2026-05-12T01:41:35.093Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RcfZT6kKwvEAmF9rsf1Js6`</summary>

```json
{
  "query": "RTMC rollout tree credit assignment arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26eebfff-05e6-4686-9ffc-6da09db4b28a",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011Cawpm5SaAUb6KdFTEyJDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e9f3db7-975a-4581-a1c3-96a06c908ed4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KFyTYLqf48EVrqhtUbPqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8092,
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

_source line 9 · 2026-05-12T01:41:35.609Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RD7f2tqtZ4FNTKmi98qK5R`</summary>

```json
{
  "query": "arXiv 2603.18859"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e9f3db7-975a-4581-a1c3-96a06c908ed4",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011Cawpm5SaAUb6KdFTEyJDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65decb53-894f-4fbd-a23f-86dd8ed76267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KFyTYLqf48EVrqhtUbPqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8092,
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

_source line 10 · 2026-05-12T01:41:35.818Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014bD49A199koYBF1L8f2VYi`</summary>

```json
{
  "query": "arXiv 2604.11037"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65decb53-894f-4fbd-a23f-86dd8ed76267",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011Cawpm5SaAUb6KdFTEyJDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bab0dc72-ebcf-4d5d-9a91-e6819c4347f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KFyTYLqf48EVrqhtUbPqW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8092,
      "output_tokens": 211,
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
          "output_tokens": 211,
          "cache_read_input_tokens": 8092,
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

_source line 11 · 2026-05-12T01:41:40.929Z_

<details><summary>↩ Tool result · `toolu_01RD7f2tqtZ4FNTKmi98qK5R`</summary>

```text
Web search results for query: "arXiv 2603.18859"

Links: [{"title":"[2603.18859] RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/abs/2603.18859"},{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/html/2603.18859"},{"title":"[2604.18859] Testing $Λ$CDM versus dynamical dark energy in one year: A DESI spectroscopic follow-up program for Rubin supernovae","url":"https://arxiv.org/abs/2604.18859"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?show=500&skip=725"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2305.18859.pdf"},{"title":"[2404.18859] Leading terms of generalized Plücker formulas","url":"https://arxiv.org/abs/2404.18859"},{"title":"Computer Vision and Pattern Recognition","url":"https://arxiv.org/list/cs.CV/pastweek?skip=7&show=1000"},{"title":"[2509.18859] A sterile-neutrino search using data from the MicroBooNE liquid-argon time projection chamber performed in an undergraduate teaching laboratory","url":"https://arxiv.org/abs/2509.18859"},{"title":"Paper page - Hyperagents","url":"https://huggingface.co/papers/2603.19461"},{"title":"A Tauberian characterization of the Riemann hypothesis through the floor function","url":"https://arxiv.org/html/2407.18859"}]

Based on the search results, arXiv paper 2603.18859 is titled "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models" and was submitted on March 19, 2026.

The paper introduces RewardFlow, a lightweight method for estimating state-level rewards tailored to agentic reasoning tasks. The work addresses how reinforcement learning can enhance the agentic reasoning capabilities of large language models, but notes that the inherent sparsity of terminal rewards hinders fine-grained, state-level optimization.

The authors are Xiao Feng, Bo Han, Zhanke Zhou, Jiaqi Fan, Jiangchao Yao, Ka Ho Li, Dahai Yu, and Michael Kwok-Po Ng, affiliated with institutions including Hong Kong Baptist University, TCL Corporate Research, Shanghai Jiao Tong University, and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65decb53-894f-4fbd-a23f-86dd8ed76267",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "a47c1704-25ab-41fe-b3ac-a179692696ab",
  "sourceToolAssistantUUID": "65decb53-894f-4fbd-a23f-86dd8ed76267",
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

_source line 12 · 2026-05-12T01:41:41.439Z_

<details><summary>↩ Tool result · `toolu_0172jZ2gDrgzXL9BNPZvQJ9r`</summary>

```text
Web search results for query: "RewardFlow state graph reward propagation arXiv 2026"

Links: [{"title":"[2603.18859] RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/abs/2603.18859"},{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/html/2603.18859"},{"title":"RewardFlow: Propagating Reward in the State Graphs of Agentic Learning with LLMs | OpenReview","url":"https://openreview.net/forum?id=5oGJbM5u86"},{"title":"[2604.08536v1] RewardFlow: Generate Images by Optimizing What You Reward","url":"https://arxiv.org/abs/2604.08536v1"},{"title":"REWARDFLOW: PROPAGATING REWARD IN THE STATE ...","url":"https://openreview.net/pdf?id=5oGJbM5u86"},{"title":"Transductive Reward Inference on Graph","url":"https://arxiv.org/html/2402.03661v1"},{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/402860521_RewardFlow_Topology-Aware_Reward_Propagation_on_State_Graphs_for_Agentic_RL_with_Large_Language_Models"},{"title":"[2402.03661] Transductive Reward Inference on Graph","url":"https://arxiv.org/abs/2402.03661"},{"title":"[2601.20218] DenseGRPO: From Sparse to Dense Reward for Flow Matching Model Alignment","url":"https://arxiv.org/abs/2601.20218"},{"title":"[2010.02474v2] Reward Propagation Using Graph Convolutional Networks","url":"https://arxiv.org/abs/2010.02474v2"}]

Based on the search results, I found the paper you're looking for. Here's what I found about RewardFlow:

RewardFlow leverages the intrinsic topological structure of states within reasoning trajectories by constructing state graphs, which enables an analysis of state-wise contributions to success, followed by topology-aware graph propagation to quantify contributions and yield objective, state-level rewards.

RewardFlow is a lightweight method for estimating state-level rewards tailored to agentic reasoning tasks. The method employs graph-based propagation methods to estimate state-wise rewards, where outcome rewards from successful terminal states are propagated backward to intermediate states along observed transitions, capturing topological signals such as reachability and proximity.

RewardFlow constructs a state graph from multiple rollouts and propagates terminal rewards from successful states to all visited states using graph propagation methods such as Breadth-First Search and Personalized PageRank.

When integrated as dense rewards for RL optimization, RewardFlow substantially outperforms prior RL baselines across four agentic reasoning benchmarks, demonstrating superior performance, robustness, and training efficiency.

The paper was submitted to arXiv on March 19, 2026 (arxiv ID: 2603.18859) and is authored by Xiao Feng and 7 other researchers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26eebfff-05e6-4686-9ffc-6da09db4b28a",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "903675f7-a70b-4e58-bf35-d6ba6f91106a",
  "sourceToolAssistantUUID": "26eebfff-05e6-4686-9ffc-6da09db4b28a",
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

_source line 13 · 2026-05-12T01:41:41.590Z_

<details><summary>↩ Tool result · `toolu_014bD49A199koYBF1L8f2VYi`</summary>

```text
Web search results for query: "arXiv 2604.11037"

Links: [{"title":"RTMC: Step-Level Credit Assignment via Rollout Trees","url":"https://arxiv.org/html/2604.11037"},{"title":"[2604.11037] RTMC: Step-Level Credit Assignment via Rollout Trees","url":"https://arxiv.org/abs/2604.11037"},{"title":"[2602.11037] Generalized Langevin Models of Linear Agent-Based Systems: Strategic Influence Through Environmental Coupling","url":"https://arxiv.org/abs/2602.11037"},{"title":"Resource Constrained Pathfinding with A* and Negative Weights","url":"https://arxiv.org/html/2503.11037"},{"title":"Fine-Grained Engine Fault Sound Event Detection Using Multimodal Signals","url":"https://arxiv.org/html/2403.11037"},{"title":"[2504.11037] Statistical complexity as a probe of mass and phase structure in compact objects","url":"https://arxiv.org/abs/2504.11037"},{"title":"[2601.11037] BAPO: Boundary-Aware Policy Optimization for Reliable Agentic Search","url":"https://arxiv.org/abs/2601.11037"},{"title":"[2603.11037] Realizing the Emery Model in Optical Lattices for Quantum Simulation of Cuprates and Nickelates","url":"https://arxiv.org/abs/2603.11037"},{"title":"[2004.11037] Benchmarking near-term devices with quantum error correction","url":"https://ar5iv.labs.arxiv.org/html/2004.11037"},{"title":"[2106.11037] One Million Scenes for Autonomous Driving: ONCE Dataset","url":"https://ar5iv.labs.arxiv.org/html/2106.11037"}]

Based on the search results, here's what I found for arXiv paper 2604.11037:

**Title:** RTMC: Step-Level Credit Assignment via Rollout Trees

**Authors and Affiliation:** Tao Wang, Suhang Zheng, and Xiaoxiao Xu from Alibaba Group

**Publication Date:** April 13, 2026

**Overview:** The paper addresses multi-step agentic reinforcement learning, where existing approaches like GRPO assign uniform advantages to actions, while learned value networks can be fragile under sparse rewards. 

**Main Contribution:** The authors introduce Rollout-Tree Monte Carlo (RTMC) advantage estimation, which aggregates return statistics across rollouts sharing a common state to produce per-step Q-values and advantages—without any learned critic. A state-action signature system compresses raw interaction histories into compact, comparable representations, making cross-rollout state matching tractable.

You can view the full paper at: https://arxiv.org/abs/2604.11037


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bab0dc72-ebcf-4d5d-9a91-e6819c4347f1",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "9b7fab80-9842-4cde-9d36-26b97ae13c6b",
  "sourceToolAssistantUUID": "bab0dc72-ebcf-4d5d-9a91-e6819c4347f1",
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

_source line 14 · 2026-05-12T01:41:42.069Z_

<details><summary>↩ Tool result · `toolu_01RcfZT6kKwvEAmF9rsf1Js6`</summary>

```text
Web search results for query: "RTMC rollout tree credit assignment arXiv 2026"

Links: [{"title":"RTMC: Step-Level Credit Assignment via Rollout Trees","url":"https://arxiv.org/html/2604.11037"},{"title":"[2604.11037] RTMC: Step-Level Credit Assignment via Rollout Trees","url":"https://arxiv.org/abs/2604.11037"},{"title":"(PDF) RTMC: Step-Level Credit Assignment via Rollout Trees","url":"https://www.researchgate.net/publication/403791864_RTMC_Step-Level_Credit_Assignment_via_Rollout_Trees"},{"title":"MICA: Multi-granularity Intertemporal Credit Assignment for Long-Horizon Emotional Support Dialogue","url":"https://arxiv.org/html/2603.06194v2"},{"title":"Computer Science Apr 2026","url":"https://arxiv.org/list/cs/2026-04?skip=5800&show=100"},{"title":"Maximizing Rollout Informativeness under a Fixed Budget: A Submodular View of Tree Search for Tool-Use Agentic Reinforcement Learning","url":"https://arxiv.org/html/2605.05262"},{"title":"TSR: Trajectory‑Search Rollouts for Multi‑Turn RL of LLM Agents","url":"https://arxiv.org/html/2602.11767v1"},{"title":"Xiaoxiao Xu's research works | Alibaba Group and other places","url":"https://www.researchgate.net/scientific-contributions/Xiaoxiao-Xu-2321074403"},{"title":"Published at ICLR 2026 Workshop on Agents in the Wild. TSR: TRAJECTORY-SEARCH","url":"https://openreview.net/pdf?id=ayVIbNrYiC"},{"title":"Tree Search for LLM Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2509.21240"}]

I found the paper you're looking for! Here are the key details about RTMC:

## RTMC: Step-Level Credit Assignment via Rollout Trees

RTMC (Rollout-Tree Monte Carlo) is an advantage estimation method that aggregates return statistics across rollouts sharing a common state to produce per-step Q-values and advantages without any learned critic.

**The Core Problem:**
Critic-free methods like GRPO assign a single advantage to an entire trajectory, unable to distinguish good steps from bad ones within a multi-turn episode.

**The Key Innovation:**
The method observes that group rollouts targeting the same problem often traverse overlapping intermediate states, implicitly forming a tree whose branches diverge at successive decision points. A state-action signature system compresses raw interaction histories into compact, comparable representations, making cross-rollout state matching tractable.

**How It Works:**
RTMC down-weights frequently visited actions with low estimated advantage, while steering search toward branches that reach finish with high success likelihood.

The paper appears to be arxiv:2604.11037 and was published around April 2026. The work addresses a critical gap in agentic reinforcement learning where credit assignment at the step level, rather than trajectory level, is essential for effective multi-turn agent training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e9f3db7-975a-4581-a1c3-96a06c908ed4",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "011fabf6-7f74-458f-8067-fea0ce4274a5",
  "sourceToolAssistantUUID": "4e9f3db7-975a-4581-a1c3-96a06c908ed4",
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

_source line 15 · 2026-05-12T01:41:44.628Z_

Both papers exist. Let me now fetch the actual abstracts and detailed content from each paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "011fabf6-7f74-458f-8067-fea0ce4274a5",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011CawpmvAVZtGZWfZR7jrns",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48176ce5-b1c1-4274-a25f-4f58c930ddca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qMdQVkkgg9CSfD1BH7gnW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1455,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 10002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 16 · 2026-05-12T01:41:46.998Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UDRF5S4dvJ6CNXyMM1pGSS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.18859",
  "prompt": "Extract the full abstract of this paper. Also extract any details about: (1) how state graphs are constructed, (2) whether state hashing is used, (3) how rewards are propagated through the graph, (4) what benchmarks are evaluated (especially ALFWorld results), (5) how states are identified/matched across rollouts."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48176ce5-b1c1-4274-a25f-4f58c930ddca",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011CawpmvAVZtGZWfZR7jrns",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c476ec8-eaeb-4c35-a424-f03208f6bc43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qMdQVkkgg9CSfD1BH7gnW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1455,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 10002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 17 · 2026-05-12T01:41:52.143Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019Xbkeh3ziaivWz5BqjA79m`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.11037",
  "prompt": "Extract the full abstract of this paper. Also extract any details about: (1) what \"rollout tree structure\" means, (2) how states are matched across rollouts (state-action signatures), (3) how Monte Carlo advantages are computed, (4) whether it uses unbiased per-step MC advantages, (5) what benchmarks are evaluated."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c476ec8-eaeb-4c35-a424-f03208f6bc43",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011CawpmvAVZtGZWfZR7jrns",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42f6127e-20e1-4800-a1ee-34222049d3e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qMdQVkkgg9CSfD1BH7gnW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1455,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 10002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 18 · 2026-05-12T01:41:52.411Z_

<details><summary>↩ Tool result · `toolu_01UDRF5S4dvJ6CNXyMM1pGSS`</summary>

```text
# RewardFlow Paper Summary

## Full Abstract

"Reinforcement learning (RL) holds significant promise for enhancing the agentic reasoning capabilities of large language models (LLMs) with external environments. However, the inherent sparsity of terminal rewards hinders fine-grained, state-level optimization. Although process reward modeling offers a promising alternative, training dedicated reward models often entails substantial computational costs and scaling difficulties. To address these challenges, we introduce RewardFlow, a lightweight method for estimating state-level rewards tailored to agentic reasoning tasks. RewardFlow leverages the intrinsic topological structure of states within reasoning trajectories by constructing state graphs. This enables an analysis of state-wise contributions to success, followed by topology-aware graph propagation to quantify contributions and yield objective, state-level rewards. When integrated as dense rewards for RL optimization, RewardFlow substantially outperforms prior RL baselines across four agentic reasoning benchmarks, demonstrating superior performance, robustness, and training efficiency."

## Key Details

**State Graph Construction & Identification:**
The abstract indicates the method constructs "state graphs" that leverage "the intrinsic topological structure of states within reasoning trajectories," but specific technical details about state hashing, matching mechanisms, or construction procedures are not provided in this web page content.

**Reward Propagation:**
The method uses "topology-aware graph propagation to quantify contributions and yield objective, state-level rewards," though the actual propagation algorithm details are absent.

**Benchmarks:**
The paper evaluates across "four agentic reasoning benchmarks," but specific benchmark names (including ALFWorld results) are not mentioned in this excerpt.

**Implementation:**
Code is publicly available via GitHub link.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c476ec8-eaeb-4c35-a424-f03208f6bc43",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "886f47fe-651f-4fc0-8fb3-9b5daedde297",
  "sourceToolAssistantUUID": "2c476ec8-eaeb-4c35-a424-f03208f6bc43",
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

_source line 19 · 2026-05-12T01:41:57.731Z_

<details><summary>↩ Tool result · `toolu_019Xbkeh3ziaivWz5BqjA79m`</summary>

```text
# RTMC Paper Summary

## Full Abstract
"Multi-step agentic reinforcement learning benefits from fine-grained credit assignment, yet existing approaches offer limited options: critic-free methods like GRPO assign a uniform advantage to every action in a trajectory, while learned value networks introduce notable overhead and can be fragile under sparse rewards. We observe that group rollouts targeting the same problem often traverse overlapping intermediate states, implicitly forming a tree whose branches diverge at successive decision points. Building on this insight, we introduce Rollout-Tree Monte Carlo (RTMC) advantage estimation, which aggregates return statistics across rollouts sharing a common state to produce per-step Q-values and advantages--without any learned critic. A state-action signature system compresses raw interaction histories into compact, comparable representations, making cross-rollout state matching tractable. On SWE-bench Verified, RTMC improves pass@1 by 3.2 percentage points over GRPO."

## Key Details Extracted

**(1) Rollout Tree Structure:** The implicit tree forms when multiple rollouts solving the same problem traverse overlapping intermediate states, with branches diverging at successive decision points.

**(2) State Matching (State-Action Signatures):** A signature system compresses interaction histories into compact representations, enabling tractable cross-rollout state comparison and matching.

**(3) Monte Carlo Advantages:** The method aggregates return statistics across rollouts sharing a common state to produce per-step Q-values and advantages.

**(4) Unbiased Per-Step MC:** The abstract does not explicitly specify whether advantages are unbiased.

**(5) Benchmarks:** SWE-bench Verified (showing 3.2 percentage point improvement in pass@1 over GRPO).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42f6127e-20e1-4800-a1ee-34222049d3e1",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "301d39c5-85fd-4ace-b628-a7917424e82d",
  "sourceToolAssistantUUID": "42f6127e-20e1-4800-a1ee-34222049d3e1",
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

_source line 20 · 2026-05-12T01:42:01.309Z_

Good, I have the abstracts. Now let me fetch the full HTML versions for more technical detail, especially about RewardFlow's graph construction mechanism and state hashing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "301d39c5-85fd-4ace-b628-a7917424e82d",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011Cawpo58mapRoukQbapYhZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ac6fe5f-7c92-467b-8b8f-386af5911699",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjvcQShFA2CSi6KmbqxzUP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 11911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2704,
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

_source line 21 · 2026-05-12T01:42:07.138Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FJqDsKJzNoEXJMVxnnoP5R`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.18859",
  "prompt": "I need detailed technical information about how RewardFlow works. Specifically extract:\n\n1. HOW ARE STATE GRAPHS CONSTRUCTED? What defines a \"state\"? How are states identified and matched across different rollouts? Is there any hashing of states?\n\n2. WHAT GRAPH PROPAGATION METHOD is used? BFS? PageRank? Personalized PageRank? What are the details?\n\n3. WHAT BENCHMARKS are evaluated? What are the specific numbers on ALFWorld? Is there a 12.3% relative gain mentioned?\n\n4. How does this differ from simply using trajectory-level rewards? What is the key insight about graph topology?\n\n5. Any mention of rollout allocation, exploration strategies, or using the graph structure to decide WHERE to explore?\n\nPlease be as detailed as possible about the state identification/matching mechanism."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ac6fe5f-7c92-467b-8b8f-386af5911699",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011Cawpo58mapRoukQbapYhZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb910b82-e9c5-4be9-b6f6-a1e859f7c6f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjvcQShFA2CSi6KmbqxzUP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 11911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2704,
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

_source line 22 · 2026-05-12T01:42:11.087Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014SMPEqFght7hKUoPp7n8M2`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.11037",
  "prompt": "I need detailed technical information about how RTMC works. Specifically extract:\n\n1. How are states matched across rollouts? What is the \"state-action signature\" system? Is it hashing-based?\n\n2. How are per-step Q-values and advantages computed from the rollout tree? Is it truly unbiased Monte Carlo estimation?\n\n3. What benchmarks beyond SWE-bench are evaluated?\n\n4. How does the rollout tree differ from a simple state graph? Is it specifically a tree structure or a DAG?\n\n5. Any mention of using the tree structure for rollout allocation or exploration decisions?\n\n6. How do they handle the state identification problem - do they hash observations, use embeddings, or something else?\n\nPlease be as detailed as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb910b82-e9c5-4be9-b6f6-a1e859f7c6f4",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011Cawpo58mapRoukQbapYhZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62667aff-9611-4132-97ad-80b12a95025b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjvcQShFA2CSi6KmbqxzUP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 11911,
      "output_tokens": 532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 532,
          "cache_read_input_tokens": 11911,
          "cache_creation_input_tokens": 2704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2704,
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

_source line 23 · 2026-05-12T01:42:17.840Z_

<details><summary>↩ Tool result · `toolu_01FJqDsKJzNoEXJMVxnnoP5R`</summary>

```text
# RewardFlow: Technical Architecture Summary

## 1. State Graph Construction

**State Definition & Matching:**
States aggregate observations across trajectories. The paper normalizes states via function *f* to handle representational variability. For ALFWorld, the approach "enrich[es] the raw observation by automatically detecting transformative actions (e.g., clean, heat, cool) and append[ing] the resulting property changes to the text."

For stochastic environments like DeepResearch, states merge using embedding similarity: "States s and s′ are merged into a single super-node if their cosine similarity exceeds a threshold (default 0.9)." The paper uses E5 embeddings for text similarity measurement.

**Graph Structure:**
The formal definition aggregates across G trajectories:
- Nodes: unique normalized states
- Edges: observed state-action transitions
- Invalid transitions are filtered to remove spurious edges from hallucinated actions

## 2. Graph Propagation Method

**Algorithm: Multi-source Inverse BFS**

"Perform multi-source inverse BFS from all success terminals, traversing transitions backwards, to obtain the shortest-hop distance to the nearest success node."

Reward assignment: R(ŝ) = γ^d(ŝ) where d represents hop-distance to success. States unreachable to success receive R = 0.

Action-level rewards derive as potential differences: r̃(s_t, a_t) = R(s_{t+1}) - R(s_t)

## 3. Benchmark Results

**ALFWorld Performance (Qwen2.5-7B):**
- RewardFlow: 89.8% success rate
- Previous best (GiGPO): 82.8%
- **Relative gain: +7.0 percentage points** (not 12.3%)

**Sokoban:** RewardFlow achieves 62.4% vs GiGPO's 34.4% (+27.7% improvement)

The 12.3% figure appears in comparative gains on ALFWorld with the 1.5B model across some baselines.

## 4. Key Insight: Graph Topology vs. Trajectory-Level Rewards

Standard approaches assign uniform rewards across entire trajectories. RewardFlow exploits topological structure: states closer to success receive proportionally higher rewards based on graph distance, not just binary success/failure. This enables "fine-grained credit assignment" where intermediate states receive objective rewards reflecting their proximity to task completion, independent of trajectory outcomes.

## 5. Rollout Allocation & Exploration

The paper does **not** propose using graph structure to guide exploration allocation. RewardFlow constructs graphs post-hoc from sampled trajectories for reward estimation only. Exploration remains standard policy sampling; no adaptive allocation mechanism based on graph coverage is mentioned.

The robustness analysis (Table 4) shows RewardFlow performs well even with sparse sampling (4 rollouts), but this reflects graph robustness to limited data—not strategic exploration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb910b82-e9c5-4be9-b6f6-a1e859f7c6f4",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "cb8f80c2-290d-4dc4-8de7-8b371226dfa0",
  "sourceToolAssistantUUID": "cb910b82-e9c5-4be9-b6f6-a1e859f7c6f4",
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

_source line 24 · 2026-05-12T01:42:19.886Z_

<details><summary>↩ Tool result · `toolu_014SMPEqFght7hKUoPp7n8M2`</summary>

```text
# RTMC Technical Details

## 1. State-Action Signature System

The paper uses **hand-crafted, rule-based signatures** rather than hashing. For states, they employ:

- **View bucketing**: Files partitioned into 100-line buckets (e.g., `V[2]` for lines 200–299)
- **Content hashing**: "Each edit represented by 4-character MD5 hash" of old+new text
- **Operation sets**: Track cumulative effects (views, modifications, insertions) per file, order-invariant

Actions are classified by effect category (view, search, modify, create, execute, test, install, think, finish) with scope details. The state signature concatenates: `file1:OPS1|file2:OPS2|...|FLAGS`

## 2. Per-Step Advantage Computation

Yes, truly unbiased first-visit Monte Carlo:

> "Q^(s,a) = 1/N(s,a) ∑ G_t^(i)" across rollouts visiting (s,a)

State-value estimates use visit-weighted averaging: "V^(s) = ∑_a N(s,a)·Q^(s,a) / ∑_a N(s,a)"

Advantages: A^ = Q^ - V^. The authors note variance scales as σ²_Q/N(s,a), motivating their Bayesian shrinkage prior correction.

## 3. Benchmark Evaluation

**Only SWE-bench Verified (500 problems)** is evaluated. The paper explicitly acknowledges this limitation: "Single benchmark. We evaluate on SWE-bench Verified with a single base model."

## 4. Tree vs. DAG Structure

Technically a **tree (not DAG)**. The paper states: "each signature appears at most once per rollout, satisfying the first-visit Monte Carlo condition." Since signatures encode cumulative history, repeated visits to identical abstract states don't occur within a single trajectory.

## 5. Tree Structure for Exploration

**No rollout allocation or exploration decisions mentioned.** The tree is constructed post-hoc for advantage computation only, not for directing future sampling.

## 6. State Identification Mechanism

**Pure rule-based abstraction**, no learned embeddings. Authors note this as a key limitation: "hand-crafted state-action signatures...inevitably leave blind spots" and discuss learned signatures as "promising future work."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62667aff-9611-4132-97ad-80b12a95025b",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "f603a16f-434a-4a2b-88a7-ac041243e4cd",
  "sourceToolAssistantUUID": "62667aff-9611-4132-97ad-80b12a95025b",
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

_source line 25 · 2026-05-12T01:42:22.517Z_

Now let me do one more targeted search to verify the specific ALFWorld 12.3% claim for RewardFlow.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f603a16f-434a-4a2b-88a7-ac041243e4cd",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011CawpphpB9bMMjArKWc9zg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0a586a0-5dd5-44de-9915-04be6b599ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaX4ZBvBcRfRaMiKSPUYr6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1842,
      "cache_read_input_tokens": 14615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1842,
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

_source line 26 · 2026-05-12T01:42:23.075Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HQSbvbdVMFWtwKERY8pBu3`</summary>

```json
{
  "query": "RewardFlow ALFWorld 12.3% relative gain 1.5B model results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0a586a0-5dd5-44de-9915-04be6b599ebc",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011CawpphpB9bMMjArKWc9zg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7fa1763-2222-4d71-bff5-0445f857a785",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaX4ZBvBcRfRaMiKSPUYr6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1842,
      "cache_read_input_tokens": 14615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1842,
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

_source line 27 · 2026-05-12T01:42:23.259Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U9ZaCFNHe7L1kkYkaVs4FP`</summary>

```json
{
  "query": "RewardFlow state hashing embedding similarity state matching mechanism"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7fa1763-2222-4d71-bff5-0445f857a785",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011CawpphpB9bMMjArKWc9zg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78d6117e-b762-491e-94ac-92295bcb8c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaX4ZBvBcRfRaMiKSPUYr6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1842,
      "cache_read_input_tokens": 14615,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1842
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 14615,
          "cache_creation_input_tokens": 1842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1842,
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

_source line 28 · 2026-05-12T01:42:28.324Z_

<details><summary>↩ Tool result · `toolu_01HQSbvbdVMFWtwKERY8pBu3`</summary>

```text
Web search results for query: "RewardFlow ALFWorld 12.3% relative gain 1.5B model results"

Links: [{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/html/2603.18859"},{"title":"Agent Planning with World Knowledge Model","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf"},{"title":"Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/html/2502.10325v1"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"yolay/SPEAR-ALFWorld-DrBoT-GRPO-1.5B · Hugging Face","url":"https://huggingface.co/yolay/SPEAR-ALFWorld-DrBoT-GRPO-1.5B"},{"title":"AgentRM: Enhancing Agent Generalization with Reward ...","url":"https://aclanthology.org/2025.acl-long.945.pdf"},{"title":"Updated ALFWorld Model Performance Metrics Model Success Rate Reward... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Updated-ALFWorld-Model-Performance-Metrics-Model-Success-Rate-Reward-Precision-Completion_tbl2_371311588"},{"title":"[Quick Review] Differentiable Evolutionary Reinforcement Learning","url":"https://liner.com/review/differentiable-evolutionary-reinforcement-learning"},{"title":"A Hierarchical Multi-Agent Framework for Strategic ...","url":"https://openreview.net/pdf?id=VYdbeSoXWD"},{"title":"Learning to Simulate from Experience for Better AI Agents","url":"https://arxiv.org/pdf/2510.09577"}]

Based on the search results, I found information about RewardFlow and its performance on ALFWorld with the 1.5B model.

RewardFlow demonstrates particularly large gains on smaller models (1.5B/3B), with fine-grained rewards substantially reducing optimization difficulty and markedly improving agentic reasoning in lower-capacity models. However, the search results don't show the exact 12.3% relative gain figure you mentioned for the 1.5B model on ALFWorld.

On ALFWorld, RewardFlow achieves the highest overall success rate (89.8% at 7B, +7.0% over GiGPO) and ranks first or second in nearly all subtasks across all model sizes. The results indicate that RewardFlow is particularly effective for improving performance on smaller models, though the specific 12.3% relative gain metric you referenced doesn't appear in the available search results. The paper focuses on absolute success rate improvements and comparisons with baseline methods like GiGPO and GRPO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7fa1763-2222-4d71-bff5-0445f857a785",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "d1b2b020-e9dd-4960-a7ad-05d17882252f",
  "sourceToolAssistantUUID": "a7fa1763-2222-4d71-bff5-0445f857a785",
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

_source line 29 · 2026-05-12T01:42:30.393Z_

<details><summary>↩ Tool result · `toolu_01U9ZaCFNHe7L1kkYkaVs4FP`</summary>

```text
Web search results for query: "RewardFlow state hashing embedding similarity state matching mechanism"

Links: [{"title":"KEENHash: Hashing Programs into Function-Aware Embeddings for Large-Scale Binary Code Similarity Analysis | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3728911"},{"title":"[2506.11612] KEENHash: Hashing Programs into Function-Aware Embeddings for Large-Scale Binary Code Similarity Analysis","url":"https://arxiv.org/abs/2506.11612"},{"title":"Embedding similarity search. Searching for something similar is a… | by Roman Kyslyi, PhD | Medium","url":"https://medium.com/mlearning-ai/embedding-similarity-search-25c6911240af"},{"title":"Similarity Hashing and Perceptual Hashes | by Prof Bill Buchanan OBE FRSE | Medium","url":"https://billatnapier.medium.com/similarity-hashing-and-perceptial-hashes-963fba36c8b5"},{"title":"KEENHash: Hashing Programs into Function-Aware Embeddings for Large-Scale Binary Code Similarity Analysis | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.11612v1"},{"title":"KEENHash: Hashing Programs into Function-Aware Embeddings for Large-Scale Binary Code Similarity Analysis","url":"https://arxiv.org/html/2506.11612"},{"title":"[PDF] KEENHash: Hashing Programs into Function-Aware Embeddings for Large-Scale Binary Code Similarity Analysis | Semantic Scholar","url":"https://www.semanticscholar.org/paper/cb2f552524e6ff89fb4d6fdcc0a335d2141b9804"},{"title":"Embedding-based subsequence matching in time-series databases | ACM Transactions on Database Systems","url":"https://dl.acm.org/doi/10.1145/2000824.2000827"},{"title":"Semantic Hashing with Locality Sensitive Embeddings | OpenReview","url":"https://openreview.net/forum?id=sFDJNhwz7S"},{"title":"GitHub - SystemSecurityStorm/Awesome-Binary-Similarity: An awesome & curated list of binary code similarity papers","url":"https://github.com/SystemSecurityStorm/Awesome-Binary-Similarity"}]

Based on the search results, I found information related to hashing, embedding similarity, and state matching mechanisms, though the results focus primarily on **KEENHash**, a binary code similarity analysis system rather than something specifically called "RewardFlow."

## Key Findings on Hashing and Embedding Similarity:

In hash-based approaches, the idea is to learn a model that converts an item into a code, where similar items will produce the same or similar code. This approach significantly reduces the memory needed.

The fewer the bits that change in the similarity hashes, the more likely that we have a match.

## KEENHash: A Related System

The search results prominently feature **KEENHash**, which implements a state matching mechanism through hashing and embeddings: KEENHash hashes binaries into program-level representations through large language model (LLM)-generated function embeddings, and condenses a binary into one compact and fixed-length program embedding using K-Means and Feature Hashing.

The combination of K-Means clustering with Feature Hashing transforms the traditionally expensive function matching problem into efficient nearest-neighbor searches and bit-vector operations.

**Note:** The search results do not contain specific information about a system called "RewardFlow." If you're looking for information about a specific RewardFlow system, you may want to provide additional context or search with different terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78d6117e-b762-491e-94ac-92295bcb8c3d",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "ae3985a1-b142-4ba9-8359-c6e09a237831",
  "sourceToolAssistantUUID": "78d6117e-b762-491e-94ac-92295bcb8c3d",
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

_source line 30 · 2026-05-12T01:42:33.585Z_

Let me fetch the RewardFlow HTML paper to get the specific ALFWorld numbers for the 1.5B model and the detailed state identification mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae3985a1-b142-4ba9-8359-c6e09a237831",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011CawpqUnNbPFDnhoM9nfCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0b4e53b-ce0f-48af-b65d-3113a0f6e23e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rdeq6C2nat9oVePfALgv1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1879,
      "cache_read_input_tokens": 16457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1879,
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

_source line 31 · 2026-05-12T01:42:39.940Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HPJWPUBv8F2RD2d7VgbUQ8`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.18859",
  "prompt": "I need specific information:\n\n1. What are the exact ALFWorld results for the Qwen2.5-1.5B model? List all methods and their success rates. Is there a 12.3% relative gain for RewardFlow over any baseline?\n\n2. How exactly does the state normalization function f work? Does it use hashing? For text-based environments like ALFWorld, how are states compared - exact string match, hashing, or embedding similarity?\n\n3. For the embedding-based merging (cosine similarity > 0.9 with E5), which environments use this versus exact matching?\n\n4. Could the state graph be used for purposes OTHER than reward propagation - e.g., for deciding where to allocate more rollouts? Does the paper discuss this at all?\n\n5. What is the formal definition of the state graph (nodes, edges)?\n\nPlease provide exact numbers from tables if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0b4e53b-ce0f-48af-b65d-3113a0f6e23e",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011CawpqUnNbPFDnhoM9nfCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3ae61db-f77a-45c5-8597-1d37b61a1f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rdeq6C2nat9oVePfALgv1Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1879,
      "cache_read_input_tokens": 16457,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1879
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 315,
          "cache_read_input_tokens": 16457,
          "cache_creation_input_tokens": 1879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1879,
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

_source line 32 · 2026-05-12T01:42:47.250Z_

<details><summary>↩ Tool result · `toolu_01HPJWPUBv8F2RD2d7VgbUQ8`</summary>

````text
# RewardFlow Paper Analysis

## 1. ALFWorld Qwen2.5-1.5B Results

From Table 1, the success rates for Qwen2.5-1.5B-Instruct are:

| Method | Success Rate |
|--------|--------------|
| RLOO | 49.2% |
| GRPO | 50.0% |
| GiGPO | 53.1% |
| RewardFlow | 68.8% |

RewardFlow achieves a **29.5% relative improvement over GiGPO** (not 12.3%). The 12.3% figure mentioned in the abstract refers to ALFWorld results averaged across all model sizes.

## 2. State Normalization Function

The paper provides limited formal specification. For ALFWorld, state normalization works by:

> "enrich the raw observation by automatically detecting transformative actions (e.g., clean, heat, cool) and appending the resulting property changes"

For DeepResearch (stochastic environment), they use **embedding-based clustering**: states are merged if cosine similarity exceeds 0.9 using E5 embeddings. The general function is notational rather than algorithmic:

```
f(s) = cluster representative(s) if semantically equivalent,
       s ⊕ critical features if ambiguous,
       s otherwise
```

No exact string matching or hashing is explicitly described for ALFWorld.

## 3. Embedding vs. Exact Matching

- **ALFWorld/WebShop/Sokoban**: Feature enrichment (appending property changes)
- **DeepResearch**: "embedding-based node aggregation using a sentence transformer" with cosine similarity threshold 0.9

## 4. Graph Usage Beyond Reward Propagation

The paper does **not discuss** using state graphs for allocation decisions or sampling strategies. The graph is exclusively used for backward reward propagation.

## 5. Formal State Graph Definition

From equation (2):

> "state graph 𝒢_state = (𝒮, 𝒜, 𝒯) with the sets of states (𝒮), actions (𝒜), and transitions (𝒯)"

Nodes = states aggregated across trajectories; directed edges = observed state-action transitions with valid environment outcomes.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3ae61db-f77a-45c5-8597-1d37b61a1f04",
  "isSidechain": true,
  "promptId": "cfde047a-a2fc-4d3f-8aad-8bb03e31b224",
  "agentId": "ae39de92b4d475ccd",
  "type": "user",
  "uuid": "3356cc5c-6b7a-43e9-b799-709693405749",
  "sourceToolAssistantUUID": "c3ae61db-f77a-45c5-8597-1d37b61a1f04",
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

_source line 33 · 2026-05-12T01:43:44.216Z_

Now I have all the information needed. Here is my comprehensive report.

---

## Verification Report

### Paper 1: RewardFlow (arXiv 2603.18859, March 2026)

**Does the paper exist?** Yes. The paper is real and available at [arXiv 2603.18859](https://arxiv.org/abs/2603.18859). Full title: "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models" by Xiao Feng et al. (Hong Kong Baptist University, TCL, Shanghai Jiao Tong University). It also has an [OpenReview submission](https://openreview.net/forum?id=5oGJbM5u86).

**What does it actually do?** The description in the research idea is broadly accurate. RewardFlow:
- Constructs state graphs across multiple rollouts by aggregating observed states and transitions
- Performs multi-source inverse BFS from all successful terminal states
- Assigns state-level rewards via R(s) = gamma^d(s), where d is the shortest hop-distance to a success node
- Derives action-level rewards as potential differences: r(s_t, a_t) = R(s_{t+1}) - R(s_t)
- These dense rewards replace sparse terminal rewards during RL training

**ALFWorld "12.3% relative gain" claim -- partially accurate but misleading.** The 12.3% figure apparently refers to an average across model sizes, not the headline result. The actual numbers on ALFWorld for Qwen2.5-1.5B show RewardFlow at 68.8% vs. GiGPO at 53.1% (a ~29.5% relative gain). For the 7B model, RewardFlow achieves 89.8% vs. GiGPO at 82.8% (+7.0 absolute points, ~8.5% relative). The "12.3%" figure likely comes from averaging across model scales or comparing to a different baseline (e.g., GRPO). The claim is not fabricated, but citing it as "the" result is cherry-picked.

**How does RewardFlow's graph construction compare to STAG?**

This is the critical question. Key differences in state identification:

| Aspect | RewardFlow | Typical "STAG-like" approach |
|--------|-----------|------------------------------|
| **State matching (deterministic envs)** | Feature enrichment: appends detected property changes (e.g., "clean", "heat") to raw observations, then matches enriched text | Would typically use state hashing for exact matching |
| **State matching (stochastic envs)** | Embedding similarity via E5 sentence transformer, cosine threshold > 0.9, merging similar states into super-nodes | Could use similar or different mechanism |
| **Graph structure** | DAG of unique states + observed transitions, aggregated across all rollouts for a problem | Similar -- state graph or tree across rollouts |
| **Purpose of graph** | Exclusively reward estimation (backward BFS propagation) | Rollout allocation / exploration decisions |

**Does RewardFlow use state hashing?** No, not explicitly. For text-based environments like ALFWorld, it uses feature-enriched observation matching (essentially augmented string comparison). For stochastic environments, it uses embedding-based cosine similarity. The paper does not describe a hash function.

**Could RewardFlow's graph be trivially repurposed for rollout allocation?**

This is a nuanced question. The honest answer is: **the graph structure itself could in principle be reused, but the purpose and design choices diverge significantly.**

- RewardFlow builds the graph **post-hoc** from a batch of completed rollouts, purely to estimate rewards. It never uses the graph to guide future exploration.
- A rollout allocation system (like STAG) would need to build the graph **online/incrementally** and use graph properties (e.g., underexplored branches, high-uncertainty nodes) to decide where to sample next.
- RewardFlow's state normalization is designed for reward credit assignment accuracy, not for identifying exploration frontiers.
- However, the core data structure (state graph with transition edges across rollouts) is conceptually very similar. Someone familiar with RewardFlow would reasonably see how to extend it for allocation.

**Bottom line on novelty concern:** RewardFlow and a STAG-like system share the fundamental idea of "build a graph of states across rollouts." But RewardFlow uses this graph purely for backward reward propagation, while STAG would use it for forward exploration allocation. These are complementary rather than overlapping applications of the same data structure. That said, the graph construction methodology is similar enough that a reviewer could reasonably ask "how does your graph differ from RewardFlow's?" -- and the answer would need to emphasize the different state identification mechanism (hashing vs. enrichment/embedding) and the entirely different downstream use (allocation vs. reward estimation).

---

### Paper 2: RTMC (arXiv 2604.11037, April 2026)

**Does the paper exist?** Yes. The paper is real and available at [arXiv 2604.11037](https://arxiv.org/abs/2604.11037). Full title: "RTMC: Step-Level Credit Assignment via Rollout Trees" by Tao Wang, Suhang Zheng, and Xiaoxiao Xu (Alibaba Group).

**What does it actually do?** The description in the research idea is accurate. RTMC:
- Observes that multiple rollouts for the same problem often traverse overlapping intermediate states, forming an implicit tree
- Uses hand-crafted **state-action signatures** to identify matching states across rollouts: files partitioned into 100-line "view buckets," edits represented by 4-character MD5 hashes, operations tracked as order-invariant sets
- Computes first-visit Monte Carlo Q-values: Q_hat(s,a) = (1/N(s,a)) * sum of returns across all rollouts visiting (s,a)
- Derives advantages as A_hat = Q_hat - V_hat, with a Bayesian shrinkage prior to handle variance

**"Unbiased per-step MC advantages" claim -- mostly accurate.** The paper uses standard first-visit Monte Carlo estimation, which is unbiased by construction (assuming the state-action signatures correctly identify equivalent states). The paper does note they add a Bayesian shrinkage correction for high-variance estimates, which technically introduces a small bias for variance reduction, but the base estimator is unbiased.

**Key technical details:**
- The structure is technically a **tree** (not a DAG), because signatures encode cumulative history, so each signature appears at most once per rollout
- State identification is **purely rule-based** (no learned embeddings) -- a known limitation the authors acknowledge
- Only evaluated on **SWE-bench Verified** (500 problems), showing +3.2 percentage points over GRPO in pass@1
- The tree is used **only for advantage computation**, not for exploration or rollout allocation
- The authors explicitly note hand-crafted signatures as a limitation and suggest learned signatures as future work

---

### Summary Table

| Claim | Verdict |
|-------|---------|
| RewardFlow exists at arXiv 2603.18859 | **Confirmed** |
| RewardFlow builds state graphs and backpropagates rewards | **Confirmed** |
| RewardFlow achieves 12.3% relative gain on ALFWorld | **Partially accurate** -- this appears to be averaged across model sizes or vs. a specific baseline; individual model results range from ~8.5% to ~29.5% relative gains |
| RTMC exists at arXiv 2604.11037 | **Confirmed** |
| RTMC exploits implicit rollout tree structure | **Confirmed** |
| RTMC produces unbiased per-step MC advantages | **Mostly confirmed** -- base estimator is unbiased; Bayesian shrinkage adds slight bias for variance reduction |
| RewardFlow's graph could undermine STAG's novelty | **Partial concern** -- the graph data structure is similar, but RewardFlow uses it for reward estimation (backward), not rollout allocation (forward). The state identification mechanisms also differ (enrichment/embedding vs. hashing). A STAG paper should explicitly position against RewardFlow. |

Sources:
- [RewardFlow (arXiv abstract)](https://arxiv.org/abs/2603.18859)
- [RewardFlow (full HTML)](https://arxiv.org/html/2603.18859)
- [RewardFlow (OpenReview)](https://openreview.net/forum?id=5oGJbM5u86)
- [RTMC (arXiv abstract)](https://arxiv.org/abs/2604.11037)
- [RTMC (full HTML)](https://arxiv.org/html/2604.11037)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3356cc5c-6b7a-43e9-b799-709693405749",
  "isSidechain": true,
  "agentId": "ae39de92b4d475ccd",
  "requestId": "req_011Cawprj8cLh6mxSGRLqoQ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67b6150d-0048-4024-8bde-f0ad23cccd51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03bcb917-9559-42d4-a7c1-5c77316fe5b7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcWtj6nX3vr9VrTMUbHbtU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 18336,
      "output_tokens": 2101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 866
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2101,
          "cache_read_input_tokens": 18336,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 866,
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
