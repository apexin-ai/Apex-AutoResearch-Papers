# Research conversation: I need to find papers that use physics signals (CoM, ZMP, centroidal momentum) for humanoid RL, to cite as validation th

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a630a8898be3c811e.jsonl`
- **Structured JSON:** [`b8f5f3ce7d422274284b.json`](../../sessions/b8/b8f5f3ce7d422274284b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-10T20:23:20.325Z_

I need to find papers that use physics signals (CoM, ZMP, centroidal momentum) for humanoid RL, to cite as validation that these signals are meaningful. The reviewer mentioned "AGILE (arXiv 2026)" but research suggests this may not be the right paper. The reviewer also mentioned "Embedding Classical Balance Control (arXiv 2026, arXiv:2603.08619)".

Search for:
1. Use WebFetch on https://arxiv.org/abs/2603.08619 to get details on "Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery"
2. Use WebSearch for "centroidal momentum humanoid reinforcement learning 2025 2026" to find other relevant papers
3. Use WebSearch for "AGILE humanoid physics CoM ZMP arXiv 2026" to try to find the specific AGILE paper the reviewer may have meant

I need: titles, authors, arXiv IDs, and what physics signals they use. Report findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "a630a8898be3c811e",
  "type": "user",
  "uuid": "8c159088-aeb0-470c-96e3-bb6dd6e6b4ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:23:20.328Z_

```json
{
  "parentUuid": "8c159088-aeb0-470c-96e3-bb6dd6e6b4ae",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
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
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "072d4f1f-7310-4f1e-b94a-a30fe7766b24",
  "timestamp": "2026-05-10T20:23:20.328Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T20:23:22.293Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011wx5wBoGkQp1zEDJv6Zdnk`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "072d4f1f-7310-4f1e-b94a-a30fe7766b24",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWgvrReRhWdYH89i2mv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b81939d2-59d3-4664-8ba2-a0aa92a91d16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015wNEZsbscsnq2D27NCMaUz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 7946,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 777
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 7946,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 777,
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

_source line 4 · 2026-05-10T20:23:22.296Z_

<details><summary>↩ Tool result · `toolu_011wx5wBoGkQp1zEDJv6Zdnk`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "b81939d2-59d3-4664-8ba2-a0aa92a91d16",
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "a630a8898be3c811e",
  "type": "user",
  "uuid": "7264087f-7f0c-4cb1-b728-22ecfd85fc93",
  "sourceToolAssistantUUID": "b81939d2-59d3-4664-8ba2-a0aa92a91d16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T20:23:24.644Z_

I'll run all three searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7264087f-7f0c-4cb1-b728-22ecfd85fc93",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWh5gFHdUg4bkaDWBTz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb103112-3be6-4e38-b4bd-369b132d0e08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011UaeLhWdQctuUURc2fr5Ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 6 · 2026-05-10T20:23:26.062Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018FRZVsJ75roQtL9ksanv6b`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.08619",
  "prompt": "Extract the full title, all authors, arXiv ID, abstract, and specifically what physics signals (CoM, ZMP, centroidal momentum, angular momentum, or other balance/physics signals) are used in this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb103112-3be6-4e38-b4bd-369b132d0e08",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWh5gFHdUg4bkaDWBTz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dd62b48-b1e8-41ad-90cc-651c68c34341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011UaeLhWdQctuUURc2fr5Ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 7 · 2026-05-10T20:23:26.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012yxE3diJWBfBacBEX7QRgM`</summary>

```json
{
  "query": "centroidal momentum humanoid reinforcement learning 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dd62b48-b1e8-41ad-90cc-651c68c34341",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWh5gFHdUg4bkaDWBTz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f369934c-27af-4a0a-887f-5dbe5b085c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011UaeLhWdQctuUURc2fr5Ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 8 · 2026-05-10T20:23:27.087Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D58rYA9iAGmgN8dXCu322M`</summary>

```json
{
  "query": "AGILE humanoid physics CoM ZMP arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f369934c-27af-4a0a-887f-5dbe5b085c82",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWh5gFHdUg4bkaDWBTz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc8e989a-514a-441e-94f0-d89e12c72646",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011UaeLhWdQctuUURc2fr5Ww",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8723,
      "output_tokens": 242,
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
          "output_tokens": 242,
          "cache_read_input_tokens": 8723,
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

_source line 9 · 2026-05-10T20:23:33.046Z_

<details><summary>↩ Tool result · `toolu_012yxE3diJWBfBacBEX7QRgM`</summary>

```text
Web search results for query: "centroidal momentum humanoid reinforcement learning 2025 2026 arXiv"

Links: [{"title":"[2507.04140] Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2507.04140"},{"title":"Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11177014/"},{"title":"Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2507.04140"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery","url":"https://arxiv.org/html/2603.08619"},{"title":"Unified Multi-Rate Model Predictive Control for a Jet-Powered Humanoid Robot","url":"https://arxiv.org/html/2505.16478"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning","url":"https://www.researchgate.net/publication/398057594_Humanoid_Whole-Body_Locomotion_on_Narrow_Terrain_via_Dynamic_Balance_and_Reinforcement_Learning"},{"title":"Whole-body control for humanoid robot locomotion | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/whole-body-control-for-humanoid-robot-locomotion-2/"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"}]

I found several relevant papers on centroidal momentum and humanoid reinforcement learning from 2025-2026. Here are the key results:

## Main Paper

The primary result is an arXiv paper titled "Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning" (arXiv 2507.04140, July 5, 2025). 

This approach employs separate actor-critic structures for the arms and legs, trained with centralized critics but decentralized actors that share only base states and centroidal angular momentum (CAM) observations, allowing each agent to specialize in task-relevant behaviors through modular reward design.

The arm agent guided by CAM tracking and damping rewards promotes arm motions that reduce overall angular momentum and vertical ground reaction moments, contributing to improved balance during locomotion or under external perturbations. The learned policy was deployed on a humanoid platform, achieving robust performance across diverse locomotion tasks, including flat-ground walking, rough terrain traversal, and stair climbing.

## Related Work

Another notable 2026 paper on centroidal momentum is "Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery," which embeds classical balance metrics including centroidal momentum as privileged critic inputs and reward shaping during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f369934c-27af-4a0a-887f-5dbe5b085c82",
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "a630a8898be3c811e",
  "type": "user",
  "uuid": "d89e03b6-e651-4451-9519-02bf9788455b",
  "sourceToolAssistantUUID": "f369934c-27af-4a0a-887f-5dbe5b085c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T20:23:33.658Z_

<details><summary>↩ Tool result · `toolu_01D58rYA9iAGmgN8dXCu322M`</summary>

```text
Web search results for query: "AGILE humanoid physics CoM ZMP arXiv 2026"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"[2502.01143] ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills","url":"https://arxiv.org/abs/2502.01143"},{"title":"Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning","url":"https://arxiv.org/html/2408.14472v1"},{"title":"AGILOped: Agile Open-Source Humanoid Robot for Research","url":"https://arxiv.org/html/2509.09364v1"},{"title":"Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic","url":"https://arxiv.org/pdf/2502.17219"},{"title":"ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills","url":"https://arxiv.org/html/2502.01143"},{"title":"Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning","url":"https://arxiv.org/html/2502.17219v1"},{"title":"AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning","url":"https://arxiv.org/html/2603.20147v1"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2208.00221"}]

Based on the search results, I found several highly relevant papers from 2026 related to AGILE, humanoid robotics, physics, center of mass (CoM), and zero moment point (ZMP):

## Key Findings:

**AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning** - This paper presents the AGILE learning workflow, which appears to be a comprehensive framework for training humanoid robots. The policy deploys directly to real Unitree G1 hardware without distillation, demonstrating practical sim-to-real transfer capabilities.

## Related Physics-Based Humanoid Control Papers:

**AGILOped** - An agile humanoid robot that uses Linear Inverted Pendulum (LIP) Center of Mass (CoM) control alongside Zero Moment Point (ZMP) analysis for stable walking.

**Dynamic Balanced Humanoid Locomotion (DBHL)** - A novel whole-body locomotion algorithm that uses dynamic balance mechanisms with Zero-Moment Point (ZMP)-driven rewards for humanoid robots to traverse extreme terrains.

**ASAP: Aligning Simulation and Real-World Physics** - A framework designed to tackle dynamics mismatch and enable agile humanoid whole-body skills.

These papers all appear in 2026 arXiv preprints and address the intersection of agile humanoid control, physics-based modeling (particularly CoM and ZMP), and reinforcement learning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc8e989a-514a-441e-94f0-d89e12c72646",
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "a630a8898be3c811e",
  "type": "user",
  "uuid": "201ef297-e126-4edc-8c47-5cfe3830f584",
  "sourceToolAssistantUUID": "bc8e989a-514a-441e-94f0-d89e12c72646",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T20:23:37.839Z_

<details><summary>↩ Tool result · `toolu_018FRZVsJ75roQtL9ksanv6b`</summary>

```text
# Paper Extraction Summary

**Full Title:** Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery

**Authors:** Nehar Poddar, Stephen McCrory, Luigi Penco, Geoffrey Clark, Hakki Erhan Svil, Robert Griffin

**arXiv ID:** 2603.08619

**Physics Signals Used:**
The paper explicitly incorporates three classical balance metrics:
- **Capture point** – a foundational stability measure in bipedal control
- **Center-of-mass (CoM) state** – position and velocity information
- **Centroidal momentum** – the linear momentum of the robot's center of mass

These metrics function as "privileged critic inputs" during training, while reward shaping is "directly around these quantities," though the actor network itself relies only on proprioceptive feedback for deployment.

**Key Abstract Points:**
The approach enables a unified policy spanning "ankle and hip strategies for small disturbances, corrective stepping under large pushes, and compliant falling with multi-contact stand-up." Testing on the Unitree H1-2 simulator achieved "93.4% recovery rate across randomized initial poses." An ablation study demonstrated that removing this balance-informed structure caused "stand-up learning to fail entirely."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dd62b48-b1e8-41ad-90cc-651c68c34341",
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "a630a8898be3c811e",
  "type": "user",
  "uuid": "749f8bc7-b869-46ce-920f-802c668bda16",
  "sourceToolAssistantUUID": "7dd62b48-b1e8-41ad-90cc-651c68c34341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T20:23:39.842Z_

Good — I found the AGILE paper. Let me now fetch its details and the other relevant papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "749f8bc7-b869-46ce-920f-802c668bda16",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWiDnRz8tBhFnH9JGyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a42125c0-c095-4db1-8f0e-996f731aa6ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q3CZjdg6qRh9LXHgYL4am1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1748,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 10611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 560,
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

_source line 13 · 2026-05-10T20:23:42.126Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FKghDjrH9NyJPwRsFvmPtV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.20147",
  "prompt": "Extract the full title, all authors, arXiv ID, submission date, and specifically what physics signals are used (CoM, ZMP, centroidal momentum, angular momentum, capture point, or other balance/physics signals). Include details on how these signals are used in training or reward."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a42125c0-c095-4db1-8f0e-996f731aa6ab",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWiDnRz8tBhFnH9JGyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efdb93b9-48da-4154-adba-ba1ebd9f660b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q3CZjdg6qRh9LXHgYL4am1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1748,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 10611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 560,
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

_source line 14 · 2026-05-10T20:23:43.061Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RuCPrkndwni1Gu8AiwuKs6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.04140",
  "prompt": "Extract the full title, all authors, arXiv ID, submission date, and specifically what physics signals are used (CoM, ZMP, centroidal momentum, angular momentum, or other balance/physics signals). Include details on how centroidal angular momentum is used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efdb93b9-48da-4154-adba-ba1ebd9f660b",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWiDnRz8tBhFnH9JGyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66f476f2-2618-4368-8c49-5ec592608856",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q3CZjdg6qRh9LXHgYL4am1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1748,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 10611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 560,
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

_source line 15 · 2026-05-10T20:23:44.462Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N5pwGpK1NZcQv4uMkp9T7V`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.17219",
  "prompt": "Extract the full title, all authors, arXiv ID, submission date, and specifically what physics signals are used (CoM, ZMP, centroidal momentum, angular momentum, or other balance/physics signals). How is ZMP used in the reward or training?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66f476f2-2618-4368-8c49-5ec592608856",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWiDnRz8tBhFnH9JGyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99467345-c6fe-43e3-854a-26c16ce3488a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q3CZjdg6qRh9LXHgYL4am1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1748,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 10611,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 560
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1748,
          "output_tokens": 409,
          "cache_read_input_tokens": 10611,
          "cache_creation_input_tokens": 560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 560,
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

_source line 16 · 2026-05-10T20:23:45.905Z_

<details><summary>↩ Tool result · `toolu_01FKghDjrH9NyJPwRsFvmPtV`</summary>

```text
# AGILE Paper Summary

**Full Title:** "AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning"

**Authors:** Huihua Zhao, Rafael Cathomen, Lionel Gulich, Wei Liu, Efe Arda Ongan, Michael Lin, Shalin Jain, Soha Pouya, Yan Chang

**arXiv ID:** 2603.20147

**Submission Date:** March 20, 2026

## Physics Signals Used

The provided webpage content does not contain specific information about which physics signals (CoM, ZMP, centroidal momentum, angular momentum, capture point, or other balance/physics metrics) are employed in the training process or reward functions.

The abstract indicates the workflow addresses "humanoid behaviors" and includes stages for "interactive environment verification, reproducible training, unified evaluation," and mentions "training stabilizations and algorithmic enhancements," but it does not detail the specific physics-based signals or control approaches utilized. To obtain this information, accessing the full PDF or HTML version of the paper would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efdb93b9-48da-4154-adba-ba1ebd9f660b",
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "a630a8898be3c811e",
  "type": "user",
  "uuid": "dce0df8a-72c8-4217-9d6d-f15ecdf7de34",
  "sourceToolAssistantUUID": "efdb93b9-48da-4154-adba-ba1ebd9f660b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T20:23:48.426Z_

<details><summary>↩ Tool result · `toolu_01RuCPrkndwni1Gu8AiwuKs6`</summary>

```text
# Paper Details

**Full Title:** Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning

**Authors:** Ho Jae Lee, Se Hwan Jeon, Sangbae Kim

**arXiv ID:** 2507.04140

**Submission Date:** July 5, 2025

---

## Physics Signals Used

The research employs **centroidal angular momentum (CAM)** as its primary physics signal. According to the abstract, the framework features "decentralized actors that share only base states and centroidal angular momentum observations."

**How CAM is Used:**

The arm agent receives specific guidance through CAM-based rewards. The system uses "CAM tracking and damping rewards" that "promote arm motions that reduce overall angular momentum and vertical ground reaction moments." This approach enables the robot to maintain balance during locomotion and when responding to external disturbances.

The methodology reflects a biomimetic principle: "Humans naturally swing their arms during locomotion to regulate whole-body dynamics, reduce angular momentum, and help maintain balance," which inspired this limb-level control approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66f476f2-2618-4368-8c49-5ec592608856",
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "a630a8898be3c811e",
  "type": "user",
  "uuid": "8336427f-0753-4877-bd02-f5efb5ddbc3d",
  "sourceToolAssistantUUID": "66f476f2-2618-4368-8c49-5ec592608856",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T20:23:49.370Z_

<details><summary>↩ Tool result · `toolu_01N5pwGpK1NZcQv4uMkp9T7V`</summary>

```text
# Paper Summary

**Full Title:** Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning

**Authors:** Weiji Xie, Chenjia Bai, Jiyuan Shi, Junkai Yang, Yunfei Ge, Weinan Zhang, Xuelong Li

**arXiv ID:** 2502.17219

**Submission Date:** February 24, 2025 (revised February 28, 2025)

## Physics Signals Used

The paper employs **Zero-Moment Point (ZMP)** as its primary balance mechanism. According to the abstract, the authors introduce "a dynamic balance mechanism by leveraging an extended measure of Zero-Moment Point (ZMP)-driven rewards" within their whole-body actor-critic framework.

## ZMP Implementation in Training

The ZMP-driven rewards are integrated into the reinforcement learning approach alongside "task-driven rewards" to enable coordinated actions across the robot's upper and lower limbs. However, the document provided does not contain detailed technical specifications regarding the specific formulation of how ZMP is computed or its exact mathematical representation in the reward function. The methodology focuses on using ZMP measures to achieve robust locomotion on narrow terrains without external perception, relying solely on proprioceptive feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99467345-c6fe-43e3-854a-26c16ce3488a",
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "a630a8898be3c811e",
  "type": "user",
  "uuid": "d20b5c41-dbca-4918-80c6-3c891b9ccfd1",
  "sourceToolAssistantUUID": "99467345-c6fe-43e3-854a-26c16ce3488a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T20:23:52.079Z_

The AGILE paper (2603.20147) abstract didn't reveal physics signals — let me fetch its full HTML for more detail, and also do a more targeted search for any other AGILE 2026 paper that might more directly match the reviewer's reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d20b5c41-dbca-4918-80c6-3c891b9ccfd1",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWj54LiRxMufiqJoPSs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad0ef291-73b7-4d65-92e2-e8fde1714d37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018zgzM7vTgjXXwYvL9ZGWXt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3030,
      "cache_read_input_tokens": 11171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3030,
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

_source line 20 · 2026-05-10T20:23:53.524Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016WzcJ5sKaPTCXUMMs9uJzf`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.20147v1",
  "prompt": "What physics signals does this paper use? Specifically look for: Center of Mass (CoM), Zero Moment Point (ZMP), centroidal momentum, angular momentum, capture point, linear inverted pendulum. How are these used in the reward function, critic inputs, or training process?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad0ef291-73b7-4d65-92e2-e8fde1714d37",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWj54LiRxMufiqJoPSs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9551c5d5-2545-49f3-95ad-89180396ffad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018zgzM7vTgjXXwYvL9ZGWXt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3030,
      "cache_read_input_tokens": 11171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3030,
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

_source line 21 · 2026-05-10T20:23:53.958Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014dShT3tLJwGyUJ1hcifc43`</summary>

```json
{
  "query": "AGILE humanoid reinforcement learning CoM centroidal momentum ZMP reward 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9551c5d5-2545-49f3-95ad-89180396ffad",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWj54LiRxMufiqJoPSs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d701cf6-c83b-4d72-92b8-f033cfbce4bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018zgzM7vTgjXXwYvL9ZGWXt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3030,
      "cache_read_input_tokens": 11171,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 11171,
          "cache_creation_input_tokens": 3030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3030,
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

_source line 22 · 2026-05-10T20:24:02.094Z_

<details><summary>↩ Tool result · `toolu_014dShT3tLJwGyUJ1hcifc43`</summary>

```text
Web search results for query: "AGILE humanoid reinforcement learning CoM centroidal momentum ZMP reward 2026 arXiv"

Links: [{"title":"[2507.04140] Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2507.04140"},{"title":"Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2507.04140"},{"title":"Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning","url":"https://arxiv.org/html/2502.17219v1"},{"title":"Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11177014/"},{"title":"Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic","url":"https://arxiv.org/pdf/2502.17219"},{"title":"Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery","url":"https://arxiv.org/html/2603.08619"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning","url":"https://arxiv.org/html/2408.14472v1"},{"title":"RL-augmented MPC Framework for Agile and Robust Bipedal Footstep","url":"https://arxiv.org/pdf/2407.17683"}]

I found several relevant research papers on humanoid robot control using reinforcement learning with concepts related to centroidal momentum, center of mass (CoM), and Zero Moment Point (ZMP). Here are the key results:

## Primary Results:

1. **"Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning"** (arXiv 2507.04140, July 2025)
   - Presents a limb-level multi-agent reinforcement learning framework that enables coordinated whole-body control of humanoid robots through emergent arm motion, with separate actor-critic structures for the arms and legs trained with centralized critics but decentralized actors that share only base states and centroidal angular momentum observations.
   - The arm agent guided by centroidal angular momentum tracking and damping rewards promotes arm motions that reduce overall angular momentum and vertical ground reaction moments.

2. **"Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning"** (arXiv 2502.17219, February 2025)
   - Designs a reward function for the RL policy that encourages the ZMP coordinates to be close to the center of the humanoid's support polygon, calculated using privileged information obtained from simulations, while the policy is learned solely based on proprioception via an asymmetric actor-critic framework.

3. **"Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery"** (arXiv 2603.08619, March 2026)
   - Presents a unified RL policy that embeds classical balance metrics—capture point, center-of-mass state, and centroidal momentum—as privileged critic inputs and shapes rewards directly around these quantities during training.

These papers directly address the topics you searched for: humanoid robotics, reinforcement learning, CoM/centroidal dynamics, and ZMP-based rewards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d701cf6-c83b-4d72-92b8-f033cfbce4bb",
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "a630a8898be3c811e",
  "type": "user",
  "uuid": "59806419-997f-495b-8586-24347372e9f8",
  "sourceToolAssistantUUID": "6d701cf6-c83b-4d72-92b8-f033cfbce4bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T20:24:04.689Z_

<details><summary>↩ Tool result · `toolu_016WzcJ5sKaPTCXUMMs9uJzf`</summary>

```text
# Physics Signals Analysis: AGILE Paper

Based on the provided content, **the paper does not explicitly employ Center of Mass (CoM), Zero Moment Point (ZMP), centroidal momentum, angular momentum, capture point, or linear inverted pendulum models**.

## What the Paper Actually Uses

The framework relies on **proprioceptive observations** rather than advanced momentum-based physics signals:

- **Observation spaces** include "noisy" joint states, with critics receiving additional information like "scans" (terrain), "vel" (velocity), "ht" (height), and "forces"
- The reward structure focuses on **task-level tracking** (velocity commands, height maintenance) and **style/regularization** components, not momentum stability metrics
- Motion quality is assessed through **joint-level diagnostics**: "RMS acceleration, jerk, and joint-limit violations"

## Training Approach Instead

Rather than physics-based stability constraints, AGILE stabilizes learning through:

1. **Virtual harness**: External PD forces on root body orientation and height during early training
2. **L2C2 regularization**: Enforces smooth observation-to-action mappings via Lipschitz continuity
3. **Domain randomization**: Randomizes dynamics, mass, contact parameters, and actuator delays

The framework prioritizes **smooth, hardware-safe control** over theoretically grounded momentum-based stability, achieving sim-to-real transfer through empirical regularization rather than physics-informed signal shaping.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9551c5d5-2545-49f3-95ad-89180396ffad",
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "a630a8898be3c811e",
  "type": "user",
  "uuid": "00045e81-29c1-459a-8993-4885226a6e9f",
  "sourceToolAssistantUUID": "9551c5d5-2545-49f3-95ad-89180396ffad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T20:24:28.842Z_

Here is a complete summary of all findings:

---

## Paper 1: Confirmed — arXiv:2603.08619

**Title:** Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery

**Authors:** Nehar Poddar, Stephen McCrory, Luigi Penco, Geoffrey Clark, Hakki Erhan Svil, Robert Griffin

**arXiv ID:** 2603.08619 (March 2026)

**Physics signals used:**
- Center of Mass (CoM) — position and velocity as privileged critic inputs
- Centroidal momentum — as a privileged critic input and reward shaping signal
- Capture point — as a privileged critic input and reward shaping signal

These are embedded as privileged inputs to the critic during asymmetric actor-critic training, with rewards shaped directly around these quantities. The actor uses only proprioception at deployment. The ablation found that removing the balance-informed structure caused stand-up learning to fail entirely. Tested on Unitree H1-2 (93.4% recovery rate).

---

## Paper 2: AGILE — arXiv:2603.20147

**Title:** AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning

**Authors:** Huihua Zhao, Rafael Cathomen, Lionel Gulich, Wei Liu, Efe Arda Ongan, Michael Lin, Shalin Jain, Soha Pouya, Yan Chang

**arXiv ID:** 2603.20147 (March 26, 2026)

**Physics signals used:** None of the classical physics signals (CoM, ZMP, centroidal momentum, capture point) appear in this paper. It uses proprioceptive observations, task-level tracking rewards, a virtual harness for early training, and L2C2 (Lipschitz continuity) regularization for stability. This is almost certainly NOT the paper the reviewer meant when citing a physics-signal-based approach — the reviewer's citation of AGILE for physics signals appears to be a misattribution.

---

## Paper 3: Centroidal Momentum RL — arXiv:2507.04140

**Title:** Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning

**Authors:** Ho Jae Lee, Se Hwan Jeon, Sangbae Kim (MIT)

**arXiv ID:** 2507.04140 (July 2025)

**Physics signals used:**
- Centroidal angular momentum (CAM) — shared as an observation between arm and leg agents; used in CAM tracking and CAM damping reward terms to reduce whole-body angular momentum and stabilize locomotion

Published in IEEE as well. Demonstrates real hardware deployment across flat ground, rough terrain, and stair climbing.

---

## Paper 4: ZMP-Driven RL — arXiv:2502.17219

**Title:** Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning

**Authors:** Weiji Xie, Chenjia Bai, Jiyuan Shi, Junkai Yang, Yunfei Ge, Weinan Zhang, Xuelong Li

**arXiv ID:** 2502.17219 (February 2025)

**Physics signals used:**
- Zero Moment Point (ZMP) — ZMP coordinates used as privileged information from simulation to compute reward; the reward encourages ZMP to remain within the support polygon. Actor uses only proprioception (asymmetric actor-critic).

---

## Key Conclusions

1. **arXiv:2603.08619** is confirmed and is the strongest citation for using CoM, centroidal momentum, and capture point as privileged RL signals.

2. **The reviewer's "AGILE (arXiv 2026)" citation for physics signals is likely wrong.** AGILE (2603.20147) does not use CoM/ZMP/centroidal momentum. The reviewer may have confused it with 2603.08619 or another paper.

3. For additional citations validating physics signals in humanoid RL, the two strongest supporting papers are:
   - **2507.04140** — centroidal angular momentum as critic observation and reward (2025)
   - **2502.17219** — ZMP as privileged reward signal (2025)

Sources:
- [Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery](https://arxiv.org/abs/2603.08619)
- [AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning](https://arxiv.org/abs/2603.20147)
- [Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2507.04140)
- [Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning](https://arxiv.org/abs/2502.17219)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00045e81-29c1-459a-8993-4885226a6e9f",
  "isSidechain": true,
  "agentId": "a630a8898be3c811e",
  "requestId": "req_011CauWkCbJM1bDzisHQ12WB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc8bb37a-d612-4976-92b6-f75ca36764c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ANQELWxCE6E45rio8zv8sE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 14201,
      "output_tokens": 1187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 623
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1002,
          "output_tokens": 1187,
          "cache_read_input_tokens": 14201,
          "cache_creation_input_tokens": 623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 623,
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
