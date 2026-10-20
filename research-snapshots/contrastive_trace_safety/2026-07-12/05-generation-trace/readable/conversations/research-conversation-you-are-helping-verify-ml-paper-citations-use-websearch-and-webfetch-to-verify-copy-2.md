# Research conversation: You are helping verify ML paper citations. Use WebSearch and WebFetch to verify these three papers exist and are correct

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4eb21958785d9238.jsonl`
- **Structured JSON:** [`bc8f28ea6191b9ef8615.json`](../../sessions/bc/bc8f28ea6191b9ef8615.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-10T18:43:29.172Z_

You are helping verify ML paper citations. Use WebSearch and WebFetch to verify these three papers exist and are correctly characterized:

1. **SWE-PRM / "When Agents Go Astray"** (arXiv:2509.02360, Sept 2025, IBM Research) — claimed: first PRM for SWE agents, prompt-based behavioral pattern detection (looping, drift, redundancy), 40%→50.6% on SWE-bench Verified. NOT a trained model.

2. **SWE-RM** (arXiv:2512.21919, Dec 2025, Qwen team) — claimed: 30B MoE reward model (3B active), trained on ~100K trajectories, binary whole-trajectory scoring, 51.6→62.0% (Flash) and 67.0→74.6% (Max) on SWE-bench Verified via best-of-N.

3. **SWE-Shepherd** (arXiv:2604.10493, April 2026) — claimed: step-level action-utility PRMs for SWE agents, achieves only 51% vs. 57% greedy baseline on 100 SWE-bench Verified tasks.

For each paper:
- Search for its arXiv ID and title
- Verify the key claims (scores, methods, dates)
- Report any discrepancies

Also search for: "SWE-bench Verified SOTA 2026" and "reward model SWE-bench 2026" to find any additional competitors not mentioned.

Report concisely: for each paper, state whether it exists and if the characterization is accurate. List any competitors found that are not in the idea's landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "840aefb1-f7dc-4a77-a966-d228d79eeab7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:43:29.176Z_

```json
{
  "parentUuid": "840aefb1-f7dc-4a77-a966-d228d79eeab7",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c9f60050-2ef1-4476-84a2-be2358653bf3",
  "timestamp": "2026-05-10T18:43:29.176Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:43:31.256Z_



I'll search for all three papers and the competitive landscape in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9f60050-2ef1-4476-84a2-be2358653bf3",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP5J7Y9LD9TTexxKwTb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1745a16a-9231-4f07-bb3e-6fbdeae8a903",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUG11F2MN7GZMTvmahheU1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8224,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8224,
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

_source line 4 · 2026-05-10T18:43:31.428Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TSN5cxu66yasH7fVYki73A`</summary>

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
  "parentUuid": "1745a16a-9231-4f07-bb3e-6fbdeae8a903",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP5J7Y9LD9TTexxKwTb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61375b11-6721-4314-8a8d-b6a97d648fc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUG11F2MN7GZMTvmahheU1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8224,
      "cache_read_input_tokens": 0,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8224,
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

_source line 5 · 2026-05-10T18:43:31.431Z_

<details><summary>↩ Tool result · `toolu_01TSN5cxu66yasH7fVYki73A`</summary>

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
  "parentUuid": "61375b11-6721-4314-8a8d-b6a97d648fc1",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "02aedece-9a5e-4f3b-b7c4-576ba0ebdb66",
  "sourceToolAssistantUUID": "61375b11-6721-4314-8a8d-b6a97d648fc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:43:33.937Z_



Now let me search for all three papers and the competitive landscape in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02aedece-9a5e-4f3b-b7c4-576ba0ebdb66",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP5U73yBEzpy8qjEr29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a8665be-159d-437a-a5ee-bb4ffcba7051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkzVeoK83wcmCcg96rAjV3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 7 · 2026-05-10T18:43:35.529Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CQL4MfeWkK6nt7m1AahSfj`</summary>

```json
{
  "query": "arXiv 2509.02360 \"When Agents Go Astray\" SWE-PRM IBM Research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a8665be-159d-437a-a5ee-bb4ffcba7051",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP5U73yBEzpy8qjEr29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcefb052-faa4-4edf-b4b9-8bfb109af132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkzVeoK83wcmCcg96rAjV3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 8 · 2026-05-10T18:43:36.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dmnw6ELNDg4GLGV8RJK82a`</summary>

```json
{
  "query": "arXiv 2512.21919 SWE-RM Qwen reward model SWE-bench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcefb052-faa4-4edf-b4b9-8bfb109af132",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP5U73yBEzpy8qjEr29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e944118f-459d-4905-a9f2-7ca746f1ce79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkzVeoK83wcmCcg96rAjV3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 9 · 2026-05-10T18:43:37.411Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q97YzuYcpznPgUq3FcyFR8`</summary>

```json
{
  "query": "arXiv 2604.10493 SWE-Shepherd step-level PRM SWE agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e944118f-459d-4905-a9f2-7ca746f1ce79",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP5U73yBEzpy8qjEr29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70bbb20e-5ee5-495d-88f9-7828bb784f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkzVeoK83wcmCcg96rAjV3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 10 · 2026-05-10T18:43:37.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VS1j1Av4WiXgNuWVuQPYY8`</summary>

```json
{
  "query": "SWE-bench Verified SOTA 2026 state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70bbb20e-5ee5-495d-88f9-7828bb784f1c",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP5U73yBEzpy8qjEr29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c195888-2d40-44a1-826d-090621e914d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkzVeoK83wcmCcg96rAjV3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 11 · 2026-05-10T18:43:38.343Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BL31pqfXzM5NaY3CjRhmPC`</summary>

```json
{
  "query": "reward model SWE-bench 2026 process reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c195888-2d40-44a1-826d-090621e914d0",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP5U73yBEzpy8qjEr29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4da9d76d-1699-498a-961b-bb9053e9f35e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkzVeoK83wcmCcg96rAjV3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8224,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 8224,
          "cache_creation_input_tokens": 1904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1904,
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

_source line 12 · 2026-05-10T18:43:43.296Z_

<details><summary>↩ Tool result · `toolu_01CQL4MfeWkK6nt7m1AahSfj`</summary>

```text
Web search results for query: "arXiv 2509.02360 "When Agents Go Astray" SWE-PRM IBM Research"

Links: [{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/html/2509.02360"},{"title":"[2509.02360] When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/abs/2509.02360"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs Shubham Gandhi∗","url":"https://arxiv.org/pdf/2509.02360"},{"title":"Act Like You’re Paying for This: Course-Correcting Code Agents with PRMs","url":"https://arxiv.org/html/2509.02360v1"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/when-agents-go-astray-course-correcting-swe-agents-with-prms"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs | OpenReview","url":"https://openreview.net/forum?id=wyrcoDNaGO"},{"title":"[2510.02360] Spiral of Silence in Large Language Model Agents","url":"https://arxiv.org/abs/2510.02360"},{"title":"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?","url":"https://arxiv.org/html/2509.16941"},{"title":"Spiral of Silence in Large Language Model Agents","url":"https://arxiv.org/pdf/2510.02360"},{"title":"[2509.16941] SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?","url":"https://arxiv.org/abs/2509.16941"}]

Based on the search results, I found information about arXiv paper 2509.02360 "When Agents go Astray: Course-Correcting SWE Agents with PRMs."

## Overview

The paper introduces SWE-PRM, an inference-time Process Reward Model (PRM) that intervenes during execution to detect and course-correct trajectory-level errors, with a PRM design that leverages a taxonomy of common inefficiencies and delivers lightweight, interpretable feedback without modifying the underlying policy.

## Problem Being Addressed

Large Language Model (LLM) agents are increasingly deployed for complex, multi-step software engineering (SWE) tasks, however their trajectories often contain costly inefficiencies, such as redundant exploration, looping, and failure to terminate once a solution is reached, and prior work has largely treated these errors in a post-hoc manner, diagnosing failures only after execution.

## Key Results

On SWE-bench Verified, closed-source PRMs improve resolution from 40.0% to 50.6% (with the largest gains on medium and hard tasks), and among feedback strategies, taxonomy-guided PRMs outperform unguided or explicit action-prescriptive variants, increasing success rate while reducing trajectory length. These benefits come at an acceptable added inference cost of as low as $0.2, making PRMs a practical and scalable mechanism for improving SWE agents' reliability and efficiency.

## Authors and Affiliation

The paper is authored by Shubham Gandhi et al. and was submitted to NeurIPS 2025 with IBM Research as an affiliation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcefb052-faa4-4edf-b4b9-8bfb109af132",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "ddda5b0e-89d0-417d-b802-14573cab0bd8",
  "sourceToolAssistantUUID": "fcefb052-faa4-4edf-b4b9-8bfb109af132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:43:43.360Z_

<details><summary>↩ Tool result · `toolu_01Dmnw6ELNDg4GLGV8RJK82a`</summary>

```text
Web search results for query: "arXiv 2512.21919 SWE-RM Qwen reward model SWE-bench"

Links: [{"title":"[2512.21919] SWE-RM: Execution-free Feedback For Software Engineering Agents","url":"https://arxiv.org/abs/2512.21919"},{"title":"2025-12-29 SWE-RM: EXECUTION-FREE FEEDBACK FOR SOFT- WARE ENGINEERING AGENTS","url":"https://www.arxiv.org/pdf/2512.21919"},{"title":"SWE-RM: Execution-Free Feedback for Software Engineering Agents","url":"https://arxiv.org/html/2512.21919v1"},{"title":"SWE-RM: Execution-free Feedback For Software Engineering Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.21919v1"},{"title":"Paper page - SWE-RM: Execution-free Feedback For Software Engineering Agents","url":"https://huggingface.co/papers/2512.21919"},{"title":"SWE-RM: Execution-free Feedback for Software Engineering Agents | OpenReview","url":"https://openreview.net/forum?id=H9wMe1G76j"},{"title":"Natural Language Processing Papers on X: \"SWE-RM: Execution-free Feedback For Software Engineering Agents KaShun Shum, Binyuan Hui, Jiawei Chen, Lei Zhang, X. W., Jiaxi Yang, Yuzhen Huang, Junyang Lin, Junxian He (arXiv:2512.21919) https://t.co/6Ek3le9WwT\" / X","url":"https://x.com/HEI/status/2005573373896597610"},{"title":"GitHub - allenai/reward-bench: RewardBench: the first evaluation tool for reward models. · GitHub","url":"https://github.com/allenai/reward-bench"},{"title":"RewardBench 2: Advancing Reward Model Evaluation","url":"https://arxiv.org/html/2506.01937v1"},{"title":"RewardBench: Evaluating Reward Models for Language Modeling","url":"https://arxiv.org/html/2403.13787v1"}]

Based on the search results, here's information about arXiv paper 2512.21919:

## SWE-RM: Execution-Free Feedback For Software Engineering Agents

This paper presents SWE-RM, execution-free feedback for software engineering agents. 

### Key Innovation

SWE-RM is an accurate and robust reward model adopting a mixture-of-experts architecture with 30B total parameters and 3B activated during inference. SWE-RM supports 256k context length, enabling scoring of complex, long trajectories common in challenging software engineering tasks.

### Performance Results

SWE-RM increases the accuracy of Qwen3-Coder-Flash from 51.6% to 62.0%, and Qwen3-Coder-Max from 67.0% to 74.6% on SWE-Bench Verified using test-time scaling (TTS), achieving new state-of-the-art performance among open-source models. On RL training, SWE-RM lifts the resolve rate of execution-based counterparts by 3 absolute points on SWE-Bench Verified.

### Research Approach

The researchers identify classification accuracy and calibration as crucial for RL training, conduct comprehensive controlled experiments to investigate training robust reward models, and analyze the impact of various factors such as training data scale, policy mixtures, and data source composition.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e944118f-459d-4905-a9f2-7ca746f1ce79",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "7c8827c6-1229-42cc-aac8-9a571a59b613",
  "sourceToolAssistantUUID": "e944118f-459d-4905-a9f2-7ca746f1ce79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:43:44.611Z_

<details><summary>↩ Tool result · `toolu_01VS1j1Av4WiXgNuWVuQPYY8`</summary>

```text
Web search results for query: "SWE-bench Verified SOTA 2026 state of the art"

Links: [{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"Codesota — the open registry of state-of-the-art machine learning","url":"https://www.codesota.com/browse/agentic/swe-bench"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/sweVerified"},{"title":"[State of Code Evals] After SWE-bench, Code Clash & SOTA Coding Benchmarks recap — John Yang","url":"https://www.latent.space/p/state-of-code-evals-after-swe-bench"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"CodeSOTA: The Open, Callable Registry of State of the Art","url":"https://www.codesota.com/"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason","url":"https://arxiv.org/html/2506.12286v3"}]

Based on the search results, here's the current state-of-the-art performance on SWE-bench Verified as of May 2026:

## Current SOTA Leaders (May 2026)

As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Verified leaderboard with 93.9%, followed by Claude Opus 4.7 (Adaptive) (87.6%) and GPT-5.3 Codex (85%).

However, there are some variations depending on the source and evaluation methodology. Claude Mythos Preview from Anthropic leads with a score of 0.939 (93.9%), followed by Claude Opus 4.7 at 87.6% and Claude Opus 4.5 at 80.9%.

## What SWE-bench Verified Measures

SWE-bench Verified is a human-filtered subset of 500 instances from SWE-bench, created in collaboration with OpenAI. Human annotators reviewed each instance to ensure the problem descriptions are clear, the test patches are correct, and the tasks are solvable given the available information.

## Important Caveat: Recent Concerns About Memorization

It's worth noting that SWE-Bench Verified performance substantially reflects memorization of training sequences, with the inability to reproduce functions from less-curated instances within the same repositories suggesting that apparent programming ability might result from an artifact of exposure to the specific, high-quality solutions selected for benchmark inclusion.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c195888-2d40-44a1-826d-090621e914d0",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "06ad5d2f-335a-4b9d-8926-f09a0f2fac82",
  "sourceToolAssistantUUID": "1c195888-2d40-44a1-826d-090621e914d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T18:43:45.253Z_

<details><summary>↩ Tool result · `toolu_01Q97YzuYcpznPgUq3FcyFR8`</summary>

```text
Web search results for query: "arXiv 2604.10493 SWE-Shepherd step-level PRM SWE agents"

Links: [{"title":"[2604.10493] SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/abs/2604.10493"},{"title":"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/html/2604.10493"},{"title":"SWE-TRACE: Optimizing Long-Horizon SWE Agents through Rubric Process Reward Models and Heuristic Test-Time Scaling","url":"https://arxiv.org/html/2604.14820"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/html/2509.02360"},{"title":"Act Like You’re Paying for This: Course-Correcting Code Agents with PRMs","url":"https://arxiv.org/html/2509.02360v1"},{"title":"[2604.14820] SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling","url":"https://arxiv.org/abs/2604.14820"},{"title":"MATH-SHEPHERD: VERIFY AND REINFORCE LLMS STEP-BY-STEP WITHOUT HUMAN ANNOTATIONS","url":"https://arxiv.org/pdf/2312.08935"},{"title":"Math-Shepherd: LLM Step-by-Step Verification","url":"https://www.emergentmind.com/papers/2312.08935"},{"title":"[PDF] Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Math-Shepherd:-Verify-and-Reinforce-LLMs-without-Wang-Li/4ba57555bef02f988f2ed3bab2f102733dc55221"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs | OpenReview","url":"https://openreview.net/forum?id=wyrcoDNaGO"}]

I found the paper you're looking for! Here's what arXiv 2604.10493 is about:

## SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents

SWE-Shepherd is a framework that introduces Process Reward Models (PRMs) to provide dense, step-level supervision for repository-level code agents.

### The Problem It Addresses

Automating real-world software engineering tasks remains challenging for LLM-based agents due to the need for long-horizon reasoning over large, evolving codebases and making consistent decisions across interdependent actions. Existing approaches typically rely on static prompting strategies or handcrafted heuristics to select actions such as code editing, file navigation, and test execution, but they lack fine-grained feedback on intermediate decisions. This leads to inefficient exploration, error propagation, and brittle solution trajectories.

### How It Works

Instead of relying solely on sparse signals of final task success, SWE-Shepherd converts agent trajectories into dense, step-level supervision by assigning scalar rewards to intermediate actions according to their estimated contribution toward resolving the issue.

Using trajectories from SWE-Bench, they construct an action-level reward dataset and train a lightweight reward model on a base LLM to estimate the usefulness of intermediate actions. During inference, the PRM evaluates candidate actions and guides the agent toward higher-reward decisions without requiring full reinforcement learning.

### Results

Experiments on SWE-Bench Verified demonstrate improved interaction efficiency and action quality, while also highlighting challenges in aligning intermediate rewards with final task success.

The paper was submitted on April 12, 2026 by Mahir Labib Dihan and Md Ashrafur Rahman Khan from Bangladesh University of Engineering and Technology (BUET).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70bbb20e-5ee5-495d-88f9-7828bb784f1c",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "2293eaae-efc7-433c-9e79-a1493b2a8581",
  "sourceToolAssistantUUID": "70bbb20e-5ee5-495d-88f9-7828bb784f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:43:46.586Z_

<details><summary>↩ Tool result · `toolu_01BL31pqfXzM5NaY3CjRhmPC`</summary>

```text
Web search results for query: "reward model SWE-bench 2026 process reward"

Links: [{"title":"GitHub - allenai/reward-bench: RewardBench: the first evaluation tool for reward models. · GitHub","url":"https://github.com/allenai/reward-bench"},{"title":"RewardBench 2: Advancing Reward Model Evaluation | OpenReview","url":"https://openreview.net/forum?id=fb0G86Dewb"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and","url":"https://arxiv.org/pdf/2506.17208"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"[2403.13787] RewardBench: Evaluating Reward Models for Language Modeling","url":"https://arxiv.org/abs/2403.13787"},{"title":"RewardBench: Evaluating Reward Models for Language Modeling | OpenReview","url":"https://openreview.net/forum?id=XiConLcsqq"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 Leaderboard","url":"https://www.morphllm.com/swe-benchmark"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"}]

Based on the search results, I found information about reward models and SWE-bench, though the specific connection between "process reward" and these benchmarks in 2026 isn't directly detailed in these results. Here's what I found:

## Reward Models and Benchmarking

Reward models are used throughout the post-training of language models to capture nuanced signals from preference data and provide a training target for optimization across instruction following, reasoning, safety, and more domains.

### RewardBench

RewardBench 2 is a new multi-skill reward modeling benchmark designed to bring new, challenging data for accuracy-based reward model evaluation, and it sources new human prompts instead of existing prompts from downstream evaluations. The paper describes the benchmark construction process and reports how existing models perform on it, while quantifying how performance on the benchmark correlates with downstream use of the models in both inference-time scaling algorithms, like best-of-N sampling, and RLHF training algorithms like proximal policy optimization.

### SWE-bench 2026

Regarding SWE-bench and 2026, during training with the SWE-RL approach, the policy LLM is tasked with solving a given issue through reasoning and producing the code changes, then converted into a consistent patch format for reward calculation. This suggests that reward models play a role in evaluating solutions on SWE-bench through patch scoring.

If you're looking for more specific information about how "process reward" models are being used with SWE-bench in 2026, I'd recommend checking the latest research papers and leaderboards directly, as this appears to be an emerging area of research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4da9d76d-1699-498a-961b-bb9053e9f35e",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "3946cb66-0dc6-44a3-ba6e-574fc71e746a",
  "sourceToolAssistantUUID": "4da9d76d-1699-498a-961b-bb9053e9f35e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T18:43:50.209Z_

Good, I have initial results for all three papers. Let me now fetch the actual arXiv pages to verify specific claims in more detail, and also search for additional competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3946cb66-0dc6-44a3-ba6e-574fc71e746a",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP6aaGNZLKjQLX8v1qz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f859ebce-2f8a-40de-a0a3-fdf607596604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141XteBSHSXZyzu7j7PTUZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4852,
      "cache_read_input_tokens": 10128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4852,
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

_source line 18 · 2026-05-10T18:43:54.230Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D5E9tb7JdRAVhxhcV8Gyoa`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.02360",
  "prompt": "Extract: 1) The exact title, 2) Authors and affiliations, 3) Submission date, 4) Whether it is a trained model or prompt-based, 5) Key results/scores on SWE-bench Verified (specifically the 40% to 50.6% claim), 6) What behavioral patterns it detects (looping, drift, redundancy), 7) Whether it claims to be the \"first PRM for SWE agents\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f859ebce-2f8a-40de-a0a3-fdf607596604",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP6aaGNZLKjQLX8v1qz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1b6f987-1769-4e1e-a4da-952a5f4a9e26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141XteBSHSXZyzu7j7PTUZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4852,
      "cache_read_input_tokens": 10128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4852,
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

_source line 19 · 2026-05-10T18:43:57.890Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ESjryeG86XmPvXiUnkPWke`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.21919",
  "prompt": "Extract: 1) Exact title, 2) Authors and affiliations (is it Qwen team?), 3) Submission date, 4) Model architecture (30B MoE, 3B active?), 5) Training data size (~100K trajectories?), 6) Scoring method (binary whole-trajectory?), 7) Exact scores: 51.6 to 62.0% for Flash, 67.0 to 74.6% for Max on SWE-bench Verified, 8) Whether it uses best-of-N"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1b6f987-1769-4e1e-a4da-952a5f4a9e26",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP6aaGNZLKjQLX8v1qz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e018d71d-1b05-48c7-ad5e-b49c14d8136f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141XteBSHSXZyzu7j7PTUZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4852,
      "cache_read_input_tokens": 10128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4852,
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

_source line 20 · 2026-05-10T18:43:59.461Z_

<details><summary>↩ Tool result · `toolu_01D5E9tb7JdRAVhxhcV8Gyoa`</summary>

```text
# Paper Analysis: SWE-PRM

**1) Exact Title:**
"When Agents go Astray: Course-Correcting SWE Agents with PRMs"

**2) Authors and Affiliations:**
The page lists five authors—Shubham Gandhi, Jason Tsay, Jatin Ganhotra, Kiran Kate, and Yara Rizk—but does not provide their institutional affiliations.

**3) Submission Date:**
Initial submission: September 2, 2025; revised version: October 21, 2025

**4) Trained Model vs. Prompt-Based:**
The abstract describes a "Process Reward Model (PRM)" that operates at inference time without modifying the underlying policy, suggesting a trained model component, though the page doesn't explicitly state the training methodology.

**5) Key Results on SWE-bench Verified:**
The abstract states: "closed-source PRMs improve resolution from 40.0% to 50.6% (+10.6 p.p.)" This represents a 10.6 percentage point improvement, with noted gains on medium and hard difficulty tasks.

**6) Behavioral Patterns Detected:**
The paper identifies three inefficiency categories: "redundant exploration, looping, and failure to terminate once a solution is reached."

**7) "First PRM for SWE Agents" Claim:**
The page contains no such claim. It presents this as a novel contribution but doesn't assert being the first to apply PRMs to software engineering agents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1b6f987-1769-4e1e-a4da-952a5f4a9e26",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "ed024b00-4897-4e86-bad2-f2ee370b8838",
  "sourceToolAssistantUUID": "d1b6f987-1769-4e1e-a4da-952a5f4a9e26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T18:44:00.583Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FsxTDSydkHoz9VUoySPCQP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.10493",
  "prompt": "Extract: 1) Exact title, 2) Authors and affiliations, 3) Submission date, 4) Whether it uses step-level action-utility PRMs, 5) Exact scores on SWE-bench Verified (specifically the claim of 51% vs 57% greedy baseline on 100 tasks), 6) Number of SWE-bench Verified tasks evaluated, 7) Any key limitations or caveats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed024b00-4897-4e86-bad2-f2ee370b8838",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP6aaGNZLKjQLX8v1qz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c4bd341-b655-44e9-b319-8422fe23e8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141XteBSHSXZyzu7j7PTUZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4852,
      "cache_read_input_tokens": 10128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4852,
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

_source line 22 · 2026-05-10T18:44:01.012Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ByuLfs9UPWjJq75ZKq87Ho`</summary>

```json
{
  "query": "SWE-TRACE \"process reward model\" SWE-bench 2604.14820"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c4bd341-b655-44e9-b319-8422fe23e8a2",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP6aaGNZLKjQLX8v1qz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1bf3c1f-10a5-4e81-8d41-dc5fb6a3b40e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141XteBSHSXZyzu7j7PTUZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4852,
      "cache_read_input_tokens": 10128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4852,
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

_source line 23 · 2026-05-10T18:44:01.916Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017fodLYeb9NRbbz4PWGpmBo`</summary>

```json
{
  "query": "\"SWE-bench\" reward model test-time scaling 2025 2026 best-of-N"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1bf3c1f-10a5-4e81-8d41-dc5fb6a3b40e",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP6aaGNZLKjQLX8v1qz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "682fc962-3d22-4327-a58d-f2cdcaed77fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141XteBSHSXZyzu7j7PTUZq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4852,
      "cache_read_input_tokens": 10128,
      "output_tokens": 697,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 697,
          "cache_read_input_tokens": 10128,
          "cache_creation_input_tokens": 4852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4852,
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

_source line 24 · 2026-05-10T18:44:02.413Z_

<details><summary>↩ Tool result · `toolu_01ESjryeG86XmPvXiUnkPWke`</summary>

```text
# SWE-RM Paper Analysis

**1) Exact Title:**
"SWE-RM: Execution-free Feedback For Software Engineering Agents"

**2) Authors and Affiliations:**
The paper lists 9 authors: KaShun Shum, Binyuan Hui, Jiawei Chen, Lei Zhang, X. W., Jiaxi Yang, Yuzhen Huang, Junyang Lin, and Junxian He. The webpage does not specify institutional affiliations, and there is no indication these are from the Qwen team based on the available content.

**3) Submission Date:**
"Submitted on 26 Dec 2025" (arXiv:2512.21919v1)

**4) Model Architecture:**
"mixture-of-experts architecture with 30B total parameters and 3B activated during inference"

**5) Training Data Size:**
Not specified in the provided content.

