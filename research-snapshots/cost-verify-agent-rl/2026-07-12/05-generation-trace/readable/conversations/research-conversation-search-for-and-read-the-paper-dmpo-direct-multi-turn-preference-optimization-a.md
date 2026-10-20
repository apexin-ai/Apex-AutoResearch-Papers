# Research conversation: Search for and read the paper "DMPO: Direct Multi-Turn Preference Optimization" (arXiv 2406.14868). I need to understand

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a76b8ec9d8df322ec.jsonl`
- **Structured JSON:** [`39aff4e5e3d3ded14580.json`](../../sessions/39/39aff4e5e3d3ded14580.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-10T18:41:29.639Z_

Search for and read the paper "DMPO: Direct Multi-Turn Preference Optimization" (arXiv 2406.14868). I need to understand:
1. What is the core method (how does it handle multi-turn DPO)?
2. What is the length normalization mechanism?
3. What benchmarks does it evaluate on?
4. What are its limitations?

Use WebSearch to find the paper, then use WebFetch to read the abstract and method details from the arXiv page. Report a concise summary (under 300 words).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "36700c88-7827-4864-8959-5e80899588bf",
  "agentId": "a76b8ec9d8df322ec",
  "type": "user",
  "uuid": "3bb094ef-4e82-403f-a978-292ef22a2fa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:41:29.647Z_

```json
{
  "parentUuid": "3bb094ef-4e82-403f-a978-292ef22a2fa6",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
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
  "uuid": "68438a89-19af-447f-8a7a-81b8bc2b0c8f",
  "timestamp": "2026-05-10T18:41:29.647Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T18:41:33.058Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YUry4wkhnPGyGWdSkUVzJP`</summary>

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
  "parentUuid": "68438a89-19af-447f-8a7a-81b8bc2b0c8f",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
  "requestId": "req_011CauNvVBYST6Z6xzoY1Yj8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3c4743c-93b3-47d1-bbb3-7c9ee8fe389e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hxmKTQri3HgRqADWQMKek",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 673,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 673,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-10T18:41:33.099Z_

<details><summary>↩ Tool result · `toolu_01YUry4wkhnPGyGWdSkUVzJP`</summary>

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
  "parentUuid": "c3c4743c-93b3-47d1-bbb3-7c9ee8fe389e",
  "isSidechain": true,
  "promptId": "36700c88-7827-4864-8959-5e80899588bf",
  "agentId": "a76b8ec9d8df322ec",
  "type": "user",
  "uuid": "9248abcc-2daa-4e77-b2a7-1031c204b632",
  "sourceToolAssistantUUID": "c3c4743c-93b3-47d1-bbb3-7c9ee8fe389e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T18:41:36.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015YPkQjKEYxQg1L4Gmqo5p4`</summary>

```json
{
  "query": "DMPO Direct Multi-Turn Preference Optimization arXiv 2406.14868",
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
  "parentUuid": "9248abcc-2daa-4e77-b2a7-1031c204b632",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
  "requestId": "req_011CauNvkN6rTSd9hCZqd2v6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edbdaf33-4e5e-4531-add5-c3451c4f8b41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qhYsdxUwCbMWg4jxboxPb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8896,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 8896,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1888,
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

_source line 6 · 2026-05-10T18:41:42.767Z_

<details><summary>↩ Tool result · `toolu_015YPkQjKEYxQg1L4Gmqo5p4`</summary>

```text
Web search results for query: "DMPO Direct Multi-Turn Preference Optimization arXiv 2406.14868"

Links: [{"title":"[2406.14868] Direct Multi-Turn Preference Optimization for Language Agents","url":"https://arxiv.org/abs/2406.14868"},{"title":"Direct Multi-Turn Preference Optimization for Language Agents","url":"https://arxiv.org/pdf/2406.14868"},{"title":"Importance Sampling for Multi-Negative Multimodal Direct Preference Optimization","url":"https://arxiv.org/html/2509.25717"},{"title":"DiaTool-DPO: Multi-Turn Direct Preference Optimization for Tool-Augmented Large Language Models","url":"https://arxiv.org/html/2504.02882v1"},{"title":"SDPO: Segment-Level Direct Preference Optimization for Social Agents","url":"https://arxiv.org/html/2501.01821"},{"title":"[2504.02882] DiaTool-DPO: Multi-Turn Direct Preference Optimization for Tool-Augmented Large Language Models","url":"https://arxiv.org/abs/2504.02882"},{"title":"mDPO: Conditional Preference Optimization for Multimodal Large Language Models","url":"https://arxiv.org/html/2406.11839"},{"title":"A Comprehensive Survey of Direct Preference Optimization: Datasets, Theories, Variants, and Applications","url":"https://arxiv.org/html/2410.15595v2"},{"title":"A Survey of Direct Preference Optimization","url":"https://arxiv.org/html/2503.11701v1"},{"title":"Finetuning Large Language Model for Personalized Ranking","url":"https://arxiv.org/html/2405.16127"}]

Based on the search results, I found information about DMPO (Direct Multi-Turn Preference Optimization) from arXiv paper 2406.14868:

## Overview

Direct Multi-Turn Preference Optimization for Language Agents is the paper 2406.14868. DMPO uses state-action occupancy measure constraints and trajectory length normalization to improve multi-turn alignment learning.

## Key Features

DMPO is a simple loss function for multi-turn agent tasks that directly optimizes the RL objective by maximizing the likelihood of preferred trajectories over dispreferred ones.

DMPO enhances the existing DPO method by replacing the policy constraint with a State-Action Occupancy Measure (SAOM) constraint and incorporating length normalization into the Bradley-Terry model, effectively addressing challenges in multi-turn scenarios.

## Evaluation

Extensive experiments on three multi-turn agent task datasets confirm the effectiveness and superiority of the DMPO loss. DMPO was proposed to address agent tasks such as WebShop, ScienceWorld, and ALFWorld.

The paper was first published on June 21, 2024, and has undergone several revisions, with the most recent update in February 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edbdaf33-4e5e-4531-add5-c3451c4f8b41",
  "isSidechain": true,
  "promptId": "36700c88-7827-4864-8959-5e80899588bf",
  "agentId": "a76b8ec9d8df322ec",
  "type": "user",
  "uuid": "47d8f3cb-dcc5-4a9a-8709-7ac85264c149",
  "sourceToolAssistantUUID": "edbdaf33-4e5e-4531-add5-c3451c4f8b41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T18:41:47.125Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RHbW4cECMDqRPvysAMi8au`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.14868",
  "prompt": "Extract the full abstract, the core method details (how DMPO handles multi-turn DPO, what is state-action occupancy measure constraint, how length normalization works), the benchmarks used for evaluation, and any stated limitations of the approach."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d8f3cb-dcc5-4a9a-8709-7ac85264c149",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
  "requestId": "req_011CauNwTAH1tL4Vt2wfCrUn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "181eb769-4ea0-4a55-89d9-a18aaf340221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNX3Lji6ttnRtdVjDNbtkE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 10784,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 10784,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 836,
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

_source line 8 · 2026-05-10T18:41:52.516Z_

<details><summary>↩ Tool result · `toolu_01RHbW4cECMDqRPvysAMi8au`</summary>

```text
# Direct Multi-Turn Preference Optimization for Language Agents: Key Details

## Full Abstract
"Adapting Large Language Models (LLMs) for agent tasks is critical in developing language agents. Direct Preference Optimization (DPO) is a promising technique for this adaptation with the alleviation of compounding errors, offering a means to directly optimize Reinforcement Learning (RL) objectives. However, applying DPO to multi-turn tasks presents challenges due to the inability to cancel the partition function. Overcoming this obstacle involves making the partition function independent of the current state and addressing length disparities between preferred and dis-preferred trajectories. In this light, we replace the policy constraint with the state-action occupancy measure constraint in the RL objective and add length normalization to the Bradley-Terry model, yielding a novel loss function named DMPO for multi-turn agent tasks with theoretical explanations. Extensive experiments on three multi-turn agent task datasets confirm the effectiveness and superiority of the DMPO loss."

## Core Method Details

**The DMPO Approach:**
The paper introduces DMPO through two key modifications:

1. **State-Action Occupancy Measure Constraint**: Rather than applying traditional policy constraints, the authors "replace the policy constraint with the state-action occupancy measure constraint in the RL objective," enabling the partition function to become independent of the current state and allowing it to be cancelled during optimization.

2. **Length Normalization**: The researchers "add length normalization to the Bradley-Terry model" to handle trajectories with different lengths in multi-turn settings.

## Benchmarks
The abstract indicates evaluation occurred on "three multi-turn agent task datasets" but specific benchmark names are not detailed in the provided webpage content.

## Stated Limitations
No explicit limitations are mentioned in the webpage excerpt provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "181eb769-4ea0-4a55-89d9-a18aaf340221",
  "isSidechain": true,
  "promptId": "36700c88-7827-4864-8959-5e80899588bf",
  "agentId": "a76b8ec9d8df322ec",
  "type": "user",
  "uuid": "871d1dc0-1abe-4308-9b66-8db215b2df82",
  "sourceToolAssistantUUID": "181eb769-4ea0-4a55-89d9-a18aaf340221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T18:41:57.927Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XAixiDRQg4tTTz7Jp5xMhW`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2406.14868",
  "prompt": "Extract: 1) The specific benchmarks/datasets used for evaluation (e.g. WebShop, ALFWorld, ScienceWorld). 2) Details on how length normalization works mathematically or conceptually - does it divide the log-probability by trajectory length? 3) Any stated limitations or future work section. 4) How exactly the state-action occupancy measure (SAOM) constraint differs from the standard policy constraint in DPO and why it helps in multi-turn settings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "871d1dc0-1abe-4308-9b66-8db215b2df82",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
  "requestId": "req_011CauNxAv18BPq98tBxmfuw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa1aa905-8b84-4499-85cb-a3b986cc1915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3DKpWEUeP92J443Meeo3E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 540,
      "cache_read_input_tokens": 11620,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 540
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 11620,
          "cache_creation_input_tokens": 540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 540,
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

_source line 10 · 2026-05-10T18:42:02.340Z_

<details><summary>↩ Tool result · `toolu_01XAixiDRQg4tTTz7Jp5xMhW`</summary>

```text
I appreciate your request, but I must note that the provided content appears to be a PDF file encoded in binary format rather than readable text. The material shows PDF stream objects, image data, and compressed content that cannot be meaningfully parsed to extract the specific information you're requesting.

To properly answer your questions about:
1. Benchmark datasets used
2. Length normalization mathematics
3. Limitations and future work
4. SAOM constraint mechanics

I would need access to the actual readable text or a properly formatted document. The current content consists largely of:
- PDF object definitions (XObject, Form, Image types)
- Compressed/encoded streams
- Binary image data (JPEG streams)
- Flate-encoded content

**Recommendation:** Could you provide:
- A text-extracted version of the paper
- A direct link to the paper
- The paper title so I can reference it properly

This would allow me to deliver accurate, properly-quoted information within your specified constraints.

[Binary content (application/pdf, 1.6MB) also saved to /home/ubuntu/.claude-account-2/projects/-/fd09aaea-1e2a-47f1-ba7a-1943938c18c7/tool-results/webfetch-1778438517951-0jd0ep.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa1aa905-8b84-4499-85cb-a3b986cc1915",
  "isSidechain": true,
  "promptId": "36700c88-7827-4864-8959-5e80899588bf",
  "agentId": "a76b8ec9d8df322ec",
  "type": "user",
  "uuid": "525d0426-ba93-433a-b189-9d846cff5822",
  "sourceToolAssistantUUID": "aa1aa905-8b84-4499-85cb-a3b986cc1915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T18:42:06.861Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YaqKvnF9LjJUuFLnMrBQkB`</summary>

```json
{
  "url": "https://arxiv.org/html/2406.14868",
  "prompt": "Extract: 1) The specific benchmarks/datasets used for evaluation (e.g. WebShop, ALFWorld, ScienceWorld). 2) Details on how length normalization works - does it divide the log-probability by trajectory length? What is the formula? 3) Any stated limitations or future work section. 4) How exactly the state-action occupancy measure (SAOM) constraint differs from the standard policy constraint in DPO and why it helps in multi-turn settings - what is the key mathematical insight?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "525d0426-ba93-433a-b189-9d846cff5822",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
  "requestId": "req_011CauNxtt8CXJmvbSAW1gYv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c337c42-69b6-42e8-9e76-a71195c98716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RfdeQeoDX9B3PXGwg8fGV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 493,
      "cache_read_input_tokens": 12160,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 493
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 12160,
          "cache_creation_input_tokens": 493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 493,
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

_source line 12 · 2026-05-10T18:42:06.874Z_

<details><summary>↩ Tool result · reported error · `toolu_01YaqKvnF9LjJUuFLnMrBQkB`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c337c42-69b6-42e8-9e76-a71195c98716",
  "isSidechain": true,
  "promptId": "36700c88-7827-4864-8959-5e80899588bf",
  "agentId": "a76b8ec9d8df322ec",
  "type": "user",
  "uuid": "1d5cae07-f7cf-4657-b233-d72cb2d14262",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "0c337c42-69b6-42e8-9e76-a71195c98716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T18:42:10.270Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NNHhJmaBauHT5NmPTNrbaQ`</summary>

```json
{
  "query": "DMPO \"Direct Multi-Turn Preference Optimization\" length normalization state-action occupancy measure WebShop ALFWorld limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d5cae07-f7cf-4657-b233-d72cb2d14262",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
  "requestId": "req_011CauNyELA2av2p2TnGWGkA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76b82dfa-f1dc-4617-876f-e13082e2c69b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kRLmth27yrwh56nQ5jamt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 224,
      "cache_read_input_tokens": 12653,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 12653,
          "cache_creation_input_tokens": 224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 224,
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

_source line 14 · 2026-05-10T18:42:16.057Z_

<details><summary>↩ Tool result · `toolu_01NNHhJmaBauHT5NmPTNrbaQ`</summary>

```text
Web search results for query: "DMPO "Direct Multi-Turn Preference Optimization" length normalization state-action occupancy measure WebShop ALFWorld limitations"

Links: [{"title":"[2406.14868] Direct Multi-Turn Preference Optimization for Language Agents","url":"https://arxiv.org/abs/2406.14868"},{"title":"DiaTool-DPO: Multi-Turn Direct Preference Optimization for Tool-Augmented Large Language Models","url":"https://arxiv.org/html/2504.02882v1"},{"title":"Direct Multi-Turn Preference Optimization for Language Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240614868S/abstract"},{"title":"Paper page - Direct Multi-Turn Preference Optimization for Language Agents","url":"https://huggingface.co/papers/2406.14868"},{"title":"Direct Multi-Turn Preference Optimization for Language Agents","url":"https://arxiv.org/pdf/2406.14868"},{"title":"Direct Multi-Turn Preference Optimization for Language Agents | USTC Lab for Data Science","url":"https://data-science.ustc.edu.cn/_upload/tpl/15/04/5380/template5380/publication/emnlp24-swt.html"},{"title":"Direct Multi-Turn Preference Optimization for Language Agents | OpenReview","url":"https://openreview.net/forum?id=FVTPELeltD"},{"title":"[2504.02882] DiaTool-DPO: Multi-Turn Direct Preference Optimization for Tool-Augmented Large Language Models","url":"https://ar5iv.labs.arxiv.org/html/2504.02882"},{"title":"1 A Survey of Direct Preference Optimization","url":"https://www.arxiv.org/pdf/2503.11701"},{"title":"SDPO: Segment-Level Direct Preference Optimization for Social Agents","url":"https://arxiv.org/html/2501.01821v1"}]

Based on the web search results, here's what I found about DMPO (Direct Multi-Turn Preference Optimization):

## Overview

DMPO introduces a novel loss function to address challenges in applying Direct Preference Optimization to multi-turn agent tasks by adjusting the RL objective and normalizing trajectory lengths.

## Key Technical Components

DMPO replaces the policy constraint with the state-action occupancy measure constraint in the RL objective and adds length normalization to the Bradley-Terry model. More specifically, DMPO uses state-action occupancy measure constraints and trajectory length normalization to improve multi-turn alignment learning.

## Applications

DMPO was proposed to address agent tasks such as WebShop, ScienceWorld, and ALFWorld.

## Limitations and Modifications

Recent research has identified limitations in DMPO's approach to length normalization. DMPO does not discuss the impact of length normalization, and this transformation lacks rigorous theoretical justification. Additionally, contrary to the findings of DMPO, some follow-up work found minimal impact of reward scaling on evaluation metrics, attributed to different evaluation approaches between agent tasks and tool-augmented LLM tasks where agent tasks accumulate errors through trajectories making initial turns more important than later turns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76b82dfa-f1dc-4617-876f-e13082e2c69b",
  "isSidechain": true,
  "promptId": "36700c88-7827-4864-8959-5e80899588bf",
  "agentId": "a76b8ec9d8df322ec",
  "type": "user",
  "uuid": "a684e35a-a406-4396-bd7e-7b689bcad185",
  "sourceToolAssistantUUID": "76b82dfa-f1dc-4617-876f-e13082e2c69b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T18:42:20.607Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018nHWR8wHgXcxzvMX1cZ5v9`</summary>

```json
{
  "url": "https://openreview.net/forum?id=FVTPELeltD",
  "prompt": "Extract details about DMPO: 1) How the state-action occupancy measure constraint works and why it helps cancel the partition function in multi-turn DPO. 2) The length normalization mechanism - formula or description. 3) The three benchmarks (WebShop, ALFWorld, ScienceWorld) and key results. 4) Any stated limitations, weaknesses, or criticism from reviewers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a684e35a-a406-4396-bd7e-7b689bcad185",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
  "requestId": "req_011CauNyuW6tm7u5EMnrQ9Hs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec9531fa-c01c-48d4-bd62-7b4fc628bc7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3S6tr7G8jvYHwsdZ3UXAS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 12877,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 12877,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 875,
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

_source line 16 · 2026-05-10T18:42:24.949Z_

<details><summary>↩ Tool result · `toolu_018nHWR8wHgXcxzvMX1cZ5v9`</summary>

```text
I appreciate your detailed question about DMPO, but I must be transparent: **the web page content provided contains only OpenReview's navigation and footer information—it does not include any technical details about DMPO or any research paper.**

The page excerpt shows:
- OpenReview's login page
- Navigation links (About, Venues, FAQ, Contact, etc.)
- Footer copyright and policy links
- A general mission statement about open peer review

To extract information about DMPO's state-action occupancy measures, length normalization, benchmark results, or reviewer critiques, I would need the actual research paper or article content, which is not present in the material you shared.

**I cannot fabricate technical details or research findings.** If you'd like me to analyze DMPO, please provide:
1. The full paper text or abstract
2. A direct link to the OpenReview submission
3. The relevant sections discussing methodology and results

I'm happy to help once you share the actual source material.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec9531fa-c01c-48d4-bd62-7b4fc628bc7e",
  "isSidechain": true,
  "promptId": "36700c88-7827-4864-8959-5e80899588bf",
  "agentId": "a76b8ec9d8df322ec",
  "type": "user",
  "uuid": "ef6aff1f-16f7-414b-9be1-1e4a4cc759b4",
  "sourceToolAssistantUUID": "ec9531fa-c01c-48d4-bd62-7b4fc628bc7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T18:42:28.643Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KgHG4cpaHHyLPnQkTAzBuc`</summary>

```json
{
  "url": "https://huggingface.co/papers/2406.14868",
  "prompt": "Extract all technical details about DMPO: 1) How the state-action occupancy measure constraint works. 2) The length normalization mechanism. 3) Benchmarks and results. 4) Limitations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef6aff1f-16f7-414b-9be1-1e4a4cc759b4",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
  "requestId": "req_011CauNzZZ5w1sUgby3KvuzN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1709095-2dcc-483d-865f-4114889e6564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKXvrvqunpma4H34kzFuFD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 13752,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 13752,
          "cache_creation_input_tokens": 404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 404,
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

_source line 18 · 2026-05-10T18:42:29.259Z_

<details><summary>↩ Tool result · `toolu_01KgHG4cpaHHyLPnQkTAzBuc`</summary>

```text
&lt;persisted-output>
Output too large (53.7KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-/fd09aaea-1e2a-47f1-ba7a-1943938c18c7/tool-results/toolu_01KgHG4cpaHHyLPnQkTAzBuc.txt

Preview (first 2KB):
# Direct Multi-Turn Preference Optimization for Language Agents

Wentao Shi&lt;sup>1\*&lt;/sup> Mengqi Yuan&lt;sup>1\*&lt;/sup> Junkang Wu&lt;sup>1&lt;/sup> Qifan Wang&lt;sup>2&lt;/sup> Fuli Feng&lt;sup>1†&lt;/sup>

&lt;sup>1&lt;/sup>University of Science and Technology of China &lt;sup>2&lt;/sup>Meta AI

{shiwentao123, yuanmengqi}@mail.ustc.edu.cn wqfcr@fb.com {jkwu0909, fulifeng93}@gmail.com

## Abstract

Adapting Large Language Models (LLMs) for agent tasks is critical in developing language agents. Direct Preference Optimization (DPO) is a promising technique for this adaptation with the alleviation of compounding errors, offering a means to directly optimize Reinforcement Learning (RL) objectives. However, applying DPO to multi-turn tasks presents challenges due to the inability to cancel the partition function. Overcoming this obstacle involves making the partition function independent of the current state and addressing length disparities between preferred and dis-preferred trajectories. In this light, we replace the policy constraint with the state-action occupancy measure constraint in the RL objective and add length normalization to the Bradley-Terry model, yielding a novel loss function named DMPO for multi-turn agent tasks with theoretical explanations. Extensive experiments on three multi-turn agent task datasets confirm the effectiveness and superiority of the DMPO loss. The code is available at &lt;https://github.com/swt-user/DMPO>.

## 1 Introduction

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1709095-2dcc-483d-865f-4114889e6564",
  "isSidechain": true,
  "promptId": "36700c88-7827-4864-8959-5e80899588bf",
  "agentId": "a76b8ec9d8df322ec",
  "type": "user",
  "uuid": "b89e0642-28ca-4a1f-8456-961a53c9ce32",
  "sourceToolAssistantUUID": "d1709095-2dcc-483d-865f-4114889e6564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T18:42:32.875Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BhKitHKWPeNJPVTnXJVrYC`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-/fd09aaea-1e2a-47f1-ba7a-1943938c18c7/tool-results/toolu_01KgHG4cpaHHyLPnQkTAzBuc.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b89e0642-28ca-4a1f-8456-961a53c9ce32",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
  "requestId": "req_011CauNzsxcpfRorEH2fxEdF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3b9478e-72ea-4916-b9de-9eb3910fa3c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GA2Q9w7wnonLUsKK7RnkWe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 14156,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 14156,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 628,
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

_source line 20 · 2026-05-10T18:42:33.194Z_

<details><summary>↩ Tool result · `toolu_01BhKitHKWPeNJPVTnXJVrYC`</summary>

```text
1	# Direct Multi-Turn Preference Optimization for Language Agents
2	
3	Wentao Shi&lt;sup>1\*&lt;/sup> Mengqi Yuan&lt;sup>1\*&lt;/sup> Junkang Wu&lt;sup>1&lt;/sup> Qifan Wang&lt;sup>2&lt;/sup> Fuli Feng&lt;sup>1†&lt;/sup>
4	
5	&lt;sup>1&lt;/sup>University of Science and Technology of China &lt;sup>2&lt;/sup>Meta AI
6	
7	{shiwentao123, yuanmengqi}@mail.ustc.edu.cn wqfcr@fb.com {jkwu0909, fulifeng93}@gmail.com
8	
9	## Abstract
10	
11	Adapting Large Language Models (LLMs) for agent tasks is critical in developing language agents. Direct Preference Optimization (DPO) is a promising technique for this adaptation with the alleviation of compounding errors, offering a means to directly optimize Reinforcement Learning (RL) objectives. However, applying DPO to multi-turn tasks presents challenges due to the inability to cancel the partition function. Overcoming this obstacle involves making the partition function independent of the current state and addressing length disparities between preferred and dis-preferred trajectories. In this light, we replace the policy constraint with the state-action occupancy measure constraint in the RL objective and add length normalization to the Bradley-Terry model, yielding a novel loss function named DMPO for multi-turn agent tasks with theoretical explanations. Extensive experiments on three multi-turn agent task datasets confirm the effectiveness and superiority of the DMPO loss. The code is available at &lt;https://github.com/swt-user/DMPO>.
12	
13	## 1 Introduction
14	
15	Developing generalist agents capable of solving complex tasks has been a central goal in the artificial intelligence community (Reed et al., 2022; Team et al., 2024). Recently, *Language agents* (Yao et al., 2022b) emerge as a prominent research direction, leveraging the considerable potential of Large Language Models to address intricate tasks involving instruction following (Ouyang et al., 2022), action planning (Huang et al., 2022), and tool utilization (Schick et al., 2024). Nevertheless, the substantial disparity between the pretraining task of Large Language Models and the requirements of agent tasks suggests significant potential for future advancements in language agent capabilities.
16	
17	Behavioral Cloning (BC) (Pomerleau, 1991) is a frequently employed approach to bridge the domain gap by fine-tuning LLMs through expert agent trajectories. Recent endeavors in BC (Chen et al., 2023; Zeng et al., 2023; Yin et al., 2023) involve the Supervised Fine-tuning of LLMs on optimal state-action pairs. Although these methods enable swift adaptation of LLMs to agent tasks, BC is notably susceptible to *compounding errors* — minor errors of the learner accumulate along interactions between the agent and environment, leading to performance deterioration in non-deterministic environments (Ross et al., 2011).
18	
19	In alleviating compounding errors, Direct Preference Optimization (Rafailov et al., 2024b) has demonstrated remarkable success in the single-turn preference alignment task due to its simple implementation and robustness. DPO optimizes RL objectives by maximizing the likelihood of preferred responses over dis-preferred responses, mitigating the need for continuous interaction with the environment and the training instability commonly associated with traditional RL algorithms (Christianos et al., 2023; Liang et al., 2024). Although there has been an initial endeavor to apply the DPO loss on LLMs for agent tasks (Song et al., 2024), it encounters suboptimal performance, as it is tailored specifically for the single-turn bandit setting and is ill-suited for multi-turn agent tasks.
20	
21	This work aims to develop a robust loss function capable of directly optimizing RL objectives in multi-turn scenarios. The crux of this pursuit involves eliminating the partition function in the Bradley-Terry (BT) model (Bradley and Terry, 1952; Christiano et al., 2017). This entails ensuring the partition function’s independence from the current state and neutralizing the impact of the length disparity between preferred and dis-preferred trajectories. To achieve this, we substitute the policy constraint with the state-action occupancy measure (SAOM) (Johnson et al., 2000) constraint in the
22	
23	\*Both authors contributed equally to this research.
24	
25	†Corresponding AuthorFigure 1: Illustration of DMPO loss, which directly optimizes the RL objective by maximizing the likelihood of the preferred trajectory over the dispreferred trajectory.
26	
27	RL objective and introduce length normalization into the BT model. These adjustments culminate in the development of a new and simple loss function DMPO for multi-turn agent tasks. As shown in Figure 1, DMPO directly optimizes the RL objective by maximizing the likelihood of preferred ("win") trajectory over dis-preferred ("lose") trajectory. Notably, the SAOM constraint has advantages in mitigating compounding errors compared to the policy constraint (Xu et al., 2020; Ghasemipour et al., 2020). Furthermore, the derivation offers a theoretical rationale for the efficacy of the length normalization technique in DPO loss (Meng et al., 2024).
28	
29	To summarize, our contributions are threefold:
30	
31	- • We introduce a new loss function called DMPO, which directly optimizes RL objectives in multi-turn scenarios, thereby mitigating the compounding errors associated with BC methods.
32	- • We provide a theoretical explanation for the efficacy of the length normalization technique, illustrating how it cancels out the partition function in the BT model and improves performance.
33	- • Extensive experiments on three multi-turn agent task datasets validate the effectiveness and the superiority of the DMPO loss function.
34	
35	## 2 Related Work
36	
37	In this section, we first introduce the in-context learning methods and fine-tuning methods of language agents and then review the literature in preference-based RL.
38	
39	**In-Context Learning** Inspired by the superior in-context learning capabilities of LLMs (Achiam
40	
41	et al., 2023), researchers have designed various instruction prompts for LLMs, equipped with memory modules (Zhang et al., 2024), toolkits (Qu et al., 2024), and various workflows (Sumers et al., 2023), to build language agents for various real-world domains. ReAct (Yao et al., 2022b) incorporates CoT reasoning (Wei et al., 2022) into action generation. Reflexion (Shinn et al., 2024) and PROMST (Chen et al., 2024) refine the prompt using environment feedback. However, these in-context learning methods fail to fully exploit the potential of LLMs, since most LLMs are not specifically trained for agent tasks. This work focuses on adapting the LLMs to agent tasks through fine-tuning.
42	
43	**Agent Tuning** Recent studies, including FireAct (Chen et al., 2023), AgentTuning (Zeng et al., 2023), Lumos (Yin et al., 2023), MIMIR (Deng et al., 2024), AUTOACT (Qiao et al., 2024), and  $\alpha$ -UMi (Shen et al., 2024) supervised fine-tuning LLMs with self-instruct or expert trajectories. However, such BC approaches suffer from compounding errors when interacting with dynamic environments. Taking a step further, Pangu (Christianos et al., 2023) and CMAT (Liang et al., 2024) utilize RL technologies to further fine-tune the LLMs, which may result in a complex and unstable training procedure. To simplify the procedure, ETO (Song et al., 2024) and EMMA (Yang et al., 2024) directly employ the DPO loss (Rafailov et al., 2024b) to optimize the RL objective for the agent task. Nevertheless, the DPO loss is designed for single-turn bandit settings and is ill-suited for multi-turn scenarios. Along this line, this work extends the DPO loss in multi-turn scenarios and derives the DMPO loss.
44	
45	**Preference-Based RL** In multi-turn scenarios, preference-based RL typically starts by explicitly learning a reward function from preference data and then optimizing it (Fürnkranz et al., 2012; Christiano et al., 2017; Hejna III and Sadigh, 2023; Shin et al., 2021). However, this two-stage learning process presents challenges regarding training efficiency and instability. This work instead presents a single-stage policy learning approach using DMPO loss that directly optimizes a policy to satisfy preferences. While IPL (Hejna and Sadigh, 2024) and CPL (Hejna et al., 2023) share a similar idea with our work in eliminating the reward learning stage, their loss functions are limited to trajectory pairs of equal length, significantly restricting their applicability.### 3 Preliminary
46	
47	In this section, we present multi-turn agent task formulation and briefly introduce Direct Preference Optimization (DPO) loss.
48	
49	#### 3.1 Task Description
50	
51	The agent task can be formulated as a Markov decision process (MDP). A MDP is a 5-tuple  $(\mathcal{S}, \mathcal{A}, \mathcal{T}, \mathcal{R}, \gamma)$ , where  $\mathcal{S}$  denotes the state space,  $\mathcal{A}$  denotes action space,  $\mathcal{T}$  denotes dynamic transition function  $\mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S}$ ,  $\mathcal{R}$  denotes reward function  $\mathcal{S} \times \mathcal{A} \rightarrow [0, 1]$ , and  $\gamma \in [0, 1]$  is the discount factor. The goal for the agent is to choose actions at each time step that maximize the expected future discounted reward  $\mathbb{E} \left[ \sum_{t=0}^{T-1} \gamma^t r(s_t, a_t) \right]$ , where  $T$  is the trajectory length.
52	
53	In the language agent setting (Christianos et al., 2023), the state space and action space are both subsets of the language space. For the initial state  $s_0 \in \mathcal{S}$ , it contains the task instruction and prompt. At each time step  $t$ , LLMs generate action  $a_t$  according to the policy  $\pi_\theta(a_t|s_t)$  with the parameter  $\theta$ . Then the environment will return dynamic feedback  $o_t$  and transport the state into  $s_{t+1}$ . Note that the new state  $s_{t+1}$  is just a simple combination of  $s_t$ ,  $a_t$ , and  $o_t$ , and the trajectory  $\tau = (s_0, a_0, s_1, a_1, \dots, s_T, a_T)$ .
54	
55	#### 3.2 Direct Preference Optimization
56	
57	The aim of the DPO loss is to directly optimize RL objectives with KL divergence constraints on the policy function:
58	
59	$$\max_{\pi_\theta} \mathbb{E}_\tau \left[ \sum_{t=0}^{T-1} \gamma^t r(s_t, a_t) \right] - \beta \mathbb{D}_{KL}[\pi_\theta(a_t|s_t) || \pi_{ref}(a_t|s_t)], \quad (1)$$
60	
61	where  $\mathbb{E}$  is the expectation function,  $\mathbb{D}_{KL}[\cdot || \cdot]$  denotes the KL divergence between two distributions,  $\pi_{ref}$  denotes a reference policy, and the  $\beta$  is a parameter controlling the deviation from the base reference policy  $\pi_{ref}$ . The DPO loss is tailored for the single-turn preference alignment setting, where the trajectory length ( $T$ ) is limited to 1.
62	
63	Notably, the reward function is learned through the Bradley-Terry (BT) model (Bradley and Terry, 1952; Christiano et al., 2017):
64	
65	$$p(a_0^w \succ a_0^l | s_0) = \frac{\exp(r(s_0, a_0^w))}{\exp(r(s_0, a_0^w)) + \exp(r(s_0, a_0^l))}, \quad (2)$$
66	
67	which gives the probability that the “win” action  $a_0^w$  is preferred to the “lose” action  $a_0^l$  given the state  $s_0$ .
68	
69	Then DPO leverages the established closed-form solution for the single-turn formulation of the reinforcement learning problem in Eq (1) presented in (Ziebart et al., 2008; Ziebart, 2010):
70	
71	$$\pi^*(a|s) = \frac{1}{Z(s)} \pi_{ref}(a|s) e^{r(s,a)}, \quad (3)$$
72	
73	where  $\pi^*$  denotes the optimal policy and  $Z(s)$  denotes the partition function that normalizes it. We can easily rearrange Eq (3) and substitute it into Eq (2) to get the BT model over policy:
74	
75	$$p(a_0^w \succ a_0^l | s_0) = \sigma \left( \beta \log \frac{\pi_\theta(a_0^w | s_0)}{\pi_{ref}(a_0^w | s_0)} - \beta \log \frac{\pi_\theta(a_0^l | s_0)}{\pi_{ref}(a_0^l | s_0)} \right), \quad (4)$$
76	
77	where the partition function  $Z(s)$  is canceled from the BT model and  $\sigma$  is the sigmoid function. The DPO loss obtains the optimal policy  $\pi_\theta^*$  by maximizing the likelihood:
78	
79	$$\mathcal{L}_{DPO} = -\mathbb{E}_{(s_0, a_0^w, a_0^l) \sim D} \log \left[ p(a_0^w \succ a_0^l | s_0) \right], \quad (5)$$
80	
81	where  $D$  represents the preference dataset. Nonetheless, such concise and elegant derivations are only suitable for single-turn preference optimization tasks. As shown in Eq (3), the partition function  $Z(s)$  is dependent on the current state  $s$ , which precludes its cancellation under the policy constraint in the multi-turn setting.
82	
83	### 4 Method
84	
85	In this section, we will outline the definition and benefits of the state-action occupancy measure. Subsequently, we will introduce two adjustments to derive the DMPO loss. Finally, we will delve deeper into the analysis of the DMPO loss.
86	
87	#### 4.1 State-Action Occupancy Measure
88	
89	The discounted state-action occupancy measure  $d^\pi(s, a)$  of a policy  $\pi$  describes the distribution of state-action pairs that an agent visits in the space with policy  $\pi$ :
90	
91	$$d^\pi(s, a) = \frac{1 - \gamma}{1 - \gamma^T} \sum_{t=0}^{T-1} \gamma^t \mathbb{P}(s_t = s, a_t = a | \pi), \quad (6)$$Figure 2: Illustration of expert trajectories and trajectories learned under the constraints of policy and state-action occupancy measure.
92	
93	where  $\mathbb{P}(\cdot)$  denotes the probability and the coefficient  $(1 - \gamma)/(1 - \gamma^T)$  is used to normalize the probability distribution.
94	
95	First, we will provide an intuitive explanation of how the SAOM constraint can reduce the compounding error. In imitation learning, the conventional SFT learning objective aims to minimize the KL divergence between the expert policy and the current policy:
96	
97	$$\begin{aligned} & \min_{\pi_{\theta}} \mathbb{E}_{(s,a) \sim d^E} [\mathbb{D}_{KL}(\pi_E(a|s) || \pi_{\theta}(a|s))] \\ &= - \max_{\pi_{\theta}} \mathbb{E}_{(s,a) \sim d^E} [\log(\pi_{\theta}(a|s))], \end{aligned} \quad (7)$$
98	
99	where  $\pi_E$  is the expert policy and  $d^E$  is the SAOM with policy  $\pi_E$ . As shown in Figure 2, the trajectories learned under policy constraints are susceptible to significant compounding error. This vulnerability stems from the fact that expert datasets are unable to comprehensively cover all possible states. Consequently, the SFT loss leads the model to choose random actions in states that are not represented in the expert datasets. As a result, the model gradually deviates from the expert trajectories after the initial error, illustrating the phenomenon known as compounding error.
100	
101	To alleviate the compounding error, subsequent imitation learning research such as (Abbeel and Ng, 2004; Ghasemipour et al., 2020; Ho and Ermon, 2016) employ the SAOM constraint:
102	
103	$$\min_{\pi_{\theta}} \mathbb{E}_{(s,a) \sim d^E} [\mathbb{D}_{(\cdot)}(d^{\pi_{\theta}}(a|s) || d^{\pi_E}(a|s))], \quad (8)$$
104	
105	where different approaches utilize different distribution distance measures  $\mathbb{D}_{(\cdot)}$ . The strength of SAOM constraint lies in its ability to steer action selection towards distributions that closely mimic expert state-action pairs, especially in unexplored states within the expert datasets. Illustrated in Figure 2, at state  $s_2$ , policy constraints lead the model to choose actions uniformly, whereas SAOM constraints aim to lead the model toward actions that
106	
107	bring the next state back onto the expert trajectory. This effectively mitigates compounding errors and enhances the cumulative reward.
108	
109	## 4.2 DMPO
110	
111	Inspired by imitation learning, we substitute the policy constraint with the SAOM constraint in Eq (1) and get the following RL objective:
112	
113	$$\begin{aligned} & \max_{\pi_{\theta}} \mathbb{E}_{(s,a) \sim d^{\pi_{\theta}}(s,a)} [r(s, a)] \\ & - \beta \mathbb{D}_{KL}[d^{\pi_{\theta}}(s, a) || d^{\pi_{ref}}(s, a)], \end{aligned} \quad (9)$$
114	
115	where  $\pi_{ref}$  represents the reference policy. Similar to (Rafailov et al., 2024b), it is straightforward to show that the optimal solution to the RL objective in Eq (9) takes the form:
116	
117	$$d^{\pi^*}(s, a) = \frac{1}{Z} d^{\pi_{ref}}(s, a) \exp\left(\frac{1}{\beta} r(s, a)\right), \quad (10)$$
118	
119	where  $\pi^*$  represents the optimal policy,  $Z$  is the partition function that normalizes the probability. It's noteworthy that as  $d^{\pi}(s, a)$  is a function of  $(s, a)$  pairs, normalizing it results in the partition functions  $Z$  being independent of the current state  $s$ . Consequently,  $Z$  remains constant for all  $(s, a)$  pairs, providing us with the opportunity to eliminate them. Easily, we can rearrange Eq (10) into:
120	
121	$$r(s, a) = \beta \log \frac{d^{\pi^*}(s, a)}{d^{\pi_{ref}}(s, a)} + \beta \log Z. \quad (11)$$
122	
123	Similar to Eq (2), we learn the reward function for multi-turn scenarios through the BT model:
124	
125	$$\begin{aligned} & p(\tau^w \succ \tau^l | s_0) = \\ & \sigma \left( \sum_{t=0}^{T_w-1} \gamma^t r(s_t^w, a_t^w) - \sum_{t=0}^{T_l-1} \gamma^t r(s_t^l, a_t^l) \right), \end{aligned} \quad (12)$$
126	
127	where  $\tau^w$  and  $\tau^l$  represent the "win" and "lose" trajectories respectively,  $T_w$  and  $T_l$  represent the "win" and "loss" trajectory length respectively. However, since  $T^w \neq T^l$ , the partition function  $Z$  cannot be canceled directly in Eq (12).
128	
129	To overcome this obstacle, we introduce the length normalization technique to Eq (12):
130	
131	$$\begin{aligned} p(\tau^w \succ \tau^l | s_0) &= \sigma \left( \frac{1 - \gamma}{1 - \gamma^{T_w}} \sum_{t=0}^{T_w-1} \gamma^t r(s_t^w, a_t^w) \right. \\ &\quad \left. - \frac{1 - \gamma}{1 - \gamma^{T_l}} \sum_{t=0}^{T_l-1} \gamma^t r(s_t^l, a_t^l) \right). \end{aligned} \quad (13)$$In this way, we can eliminate the partition function  $Z$  in Eq (13) by substituting the reward function  $r(s, a)$  in Eq (11). Then we maximize the likelihood and obtain:
132	
133	$$L_{DMPO} = -\mathbb{E}_{(s_0, \tau^w, \tau^l) \sim D} \log \sigma \left[ \frac{1 - \gamma}{1 - \gamma^{T_w}} \sum_{t=0}^{T_w-1} \beta \gamma^t \log \frac{d^{\pi_\theta}(s_t^w, a_t^w)}{d^{\pi_{ref}}(s_t^w, a_t^w)} - \frac{1 - \gamma}{1 - \gamma^{T_l}} \sum_{t=0}^{T_l-1} \beta \gamma^t \log \frac{d^{\pi_\theta}(s_t^l, a_t^l)}{d^{\pi_{ref}}(s_t^l, a_t^l)} \right], \quad (14)$$
134	
135	where the  $d^\pi(s_t, a_t)$  can be further written as:
136	
137	$$d^\pi(s = s_t^w, a = a_t^w) = \gamma^t \cdot P(s_0) \prod_{k=0}^{t-1} \pi(a_k^w | s_k^w) P(s_{k+1}^w | s_k^w, a_k^w), \quad (15)$$
138	
139	where  $P(s_0)$  represents the probability of the initial state  $s_0$  and  $P(s_{k+1} | s_k, a_k)$  denotes the transition functions. In general, obtaining the SAOM  $d^\pi(s_t, a_t)$  is challenging because we do not know the transition function  $P(s_{k+1} | s_k, a_k)$  in dynamic environments. However, in Eq (14) we simply calculate the ratio between the current SAOM  $d^{\pi_\theta}(s_t, a_t)$  and the reference SAOM  $d^{\pi_{ref}}(s_t, a_t)$ . It is important to note that the transition function remains consistent for both, allowing for cancellation. By substituting the Eq (15) into Eq (14), we can obtain the DMPO loss function:
140	
141	$$L_{DMPO} = -\mathbb{E}_{(s_0, \tau^w, \tau^l) \sim D} \log \sigma \left[ \sum_{t=0}^{T_w-1} \beta \phi(t, T_w) \log \frac{\pi_\theta(a_t^w | s_t^w)}{\pi_{ref}(a_t^w | s_t^w)} - \sum_{t=0}^{T_l-1} \beta \phi(t, T_l) \log \frac{\pi_\theta(a_t^l | s_t^l)}{\pi_{ref}(a_t^l | s_t^l)} \right], \quad (16)$$
142	
143	where the discount function  $\phi(t, T) = \gamma^t \cdot (1 - \gamma^{T-t}) / (1 - \gamma^T)$ . It's noteworthy that DMPO reweights state-action pairs at various steps using a discount function  $\phi(t, T)$ .
144	
145	### 4.3 In-Depth Analysis
146	
147	In this subsection, we will explore the advantages of the DMPO loss and present some lemmas and observations.
148	
149	**Corollary 4.0.1.** *The DMPO loss assigns higher weights to state-action pairs at early steps, where the weight is related to discount factor  $\gamma$ .*
150	
151	*Proof.* To prove the lemma, we analyze the gradient of the loss function  $L_{DMPO}$  according to  $\theta$ :
152	
153	$$\nabla_\theta L_{DMPO} = -\mathbb{E}_{(s_0, \tau^w, \tau^l) \sim D} \sigma [\Phi(\tau^l) - \Phi(\tau^w)] \left[ \sum_{t=0}^{T_w-1} \beta \phi(t, T_w) \nabla_\theta \log \pi_\theta(a_t^w | s_t^w) - \sum_{t=0}^{T_l-1} \beta \phi(t, T_l) \nabla_\theta \log \pi_\theta(a_t^l | s_t^l) \right], \quad (17)$$
154	
155	where function  $\Phi(\tau) = \sum_{t=0}^{T-1} \beta \phi(t, T) \log \frac{\pi_\theta(a_t | s_t)}{\pi_{ref}(a_t | s_t)}$  and  $\phi(t, T) = \gamma^t \cdot (1 - \gamma^{T-t}) / (1 - \gamma^T)$ . The discount function  $\phi(t, T)$  decreases as  $t$  increases and is related to the discounted factor  $\gamma$ . This completes the proof.  $\square$
156	
157	**Corollary 4.0.2.** *The DMPO loss degenerates into the single-turn DPO loss when the discount factor  $\gamma$  approaches zero.*
158	
159	*Proof.* When  $\gamma$  equals 0, the function  $\phi(t, T)$  is 1 at  $t = 0$ , and 0 otherwise, which is equivalent to a single-turn DPO loss.  $\square$
160	
161	Based on the analysis above, we have the following observations:
162	
163	**Observation 4.0.1.** *Similar to the DPO loss, the DMPO loss increases the likelihood of the preferred trajectories  $\tau_w$  and decreases the likelihood of the dispreferred trajectories  $\tau_l$ .*
164	
165	**Observation 4.0.2.** *If the reward  $\Phi(\tau_l)$  of dispreferred trajectory is estimated higher by the policy  $\pi_\theta$ , the weight  $\sigma [\Phi(\tau^l) - \Phi(\tau^w)]$  will be larger.*
166	
167	**Length Normalization Explanation** In SimPO (Meng et al., 2024), the effectiveness of the length normalization technique was empirically demonstrated. However, a theoretical explanation was not provided. Our derivation shows that it assists in eliminating the partition function. Without length normalization in Eq (13), a length-dependent bias term arises in the BT model, degrading model performance as the disparity in trajectory lengths between preferred and dispreferred samples increases.
168	
169	**Further Discussion** As discussed in Section 4.2, the optimal solution to the RL objective in Eq (9) takes the form shown in Eq (10). However, it is contended that achieving the optimal solution may not always be feasible when dealing with an arbitrary reward function  $r(s, a)$  within the context of&lt;table border="1">
170	&lt;thead>
171	&lt;tr>
172	&lt;th>Dataset&lt;/th>
173	&lt;th>WebShop&lt;/th>
174	&lt;th>ScienceWorld&lt;/th>
175	&lt;th>ALFWorld&lt;/th>
176	&lt;/tr>
177	&lt;/thead>
178	&lt;tbody>
179	&lt;tr>
180	&lt;td>Train&lt;/td>
181	&lt;td>1938&lt;/td>
182	&lt;td>1483&lt;/td>
183	&lt;td>3321&lt;/td>
184	&lt;/tr>
185	&lt;tr>
186	&lt;td>Test-Seen&lt;/td>
187	&lt;td>200&lt;/td>
188	&lt;td>194&lt;/td>
189	&lt;td>140&lt;/td>
190	&lt;/tr>
191	&lt;tr>
192	&lt;td>Test-Unseen&lt;/td>
193	&lt;td>-&lt;/td>
194	&lt;td>241&lt;/td>
195	&lt;td>134&lt;/td>
196	&lt;/tr>
197	&lt;/tbody>
198	&lt;/table>
199	
200	Table 1: Statistics of three agent datasets. “Train”, “Test-Seen”, and “Test-Unseen” refer to the number of tasks in each set respectively.
201	
202	a language agent setting. This limitation arises due to the definition of the new state  $s_{t+1}$  as a composite of  $s_t$ ,  $a_t$ , and  $o_t$ , which introduces an inherent constraint on the transition function between states. In general, in multi-turn dynamic environments, no loss function can rigorously optimize the RL objective, and the DMPO loss serves as a good approximation. In many cases, the DMPO loss can precisely optimize the RL objective in Eq (9).
203	
204	## 5 Experiments
205	
206	In this section, we conduct extensive experiments on three agent tasks to demonstrate the effectiveness of the proposed DMPO loss function. Our experiments aim to address the following questions:
207	
208	- • **RQ1:** Can the DMPO loss function exhibit robustness to noisy training trajectories data and mitigate compounding errors?
209	- • **RQ2:** How does the DMPO loss function perform compared to other baselines?
210	- • **RQ3:** What is the impact of the discount factor  $\gamma$  and the trajectory length on the DMPO loss?
211	
212	### 5.1 Experiment Setting
213	
214	**Datasets** Following prior work (Song et al., 2024), we conduct experiments on three representative agent datasets, including WebShop (Yao et al., 2022a), ScienceWorld (Wang et al., 2022), and ALFWorld (Shridhar et al., 2020b).
215	
216	- • WebShop is a simulated shopping website environment where agents find and purchase products according to specifications provided in a natural language instruction. The final reward  $r \in [0, 1]$  is calculated based on how closely the purchased products match the specified criteria.
217	- • ScienceWorld is an interactive text environment that tests agents’ scientific reasoning abilities in elementary science experiments with 10 task types. The final reward  $r \in [0, 1]$  is computed based on the number of subgoals the agent successfully accomplishes within each task.
218	- • ALFWorld is a simulated text-based environment
219	
220	that enables agents to complete embodied household tasks from the ALFRED benchmark (Shridhar et al., 2020a). The final binary rewards signify the completion status of the task.
221	
222	All three environments can be formally described as MDP and conducted by language agents. The statistical details of our datasets are outlined in Table 1. Following (Song et al., 2024), in addition to the in-distribution “seen” test sets, both ScienceWorld and ALFWorld include “unseen” test sets that include out-of-distribution tasks. These additional test sets enable us to evaluate the generalization capabilities of different agents.
223	
224	**Training Setting** We assess the robustness and effectiveness of the DMPO loss function by employing two distinct training scenarios: Noisy setting and Clean setting. Following (Song et al., 2024), we adopt the experts’ trajectories as the “win” trajectories to form preference trajectory data in both noisy setting and clean setting. Initially, we utilize the LLMs, which have been fine-tuned with expert trajectories, to generate new trajectories on the training set. We observe that the LLMs have a tendency to generate trajectories with repeated actions or meaningless words. In the noisy setting, these noisy trajectories are used as “lose” trajectories for preference data. Conversely, in the Clean setting, we eliminate the noisy trajectories and employ the remaining ones as “lose” trajectories for preference data.
225	
226	**Parameter Settings** In this work, we utilize two different base models Llama-2-7B-Chat (Touvron et al., 2023) and Mistral-7B-Instruct-v0.2 (Jiang et al., 2023) to build language agents. Following (Song et al., 2024), we utilize the AdamW optimizer. When supervised fine-tuning the base models to get the reference model, we set the batch size to 64. The learning rate is selected from  $\{1e-5, 2e-5, 3e-5\}$  with 3% warm up and a cosine scheduler. When refining the agents with DMPO loss function, we set the batch size to 32 and tune the hyperparameters  $\beta$  and  $\gamma$  within the ranges of  $\{0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9\}$  and  $\{0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99\}$  respectively. We conduct all experiments on 8 NVIDIA A100 GPUs.
227	
228	**Evaluation Setting** Following (Song et al., 2024), we evaluate all methods using the ReAct-style interaction format (Yao et al., 2022b), which generates both reasoning traces and actions in an in-&lt;table border="1">
229	&lt;thead>
230	&lt;tr>
231	&lt;th rowspan="2">Method&lt;/th>
232	&lt;th rowspan="2">WebShop&lt;/th>
233	&lt;th colspan="2">ScienceWorld&lt;/th>
234	&lt;th colspan="2">ALFWorld&lt;/th>
235	&lt;/tr>
236	&lt;tr>
237	&lt;th>Seen&lt;/th>
238	&lt;th>Unseen&lt;/th>
239	&lt;th>Seen&lt;/th>
240	&lt;th>Unseen&lt;/th>
241	&lt;/tr>
242	&lt;/thead>
243	&lt;tbody>
244	&lt;tr>
245	&lt;td>Llama-2-7B-Chat + DPO&lt;/td>
246	&lt;td>0.641 &lt;math>\pm&lt;/math> 0.002&lt;/td>
247	&lt;td>0.601 &lt;math>\pm&lt;/math> 0.004&lt;/td>
248	&lt;td>0.576 &lt;math>\pm&lt;/math> 0.001&lt;/td>
249	&lt;td>&lt;b>0.474&lt;/b> &lt;math>\pm&lt;/math> 0.004&lt;/td>
250	&lt;td>0.540 &lt;math>\pm&lt;/math> 0.005&lt;/td>
251	&lt;/tr>
252	&lt;tr>
253	&lt;td>Llama-2-7B-Chat + DMPO&lt;/td>
254	&lt;td>&lt;b>0.666&lt;/b> &lt;math>\pm&lt;/math> 0.007&lt;/td>
255	&lt;td>&lt;b>0.619&lt;/b> &lt;math>\pm&lt;/math> 0.003&lt;/td>
256	&lt;td>&lt;b>0.584&lt;/b> &lt;math>\pm&lt;/math> 0.005&lt;/td>
257	&lt;td>0.433 &lt;math>\pm&lt;/math> 0.004&lt;/td>
258	&lt;td>&lt;b>0.550&lt;/b> &lt;math>\pm&lt;/math> 0.004&lt;/td>
259	&lt;/tr>
260	&lt;tr>
261	&lt;td>Mistral-7B-Instructv0.2 + DPO&lt;/td>
262	&lt;td>0.637 &lt;math>\pm&lt;/math> 0.007&lt;/td>
263	&lt;td>0.700 &lt;math>\pm&lt;/math> 0.003&lt;/td>
264	&lt;td>0.629 &lt;math>\pm&lt;/math> 0.008&lt;/td>
265	&lt;td>&lt;b>0.745&lt;/b> &lt;math>\pm&lt;/math> 0.004&lt;/td>
266	&lt;td>0.883 &lt;math>\pm&lt;/math> 0.004&lt;/td>
267	&lt;/tr>
268	&lt;tr>
269	&lt;td>Mistral-7B-Instructv0.2 + DMPO&lt;/td>
270	&lt;td>&lt;b>0.643&lt;/b> &lt;math>\pm&lt;/math> 0.008&lt;/td>
271	&lt;td>&lt;b>0.708&lt;/b> &lt;math>\pm&lt;/math> 0.015&lt;/td>
272	&lt;td>&lt;b>0.651&lt;/b> &lt;math>\pm&lt;/math> 0.004&lt;/td>
273	&lt;td>0.742 &lt;math>\pm&lt;/math> 0.012&lt;/td>
274	&lt;td>&lt;b>0.888&lt;/b> &lt;math>\pm&lt;/math> 0.000&lt;/td>
275	&lt;/tr>
276	&lt;/tbody>
277	&lt;/table>
278	
279	Table 2: Noisy setting: The average reward of different base LLMs on three agent datasets. "Seen" denotes in-distribution test sets, while "Unseen" denotes out-of-distribution test sets. The results are averaged with three distinct random seeds. The best results for each base model are highlighted in bold.
280	
281	&lt;table border="1">
282	&lt;thead>
283	&lt;tr>
284	&lt;th rowspan="2">Method&lt;/th>
285	&lt;th rowspan="2">WebShop&lt;/th>
286	&lt;th colspan="2">ScienceWorld&lt;/th>
287	&lt;/tr>
288	&lt;tr>
289	&lt;th>Seen&lt;/th>
290	&lt;th>Unseen&lt;/th>
291	&lt;/tr>
292	&lt;/thead>
293	&lt;tbody>
294	&lt;tr>
295	&lt;td>GPT-4*&lt;/td>
296	&lt;td>0.632&lt;/td>
297	&lt;td>0.648&lt;/td>
298	&lt;td>0.644&lt;/td>
299	&lt;/tr>
300	&lt;tr>
301	&lt;td>GPT-3.5-Turbo*&lt;/td>
302	&lt;td>0.624&lt;/td>
303	&lt;td>0.165&lt;/td>
304	&lt;td>0.130&lt;/td>
305	&lt;/tr>
306	&lt;tr>
307	&lt;td>Base*&lt;/td>
308	&lt;td>0.179&lt;/td>
309	&lt;td>0.380&lt;/td>
310	&lt;td>0.310&lt;/td>
311	&lt;/tr>
312	&lt;tr>
313	&lt;td>Best-of-N*&lt;/td>
314	&lt;td>0.638&lt;/td>
315	&lt;td>0.702&lt;/td>
316	&lt;td>0.576&lt;/td>
317	&lt;/tr>
318	&lt;tr>
319	&lt;td>RFT*&lt;/td>
320	&lt;td>0.636&lt;/td>
321	&lt;td>0.716&lt;/td>
322	&lt;td>0.543&lt;/td>
323	&lt;/tr>
324	&lt;tr>
325	&lt;td>PPO*&lt;/td>
326	&lt;td>0.642&lt;/td>
327	&lt;td>0.594&lt;/td>
328	&lt;td>0.517&lt;/td>
329	&lt;/tr>
330	&lt;tr>
331	&lt;td>SFT&lt;/td>
332	&lt;td>0.631&lt;/td>
333	&lt;td>0.568&lt;/td>
334	&lt;td>0.560&lt;/td>
335	&lt;/tr>
336	&lt;tr>
337	&lt;td>ETO&lt;/td>
338	&lt;td>0.698 &lt;math>\pm&lt;/math> 0.003&lt;/td>
339	&lt;td>0.685 &lt;math>\pm&lt;/math> 0.004&lt;/td>
340	&lt;td>0.611 &lt;math>\pm&lt;/math> 0.003&lt;/td>
341	&lt;/tr>
342	&lt;tr>
343	&lt;td>DMPO&lt;/td>
344	&lt;td>&lt;b>0.701&lt;/b> &lt;math>\pm&lt;/math> 0.003&lt;/td>
345	&lt;td>&lt;b>0.724&lt;/b> &lt;math>\pm&lt;/math> 0.005&lt;/td>
346	&lt;td>&lt;b>0.617&lt;/b> &lt;math>\pm&lt;/math> 0.002&lt;/td>
347	&lt;/tr>
348	&lt;/tbody>
349	&lt;/table>
350	
351	Table 3: Clean setting: The average reward of different methods on two agent datasets based on Llama-2-7B-Chat. The best results of tuning methods are highlighted in bold. \*Results are taken from (Song et al., 2024).
352	
353	terleaved manner. For each task, we add 1-shot examples for each task, which can be found in (Song et al., 2024). Unless otherwise stated, we set the decoding generate temperature as 0.0.
354	
355	## 5.2 Noisy Setting Results (RQ1)
356	
357	In the noisy setting, we utilize the noisy trajectories as "lose" trajectories for preference data to investigate the robustness of the DMPO loss function. As shown in Table 2, we evaluate the DMPO loss function with two different base models on two representative agent tasks and observe that:
358	
359	- • In all Unseen test sets and most Seen test sets for both base models, the DMPO loss function outperforms the DPO loss function. This superiority stems from DMPO assigning greater importance to initial state-action pairs, prioritizing high-quality expert actions from the early stages, and reducing the influence of noisy "lose" actions in later stages. This mitigates the influence of noise, endowing the model with enhanced generalization capabilities. Meanwhile, the DPO loss is not appropriate for multi-turn settings and cannot cancel out the partition function in the BT model, thereby resulting in its inferior performance.
360	- • The performance of Mistral-7B-Instruct-v0.2 is
361	
362	significantly better than that of Llama-2-7B-Chat on ScienceWorld and ALFWorld. This observation suggests a positive correlation between the effectiveness of the base model and its performance enhancement after fine-tuning for agent tasks using the DMPO loss function.
363	
364	## 5.3 Clean Setting Results (RQ2)
365	
366	In clean setting, we filter out the noisy trajectories and select high-quality trajectories as the "lose" trajectories for preference data, enabling us to utilize the DMPO loss function fully.
367	
368	**Baselines** Following (Song et al., 2024), we compare our models trained by DMPO loss function with the following representative baselines. 1) Base: default LLM without tuning. 2) SFT: LLM fine-tuned through supervised learning on expert trajectories. 3) Best-of-N: This approach involves using an SFT-based agent for sampling and selecting the trajectory with the highest reward out of N samples. Here, N is specified as 10. 4) RFT (Rejection sampling Fine-Tuning) (Yuan et al., 2023): This approach augments the expert trajectory dataset by incorporating successful trajectories and subsequently trains the agent on the augmented dataset. 5) PPO (Proximal Policy Optimization) (Schulman et al., 2017) directly optimize RL objectives to maximize the cumulative rewards. 6) ETO (Exploration-based Trajectory Optimization) (Song et al., 2024) iteratively explores the environment to enhance the training preference data and utilizes DPO loss to learn from preference data.
369	
370	**Results** Based on the Llama-2-7B-Chat model, we show the comparison results under clean setting in Table 3. Notably, we observe that:
371	
372	- • All fine-tuning methods significantly outperform the base model on both datasets, with improvements of at least 49%. On Webshop, they even surpass the performance of advanced closed-source LLMs. This underscores the significant gap be-Figure 3: The effect of hyperparameter  $\gamma$  on the relative performance of the model trained with DMPO loss on the WebShop dataset in both noisy and clean settings.
373	
374	tween the pre-training tasks of LLMs and the agent tasks. By fine-tuning LLMs, language agents exhibit substantial potential for improvement.
375	
376	- • The model trained using DMPO loss achieved optimal performance on both datasets, highlighting the effectiveness of DMPO loss in learning from preference data. The improvement over the SFT model suggests that DMPO reduces the compounding errors, resulting in higher rewards.
377	- • The model trained using DMPO loss exhibits substantial performance improvements compared to the noisy setting, achieving an average increase of 5.2% on Webshop and 11.3% on ScienceWorld. This highlights the importance of selecting high-quality "lose" trajectories in constructing preference data, as opting for such trajectories yields superior performance.
378	
379	#### 5.4 Ablation Study (RQ3)
380	
381	**Hyperparameter Analysis** To verify the impact of reweight function  $\phi(t, T)$  in Eq (17), we tune the the hyperparameter  $\gamma$  on WebShop and present the results in Figure 3. Our findings reveal that both base models achieve optimal performance with a smaller  $\gamma$  in the noisy setting and a larger  $\gamma$  in the clean setting. According to Eq (17), a smaller  $\gamma$  implies that the DMPO loss assigns reduced weight to the state-action pairs in later steps. This indicates that DMPO can balance the impact of noise by adjusting the parameter  $\gamma$ . When faced with noisy "loss" trajectories, selecting a smaller  $\gamma$  can
382	
383	Figure 4: The effect of "loss" trajectories length on the performance of the model trained with DPO and DMPO loss in the noisy setting on ScienceWorld. The base model is Mistral-7B-Instruct-v0.2.
384	
385	help alleviate noise impact. Conversely, when dealing with high-quality "loss" trajectories, a larger gamma can be selected to better learn strategies from the state-action pairs in later steps.
386	
387	**Length Analysis** To examine the impact of trajectory length on model performance, we conducted an experiment by categorizing the noisy trajectories into three groups based on their maximum length. We ensure that the number of preference data in each group is the same. As shown in Figure 4, we observe that the performance of the model trained with DPO loss function decreases rapidly as the length of noisy "loss" trajectories increases. In contrast, the model trained with the DMPO loss function exhibits robustness against noisy "loss" trajectory length. This is attributed to the length normalization employed in the DMPO loss, which mitigates the influence of inconsistent lengths between "win" and "lose" trajectories.
388	
389	## 6 Conclusion
390	
391	In this work, we propose a simple and robust loss function DMPO loss, which directly optimizes the RL objective for multi-turn agent tasks. By substituting the policy constraint with the SAOM constraint and introducing the length normalization into BT model, we eliminate the partition function in the BT model and derive the DMPO loss function. The SAOM constraint has played a pivotal role in mitigating compounding errors. Meanwhile, this derivation offers a theoretical rationale for the efficacy of the length normalization technique. Extensive experiments on three agent datasets demonstrate the effectiveness of DMPO loss, highlighting its capability to reduce compounding errors and its resilience to trajectory length disparity.## 7 Limitation
392	
393	This paper primarily focuses on issues when fine-tuning LLMs on the agent tasks and derives a simple and robust loss function. However, our study has several limitations: 1) We solely concentrate on turn-wise task formulation which results in sparse rewards for LLMs. Exploring token-wise task formulation as suggested in (Rafailov et al., 2024a) would be a valuable avenue for future investigation. 2) The experiments in this work are conducted using 7B-sized models on simulated datasets. Future experiments on larger models and datasets can provide stronger validation of our conclusions.
394	
395	## 8 Ethical Considerations
396	
397	In this paper, we present a new DMPO loss function for refining LLMs in agent tasks, without bringing forth additional ethical dilemmas. We utilize publicly accessible data while conscientiously steering clear of sensitive information. Additionally, the use of LLMs could perpetuate unnoticed societal biases. We suggest thorough risk assessments and advise users to be mindful of the potential risks linked to model deployment.
398	
399	## 9 Acknowledgments
400	
401	This work is supported by the National Natural Science Foundation of China (62272437). This research was also supported by the advanced computing resources provided by the Supercomputing Center of the USTC.
402	
403	## References
404	
405	Pieter Abbeel and Andrew Y Ng. 2004. Apprenticeship learning via inverse reinforcement learning. In *Proceedings of the twenty-first international conference on Machine learning*, page 1.
406	
407	Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. 2023. Gpt-4 technical report. *arXiv preprint arXiv:2303.08774*.
408	
409	Ralph Allan Bradley and Milton E. Terry. 1952. [Rank analysis of incomplete block designs: I. the method of paired comparisons](#). *Biometrika*, 39(3/4):324–345.
410	
411	Baian Chen, Chang Shu, Ehsan Shareghi, Nigel Collier, Karthik Narasimhan, and Shunyu Yao. 2023. Fireact: Toward language agent fine-tuning. *arXiv preprint arXiv:2310.05915*.
412	
413	Yongchao Chen, Jacob Arkin, Yilun Hao, Yang Zhang, Nicholas Roy, and Chuchu Fan. 2024. Prompt optimization in multi-step tasks (promst): Integrating human feedback and preference alignment. *arXiv preprint arXiv:2402.08702*.
414	
415	Paul F Christiano, Jan Leike, Tom Brown, Miljan Marćić, Shane Legg, and Dario Amodei. 2017. Deep reinforcement learning from human preferences. *Advances in neural information processing systems*, 30.
416	
417	Filippos Christianos, Georgios Papoudakis, Matthieu Zimmer, Thomas Coste, Zhihao Wu, Jingxuan Chen, Khyati Khandelwal, James Doran, Xidong Feng, Jiacheng Liu, et al. 2023. Pangu-agent: A fine-tunable generalist agent with structured reasoning. *arXiv preprint arXiv:2312.14878*.
418	
419	Chunyuan Deng, Xiangru Tang, Yilun Zhao, Hanming Wang, Haoran Wang, Wangchunshu Zhou, Arman Cohan, and Mark Gerstein. 2024. Mimir: A streamlined platform for personalized agent tuning in domain expertise. *arXiv preprint arXiv:2404.04285*.
420	
421	Johannes Fürnkranz, Eyke Hüllermeier, Weiwei Cheng, and Sang-Hyeun Park. 2012. Preference-based reinforcement learning: a formal framework and a policy iteration algorithm. *Machine learning*, 89:123–156.
422	
423	Seyed Kamyar Seyed Ghasemipour, Richard Zemel, and Shixiang Gu. 2020. A divergence minimization perspective on imitation learning methods. In *Conference on robot learning*, pages 1259–1277. PMLR.
424	
425	Joey Hejna, Rafael Rafailov, Harshit Sikchi, Chelsea Finn, Scott Niekum, W Bradley Knox, and Dorsa Sadigh. 2023. Contrastive preference learning: Learning from human feedback without rl. *arXiv preprint arXiv:2310.13639*.
426	
427	Joey Hejna and Dorsa Sadigh. 2024. Inverse preference learning: Preference-based rl without a reward function. *Advances in Neural Information Processing Systems*, 36.
428	
429	Donald Joseph Hejna III and Dorsa Sadigh. 2023. Few-shot preference learning for human-in-the-loop rl. In *Conference on Robot Learning*, pages 2014–2025. PMLR.
430	
431	Jonathan Ho and Stefano Ermon. 2016. Generative adversarial imitation learning. *Advances in neural information processing systems*, 29.
432	
433	Wenlong Huang, Pieter Abbeel, Deepak Pathak, and Igor Mordatch. 2022. Language models as zero-shot planners: Extracting actionable knowledge for embodied agents. In *International conference on machine learning*, pages 9118–9147. PMLR.
434	
435	Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de Las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Léo Renaud Lavaud, Marie-Anne Lachaux, Pierre Stock,Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. 2023. Mistral 7b. *CoRR*, abs/2310.06825.
436	
437	Jeffrey D. Johnson, Jinghong Li, and Zengshi Chen. 2000. Reinforcement learning: An introduction: R.S. Sutton, A.G. Barto, MIT press, Cambridge, MA 1998, 322 pp. ISBN 0-262-19398-1. *Neurocomputing*, 35(1-4):205–206.
438	
439	Xuechen Liang, Meiling Tao, Tianyu Shi, and Yiting Xie. 2024. Cmat: A multi-agent collaboration tuning framework for enhancing small language models. *arXiv preprint arXiv:2404.01663*.
440	
441	Yu Meng, Mengzhou Xia, and Danqi Chen. 2024. [Simpo: Simple preference optimization with a reference-free reward](#). *Preprint*, arXiv:2405.14734.
442	
443	Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. 2022. Training language models to follow instructions with human feedback. *Advances in neural information processing systems*, 35:27730–27744.
444	
445	Dean A Pomerleau. 1991. Efficient training of artificial neural networks for autonomous navigation. *Neural computation*, 3(1):88–97.
446	
447	Shuofei Qiao, Ningyu Zhang, Runnan Fang, Yujie Luo, Wangchunshu Zhou, Yuchen Eleanor Jiang, Chengfei Lv, and Huajun Chen. 2024. Autoact: Automatic agent learning from scratch via self-planning. *arXiv preprint arXiv:2401.05268*.
448	
449	Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, and Ji-Rong Wen. 2024. [Tool learning with large language models: A survey](#). *Preprint*, arXiv:2405.17935.
450	
451	Rafael Rafailov, Joey Hejna, Ryan Park, and Chelsea Finn. 2024a. From  $r$  to  $q^*$ : Your language model is secretly a  $q$ -function. *arXiv preprint arXiv:2404.12358*.
452	
453	Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. 2024b. Direct preference optimization: Your language model is secretly a reward model. *Advances in Neural Information Processing Systems*, 36.
454	
455	Scott E. Reed, Konrad Zolna, Emilio Parisotto, Sergio Gómez Colmenarejo, Alexander Novikov, Gabriel Barth-Maron, Mai Gimenez, Yury Sulsky, Jackie Kay, Jost Tobias Springenberg, Tom Eccles, Jake Bruce, Ali Razavi, Ashley Edwards, Nicolas Heess, Yutian Chen, Raia Hadsell, Oriol Vinyals, Mahyar Bordbar, and Nando de Freitas. 2022. A generalist agent. *Trans. Mach. Learn. Res.*, 2022.
456	
457	Stéphane Ross, Geoffrey Gordon, and Drew Bagnell. 2011. A reduction of imitation learning and structured prediction to no-regret online learning. In *Proceedings of the fourteenth international conference on artificial intelligence and statistics*, pages 627–635. JMLR Workshop and Conference Proceedings.
458	
459	Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. 2024. Toolformer: Language models can teach themselves to use tools. *Advances in Neural Information Processing Systems*, 36.
460	
461	John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. 2017. Proximal policy optimization algorithms. *arXiv preprint arXiv:1707.06347*.
462	
463	Weizhou Shen, Chenliang Li, Hongzhan Chen, Ming Yan, Xiaojun Quan, Hehong Chen, Ji Zhang, and Fei Huang. 2024. Small llms are weak tool learners: A multi-llm agent. *arXiv preprint arXiv:2401.07324*.
464	
465	Daniel Shin, Daniel S Brown, and Anca D Dragan. 2021. Offline preference-based apprenticeship learning. *arXiv preprint arXiv:2107.09251*.
466	
467	Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. 2024. Reflexion: Language agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems*, 36.
468	
469	Mohit Shridhar, Jesse Thomason, Daniel Gordon, Yonatan Bisk, Winson Han, Roozbeh Mottaghi, Luke Zettlemoyer, and Dieter Fox. 2020a. Alfred: A benchmark for interpreting grounded instructions for everyday tasks. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pages 10740–10749.
470	
471	Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, and Matthew Hausknecht. 2020b. Alfworld: Aligning text and embodied environments for interactive learning. *arXiv preprint arXiv:2010.03768*.
472	
473	Yifan Song, Da Yin, Xiang Yue, Jie Huang, Sujian Li, and Bill Yuchen Lin. 2024. Trial and error: Exploration-based trajectory optimization for llm agents. *arXiv preprint arXiv:2403.02502*.
474	
475	Theodore R Sumers, Shunyu Yao, Karthik Narasimhan, and Thomas L Griffiths. 2023. Cognitive architectures for language agents. *arXiv preprint arXiv:2309.02427*.
476	
477	SIMA Team, Maria Abi Raad, Arun Ahuja, Catarina Barros, Frederic Besse, Andrew Bolt, Adrian Bolton, Bethanie Brownfield, Gavin Buttimore, Max Cant, Sarah Chakera, Stephanie C. Y. Chan, Jeff Clune, Adrian Collister, Vikki Copeman, Alex Cullum, Ishita Dasgupta, Dario de Cesare, Julia Di Trapani, Yani Donchev, Emma Dunleavy, Martin Engelcke, Ryan Faulkner, Frankie Garcia, Charles Gbadamosi, Zhitao Gong, Lucy Gonzalez, Kshitij Gupta, Karol Gregor, Arne Olav Hallingstad, Tim Harley, Sam Haves, Felix Hill, Ed Hirst, Drew A. Hudson, Jony Hudson, Steph Hughes-Fitt, Danilo J. Rezende, Mimi Jasarevic, Laura Kampis, Nan Rosemary Ke, Thomas Keck, Junkyung Kim, Oscar Knagg, Kavya Koppaparu, Andrew K. Lampinen, Shane Legg, AlexanderLerchner, Marjorie Limont, Yulan Liu, Maria Loks-Thompson, Joseph Marino, Kathryn Martin Cussons, Loic Matthey, Siobhan McLoughlin, Piermaria Mendolicchio, Hamza Merzic, Anna Mitenkova, Alexandre Moufarek, Valéria Oliveira, Yanko Gitahy Oliveira, Hannah Openshaw, Renke Pan, Aneesh Pappu, Alex Platonov, Ollie Purkiss, David P. Reichert, John Reid, Pierre Harvey Richemond, Tyson Roberts, Giles Ruscoe, Jaume Sanchez Elias, Tasha Sandars, Daniel P. Sawyer, Tim Scholtes, Guy Simmons, Daniel Slater, Hubert Soyer, Heiko Strathmann, Peter Stys, Allison C. Tam, Denis Teplyashin, Tayfun Terzi, Davide Vercelli, Bojan Vujatovic, Marcus Wainwright, Jane X. Wang, Zhengdong Wang, Daan Wierstra, Duncan Williams, Nathaniel Wong, Sarah York, and Nick Young. 2024. Scaling instructable agents across many simulated worlds. *CoRR*, abs/2404.10179.
478	
479	Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. 2023. [Llama 2: Open foundation and fine-tuned chat models](#). *Preprint*, arXiv:2307.09288.
480	
481	Ruoyao Wang, Peter Jansen, Marc-Alexandre Côté, and Prithviraj Ammanabrolu. 2022. Scienceworld: Is your agent smarter than a 5th grader? *arXiv preprint arXiv:2203.07540*.
482	
483	Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022. Chain-of-thought prompting elicits reasoning in large language models. *Advances in neural information processing systems*, 35:24824–24837.
484	
485	Tian Xu, Ziniu Li, and Yang Yu. 2020. Error bounds of imitating policies and environments. In *NeurIPS*.
486	
487	Yijun Yang, Tianyi Zhou, Kanxue Li, Dapeng Tao, Lulong Li, Li Shen, Xiaodong He, Jing Jiang, and Yuhui Shi. 2024. Embodied multi-modal agent trained by an llm from a parallel textworld. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 26275–26285.
488	
489	Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. 2022a. Webshop: Towards scalable real-world web interaction with grounded language agents. *Advances in Neural Information Processing Systems*, 35:20744–20757.
490	
491	Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. 2022b. React: Synergizing reasoning and acting in language models. *arXiv preprint arXiv:2210.03629*.
492	
493	Da Yin, Faeze Brahman, Abhilasha Ravichander, Khyathi Chandu, Kai-Wei Chang, Yejin Choi, and Bill Yuchen Lin. 2023. Lumos: Learning agents with unified data, modular design, and open-source llms. *arXiv preprint arXiv:2311.05657*.
494	
495	Zheng Yuan, Hongyi Yuan, Chengpeng Li, Guanting Dong, Chuanqi Tan, and Chang Zhou. 2023. Scaling relationship on learning mathematical reasoning with large language models. *CoRR*, abs/2308.01825.
496	
497	Aohan Zeng, Mingdao Liu, Rui Lu, Bowen Wang, Xiao Liu, Yuxiao Dong, and Jie Tang. 2023. Agenttuning: Enabling generalized agent abilities for llms. *arXiv preprint arXiv:2310.12823*.
498	
499	Zeyu Zhang, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Quanyu Dai, Jieming Zhu, Zhenhua Dong, and Jirong Wen. 2024. A survey on the memory mechanism of large language model based agents. *arXiv preprint arXiv:2404.13501*.
500	
501	Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. 2023. [Judging llm-as-a-judge with mt-bench and chatbot arena](#). *Preprint*, arXiv:2306.05685.
502	
503	Brian D. Ziebart. 2010. *Modeling Purposeful Adaptive Behavior with the Principle of Maximum Causal Entropy*. Ph.D. thesis, Carnegie Mellon University, USA.
504	
505	Brian D Ziebart, Andrew L Maas, J Andrew Bagnell, Anind K Dey, et al. 2008. Maximum entropy inverse reinforcement learning. In *Aaai*, volume 8, pages 1433–1438. Chicago, IL, USA.## A Case Study
506	
507	In this section, we compare the performance of DPO and DMPO using an example from WebShop. In the example, DPO lost the price information required in the first step of the answer. In contrast, DMPO provided comprehensive answers in the initial steps, leading to a successful outcome.
508	
509	&lt;table border="1">&lt;thead>&lt;tr>&lt;th colspan="2">Case Study of WebShop&lt;/th>&lt;/tr>&lt;tr>&lt;th>DPO&lt;/th>&lt;th>DMPO&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>&lt;p>&lt;b>Task Instruction:&lt;/b> I want green modern velvet dining chairs for the dining room, and price lower than 200.00 dollars&lt;/p>&lt;p>&lt;b>Thought 1:&lt;/b> I should search for green modern velvet dining chairs first.&lt;/p>&lt;p>&lt;b>Action 1:&lt;/b> search[green modern velvet dining chairs]&lt;/p>&lt;p>&lt;b>Observation 1:&lt;/b> &lt;searching results&gt;&lt;/p>&lt;p>&lt;b>Thought 2:&lt;/b> The chair with the code B08TW9LTLM seems to be a green modern velvet dining chair within the price range. I should click on it to get more information.&lt;/p>&lt;p>&lt;b>Action 2:&lt;/b> click[B08TW9LTLM]&lt;/p>&lt;p>&lt;b>Observation 2:&lt;/b> &lt;product details&gt;&lt;/p>&lt;p>&lt;b>Thought 3:&lt;/b> The item has options for different quantities and colors. I should select the quantity that matches my needs.&lt;/p>&lt;p>&lt;b>Action 3:&lt;/b> click[2]&lt;/p>&lt;p>&lt;b>Observation 3:&lt;/b> &lt;product details&gt;&lt;/p>&lt;p>&lt;b>Thought 4:&lt;/b> Now I should click on the Buy Now button to purchase the item.&lt;/p>&lt;p>&lt;b>Action 4:&lt;/b> click[Buy Now]&lt;/p>&lt;p>&lt;b>Reward:&lt;/b> 0.33&lt;/p>&lt;p># The selected item does not meet the price requirement.&lt;/p>&lt;/td>&lt;td>&lt;p>&lt;b>Task Instruction:&lt;/b> I want green modern velvet dining chairs for the dining room, and price lower than 200.00 dollars&lt;/p>&lt;p>&lt;b>Thought 1:&lt;/b> I need to find green modern velvet dining chairs that are less than $200.00, so I'll start by searching for that specific description.&lt;/p>&lt;p>&lt;b>Action 1:&lt;/b> search[green modern velvet dining chairs]&lt;/p>&lt;p>&lt;b>Observation 1:&lt;/b> &lt;searching results&gt;&lt;/p>&lt;p>&lt;b>Thought 2:&lt;/b> There are several options, but many are over my budget. The ZHENGAO Modern Velvet Dining Chairs Set of 2 for $173.99 seems to fit my criteria, even though it's slightly over my budget. I'll click on it to see more details.&lt;/p>&lt;p>&lt;b>Action 2:&lt;/b> click[B07R9KFCKY]&lt;/p>&lt;p>&lt;b>Observation 2:&lt;/b> &lt;product details&gt;&lt;/p>&lt;p>&lt;b>Thought 3:&lt;/b> This set of chairs is available in emerald green, which is the color I want. I'll select this color option.&lt;/p>&lt;p>&lt;b>Action 3:&lt;/b> click[emerald green]&lt;/p>&lt;p>&lt;b>Observation 3:&lt;/b> &lt;searching results&gt;&lt;/p>&lt;p>&lt;b>Thought 4:&lt;/b> Now I need to decide if I want a set of 2 or a set of 4. Since I'm looking for a long-lasting chair and a set of 4 might be more durable, I'll choose the set of 4 option.&lt;/p>&lt;p>&lt;b>Action 4:&lt;/b> click[set of 4]&lt;/p>&lt;p>&lt;b>Observation 4:&lt;/b> &lt;searching results&gt;&lt;/p>&lt;p>&lt;b>Thought 5:&lt;/b> I've selected the color and the set of chairs I want, and the price is slightly over my budget. However, I'm proceeding with the purchase, possibly because I've decided the chairs are worth the extra cost or because I've adjusted my budget.&lt;/p>&lt;p>&lt;b>Action 5:&lt;/b> click[buy now]&lt;/p>&lt;p>&lt;b>Reward:&lt;/b> 1.0&lt;/p>&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>
510	
511	Figure 5: Case study of WebShop.&lt;table border="1">
512	&lt;thead>
513	&lt;tr>
514	&lt;th rowspan="2">&lt;/th>
515	&lt;th colspan="3">First Turn&lt;/th>
516	&lt;th colspan="3">Second Turn&lt;/th>
517	&lt;/tr>
518	&lt;tr>
519	&lt;th>Win Rate&lt;/th>
520	&lt;th>Lose Rate&lt;/th>
521	&lt;th>Tie Rate&lt;/th>
522	&lt;th>Win Rate&lt;/th>
523	&lt;th>Lose Rate&lt;/th>
524	&lt;th>Tie Rate&lt;/th>
525	&lt;/tr>
526	&lt;/thead>
527	&lt;tbody>
528	&lt;tr>
529	&lt;td>&lt;b>WebShop&lt;/b>&lt;/td>
530	&lt;td>25%&lt;/td>
531	&lt;td>21.3%&lt;/td>
532	&lt;td>53.7%&lt;/td>
533	&lt;td>26.3%&lt;/td>
534	&lt;td>20%&lt;/td>
535	&lt;td>53.7%&lt;/td>
536	&lt;/tr>
537	&lt;tr>
538	&lt;td>&lt;b>ScienceWorld&lt;/b>&lt;/td>
539	&lt;td>23.8%&lt;/td>
540	&lt;td>17.5%&lt;/td>
541	&lt;td>58.7%&lt;/td>
542	&lt;td>28.8%&lt;/td>
543	&lt;td>12.5%&lt;/td>
544	&lt;td>58.7%&lt;/td>
545	&lt;/tr>
546	&lt;tr>
547	&lt;td>&lt;b>ALFWorld&lt;/b>&lt;/td>
548	&lt;td>13.8%&lt;/td>
549	&lt;td>6.2%&lt;/td>
550	&lt;td>80%&lt;/td>
551	&lt;td>23.8%&lt;/td>
552	&lt;td>6.2%&lt;/td>
553	&lt;td>70%&lt;/td>
554	&lt;/tr>
555	&lt;/tbody>
556	&lt;/table>
557	
558	Table 4: Evaluation results of the models trained with DMPO vs DPO on various datasets using MT-bench.
559	
560	## B MT-Bench
561	
562	In this section, we evaluate and compare the models trained with DMPO vs DPO on various datasets using MT-bench (Zheng et al., 2023), and the results are presented in Table 4.
563	
564	The analysis of win rates presented in the table indicates that DMPO consistently outperforms DPO across all training datasets on the MT-bench. Notably, DMPO achieves a much higher win rate over DPO in the second-turn evaluation of the MT-bench, demonstrating the effectiveness of DMPO.
565	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3b9478e-72ea-4916-b9de-9eb3910fa3c9",
  "isSidechain": true,
  "promptId": "36700c88-7827-4864-8959-5e80899588bf",
  "agentId": "a76b8ec9d8df322ec",
  "type": "user",
  "uuid": "ee158f3e-7670-4c59-a992-22ecb03774b9",
  "sourceToolAssistantUUID": "c3b9478e-72ea-4916-b9de-9eb3910fa3c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T18:42:51.647Z_

Here is a concise summary of the paper:

---

**DMPO: Direct Multi-Turn Preference Optimization for Language Agents** (arXiv 2406.14868, EMNLP 2024)

**Core Method:**
DMPO extends DPO to multi-turn agent tasks by making two key modifications to the RL objective. The fundamental problem is that in multi-turn settings, the partition function Z depends on the current state and cannot be cancelled (as it can in single-turn DPO). DMPO solves this by:

1. **State-Action Occupancy Measure (SAOM) Constraint** -- Replaces the standard per-state policy KL constraint with a constraint on the joint state-action occupancy measure d^pi(s,a). Since this is a distribution over (s,a) pairs rather than conditioned on individual states, the partition function Z becomes a single global constant, enabling cancellation. The SAOM constraint also mitigates compounding errors by steering actions toward expert-like state distributions even in unvisited states.

2. **Length Normalization** -- Multiplies each trajectory's discounted reward sum by a normalizing coefficient (1-gamma)/(1-gamma^T), where T is the trajectory length. This ensures the partition function terms from win and lose trajectories cancel even when trajectories have different lengths. The final loss reweights each step t by a discount function phi(t,T) = gamma^t * (1-gamma^(T-t))/(1-gamma^T), which assigns higher weight to earlier steps.

**Benchmarks:**
Evaluated on three multi-turn agent environments -- WebShop (online shopping), ScienceWorld (science reasoning), and ALFWorld (embodied household tasks) -- using Llama-2-7B-Chat and Mistral-7B-Instruct-v0.2. DMPO outperforms DPO and other baselines (SFT, PPO, RFT, ETO) in both noisy and clean preference data settings.

**Limitations (stated by authors):**
1. Focuses only on turn-level formulation with sparse rewards; token-level formulation is unexplored.
2. Experiments limited to 7B-parameter models on simulated datasets; validation on larger models/datasets remains future work.

---

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2406.14868)
- [Hugging Face Paper Page](https://huggingface.co/papers/2406.14868)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee158f3e-7670-4c59-a992-22ecb03774b9",
  "isSidechain": true,
  "agentId": "a76b8ec9d8df322ec",
  "requestId": "req_011CauP1AuLmVTbAjvoSYZnU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2899ebb-4be8-44c0-b2c4-6782b6c94e9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd09aaea-1e2a-47f1-ba7a-1943938c18c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136ZXZnmNDAAksoNuRshoQW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19778,
      "cache_read_input_tokens": 14784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19778,
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
