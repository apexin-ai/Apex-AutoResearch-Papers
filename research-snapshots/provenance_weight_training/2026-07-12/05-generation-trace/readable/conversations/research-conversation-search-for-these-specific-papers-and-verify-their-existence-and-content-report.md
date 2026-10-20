# Research conversation: Search for these specific papers and verify their existence and content. Report back the key details (title, authors, ve

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a38eeb6543c36a1cd.jsonl`
- **Structured JSON:** [`d3a54290ff76dbd9493e.json`](../../sessions/d3/d3a54290ff76dbd9493e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

57 recorded events

### User

_source line 1 · 2026-05-10T13:07:17.885Z_

Search for these specific papers and verify their existence and content. Report back the key details (title, authors, venue, abstract content) for each:

1. BridgeV2W (arXiv:2602.03793, February 2026) - search for "BridgeV2W" and "arXiv 2602.03793" to confirm whether this paper uses ControlNet + URDF embodiment masks injected into video diffusion models for robot manipulation video generation.

2. Dream2Act (arXiv:2603.19709) - search for "Dream2Act" humanoid robot video to confirm: does it use post-hoc URDF-constrained IK after video generation? What is described as its primary limitation?

3. EA-WM (arXiv:2605.06192) - search for "EA-WM" and "Event-Aware World Model" to confirm it uses kinematic heatmaps injected into Wan 2.2 cross-attention for arm manipulation on WorldArena benchmark.

4. VAG (arXiv:2604.09330) - search for "VAG dual-stream video action generation" to check whether the paper explicitly states "video branch not influenced by action branch" or whether this is an inference.

5. Search for any NEW papers from March-May 2026 on: humanoid robot video generation, URDF-conditioned video diffusion, kinematic conditioning for robot video synthesis, full-body humanoid training data generation.

Use searches on arxiv.org, Google Scholar, and semantic scholar. Report what you actually find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "153a71ce-cd03-4635-b7d1-64aa9663d55e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T13:07:19.167Z_

I'll systematically search for each of these papers and verify their details. Let me start with parallel searches for the specific papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "153a71ce-cd03-4635-b7d1-64aa9663d55e",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwSPKP6fCb9R8MeVMU2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0a0cbde3-fb11-444a-aacc-8c222e28915c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y78isgBWw2pPoFKCmU9p43",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 784,
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

_source line 3 · 2026-05-10T13:07:19.407Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LRg4esY3k1ZbsMCZBStW2J`</summary>

```json
{
  "query": "BridgeV2W arXiv 2602.03793"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a0cbde3-fb11-444a-aacc-8c222e28915c",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwSPKP6fCb9R8MeVMU2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "432a2b26-9d31-451b-a84c-a87f45d0c658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y78isgBWw2pPoFKCmU9p43",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 784,
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

_source line 4 · 2026-05-10T13:07:19.638Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FAXUDXVcGbtU4428zyF8eR`</summary>

```json
{
  "query": "BridgeV2W ControlNet URDF video diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "432a2b26-9d31-451b-a84c-a87f45d0c658",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwSPKP6fCb9R8MeVMU2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4bddbd70-2325-455d-8d53-cb9b71650f5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y78isgBWw2pPoFKCmU9p43",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 784,
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

_source line 5 · 2026-05-10T13:07:19.848Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JyFYAvdRuz2Vm3JPMZWwMX`</summary>

```json
{
  "query": "Dream2Act arXiv 2603.19709 humanoid robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bddbd70-2325-455d-8d53-cb9b71650f5f",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwSPKP6fCb9R8MeVMU2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "729bd4f7-6ce8-422b-97ec-3fa227813b18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y78isgBWw2pPoFKCmU9p43",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 16155,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 236,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 784,
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

_source line 6 · 2026-05-10T13:07:19.889Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V7MWRPvKvuULhrDamTwsPG`</summary>

```json
{
  "query": "Dream2Act video generation URDF IK"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "729bd4f7-6ce8-422b-97ec-3fa227813b18",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwSPKP6fCb9R8MeVMU2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98f40b4b-14e8-4b6d-bb42-18bafa317ecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y78isgBWw2pPoFKCmU9p43",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 16155,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 236,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 784,
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

_source line 7 · 2026-05-10T13:07:25.437Z_

<details><summary>↩ Tool result · `toolu_01V7MWRPvKvuULhrDamTwsPG`</summary>

```text
Web search results for query: "Dream2Act video generation URDF IK"

Links: [{"title":"GitHub - KDharmarajanDev/Dream2Flow: Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow · GitHub","url":"https://github.com/KDharmarajanDev/Dream2Flow"},{"title":"Introduction to IKFast and prerequisite — framefab_irb6600_support documentation","url":"https://choreo.readthedocs.io/en/latest/doc/ikfast_tutorial.html"},{"title":"URDF-Anything+: Autoregressive Articulated 3D Models Generation for Physical Simulation","url":"https://arxiv.org/html/2603.14010v1"},{"title":"URDF Studio - Robot Design & Visualization Platform | 机器人可视化设计平台","url":"https://urdf.d-robotics.cc/"},{"title":"Lula Kinematics Solver with custom URDF arm - Isaac Sim - NVIDIA Developer Forums","url":"https://forums.developer.nvidia.com/t/lula-kinematics-solver-with-custom-urdf-arm/280482"},{"title":"GitHub - OpenLegged/URDF-Studio: URDF-Studio is a web-based visual URDF robot modeler with 3D workspace, structured skeleton/detail/hardware workflows, motor library integration, MuJoCo export, and AI assistance. · GitHub","url":"https://github.com/OpenLegged/URDF-Studio"},{"title":"GitHub - ADVRHumanoids/modular_hhcm: Tool for URDF generation of modular robots","url":"https://github.com/ADVRHumanoids/modular_hhcm"},{"title":"Dream2Flow","url":"https://dream2flow.github.io/"},{"title":"DriveDreamer-2: LLM-Enhanced World Models for Diverse Driving Video Generation","url":"https://drivedreamer2.github.io/"},{"title":"[2512.24766] Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow","url":"https://arxiv.org/abs/2512.24766"}]

Based on the search results, I found information about related projects but not specifically "Dream2Act." However, I did find information about similar work:

## Dream2Flow

Dream2Flow is a framework that bridges video generation and robotic control through 3D object flow as an intermediate representation, reconstructing 3D object motions from generated videos and formulating manipulation as object trajectory tracking. By separating the state changes from the actuators that realize those changes, Dream2Flow overcomes the embodiment gap and enables zero-shot guidance from pre-trained video models to manipulate objects of diverse categories—including rigid, articulated, deformable, and granular.

Through trajectory optimization or reinforcement learning, Dream2Flow converts reconstructed 3D object flow into executable low-level commands without task-specific demonstrations, with simulation and real-world experiments highlighting 3D object flow as a general and scalable interface for adapting video generation models to open-world robotic manipulation.

## Related URDF Work

I also found that Dream2Flow's planner uses URDF files and supports configuration parameters including urdf_path (as a robot_descriptions package name or filesystem path), target_link_name, and various optimization parameters.

If you're looking for more specific information about a project called "Dream2Act" specifically, it may be a very recent or niche project that isn't yet widely indexed online, or it might be known by a slightly different name.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98f40b4b-14e8-4b6d-bb42-18bafa317ecc",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "c5b8e947-8ce2-4d77-80ae-51851a8371c5",
  "sourceToolAssistantUUID": "98f40b4b-14e8-4b6d-bb42-18bafa317ecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T13:07:25.765Z_

<details><summary>↩ Tool result · `toolu_01FAXUDXVcGbtU4428zyF8eR`</summary>

```text
Web search results for query: "BridgeV2W ControlNet URDF video diffusion"

Links: [{"title":"[2602.03793] BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks","url":"https://arxiv.org/abs/2602.03793"},{"title":"[2602.03793v1] BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks","url":"https://arxiv.org/abs/2602.03793v1"},{"title":"[2307.14073] VideoControlNet: A Motion-Guided Video-to-Video Translation Framework by Using Diffusion Model with ControlNet","url":"https://arxiv.org/abs/2307.14073"},{"title":"BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks | OpenReview","url":"https://openreview.net/forum?id=ZGWwV34Vmu"},{"title":"GitHub - ZhihaoHu/VideoControlNet: Official Pytorch Implementation for \"VideoControlNet: A Motion-Guided Video-to-Video Translation Framework by Using Diffusion Model with ControlNet\" · GitHub","url":"https://github.com/ZhihaoHu/VideoControlNet"},{"title":"Control-A-Video: Controllable Text-to-Video Generation with Diffusion Models","url":"https://controlavideo.github.io/"},{"title":"GitHub - un1tz3r0/controlnetvideo: Apply controlnet to video clips · GitHub","url":"https://github.com/un1tz3r0/controlnetvideo"},{"title":"VideoControlNet: A Motion-Guided Video-to-Video Translation ...","url":"https://vcg-aigc.github.io/"},{"title":"[2408.13005] EasyControl: Transfer ControlNet to Video Diffusion for Controllable Generation and Interpolation","url":"https://arxiv.org/abs/2408.13005"},{"title":"GitHub - DavideAlidosi/sd-webui-animatediff-for-ControlNet: AnimateDiff for AUTOMATIC1111 Stable Diffusion WebUI for ControlNet · GitHub","url":"https://github.com/DavideAlidosi/sd-webui-animatediff-for-ControlNet"}]

Based on the search results, here's what I found about BridgeV2W and its related components:

## BridgeV2W Overview

BridgeV2W addresses embodied world models, which have emerged as a promising paradigm in robotics, leveraging large-scale Internet videos or pretrained video generation models to enrich visual and motion priors. However, existing approaches face key challenges: a misalignment between coordinate-space actions and pixel-space videos, sensitivity to camera viewpoint, and non-unified architectures across embodiments.

## Technical Approach

BridgeV2W converts coordinate-space actions into pixel-aligned embodiment masks rendered from the URDF and camera parameters. These masks are then injected into a pretrained video generation model via a ControlNet-style pathway, which aligns the action control signals with predicted videos, adds view-specific conditioning to accommodate camera viewpoints, and yields a unified world model architecture across embodiments.

## Additional Features

To mitigate overfitting to static backgrounds, BridgeV2W further introduces a flow-based motion loss that focuses on learning dynamic and task-related motion.

The paper was published on arXiv in February 2026 and appears to be a recent development in bridging video generation models with embodied world models for robotics applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bddbd70-2325-455d-8d53-cb9b71650f5f",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "cb445c74-ff5b-4e76-b3ae-4492a64e3b7f",
  "sourceToolAssistantUUID": "4bddbd70-2325-455d-8d53-cb9b71650f5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T13:07:27.115Z_

<details><summary>↩ Tool result · `toolu_01LRg4esY3k1ZbsMCZBStW2J`</summary>

```text
Web search results for query: "BridgeV2W arXiv 2602.03793"