**6) Scoring Method:**
Not explicitly detailed in the abstract provided. The content mentions "execution-free feedback from reward models" but does not specify whether scoring is binary or trajectory-level.

**7) Exact Performance Scores:**
- Qwen3-Coder-Flash: increased "from 51.6% to 62.0%"
- Qwen3-Coder-Max: increased "from 67.0% to 74.6%"
- Both measured on "SWE-Bench Verified using TTS"

**8) Best-of-N Usage:**
Not mentioned in the provided webpage content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e018d71d-1b05-48c7-ad5e-b49c14d8136f",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "f12368ae-675c-4d0d-a5ac-0162fd6b3c12",
  "sourceToolAssistantUUID": "e018d71d-1b05-48c7-ad5e-b49c14d8136f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T18:44:06.422Z_

<details><summary>↩ Tool result · `toolu_01ByuLfs9UPWjJq75ZKq87Ho`</summary>

```text
Web search results for query: "SWE-TRACE "process reward model" SWE-bench 2604.14820"

Links: [{"title":"[2604.14820] SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling","url":"https://arxiv.org/abs/2604.14820"},{"title":"SWE-TRACE: Optimizing Long-Horizon SWE Agents through Rubric Process Reward Models and Heuristic Test-Time Scaling","url":"https://arxiv.org/html/2604.14820"}]

Based on the search results, here's what I found about SWE-TRACE:

SWE-TRACE (Trajectory Reduction and Agentic Criteria Evaluation) is a unified framework optimizing the SWE agent lifecycle across data curation, reinforcement learning (RL), and test-time inference.

Regarding the process reward model specifically: SWE-TRACE uses a Memory-Augmented Agentic RL pipeline featuring a Rubric-Based Process Reward Model (PRM), where an auxiliary Rubric-Agent provides dense, fine-grained heuristic feedback on intermediate steps, guiding the model through long-horizon tasks.

The framework has three main components:

1. **Data Curation**: An LLM multi-task cascading method utilizing step-wise oracle verification to distill a 60K-instance Supervised Fine-Tuning (SFT) corpus strictly biased toward token-efficient, shortest-path trajectories.

2. **Test-Time Inference**: The framework bridges training and inference by repurposing the PRM for heuristic-guided Test-Time Scaling (TTS), dynamically evaluating and pruning action candidates at each step to achieve superior search efficiency.

3. **Results**: Extensive experiments on standard SWE benchmarks demonstrate that SWE-TRACE significantly advances the state-of-the-art, maximizing resolution rates while drastically reducing both token consumption and inference latency.

The paper was published in April 2026 (arXiv:2604.14820) by researchers including Hao Han, Jin Xie, and others from vivo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1bf3c1f-10a5-4e81-8d41-dc5fb6a3b40e",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "cdec04b5-1db6-410f-bb0f-58d29c2d1098",
  "sourceToolAssistantUUID": "a1bf3c1f-10a5-4e81-8d41-dc5fb6a3b40e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T18:44:06.726Z_

<details><summary>↩ Tool result · `toolu_01FsxTDSydkHoz9VUoySPCQP`</summary>

```text
# SWE-Shepherd Paper Extract

