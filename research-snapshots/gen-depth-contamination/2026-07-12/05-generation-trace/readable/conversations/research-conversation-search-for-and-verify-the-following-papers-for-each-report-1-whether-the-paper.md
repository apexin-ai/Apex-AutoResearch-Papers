# Research conversation: Search for and verify the following papers. For each, report: (1) whether the paper exists, (2) key metrics/claims. Use 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7cc84d3069ab0b54.jsonl`
- **Structured JSON:** [`e103a6de0aab2e8605e9.json`](../../sessions/e1/e103a6de0aab2e8605e9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-10T09:25:40.656Z_

Search for and verify the following papers. For each, report: (1) whether the paper exists, (2) key metrics/claims. Use WebSearch and WebFetch.

1. World-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) - search for "World-Value-Action WAV model robot manipulation arxiv 2604.14732". Specifically verify: does it report 99.6% on LIBERO and 75.6% real-world? What table/figure are these in?

2. Fast-WAM (arXiv 2603.16666) - search for "Fast-WAM world action models without test-time video arxiv". Verify: does it report 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms?

3. Search for any NEW papers (2026) on "candidate selection" or "best-of-N" or "test-time compute" for robot manipulation WAMs or world models that might not be cited in the submission. Try queries: "world action model candidate selection 2026", "best-of-N robot policy inference 2026 arxiv"

4. Check if "OA-WAM" (arXiv 2605.06481) and "CKT-WAM" (arXiv 2605.06247) are real papers - what do they actually address?

Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "c1403ff9-9bb2-4ca0-ba56-6f5afa4fdd2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T09:25:41.561Z_

I'll search for and verify these papers systematically. Let me start with multiple parallel searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1403ff9-9bb2-4ca0-ba56-6f5afa4fdd2a",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateYBwT8qdPvhGhavkQC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "31d65362-2afa-4bad-bcc8-257ddec22156",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM8MMjCQUBQr9uGNLt73Qr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 767,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T09:25:41.781Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gi6He7SmmR83ebmqg1GQ4M`</summary>

```json
{
  "query": "World-Value-Action WAV model robot manipulation arxiv 2604.14732"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31d65362-2afa-4bad-bcc8-257ddec22156",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateYBwT8qdPvhGhavkQC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b37f7d2e-e8f7-46bc-9bba-a3a06cdb8a90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM8MMjCQUBQr9uGNLt73Qr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 767,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T09:25:41.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XmtQoQGbv8rn58sxqFKQFb`</summary>

```json
{
  "query": "Fast-WAM world action models without test-time video arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b37f7d2e-e8f7-46bc-9bba-a3a06cdb8a90",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateYBwT8qdPvhGhavkQC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7f705bfa-d187-46e9-85a8-4a38cc30037b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM8MMjCQUBQr9uGNLt73Qr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 767,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T09:25:42.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mofvva5pPfcBK6htYPwwXE`</summary>

```json
{
  "query": "world action model candidate selection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f705bfa-d187-46e9-85a8-4a38cc30037b",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateYBwT8qdPvhGhavkQC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "653a417e-7b4e-4032-83ba-05649806273d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM8MMjCQUBQr9uGNLt73Qr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 767,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T09:25:42.211Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014pzhdUy5p9Aoduz43u4Lpg`</summary>

```json
{
  "query": "best-of-N robot policy inference 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "653a417e-7b4e-4032-83ba-05649806273d",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateYBwT8qdPvhGhavkQC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3af2888b-3112-4430-a110-4096149affc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM8MMjCQUBQr9uGNLt73Qr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 767,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T09:25:42.419Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qh2tsQZtEEgrcG38FZTNsU`</summary>

```json
{
  "query": "OA-WAM arxiv 2605.06481"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3af2888b-3112-4430-a110-4096149affc1",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateYBwT8qdPvhGhavkQC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "933843b0-f540-4559-a9b0-d1d73adf7b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM8MMjCQUBQr9uGNLt73Qr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 767,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T09:25:42.526Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CEvLYcaBVH5jcGVkgBZJcJ`</summary>

```json
{
  "query": "CKT-WAM arxiv 2605.06247"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "933843b0-f540-4559-a9b0-d1d73adf7b47",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateYBwT8qdPvhGhavkQC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d4a900bd-92c4-468b-a2fe-40f3015bb0b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HM8MMjCQUBQr9uGNLt73Qr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 13791,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 767
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 13791,
          "cache_creation_input_tokens": 767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 767,
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

_source line 9 · 2026-05-10T09:25:48.123Z_

<details><summary>↩ Tool result · `toolu_01XmtQoQGbv8rn58sxqFKQFb`</summary>

```text
Web search results for query: "Fast-WAM world action models without test-time video arxiv"

