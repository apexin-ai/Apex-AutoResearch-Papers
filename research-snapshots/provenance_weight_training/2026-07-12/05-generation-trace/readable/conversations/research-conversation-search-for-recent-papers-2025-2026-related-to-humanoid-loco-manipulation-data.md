# Research conversation: Search for recent papers (2025-2026) related to humanoid loco-manipulation data generation, specifically looking for any

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae1ebe7f07cf40db0.jsonl`
- **Structured JSON:** [`32c5e3388d785e66f205.json`](../../sessions/32/32c5e3388d785e66f205.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

60 recorded events

### User

_source line 1 · 2026-05-10T13:03:08.656Z_

Search for recent papers (2025-2026) related to humanoid loco-manipulation data generation, specifically looking for any work that does SE(3) object-centric demonstration multiplication for mobile humanoids, combined locomotion+manipulation data augmentation, or MimicGen-style extensions for bipedal humanoid robots. Also verify whether DreamGen (arXiv:2505.12705) truly only addresses stationary manipulation or also mobile/loco-manipulation.

Search queries to use:
1. "humanoid loco-manipulation data generation 2026" on arxiv
2. "mobile manipulation demonstration augmentation bipedal 2026" 
3. "MimicGen humanoid locomotion" or "humanoid demo multiplication"
4. DreamGen arXiv 2505.12705 to verify its scope (stationary vs mobile manipulation)
5. "whole-body humanoid data generation" 2025 2026
6. Search arxiv.org for "loco-manipulation data" 2026

Report back: (a) any papers that do coupled SE(3) stance+arm encoding for humanoid demo multiplication (would undermine novelty), (b) whether DreamGen truly is stationary-manipulation only as claimed, (c) any other concurrent 2026 work doing procedural humanoid data generation that isn't in the paper's landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "0282b4b9-d90a-4d90-be66-cd9e1f04230c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T13:03:10.540Z_

I'll help you search for recent papers on humanoid loco-manipulation data generation. Let me conduct a comprehensive search across these topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0282b4b9-d90a-4d90-be66-cd9e1f04230c",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw81qYhVDGA6dj6d3qT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "74148474-f53d-405a-a36b-65797793ebe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4L1Nf4qau2ekn1jDu9bTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 728,
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

_source line 3 · 2026-05-10T13:03:10.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JNKYTgATNQJwLhrS8RCN1y`</summary>

```json
{
  "query": "humanoid loco-manipulation data generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74148474-f53d-405a-a36b-65797793ebe7",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw81qYhVDGA6dj6d3qT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3048f713-20a9-470b-9f06-c92937992750",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4L1Nf4qau2ekn1jDu9bTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 728,
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

_source line 4 · 2026-05-10T13:03:10.799Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VVn5N5yQtdBPdi3Afq7BGR`</summary>

```json
{
  "query": "mobile manipulation demonstration augmentation bipedal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3048f713-20a9-470b-9f06-c92937992750",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw81qYhVDGA6dj6d3qT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9e1147a1-82d7-42f9-b491-fdd27b4f5044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4L1Nf4qau2ekn1jDu9bTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 728,
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

_source line 5 · 2026-05-10T13:03:10.974Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012AcNAoJ5Qt7TQw5Xk7324t`</summary>

```json
{
  "query": "MimicGen humanoid locomotion demo multiplication"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e1147a1-82d7-42f9-b491-fdd27b4f5044",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw81qYhVDGA6dj6d3qT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68bb68bf-409d-4284-b372-dc15ea7a33e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4L1Nf4qau2ekn1jDu9bTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 728,
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

_source line 6 · 2026-05-10T13:03:11.203Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M1GfYfjWjUV4NHjC99qHYu`</summary>

```json
{
  "query": "DreamGen arXiv 2505.12705"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68bb68bf-409d-4284-b372-dc15ea7a33e0",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw81qYhVDGA6dj6d3qT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "02d312c1-7632-40d4-badc-32bd31b3c1dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4L1Nf4qau2ekn1jDu9bTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 728,
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

_source line 7 · 2026-05-10T13:03:11.531Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WZhc4Q89EV2vyGXoo18Buq`</summary>

```json
{
  "query": "whole-body humanoid data generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02d312c1-7632-40d4-badc-32bd31b3c1dc",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw81qYhVDGA6dj6d3qT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1c3c3bc8-0473-454f-b365-d7c648996fc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4L1Nf4qau2ekn1jDu9bTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 728,
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

_source line 8 · 2026-05-10T13:03:11.602Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DVW4DLUmc8DxcuZ18dA4Hc`</summary>

```json
{
  "query": "loco-manipulation data generation bipedal robots 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c3c3bc8-0473-454f-b365-d7c648996fc9",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw81qYhVDGA6dj6d3qT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "064a0cbf-2519-4e28-b942-3e65cb20bd63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4L1Nf4qau2ekn1jDu9bTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 728,
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

### Tool result

_source line 9 · 2026-05-10T13:03:17.856Z_

<details><summary>↩ Tool result · `toolu_012AcNAoJ5Qt7TQw5Xk7324t`</summary>

```text
Web search results for query: "MimicGen humanoid locomotion demo multiplication"