**1) Exact Title:**
"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents"

**2) Authors and Affiliations:**
Mahir Labib Dihan and Md Ashrafur Rahman Khan. No affiliations are listed on this arXiv page.

**3) Submission Date:**
April 12, 2026

**4) Step-level Action-Utility PRMs:**
Yes. The abstract states the framework "introduces Process Reward Models (PRMs) to provide dense, step-level supervision" and "train a lightweight reward model...to estimate the usefulness of intermediate actions."

**5) SWE-Bench Verified Scores (51% vs 57%):**
No such specific scores appear in the provided content. The abstract only mentions "improved interaction efficiency and action quality" without citing numerical benchmarks.

**6) Number of SWE-Bench Verified Tasks:**
Not specified in the provided excerpt.

**7) Key Limitations/Caveats:**
The abstract identifies one critical limitation: "challenges in aligning intermediate rewards with final task success," suggesting the reward model's step-level judgments don't consistently correlate with solving the full task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c4bd341-b655-44e9-b319-8422fe23e8a2",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "e21eaa65-5380-474f-a8d6-926e5e66f820",
  "sourceToolAssistantUUID": "2c4bd341-b655-44e9-b319-8422fe23e8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T18:44:09.805Z_

<details><summary>↩ Tool result · `toolu_017fodLYeb9NRbbz4PWGpmBo`</summary>