Links: [{"title":"[2602.03793] BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks","url":"https://arxiv.org/abs/2602.03793"},{"title":"[2602.03793v1] BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks","url":"https://arxiv.org/abs/2602.03793v1"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1318&show=2000"},{"title":"[2308.12952] BridgeData V2: A Dataset for Robot Learning at Scale","url":"https://arxiv.org/abs/2308.12952"},{"title":"BridgeData V2: A Dataset for Robot Learning at Scale","url":"https://rail-berkeley.github.io/bridgedata/"},{"title":"BridgeData V2: A Dataset for Robot Learning at Scale","url":"https://arxiv.org/html/2308.12952v3"},{"title":"[2512.03793] The enshittification of online search? Privacy and quality of Google, Bing and Apple in coding advice","url":"https://arxiv.org/abs/2512.03793"},{"title":"BridgeData V2: A Dataset for Robot Learning at Scale","url":"https://www.researchgate.net/publication/373364151_BridgeData_V2_A_Dataset_for_Robot_Learning_at_Scale"},{"title":"BRIDGE: Predicting Human Task Completion Time From Model Performance","url":"https://arxiv.org/html/2602.07267v1"},{"title":"[2503.03793] A generalisation of Henstock-Kurzweil integral to compact metric spaces","url":"https://arxiv.org/abs/2503.03793"}]

Based on the search results, here's what I found about BridgeV2W arXiv 2602.03793:

## Overview

BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks is a paper by Yixiang Chen and 10 other authors, submitted on February 3, 2026.

## Problem and Solution

Embodied world models have emerged as a promising paradigm in robotics, leveraging large-scale Internet videos or pretrained video generation models, but they face key challenges: misalignment between coordinate-space actions and pixel-space videos, sensitivity to camera viewpoint, and non-unified architectures across embodiments.

BridgeV2W converts coordinate-space actions into pixel-aligned embodiment masks rendered from the URDF and camera parameters, which are then injected into a pretrained video generation model via a ControlNet-style pathway to align action control signals with predicted videos, add view-specific conditioning, and yield a unified world model architecture across embodiments.

## Technical Contributions

To mitigate overfitting to static backgrounds, BridgeV2W introduces a flow-based motion loss that focuses on learning dynamic and task-relevant regions.

## Experimental Results

Experiments on single-arm (DROID) and dual-arm (AgiBot-G1) datasets show that BridgeV2W improves video generation quality compared to prior state-of-the-art methods, and it demonstrates potential on downstream real-world tasks including policy evaluation and goal-conditioned planning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "432a2b26-9d31-451b-a84c-a87f45d0c658",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "0793b004-f9c1-45f0-a823-474349220693",
  "sourceToolAssistantUUID": "432a2b26-9d31-451b-a84c-a87f45d0c658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T13:07:27.294Z_

<details><summary>↩ Tool result · `toolu_01JyFYAvdRuz2Vm3JPMZWwMX`</summary>

```text
Web search results for query: "Dream2Act arXiv 2603.19709 humanoid robot"

Links: [{"title":"Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis","url":"https://arxiv.org/html/2603.19709v1"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"SafeFlow: Real-Time Text-Driven Humanoid Whole-Body Control via Physics-Guided Rectified Flow and Selective Safety Gating","url":"https://arxiv.org/html/2603.23983"},{"title":"DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion","url":"https://arxiv.org/html/2509.14353v1"},{"title":"Robotics","url":"https://arxiv.org/list/cs.RO/recent"},{"title":"Scaling Tasks, Not Samples: Mastering Humanoid Control through Multi-Task Model-Based Reinforcement Learning","url":"https://arxiv.org/html/2603.01452"},{"title":"Human2Robot: Learning Robot Actions from Paired Human-Robot Videos","url":"https://arxiv.org/html/2502.16587v1"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2603.12263"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control","url":"https://arxiv.org/html/2603.22201v1"}]

Based on the search results, here's what I found about Dream2Act (arXiv 2603.19709):

## Overview
Dream2Act is a robot-centric framework that enables zero-shot interaction through generative video synthesis.

## The Problem It Addresses
Equipping humanoid robots with versatile interaction skills typically requires either extensive task-specific policy training or explicit human-to-robot motion retargeting. However, learning-based policies are hindered by prohibitive data collection costs, limiting their scalability. Meanwhile, retargeting paradigms rely heavily on human-centric pose estimation (e.g., SMPL), which inevitably introduces the morphology gap. Such skeletal scale mismatches result in severe spatial misalignments when mapped to robots, compromising interaction success.

## How It Works
Given an image of the predefined robot and target object in third-person view, the framework leverages video generation models to envision videos in which the physical robot completes the task with spatially aligned, morphology-consistent motion. It then employs a robust, high-fidelity pose extraction system to recover physically feasible, robot-native joint trajectories from these synthesized "dreams", which are subsequently executed via a general-purpose whole-body controller.

## Key Advantages
By operating strictly within the robot-native coordinate space, Dream2Act effectively avoids traditional retargeting errors and eliminates the need for task-specific policy training.

## Evaluation
Dream2Act was evaluated on the Unitree G1 across four categories of whole-body mobile interaction tasks (multi-position ball kicking, sofa sitting, bag punching, and box hugging).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "729bd4f7-6ce8-422b-97ec-3fa227813b18",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "550eef06-3083-407f-8e34-55e692665fd5",
  "sourceToolAssistantUUID": "729bd4f7-6ce8-422b-97ec-3fa227813b18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T13:07:28.928Z_

Good progress. Let me continue with the remaining papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "550eef06-3083-407f-8e34-55e692665fd5",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwT5Ubzi5GMGj2BE65G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7e7e7b96-4fb6-4bb2-ba62-4abfe02655cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014hxDRQzwoKrmcr5tFvPmjZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 3677,
      "cache_read_input_tokens": 16939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3677,
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

_source line 12 · 2026-05-10T13:07:29.142Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M5RBKhz1G2aTRStvcYf8EY`</summary>

```json
{
  "query": "EA-WM arXiv 2605.06192"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e7e7b96-4fb6-4bb2-ba62-4abfe02655cd",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwT5Ubzi5GMGj2BE65G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ab4b4f36-10b8-4e20-85dc-247dd1e0a80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014hxDRQzwoKrmcr5tFvPmjZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 3677,
      "cache_read_input_tokens": 16939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3677,
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

_source line 13 · 2026-05-10T13:07:29.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q9doPza4XC36XBG9mm1zdv`</summary>

```json
{
  "query": "EA-WM Event-Aware World Model kinematic heatmap"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab4b4f36-10b8-4e20-85dc-247dd1e0a80c",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwT5Ubzi5GMGj2BE65G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "440a67e8-cbf5-4556-9dad-4ba6406bb0ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014hxDRQzwoKrmcr5tFvPmjZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 3677,
      "cache_read_input_tokens": 16939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3677,
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

_source line 14 · 2026-05-10T13:07:29.773Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BDWd5TXwN5U4DYjztt1HgZ`</summary>

```json
{
  "query": "VAG arXiv 2604.09330 video action generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "440a67e8-cbf5-4556-9dad-4ba6406bb0ad",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwT5Ubzi5GMGj2BE65G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "15f272bb-087e-41f7-a8a3-bcf964c8628e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014hxDRQzwoKrmcr5tFvPmjZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 3677,
      "cache_read_input_tokens": 16939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3677,
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

_source line 15 · 2026-05-10T13:07:29.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HGwZmyPRFqRiiTBWjXbbhZ`</summary>

```json
{
  "query": "VAG dual-stream video action generation robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15f272bb-087e-41f7-a8a3-bcf964c8628e",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwT5Ubzi5GMGj2BE65G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9aac07ac-3568-4774-aa93-f7497c0cfef0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014hxDRQzwoKrmcr5tFvPmjZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 3677,
      "cache_read_input_tokens": 16939,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3677
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 900,
          "output_tokens": 217,
          "cache_read_input_tokens": 16939,
          "cache_creation_input_tokens": 3677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3677,
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

_source line 16 · 2026-05-10T13:07:35.412Z_

<details><summary>↩ Tool result · `toolu_01Q9doPza4XC36XBG9mm1zdv`</summary>

```text
Web search results for query: "EA-WM Event-Aware World Model kinematic heatmap"

Links: [{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"WAVES Heatmap system and EA | Forex Factory","url":"https://www.forexfactory.com/thread/116892-waves-heatmap-system-and-ea"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/Awesome-World-Models"},{"title":"Heat Map | Enterprise Architect User Guide","url":"https://sparxsystems.com/enterprise_architect_user_guide/14.0/guidebooks/tools_ea_heat_maps.html"},{"title":"EA Technology ConnectMore Interactive Map","url":"https://connectmore-heatmap.azurewebsites.net/"},{"title":"Embodiment-Aware World Models","url":"https://www.emergentmind.com/topics/embodiment-aware-world-model"},{"title":"Heat-map - EVM","url":"https://evm2.who.int/Global/Heatmap"},{"title":"A Heatmap guide for game level analysis | by Daria Rodionova | Medium","url":"https://medium.com/@dariarodionovano/a-heatmap-guide-for-game-level-analysis-68cb6a7bcb2b"},{"title":"Free EA Models","url":"https://enterprise-architecture.org/resources/free-enterprise-architecture-models/"},{"title":"Heatmap | Player Movement Data Visualization [1.18.2+] | SpigotMC - High Performance Minecraft Software","url":"https://www.spigotmc.org/resources/heatmap-player-movement-data-visualization-1-18-2.115407/"}]

Based on the search results, I found relevant information about EA-WM:

EA-WM is an event-aware robotic video world model conditioned on Structured Kinematic-to-Visual Action Fields (KVAFs). 

Regarding the kinematic heatmap specifically, KVAFs render depth-aware arm structures, joint landmarks, gripper geometry, end-effector heatmaps, and pose cues as temporally aligned visual fields. For each KVAF frame, candidate end-effector centers are detected from high-intensity heatmap regions.

EA-WM constructs KVAFs by lifting low-dimensional robot actions and kinematic states into the target camera view through robot kinematics and camera projection. Compared with raw action vectors, KVAFs bring action conditioning into the same image domain as future video generation, thereby alleviating domain misalignment and providing richer spatial and geometric cues for robotic world modeling.

The research appears to be very recent, with the paper available on arXiv as of two days ago.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "440a67e8-cbf5-4556-9dad-4ba6406bb0ad",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "1d1fb148-543c-44eb-b7fb-4e7a70b957a0",
  "sourceToolAssistantUUID": "440a67e8-cbf5-4556-9dad-4ba6406bb0ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T13:07:36.709Z_

<details><summary>↩ Tool result · `toolu_01BDWd5TXwN5U4DYjztt1HgZ`</summary>

```text
Web search results for query: "VAG arXiv 2604.09330 video action generation"

Links: [{"title":"[2604.09330] VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis","url":"https://arxiv.org/abs/2604.09330"},{"title":"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis","url":"https://arxiv.org/html/2604.09330"},{"title":"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis | alphaXiv","url":"https://www.alphaxiv.org/abs/2604.09330"},{"title":"ActionParty: Multi-Subject Action Binding in Generative Video Games","url":"https://arxiv.org/html/2604.02330"},{"title":"[2604.21362] KD-CVG: A Knowledge-Driven Approach for Creative Video Generation","url":"https://arxiv.org/abs/2604.21362"},{"title":"\\vm and \\vam: Autonomous Driving through Video Generative Modeling","url":"https://arxiv.org/html/2502.15672v1"},{"title":"[2604.10383] Agentic Video Generation: From Text to Executable Event Graphs via Tool-Constrained LLM Planning","url":"https://arxiv.org/abs/2604.10383"},{"title":"Action Images: End-to-End Policy Learning via Multiview Video Generation","url":"https://arxiv.org/html/2604.06168"},{"title":"Action-Aware Generative Sequence Modeling for Short Video Recommendation","url":"https://arxiv.org/html/2604.25834"},{"title":"[2604.04198v1] DriveVA: Video Action Models are Zero-Shot Drivers","url":"https://arxiv.org/abs/2604.04198v1"}]

Based on the search results, here's what I found about VAG (arXiv 2604.09330):

## Paper Overview

VAG is a unified flow-matching-based dual-stream framework that jointly generates video and action under visual and language conditioning.

## Problem It Addresses

Robot foundation models trained on large-scale human teleoperation data have enabled complex real-world tasks, but scaling these systems remains difficult due to expensive and labor-intensive task-specific demonstrations. While synthetic data, especially generated videos, offers promise, existing World Models do not provide paired action trajectories. World-Action models partially address this by predicting actions with visual outputs, yet often lack strong video-action alignment, while two-stage pipelines introduce inefficiency and error accumulation.

## Key Technical Contributions

VAG improves cross-modal consistency during generation by synchronizing denoising in both branches and using an adaptive 3D pooling mechanism to transfer compact global video context to the action branch.

## Results and Applications

VAG produces aligned video-action pairs with competitive prediction quality, supports executable trajectory replay, and provides useful synthetic pretraining data that improves downstream policy generalization.

The paper was submitted on April 10, 2026, and appears to be a contribution from researchers at GigaAI and several academic institutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15f272bb-087e-41f7-a8a3-bcf964c8628e",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "46dea861-37e4-4caf-bde8-144ec72687c4",
  "sourceToolAssistantUUID": "15f272bb-087e-41f7-a8a3-bcf964c8628e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T13:07:36.758Z_

<details><summary>↩ Tool result · `toolu_01HGwZmyPRFqRiiTBWjXbbhZ`</summary>

```text
Web search results for query: "VAG dual-stream video action generation robot"

Links: [{"title":"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis","url":"https://arxiv.org/html/2604.09330v1"},{"title":"[2604.09330] VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis","url":"https://arxiv.org/abs/2604.09330"},{"title":"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis | alphaXiv","url":"https://www.alphaxiv.org/abs/2604.09330"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"},{"title":"GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/robbyant/lingbot-va"},{"title":"GitHub - PRB-R-NINE-T/lingbot-va-fork: Causal video-action world model for generalist robot control","url":"https://github.com/PRB-R-NINE-T/lingbot-va-fork"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"GitHub - jmwang0117/Video4Robot: List of papers on video-centric robot learning · GitHub","url":"https://github.com/jmwang0117/Video4Robot"},{"title":"RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation","url":"https://arxiv.org/html/2601.05241"},{"title":"Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation","url":"https://homangab.github.io/gen2act/"}]

Based on the search results, here's what I found about VAG:

## VAG: Dual-Stream Video-Action Generation

VAG is a novel dual-stream video-action generation framework within a unified Flow-Matching-based generative formulation. Conditioned on the image and textual instruction, it is capable of synthesizing high-quality aligned video-action pairs in a single feed-forward pass.

### Purpose and Motivation

Recent advances in robot foundation models trained on large-scale human teleoperation data have enabled robots to perform increasingly complex real-world tasks. However, scaling these systems remains difficult because collecting task-specific demonstrations is expensive and labor-intensive. Synthetic data, especially generated videos, offer a promising direction, but existing World Models (WMs) are not directly suitable for policy learning since they do not provide paired action trajectories.

### Technical Approach

By synchronizing denoising in both branches and using an adaptive 3D pooling mechanism to transfer compact global video context to the action branch, VAG improves cross-modal consistency during generation.

### Key Results

The synthesized trajectories can be executed in simulation and replayed on a real robot with reasonable video-action consistency. Additionally, when VAG-generated data is used for pretraining, the downstream VLA success rate increases from 35% to 55% (+20% absolute).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aac07ac-3568-4774-aa93-f7497c0cfef0",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "2931e054-b2b7-4220-8045-c7f2befc82cc",
  "sourceToolAssistantUUID": "9aac07ac-3568-4774-aa93-f7497c0cfef0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T13:07:37.107Z_

<details><summary>↩ Tool result · `toolu_01M5RBKhz1G2aTRStvcYf8EY`</summary>

```text
Web search results for query: "EA-WM arXiv 2605.06192"

Links: [{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/pastweek?skip=185&show=1000"},{"title":"[2603.06192] Transformer-Based Pulse Shape Discrimination in HPGe Detectors with Masked Autoencoder Pre-training","url":"https://arxiv.org/abs/2603.06192"},{"title":"[2602.06192] Hypersoft X-ray Sources: A New Class of Luminous Cosmic Emitters","url":"https://arxiv.org/abs/2602.06192"},{"title":"Transformer-Based Pulse Shape Discrimination in HPGe Detectors with Masked Autoencoder Pre-training","url":"https://arxiv.org/html/2603.06192"},{"title":"[2304.06192] Progression in self-efficacy, interest, identity, sense of belonging, perceived recognition and effectiveness of peer interaction of physics majors and comparison with non-majors and Ph.D. students","url":"https://arxiv.org/abs/2304.06192"},{"title":"You Snooze, You Lose: Automatic Safety Alignment Restoration through Neural Weight Translation","url":"https://arxiv.org/html/2605.04992v1"},{"title":"[2605.06161] Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges","url":"https://arxiv.org/abs/2605.06161"},{"title":"[2605.05258] PARNESS: A Paper Harness for End-to-End Automated Scientific Research with Dynamic Workflows, Full-Text Indexing, and Cross-Run Knowledge Accumulation","url":"https://arxiv.org/abs/2605.05258"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"}]

Based on the search results, I found information about arXiv paper 2605.06192:

## EA-WM: Event-Aware Generative World Model

EA-WM is an Event-Aware Generative World Model that effectively closes the loop between kinematic control and visual perception. Rather than injecting joint or end-effector actions as abstract, low-dimensional tokens, EA-WM projects actions and kinematic states directly into the target camera view as Structured Kinematic-to-Visual Action Fields (KVAFs).

**Key Components:**

- At the representation level, EA-WM constructs KVAFs by lifting low-dimensional robot actions and kinematic states into the target camera view through robot kinematics and camera projection, rendering depth-aware arm structures, joint landmarks, gripper geometry, end-effector heatmaps, and pose cues as temporally aligned visual fields.

- EA-WM proposes an event-aware bidirectional fusion mechanism driven by Event-Difference Latent Supervision (EDLS), which explicitly regularizes cross-stream attention using temporal difference latents, compelling the model to dynamically attend to critical regions of robot motion, object state transitions, and robot-object interaction dynamics.

**Authors and Affiliation:**
The paper is authored by Zhaoyang Yang, Yurun Jin, Lizhe Qi, Kai Chen, and Cong Huang from Fudan University, Zhongguancun Academy, Zhongguancun Institute of Artificial Intelligence, University of Science and Technology of China, and DeepCybo.

The model achieves superior performance on the WorldArena benchmark, significantly enhancing physical adherence, 3D geometric accuracy, and fine-grained controllability compared to existing state-of-the-art baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab4b4f36-10b8-4e20-85dc-247dd1e0a80c",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "b564fe0a-0f54-4ef4-b5d9-3af921502b97",
  "sourceToolAssistantUUID": "ab4b4f36-10b8-4e20-85dc-247dd1e0a80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T13:07:38.699Z_

Excellent. Now let me search for new papers from March-May 2026 on the specific topics you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b564fe0a-0f54-4ef4-b5d9-3af921502b97",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwToUxm5t5QSNboTTDe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f0b0b5f8-120e-4a60-b8a8-69105d1dd998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lif8J2keMZtS6xEEkTjq4u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2466,
      "cache_creation_input_tokens": 2203,
      "cache_read_input_tokens": 20616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2203,
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

_source line 21 · 2026-05-10T13:07:38.922Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SdgSJm18UJGjZpoiVNtop1`</summary>

```json
{
  "query": "humanoid robot video generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0b0b5f8-120e-4a60-b8a8-69105d1dd998",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwToUxm5t5QSNboTTDe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e4fec6bb-1f64-497c-beb8-ad2d16be8be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lif8J2keMZtS6xEEkTjq4u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2466,
      "cache_creation_input_tokens": 2203,
      "cache_read_input_tokens": 20616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2203,
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

_source line 22 · 2026-05-10T13:07:39.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LayoQoLFMo9Vhwr9Q72ULn`</summary>

```json
{
  "query": "URDF-conditioned video diffusion robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4fec6bb-1f64-497c-beb8-ad2d16be8be5",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwToUxm5t5QSNboTTDe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "919836b0-2086-4a3c-81e3-955d2095b4a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lif8J2keMZtS6xEEkTjq4u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2466,
      "cache_creation_input_tokens": 2203,
      "cache_read_input_tokens": 20616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2203,
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

_source line 23 · 2026-05-10T13:07:39.599Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VKaFYi2ch2jXzdnxoVJCoX`</summary>

```json
{
  "query": "kinematic conditioning robot video synthesis 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "919836b0-2086-4a3c-81e3-955d2095b4a8",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwToUxm5t5QSNboTTDe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7188d725-ac76-434e-8df6-62cf08b88d32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lif8J2keMZtS6xEEkTjq4u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2466,
      "cache_creation_input_tokens": 2203,
      "cache_read_input_tokens": 20616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2203,
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

_source line 24 · 2026-05-10T13:07:39.816Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017RS5h4vsVhSHEfizU1KpDC`</summary>

```json
{
  "query": "full-body humanoid training data generation March April May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7188d725-ac76-434e-8df6-62cf08b88d32",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwToUxm5t5QSNboTTDe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "331fd69d-6f28-47ad-9c63-23af7c67ed0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lif8J2keMZtS6xEEkTjq4u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2466,
      "cache_creation_input_tokens": 2203,
      "cache_read_input_tokens": 20616,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2203
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2466,
          "output_tokens": 223,
          "cache_read_input_tokens": 20616,
          "cache_creation_input_tokens": 2203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2203,
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

_source line 25 · 2026-05-10T13:07:46.204Z_

<details><summary>↩ Tool result · `toolu_01SdgSJm18UJGjZpoiVNtop1`</summary>

```text
Web search results for query: "humanoid robot video generation 2026"

Links: [{"title":"New OMNI Humanoid Robot 2026 Release SHAKES AI Industry (AI NEWS) - YouTube","url":"https://www.youtube.com/watch?v=87by4MwD5fA"},{"title":"Humanoids conquered CES 2026 - Humanoid.guide","url":"https://humanoid.guide/humanoids-ces-2026/"},{"title":"Robot Videos: Atlas Humanoid, CES 2026 Bots , and More","url":"https://spectrum.ieee.org/robots-ces-2026"},{"title":"Video: Unitree’s G1 humanoid robot stuns with skating flips and spin in wild demo","url":"https://interestingengineering.com/ai-robotics/china-unitree-g1-humanoid-robot"},{"title":"Videos: Humanoid Robot Production, Mars Rovers, More - IEEE Spectrum","url":"https://spectrum.ieee.org/video-friday-humanoid-robot-production"},{"title":"National Robotics Week — Latest Physical AI Research, Breakthroughs and Resources | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/national-robotics-week-2026/"},{"title":"Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology","url":"https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"},{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"9 humanoid robots at CES 2026 that showed the future is already here","url":"https://interestingengineering.com/ai-robotics/9-humanoid-robots-at-ces-2026"},{"title":"Robot Videos: Atlas Humanoid, CES 2026 Bots , and More","url":"https://startupnews.fyi/2026/01/10/robot-videos-atlas-humanoid-ces-2026-bots-and-more/"}]

Based on the search results, here's what's happening with humanoid robots and video generation in 2026:

## Humanoid Robot Production & Demonstrations

New humanoid robots are hitting production in 2026. CES 2026 showcased humanoid robots built for real work, and marked a clear break from past patterns where robots now actually work, deployed in factory floors and hospital environments to home kitchens and service desks.

## Video Generation & AI Training

The search results reveal that video generation technology is being used to train and develop humanoid robots. Building on advancements in video generation and world models for autonomous vehicles, researchers have trained a world model that serves as a virtual simulator for robots. Additionally, new NVIDIA Cosmos world models for generating synthetic data help systems learn more efficiently and generalize across environments.

## Notable Demonstrations

Unitree Robotics unveiled its G1 humanoid executing 360° turns, one-leg spins, and front flips, showcasing strong balance control and motion stability. Boston Dynamics formally introduced the production-ready version of its electric Atlas humanoid, with Atlas autonomously rising from a flat position using a non-human joint-flipping maneuver.

The convergence of advanced video generation, world models, and physical AI is enabling more sophisticated training and demonstration of humanoid robots in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4fec6bb-1f64-497c-beb8-ad2d16be8be5",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "59603c3c-4d06-4784-9877-0ca3e40f1df5",
  "sourceToolAssistantUUID": "e4fec6bb-1f64-497c-beb8-ad2d16be8be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T13:07:47.394Z_

<details><summary>↩ Tool result · `toolu_01LayoQoLFMo9Vhwr9Q72ULn`</summary>

```text
Web search results for query: "URDF-conditioned video diffusion robot 2026"

Links: [{"title":"URDFormer","url":"https://urdformer.github.io/"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"LEARNING TO ACT FROM ACTIONLESS VIDEOS THROUGH DENSE CORRESPONDENCES","url":"https://flow-diffusion.github.io/AVDC.pdf"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"GitHub - ziqihuangg/Awesome-From-Video-Generation-to-World-Model: A list of works on video generation towards world model · GitHub","url":"https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model/"}]

Based on the web search results, I found several relevant research directions combining URDF, video diffusion, and robotics. Here are the key findings:

## URDF-Conditioned Video Diffusion for Robotics

URDFormer is a system that predicts URDF descriptions from a single image of an object, automatically collects data, and trains a robot within a simulator. The approach leverages image-conditioned stable diffusion to convert initial synthetic images into photorealistic images.

## Video Diffusion Models in Robotics (2026)

Recent research has expanded the use of video diffusion models for robotic applications. A unified diffusion-based learning framework has been proposed that integrates action diffusion and image diffusion processes into a single diffusion transformer model conditioned on independent diffusion timesteps.

## Conditioning Mechanisms for Video Generation

Video diffusion models introduce conditioning inputs into the video generation process through channel concatenation, cross-attention, or adaptive normalization. Channel concatenation is most effective when the conditioning signal is spatially aligned with the target output, such as in image-to-video generation, depth guidance, or pose conditioning.

## Related Applications

The field has also seen developments in counterfactual world models via digital twin-conditioned video diffusion, which relates to using structured descriptions (like URDFs) to condition video generation for simulation and planning tasks.

These approaches demonstrate how URDF representations can be effectively integrated with video diffusion models to improve robot learning and simulation capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "919836b0-2086-4a3c-81e3-955d2095b4a8",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "2bf865da-db76-400d-b7b4-22bd0a24382d",
  "sourceToolAssistantUUID": "919836b0-2086-4a3c-81e3-955d2095b4a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T13:07:48.291Z_

<details><summary>↩ Tool result · `toolu_017RS5h4vsVhSHEfizU1KpDC`</summary>

```text
Web search results for query: "full-body humanoid training data generation March April May 2026"

Links: [{"title":"Humanoid data: 10 Things That Matter in AI Right Now | MIT Technology Review","url":"https://www.technologyreview.com/2026/04/21/1135656/humanoid-data-robot-training-ai-artificial-intelligence/"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"The gig workers who are training humanoid robots at home | MIT Technology Review","url":"https://www.technologyreview.com/2026/04/01/1134863/humanoid-data-training-gig-economy-2026-breakthrough-technology/"},{"title":"[2510.08807] Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation","url":"https://arxiv.org/abs/2510.08807"},{"title":"GR00T-WholeBodyControl Documentation — GR00T-WholeBodyControl Documentation","url":"https://nvlabs.github.io/GR00T-WholeBodyControl/"},{"title":"Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation","url":"https://arxiv.org/html/2510.08807v1"},{"title":"[2604.17335] Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/abs/2604.17335"},{"title":"Humanoid Training Data Survey - Humanoid.guide","url":"https://humanoid.guide/humanoid-training-data-survey/"},{"title":"Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation","url":"https://human2humanoid.com/"}]

Based on the search results, here's what I found about full-body humanoid training data generation during March-May 2026:

## Recent Developments in Humanoid Training Data

**Industry Focus and Growing Gig Economy:**
At-home data recording is becoming a booming gig economy around the world, with data companies like Scale AI and Encord recruiting armies of data recorders, while DoorDash pays delivery drivers to film themselves doing chores. Robotics companies want tremendous amounts of data on how we move our hands and limbs, and their tactics are getting strange.

**NVIDIA GR00T Platform Updates:**
BONES-SEED was open-sourced with 142K+ human motions (approximately 288 hours) with G1 MuJoCo trajectories in March 2026. Additionally, SONIC training code and checkpoint were released on HuggingFace in April 2026. An end-to-end VLA workflow was released in May 2026 for collecting teleop data, fine-tuning Isaac-GR00T N1.7, and deploying with SONIC whole-body control.

**Data Collection Challenges:**
For robots to work in factories and serve as housekeepers, real-world data, however time-consuming and expensive to collect, may be what we need. The availability of high-quality humanoid training data has become the primary bottleneck to commercial viability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "331fd69d-6f28-47ad-9c63-23af7c67ed0f",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "18e5a1b9-2a4b-4993-b235-eb550dc475d1",
  "sourceToolAssistantUUID": "331fd69d-6f28-47ad-9c63-23af7c67ed0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T13:07:48.585Z_

<details><summary>↩ Tool result · `toolu_01VKaFYi2ch2jXzdnxoVJCoX`</summary>

```text
Web search results for query: "kinematic conditioning robot video synthesis 2026"

Links: [{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/"},{"title":"Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis","url":"https://arxiv.org/html/2603.19709v1"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"2026-3-16 Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/assets/kimodo_tech_report.pdf"},{"title":"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis","url":"https://arxiv.org/html/2604.09330"},{"title":"Learning Long-term Motion Embeddings for Efficient Kinematics Generation | CVPR 2026","url":"https://compvis.github.io/long-term-motion/"},{"title":"GitHub - ziqihuangg/Awesome-From-Video-Generation-to-World-Model: A list of works on video generation towards world model · GitHub","url":"https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model/"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://arxiv.org/html/2603.15546v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"}]

Based on the search results, here are several recent research projects combining kinematic conditioning with robot video synthesis in 2026:

## Key Projects:

**1. Kimodo - Scaling Controllable Human Motion Generation**

Kimodo is an expressive and controllable kinematic motion diffusion model trained on 700 hours of optical motion capture data that generates high-quality motions while being easily controlled through text and a comprehensive suite of kinematic constraints including full-body keyframes, sparse joint positions/rotations, 2D waypoints, and dense 2D paths. In a proof of concept, Kimodo can be used to generate a kinematic motion on the G1 robot skeleton, then GEAR-SONIC tracks the motion in simulation.

**2. Dream2Act - Robot-Centric Video Synthesis**

Dream2Act is a novel framework that achieves zero-shot humanoid interaction through generative video synthesis, introducing a novel paradigm for whole-body robot motion acquisition that offers a scalable alternative to costly manual teleoperation. The framework employs a high-fidelity pose estimation and reconstruction pipeline to recover robot-native kinematic trajectories directly from synthesized sequences, which are then executed through a general-purpose whole-body controller SONIC.

**3. EA-WM - Event-Aware Generative World Model**

EA-WM is an Event-Aware Generative World Model that effectively closes the loop between kinematic control and visual perception by projecting actions and kinematic states directly into the target camera view as Structured Kinematic-to-Visual Action Fields (KVAFs).

**4. VAG - Dual-Stream Video-Action Generation**

VAG is a novel dual-stream generative framework designed to synthesize aligned video–action pairs, using an adaptive 3D pooling module as a bridge between video and action generation, ensuring that generated visual and motor signals are rigorously aligned at every timestep without cumulative errors.

These projects represent the cutting edge of combining kinematic conditioning with video synthesis for robot control in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7188d725-ac76-434e-8df6-62cf08b88d32",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "065b9493-8fba-456e-9ef8-c7f8f4329fac",
  "sourceToolAssistantUUID": "7188d725-ac76-434e-8df6-62cf08b88d32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-10T13:07:50.040Z_

Now let me fetch the actual Dream2Act paper to get more details about it and verify the specific claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "065b9493-8fba-456e-9ef8-c7f8f4329fac",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwUeWEujAPDd8K9pjbj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e1d7050-8c9f-45f5-93fb-9538aa48d0d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y7yTnaGZm78iW6n8GQfg79",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 5414,
      "cache_read_input_tokens": 22819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5414,
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

_source line 30 · 2026-05-10T13:07:50.464Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ja37u2SpB5WYM8qCpqgVH3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.19709",
  "prompt": "What is the title, authors, abstract, and primary limitation mentioned in this paper?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e1d7050-8c9f-45f5-93fb-9538aa48d0d2",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwUeWEujAPDd8K9pjbj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9035c40-21a1-4704-9e77-467f19a8a4d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y7yTnaGZm78iW6n8GQfg79",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 5414,
      "cache_read_input_tokens": 22819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5414,
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

_source line 31 · 2026-05-10T13:07:51.072Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013uRCm3yvhHAmdAuTkcGLzU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.09330",
  "prompt": "Does the paper state that the video branch is not influenced by the action branch, or is this an inference? What does the paper explicitly say about the relationship between branches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9035c40-21a1-4704-9e77-467f19a8a4d2",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwUeWEujAPDd8K9pjbj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3bc5b175-523c-4d52-831a-268b1a33ded7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y7yTnaGZm78iW6n8GQfg79",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 5414,
      "cache_read_input_tokens": 22819,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5414
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 876,
          "output_tokens": 221,
          "cache_read_input_tokens": 22819,
          "cache_creation_input_tokens": 5414,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5414,
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

_source line 32 · 2026-05-10T13:07:54.762Z_

<details><summary>↩ Tool result · `toolu_013uRCm3yvhHAmdAuTkcGLzU`</summary>

```text
# Branch Relationship Analysis

Based on the provided content, the paper does **not** explicitly state whether the video branch is influenced by the action branch. The abstract describes the framework as a "dual-stream" system that "jointly generates video and action," but does not detail the directional flow of information between branches.

What the paper **does** explicitly say is that it uses "synchronized denoising in both branches" and "adaptive 3D pooling" to transfer "compact global video context to the action branch." This indicates the video branch influences the action branch, but the provided text does not clarify whether influence flows in the reverse direction.

The statement about synchronizing denoising suggests interdependence rather than complete independence, but determining whether the video branch is uninfluenced by actions would require the full paper text beyond this abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bc5b175-523c-4d52-831a-268b1a33ded7",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "865b0d9e-ceff-4f33-a9b6-9bd327e9c7ff",
  "sourceToolAssistantUUID": "3bc5b175-523c-4d52-831a-268b1a33ded7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T13:07:55.532Z_

<details><summary>↩ Tool result · `toolu_01Ja37u2SpB5WYM8qCpqgVH3`</summary>

```text
# Paper Summary

**Title:** "Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis"

**Authors:** Weisheng Xu, Jian Li, Yi Gu, Bin Yang, Haodong Chen, Shuyi Lin, Mingqian Zhou, Jing Tan, Qiwei Wu, Xiangrui Jiang, Taowen Wang, Jiawen Wen, Qiwei Liang, Jiaxi Zhang, and Renjing Xu

**Abstract:** The research presents Dream2Act, a framework that enables humanoid robots to perform complex interaction tasks without extensive training. Rather than relying on conventional motion retargeting (which introduces morphology mismatches), the approach uses generative video synthesis to envision robot-appropriate movements. A pose extraction system recovers feasible joint trajectories from synthesized videos, which are then executed. Testing on the Unitree G1 robot across four tasks (ball kicking, sofa sitting, bag punching, box hugging) achieved "a 37.5% overall success rate, compared to 0% for conventional retargeting."

**Primary Limitation:** While the paper doesn't explicitly state limitations in the provided content, the results suggest the framework's modest success rate indicates room for improvement in task completion reliability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9035c40-21a1-4704-9e77-467f19a8a4d2",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "5deec0c3-93fb-4fe8-aa52-126fcfbbeb90",
  "sourceToolAssistantUUID": "d9035c40-21a1-4704-9e77-467f19a8a4d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-10T13:07:56.762Z_

Let me get more specific information about VAG's architecture and search for more recent papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5deec0c3-93fb-4fe8-aa52-126fcfbbeb90",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwVACg2uYVEekdCH6h9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ca8b83e7-be65-4387-92f9-741967997f26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017HcrwJLbfjeb4ahaMkj5ub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 205,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 28233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-10T13:07:57.224Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M7m6C5byTFUQ7R4tcEkCuX`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.09330v1",
  "prompt": "Describe the architecture: does the paper explicitly state that the video branch is not influenced by the action branch? What is the exact mechanism of how video and action branches interact?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca8b83e7-be65-4387-92f9-741967997f26",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwVACg2uYVEekdCH6h9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "72801eb8-8dd4-48cd-9a66-05b1ed8316fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017HcrwJLbfjeb4ahaMkj5ub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 205,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 28233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-10T13:07:57.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Lq2egDzMQULEuxKCNZNiu`</summary>

```json
{
  "query": "robot video generation arxiv March 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72801eb8-8dd4-48cd-9a66-05b1ed8316fb",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwVACg2uYVEekdCH6h9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f85c34f1-d57c-4375-995a-706cf6b1ad9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017HcrwJLbfjeb4ahaMkj5ub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 205,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 28233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-10T13:07:57.641Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AuBaQoGBXYrXzZD9DRkpTs`</summary>

```json
{
  "query": "robot video generation arxiv April 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f85c34f1-d57c-4375-995a-706cf6b1ad9d",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwVACg2uYVEekdCH6h9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b0e92492-04ed-4da7-85a0-6fba60963103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017HcrwJLbfjeb4ahaMkj5ub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 205,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 28233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-10T13:07:57.735Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SwWw4spyFFL76FypZ2sqD2`</summary>

```json
{
  "query": "robot video generation arxiv May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0e92492-04ed-4da7-85a0-6fba60963103",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwVACg2uYVEekdCH6h9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f5b50d19-cd51-4b13-8705-7629ed46deaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017HcrwJLbfjeb4ahaMkj5ub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 205,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 28233,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1426
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 205,
          "output_tokens": 267,
          "cache_read_input_tokens": 28233,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1426,
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

_source line 39 · 2026-05-10T13:08:02.892Z_

<details><summary>↩ Tool result · `toolu_01M7m6C5byTFUQ7R4tcEkCuX`</summary>

```text
# VAG Architecture: Video-Action Branch Interaction

## Explicit Statement on Unidirectional Flow

Yes, the paper explicitly acknowledges this limitation. In the "Limitations and Future Work" section, the authors state:

> "VAG currently leverages visual information to guide action generation effectively, whereas video generation has not been influenced by the action branch, wasting beneficial control signals."

## Interaction Mechanism

The architecture implements a **unidirectional information flow**:

**Video Branch → Action Branch:**
- During each denoising step, the video branch produces a clean latent representation
- This latent undergoes **adaptive 3D pooling**, which "averages the entire spatiotemporal features of each channel" into a compact embedding
- The resulting global vector conditions the action branch's U-Net denoiser
- Both branches denoise synchronously at the same noise intensity

**Action Branch → Video Branch:**
- The paper confirms no reciprocal influence occurs
- The authors identify this as a design limitation worth addressing in future work

## Key Technical Detail

The pooling mechanism is deliberately "non-learnable" and "simple but efficient," converting spatiotemporal video information (dimensions C'×(T-1/4+1)×⌊H/8⌋×⌊W/8⌋) into a global condition vector without additional linear layers, ensuring computational efficiency while maintaining alignment between modalities.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72801eb8-8dd4-48cd-9a66-05b1ed8316fb",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "71dcbbad-a52d-412b-9b32-3442991ec4c2",
  "sourceToolAssistantUUID": "72801eb8-8dd4-48cd-9a66-05b1ed8316fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T13:08:04.908Z_

<details><summary>↩ Tool result · `toolu_01SwWw4spyFFL76FypZ2sqD2`</summary>

```text
Web search results for query: "robot video generation arxiv May 2026"

Links: [{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Video Generators are Robot Policies","url":"https://arxiv.org/html/2508.00795v1"},{"title":"RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models","url":"https://arxiv.org/html/2605.03821"},{"title":"Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation","url":"https://arxiv.org/html/2409.16283v1"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation","url":"https://arxiv.org/html/2601.05241"},{"title":"Action Images: End-to-End Policy Learning via Multiview Video Generation","url":"https://arxiv.org/html/2604.06168v1"},{"title":"Large Video Planner Enables Generalizable Robot Control","url":"https://arxiv.org/html/2512.15840v1"},{"title":"[2603.28489] Video Generation Models as World Models: Efficient Paradigms, Architectures and Algorithms","url":"https://arxiv.org/abs/2603.28489"},{"title":"[2604.27621] Robot Learning from Human Videos: A Survey","url":"https://arxiv.org/abs/2604.27621"}]

Based on the search results, here are recent papers on robot video generation from arXiv in May 2026:

## Recent Robot Video Generation Papers (May 2026)

**RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models** 
This paper (May 5, 2026) addresses how existing robot video world models trained with low-level objectives such as reconstruction and perceptual similarity are poorly aligned with capabilities that matter most for robot decision making, including instruction following, manipulation success, and physical plausibility. RoboAlign-R1 combines reward-aligned post-training with stabilized long-horizon inference and constructs RobotWorldBench, a benchmark of 10,000 annotated video–instruction pairs from four robot data sources.

**EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields**
EA-WM is an Event-Aware Generative World Model that closes the loop between kinematic control and visual perception by projecting actions and kinematic states directly into the target camera view as Structured Kinematic-to-Visual Action Fields (KVAFs).

**Action Images: End-to-End Policy Learning via Multiview Video Generation**
Action Images formulates policy learning as multiview video generation by translating 7-DoF robot actions into interpretable action images: multi-view action videos that are grounded in 2D pixels and explicitly track robot-arm motion.

These papers represent recent advances in using video generation models for robot learning and control tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5b50d19-cd51-4b13-8705-7629ed46deaa",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "3cb2eee2-7694-4fae-b569-59da1477445c",
  "sourceToolAssistantUUID": "f5b50d19-cd51-4b13-8705-7629ed46deaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T13:08:05.277Z_

<details><summary>↩ Tool result · `toolu_017Lq2egDzMQULEuxKCNZNiu`</summary>

```text
Web search results for query: "robot video generation arxiv March 2026"

Links: [{"title":"Video Generators are Robot Policies","url":"https://arxiv.org/html/2508.00795v1"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"[2603.13438] Draft-and-Target Sampling for Video Generation Policy","url":"https://arxiv.org/abs/2603.13438"},{"title":"Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation","url":"https://arxiv.org/html/2409.16283v1"},{"title":"[2604.27621] Robot Learning from Human Videos: A Survey","url":"https://arxiv.org/abs/2604.27621"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"VideoVLA: Video Generators Can Be Generalizable Robot Manipulators","url":"https://arxiv.org/html/2512.06963"},{"title":"[2601.15282v1] Rethinking Video Generation Model for the Embodied World","url":"https://arxiv.org/abs/2601.15282v1"},{"title":"Large Video Planner Enables Generalizable Robot Control","url":"https://arxiv.org/html/2512.15840v1"},{"title":"Large-Scale Actionless Video Pre-Training via Discrete Diffusion for Efficient Policy Learning","url":"https://arxiv.org/html/2402.14407v1"}]

Based on the web search results for "robot video generation arxiv March 2026," I found several recent papers on this topic:

## Key March 2026 Paper

The most recent paper from March 2026 is "Draft-and-Target Sampling for Video Generation Policy" (arXiv 2603.13438, published March 13, 2026). This work addresses video generation models being used as robot policies to predict future states, while tackling their high computational cost and long inference time. The paper proposes Draft-and-Target Sampling, a training-free diffusion inference paradigm that uses self-play denoising with two complementary trajectories, along with token chunking and progressive acceptance to reduce computation. Experiments show the method can achieve up to 2.1x speedup with minimal compromise to success rate.

## Related Recent Work

Other recent papers in this area include:
- A comprehensive survey on "Video Generation Models in Robotics" (January 2026) that provides exhaustive discussion of video generation models in robotics, especially in robot manipulation
- RoVid-X project (January 2026) introducing the largest open-source robotic dataset for video generation with 4 million annotated video clips
- VideoVLA (December 2025) transforming large video generation models into robotic Vision-Language-Action manipulators using a multi-modal Diffusion Transformer


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f85c34f1-d57c-4375-995a-706cf6b1ad9d",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "b7a9aa70-6100-4772-b0f6-eab999819691",
  "sourceToolAssistantUUID": "f85c34f1-d57c-4375-995a-706cf6b1ad9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T13:08:06.312Z_

<details><summary>↩ Tool result · `toolu_01AuBaQoGBXYrXzZD9DRkpTs`</summary>

```text
Web search results for query: "robot video generation arxiv April 2026"

Links: [{"title":"Video Generators are Robot Policies","url":"https://arxiv.org/html/2508.00795v1"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning","url":"https://arxiv.org/html/2506.09985v1"},{"title":"Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation","url":"https://arxiv.org/html/2409.16283v1"},{"title":"[2604.27621] Robot Learning from Human Videos: A Survey","url":"https://arxiv.org/abs/2604.27621"},{"title":"Large Video Planner Enables Generalizable Robot Control","url":"https://arxiv.org/html/2512.15840v1"},{"title":"Computer Science Apr 2026","url":"https://arxiv.org/list/cs/2026-04?skip=1500"},{"title":"VideoVLA: Video Generators Can Be Generalizable Robot Manipulators","url":"https://arxiv.org/html/2512.06963"},{"title":"New AI system pushes the time limits of generative video","url":"https://techxplore.com/news/2026-02-ai-limits-generative-video.html"},{"title":"[2409.16283] Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation","url":"https://arxiv.org/abs/2409.16283"}]

Based on the search results, here are some notable papers on robot video generation from arxiv around April 2026:

## Recent Papers on Robot Video Generation (April 2026)

One significant paper from April 26, 2026 explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot trajectories), to develop models capable of understanding, predicting, and planning in the physical world. The paper presents V-JEPA 2, which achieves strong performance on motion understanding and state-of-the-art performance on human action anticipation.

Another recent contribution is a survey on robot learning from human videos, submitted on April 30, 2026. This work addresses the critical challenge of scaling robot data by covering the field of learning robot manipulation skills from human video data, driven by the abundance of human activity videos and advances in computer vision, with the promise of enabling robots to acquire skills from vast and readily available human demonstrations.

## Other Notable Work

A survey on video generation models in robotics provides an exhaustive discussion of video generation models in robotics, especially in robot manipulation, with comprehensive review of generative video models as world models in robotics and discussion of specific applications, associated challenges, and future directions.

These papers collectively demonstrate the growing interest in leveraging video generation models for advancing robot learning and control capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0e92492-04ed-4da7-85a0-6fba60963103",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "ba8f6f6a-06f6-4767-aaa4-850a8ae3a762",
  "sourceToolAssistantUUID": "b0e92492-04ed-4da7-85a0-6fba60963103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-10T13:08:07.462Z_

Let me search for more specific papers on humanoid video generation and URDF-based approaches from the March-May 2026 period.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba8f6f6a-06f6-4767-aaa4-850a8ae3a762",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwVxFrrrGgiJ7h9hhNN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fda4523e-f217-4ba2-91ea-02625fcc0f90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Tv18KUJLLnXTasvLtNmDd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 2433,
      "cache_read_input_tokens": 29659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2433,
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

_source line 44 · 2026-05-10T13:08:07.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016BcRMkhcRHrHMetWbYQDB2`</summary>

```json
{
  "query": "\"humanoid\" video generation diffusion 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fda4523e-f217-4ba2-91ea-02625fcc0f90",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwVxFrrrGgiJ7h9hhNN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "00d7d7a5-67ed-42d8-af79-37d8a96ed083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Tv18KUJLLnXTasvLtNmDd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 2433,
      "cache_read_input_tokens": 29659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2433,
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

_source line 45 · 2026-05-10T13:08:07.955Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TJaNbb1KS1kDnpytoBhjC2`</summary>

```json
{
  "query": "URDF robot skeleton video conditioning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00d7d7a5-67ed-42d8-af79-37d8a96ed083",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwVxFrrrGgiJ7h9hhNN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb865c33-35cf-4cef-beb1-3ad8fcd93ed4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Tv18KUJLLnXTasvLtNmDd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 2433,
      "cache_read_input_tokens": 29659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2433,
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

_source line 46 · 2026-05-10T13:08:08.155Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017vY3Uad3K25dQCVuijERip`</summary>

```json
{
  "query": "kinematic heatmap robot video 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb865c33-35cf-4cef-beb1-3ad8fcd93ed4",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwVxFrrrGgiJ7h9hhNN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1485b4d5-edbe-4b18-bc30-a3568c5827b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Tv18KUJLLnXTasvLtNmDd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 2433,
      "cache_read_input_tokens": 29659,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2433
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 832,
          "output_tokens": 184,
          "cache_read_input_tokens": 29659,
          "cache_creation_input_tokens": 2433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2433,
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

_source line 47 · 2026-05-10T13:08:14.513Z_

<details><summary>↩ Tool result · `toolu_01TJaNbb1KS1kDnpytoBhjC2`</summary>

```text
Web search results for query: "URDF robot skeleton video conditioning 2026"

Links: [{"title":"GitHub - OpenLegged/URDF-Studio: URDF-Studio is a web-based visual URDF robot modeler with 3D workspace, structured skeleton/detail/hardware workflows, motor library integration, MuJoCo export, and AI assistance. · GitHub","url":"https://github.com/OpenLegged/URDF-Studio"},{"title":"Kinematic Skeleton","url":"https://github.com/dfki-ric/phobos/wiki/Kinematic-Skeleton"},{"title":"GitHub - ankurhanda/robot-assets: A repository of various URDFs and assets needed for robot manipulation · GitHub","url":"https://github.com/ankurhanda/robot-assets"},{"title":"Introduction to URDF — Industrial Training documentation","url":"https://industrial-training-master.readthedocs.io/en/melodic/_source/session3/Intro-to-URDF.html"},{"title":"URDFormer","url":"https://urdformer.github.io/"},{"title":"How to Build Your First Robot Model (URDF): Best Practices and Tips | by Chayma GARGOUCH | Medium","url":"https://medium.com/@chayma.gargouche/how-to-build-your-first-robot-model-urdf-best-practices-and-tips-364d01dee83d"},{"title":"urdf-models · GitHub Topics · GitHub","url":"https://github.com/topics/urdf-models"},{"title":"URDF for Robot Modeling - Full Course | The Construct","url":"https://www.theconstruct.ai/robotigniteacademy_learnros/ros-courses-library/urdf-ros-robot-modeling/"},{"title":"GitHub - unidex-ai/UniDex: [CVPR 2026] UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos · GitHub","url":"https://github.com/unidex-ai/UniDex"},{"title":"Robotics # Build-a-Bot using URDF | by Dilip Kumar | Medium","url":"https://dilipkumar.medium.com/robotics-build-a-bot-using-urdf-ad20a244131c"}]

Based on the search results, here are the key findings related to your query about URDF robot skeleton video conditioning in 2026:

## Recent URDF-Related Projects (2026)

**URDFormer** is a notable recent project that combines URDF prediction with video/image processing. It leverages image-conditioned stable diffusion to convert initial synthetic images into photorealistic images, which relates to your interest in video conditioning. Given a single image of an object, URDFormer predicts its URDF, automatically collects data, and trains a robot within a simulator.

**UniDex** is another 2026 project that involves URDF skeleton work with video data. UniDex provides a robot foundation suite for universal dexterous hand control from egocentric human videos, and it includes URDF files placed under specific directories with configuration files to specify parameters for hand models.

## URDF Basics

To provide context, a URDF (Unified Robot Description Format) is the "skeleton" of a robot and is an XML file that tells ROS exactly what the robot looks like, how much it weighs, and how its parts are connected to each other.

These 2026 projects show active development in combining URDF robot skeletons with video-based conditioning and image synthesis techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb865c33-35cf-4cef-beb1-3ad8fcd93ed4",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "5269591b-3894-4f85-b86f-9f268b75da99",
  "sourceToolAssistantUUID": "cb865c33-35cf-4cef-beb1-3ad8fcd93ed4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T13:08:16.383Z_

<details><summary>↩ Tool result · `toolu_017vY3Uad3K25dQCVuijERip`</summary>

```text
Web search results for query: "kinematic heatmap robot video 2026"

Links: [{"title":"Visualization of the RSS heat-map along with the robot locations and... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Visualization-of-the-RSS-heat-map-along-with-the-robot-locations-and-the-view-of-the_fig4_289828485"},{"title":"Robot motion heatmap - YouTube","url":"https://www.youtube.com/watch?v=wmvgq9rOU0w"},{"title":"Heatmap of the robot movement during simulation rendered with RAWSim-O | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Heatmap-of-the-robot-movement-during-simulation-rendered-with-RAWSim-O_fig2_320413347"},{"title":"National Robotics Week — Latest Physical AI Research, Breakthroughs and Resources | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/national-robotics-week-2026/"},{"title":"Humanoid Robot Comparison 2026: OpenArm vs Mobile ALOHA vs Unitree G1 | SVRC","url":"https://www.roboticscenter.ai/blog/humanoid-robot-comparison-2026"},{"title":"Empirical investigation of how robot head motion influences acceptance of heatmap-based XAI: Designing XAI with social robot | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10731272/"},{"title":"Demonstrate once, execute on many: Kinematic intelligence for cross-robot skill transfer | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.aea1995"},{"title":"Kinematic intelligence lets three different robots learn the same task safely","url":"https://techxplore.com/news/2026-04-kinematic-intelligence-robots-task-safely.html"},{"title":"MAPEX: Map Exploitation for Vision-Based Ship Trajectory Prediction","url":"https://www.mdpi.com/2079-8954/14/5/536"},{"title":"Heatmap of the robot's movements within each exhibit area during the... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Heatmap-of-the-robots-movements-within-each-exhibit-area-during-the-first-in-robot_fig5_276087500"}]

Based on the search results, here are the key findings related to your query about kinematic heatmap robot video 2026:

## Kinematic Intelligence Research (2026)

Researchers in the Learning Algorithms and Systems Laboratory (LASA) at EPFL's School of Engineering developed a robotic control framework called kinematic intelligence that takes human-demonstrated tasks, mathematically converts them into general movement strategies, and then adapts them so different robots can perform tasks based on their physical design.

The researchers recorded human-demonstrated object-manipulation tasks using motion-capture technology, then mathematically converted these recorded tasks into general movement strategies. They also developed a systematic classification of physical limits of different robot designs and their classification ensures robots can carry out tasks safely within their mechanical limits.

Three completely different commercial robots were able to reproduce the same sequence safely and reliably, with each robot handling different steps of the task and interpreting the same skill in its own way while staying within safe and feasible limits.

## XAI Heatmap Visualization (2026)

Additionally, a study investigated how robot head motion towards an AI attention heatmap during a visual identification task influences human user trust in explainable AI (XAI), finding that robot head motion presented in a video increased user acceptance of AI-generated results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1485b4d5-edbe-4b18-bc30-a3568c5827b2",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "acb33d0f-e2e2-4a28-ab9b-b03148b38fa7",
  "sourceToolAssistantUUID": "1485b4d5-edbe-4b18-bc30-a3568c5827b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T13:08:16.975Z_

<details><summary>↩ Tool result · `toolu_016BcRMkhcRHrHMetWbYQDB2`</summary>

```text
Web search results for query: ""humanoid" video generation diffusion 2026 arxiv"

Links: [{"title":"FlowAct-R1: Towards Interactive Humanoid Video Generation","url":"https://arxiv.org/html/2601.10103v1"},{"title":"[2601.10103] FlowAct-R1: Towards Interactive Humanoid Video Generation","url":"https://arxiv.org/abs/2601.10103"},{"title":"Rethinking Video Generation Model for the Embodied World","url":"https://arxiv.org/html/2601.15282v1"},{"title":"X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale","url":"https://arxiv.org/html/2512.04537v1"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis","url":"https://arxiv.org/html/2603.19709v1"},{"title":"DreaMoving: A Human Video Generation Framework based on Diffusion Models","url":"https://arxiv.org/html/2312.05107v2"},{"title":"[2507.16869] Controllable Video Generation: A Survey","url":"https://arxiv.org/abs/2507.16869"},{"title":"Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades","url":"https://arxiv.org/html/2603.08028"},{"title":"Human Motion Video Generation: A Survey","url":"https://arxiv.org/html/2509.03883v1"}]

Based on the search results, here are several recent arxiv papers from 2026 on humanoid video generation using diffusion models:

## Key Papers Found:

**1. FlowAct-R1: Towards Interactive Humanoid Video Generation**
Interactive humanoid video generation aims to synthesize lifelike visual agents that can engage with humans through continuous and responsive video. FlowAct-R1 is a framework specifically designed for real-time interactive humanoid video generation, built upon a MMDiT architecture, that enables the streaming synthesis of video with arbitrary durations while maintaining low-latency responsiveness. The framework achieves a stable 25fps at 480p resolution with a time-to-first-frame (TTFF) of only around 1.5 seconds.

**2. X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale**
X-Humanoid adapts the powerful Wan 2.2 diffusion transformer (DiT) model into a video-in video-out structure. The approach was applied to create a large-scale, 60-hour "robotized" version of the Ego-Exo4D dataset, featuring the Tesla Optimus humanoid.

**3. Dream2Act: Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis**
Dream2Act is a novel framework that achieves zero-shot humanoid interaction through generative video synthesis. Given only a single third-person image of the humanoid and an interaction object, the framework leverages powerful image-to-video diffusion priors to hallucinate realistic and temporally coherent videos of the physical robot executing the desired task.

**4. Rethinking Video Generation Model for the Embodied World**
This paper discusses video generation models applied to robotic scenarios, including humanoid robots, presenting evaluation benchmarks for various embodiment types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00d7d7a5-67ed-42d8-af79-37d8a96ed083",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "58b065b9-6aa4-48c9-a046-23c7d91b95dc",
  "sourceToolAssistantUUID": "00d7d7a5-67ed-42d8-af79-37d8a96ed083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-10T13:08:18.181Z_

Let me do one more focused search on the specific papers and recent work to ensure comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58b065b9-6aa4-48c9-a046-23c7d91b95dc",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwWjq2AJr2diHxfGiac",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d8e8dc2f-3bf6-48b4-aa25-3c1d5013fff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012YzecKhG74Ut5muoJK1FpB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1822,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 32092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 51 · 2026-05-10T13:08:19.061Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YJNDX9pKe2ZgyUcmFvcXjw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06192",
  "prompt": "What is the full title, authors, submission date, and abstract? Does it mention Wan 2.2 and WorldArena benchmark?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8e8dc2f-3bf6-48b4-aa25-3c1d5013fff4",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwWjq2AJr2diHxfGiac",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "196e2bd5-dfdb-4f5e-974d-01fc2faa959c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012YzecKhG74Ut5muoJK1FpB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1822,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 32092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 52 · 2026-05-10T13:08:19.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VxzobHWodP2DdANpXiUjyA`</summary>

```json
{
  "query": "Kimodo robot skeleton video generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "196e2bd5-dfdb-4f5e-974d-01fc2faa959c",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwWjq2AJr2diHxfGiac",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5e42c028-b5ee-46a6-a96c-1f30839ef44c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012YzecKhG74Ut5muoJK1FpB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1822,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 32092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 53 · 2026-05-10T13:08:19.684Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KiVhgE9onK7MfYTkyBTkyP`</summary>

```json
{
  "query": "RoboAlign-R1 robot video world model May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e42c028-b5ee-46a6-a96c-1f30839ef44c",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwWjq2AJr2diHxfGiac",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "896f0583-c3f9-4db9-885b-ec18ae9ba3dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012YzecKhG74Ut5muoJK1FpB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1822,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 32092,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1822,
          "output_tokens": 226,
          "cache_read_input_tokens": 32092,
          "cache_creation_input_tokens": 1902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1902,
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

_source line 54 · 2026-05-10T13:08:22.835Z_

<details><summary>↩ Tool result · `toolu_01YJNDX9pKe2ZgyUcmFvcXjw`</summary>

```text
# Paper Summary

**Full Title:** "EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields"

**Authors:** Zhaoyang Yang, Yurun Jin, Lizhe Qi, Cong Huang, and Kai Chen

**Submission Date:** May 7, 2026

**Abstract Summary:** The paper presents an approach that "effectively closes the loop between kinematic control and visual perception" by projecting robot actions directly into camera views as structured fields. It introduces bidirectional fusion blocks to capture object state changes and interaction dynamics.

---

**Regarding your specific questions:**

The document does **not mention "Wan 2.2"** in the visible content.

However, it **does reference the WorldArena benchmark**: The abstract states the work was "Evaluated on the comprehensive WorldArena benchmark" where "EA-WM achieves state-of-the-art performance, outperforming existing baselines by a significant margin."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "196e2bd5-dfdb-4f5e-974d-01fc2faa959c",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "da9007f7-db53-4db8-bd4b-89762403ed2a",
  "sourceToolAssistantUUID": "196e2bd5-dfdb-4f5e-974d-01fc2faa959c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-10T13:08:26.387Z_

<details><summary>↩ Tool result · `toolu_01VxzobHWodP2DdANpXiUjyA`</summary>

```text
Web search results for query: "Kimodo robot skeleton video generation 2026"

Links: [{"title":"GitHub - nv-tlabs/kimodo: Official implementation of Kimodo, a kinematic motion diffusion model for high-quality human(oid) motion generation. · GitHub","url":"https://github.com/nv-tlabs/kimodo"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/"},{"title":"2026-3-16 Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/assets/kimodo_tech_report.pdf"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://arxiv.org/html/2603.15546v1"},{"title":"kimodo/README.md at main · nv-tlabs/kimodo","url":"https://github.com/nv-tlabs/kimodo/blob/main/README.md"},{"title":"Kimodo — NVIDIA Open-Source 3D Motion Generation AI","url":"https://kimodo.net/models"},{"title":"NVIDIA’s Kimodo generates studio-quality 3D motion from text, and it’s free - Efficienist","url":"https://efficienist.com/nvidias-kimodo-generates-studio-quality-3d-motion-from-text-and-its-free/"},{"title":"nvidia/Kimodo-SOMA-RP-v1 · Hugging Face","url":"https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1"},{"title":"NVIDIA Kimodo: AI-Powered 3D Motion Generation","url":"https://howaiworks.ai/blog/nvidia-kimodo-3d-motion-generation"},{"title":"NVIDIA Kimodo Turns Text Into Motion | TheQuery","url":"https://www.thequery.in/articles/nvidia-kimodo-motion-generation-release"}]

Based on the search results, here's what I found about Kimodo:

## Overview

Kimodo generates high-quality 3D human and robot motions, and is controlled through text prompts and an extensive set of constraints such as full-body pose keyframes, end-effector positions/rotations, 2D paths, and 2D waypoints.

## 2026 Release Timeline

The initial open-source release of Kimodo occurred on March 16, 2026, with five model variants (SOMA, G1, SMPL-X), CLI, interactive demo, and timeline annotations for BONES-SEED. The Kimodo Motion Generation Benchmark was released on April 10, 2026, alongside new v1.1 Kimodo-SOMA models.

## Robot Skeleton Support

Regarding robot motion generation specifically, the model generates high-quality 3D human and robot motions. Several variations of Kimodo are available trained on various skeletons and datasets. One key variant is trained on the proprietary Bones Rigplay dataset retargeted to the 34-joint Unitree G1 robot skeleton.

## Capabilities

Kimodo is an expressive and controllable kinematic motion diffusion model trained on 700 hours of optical motion capture data. By default, a custom NPZ format is saved that is compatible with the web demo. For Kimodo-G1 models, the motion can be saved in the standard MuJoCo qpos CSV format.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e42c028-b5ee-46a6-a96c-1f30839ef44c",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "2485144e-9b55-41a2-949d-1925c7416bce",
  "sourceToolAssistantUUID": "5e42c028-b5ee-46a6-a96c-1f30839ef44c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-10T13:08:26.909Z_

<details><summary>↩ Tool result · `toolu_01KiVhgE9onK7MfYTkyBTkyP`</summary>

```text
Web search results for query: "RoboAlign-R1 robot video world model May 2026"

Links: [{"title":"[2605.03821] RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models","url":"https://arxiv.org/abs/2605.03821"},{"title":"RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models","url":"https://arxiv.org/html/2605.03821"},{"title":"1 World-R1 enables geometrically consistent world modeling in video foundation models via reinforcement learning. It accepts text input and generates high-quality 3D consistent videos. We visualize the reconstruction results alongside the video frames. Video results are in our supplementary material.","url":"https://arxiv.org/html/2604.24764v1"},{"title":"Neo humanoid maker 1X releases world model to help bots learn what they see | TechCrunch","url":"https://techcrunch.com/2026/01/13/neo-humanoid-maker-1x-releases-world-model-to-help-bots-learn-what-they-see/"},{"title":"January 2026 World-R1: Reinforcing 3D Constraints for Text-to-Video Generation","url":"https://arxiv.org/pdf/2604.24764"},{"title":"1X NEO Review: $20K Home Robot [2026]","url":"https://blog.robozaps.com/b/1x-neo-review"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Can world models unlock general purpose robotics? - Bessemer Venture Partners","url":"https://www.bvp.com/atlas/can-world-models-unlock-general-purpose-robotics"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"1X World Model","url":"https://www.1x.tech/discover/1x-world-model"}]

I found relevant information about RoboAlign-R1. Here's what the search revealed:

## RoboAlign-R1 Overview

RoboAlign-R1 is a framework that combines reward-aligned post-training with stabilized long-horizon inference for robot video world models.

### Key Features

The framework includes RobotWorldBench, a benchmark of 10,000 annotated video-instruction pairs collected from four robot data sources, and trains a multimodal teacher judge, RoboAlign-Judge, to provide fine-grained six-dimensional evaluation of generated videos. A lightweight student reward model is distilled from the teacher for efficient reinforcement-learning-based post-training.

### Performance

RoboAlign-R1 improves the aggregate six-dimension score by 10.1% over the strongest baseline, including gains of 7.5% on Manipulation Accuracy and 4.6% on Instruction Following.

### Long-Horizon Improvements

To reduce long-horizon rollout drift, the framework introduces Sliding Window Re-encoding (SWR), a training-free inference strategy that periodically refreshes the generation context. SWR improves long-horizon prediction quality with only about 1% additional latency, yielding a 2.8% gain in SSIM and a 9.8% reduction in LPIPS.

The research was published on May 5, 2026, making it very recent work in the field of robot video world models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "896f0583-c3f9-4db9-885b-ec18ae9ba3dc",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a38eeb6543c36a1cd",
  "type": "user",
  "uuid": "99a3a3fb-ad15-4e22-a8a8-948461c8d70e",
  "sourceToolAssistantUUID": "896f0583-c3f9-4db9-885b-ec18ae9ba3dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-10T13:08:54.542Z_

Perfect. Now let me compile my comprehensive findings report.

---

## COMPREHENSIVE SEARCH RESULTS AND VERIFICATION

### **PAPER 1: BridgeV2W (arXiv:2602.03793) - CONFIRMED**

**Status:** CONFIRMED - Paper exists and details verified

**Full Title:** "BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks"

**Submission Date:** February 3, 2026

**Authors:** Yixiang Chen et al. (11+ authors)

**Key Claims - VERIFIED:**
- ✅ **Uses ControlNet + URDF embodiment masks**: CONFIRMED. The paper converts coordinate-space actions into pixel-aligned embodiment masks rendered from URDF and camera parameters, then injects them into a pretrained video generation model via a ControlNet-style pathway.
- ✅ **Injected into video diffusion models for robot manipulation**: CONFIRMED. The masks are injected to align action control signals with predicted videos.
- ✅ **Robot manipulation video generation**: CONFIRMED. Experiments on single-arm (DROID) and dual-arm (AgiBot-G1) datasets.

**Technical Details:**
- Converts coordinate-space actions to pixel-aligned embodiment masks (URDF + camera rendering)
- Introduces flow-based motion loss to focus on dynamic, task-relevant regions
- Unified architecture across different robot embodiments

**Source:** https://arxiv.org/abs/2602.03793

---

### **PAPER 2: Dream2Act (arXiv:2603.19709) - CONFIRMED WITH CLARIFICATION**

**Status:** CONFIRMED - But with important clarification on methodology

**Full Title:** "Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis"

**Submission Date:** March 2026

**Authors:** Weisheng Xu, Jian Li, Yi Gu, and 12 others

**Key Claims - PARTIALLY VERIFIED:**
- ✅ **Humanoid robot video generation**: CONFIRMED. Uses generative video synthesis to create robot-appropriate movements.
- ⚠️ **Post-hoc URDF-constrained IK after video generation**: NOT EXPLICITLY CONFIRMED as described. The paper uses a "high-fidelity pose extraction system to recover physically feasible, robot-native joint trajectories from synthesized videos" - but this is not explicitly stated as "post-hoc URDF-constrained IK." The mechanism is pose extraction, not necessarily URDF-IK.

**Primary Limitation:**
The paper's own results suggest a primary limitation: the framework achieved only **37.5% overall success rate** on four tasks (ball kicking, sofa sitting, bag punching, box hugging) on the Unitree G1 robot, suggesting significant room for improvement in task completion reliability.

**Source:** https://arxiv.org/abs/2603.19709

---

### **PAPER 3: EA-WM (arXiv:2605.06192) - CONFIRMED WITH PARTIAL VERIFICATION**

**Status:** CONFIRMED - Paper exists with verified kinematic conditioning, PARTIAL verification of Wan 2.2 claim

**Full Title:** "EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields"

**Submission Date:** May 7, 2026

**Authors:** Zhaoyang Yang, Yurun Jin, Lizhe Qi, Cong Huang, Kai Chen (Fudan University, Zhongguancun Academy, DeepCybo)

**Key Claims - VERIFICATION STATUS:**
- ✅ **Uses kinematic conditioning**: CONFIRMED. Constructs "Structured Kinematic-to-Visual Action Fields (KVAFs)" by lifting low-dimensional robot actions/kinematic states into target camera view.
- ✅ **Kinematic heatmaps**: CONFIRMED. Renders "depth-aware arm structures, joint landmarks, gripper geometry, **end-effector heatmaps**, and pose cues."
- ✅ **WorldArena benchmark**: CONFIRMED. Achieves state-of-the-art on WorldArena benchmark.
- ⚠️ **Wan 2.2 cross-attention**: NOT FOUND IN AVAILABLE CONTENT. The paper does not mention "Wan 2.2" in the accessible portions. This claim cannot be verified from the materials reviewed.
- ✅ **Arm manipulation**: CONFIRMED. Paper focuses on arm manipulation tasks.

**Technical Details:**
- Event-Difference Latent Supervision (EDLS) for cross-stream attention fusion
- Projects actions/kinematic states as visual fields in camera space
- Addresses kinematic-to-visual domain alignment

**Source:** https://arxiv.org/abs/2605.06192

---

### **PAPER 4: VAG (arXiv:2604.09330) - CONFIRMED WITH EXPLICIT FINDING**

**Status:** CONFIRMED - Paper explicitly states the architectural limitation you referenced

**Full Title:** "VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis"

**Submission Date:** April 10, 2026

**Key Finding on Branch Independence:**
✅ **EXPLICIT STATEMENT FOUND**: The paper's "Limitations and Future Work" section explicitly states:

> "VAG currently leverages visual information to guide action generation effectively, whereas **video generation has not been influenced by the action branch, wasting beneficial control signals.**"

This is **NOT an inference** - the authors explicitly acknowledge this as a design limitation.

**Architecture:**
- **Video → Action**: Video branch produces clean latent, undergoes adaptive 3D pooling to create global condition vector for action branch
- **Action → Video**: NO reciprocal influence (acknowledged limitation)
- Both branches denoise synchronously

**Performance:**
- Synthesized trajectories can be executed in simulation and real robots
- +20% improvement in downstream VLA success rate (35% → 55% with VAG pretraining)

**Source:** https://arxiv.org/abs/2604.09330

---

### **NEW PAPERS FROM MARCH-MAY 2026**

**Found 5 significant new papers:**

#### **1. Draft-and-Target Sampling for Video Generation Policy (arXiv:2603.13438)**
- **Date:** March 13, 2026
- **Focus:** Efficient video generation for robot policies with 2.1x speedup
- **Method:** Training-free diffusion inference with self-play denoising
- **Source:** https://arxiv.org/abs/2603.13438

#### **2. FlowAct-R1: Towards Interactive Humanoid Video Generation**
- **Date:** January 2026 (edge of your range)
- **Focus:** Real-time interactive humanoid video synthesis
- **Performance:** 25fps at 480p with 1.5s time-to-first-frame
- **Architecture:** MMDiT-based for streaming synthesis
- **Source:** https://arxiv.org/abs/2601.10103

#### **3. Kimodo: Scaling Controllable Human Motion Generation (arXiv:2603.15546)**
- **Date:** March 16, 2026 (open source release)
- **Focus:** Kinematic motion diffusion for humanoid skeleton control
- **Training:** 700 hours optical motion capture
- **Robot Support:** Unitree G1 skeleton variant available
- **Constraints:** Full-body keyframes, joint positions/rotations, 2D waypoints, 2D paths
- **Source:** https://arxiv.org/abs/2603.15546

#### **4. RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models (arXiv:2605.03821)**
- **Date:** May 5, 2026
- **Focus:** Aligning robot video world models with downstream task performance
- **Benchmark:** RobotWorldBench (10,000 annotated video-instruction pairs)
- **Improvements:** 10.1% aggregate improvement, 7.5% on manipulation accuracy, 4.6% on instruction following
- **Innovation:** Sliding Window Re-encoding (SWR) for long-horizon consistency
- **Source:** https://arxiv.org/abs/2605.03821

#### **5. X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale**
- **Focus:** Adapts Wan 2.2 diffusion transformer for video-in/video-out structure
- **Dataset:** 60-hour "robotized" Ego-Exo4D with Tesla Optimus humanoid
- **Method:** Applies Wan 2.2 DiT to human video retargeting for robots
- **Source:** https://arxiv.org/html/2512.04537v1

#### **6. V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning (arXiv:2506.09985)**
- **Date:** April 26, 2026
- **Focus:** Self-supervised learning combining internet-scale video with robot interaction data
- **Performance:** State-of-the-art on human action anticipation
- **Source:** https://arxiv.org/html/2506.09985v1

#### **7. Robot Learning from Human Videos: A Survey (arXiv:2604.27621)**
- **Date:** April 30, 2026
- **Focus:** Comprehensive review of learning robot skills from human video data
- **Motivation:** Scaling robot data by leveraging abundant human demonstrations
- **Source:** https://arxiv.org/abs/2604.27621

---

### **SUMMARY OF VERIFICATION**

| Paper | Status | Key Finding |
|-------|--------|------------|
| BridgeV2W | ✅ CONFIRMED | ControlNet + URDF embodiment masks verified |
| Dream2Act | ✅ CONFIRMED | Pose extraction (not explicitly URDF-IK); 37.5% success rate |
| EA-WM | ✅ MOSTLY CONFIRMED | Kinematic heatmaps verified; Wan 2.2 claim unverified |
| VAG | ✅ CONFIRMED | **Explicit** statement about video-action independence found |

**Notable Finding:** You were right about VAG - the paper explicitly identifies the unidirectional information flow (video→action, no action→video) as a limitation in the limitations section, making it a documented design choice rather than an inference.

Sources:
- [BridgeV2W arxiv](https://arxiv.org/abs/2602.03793)
- [Dream2Act arxiv](https://arxiv.org/abs/2603.19709)
- [EA-WM arxiv](https://arxiv.org/abs/2605.06192)
- [VAG arxiv](https://arxiv.org/abs/2604.09330)
- [Draft-and-Target Sampling arxiv](https://arxiv.org/abs/2603.13438)
- [FlowAct-R1 arxiv](https://arxiv.org/abs/2601.10103)
- [Kimodo arxiv](https://arxiv.org/abs/2603.15546)
- [RoboAlign-R1 arxiv](https://arxiv.org/abs/2605.03821)
- [X-Humanoid arxiv](https://arxiv.org/html/2512.04537v1)
- [V-JEPA 2 arxiv](https://arxiv.org/html/2506.09985v1)
- [Robot Learning from Human Videos Survey arxiv](https://arxiv.org/abs/2604.27621)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99a3a3fb-ad15-4e22-a8a8-948461c8d70e",
  "isSidechain": true,
  "agentId": "a38eeb6543c36a1cd",
  "requestId": "req_011CatwXUKeKvpbsjtN6nWmh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b2e13ee-3866-4675-9f03-4f58e8d418b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017F3HtHMKQoHTfKbkb21tYR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4084,
      "cache_read_input_tokens": 33994,
      "output_tokens": 2781,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4084
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2781,
          "cache_read_input_tokens": 33994,
          "cache_creation_input_tokens": 4084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4084,
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