Links: [{"title":"MimicGen","url":"https://mimicgen.github.io/"},{"title":"GitHub - NVlabs/mimicgen: This code corresponds to simulation environments used as part of the MimicGen project. · GitHub","url":"https://github.com/NVlabs/mimicgen"},{"title":"MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | OpenReview","url":"https://openreview.net/forum?id=dk-2R1f_LR"},{"title":"[2310.17596] MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations","url":"https://ar5iv.labs.arxiv.org/html/2310.17596"},{"title":"ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning","url":"https://arxiv.org/html/2510.05070v1"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://arxiv.org/html/2410.24185v1"},{"title":"MimicGen: Scalable Robot Data Generation","url":"https://www.emergentmind.com/topics/mimicgen-environment"},{"title":"Overview — mimicgen 1.0 documentation","url":"https://mimicgen.github.io/docs/introduction/overview.html"},{"title":"VisualMimic Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/html/2509.20322v1"},{"title":"GitHub - visualmimic/VisualMimic: [arXiv 2025] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation · GitHub","url":"https://github.com/visualmimic/VisualMimic"}]

Based on the search results, I found information about MimicGen and related work on humanoid locomotion:

## MimicGen Overview

MimicGen is a system for automatically synthesizing large-scale datasets from a small number of human demonstrations by adapting them to new scene configurations, object instances, and robot arms.

## Data Generation and Scaling

MimicGen was used to autonomously generate over 50,000 demonstrations from less than 200 human demonstrations across 18 tasks, multiple simulators, and the real-world. The system demonstrates impressive data multiplication capabilities, particularly evident in the example that MimicGen generated 1000 demos for each of 3 reset distributions from just 10 human demos.

## Effectiveness

Policies trained on 200 demos generated by MimicGen from 10 human demos achieved comparable performance to policies trained on 200 human demos.

## Related Humanoid Work

The search also revealed related systems like DexMimicGen, a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands. Additionally, VisualMimic is a visual sim-to-real framework that integrates visual perception with whole-body control for humanoid loco-manipulation, enabling humanoid robots to robustly perform diverse loco-manipulation tasks directly from visual and proprioceptive inputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68bb68bf-409d-4284-b372-dc15ea7a33e0",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "042dfbbd-a997-4cee-9a1a-fe31edb50656",
  "sourceToolAssistantUUID": "68bb68bf-409d-4284-b372-dc15ea7a33e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T13:03:18.599Z_

<details><summary>↩ Tool result · `toolu_01JNKYTgATNQJwLhrS8RCN1y`</summary>

```text
Web search results for query: "humanoid loco-manipulation data generation 2026"

Links: [{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633"},{"title":"[Literature Review] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://www.themoonlight.io/en/review/omniretarget-interaction-preserving-data-generation-for-humanoid-whole-body-loco-manipulation-and-scene-interaction"},{"title":"Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/11202977/11203009/11203092.pdf"},{"title":"[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2603.12263"},{"title":"(PDF) OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://www.researchgate.net/publication/396049126_OmniRetarget_Interaction-Preserving_Data_Generation_for_Humanoid_Whole-Body_Loco-Manipulation_and_Scene_Interaction"},{"title":"Robust Visuomotor Control for Humanoid Loco-Manipulation Using Hybrid Reinforcement Learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12292580/"},{"title":"Opt2Skill: Versatile Humanoid Loco-Manipulation through Model-Based Trajectory Optimization and Reinforcement Learning – Laboratory for Intelligent Decision and Autonomous Robots","url":"https://lab-idar.gatech.edu/opt2skill-achieving-versatile-humanoid-loco-manipulation-through-model-based-trajectory-optimization-and-reinforcement-learning/"},{"title":"HUMANOID-LLA: OPEN-VOCABULARY ...","url":"https://openreview.net/pdf/830d6b6b95ad212ad757bba8ac1fac08c6273041.pdf"}]

Based on the search results, there is significant recent research activity in humanoid loco-manipulation data generation in 2026. Here are the key findings:

## Notable 2026 Research Projects

WholeBodyVLA is a unified Vision-Language-Action framework for large-space humanoid loco-manipulation that learns unified latent actions from action-free egocentric videos through a Latent Action Model (LAM).

Ψ₀ (Psi-Zero) is an open foundation model to address challenging humanoid loco-manipulation tasks. Research identifies that pre-training on high-quality egocentric human manipulation data followed by post-training on domain-specific real-world humanoid trajectories yields superior performance, achieving the best results using about 800 hours of human video data and 30 hours of real-world robot data.

## Data Generation Methods

OmniRetarget is an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. OmniRetarget generated over 8-hour trajectories that enable proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid.

Research using latent diffusion models generates realistic RGB human-object interaction scenes to guide humanoid loco-manipulation planning, extracting contact locations and robot configurations for whole-body trajectory optimization.

These approaches represent a shift toward more efficient, high-quality data generation for training humanoid robots on complex loco-manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3048f713-20a9-470b-9f06-c92937992750",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "fc5e1f23-f34e-4522-b2e1-f3a597852d85",
  "sourceToolAssistantUUID": "3048f713-20a9-470b-9f06-c92937992750",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T13:03:18.714Z_

<details><summary>↩ Tool result · `toolu_01VVn5N5yQtdBPdi3Afq7BGR`</summary>

```text
Web search results for query: "mobile manipulation demonstration augmentation bipedal 2026"

Links: [{"title":"MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation","url":"https://www.researchgate.net/publication/396747308_MoMaGen_Generating_Demonstrations_under_Soft_and_Hard_Constraints_for_Multi-Step_Bimanual_Mobile_Manipulation"},{"title":"Dynamic Mobile Manipulation via Whole-Body Bilateral Teleoperation of a Wheeled Humanoid | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel7/7083369/10360389/10323148.pdf"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"DYNAMIXEL in Research","url":"https://www.robotis.us/dynamixel-in-research/"},{"title":"MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation | OpenReview","url":"https://openreview.net/forum?id=bGPDviEtZ1"},{"title":"SuperSuit: An Isomorphic Bimodal Interface for Scalable Mobile Manipulation","url":"https://arxiv.org/html/2603.06280v1"},{"title":"TYPE Mini Review PUBLISHED 01 December 2025 DOI 10.3389/frobt.2025.1678567","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"},{"title":"MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation","url":"https://arxiv.org/html/2510.18316v1"},{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"Humanoid robots in 2026: Types, prices, and what’s next - Standard Bots","url":"https://standardbots.com/blog/humanoid-robot"}]

Based on the web search results, here are the key findings related to mobile manipulation demonstration augmentation for bipedal robots in 2026:

## Mobile Manipulation Demonstrations

MoMaGen is a data generation method for bimanual mobile manipulation that formulates data generation as a constrained optimization problem with hard constraints (e.g., reachability, visibility during manipulation) and soft constraints (e.g., visibility while navigation).

Multi-step bimanual mobile manipulation challenges include determining base placement to ensure reachability and positioning the camera to provide sufficient visibility for visuomotor policies.

## Demonstration Augmentation Approaches

The X-Gen family of techniques leverages simulation and augmentation based on a small number of human demonstrations that are used as seeds to generate multiple new variations automatically. Data generated by MoMaGen can be used to train successful imitation learning policies using a single source demo, and the trained policy can be fine-tuned with a very small amount of real-world data (40 demos) to be successfully deployed on real robotic hardware.

## Bipedal Robots and Teleoperation Systems

One proposed system for bipedal stability is primarily composed of bipedal-oriented assistive subsystems and a seat-type whole-body exoskeleton cockpit called "TABLIS".

CHILD is a compact reconfigurable teleoperation system that enables joint level control over humanoid robots, fits within a standard baby carrier, and allows the operator control over all four limbs while supporting both direct joint mapping for fullbody control and loco-manipulation.

## 2026 Humanoid Robot Deployments

Digit is currently deployed in pilot programs with major logistics companies, lifts and carries standard warehouse totes, navigates ramps and uneven flooring, and its bipedal legs let it work in facilities not designed for wheeled robots.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e1147a1-82d7-42f9-b491-fdd27b4f5044",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "7d88b1c5-a9d0-4d4c-9c20-f1b5e81d71e0",
  "sourceToolAssistantUUID": "9e1147a1-82d7-42f9-b491-fdd27b4f5044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T13:03:18.896Z_

<details><summary>↩ Tool result · `toolu_01M1GfYfjWjUV4NHjC99qHYu`</summary>

```text
Web search results for query: "DreamGen arXiv 2505.12705"

Links: [{"title":"[2505.12705] DreamGen: Unlocking Generalization in Robot Learning through Video World Models","url":"https://arxiv.org/abs/2505.12705"},{"title":"(PDF) DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories","url":"https://www.researchgate.net/publication/391878946_DreamGen_Unlocking_Generalization_in_Robot_Learning_through_Neural_Trajectories"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories","url":"https://arxiv.org/html/2505.12705v1"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DreamGen:-Unlocking-Generalization-in-Robot-through-Jang-Ye/52be025b0de2e1c0783dd6d7eb5c8114e039479e"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Video World Models","url":"https://arxiv.org/html/2505.12705"},{"title":"GitHub - NVIDIA/GR00T-Dreams: DreamGen: Nvidia GEAR Lab's initiative to solve the robotics data problem using world models · GitHub","url":"https://github.com/nvidia/GR00T-dreams"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Video World Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250512705J/abstract"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Video World Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2505.12705"},{"title":"DreamGen","url":"https://research.nvidia.com/labs/gear/dreamgen/"},{"title":"GR00T-Dreams (DreamGen) | sudoremove","url":"https://sudoremove.com/en/knowledge/models/dreamgen/"}]

Based on the search results, here's what I found about DreamGen (arXiv:2505.12705):

## Overview

DreamGen is a simple yet highly effective 4-stage pipeline for training robot policies that generalize across behaviors and environments through neural trajectories - synthetic robot data generated from video world models.

## Key Features

DreamGen leverages state-of-the-art image-to-video generative models, adapting them to the target robot embodiment to produce photorealistic synthetic videos of familiar or novel tasks in diverse environments. Since these models generate only videos, they recover pseudo-action sequences using either a latent action model or an inverse-dynamics model (IDM).

## Performance Results

DreamGen unlocks strong behavior and environment generalization: a humanoid robot can perform 22 new behaviors in both seen and unseen environments, while requiring teleoperation data from only a single pick-and-place task in one environment. DreamGen shows consistent gains on success rate across all robots: from 37% to 46.4% on average of 4 GR1 humanoid tasks, 23% to 37% on average of 3 Franka tasks, and from 21% to 45.5% on average of 2 SO-100 tasks, all using just 10 to 13 real-world trajectories per task.

## Evaluation

To evaluate the pipeline systematically, the researchers introduce DreamGen Bench, a video generation benchmark that shows a strong correlation between benchmark performance and downstream policy success.

The paper was authored by Joel Jang and 27 other co-authors and was published on arXiv in May 2025. Code is available at https://github.com/NVIDIA/GR00T-Dreams.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02d312c1-7632-40d4-badc-32bd31b3c1dc",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "cd06b8fd-ff44-4749-abf5-15b2bdebc0eb",
  "sourceToolAssistantUUID": "02d312c1-7632-40d4-badc-32bd31b3c1dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T13:03:19.915Z_

<details><summary>↩ Tool result · `toolu_01DVW4DLUmc8DxcuZ18dA4Hc`</summary>

```text
Web search results for query: "loco-manipulation data generation bipedal robots 2026 arxiv"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Humanoid Loco-Manipulations Pattern Generation and Stabilization Control","url":"https://arxiv.org/html/2505.24116"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v2"},{"title":"Bipedalism for Quadrupedal Robots: Versatile Loco-Manipulation through Risk-Adaptive Reinforcement Learning","url":"https://arxiv.org/html/2507.20382v1"},{"title":"[2507.20382] Bipedalism for Quadrupedal Robots: Versatile Loco-Manipulation through Risk-Adaptive Reinforcement Learning","url":"https://arxiv.org/abs/2507.20382"},{"title":"Deep Reinforcement Learning for Robotic Bipedal Locomotion: A Brief Survey","url":"https://arxiv.org/html/2404.17070v2"},{"title":"Rambo: RL-Augmented Model-Based Whole-Body Control for Loco-Manipulation","url":"https://arxiv.org/html/2504.06662v4"},{"title":"MLM: Learning Multi-task Loco-Manipulation Whole-Body Control for Quadruped Robot with Arm","url":"https://arxiv.org/html/2508.10538v1"},{"title":"Generative Artificial Intelligence in Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2503.03464v1"},{"title":"Frontiers | Imitation learning for legged robot locomotion: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/full"}]

I found several relevant results on loco-manipulation for bipedal robots from arXiv. Here's what the search revealed:

## Recent 2026 arXiv Papers

EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration was published on arXiv in 2026.02. Additionally, several other 2026 papers on humanoid loco-manipulation have been published, including Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation and ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation.

## Data Generation and Training Approaches

A recent framework develops a real-world and simulation dual data driven RL framework for quadruped robot whole-body loco-manipulation control. This approach uses UMI-like methods to obtain only end-effector 6D manipulation trajectories, and integrates real-world multi-task manipulation trajectories into simulation to efficiently generate training data that interacts with the environment.

Some work employs LLM-driven systems for task generation and assignment, producing 300 episodes for loco-manipulation benchmarks.

## Control Methods

Rambo is a hybrid framework that integrates model-based whole-body control within a feedback policy trained with reinforcement learning, where the model-based module generates feedforward torques by solving a quadratic program.

The search results show significant active research in 2025-2026 on combining data generation techniques with bipedal and humanoid robot loco-manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "064a0cbf-2519-4e28-b942-3e65cb20bd63",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "7988115b-d317-41fd-808f-bf115252717b",
  "sourceToolAssistantUUID": "064a0cbf-2519-4e28-b942-3e65cb20bd63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T13:03:28.126Z_

<details><summary>↩ Tool result · `toolu_01WZhc4Q89EV2vyGXoo18Buq`</summary>

```text
Web search results for query: "whole-body humanoid data generation 2025 2026"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Gait Generation and Motion Implementation of Humanoid Robots Based on Hierarchical Whole-Body Control","url":"https://www.mdpi.com/2079-9292/14/23/4714"},{"title":"A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/41468330/"},{"title":"[2506.20487] A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots","url":"https://arxiv.org/abs/2506.20487"},{"title":"Whole-body control for humanoid robot locomotion | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/whole-body-control-for-humanoid-robot-locomotion-2/"},{"title":"Research on humanoid robot motion generation and real-time trajectory optimization based on sparse attention mechanism in deep reinforcement learning | Discover Artificial Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44163-025-00603-3"},{"title":"Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation","url":"https://arxiv.org/html/2510.08807v1"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"AI Humanoid Robots 2026: Technology, Builders & Future","url":"https://www.articsledge.com/post/ai-humanoid-robots"},{"title":"Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260109518H/abstract"}]

Based on the search results, here's what I found regarding whole-body humanoid data generation in 2025-2026:

## Recent Research and Development

Multiple papers from 2025-2026 focus on whole-body humanoid control, including topics such as "Whole-body Multi-contact Motion Control for Humanoid Robots Based on Distributed Tactile Sensors" and "Scalable and General Whole-Body Control for Cross-Humanoid Locomotion."

## Data Generation and Datasets

A comprehensive dataset for humanoid manipulation has been created using two Unitree humanoid robots: the 29-DoF G1 with 7-DoF three-fingered dexterous hands and the 27-DoF H1 with 6-DoF INSPIRE hands, both equipped with Intel RealSense RGB-D cameras and a Livox LiDAR system.

Data collection uses an Apple Vision Pro to capture wrist and finger keypoints, with finger motions mapped onto the robot's dexterous hands via a dex-retargeting system, and wrist poses converted into arm joint commands through inverse kinematics algorithms.

## Key Challenges and Solutions

Recent research addresses three major bottlenecks in humanoid robot motion generation: motion discretization, strategy homogeneity, and dynamic response delay, using deep reinforcement learning frameworks integrated with sparse attention mechanisms.

Behavior foundation models (BFMs) have emerged as a new paradigm that leverages large-scale pre-training to learn reusable primitive skills and broad behavioral priors, enabling zero-shot or rapid adaptation to a wide range of downstream tasks.

The field is rapidly advancing with both data collection systems and control frameworks being developed to improve whole-body humanoid capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c3c3bc8-0473-454f-b365-d7c648996fc9",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "89ce30d7-1b55-476b-91b7-ec65e8454f37",
  "sourceToolAssistantUUID": "1c3c3bc8-0473-454f-b365-d7c648996fc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T13:03:30.336Z_

Now let me search more specifically for DreamGen's scope to verify whether it addresses mobile manipulation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89ce30d7-1b55-476b-91b7-ec65e8454f37",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw9TD4aayU7RERkfV4E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35a6b97e-203f-4ae5-ba2f-585bc9a1ddf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V5J1jibn5PoTUjhdFjWUnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 937,
      "cache_creation_input_tokens": 6090,
      "cache_read_input_tokens": 16883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6090,
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

_source line 16 · 2026-05-10T13:03:30.969Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017xAv3og6Srp9bNTsEkhiW4`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.12705",
  "prompt": "Does DreamGen address mobile manipulation, loco-manipulation, humanoid locomotion, or only stationary manipulation? What are the specific robot embodiments and tasks evaluated?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35a6b97e-203f-4ae5-ba2f-585bc9a1ddf7",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw9TD4aayU7RERkfV4E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cad50a19-d1f3-4da1-a704-158da098e7f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V5J1jibn5PoTUjhdFjWUnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 937,
      "cache_creation_input_tokens": 6090,
      "cache_read_input_tokens": 16883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6090,
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

_source line 17 · 2026-05-10T13:03:31.386Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013PKA6vFtjbngkZtcLk7UAT`</summary>

```json
{
  "query": "SE(3) object-centric demonstration humanoid manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cad50a19-d1f3-4da1-a704-158da098e7f6",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw9TD4aayU7RERkfV4E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "64c37ca1-4377-4e2f-bd86-29cc344e16cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V5J1jibn5PoTUjhdFjWUnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 937,
      "cache_creation_input_tokens": 6090,
      "cache_read_input_tokens": 16883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6090,
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

_source line 18 · 2026-05-10T13:03:31.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Svg6y5m3C4QJqfyBGosJ4C`</summary>

```json
{
  "query": "DexMimicGen bimanual dexterous 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64c37ca1-4377-4e2f-bd86-29cc344e16cb",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw9TD4aayU7RERkfV4E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "07019c9b-26ee-4a60-a23d-ed1228fcd795",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V5J1jibn5PoTUjhdFjWUnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 937,
      "cache_creation_input_tokens": 6090,
      "cache_read_input_tokens": 16883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6090,
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

_source line 19 · 2026-05-10T13:03:31.874Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012otXYvERioC85fB7D5kXXg`</summary>

```json
{
  "query": "VisualMimic humanoid loco-manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07019c9b-26ee-4a60-a23d-ed1228fcd795",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011Catw9TD4aayU7RERkfV4E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c1eacfb-d971-4f5b-87fb-fba8b3c5dbcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V5J1jibn5PoTUjhdFjWUnt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 937,
      "cache_creation_input_tokens": 6090,
      "cache_read_input_tokens": 16883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6090,
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

_source line 20 · 2026-05-10T13:03:34.341Z_

<details><summary>↩ Tool result · `toolu_017xAv3og6Srp9bNTsEkhiW4`</summary>

```text
# DreamGen: Robot Embodiments and Tasks

Based on the provided content, the abstract mentions that "a humanoid robot can perform 22 new behaviors in both seen and unseen environments," indicating evaluation on a humanoid embodiment. However, the webpage excerpt does not provide detailed specifications about the specific tasks evaluated or whether mobile manipulation, loco-manipulation, or humanoid locomotion were addressed.

The abstract indicates the system was tested on "pick-and-place" task data for training, but the document does not elaborate on the full range of manipulation types or locomotion capabilities assessed. To determine the specific robot embodiments tested and complete task breakdown, you would need to access the full paper PDF or visit the research website linked in the materials.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cad50a19-d1f3-4da1-a704-158da098e7f6",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "c8aee27d-90ba-49a4-8ca8-a5daba7bd8b7",
  "sourceToolAssistantUUID": "cad50a19-d1f3-4da1-a704-158da098e7f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T13:03:37.671Z_

<details><summary>↩ Tool result · `toolu_01Svg6y5m3C4QJqfyBGosJ4C`</summary>

```text
Web search results for query: "DexMimicGen bimanual dexterous 2024 2025"

Links: [{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://dexmimicgen.github.io/"},{"title":"[2410.24185] DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://arxiv.org/abs/2410.24185"},{"title":"GitHub - NVlabs/dexmimicgen: This code corresponds to simulation environments used as part of the DexMimicGen project. · GitHub","url":"https://github.com/NVlabs/dexmimicgen/"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning | NVIDIA Seattle Robotics Lab","url":"https://research.nvidia.com/labs/srl/publication/jiang-2025-dex-mimic-gen/"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://www.researchgate.net/publication/395229889_DexMimicGen_Automated_Data_Generation_for_Bimanual_Dexterous_Manipulation_via_Imitation_Learning"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://arxiv.org/html/2410.24185v2"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241024185J/abstract"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734v1"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/11127273/11127223/11127809.pdf"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/dexmimicgen-automated-data-generation-bimanual-dexterous-manipulation"}]

Based on the search results, here's what I found about DexMimicGen:

## Overview

DexMimicGen is a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands.

## Key Innovation

The core idea is to leverage a small set of human demonstrations and use demonstration transformation and replay in physical simulation to automatically generate large amounts of training data suitable for imitation learning in the bimanual dexterous manipulation setting.

## Technical Approach

Bimanual dexterous manipulation involves three types of subtasks where the two arms need to achieve sub-goals independently, with coordination, and following a specific order. First, each arm must operate independently of the other arm to achieve different goals. Next, the arms must coordinate to accomplish a shared goal. Finally, one arm's subtask must be completed before the next one can be attempted.

## Real-World Application

The system generated 21K demos across multiple tasks from just 60 source human demos and includes a real-to-sim-to-real pipeline deployed on a real-world humanoid can sorting task.

## Publication

DexMimicGen was presented at the 2025 IEEE International Conference on Robotics and Automation (ICRA).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07019c9b-26ee-4a60-a23d-ed1228fcd795",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "f6a807cb-b965-4a8a-9720-3fb7a90d3165",
  "sourceToolAssistantUUID": "07019c9b-26ee-4a60-a23d-ed1228fcd795",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T13:03:39.790Z_

<details><summary>↩ Tool result · `toolu_012otXYvERioC85fB7D5kXXg`</summary>

```text
Web search results for query: "VisualMimic humanoid loco-manipulation 2025"

Links: [{"title":"GitHub - visualmimic/VisualMimic: [arXiv 2025] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation · GitHub","url":"https://github.com/visualmimic/VisualMimic"},{"title":"VisualMimic","url":"https://visualmimic.github.io/"},{"title":"[2509.20322] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/abs/2509.20322"},{"title":"[2509.20322v1] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/abs/2509.20322v1"},{"title":"VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation - Paper Detail","url":"https://deeplearn.org/arxiv/639531/visualmimic:-visual-humanoid-loco-manipulation-via-motion-tracking-and-generation"},{"title":"VisualMimic Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/html/2509.20322v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation","url":"https://viral-humanoid.github.io/"},{"title":"(PDF) VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://www.researchgate.net/publication/395807090_VisualMimic_Visual_Humanoid_Loco-Manipulation_via_Motion_Tracking_and_Generation"}]

I found comprehensive information about VisualMimic. Here's a summary of the research:

## Overview

VisualMimic is a visual sim-to-real framework that unifies egocentric vision with hierarchical whole-body control for humanoid robots. The paper was published on arXiv in 2025 by researchers from Stanford University including Shaofeng Yin, Yanjie Ze, Hong-Xing Yu, C. Karen Liu, and Jiajun Wu.

## Key Technical Approach

VisualMimic combines a task-agnostic low-level keypoint tracker—trained from human motion data via a teacher-student scheme—with a task-specific high-level policy that generates keypoint commands from visual and proprioceptive input. To ensure stable training, the framework injects noise into the low-level policy and clips high-level actions using human motion statistics.

## Capabilities and Tasks

VisualMimic enables zero-shot transfer of visuomotor policies trained in simulation to real humanoid robots, accomplishing a wide range of loco-manipulation tasks such as box lifting, pushing, football dribbling, and kicking. The policies also generalize robustly to outdoor environments.

## Real-World Results

The humanoid robot can lift a 0.5-kilogram box to a height of 1 meter, push a very large box (similar height as the robot and weight 3.8 kilograms) straight and steady with its whole body, dribble a football with the fluency of an experienced player, and kick a box forward with alternating feet.

The code and checkpoints have been made available, with the Sim2Sim pipeline released as of September 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c1eacfb-d971-4f5b-87fb-fba8b3c5dbcf",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "f225c677-7957-4013-8e3c-2084bdeced63",
  "sourceToolAssistantUUID": "7c1eacfb-d971-4f5b-87fb-fba8b3c5dbcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T13:03:44.233Z_

<details><summary>↩ Tool result · `toolu_013PKA6vFtjbngkZtcLk7UAT`</summary>

```text
Web search results for query: "SE(3) object-centric demonstration humanoid manipulation 2025 2026"

Links: [{"title":"NVIDIA Research Breakthroughs Put Advanced Robots in Motion | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/nvidia-research-robotics-icra-2025/"},{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation | NVIDIA Seattle Robotics Lab","url":"https://research.nvidia.com/labs/srl/publication/hsu-2025-spot/"},{"title":"Yuke Zhu GDC 3.422, 2317 Speedway, Austin, TX, 78712 USA https://yukezhu.me","url":"https://yukezhu.me/documents/yukez.pdf"},{"title":"Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology","url":"https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"},{"title":"A Survey of Embodied Learning for Object-centric Robotic Manipulation | Machine Intelligence Research | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11633-025-1542-8"},{"title":"UT Austin at the International Conference on Robotics and Automation (ICRA) 2025 | Texas Robotics","url":"https://robotics.utexas.edu/news/304"},{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"Frontiers | Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1682437/full"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"AI Humanoid Robots 2026: Technology, Builders & Future","url":"https://www.articsledge.com/post/ai-humanoid-robots"}]

Based on the web search results, here's what I found regarding SE(3) object-centric demonstration humanoid manipulation research in 2025-2026:

## Key Finding: SPOT Framework

SPOT is a learning framework that uses SE(3) pose trajectory diffusion for object-centric manipulation, enabling cross-embodiment generalization.

SPOT was authored by Cheng-Chun Hsu, Bowen Wen, Jie Xu, Yashraj Narang, Xiaolong Wang, Yuke Zhu, Joydeep Biswas, and Stan Birchfield in May 2025. This research was presented at ICRA (International Conference on Robotics and Automation) 2025.

## Related Research Context

The search results show that embodied learning for object-centric robotic manipulation is a rapidly developing and challenging area in embodied AI that is crucial for advancing next-generation intelligent robots.

Additionally, HOVER, a unified neural controller for humanoid robots, was developed to seamlessly transition between locomotion, manipulation and other modes.

The SPOT framework appears to be a significant contribution to the field, representing recent advances in SE(3) pose-based manipulation learning for humanoid robots with object-centric approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64c37ca1-4377-4e2f-bd86-29cc344e16cb",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "e47552dc-df7a-4814-979b-1dadd9fa1465",
  "sourceToolAssistantUUID": "64c37ca1-4377-4e2f-bd86-29cc344e16cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T13:03:45.421Z_

Let me search for more specific information about coupled SE(3) stance approaches and any recent work on procedural data generation for humanoid robots:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e47552dc-df7a-4814-979b-1dadd9fa1465",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwAdnpt352rRSwd7pwx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9e57d27-d30b-49f3-917b-ac65af1b87dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KecPtuiMW2b4q1EAJCRMQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1999,
      "cache_creation_input_tokens": 2474,
      "cache_read_input_tokens": 22973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2474,
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

_source line 25 · 2026-05-10T13:03:45.866Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019VnrLGr2foQuVKSBH1SSqr`</summary>

```json
{
  "query": "\"coupled SE(3)\" OR \"stance+manipulation\" humanoid 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9e57d27-d30b-49f3-917b-ac65af1b87dc",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwAdnpt352rRSwd7pwx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c95874b0-4caf-468a-8c8b-5fc03bd18e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KecPtuiMW2b4q1EAJCRMQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1999,
      "cache_creation_input_tokens": 2474,
      "cache_read_input_tokens": 22973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2474,
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

_source line 26 · 2026-05-10T13:03:46.082Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012xiZSN63sD9ZsocgWsic27`</summary>

```json
{
  "query": "procedural data generation humanoid robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c95874b0-4caf-468a-8c8b-5fc03bd18e7e",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwAdnpt352rRSwd7pwx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3b631e8a-1762-477c-910c-fa2aec28f9f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KecPtuiMW2b4q1EAJCRMQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1999,
      "cache_creation_input_tokens": 2474,
      "cache_read_input_tokens": 22973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2474,
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

_source line 27 · 2026-05-10T13:03:46.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019upWwbrnQdQdyxaH5ifVbS`</summary>

```json
{
  "query": "ResMimic humanoid loco-manipulation residual learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b631e8a-1762-477c-910c-fa2aec28f9f6",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwAdnpt352rRSwd7pwx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d8e5e44d-bc10-49d4-ab29-6e656c0a2e2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KecPtuiMW2b4q1EAJCRMQX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1999,
      "cache_creation_input_tokens": 2474,
      "cache_read_input_tokens": 22973,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2474
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1999,
          "output_tokens": 198,
          "cache_read_input_tokens": 22973,
          "cache_creation_input_tokens": 2474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2474,
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

_source line 28 · 2026-05-10T13:03:53.610Z_

<details><summary>↩ Tool result · `toolu_012xiZSN63sD9ZsocgWsic27`</summary>

```text
Web search results for query: "procedural data generation humanoid robot 2025 2026"

Links: [{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"AI Humanoid Robots 2026: Technology, Builders & Future","url":"https://www.articsledge.com/post/ai-humanoid-robots"},{"title":"Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology","url":"https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"},{"title":"Humanoid Robots News | AI Breakthroughs, Robotics Trends & Synthetic Updates","url":"https://humanoid.press/"},{"title":"Will 2026 be the year of the Humanoid Robot?","url":"https://www.datapro.news/p/will-2026-be-the-year-of-the-humanoid-robot"},{"title":"Humanoid robots in 2026: Types, prices, and what’s next - Standard Bots","url":"https://standardbots.com/blog/humanoid-robot"},{"title":"Humanoid Robots 2025: The Race to Useful Intelligence - Edge AI and Vision Alliance","url":"https://www.edge-ai-vision.com/2025/11/humanoid-robots-2025-the-race-to-useful-intelligence/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Use Case: NVIDIA Computing Platforms for Humanoid Robots","url":"https://www.nvidia.com/en-us/use-cases/humanoid-robots/"},{"title":"Industry Insights: Humanoid Robots in 2025: The Next Stage of Evolution","url":"https://www.automate.org/industry-insights/humanoid-robots-are-evolving"}]

I've completed the web search for "procedural data generation humanoid robot 2025 2026". Here are the key findings:

## Data Generation in Humanoid Robotics

A single humanoid robot deployed on a production line generates terabytes of high-dimensional data every hour: 3D point clouds from LiDAR, RGB-D video streams, tactile sensor data from force-sensitive grippers, joint-level telemetry, and IMU readings.

The challenge for 2026 is not just collecting this data, but curating it into a high-quality "Digital Nervous System" that can be used to improve the robot's performance continuously.

## Procedural/Synthetic Data Generation

A major advancement in addressing data collection challenges is the use of synthetic data generation. The NVIDIA Isaac GR00T-Dreams blueprint generates vast amounts of synthetic trajectory data using NVIDIA Cosmos™ world foundation models, prompted by a single image and language instructions. This enables robots to learn new tasks in unfamiliar environments without needing specific teleoperation data.

## Data Infrastructure

Boston Dynamics' RMAC (Robot Metaplant Application Centre) opens in 2026 as a "data factory" for training Atlas, serving as a centralised hub for data collection and building the training datasets that will teach Atlas the full range of tasks.

## Real-World Deployment Context

Teleoperated sessions with 1X's NEO robot both solve tasks and generate training data, so the robot's "skills library" grows over time. This represents a practical approach to continuous data collection and model improvement in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b631e8a-1762-477c-910c-fa2aec28f9f6",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "de4e8a06-9df5-4110-8c1f-c35cff30c7b4",
  "sourceToolAssistantUUID": "3b631e8a-1762-477c-910c-fa2aec28f9f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T13:03:53.748Z_

<details><summary>↩ Tool result · `toolu_019upWwbrnQdQdyxaH5ifVbS`</summary>

```text
Web search results for query: "ResMimic humanoid loco-manipulation residual learning 2025"

Links: [{"title":"[2510.05070] ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning","url":"https://arxiv.org/abs/2510.05070"},{"title":"ResMimic: From General Motion Tracking to Humanoid Whole-Body Loco-Manipulation via Residual Learning","url":"https://resmimic.github.io/"},{"title":"[2510.05070v1] ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning","url":"https://arxiv.org/abs/2510.05070v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning | BibSonomy","url":"https://www.bibsonomy.org/bibtex/279fd76c106c4a9cf8e406a2fcd1d79d1/kolev"},{"title":"ResMimic: From General Motion Tracking to Humanoid Whole-body","url":"https://arxiv.org/pdf/2510.05070"},{"title":"(PDF) ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning","url":"https://www.researchgate.net/publication/396250470_ResMimic_From_General_Motion_Tracking_to_Humanoid_Whole-body_Loco-Manipulation_via_Residual_Learning"},{"title":"Sim-to-Real Learning for Humanoid Box Loco-Manipulation | Request PDF","url":"https://www.researchgate.net/publication/382977746_Sim-to-Real_Learning_for_Humanoid_Box_Loco-Manipulation"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model","url":"https://arxiv.org/html/2602.11758v1"}]

I found detailed information about ResMimic. Here's a summary of the research:

## ResMimic Overview

ResMimic is a two-stage residual learning framework for precise and expressive humanoid control from human motion data. The system was evaluated in both simulation and on a real Unitree G1 humanoid.

## How It Works

The framework operates in two stages:

1. **General Motion Tracking (GMT)**: A GMT policy, trained on large-scale human-only motion, serves as a task-agnostic base for generating human-like whole-body movements.

2. **Residual Refinement**: An efficient but precise residual policy is then learned to refine the GMT outputs to improve locomotion and incorporate object interaction.

## Key Technical Features

The design includes: (i) a point-cloud-based object tracking reward for smoother optimization, (ii) a contact reward that encourages accurate humanoid body-object interactions, and (iii) a curriculum-based virtual object controller to stabilize early training.

## Results and Applications

Results show substantial gains in task success, training efficiency, and robustness over strong baselines. Humanoid whole-body loco-manipulation promises transformative capabilities for daily service and warehouse tasks.

The paper was published on arXiv in October 2025 (arXiv:2510.05070) by authors including Siheng Zhao, Yanjie Ze, Yue Wang, C. Karen Liu, Pieter Abbeel, Guanya Shi, and Rocky Duan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8e5e44d-bc10-49d4-ab29-6e656c0a2e2b",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "1eaa49db-79ab-4123-aa7f-fe98059e3b38",
  "sourceToolAssistantUUID": "d8e5e44d-bc10-49d4-ab29-6e656c0a2e2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T13:03:53.780Z_

<details><summary>↩ Tool result · `toolu_019VnrLGr2foQuVKSBH1SSqr`</summary>

```text
Web search results for query: ""coupled SE(3)" OR "stance+manipulation" humanoid 2025 2026"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"A Two-Stage Reinforcement Learning Framework for Humanoid Robot Sitting and Standing-Up - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12650239/"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"Humanoid robots in 2026: Types, prices, and what’s next - Standard Bots","url":"https://standardbots.com/blog/humanoid-robot"},{"title":"It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots","url":"https://arxiv.org/pdf/2510.10206"},{"title":"Humanoid dexterous hands from structure to gesture semantics for enhanced human–robot interaction: A review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S266737972500049X"},{"title":"Humanoids conquered CES 2026 - Humanoid.guide","url":"https://humanoid.guide/humanoids-ces-2026/"},{"title":"Humanoid Robots 2025: Guide to All Models - Qviro Blog","url":"https://qviro.com/blog/humanoid-robots-all-models/"},{"title":"Humanoid Robots Guide (2025): Types, History, Best Models, Anatomy and Applications | Top 3D Shop","url":"https://top3dshop.com/blog/humanoid-robots-types-history-best-models"}]

I've completed the web search for the query "coupled SE(3) stance manipulation humanoid 2025 2026". The results show a rich landscape of recent humanoid robotics research and development. Here are the key findings:

## Academic Research

Recent research addresses coupled dynamics in humanoid interactions, where single-humanoid approaches that neglect coupled dynamics cause critical consequences including misaligned contacts and loss of coordinated behaviors in closely coupled motions such as hand-holding or shoulder contact, highlighting the need for approaches that explicitly model inter-agent dynamics.

In sit-stand tasks, common "phase coupling" techniques used in walking control (such as synchronization between left and right legs) completely fail, and a two-stage reinforcement learning framework decouples action discovery from action refinement to address challenges in sit-stand control.

## Humanoid Loco-Manipulation Advances

Recent papers from 2025-2026 include FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation (2025.05), FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid (2026.03), and ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation (2025.07).

## Commercial Development

CES 2026 in Las Vegas reaffirmed that humanoid robotics is no longer niche, with industry heavyweights like Nvidia, LG, Boston Dynamics and Chinese robotics firms spotlighting advancements that push humanoids closer to everyday utility.

The search results reveal significant progress in both the theoretical foundations (SE(3) group theory applications) and practical implementations of stance and manipulation for humanoid robots during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c95874b0-4caf-468a-8c8b-5fc03bd18e7e",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "3deb767f-92a0-42b9-b5d8-f0d8833669aa",
  "sourceToolAssistantUUID": "c95874b0-4caf-468a-8c8b-5fc03bd18e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T13:03:54.949Z_

Now let me get more details on the specific papers to understand their technical approaches better:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3deb767f-92a0-42b9-b5d8-f0d8833669aa",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwBLZGfvVUYDjkSvSiE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "526a4b1c-e568-421c-a0e3-06459deb838f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R7XaQNM8JF1RdjXCiJmxCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1965,
      "cache_creation_input_tokens": 3159,
      "cache_read_input_tokens": 25447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3159,
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

_source line 32 · 2026-05-10T13:03:55.805Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FwvyURFMHW6dCciVCdmj3b`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.05070",
  "prompt": "What is ResMimic's technical approach? Does it use SE(3) object-centric representations for demonstration multiplication? How does it encode the stance and manipulation together?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "526a4b1c-e568-421c-a0e3-06459deb838f",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwBLZGfvVUYDjkSvSiE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e327da64-435e-4d88-bc1c-73f3ddb6cecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R7XaQNM8JF1RdjXCiJmxCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1965,
      "cache_creation_input_tokens": 3159,
      "cache_read_input_tokens": 25447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3159,
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

_source line 33 · 2026-05-10T13:03:56.030Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VFPt4wuyMBMHitE4Ay9b7m`</summary>

```json
{
  "query": "OmniRetarget interaction mesh demonstration multiplication 2509.26633"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e327da64-435e-4d88-bc1c-73f3ddb6cecf",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwBLZGfvVUYDjkSvSiE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0a91c0af-8ad0-478a-a5c1-20311b75d1e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R7XaQNM8JF1RdjXCiJmxCR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1965,
      "cache_creation_input_tokens": 3159,
      "cache_read_input_tokens": 25447,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3159
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1965,
          "output_tokens": 186,
          "cache_read_input_tokens": 25447,
          "cache_creation_input_tokens": 3159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3159,
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

_source line 34 · 2026-05-10T13:03:59.948Z_

<details><summary>↩ Tool result · `toolu_01FwvyURFMHW6dCciVCdmj3b`</summary>

```text
# ResMimic's Technical Approach

Based on the provided abstract and content, I cannot identify specific details about SE(3) object-centric representations, demonstration multiplication, or how the system encodes stance and manipulation together.

What the available information reveals is that ResMimic employs "a two-stage residual learning framework" where a general motion tracking policy serves as a foundation, then "an efficient but precise residual policy is then learned to refine the GMT outputs." 

The framework incorporates three specific technical components: a "point-cloud-based object tracking reward," a "contact reward that encourages accurate humanoid body-object interactions," and a "curriculum-based virtual object controller."

To obtain details about SE(3) representations, demonstration multiplication methodology, and the specific encoding mechanisms for stance and manipulation, you would need to access the full paper PDF or HTML version linked on this arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e327da64-435e-4d88-bc1c-73f3ddb6cecf",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "7e009062-8e9f-4482-a973-bb0b5e2dade3",
  "sourceToolAssistantUUID": "e327da64-435e-4d88-bc1c-73f3ddb6cecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T13:04:01.504Z_

<details><summary>↩ Tool result · `toolu_01VFPt4wuyMBMHitE4Ay9b7m`</summary>

```text
Web search results for query: "OmniRetarget interaction mesh demonstration multiplication 2509.26633"

Links: [{"title":"[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633"},{"title":"OmniRetarget","url":"https://omniretarget.github.io/"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid","url":"https://arxiv.org/pdf/2509.26633"},{"title":"OmniRetarget: Humanoid Data Generation","url":"https://www.emergentmind.com/papers/2509.26633"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/html/2509.26633v2"},{"title":"Paper page - OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://huggingface.co/papers/2509.26633"},{"title":"[2509.26633v1] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633v1"},{"title":"[PDF] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OmniRetarget:-Interaction-Preserving-Data-for-and-Yang-Huang/234018fa87b6c649830e1e6274362c58445a9fbc"},{"title":"(PDF) OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://www.researchgate.net/publication/396049126_OmniRetarget_Interaction-Preserving_Data_Generation_for_Humanoid_Whole-Body_Loco-Manipulation_and_Scene_Interaction"},{"title":"Embodied AI Reading Notes on X: \"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction Project: https://t.co/X8p5jesI8X Paper: https://t.co/qkaGwJjWSY New Paper from Amazon FAR proves that by leveraging high quality data from a https://t.co/JkrlmhZykL\" / X","url":"https://x.com/EmbodiedAIRead/status/1976853666662694987"}]

Based on the search results, here's what I found about OmniRetarget (arXiv:2509.26633):

## Overview

OmniRetarget is an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects.

## Key Technical Approach

By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Delaunay tetrahedralization is used to form the mesh, ensuring accurate contact modeling.

## Capabilities

Preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations.

## Evaluation Results

OmniRetarget was evaluated by retargeting motions from OMOMO, LAFAN1, and in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks.

The paper was published on September 30, 2025, by researchers from Amazon FAR, MIT, UC Berkeley, Stanford University, and CMU.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a91c0af-8ad0-478a-a5c1-20311b75d1e2",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "943c4b47-7023-4f0f-975b-d5d67a2cac5e",
  "sourceToolAssistantUUID": "0a91c0af-8ad0-478a-a5c1-20311b75d1e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-10T13:04:02.811Z_

Let me fetch the full OmniRetarget paper to understand its technical depth on interaction modeling:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "943c4b47-7023-4f0f-975b-d5d67a2cac5e",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwBub7zXuZnBUVRb9Na",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "249b289f-4219-49ab-b4fb-32709e104d18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D6U3Tjz2o19cxSi6gFhPnW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3477,
      "cache_read_input_tokens": 28606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3477,
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

_source line 37 · 2026-05-10T13:04:03.676Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VxecXJDL5j2QU3KYD76Xub`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.26633",
  "prompt": "What is OmniRetarget's core technical innovation? Does it use SE(3) representations or object-centric framing? How does the interaction mesh encode coupled stance and manipulation? What kind of demonstration multiplication does it perform?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "249b289f-4219-49ab-b4fb-32709e104d18",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwBub7zXuZnBUVRb9Na",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3e1d5b10-5972-4d73-8b74-5eaae949d07f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D6U3Tjz2o19cxSi6gFhPnW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3477,
      "cache_read_input_tokens": 28606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3477,
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

_source line 38 · 2026-05-10T13:04:03.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DJquh4cNnwAH3vzh4p8yC4`</summary>

```json
{
  "query": "\"DreamGen\" \"loco-manipulation\" OR \"locomotion\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e1d5b10-5972-4d73-8b74-5eaae949d07f",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwBub7zXuZnBUVRb9Na",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60f4b5ea-2a89-4874-a278-a83f0cff1ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D6U3Tjz2o19cxSi6gFhPnW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3477,
      "cache_read_input_tokens": 28606,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3477
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 203,
          "cache_read_input_tokens": 28606,
          "cache_creation_input_tokens": 3477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3477,
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

_source line 39 · 2026-05-10T13:04:07.921Z_

<details><summary>↩ Tool result · `toolu_01VxecXJDL5j2QU3KYD76Xub`</summary>

```text
# OmniRetarget: Technical Innovation Summary

Based on the available abstract, here's what can be confirmed:

**Core Innovation:**
OmniRetarget's primary technical contribution is an "interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects." The method minimizes Laplacian deformation between human and robot meshes while enforcing kinematic constraints.

**SE(3) Representations & Object-Centric Framing:**
The provided content does not discuss SE(3) representations or object-centric framing approaches.

**Interaction Mesh Encoding:**
The document confirms the interaction mesh preserves "task-relevant interactions" and "contact relationships" but doesn't detail how coupled stance and manipulation are specifically encoded in the architecture.

**Demonstration Multiplication:**
The abstract confirms OmniRetarget enables "efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations," generating "over 8-hour trajectories" from source datasets (OMOMO, LAFAN1, and in-house MoCap).

**Note:** For deeper technical details on the interaction mesh architecture, SE(3) handling, and specific encoding mechanisms, the full paper PDF would be necessary, as the abstract provided focuses on results and practical applications rather than algorithmic specifics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e1d5b10-5972-4d73-8b74-5eaae949d07f",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "3f8c8d35-5d17-4f05-889f-e7e7c30fc4fd",
  "sourceToolAssistantUUID": "3e1d5b10-5972-4d73-8b74-5eaae949d07f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T13:04:10.815Z_

<details><summary>↩ Tool result · `toolu_01DJquh4cNnwAH3vzh4p8yC4`</summary>

```text
Web search results for query: ""DreamGen" "loco-manipulation" OR "locomotion""

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"DreamControl: Human-Inspired Whole-Body Humanoid Control for","url":"https://genrobo.github.io/DreamControl/static/paper/DreamControl_arxiv.pdf"},{"title":"Paper-List/README.md at main · YanjieZe/Paper-List","url":"https://github.com/YanjieZe/Paper-List/blob/main/README.md"},{"title":"Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models","url":"https://arxiv.org/html/2504.16843v1"},{"title":"Robust Visuomotor Control for Humanoid Loco-Manipulation Using Hybrid Reinforcement Learning","url":"https://www.mdpi.com/2313-7673/10/7/469"},{"title":"[2604.00202] DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors","url":"https://arxiv.org/abs/2604.00202"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"GitHub - aCodeDog/awesome-loco-manipulation · GitHub","url":"https://github.com/aCodeDog/awesome-loco-manipulation"},{"title":"Versatile multicontact planning and control for legged loco-manipulation | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.adg5014"},{"title":"Dynamic Loco-Manipulation via Hybrid Whole-body Bilateral Teleoperation of a Wheeled Humanoid","url":"https://arxiv.org/html/2407.12189"}]

Based on the web search results, I found information related to your query, though the specific term "DreamGen" does not appear prominently in the results. However, I did find relevant information about related work in humanoid loco-manipulation:

## Key Findings:

**DreamControl (Related Work):**
The search results reveal DreamControl, which addresses these issues by leveraging off-the-shelf human motion diffusion models as a generative prior to guide RL policies during training. There's also an improved framework that trains a guided diffusion model directly in the humanoid robot's motion space, aggregating diverse human and robot datasets into a unified embodiment space.

**Loco-Manipulation Research:**
The results show extensive research in humanoid loco-manipulation. In loco-manipulation task, a humanoid robot performs bipedal locomotion and object manipulation simultaneously or alternatively, and it involves coordinate movement of all four limbs of a humanoid robot.

**Recent Approaches:**
One recent work uses the capabilities of latent diffusion models (LDMs) to generate realistic RGB human-object interaction scenes to guide humanoid loco-manipulation planning, extracting from the generated images both the contact locations and robot configurations that are then used inside a whole-body trajectory optimization formulation.

The search results contain many papers on humanoid loco-manipulation and locomotion, but I did not find a specific project or paper explicitly titled "DreamGen." If you're looking for a specific paper or project by that name, you may want to search more specifically or provide additional context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60f4b5ea-2a89-4874-a278-a83f0cff1ec2",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "0e4e45cf-e066-48f2-b02a-3d4dba2848da",
  "sourceToolAssistantUUID": "60f4b5ea-2a89-4874-a278-a83f0cff1ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-10T13:04:12.316Z_

Let me search more specifically for DreamGen's full scope and verify if it truly only addresses stationary manipulation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e4e45cf-e066-48f2-b02a-3d4dba2848da",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwCbPX1TAuCeSCGTdCf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "582b5e7c-25f9-4301-8c2f-5b6ea8faf4df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T6NFZzaMTBowMGDEyAdbk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1575,
      "cache_read_input_tokens": 32083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1575,
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

_source line 42 · 2026-05-10T13:04:13.196Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HC2yzYVzYuxnJSfGyB6wiT`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.12705",
  "prompt": "What specific tasks and robot embodiments does DreamGen evaluate? Does it include any mobile manipulation, humanoid locomotion, or loco-manipulation tasks? List all tasks mentioned in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "582b5e7c-25f9-4301-8c2f-5b6ea8faf4df",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwCbPX1TAuCeSCGTdCf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b9a76822-c644-49f1-bbe4-16de9f5eec54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T6NFZzaMTBowMGDEyAdbk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1575,
      "cache_read_input_tokens": 32083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1575,
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

_source line 43 · 2026-05-10T13:04:13.513Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018iByifrfjv2zcZ6Qo3ciYN`</summary>

```json
{
  "query": "DreamGen \"GR1 humanoid\" OR \"Franka\" OR \"SO-100\" pick-and-place"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9a76822-c644-49f1-bbe4-16de9f5eec54",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwCbPX1TAuCeSCGTdCf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "361c7bb3-e0ab-490b-a5ef-cc9562ac2fb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T6NFZzaMTBowMGDEyAdbk7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1575,
      "cache_read_input_tokens": 32083,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1575
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 207,
          "cache_read_input_tokens": 32083,
          "cache_creation_input_tokens": 1575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1575,
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

_source line 44 · 2026-05-10T13:04:18.669Z_

<details><summary>↩ Tool result · `toolu_01HC2yzYVzYuxnJSfGyB6wiT`</summary>

```text
# DreamGen Task and Embodiment Evaluation

## Robot Embodiments

DreamGen evaluates three distinct robot platforms:

1. **Fourier GR1 Humanoid** - A humanoid robot used for dexterous manipulation
2. **Franka Emika Panda** - A collaborative robotic arm
3. **LeRobot SO-100** - A low-cost robot arm

## Task Categories

### Real-World GR1 Tasks (Data Augmentation)
- Hammering
- Wiping
- Folding towels
- Stacking bowls

### Real-World Franka Tasks
- Pick-and-place
- Cube stacking
- Tool usage (scooping M&Ms)

### Real-World SO-100 Tasks
- Picking strawberries
- Tic-tac-toe placement

### Simulation Tasks (RoboCasa)
The paper evaluates "24 tasks" spanning pick-and-place, door/drawer manipulation, knob turning, lever operation, and button pressing.

### Behavior Generalization Tasks (Novel Verbs)
"14 novel behavior tasks" including pouring water, opening appliances, using tools, and manipulating articulated objects.

## Scope Limitations

**DreamGen does not include mobile manipulation, humanoid locomotion, or loco-manipulation.** The research focuses exclusively on arm-based manipulation and stationary humanoid upper-body tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9a76822-c644-49f1-bbe4-16de9f5eec54",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "58df331c-c223-4625-9a07-cece288260d9",
  "sourceToolAssistantUUID": "b9a76822-c644-49f1-bbe4-16de9f5eec54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T13:04:21.169Z_

<details><summary>↩ Tool result · `toolu_018iByifrfjv2zcZ6Qo3ciYN`</summary>

```text
Web search results for query: "DreamGen "GR1 humanoid" OR "Franka" OR "SO-100" pick-and-place"

Links: [{"title":"DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories","url":"https://arxiv.org/html/2505.12705v1"},{"title":"GitHub - NVIDIA/GR00T-Dreams: DreamGen: Nvidia GEAR Lab's initiative to solve the robotics data problem using world models · GitHub","url":"https://github.com/NVIDIA/GR00T-Dreams"},{"title":"DreamGen","url":"https://research.nvidia.com/labs/gear/dreamgen/"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Video World Models","url":"https://arxiv.org/html/2505.12705"},{"title":"Jim Fan on X: \"What if robots could dream inside a video generative model? Introducing DreamGen, a new engine that scales up robot learning not with fleets of human operators, but with digital dreams in pixels. DreamGen produces massive volumes of neural trajectories - photorealistic robot https://t.co/EqAScBuh2N\" / X","url":"https://x.com/DrJimFan/status/1924819887139987855"},{"title":"Enhance Robot Learning with Synthetic Trajectory Data Generated by World Foundation Models | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/"},{"title":"[Literature Review] DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories","url":"https://www.themoonlight.io/en/review/dreamgen-unlocking-generalization-in-robot-learning-through-neural-trajectories"},{"title":"DreamGen Pipeline for Robot Learning","url":"https://www.emergentmind.com/topics/dreamgen-pipeline"},{"title":"Deep dive into GROOT N1.5: A Foundation Model for Generalist Humanoid Robots","url":"https://blog.phospho.ai/d-groot-n1-5-a-foundation-model-for-generalist-humanoid-robots/"},{"title":"Dissecting GROOT N1: A Foundation Model for Generalist Humanoid Robots","url":"https://blog.phospho.ai/dissecting-groot-n1-a-foundation-model-for-generalist-humanoid-robots/"}]

I found comprehensive information about DreamGen's work with these robot platforms. Here's what the search revealed:

## DreamGen with Multiple Robot Platforms

DreamGen evaluates on 9 real-world tasks across three embodiments: the GR1 humanoid robot, the Franka arm robot, and the low-cost SO-100 robot arm.

### Pick-and-Place Tasks

Notably, the video world model and the IDM model were trained only on pick-and-place teleoperation data in a single environment. Despite this limited initial training, starting with just a single-task dataset of pick-and-place, the humanoid robot learns 22 new behaviors, such as pouring, folding, scooping, ironing, and hammering, despite never seeing those verbs before.

### Task-Specific Results

For the two SO-100 tasks, 40 and 50 trajectories were collected for the strawberry pick-and-place and tic-tac-toe tasks, respectively. For Franka Emika Panda arm, 100 teleoperation data were collected for three manipulation tasks, pick-and-place, cube stacking, and tool use.

### Performance Improvements

DreamGen shows consistent gains on success rate across all robots: from 37% to 46.4% on average of 4 GR1 humanoid tasks, 23% to 37% on average of 3 Franka tasks, and from 21% to 45.5% on average of 2 SO-100 tasks, all using just 10 to 13 real-world trajectories per task.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "361c7bb3-e0ab-490b-a5ef-cc9562ac2fb0",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "90aa60d0-ad6d-4bf7-b410-7c59009fdfcb",
  "sourceToolAssistantUUID": "361c7bb3-e0ab-490b-a5ef-cc9562ac2fb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-10T13:04:22.559Z_

Perfect. Now let me search for any other emerging work that might involve coupled SE(3) or mobile manipulation for humanoids that hasn't been covered yet:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90aa60d0-ad6d-4bf7-b410-7c59009fdfcb",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwDMfYkH92JTvH5FM7w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "acf2b48f-1cff-4979-8e5c-7545d14e5067",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014GzpmmEPseEiT8ok1nZurv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 33658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1577,
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

_source line 47 · 2026-05-10T13:04:22.964Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013rM3S8miRr519WLsorGpMh`</summary>

```json
{
  "query": "\"EgoHumanoid\" loco-manipulation egocentric 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acf2b48f-1cff-4979-8e5c-7545d14e5067",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwDMfYkH92JTvH5FM7w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "64a70ef8-8b3f-4446-ac06-238bd52d9bd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014GzpmmEPseEiT8ok1nZurv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 33658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1577,
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

_source line 48 · 2026-05-10T13:04:23.387Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H3xutj2sibNJFT9VRwXohR`</summary>

```json
{
  "query": "SPOT \"SE(3) pose trajectory\" manipulation embodiment 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64a70ef8-8b3f-4446-ac06-238bd52d9bd9",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwDMfYkH92JTvH5FM7w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "acda7e12-00c8-4158-9c70-015336ee5e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014GzpmmEPseEiT8ok1nZurv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 33658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1577,
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

_source line 49 · 2026-05-10T13:04:23.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014SMJQ1FSzjeAYAUFxAdpyR`</summary>

```json
{
  "query": "GR00T foundation model humanoid loco-manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acda7e12-00c8-4158-9c70-015336ee5e2c",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwDMfYkH92JTvH5FM7w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7a0670d0-163d-4ab6-bcc3-a5f62cce1dc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014GzpmmEPseEiT8ok1nZurv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1577,
      "cache_read_input_tokens": 33658,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 201,
          "cache_read_input_tokens": 33658,
          "cache_creation_input_tokens": 1577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1577,
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

_source line 50 · 2026-05-10T13:04:30.371Z_

<details><summary>↩ Tool result · `toolu_01H3xutj2sibNJFT9VRwXohR`</summary>

```text
Web search results for query: "SPOT "SE(3) pose trajectory" manipulation embodiment 2025"

Links: [{"title":"[2411.00965] SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation","url":"https://arxiv.org/abs/2411.00965"},{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation","url":"https://nvlabs.github.io/object_centric_diffusion/"},{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation | Research","url":"https://research.nvidia.com/publication/2025-05_spot-se3-pose-trajectory-diffusion-object-centric-manipulation"},{"title":"GitHub - NVlabs/object_centric_diffusion: SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation · GitHub","url":"https://github.com/NVlabs/object_centric_diffusion"},{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation","url":"https://www.joydeepb.com/Publications/icra2025_spot.pdf"},{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation – UT Austin Robot Perception and Learning Lab","url":"https://rpl.cs.utexas.edu/publications/2025/05/19/hsu-icra25-spot/"},{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation | NVIDIA Seattle Robotics Lab","url":"https://research.nvidia.com/labs/srl/publication/hsu-2025-spot/"},{"title":"(PDF) SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation","url":"https://www.researchgate.net/publication/385528942_SPOT_SE3_Pose_Trajectory_Diffusion_for_Object-Centric_Manipulation"},{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation | NVIDIA Learning and Perception Research","url":"https://research.nvidia.com/labs/lpr/publication/hsu2025spot/"},{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation | Request PDF","url":"https://www.researchgate.net/publication/395221293_SPOT_SE3_Pose_Trajectory_Diffusion_for_Object-Centric_Manipulation"}]

I found relevant results for your search query on SPOT. Here's what the research shows:

## Overview

SPOT is an object-centric imitation learning framework that captures each task by an SE(3) object pose trajectory representation relative to the target.

## Key Features and Approach

This approach decouples embodiment actions from sensory inputs, facilitating learning from various demonstration types, including both action-based and action-less human hand demonstrations, as well as cross-embodiment generalization. Additionally, object pose trajectories inherently capture planning constraints from demonstrations without the need for manually crafted rules.

## Training and Execution

The diffusion model is trained on demonstration trajectories extracted from videos without needing action data from the same embodiment, with object pose trajectories extracted from demonstration RGBD videos (e.g., collected with an iPhone), which are independent of the embodiment. During task execution, the task-relevant object is constantly tracked, and its pose is forwarded to the trajectory diffusion model to predict the object's future trajectory in SE(3), which leads to task accomplishment, with the generated trajectories then converted into embodiment-agnostic action plans for closed-loop manipulation.

## Results

In real-world evaluation, using only eight demonstrations shot on an iPhone, the approach completed all tasks while fully complying with task constraints. The research was published at the IEEE International Conference on Robotics and Automation (ICRA) in May 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acda7e12-00c8-4158-9c70-015336ee5e2c",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "cf9aa810-5d32-444b-b112-b8d6b0209dd9",
  "sourceToolAssistantUUID": "acda7e12-00c8-4158-9c70-015336ee5e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-10T13:04:30.516Z_

<details><summary>↩ Tool result · `toolu_013rM3S8miRr519WLsorGpMh`</summary>

```text
Web search results for query: ""EgoHumanoid" loco-manipulation egocentric 2026"

Links: [{"title":"[2602.10106] EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration","url":"https://arxiv.org/abs/2602.10106"},{"title":"EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration","url":"https://arxiv.org/html/2602.10106v1"},{"title":"EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration | Request PDF","url":"https://www.researchgate.net/publication/400660604_EgoHumanoid_Unlocking_In-the-Wild_Loco-Manipulation_with_Robot-Free_Egocentric_Demonstration"},{"title":"GitHub - OpenDriveLab/EgoHumanoid: The first framework enabling humanoid robots to learn whole-body loco-manipulation from egocentric human demos · GitHub","url":"https://github.com/OpenDriveLab/EgoHumanoid"},{"title":"EGOHUMANOID | Human-to-Humanoid Transfer for Loco-Manipulation","url":"https://opendrivelab.com/EgoHumanoid/"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Robots Learn To Walk And Manipulate Objects By Watching Humans Perform Tasks","url":"https://quantumzeitgeist.com/robots-learn-walk-manipulate-objects/"},{"title":"EgoMimic: Scaling Imitation Learning via Egocentric Video","url":"https://www.researchgate.net/publication/395228678_EgoMimic_Scaling_Imitation_Learning_via_Egocentric_Video"},{"title":"human-motion-arxiv-daily/README.md at main · AndrewDing616/human-motion-arxiv-daily","url":"https://github.com/AndrewDing616/human-motion-arxiv-daily/blob/main/README.md"}]

Based on the search results, here's what I found about EgoHumanoid:

## Overview

EgoHumanoid is the first framework to co-train a vision-language-action policy using abundant egocentric human demonstrations together with a limited amount of robot data, enabling humanoids to perform loco-manipulation across diverse real-world environments.

## Key Innovation

To bridge the embodiment gap between humans and robots, including discrepancies in physical morphology and viewpoint, the framework introduces a systematic alignment pipeline spanning from hardware design to data processing. The pipeline has two core components:

1. View alignment reduces visual discrepancies by transforming human egocentric observations to approximate robot viewpoints using depth-based reprojection and inpainting.

2. Action alignment employs a unified action space shared by humans and robots, using delta end-effector poses for upper body control and discrete commands for locomotion.

## Performance Results

Extensive real-world experiments demonstrate that incorporating robot-free egocentric data significantly outperforms robot-only baselines by 51%, particularly in unseen environments.

## Data Collection

The portable human setup integrates a VR headset, body trackers for pose estimation, and an egocentric camera, enabling scalable collection in varied scenarios without robot hardware. Complementary robot data, collected via VR-based teleoperation, provides embodiment-accurate supervision for manipulation-intensive behaviors.

The paper was published on arXiv in February 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64a70ef8-8b3f-4446-ac06-238bd52d9bd9",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "c1e4811d-bf31-4494-bcb2-a3448bd1891b",
  "sourceToolAssistantUUID": "64a70ef8-8b3f-4446-ac06-238bd52d9bd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-10T13:04:30.976Z_

<details><summary>↩ Tool result · `toolu_014SMJQ1FSzjeAYAUFxAdpyR`</summary>

```text
Web search results for query: "GR00T foundation model humanoid loco-manipulation 2026"

Links: [{"title":"GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub","url":"https://github.com/NVIDIA/Isaac-GR00T"},{"title":"[2503.14734] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/abs/2503.14734"},{"title":"2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"},{"title":"Isaac GR00T - Generalist Robot 00 Technology | NVIDIA Developer","url":"https://developer.nvidia.com/isaac/gr00t"},{"title":"NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots","url":"https://huggingface.co/blog/nvidia/gr00t-n1-7"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734v1"},{"title":"Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"},{"title":"NVIDIA Announces Isaac GR00T N1 — the World’s First Open Humanoid Robot Foundation Model — and Simulation Frameworks to Speed Robot Development | NVIDIA Newsroom","url":"https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks"},{"title":"2025-3-18 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T_1_Whitepaper.pdf"},{"title":"(PDF) GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://www.researchgate.net/publication/390019361_GR00T_N1_An_Open_Foundation_Model_for_Generalist_Humanoid_Robots"}]

Based on the search results, here's what I found about GR00T and humanoid loco-manipulation:

## GR00T Foundation Model Overview

NVIDIA Isaac GR00T N1.7 is an open vision-language-action (VLA) model for generalized humanoid robot skills. It is an open, commercially licensed Vision-Language-Action model for humanoid robots, built on the premise that human data is the most scalable source of robot intelligence.

## Architecture

GR00T N1 is a Vision-Language-Action (VLA) model with a dual-system architecture. The vision-language module (System 2) interprets the environment through vision and language instructions. The subsequent diffusion transformer module (System 1) generates fluid motor actions in real time. Both modules are tightly coupled and jointly trained end-to-end.

## Humanoid Capabilities and Loco-Manipulation

GR00T N1.7 supports whole-body humanoid control and can predict compact latent action tokens that a learned whole-body controller decodes into full-body joint commands — including legs, arms, and hands. A single policy produces language-conditioned, coordinated manipulation and locomotion end-to-end.

However, regarding loco-manipulation specifically: Currently, GR00T N1 model focuses primarily on short-horizon tabletop manipulation tasks. In future work, they aim to extend its capabilities to tackle long-horizon loco-manipulation, which will require advancements in humanoid hardware, model architecture, and training corpora.

NVIDIA Isaac GR00T N1.6 integrates multimodal vision-language-action policies and world models such as NVIDIA Cosmos Reason to enable humanoid robots to perform end-to-end loco-manipulation and reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a0670d0-163d-4ab6-bcc3-a5f62cce1dc7",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "0ddbe8a2-2a66-4404-ba08-50ea84954209",
  "sourceToolAssistantUUID": "7a0670d0-163d-4ab6-bcc3-a5f62cce1dc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-10T13:04:32.137Z_

Let me search for a few more recent 2026 works to ensure comprehensive coverage:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ddbe8a2-2a66-4404-ba08-50ea84954209",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwE5bSBoDZU7QJ4RgPm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b760f81b-8193-4a3b-ad4f-6d72c0fbac6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012Nq8dj5eo46WVxomRX7rCF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 35235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3309,
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

_source line 54 · 2026-05-10T13:04:32.599Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016QpStSTrgcSD7CLqv82dBo`</summary>

```json
{
  "query": "\"ULTRA\" \"Unified Multimodal Control\" humanoid loco-manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b760f81b-8193-4a3b-ad4f-6d72c0fbac6c",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwE5bSBoDZU7QJ4RgPm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6e233666-e3ee-4009-95e6-1883d14cfe70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012Nq8dj5eo46WVxomRX7rCF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 35235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3309,
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

_source line 55 · 2026-05-10T13:04:33.011Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RvBkg4YfBWhoVkhyZnLNGC`</summary>

```json
{
  "query": "Ψ0 \"Psi-Zero\" humanoid foundation model loco-manipulation 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e233666-e3ee-4009-95e6-1883d14cfe70",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwE5bSBoDZU7QJ4RgPm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cac09634-e845-4d1f-8562-1a0bf2edf086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012Nq8dj5eo46WVxomRX7rCF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 35235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3309,
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

_source line 56 · 2026-05-10T13:04:33.250Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C5cAvbRQQGHkgNnDB1m81x`</summary>

```json
{
  "query": "WholeBodyVLA ICLR 2026 loco-manipulation latent action"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cac09634-e845-4d1f-8562-1a0bf2edf086",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwE5bSBoDZU7QJ4RgPm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df6cc6f6-7578-4db7-895b-58a67c41b49d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012Nq8dj5eo46WVxomRX7rCF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3309,
      "cache_read_input_tokens": 35235,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3309
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 204,
          "cache_read_input_tokens": 35235,
          "cache_creation_input_tokens": 3309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3309,
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

_source line 57 · 2026-05-10T13:04:40.434Z_

<details><summary>↩ Tool result · `toolu_016QpStSTrgcSD7CLqv82dBo`</summary>

```text
Web search results for query: ""ULTRA" "Unified Multimodal Control" humanoid loco-manipulation 2026"

Links: [{"title":"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://ultra-humanoid.github.io/"},{"title":"[2603.03279v1] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/abs/2603.03279v1"},{"title":"[2603.03279] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/abs/2603.03279"},{"title":"ULTRA: Autonomous Humanoid Control via Multimodal Learning | ThatNewAI","url":"https://thatnewai.com/news/ultra-autonomous-humanoid-control-via-multimodal-learning"},{"title":"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation | alphaXiv","url":"https://www.alphaxiv.org/abs/2603.03279"},{"title":"ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2507.06905"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Unified Humanoid Control: The Convergence of Locomotion and Manipulation - Alabia Insights - Robôs, IA e o Futuro","url":"https://alabia.com.br/insights/trabalho/futuro-do-trabalho/unified-humanoid-control-framework/"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"[2507.06905] ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2507.06905"}]

I found detailed information about ULTRA. Here's what the research reveals:

## ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation

ULTRA is a research paper authored by Xialin He, Sirui Xu, and colleagues, published on arXiv (2603.03279) in March 2026.

### Key Challenges Addressed

The research tackles the central barrier of achieving autonomous and versatile whole-body loco-manipulation in humanoids, addressing limitations where retargeted data are often scarce or low-quality, methods struggle to scale to large skill repertoires, and existing approaches rely on tracking predefined motion references rather than generating behavior from perception and high-level task specifications.

### Framework Components

ULTRA is a unified framework with two key components: first, a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions; second, a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs.

### Technical Approach

The framework distills a universal tracking policy into the controller, compresses motor skills into a compact latent space, and applies reinforcement learning finetuning to expand coverage and improve robustness under out-of-distribution scenarios, enabling coordinated whole-body behavior from sparse intent without test-time reference motions.

### Evaluation Results

ULTRA was evaluated in simulation and on a real Unitree G1 humanoid, with results showing that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines with limited skills.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e233666-e3ee-4009-95e6-1883d14cfe70",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "55ecc34f-8e5a-4783-a3df-6aad28e64071",
  "sourceToolAssistantUUID": "6e233666-e3ee-4009-95e6-1883d14cfe70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T13:04:40.833Z_

<details><summary>↩ Tool result · `toolu_01RvBkg4YfBWhoVkhyZnLNGC`</summary>

```text
Web search results for query: "Ψ0 "Psi-Zero" humanoid foundation model loco-manipulation 2603"

Links: [{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2603.12263v1"},{"title":"[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2603.12263"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://psi-lab.ai/Psi0/"},{"title":"GitHub - physical-superintelligence-lab/Psi0: [RSS26'] Welcome to Psi-Zero, a Humanoid VLA towards Universal Humanoid Intelligence. · GitHub","url":"https://github.com/physical-superintelligence-lab/Psi0"},{"title":"$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.12263"},{"title":"$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://www.wispaper.ai/en/blog/psi-zero-open-foundation-model-universal-humanoid-loco-manipulation-20260314/eng"},{"title":"Ψ0: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (Mar 2026) - YouTube","url":"https://www.youtube.com/watch?v=sf31pDnScf8"},{"title":"Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation","url":"https://arxiv.org/html/2504.09532"},{"title":"How MANUS Gloves Enable Dexterous Teleoperation for USC PSI Lab's Humanoid Foundation Model-MANUS Use Case","url":"https://www.manus-meta.com/use-cases/how-manus-gloves-enable-dexterous-teleoperation-for-usc-psi-labs-humanoid-foundation-model"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation - Hongyi Jing","url":"https://hongyijing.me/publications/psi-0/"}]

I found comprehensive information about Ψ₀ (Psi-Zero). Here are the key details:

## Overview
Ψ₀ (Psi-Zero) is an open foundation model to address challenging humanoid loco-manipulation tasks. It is an open vision-language-action (VLA) model for dexterous humanoid loco-manipulation.

## Architecture and Design
Ψ₀ employs a staged training paradigm that combines a 2.5B parameter Vision-Language Model (VLM) with a flow-based Multi-Modal Diffusion Transformer (MM-DiT). The backbone is based on Qwen's Qwen3-VL-2B-Instruct, which extracts vision–language features from observations and instructions, and these features condition a flow-based multimodal diffusion transformer inspired by Stable Diffusion 3.

## Training Approach
The model autoregressively pre-trains a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations, and then post-trains a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control.

## Performance
It achieves state-of-the-art performance on complex, long-horizon tasks, outperforming existing baselines by over 40% in success rate while using significantly less robot-specific data. The foundation model is capable of acquiring new long-horizontal dexterous loco-manipulation skill by fine-tuning using as few as 80 trajectories.

## Key Innovation
Ψ₀ solves the "stop-and-think" behavior problem with Training-time RTC by masking the first few steps of an action chunk during training, allowing the model to learn to "inpaint" future actions that are perfectly continuous with the actions currently being executed, resulting in smooth motion.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cac09634-e845-4d1f-8562-1a0bf2edf086",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "7c5b7f26-af4d-4810-969d-098b3e2dd50d",
  "sourceToolAssistantUUID": "cac09634-e845-4d1f-8562-1a0bf2edf086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-10T13:04:42.490Z_

<details><summary>↩ Tool result · `toolu_01C5cAvbRQQGHkgNnDB1m81x`</summary>

```text
Web search results for query: "WholeBodyVLA ICLR 2026 loco-manipulation latent action"

Links: [{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"WholebodyVLA/README.md at main · OpenDriveLab/WholebodyVLA","url":"https://github.com/OpenDriveLab/WholebodyVLA/blob/main/README.md"},{"title":"WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control | OpenReview","url":"https://openreview.net/forum?id=OCJmVjyzN7"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/3067651d96704608727027ec28fda2eb8c2a7c4a.pdf"},{"title":"[2512.11047] WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control","url":"https://arxiv.org/abs/2512.11047"},{"title":"WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA","url":"https://openreview.net/pdf/579ba365d7c59e61b47f4b8efa00c06c9b2e22ea.pdf"},{"title":"Pull requests · OpenDriveLab/WholebodyVLA","url":"https://github.com/OpenDriveLab/WholebodyVLA/pulls"},{"title":"WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control","url":"https://arxiv.org/html/2512.11047v1"},{"title":"WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control","url":"https://wholebodyvla.github.io/"},{"title":"WholeBodyVLA: Unified Loco-Manipulation Control","url":"https://www.emergentmind.com/papers/2512.11047"}]

Based on the search results, here's information about WholeBodyVLA:

## Overview

WholeBodyVLA is a unified Vision-Language-Action framework for large-space humanoid loco-manipulation. The research was published at ICLR 2026 and presents a unified VLA framework enabling large-space humanoid loco-manipulation via unified latent learning and loco–manipulation–oriented RL.

## Key Components

**Latent Action Learning:** It learns unified latent actions from action-free egocentric videos through a Latent Action Model (LAM), and employs a loco-manipulation-oriented (LMO) RL policy for precise and stable whole-body coordination.

**System Architecture:** The system encodes egocentric images and language instructions into latent action tokens, which are decoded into dual-arm joint actions and locomotion commands, enabling end-to-end control for complex loco-manipulation tasks.

## Technical Contributions

To acquire richer loco-manipulation knowledge, the approach proposes a unified latent learning framework that enables Vision-Language-Action (VLA) system to learn from low-cost action-free egocentric videos. Additionally, a loco–manipulation–oriented (LMO) RL policy is presented specifically tailored for accurate and stable core loco-manipulation movements, such as advancing, turning, and squatting.

## Performance

The work was verified via comprehensive experiments on the AgiBot X2 humanoid, outperforming prior baselines by 21.3% and demonstrates strong generalization and high extensibility across a broad range of tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df6cc6f6-7578-4db7-895b-58a67c41b49d",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "ae1ebe7f07cf40db0",
  "type": "user",
  "uuid": "b73ead99-badf-4d46-92d2-30d76eb574f1",
  "sourceToolAssistantUUID": "df6cc6f6-7578-4db7-895b-58a67c41b49d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-10T13:05:08.623Z_

Excellent. Now I have comprehensive information. Let me compile my findings into a detailed report.

## COMPREHENSIVE SEARCH REPORT: Humanoid Loco-Manipulation Data Generation (2025-2026)

Based on an extensive search of recent literature (2025-2026), here are my findings addressing your specific questions:

---

### **(A) COUPLED SE(3) STANCE+ARM ENCODING FOR HUMANOID DEMO MULTIPLICATION**

**Finding: SPOT (arXiv:2411.00965 / ICRA 2025) is the primary work using SE(3) object-centric representations.**

SPOT uses SE(3) pose trajectory diffusion for object-centric manipulation, enabling cross-embodiment generalization. However, **SPOT focuses exclusively on stationary object manipulation tasks** (pick-and-place, object pushing, etc.). It does not encode coupled stance+manipulation or address locomotion at all.

**Other works checked for coupled SE(3) stance encoding:**
- **ResMimic (arXiv:2510.05070)**: Uses point-cloud-based object tracking rewards and contact rewards, but does NOT use SE(3) representations. Instead uses residual learning on top of human motion tracking.
- **OmniRetarget (arXiv:2509.26633)**: Uses an "interaction mesh" with Laplacian deformation to preserve spatial and contact relationships between agent-terrain-objects, but this is **not an SE(3) object-centric representation**. It's a mesh-based retargeting approach that preserves task-relevant interactions across embodiments.
- **DexMimicGen (arXiv:2410.24185)**: Focuses on bimanual dexterous manipulation synthesis from demonstrations, but does not address locomotion.

**Conclusion**: No existing work discovered that implements **coupled SE(3) stance+arm encoding** for humanoid loco-manipulation demonstration multiplication. This appears to be genuinely novel territory.

---

### **(B) DREAMGEN SCOPE VERIFICATION**

**Finding: DreamGen (arXiv:2505.12705) is EXCLUSIVELY stationary manipulation.**

Based on the full paper HTML, DreamGen evaluates on:
- **Humanoid tasks** (GR1): hammering, wiping, folding towels, stacking bowls
- **Robotic arm tasks** (Franka): pick-and-place, cube stacking, tool use
- **Low-cost arm tasks** (SO-100): strawberry picking, tic-tac-toe
- **Simulation tasks** (RoboCasa): 24 tasks including doors, drawers, knobs
- **Novel behaviors** (14 tasks): pouring, opening appliances, tool use

**Confirmed**: DreamGen does **NOT** address mobile manipulation, humanoid locomotion, or loco-manipulation. The humanoid (GR1) is used only for upper-body manipulation from fixed positions. The work explicitly uses teleoperation data from "a single pick-and-place task in one environment" to generalize to behaviors like pouring and hammering.

---

### **(C) CONCURRENT 2026 HUMANOID LOCO-MANIPULATION DATA GENERATION WORK**

Several projects are addressing procedural/synthetic data generation for humanoid loco-manipulation that may not have been in your paper's landscape:

**1. EgoHumanoid (arXiv:2602.10106, Feb 2026)**
- First framework for loco-manipulation using robot-free egocentric human demonstrations
- Uses view alignment (depth-based reprojection) and action alignment (unified action space)
- 51% improvement over robot-only baselines
- **Approach**: Not procedural generation, but human demonstration bridging via embodiment alignment

**2. WholeBodyVLA (ICLR 2026, arXiv:2512.11047)**
- Unified latent VLA for whole-body loco-manipulation via action-free egocentric videos
- **Novel aspect**: Learns latent actions from **action-free video** (no action labels needed)
- Proposes loco-manipulation-oriented (LMO) RL for stable whole-body coordination
- Verified on AgiBot X2 humanoid
- **Approach**: Vision-language conditioning + latent action learning (not procedural generation, but data-efficient learning)

**3. Ψ₀ / Psi-Zero (arXiv:2603.12263, Mar 2026, RSS 2026)**
- Open foundation model for universal humanoid loco-manipulation
- Training approach: Pre-trains VLM on large-scale egocentric human videos, then post-trains on humanoid-specific data
- Achieves 40% improvement over baselines with minimal robot data (80 trajectories to fine-tune)
- **Not procedural generation but efficient pre-training + fine-tuning**

**4. ULTRA (arXiv:2603.03279, Mar 2026)**
- Unified multimodal control for autonomous whole-body loco-manipulation
- **Physics-driven neural retargeting algorithm** that translates motion capture to humanoid embodiments while preserving physical plausibility
- Distills universal tracking policy + applies RL fine-tuning
- Verified on Unitree G1 in real world
- **Approach**: Retargeting + distillation + sparse task specs (not SE(3) demo multiplication)

**5. VisualMimic (arXiv:2509.20322, Sep 2025)**
- Visual sim-to-real for humanoid loco-manipulation
- Unifies egocentric vision with hierarchical whole-body control
- Uses task-agnostic keypoint tracker trained from human motion data
- **Approach**: Keypoint tracking + hierarchical control (not procedural data generation)

**6. ResMimic (arXiv:2510.05070, Oct 2025)**
- Two-stage residual learning: general motion tracking + residual refinement
- Trained on large-scale human-only motion, refined for object interaction
- Verified on Unitree G1
- **Approach**: Human motion transfer + residual RL (not demonstration multiplication)

**7. OmniRetarget (arXiv:2509.26633, Sep 2025)**
- Interaction-preserving data generation via interaction mesh
- Generates 8+ hours of trajectories from source datasets
- Interaction mesh explicitly preserves agent-terrain-object spatial relationships
- Verified on Unitree G1 for parkour + loco-manipulation
- **Approach**: Mesh-based retargeting that preserves contact, not SE(3)-based multiplication

**8. GR00T N1.x (Foundation Model)**
- Vision-language-action model for humanoid whole-body control
- **Current state**: "Focuses primarily on short-horizon tabletop manipulation tasks"
- **Explicitly stated limitation**: "In future work, they aim to extend to long-horizon loco-manipulation"
- Uses NVIDIA Cosmos world models for synthetic data generation (DreamGen-style video generation)

---

### **SUMMARY OF KEY FINDINGS**

| Finding | Status |
|---------|--------|
| **Coupled SE(3) stance+arm encoding for demo multiplication** | NOT FOUND - appears novel |
| **DreamGen scope (stationary vs mobile)** | CONFIRMED: Stationary manipulation only |
| **SE(3) object-centric methods in humanoid loco-manipulation** | Only SPOT (2025), but stationary manipulation only |
| **Concurrent procedural data generation for humanoid loco-manipulation (2026)** | Multiple approaches found, but none use SE(3) demo multiplication |

---

### **MOST RELEVANT CONCURRENT WORK**

The closest competing approaches in your space are:

1. **OmniRetarget** - Interaction mesh approach to preserve contact relationships during retargeting (but no SE(3) encoding)
2. **ULTRA** - Physics-driven retargeting for loco-manipulation, but uses sparse task specs not SE(3) trajectories
3. **ResMimic** - Human motion transfer with contact rewards, but residual-learning approach not demonstration multiplication
4. **Ψ₀ (Psi-Zero)** - Large-scale pre-training on human egocentric video + humanoid post-training (data-efficient but not procedural generation)

None of these use **coupled SE(3) stance+manipulation encodings for demonstration multiplication**, which appears to be your novel contribution.

---

## Sources

- [OmniRetarget: Interaction-Preserving Data Generation](https://arxiv.org/abs/2509.26633)
- [ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning](https://arxiv.org/abs/2510.05070)
- [VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation](https://arxiv.org/abs/2509.20322)
- [DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories](https://arxiv.org/abs/2505.12705)
- [EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106)
- [SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation](https://arxiv.org/abs/2411.00965)
- [ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2603.03279)
- [Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)
- [WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control](https://arxiv.org/abs/2512.11047)
- [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](https://arxiv.org/abs/2410.24185)
- [MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation](https://arxiv.org/abs/2510.18316)
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)
- [awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b73ead99-badf-4d46-92d2-30d76eb574f1",
  "isSidechain": true,
  "agentId": "ae1ebe7f07cf40db0",
  "requestId": "req_011CatwEvpcrVfcb3tJbCB3B",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1f113078-c28c-4637-971d-e8b74d58d348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SEnbGq6KULqKmNHkVuhH4i",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3415,
      "cache_read_input_tokens": 38544,
      "output_tokens": 2534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2534,
          "cache_read_input_tokens": 38544,
          "cache_creation_input_tokens": 3415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3415,
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