```text
Web search results for query: ""SWE-bench" reward model test-time scaling 2025 2026 best-of-N"

Links: [{"title":"SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025","url":"https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"Test-Time Compute Orchestration for SWE-bench with AI21 Maestro","url":"https://www.ai21.com/blog/test-time-compute-swe-bench/"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"What is SWE-bench? | AI21","url":"https://www.ai21.com/glossary/tech/what-is-swe-bench/"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"Published as a conference paper at ICLR 2025 SWE-SEARCH: ENHANCING SOFTWARE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a1e6783e4d739196cad3336f12d402bf-Paper-Conference.pdf"},{"title":"SWE-bench Verified Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-verified-benchmark"}]

Based on the search results, here's what I found about SWE-bench, reward models, test-time scaling, and best-of-N approaches in 2025-2026:

## Key Findings on Test-Time Scaling and Best-of-N

SWE-bench is used to evaluate the impact of orchestration strategies such as test-time compute scaling or best-of-N sampling.

Strategies like "best of N" (also using more compute to improve accuracy) have joined the agentic game and showed value in many use cases.

## Reward Model Approaches

Rather than using prompt-based reranking strategies, trained dedicated critic models have provided more effective results, implementing a temporal difference (TD) learning objective to propagate trajectory-level success signals from unit test execution backward through each trajectory. One approach finetunes Qwen 2.5 Coder Instruct 32B as a critic model.

## State-of-the-Art Performance

OpenHands achieved state-of-the-art results on SWE-Bench Verified. More recently, Claude Mythos Preview from Anthropic currently leads the SWE-Bench Verified leaderboard with a score of 0.939 (93.9%).

## Test-Time Scaling Results

Skywork-SWE-32B achieved 38.0% (single run) and 47.0% with test-time scaling, demonstrating significant gains from inference-time compute allocation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "682fc962-3d22-4327-a58d-f2cdcaed77fb",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "1d57921d-c4df-4c80-a8f8-0a29faf0710a",
  "sourceToolAssistantUUID": "682fc962-3d22-4327-a58d-f2cdcaed77fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T18:44:13.540Z_

Let me get more details on the SWE-Shepherd scores and SWE-RM training data, plus check for additional competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d57921d-c4df-4c80-a8f8-0a29faf0710a",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP8HsV5avaQPhTsFT4W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ba28c1e-992c-4c2b-ac58-6a12d8de7a81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqbEreAwBqfknz6sbURqGW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3210,
      "cache_read_input_tokens": 14980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3210,
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

_source line 29 · 2026-05-10T18:44:16.806Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0151cWmmafvRiqLaSXNFKPmf`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.10493",
  "prompt": "Extract the exact numerical results on SWE-bench Verified: 1) What scores does SWE-Shepherd achieve? 2) What is the greedy baseline score? 3) How many SWE-bench Verified tasks were evaluated? 4) Is there a claim of 51% vs 57%? 5) What base model is used? 6) Who are the authors and their affiliations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ba28c1e-992c-4c2b-ac58-6a12d8de7a81",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP8HsV5avaQPhTsFT4W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b49c6ae0-5bb1-43a3-aa44-d9d1f6e8120e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqbEreAwBqfknz6sbURqGW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3210,
      "cache_read_input_tokens": 14980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3210,
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

