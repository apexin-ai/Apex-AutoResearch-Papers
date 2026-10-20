# Research conversation: Search for these specific March 2026 papers on humanoid loco-manipulation to get their details and determine if they're 

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a83e64755b4ce8ece.jsonl`
- **Structured JSON:** [`6849a2067b21c58b85f2.json`](../../sessions/68/6849a2067b21c58b85f2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-10T13:06:08.933Z_

Search for these specific March 2026 papers on humanoid loco-manipulation to get their details and determine if they're relevant to a paper called "LocoMimicGen" about procedural demonstration multiplication for humanoid robots:

1. ULTRA (arXiv:2603.03279, March 2026): "Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation" - Search arxiv for this paper to understand what it does. Is it retargeting-based or procedural generation?

2. Psi-Zero / Ψ₀ (arXiv:2603.12263, March 2026): "Open Foundation Model Towards Universal Humanoid Loco-Manipulation" - What approach does it use? Foundation model pre-training vs. procedural generation?

3. Also search for any other 2026 papers that might be doing MimicGen-style data generation for mobile humanoids, or any work on "inverse reachability map for humanoid" or "bipedal arm reachability data generation" that isn't already in this list: [DemoHLM, OmniRetarget, MoMaGen, DreamGen, EgoHumanoid, HoMMI, HuMI, HumanX]

4. Search for "Unitree G1 loco-manipulation 2026" and "bipedal humanoid manipulation data 2026" to catch anything missed.

Report: the core approach of ULTRA and Psi-Zero (are they retargeting? generative? procedural?), whether they could be considered direct competitors to SE(3)-based demo multiplication, and any other papers found that the landscape might be missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "caac7ed0-b365-43b8-9efd-29e2c1ad00f0",
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

_source line 2 · 2026-05-10T13:06:10.914Z_

I'll search for these papers to help you understand the landscape of humanoid loco-manipulation work. Let me start by searching for these specific papers and related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caac7ed0-b365-43b8-9efd-29e2c1ad00f0",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwMJuaRTxN53BkXWpN3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23aaaaca-12cc-4259-95a9-b35c4c961701",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BhJBegNq1X25qkns6vpqNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 818,
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

_source line 3 · 2026-05-10T13:06:11.246Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012qdcXxUg8Em5h7kDtQPJUt`</summary>

```json
{
  "query": "ULTRA arXiv:2603.03279 March 2026 humanoid loco-manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23aaaaca-12cc-4259-95a9-b35c4c961701",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwMJuaRTxN53BkXWpN3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4659097b-2649-481b-9a16-550c2b8c3f5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BhJBegNq1X25qkns6vpqNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 818,
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

_source line 4 · 2026-05-10T13:06:11.272Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013xtdWnLFdjP42RdMj7p5Mm`</summary>

```json
{
  "query": "Psi-Zero Ψ₀ arXiv:2603.12263 March 2026 humanoid"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4659097b-2649-481b-9a16-550c2b8c3f5e",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwMJuaRTxN53BkXWpN3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2237334-e204-4579-9370-5c73c37fabd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BhJBegNq1X25qkns6vpqNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 818,
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

_source line 5 · 2026-05-10T13:06:11.476Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qt18j7xtou4uitNcKjaKF6`</summary>

```json
{
  "query": "MimicGen style data generation mobile humanoids 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2237334-e204-4579-9370-5c73c37fabd0",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwMJuaRTxN53BkXWpN3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2ff14df7-ce13-4c1a-964b-9974fc557616",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BhJBegNq1X25qkns6vpqNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 818,
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

_source line 6 · 2026-05-10T13:06:11.582Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016WwUBCCAwg7vcTt21GC9YM`</summary>

```json
{
  "query": "inverse reachability map humanoid bipedal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ff14df7-ce13-4c1a-964b-9974fc557616",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwMJuaRTxN53BkXWpN3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5fa63df0-47cf-4953-b7de-3be3158e9dde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BhJBegNq1X25qkns6vpqNe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 16155,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 818
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 818,
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

_source line 7 · 2026-05-10T13:06:17.222Z_

<details><summary>↩ Tool result · `toolu_013xtdWnLFdjP42RdMj7p5Mm`</summary>

```text
Web search results for query: "Psi-Zero Ψ₀ arXiv:2603.12263 March 2026 humanoid"