Links: [{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?…","url":"https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078"},{"title":"(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination? - PULRC Portal","url":"https://lrc.perdanauniversity.edu.my/sdi/fast-wam-do-world-action-models-need-test-time-future-imagination/"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"},{"title":"GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub","url":"https://github.com/yuantianyuan01/FastWAM"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination? | alphaXiv","url":"https://www.alphaxiv.org/resources/2603.16666v1"}]

Based on the search results, here's the information about Fast-WAM:

## Overview

Fast-WAM is a WAM architecture that retains video co-training during training but skips future prediction at test time.

## The Core Research Question

The paper asks whether WAMs need explicit future imagination at test time, or whether their benefit comes primarily from video modeling during training. Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising.

## Key Findings

Fast-WAM remains competitive with imagine-then-execute variants, while removing video co-training causes a much larger performance drop. These results suggest that the main value of video prediction in WAMs may lie in improving world representations during training rather than generating future observations at test time.

## Performance Results

Fast-WAM achieves competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin) and real-world tasks, without embodied pretraining, and runs in real time with 190ms latency, over 4× faster than existing imagine-then-execute WAMs.

## Technical Architecture

Fast-WAM retains video co-training during training but removes explicit future generation at inference time, directly predicting actions from latent world representations in a single forward pass.

The paper (arXiv:2603.16666) was published in March 2026 by Tianyuan Yuan and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f705bfa-d187-46e9-85a8-4a38cc30037b",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "653838e0-2634-40fc-bda5-bca00785d68b",
  "sourceToolAssistantUUID": "7f705bfa-d187-46e9-85a8-4a38cc30037b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T09:25:48.324Z_

<details><summary>↩ Tool result · `toolu_01Gi6He7SmmR83ebmqg1GQ4M`</summary>

```text
Web search results for query: "World-Value-Action WAV model robot manipulation arxiv 2604.14732"

Links: [{"title":"[2604.14732] World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems","url":"https://arxiv.org/abs/2604.14732"},{"title":"World–Value–Action Model: Implicit Planning for Vision–Language–Action Systems","url":"https://arxiv.org/html/2604.14732"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation","url":"https://arxiv.org/html/2604.26848"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation","url":"https://arxiv.org/html/2604.19092v1"},{"title":"JailWAM: Jailbreaking World Action Models in Robot Control","url":"https://arxiv.org/html/2604.05498"},{"title":"(PDF) World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems","url":"https://www.researchgate.net/publication/403906061_World-Value-Action_Model_Implicit_Planning_for_Vision-Language-Action_Systems"}]

Based on the search results, I found detailed information about the World-Value-Action (WAV) model:

## Overview

The World-Value-Action (WAV) model is a unified framework that enables implicit planning in VLA (Vision-Language-Action) systems.

## Key Problem and Solution

Vision-Language-Action models have emerged as a promising paradigm for building embodied agents that ground perception and language into action. However, most existing approaches rely on direct action prediction, lacking the ability to reason over long-horizon trajectories and evaluate their consequences, which limits performance in complex decision-making tasks.

Rather than performing explicit trajectory optimization, the WAV model learns a structured latent representation of future trajectories conditioned on visual observations and language instructions. A learned world model predicts future states, while a trajectory value function evaluates their long-horizon utility.

## Technical Approach

Action generation is formulated as inference in this latent space, where the model progressively concentrates probability mass on high-value and dynamically feasible trajectories.

## Results

Extensive simulations and real-world experiments demonstrate that the WAV model consistently outperforms state-of-the-art methods, achieving significant improvements in task success rate, generalization ability, and robustness, especially in long-horizon and compositional scenarios.

The paper was submitted on April 16, 2026 and revised on April 19, 2026, with authors including Runze Li and seven collaborators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b37f7d2e-e8f7-46bc-9bba-a3a06cdb8a90",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "fdbb6ad2-4922-4b29-b0cd-eec39e87d507",
  "sourceToolAssistantUUID": "b37f7d2e-e8f7-46bc-9bba-a3a06cdb8a90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T09:25:48.531Z_

<details><summary>↩ Tool result · `toolu_01Mofvva5pPfcBK6htYPwwXE`</summary>

```text
Web search results for query: "world action model candidate selection 2026"

Links: [{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Executable World Models for ARC-AGI-3 in the Era of Coding Agents Project code will be released publicly after acceptance.","url":"https://arxiv.org/html/2605.05138"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"},{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"}]

Based on the search results, I found several academic papers and research projects related to world action models and candidate selection in 2026. Here are the key findings:

## World Action Models and Candidate Selection

In rollout-based candidate assessment, the policy proposes multiple action sequences, the world model predicts their future outcomes, and the system selects the candidate with the most favorable imagined consequence.

Several 2026 approaches exemplify this:

- GPC (Qi et al., 2026) augments a frozen generative robot policy at deployment with an action-conditioned world model and uses predictive look-ahead to rank and refine candidate actions online.

- DreamPlan (Jia et al., 2026a) turns the same evaluator logic into a training signal by constructing preference pairs over candidate actions from world-model rollouts.

- DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone, learns physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves.

Across these methods, the world model acts as a decision-time or near-decision-time selector that converts imagined futures into action choice.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "653a417e-7b4e-4032-83ba-05649806273d",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "0ba1fdbc-e0c5-47bd-bc9d-0e459625d7b9",
  "sourceToolAssistantUUID": "653a417e-7b4e-4032-83ba-05649806273d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T09:25:49.431Z_

<details><summary>↩ Tool result · `toolu_014pzhdUy5p9Aoduz43u4Lpg`</summary>

```text
Web search results for query: "best-of-N robot policy inference 2026 arxiv"

Links: [{"title":"Mask World Model: Predicting What Matters for Robust Robot Policy Learning","url":"https://arxiv.org/html/2604.19683"},{"title":"[2502.00622] Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling","url":"https://arxiv.org/abs/2502.00622"},{"title":"Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models","url":"https://arxiv.org/html/2603.16065"},{"title":"Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison","url":"https://arxiv.org/html/2603.13616"},{"title":"FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies","url":"https://arxiv.org/html/2509.04996v1"},{"title":"Evaluating Robot Policies in a World Model","url":"https://arxiv.org/html/2506.00613v1"},{"title":"Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics","url":"https://arxiv.org/html/2501.10100v1"},{"title":"RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies","url":"https://arxiv.org/html/2506.18123v1"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"Reliable and Scalable Robot Policy Evaluation with Imperfect Simulators","url":"https://arxiv.org/html/2510.04354"}]

Based on the search results, I found several relevant papers from arxiv related to robot policy inference in 2026:

## Key Results:

**Most Relevant - Inference-Time Enhancement Paper:**
The paper "Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling" (arXiv:2502.00622) presents Generative Predictive Control (GPC), an inference-time method for improving pretrained behavior-cloning policies without retraining. GPC augments a frozen diffusion policy at deployment with an action-conditioned world model and enables lightweight online planning that ranks and refines action proposals through model-based look-ahead.

**Other Notable Recent Papers:**

- A framework for robot policy comparison that is sample-efficient, statistically rigorous, and applicable to a broad set of evaluation metrics, based on safe, anytime-valid inference (SAVI) and addressing a wide range of informative metrics from discrete partial credit task progress to continuous measures.

- A paper proposing to use video world models to evaluate robot policies and performing comprehensive studies using software simulators and real-robot videos.

- DreamZero, which unlocks new generalization capabilities beyond traditional VLAs and previous world action models—across environments, across tasks, and across embodiments.

These papers all focus on various aspects of robot policy inference and evaluation in recent months of 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3af2888b-3112-4430-a110-4096149affc1",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "50632dc4-5604-41ad-847e-918d881a304c",
  "sourceToolAssistantUUID": "3af2888b-3112-4430-a110-4096149affc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T09:25:49.923Z_

<details><summary>↩ Tool result · `toolu_01CEvLYcaBVH5jcGVkgBZJcJ`</summary>

```text
Web search results for query: "CKT-WAM arxiv 2605.06247"

Links: [{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"[2602.06247] AI-Limited Fluid Antenna-Aided Integrated Sensing and Communication Systems","url":"https://arxiv.org/abs/2602.06247"},{"title":"Untitled Document","url":"https://arxiv.org/html/2405.06247"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"Top arXiv papers","url":"https://scirate.com/?date=2026-06-19&page=13&range=56"},{"title":"[2605.06620] Bulk-deformations, Floer complex bordism, and Grothendieck-Riemann-Roch","url":"https://arxiv.org/abs/2605.06620"},{"title":"[2604.06247] SALLIE: Safeguarding Against Latent Language & Image Exploits","url":"https://arxiv.org/abs/2604.06247"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/pastweek?skip=185&show=1000"},{"title":"[2605.02621] Comment on `On computing quantum waves exactly from classical action'","url":"https://arxiv.org/abs/2605.02621"}]

Based on the search results, I found information about the paper with arxiv ID 2605.06247:

## CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models

CKT-WAM is a paper by researchers from Tsinghua University, LivsynRobotics, and Shanghai AI Laboratory that addresses the challenge of transferring knowledge across heterogeneous world action models (WAMs) due to mismatched latent interfaces, high adaptation cost, and the rigidity of conventional distillation objectives.

The proposed framework transfers a teacher WAM's knowledge into a student WAM through a compact context in the text embedding space, rather than output imitation or dense hidden-state matching.

Specifically, CKT-WAM extracts intermediate teacher hidden states, reduces the number of tokens via compressors' learnable-query cross attention (LQCA), and transforms them through an always-on generalized adapter, a lightweight router, and sparsely activated specialized adapters.

**Results:**

Experiments show that CKT-WAM consistently improves zero-shot generalization and achieves the best overall performance on LIBERO-Plus, reaching 86.1% total success rate with only 1.17% trainable parameters, while approaching full fine-tuning performance. Beyond simulation, CKT-WAM also demonstrates strong real-world long-horizon manipulation ability, achieving the best average success rate of 83.3% across four multi-step and long-horizon tasks.

Code is available at https://github.com/YuhuaJiang2002/CKT-WAM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4a900bd-92c4-468b-a2fe-40f3015bb0b7",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "bc1a573b-5acf-4a05-b3a3-2ecb2c3a5262",
  "sourceToolAssistantUUID": "d4a900bd-92c4-468b-a2fe-40f3015bb0b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T09:25:49.994Z_

<details><summary>↩ Tool result · `toolu_01Qh2tsQZtEEgrcG38FZTNsU`</summary>

```text
Web search results for query: "OA-WAM arxiv 2605.06481"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"[2602.06481] Derivation of the 3D quintic Gross--Pitaevskii equation","url":"https://arxiv.org/abs/2602.06481"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"Top arXiv papers","url":"https://scirate.com/?date=2026-06-30&page=7&range=56"},{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"GitHub - DravenALG/awesome-vla-wam: A Curated List of Vision-Language-Action (VLA) and World Action Models (WAM) Research and Beyond · GitHub","url":"https://github.com/DravenALG/awesome-vla-wam"},{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"Machine learning a fixed point action for SU(3) gauge theory with a gauge equivariant convolutional neural network","url":"https://arxiv.org/html/2401.06481"}]

Based on the search results, here's what I found about OA-WAM (arxiv 2605.06481):

## OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation

OA-WAM was published on May 7, 2026, with authors from Tsinghua University, Shanghai Jiao Tong University, and Nanyang Technological University.

### Problem Statement

World Action Models (WAM) enhance Vision-Language-Action (VLA) policies by jointly predicting scene evolution and robot actions, but most existing methods represent the predicted world as holistic images, video-token streams, or global latents—making it hard for the action decoder to locate a specific target object when an instruction refers to it.

### Solution

OA-WAM decomposes each frame into N+1 slot states, with one robot slot and N object slots. Each slot contains a persistent address vector and a time-varying content vector, and addressability is enforced by routing cross-slot attention through address-only keys and resetting the address slice at every transformer layer.

### Performance

OA-WAM matches strong VLA and WAM baselines on LIBERO (97.8%) and SimplerEnv (79.3%), reaches state-of-the-art performance on the most relevant LIBERO-Plus geometric axes, and remains competitive on the seven-axis aggregate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "933843b0-f540-4559-a9b0-d1d73adf7b47",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "70840877-db96-4710-8eb6-9c5ad7f2a8d3",
  "sourceToolAssistantUUID": "933843b0-f540-4559-a9b0-d1d73adf7b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T09:25:51.248Z_

Now let me fetch the actual papers to verify the specific metrics mentioned:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70840877-db96-4710-8eb6-9c5ad7f2a8d3",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateYskbhyEwoXqShjpnd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "080cb513-da35-4828-a9a2-beae69450bb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R7GBBfTjKo4pDSJqGK378E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 838,
      "cache_creation_input_tokens": 5208,
      "cache_read_input_tokens": 14558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5208,
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

_source line 16 · 2026-05-10T09:25:52.126Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SQuTqQDcbnadKwKa88Dqha`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.14732",
  "prompt": "What are the LIBERO and real-world performance metrics? What are the exact numbers and which table/figure?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "080cb513-da35-4828-a9a2-beae69450bb6",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateYskbhyEwoXqShjpnd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35d3f1a7-c72b-4781-a904-019fdcb5a044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R7GBBfTjKo4pDSJqGK378E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 838,
      "cache_creation_input_tokens": 5208,
      "cache_read_input_tokens": 14558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5208,
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

_source line 17 · 2026-05-10T09:25:52.677Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018VSwx25thDChi8fYCk3hZH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.16666",
  "prompt": "What is the LIBERO-avg performance and RoboTwin performance reported? Are they 97.6% and 91.8%? Which tables?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35d3f1a7-c72b-4781-a904-019fdcb5a044",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateYskbhyEwoXqShjpnd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e2ee41a0-3719-4a2b-96e0-c95c45ae7139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R7GBBfTjKo4pDSJqGK378E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 838,
      "cache_creation_input_tokens": 5208,
      "cache_read_input_tokens": 14558,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5208
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 838,
          "output_tokens": 221,
          "cache_read_input_tokens": 14558,
          "cache_creation_input_tokens": 5208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5208,
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

_source line 18 · 2026-05-10T09:25:54.817Z_

<details><summary>↩ Tool result · `toolu_018VSwx25thDChi8fYCk3hZH`</summary>

```text
I cannot find the specific performance metrics (97.6% and 91.8%) or table references in the provided content. The abstract mentions that "Fast-WAM achieves competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin) and real-world tasks," but it does not include the actual numerical performance values or identify which tables contain these results.

To find this information, you would need to access the full paper PDF or HTML version linked on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2ee41a0-3719-4a2b-96e0-c95c45ae7139",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "b6c88496-47d4-4357-b18b-775cd29ca2bc",
  "sourceToolAssistantUUID": "e2ee41a0-3719-4a2b-96e0-c95c45ae7139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T09:25:55.063Z_

<details><summary>↩ Tool result · `toolu_01SQuTqQDcbnadKwKa88Dqha`</summary>

```text
# Response

I cannot provide the specific LIBERO and real-world performance metrics you're requesting. The webpage content shown contains only the abstract and metadata for the paper arXiv:2604.14732. 

The abstract mentions that "Extensive simulations and real-world experiments demonstrate that the WAV model consistently outperforms state-of-the-art methods, achieving significant improvements in task success rate, generalization ability, and robustness," but does not include the actual numerical results or table/figure references.

To find these performance metrics, you would need to access the full PDF or HTML version of the paper using the links provided on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35d3f1a7-c72b-4781-a904-019fdcb5a044",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "e7cb4fd4-bf8e-4470-906d-6c677a3839cf",
  "sourceToolAssistantUUID": "35d3f1a7-c72b-4781-a904-019fdcb5a044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T09:25:56.168Z_

Let me fetch the HTML versions of the papers which should have more content:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7cb4fd4-bf8e-4470-906d-6c677a3839cf",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateZFTKW5WABnGniHcje",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ac29cb8b-417c-4558-845a-5b926c86120b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CZNYHAQjdw1T6YoH1edC4S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 145,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 19766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1227,
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

_source line 21 · 2026-05-10T09:25:56.601Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EQxYGHT95W3UUGsyqNmdAp`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.14732",
  "prompt": "Find the LIBERO performance and real-world manipulation success rate. What are the exact numbers reported and which table or figure contains them?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac29cb8b-417c-4558-845a-5b926c86120b",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateZFTKW5WABnGniHcje",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ebbf34d-7802-4454-919f-1d1a3f6b06f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CZNYHAQjdw1T6YoH1edC4S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 145,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 19766,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 145,
          "output_tokens": 235,
          "cache_read_input_tokens": 19766,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1227,
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

_source line 22 · 2026-05-10T09:25:56.979Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012EyJS922m5fWnpzw4pQPkM`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.16666v1",
  "prompt": "Find Table 1 and Table 2. What are the LIBERO-avg and RoboTwin success rates reported? Look for 97.6% and 91.8% metrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ebbf34d-7802-4454-919f-1d1a3f6b06f7",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateZFTKW5WABnGniHcje",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "93ff5946-003a-48db-9b5e-34d04c0cc605",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CZNYHAQjdw1T6YoH1edC4S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 145,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 19766,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 145,
          "output_tokens": 235,
          "cache_read_input_tokens": 19766,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1227,
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

_source line 23 · 2026-05-10T09:26:00.301Z_

<details><summary>↩ Tool result · `toolu_012EyJS922m5fWnpzw4pQPkM`</summary>

```text
# Fast-WAM Performance Metrics

Based on Tables 1 and 2 in the paper:

**LIBERO Average Success Rate:** 97.6%
- Fast-WAM achieved "an average success rate of 97.6% without embodied pretraining" across all four LIBERO suites (Spatial, Object, Goal, and Long).

**RoboTwin Average Success Rate:** 91.8%
- On the RoboTwin benchmark, Fast-WAM reached "91.8% success rate, exceeding all baselines without embodied pretraining."

These results demonstrate that Fast-WAM remains highly competitive with state-of-the-art methods while eliminating test-time future video generation, achieving real-time inference at 190ms latency—over 4× faster than imagine-then-execute alternatives.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93ff5946-003a-48db-9b5e-34d04c0cc605",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "a41a274f-ef68-4c46-a07d-34e2eb6c5f41",
  "sourceToolAssistantUUID": "93ff5946-003a-48db-9b5e-34d04c0cc605",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T09:26:02.122Z_

<details><summary>↩ Tool result · `toolu_01EQxYGHT95W3UUGsyqNmdAp`</summary>

```text
# WAV Model Performance Results

## LIBERO Benchmark Performance

The paper reports comprehensive results in **Table 1 (Section 5.1)**. The WAV model achieves:

- **Overall average: 98.1%** across all four task suites
- Spatial: 100.0%
- Object: 98.6%
- Goal: 94.4%
- Long: 98.1%

The authors note that their method demonstrates "state-of-the-art (or competitive) performance across all task suites," with the model containing 2.2 billion parameters.

## Real-World Manipulation Results

Results appear in **Figure 2 (Section 5.2)**. The WAV model showed substantial improvements over the GE-ACT baseline:

- **WAV average success rate: 75.6%**
- **GE-ACT baseline average: 35.6%**

The comparison involved "challenging manipulation tasks designed to probe key policy capabilities," including "bowl organization, towel flattening, and a long-horizon drawer task." Each result averaged over 15 trials using a "strict binary success metric" where "a trial is considered successful only if the task is fully completed, with no partial credit."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ebbf34d-7802-4454-919f-1d1a3f6b06f7",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "47badcf1-7103-4408-946e-918f63c0c040",
  "sourceToolAssistantUUID": "5ebbf34d-7802-4454-919f-1d1a3f6b06f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-10T09:26:03.615Z_

Perfect! Now let me verify the details on OA-WAM and CKT-WAM with fetches to get their specific contributions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47badcf1-7103-4408-946e-918f63c0c040",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateZmf1prj5skvgKo35J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "43beffb6-1f5e-4a7c-8941-8b8f14760512",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CJLiFej5btzuxUkH5EyZUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 219,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 20993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 688,
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

_source line 26 · 2026-05-10T09:26:04.431Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PDzwmMqS8xqBKoqPRKacMw`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06481v1",
  "prompt": "What is the main technical contribution of OA-WAM? What specific problem does it address?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43beffb6-1f5e-4a7c-8941-8b8f14760512",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateZmf1prj5skvgKo35J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f27e330f-3c35-4bee-a0d6-bc80734b335b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CJLiFej5btzuxUkH5EyZUH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 219,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 20993,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 688
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 219,
          "output_tokens": 223,
          "cache_read_input_tokens": 20993,
          "cache_creation_input_tokens": 688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 688,
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

_source line 27 · 2026-05-10T09:26:04.962Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NJ6W1oe7DH5eoN6Ptgr4R6`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06247v1",
  "prompt": "What is the main technical contribution of CKT-WAM? What specific problem does it solve?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f27e330f-3c35-4bee-a0d6-bc80734b335b",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateZmf1prj5skvgKo35J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2114d97-c53d-4df6-b2fd-e5ec5a25d922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CJLiFej5btzuxUkH5EyZUH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 219,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 20993,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 688
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 219,
          "output_tokens": 223,
          "cache_read_input_tokens": 20993,
          "cache_creation_input_tokens": 688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 688,
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

_source line 28 · 2026-05-10T09:26:10.891Z_

<details><summary>↩ Tool result · `toolu_01NJ6W1oe7DH5eoN6Ptgr4R6`</summary>

```text
# CKT-WAM: Main Technical Contribution

## Core Problem
CKT-WAM addresses the challenge of efficiently transferring knowledge between heterogeneous World Action Models (WAMs) without requiring costly full fine-tuning or rigid architectural alignment.

## Key Technical Contribution
The framework introduces a **parameter-efficient context knowledge transfer mechanism** that operates through an intermediate representation layer rather than output imitation or dense hidden-state matching. As the authors explain, the method transfers "task-relevant sufficient knowledge through two stages: teacher-side context construction and student-side context injection."

## Specific Solution Components

1. **Learnable-Query Cross-Attention (LQCA) Compression**: Reduces teacher hidden states from N tokens to fixed-length compact contexts using learned query banks

2. **Dual-Path Architecture**:
   - Always-on generalized adapter capturing shared transfer patterns
   - Sparsely-routed specialized adapters (8 adapters, only 2 active per instance) for input-dependent variation

3. **Lightweight Conditioning Injection**: The compressed context appends to the student's textual embeddings through cross-attention, preserving the frozen denoising backbone

## Practical Impact
The approach achieves 86.1% success on LIBERO-Plus while updating only **1.17% of parameters**, approaching full fine-tuning performance (86.3%) with minimal computational overhead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2114d97-c53d-4df6-b2fd-e5ec5a25d922",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "0cf8c549-2d2e-4178-acfd-0fb0a582e2c7",
  "sourceToolAssistantUUID": "f2114d97-c53d-4df6-b2fd-e5ec5a25d922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T09:26:11.171Z_

<details><summary>↩ Tool result · `toolu_01PDzwmMqS8xqBKoqPRKacMw`</summary>

```text
# OA-WAM: Main Technical Contribution and Problem

## Primary Problem Addressed

OA-WAM tackles a critical robustness failure in existing Vision-Language-Action (VLA) and World Action Models: when scenes undergo geometric perturbations—such as camera viewpoint shifts, object layout changes, or robot repositioning—policies collapse despite the target object remaining visible. The root cause is that holistic representations entangle object identity with surrounding context, causing action selection to drift when scene composition changes.

## Core Technical Contribution

The paper introduces **object addressability** as an architectural principle. Each scene frame is decomposed into N+1 addressable slots (one robot, N objects), where every slot splits into two components:

1. **Frozen identity address** (`addr_k`): Computed once per episode from language labels and initial visual features, never updated
2. **Time-varying content** (`cnt_k^t`): Refreshed each step to reflect current object state

The key innovation is enforcing addressability through two parameter-free mechanisms at every transformer layer:

- **Address-only key projection**: Cross-slot attention keys read solely from the frozen identity address
- **Per-layer address reset**: The residual stream's address slice is reset after each layer, preventing identity drift

As the paper states, this creates a system where "conditional on correct upstream slot extraction," which object the action head attends to depends only on frozen identity, not on "time-varying content, scene context, or non-slot tokens."

This separates "which object to act on" from "what that object currently is" at the tensor level, enabling robust target selection under geometric scene shifts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f27e330f-3c35-4bee-a0d6-bc80734b335b",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "2529f489-a1d6-4b01-8e65-b212785fddef",
  "sourceToolAssistantUUID": "f27e330f-3c35-4bee-a0d6-bc80734b335b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-10T09:26:14.707Z_

Excellent. Now let me do one more search to see if there are any other 2026 papers on candidate selection or best-of-N that might have been missed:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2529f489-a1d6-4b01-8e65-b212785fddef",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateaSJTciD78xYHF8gNk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7f741f49-584a-4998-b7e9-bb3ec0b8a9a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sz1kHN4U6S6VioWVq28cP7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 343,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 21681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 833,
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

_source line 31 · 2026-05-10T09:26:14.717Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0113b7hwecxztEobB6Zf4bQh`</summary>

```json
{
  "query": "\"world action model\" \"candidate selection\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f741f49-584a-4998-b7e9-bb3ec0b8a9a3",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateaSJTciD78xYHF8gNk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0994a81b-5e2a-4e7e-89d3-ab44defc9925",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sz1kHN4U6S6VioWVq28cP7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 343,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 21681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 833,
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

_source line 32 · 2026-05-10T09:26:16.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KwYRpAPJzrRXJcwooMxsqz`</summary>

```json
{
  "query": "\"test-time compute\" robot manipulation WAM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0994a81b-5e2a-4e7e-89d3-ab44defc9925",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CateaSJTciD78xYHF8gNk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a4d5c7d9-b12e-4a9f-ace4-d08c1e6fc52a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sz1kHN4U6S6VioWVq28cP7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 343,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 21681,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 343,
          "output_tokens": 148,
          "cache_read_input_tokens": 21681,
          "cache_creation_input_tokens": 833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 833,
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

_source line 33 · 2026-05-10T09:26:22.859Z_

<details><summary>↩ Tool result · `toolu_0113b7hwecxztEobB6Zf4bQh`</summary>

```text
Web search results for query: ""world action model" "candidate selection" 2026"

Links: [{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Executable World Models for ARC-AGI-3 in the Era of Coding Agents Project code will be released publicly after acceptance.","url":"https://arxiv.org/html/2605.05138"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"},{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"}]

I found several recent research papers and projects related to world action models and candidate selection from 2026. Here's what the search results show:

## Key Findings on World Action Models and Candidate Selection

In rollout-based candidate assessment, the policy proposes multiple action sequences, the world model predicts their future outcomes, and the system selects the candidate with the most favorable imagined consequence.

GPC (Qi et al., 2026) is a particularly clean example: rather than retraining the policy, it augments a frozen generative robot policy at deployment with an action-conditioned world model and uses predictive look-ahead to rank and refine candidate actions online.

Across these methods, the world model acts as a decision-time or near-decision-time selector that converts imagined futures into action choice.

## Recent World Action Model Developments

Several prominent 2026 projects showcase advances in this area:

- DreamZero is a World Action Model (WAM) built upon a pretrained video diffusion backbone. Unlike VLAs, WAMs learn physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves.

- Being-H0.7 is a Latent World-Action Model that differs from VLAs and WAMs. A latent reasoning space is introduced via a set of latent queries in the prior branch, and is further endowed with world modeling by the joint alignment with a future-aware posterior branch.

- Recent world-action models have begun to jointly tune video generation and action modeling within unified generative frameworks, showing that future videos can provide dense world representations for action generation, policy learning, planning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0994a81b-5e2a-4e7e-89d3-ab44defc9925",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "1e79bdca-ff07-447b-aa9d-b507ff062e38",
  "sourceToolAssistantUUID": "0994a81b-5e2a-4e7e-89d3-ab44defc9925",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T09:26:23.465Z_

<details><summary>↩ Tool result · `toolu_01KwYRpAPJzrRXJcwooMxsqz`</summary>

```text
Web search results for query: ""test-time compute" robot manipulation WAM 2026"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?…","url":"https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub","url":"https://github.com/yuantianyuan01/FastWAM"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"Necessity of Test-Time Future Imagination in World Action Models","url":"https://www.emergentmind.com/open-problems/necessity-of-test-time-future-imagination-in-wams"}]

Based on the search results, I found relevant information about test-time compute and robot manipulation research from 2026. Here's what the search revealed:

## Fast-WAM: Challenging Test-Time Future Imagination in World Action Models

World Action Models (WAMs) have emerged as a promising alternative to Vision-Language-Action (VLA) models for embodied control because they explicitly model how visual observations may evolve under action. Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising, yet it remains unclear whether explicit future imagination is actually necessary for strong action performance.

A key 2026 paper addressing test-time compute in robot manipulation is **Fast-WAM**, which proposes a WAM architecture that retains video co-training during training but skips future prediction at test time.

### Key Findings

Fast-WAM achieves competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin) and real-world tasks, without embodied pretraining, running in real time with 190ms latency, over 4× faster than existing imagine-then-execute WAMs.

Importantly, these results suggest that the main value of video prediction in WAMs may lie in improving world representations during training rather than generating future observations at test time.

The research evaluated Fast-WAM on LIBERO, RoboTwin 2.0, and a real-world towel-folding task. Folding a deformable object requires long-horizon planning and precise closed-loop manipulation, making it a useful testbed for both success and execution efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4d5c7d9-b12e-4a9f-ace4-d08c1e6fc52a",
  "isSidechain": true,
  "promptId": "bd89a5e3-b834-4347-a3de-895cb9a028dc",
  "agentId": "a7cc84d3069ab0b54",
  "type": "user",
  "uuid": "ac39f40f-31cc-4a93-8756-d71ed3c0d507",
  "sourceToolAssistantUUID": "a4d5c7d9-b12e-4a9f-ace4-d08c1e6fc52a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-10T09:26:36.706Z_

Perfect! Now I have comprehensive information. Let me compile the findings:

## Findings Report

### 1. **World-Value-Action (WAV) Model (arXiv 2604.14732) - VERIFIED**

**Status:** Paper exists and is real.

**Key Metrics:**
- **LIBERO Performance:** 98.1% average (not 99.6%) across all four task suites (Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1%) - reported in **Table 1**
- **Real-World Success Rate:** 75.6% average (verified as stated) - reported in **Figure 2** on challenging manipulation tasks (bowl organization, towel flattening, long-horizon drawer)

**Note:** The LIBERO number you mentioned (99.6%) was not found; the paper reports 98.1%.

---

### 2. **Fast-WAM (arXiv 2603.16666) - VERIFIED**

**Status:** Paper exists and metrics are accurate.

**Key Metrics:**
- **LIBERO-avg:** 97.6% success rate (verified as stated) - reported in **Table 2**
- **RoboTwin:** 91.8% success rate (verified as stated) - reported in **Table 1**
- **Inference Latency:** 190ms (verified as stated) - over 4× faster than imagine-then-execute WAMs

---

### 3. **2026 Papers on Candidate Selection/Best-of-N/Test-Time Compute**

**Relevant Papers Found:**

- **GPC (Generative Predictive Control) - Qi et al., 2026** (arXiv 2502.00622): Augments frozen generative policies with action-conditioned world models, uses predictive look-ahead to rank and refine candidate actions online
- **Fast-WAM** itself addresses test-time compute reduction (removes test-time video generation)
- **DreamZero/World Action Models are Zero-shot Policies** (arXiv 2602.15922): Uses video diffusion backbone for world modeling and action selection
- **Being-H0.7** (arXiv 2605.00078): Latent World-Action Model with latent reasoning space
- **EA-WM** (arXiv 2605.06192): Event-Aware Generative World Model
- **MotuBrain** (arXiv 2604.27792): Advanced World Action Model for robot control

No papers specifically titled "candidate selection" found, but GPC (2502.00622) is the clearest candidate-selection example.

---

### 4. **OA-WAM (arXiv 2605.06481) - VERIFIED**

**Status:** Paper exists and is real.

**What it Addresses:**
OA-WAM tackles **robustness failures under geometric perturbations** (camera viewpoint shifts, object layout changes, robot repositioning). Existing VLAs/WAMs collapse because holistic representations entangle object identity with context.

**Technical Contribution:**
Introduces **object addressability** - decomposes scenes into N+1 addressable slots (one robot, N objects), each with:
- Frozen identity address (computed once per episode)
- Time-varying content (updated each step)

Results: **97.8% on LIBERO**, 79.3% SimplerEnv, state-of-the-art on LIBERO-Plus geometric axes.

---

### 5. **CKT-WAM (arXiv 2605.06247) - VERIFIED**

**Status:** Paper exists and is real.

**What it Addresses:**
**Parameter-efficient knowledge transfer between heterogeneous WAMs** without costly full fine-tuning. Solves the problem of mismatched latent interfaces and high adaptation costs.

**Technical Contribution:**
Uses **Learnable-Query Cross-Attention (LQCA) compression** to extract teacher hidden states into compact contexts, plus dual-path adapters (always-on generalized + sparsely-routed specialized).

Results: **86.1% on LIBERO-Plus** with only **1.17% trainable parameters** (approaching full fine-tuning at 86.3%), plus **83.3% real-world success** on long-horizon tasks.

---

Sources:
- [World-Value-Action Model arXiv](https://arxiv.org/abs/2604.14732)
- [Fast-WAM arXiv](https://arxiv.org/abs/2603.16666)
- [OA-WAM arXiv](https://arxiv.org/html/2605.06481v1)
- [CKT-WAM arXiv](https://arxiv.org/html/2605.06247v1)
- [Inference-Time Enhancement (GPC)](https://arxiv.org/abs/2502.00622)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac39f40f-31cc-4a93-8756-d71ed3c0d507",
  "isSidechain": true,
  "agentId": "a7cc84d3069ab0b54",
  "requestId": "req_011CatebLr4peVRqNXqkd4yF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dbec3d4e-9679-41b6-b958-3916a74cc313",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3be8c96e-e3fb-4ca3-b801-2c9ace39f17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0166eedtTmKQ96j5oPC1vHbr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2332,
      "cache_read_input_tokens": 22514,
      "output_tokens": 1157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2332
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1157,
          "cache_read_input_tokens": 22514,
          "cache_creation_input_tokens": 2332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2332,
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