_source line 30 · 2026-05-10T18:44:19.737Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015Nr4phgDfHGiW4Ebx1HMfs`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.21919v1",
  "prompt": "Extract: 1) Training data size - how many trajectories were used to train SWE-RM? 2) Is scoring binary/whole-trajectory? 3) Does it use best-of-N sampling? 4) Author affiliations - are they from Qwen team/Alibaba? 5) Any mention of ~100K trajectories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b49c6ae0-5bb1-43a3-aa44-d9d1f6e8120e",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP8HsV5avaQPhTsFT4W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41f42a05-4287-493f-833b-2f30c1af767e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqbEreAwBqfknz6sbURqGW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3210,
      "cache_read_input_tokens": 14980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3210,
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

_source line 31 · 2026-05-10T18:44:20.223Z_

<details><summary>↩ Tool result · `toolu_0151cWmmafvRiqLaSXNFKPmf`</summary>

```text
# SWE-Shepherd Results Summary

**1) SWE-Shepherd scores on SWE-Bench Verified:**
- Resolution rate: 51%
- Average cost: 0.053
- Average steps: 12.2

**2) Greedy baseline (mini-SWE-Agent) score:**
- Resolution rate: 57%
- Average cost: 0.029
- Average steps: 15.2

**3) Number of tasks evaluated:**
"100 tasks sampled from SWE-Bench Verified"

**4) 51% vs 57% comparison:**
Yes, this discrepancy is explicitly stated. The paper notes that "SWE-Shepherd reduces the number of interaction steps, indicating more directed exploration. However, it yields a modest drop in resolution rate."

**5) Base model:**
"gpt-5-mini" as shown in Table 1's caption

**6) Authors and affiliations:**
Mahir Labib Dihan and Md Ashrafur Rahman Khan, both from "Bangladesh University of Engineering and Technology (BUET)Bangladesh"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b49c6ae0-5bb1-43a3-aa44-d9d1f6e8120e",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "d503ba72-e6ea-4d46-a294-cba963ddbaa2",
  "sourceToolAssistantUUID": "b49c6ae0-5bb1-43a3-aa44-d9d1f6e8120e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-10T18:44:21.732Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015GwB1jnPTgx6kDhcAnuFQV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.14820",
  "prompt": "Extract: 1) Exact title, 2) Authors and affiliations, 3) Key SWE-bench Verified scores, 4) How does the PRM work (rubric-based?), 5) Is this a competitor to SWE-Shepherd and SWE-PRM?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d503ba72-e6ea-4d46-a294-cba963ddbaa2",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP8HsV5avaQPhTsFT4W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82a13892-70b5-41a5-9f61-b05902d77414",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqbEreAwBqfknz6sbURqGW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3210,
      "cache_read_input_tokens": 14980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3210,
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

