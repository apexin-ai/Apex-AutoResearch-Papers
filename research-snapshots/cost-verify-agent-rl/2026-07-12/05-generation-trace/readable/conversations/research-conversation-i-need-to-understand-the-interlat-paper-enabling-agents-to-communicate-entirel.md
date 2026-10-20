# Research conversation: I need to understand the Interlat paper: "Enabling Agents to Communicate Entirely in Latent Space" by Du et al., arXiv 2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6eccb847c5a694e7.jsonl`
- **Structured JSON:** [`64de1afa6109fa9cac16.json`](../../sessions/64/64de1afa6109fa9cac16.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-10T20:48:34.471Z_

I need to understand the Interlat paper: "Enabling Agents to Communicate Entirely in Latent Space" by Du et al., arXiv 2511.09149 (revised April 2026).

Please:
1. Use WebSearch to find this paper (try: "Interlat arXiv 2511.09149 Du agents communicate latent space" and "enabling agents communicate entirely latent space")
2. Use WebFetch to read the paper from arXiv (https://arxiv.org/abs/2511.09149)
3. Identify:
   - What is their core mechanism for inter-agent latent communication?
   - How do they compress/transfer hidden states between agents?
   - How does this compare to LatentMAS (shared working memory of last-layer embeddings), RecursiveMAS (RecursiveLink modules), and DiffMAS (KV-cache trace construction)?
   - What benchmarks do they evaluate on and what results do they achieve?
   - Was it revised in April 2026? What changed?

I need this for a research landscape analysis of latent vs text communication methods in multi-agent LLM systems. Report in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "8419dc24-c0bb-4fe5-81fd-71a6466cc6b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:48:34.475Z_

```json
{
  "parentUuid": "8419dc24-c0bb-4fe5-81fd-71a6466cc6b6",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
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
  "uuid": "1aa80bdf-7cbf-40f6-bd68-e0588ec3152d",
  "timestamp": "2026-05-10T20:48:34.475Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T20:48:36.734Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then search for and fetch the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aa80bdf-7cbf-40f6-bd68-e0588ec3152d",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYcYUta4k1ZEderoYpg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac7ee826-7620-4ec6-b367-94ae824ee247",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7gwkTAMo39gY29P3uN3By",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 821,
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

_source line 4 · 2026-05-10T20:48:37.032Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015uUpr7dRvxSM7JKLnLK9b6`</summary>

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
  "parentUuid": "ac7ee826-7620-4ec6-b367-94ae824ee247",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYcYUta4k1ZEderoYpg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86e347ce-64bf-4fc3-b82e-512a01f3bd60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7gwkTAMo39gY29P3uN3By",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 8223,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 821
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 821,
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

_source line 5 · 2026-05-10T20:48:37.035Z_

<details><summary>↩ Tool result · `toolu_015uUpr7dRvxSM7JKLnLK9b6`</summary>

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
  "parentUuid": "86e347ce-64bf-4fc3-b82e-512a01f3bd60",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "6145e5a3-932c-4d46-90c6-b4b791c114cb",
  "sourceToolAssistantUUID": "86e347ce-64bf-4fc3-b82e-512a01f3bd60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T20:48:39.804Z_



Now let me search for the paper and fetch it from arXiv in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6145e5a3-932c-4d46-90c6-b4b791c114cb",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYcjfbRVBh9KwFNNmaj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f6a1ab0-245d-4e32-8760-5af9e5f0343d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sf4ZHgkNnPapsQVkFgz54x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 7 · 2026-05-10T20:48:41.224Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0152VXjQvL6bin7EMsoGkW6U`</summary>

```json
{
  "query": "Interlat arXiv 2511.09149 Du agents communicate latent space"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f6a1ab0-245d-4e32-8760-5af9e5f0343d",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYcjfbRVBh9KwFNNmaj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77d2f21d-608f-467e-998c-fee5fc38f714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sf4ZHgkNnPapsQVkFgz54x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 8 · 2026-05-10T20:48:41.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FGWh1rBomXHPSkPtBgRtV7`</summary>

```json
{
  "query": "enabling agents communicate entirely latent space Du 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77d2f21d-608f-467e-998c-fee5fc38f714",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYcjfbRVBh9KwFNNmaj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbe21217-e803-4135-828b-5ca1b4acea54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sf4ZHgkNnPapsQVkFgz54x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 9 · 2026-05-10T20:48:43.863Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y8DsLKHsNU4BPBTYNa4CSB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.09149",
  "prompt": "Extract all details about this paper: title, authors, abstract, full content if available. What is the paper about? What is the core mechanism? What are the benchmarks and results? Is there any revision history - was it revised in April 2026? What changed in any revisions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbe21217-e803-4135-828b-5ca1b4acea54",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYcjfbRVBh9KwFNNmaj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59b9ad35-4293-4f26-9a2b-ac2864d604eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sf4ZHgkNnPapsQVkFgz54x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9044,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 260,
          "cache_read_input_tokens": 9044,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 10 · 2026-05-10T20:48:48.663Z_

<details><summary>↩ Tool result · `toolu_0152VXjQvL6bin7EMsoGkW6U`</summary>

```text
Web search results for query: "Interlat arXiv 2511.09149 Du agents communicate latent space"

Links: [{"title":"[2511.09149] Enabling Agents to Communicate Entirely in Latent Space","url":"https://arxiv.org/abs/2511.09149"},{"title":"Enabling Agents to Communicate Entirely in Latent Space","url":"https://arxiv.org/html/2511.09149"},{"title":"Enabling Agents to Communicate Entirely in Latent Space Zhuoyun Du1†*","url":"https://arxiv.org/pdf/2511.09149"},{"title":"Enabling Agents to Communicate Entirely in Latent Space | OpenReview","url":"https://openreview.net/forum?id=rmYbgsehTd"},{"title":"Position: Introspective Experience from Conversational Environments as a Path to Better Learning","url":"https://arxiv.org/html/2602.14910v1"},{"title":"Enabling Agents to Communicate Entirely in Latent Space | Request PDF","url":"https://www.researchgate.net/publication/397556064_Enabling_Agents_to_Communicate_Entirely_in_Latent_Space"},{"title":"Computer Science Nov 2025","url":"https://arxiv.org/list/cs/2025-11?skip=4300&show=100"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=40475&show=2000"},{"title":"[Literature Review] Enabling Agents to Communicate Entirely in Latent Space","url":"https://www.themoonlight.io/en/review/enabling-agents-to-communicate-entirely-in-latent-space"},{"title":"Telepathy for AI? How Latent Communication Could Change...","url":"https://www.machinebrief.com/news/telepathy-for-ai-how-latent-communication-could-change-the-g-7y97"}]

I found the paper! Here's information about **Interlat (arXiv 2511.09149)**:

## Overview

Interlat (Inter-agent Latent Space Communication) is a paradigm that leverages the continuous last hidden states of an LLM as a representation of its thought for direct communication (termed latent communication).

## Key Motivation

While natural language is the de facto communication medium for LLM-based agents, it presents a fundamental constraint. The process of downsampling rich, internal latent states into discrete tokens inherently limits the depth and nuance of information that can be transmitted, thereby hindering collaborative problem-solving.

## Technical Approach

Rather than transmitting discrete tokens decoded by the language head, Interlat directly transmits the temporally aligned last-layer hidden states corresponding to an agent's generated message, treating them as a representation of its thoughts. An additional learned compression process further compresses latent communication via latent space reasoning.

## Results and Performance

Experiments demonstrate that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, even across heterogeneous models, promoting more exploratory behavior and enabling genuine utilization of latent information. Additionally, latent messages can be compressed to as few as 8 tokens while maintaining competitive performance, achieving up to a 24× reduction in communication latency.

## Authors

The paper was authored by Zhuoyun Du and 8 other authors (Runze Wang, Huiyu Bai, Zouying Cao, Xiaoyong Zhu, Yu Cheng, Bo Zheng, Wei Chen, and Haochao Ying).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77d2f21d-608f-467e-998c-fee5fc38f714",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "6edbc9a9-53bf-410f-9086-fe4bf8c7103f",
  "sourceToolAssistantUUID": "77d2f21d-608f-467e-998c-fee5fc38f714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T20:48:49.031Z_

<details><summary>↩ Tool result · `toolu_01FGWh1rBomXHPSkPtBgRtV7`</summary>

```text
Web search results for query: "enabling agents communicate entirely latent space Du 2025"

Links: [{"title":"[2511.09149] Enabling Agents to Communicate Entirely in Latent Space","url":"https://arxiv.org/abs/2511.09149"},{"title":"Enabling Agents to Communicate Entirely in Latent Space | OpenReview","url":"https://openreview.net/forum?id=rmYbgsehTd"},{"title":"Enabling Agents to Communicate Entirely in Latent Space Zhuoyun Du1†*","url":"https://arxiv.org/pdf/2511.09149"},{"title":"Enabling Agents to Communicate Entirely in Latent Space","url":"https://arxiv.org/html/2511.09149v4"},{"title":"Enabling Agents to Communicate Entirely in Latent Space | Request PDF","url":"https://www.researchgate.net/publication/397556064_Enabling_Agents_to_Communicate_Entirely_in_Latent_Space"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=40475&show=2000"},{"title":"The Invisible AI Threat: Latent Collaboration's Efficiency Breakthrough and Dangerous Security Risks","url":"https://kenhuangus.substack.com/p/latentmas-ai-agents-collaborate-at"},{"title":"GitHub - YU-deep/Awesome-Latent-Space: A paper list of Awesome Latent Space. · GitHub","url":"https://github.com/YU-deep/Awesome-Latent-Space"},{"title":"Position: Introspective Experience from Conversational Environments as a Path to Better Learning","url":"https://arxiv.org/html/2602.14910v1"},{"title":"Computer Science Nov 2025","url":"https://arxiv.org/list/cs/2025-11?skip=4300&show=100"}]

I found the research paper you're looking for! Here are the key findings:

## Enabling Agents to Communicate Entirely in Latent Space

The paper proposes Interlat (Inter-agent Latent Space Communication), a paradigm that leverages the continuous last hidden states of an LLM as a representation of its thought for direct communication.

### The Problem

While natural language is the de facto communication medium for LLM-based agents, it presents a fundamental constraint. The process of downsampling rich, internal latent states into discrete tokens inherently limits the depth and nuance of information that can be transmitted, thereby hindering collaborative problem-solving.

### The Solution

Inspired by telepathy, which bypasses symbolic language in communication, the approach leverages the continuous last hidden states of an LLM as a representation of its thought for direct communication (termed latent communication). An additional learned compression process further compresses latent communication via latent space reasoning.

### Results

Experiments demonstrate that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, even across heterogeneous models, promoting more exploratory behavior and enabling genuine utilization of latent information. Further compression not only substantially accelerates inference by up to 24 times but also maintains competitive performance through an efficient information-preserving mechanism.

The paper was submitted by Zhuoyun Du and colleagues and represents a feasibility study of entirely latent space inter-agent communication.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbe21217-e803-4135-828b-5ca1b4acea54",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "54f5204f-33a1-42e6-ba11-5df0bbceed4e",
  "sourceToolAssistantUUID": "bbe21217-e803-4135-828b-5ca1b4acea54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T20:48:50.548Z_

<details><summary>↩ Tool result · `toolu_01Y8DsLKHsNU4BPBTYNa4CSB`</summary>

```text
# Paper Summary: Enabling Agents to Communicate Entirely in Latent Space

## Basic Information
- **arXiv ID:** 2511.09149
- **Submitted:** November 12, 2025
- **Current Version:** v4 (April 16, 2026)
- **Status:** Accepted to ACL 2026
- **Authors:** Zhuoyun Du, Runze Wang, Huiyu Bai, Zouying Cao, Xiaoyong Zhu, Yu Cheng, Bo Zheng, Wei Chen, Haochao Ying

## Core Topic
This research proposes **Interlat** (Inter-agent Latent Space Communication), a novel communication paradigm for LLM-based agents that bypasses natural language entirely.

## Key Mechanism
Rather than converting internal model states into discrete tokens, the method leverages "continuous last hidden states of an LLM as a representation of its thought for direct communication." Additionally, learned compression further optimizes latent space reasoning.

## Main Results
- Outperforms fine-tuned chain-of-thought prompting and single-agent baselines
- Works across heterogeneous models
- Promotes more exploratory behavior
- Achieves "up to 24 times" inference acceleration through compression while maintaining performance

## Revision History
The paper underwent four revisions:
- **v1:** November 12, 2025
- **v2:** January 7, 2026
- **v3:** January 21, 2026
- **v4:** April 16, 2026

The April 2026 revision occurred after acceptance notification. Specific content changes aren't detailed in the provided excerpt.

**Code availability:** Authors provided implementation on GitHub.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59b9ad35-4293-4f26-9a2b-ac2864d604eb",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "d546256d-acb4-43c0-9beb-259e9ed14096",
  "sourceToolAssistantUUID": "59b9ad35-4293-4f26-9a2b-ac2864d604eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T20:48:53.754Z_

Good, I have the basic overview. Now let me fetch the full HTML version and the OpenReview page for deeper technical details, benchmarks, and comparison material.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d546256d-acb4-43c0-9beb-259e9ed14096",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYdjG4TmKJviUwV53Bk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ec4c612-16ae-4b1d-ad49-3dde20af31f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSBVVi73soiXadkazD4z5o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2466,
      "cache_read_input_tokens": 10957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2466,
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

_source line 14 · 2026-05-10T20:49:01.365Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WjzXd2WQemo8sid6SJmSS6`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.09149v4",
  "prompt": "Extract ALL technical details from this paper. Specifically:\n\n1. CORE MECHANISM: How exactly does Interlat work? How are hidden states extracted, transmitted, and injected into the receiving agent? What layers are used? How does the receiving agent process latent messages?\n\n2. COMPRESSION: How do they compress hidden states? What is the compression module architecture? How do they go from full hidden states to 8 tokens? What is the \"latent space reasoning\" compression?\n\n3. TRAINING: How is the system trained? What losses are used? Is it end-to-end? What models are used as base?\n\n4. BENCHMARKS: What exact benchmarks are evaluated? What are the numerical results (accuracy, scores)? Include all tables/numbers.\n\n5. COMPARISONS: Do they compare to any other latent communication methods? Do they mention LatentMAS, RecursiveMAS, DiffMAS, or other baselines?\n\n6. REVISION HISTORY: What changed between versions, especially in the April 2026 v4 revision?\n\n7. Any details about heterogeneous model communication - how do different model architectures communicate in latent space?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ec4c612-16ae-4b1d-ad49-3dde20af31f8",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYdjG4TmKJviUwV53Bk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e1b956e-f91d-44db-b3cc-88636694bddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSBVVi73soiXadkazD4z5o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2466,
      "cache_read_input_tokens": 10957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2466,
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

_source line 15 · 2026-05-10T20:49:02.755Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KfRK1XR5V95U6f9XyjXKkX`</summary>

```json
{
  "url": "https://openreview.net/forum?id=rmYbgsehTd",
  "prompt": "Extract all review details, scores, and discussion about this paper. What did reviewers say about strengths and weaknesses? What was the final decision? Any comparisons to related work mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e1b956e-f91d-44db-b3cc-88636694bddb",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYdjG4TmKJviUwV53Bk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9094ab1e-ca48-4555-a6c1-a0aee8e2b9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSBVVi73soiXadkazD4z5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2466,
      "cache_read_input_tokens": 10957,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2466
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 10957,
          "cache_creation_input_tokens": 2466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2466,
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

_source line 16 · 2026-05-10T20:49:06.717Z_

<details><summary>↩ Tool result · `toolu_01KfRK1XR5V95U6f9XyjXKkX`</summary>

```text
I cannot provide the review details, scores, and discussion you've requested because this information is not present in the web page content you provided.

The page shows only:
- The paper title and authors
- A submission status marked as "Withdrawn Submission"
- An abstract describing the research
- Basic metadata (keywords, submission number, primary area)

The actual peer reviews, reviewer scores, discussion comments, and final decision are not included in this webpage excerpt. To access that information, you would need to:

1. Visit the full OpenReview page for this paper
2. Check if reviews are publicly visible (some papers only show reviews after decisions are finalized)
3. Note that this paper is marked as "Withdrawn," which may affect review visibility

The abstract does mention the work "outperforms both fine-tuned chain-of-thought prompting and single-agent baselines," but this is the authors' claim rather than reviewer feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9094ab1e-ca48-4555-a6c1-a0aee8e2b9cd",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "0ba7f8f6-e7f3-4c02-8b0b-6e4d6c8c2ef8",
  "sourceToolAssistantUUID": "9094ab1e-ca48-4555-a6c1-a0aee8e2b9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T20:49:24.758Z_

<details><summary>↩ Tool result · `toolu_01WjzXd2WQemo8sid6SJmSS6`</summary>

````text
# Technical Details from "Enabling Agents to Communicate Entirely in Latent Space"

## 1. CORE MECHANISM

**Hidden State Extraction:**
The system collects last-layer hidden states h_ℓ ∈ ℝ^d from the transformer immediately before predicting token y_ℓ, assembling them into matrix H ∈ ℝ^(L×d) where L is sequence length.

**Transmission Protocol:**
Special tokens `&lt;bop>` (beginning) and `&lt;eop>` (end) mark latent communication boundaries. The receiving agent's input embedding becomes: `[e(x₁),...,e(xᵢ),h₁,h₂,...,h_L,e(xⱼ)]` where e(·) denotes token embeddings.

**Processing:**
"A trainable light-weight self-attention and a projection layer" form a communication adapter that rescales and interprets received latent states before the actor processes them.

**Layer Selection:**
The method uses last-layer hidden states specifically, avoiding ad-hoc layer selection overhead mentioned as a limitation of prior work.

---

## 2. COMPRESSION MECHANISM

**Architecture:**
A separate reasoning model M_φ generates compact latent messages H_K ∈ ℝ^(K×d) where K ≪ L through "autoregressive reasoning entirely in latent space by feeding its last hidden state back as the next input embedding through a lightweight projection."

**Process Flow:**
Rather than truncating full sequences, the compression model performs iterative latent generation: `⟨M_φ(Eᵢ)→hᵢ, Eᵢ₊₁=Eᵢ⊕Proj(hᵢ)⟩`

**Compression Ratio:**
Results demonstrate compression "to as few as 8 tokens while maintaining competitive performance, achieving up to a 24× reduction in communication latency" from 9.19s to 0.39s.

**Training Objective:**
Three-component loss: `ℒ_compress = λ_task·ℒ_task + λ_pref·ℒ_pref + λ_geom·ℒ_geom`

- **Task loss:** Cross-entropy ensuring downstream utility
- **Preference loss:** Uncertainty-weighted KL divergence aligning compressed/full behaviors at positions where latents reduce uncertainty
- **Geometry loss:** Cosine similarity maintaining directional alignment: `ℒ_geom = 1 - cos(z̄^(A), z̄^(D))`

---

## 3. TRAINING PROCEDURE

**Actor Training:**
Supervised fine-tuning with three regularization objectives:

```
ℒ_total = ℒ_task + λ_S·ℒ_sep + λ_A·ℒ_align
```

**Conditional Thought Separation:**
Minimizes weighted Jensen–Shannon divergence between matched latents H and mismatched H̃: "separates matched from mismatched conditional distributions, providing a robust training signal."

**Plan-Aligned Regulation:**
Regularizes predictions using language-space plans to prevent exploiting the separation objective: `ℒ_align = (β/|S|)∑KL(p_θ(·|H)‖p_plan(·|P)) + (α/|S|)∑(1-cos(z_θ(H),z_plan(P)))`

**Curriculum Learning:**
"Token-to-latent curriculum that stochastically replaces early communication positions with their corresponding plan token embeddings" with replacement rate r ∈ {0,0.1,...,1.0}.

**Implementation:**
- Base models: Qwen2.5-7B/0.5B-Base, LLaMA3.1-8B-Base
- Learning rate: 1×10⁻⁵ (actor), 5×10⁻⁵ (reasoning)
- Batch size: 16
- bfloat16 precision, FlashAttention-2, DeepSpeed
- Hyperparameters: λ_sep ∈ [0.1,1.0], λ_align ∈ [0.1,0.2], dynamically annealed

---

## 4. BENCHMARKS & RESULTS

**ALFWorld Embodied Tasks:**

| Model | Seen % | Unseen % | Steps |
|-------|--------|----------|-------|
| **Interlat** | **70.48** | **65.42** | 9.41/12.54 |
| Text (CoT) | 64.29 | 62.44 | 8.76/12.77 |
| No-Comm | 62.14 | 62.19 | 10.19/13.90 |
| CoT (full) | 67.14 | 64.93 | 8.15/12.04 |

Across three model backbones (Qwen2.5-7B, Qwen2.5-0.5B, LLaMA3.1-8B), Interlat consistently outperforms baselines.

**MATH Benchmark:**

| Method | Overall | Level-3 | Level-4 | Level-5 |
|--------|---------|---------|---------|---------|
| Interlat | 36.88% | 40.08% | 27.45% | **15.80%** |
| CoT (full) | 38.35% | 45.65% | 31.19% | 15.05% |
| Text | 34.35% | 37.60% | 26.30% | 14.20% |

Interlat surpasses CoT on most challenging Level-5 tasks.

**Compression Performance (Qwen2.5-7B):**

| Length | Seen | Unseen | Latency |
|--------|------|--------|---------|
| Full (128L) | 68.10% | 62.94% | 2.25s |
| 64L | 67.14% | 61.94% | 1.16s |
| 8L | 66.43% | 60.45% | 0.20s |

---

## 5. COMPARATIVE ANALYSIS

**Variants Evaluated:**
- CrossTask (different task latents): 61.43% → substantial degradation confirming task-specificity
- CovGauss, RandomRot (structure-preserving noise): significant performance drops indicating reliance on geometric structure
- Qwen2LLaMA (cross-family): 70.95% seen, 71.39% unseen, demonstrating heterogeneous model compatibility

**No Direct Comparison to:**
The paper doesn't explicitly compare against LatentMAS, RecursiveMAS, or DiffMAS. It cites recent work like Ramesh & Li (2025) on "activations between language model agents" and Tang et al. (2025) on "state delta trajectory," positioning Interlat as providing more efficient, language-free communication.

---

## 6. HETEROGENEOUS MODEL COMMUNICATION

**Cross-Family Results:**
"Feeding Qwen-derived latents to train an LLaMA actor yield even stronger performance gains" (70.95% vs 70.48% baseline). The paper argues this demonstrates "latent-level inter-agent understanding that transfers across heterogeneous representations" since different model families have distinct latent manifolds but can still interpret shared task-relevant information.

**Mechanism:**
The communication adapter (lightweight self-attention + projection) provides sufficient bridging that latent semantics generalize across model families without parameter sharing.

---

## 7. REVISION HISTORY (v4, April 2026)

The document shows **arXiv:2511.09149v4** dated April 16, 2026. Specific changes between versions are not detailed in the provided content, though the comprehensive appendices (A-H) suggest iterative refinement of experimental analysis and ablation studies.

---

## Key Innovation Summary

Interlat bypasses language discretization by transmitting continuous last-layer hidden states. Unlike prior activation-grafting methods, it enables full-length latent trajectories through an adapter, then compresses via autoregressive latent-space reasoning. The three-loss training objective ensures task utility, behavioral alignment, and geometric consistency—achieving 24× speedup while maintaining performance parity across heterogeneous models.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e1b956e-f91d-44db-b3cc-88636694bddb",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "e2482ca5-83f7-4367-baee-31390032a234",
  "sourceToolAssistantUUID": "3e1b956e-f91d-44db-b3cc-88636694bddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T20:49:27.542Z_

Interesting -- the OpenReview page shows "Withdrawn Submission" while arXiv says "Accepted to ACL 2026." Let me dig deeper into revision details and any related work comparisons.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2482ca5-83f7-4367-baee-31390032a234",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYgFWYP4Hn6wxRpxejR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51785494-c1fd-45e3-980b-086b3cf3b9f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MteauZUtcLnFjQVT14E1UW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 233,
      "cache_creation_input_tokens": 2553,
      "cache_read_input_tokens": 13423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2553,
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

_source line 19 · 2026-05-10T20:49:28.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W7ucVfdEePr5UtVJWADbet`</summary>

```json
{
  "query": "Interlat Du 2511.09149 ACL 2026 accepted revision changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51785494-c1fd-45e3-980b-086b3cf3b9f0",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYgFWYP4Hn6wxRpxejR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2de3fd8a-cd22-41b6-a6a8-b4831df072ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MteauZUtcLnFjQVT14E1UW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 233,
      "cache_creation_input_tokens": 2553,
      "cache_read_input_tokens": 13423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2553,
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

_source line 20 · 2026-05-10T20:49:28.977Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sqt81bKcPJAUzxiEQY2MTy`</summary>

```json
{
  "query": "LatentMAS RecursiveMAS DiffMAS latent communication multi-agent LLM comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2de3fd8a-cd22-41b6-a6a8-b4831df072ee",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYgFWYP4Hn6wxRpxejR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2e7e8f3-7140-4328-85ee-a0e6cfcfc3fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MteauZUtcLnFjQVT14E1UW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 233,
      "cache_creation_input_tokens": 2553,
      "cache_read_input_tokens": 13423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2553,
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

_source line 21 · 2026-05-10T20:49:32.079Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NBn2MhyMrabgVNafyViWAA`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2511.09149",
  "prompt": "Look for: 1) Related work section - do they discuss LatentMAS, RecursiveMAS, DiffMAS, or other latent inter-agent communication methods? 2) Any discussion of shared working memory, KV-cache traces, or recursive link modules? 3) The conclusion and limitations section. 4) Any mention of revision history or what changed in different versions. 5) The exact benchmarks used and full numerical results tables. 6) Details about the communication adapter architecture."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2e7e8f3-7140-4328-85ee-a0e6cfcfc3fc",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYgFWYP4Hn6wxRpxejR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3163b7a7-5c36-4519-81f5-c17990d44f96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MteauZUtcLnFjQVT14E1UW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 233,
      "cache_creation_input_tokens": 2553,
      "cache_read_input_tokens": 13423,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2553
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 233,
          "output_tokens": 348,
          "cache_read_input_tokens": 13423,
          "cache_creation_input_tokens": 2553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2553,
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

_source line 22 · 2026-05-10T20:49:32.292Z_

<details><summary>↩ Tool result · reported error · `toolu_01NBn2MhyMrabgVNafyViWAA`</summary>

```text
maxContentLength size of 10485760 exceeded
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3163b7a7-5c36-4519-81f5-c17990d44f96",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "fa36abe5-5ec9-4fa5-92cf-0b16113170d8",
  "toolUseResult": "Error: maxContentLength size of 10485760 exceeded",
  "sourceToolAssistantUUID": "3163b7a7-5c36-4519-81f5-c17990d44f96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T20:49:33.940Z_

<details><summary>↩ Tool result · `toolu_01W7ucVfdEePr5UtVJWADbet`</summary>

```text
Web search results for query: "Interlat Du 2511.09149 ACL 2026 accepted revision changes"

Links: [{"title":"[2511.09149] Enabling Agents to Communicate Entirely in Latent Space","url":"https://arxiv.org/abs/2511.09149"},{"title":"Enabling Agents to Communicate Entirely in Latent Space","url":"https://arxiv.org/html/2511.09149"},{"title":"Federal Register :: Notice Pursuant to the National Cooperative Research and Production Act of 1993-The Open Group, L.L.C.","url":"https://www.federalregister.gov/documents/2026/05/08/2026-09149/notice-pursuant-to-the-national-cooperative-research-and-production-act-of-1993-the-open-group-llc"},{"title":"Accepted Papers - ACL 2026","url":"https://2026.aclweb.org/program/accepted_papers/"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"Enabling Agents to Communicate Entirely in Latent Space Zhuoyun Du1†*","url":"https://arxiv.org/pdf/2511.09149"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"2024Q1 Reports: ACL 2026 - Admin Wiki","url":"https://aclweb.org/adminwiki/index.php/2024Q1_Reports:_ACL_2026"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"21 papers were accepted at ACL 2026 | Center for Advanced Intelligence Project","url":"https://aip.riken.jp/news/acl2026/"}]

Based on the search results, I found information about the paper referenced by that identifier:

The paper arXiv:2511.09149 was submitted on November 12, 2025 (v1) and last revised on April 16, 2026 (v4). The paper is titled "Enabling Agents to Communicate Entirely in Latent Space" and is authored by Zhuoyun Du and colleagues.

The paper proposes Interlat (Inter-agent Latent Space Communication), a paradigm that leverages the continuous last hidden states of an LLM as a representation of its thought for direct communication, with an additional learned compression process that further compresses latent communication via latent space reasoning.

However, I was unable to find specific information in the search results about this paper's acceptance status at ACL 2026 or details about specific revision changes made to the paper. The search results show that ACL 2026 accepted 21 papers in total, but do not provide a detailed list confirming whether this particular paper was among the accepted papers or what revision changes were made during the review process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2de3fd8a-cd22-41b6-a6a8-b4831df072ee",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "ee9aba5d-4c9c-495b-92ae-f284c01ca46c",
  "sourceToolAssistantUUID": "2de3fd8a-cd22-41b6-a6a8-b4831df072ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T20:49:39.722Z_

<details><summary>↩ Tool result · `toolu_01Sqt81bKcPJAUzxiEQY2MTy`</summary>

```text
Web search results for query: "LatentMAS RecursiveMAS DiffMAS latent communication multi-agent LLM comparison"

Links: [{"title":"GitHub - Gen-Verse/LatentMAS: [ICML 2026 Spotlight] Latent Collaboration in Multi-Agent Systems · GitHub","url":"https://github.com/Gen-Verse/LatentMAS"},{"title":"Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/html/2511.20639v1"},{"title":"Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems","url":"https://arxiv.org/html/2604.21794"},{"title":"Paper page - Latent Collaboration in Multi-Agent Systems","url":"https://huggingface.co/papers/2511.20639"},{"title":"The Invisible AI Threat: Latent Collaboration's Efficiency Breakthrough and Dangerous Security Risks","url":"https://kenhuangus.substack.com/p/latentmas-ai-agents-collaborate-at"},{"title":"[2511.20639] Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/abs/2511.20639"},{"title":"[2604.13349] When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration","url":"https://arxiv.org/abs/2604.13349"},{"title":"Latent Collaboration in Multi-Agent Systems [Quick Review]","url":"https://liner.com/review/latent-collaboration-in-multiagent-systems"},{"title":"When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration","url":"https://arxiv.org/html/2604.13349"},{"title":"Recursive Multi-Agent Systems","url":"https://recursivemas.github.io/"}]

Based on the web search results, here's a comprehensive overview of these three latent communication frameworks for multi-agent LLM systems:

## LatentMAS

LatentMAS is an end-to-end training-free framework that enables pure latent collaboration among LLM agents. Each agent first performs auto-regressive latent thoughts generation through last-layer hidden embeddings, and a shared latent working memory then preserves and transfers each agent's internal representations, ensuring lossless information exchange. LatentMAS has been accepted into ICML 2026 as a spotlight.

Performance-wise, empirical evaluations across 9 comprehensive benchmarks spanning math and science reasoning, commonsense understanding, and code generation show that LatentMAS consistently outperforms strong single-model and text-based MAS baselines, achieving up to 14.6% higher accuracy, reducing output token usage by 70.8%-83.7%, and providing 4x-4.3x faster end-to-end inference.

## DiffMAS

DiffMAS is evaluated against three representative inference paradigms: single-model inference, text-based multi-agent systems (TextMAS), training-free latent multi-agent systems (LatentMAS), and cache-to-cache communication (C2C).

A key finding is that DiffMAS consistently achieves higher self-consistency than LatentMAS and TextMAS across both Qwen3-4B and Qwen3-8B, displaying a clear shift toward high-consistency outcomes (3–4 correct samples) across most problems, indicating more stable reasoning trajectories. Additionally, in DiffMAS, cross-agent latent states remain within a shared computation graph and are jointly optimized, allowing upstream representations to adapt and reduce downstream uncertainty.

## RecursiveMAS

RecursiveMAS is a recursive multi-agent framework that casts the entire system as a unified latent-space recursive computation, connecting heterogeneous agents as a collaboration loop through a lightweight RecursiveLink module, enabling in-distribution latent thoughts generation and cross-agent latent state transfer. RecursiveMAS achieves +8.3% accuracy, up to 2.4x speedup, and up to 75.6% fewer tokens across 9 benchmarks.

These three frameworks represent different approaches to enabling efficient multi-agent LLM collaboration through latent communication rather than text-based exchange.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2e7e8f3-7140-4328-85ee-a0e6cfcfc3fc",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "092c4cd5-300f-468c-96f9-691ad9f02851",
  "sourceToolAssistantUUID": "f2e7e8f3-7140-4328-85ee-a0e6cfcfc3fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-10T20:49:46.379Z_

The PDF was too large. Let me fetch more details from the HTML version and also get details on the comparison frameworks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "092c4cd5-300f-468c-96f9-691ad9f02851",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYhMUVg4NgMN69kDp28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35ee8edd-93a3-4889-915a-957efe35c67f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xio3CuGn9VDmSkYeJPz6nY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 43,
      "cache_creation_input_tokens": 2548,
      "cache_read_input_tokens": 15976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2548,
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

_source line 26 · 2026-05-10T20:49:49.320Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NiydhBW8hHJuz2MgshQ18P`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.09149v4",
  "prompt": "Focus ONLY on: 1) The Related Work section - what prior latent communication methods do they cite and discuss? Do they mention LatentMAS, RecursiveMAS, DiffMAS? 2) Limitations section 3) Any mention of what changed between v1-v4 revisions. 4) The conclusion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35ee8edd-93a3-4889-915a-957efe35c67f",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYhMUVg4NgMN69kDp28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c10748e-8edd-4bd9-93d4-8b1c624a9ff7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xio3CuGn9VDmSkYeJPz6nY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 43,
      "cache_creation_input_tokens": 2548,
      "cache_read_input_tokens": 15976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2548,
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

_source line 27 · 2026-05-10T20:49:51.224Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J7y5r2Z1XWVVrjdgMvAbJC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.20639",
  "prompt": "Extract details about LatentMAS: how does the shared working memory of last-layer embeddings work? What is the core mechanism? How does it compare to Interlat? What benchmarks are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c10748e-8edd-4bd9-93d4-8b1c624a9ff7",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYhMUVg4NgMN69kDp28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b8aae0e-1722-478d-b66a-b96747ca1376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xio3CuGn9VDmSkYeJPz6nY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 43,
      "cache_creation_input_tokens": 2548,
      "cache_read_input_tokens": 15976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2548,
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

_source line 28 · 2026-05-10T20:49:52.573Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UFNWwwaEmnaCsCWWBv4zWu`</summary>

```json
{
  "url": "https://recursivemas.github.io/",
  "prompt": "Extract all details about RecursiveMAS: what is the RecursiveLink module? How does it enable cross-agent latent state transfer? How does it compare to Interlat and LatentMAS?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b8aae0e-1722-478d-b66a-b96747ca1376",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYhMUVg4NgMN69kDp28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f6f45d1-15c3-43fb-8a22-36e4888ccc7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xio3CuGn9VDmSkYeJPz6nY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 43,
      "cache_creation_input_tokens": 2548,
      "cache_read_input_tokens": 15976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2548,
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

_source line 29 · 2026-05-10T20:49:54.344Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Su1SHK8EnDuhJ2fXr8gAyk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.13349",
  "prompt": "Extract details about DiffMAS or this compression method for latent multi-agent collaboration. What is the core mechanism? How does KV-cache trace construction work? How does it compare to LatentMAS and Interlat?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f6f45d1-15c3-43fb-8a22-36e4888ccc7f",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYhMUVg4NgMN69kDp28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0592924c-d3d4-459c-bf18-15d73644661f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xio3CuGn9VDmSkYeJPz6nY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 43,
      "cache_creation_input_tokens": 2548,
      "cache_read_input_tokens": 15976,
      "output_tokens": 517,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2548
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 43,
          "output_tokens": 517,
          "cache_read_input_tokens": 15976,
          "cache_creation_input_tokens": 2548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2548,
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

_source line 30 · 2026-05-10T20:49:56.592Z_

<details><summary>↩ Tool result · `toolu_01NiydhBW8hHJuz2MgshQ18P`</summary>

```text
# Analysis of arXiv Paper 2511.09149v4

## 1. Related Work Section - Prior Latent Communication Methods

The paper cites several latent communication approaches but does **not mention LatentMAS, RecursiveMAS, or DiffMAS**.

Cited prior latent communication methods include:

- **Pham et al. (2023)**: "Let models speak ciphers" - transmits "probability-weighted tokenizer embeddings"
- **Ramesh and Li (2025)**: "Communicating activations between language model agents" - uses "one-shot activation grafting" or "blends hidden activations between agents"
- **Tang et al. (2025)**: "Augmenting multi-agent communication with state delta trajectory" - communicates "per-token latent deltas tied to language trajectories"
- **Zheng et al. (2025)**: "Thought communication in multiagent collaboration" - infers "latent 'thoughts' from hidden states via an autoencoder"

The authors note their approach differs because they "directly transmit temporally aligned sequences of last hidden states" without requiring "parameter sharing," "memory coupling," or "cache synchronization."

## 2. Limitations Section

Key limitations acknowledged:

- Experiments "mainly focus on a controlled two-agent setting" on limited benchmarks (ALFWorld, MATH)
- Requires "access to internal model representations" - inapplicable to "closed-source or API-only models"
- "Latent communication trades human interpretability for efficiency" - messages are "not directly human-readable," complicating "debugging, monitoring, and failure analysis"

## 3. Version Changes (v1-v4)

The document provides **no explicit changelog** describing modifications between revisions.

## 4. Conclusion

The authors position this as "an initial yet concrete step toward understanding and enabling inter-agent communication beyond language." They highlight that "latent space communication can support effective coordination and can be aggressively compressed while preserving task utility," suggesting it represents "a complementary paradigm to language-based interaction in LLM-powered agent systems."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c10748e-8edd-4bd9-93d4-8b1c624a9ff7",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "ab2ee28d-9b46-4665-aab4-2565d8aadc2b",
  "sourceToolAssistantUUID": "3c10748e-8edd-4bd9-93d4-8b1c624a9ff7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T20:49:57.086Z_

<details><summary>↩ Tool result · `toolu_01J7y5r2Z1XWVVrjdgMvAbJC`</summary>

```text
# LatentMAS: Key Details

## Core Mechanism
LatentMAS enables agents to collaborate directly within continuous latent space rather than through text-based communication. The framework operates through:

1. **Latent Thought Generation**: Each agent performs "auto-regressive latent thoughts generation through last-layer hidden embeddings"
2. **Shared Working Memory**: A "shared latent working memory" preserves and transfers internal representations between agents, ensuring "lossless information exchange"

## Advantages Over Text-Based MAS
The paper claims LatentMAS achieves:
- Higher expressiveness and lossless information preservation
- "Substantially lower complexity than vanilla text-based MAS"
- Up to 14.6% higher accuracy
- 70.8%-83.7% reduction in output token usage
- 4x-4.3x faster end-to-end inference

## Benchmarks Used
Testing spans 9 comprehensive benchmarks across:
- Math and science reasoning
- Commonsense understanding
- Code generation

## Note on Interlat
The provided content does **not mention Interlat** or any comparison to it, so I cannot address that comparison based on this source material.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b8aae0e-1722-478d-b66a-b96747ca1376",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "97bdd4eb-e206-4e2a-a47f-73e45940bd72",
  "sourceToolAssistantUUID": "2b8aae0e-1722-478d-b66a-b96747ca1376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T20:49:58.516Z_

<details><summary>↩ Tool result · `toolu_01Su1SHK8EnDuhJ2fXr8gAyk`</summary>

```text
# Analysis of the Paper

Based on the provided arXiv page, I can share the following:

## Core Mechanism

The paper introduces **Orthogonal Backfill (OBF)**, a compression technique for multi-agent LLM collaboration. Rather than relaying full key-value caches between agents, OBF applies "eviction-style KV compression" while mitigating information loss through "a low-rank orthogonal residual from discarded KV states injected into the retained KV states."

## Key Findings

The method achieves "performance comparable to full KV relay while reducing communication cost by 79.8%--89.4%" across nine benchmarks. Notably, OBF "improves the performance and achieves the best results on 7 of the 9 benchmarks," suggesting selective information preservation outperforms transmitting complete context.

## Limitations of Available Information

The arXiv abstract does not provide sufficient technical detail about:
- KV-cache trace construction specifics
- Detailed comparisons with LatentMAS or Interlat methods
- The mathematical foundations of the orthogonal residual approach

For comprehensive technical details on these aspects, consulting the full PDF paper would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0592924c-d3d4-459c-bf18-15d73644661f",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "152618ad-3c0d-411f-8e01-aa4f4acb2bf3",
  "sourceToolAssistantUUID": "0592924c-d3d4-459c-bf18-15d73644661f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T20:50:00.513Z_

<details><summary>↩ Tool result · `toolu_01UFNWwwaEmnaCsCWWBv4zWu`</summary>

```text
# RecursiveMAS: Key Components

## RecursiveLink Module

The RecursiveLink is "a small two-layer residual module that transmits an agent's last-layer hidden states" across two types of transitions:

**Inner Link:** Maps hidden states back into input embedding space, enabling agents to generate continuous latent thoughts without converting to tokens.

**Outer Link:** Adds projection functionality allowing latent outputs from one agent to serve as conditioning inputs for another agent, even when they have different hidden dimensions.

The residual design preserves original semantic content, requiring the module to learn only distributional shifts—enhancing training stability.

## Cross-Agent Latent State Transfer

RecursiveMAS chains agents into a recursive loop where:
- Each agent uses its inner link for latent thought generation
- The outer link forwards these latent thoughts to the next agent as conditioning input
- The final agent's outputs loop back to the first agent
- "Only the final round decodes text—all intermediate rounds collaborate purely in latent space"

## Comparison to Other Approaches

The document contains **no mentions of "Interlat" or "LatentMAS"** frameworks. It compares RecursiveMAS against established baselines including Mixture-of-Agents, TextGrad, LoopLM, and Recursive-TextMAS—showing consistent improvements like +8.3% average accuracy and 2.4× speedup.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f6f45d1-15c3-43fb-8a22-36e4888ccc7f",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "38c27351-59a3-4e07-8429-865ddee65750",
  "sourceToolAssistantUUID": "2f6f45d1-15c3-43fb-8a22-36e4888ccc7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-10T20:50:04.316Z_

Now let me get one final piece -- the ACL 2026 accepted papers list to verify acceptance, and check if there's a blog or discussion that compares these methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38c27351-59a3-4e07-8429-865ddee65750",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYitMeL2LZzMPJVEP3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d74614a-acb0-4252-afa3-9f648d73c2e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LANey7MLEmEkVrv1NtCk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 304,
      "cache_creation_input_tokens": 1711,
      "cache_read_input_tokens": 18524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1711,
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

_source line 35 · 2026-05-10T20:50:06.793Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Mhwyy1a3MDhbRqWooJ1dUJ`</summary>

```json
{
  "url": "https://2026.aclweb.org/program/accepted_papers/",
  "prompt": "Search the list of accepted papers for 'Interlat' or 'Enabling Agents to Communicate Entirely in Latent Space' or 'Zhuoyun Du'. Is this paper on the accepted list? What category (main conference, findings, etc.)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d74614a-acb0-4252-afa3-9f648d73c2e1",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYitMeL2LZzMPJVEP3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df5bdd93-9673-4643-8b41-1237e31eaf27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LANey7MLEmEkVrv1NtCk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 304,
      "cache_creation_input_tokens": 1711,
      "cache_read_input_tokens": 18524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1711,
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

_source line 36 · 2026-05-10T20:50:07.085Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018pQ2K3cXGSxd2rKJtrDEZY`</summary>

```json
{
  "query": "\"Interlat\" vs \"LatentMAS\" latent multi-agent communication comparison 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df5bdd93-9673-4643-8b41-1237e31eaf27",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYitMeL2LZzMPJVEP3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae700479-fcd4-4470-8ac2-c6bd0c85c958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LANey7MLEmEkVrv1NtCk4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 304,
      "cache_creation_input_tokens": 1711,
      "cache_read_input_tokens": 18524,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 304,
          "output_tokens": 243,
          "cache_read_input_tokens": 18524,
          "cache_creation_input_tokens": 1711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1711,
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

_source line 37 · 2026-05-10T20:50:09.341Z_

<details><summary>↩ Tool result · `toolu_01Mhwyy1a3MDhbRqWooJ1dUJ`</summary>

```text
Based on the web page content provided, I cannot determine whether the paper you're asking about is on the accepted list. The page simply states "Coming soon!" under the Accepted Papers section, meaning the actual list of accepted papers has not yet been published.

To find this information, you would need to check back at the ACL 2026 website once the accepted papers list becomes available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df5bdd93-9673-4643-8b41-1237e31eaf27",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "39aa1e90-6cab-4f0a-9cc2-6fa09ec2c0a8",
  "sourceToolAssistantUUID": "df5bdd93-9673-4643-8b41-1237e31eaf27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T20:50:15.595Z_

<details><summary>↩ Tool result · `toolu_018pQ2K3cXGSxd2rKJtrDEZY`</summary>

```text
Web search results for query: ""Interlat" vs "LatentMAS" latent multi-agent communication comparison 2026"

Links: [{"title":"GitHub - Gen-Verse/LatentMAS: [ICML 2026 Spotlight] Latent Collaboration in Multi-Agent Systems · GitHub","url":"https://github.com/Gen-Verse/LatentMAS"},{"title":"Enabling Agents to Communicate Entirely in Latent Space | OpenReview","url":"https://openreview.net/forum?id=rmYbgsehTd"},{"title":"[2511.09149] Enabling Agents to Communicate Entirely in Latent Space","url":"https://arxiv.org/abs/2511.09149"},{"title":"[2511.20639] Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/abs/2511.20639"},{"title":"Enabling Agents to Communicate Entirely in Latent Space","url":"https://arxiv.org/html/2511.09149"},{"title":"Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/html/2511.20639v1"},{"title":"The Invisible AI Threat: Latent Collaboration's Efficiency Breakthrough and Dangerous Security Risks","url":"https://kenhuangus.substack.com/p/latentmas-ai-agents-collaborate-at"},{"title":"Paper page - Latent Collaboration in Multi-Agent Systems","url":"https://huggingface.co/papers/2511.20639"},{"title":"Latent Collaboration in Multi-Agent Systems","url":"https://www.emergentmind.com/papers/2511.20639"},{"title":"[2604.13349] When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration","url":"https://arxiv.org/abs/2604.13349"}]

Based on the search results, I found detailed information about both Interlat and LatentMAS, two recent approaches to latent multi-agent communication:

## **Interlat (Inter-agent Latent Space Communication)**

Interlat proposes a paradigm that leverages the last hidden states of an LLM as a representation of its mind for direct communication (termed "latent communication"). Inspired by telepathy, it leverages the continuous last hidden states of an LLM as a representation of its thought for direct communication, with an additional learned compression process that further compresses latent communication via latent space reasoning.

**Performance:** Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, promoting more exploratory behavior and enabling genuine utilization of latent information. Further compression not only substantially accelerates inference by up to 24 times but also maintains competitive performance through an efficient information-preserving mechanism.

## **LatentMAS (Latent Collaboration in Multi-Agent Systems)**

LatentMAS has been accepted into ICML 2026 as a spotlight. LatentMAS is an end-to-end training-free framework that enables pure latent collaboration among LLM agents, where each agent performs auto-regressive latent thoughts generation through last-layer hidden embeddings, and a shared latent working memory preserves and transfers each agent's internal representations, ensuring lossless information exchange.

**Performance:** LatentMAS consistently outperforms strong single-model and text-based MAS baselines, achieving up to 14.6% higher accuracy, reducing output token usage by 70.8%-83.7%, and providing 4x-4.3x faster end-to-end inference.

## **Key Theoretical Differences**

LatentMAS provides theoretical analyses establishing that it attains higher expressiveness and lossless information preservation with substantially lower complexity than vanilla text-based MAS.

Both approaches represent significant advances in enabling agents to communicate without converting thoughts to text, with LatentMAS emphasizing training-free operation and LatentMAS focusing on compression techniques for efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae700479-fcd4-4470-8ac2-c6bd0c85c958",
  "isSidechain": true,
  "promptId": "863e88ec-80da-4b68-8ecb-81ec44d16434",
  "agentId": "a6eccb847c5a694e7",
  "type": "user",
  "uuid": "f82c429d-4074-4269-89dc-0887bc0a530d",
  "sourceToolAssistantUUID": "ae700479-fcd4-4470-8ac2-c6bd0c85c958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-10T20:51:37.144Z_

I now have comprehensive information. Here is the detailed report.

---

## Interlat: "Enabling Agents to Communicate Entirely in Latent Space" (Du et al., arXiv 2511.09149)

### Paper Metadata
- **Authors:** Zhuoyun Du, Runze Wang, Huiyu Bai, Zouying Cao, Xiaoyong Zhu, Yu Cheng, Bo Zheng, Wei Chen, Haochao Ying
- **Submitted:** November 12, 2025 (v1)
- **Latest revision:** v4, April 16, 2026
- **Venue claim:** The arXiv abstract page states "Accepted to ACL 2026," though the ACL 2026 accepted papers list has not yet been published (it says "Coming soon!"). The OpenReview submission (rmYbgsehTd) shows status "Withdrawn Submission," suggesting the paper may have been withdrawn from one venue (e.g., an ARR cycle) and submitted/accepted elsewhere.

---

### 1. Core Mechanism for Inter-Agent Latent Communication

Interlat replaces natural-language message-passing between agents with **direct transmission of last-layer hidden states**.

**How it works step by step:**

1. **Hidden state extraction:** When an agent generates a response, the system collects the last-layer hidden state **h_l in R^d** from the transformer at each token position (immediately before predicting the next token). These are assembled into a matrix **H in R^(L x d)** where L is the sequence length.

2. **Transmission:** Special boundary tokens `&lt;bop>` (beginning of plan) and `&lt;eop>` (end of plan) demarcate the latent message region. The receiving agent's input becomes: `[e(x_1), ..., e(x_i), h_1, h_2, ..., h_L, e(x_j)]` -- i.e., continuous hidden-state vectors are spliced directly into the embedding sequence in place of discrete token embeddings.

3. **Communication adapter:** A **trainable lightweight self-attention layer + projection layer** sits at the receiver. This adapter rescales and reinterprets the incoming latent states before the receiving model processes them. This is what enables cross-architecture communication.

4. **No parameter sharing or memory coupling required** -- the adapter provides sufficient bridging that latent semantics transfer even across model families.

---

### 2. Compression / Transfer of Hidden States

Interlat includes a dedicated **compression module** for reducing latent message length:

- **Architecture:** A separate reasoning model M_phi generates compact latent messages **H_K in R^(K x d)** where K is much smaller than L. It works by **autoregressive reasoning entirely in latent space** -- feeding its own last hidden state back as the next input embedding through a lightweight projection: `M_phi(E_i) -> h_i, E_{i+1} = E_i + Proj(h_i)`.

- **Compression ratio:** Full messages of 128 latent tokens can be compressed to as few as **8 tokens** while maintaining competitive performance, achieving up to **24x reduction in communication latency** (from 9.19s to 0.39s).

- **Training loss (three components):**
  - **Task loss (L_task):** Cross-entropy ensuring downstream utility of compressed messages.
  - **Preference loss (L_pref):** Uncertainty-weighted KL divergence aligning compressed and full behaviors at positions where latents reduce uncertainty.
  - **Geometry loss (L_geom):** Cosine similarity maintaining directional alignment between compressed and full representations: `L_geom = 1 - cos(z_bar^A, z_bar^D)`.

**Actor training** also uses a multi-component loss: `L_total = L_task + lambda_S * L_sep + lambda_A * L_align`, where:
- **Conditional thought separation (L_sep):** Minimizes weighted Jensen-Shannon divergence between matched and mismatched latent inputs, ensuring the receiver distinguishes relevant from irrelevant latent messages.
- **Plan-aligned regulation (L_align):** Regularizes against language-space plans to prevent exploiting the separation objective.
- A **token-to-latent curriculum** stochastically replaces early communication positions with corresponding plan token embeddings (replacement rate r in {0, 0.1, ..., 1.0}).

---

### 3. Benchmarks and Results

**ALFWorld (embodied household tasks):**

| Model Config | Seen (%) | Unseen (%) | Steps (Succ/All) |
|---|---|---|---|
| Interlat (Qwen2.5-7B) | **70.48** | **65.42** | 9.41 / 12.54 |
| Text CoT (fine-tuned) | 64.29 | 62.44 | 8.76 / 12.77 |
| No Communication | 62.14 | 62.19 | 10.19 / 13.90 |
| CoT (full) | 67.14 | 64.93 | 8.15 / 12.04 |

Consistent gains across three backbones (Qwen2.5-7B, Qwen2.5-0.5B, LLaMA3.1-8B).

**MATH benchmark:**

| Method | Overall | Level-3 | Level-4 | Level-5 |
|---|---|---|---|---|
| Interlat | 36.88% | 40.08% | 27.45% | **15.80%** |
| CoT (full) | 38.35% | 45.65% | 31.19% | 15.05% |
| Text | 34.35% | 37.60% | 26.30% | 14.20% |

Interlat surpasses CoT specifically on the hardest Level-5 problems.

**Compression results (Qwen2.5-7B, ALFWorld):**

| Latent Length | Seen (%) | Unseen (%) | Latency |
|---|---|---|---|
| Full (128) | 68.10 | 62.94 | 2.25s |
| 64 | 67.14 | 61.94 | 1.16s |
| 8 | 66.43 | 60.45 | 0.20s |

**Heterogeneous model results:** Feeding Qwen-derived latents to train a LLaMA actor yielded **70.95% seen / 71.39% unseen** -- actually slightly better than homogeneous Qwen-to-Qwen, demonstrating cross-family latent transfer works.

---

### 4. Comparison to LatentMAS, RecursiveMAS, and DiffMAS (OBF)

Interlat does **not** directly cite or compare against LatentMAS, RecursiveMAS, or DiffMAS. These are all contemporaneous works (late 2025 / early 2026). Here is a structured comparison based on my research:

| Dimension | **Interlat** | **LatentMAS** | **RecursiveMAS** | **DiffMAS/OBF** |
|---|---|---|---|---|
| **Venue** | ACL 2026 (claimed) | ICML 2026 Spotlight | -- | arXiv Apr 2026 |
| **What is transmitted** | Last-layer hidden states (full sequence) | Last-layer hidden embeddings via shared working memory | Last-layer hidden states via RecursiveLink module | Compressed KV-cache with orthogonal residual backfill |
| **Training required?** | Yes (adapter + compression module) | **Training-free** | Yes (lightweight RecursiveLink, 2-layer residual module) | Yes (eviction-style compression) |
| **Compression** | Autoregressive latent-space reasoning; down to 8 tokens (24x speedup) | No explicit compression -- full latent thoughts shared | Implicit via RecursiveLink projection | Orthogonal Backfill (OBF): 79.8-89.4% KV-cache reduction |
| **Cross-architecture** | Yes, via communication adapter (Qwen -> LLaMA demonstrated) | Not emphasized | Yes, outer link handles different hidden dimensions | Not specified |
| **Memory mechanism** | Direct injection into embedding sequence | Shared latent working memory pool | Recursive loop: agents chain via inner/outer links | KV-cache relay with compressed traces |
| **Key insight** | Temporally aligned hidden states as "thought representation"; aggressive compression preserves task utility | Lossless information exchange through shared memory; no training needed | Entire system as unified recursive latent computation; only final round decodes text | Selective information preservation via orthogonal residual from discarded KV states outperforms full relay |
| **Benchmarks** | ALFWorld, MATH (2 benchmarks) | 9 benchmarks (math, science, commonsense, code) | 9 benchmarks | 9 benchmarks |
| **Best claimed gain** | +6% over no-comm on ALFWorld; 24x latency reduction | +14.6% accuracy; 70-84% token reduction; 4-4.3x speedup | +8.3% accuracy; 2.4x speedup; 75.6% fewer tokens | Comparable to full relay at 79-89% communication cost reduction |

**Key architectural distinctions:**

- **Interlat** is the most focused on **compression of latent messages** -- its autoregressive latent-space reasoning module that iteratively generates compact latent summaries is unique. It also provides the most detailed analysis of *what the latent messages encode* (ablations with CrossTask, CovGauss, RandomRot noise showing reliance on geometric structure).

- **LatentMAS** is the only **training-free** approach, using a shared working memory pool. This is a major practical advantage but means it cannot optimize the latent representations for the communication task.

- **RecursiveMAS** casts the multi-agent system as a **single recursive computation graph** with RecursiveLink modules (2-layer residual networks) bridging agents. Its inner/outer link distinction (inner for self-latent-thought, outer for cross-agent transfer) is architecturally distinct from Interlat's single communication adapter.

- **DiffMAS/OBF** operates at the **KV-cache level** rather than hidden-state level, using eviction-style compression with orthogonal residual backfill from discarded states. This is a fundamentally different communication substrate.

---

### 5. Revision History

The paper went through four versions:
- **v1:** November 12, 2025 (initial submission)
- **v2:** January 7, 2026
- **v3:** January 21, 2026
- **v4:** April 16, 2026

The paper provides **no explicit changelog** between versions. The April 2026 revision (v4) likely corresponds to a camera-ready or post-acceptance revision. The comprehensive appendices (A through H) in the current version suggest iterative expansion of experimental analysis and ablation studies across revisions. The OpenReview submission (rmYbgsehTd) is marked "Withdrawn Submission," which is consistent with withdrawing from one review cycle (possibly ICLR or an ARR cycle) to submit to ACL.

---

### 6. Limitations Acknowledged by the Authors

- Experiments focus on a **controlled two-agent setting** with only two benchmarks (ALFWorld, MATH) -- narrower evaluation than LatentMAS/RecursiveMAS (9 benchmarks each).
- Requires **access to internal model representations** -- inapplicable to closed-source or API-only models.
- Latent messages are **not human-readable**, complicating debugging, monitoring, and failure analysis.

---

### Summary for Your Landscape Analysis

Interlat's distinctive contribution to the latent multi-agent communication landscape is its **compression pipeline** -- the autoregressive latent-space reasoning module with the three-component loss (task + preference + geometry) that enables 24x compression while preserving task performance. It is the paper most focused on demonstrating that latent communication can be *aggressively compressed*. However, its evaluation scope is notably narrower than competing methods (2 vs. 9 benchmarks), and it requires training (unlike LatentMAS). The cross-architecture results (Qwen-to-LLaMA) are a strength shared with RecursiveMAS but not demonstrated in LatentMAS or OBF.

Sources:
- [Interlat - arXiv page](https://arxiv.org/abs/2511.09149)
- [Interlat - HTML full text](https://arxiv.org/html/2511.09149v4)
- [Interlat - OpenReview](https://openreview.net/forum?id=rmYbgsehTd)
- [LatentMAS - arXiv](https://arxiv.org/abs/2511.20639)
- [LatentMAS - GitHub](https://github.com/Gen-Verse/LatentMAS)
- [RecursiveMAS - Project page](https://recursivemas.github.io/)
- [OBF/DiffMAS compression - arXiv](https://arxiv.org/abs/2604.13349)
- [ACL 2026 Accepted Papers (not yet published)](https://2026.aclweb.org/program/accepted_papers/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f82c429d-4074-4269-89dc-0887bc0a530d",
  "isSidechain": true,
  "agentId": "a6eccb847c5a694e7",
  "requestId": "req_011CauYjzsLdiyjcSeUViYjb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6577671a-cfe8-449a-a937-8f0dd6f9018d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0193cec-8a3a-4441-80b6-a0e385e9422b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NktMfkmvbAGiQw1rz4U5t6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1665,
      "cache_read_input_tokens": 20235,
      "output_tokens": 3268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1665
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3268,
          "cache_read_input_tokens": 20235,
          "cache_creation_input_tokens": 1665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1665,
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
