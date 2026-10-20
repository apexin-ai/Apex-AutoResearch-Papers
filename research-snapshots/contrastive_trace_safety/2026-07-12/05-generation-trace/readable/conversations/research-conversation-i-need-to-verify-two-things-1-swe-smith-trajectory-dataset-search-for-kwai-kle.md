# Research conversation: I need to verify two things: 1. SWE-smith trajectory dataset: Search for "Kwai-Klear/SWE-smith-mini_swe_agent_plus-traje

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a859236b7efeb0da8.jsonl`
- **Structured JSON:** [`ffc54fb81abf1daa5471.json`](../../sessions/ff/ffc54fb81abf1daa5471.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-10T18:31:47.675Z_

I need to verify two things:

1. SWE-smith trajectory dataset: Search for "Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k" on HuggingFace or the web. Is this dataset publicly available? Also search for "SWE-smith NeurIPS 2025" to verify the paper.

2. Agent-RLVR (arXiv:2506.11425, June 2026): This paper is claimed to be from June 2026, but today is May 2026. Search for "Agent-RLVR arXiv 2506.11425" and "Training SWE Agents via Guidance and Environment Rewards". Does this paper actually exist? A June 2026 arXiv ID would be suspicious since we're in May 2026.

3. Also search for "When Agents Go Astray SWE-PRM arXiv 2509.02360" - this was flagged as a potentially missing competitor. Verify it exists and what it does.

Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a859236b7efeb0da8",
  "type": "user",
  "uuid": "09e483b9-8c31-413b-b1c2-7e2ff2badb33",
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

_source line 2 · 2026-05-10T18:31:47.685Z_

```json
{
  "parentUuid": "09e483b9-8c31-413b-b1c2-7e2ff2badb33",
  "isSidechain": true,
  "agentId": "a859236b7efeb0da8",
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
  "uuid": "8222ae84-167c-4f31-8415-a4ee14e03a47",
  "timestamp": "2026-05-10T18:31:47.685Z",
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

_source line 3 · 2026-05-10T18:31:50.926Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Sgw1t7dyFsnPTN9q1UcnG7`</summary>

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
  "parentUuid": "8222ae84-167c-4f31-8415-a4ee14e03a47",
  "isSidechain": true,
  "agentId": "a859236b7efeb0da8",
  "requestId": "req_011CauNBb44NJoqzMdcCb7nW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7fff195-4c50-4fdc-8a3b-85dd7482535c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4MLEisWkLTQxjpAy9o2F2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 801
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 801,
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

_source line 4 · 2026-05-10T18:31:50.931Z_

<details><summary>↩ Tool result · `toolu_01Sgw1t7dyFsnPTN9q1UcnG7`</summary>

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
  "parentUuid": "f7fff195-4c50-4fdc-8a3b-85dd7482535c",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a859236b7efeb0da8",
  "type": "user",
  "uuid": "0fd9b16b-4f63-4c30-954f-dcdd2053a6f8",
  "sourceToolAssistantUUID": "f7fff195-4c50-4fdc-8a3b-85dd7482535c",
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

_source line 5 · 2026-05-10T18:31:54.269Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018W7gSyRyLeiD4h7AcpsCe4`</summary>

```json
{
  "query": "Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k HuggingFace dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fd9b16b-4f63-4c30-954f-dcdd2053a6f8",
  "isSidechain": true,
  "agentId": "a859236b7efeb0da8",
  "requestId": "req_011CauNBq4g9qCZKbJFfKZpm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6da54991-81d4-4313-89bb-982467d0b7ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REasDSbP3YHjeiLA1PQo1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T18:31:54.787Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Peip2ZT2L3MDjmEZ8yoSeg`</summary>

```json
{
  "query": "SWE-smith NeurIPS 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6da54991-81d4-4313-89bb-982467d0b7ea",
  "isSidechain": true,
  "agentId": "a859236b7efeb0da8",
  "requestId": "req_011CauNBq4g9qCZKbJFfKZpm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bea5598-2447-48b6-be2d-bed63a1a63f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REasDSbP3YHjeiLA1PQo1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T18:31:55.270Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YcT9ApXqSa8PXjebN4vaee`</summary>

```json
{
  "query": "Agent-RLVR arXiv 2506.11425 \"Training SWE Agents via Guidance and Environment Rewards\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bea5598-2447-48b6-be2d-bed63a1a63f1",
  "isSidechain": true,
  "agentId": "a859236b7efeb0da8",
  "requestId": "req_011CauNBq4g9qCZKbJFfKZpm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3082cfb-bb54-43cf-9103-4c478d4885f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REasDSbP3YHjeiLA1PQo1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T18:31:55.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FjSYsyq9ZSwtsYYnP4LQjA`</summary>

```json
{
  "query": "\"When Agents Go Astray\" SWE-PRM arXiv 2509.02360"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3082cfb-bb54-43cf-9103-4c478d4885f3",
  "isSidechain": true,
  "agentId": "a859236b7efeb0da8",
  "requestId": "req_011CauNBq4g9qCZKbJFfKZpm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbad461f-302c-44a5-b292-1a909558e899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REasDSbP3YHjeiLA1PQo1f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9024,
      "output_tokens": 259,
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
          "output_tokens": 259,
          "cache_read_input_tokens": 9024,
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

_source line 9 · 2026-05-10T18:32:00.892Z_

<details><summary>↩ Tool result · `toolu_018W7gSyRyLeiD4h7AcpsCe4`</summary>

```text
Web search results for query: "Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k HuggingFace dataset"

Links: [{"title":"Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k"},{"title":"mini-swe-agent-plus - a Kwai-Klear Collection","url":"https://huggingface.co/collections/Kwai-Klear/mini-swe-agent-plus"},{"title":"GitHub - Kwai-Klear/mini-swe-agent-plus: mini-swe-agent-plus: a tiny (~100 LOC) GitHub issue fixer—now with a robust multi-line text edit tool.","url":"https://github.com/Kwai-Klear/mini-swe-agent-plus"},{"title":"Kwai-Klear (Klear team, Kuaishou Technology)","url":"https://huggingface.co/Kwai-Klear"},{"title":"Klear-AgentForge - a Kwai-Klear Collection","url":"https://huggingface.co/collections/Kwai-Klear/klear-agentforge"},{"title":"SWE-bench/SWE-smith-trajectories · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SWE-bench/SWE-smith-trajectories"},{"title":"JetBrains-Research/agent-trajectories-swesmith-random-subset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/JetBrains-Research/agent-trajectories-swesmith-random-subset"},{"title":"SWE-bench/SWE-agent-LM-32B · Hugging Face","url":"https://huggingface.co/SWE-bench/SWE-agent-LM-32B"},{"title":"Running on SWE-Smith instances · Issue #1233 · SWE-agent/SWE-agent","url":"https://github.com/SWE-agent/SWE-agent/issues/1233"},{"title":"README.md · SWE-bench/SWE-smith-trajectories at main","url":"https://huggingface.co/datasets/SWE-bench/SWE-smith-trajectories/blob/main/README.md"}]

Based on the search results, here's what I found about the Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k HuggingFace dataset:

## Dataset Overview

The dataset contains 65,994 rows with a total size of 1.58 GB.

## Purpose and Training

This is a collection of mini-swe-agent-plus and corresponding rollout traces that drive Qwen3-8B to a 39% solve rate on SWE-bench Verified. The collection includes 66k trajectories based on SWE-smith and studies model performance with different data scaling.

## Performance Results

The solve rate on SWE-bench Verified improves approximately linearly with the logarithm of the data scale (1k → 66k trajectories). Klear-Agent-8B trained on this dataset with mini-swe-agent-plus significantly outperforms other ~8B models and matches several open 32B systems.

## Training Methodology

The approach uses effective supervised fine-tuning (SFT) with synthetic data followed by multi-turn reinforcement learning (RL) for boosting agentic models.

You can access the dataset directly on Hugging Face at the URL you provided to load it using the HuggingFace datasets library.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6da54991-81d4-4313-89bb-982467d0b7ea",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a859236b7efeb0da8",
  "type": "user",
  "uuid": "42c837ce-65fd-4f94-a141-0e59aab19341",
  "sourceToolAssistantUUID": "6da54991-81d4-4313-89bb-982467d0b7ea",
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

_source line 10 · 2026-05-10T18:32:01.251Z_

<details><summary>↩ Tool result · `toolu_01YcT9ApXqSa8PXjebN4vaee`</summary>

```text
Web search results for query: "Agent-RLVR arXiv 2506.11425 "Training SWE Agents via Guidance and Environment Rewards""

Links: [{"title":"[2506.11425] Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards","url":"https://arxiv.org/abs/2506.11425"},{"title":"Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards","url":"https://arxiv.org/html/2506.11425v1"},{"title":"Agent-RLVR: Training Software Engineering Agents via ...","url":"https://arxiv.org/pdf/2506.11425"},{"title":"(PDF) Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards","url":"https://www.researchgate.net/publication/392717328_Agent-RLVR_Training_Software_Engineering_Agents_via_Guidance_and_Environment_Rewards"},{"title":"Agent-RLVR - Scale Labs | Scale Labs","url":"https://labs.scale.com/papers/agent_rlvr"},{"title":"Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.11425v2"},{"title":"Internalizing Agency from Reflective Experience","url":"https://arxiv.org/html/2603.16843"},{"title":"Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards - haebom","url":"https://slashpage.com/haebom/daily_arxiv?lang=en&tl=en&post=36nj8v2wke3xw25ykq9z"},{"title":"Agent-RLVR","url":"https://scale.com/research/agent_rlvr"},{"title":"Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards","url":"https://paperreading.club/page?id=316243"}]

I found the paper! Here's a summary of Agent-RLVR (arXiv 2506.11425):

## Overview

Agent-RLVR is a framework that makes RLVR (Reinforcement Learning from Verifiable Rewards) effective in challenging agentic settings, with an initial focus on software engineering tasks.

## The Problem

While RLVR has been widely adopted and demonstrated notable success in verifiable domains like math and competitive programming tasks, its efficacy diminishes significantly when applied to agentic environments. These settings, characterized by multi-step, complex problem solving, lead to high failure rates even for frontier LLMs, as the reward landscape is too sparse for effective model training via conventional RLVR.

## The Solution: Agent Guidance

Inspired by human pedagogy, Agent-RLVR introduces agent guidance, a mechanism that actively steers the agent towards successful trajectories by leveraging diverse informational cues. These cues, ranging from high-level strategic plans to dynamic feedback on the agent's errors and environmental interactions, emulate a teacher's guidance, enabling the agent to navigate difficult solution spaces and promotes active self-improvement via additional environment exploration.

## Training Loop

In the Agent-RLVR training loop, agents first attempt to solve tasks to produce initial trajectories, which are then validated by unit tests and supplemented with agent guidance. Agents then reattempt with guidance, and the agent policy is updated with RLVR based on the rewards of these guided trajectories.

## Results

Agent-RLVR elevates the pass@1 performance of Qwen-2.5-72B-Instruct from 9.4% to 22.4% on SWE-Bench Verified. Additionally, the guidance-augmented RLVR data is useful for test-time reward model training, further boosting pass@1 to 27.8%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3082cfb-bb54-43cf-9103-4c478d4885f3",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a859236b7efeb0da8",
  "type": "user",
  "uuid": "7ee8ba2d-bc33-42b7-95a2-9659ccf8a9e1",
  "sourceToolAssistantUUID": "d3082cfb-bb54-43cf-9103-4c478d4885f3",
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

_source line 11 · 2026-05-10T18:32:03.299Z_

<details><summary>↩ Tool result · `toolu_01FjSYsyq9ZSwtsYYnP4LQjA`</summary>

```text
Web search results for query: ""When Agents Go Astray" SWE-PRM arXiv 2509.02360"

Links: [{"title":"[2509.02360] When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/abs/2509.02360"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/html/2509.02360"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs Shubham Gandhi∗","url":"https://arxiv.org/pdf/2509.02360"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250902360G/abstract"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs | OpenReview","url":"https://openreview.net/forum?id=wyrcoDNaGO"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/when-agents-go-astray-course-correcting-swe-agents-with-prms"}]

I found the paper! Here's what I found about "When Agents Go Astray: Course-Correcting SWE Agents with PRMs" (arXiv 2509.02360):

## Overview
SWE-PRM is an inference-time Process Reward Model (PRM) that intervenes during execution to detect and course-correct trajectory-level errors.

## The Problem
Large Language Model (LLM) agents are increasingly deployed for complex, multi-step software engineering (SWE) tasks, but their trajectories often contain costly inefficiencies, such as redundant exploration, looping, and failure to terminate once a solution is reached. Prior work has largely treated these errors in a post-hoc manner, diagnosing failures only after execution.

## The Solution
The PRM design leverages a taxonomy of common inefficiencies and delivers lightweight, interpretable feedback without modifying the underlying policy. This is the first application of PRMs for real-time trajectory-level error correction in SWE agents.

## Results
On SWE-bench Verified, closed-source PRMs improve resolution from 40.0% to 50.6% (+10.6 p.p.), with the largest gains on medium and hard tasks. These benefits come at an acceptable added inference cost of as low as $0.2, making PRMs a practical and scalable mechanism for improving SWE agents' reliability and efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbad461f-302c-44a5-b292-1a909558e899",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a859236b7efeb0da8",
  "type": "user",
  "uuid": "8dd4a066-6ea3-4e0b-b5d4-27337761d628",
  "sourceToolAssistantUUID": "bbad461f-302c-44a5-b292-1a909558e899",
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

_source line 12 · 2026-05-10T18:32:04.253Z_

<details><summary>↩ Tool result · `toolu_01Peip2ZT2L3MDjmEZ8yoSeg`</summary>

```text
Web search results for query: "SWE-smith NeurIPS 2025 paper"

Links: [{"title":"GitHub - SWE-bench/SWE-smith: [NeurIPS 2025 D&B Spotlight] Scaling Data for SWE-agents · GitHub","url":"https://github.com/SWE-bench/SWE-smith"},{"title":"NeurIPS Poster SWE-smith: Scaling Data for Software Engineering Agents","url":"https://neurips.cc/virtual/2025/poster/121828"},{"title":"SWE-smith: Scaling Data for Software Engineering Agents | OpenReview","url":"https://openreview.net/forum?id=63iVrXc8cC"},{"title":"SWE-bench · GitHub","url":"https://github.com/swe-bench"},{"title":"NeurIPS 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/neurips-paper-list/neurips-2025-paper-list/"},{"title":"NeurIPS 2025 Call for Papers","url":"https://neurips.cc/Conferences/2025/CallForPapers"},{"title":"Announcing the NeurIPS 2025 Best Paper Awards – NeurIPS Blog","url":"https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/"},{"title":"[2504.21798] SWE-smith: Scaling Data for Software Engineering Agents","url":"https://arxiv.org/abs/2504.21798"},{"title":"SWE-smith: Scaling Data for Software Engineering Agents","url":"https://arxiv.org/pdf/2504.21798"},{"title":"NeurIPS 2025 Best Paper Awards | Hacker News","url":"https://news.ycombinator.com/item?id=46155701"}]

Based on the search results, here's information about the SWE-smith NeurIPS 2025 paper:

## Overview

The paper is titled "SWE-smith: Scaling Data for Software Engineering Agents" by John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, and Diyi Yang. It was accepted as a Spotlight paper at the NeurIPS 2025 Datasets & Benchmarks Track.

## Main Contribution

The paper addresses a significant pain point: existing datasets for software engineering are small, with at most 1,000s of training instances from 11 or fewer GitHub repositories, and the curation procedures are complex, requiring hundreds of hours of human labor and several terabytes of storage.

To address this, the authors introduce SWE-smith, a novel pipeline for generating software engineering training data at scale that, given any Python codebase, constructs a corresponding execution environment and automatically synthesizes 100s to 1,000s of task instances that break existing test(s) in the codebase.

## Results

Using SWE-smith, the authors create a dataset of 50k instances sourced from 128 GitHub repositories, an order of magnitude larger than all previous works. They trained SWE-agent-LM-32B, achieving 40.2% Pass@1 resolve rate on the SWE-bench Verified benchmark, state of the art among open source models.

The paper's arXiv ID is 2504.21798.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bea5598-2447-48b6-be2d-bed63a1a63f1",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a859236b7efeb0da8",
  "type": "user",
  "uuid": "c3c38004-00bc-49a8-bf8e-2bfcebf79d99",
  "sourceToolAssistantUUID": "7bea5598-2447-48b6-be2d-bed63a1a63f1",
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

_source line 13 · 2026-05-10T18:32:27.692Z_

Here are my findings on all three items:

---

## 1. SWE-smith Trajectory Dataset (Kwai-Klear)

**Status: EXISTS and is publicly available.**

The dataset `Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k` is live on HuggingFace with 65,994 rows (1.58 GB). It contains trajectories used to train Klear-Agent-8B (Qwen3-8B fine-tuned) to a 39% solve rate on SWE-bench Verified.

**SWE-smith NeurIPS 2025: CONFIRMED.** The paper "SWE-smith: Scaling Data for Software Engineering Agents" (arXiv:2504.21798) was accepted as a **Spotlight** at the NeurIPS 2025 Datasets & Benchmarks Track. Authors include John Yang, Kilian Lieret, Carlos E. Jimenez, et al. It introduces a pipeline for generating SWE training data at scale (50k instances from 128 repos) and trains SWE-agent-LM-32B to 40.2% on SWE-bench Verified.

---

## 2. Agent-RLVR (arXiv:2506.11425)

**Status: EXISTS -- but the date anomaly is notable.**

The paper is live on arXiv at `2506.11425` and also on ResearchGate, alphaXiv, Scale Labs, and paperreading.club. The arXiv ID prefix `2506` indicates a June 2025 submission (not June 2026). ArXiv IDs use the format YYMM, so `2506` = June 2025, which is perfectly valid given today's date of May 2026.

**What it does:** Agent-RLVR introduces "agent guidance" to make RLVR work in multi-step agentic settings. It lifts Qwen-2.5-72B-Instruct from 9.4% to 22.4% on SWE-Bench Verified (pass@1), and to 27.8% with test-time reward model augmentation. Published by Scale AI.

**Conclusion:** The paper is NOT from June 2026 -- it is from June 2025. The `2506` prefix means 2025-06, not 2026-06. It is a legitimate, existing paper.

---

## 3. "When Agents Go Astray" / SWE-PRM (arXiv:2509.02360)

**Status: EXISTS.**

The paper is on arXiv (`2509.02360` = September 2025), also listed on OpenReview and IBM Research (confirming IBM affiliation). It was submitted to NeurIPS 2025.

**What it does:** Introduces SWE-PRM, an inference-time Process Reward Model that detects and course-corrects trajectory-level errors (redundant exploration, looping, failure to terminate) in real time during SWE agent execution. On SWE-bench Verified, closed-source PRMs improve resolution from 40.0% to 50.6% (+10.6 percentage points) at only ~$0.2 added inference cost per instance. This is the first application of PRMs for real-time trajectory-level error correction in SWE agents.

---

## Summary

| Item | Exists? | Notes |
|------|---------|-------|
| Kwai-Klear trajectories-66k | Yes | Public on HuggingFace, 66k rows |
| SWE-smith NeurIPS 2025 | Yes | Spotlight at D&B track, arXiv:2504.21798 |
| Agent-RLVR arXiv:2506.11425 | Yes | June **2025** (not 2026), by Scale AI |
| SWE-PRM arXiv:2509.02360 | Yes | September 2025, IBM Research, submitted to NeurIPS 2025 |

The claim that Agent-RLVR is from "June 2026" appears to be a misreading of the arXiv ID. `2506` in arXiv notation means year 20**25**, month 06. The paper is real and roughly one year old.

Sources:
- [Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k](https://huggingface.co/datasets/Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k)
- [SWE-smith GitHub (NeurIPS 2025 D&B Spotlight)](https://github.com/SWE-bench/SWE-smith)
- [SWE-smith on arXiv](https://arxiv.org/abs/2504.21798)
- [Agent-RLVR on arXiv](https://arxiv.org/abs/2506.11425)
- [Agent-RLVR on Scale Labs](https://labs.scale.com/papers/agent_rlvr)
- [When Agents Go Astray on arXiv](https://arxiv.org/abs/2509.02360)
- [When Agents Go Astray - IBM Research](https://research.ibm.com/publications/when-agents-go-astray-course-correcting-swe-agents-with-prms)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3c38004-00bc-49a8-bf8e-2bfcebf79d99",
  "isSidechain": true,
  "agentId": "a859236b7efeb0da8",
  "requestId": "req_011CauNCpKoRjF7vDN8Tn4nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "048a2b69-9c7d-4ab1-9c54-03885a82431b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6kEcht9jWLVwGj1ppgpXR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1707,
      "cache_creation_input_tokens": 2147,
      "cache_read_input_tokens": 10416,
      "output_tokens": 1322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2147
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1707,
          "output_tokens": 1322,
          "cache_read_input_tokens": 10416,
          "cache_creation_input_tokens": 2147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2147,
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