_source line 33 · 2026-05-10T18:44:22.150Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AfHeitveyuCTBgp14Q7edY`</summary>

```json
{
  "query": "OpenHands critic model SWE-bench test-time scaling best-of-N reward model 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82a13892-70b5-41a5-9f61-b05902d77414",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP8HsV5avaQPhTsFT4W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e05e844b-9ee0-4192-b7ee-64916d8deabb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqbEreAwBqfknz6sbURqGW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3210,
      "cache_read_input_tokens": 14980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3210,
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

_source line 34 · 2026-05-10T18:44:22.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KpcP2aHz6dRRXvVuRpChbw`</summary>

```json
{
  "query": "SWE-Search MCTS process reward model SWE-bench verified 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e05e844b-9ee0-4192-b7ee-64916d8deabb",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP8HsV5avaQPhTsFT4W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba432853-bcf2-4f36-b406-6ad9fdafaf2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqbEreAwBqfknz6sbURqGW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3210,
      "cache_read_input_tokens": 14980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3210,
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

_source line 35 · 2026-05-10T18:44:25.064Z_

<details><summary>↩ Tool result · `toolu_015Nr4phgDfHGiW4Ebx1HMfs`</summary>

```text
# SWE-RM: Key Details

**1) Training Data Size:**
The paper used approximately 100,000 trajectories for training. The authors state: "the final usable trajectories for training is around 100k" after collecting over 400k multi-turn trajectories and filtering.

**2) Scoring Method:**
Scoring is whole-trajectory based, not binary. The model outputs a continuous score in the range [0,1] derived from log probabilities of YES/NO tokens: "the final score r is calculated by exp(ly)/(exp(ly)+exp(ln)), which maps to a continuous reward model score r∈[0,1]"

**3) Best-of-N Sampling:**
Yes, the paper extensively uses best-of-N sampling through test-time scaling (TTS). They evaluate "RM@K" which represents "the resolve rate of final selected trajectories from k samples" with k ranging up to 32.

**4) Author Affiliations:**
The authors are indeed from the Qwen team at Alibaba Group. The paper lists: "Qwen Team, Alibaba Group" as one of the primary affiliations for most authors.

**5) ~100K Trajectories Mention:**
Confirmed. The paper explicitly references this scale multiple times in training and evaluation sections, particularly when discussing data scaling effects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41f42a05-4287-493f-833b-2f30c1af767e",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "82b3a954-00b5-4652-8145-d1233075fd35",
  "sourceToolAssistantUUID": "41f42a05-4287-493f-833b-2f30c1af767e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T18:44:26.719Z_

<details><summary>↩ Tool result · `toolu_015GwB1jnPTgx6kDhcAnuFQV`</summary>

```text
# SWE-TRACE Paper Analysis

**1) Exact Title:**
"SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling"

**2) Authors and Affiliations:**
The paper lists eight authors: Hao Han, Jin Xie, Xuehao Ma, Weiquan Zhu, Ziyao Zhang, ZhiLiang Long, Hongkai Chen, and Qingwen Ye. However, **no institutional affiliations are provided in this webpage content**.

**3) Key SWE-bench Verified Scores:**
This information is **not available** in the provided webpage. The abstract does not specify exact benchmark scores.

**4) How the PRM Works:**
The framework features "a Rubric-Based Process Reward Model (PRM)" where "an auxiliary Rubric-Agent provides dense, fine-grained heuristic feedback on intermediate steps, guiding the model through long-horizon tasks." The PRM is later repurposed for test-time scaling through dynamic evaluation and pruning of action candidates.

**5) Competitor Comparison:**
The webpage content **does not mention SWE-Shepherd or SWE-PRM**, so no direct comparison to these systems can be determined from this material.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82a13892-70b5-41a5-9f61-b05902d77414",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "0f45036f-f929-466f-a661-1e90b1f47214",
  "sourceToolAssistantUUID": "82a13892-70b5-41a5-9f61-b05902d77414",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T18:44:29.811Z_

<details><summary>↩ Tool result · `toolu_01KpcP2aHz6dRRXvVuRpChbw`</summary>

```text
Web search results for query: "SWE-Search MCTS process reward model SWE-bench verified 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 SWE-SEARCH: ENHANCING SOFTWARE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a1e6783e4d739196cad3336f12d402bf-Paper-Conference.pdf"},{"title":"[2410.20285] SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement","url":"https://arxiv.org/abs/2410.20285"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-TRACE: Optimizing Long-Horizon SWE Agents through Rubric Process Reward Models and Heuristic Test-Time Scaling","url":"https://arxiv.org/html/2604.14820"},{"title":"SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement | OpenReview","url":"https://openreview.net/forum?id=G7sIFXugTX"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"2025-12-29 SWE-RM: EXECUTION-FREE FEEDBACK FOR SOFT- WARE ENGINEERING AGENTS","url":"https://www.arxiv.org/pdf/2512.21919"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"}]

Based on the search results, here's what I found about SWE-Search, MCTS, process reward models, and SWE-bench Verified:

## SWE-Search with MCTS

SWE-Search is a multi-agent framework that integrates Monte Carlo Tree Search (MCTS) with a self-improvement mechanism to enhance software agents' performance on repository-level software tasks. The search algorithm employed is a modified Monte Carlo Tree Search (MCTS), specifically adapted for the tasks of the SWE-Agent. The approach adopts a heuristic-based selection function, similar to the approach used in AlphaZero.

## Framework Components

The framework includes a SWE-Agent for adaptive exploration, a Value Agent for iterative feedback, and a Discriminator Agent that facilitates multi-agent debate for collaborative decision-making.

## Performance on SWE-bench

Applied to the SWE-bench benchmark, the approach demonstrates a 23% relative improvement in performance across five models compared to standard open-source agents without MCTS. The analysis reveals how performance scales with increased inference-time compute through deeper search, providing a pathway to improve software agents without requiring larger models or additional training data.

## SWE-bench Verified

SWE-bench Verified is a human-filtered subset of 500 instances from SWE-bench, created in collaboration with OpenAI.

## Reward Models for SWE

Related to your query about reward models, SWE-RM is an accurate and robust reward model adopting a mixture-of-experts architecture with 30B total parameters and 3B activated during inference. SWE-RM achieves state-of-the-art open-source test-time scaling gains on SWE-Bench Verified.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba432853-bcf2-4f36-b406-6ad9fdafaf2d",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "16fabbe2-ef0b-40a2-a3d7-323243a4d486",
  "sourceToolAssistantUUID": "ba432853-bcf2-4f36-b406-6ad9fdafaf2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T18:44:29.974Z_

<details><summary>↩ Tool result · `toolu_01AfHeitveyuCTBgp14Q7edY`</summary>

```text
Web search results for query: "OpenHands critic model SWE-bench test-time scaling best-of-N reward model 2025"