Links: [{"title":"[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2603.12263"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2603.12263v1"},{"title":"GitHub - physical-superintelligence-lab/Psi0: [RSS26'] Welcome to Psi-Zero, a Humanoid VLA towards Universal Humanoid Intelligence. · GitHub","url":"https://github.com/physical-superintelligence-lab/Psi0"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation - Hongyi Jing","url":"https://hongyijing.me/publications/psi-0/"},{"title":"最新开源！全身运动操作的VLA基础模型，wholebody任务今年的风向标～_机器人_数据_动作","url":"https://www.sohu.com/a/997275103_115479"},{"title":"Ψ0: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (Mar 2026) - YouTube","url":"https://www.youtube.com/watch?v=sf31pDnScf8"},{"title":"$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.12263"},{"title":"How MANUS Gloves Enable Dexterous Teleoperation for USC PSI Lab's Humanoid Foundation Model-MANUS Use Case","url":"https://www.manus-meta.com/use-cases/how-manus-gloves-enable-dexterous-teleoperation-for-usc-psi-labs-humanoid-foundation-model"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://psi-lab.ai/Psi0/"},{"title":"Introducing Ψ₀: An Open Foundation Model Towards ...","url":"https://www.linkedin.com/pulse/introducing-%CF%88-open-foundation-model-towards-universal-yue-wang-rvapc"}]

I found the research paper on Psi-Zero. Here are the key details:

## Psi-Zero (Ψ₀) Overview

Psi-Zero is an open foundation model to address challenging humanoid loco-manipulation tasks. The paper was published on March 12, 2026.

## Key Innovation

Existing approaches often attempt to address humanoid loco-manipulation by co-training on large and diverse human and humanoid data, but this strategy is suboptimal due to fundamental kinematic and motion disparities between humans and humanoid robots, resulting in unsatisfactory data efficiency and model performance despite considerable data volume.

To address this challenge, Psi-Zero decouples the learning process to maximize the utility of heterogeneous data sources by proposing a staged training paradigm: first, it autoregressively pre-trains a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations, then it post-trains a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control.

## Performance Results

Psi-Zero achieves the best performance using only about 800 hours of human video data and 30 hours of real-world robot data, outperforming baselines pre-trained on more than 10x as much data by over 40% in overall success rate across multiple tasks.

The entire ecosystem will be open-sourced to the community, including a data processing and training pipeline, a humanoid foundation model, and a real-time action inference engine.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2237334-e204-4579-9370-5c73c37fabd0",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "4d7f7da3-4154-443a-95b8-6c7af1c2e291",
  "sourceToolAssistantUUID": "f2237334-e204-4579-9370-5c73c37fabd0",
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

_source line 8 · 2026-05-10T13:06:17.859Z_

<details><summary>↩ Tool result · `toolu_012qdcXxUg8Em5h7kDtQPJUt`</summary>

```text
Web search results for query: "ULTRA arXiv:2603.03279 March 2026 humanoid loco-manipulation"

Links: [{"title":"[2603.03279] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/abs/2603.03279"},{"title":"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/html/2603.03279"},{"title":"[2603.03279v1] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/abs/2603.03279v1"},{"title":"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://ultra-humanoid.github.io/"},{"title":"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation | alphaXiv","url":"https://www.alphaxiv.org/abs/2603.03279"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning | OpenReview","url":"https://openreview.net/forum?id=hVoIz6xD9Q"},{"title":"X-Loco: Towards Generalist Humanoid Locomotion Control via Synergetic Policy Distillation","url":"https://arxiv.org/html/2603.03733"},{"title":"HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit","url":"https://arxiv.org/html/2502.13013v1"},{"title":"Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models","url":"https://arxiv.org/html/2504.16843v1"}]

I found the research paper you were searching for. Here's what the paper is about:

ULTRA (arXiv:2603.03279) is a paper submitted on March 3, 2026 by Xialin He, Sirui Xu, Xinyao Li, Runpei Dong, Liuyu Bian, Yu-Xiong Wang, and Liang-Yan Gui from the University of Illinois Urbana-Champaign.

The paper addresses the challenge that achieving autonomous and versatile whole-body loco-manipulation remains a central barrier to making humanoids practically useful, with existing approaches being fundamentally constrained by scarce or low-quality retargeted data, difficulty scaling to large skill repertoires, and reliance on tracking predefined motion references rather than generating behavior from perception and high-level task specifications.

To address these limitations, ULTRA proposes a unified framework with two key components: first, a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions, and second, a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs.

You can find the full paper and project details at the official project website: https://ultra-humanoid.github.io/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4659097b-2649-481b-9a16-550c2b8c3f5e",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "39007048-866b-426f-8ea3-de676780716e",
  "sourceToolAssistantUUID": "4659097b-2649-481b-9a16-550c2b8c3f5e",
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

_source line 9 · 2026-05-10T13:06:18.144Z_

<details><summary>↩ Tool result · `toolu_01Qt18j7xtou4uitNcKjaKF6`</summary>

```text
Web search results for query: "MimicGen style data generation mobile humanoids 2026"

Links: [{"title":"MimicGen","url":"https://mimicgen.github.io/"},{"title":"MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | OpenReview","url":"https://openreview.net/forum?id=dk-2R1f_LR"},{"title":"[2310.17596] MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations","url":"https://arxiv.org/abs/2310.17596"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://arxiv.org/html/2410.24185v1"},{"title":"MimicGen: Scalable Robot Data Generation","url":"https://www.emergentmind.com/topics/mimicgen-environment"},{"title":"GitHub - NVlabs/mimicgen: This code corresponds to simulation environments used as part of the MimicGen project. · GitHub","url":"https://github.com/NVlabs/mimicgen"},{"title":"DexMimicGen: Automated Data Generation for Bimanual ...","url":"https://openreview.net/pdf/4189a2bc6c20d5c52d0e6542702e1be54de0fe82.pdf"},{"title":"MimicGen: Scalable Data Generation for Robotics","url":"https://www.emergentmind.com/topics/mimicgen"},{"title":"MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | NVIDIA Learning and Perception Research","url":"https://research.nvidia.com/labs/lpr/publication/mandlekar2023mimicgen/"},{"title":"MimicGen: A Data Generation System for S...","url":"https://axi.lims.ac.uk/paper/2310.17596"}]

Based on the search results, here's what I found about MimicGen-style data generation for mobile humanoids in 2026:

## MimicGen Overview

MimicGen is a system for automatically synthesizing large-scale datasets from a small number of human demonstrations by adapting them to new scene configurations, object instances, and robot arms. The system was used to autonomously generate over 50,000 demonstrations from less than 200 human demonstrations across 18 tasks, multiple simulators, and the real-world.

## Extension to Mobile Humanoids

The latest development is **DexMimicGen**, which extends MimicGen to humanoid robots. DexMimicGen (DexMG) is a large-scale automated data generation system for bimanual robots with dexterous hands, such as humanoids. DexMimicGen extends this approach to dual-arm and humanoid robots in MuJoCo, supporting both parallel-jaw grippers and 6-DoF dexterous hands as in the GR-1 humanoid.

DexMimicGen has been deployed on nine simulation tasks across three embodiments — two arms with parallel-jaw grippers (top), two arms with dexterous hands (middle), and a humanoid (bottom).

## Technical Advances

DexMimicGen incorporates a flexible per-arm subtask segmentation strategy, allowing each arm to execute its subtasks independently while still accommodating the necessary coordination phases. DexMG employs a synchronization strategy to ensure precise alignment of actions during coordination subtasks and an ordering constraint mechanism to enforce the correct order of actions during sequential subtasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ff14df7-ce13-4c1a-964b-9974fc557616",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "8cc1c372-13fe-4c03-81fc-d0197d724933",
  "sourceToolAssistantUUID": "2ff14df7-ce13-4c1a-964b-9974fc557616",
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

_source line 10 · 2026-05-10T13:06:18.266Z_

<details><summary>↩ Tool result · `toolu_016WwUBCCAwg7vcTt21GC9YM`</summary>

```text
Web search results for query: "inverse reachability map humanoid bipedal 2026"

Links: [{"title":"Orientation-based reachability map for robot base placement | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/7353564/"},{"title":"Humanoid Loco-manipulation Planning based on Graph Search and Reachability Maps","url":"https://arxiv.org/html/2505.23505"},{"title":"Oriented Surface Reachability Maps for Robot Placement","url":"https://h2t.iar.kit.edu/pdf/Birr2022.pdf"},{"title":"Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation","url":"https://arxiv.org/html/2508.11275v1"},{"title":"Stance Selection for Humanoid Grasping Tasks by Inverse Reachability Maps","url":"http://www2.informatik.uni-freiburg.de/~burgetf/pub/burgetf15icra_final_submission.pdf"},{"title":"iDRM: Humanoid motion planning with realtime end-pose selection in complex environments | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/7803288/"},{"title":"(PDF) Stance Selection for Humanoid Grasping Tasks by Inverse Reachability Maps","url":"https://www.researchgate.net/publication/273131725_Stance_Selection_for_Humanoid_Grasping_Tasks_by_Inverse_Reachability_Maps"},{"title":"RM4D: A Combined Reachability and Inverse Reachability Map for Common 6-/7-axis Robot Arms by Dimensionality Reduction to 4D","url":"https://arxiv.org/html/2410.06968v1"},{"title":"Optimization of Wheelchair-Mounted Robotic Arms’ Base Placement by Fusing Occupied Grid Map and Inverse Reachability Map","url":"https://www.mdpi.com/2076-3417/13/14/8510"},{"title":"Efficient SE(3) Reachability Map Generation via Interplanar Integration of Intra-planar Convolutions | Request PDF","url":"https://www.researchgate.net/publication/355429152_Efficient_SE3_Reachability_Map_Generation_via_Interplanar_Integration_of_Intra-planar_Convolutions"}]

Based on the search results, I found several relevant papers and research on inverse reachability maps for humanoid bipedal robots. Here's what the current research shows:

## Overview of Inverse Reachability Maps for Humanoids

An Inverse Reachability Map represents the reachability of a given TCP (tool center point) pose with respect to the pose of the mobile base given in the frame of reference of the TCP.

## Recent Research in 2025-2026

Two particularly relevant recent papers include:

1. **Humanoid Loco-manipulation Planning**: Research on humanoid and bipedal locomotion focuses on multi-contact whole-body motion planning that alternates or simultaneously performs bipedal locomotion and object manipulation, while considering obstacle avoidance, foot stepping while moving objects, and regrasping when necessary.

2. **Learning Differentiable Reachability Maps**: A data-driven method learns a continuous representation of kinematic reachability (differentiable reachability map) that is continuous and differentiable with respect to task-space coordinates, enabling its direct use as constraints in continuous optimization for humanoid motion planning.

## Applications for Humanoid Robots

The inverse reachability map concept has been extended to bipedal humanoid robots with the assumption that the environment is flat. Additionally, an inverse reachability map can contain a collection of potential stance poses for the robot and be used to select a statically stable, collision-free stance configuration to reach a given grasping target.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fa63df0-47cf-4953-b7de-3be3158e9dde",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "c60929c2-1f26-4ef8-9c3a-58853201c712",
  "sourceToolAssistantUUID": "5fa63df0-47cf-4953-b7de-3be3158e9dde",
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

_source line 11 · 2026-05-10T13:06:19.708Z_

Now let me search for more papers on bipedal humanoid manipulation and Unitree G1 work:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c60929c2-1f26-4ef8-9c3a-58853201c712",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwMzJR4PuNTFZhBgKZD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe0b29a2-27d9-47ea-8be6-c96f5409ce40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014U4eqPRuieHQahD26jRGhn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 16973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4835,
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

_source line 12 · 2026-05-10T13:06:20.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DBmcTH3NqQaztE91af9aXV`</summary>

```json
{
  "query": "Unitree G1 loco-manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe0b29a2-27d9-47ea-8be6-c96f5409ce40",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwMzJR4PuNTFZhBgKZD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f1fb5173-7d8c-4df3-bf6f-3fa921bacaf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014U4eqPRuieHQahD26jRGhn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 16973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4835,
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

_source line 13 · 2026-05-10T13:06:20.384Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RFeWMGzDd3nja7YHrshpfr`</summary>

```json
{
  "query": "bipedal humanoid manipulation data generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1fb5173-7d8c-4df3-bf6f-3fa921bacaf6",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwMzJR4PuNTFZhBgKZD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d73f4c0f-b93a-4c94-a986-e1735acdad38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014U4eqPRuieHQahD26jRGhn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 16973,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4835
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 178,
          "cache_read_input_tokens": 16973,
          "cache_creation_input_tokens": 4835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4835,
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

_source line 14 · 2026-05-10T13:06:20.408Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012p6CU47XUNCVNZrpLfEiUE`</summary>

```json
{
  "query": "\"procedural demonstration\" humanoid manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d73f4c0f-b93a-4c94-a986-e1735acdad38",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwMzJR4PuNTFZhBgKZD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "78ce15b1-8be8-4b78-8541-11bd9c2f9361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014U4eqPRuieHQahD26jRGhn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 16973,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4835
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 178,
          "cache_read_input_tokens": 16973,
          "cache_creation_input_tokens": 4835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4835,
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

_source line 15 · 2026-05-10T13:06:27.854Z_

<details><summary>↩ Tool result · `toolu_01DBmcTH3NqQaztE91af9aXV`</summary>

```text
Web search results for query: "Unitree G1 loco-manipulation 2026"

Links: [{"title":"Unitree G1 Price & Specs 2026 | $16,000–$73,900 | 16 Configs","url":"https://botinfo.ai/articles/unitree-g1"},{"title":"Unitree G1 Price & Review [2026]","url":"https://blog.robozaps.com/b/unitree-g1-review"},{"title":"[2507.06905] ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2507.06905"},{"title":"Sirui Xu | About","url":"https://sirui-xu.github.io/"},{"title":"ULTRA: Autonomous Humanoid Control via Multimodal Learning | ThatNewAI","url":"https://thatnewai.com/news/ultra-autonomous-humanoid-control-via-multimodal-learning"},{"title":"ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control","url":"https://arxiv.org/html/2602.11321v2"},{"title":"Unitree G1 · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/en/unitree_g1"},{"title":"Amazon's OmniRetarget Teaches Humanoids Complex Skills by Preserving Physical Interactions | Humanoids Daily","url":"https://www.humanoidsdaily.com/news/amazons-omniretarget-teaches-humanoids-complex-skills-by-preserving-physical-interactions"},{"title":"Unitree G1: Price, Details, Review 2026 | Full Humanoid Specs","url":"https://www.originofbots.com/robot/unitree-g1-by-unitree-robotics-details-specifications-rating"},{"title":"HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit","url":"https://arxiv.org/html/2502.13013v1"}]

Based on the search results, here's what I found about Unitree G1 loco-manipulation in 2026:

## Research and Development Breakthroughs

Recent research has demonstrated unified loco-manipulation controllers on the Unitree G1, with a single unified policy achieving tracking accuracy, large workspace, and robustness while simultaneously tracking root velocity, root height, torso rotation, and dual-arm joint positions.

ULTRA framework has been evaluated on the real Unitree G1 humanoid, showing that it generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines.

## Real-World Deployment and Control

The Unitree G1 has demonstrated diverse loco-manipulation tasks under teleoperation including returning ping-pong balls from varying positions, balancing ping-pong balls on a paddle, juggling, catching frisbees while moving, and cooperatively lifting boxes, with some tasks performed using optical motion capture systems.

Amazon's OmniRetarget system enabled zero-shot transfer of complex loco-manipulation skills from simulation to a real Unitree G1 robot, with the robot performing dynamic sequences including carrying boxes, climbing over obstacles, and executing 30-second parkour routines.

## Software Support

LeRobot now supports the Unitree G1, allowing users to teleoperate, train loco-manipulation policies, and test in simulation.

## Hardware Variants

The G1-D is a wheeled variant of the G1 announced in April 2026 that replaces the bipedal legs with a differential drive wheeled base while keeping the same upper body, arms, and manipulation capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1fb5173-7d8c-4df3-bf6f-3fa921bacaf6",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "3bfa23c5-3d20-4f40-8335-b2ab02ca09f3",
  "sourceToolAssistantUUID": "f1fb5173-7d8c-4df3-bf6f-3fa921bacaf6",
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

_source line 16 · 2026-05-10T13:06:28.108Z_

<details><summary>↩ Tool result · `toolu_012p6CU47XUNCVNZrpLfEiUE`</summary>

```text
Web search results for query: ""procedural demonstration" humanoid manipulation 2026"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"9 humanoid robots at CES 2026 that showed the future is already here","url":"https://interestingengineering.com/ai-robotics/9-humanoid-robots-at-ces-2026"},{"title":"Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology","url":"https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"},{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"Humanoids conquered CES 2026 - Humanoid.guide","url":"https://humanoid.guide/humanoids-ces-2026/"},{"title":"Humanoid Robots in 2026: The Complete Market Overview | SVRC","url":"https://www.roboticscenter.ai/blog/humanoid-robot-2026"},{"title":"Humanoid Robot Dexterous Manipulation 2026 — PatSnap Eureka | PatSnap","url":"https://www.patsnap.com/resources/blog/rd-blog/humanoid-robot-dexterous-manipulation-2026-patsnap-eureka/"},{"title":"From Task Execution to Value Creation: What the 2026 Humanoid Robot Half Marathon Reveals About Industry Progress","url":"https://www.idc.com/resource-center/blog/humanoid-robotics-commercialization-2026/"},{"title":"Humanoid robots in 2026: Types, prices, and what’s next - Standard Bots","url":"https://standardbots.com/blog/humanoid-robot"},{"title":"Top 10 Chinese Humanoid Robots of 2026","url":"https://humanoidroboticstechnology.com/articles/top-10-chinese-humanoid-robots-of-2026/"}]

Based on the search results, here's what I found about procedural demonstration in humanoid manipulation in 2026:

## Key Developments in Procedural Demonstration for Humanoid Manipulation

Recent research papers from 2025-2026 include "Lightning Grasp: High Performance Procedural Grasp Synthesis with Contact Fields", which represents advances in procedural approaches to robotic grasping.

## Learning from Demonstrations

Advances in imitation learning and large-scale robot pre-training have made it possible to teach manipulation behaviors through demonstration rather than hand-written controllers, dramatically reducing the task engineering burden that made earlier humanoids impractical.

With AI-first humanoid robots using foundation models, behavior comes from learned policies instead of hand-coded scripts. Vision-language-action models map natural language and demonstrations to sequences of actions, and teleoperation traces provide training data for autonomous policies.

## Extended Reality (XR) Teleoperation

A significant trend for procedural demonstration involves XR interfaces. Both Baker Hughes (2021) and Boston Dynamics (2023) frame XR teleoperation not merely as a control interface but as a structured data collection pipeline for training autonomous manipulation policies. Shenzhen Daxiang Robot Technology filed two CN patents (2025) on VR-based humanoid remote control integrating head-worn devices, hand tracking, and joint motor execution.

## Industry Applications

More than 85% of deployments were concentrated in performances, education, data collection and guided tour service scenarios—primarily focused on demonstration, interaction, and technology validation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78ce15b1-8be8-4b78-8541-11bd9c2f9361",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "e0bbec43-d0ad-4935-af80-9c0273837115",
  "sourceToolAssistantUUID": "78ce15b1-8be8-4b78-8541-11bd9c2f9361",
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

_source line 17 · 2026-05-10T13:06:28.327Z_

<details><summary>↩ Tool result · `toolu_01RFeWMGzDd3nja7YHrshpfr`</summary>

```text
Web search results for query: "bipedal humanoid manipulation data generation 2026"

Links: [{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"AI Humanoid Robots 2026: Technology, Builders & Future","url":"https://www.articsledge.com/post/ai-humanoid-robots"},{"title":"Humanoid robots in 2026: Types, prices, and what’s next - Standard Bots","url":"https://standardbots.com/blog/humanoid-robot"},{"title":"Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology","url":"https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"Opportunities challenges and roadmap for humanoid robots in construction | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-30252-6"},{"title":"Humanoid says its first bipedal robot can start walking just 48 hours after assembly - The Robot Report","url":"https://www.therobotreport.com/humanoid-sayss-first-bipedal-robot-can-start-walking-just-48-hours-after-assembly/"},{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"6 Most Human-Like Humanoid Robots in 2026","url":"https://www.originofbots.com/articles/most-human-like-humanoid-robots-in-2026"}]

Here are the search results for "bipedal humanoid manipulation data generation 2026":

## Key Findings

**Data Generation and Cost Trends:**
The average cost per hour of high-quality teleoperation data fell from $340/hour in early 2024 to $118/hour as of March 2026 — a 60% decrease. Chinese companies are producing commodity-grade leader-follower teleoperation systems for under $2,000 — hardware that enables the large-scale data collection campaigns that VLA models require.

**Recent Research Progress:**
Several recent papers from March 2026 address humanoid manipulation capabilities, including "EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration" and "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation", as well as other works focused on manipulation tasks like object balancing and force-adaptive manipulation.

**Vision-Language-Action Models:**
Vision-Language-Action (VLA) models integrate vision encoders, language models, and action decoders into a single trainable stack, allowing robots to follow natural-language instructions. VLA adoption tripled in 2025–2026 and is now present in 40% of all new robot deployments.

**Commercial Platforms:**
Twelve commercial humanoid platforms are now available for purchase or structured lease, up from just 3 in 2024. Four are bipedal full-humanoids, three are upper-body torsos, and five are humanoid-adjacent mobile bases with dexterous arms. Prices range from $28,000 for torso-only systems to $245,000 for full bipeds.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d73f4c0f-b93a-4c94-a986-e1735acdad38",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "d468ba20-5ea3-4810-9a7b-50dd7a8b10ff",
  "sourceToolAssistantUUID": "d73f4c0f-b93a-4c94-a986-e1735acdad38",
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

_source line 18 · 2026-05-10T13:06:29.534Z_

Let me search for more specific papers that might compete with SE(3)-based demo multiplication:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d468ba20-5ea3-4810-9a7b-50dd7a8b10ff",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwNjKHrJ5k2FVBQEqhP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "74645dd9-0e1d-4b08-9ef6-d319889cb548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RwqYUArt7mwneyX6wWB7M9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 2112,
      "cache_read_input_tokens": 21808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2112,
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

_source line 19 · 2026-05-10T13:06:29.970Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MsGuqfjmgYwvM6H5W6Uc5m`</summary>

```json
{
  "query": "LocoMimicGen procedural demonstration multiplication humanoid"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74645dd9-0e1d-4b08-9ef6-d319889cb548",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwNjKHrJ5k2FVBQEqhP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d345b99-89f8-4359-9d39-96c41c285080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RwqYUArt7mwneyX6wWB7M9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 2112,
      "cache_read_input_tokens": 21808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2112,
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

_source line 20 · 2026-05-10T13:06:30.197Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E8ac7z7XRNAAoUm6s9jnxV`</summary>

```json
{
  "query": "SE(3) transformation humanoid manipulation data 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d345b99-89f8-4359-9d39-96c41c285080",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwNjKHrJ5k2FVBQEqhP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98efccde-203d-496b-a306-168a607a02c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RwqYUArt7mwneyX6wWB7M9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 2112,
      "cache_read_input_tokens": 21808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2112,
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

_source line 21 · 2026-05-10T13:06:30.300Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SSggDeba63BzfNidyJS2N2`</summary>

```json
{
  "query": "\"foundation model\" humanoid loco-manipulation March 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98efccde-203d-496b-a306-168a607a02c0",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwNjKHrJ5k2FVBQEqhP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "436335af-5739-4ced-98f4-84690c4a4173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RwqYUArt7mwneyX6wWB7M9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 2112,
      "cache_read_input_tokens": 21808,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2112
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 946,
          "output_tokens": 178,
          "cache_read_input_tokens": 21808,
          "cache_creation_input_tokens": 2112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2112,
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

_source line 22 · 2026-05-10T13:06:35.885Z_

<details><summary>↩ Tool result · `toolu_01MsGuqfjmgYwvM6H5W6Uc5m`</summary>

```text
Web search results for query: "LocoMimicGen procedural demonstration multiplication humanoid"

Links: [{"title":"VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2511.15200v1"},{"title":"Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation","url":"https://viral-humanoid.github.io/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation Tairan He1,2*","url":"https://viral-humanoid.github.io/static/viral.pdf"},{"title":"GitHub - aCodeDog/awesome-loco-manipulation · GitHub","url":"https://github.com/aCodeDog/awesome-loco-manipulation"},{"title":"GitHub - visualmimic/VisualMimic: [arXiv 2025] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation · GitHub","url":"https://github.com/visualmimic/VisualMimic"},{"title":"GitHub - lchaumartin/HumanoidProceduralAnimation: A fully procedural approach to humanoïd animation · GitHub","url":"https://github.com/lchaumartin/HumanoidProceduralAnimation"},{"title":"[2509.20322] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/abs/2509.20322"},{"title":"VisualMimic Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/html/2509.20322v1"},{"title":"2025-3-18 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T%20N1%20Whitepaper.pdf"}]

Based on the search results, I found relevant information about your query. The search results don't contain a specific project called "LocoMimicGen," but they do reference related work. Here's what I found:

The most relevant match appears to be DexMimicGen, which synthesizes large-scale robot manipulation trajectories by starting with a small set of human demonstrations and applying demonstration transformation and replay in simulation to expand the dataset automatically. This tool is being used in recent humanoid robot research.

Additionally, the search results show several related frameworks for humanoid robot loco-manipulation:

1. **VIRAL**: A visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware.

2. **VisualMimic**: A visual sim-to-real framework that unifies egocentric vision with hierarchical whole-body control, combining a task-agnostic low-level keypoint tracker trained from human motion data via a teacher-student scheme with a task-specific high-level policy.

If you're looking for information about a specific "LocoMimicGen" project or tool, it may be a newer or more specialized technique not yet widely documented. Could you provide more context about where you encountered this term, or would you like me to search for more specific information?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d345b99-89f8-4359-9d39-96c41c285080",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "ed2d7048-f531-4f70-b498-2e7c1b65bb8b",
  "sourceToolAssistantUUID": "4d345b99-89f8-4359-9d39-96c41c285080",
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

_source line 23 · 2026-05-10T13:06:37.640Z_

<details><summary>↩ Tool result · `toolu_01SSggDeba63BzfNidyJS2N2`</summary>

```text
Web search results for query: ""foundation model" humanoid loco-manipulation March 2026"

Links: [{"title":"[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2603.12263"},{"title":"Ψ0: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (Mar 2026) - YouTube","url":"https://www.youtube.com/watch?v=sf31pDnScf8"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://psi-lab.ai/Psi0/"},{"title":"How MANUS Gloves Enable Dexterous Teleoperation for USC PSI Lab's Humanoid Foundation Model-MANUS Use Case","url":"https://www.manus-meta.com/use-cases/how-manus-gloves-enable-dexterous-teleoperation-for-usc-psi-labs-humanoid-foundation-model"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"[2503.14734] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/abs/2503.14734"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734v2"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2603.12263v1"},{"title":"2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"}]

Based on the search results, here are the key findings about foundation models for humanoid loco-manipulation from March 2026:

## Ψ₀ (Psi-Zero)

Ψ₀ (Psi-Zero) is an open foundation model to address challenging humanoid loco-manipulation tasks, submitted on March 12, 2026. Rather than co-training on large and diverse human and humanoid data, the model addresses fundamental kinematic and motion disparities between humans and humanoid robots.

**Training Approach:**
The model uses a staged training paradigm: first, it autoregressively pre-trains a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations, then post-trains a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control.

**Performance:**
Ψ₀ achieves the best performance using only about 800 hours of human video data and 30 hours of real-world robot data, outperforming baselines pre-trained on more than 10x as much data by over 40% in overall success rate across multiple tasks.

**Open-Source Commitment:**
The entire ecosystem will be open-sourced to the community, including a data processing and training pipeline, a humanoid foundation model, and a real-time action inference engine.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "436335af-5739-4ced-98f4-84690c4a4173",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "70eeff0d-5876-44eb-a408-54271979e07d",
  "sourceToolAssistantUUID": "436335af-5739-4ced-98f4-84690c4a4173",
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

_source line 24 · 2026-05-10T13:06:38.582Z_

<details><summary>↩ Tool result · `toolu_01E8ac7z7XRNAAoUm6s9jnxV`</summary>

```text
Web search results for query: "SE(3) transformation humanoid manipulation data 2026"

Links: [{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"Humanoid Robot Dexterous Manipulation 2026 — PatSnap Eureka | PatSnap","url":"https://www.patsnap.com/resources/blog/rd-blog/humanoid-robot-dexterous-manipulation-2026-patsnap-eureka/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"PHUMA: PHYSICALLY-GROUNDED HUMANOID ...","url":"https://openreview.net/pdf/a36747cac87a488230dfe8cb6d5c0aa5a6db82d7.pdf"},{"title":"Optimus 3 — Tesla’s Third‑Generation Industrial Humanoid Robot","url":"https://humanoid.press/database/humanoid-press-database-tesla-optimus-3/"},{"title":"EngineAI's CEO-kicking, combat-ready humanoid robots dazzle CES 2026","url":"https://interestingengineering.com/ces-2026/ceo-kicking-combat-ready-humanoid-robots"},{"title":"Agile Robots launches humanoid robot for industry: Agile ONE | Agile Robots SE","url":"https://www.agile-robots.com/en/news/detail/agile-robots-launches-humanoid-robot-for-industry-agile-one/"},{"title":"Humanoids conquered CES 2026 - Humanoid.guide","url":"https://humanoid.guide/humanoids-ces-2026/"},{"title":"Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology","url":"https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"},{"title":"MATRIX-3 | Third-generation flagship humanoid robot","url":"https://www.matrixrobotics.ai/matrix-3"}]

Based on the search results, here's what I found regarding SE(3) transformation, humanoid manipulation, and 2026 developments:

## Recent Trends in Humanoid Manipulation (2026)

The field has moved from model-based planning toward learning-driven policies augmented by extended reality (XR) teleoperation and simulation-to-real transfer.

### Key Data Collection and Learning Approaches

The most consequential convergence is that of XR teleoperation and imitation learning infrastructure: both Baker Hughes (2021) and Boston Dynamics (2023) frame XR teleoperation not merely as a control interface but as a structured data collection pipeline for training autonomous manipulation policies.

Shenzhen Daxiang Robot Technology's two CN patents (filed February and March 2025) describe complete VR-based systems integrating headsets, hand tracking, visual sensors, and joint motor execution for humanoid remote control.

### Dexterous Manipulation Advances

Humanoid robot dexterous manipulation — the ability to perform complex, multi-fingered grasping, in-hand object reorientation, and precise tool use — sits at the intersection of mechanical hand design, sensorimotor control, and human-robot interface engineering.

### Recent Research Publications

Multiple arXiv papers from February 2026 cover topics including "Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation" and "HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model."

The search results show substantial activity in humanoid manipulation research and development for 2026, with a focus on learning from human demonstrations and real-world data collection through teleoperation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98efccde-203d-496b-a306-168a607a02c0",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "4f0e9f1c-7ecd-4d5f-ba92-862171b8d13a",
  "sourceToolAssistantUUID": "98efccde-203d-496b-a306-168a607a02c0",
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

_source line 25 · 2026-05-10T13:06:39.780Z_

Let me do a couple more targeted searches to catch any papers I might have missed:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f0e9f1c-7ecd-4d5f-ba92-862171b8d13a",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwPVA2RuXnFjQNGAXkg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb8477fd-de6b-481e-bba2-66b700926435",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ACQhDfAMMq9xYC3ZHVjtt5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 940,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 23920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3121,
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

_source line 26 · 2026-05-10T13:06:40.001Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xun3DcC8SZfN73TNd97KUv`</summary>

```json
{
  "query": "GR00T N1 foundation model humanoid manipulation March 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb8477fd-de6b-481e-bba2-66b700926435",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwPVA2RuXnFjQNGAXkg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "219e8a5d-c55a-4080-8cc9-ba9af5698da5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ACQhDfAMMq9xYC3ZHVjtt5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 940,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 23920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3121,
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

_source line 27 · 2026-05-10T13:06:40.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H9JyayUhsbCJUzRhoNme86`</summary>

```json
{
  "query": "\"whole-body loco-manipulation\" data generation 2026 -retargeting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "219e8a5d-c55a-4080-8cc9-ba9af5698da5",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwPVA2RuXnFjQNGAXkg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "63fb1dc4-bbba-4904-9e83-4ee881f76b62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ACQhDfAMMq9xYC3ZHVjtt5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 940,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 23920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3121,
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

_source line 28 · 2026-05-10T13:06:40.450Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KMhyT6KraYoKdJQx4unaKJ`</summary>

```json
{
  "query": "humanoid motion primitive generation SE3 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63fb1dc4-bbba-4904-9e83-4ee881f76b62",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwPVA2RuXnFjQNGAXkg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a9551554-a926-45c0-a356-0e25ea7f4df4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ACQhDfAMMq9xYC3ZHVjtt5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 940,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 23920,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 940,
          "output_tokens": 182,
          "cache_read_input_tokens": 23920,
          "cache_creation_input_tokens": 3121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3121,
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

_source line 29 · 2026-05-10T13:06:47.110Z_

<details><summary>↩ Tool result · `toolu_01H9JyayUhsbCJUzRhoNme86`</summary>

```text
Web search results for query: ""whole-body loco-manipulation" data generation 2026 -retargeting"

Links: [{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control | OpenReview","url":"https://openreview.net/forum?id=OCJmVjyzN7"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"WholebodyVLA/README.md at main · OpenDriveLab/WholebodyVLA","url":"https://github.com/OpenDriveLab/WholebodyVLA/blob/main/README.md"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/html/2509.26633v2"},{"title":"[2512.11047] WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control","url":"https://arxiv.org/abs/2512.11047"},{"title":"[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633"},{"title":"Scalable and General Whole-Body Control for Cross-Humanoid Locomotion","url":"https://arxiv.org/html/2602.05791"},{"title":"(PDF) OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://www.researchgate.net/publication/396049126_OmniRetarget_Interaction-Preserving_Data_Generation_for_Humanoid_Whole-Body_Loco-Manipulation_and_Scene_Interaction"},{"title":"[ICRA 2026] Safe Whole-Body Loco-Manipulation via Combined Model and Learning-based Control - YouTube","url":"https://www.youtube.com/watch?v=3HwqI6DK-7k"}]

Based on the search results, here are key findings related to whole-body loco-manipulation data generation in 2026:

## Major 2026 Research Projects

A unified latent learning framework has been proposed that enables Vision-Language-Action (VLA) systems to learn from low-cost action-free egocentric videos, with an efficient data collection pipeline devised to augment the dataset and scale the benefits.

## Data Generation Approaches

One significant approach is OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. This method generates over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines.

## Key Technical Components

A novel approach learns unified latent actions from manipulation and manipulation-aware locomotion videos without action annotations. Additionally, a locomotion-oriented reinforcement learning policy enables precise and stable whole-body coordination under disturbances.

## Real-World Applications

High-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63fb1dc4-bbba-4904-9e83-4ee881f76b62",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "e18a72cf-1dec-4e9a-8846-ecd508f04905",
  "sourceToolAssistantUUID": "63fb1dc4-bbba-4904-9e83-4ee881f76b62",
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

_source line 30 · 2026-05-10T13:06:47.298Z_

<details><summary>↩ Tool result · `toolu_01Xun3DcC8SZfN73TNd97KUv`</summary>

```text
Web search results for query: "GR00T N1 foundation model humanoid manipulation March 2026"

Links: [{"title":"[2503.14734] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/abs/2503.14734"},{"title":"NVIDIA Announces Isaac GR00T N1 — the World’s First Open Humanoid Robot Foundation Model — and Simulation Frameworks to Speed Robot Development | NVIDIA Newsroom","url":"https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks"},{"title":"2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734v1"},{"title":"(PDF) GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://www.researchgate.net/publication/390019361_GR00T_N1_An_Open_Foundation_Model_for_Generalist_Humanoid_Robots"},{"title":"NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots | Research","url":"https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots"},{"title":"2025-3-18 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T_1_Whitepaper.pdf"},{"title":"Paper page - GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://huggingface.co/papers/2503.14734"},{"title":"Isaac GR00T - Generalist Robot 00 Technology | NVIDIA Developer","url":"https://developer.nvidia.com/isaac/gr00t"},{"title":"NVIDIA Isaac GR00T N1 Foundation Model For Humanoid Robots","url":"https://www.labellerr.com/blog/nvidia-groot-n1/"}]

Based on the search results, here's what I found about GR00T N1:

## Overview

GR00T N1 is an open foundation model for humanoid robots. It is described as the world's first open, fully customizable foundation model for generalized humanoid reasoning and skills.

## Architecture

GR00T N1 is a Vision-Language-Action (VLA) model with a dual-system architecture. The vision-language module (System 2) interprets the environment through vision and language instructions. The subsequent diffusion transformer module (System 1) generates fluid motor actions in real time.

## Training Data

GR00T N1 is trained with a heterogeneous mixture of real-robot trajectories, human videos, and synthetically generated datasets.

## Manipulation Capabilities

The model was deployed on the Fourier GR-1 humanoid robot for language-conditioned bimanual manipulation tasks, achieving strong performance with high data efficiency. GR00T N1 can easily generalize across common tasks — such as grasping, moving objects with one or both arms, and transferring items from one arm to another — or perform multistep tasks that require long context and combinations of general skills.

## Performance

GR00T N1 outperforms the state-of-the-art imitation learning baselines on standard simulation benchmarks across multiple robot embodiments.

## Availability

GR00T N1 is available now and is the first of a family of fully customizable models that NVIDIA will pretrain and release to worldwide robotics developers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "219e8a5d-c55a-4080-8cc9-ba9af5698da5",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "ba8b764c-401e-4d8c-b404-57fac189ac05",
  "sourceToolAssistantUUID": "219e8a5d-c55a-4080-8cc9-ba9af5698da5",
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

_source line 31 · 2026-05-10T13:06:48.966Z_

<details><summary>↩ Tool result · `toolu_01KMhyT6KraYoKdJQx4unaKJ`</summary>

```text
Web search results for query: "humanoid motion primitive generation SE3 2026"

Links: [{"title":"Humanoid robot learns impressive tennis skills from imperfect human motion","url":"https://techxplore.com/news/2026-03-humanoid-robot-tennis-skills-imperfect.html"},{"title":"Research on humanoid robot motion generation and real-time trajectory optimization based on sparse attention mechanism in deep reinforcement learning | Discover Artificial Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44163-025-00603-3"},{"title":"Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions","url":"https://arxiv.org/html/2410.12773v1"},{"title":"MATRIX-3 | Third-generation flagship humanoid robot","url":"https://www.matrixrobotics.ai/matrix-3"},{"title":"HUMANOID-LLA: OPEN-VOCABULARY ...","url":"https://openreview.net/pdf/830d6b6b95ad212ad757bba8ac1fac08c6273041.pdf"},{"title":"ALIGNING LARGE MOTION MODELS WITH HUMANOID ...","url":"https://openreview.net/pdf?id=KhNq7zm2UL"},{"title":"Humanoids conquered CES 2026 - Humanoid.guide","url":"https://humanoid.guide/humanoids-ces-2026/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"2026 humanoid robot launches - Electronics360 - GlobalSpec","url":"https://electronics360.globalspec.com/article/23332/2026-humanoid-robot-launches"},{"title":"AI Humanoid Robots 2026: Technology, Builders & Future","url":"https://www.articsledge.com/post/ai-humanoid-robots"}]

I've performed a web search for "humanoid motion primitive generation SE3 2026" and found several relevant research results. Here are the key findings:

## Recent Research on Humanoid Motion Primitives (2026)

A new system enables humanoid robots to learn tennis skills using imperfect, fragmentary human motion data, focusing on primitive actions like forehand and backhand strokes. This work, called LATENT, achieved a 96.5% success rate in returning balls within 2.5 meters of target locations, surpassing previous methods in accuracy and motion naturalness.

In the field of humanoid motion generation, the pose coordination embedding technology constructs a four-dimensional motion primitive space through a Gaussian mixture model, achieving a trajectory similarity of 89.3% in a structured environment.

## Motion Primitive Frameworks

Research on unified motion vocabularies has made progress in 2026. Through joint quantization of paired human motions and their retargeted humanoid counterparts, researchers ensure that the same discrete token corresponds to the same motion primitive across both embodiments, resulting in a compact and reusable motion language that benefits from the scalability of human motion datasets, remains compatible with humanoid actuation constraints, and provides a discrete interface suitable for large language model based reasoning and generation.

## General Advances in 2026

January 2026 marked a major milestone for the humanoid robotics sector, as several leading manufacturers unveiled production-ready platforms and next-generation models, with companies including Boston Dynamics, Unitree Robotics, AgiBot, LG Electronics and NEURA Robotics introducing humanoid systems designed for real-world deployment, representing a broader industry shift toward scalable, commercially viable humanoid platforms.

The research appears to focus on improving how humanoid robots learn and execute motion primitives from human demonstrations, with emphasis on composing these primitives for complex tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9551554-a926-45c0-a356-0e25ea7f4df4",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "c4dfcf7d-226f-4250-8a26-a0da38f68352",
  "sourceToolAssistantUUID": "a9551554-a926-45c0-a356-0e25ea7f4df4",
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

_source line 32 · 2026-05-10T13:06:50.802Z_

Excellent! Let me do one more search to check for WholeBodyVLA and any other procedural generation papers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4dfcf7d-226f-4250-8a26-a0da38f68352",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwQFbUpqe1JDeaPsTex",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fbfc22c7-4d95-407e-a475-28221a966b67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H97bbihT9KfhnyDWxn1Ayq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4044,
      "cache_read_input_tokens": 27041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4044,
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

_source line 33 · 2026-05-10T13:06:51.180Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M5N2AVtyqhGKgimsmbjhAF`</summary>

```json
{
  "query": "WholeBodyVLA ICLR 2026 humanoid loco-manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbfc22c7-4d95-407e-a475-28221a966b67",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwQFbUpqe1JDeaPsTex",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "52825a59-da67-45a2-917a-b3d7c93f8855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H97bbihT9KfhnyDWxn1Ayq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4044,
      "cache_read_input_tokens": 27041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4044,
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

_source line 34 · 2026-05-10T13:06:51.668Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FHuRZiyqjJESyLNjrFgvsd`</summary>

```json
{
  "query": "\"EgoHumanoid\" \"robot-free\" demonstration March 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52825a59-da67-45a2-917a-b3d7c93f8855",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwQFbUpqe1JDeaPsTex",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d6ecf46-26a3-4790-ba6f-a1c35e866287",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H97bbihT9KfhnyDWxn1Ayq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4044,
      "cache_read_input_tokens": 27041,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4044
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 148,
          "cache_read_input_tokens": 27041,
          "cache_creation_input_tokens": 4044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4044,
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

_source line 35 · 2026-05-10T13:06:57.791Z_

<details><summary>↩ Tool result · `toolu_01FHuRZiyqjJESyLNjrFgvsd`</summary>

```text
Web search results for query: ""EgoHumanoid" "robot-free" demonstration March 2026"

Links: [{"title":"EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration | Request PDF","url":"https://www.researchgate.net/publication/400660604_EgoHumanoid_Unlocking_In-the-Wild_Loco-Manipulation_with_Robot-Free_Egocentric_Demonstration"},{"title":"EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration","url":"https://arxiv.org/html/2602.10106v1"},{"title":"GitHub - OpenDriveLab/EgoHumanoid: The first framework enabling humanoid robots to learn whole-body loco-manipulation from egocentric human demos · GitHub","url":"https://github.com/OpenDriveLab/EgoHumanoid"},{"title":"EGOHUMANOID | Human-to-Humanoid Transfer for Loco-Manipulation","url":"https://opendrivelab.com/EgoHumanoid/"},{"title":"[2602.10106] EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration","url":"https://arxiv.org/abs/2602.10106"},{"title":"The Humanoid Robot Revolution: What's Coming in 2026 (And Why Silicon Valley Is Terrified) - YouTube","url":"https://www.youtube.com/watch?v=I3pupzwiGJQ"},{"title":"Top 5 Humanoid Robot Trade Shows 2026 - Qviro Blog","url":"https://qviro.com/blog/humanoid-robot-trade-shows-2026/"},{"title":"Humanoid Robots News | AI Breakthroughs, Robotics Trends & Synthetic Updates","url":"https://humanoid.press/"},{"title":"Top 10 robotics developments of March 2026 - The Robot Report","url":"https://www.therobotreport.com/top-10-robotics-developments-march-2026/"},{"title":"Humanoids Summit","url":"https://humanoidssummit.com/"}]

Based on the search results, here's what I found about EgoHumanoid and robot-free demonstration:

EgoHumanoid is the first framework to co-train a vision-language-action policy using abundant egocentric human demonstrations together with a limited amount of robot data, enabling humanoids to perform loco-manipulation across diverse real-world environments.

Extensive real-world experiments demonstrate that incorporating robot-free egocentric data significantly outperforms robot-only baselines by 51%, particularly in unseen environments.

The research introduces view alignment that reduces visual discrepancies by transforming human egocentric observations to approximate robot viewpoints, and action alignment that employs a unified action space shared by humans and robots, using delta end-effector poses for upper body control and discrete commands for locomotion.

EgoHumanoid is validated on a Unitree G1 humanoid robot across four indoor and outdoor loco-manipulation tasks.

The framework appears to have been published in February 2026 based on the research paper dates found in the results. While the search results mention various March 2026 robotics events, they don't specifically reference an EgoHumanoid demonstration scheduled for March 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d6ecf46-26a3-4790-ba6f-a1c35e866287",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "9eeafa95-fe9c-4664-833e-774b0d378b17",
  "sourceToolAssistantUUID": "4d6ecf46-26a3-4790-ba6f-a1c35e866287",
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

_source line 36 · 2026-05-10T13:06:58.315Z_

<details><summary>↩ Tool result · `toolu_01M5N2AVtyqhGKgimsmbjhAF`</summary>

```text
Web search results for query: "WholeBodyVLA ICLR 2026 humanoid loco-manipulation"

Links: [{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"WholebodyVLA/README.md at main · OpenDriveLab/WholebodyVLA","url":"https://github.com/OpenDriveLab/WholebodyVLA/blob/main/README.md"},{"title":"WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control | OpenReview","url":"https://openreview.net/forum?id=OCJmVjyzN7"},{"title":"[2512.11047] WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control","url":"https://arxiv.org/abs/2512.11047"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/3067651d96704608727027ec28fda2eb8c2a7c4a.pdf"},{"title":"WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA","url":"https://openreview.net/pdf/380d841ddb75fd0dbf1e943bfef2875ce0fe6303.pdf"},{"title":"Pull requests · OpenDriveLab/WholebodyVLA","url":"https://github.com/OpenDriveLab/WholebodyVLA/pulls"},{"title":"Publication | OpenDriveLab","url":"https://opendrivelab.com/publications"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Preprint WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA","url":"https://opendrivelab.com/WholeBodyVLA/static/pdf/WholeBodyVLA.pdf"}]

Based on the search results, here's what I found about WholeBodyVLA at ICLR 2026:

## Overview

WholeBodyVLA is a unified Vision-Language-Action framework for large-space humanoid loco-manipulation. The paper was published as a conference paper at ICLR 2026 by researchers from Fudan University, OpenDriveLab & MMLab at The University of Hong Kong, AGIBOT, and others.

## Key Contributions

The framework enables Vision-Language-Action (VLA) systems to learn from low-cost action-free egocentric videos through a unified latent learning framework. A loco-manipulation-oriented (LMO) RL policy is presented that is specifically tailored for accurate and stable core loco-manipulation movements, such as advancing, turning, and squatting.

## Performance and Significance

WholeBodyVLA is one of its kind enabling large-space humanoid loco-manipulation and was verified via comprehensive experiments on the AgiBot X2 humanoid, outperforming prior baselines by 21.3%. It also demonstrates strong generalization and high extensibility across a broad range of tasks.

## Availability

The framework includes a locomotion-oriented reinforcement learning policy that enables precise and stable whole-body coordination under disturbances. The code and checkpoints are available on GitHub at OpenDriveLab/WholebodyVLA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52825a59-da67-45a2-917a-b3d7c93f8855",
  "isSidechain": true,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "agentId": "a83e64755b4ce8ece",
  "type": "user",
  "uuid": "366657eb-d70e-4752-836a-e6cdebd46937",
  "sourceToolAssistantUUID": "52825a59-da67-45a2-917a-b3d7c93f8855",
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

_source line 37 · 2026-05-10T13:07:17.194Z_

Perfect! Now I have comprehensive information. Let me compile my findings into a clear report.

## Report: March 2026 Humanoid Loco-Manipulation Landscape Analysis

### Papers Found and Core Approaches

**1. ULTRA (arXiv:2603.03279, March 2026)**
- **Core Approach:** Physics-driven retargeting (NOT procedural generation)
- **Method:** Two-component framework: (1) physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions, (2) unified multimodal controller supporting both dense references and sparse task specifications
- **Key Innovation:** Addresses scarce/low-quality retargeted data through physics preservation
- **Relevance to SE(3) demo multiplication:** Direct competitor via retargeting, but different mechanism—uses physics constraints rather than procedural SE(3) transformation. Both aim to scale from limited demonstrations

**2. Ψ₀ (Psi-Zero) (arXiv:2603.12263, March 2026)**
- **Core Approach:** Foundation model pre-training (NOT procedural generation)
- **Method:** Staged training paradigm: (1) Autoregressive VLM pre-training on 800 hours of egocentric human videos, (2) Flow-based action expert post-training on 30 hours of high-quality robot data
- **Key Innovation:** Decoupled learning addressing kinematic/motion disparities between humans and humanoids; outperforms 10x larger datasets by 40% success rate improvement
- **Relevance to SE(3) demo multiplication:** Orthogonal approach—uses foundation model scaling rather than procedural transformation. Not a direct competitor to demo multiplication but complementary (large-scale pre-training vs. small-scale synthesis)

### Additional Papers Found (Not in Original List)

**3. WholeBodyVLA (ICLR 2026, December 2025 arXiv:2512.11047)**
- **Core Approach:** Unified latent VLA from action-free videos + RL
- **Method:** Learns from low-cost action-free egocentric videos via unified latent learning framework, with locomotion-oriented RL policy for stable whole-body coordination
- **Implementation:** Verified on AgiBot X2, outperforms baselines by 21.3%
- **Relevance:** Data generation adjacent—uses RL for augmentation but not procedural transformation

**4. EgoHumanoid (arXiv:2602.10106, February 2026)**
- **Core Approach:** Human-to-robot transfer with view/action alignment (NOT procedural generation)
- **Method:** Co-trains vision-language-action policy using egocentric human demonstrations + limited robot data; view alignment (transforms human egocentric to robot viewpoint) + action alignment (unified action space with delta end-effector poses)
- **Key Innovation:** 51% performance improvement over robot-only baselines using robot-free data
- **Relevance:** Alignment-based data synthesis rather than procedural multiplication

**5. DexMimicGen (2024, extended to humanoids 2025)**
- **Core Approach:** Procedural demo transformation (most similar to LocoMimicGen)
- **Method:** Extends MimicGen to humanoid robots; uses per-arm subtask segmentation, synchronization strategy for coordination, ordering constraints for sequential subtasks
- **Key Innovation:** Automated large-scale data generation for dexterous humanoids (e.g., GR-1)
- **Relevance:** **Highly relevant—this IS a MimicGen-style procedural demonstration multiplier for humanoids.** Uses scene/configuration adaptation rather than SE(3) but same philosophy of expanding limited demos

**6. GR00T N1 (arXiv:2503.14734, March 2026)**
- **Core Approach:** Foundation model VLA with dual-system architecture
- **Method:** Vision-language module (System 2) + diffusion transformer module (System 1); trained on heterogeneous mix of real robot trajectories, human videos, synthetically generated datasets
- **Key Innovation:** Deployed on Fourier GR-1 for bimanual manipulation
- **Relevance:** Foundation model approach—complementary to procedural generation, not a direct competitor

**7. OmniRetarget (arXiv:2509.26633, September 2025)**
- **Core Approach:** Interaction-preserving retargeting (mentioned in your original list)
- **Method:** Uses interaction mesh to explicitly model/preserve spatial and contact relationships between agent, terrain, manipulated objects
- **Key Innovation:** Generates 8+ hour trajectories with better kinematic constraint satisfaction and contact preservation than baselines
- **Relevance:** Retargeting-based (similar philosophy to ULTRA), not procedural generation

### Competitive Landscape Summary

**Direct Competitors to SE(3)-based Demo Multiplication:**
- **ULTRA** — retargeting-based, not procedural, but competing approach for scaling from limited demos
- **DexMimicGen** — procedural but uses scene/configuration adaptation rather than SE(3) transformation
- Neither ULTRA nor Psi-Zero are direct SE(3) competitors; both use different scaling mechanisms

**Orthogonal Approaches (Foundation Models):**
- Ψ₀, GR00T N1, EgoHumanoid, WholeBodyVLA all use foundation model pre-training or large-scale dataset approaches
- These complement rather than compete with procedural demo multiplication (can be used together)

**Key Gaps in Landscape:**
- Most 2026 papers focus on either (1) retargeting with better contact preservation (ULTRA, OmniRetarget), or (2) foundation model scaling (Psi-Zero, GR00T N1)
- **No papers found specifically on SE(3)-based procedural demo multiplication for whole-body loco-manipulation**
- DexMimicGen is the closest existing procedural approach but for dexterous arms, not mobile humanoids
- WholeBodyVLA uses RL-based augmentation but not explicit procedural transformation
- This suggests **LocoMimicGen would be filling a gap**: SE(3)-based procedural multiplication for mobile humanoid loco-manipulation

### Sources
- [ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2603.03279)
- [Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)
- [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation](https://arxiv.org/html/2410.24185v1)
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)
- [EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106)
- [WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control](https://arxiv.org/abs/2512.11047)
- [OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2509.26633)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "366657eb-d70e-4752-836a-e6cdebd46937",
  "isSidechain": true,
  "agentId": "a83e64755b4ce8ece",
  "requestId": "req_011CatwQwcmmXKP9uJ4vjaXk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9ad97160-1a50-41ee-a176-d27739d98a22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GDCcTB91P7JRmapCJdGFSV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 875,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 31085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1083,
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
