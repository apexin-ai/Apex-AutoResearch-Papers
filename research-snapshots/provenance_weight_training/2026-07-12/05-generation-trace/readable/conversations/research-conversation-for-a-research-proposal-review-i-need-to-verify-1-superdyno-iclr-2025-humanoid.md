# Research conversation: For a research proposal review, I need to verify: 1. "SuperDyno" ICLR 2025 humanoid neural dynamics - verify this paper 

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6cf77a0047a23b0c.jsonl`
- **Structured JSON:** [`fb9178cc001e42e81a42.json`](../../sessions/fb/fb9178cc001e42e81a42.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-10T19:21:57.852Z_

For a research proposal review, I need to verify:

1. "SuperDyno" ICLR 2025 humanoid neural dynamics - verify this paper exists and what it does
2. "Humanoid Hanoi" arXiv:2602.13850 skill composition distribution shift - verify this paper
3. "FALCON" arXiv:2505.06776 force-adaptive humanoid loco-manipulation - verify this paper
4. Search for: "learned dynamics" OR "neural dynamics" humanoid skill composition feasibility 2025 2026 - are there papers that learn dynamics models specifically for predicting skill composition success?

Use WebSearch for each query. Report what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "a6cf77a0047a23b0c",
  "type": "user",
  "uuid": "d59b9652-48ab-45c1-9e86-16f6a31f9326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T19:21:59.628Z_

I'll search for each of these papers and research areas to verify them for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d59b9652-48ab-45c1-9e86-16f6a31f9326",
  "isSidechain": true,
  "agentId": "a6cf77a0047a23b0c",
  "requestId": "req_011CauS1UjF5LBUqNB4oHcuR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8a04de52-07d2-426c-b2e8-149545839486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018mZGir1ovCWkypLRBJ67LS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 579,
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

_source line 3 · 2026-05-10T19:21:59.645Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MjcGs5EJJXVvWgmBwVcnqy`</summary>

```json
{
  "query": "SuperDyno ICLR 2025 humanoid neural dynamics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a04de52-07d2-426c-b2e8-149545839486",
  "isSidechain": true,
  "agentId": "a6cf77a0047a23b0c",
  "requestId": "req_011CauS1UjF5LBUqNB4oHcuR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ca31dce4-8eaf-43fe-9830-54bfdbcf859c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018mZGir1ovCWkypLRBJ67LS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 579,
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

_source line 4 · 2026-05-10T19:21:59.791Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CBZfirGH6KGj68tjQjxSnJ`</summary>

```json
{
  "query": "Humanoid Hanoi arXiv:2602.13850 skill composition distribution shift"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca31dce4-8eaf-43fe-9830-54bfdbcf859c",
  "isSidechain": true,
  "agentId": "a6cf77a0047a23b0c",
  "requestId": "req_011CauS1UjF5LBUqNB4oHcuR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23f8d39f-e498-454d-b5d8-3da2b8b055c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018mZGir1ovCWkypLRBJ67LS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 579
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 13649,
          "cache_creation_input_tokens": 579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 579,
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

_source line 5 · 2026-05-10T19:21:59.795Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GdbeTEJ5cJuJqLKn2D68Qk`</summary>

```json
{
  "query": "FALCON arXiv:2505.06776 force-adaptive humanoid loco-manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23f8d39f-e498-454d-b5d8-3da2b8b055c6",
  "isSidechain": true,
  "agentId": "a6cf77a0047a23b0c",
  "requestId": "req_011CauS1UjF5LBUqNB4oHcuR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6dbab8a3-b9b0-4b02-9748-c35c2a67ad1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018mZGir1ovCWkypLRBJ67LS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 579
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 13649,
          "cache_creation_input_tokens": 579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 579,
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

_source line 6 · 2026-05-10T19:21:59.799Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rnsg4Y2Hwj8xPjpttQKS9G`</summary>

```json
{
  "query": "\"learned dynamics\" OR \"neural dynamics\" humanoid skill composition feasibility 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dbab8a3-b9b0-4b02-9748-c35c2a67ad1d",
  "isSidechain": true,
  "agentId": "a6cf77a0047a23b0c",
  "requestId": "req_011CauS1UjF5LBUqNB4oHcuR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2bb83e3e-c9a1-4115-be12-9075d1c4d708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018mZGir1ovCWkypLRBJ67LS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 13649,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 579
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 13649,
          "cache_creation_input_tokens": 579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 579,
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

_source line 7 · 2026-05-10T19:22:05.365Z_

<details><summary>↩ Tool result · `toolu_01CBZfirGH6KGj68tjQjxSnJ`</summary>

```text
Web search results for query: "Humanoid Hanoi arXiv:2602.13850 skill composition distribution shift"