Links: [{"title":"SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025","url":"https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model"},{"title":"OpenHands/openhands-critic-32b-exp-20250417 · Hugging Face","url":"https://huggingface.co/OpenHands/openhands-critic-32b-exp-20250417"},{"title":"Feature: Implement Critic Model · Issue #8963 · All-Hands-AI/OpenHands","url":"https://github.com/All-Hands-AI/OpenHands/issues/8963"},{"title":"[Agent] Implement Critic Model · Issue #8963 · OpenHands/OpenHands","url":"https://github.com/OpenHands/OpenHands/issues/8963"},{"title":"OpenHands/evaluation/benchmarks/swe_bench/SWE-Gym.md at main · OpenHands/OpenHands","url":"https://github.com/OpenHands/OpenHands/blob/main/evaluation/benchmarks/swe_bench/SWE-Gym.md"},{"title":"Skywork-SWE: Unveiling Data Scaling Laws for Software Engineering in LLMs","url":"https://arxiv.org/html/2506.19290v1"},{"title":"OpenHands vs SWE-Agent: AI Coding Agents Compared | Local AI Master","url":"https://localaimaster.com/blog/openhands-vs-swe-agent"},{"title":"GitHub - OpenHands/benchmarks: Evaluation harness for OpenHands V1. · GitHub","url":"https://github.com/OpenHands/benchmarks"},{"title":"SWE-Gym/docs/OpenHands.md at main · SWE-Gym/SWE-Gym","url":"https://github.com/SWE-Gym/SWE-Gym/blob/main/docs/OpenHands.md"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=lpFFpTbi9s"}]

Based on the search results, here's what I found about OpenHands' critic model and test-time scaling approach:

## OpenHands Critic Model and Test-Time Scaling

OpenHands trained a dedicated critic model rather than using a prompt-based reranking strategy, which provided more effective results.

### Training Approach

For the training process, they rolled out agent trajectories to avoid data leakage, implemented a temporal difference (TD) learning objective to propagate trajectory-level success signals from unit test execution backward through each trajectory, and added a regression head on top of the last layer to predict reward values.

### Model Details

They used veRL to finetune Qwen 2.5 Coder Instruct 32B as a critic model. The critic model is publicly available on HuggingFace for researchers.

### Best-of-N Reward Model Strategy

For each SWE-Bench problem, they run OpenHands agent multiple times using Claude 3.7 Sonnet with sampling temperature 1.0 to generate multiple solutions that lead to multiple code patches. They trained a "critic model" that evaluates each solution and predicts whether it's a good solution or not, filter out code patches that fail regression and reproduction tests, and select the solution from the trajectory with the highest score as the final answer.

### Performance Impact

The OpenHands agent's baseline performance on SWE-Bench Verified is 60.6%. This test-time scaling approach with the critic model helped achieve state-of-the-art results on SWE-Bench Verified in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e05e844b-9ee0-4192-b7ee-64916d8deabb",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "e852b3a2-886f-451e-a52d-0f7a0364f87f",
  "sourceToolAssistantUUID": "e05e844b-9ee0-4192-b7ee-64916d8deabb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-10T18:44:38.710Z_

Let me get the SWE-TRACE scores and check for any other recent competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e852b3a2-886f-451e-a52d-0f7a0364f87f",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP9n7diStLgyTtB3nx4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b43d1449-fa3c-49a6-8cd0-2526e3837a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBmR1TYinywi4TqrpS1CEX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 932,
      "cache_creation_input_tokens": 2518,
      "cache_read_input_tokens": 18190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2518,
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

_source line 40 · 2026-05-10T18:44:40.881Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Eiz3GudfKbeUiKp2PCMdQh`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.14820",
  "prompt": "Extract the exact numerical results on SWE-bench Verified and SWE-bench. What resolution rates does SWE-TRACE achieve? What are the baseline comparisons? Who are the authors affiliated with (vivo?)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b43d1449-fa3c-49a6-8cd0-2526e3837a86",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP9n7diStLgyTtB3nx4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b283cc8b-de74-4988-b021-e1175539c791",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBmR1TYinywi4TqrpS1CEX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 932,
      "cache_creation_input_tokens": 2518,
      "cache_read_input_tokens": 18190,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 932,
          "output_tokens": 209,
          "cache_read_input_tokens": 18190,
          "cache_creation_input_tokens": 2518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2518,
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

_source line 41 · 2026-05-10T18:44:41.070Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013WFakYWKaCWTGQVUJKJuBa`</summary>

```json
{
  "query": "SWE-RL reinforcement learning SWE-bench reward model 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b283cc8b-de74-4988-b021-e1175539c791",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauP9n7diStLgyTtB3nx4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d88349ee-0c56-49db-aa9e-205cf0b975ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBmR1TYinywi4TqrpS1CEX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 932,
      "cache_creation_input_tokens": 2518,
      "cache_read_input_tokens": 18190,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 932,
          "output_tokens": 209,
          "cache_read_input_tokens": 18190,
          "cache_creation_input_tokens": 2518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2518,
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

_source line 42 · 2026-05-10T18:44:46.672Z_

<details><summary>↩ Tool result · `toolu_01Eiz3GudfKbeUiKp2PCMdQh`</summary>

```text
# SWE-TRACE Results Summary

## Main Performance Results on SWE-bench Verified

According to Table 2, SWE-TRACE achieves:

- **SWE-TRACE-4B**: 38.9% resolve rate (40.7% with heuristic-guided TTS)
- **SWE-TRACE-30B**: 63.5% resolve rate (71.2% with heuristic-guided TTS)

## Key Baseline Comparisons

The paper compares against several notable systems:

- **SWE-Master-4B-RL**: 33.4% (SWE-TRACE outperforms by 5.5 points)
- **SWE-Master-32B**: 61.4% without TTS; 70.8% with TTS@8
- **DeepSWE-32B + TTS@16**: 59.0%
- **R2E-Gym-32B + TTS@16**: 49.4%

The 30B-A3B variant with heuristic-guided test-time scaling reaches 71.2%, matching top open-source performance.

## Author Affiliations

"Hao Han, Jin Xie, Xuehao Ma, Weiquan Zhu, Ziyao Zhang, ZhiLiang Long, Hongkai Chen and Qingwen Ye" are affiliated with **vivo, ShenZhen, China**. The corresponding author is listed as Chen (allenhkchen@gmail.com).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b283cc8b-de74-4988-b021-e1175539c791",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "8c76e451-7f27-4646-8676-338b14e72d86",
  "sourceToolAssistantUUID": "b283cc8b-de74-4988-b021-e1175539c791",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T18:44:47.818Z_

<details><summary>↩ Tool result · `toolu_013WFakYWKaCWTGQVUJKJuBa`</summary>

```text
Web search results for query: "SWE-RL reinforcement learning SWE-bench reward model 2025 arXiv"

Links: [{"title":"[2502.18449] SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution","url":"https://arxiv.org/abs/2502.18449"},{"title":"GitHub - facebookresearch/swe-rl: [NeurIPS'25] Official codebase for \"SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution\" · GitHub","url":"https://github.com/facebookresearch/swe-rl"},{"title":"SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution | OpenReview","url":"https://openreview.net/forum?id=ULblO61XZ0"},{"title":"SWE-RL: Advancing LLM Reasoning via Reinforcement ...","url":"https://arxiv.org/pdf/2502.18449"},{"title":"SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution","url":"https://arxiv.org/html/2502.18449v1"},{"title":"Paper page - SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution","url":"https://huggingface.co/papers/2502.18449"},{"title":"NeurIPS Poster SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution","url":"https://neurips.cc/virtual/2025/poster/117772"},{"title":"Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning","url":"https://arxiv.org/html/2508.03501v1"},{"title":"2025-12-29 SWE-RM: EXECUTION-FREE FEEDBACK FOR SOFT- WARE ENGINEERING AGENTS","url":"https://www.arxiv.org/pdf/2512.21919"},{"title":"2025-12-23 - by Kim Seonghyeon - arXiv Daily","url":"https://rosinality.substack.com/p/2025-12-23"}]

Based on the search results, here's what I found about SWE-RL:

## Overview

SWE-RL is the first approach to scale RL-based LLM reasoning for real-world software engineering. It leverages a lightweight rule-based reward (e.g., the similarity score between ground-truth and LLM-generated solutions) and enables LLMs to autonomously recover a developer's reasoning processes and solutions by learning from extensive open-source software evolution data.

## Key Results

Trained on top of Llama 3, the resulting reasoning model, Llama3-SWE-RL-70B, achieves a 41.0% solve rate on SWE-bench Verified -- a human-verified collection of real-world GitHub issues. This is the best performance reported for medium-sized (<100B) LLMs to date, even comparable to leading proprietary LLMs like GPT-4o.

## Generalization Beyond Software Engineering

Despite performing RL solely on software evolution data, Llama3-SWE-RL has emerged with generalized reasoning skills and shows improved results on five out-of-domain tasks, namely, function coding, library use, code reasoning, mathematics, and general language understanding.

## Publication Details

The paper (arXiv:2502.18449) was published on February 25, 2025, and was accepted as a NeurIPS 2025 poster.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d88349ee-0c56-49db-aa9e-205cf0b975ef",
  "isSidechain": true,
  "promptId": "7f60437d-c1e5-4843-9b85-b330ef5e25c7",
  "agentId": "a4eb21958785d9238",
  "type": "user",
  "uuid": "525d3192-9bd2-475c-93c1-2c15878c2d97",
  "sourceToolAssistantUUID": "d88349ee-0c56-49db-aa9e-205cf0b975ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-10T18:45:30.510Z_

Now I have sufficient information to compile a comprehensive verification report. Here is the summary:

---

## Paper Verification Report

### Paper 1: SWE-PRM / "When Agents Go Astray" (arXiv:2509.02360)

**EXISTS: YES**

| Claim | Verification | Status |
|-------|-------------|--------|
| Title | "When Agents go Astray: Course-Correcting SWE Agents with PRMs" | CORRECT |
| arXiv ID | 2509.02360 | CORRECT |
| Date | Submitted Sept 2, 2025 (revised Oct 21, 2025) | CORRECT |
| Affiliation | IBM Research (confirmed via IBM Research publications page) | CORRECT |
| Method | Prompt-based behavioral pattern detection (looping, redundancy, failure to terminate) | MOSTLY CORRECT -- the paper calls these "taxonomy-guided PRMs" using prompt-based inference-time intervention. The behavioral patterns listed are "redundant exploration, looping, and failure to terminate" rather than "looping, drift, redundancy" |
| Scores | 40.0% -> 50.6% on SWE-bench Verified | CORRECT (exact match) |
| "First PRM for SWE agents" | NOT explicitly claimed in the paper | DISCREPANCY -- the characterization says it claims this, but the paper does not make this assertion |
| Not a trained model | The paper describes using closed-source LLMs as PRMs at inference time with taxonomy-guided prompts, not training a dedicated model | CORRECT |

**Minor discrepancies:** (1) The behavioral patterns are described as "redundant exploration, looping, failure to terminate" -- the user's characterization says "drift" instead of "failure to terminate." (2) The "first PRM" claim is not in the paper itself.

---

### Paper 2: SWE-RM (arXiv:2512.21919)

**EXISTS: YES**

| Claim | Verification | Status |
|-------|-------------|--------|
| Title | "SWE-RM: Execution-free Feedback For Software Engineering Agents" | CORRECT |
| arXiv ID | 2512.21919 | CORRECT |
| Date | Submitted Dec 26, 2025 | CORRECT (Dec 2025) |
| Affiliation | Qwen Team, Alibaba Group | CORRECT |
| Architecture | 30B MoE, 3B active during inference | CORRECT |
| Training data | ~100K trajectories (filtered from 400K+) | CORRECT |
| Scoring method | Whole-trajectory scoring, continuous [0,1] via YES/NO log-probs | PARTIALLY CORRECT -- it is whole-trajectory, but NOT binary; it produces a continuous score in [0,1] |
| Scores | Flash: 51.6% -> 62.0%, Max: 67.0% -> 74.6% on SWE-bench Verified | CORRECT (exact match) |
| Best-of-N | Uses test-time scaling (TTS) with RM@K (best-of-N selection) | CORRECT |

**Minor discrepancy:** The scoring is described as "binary" in the characterization, but it is actually continuous [0,1] derived from log-probabilities of YES/NO tokens. It is whole-trajectory (not step-level), which is correct.

---

### Paper 3: SWE-Shepherd (arXiv:2604.10493)

**EXISTS: YES**

| Claim | Verification | Status |
|-------|-------------|--------|
| Title | "SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents" | CORRECT |
| arXiv ID | 2604.10493 | CORRECT |
| Date | April 12, 2026 | CORRECT |
| Affiliation | Bangladesh University of Engineering and Technology (BUET) | Not mentioned in user's characterization but confirmed |
| Method | Step-level action-utility PRMs for SWE agents | CORRECT |
| Scores | 51% resolution rate vs. 57% greedy baseline | CORRECT (exact match) |
| Evaluation scope | 100 tasks from SWE-bench Verified | CORRECT |
| Base model | Uses gpt-5-mini | Not mentioned in characterization |

**No significant discrepancies.** The characterization is accurate. The paper does show a *decrease* from the greedy baseline (57% -> 51%), which is correctly noted. The paper acknowledges "challenges in aligning intermediate rewards with final task success."

---

### Additional Competitors NOT Mentioned in the Landscape

The following relevant works were found that also address reward models / test-time scaling for SWE-bench and are not listed in the user's three papers:

1. **SWE-TRACE** (arXiv:2604.14820, April 2026, vivo) -- Uses a Rubric-Based Process Reward Model (PRM) with heuristic-guided test-time scaling. Achieves 63.5% (71.2% with TTS) on SWE-bench Verified with a 30B model. This is a direct competitor using step-level PRMs.

2. **OpenHands Critic Model** (Nov 2025, All-Hands-AI) -- A trained critic model (finetuned Qwen 2.5 Coder 32B) using temporal difference learning for trajectory evaluation, combined with best-of-N selection. Achieved SOTA on SWE-bench Verified in late 2025 (baseline 60.6%, improved with TTS).

3. **SWE-Search** (arXiv:2410.20285, ICLR 2025) -- Uses Monte Carlo Tree Search with a Value Agent providing process-level feedback. Achieves 23% relative improvement over standard agents. Not a trained reward model but uses LLM-as-judge for value estimation.

4. **SWE-RL** (arXiv:2502.18449, Feb 2025, Meta/Facebook Research, NeurIPS 2025) -- Uses RL with rule-based rewards (not a learned reward model) to train Llama 3 for SWE tasks. Achieves 41.0% on SWE-bench Verified with a 70B model.

5. **SWE-TRACE** and **SWE-Shepherd** are the most directly comparable as step-level PRM approaches published in April 2026.

---

### Summary of Discrepancies

- **Paper 1 (SWE-PRM):** Two minor issues: (a) behavioral patterns are "redundant exploration, looping, failure to terminate" not "looping, drift, redundancy"; (b) "first PRM for SWE agents" claim is not made in the paper.
- **Paper 2 (SWE-RM):** One minor issue: scoring is continuous [0,1], not "binary" as characterized.
- **Paper 3 (SWE-Shepherd):** Characterization is accurate. All numbers match.

All three papers exist and are real. The key claims (scores, methods, dates) are substantively correct with the minor caveats noted above.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "525d3192-9bd2-475c-93c1-2c15878c2d97",
  "isSidechain": true,
  "agentId": "a4eb21958785d9238",
  "requestId": "req_011CauPB6LXksGCSsswRA8Rc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e45a5447-4757-43a3-a1cf-b4c8e183f330",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e48a7609-5e29-4d47-9bd4-04d751de1c24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019izWXgdsPo2qVtFcezJTa6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2449,
      "cache_read_input_tokens": 20708,
      "output_tokens": 1715,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1715,
          "cache_read_input_tokens": 20708,
          "cache_creation_input_tokens": 2449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2449,
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
