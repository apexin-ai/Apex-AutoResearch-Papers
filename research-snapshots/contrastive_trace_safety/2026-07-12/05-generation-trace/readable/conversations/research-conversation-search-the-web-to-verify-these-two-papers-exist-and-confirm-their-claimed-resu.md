# Research conversation: Search the web to verify these two papers exist and confirm their claimed results: 1. SWE-RM (arXiv:2512.21919, Dec 2025

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a59c710e946146e09.jsonl`
- **Structured JSON:** [`43cbded003c7ac95b00e.json`](../../sessions/43/43cbded003c7ac95b00e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-10T18:28:41.636Z_

Search the web to verify these two papers exist and confirm their claimed results:

1. SWE-RM (arXiv:2512.21919, Dec 2025) - Claims to be a 30B MoE reward model for SWE agents achieving 51.6→62.0% (Flash) and 67.0→74.6% (Max) on SWE-bench Verified via best-of-N. From the Qwen team.

2. SWE-Shepherd (arXiv:2604.10493, April 2026) - Claims step-level action-utility PRMs for SWE agents achieving only 51% vs. 57% greedy baseline on 100 SWE-bench Verified tasks.

For each:
- Search for the paper on arxiv (use WebSearch with queries like "SWE-RM arXiv 2512.21919" and "SWE-Shepherd arXiv 2604.10493")
- Verify the paper exists and confirm the claimed numbers
- Note any discrepancies between what's claimed in the proposal and what the actual paper says

Report your findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "c810a1a6-6c0b-48d2-a66d-4e9c6225bdb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:28:41.640Z_

```json
{
  "parentUuid": "c810a1a6-6c0b-48d2-a66d-4e9c6225bdb4",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
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
  "uuid": "6d6bd60f-248d-4ba2-b277-0707056e8264",
  "timestamp": "2026-05-10T18:28:41.640Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T18:28:44.636Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HGkFSPwvvdkyEgsxEnVSRr`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d6bd60f-248d-4ba2-b277-0707056e8264",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauMwtHGGzxiDayrEE31b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b58e8f8f-f042-4836-aaad-4e13d94ac272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RuFxbSgCzfohmP7e2m2To2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9035,
      "cache_read_input_tokens": 0,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9035
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9035,
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

_source line 4 · 2026-05-10T18:28:44.644Z_

<details><summary>↩ Tool result · `toolu_01HGkFSPwvvdkyEgsxEnVSRr`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b58e8f8f-f042-4836-aaad-4e13d94ac272",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "9c7e6b21-1785-4d6f-826d-671b1784abf6",
  "sourceToolAssistantUUID": "b58e8f8f-f042-4836-aaad-4e13d94ac272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T18:28:48.516Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014SNnfZb7pmhVWRrGrQXiLT`</summary>

```json
{
  "query": "SWE-RM arXiv 2512.21919 reward model SWE agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c7e6b21-1785-4d6f-826d-671b1784abf6",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauMx7CtWRN9ahQ5ao1xY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5086bf7-9380-4c20-9d8d-eb98c73b752e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFej9HFMxmvc3YFiSWxpx3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T18:28:48.747Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RnKGQZL7JRfyogM7mJCfmf`</summary>

```json
{
  "query": "SWE-Shepherd arXiv 2604.10493 step-level PRM SWE agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5086bf7-9380-4c20-9d8d-eb98c73b752e",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauMx7CtWRN9ahQ5ao1xY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b117031-61b7-48a5-96df-c73a7e7208d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFej9HFMxmvc3YFiSWxpx3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9035,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 133,
          "cache_read_input_tokens": 9035,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-10T18:28:55.307Z_

<details><summary>↩ Tool result · `toolu_014SNnfZb7pmhVWRrGrQXiLT`</summary>

```text
Web search results for query: "SWE-RM arXiv 2512.21919 reward model SWE agents"

Links: [{"title":"[2512.21919] SWE-RM: Execution-free Feedback For Software Engineering Agents","url":"https://arxiv.org/abs/2512.21919"},{"title":"SWE-RM: Execution-free Feedback For Software Engineering Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.21919v1"},{"title":"SWE-RM: Execution-Free Feedback for Software Engineering Agents","url":"https://arxiv.org/html/2512.21919"},{"title":"2025-12-29 SWE-RM: EXECUTION-FREE FEEDBACK FOR SOFT- WARE ENGINEERING AGENTS","url":"https://www.arxiv.org/pdf/2512.21919"},{"title":"Paper page - SWE-RM: Execution-free Feedback For Software Engineering Agents","url":"https://huggingface.co/papers/2512.21919"},{"title":"Natural Language Processing Papers on X: \"SWE-RM: Execution-free Feedback For Software Engineering Agents KaShun Shum, Binyuan Hui, Jiawei Chen, Lei Zhang, X. W., Jiaxi Yang, Yuzhen Huang, Junyang Lin, Junxian He (arXiv:2512.21919) https://t.co/6Ek3le9WwT\" / X","url":"https://x.com/HEI/status/2005573373896597610"},{"title":"SWE-RM: Execution-free Feedback for Software Engineering Agents | OpenReview","url":"https://openreview.net/forum?id=H9wMe1G76j"},{"title":"Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards","url":"https://arxiv.org/html/2506.11425v2"},{"title":"Execution-Free Feedback in SWE-RM Verifiers","url":"https://www.emergentmind.com/topics/execution-free-feedback"},{"title":"SWE-RM: Execution-free Feedback For Software Engineering Agents","url":"https://www.researchgate.net/publication/399135623_SWE-RM_Execution-free_Feedback_For_Software_Engineering_Agents"}]

Based on the search results, here's what I found about SWE-RM (arXiv:2512.21919):

## Overview

SWE-RM is a paper titled "Execution-free Feedback For Software Engineering Agents" by KaShun Shum and 8 other authors. It was submitted on December 26, 2025.

## Key Problem

Execution-based feedback like unit testing is widely used in the development of coding agents through test-time scaling (TTS) and reinforcement learning (RL), but this paradigm requires scalable and reliable collection of unit test cases to provide accurate feedback, and the resulting feedback is often sparse and cannot effectively distinguish between trajectories that are both successful or both unsuccessful.

## Solution

Execution-free feedback from reward models can provide more fine-grained signals without depending on unit test cases. The authors introduce SWE-RM, an accurate and robust reward model adopting a mixture-of-experts architecture with 30B total parameters and 3B activated during inference.

## Performance

SWE-RM increases the accuracy of Qwen3-Coder-Flash from 51.6% to 62.0%, and Qwen3-Coder-Max from 67.0% to 74.6% on SWE-Bench Verified using TTS.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5086bf7-9380-4c20-9d8d-eb98c73b752e",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "b7dddcc1-bd7d-4b86-964c-4bb464e18efe",
  "sourceToolAssistantUUID": "e5086bf7-9380-4c20-9d8d-eb98c73b752e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T18:28:55.466Z_

<details><summary>↩ Tool result · `toolu_01RnKGQZL7JRfyogM7mJCfmf`</summary>

```text
Web search results for query: "SWE-Shepherd arXiv 2604.10493 step-level PRM SWE agents"

Links: [{"title":"[2604.10493] SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/abs/2604.10493"},{"title":"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/html/2604.10493"},{"title":"SWE-TRACE: Optimizing Long-Horizon SWE Agents through Rubric Process Reward Models and Heuristic Test-Time Scaling","url":"https://arxiv.org/html/2604.14820v1"},{"title":"Act Like You’re Paying for This: Course-Correcting Code Agents with PRMs","url":"https://arxiv.org/html/2509.02360v1"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/html/2509.02360"},{"title":"Web-Shepherd: Advancing PRMs for Reinforcing Web Agents","url":"https://arxiv.org/html/2505.15277"},{"title":"[2604.14820] SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling","url":"https://arxiv.org/abs/2604.14820"},{"title":"[2505.15277] Web-Shepherd: Advancing PRMs for Reinforcing Web Agents","url":"https://arxiv.org/abs/2505.15277"},{"title":"MATH-SHEPHERD: VERIFY AND REINFORCE LLMS STEP-BY-STEP WITHOUT HUMAN ANNOTATIONS","url":"https://arxiv.org/pdf/2312.08935"},{"title":"[2509.02360] When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/abs/2509.02360"}]

Based on the search results, here's what I found about SWE-Shepherd (arXiv 2604.10493):

SWE-Shepherd is a framework that introduces Process Reward Models (PRMs) to provide dense, step-level supervision for repository-level code agents.

**Key Features:**

- SWE-Shepherd converts agent trajectories into dense, step-level supervision by assigning scalar rewards to intermediate actions according to their estimated contribution toward resolving the issue.

- Using trajectories from SWE-Bench, the framework constructs an action-level reward dataset and trains a lightweight reward model on a base LLM to estimate the usefulness of intermediate actions. During inference, the PRM evaluates candidate actions and guides the agent toward higher-reward decisions without requiring full reinforcement learning.

**Results:**

- Experiments on SWE-Bench Verified demonstrate improved interaction efficiency and action quality, while also highlighting challenges in aligning intermediate rewards with final task success.

**Authors:**

The paper was submitted on April 12, 2026 by Mahir Labib Dihan and Md Ashrafur Rahman Khan.

The framework addresses limitations in existing SWE agent approaches by providing fine-grained feedback on intermediate decisions rather than relying solely on sparse final success signals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b117031-61b7-48a5-96df-c73a7e7208d3",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "476212f5-fae6-407d-aace-7a535f23fc83",
  "sourceToolAssistantUUID": "0b117031-61b7-48a5-96df-c73a7e7208d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T18:28:58.778Z_

Now let me get more details on the SWE-Shepherd paper's specific numerical results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "476212f5-fae6-407d-aace-7a535f23fc83",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauMxtgbYSof1azFvsSy9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6557c30f-5407-4c48-9c83-a006ff10f696",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X674eDsi4H7inGysz23nkQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1936,
      "cache_read_input_tokens": 10427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1936,
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

_source line 10 · 2026-05-10T18:28:59.469Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ARmST1fSbJFfY99JGuRaw6`</summary>

```json
{
  "query": "SWE-Shepherd 2604.10493 results SWE-bench Verified percentage accuracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6557c30f-5407-4c48-9c83-a006ff10f696",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauMxtgbYSof1azFvsSy9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2db21b6b-e1f1-4147-8329-52795fa7af54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X674eDsi4H7inGysz23nkQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1936,
      "cache_read_input_tokens": 10427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1936,
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

_source line 11 · 2026-05-10T18:28:59.759Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FaU7ZKS8WqHr4Q7rWTnKGs`</summary>

```json
{
  "query": "SWE-RM Qwen team authors Qwen3-Coder best-of-N"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2db21b6b-e1f1-4147-8329-52795fa7af54",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauMxtgbYSof1azFvsSy9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c82546ad-7e4c-49bd-95d9-b1397f9ef73d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X674eDsi4H7inGysz23nkQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1936,
      "cache_read_input_tokens": 10427,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 10427,
          "cache_creation_input_tokens": 1936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1936,
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

_source line 12 · 2026-05-10T18:29:03.881Z_

<details><summary>↩ Tool result · `toolu_01ARmST1fSbJFfY99JGuRaw6`</summary>

```text
Web search results for query: "SWE-Shepherd 2604.10493 results SWE-bench Verified percentage accuracy"

Links: [{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"[2604.10493] SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/abs/2604.10493"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/html/2604.10493"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-bench Results Viewer","url":"https://www.swebench.com/viewer.html"}]

Based on the search results, I found information about the SWE-Shepherd paper (arXiv 2604.10493). SWE-Shepherd is a framework that introduces Process Reward Models (PRMs) to provide dense, step-level supervision for repository-level code agents, using trajectories from SWE-Bench to construct an action-level reward dataset and train a lightweight reward model.

However, the search results do not contain the specific percentage accuracy results on SWE-bench Verified. The abstract mentions that experiments on SWE-Bench Verified demonstrate improved interaction efficiency and action quality, but the actual accuracy percentages are not included in these search result excerpts.

To find the specific accuracy percentage, you would need to access the full paper on arXiv or check the official SWE-bench Verified leaderboards at swebench.com, which appears to have detailed benchmark results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2db21b6b-e1f1-4147-8329-52795fa7af54",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "dab42248-f60a-47bc-b0e1-8e4e434f21b1",
  "sourceToolAssistantUUID": "2db21b6b-e1f1-4147-8329-52795fa7af54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:29:06.390Z_

<details><summary>↩ Tool result · `toolu_01FaU7ZKS8WqHr4Q7rWTnKGs`</summary>

```text
Web search results for query: "SWE-RM Qwen team authors Qwen3-Coder best-of-N"

Links: [{"title":"Qwen3-Coder-Next: Pushing Small Hybrid Models","url":"https://qwen.ai/blog?id=qwen3-coder-next"},{"title":"Qwen/Qwen3-Coder-Next · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Coder-Next"},{"title":"Qwen3-Coder-Next Technical Report","url":"https://arxiv.org/html/2603.00729v1"},{"title":"GitHub - QwenLM/Qwen3-Coder: Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. · GitHub","url":"https://github.com/QwenLM/Qwen3-Coder"},{"title":"Qwen3-Coder: Agentic Coding in the World | Qwen","url":"https://qwenlm.github.io/blog/qwen3-coder/"},{"title":"Qwen/Qwen3-Coder-480B-A35B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct"},{"title":"2026-03-03 Qwen3-Coder-Next Technical Report Qwen Team","url":"https://arxiv.org/pdf/2603.00729"},{"title":"Qwen/Qwen3.6-35B-A3B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-35B-A3B"},{"title":"Qwen/Qwen3-Coder-30B-A3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"}]

Based on the search results, I found information about the SWE-RM, Qwen team, Qwen3-Coder, and best-of-N approaches:

SWE-RM is described as "execution-free feedback for software engineering agents" and was authored by K. Shum, B. Hui, J. Chen, L. Zhang, X. W., J. Yang, Y. Huang, J. Lin, and J. He in 2025. This work is cited in the context of the Qwen3-Coder-Next technical report.

The Qwen3-Coder-Next Technical Report is authored by the Qwen Team, and rather than relying solely on parameter scaling, Qwen3-Coder-Next focuses on scaling agentic training signals through training with large collections of verifiable coding tasks paired with executable environments, including continued pretraining on code- and agent-centric data, supervised fine-tuning on data containing high-quality agent trajectories, domain-specialized expert training, and expert distillation into a single deployment-ready model.

While the search results reference SWE-RM and discuss the Qwen3-Coder models in detail, the specific mention of a "best-of-N" approach by these authors together is not explicitly detailed in these search results. For more specific information about the best-of-N technique used with SWE-RM and Qwen3-Coder, you may need to consult the full technical papers directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c82546ad-7e4c-49bd-95d9-b1397f9ef73d",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "620f65d7-5e65-4659-9c7b-017d2ef37c7d",
  "sourceToolAssistantUUID": "c82546ad-7e4c-49bd-95d9-b1397f9ef73d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-10T18:29:10.250Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VG6LYiYG9ZEADsEZtbC4Ae`</summary>

```json
{
  "query": "\"SWE-Shepherd\" \"51%\" OR \"57%\" SWE-bench greedy baseline 100 tasks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "620f65d7-5e65-4659-9c7b-017d2ef37c7d",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauMyhMjpuPVeNxD1FkhS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1aca1ed3-fae2-4374-9fa5-aba0ea2bdb6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTncgXriJWDeSVXJjVw6A3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1757,
      "cache_read_input_tokens": 12363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1757,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T18:29:10.541Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FZdpK2f6zgS4BowmaoYTLa`</summary>

```json
{
  "query": "arxiv 2604.10493 SWE-Shepherd Mahir Labib Dihan results table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aca1ed3-fae2-4374-9fa5-aba0ea2bdb6f",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauMyhMjpuPVeNxD1FkhS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba1e7a96-51f7-4ef9-84e2-d98dc06b086d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTncgXriJWDeSVXJjVw6A3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1757,
      "cache_read_input_tokens": 12363,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1757
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 12363,
          "cache_creation_input_tokens": 1757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1757,
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

_source line 16 · 2026-05-10T18:29:15.523Z_

<details><summary>↩ Tool result · `toolu_01FZdpK2f6zgS4BowmaoYTLa`</summary>

```text
Web search results for query: "arxiv 2604.10493 SWE-Shepherd Mahir Labib Dihan results table"

Links: [{"title":"[2604.10493] SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/abs/2604.10493"},{"title":"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/html/2604.10493"},{"title":"Mahir Labib Dihan","url":"https://scholar.google.com/citations?user=zha3IiwAAAAJ&hl=en"},{"title":"Software Engineering","url":"https://arxiv.org/list/cs.SE/recent?skip=95&show=1000"},{"title":"[2604.10481] PatchRecall: Patch-Driven Retrieval for Automated Program Repair","url":"https://arxiv.org/abs/2604.10481"},{"title":"Mahir Labib Dihan - ACL Anthology","url":"https://aclanthology.org/people/mahir-labib-dihan/"},{"title":"[2604.16581] NCO4CVRP: Neural Combinatorial Optimization for the Capacitated Vehicle Routing Problem","url":"https://arxiv.org/abs/2604.16581"},{"title":"Mahir Labib Dihan","url":"https://mahirlabibdihan.github.io/"},{"title":"MapEval: A Map-Based Evaluation of Geo-Spatial Reasoning in Foundation Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250100316L/abstract"},{"title":"[2512.19122] BanglaForge: LLM Collaboration with Self-Refinement for Bangla Code Generation","url":"https://arxiv.org/abs/2512.19122"}]

I found the arXiv paper! The paper proposes SWE-Shepherd, a framework that introduces Process Reward Models (PRMs) to provide dense, step-level supervision for repository-level code agents, using trajectories from SWE-Bench to construct an action-level reward dataset and train a lightweight reward model.

However, the search results I retrieved contain abstract and overview information about the paper but do not include the specific results table from the paper. To view the detailed results table, you would need to access the full PDF at https://arxiv.org/abs/2604.10493 or the HTML version at https://arxiv.org/html/2604.10493. 

Would you like me to search for more specific information about the experimental results or metrics reported in this paper?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba1e7a96-51f7-4ef9-84e2-d98dc06b086d",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "5effc2ce-eb09-422f-95ce-cd8748545480",
  "sourceToolAssistantUUID": "ba1e7a96-51f7-4ef9-84e2-d98dc06b086d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T18:29:22.754Z_

<details><summary>↩ Tool result · `toolu_01VG6LYiYG9ZEADsEZtbC4Ae`</summary>

```text
Web search results for query: ""SWE-Shepherd" "51%" OR "57%" SWE-bench greedy baseline 100 tasks"

Links: [{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-bench Results Viewer","url":"https://www.swebench.com/viewer.html"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"HAL: SWE-bench Verified Mini Leaderboard","url":"https://hal.cs.princeton.edu/swebench_verified_mini"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"}]

The search results provide some relevant information about SWE-Bench and various submissions, but don't specifically mention "SWE-Shepherd" with the exact percentages you're looking for. Let me search more specifically for SWE-Shepherd:

Links: [{"title":"[2604.10493] SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/abs/2604.10493"},{"title":"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/html/2604.10493"},{"title":"MATH-SHEPHERD: VERIFY AND REINFORCE LLMS STEP-BY-STEP WITHOUT HUMAN ANNOTATIONS","url":"https://arxiv.org/pdf/2312.08935"},{"title":"[2312.08935] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations","url":"https://arxiv.org/abs/2312.08935"},{"title":"[2308.04592] Shepherd: A Critic for Language Model Generation","url":"https://arxiv.org/abs/2308.04592"},{"title":"[2405.15793] SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://arxiv.org/abs/2405.15793"},{"title":"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering","url":"https://arxiv.org/pdf/2405.15793"},{"title":"[PDF] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Math-Shepherd:-Verify-and-Reinforce-LLMs-without-Wang-Li/4ba57555bef02f988f2ed3bab2f102733dc55221"},{"title":"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.510/"},{"title":"[PDF] SHEPHERD: Serving DNNs in the Wild | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SHEPHERD:-Serving-DNNs-in-the-Wild-Zhang-Tang/2eace6acf43e28cc19876b9983d1c64c54c14c1d"}]

Good! I found the SWE-Shepherd paper. Now let me search for more specific performance numbers from that paper:

Links: [{"title":"SWE-bench Results Viewer","url":"https://www.swebench.com/viewer.html"},{"title":"Introducing GPT-5.5 | OpenAI","url":"https://openai.com/index/introducing-gpt-5-5/"},{"title":"GPT-5.5 Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gpt-5.5"},{"title":"HAL: SWE-bench Verified Mini Leaderboard","url":"https://hal.cs.princeton.edu/swebench_verified_mini"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"GPT 5.4 Complete Guide 2026: Features, Pricing, Benchmarks & How to Use | NxCode","url":"https://www.nxcode.io/resources/news/gpt-5-4-complete-guide-features-pricing-models-2026"},{"title":"GitHub - SWE-agent/mini-swe-agent: The 100 line AI agent that solves GitHub issues or helps you in your command line. Radically simple, no huge configs, no giant monorepo—but scores >74% on SWE-bench verified!","url":"https://github.com/SWE-agent/mini-swe-agent"},{"title":"Everything You Need to Know About GPT-5.5 - Vellum","url":"https://www.vellum.ai/blog/everything-you-need-to-know-about-gpt-5-5"}]

Let me search for the actual SWE-Shepherd paper PDF or full text to find the specific numbers:

Links: [{"title":"[2604.10493] SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/abs/2604.10493"},{"title":"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/html/2604.10493"}]

Let me search more specifically for the performance results with those exact percentages:

No links found.

Based on my search results, I found information about the SWE-Shepherd paper. SWE-Shepherd is a framework that introduces Process Reward Models (PRMs) to provide dense, step-level supervision for repository-level code agents.

The paper evaluates SWE-Shepherd on 100 tasks sampled from SWE-Bench Verified. SWE-Shepherd is mini-SWE-Agent augmented with the trained Process Reward Model (PRM) for action scoring and selection.

The paper includes results comparing different approaches on this task subset, with SWE-Shepherd showing improvements over baseline methods through its reward-guided search approach. However, the specific percentage values (51% and 57%) you mentioned in your search query are not clearly visible in the search results I retrieved. To find these exact figures, you would need to access the full paper PDF directly, which contains the detailed results table referenced as "Table 1" in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1aca1ed3-fae2-4374-9fa5-aba0ea2bdb6f",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "24cf6a70-a43a-44c5-838e-043fb8037cf0",
  "sourceToolAssistantUUID": "1aca1ed3-fae2-4374-9fa5-aba0ea2bdb6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T18:29:26.508Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013eLfzYNaHVyr7e37nXTCNL`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24cf6a70-a43a-44c5-838e-043fb8037cf0",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauMzuN5fPgqJHEvxXQ55",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9b13b7f-6f7f-4036-b332-138a2985d5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKi3YK8s9ZQCuMDoSCvAnH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 698,
      "cache_creation_input_tokens": 1998,
      "cache_read_input_tokens": 14120,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1998
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 698,
          "output_tokens": 76,
          "cache_read_input_tokens": 14120,
          "cache_creation_input_tokens": 1998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1998,
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

_source line 19 · 2026-05-10T18:29:26.511Z_

<details><summary>↩ Tool result · `toolu_013eLfzYNaHVyr7e37nXTCNL`</summary>

````text
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
  "parentUuid": "e9b13b7f-6f7f-4036-b332-138a2985d5bb",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "49bbfcbb-3d45-4de7-b34c-51007e3f67f5",
  "sourceToolAssistantUUID": "e9b13b7f-6f7f-4036-b332-138a2985d5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T18:29:31.544Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014SBek1NLc8coGBU3DaCGLL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.10493",
  "prompt": "Extract the main experimental results from this paper. What are the specific percentage numbers reported on SWE-bench Verified? What is the greedy baseline performance? What does the PRM-guided approach achieve? How many tasks were used in evaluation? Report all numbers from the results/experiments section."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49bbfcbb-3d45-4de7-b34c-51007e3f67f5",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauN1BiLpYe43mCku5gA9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f04b3ca2-fdca-4a29-96f6-8e3363ebe100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiaT9thta6LG25BPJ85Fc4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 16118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1292,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T18:29:33.812Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PYAcq9f7bVREisR3waNwnq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.21919",
  "prompt": "Extract the main experimental results from this paper. What are the specific percentage numbers reported? What is the improvement on SWE-bench Verified? What models are used (Qwen3-Coder-Flash, Qwen3-Coder-Max)? What is the architecture (MoE, 30B parameters)? Who are the authors and what team are they from? Report all key numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f04b3ca2-fdca-4a29-96f6-8e3363ebe100",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauN1BiLpYe43mCku5gA9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82b10ff4-e02b-45b3-a6de-35719fcb58c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiaT9thta6LG25BPJ85Fc4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 16118,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1292
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 16118,
          "cache_creation_input_tokens": 1292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1292,
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

_source line 22 · 2026-05-10T18:29:34.484Z_

<details><summary>↩ Tool result · `toolu_014SBek1NLc8coGBU3DaCGLL`</summary>

```text
I cannot provide the specific experimental results you're requesting. While the webpage contains the abstract and metadata for the SWE-Shepherd paper, it does not include the actual results section or experimental data.

The abstract mentions that the paper demonstrates "improved interaction efficiency and action quality" on SWE-Bench Verified, but specific percentage numbers, baseline performance metrics, and task counts are not present in this page content.

To access these experimental details, you would need to view the full PDF or HTML version of the paper using the links provided on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f04b3ca2-fdca-4a29-96f6-8e3363ebe100",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "315a645f-f12e-4a1c-82e2-45790d8830b3",
  "sourceToolAssistantUUID": "f04b3ca2-fdca-4a29-96f6-8e3363ebe100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T18:29:38.291Z_

<details><summary>↩ Tool result · `toolu_01PYAcq9f7bVREisR3waNwnq`</summary>

```text
# SWE-RM: Key Experimental Results

## Performance Improvements on SWE-Bench Verified

The paper reports significant accuracy gains using test-time scaling (TTS):

- **Qwen3-Coder-Flash**: Improved from 51.6% to 62.0% accuracy
- **Qwen3-Coder-Max**: Improved from 67.0% to 74.6% accuracy

These improvements represent substantial gains, with the Qwen3-Coder-Max achieving "new state-of-the-art performance among open-source models."

## Model Architecture

SWE-RM employs a "mixture-of-experts architecture with 30B total parameters and 3B activated during inference," enabling efficient performance without requiring full model activation.

## Research Focus

Rather than relying on execution-based feedback like unit tests, the paper develops "execution-free feedback from reward models" that provide "more fine-grained signals." The authors emphasize that successful TTS performance doesn't necessarily translate to reinforcement learning effectiveness, so they analyze classification accuracy and calibration alongside trajectory selection ability.

## Author Information

The paper was submitted December 26, 2025, by a nine-person research team led by KaShun Shum, though institutional affiliations aren't specified in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82b10ff4-e02b-45b3-a6de-35719fcb58c0",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "d3f1e755-161a-4e0a-9042-489478d8e73c",
  "sourceToolAssistantUUID": "82b10ff4-e02b-45b3-a6de-35719fcb58c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T18:29:43.641Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BDatpB9DsGMFT5JyM9NGot`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.10493",
  "prompt": "Extract the main experimental results from this paper. What are the specific percentage numbers reported on SWE-bench Verified? What is the greedy baseline performance? What does the PRM-guided approach achieve? How many tasks were used in evaluation? What is the resolve rate? Report ALL numbers from the results tables and experiments section. Also note: does the paper use \"action-utility\" PRMs specifically? Does it report 51% vs 57%?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f1e755-161a-4e0a-9042-489478d8e73c",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauN23jPw1ZjaWQvXxj4Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "433a7f83-e6f9-4bfb-8abe-fe62c8f06243",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbfHV8ryMNbtQwMR5n9gPY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 17410,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 878
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 17410,
          "cache_creation_input_tokens": 878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 878,
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

_source line 25 · 2026-05-10T18:29:48.252Z_

<details><summary>↩ Tool result · `toolu_01BDatpB9DsGMFT5JyM9NGot`</summary>

```text
# SWE-Shepherd Experimental Results

## Evaluation Setup
The paper evaluated on **100 tasks** sampled from SWE-Bench Verified, with a maximum of 30 interaction steps per task.

## Performance Metrics (Table 1)

| Method | Resolution Rate | Avg. Cost | Avg. Steps |
|--------|-----------------|-----------|------------|
| SWE-Search | 31% | 0.274 | – |
| mini-SWE-Agent (baseline) | 57% | 0.029 | 15.2 |
| SWE-Shepherd (PRM-guided) | 51% | 0.053 | 12.2 |

## Key Findings

The greedy baseline (mini-SWE-Agent) achieved **57% resolution**. The PRM-guided approach achieved **51% resolution** while reducing interaction steps from 15.2 to 12.2, demonstrating improved efficiency but a modest performance trade-off.

## Reward Analysis (Table 2)

Average reward scores showed minimal differentiation:
- Resolved tasks: 0.4894
- Unresolved tasks: 0.4818

The authors noted this "small difference in rewards indicates that the current reward function only weakly correlates with task success."

## PRM Type

The paper does not specifically label the approach as "action-utility" PRMs but rather describes it as assigning "scalar rewards to intermediate actions according to their estimated contribution toward resolving the issue."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "433a7f83-e6f9-4bfb-8abe-fe62c8f06243",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a59c710e946146e09",
  "type": "user",
  "uuid": "059329b7-ff9c-4a54-a460-9ab4b60b8751",
  "sourceToolAssistantUUID": "433a7f83-e6f9-4bfb-8abe-fe62c8f06243",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T18:30:08.438Z_

Now I have all the information needed to provide a comprehensive verification report.

## Findings

### Paper 1: SWE-RM (arXiv:2512.21919, Dec 2025)

**Status: CONFIRMED -- the paper exists and the claimed numbers match.**

- The paper is titled "SWE-RM: Execution-free Feedback For Software Engineering Agents" and was submitted December 26, 2025.
- It is indeed a 30B MoE reward model with 3B parameters activated during inference.
- The reported results exactly match the claims: Qwen3-Coder-Flash improves from **51.6% to 62.0%**, and Qwen3-Coder-Max improves from **67.0% to 74.6%** on SWE-bench Verified via test-time scaling (best-of-N).
- Authors include KaShun Shum, Binyuan Hui, Jiawei Chen, Lei Zhang, Jiaxi Yang, Yuzhen Huang, Junyang Lin, and Junxian He. Binyuan Hui and Junyang Lin are known Qwen team members, so the attribution to the Qwen team is accurate.

**No discrepancies found.**

---

### Paper 2: SWE-Shepherd (arXiv:2604.10493, April 2026)

**Status: CONFIRMED -- the paper exists and the claimed numbers match.**

- The paper is titled "SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents" and was submitted April 12, 2026, by Mahir Labib Dihan and Md Ashrafur Rahman Khan.
- The paper evaluates on **100 tasks** sampled from SWE-bench Verified -- this matches the claim.
- The results confirm: the PRM-guided SWE-Shepherd achieves **51% resolution rate**, while the greedy baseline (mini-SWE-Agent) achieves **57%** -- exactly matching the claimed numbers.
- The paper does describe step-level PRMs that assign scalar rewards to intermediate actions based on their contribution toward resolving the issue.

**Minor discrepancy in terminology:** The proposal calls these "action-utility PRMs," but the paper itself does not use that exact phrase. It describes assigning "scalar rewards to intermediate actions according to their estimated contribution toward resolving the issue," which is semantically equivalent but not the paper's own terminology.

**Notable context:** The paper's PRM actually *underperforms* the greedy baseline (51% vs. 57%), though it does so with fewer interaction steps (12.2 vs. 15.2). The paper acknowledges this limitation, noting the reward function "only weakly correlates with task success."

---

### Summary

Both papers are real, published on arXiv at the stated IDs, and the numerical results quoted in the proposal are accurate. The only minor issue is the "action-utility PRM" terminology for SWE-Shepherd, which is a reasonable paraphrase but not the paper's own wording.

Sources:
- [SWE-RM (arXiv:2512.21919)](https://arxiv.org/abs/2512.21919)
- [SWE-RM on AlphaXiv](https://www.alphaxiv.org/overview/2512.21919v1)
- [SWE-RM on HuggingFace Papers](https://huggingface.co/papers/2512.21919)
- [SWE-Shepherd (arXiv:2604.10493)](https://arxiv.org/abs/2604.10493)
- [SWE-Shepherd HTML version](https://arxiv.org/html/2604.10493)
- [Mahir Labib Dihan - Google Scholar](https://scholar.google.com/citations?user=zha3IiwAAAAJ&hl=en)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "059329b7-ff9c-4a54-a460-9ab4b60b8751",
  "isSidechain": true,
  "agentId": "a59c710e946146e09",
  "requestId": "req_011CauN2nRvJWbnjsZdNq4ib",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a620bd9b-0c8e-46af-a797-d48ccbd34be4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EbX6mGE9QgbCuGQTdhEgy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 534,
      "cache_read_input_tokens": 18288,
      "output_tokens": 926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 534
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 926,
          "cache_read_input_tokens": 18288,
          "cache_creation_input_tokens": 534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 534,
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
