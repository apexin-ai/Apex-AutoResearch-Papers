# Research conversation: I need to research the paper "DemoHLM" (arXiv:2510.11258) about generating diverse humanoid loco-manipulation trajectori

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a631f7163574985c8.jsonl`
- **Structured JSON:** [`d4358e4c6c8e158bcacc.json`](../../sessions/d4/d4358e4c6c8e158bcacc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-10T19:14:27.546Z_

I need to research the paper "DemoHLM" (arXiv:2510.11258) about generating diverse humanoid loco-manipulation trajectories from a single teleoperated demonstration.

Please:
1. Use WebSearch to find "DemoHLM humanoid loco-manipulation demonstration generation arXiv 2510.11258"
2. Use WebFetch to read the paper from arxiv.org/abs/2510.11258
3. Summarize: What is DemoHLM's pipeline? How does it convert demos to object-centric representations? What's the 3-stage pipeline (locomotion → pre-manipulation → manipulation)? What robot does it use? What are its limitations?

Report back with detailed findings about the method, results, and how it compares to grammar-based compositional task generation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a631f7163574985c8",
  "type": "user",
  "uuid": "242fc480-5a4f-4a58-bceb-0dc6e4677cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:14:27.548Z_

```json
{
  "parentUuid": "242fc480-5a4f-4a58-bceb-0dc6e4677cfe",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
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
  "uuid": "5d670673-eeb6-4cce-a99c-90795a2a82f0",
  "timestamp": "2026-05-10T19:14:27.548Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T19:14:30.610Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SxY17yD83GQjab4yHtVCfB`</summary>

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
  "parentUuid": "5d670673-eeb6-4cce-a99c-90795a2a82f0",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
  "requestId": "req_011CauRSHZNDE7S1YEe15gVm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "145eef26-e1b0-4aca-ba0a-5d6caf3c6f94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JerHbfVxNKRVqsJAoEJXtF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 7164,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 706
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 7164,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 706,
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

_source line 4 · 2026-05-10T19:14:30.618Z_

<details><summary>↩ Tool result · `toolu_01SxY17yD83GQjab4yHtVCfB`</summary>

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
  "parentUuid": "145eef26-e1b0-4aca-ba0a-5d6caf3c6f94",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a631f7163574985c8",
  "type": "user",
  "uuid": "1a99484e-45e6-44c9-9083-c1547d644b9b",
  "sourceToolAssistantUUID": "145eef26-e1b0-4aca-ba0a-5d6caf3c6f94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:14:34.050Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ntz6L5Qv4rtSiXrD6NVmrY`</summary>

```json
{
  "query": "DemoHLM humanoid loco-manipulation demonstration generation arXiv 2510.11258"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a99484e-45e6-44c9-9083-c1547d644b9b",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
  "requestId": "req_011CauRSWnr8NCH683exUq44",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b28f2056-afac-4bd2-b810-29ec0d8039b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D71w2Ax8kh1eaXnFb8BXNQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1881,
      "cache_read_input_tokens": 7870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1881,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 75,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T19:14:36.138Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BfsCeWX7jxjYNStrQgvg6T`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.11258",
  "prompt": "Extract all details about the DemoHLM paper: What is the full title? Who are the authors? What is the complete pipeline? How does it convert demonstrations to object-centric representations? What is the 3-stage pipeline (locomotion, pre-manipulation, manipulation)? What robot platform does it use? What are its limitations? What are the key results? How does it compare to other methods? What datasets or benchmarks does it use? What is the grammar-based or compositional task generation approach if mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b28f2056-afac-4bd2-b810-29ec0d8039b4",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
  "requestId": "req_011CauRSWnr8NCH683exUq44",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28352813-d890-4950-bf29-a44895267c01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D71w2Ax8kh1eaXnFb8BXNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1881,
      "cache_read_input_tokens": 7870,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1881
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 7870,
          "cache_creation_input_tokens": 1881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1881,
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

_source line 7 · 2026-05-10T19:14:41.058Z_

<details><summary>↩ Tool result · `toolu_01Ntz6L5Qv4rtSiXrD6NVmrY`</summary>

```text
Web search results for query: "DemoHLM humanoid loco-manipulation demonstration generation arXiv 2510.11258"

Links: [{"title":"DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2510.11258v1"},{"title":"EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration","url":"https://arxiv.org/html/2602.10106v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Sim-to-Real Learning for Humanoid Box Loco-Manipulation | Request PDF","url":"https://www.researchgate.net/publication/382977746_Sim-to-Real_Learning_for_Humanoid_Box_Loco-Manipulation"},{"title":"EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration | Request PDF","url":"https://www.researchgate.net/publication/400660604_EgoHumanoid_Unlocking_In-the-Wild_Loco-Manipulation_with_Robot-Free_Egocentric_Demonstration"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"[2507.00833v1] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/abs/2507.00833v1"},{"title":"GitHub - visualmimic/VisualMimic: [arXiv 2025] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation · GitHub","url":"https://github.com/visualmimic/VisualMimic"},{"title":"VisualMimic Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/html/2509.20322v1"}]

Based on the search results, here's information about DemoHLM (arXiv 2510.11258):

## Overview

DemoHLM is a framework for humanoid loco-manipulation that enables generalizable loco-manipulation on a real humanoid robot from a single demonstration in simulation.

## Key Problem

Loco-manipulation is a fundamental challenge for humanoid robots to achieve versatile interactions in human environments. Although recent studies have made significant progress in humanoid whole-body control, loco-manipulation remains underexplored and often relies on hard-coded task definitions or costly real-world data collection, which limits autonomy and generalization.

## Technical Approach

DemoHLM adopts a hierarchy that integrates a low-level universal whole-body controller with high-level manipulation policies for multiple tasks. The whole-body controller maps whole-body motion commands to joint torques and provides omnidirectional mobility for the humanoid robot.

For each task, DemoHLM requires only a single demonstration and automatically synthesizes hundreds to thousands of successful trajectories that complete the same task in varied environments.

## Results

Experiments show that increasing the amount of simulated data leads to substantial performance gains and improved generalization across varying initial states. Moreover, the generated data remain consistently effective across different behavior cloning algorithms, suggesting that the framework scalably produces high-quality data for different policy learning methods.

Real-world experiments on a Unitree G1 robot equipped with an RGB-D camera validate the sim-to-real transferability of DemoHLM, demonstrating robust performance under spatial variations across ten loco-manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b28f2056-afac-4bd2-b810-29ec0d8039b4",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a631f7163574985c8",
  "type": "user",
  "uuid": "36ee356f-0ece-41bc-9e09-d93a962c1250",
  "sourceToolAssistantUUID": "b28f2056-afac-4bd2-b810-29ec0d8039b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T19:14:41.369Z_

<details><summary>↩ Tool result · `toolu_01BfsCeWX7jxjYNStrQgvg6T`</summary>

```text
# DemoHLM Paper Summary

**Full Title:** "DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation"

**Authors:** Yuhui Fu, Feiyang Xie, Chaoyi Xu, Jing Xiong, Haoqi Yuan, and Zongqing Lu

## Key Framework Components

The system employs a hierarchical architecture combining two main elements: a "low-level universal whole-body controller" that converts motion commands to joint torques while enabling omnidirectional movement, plus high-level manipulation policies trained through simulation-based imitation learning.

## Pipeline Overview

Policies are "learned in simulation via data generation and imitation learning," then command the whole-body controller using visual feedback from an RGB-D camera to perform loco-manipulation tasks.

## Robot Platform

The research validates findings on a **Unitree G1 robot** equipped with an RGB-D camera.

## Key Results

The research demonstrates "a positive correlation between the amount of synthetic data and policy performance," indicating effective data generation and efficient learning. Real-world testing shows "robust performance under spatial variations across ten loco-manipulation tasks."

## Information Not Provided

The webpage content does not detail:
- Specific three-stage pipeline breakdown
- Object-centric representation conversion methods
- Comparisons with other approaches
- Dataset or benchmark specifications
- Grammar-based task generation approaches
- Detailed limitations

Access the full paper via PDF or HTML for comprehensive technical details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28352813-d890-4950-bf29-a44895267c01",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a631f7163574985c8",
  "type": "user",
  "uuid": "9841dfd1-9623-4dab-904b-c9c286953bfd",
  "sourceToolAssistantUUID": "28352813-d890-4950-bf29-a44895267c01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T19:14:44.485Z_

Let me fetch the full HTML version of the paper for more technical details about the pipeline stages and methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9841dfd1-9623-4dab-904b-c9c286953bfd",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
  "requestId": "req_011CauRTJYRgTXSGaGooD4Hn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "151ca4b6-98c3-49fb-884a-4e5fa7729a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ANA5YF468tYpTdHKXSdZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1670,
      "cache_read_input_tokens": 9751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1670,
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

_source line 10 · 2026-05-10T19:14:47.133Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VJyQFByE5tEzH5Vq8tQ9tN`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.11258v1",
  "prompt": "Extract detailed information about: 1) The complete 3-stage pipeline (locomotion, pre-manipulation, manipulation) - how each stage works. 2) How demonstrations are converted to object-centric representations. 3) The data generation process from a single demonstration. 4) What is the whole-body controller architecture? 5) What are the specific limitations mentioned? 6) How does it compare to other methods like grammar-based compositional task generation or other baselines? 7) What are the specific tasks tested? 8) What metrics are used for evaluation? 9) Any details about the randomization or augmentation strategy."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "151ca4b6-98c3-49fb-884a-4e5fa7729a92",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
  "requestId": "req_011CauRTJYRgTXSGaGooD4Hn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "829b9ff0-b06b-44b6-aaab-257c974b0f47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ANA5YF468tYpTdHKXSdZQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1670,
      "cache_read_input_tokens": 9751,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1670
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 9751,
          "cache_creation_input_tokens": 1670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1670,
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

_source line 11 · 2026-05-10T19:14:59.789Z_

<details><summary>↩ Tool result · `toolu_01VJyQFByE5tEzH5Vq8tQ9tN`</summary>

```text
# DemoHLM Framework Analysis

## 1) Three-Stage Pipeline

**Locomotion Stage**: Uses a PD controller to generate velocity commands (vx, vy, ωyaw) that guide the robot's root to reach a suitable starting position. The stage concludes when distance and rotation thresholds are met.

**Pre-Manipulation Stage**: Based on object-centric trajectories, the system "defines target end-effector poses as: T^eef = Tobjeef T¯obj" to ensure similar effects under different conditions. An interpolation trajectory bridges any discrepancies between current and target end-effector poses.

**Manipulation Stage**: Switches from object-centric to proprioception-centric poses, defined as "T^eef = T¯eef(Tproeef)−1" to handle tasks where end-effectors remain largely stationary relative to objects.

## 2) Object-Centric Representation Conversion

The human demonstration is split at first contact time into two segments. The transformation involves:
- **Object-centric phase**: Converts end-effector poses relative to object using "Tobjef = Teef(T¯obj)−1"
- **Proprioception-centric phase**: Transforms using "Tproeef = Teef(T̄eef)tc−1"

These are concatenated to create relative pose trajectories for replay.

## 3) Data Generation Process

From a single VR-captured demonstration, the system generates hundreds to thousands of trajectories by:
- Converting the demonstration into object-centric end-effector poses
- Modifying high-level commands for arbitrary initial robot and object poses
- Replaying through the whole-body controller in simulation
- Collecting proprioceptive feedback, object poses, and actions

## 4) Whole-Body Controller Architecture

The controller "takes as input a set of desired motion parameters (vx, vy, ω, h, r, p, y, 𝐪upper)" where vx/vy represent linear velocities, ω is yaw rate, (h,r,p,y) specifies torso configuration, and 𝐪upper are upper-body joint targets. The controller outputs target joint positions tracked via PD control at 50 Hz.

## 5) Specific Limitations

The authors acknowledge: reliance on "simulation-generated data, which can hinder the performance on the real robot due to the sim-to-real gap"; "using a single RGB-D camera may also constrain performance in cluttered or occluded scenes"; and "using FoundationPose to provide object 6D poses limits the manipulation of unmodeled objects."

## 6) Comparison to Other Methods

DemoHLM differs from prior work by avoiding "task-specific designs such as predefined subtask decompositions" used in RL approaches, and reducing reliance on "large amounts of real-world teleoperation data" required by some whole-body control methods. No direct grammar-based compositional comparisons are provided.

## 7) Tasks Tested

**Rubber-hand tasks** (4): LiftBox, PressCube, PushCube, Handover

**Gripper tasks** (6): GraspCube, OpenCabinet, PushCart, EraseBoard, PourWater, ExchangeCube

## 8) Evaluation Metrics

Success rates measured on 5,000 rollouts per task using three independent random seeds. Real-world evaluation used 5 trials per task. Data generation success rates reported separately to account for IK solving failures.

## 9) Randomization Strategy

Initial regions (R1-R3) define randomization ranges: robot x, y coordinates and yaw orientation; object y, z coordinates and z-direction rotation. Larger regions (R3 default) introduce greater variability, though success rates decline as randomization expands.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "829b9ff0-b06b-44b6-aaab-257c974b0f47",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a631f7163574985c8",
  "type": "user",
  "uuid": "00b13a58-c80a-4409-8a2b-758e8c5c0fc1",
  "sourceToolAssistantUUID": "829b9ff0-b06b-44b6-aaab-257c974b0f47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T19:15:02.960Z_

Now let me search for more information about how DemoHLM compares to grammar-based compositional task generation approaches specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00b13a58-c80a-4409-8a2b-758e8c5c0fc1",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
  "requestId": "req_011CauRUfQ5dQ7YiR4JqeKGe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a91e4287-b79d-4a6c-b5a4-13f1a7d08621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FY53PBSeDFmDxi5MvmGKtB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 11421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
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

_source line 13 · 2026-05-10T19:15:03.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ww6NR4fvGYAZboNRv1DMy`</summary>

```json
{
  "query": "DemoHLM comparison grammar-based compositional task generation humanoid manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a91e4287-b79d-4a6c-b5a4-13f1a7d08621",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
  "requestId": "req_011CauRUfQ5dQ7YiR4JqeKGe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b0bcfa0-56d4-4d9b-bc96-c5f9ed09ab7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FY53PBSeDFmDxi5MvmGKtB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 11421,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1143
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 11421,
          "cache_creation_input_tokens": 1143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1143,
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

_source line 14 · 2026-05-10T19:15:14.783Z_

<details><summary>↩ Tool result · `toolu_018ww6NR4fvGYAZboNRv1DMy`</summary>

```text
Web search results for query: "DemoHLM comparison grammar-based compositional task generation humanoid manipulation 2025"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2510.11258v1"},{"title":"1 A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://www.techrxiv.org/users/935947/articles/1356038/master/file/data/A%20Step%20Toward%20World%20Models2/A%20Step%20Toward%20World%20Models2.pdf?inline=true"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"GitHub - BaiShuanghao/Awesome-Robotics-Manipulation: A comprehensive list of papers about Robot Manipulation, including papers, codes, and related websites. · GitHub","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation"},{"title":"Manipulation and Task Execution by Humanoids | Request PDF","url":"https://www.researchgate.net/publication/338740271_Manipulation_and_Task_Execution_by_Humanoids"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v2"},{"title":"Published as a conference paper at ICLR 2025 COMBO: COMPOSITIONAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7d03c6bf9f07acb4038eea96c63db52d-Paper-Conference.pdf"},{"title":"DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning","url":"https://arxiv.org/html/2502.16932v1"},{"title":"arXiv:2506.13751v2 [cs.RO] 19 Jun 2025 LeVERB: Humanoid Whole-Body Control","url":"https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf"}]

Based on the search results, I found information about DemoHLM and related research in humanoid manipulation. Here are the key findings:

## DemoHLM Overview

DemoHLM is a 2025 paper titled "From One Demonstration to Generalizable Humanoid Loco-Manipulation" that addresses learning manipulation skills for humanoid robots from minimal data.

## Key Capabilities

The manipulation policies, learned in simulation via a data generation and imitation learning pipeline, command the whole-body controller with closed-loop visual feedback to execute challenging loco-manipulation tasks. Experiments show a positive correlation between the amount of synthetic data and policy performance, underscoring the effectiveness of the data generation pipeline and the data efficiency of the approach.

## Real-World Validation

Real-world experiments on a Unitree G1 robot equipped with an RGB-D camera validate the sim-to-real transferability of DemoHLM, demonstrating robust performance under spatial variations across ten loco-manipulation tasks.

## Related Work in Compositional Task Generation

The search results also revealed broader research on compositional approaches in robotics. Compositional approaches decompose high-level instructions into sets of lower-level primitives and compositionally synthesize video plans on unseen goals for robot manipulation tasks, with some work learning compositional world models for multi-agent cooperation to enable accurate simulation of multiple sets of actions on the world.

The DemoHLM paper represents a significant advancement in enabling humanoid robots to learn complex manipulation skills from minimal demonstrations through synthetic data generation and sim-to-real transfer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b0bcfa0-56d4-4d9b-bc96-c5f9ed09ab7b",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a631f7163574985c8",
  "type": "user",
  "uuid": "97757eff-bd60-4e98-83a2-37b7e4db46e9",
  "sourceToolAssistantUUID": "4b0bcfa0-56d4-4d9b-bc96-c5f9ed09ab7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T19:15:18.033Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014tH9dUzoXyjmudHVtWH3Ap`</summary>

```json
{
  "query": "\"DemoHLM\" baseline comparison ACT diffusion policy behavior cloning ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97757eff-bd60-4e98-83a2-37b7e4db46e9",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
  "requestId": "req_011CauRVmPmEMVkWPLNQA6cj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01c43a27-cfbb-4148-961d-698da19c45fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DYUdkYHyRttcyoHNYAx4hL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 12564,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 12564,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1121,
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

_source line 16 · 2026-05-10T19:15:24.031Z_

<details><summary>↩ Tool result · `toolu_014tH9dUzoXyjmudHVtWH3Ap`</summary>

```text
Web search results for query: ""DemoHLM" baseline comparison ACT diffusion policy behavior cloning ablation"

Links: [{"title":"Ch. 21 - Imitation Learning - Underactuated Robotics","url":"https://underactuated.mit.edu/imitation.html"},{"title":"[2302.13335] Diffusion Model-Augmented Behavioral Cloning","url":"https://arxiv.org/abs/2302.13335"},{"title":"DiffClone: Enhanced Behaviour Cloning in Robotics with ...","url":"https://arxiv.org/pdf/2401.09243"},{"title":"Diffusion Model-Augmented Behavioral Cloning","url":"https://sites.google.com/view/diffusion-behavioral-cloning"},{"title":"Diffusion Model-Augmented Behavioral Cloning","url":"https://arxiv.org/html/2302.13335v4"},{"title":"Diffusion Model-Augmented Behavioral Cloning | OpenReview","url":"https://openreview.net/forum?id=0HIMHjYhYe"},{"title":"Residual Off-Policy RL for Finetuning Behavior Cloning Policies","url":"https://residual-offpolicy-rl.github.io/"},{"title":"Diffusion model-augmented behavioral cloning | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692361"},{"title":"(PDF) Diffusion Model-Augmented Behavioral Cloning","url":"https://www.researchgate.net/publication/368842602_Diffusion_Model-Augmented_Behavioral_Cloning"},{"title":"DiffClone: Enhanced Behaviour Cloning in Robotics with Diffusion-Driven Policy Learning","url":"https://arxiv.org/html/2401.09243v2"}]

Based on the search results, I found relevant information about diffusion policies, behavior cloning, and related approaches in robotics. However, I did not find specific information about "DemoHLM" in these results. The search returned information about related techniques and methods:

**Key findings from the search:**

Action-chunking transformers (ACT) used Conditional Variational Autoencoders (CVAE) and Diffusion Policy used Diffusion models as approaches for imitation learning.

Both the ACT paper and the Diffusion Policy paper strongly emphasized predicting an entire sequence of future actions, operating in a fashion similar to model-predictive control.

Regarding diffusion-based approaches compared to behavior cloning: Diffusion Model-Augmented Behavioral Cloning (DBC) employs a diffusion model trained to model expert behaviors and learns a policy to optimize both the BC loss (conditional) and a proposed diffusion model loss (joint), with DBC outperforming baselines in various continuous control tasks in navigation, robot arm manipulation, dexterous manipulation, and locomotion.

However, the search results do not contain specific information about "DemoHLM" or its baseline comparisons. If you're looking for information about a specific paper or method called DemoHLM, you may want to search with a more specific paper title or author information, as this particular term does not appear in the current search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01c43a27-cfbb-4148-961d-698da19c45fa",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a631f7163574985c8",
  "type": "user",
  "uuid": "9ee770b0-585d-4297-b951-5fc9a969176a",
  "sourceToolAssistantUUID": "01c43a27-cfbb-4148-961d-698da19c45fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T19:15:31.521Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TKzkfuxDLje8oRH7CxTWpF`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.11258v1",
  "prompt": "Focus on extracting: 1) The experimental results and ablation studies - what behavior cloning algorithms were tested (ACT, Diffusion Policy, etc.)? What were the success rates? 2) How does the data generation scale - what happens with more data? 3) What are the specific baselines compared against? 4) Any mention of grammar-based approaches, compositional generation, or related work that uses task grammars? 5) The full related work section - what methods does DemoHLM differentiate itself from? 6) Details about the VR teleoperation setup for the single demonstration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ee770b0-585d-4297-b951-5fc9a969176a",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
  "requestId": "req_011CauRWT5DwGrcacXfUNLkK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "402969c5-7a47-4ac3-b042-4019c83c5d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZTB9KQCE5i651MR1isKp4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 883,
      "cache_read_input_tokens": 13685,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 883
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 13685,
          "cache_creation_input_tokens": 883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 883,
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

_source line 18 · 2026-05-10T19:15:38.557Z_

<details><summary>↩ Tool result · `toolu_01TKzkfuxDLje8oRH7CxTWpF`</summary>

```text
# DemoHLM: Experimental Results and Methodology Summary

## Behavior Cloning Algorithms Tested

The paper evaluated three BC architectures on identical datasets:

- **ACT** (Action Chunking Transformers)
- **Diffusion Policy**
- **MLP** with action chunking (baseline)

Results in Table 2 show ACT and Diffusion Policy achieved comparable performance, while the simpler MLP exhibited "substantial drop in success rate" across tasks, suggesting "temporally expressive BC architectures yield stronger performance."

## Data Scaling Results

Table 1 demonstrates clear positive correlation between dataset size and performance:

| Dataset Size | Performance Pattern |
|---|---|
| 100-5000 trajectories | "Success rates increase monotonically with dataset size; however, gains gradually taper off as the dataset grows, reflecting diminishing marginal returns" |

Example: LiftBox improved from 86.41% (100 samples) to 98.83% (5000 samples).

## Baseline Comparisons

Notably, **the paper contains no direct experimental comparisons against competing methods**. Instead, it relies on related work citations to position DemoHLM's contributions. The authors compare their approach against prior work conceptually rather than empirically.

## Grammar-Based or Compositional Approaches

No mention of grammar-based task generation or compositional decomposition methods exists in this paper.

## Related Work Differentiation

Key distinctions from prior work:

- Extends MimicGen (fixed-base arms) to humanoid loco-manipulation
- Avoids task-specific reward functions unlike WoCoCo and prior RL approaches
- Transfers zero-shot to real robots (unlike SMPL-based methods)
- Requires only single demonstrations, unlike teleoperation-heavy approaches

## VR Teleoperation Details

"An Apple Vision Pro serves as the motion-capture device, using VisionProTeleop to stream head and wrist poses, which are mapped to the corresponding head and wrist links of the Unitree G1." Lower-body DoFs remain fixed during collection. Multi-task inverse kinematics (Pink library) solves for target commands.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "402969c5-7a47-4ac3-b042-4019c83c5d6f",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a631f7163574985c8",
  "type": "user",
  "uuid": "f7efb96e-e3d9-42c9-98db-55f08d3b8ff4",
  "sourceToolAssistantUUID": "402969c5-7a47-4ac3-b042-4019c83c5d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T19:16:18.468Z_

I now have comprehensive information about the DemoHLM paper. Here is my detailed research report:

---

## DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation

**arXiv: 2510.11258**
**Authors:** Yuhui Fu, Feiyang Xie, Chaoyi Xu, Jing Xiong, Haoqi Yuan, and Zongqing Lu

---

### What is DemoHLM?

DemoHLM is a framework that enables a humanoid robot to learn generalizable loco-manipulation skills from a **single teleoperated demonstration** captured in simulation. From that one demo, it automatically synthesizes hundreds to thousands of diverse successful trajectories by replaying the demonstration under varied initial conditions, then trains imitation learning policies on this synthetic data that transfer zero-shot to the real world.

---

### Pipeline Overview (Hierarchical Architecture)

DemoHLM uses a **two-level hierarchy**:

1. **Low-level universal whole-body controller** -- takes motion commands (linear velocities vx/vy, yaw rate omega, torso height/roll/pitch/yaw, upper-body joint targets) and outputs joint-level PD targets at 50 Hz, providing omnidirectional locomotion.

2. **High-level manipulation policy** -- learned via behavior cloning on the generated data, using visual feedback from an RGB-D camera to produce commands for the whole-body controller.

---

### Object-Centric Representation Conversion

The key insight enabling data generation from a single demo is converting the demonstration into **object-centric relative pose trajectories**:

- The demonstration is split at the **first contact time** (tc) into two segments.
- **Before contact (object-centric phase):** End-effector poses are expressed relative to the object: `T_obj_eef = T_eef * (T_obj_bar)^{-1}`. This means the approach trajectory is defined relative to the object, so when the object moves, the end-effector trajectory adapts accordingly.
- **After contact (proprioception-centric phase):** End-effector poses are expressed relative to the end-effector's pose at the contact moment: `T_pro_eef = T_eef * (T_eef_bar)_{tc}^{-1}`. This handles the manipulation phase where the hand remains roughly fixed relative to the object.

These relative representations allow the same demonstration to be "replayed" for arbitrary initial robot and object poses.

---

### The 3-Stage Trajectory Generation Pipeline

For each new randomized initial condition, a trajectory is generated in three stages:

1. **Locomotion Stage:** A PD controller generates velocity commands (vx, vy, omega_yaw) to navigate the robot's base from its random initial pose to a suitable starting position near the object. The stage terminates when distance and rotation thresholds are met.

2. **Pre-Manipulation Stage:** Using the object-centric representation, the system computes target end-effector poses as `T_eef = T_obj_eef * T_obj_bar`. An interpolation trajectory smoothly bridges any gap between the current end-effector pose (after locomotion) and the required starting pose for manipulation. This ensures the hand is correctly positioned relative to the object regardless of approach direction.

3. **Manipulation Stage:** Switches to the proprioception-centric representation. End-effector poses are computed as `T_eef = T_eef_bar * (T_pro_eef)^{-1}`. The controller executes the actual manipulation skill (lifting, pushing, grasping, etc.).

---

### VR Teleoperation Setup

- An **Apple Vision Pro** is used as the motion capture device via the VisionProTeleop system.
- It streams head and wrist poses, which are mapped to the G1's corresponding head and wrist links.
- Lower-body degrees of freedom remain fixed during collection.
- Multi-task inverse kinematics (using the **Pink library**) solves for full-body joint targets.

---

### Robot Platform

**Unitree G1 humanoid robot** equipped with:
- An RGB-D camera for visual feedback
- Both rubber-hand and gripper end-effectors (tested across different task sets)

---

### Experimental Results

**10 loco-manipulation tasks tested:**
- Rubber-hand tasks (4): LiftBox, PressCube, PushCube, Handover
- Gripper tasks (6): GraspCube, OpenCabinet, PushCart, EraseBoard, PourWater, ExchangeCube

**Data scaling:** Success rates increase monotonically with dataset size (100 to 5000 trajectories), with diminishing returns at larger scales. Example: LiftBox went from 86.41% (100 samples) to 98.83% (5000 samples).

**Behavior cloning architectures compared:**
- **ACT** (Action Chunking Transformers) and **Diffusion Policy** achieved comparable strong performance
- **MLP** with action chunking showed substantial drops, suggesting temporally expressive architectures are important

**Randomization regions (R1-R3):** Larger spatial randomization introduces more variability but reduces data generation success rates. R3 (largest) is used by default.

**Real-world validation:** 5 trials per task on the physical Unitree G1, demonstrating robust sim-to-real transfer.

---

### Limitations (Acknowledged by Authors)

1. **Sim-to-real gap:** Reliance on simulation-generated data can hinder real robot performance due to domain differences.
2. **Limited perception:** A single RGB-D camera may constrain performance in cluttered or occluded scenes.
3. **Object pose dependence:** Using FoundationPose for 6D object pose estimation limits manipulation to pre-modeled objects only (cannot handle unmodeled/novel objects).

---

### Relationship to Grammar-Based Compositional Task Generation

The paper does **not** mention or compare against grammar-based compositional task generation approaches. DemoHLM's approach is fundamentally different from grammar-based methods:

- **Grammar-based approaches** (e.g., task and motion planning with symbolic grammars) define tasks through compositional rules and symbolic primitives, generating diverse tasks by combining grammar elements.
- **DemoHLM** instead takes a **data-driven demonstration-centric** approach -- it does not compose new tasks from primitives but rather generates diverse *instances* of the same task by varying spatial configurations. The "diversity" is in the initial conditions and object placements, not in task structure.

DemoHLM is conceptually an extension of **MimicGen** (which worked only with fixed-base robot arms) to the full humanoid loco-manipulation setting, adding the locomotion stage and handling the unique challenges of whole-body control.

---

### Key Differentiators from Prior Work

| Prior approach | DemoHLM's advantage |
|---|---|
| RL with task-specific rewards (WoCoCo, etc.) | No reward engineering needed |
| Large real-world teleoperation datasets | Only one demo required |
| MimicGen (fixed-base arms) | Handles full humanoid locomotion + manipulation |
| SMPL-based motion retargeting | Zero-shot sim-to-real transfer |
| Hard-coded task definitions | Automatically generalizes from demonstration |

---

Sources:
- [DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (HTML)](https://arxiv.org/html/2510.11258v1)
- [DemoHLM Abstract (arXiv)](https://arxiv.org/abs/2510.11258)
- [Awesome Humanoid Robot Learning (GitHub)](https://github.com/YanjieZe/awesome-humanoid-robot-learning)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7efb96e-e3d9-42c9-98db-55f08d3b8ff4",
  "isSidechain": true,
  "agentId": "a631f7163574985c8",
  "requestId": "req_011CauRXXD3EbyL973jxAgYD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c65da26a-c820-4a55-ae33-616cd7fd8b80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxQhp1HAeehwqjBxN92gbf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 14568,
      "output_tokens": 1842,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1842,
          "cache_read_input_tokens": 14568,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 716,
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
