# Research conversation: Use WebSearch to verify the following papers actually exist. For each, search for the exact title and confirm the venue,

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a327e1a9e86a7783f.jsonl`
- **Structured JSON:** [`c569738a9a31c96afb02.json`](../../sessions/c5/c569738a9a31c96afb02.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-14T03:08:15.046Z_

Use WebSearch to verify the following papers actually exist. For each, search for the exact title and confirm the venue, year, and core contribution. Report which ones are confirmed real and which are suspect.

1. "CUPID: Curating Data your Robot Loves with Influence Functions" (CoRL 2025)
2. "Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons" (RSS 2026)
3. "Skill or Luck? Return Decomposition via Advantage Functions" (ICLR 2024)
4. "Conservative Offline Robot Policy Learning via Posterior-Transition Reweighting / PTR" (arXiv Mar 2026)
5. "Quality over Quantity: Demonstration Curation via Influence Functions / QoQ" (arXiv Mar 2026)
6. "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning" (ICRA 2026)
7. "Demo-SCORE: Curating Demonstrations using Online Experience" (RSS 2025)
8. "RINSE / Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning" (ICML 2025)

For each paper, just report: confirmed/not found, actual venue if different, and a one-line summary of what it does. Keep response under 400 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "a327e1a9e86a7783f",
  "type": "user",
  "uuid": "06bbddfa-a760-4651-a457-85271820a3c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T03:08:15.051Z_

```json
{
  "parentUuid": "06bbddfa-a760-4651-a457-85271820a3c8",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
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
  "uuid": "1bf2ab84-cd70-49bb-a46b-8046faec9608",
  "timestamp": "2026-05-14T03:08:15.051Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T03:08:17.640Z_



I'll search for each paper systematically. Let me start by loading the WebSearch tool and then searching for all papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bf2ab84-cd70-49bb-a46b-8046faec9608",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izYerkxrAhfQwM2H6q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbd3e62a-575e-4efc-9476-4a50a6b0bc26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZWL35Vxc77eAZ7FqV8vnK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8154,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8154,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T03:08:18.049Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FiHFgm91CefFHwLsupozwZ`</summary>

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
  "parentUuid": "fbd3e62a-575e-4efc-9476-4a50a6b0bc26",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izYerkxrAhfQwM2H6q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "caec19c4-d765-4da8-a1b8-a9bbed765d86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZWL35Vxc77eAZ7FqV8vnK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8154,
      "cache_read_input_tokens": 0,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8154,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T03:08:18.053Z_

<details><summary>↩ Tool result · `toolu_01FiHFgm91CefFHwLsupozwZ`</summary>

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
  "parentUuid": "caec19c4-d765-4da8-a1b8-a9bbed765d86",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "a327e1a9e86a7783f",
  "type": "user",
  "uuid": "41826c3f-cf39-41de-8b6c-d3863d464532",
  "sourceToolAssistantUUID": "caec19c4-d765-4da8-a1b8-a9bbed765d86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T03:08:22.179Z_



Now let me search for all 8 papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41826c3f-cf39-41de-8b6c-d3863d464532",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izmjQsSEvTGaEknZ1U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f54c1a59-d985-47a1-b393-d1dfba66daaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5Gw5h7aji7wr8UBdKHye3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T03:08:23.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wp1C6suzorL3CrZX9RXvbe`</summary>

```json
{
  "query": "CUPID Curating Data Robot Loves Influence Functions CoRL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f54c1a59-d985-47a1-b393-d1dfba66daaf",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izmjQsSEvTGaEknZ1U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d7d2d7f-1674-46d5-b330-5b5f2bac8abb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5Gw5h7aji7wr8UBdKHye3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T03:08:24.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0117hE3ZiXLBaM6VQQ1EdJp9`</summary>

```json
{
  "query": "Robometer Scaling General-Purpose Robotic Reward Models Trajectory Comparisons RSS 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d7d2d7f-1674-46d5-b330-5b5f2bac8abb",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izmjQsSEvTGaEknZ1U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45549ce5-8310-41cd-91ac-6921fcbe43a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5Gw5h7aji7wr8UBdKHye3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T03:08:25.139Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KFoFwEhR9GKa4dGCxoqAAg`</summary>

```json
{
  "query": "\"Skill or Luck? Return Decomposition via Advantage Functions\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45549ce5-8310-41cd-91ac-6921fcbe43a1",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izmjQsSEvTGaEknZ1U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6748fe51-2e90-4c56-bfdc-fc17c70af71d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5Gw5h7aji7wr8UBdKHye3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T03:08:26.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011iXUFAExaQX44adUhXvi4G`</summary>

```json
{
  "query": "\"Conservative Offline Robot Policy Learning\" Posterior-Transition Reweighting PTR arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6748fe51-2e90-4c56-bfdc-fc17c70af71d",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izmjQsSEvTGaEknZ1U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5df3866-e854-4167-8608-33ca2efd53fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5Gw5h7aji7wr8UBdKHye3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T03:08:27.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E1g5DTNQTJfWczs4D5DZjr`</summary>

```json
{
  "query": "\"Quality over Quantity\" Demonstration Curation Influence Functions QoQ arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5df3866-e854-4167-8608-33ca2efd53fb",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izmjQsSEvTGaEknZ1U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff393dc0-c9ca-4aee-a8d0-2ee0cd4958b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5Gw5h7aji7wr8UBdKHye3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T03:08:28.031Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K5QsXifzFpc2iPueH8tx11`</summary>

```json
{
  "query": "SCIZOR Self-Supervised Data Curation Large-Scale Imitation Learning ICRA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff393dc0-c9ca-4aee-a8d0-2ee0cd4958b3",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izmjQsSEvTGaEknZ1U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0146bcd6-0a43-422d-be98-888564dc2e6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5Gw5h7aji7wr8UBdKHye3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T03:08:28.820Z_

<details><summary>↩ Tool result · `toolu_01Wp1C6suzorL3CrZX9RXvbe`</summary>

```text
Web search results for query: "CUPID Curating Data Robot Loves Influence Functions CoRL 2025"

Links: [{"title":"GitHub - agiachris/cupid: Official repository for \"CUPID: Curating Data your Robot Loves with Influence Functions,\" accepted to CoRL 2025. · GitHub","url":"https://github.com/agiachris/cupid"},{"title":"[2506.19121] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions | OpenReview","url":"https://openreview.net/forum?id=TqevdDMqrK"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"[2506.19121v2] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121v2"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://proceedings.mlr.press/v305/agia25a.html"},{"title":"[PDF] CUPID: Curating Data your Robot Loves with Influence Functions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CUPID:-Curating-Data-your-Robot-Loves-with-Agia-Sinha/666481cd9e72de8e90e3dd12fb826338f5ce17f0"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"CUPID: Robot Data Curation via Influence Functions","url":"https://www.emergentmind.com/papers/2506.19121"}]

I found comprehensive information about CUPID. Here are the key details:

## Overview

CUPID (CUrating Performance-Influencing Demonstrations) is a data curation method for robot imitation learning that uses influence functions to estimate the causal impact of each demonstration on a policy's closed-loop performance, and was accepted to Conference on Robot Learning (CoRL) 2025.

## How It Works

CUPID is a robot data curation method based on a novel influence function-theoretic formulation for imitation learning policies. Given a set of evaluation rollouts, CUPID estimates the influence of each training demonstration on the policy's expected return, enabling ranking and selection of demonstrations according to their impact on the policy's closed-loop performance.

## Applications

CUPID curates data by 1) filtering out training demonstrations that harm policy performance and 2) subselecting newly collected trajectories that will most improve the policy.

## Key Results

Training with less than 33% of curated data can yield state-of-the-art diffusion policies on the simulated RoboMimic benchmark, with similar gains observed in hardware. Furthermore, hardware experiments show that the method can identify robust strategies under distribution shift, isolate spurious correlations, and even enhance the post-training of generalist robot policies.

## Resources

The official code repository for "CUPID: Curating Data your Robot Loves with Influence Functions" is available for CoRL 2025. The paper has been published in the proceedings with arXiv identifier 2506.19121, and code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d7d2d7f-1674-46d5-b330-5b5f2bac8abb",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "a327e1a9e86a7783f",
  "type": "user",
  "uuid": "65e97469-cb80-4cbc-99ac-8e07d422acea",
  "sourceToolAssistantUUID": "7d7d2d7f-1674-46d5-b330-5b5f2bac8abb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T03:08:29.434Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QLQx4tKTTurPjy4wWr9EEg`</summary>

```json
{
  "query": "\"Demo-SCORE\" Curating Demonstrations Online Experience RSS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65e97469-cb80-4cbc-99ac-8e07d422acea",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izmjQsSEvTGaEknZ1U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70cbcf9d-8cd3-4964-abe9-e1c43cd29fce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5Gw5h7aji7wr8UBdKHye3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T03:08:30.120Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xec9DshDwq4DJmpJ3gw5og`</summary>

```json
{
  "query": "RINSE \"Learning from the Best\" Smoothness-Driven Metrics Data Quality Imitation Learning ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70cbcf9d-8cd3-4964-abe9-e1c43cd29fce",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1izmjQsSEvTGaEknZ1U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74fb8fef-9c34-4051-8085-526ba9ac8155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5Gw5h7aji7wr8UBdKHye3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8154,
      "output_tokens": 487,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1419
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 487,
          "cache_read_input_tokens": 8154,
          "cache_creation_input_tokens": 1419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1419,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T03:08:30.968Z_

<details><summary>↩ Tool result · `toolu_0117hE3ZiXLBaM6VQQ1EdJp9`</summary>

```text
Web search results for query: "Robometer Scaling General-Purpose Robotic Reward Models Trajectory Comparisons RSS 2026"

Links: [{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"},{"title":"[2603.02115] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/html/2603.02115v1"},{"title":"GitHub - robometer/robometer: Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons · GitHub","url":"https://github.com/robometer/robometer"},{"title":"Scaling General-Purpose Robotic Reward Models via ...","url":"https://robometer.github.io/assets/robometer.pdf"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | alphaXiv","url":"https://www.alphaxiv.org/abs/2603.02115"},{"title":"[2603.02115v1] Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://arxiv.org/abs/2603.02115v1"},{"title":"Jiahui Zhang's research works | University of Southern California and other places","url":"https://www.researchgate.net/scientific-contributions/Jiahui-Zhang-2254368611"},{"title":"ROBOMETER: Scaling Robotic Reward Models - YouTube","url":"https://www.youtube.com/watch?v=WBBdgLdncG4"},{"title":"GitHub - philfung/reward-scope: visually compare robot reward functions · GitHub","url":"https://github.com/philfung/reward-scope"}]

I found comprehensive information about Robometer. Here's what the research shows:

## Overview

Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons is a paper presented at Robotics: Science and Systems (RSS) 2026.

## Key Innovation

Robometer is a scalable reward modeling framework that combines intra-trajectory progress supervision with inter-trajectory preference supervision, trained with a dual objective: a frame-level progress loss that anchors reward magnitude on expert data, and a trajectory-comparison preference loss that imposes global ordering constraints across trajectories of the same task, enabling effective learning from both real and augmented failed trajectories.

## Dataset

The authors release RBM-1M, a large-scale reward-learning dataset comprising over one million trajectories spanning diverse robot embodiments and tasks, including substantial suboptimal and failure data.

## Performance and Applications

Across benchmarks and real-world evaluations, Robometer learns more generalizable reward functions than prior methods and improves robot learning performance across a diverse set of downstream applications.

## Capabilities

A general-purpose robotic reward model trained on trajectory comparisons from the RBM-1M dataset provides dense, video-language-conditioned rewards for robot learning.

The research represents a significant advance in scaling reward models for robotics by effectively handling both labeled expert demonstrations and unlabeled suboptimal/failed trajectories through comparison-based learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45549ce5-8310-41cd-91ac-6921fcbe43a1",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "a327e1a9e86a7783f",
  "type": "user",
  "uuid": "ca052b7c-5aeb-4545-a11e-8326515333fb",
  "sourceToolAssistantUUID": "45549ce5-8310-41cd-91ac-6921fcbe43a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T03:08:32.038Z_

<details><summary>↩ Tool result · `toolu_01KFoFwEhR9GKa4dGCxoqAAg`</summary>

```text
Web search results for query: ""Skill or Luck? Return Decomposition via Advantage Functions" ICLR 2024"

Links: [{"title":"Skill or Luck? Return Decomposition via Advantage Functions | OpenReview","url":"https://openreview.net/forum?id=ZFMiHfZwIf"},{"title":"[2402.12874] Skill or Luck? Return Decomposition via Advantage Functions","url":"https://arxiv.org/abs/2402.12874"},{"title":"ICLR Poster Skill or Luck? Return Decomposition via Advantage Functions","url":"https://iclr.cc/virtual/2024/poster/18406"},{"title":"SKILL OR LUCK? RETURN DECOMPOSITION VIA AD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/277628cff838927d869cd1f671328ce0-Paper-Conference.pdf"},{"title":"Skill or Luck? Return Decomposition via Advantage Functions","url":"https://arxiv.org/html/2402.12874v1"},{"title":"Computer Science Feb 2024","url":"https://web3.arxiv.org/list/cs/2024-02?skip=6000&show=1000"},{"title":"Structured Difference-of-Q via Orthogonal Learning","url":"https://arxiv.org/pdf/2406.08697"},{"title":"Skill or Luck? Return Decomposition via Advantage Functions Hsiao-Ru Pan","url":"https://openreview.net/pdf?id=AEwuWKjH-S"},{"title":"CiteSeerX","url":"https://citeseerx.ist.psu.edu/search_result?query=Skill+or+Luck%3F+Return+Decomposition+via+Advantage+Functions."},{"title":"ICLR 2024 Papers","url":"https://iclr.cc/virtual/2024/papers.html"}]

I found the paper you're looking for! Here's information about "Skill or Luck? Return Decomposition via Advantage Functions" from ICLR 2024:

## Overview

The paper builds on the insight that the advantage function can be understood as the causal effect of an action on the return, and shows that this allows decomposing the return of a trajectory into parts caused by the agent's actions (skill) and parts outside of the agent's control (luck).

## Key Contributions

The decomposition enables a natural extension of Direct Advantage Estimation (DAE) to off-policy settings (Off-policy DAE), which can learn from off-policy trajectories without relying on importance sampling techniques or truncating off-policy actions.

## Authors

The paper is authored by Hsiao-Ru Pan and Bernhard Schölkopf.

## Methodology

The key observation is that the randomness of the environment can be treated as actions from an imaginary agent, whose actions determine the future of the decision-making agent.

## Results

The authors draw connections between Off-policy DAE and previous methods to demonstrate how it can speed up learning and when the proposed off-policy corrections are important, and use the MinAtar environments to illustrate how ignoring off-policy corrections can lead to suboptimal policy optimization performance.

You can access the paper through multiple sources including [arXiv (2402.12874)](https://arxiv.org/abs/2402.12874), [OpenReview](https://openreview.net/forum?id=ZFMiHfZwIf), and the [ICLR proceedings](https://iclr.cc/virtual/2024/poster/18406).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6748fe51-2e90-4c56-bfdc-fc17c70af71d",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "a327e1a9e86a7783f",
  "type": "user",
  "uuid": "89c2b99e-9044-49d8-867f-736e8f86ff3f",
  "sourceToolAssistantUUID": "6748fe51-2e90-4c56-bfdc-fc17c70af71d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T03:08:33.703Z_

<details><summary>↩ Tool result · `toolu_011iXUFAExaQX44adUhXvi4G`</summary>

```text
Web search results for query: ""Conservative Offline Robot Policy Learning" Posterior-Transition Reweighting PTR arXiv 2026"

Links: [{"title":"Conservative Offline Robot Policy Learning via Posterior-Transition Reweighting","url":"https://arxiv.org/html/2603.16542v1"},{"title":"Conservative Offline Robot Policy Learning via Posterior ...","url":"https://s3.dxchallenge.ai.kr/dxnews/raw/docs/f3c29c098477727a1e8f2633644bcadc7bf111b65de23eb9086f3eb7bc84d5e7.pdf"},{"title":"[2210.05178] Pre-Training for Robots: Offline RL Enables Learning New Tasks from a Handful of Trials","url":"https://arxiv.org/abs/2210.05178"},{"title":"Robustness Evaluation of Offline Reinforcement Learning for Robot Control Against Action Perturbations","url":"https://arxiv.org/html/2412.18781"},{"title":"What you reward is what you learn: Comparing rewards for online speech policy optimization in public HRI","url":"https://arxiv.org/html/2601.01969v1"},{"title":"Pre-Training for Robots: Offline RL Enables Learning New Tasks in a Handful of Trials","url":"https://arxiv.org/html/2210.05178v3"},{"title":"Robotic Policy Learning via Human-assisted Action Preference Optimization","url":"https://arxiv.org/html/2506.07127v1"},{"title":"Adversarial Fine-tuning in Offline-to-Online Reinforcement Learning for Robust Robot Control","url":"https://arxiv.org/html/2510.13358"},{"title":"1 Introduction","url":"https://arxiv.org/html/2604.24357"},{"title":"Beyond Static Datasets: Robust Offline Policy Optimization via Vetted Synthetic Transitions","url":"https://arxiv.org/html/2601.18107"}]

I found the paper you're looking for! Here's what I found:

## Conservative Offline Robot Policy Learning via Posterior-Transition Reweighting (PTR)

Posterior-Transition Reweighting (PTR) is a reward-free and conservative post-training method that decides how much each training sample should influence the supervised update.

### Key Approach

For each sample, PTR encodes the observed post-action consequence as a latent target, inserts it into a candidate pool of mismatched targets, and uses a separate transition scorer to estimate a softmax identification posterior over target indices.

A lightweight consequence encoder and transition scorer produce per-sample weights from observed post-action consequences, without requiring reward labels or a tractable policy likelihood.

### Technical Components

The method includes belief proxy tokens that summarize interaction history, an identification scorer that converts post-action consequences into a per-sample quality signal, theoretical foundations that justify reading this signal as a density ratio and KL divergence, a conservative weight mapping that bounds distribution shift, and an adaptive controller that keeps the scorer in a stable operating range.

### Experimental Results

Corrupted samples typically produce less concentrated identification posteriors and therefore lose relative emphasis, while clean samples with distinctive consequences are amplified.

The paper was published on arXiv on March 17, 2026 (arXiv:2603.16542).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5df3866-e854-4167-8608-33ca2efd53fb",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "a327e1a9e86a7783f",
  "type": "user",
  "uuid": "1a9aa093-800f-49ae-b328-bdd35ab50dc3",
  "sourceToolAssistantUUID": "d5df3866-e854-4167-8608-33ca2efd53fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T03:08:34.271Z_

<details><summary>↩ Tool result · `toolu_01K5QsXifzFpc2iPueH8tx11`</summary>

```text
Web search results for query: "SCIZOR Self-Supervised Data Curation Large-Scale Imitation Learning ICRA 2026"

Links: [{"title":"SCIZOR: Self-Supervised Data Curation for Large-Scale Imitation Learning","url":"https://ut-austin-rpl.github.io/SCIZOR/"},{"title":"[2505.22626] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/abs/2505.22626"},{"title":"Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/html/2505.22626v2"},{"title":"Huihan Liu on X: \"Our data curation work SCIZOR is accepted to ICRA 2026! Check out this self-supervised data curation approach that removes suboptimal and duplicated data for large-scale imitation learning, led by @YZ_Franklin @yuqi_xie5\" / X","url":"https://x.com/huihan_liu/status/2017698931493195899"},{"title":"SCIZOR: A Self-Supervised Approach to Data Curation for ...","url":"https://openreview.net/pdf?id=Wo8eEdFUDF"},{"title":"Copyright by Yuqi Xie 2025 1","url":"https://repositories.lib.utexas.edu/bitstreams/d8256e22-405e-4881-87d8-ca3f8008345e/download"},{"title":"(PDF) SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.researchgate.net/publication/392167457_SCIZOR_A_Self-Supervised_Approach_to_Data_Curation_for_Large-Scale_Imitation_Learning"},{"title":"GitHub - UT-Austin-RPL/SCIZOR · GitHub","url":"https://github.com/UT-Austin-RPL/SCIZOR"},{"title":"Publications – UT Austin Robot Perception and Learning Lab","url":"https://rpl.cs.utexas.edu/publications/"},{"title":"[Literature Review] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.themoonlight.io/en/review/scizor-a-self-supervised-approach-to-data-curation-for-large-scale-imitation-learning"}]

I found comprehensive information about SCIZOR. Here's a summary of the research:

## Overview

SCIZOR is a paper presented at the 2026 IEEE International Conference on Robotics and Automation (ICRA). The paper was authored by Yu Zhang, Yuqi Xie, Huihan Liu, Rutav Shah, Michael Wan, Linxi Fan, and Yuke Zhu.

## What is SCIZOR?

SCIZOR is a self-supervised data curation framework that filters out low-quality state-action pairs to improve the performance of imitation learning policies. The framework addresses a key challenge in robotics: large-scale datasets used for policy training often introduce substantial variability in quality, which can negatively impact performance, making it essential to automatically curate datasets by filtering low-quality samples.

## Key Approach

SCIZOR targets two complementary sources of low-quality data: suboptimal data, which hinder learning with undesirable actions, and redundant data, which dilute training with repetitive patterns.

The framework uses two main components:
- A progress-prediction model that flags and removes frames failing to make meaningful task progress, without needing reward signals
- Joint visual-action embeddings that are clustered to detect and discard look-alike segments, ensuring diversity

## Results

SCIZOR improved policy performance across diverse large-scale imitation learning benchmarks, achieving an average success rate increase of 15.4% compared to training on the full dataset. Specifically, SCIZOR yielded absolute gains of 5.4% on RoboMimic, 8.1% on OXEMagic, and 32.9% on Sirius-Fleet.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0146bcd6-0a43-422d-be98-888564dc2e6d",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "a327e1a9e86a7783f",
  "type": "user",
  "uuid": "5ad0e3ba-d1cb-4be6-bfd1-b77b6861c145",
  "sourceToolAssistantUUID": "0146bcd6-0a43-422d-be98-888564dc2e6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T03:08:34.940Z_

<details><summary>↩ Tool result · `toolu_01E1g5DTNQTJfWczs4D5DZjr`</summary>

```text
Web search results for query: ""Quality over Quantity" Demonstration Curation Influence Functions QoQ arXiv 2026"

Links: [{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation","url":"https://arxiv.org/html/2502.08211v1"},{"title":"Quality Over Quantity? LLM-Based Curation for a Data-Efficient Audio–Video Foundation Model","url":"https://arxiv.org/html/2503.09205v1"},{"title":"[2502.08211] Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation","url":"https://arxiv.org/abs/2502.08211"},{"title":"[2503.09205] Quality Over Quantity? LLM-Based Curation for a Data-Efficient Audio-Video Foundation Model","url":"https://arxiv.org/abs/2503.09205"},{"title":"Quality Over Quantity? LLM-Based Curation for a Data-Efficient Audio-Video Foundation Model | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/quality-over-quantity-llm-based-curation-data"},{"title":"Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250208211X/abstract"},{"title":"[2507.00038] Quality over Quantity: An Effective Large-Scale Data Reduction Strategy Based on Pointwise V-Information","url":"https://arxiv.org/abs/2507.00038"},{"title":"[2211.06440] Data Quality Over Quantity: Pitfalls and Guidelines for Process Analytics","url":"https://arxiv.org/abs/2211.06440"}]

Based on the search results, I found the paper you're looking for:

## Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning

This is an arXiv paper (2603.09056) titled "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning", published in March 2026.

**Key Contributions:**

The paper proposes Quality over Quantity (QoQ), a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations.

**Technical Approach:**

The work leverages influence functions, which quantify the impact of individual training samples on model performance. The paper introduces two key techniques to adapt influence functions for robot demonstrations: (i) using maximum influence across validation samples to capture the most relevant state-action pairs, and (ii) aggregating influence scores of state-action pairs within the same trajectory to reduce noise and improve data coverage.

**Results:**

Experiments in both simulated and real-world settings show that QoQ consistently improves policy performances over prior data selection methods. The authors report substantial improvements, with QoQ substantially outperforming baseline methods that rely on state and action features.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff393dc0-c9ca-4aee-a8d0-2ee0cd4958b3",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "a327e1a9e86a7783f",
  "type": "user",
  "uuid": "8254e2fa-e1ba-4152-807b-c7c2d43adca7",
  "sourceToolAssistantUUID": "ff393dc0-c9ca-4aee-a8d0-2ee0cd4958b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T03:08:36.737Z_

<details><summary>↩ Tool result · `toolu_01QLQx4tKTTurPjy4wWr9EEg`</summary>

```text
Web search results for query: ""Demo-SCORE" Curating Demonstrations Online Experience RSS 2025"

Links: [{"title":"[2503.03707] Curating Demonstrations using Online Experience","url":"https://arxiv.org/abs/2503.03707"},{"title":"Curating Demonstrations using Online Experience · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/71/"},{"title":"Demo-SCORE: Curating Demonstrations using Online Experience","url":"https://anniesch.github.io/demo-score/"},{"title":"Curating Demonstrations using Online Experience","url":"https://arxiv.org/html/2503.03707v1"},{"title":"[PDF] Curating Demonstrations using Online Experience | Semantic Scholar","url":"https://www.semanticscholar.org/paper/776c9466ece2a34832d4ebef206fa5c2e9855b39"},{"title":"Curating Demonstrations using Online Experience","url":"https://www.researchgate.net/publication/395366581_Curating_Demonstrations_using_Online_Experience"},{"title":"Illustration of Demo-SCORE. Our method self-curates demonstrations... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/llustration-of-Demo-SCORE-Our-method-self-curates-demonstrations-through-online-robot_fig2_389617044"},{"title":"[Literature Review] Curating Demonstrations using Online Experience","url":"https://www.themoonlight.io/en/review/curating-demonstrations-using-online-experience"},{"title":"Curating Demonstrations using Online Experience | alphaXiv","url":"https://www.alphaxiv.org/en/overview/2503.03707"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"}]

I found relevant information about Demo-SCORE. Here's what the search results reveal:

## Demo-SCORE: Curating Demonstrations using Online Experience

Demo-SCORE is a method where robots self-curate demonstrations based on online robot experience. The method was proposed by Annie S. Chen, Alec M. Lessing, Yuejiang Liu, and Chelsea Finn to improve robotic learning from heterogeneous demonstration datasets.

### The Problem

Many robot demonstration datasets contain heterogeneous demonstrations of varying quality. While this heterogeneity may benefit policy pre-training, it can hinder robot performance when used with a final imitation learning objective, as some strategies in the data may be less reliable than others or may be underrepresented, leading to poor performance when such strategies are sampled at test time.

### The Approach

The method self-curates demonstrations through online robot experience in four steps: (i) train a policy on the full demonstration set; (ii) evaluate the policy by generating rollouts with different checkpoints; (iii) use these rollouts to train and cross-validate a classifier that distinguishes between success and failure trajectories; (iv) filter out unreliable demonstrations based on the learned classifier, retaining only ones that do not reflect policy failures for subsequent policy training.

### Results

Demo-SCORE achieves over 15-35% higher absolute success rate in the resulting policy compared to the base policy trained with all original demonstrations. Experiments in simulation and the real world show that Demo-SCORE can effectively identify suboptimal demonstrations without manual curation.

The paper was published on arXiv in March 2025 and presented at Robotics: Science and Systems (RSS) 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70cbcf9d-8cd3-4964-abe9-e1c43cd29fce",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "a327e1a9e86a7783f",
  "type": "user",
  "uuid": "45c644cd-7f15-4f67-8def-93998a2acfe1",
  "sourceToolAssistantUUID": "70cbcf9d-8cd3-4964-abe9-e1c43cd29fce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T03:08:37.719Z_

<details><summary>↩ Tool result · `toolu_01Xec9DshDwq4DJmpJ3gw5og`</summary>

```text
Web search results for query: "RINSE "Learning from the Best" Smoothness-Driven Metrics Data Quality Imitation Learning ICML 2025"

Links: [{"title":"ICML Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning","url":"https://icml.cc/virtual/2025/48703"},{"title":"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning","url":"https://arxiv.org/html/2604.23000"},{"title":"[2604.23000] Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning","url":"https://arxiv.org/abs/2604.23000"},{"title":"Smoothness-Driven Metrics for Data Quality in Imitation Learning","url":"https://escholarship.org/uc/item/7d43m7q3"},{"title":"GitHub - DmitryRyumin/ICML-2025-Papers: ICML 2025 Papers: Dive into cutting-edge research from the premier machine learning conference. Stay current with breakthroughs in deep learning, generative AI, optimization, reinforcement learning, and beyond. Code implementations included. ⭐ support the future of machine learning research!","url":"https://github.com/DmitryRyumin/ICML-2025-Papers"},{"title":"Data Quality in Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=FwmvbuDiMk&noteId=yRiDkOIoZK"},{"title":"ICML Poster Reward-free World Models for Online Imitation Learning","url":"https://icml.cc/virtual/2025/poster/44035"},{"title":"GitHub - TobyLeelsz/iqmpc: Official code implementation of ICML 2025 paper: Reward-free World Models for Online Imitation Learning · GitHub","url":"https://github.com/TobyLeelsz/iqmpc"},{"title":"International Conference on Machine Learning - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning"},{"title":"ICML.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025"}]

Based on the search results, I found information about the RINSE paper presented at ICML 2025:

## RINSE: Learning from the Best

RINSE (Ranking and INdexing Smooth Examples) is a general-purpose method for filtering demonstration data based on trajectory smoothness.

### Overview

In behavioral cloning (BC), policy performance is fundamentally limited by demonstration data quality. Real-world datasets contain trajectories of varying quality due to operator skill differences, teleoperation artifacts, and procedural inconsistencies, yet standard BC treats all demonstrations equally. Existing curation methods require costly policy training in the loop or manual annotation, limiting scalability.

### Methodology

Grounded in motor control theory which establishes smoothness as a hallmark of skilled movement, RINSE uses two complementary metrics: Spectral Arc Length (SAL), a spectral measure of frequency-domain regularity, and Trajectory-Envelope Distance (TED), a spatial measure of contact-aware geometric deviation.

### Key Results

On RoboMimic benchmarks, SAL filtering achieves 16% higher success using one-sixth of the data. On real-world manipulation, TED filtering achieves 20% improvement with half the data. As a retrieval-stage filter within STRAP on LIBERO-10, RINSE re-ranking improves mean success by 5.6%. As soft weights in Re-Mix domain reweighting, RINSE scores produce domain allocations highly correlated with the learned Re-Mix allocations (Spearman ρ ≥ 0.89).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74fb8fef-9c34-4051-8085-526ba9ac8155",
  "isSidechain": true,
  "promptId": "67dbc3c0-6b67-40ae-87e6-d5bedbe528b5",
  "agentId": "a327e1a9e86a7783f",
  "type": "user",
  "uuid": "1a70efe8-bbbb-41da-9a61-7ca5faaa6e71",
  "sourceToolAssistantUUID": "74fb8fef-9c34-4051-8085-526ba9ac8155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T03:08:56.315Z_

Here are the verification results for all 8 papers:

1. **CUPID** -- **Confirmed.** CoRL 2025. Uses influence functions to estimate the causal impact of each demonstration on a robot policy's closed-loop performance, enabling data curation for imitation learning.

2. **Robometer** -- **Confirmed.** RSS 2026. Scales general-purpose robotic reward models by combining intra-trajectory progress supervision with inter-trajectory preference supervision; releases the RBM-1M dataset.

3. **Skill or Luck?** -- **Confirmed.** ICLR 2024. Decomposes trajectory returns into skill (caused by agent actions) and luck (environment stochasticity) via advantage functions, enabling off-policy Direct Advantage Estimation.

4. **Conservative Offline Robot Policy Learning / PTR** -- **Confirmed.** arXiv March 2026 (2603.16542). A reward-free conservative post-training method that reweights training samples using a posterior-transition identification scorer over post-action consequences.

5. **Quality over Quantity / QoQ** -- **Confirmed.** arXiv March 2026 (2603.09056). Uses influence functions to score each training sample's contribution to reducing validation loss, with trajectory-level aggregation for robust demonstration curation.

6. **SCIZOR** -- **Confirmed.** ICRA 2026. Self-supervised data curation that removes suboptimal and redundant data via progress prediction and visual-action embedding clustering, yielding ~15% average success rate improvement.

7. **Demo-SCORE** -- **Confirmed.** RSS 2025. Self-curates demonstrations by training a success/failure classifier on online rollouts, then filtering unreliable demos, achieving 15-35% absolute success rate gains.

8. **RINSE** -- **Confirmed.** ICML 2025. Ranks demonstrations by smoothness metrics (Spectral Arc Length and Trajectory-Envelope Distance) grounded in motor control theory; achieves 16-20% gains using a fraction of the data.

**Verdict: All 8 papers are confirmed real**, with venues and years matching the claims exactly.

Sources:
- [CUPID - arXiv](https://arxiv.org/abs/2506.19121)
- [Robometer - arXiv](https://arxiv.org/abs/2603.02115)
- [Skill or Luck - OpenReview](https://openreview.net/forum?id=ZFMiHfZwIf)
- [PTR - arXiv](https://arxiv.org/html/2603.16542v1)
- [QoQ - arXiv](https://arxiv.org/abs/2603.09056)
- [SCIZOR - arXiv](https://arxiv.org/abs/2505.22626)
- [Demo-SCORE - arXiv](https://arxiv.org/abs/2503.03707)
- [RINSE - arXiv](https://arxiv.org/abs/2604.23000)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a70efe8-bbbb-41da-9a61-7ca5faaa6e71",
  "isSidechain": true,
  "agentId": "a327e1a9e86a7783f",
  "requestId": "req_011Cb1j2DVjjJosFJvx9UpUE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07543f2f-c707-4871-b2e7-ceb35cb43db9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61cc855-bcd5-40d8-8f85-70088aeddc62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REkzyq6V4vVM6JDJL3mpcT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7770,
      "cache_read_input_tokens": 9573,
      "output_tokens": 728,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7770
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 728,
          "cache_read_input_tokens": 9573,
          "cache_creation_input_tokens": 7770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7770,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