Links: [{"title":"Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement","url":"https://arxiv.org/html/2602.13850"},{"title":"[2602.13850] Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement","url":"https://arxiv.org/abs/2602.13850"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations","url":"https://arxiv.org/html/2602.21723"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration","url":"https://arxiv.org/html/2412.15166"},{"title":"Skill Expansion and Composition in Parameter Space","url":"https://arxiv.org/html/2502.05932v2"},{"title":"[2602.02473] HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos","url":"https://arxiv.org/abs/2602.02473"},{"title":"Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control","url":"https://arxiv.org/html/2602.21599"},{"title":"[2602.21723] LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations","url":"https://arxiv.org/abs/2602.21723"}]

Based on the search results, here's what the paper arXiv:2602.13850 "Humanoid Hanoi" is about:

The paper investigates a skill-based framework for humanoid box rearrangement that enables long-horizon execution by sequencing reusable skills at the task level, where all skills execute through a shared, task-agnostic whole-body controller (WBC), providing a consistent closed-loop interface for skill composition.

The key challenge addressed relates to distribution shift: naively reusing the same pretrained WBC can reduce robustness over long horizons, as new skills and their compositions induce shifted state and command distributions. The authors address this with a simple data aggregation procedure that augments shared-WBC training with rollouts from closed-loop skill execution under domain randomization.

To evaluate the approach, they introduce Humanoid Hanoi, a long-horizon Tower-of-Hanoi box rearrangement benchmark, and report results in simulation and on the Digit V3 humanoid robot.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23f8d39f-e498-454d-b5d8-3da2b8b055c6",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "a6cf77a0047a23b0c",
  "type": "user",
  "uuid": "a5602488-aeeb-4bb0-9f64-27c0df802c2c",
  "sourceToolAssistantUUID": "23f8d39f-e498-454d-b5d8-3da2b8b055c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T19:22:06.416Z_

<details><summary>↩ Tool result · `toolu_01MjcGs5EJJXVvWgmBwVcnqy`</summary>

```text
Web search results for query: "SuperDyno ICLR 2025 humanoid neural dynamics"

Links: [{"title":"Published as a workshop paper at ICLR 2025","url":"https://openreview.net/pdf/b3031990328dd52267a571b265c15328bf6d6120.pdf"},{"title":"SuperDyno: Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics","url":"https://dynamics-humanoid.github.io/dynamics-humanoid/"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics | OpenReview","url":"https://openreview.net/forum?id=FPgKt7bA8w"},{"title":"ICLR 2025 Workshops","url":"https://iclr.cc/virtual/2025/events/workshop"},{"title":"ICLR 2025 Schedule","url":"https://iclr.cc/virtual/2025/calendar"},{"title":"GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub","url":"https://github.com/YanjieZe/Paper-List"},{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"},{"title":"Real-world humanoid locomotion with reinforcement learning | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.adi9579"},{"title":"7th Robot Learning Workshop: Towards Robots with Human-Level Abilities","url":"https://iclr.cc/virtual/2025/workshop/23997"}]

Based on the search results, I found comprehensive information about SuperDyno:

## SuperDyno: Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics

SuperDyno was published as a workshop paper at ICLR 2025, authored by Yu Lei, Zhengyi Luo, Tairan He, Jinkun Cao, Guanya Shi, and Kris Kitani from Carnegie Mellon University's Robotics Institute.

### Overview
The work proposes a novel framework that combines supervised learning and reinforcement learning for scalable humanoid controller learning. The framework combines supervised learning and reinforcement learning for scalable humanoid controller learning using a learned neural dynamics model.

### Key Contributions
The method achieves significantly higher sample efficiency and lower tracking error compared to prior approaches, scaling seamlessly to datasets with tens of thousands of motion clips. Medium-sized neural dynamics models can serve as a differentiable neural simulator for accurate prediction and effective policy optimization.

### Technical Approach
A key benefit of the learned neural network dynamics model is differentiability, as the differentiable world models bridge the gap between the simulation and control policy, allowing gradients of the loss function to be back-propagated to supervise the policy directly.

### Project Resources
The project has a website available at https://dynamics-humanoid.github.io/dynamics-humanoid/, and the paper is available on OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca31dce4-8eaf-43fe-9830-54bfdbcf859c",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "a6cf77a0047a23b0c",
  "type": "user",
  "uuid": "a85beed0-2f92-4400-bde8-884cf24451f1",
  "sourceToolAssistantUUID": "ca31dce4-8eaf-43fe-9830-54bfdbcf859c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T19:22:06.996Z_

<details><summary>↩ Tool result · `toolu_01GdbeTEJ5cJuJqLKn2D68Qk`</summary>

```text
Web search results for query: "FALCON arXiv:2505.06776 force-adaptive humanoid loco-manipulation"

Links: [{"title":"[2505.06776] FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2505.06776"},{"title":"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2505.06776v1"},{"title":"FALCON","url":"https://lecar-lab.github.io/falcon-humanoid/"},{"title":"GitHub - LeCAR-Lab/FALCON: [L4DC 2026] \"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation\" · GitHub","url":"https://github.com/LeCAR-Lab/FALCON"},{"title":"(PDF) FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation","url":"https://www.researchgate.net/publication/391675402_FALCON_Learning_Force-Adaptive_Humanoid_Loco-Manipulation"},{"title":"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation","url":"https://www.emergentmind.com/papers/2505.06776"},{"title":"CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation","url":"https://arxiv.org/html/2512.14689"},{"title":"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation","url":"https://lecar-lab.github.io/falcon-humanoid/static/falcon.pdf"},{"title":"EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration","url":"https://arxiv.org/html/2602.10106v1"},{"title":"Robust Visuomotor Control for Humanoid Loco-Manipulation Using Hybrid Reinforcement Learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12292580/"}]

Based on the search results, here's information about the FALCON paper (arXiv:2505.06776):

## Overview

FALCON is a dual-agent reinforcement-learning-based framework for robust force-adaptive humanoid loco-manipulation.

## Key Technical Approach

FALCON decomposes whole-body control into two specialized agents: (1) a lower-body agent ensuring stable locomotion under external force disturbances, and (2) an upper-body agent precisely tracking end-effector positions with implicit adaptive force compensation. These two agents are jointly trained in simulation with a force curriculum that progressively escalates the magnitude of external force exerted on the end effector while respecting torque limits.

## Results and Performance

Experiments demonstrate that, compared to the baselines, FALCON achieves 2x more accurate upper-body joint tracking, while maintaining robust locomotion under force disturbances and achieving faster training convergence. Moreover, FALCON enables policy training without embodiment-specific reward or curriculum tuning. Using the same training setup, policies are deployed across multiple humanoids, enabling forceful loco-manipulation tasks such as transporting payloads (0-20N force), cart-pulling (0-100N), and door-opening (0-40N) in the real world.

## Authors and Publication

The paper was submitted on May 10, 2025, with a revised version (v2) on November 16, 2025, by authors from Carnegie Mellon University, Field AI, and Nissan USA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dbab8a3-b9b0-4b02-9748-c35c2a67ad1d",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "a6cf77a0047a23b0c",
  "type": "user",
  "uuid": "7b77b9fe-ab11-464d-8600-41523647071b",
  "sourceToolAssistantUUID": "6dbab8a3-b9b0-4b02-9748-c35c2a67ad1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T19:22:07.061Z_

<details><summary>↩ Tool result · `toolu_01Rnsg4Y2Hwj8xPjpttQKS9G`</summary>

```text
Web search results for query: ""learned dynamics" OR "neural dynamics" humanoid skill composition feasibility 2025 2026"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"Neural Robot Dynamics","url":"https://arxiv.org/pdf/2508.15755"},{"title":"A review of learning-based dynamics models for robotic manipulation | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.adt1497"},{"title":"AI Humanoid Robots 2026: Technology, Builders & Future","url":"https://www.articsledge.com/post/ai-humanoid-robots"},{"title":"Real-world humanoid locomotion with reinforcement learning | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.adi9579"},{"title":"Humanoids 2025 Program | Wednesday October 1, 2025","url":"https://ras.papercept.net/conferences/scripts/rtf/ICHR25_ContentListWeb_2.html"},{"title":"Humanoid Robots News | AI Breakthroughs, Robotics Trends & Synthetic Updates","url":"https://humanoid.press/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

Based on the web search results, here's what I found regarding learned/neural dynamics and humanoid skill composition feasibility in 2025-2026:

## Recent Research and Developments

Neural Robot Dynamics (NeRD) is a learned robot-specific dynamics model for predicting the evolution of articulated rigid-body states under contact constraints, featuring a hybrid prediction framework where it replaces only application-agnostic simulation modules and leverages a robot-centric state representation.

Learning-based models offer an alternative by learning predictive dynamics directly from raw sensory data, capturing hard-to-model factors, reasoning about uncertainty, and accelerating high-precision simulations too slow for real-time control.

## Humanoid Skill Composition and Feasibility

The research community is actively exploring skill composition for humanoids. Recent work includes "Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition" published in 2025-2026, which directly addresses policy composition methods.

Humanoid robots have great potential to perform various human-level skills involving locomotion, manipulation, and cognitive capabilities. Recent papers from 2025-2026 demonstrate feasibility of complex skill learning, including physics-based humanoid whole-body control for learning highly-dynamic skills and work on general motion tracking policies for high dynamic humanoid whole-body control.

## Current Status

The sector continues shifting from prototypes to commercial pilots and production scaling, with multiple companies deploying humanoid robots in real-world manufacturing environments as of 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bb83e3e-c9a1-4115-be12-9075d1c4d708",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "a6cf77a0047a23b0c",
  "type": "user",
  "uuid": "a5e25cb8-115a-431f-bde9-8df5db157b17",
  "sourceToolAssistantUUID": "2bb83e3e-c9a1-4115-be12-9075d1c4d708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T19:22:17.787Z_

## Research Verification Results

### 1. SuperDyno - ICLR 2025 ✓ VERIFIED
**Status:** Paper exists and is confirmed
- **Full Title:** "Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics"
- **Publication:** Workshop paper at ICLR 2025
- **What it does:** Proposes a framework combining supervised and reinforcement learning for scalable humanoid controller learning using learned neural dynamics models. The key innovation is using differentiable neural network dynamics as a simulator for accurate prediction and effective policy optimization.
- **Key benefit:** Achieves higher sample efficiency, lower tracking error, and scales to datasets with tens of thousands of motion clips.
- **Project:** https://dynamics-humanoid.github.io/dynamics-humanoid/

### 2. Humanoid Hanoi - arXiv:2602.13850 ✓ VERIFIED
**Status:** Paper exists and is confirmed
- **Full Title:** "Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement"
- **Focus:** Addresses distribution shift in skill composition by using a shared whole-body controller (WBC) for executing multiple skills
- **What it does:** Implements a long-horizon Tower-of-Hanoi box rearrangement benchmark and tackles the problem that skill composition causes state and command distribution shifts that reduce robustness
- **Solution:** Uses data aggregation with domain randomization to augment shared-WBC training with closed-loop skill execution rollouts
- **Validation:** Tested in simulation and on Digit V3 humanoid robot

### 3. FALCON - arXiv:2505.06776 ✓ VERIFIED
**Status:** Paper exists and is confirmed
- **Full Title:** "FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation"
- **What it does:** Dual-agent RL framework for robust force-adaptive humanoid loco-manipulation that decomposes control into lower-body (stable locomotion) and upper-body (end-effector tracking with implicit force compensation) agents
- **Key results:** 2x more accurate upper-body tracking vs baselines while maintaining robust locomotion; tested on real-world tasks including payload transport (0-20N), cart-pulling (0-100N), and door-opening (0-40N)
- **Venue:** L4DC 2026
- **Authors:** CMU, Field AI, Nissan USA

### 4. Learned/Neural Dynamics for Skill Composition - LIMITED FINDINGS
**Status:** Related work exists, but limited specific papers on this exact topic
- **Found:** SuperDyno (above) uses learned neural dynamics for control, and "Neural Robot Dynamics" (NeRD) is a learned dynamics model for predicting articulated rigid-body states
- **General trend:** The research community is exploring skill composition and learned dynamics models, but there appear to be few papers specifically focused on using learned dynamics to predict skill composition feasibility
- **Related research:** "Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition" addresses policy composition methods (2025-2026)

---

Sources:
- [SuperDyno on OpenReview](https://openreview.net/forum?id=FPgKt7bA8w)
- [SuperDyno Project Website](https://dynamics-humanoid.github.io/dynamics-humanoid/)
- [Humanoid Hanoi on arXiv](https://arxiv.org/abs/2602.13850)
- [FALCON on arXiv](https://arxiv.org/abs/2505.06776)
- [FALCON Project Website](https://lecar-lab.github.io/falcon-humanoid/)
- [Neural Robot Dynamics on arXiv](https://arxiv.org/pdf/2508.15755)
- [Learning-based Dynamics Models Review](https://www.science.org/doi/10.1126/scirobotics.adt1497)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5e25cb8-115a-431f-bde9-8df5db157b17",
  "isSidechain": true,
  "agentId": "a6cf77a0047a23b0c",
  "requestId": "req_011CauS2A8LKmve2JLK2YuHU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d2c95265-8602-4bf0-bd8f-411b0a0987d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GEkFMFju7BWpZ5kjTGMSdC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4540,
      "cache_read_input_tokens": 14228,
      "output_tokens": 952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4540
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 952,
          "cache_read_input_tokens": 14228,
          "cache_creation_input_tokens": 4540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4540,
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
