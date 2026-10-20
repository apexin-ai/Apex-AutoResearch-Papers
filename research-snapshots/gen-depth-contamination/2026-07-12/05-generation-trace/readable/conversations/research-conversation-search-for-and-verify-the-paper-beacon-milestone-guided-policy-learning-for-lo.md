# Research conversation: Search for and verify the paper "BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents" (arXiv:2605.

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa805466eb3d6d97b.jsonl`
- **Structured JSON:** [`b9eef37cf177e6823e2b.json`](../../sessions/b9/b9eef37cf177e6823e2b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-11T23:54:08.615Z_

Search for and verify the paper "BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents" (arXiv:2605.06078, May 2026). I need to know:
1. Does this paper actually exist? What are its actual results on ALFWorld and WebShop?
2. Does it use environment-native milestone signals with temporal decay shaping?
3. What model sizes does it use? Does it achieve 94.5% on ALFWorld and 79.7% on WebShop at 7B?
4. Does it use formal PBRS or informal shaping?
5. What codebase does it build on?

Use WebSearch and WebFetch to find and read this paper. Try multiple search queries:
- "BEACON milestone-guided policy learning language agents arXiv 2605.06078"
- "BEACON agentic RL milestone shaping ALFWorld 2026"
- Search on arxiv.org directly

Report everything you find, including if the paper doesn't exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "aa805466eb3d6d97b",
  "type": "user",
  "uuid": "955a0c02-5895-4371-93bf-30ace02c88ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:54:08.619Z_

```json
{
  "parentUuid": "955a0c02-5895-4371-93bf-30ace02c88ef",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
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
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f034157d-7cee-44ac-8a7c-b5da6bd6eddb",
  "timestamp": "2026-05-11T23:54:08.619Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:54:10.930Z_



I'll search for this paper using multiple approaches. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f034157d-7cee-44ac-8a7c-b5da6bd6eddb",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgaCv3W184utCsf9SX3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edef193f-f58f-45e7-a06b-215712eb24a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGMQof46rWC8Nxj9HC2Wdy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9006,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9006,
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

_source line 4 · 2026-05-11T23:54:11.232Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01D9gJnd2qPPLobGYt4MZ6Wb`</summary>

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
  "parentUuid": "edef193f-f58f-45e7-a06b-215712eb24a4",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgaCv3W184utCsf9SX3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34580896-6c06-4f1c-ae32-f70b8bedc803",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGMQof46rWC8Nxj9HC2Wdy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9006,
      "cache_read_input_tokens": 0,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9006,
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

_source line 5 · 2026-05-11T23:54:11.237Z_

<details><summary>↩ Tool result · `toolu_01D9gJnd2qPPLobGYt4MZ6Wb`</summary>

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
  "parentUuid": "34580896-6c06-4f1c-ae32-f70b8bedc803",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "aa805466eb3d6d97b",
  "type": "user",
  "uuid": "ad28a62e-28dc-41ce-a342-31d344b01a67",
  "sourceToolAssistantUUID": "34580896-6c06-4f1c-ae32-f70b8bedc803",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:54:13.406Z_



Now let me run multiple searches in parallel to find this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad28a62e-28dc-41ce-a342-31d344b01a67",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgaQNrxDY2wcPavseho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bacc5cdf-452a-4a6e-a35b-c4b2ce5e6215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185WXaaQSDQAdyi9RMq1Bmp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 7 · 2026-05-11T23:54:14.359Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VkmHTX4XTygsnnf62krA7G`</summary>

```json
{
  "query": "BEACON milestone-guided policy learning language agents arXiv 2605.06078"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bacc5cdf-452a-4a6e-a35b-c4b2ce5e6215",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgaQNrxDY2wcPavseho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7562715-4245-487e-9ead-9f1be592b956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185WXaaQSDQAdyi9RMq1Bmp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 8 · 2026-05-11T23:54:15.319Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0125NjdFJH2X4qEenatfAcQG`</summary>

```json
{
  "query": "BEACON agentic RL milestone shaping ALFWorld 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7562715-4245-487e-9ead-9f1be592b956",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgaQNrxDY2wcPavseho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b91f7a4b-fb0d-4c65-8123-ac683b318484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185WXaaQSDQAdyi9RMq1Bmp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 9 · 2026-05-11T23:54:15.706Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KAkS1SwsYhW9uRwx5D8Exg`</summary>

```json
{
  "query": "arXiv 2605.06078 BEACON milestone guided policy",
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
  "parentUuid": "b91f7a4b-fb0d-4c65-8123-ac683b318484",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgaQNrxDY2wcPavseho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03a885ea-8f6e-46ab-bfba-466f870b6bd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185WXaaQSDQAdyi9RMq1Bmp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 9006,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1914
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 207,
          "cache_read_input_tokens": 9006,
          "cache_creation_input_tokens": 1914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1914,
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

_source line 10 · 2026-05-11T23:54:20.675Z_

<details><summary>↩ Tool result · `toolu_01VkmHTX4XTygsnnf62krA7G`</summary>

```text
Web search results for query: "BEACON milestone-guided policy learning language agents arXiv 2605.06078"

Links: [{"title":"[2605.06078] Milestone-Guided Policy Learning for Long-Horizon Language Agents","url":"https://arxiv.org/abs/2605.06078"},{"title":"Milestone-Guided Policy Learning for Long-Horizon Language Agents","url":"https://arxiv.org/html/2605.06078"},{"title":"[2605.07579] Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor's Internal States","url":"https://arxiv.org/abs/2605.07579"},{"title":"[1811.07882] Guiding Policies with Language via Meta-Learning","url":"https://arxiv.org/abs/1811.07882"},{"title":"[2405.04118] Policy Learning with a Language Bottleneck","url":"https://arxiv.org/abs/2405.04118"},{"title":"[2605.06448] Performance guaranteed MPC Policy Approximation via Cost Guided Learning","url":"https://arxiv.org/abs/2605.06448"},{"title":"[2605.02335] LLM-enabled Social Agents","url":"https://arxiv.org/abs/2605.02335"},{"title":"Words as Beacons: Guiding RL Agents with High-Level Language Prompts","url":"https://arxiv.org/html/2410.08632"},{"title":"BEACON: Behavioral Malware Classification with Large Language Model Embeddings and Deep Learning","url":"https://arxiv.org/html/2509.14519v1"},{"title":"Language Model Guided Reinforcement Learning in Quantitative TradingPreprint under review for FLLM 2025.","url":"https://arxiv.org/html/2508.02366v1"}]

Based on the search results, here's what I found about BEACON:

BEACON is a milestone-guided policy learning framework that leverages the compositional structure of long-horizon tasks to ensure precise credit assignment.

**Problem it addresses:**
While long-horizon agentic tasks require language agents to perform dozens of sequential decisions, training such agents with reinforcement learning remains challenging due to two root causes: credit misattribution, where correct early actions are penalized due to terminal failures, and sample inefficiency, where scarce successful trajectories result in near-total loss of learning signal.

**How it works:**
BEACON partitions trajectories at milestone boundaries, applies temporal reward shaping within segments to credit partial progress, and estimates advantages at dual scales to prevent distant failures from corrupting the evaluation of local actions.

**Performance results:**
On ALFWorld, WebShop, and ScienceWorld, BEACON consistently outperforms GRPO and GiGPO. More specifically, on long-horizon ALFWorld tasks, BEACON achieves 92.9% success rate, nearly doubling GRPO's 53.5%, while improving effective sample utilization from 23.7% to 82.0%.

The paper was submitted to arXiv on May 7, 2026, and code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7562715-4245-487e-9ead-9f1be592b956",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "aa805466eb3d6d97b",
  "type": "user",
  "uuid": "2567f98c-a7f6-4c86-95e0-d64bac0c8a5c",
  "sourceToolAssistantUUID": "e7562715-4245-487e-9ead-9f1be592b956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-11T23:54:21.791Z_

<details><summary>↩ Tool result · `toolu_0125NjdFJH2X4qEenatfAcQG`</summary>

```text
Web search results for query: "BEACON agentic RL milestone shaping ALFWorld 2026"

Links: [{"title":"Milestone-Guided Policy Learning for Long-Horizon Language Agents","url":"https://arxiv.org/html/2605.06078"},{"title":"GitHub - Gen-Verse/Open-AgentRL: [ICML 2026] RLAnything & DemyAgent: General and scalable agentic RL algorithms across terminal, GUI, SWE, and tool-call settings · GitHub","url":"https://github.com/Gen-Verse/Open-AgentRL"},{"title":"AGENTRL: SCALING AGENTIC REINFORCEMENT ...","url":"https://openreview.net/pdf?id=zq3vAmuUk9"},{"title":"Rethinking Experience Utilization in Self-Evolving Language Model Agents","url":"https://arxiv.org/html/2605.07164"},{"title":"Agentic Critical Training","url":"https://arxiv.org/html/2603.08706v1"},{"title":"Agent2 RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?","url":"https://arxiv.org/html/2604.10547"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models","url":"https://arxiv.org/html/2601.08955v2"},{"title":"The Rise of Reinforcement Learning Gyms and the Future of Agentic AI - Norwest","url":"https://www.norwest.com/blog/the-rise-of-reinforcement-learning-gyms-and-the-future-of-agentic-ai/"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=5oGJbM5u86"}]

Based on the search results, I found information about **BEACON**, a milestone-guided policy learning framework for agentic reinforcement learning:

## BEACON Overview

BEACON is a milestone-guided policy learning framework that leverages the compositional structure of long-horizon tasks to ensure precise credit assignment. It partitions trajectories at milestone boundaries, applies temporal reward shaping within segments to credit partial progress, and estimates advantages at dual scales to prevent distant failures from corrupting the evaluation of local actions.

## Performance on ALFWorld

On long-horizon ALFWorld tasks, BEACON achieves 92.9% success rate, nearly doubling GRPO's 53.5%, while improving effective sample utilization from 23.7% to 82.0%. BEACON consistently outperforms GRPO and GiGPO on ALFWorld, WebShop, and ScienceWorld.

## Key Innovation

BEACON exploits semantic milestones inherent to agentic tasks, enabling segment-level comparison within trajectories. Milestone-anchored credit assignment is an effective paradigm for training long-horizon language agents.

The code for BEACON is available on GitHub, and the research demonstrates how milestone-based reward shaping addresses fundamental challenges in training agents on long-horizon tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b91f7a4b-fb0d-4c65-8123-ac683b318484",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "aa805466eb3d6d97b",
  "type": "user",
  "uuid": "479e684b-9c7f-455a-bba3-d27e80c8625b",
  "sourceToolAssistantUUID": "b91f7a4b-fb0d-4c65-8123-ac683b318484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:54:23.817Z_

<details><summary>↩ Tool result · `toolu_01KAkS1SwsYhW9uRwx5D8Exg`</summary>

```text
Web search results for query: "arXiv 2605.06078 BEACON milestone guided policy"

Links: [{"title":"[2605.06078] Milestone-Guided Policy Learning for Long-Horizon Language Agents","url":"https://arxiv.org/abs/2605.06078"},{"title":"Milestone-Guided Policy Learning for Long-Horizon Language Agents","url":"https://arxiv.org/html/2605.06078"},{"title":"[2605.01978] Stability of Control Lyapunov Function Guided Reinforcement Learning","url":"https://arxiv.org/abs/2605.01978"},{"title":"BEACON: A Bayesian Optimization Strategy for Novelty Search in Expensive Black-Box Systems","url":"https://arxiv.org/html/2406.03616v1"},{"title":"[2605.06670] Stochastic Policy Gradient Methods in the Uncertain Volatility Model","url":"https://arxiv.org/abs/2605.06670"},{"title":"Long Context Compression with Activation Beacon","url":"https://arxiv.org/pdf/2401.03462"},{"title":"[2605.06448] Performance guaranteed MPC Policy Approximation via Cost Guided Learning","url":"https://arxiv.org/abs/2605.06448"},{"title":"beacon, a lightweight deep reinforcement learning benchmark library for flow control","url":"https://arxiv.org/html/2402.17402v2"},{"title":"[2605.05511] Non-Myopic Active Feature Acquisition via Pathwise Policy Gradients","url":"https://arxiv.org/abs/2605.05511"},{"title":"Performance guaranteed MPC Policy Approximation via Cost Guided Learning","url":"https://arxiv.org/html/2605.06448"}]

Based on the search results, here's the information about arXiv paper 2605.06078:

BEACON is a milestone-guided policy learning framework that leverages the compositional structure of long-horizon tasks to ensure precise credit assignment. 

The paper addresses the challenge of training language agents with reinforcement learning on long-horizon agentic tasks, identifying two root causes: credit misattribution (where correct early actions are penalized due to terminal failures) and sample inefficiency (where scarce successful trajectories result in near-total loss of learning signal).

BEACON partitions trajectories at milestone boundaries, applies temporal reward shaping within segments to credit partial progress, and estimates advantages at dual scales to prevent distant failures from corrupting the evaluation of local actions.

On long-horizon ALFWorld tasks, BEACON achieves 92.9% success rate, nearly doubling GRPO's 53.5%, while improving effective sample utilization from 23.7% to 82.0%. On ALFWorld, WebShop, and ScienceWorld, BEACON consistently outperforms GRPO and GiGPO.

The paper was submitted on May 7, 2026, and code is available at https://github.com/ZJU-REAL/BEACON.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03a885ea-8f6e-46ab-bfba-466f870b6bd2",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "aa805466eb3d6d97b",
  "type": "user",
  "uuid": "eef8c4e7-6539-400f-872a-f6a931aad5cc",
  "sourceToolAssistantUUID": "03a885ea-8f6e-46ab-bfba-466f870b6bd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-11T23:54:27.357Z_

The paper exists. Now let me fetch the actual arXiv abstract page and the full HTML paper to get precise details on all your questions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eef8c4e7-6539-400f-872a-f6a931aad5cc",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgbKtGXmwqSC8VvWMJd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2e02141-2607-408d-a311-a370f532b549",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNpArDiEHgnJ8HPPP7xbfw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2630,
      "cache_read_input_tokens": 10920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2630,
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

_source line 14 · 2026-05-11T23:54:29.760Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RRR69RVSPm42Y9f4EDbCy2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06078",
  "prompt": "Extract all details: full title, all authors, abstract, submission date, any mentioned results (exact numbers on ALFWorld, WebShop, ScienceWorld), model sizes, methods used, codebase, and any mention of PBRS (potential-based reward shaping), temporal decay, milestone signals, reward shaping approach."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2e02141-2607-408d-a311-a370f532b549",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgbKtGXmwqSC8VvWMJd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "736f3068-6e98-4f5c-ba4f-c55a86b70cd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNpArDiEHgnJ8HPPP7xbfw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2630,
      "cache_read_input_tokens": 10920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2630,
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

_source line 15 · 2026-05-11T23:54:34.132Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C9CRkk6C8AJbEUANX6rhdy`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06078",
  "prompt": "Extract ALL details about: 1) Exact benchmark results on ALFWorld, WebShop, and ScienceWorld (all numbers, all model sizes), 2) Whether it uses formal PBRS (potential-based reward shaping) or informal shaping, 3) Whether it uses temporal decay shaping, 4) What the milestone signals are and how they are obtained (environment-native or learned), 5) What base model sizes are used (7B, 8B, etc.), 6) What codebase or framework it builds on (e.g. verl, OpenRLHF, trl, etc.), 7) Any mention of 94.5% on ALFWorld or 79.7% on WebShop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "736f3068-6e98-4f5c-ba4f-c55a86b70cd9",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgbKtGXmwqSC8VvWMJd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf90cf91-632d-4f87-b301-4fe43b55a2b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNpArDiEHgnJ8HPPP7xbfw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2630,
      "cache_read_input_tokens": 10920,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2630
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 410,
          "cache_read_input_tokens": 10920,
          "cache_creation_input_tokens": 2630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2630,
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

_source line 16 · 2026-05-11T23:54:35.959Z_

<details><summary>↩ Tool result · `toolu_01RRR69RVSPm42Y9f4EDbCy2`</summary>

```text
# Paper Details: Milestone-Guided Policy Learning for Long-Horizon Language Agents

**Full Title:** "Milestone-Guided Policy Learning for Long-Horizon Language Agents"

**Authors:** Zixuan Wang, Yuchen Yan, Hongxing Li, Teng Pan, Dingming Li, Ruiqing Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

**Submission Date:** May 7, 2026

**arXiv ID:** 2605.06078

## Key Results

The framework called BEACON demonstrated substantial performance improvements:
- **ALFWorld (long-horizon):** 92.9% success rate versus GRPO's 53.5%
- **Sample efficiency:** Improved from 23.7% to 82.0% effective utilization
- **Comparison baselines:** Outperformed GRPO and GiGPO across all environments tested (ALFWorld, WebShop, ScienceWorld)

## Methods & Approach

The paper identifies and addresses two core training challenges: "credit misattribution, where correct early actions are penalized due to terminal failures" and sample inefficiency. The solution employs:

- Trajectory partitioning at milestone boundaries
- Temporal reward shaping applied within segments
- Dual-scale advantage estimation to prevent distant failures from affecting local action evaluation

## Code Availability

Code is available via GitHub at the repository: ZJU-REAL/BEACON

## Note on Specific Details

The abstract does not explicitly mention PBRS (potential-based reward shaping), temporal decay specifications, or model sizes. The reward shaping approach is described contextually rather than by formal terminology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "736f3068-6e98-4f5c-ba4f-c55a86b70cd9",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "aa805466eb3d6d97b",
  "type": "user",
  "uuid": "99c0c35d-309d-41a1-97d1-f7bf61ba4599",
  "sourceToolAssistantUUID": "736f3068-6e98-4f5c-ba4f-c55a86b70cd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T23:54:40.782Z_

<details><summary>↩ Tool result · `toolu_01C9CRkk6C8AJbEUANX6rhdy`</summary>

```text
# BEACON: Benchmark Results and Technical Details

## 1) Exact Benchmark Results

**ALFWorld (Qwen2.5-1.5B-Instruct):**
- Short: 96.8% | Medium: 87.0% | Long: 92.9% | Average: 91.4%

**ALFWorld (Qwen2.5-7B-Instruct):**
- Short: 95.1% | Medium: 94.9% | Long: 90.0% | Average: 94.5%

**WebShop (Qwen2.5-1.5B-Instruct):** 75.6% success

**WebShop (Qwen2.5-7B-Instruct):** 79.7% success

**ScienceWorld (Qwen2.5-1.5B-Instruct):** 45.3% success

**ScienceWorld (Qwen2.5-7B-Instruct):** 64.3% success

## 2) Reward Shaping Type

The paper uses **informal temporal reward shaping**, not formal potential-based reward shaping (PBRS). The approach applies "temporal reward decay" within segments.

## 3) Temporal Decay Shaping

Yes, extensively. The authors employ: "temporal reward shaping assigns higher credit to actions closer to milestone completion" with decay factor γ=0.95 across all benchmarks.

## 4) Milestone Signals

**Source:** Environment-native, directly observable. The paper states: "Φ detects observable state changes from environment feedback...does not require learned models or manual annotation."

- **ALFWorld:** Object state changes (pick-up, heating completion)
- **WebShop:** Page transitions advancing toward target product
- **ScienceWorld:** "Environment provides explicit subgoal signals"

## 5) Base Model Sizes

- Qwen2.5-1.5B-Instruct
- Qwen2.5-7B-Instruct

## 6) Codebase/Framework

Not specified in the document. Code availability mentioned: "available at https://github.com/ZJU-REAL/BEACON" but no framework details provided.

## 7) Specific Numbers Mentioned

Yes, both figures appear: "94.5% on ALFWorld" and "79.7% on WebShop" (7B model results).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf90cf91-632d-4f87-b301-4fe43b55a2b7",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "aa805466eb3d6d97b",
  "type": "user",
  "uuid": "33692242-64a3-4e5e-bdc4-30bd6dac0dc9",
  "sourceToolAssistantUUID": "cf90cf91-632d-4f87-b301-4fe43b55a2b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-11T23:54:48.429Z_

Excellent. I have very detailed results. Let me also check the GitHub repository to identify what codebase/framework BEACON builds on.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33692242-64a3-4e5e-bdc4-30bd6dac0dc9",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgcaT9VJTF2rNcxBuZA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f66c10c4-de30-4691-915e-432c38e2185a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UX9TVmfY5ekuznyri2rr8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 13550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1429,
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

_source line 19 · 2026-05-11T23:54:50.809Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018yAMsNsMR3TWDLTKDg1hvF`</summary>

```json
{
  "url": "https://github.com/ZJU-REAL/BEACON",
  "prompt": "What codebase or framework does BEACON build on? Look for mentions of verl, OpenRLHF, trl, DeepSpeed, vLLM, or any other RL training framework in the README, requirements, dependencies, or code structure. Also note any other technical details about the implementation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f66c10c4-de30-4691-915e-432c38e2185a",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgcaT9VJTF2rNcxBuZA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f040e7ab-c1c4-4904-824a-dc813aaafc37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UX9TVmfY5ekuznyri2rr8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 13550,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1429
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 13550,
          "cache_creation_input_tokens": 1429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1429,
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

_source line 20 · 2026-05-11T23:54:56.023Z_

<details><summary>↩ Tool result · `toolu_018yAMsNsMR3TWDLTKDg1hvF`</summary>

```text
# BEACON Framework Dependencies

BEACON builds on **verl-agent**, as explicitly stated in the README:

> "The implementation is built on top of [verl-agent](https://github.com/langfengQ/verl-agent); only the components contributed by this work are documented here."

The Acknowledgement section further clarifies that verl-agent itself extends **veRL**, another upstream framework:

> "This codebase builds on [verl-agent](https://github.com/langfengQ/verl-agent), which itself extends [veRL](https://github.com/volcengine/verl)."

## Technical Stack

Beyond the core framework, BEACON relies on:
- **PyTorch 2.6.0** and **CUDA 12.4**
- **vLLM 0.8.5** (inference engine)
- **Flash Attention 2.7.4**
- Environment-specific dependencies for ALFWorld, WebShop, and ScienceWorld

The repository structure shows BEACON's own contributions are isolated in `migpo/` (advantage and reward computation) and `agent_system/` (environment integrations), while inheriting most infrastructure from verl-agent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f040e7ab-c1c4-4904-824a-dc813aaafc37",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "aa805466eb3d6d97b",
  "type": "user",
  "uuid": "69e9cd3d-f2a7-4327-a4a1-76ce201bf52f",
  "sourceToolAssistantUUID": "f040e7ab-c1c4-4904-824a-dc813aaafc37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-11T23:55:14.874Z_

I now have comprehensive information to answer all your questions. Here is the full report:

---

## Findings on "BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents" (arXiv:2605.06078)

### 1. Does the paper exist? What are its actual results?

**Yes, the paper exists.** It was submitted to arXiv on May 7, 2026, by Zixuan Wang, Yuchen Yan, Hongxing Li, Teng Pan, Dingming Li, Ruiqing Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, and Yongliang Shen (ZJU-REAL group).

**Actual results:**

| Benchmark | Qwen2.5-1.5B | Qwen2.5-7B |
|-----------|-------------|------------|
| ALFWorld (Short) | 96.8% | 95.1% |
| ALFWorld (Medium) | 87.0% | 94.9% |
| ALFWorld (Long) | 92.9% | 90.0% |
| ALFWorld (Average) | 91.4% | **94.5%** |
| WebShop | 75.6% | **79.7%** |
| ScienceWorld | 45.3% | 64.3% |

The headline number often cited from the abstract (92.9%) is specifically the **long-horizon ALFWorld** result at **1.5B**, not the overall average.

### 2. Does it use environment-native milestone signals with temporal decay shaping?

**Yes to both.**

- **Environment-native milestones:** The milestone detector Phi "detects observable state changes from environment feedback" and "does not require learned models or manual annotation." In ALFWorld these are object state changes (pick-up, heating completion); in WebShop they are page transitions toward the target product; in ScienceWorld the environment provides explicit subgoal signals.
- **Temporal decay shaping:** The paper applies temporal reward shaping that "assigns higher credit to actions closer to milestone completion" with a decay factor gamma = 0.95 across all benchmarks.

### 3. Model sizes and the specific numbers 94.5% / 79.7%?

**Model sizes:** Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct.

**Yes, both numbers are confirmed at 7B:**
- **94.5% on ALFWorld** (average across short/medium/long) with Qwen2.5-7B
- **79.7% on WebShop** with Qwen2.5-7B

These are the paper's actual reported results.

### 4. Formal PBRS or informal shaping?

**Informal shaping.** The paper does NOT use formal potential-based reward shaping (PBRS). It applies an informal temporal reward decay within milestone-delimited segments. There is no mention of potential functions or the PBRS theoretical framework (Ng et al., 1999).

### 5. What codebase does it build on?

BEACON builds on **verl-agent** (https://github.com/langfengQ/verl-agent), which itself extends **veRL** (https://github.com/volcengine/verl). The technical stack includes PyTorch 2.6.0, CUDA 12.4, vLLM 0.8.5, and Flash Attention 2.7.4. BEACON's own contributions are isolated in `migpo/` (advantage and reward computation) and `agent_system/` (environment integrations), inheriting most RL training infrastructure from verl-agent.

---

Sources:
- [arXiv Abstract: 2605.06078](https://arxiv.org/abs/2605.06078)
- [Full HTML Paper: 2605.06078](https://arxiv.org/html/2605.06078)
- [GitHub: ZJU-REAL/BEACON](https://github.com/ZJU-REAL/BEACON)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69e9cd3d-f2a7-4327-a4a1-76ce201bf52f",
  "isSidechain": true,
  "agentId": "aa805466eb3d6d97b",
  "requestId": "req_011CawgdhZZS2StXmgMd2PZX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bab382f7-4091-445d-a430-1c0164e960cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jYdoyYG2AnENED5rLqjTG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 14979,
      "output_tokens": 979,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 465
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 979,
          "cache_read_input_tokens": 14979,
          "cache_creation_input_tokens": 465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 465,
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
