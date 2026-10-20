# Research conversation: Search for recent papers (2025-2026) on these topics to identify work that may compete with or be missed by a proposal a

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a2e7adaff6e2bf617.jsonl`
- **Structured JSON:** [`e2c62fc677397e9bef06.json`](../../sessions/e2/e2c62fc677397e9bef06.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-10T13:07:24.165Z_

Search for recent papers (2025-2026) on these topics to identify work that may compete with or be missed by a proposal about "URDF-DiT: full-body kinematic conditioning in video diffusion models for humanoid robot training data generation":

1. Search "humanoid robot video generation synthetic data 2026" on arxiv
2. Search "ControlNet URDF robot video diffusion 2025 2026" on arxiv
3. Search "inverse dynamics model robot video generation 2026" 
4. Search "kinematic conditioning video diffusion robot manipulation 2026"
5. Search "whole body humanoid data generation loco-manipulation 2026"
6. Search "action-conditioned video generation robot training data 2026"
7. Search "BridgeV2W ControlNet robot video" - this is a key paper I need verified

For each search, report the actual papers found with their arXiv IDs, titles, and whether they represent concurrent/competing work to a system that:
- Conditions video diffusion on URDF forward kinematics (29 DoF humanoid)
- Uses ControlNet-style injection into Wan 2.2 DiT cross-attention
- Generates synthetic training data for humanoid IDM/policy training
- Targets whole-body locomanipulation tasks

Be specific about what you find - I need to know if BridgeV2W (arXiv:2602.03793) actually exists and what it does.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "ae6ba40a-337c-4ff8-87c5-a1bdf9041d33",
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

_source line 2 · 2026-05-10T13:07:25.534Z_

I'll search arXiv for these recent papers to help you identify competing or related work. Let me conduct these searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae6ba40a-337c-4ff8-87c5-a1bdf9041d33",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwSr6waas92PjtCyhHs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9a5a0ed-15a7-43c8-87d2-c0e6b6862c9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015iBWHmHPWiQtp8o94573Y1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
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

_source line 3 · 2026-05-10T13:07:25.536Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UAZ6on7khkCaePGD11qRsE`</summary>

```json
{
  "query": "humanoid robot video generation synthetic data 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9a5a0ed-15a7-43c8-87d2-c0e6b6862c9b",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwSr6waas92PjtCyhHs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0bd40416-d445-46d9-83e7-cec8dd1837a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015iBWHmHPWiQtp8o94573Y1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
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

_source line 4 · 2026-05-10T13:07:25.753Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019m3ETAqcLVPPEDKg6svi22`</summary>

```json
{
  "query": "ControlNet URDF robot video diffusion 2025 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bd40416-d445-46d9-83e7-cec8dd1837a2",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwSr6waas92PjtCyhHs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6551c2d6-7c73-4984-9bf1-aa0a798842b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015iBWHmHPWiQtp8o94573Y1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
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

_source line 5 · 2026-05-10T13:07:26.008Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DyG5BQAwQriKP1zCFnNQhu`</summary>

```json
{
  "query": "inverse dynamics model robot video generation 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6551c2d6-7c73-4984-9bf1-aa0a798842b1",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwSr6waas92PjtCyhHs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "97e4bb33-9938-45a8-bf88-395c4fa874a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015iBWHmHPWiQtp8o94573Y1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
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

_source line 6 · 2026-05-10T13:07:26.158Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012qsePMRcfbW2uD84Ep9Y3b`</summary>

```json
{
  "query": "kinematic conditioning video diffusion robot manipulation 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97e4bb33-9938-45a8-bf88-395c4fa874a2",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwSr6waas92PjtCyhHs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "14ddb4e1-d973-4914-bde0-51b603517d7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015iBWHmHPWiQtp8o94573Y1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
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

_source line 7 · 2026-05-10T13:07:26.540Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P4Hdc87K8bwNNQbJqFqgVZ`</summary>

```json
{
  "query": "whole body humanoid data generation loco-manipulation 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14ddb4e1-d973-4914-bde0-51b603517d7e",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwSr6waas92PjtCyhHs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b792421-c374-4b5b-82b9-1ff5ca9fb1f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015iBWHmHPWiQtp8o94573Y1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
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

_source line 8 · 2026-05-10T13:07:26.733Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019JsDm9boHf9QTmqr5RwNfo`</summary>

```json
{
  "query": "action-conditioned video generation robot training data 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b792421-c374-4b5b-82b9-1ff5ca9fb1f9",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwSr6waas92PjtCyhHs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6c708caf-bc82-4ce9-8bae-9bd355fa1290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015iBWHmHPWiQtp8o94573Y1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 413,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 762,
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

_source line 9 · 2026-05-10T13:07:26.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017RdMtv7JdTuNb4qTAQVuqx`</summary>

```json
{
  "query": "BridgeV2W ControlNet robot video site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c708caf-bc82-4ce9-8bae-9bd355fa1290",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwSr6waas92PjtCyhHs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "164779cb-e430-41f2-8e69-4a72938a8ee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015iBWHmHPWiQtp8o94573Y1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 413,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 762,
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

_source line 10 · 2026-05-10T13:07:31.863Z_

<details><summary>↩ Tool result · `toolu_017RdMtv7JdTuNb4qTAQVuqx`</summary>

```text
Web search results for query: "BridgeV2W ControlNet robot video site:arxiv.org"

Links: [{"title":"[2602.03793] BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks","url":"https://arxiv.org/abs/2602.03793"},{"title":"[2602.03793v1] BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks","url":"https://arxiv.org/abs/2602.03793v1"},{"title":"This&That: Language-Gesture Controlled Video Generation for Robot Planning","url":"https://arxiv.org/html/2407.05530"},{"title":"LongVie 2: Multimodal Controllable Ultra-Long Video World Model","url":"https://arxiv.org/html/2512.13604"},{"title":"arXiv:2507.01012v1 [cs.CV] 1 Jul 2025","url":"https://arxiv.org/pdf/2507.01012"},{"title":"ControlNeXt: Powerful and Efficient Control for Image and Video Generation","url":"https://arxiv.org/html/2408.06070v3"},{"title":"[2408.06070] ControlNeXt: Powerful and Efficient Control for Image and Video Generation","url":"https://arxiv.org/abs/2408.06070"},{"title":"Zero-shot Synthetic Video Realism Enhancement via Structure-aware Denoising","url":"https://arxiv.org/html/2511.14719v1"},{"title":"[2307.14073] VideoControlNet: A Motion-Guided Video-to-Video Translation Framework by Using Diffusion Model with ControlNet","url":"https://arxiv.org/abs/2307.14073"},{"title":"ROPA: Synthetic Robot Pose Generation for RGB-D Bimanual Data Augmentation","url":"https://arxiv.org/html/2509.19454"}]

I found a paper on arXiv that matches your search query:

**BridgeV2W** converts coordinate-space actions into pixel-aligned embodiment masks rendered from the URDF and camera parameters. These masks are then injected into a pretrained video generation model via a ControlNet-style pathway, which aligns the action control signals with predicted videos, adds view-specific conditioning to accommodate camera viewpoints, and yields a unified world model architecture across embodiments.

The paper addresses the challenge that embodied world models, which leverage large-scale Internet videos or pretrained video generation models, still face key challenges including a misalignment between coordinate-space actions and pixel-space videos, sensitivity to camera viewpoint, and non-unified architectures across embodiments.

The paper was published on February 3, 2026, and is available at: https://arxiv.org/abs/2602.03793


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "164779cb-e430-41f2-8e69-4a72938a8ee7",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "00e4fa65-ea26-4f1b-ae81-743ac6b1c375",
  "sourceToolAssistantUUID": "164779cb-e430-41f2-8e69-4a72938a8ee7",
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

_source line 11 · 2026-05-10T13:07:33.195Z_

<details><summary>↩ Tool result · `toolu_012qsePMRcfbW2uD84Ep9Y3b`</summary>

```text
Web search results for query: "kinematic conditioning video diffusion robot manipulation 2026 site:arxiv.org"

Links: [{"title":"Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation","url":"https://arxiv.org/html/2512.17568"},{"title":"X-Diffusion: Training Diffusion Policies on Cross-Embodiment Human Demonstrations","url":"https://arxiv.org/html/2511.04671"},{"title":"Learning to Generate Rigid Body Interactions with Video Diffusion Models","url":"https://arxiv.org/html/2510.02284"},{"title":"Learning Diverse Robot Striking Motions with Diffusion Models and Kinematically Constrained Gradient Guidance","url":"https://arxiv.org/html/2409.15528v1"},{"title":"0.11373 0.2549 0.39216A0.16471 0.27451 0.42353n0.21961 0.2902 0.4549c0.27059 0.30588 0.48627h0.32549 0.32549 0.51765o0.37647 0.34118 0.55294r0.43137 0.36078 0.58431D0.48235 0.37647 0.61569r0.53725 0.39216 0.64706e0.58824 0.41176 0.67843a0.64314 0.42745 0.7098m\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset","url":"https://arxiv.org/html/2512.11797v1"},{"title":"DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy","url":"https://arxiv.org/html/2506.20668"},{"title":"Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt","url":"https://arxiv.org/html/2505.20795"},{"title":"Trajectory Conditioned Cross-embodiment Skill Transfer","url":"https://arxiv.org/html/2510.07773"},{"title":"Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation","url":"https://arxiv.org/html/2403.03890v1"},{"title":"Motion Before Action: Diffusing Object Motion as Manipulation Condition","url":"https://arxiv.org/html/2411.09658v1"}]

I found several recent papers on arxiv.org related to kinematic conditioning, video diffusion, and robot manipulation. Here are the key results:

## Recent Papers (2025-2026)

**Kinematics-Aware Diffusion Policy (KADP)** - This approach incorporates analytical joint-node mapping in diffusion processes to ensure generated node positions adhere to kinematic constraints, achieving higher success rates and stronger spatial generalizability for body-aware manipulation learning.

**AnchorDream** - An embodiment-aware video generation framework that anchors pretrained video diffusion models in robot motion to synthesize trajectory-consistent demonstrations, preventing hallucination while synthesizing objects and environments consistent with the robot's kinematics.

**X-Diffusion** - A framework that exploits the forward diffusion process where as noise is added to actions, low-level execution differences fade while high-level task guidance is preserved, enabling principled training of diffusion policies on cross-embodiment human demonstrations.

## Other Related Work

**TrajSkill** - A framework for trajectory-conditioned cross-embodiment skill transfer that uses sparse optical flow trajectories as an embodiment-agnostic representation bridging the morphological gap between human and robot embodiments.

**KineMask** - A framework for generating accurate object interactions using video diffusion models, providing low-level kinematic control over parameters such as object direction and speed.

These papers represent cutting-edge approaches to incorporating kinematic constraints into video diffusion models for robot manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14ddb4e1-d973-4914-bde0-51b603517d7e",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "fadea540-f941-4ae5-b974-0685c69b7b5b",
  "sourceToolAssistantUUID": "14ddb4e1-d973-4914-bde0-51b603517d7e",
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

_source line 12 · 2026-05-10T13:07:33.403Z_

<details><summary>↩ Tool result · `toolu_01UAZ6on7khkCaePGD11qRsE`</summary>

```text
Web search results for query: "humanoid robot video generation synthetic data 2026 site:arxiv.org"

Links: [{"title":"Rethinking Video Generation Model for the Embodied World","url":"https://arxiv.org/html/2601.15282v1"},{"title":"From Generated Human Videos to Physically Plausible Robot Trajectories","url":"https://arxiv.org/html/2512.05094"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis","url":"https://arxiv.org/html/2604.09330"},{"title":"X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale","url":"https://arxiv.org/html/2512.04537v1"},{"title":"[2512.05094v1] From Generated Human Videos to Physically Plausible Robot Trajectories","url":"https://arxiv.org/abs/2512.05094v1"},{"title":"FlowAct-R1: Towards Interactive Humanoid Video Generation","url":"https://arxiv.org/html/2601.10103v1"},{"title":"[2512.05094] From Generated Human Videos to Physically Plausible Robot Trajectories","url":"https://arxiv.org/abs/2512.05094"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734v1"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Video World Models","url":"https://arxiv.org/html/2505.12705"}]

I've found several recent research papers on arxiv.org related to humanoid robot video generation and synthetic data. Here are the key findings:

## Recent Research (2025-2026)

**Video Generation for Robotics:**

Video generation models offer valuable trade-offs between domain-specific data for control precision and large-scale pretraining data providing "World Knowledge", according to a survey on video generation models in robotics applications.

**Humanoid-Specific Projects:**

1. **GenMimic**: This framework enables humanoid robots to execute motions from video generation models using reinforcement learning trained with symmetry regularization, and includes a synthetic human-motion dataset (GenMimicBench) created with Wan2.1 and Cosmos-Predict2 models.

2. **X-Humanoid**: A project that created a large-scale 60+ hour "robotized" dataset by designing a novel data synthesis method using Unreal Engine to turn community resources into paired human-humanoid videos.

3. **FlowAct-R1**: An interactive humanoid video generation framework designed for real-time synthesis of lifelike visual agents that can engage with humans, built upon a MMDiT architecture enabling streaming synthesis of video with arbitrary durations.

4. **GR00T N1**: A foundation model that leverages off-the-shelf video generation models to create neural trajectories for training, combining real-robot trajectories, human videos, and synthetically generated datasets.

These papers demonstrate the growing focus on using video generation to create synthetic training data for humanoid robots in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bd40416-d445-46d9-83e7-cec8dd1837a2",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "38290d33-f121-492f-91e8-366e5cb2f252",
  "sourceToolAssistantUUID": "0bd40416-d445-46d9-83e7-cec8dd1837a2",
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

_source line 13 · 2026-05-10T13:07:34.443Z_

<details><summary>↩ Tool result · `toolu_01DyG5BQAwQriKP1zCFnNQhu`</summary>

```text
Web search results for query: "inverse dynamics model robot video generation 2026 site:arxiv.org"

Links: [{"title":"[2603.17808] EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards","url":"https://arxiv.org/abs/2603.17808"},{"title":"[2603.17808v2] EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards","url":"https://arxiv.org/abs/2603.17808v2"},{"title":"Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards","url":"https://arxiv.org/html/2603.17808"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"[2604.16391] Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining","url":"https://arxiv.org/abs/2604.16391"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998"},{"title":"VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation","url":"https://arxiv.org/html/2411.09153"},{"title":"Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control","url":"https://arxiv.org/html/2506.01943"}]

I found several recent papers on arXiv (2026) that combine inverse dynamics models with robot video generation. Here are the key results:

## EVA: Aligning Video World Models with Executable Robot Actions

EVA is a reinforcement-learning post-training framework that trains an inverse dynamics model on real robot trajectories and repurposes it as a reward model to evaluate generated videos through the action sequences they induce, encouraging smooth motions measured by velocity, acceleration, and jerk while penalizing actions that violate embodiment constraints. This paper was submitted on March 18, 2026.

## DeFI: Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining

DeFI proposes decoupling visual forward and inverse dynamics pretraining, introducing the General Forward Dynamics Model (GFDM) pretrained on diverse human and robot videos for future prediction, and the General Inverse Dynamics Model (GIDM), trained via self-supervised learning to infer latent actions from unlabeled video transitions. DeFI achieves state-of-the-art performance with an average task length of 4.51 for CALVIN and 51.2% success rate on SimplerEnv-Fractal benchmark.

## MotuBrain: An Advanced World Action Model for Robot Control

MotuBrain supports inference over five distributions: vision-language-action policy modeling, world modeling, video generation, inverse dynamics, and joint video-action prediction.

## LingBot-VA: Causal World Modeling for Robot Control

LingBot-VA is an autoregressive diffusion world model that addresses limitations through a unified video-action framework, operating in a continuous latent space via flow matching and autoregressively generating chunks of video and action representations through iterative denoising.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97e4bb33-9938-45a8-bf88-395c4fa874a2",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "74c27544-a0f3-43cb-84a2-92e6d0133c3b",
  "sourceToolAssistantUUID": "97e4bb33-9938-45a8-bf88-395c4fa874a2",
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

_source line 14 · 2026-05-10T13:07:34.559Z_

<details><summary>↩ Tool result · `toolu_01P4Hdc87K8bwNNQbJqFqgVZ`</summary>

```text
Web search results for query: "whole body humanoid data generation loco-manipulation 2026 site:arxiv.org"

Links: [{"title":"[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/html/2509.26633v2"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"[2509.26633v1] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633v1"},{"title":"Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models","url":"https://arxiv.org/html/2504.16843v1"},{"title":"Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations","url":"https://arxiv.org/html/2602.06643v2"},{"title":"Scalable and General Whole-Body Control for Cross-Humanoid Locomotion","url":"https://arxiv.org/html/2602.05791"},{"title":"DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2510.11258v1"},{"title":"VisualMimic Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/html/2509.20322v1"},{"title":"[2512.11047] WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control","url":"https://arxiv.org/abs/2512.11047"}]

I found several highly relevant research papers on arXiv about whole-body humanoid data generation for loco-manipulation. Here are the key results:

## Main Result: OmniRetarget

OmniRetarget is an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. This high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## Additional Related Papers

Several other recent papers address whole-body humanoid loco-manipulation:

1. **DemoHLM**: A framework for humanoid loco-manipulation that enables generalizable loco-manipulation on a real humanoid robot from a single demonstration in simulation.

2. **VisualMimic**: A visual sim-to-real framework that unifies egocentric vision with hierarchical whole-body control for humanoid robots, enabling zero-shot transfer of visuomotor policies trained in simulation to real humanoid robots, accomplishing loco-manipulation tasks such as box lifting, pushing, football dribbling, and kicking.

3. **WholeBodyVLA**: A unified framework for humanoid loco-manipulation that is one of its kind enabling large-space humanoid loco-manipulation.

These papers represent recent advances in data generation and control methods for humanoid whole-body loco-manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b792421-c374-4b5b-82b9-1ff5ca9fb1f9",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "f1b0cafd-cdce-415c-9e63-be3bdb9cd519",
  "sourceToolAssistantUUID": "0b792421-c374-4b5b-82b9-1ff5ca9fb1f9",
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

_source line 15 · 2026-05-10T13:07:34.999Z_

<details><summary>↩ Tool result · `toolu_019JsDm9boHf9QTmqr5RwNfo`</summary>

```text
Web search results for query: "action-conditioned video generation robot training data 2026 site:arxiv.org"

Links: [{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis","url":"https://arxiv.org/html/2604.09330"},{"title":"[2603.17808v2] EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards","url":"https://arxiv.org/abs/2603.17808v2"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Precise Action-to-Video Generation Through Visual Action Prompts Yuang Wang2∗","url":"https://arxiv.org/pdf/2508.13104"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"CoVAR: Co-generation of Video and Action for Robotic Manipulation via Multi-Modal Diffusion","url":"https://arxiv.org/html/2512.16023"},{"title":"See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations","url":"https://arxiv.org/html/2512.07582"},{"title":"[2603.17808] EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards","url":"https://arxiv.org/abs/2603.17808"}]

I've found several highly relevant papers on arXiv related to action-conditioned video generation for robot training data. Here's a summary of the key results:

## Recent Research in Action-Conditioned Video Generation for Robotics (2026)

**Video Generation Models in Robotics** Recent approaches train controllable video models using VQ-VAE and latent action models for frame-by-frame control, and diffusion/flow-matching has emerged as the dominant model architecture for training photorealistic controllable video models that can be steered using text, image, and other conditioning inputs.

**Multi-Modal Co-Generation Approaches:**
- VAG is a dual-stream generative framework designed to synthesize aligned video–action pairs conditioned on both visual observations and textual prompts, with an adaptive 3D pooling module ensuring that generated visual and motor signals are rigorously aligned at every timestep.

- MotuBrain adopts UniDiffuser to jointly model and schedule video and action, supporting five different inference distributions: vision-language-action policy modeling, world modeling, video generation, inverse dynamics, and joint video-action prediction.

**Training Data and Scaling:**
- X-WAM is pretrained on over 5,800 hours of robotic data, encompassing both real-robot and simulated datasets spanning diverse manipulation tasks.

- Unified world-action models can learn from a much broader family of multimodal data, including video-only data without action labels, interaction data without explicit task language, and heterogeneous robot trajectories collected from different embodiments.

**Executability Alignment:**
EVA trains an inverse dynamics model on real robot trajectories and repurposes it as a reward model that evaluates generated videos through the action sequences they induce.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c708caf-bc82-4ce9-8bae-9bd355fa1290",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "e5e3ee6e-128b-4ebd-a2b3-840fdb7b7e40",
  "sourceToolAssistantUUID": "6c708caf-bc82-4ce9-8bae-9bd355fa1290",
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

_source line 16 · 2026-05-10T13:07:37.317Z_

<details><summary>↩ Tool result · `toolu_019m3ETAqcLVPPEDKg6svi22`</summary>

```text
Web search results for query: "ControlNet URDF robot video diffusion 2025 2026 site:arxiv.org"

Links: [{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Vid2World: Crafting Video Diffusion Models to Interactive World Models","url":"https://arxiv.org/html/2505.14357v2"},{"title":"Vid2World: Crafting Video Diffusion Models to Interactive ...","url":"https://arxiv.org/pdf/2505.14357"},{"title":"Controllable Video Generation: A Survey","url":"https://arxiv.org/html/2507.16869v1"},{"title":"EPiC: Efficient Video Camera Control Learning with Precise Anchor-Video Guidance","url":"https://arxiv.org/html/2505.21876v1"},{"title":"[2408.13005] EasyControl: Transfer ControlNet to Video Diffusion for Controllable Generation and Interpolation","url":"https://arxiv.org/abs/2408.13005"},{"title":"Moaw: Unleashing Motion Awareness for Video Diffusion Models","url":"https://arxiv.org/html/2601.12761"},{"title":"[2408.06070] ControlNeXt: Powerful and Efficient Control for Image and Video Generation","url":"https://arxiv.org/abs/2408.06070"},{"title":"G-DReaM: Graph-conditioned Diffusion Retargeting across Multiple Embodiments","url":"https://arxiv.org/html/2505.20857"},{"title":"Motion Prompting: Controlling Video Generation with Motion Trajectories","url":"https://arxiv.org/html/2412.02700v1"}]

I found several relevant research papers from arxiv.org related to ControlNet, robot video generation, and diffusion models from 2025-2026. Here are the key results:

## Recent Papers on Robot Video Generation with Diffusion Models (2025-2026):

1. **Video Generation Models in Robotics Survey** (January 2026)
   - Discusses methods that encode motion trajectories and inject them via ControlNet and other conditioning adapters
   - Recent efforts focus on embodiment-specific video models tailored to robots, directly conditioning on robot states or actions to enable impressive controllability and physical grounding of generated videos

2. **Vid2World: Crafting Video Diffusion Models to Interactive World Models** (September 2025)
   - Employs ControlNet with the aim of incorporating action-conditioning into the diffusion process
   - Addresses world models for robotics applications through video-based approaches

3. **G-DReaM: Graph-conditioned Diffusion Retargeting across Multiple Embodiments** (May 2025)
   - Collects skeleton graph data of robots including Atlas, Talos, Cassie and Valkyrie, with all graph information parsed from their URDF files
   - This directly combines URDF robot specifications with diffusion-based motion generation

4. **Controllable Video Generation Survey** (July 2025)
   - The Unified Video Action Model (UVA) constructs a unified video and action model to support robotics applications, addressing the mismatch between temporal speed for action modeling and spatial resolution for video generation

These papers demonstrate active research into combining ControlNet, URDF specifications, video diffusion models, and robotics applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6551c2d6-7c73-4984-9bf1-aa0a798842b1",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "b862ae16-45ae-44ff-be0b-9e75780d3bbd",
  "sourceToolAssistantUUID": "6551c2d6-7c73-4984-9bf1-aa0a798842b1",
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

_source line 17 · 2026-05-10T13:07:39.206Z_

Excellent. I found comprehensive results. Let me now get the details on BridgeV2W and a few other key papers to give you the specific arXiv IDs and competitive assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b862ae16-45ae-44ff-be0b-9e75780d3bbd",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwTpKKPDpVrc1S7PBJk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "15c49166-8fa4-40b7-82b2-f1cef07a0226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HAPk8YY3REoEozWbRzv6dJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4507,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2908,
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

_source line 18 · 2026-05-10T13:07:39.845Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AxKCRoymkwRbP9xqefS17X`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03793",
  "prompt": "What is BridgeV2W? What does it do? How does it condition videos? Does it use ControlNet? What embodiments and robots does it target?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15c49166-8fa4-40b7-82b2-f1cef07a0226",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwTpKKPDpVrc1S7PBJk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7d3f77db-d6e1-47ba-b88f-9c4e969e6161",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HAPk8YY3REoEozWbRzv6dJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4507,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2908,
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

_source line 19 · 2026-05-10T13:07:40.477Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GLAX4W1Yc1UewRfFGAAsfn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.26633",
  "prompt": "What is OmniRetarget? Does it generate video? What data does it create for humanoid robots? What tasks does it target?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d3f77db-d6e1-47ba-b88f-9c4e969e6161",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwTpKKPDpVrc1S7PBJk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "84b603b2-9d6c-4470-9169-445dde51ac1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HAPk8YY3REoEozWbRzv6dJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4507,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2908,
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

_source line 20 · 2026-05-10T13:07:41.136Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QF9pTRJRrYfQgdMsSLV1AH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.17808",
  "prompt": "What is EVA? Does it generate synthetic video? How does it align videos with robot actions? What does it use inverse dynamics for?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84b603b2-9d6c-4470-9169-445dde51ac1b",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwTpKKPDpVrc1S7PBJk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "42203713-bc79-49c0-b047-41d06daac51e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HAPk8YY3REoEozWbRzv6dJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4507,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2908,
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

_source line 21 · 2026-05-10T13:07:41.540Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018fyvsdFziR9LxgCe9XyNgi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.17568",
  "prompt": "What is KADP? Is it about video generation or diffusion policies? How does it use kinematic constraints?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42203713-bc79-49c0-b047-41d06daac51e",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwTpKKPDpVrc1S7PBJk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86533f15-c1b3-4617-b6ac-ecf21c1b2644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HAPk8YY3REoEozWbRzv6dJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4507,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 16917,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2908
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4507,
          "output_tokens": 437,
          "cache_read_input_tokens": 16917,
          "cache_creation_input_tokens": 2908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2908,
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

_source line 22 · 2026-05-10T13:07:45.841Z_

<details><summary>↩ Tool result · `toolu_01GLAX4W1Yc1UewRfFGAAsfn`</summary>

```text
# OmniRetarget Overview

**What is OmniRetarget?**

OmniRetarget is "an interaction-preserving data generation engine based on an interaction mesh" that converts human motions into robot-executable trajectories. It addresses the embodiment gap between humans and humanoids by preserving crucial spatial and contact relationships.

**Does it generate video?**

No, OmniRetarget does not generate video. It produces kinematically feasible motion trajectories for robots.

**What data does it create?**

The system generates motion trajectory data—over 8 hours worth—that can be "augmented from a single demonstration to different robot embodiments, terrains, and object configurations." This data trains reinforcement learning policies.

**What tasks does it target?**

OmniRetarget focuses on complex whole-body skills including:
- Long-horizon parkour movements (up to 30 seconds)
- Loco-manipulation tasks (locomotion combined with object manipulation)
- General scene interaction

The research demonstrates these capabilities on a Unitree G1 humanoid robot, showing successful execution of intricate locomotion and manipulation behaviors trained on the generated data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84b603b2-9d6c-4470-9169-445dde51ac1b",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "d5200a70-86e0-4c68-92b4-38c418c1e003",
  "sourceToolAssistantUUID": "84b603b2-9d6c-4470-9169-445dde51ac1b",
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

_source line 23 · 2026-05-10T13:07:46.057Z_

<details><summary>↩ Tool result · `toolu_01QF9pTRJRrYfQgdMsSLV1AH`</summary>

```text
# EVA: Executable Video Alignment

**What is EVA?**

EVA is "a reinforcement-learning post-training framework for aligning video world models." It addresses the problem where visually coherent generated videos may still violate physical constraints needed for robot control.

**Does it generate synthetic video?**

EVA doesn't generate videos itself—instead, it improves existing video world models that produce future visual predictions based on current observations and task instructions.

**How does it align videos with robot actions?**

EVA uses a training signal derived from physical feasibility. It encourages generated rollouts to produce "smooth motions measured by velocity, acceleration, and jerk while penalizing actions that violate embodiment constraints." This ensures the videos translate into executable robot commands.

**What does it use inverse dynamics for?**

The framework "trains an inverse dynamics model on real robot trajectories and repurposes it as a reward model." This model converts generated video frames into action sequences, evaluating whether those actions are physically feasible and stable for the robot to execute. Critically, the reward signal remains informative even when videos contain visual artifacts, since such distortions typically produce infeasible control commands.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42203713-bc79-49c0-b047-41d06daac51e",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "482583b9-9ded-497b-9139-b5f821f32c50",
  "sourceToolAssistantUUID": "42203713-bc79-49c0-b047-41d06daac51e",
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

_source line 24 · 2026-05-10T13:07:46.213Z_

<details><summary>↩ Tool result · `toolu_01AxKCRoymkwRbP9xqefS17X`</summary>

```text
# BridgeV2W Overview

**What it is:**
BridgeV2W is a system that adapts pretrained video generation models to function as embodied world models for robotics. It addresses key challenges in using video models for robot control, including misalignment between action coordinates and pixel space, camera viewpoint sensitivity, and inconsistent architectures across different robot embodiments.

**What it does:**
The method "converts coordinate-space actions into pixel-aligned embodiment masks rendered from the URDF and camera parameters." It then feeds these masks into a video generation model to predict future video frames based on robot actions.

**Video conditioning approach:**
Yes, BridgeV2W uses a ControlNet-style integration. The embodiment masks are "injected into a pretrained video generation model via a ControlNet-style pathway," which aligns action signals with predicted videos and accommodates different camera viewpoints.

**Embodiments targeted:**
The paper demonstrates results on both single-arm and dual-arm robots, specifically testing on the DROID dataset (single-arm) and the AgiBot-G1 dataset (dual-arm). The approach yields "a unified world model architecture across embodiments," suggesting it generalizes to different robot morphologies.

The system also includes a flow-based motion loss to prevent overfitting to static backgrounds.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d3f77db-d6e1-47ba-b88f-9c4e969e6161",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "6f8f0a63-d3ab-4887-a859-a9575f9cc4a4",
  "sourceToolAssistantUUID": "7d3f77db-d6e1-47ba-b88f-9c4e969e6161",
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

_source line 25 · 2026-05-10T13:07:46.294Z_

<details><summary>↩ Tool result · `toolu_018fyvsdFziR9LxgCe9XyNgi`</summary>

```text
# KADP: Kinematics-Aware Diffusion Policy

KADP is **not** about video generation—it's a robotic manipulation framework using diffusion policies for whole-arm control.

## Key Characteristics

**Purpose**: KADP addresses whole-body robot control by learning actions that account for full-arm kinematics, not just end-effector positioning. This enables collision avoidance and body-object interactions.

**Spatial Consistency**: The framework uses "a set of 3D points on the arm body, naturally aligned with the 3D point cloud observations" to represent both robot states and actions in a unified 3D space, rather than joint-space representations.

**Kinematic Constraints**: The approach incorporates kinematics priors directly into diffusion processes to "guarantee the kinematic feasibility of output actions." Final joint commands are calculated through an optimization-based inverse kinematics solver.

## Core Innovation

By maintaining consistent observation and action spaces in 3D coordinates, KADP improves sample efficiency and spatial generalization compared to methods that learn in joint space—which requires the policy to implicitly learn nonlinear arm kinematics from limited demonstrations.

The framework combines diffusion-based imitation learning with kinematics-aware constraints for practical robotic execution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86533f15-c1b3-4617-b6ac-ecf21c1b2644",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "cada8083-9a69-4077-9c69-eccafcba6835",
  "sourceToolAssistantUUID": "86533f15-c1b3-4617-b6ac-ecf21c1b2644",
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

_source line 26 · 2026-05-10T13:07:48.435Z_

Perfect. Now let me get a few more key papers to provide complete competitive analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cada8083-9a69-4077-9c69-eccafcba6835",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwUUk7gTgWEWQZ9cWxQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "461e5a2c-a066-444a-9945-435313c1f3a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ub1m2oSwSvCz9MGUEXtCBr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6243,
      "cache_read_input_tokens": 19825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6243,
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

_source line 27 · 2026-05-10T13:07:49.365Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013sv5CmcKu9VAYALdFpeoxk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.09330",
  "prompt": "What is VAG? Does it generate video and action pairs? What conditioning does it use? Is it for humanoid robots or general manipulation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "461e5a2c-a066-444a-9945-435313c1f3a8",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwUUk7gTgWEWQZ9cWxQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "597d58b2-54fa-4eba-8d46-838bc006adca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ub1m2oSwSvCz9MGUEXtCBr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6243,
      "cache_read_input_tokens": 19825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6243,
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

_source line 28 · 2026-05-10T13:07:49.965Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015AvBxjbPHKWVaN3xdDPJHe`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.04537",
  "prompt": "What is X-Humanoid? Does it generate humanoid videos? How does it create synthetic data? What is the scale and methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "597d58b2-54fa-4eba-8d46-838bc006adca",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwUUk7gTgWEWQZ9cWxQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "39a4e6af-160b-411f-afaf-43b689334274",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ub1m2oSwSvCz9MGUEXtCBr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6243,
      "cache_read_input_tokens": 19825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6243,
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

_source line 29 · 2026-05-10T13:07:50.455Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015wcsXm96wvp4Gt5neMkozJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.20857",
  "prompt": "What is G-DReaM? Does it use URDF? How does it condition diffusion? What embodiments does it handle?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39a4e6af-160b-411f-afaf-43b689334274",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwUUk7gTgWEWQZ9cWxQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "674d5bbe-f216-4f45-82fa-cab71f88b216",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ub1m2oSwSvCz9MGUEXtCBr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6243,
      "cache_read_input_tokens": 19825,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6243
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 318,
          "cache_read_input_tokens": 19825,
          "cache_creation_input_tokens": 6243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6243,
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

_source line 30 · 2026-05-10T13:07:53.814Z_

<details><summary>↩ Tool result · `toolu_013sv5CmcKu9VAYALdFpeoxk`</summary>

```text
# VAG: Overview

**What is VAG?**
VAG is "a unified flow-matching-based dual-stream framework that jointly generates video and action under visual and language conditioning." It addresses limitations in existing world models by providing paired video-action outputs suitable for robot policy learning.

**Video-Action Generation:**
Yes, VAG generates aligned video-action pairs. The system uses "synchronized denoising in both branches and an adaptive 3D pooling mechanism to transfer compact global video context to the action branch," improving cross-modal consistency.

**Conditioning:**
The framework uses **visual and language conditioning** to guide generation, enabling task-specific synthetic data creation.

**Robot Type:**
The paper does not specify humanoid robots or limit itself to particular morphologies. It refers broadly to "robot foundation models" and mentions applications across "simulated and real-world settings," suggesting applicability to various embodied AI systems rather than a specific robot class.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "597d58b2-54fa-4eba-8d46-838bc006adca",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "c658877d-9592-4f9a-9465-9ece0dde1c4a",
  "sourceToolAssistantUUID": "597d58b2-54fa-4eba-8d46-838bc006adca",
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

_source line 31 · 2026-05-10T13:07:54.533Z_

<details><summary>↩ Tool result · `toolu_015wcsXm96wvp4Gt5neMkozJ`</summary>

```text
# G-DReaM Overview

**What is G-DReaM?**

G-DReaM is "a novel unified graph-conditioned diffusion-based motion generation framework for retargeting reference motions across diverse embodiments." It addresses the challenge of adapting motion patterns to different robots despite differences in structure and design.

**URDF Usage**

The provided abstract does not mention URDF (Unified Robot Description Format) or whether the method uses it.

**Diffusion Conditioning**

The system conditions diffusion through graph structures representing robot characteristics. The paper explains that "the intrinsic characteristics of heterogeneous embodiments are represented with graph structure that effectively captures topological and geometrical features." Additionally, the researchers employ "energy-based guidance formulated as retargeting losses to train the diffusion model" when ground truth motions are unavailable.

**Embodiments Handled**

The method is designed to work across "diverse embodiments" and "heterogeneous embodiments" with varying skeletal structures. The abstract notes it demonstrates "generalization to both diverse skeletal structures and similar motion patterns," though specific robot examples aren't detailed in this summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "674d5bbe-f216-4f45-82fa-cab71f88b216",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "a25f7826-935c-427c-9940-b468af4261f8",
  "sourceToolAssistantUUID": "674d5bbe-f216-4f45-82fa-cab71f88b216",
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

_source line 32 · 2026-05-10T13:07:54.845Z_

<details><summary>↩ Tool result · `toolu_015AvBxjbPHKWVaN3xdDPJHe`</summary>

```text
# X-Humanoid Overview

**What it is:** X-Humanoid is a generative video editing system that adapts human videos into humanoid robot videos, addressing data scarcity in embodied AI training.

**Video Generation:** Yes, the system generates humanoid videos by converting "web-scale human videos" into robotized versions suitable for training Vision-Language-Action models and world models.

**Synthetic Data Creation:** The researchers developed a scalable pipeline using Unreal Engine to transform "community assets into 17+ hours of paired synthetic videos" for training purposes. This synthetic data provides the paired human-humanoid examples needed to train the model.

**Scale and Methodology:**
- Applied the trained model to 60 hours of Ego-Exo4D videos
- Released a dataset containing "over 3.6 million 'robotized' humanoid video frames"
- Built on the Wan 2.2 model, adapting it into a video-to-video structure
- User studies showed 69% rated motion consistency best and 62.1% rated embodiment correctness best compared to baselines

The approach advances beyond prior solutions by handling "complex full-body motions and scene occlusions" in third-person videos rather than simply overlaying robotic arms onto egocentric footage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39a4e6af-160b-411f-afaf-43b689334274",
  "isSidechain": true,
  "promptId": "23863439-8448-4ea1-a668-f2107b10e9f7",
  "agentId": "a2e7adaff6e2bf617",
  "type": "user",
  "uuid": "657a4ecd-ca2d-4b17-809a-c5c350206aad",
  "sourceToolAssistantUUID": "39a4e6af-160b-411f-afaf-43b689334274",
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

_source line 33 · 2026-05-10T13:08:25.558Z_

Excellent. Now I have comprehensive information. Let me compile the detailed competitive analysis report.

## COMPREHENSIVE ARXIV SEARCH RESULTS: COMPETITIVE & RELATED WORK

### KEY FINDING: BridgeV2W CONFIRMED
**BridgeV2W (arXiv:2602.03793)** absolutely exists and is highly relevant to your URDF-DiT proposal.

---

## SEARCH RESULTS BY QUERY

### 1. **Humanoid Robot Video Generation Synthetic Data 2026**

**Directly Competing Work:**
- **X-Humanoid (arXiv:2512.04537)** - Generates 60+ hours of robotized humanoid videos by converting human videos via Unreal Engine synthesis. Creates 3.6M+ video frames. Uses Wan 2.2 base model with video-to-video adaptation. **VERY RELEVANT**: Same humanoid video focus, synthetic data generation approach.
- **FlowAct-R1 (arXiv:2601.10103)** - Interactive humanoid video generation using MMDiT architecture for streaming synthesis.
- **GR00T N1 (arXiv:2503.14734)** - Foundation model that leverages pretrained video generation models to create neural trajectories for humanoid robot training, combining real, human, and synthetic datasets.

**Tangentially Related:**
- Video Generation Models in Robotics survey (arXiv:2601.07823v1) - Covers robotics-specific video generation applications broadly.

---

### 2. **ControlNet URDF Robot Video Diffusion 2025-2026**

**CRITICAL COMPETITOR:**
- **BridgeV2W (arXiv:2602.03793)** - Directly uses URDF-rendered embodiment masks injected into video diffusion via **ControlNet-style pathway**. Converts coordinate-space actions to pixel-aligned masks. Tests on DROID (single-arm) and AgiBot-G1 (dual-arm). **THIS IS YOUR DIRECT COMPETITOR** for the URDF+ControlNet+video diffusion combination.

**Related but Broader Scope:**
- **G-DReaM (arXiv:2505.20857)** - Graph-conditioned diffusion for motion retargeting. Explicitly parses URDF files for skeleton/robot data (Atlas, Talos, Cassie, Valkyrie). Energy-based guidance for diffusion. Different approach (motion retargeting, not video generation).
- **Vid2World (arXiv:2505.14357)** - Uses ControlNet with video diffusion for interactive world models in robotics.
- ControlNeXt (arXiv:2408.06070) and EasyControl papers - General ControlNet video methodologies.

---

### 3. **Inverse Dynamics Model Robot Video Generation 2026**

**Key Papers:**
- **EVA (arXiv:2603.17808)** - RL post-training framework that uses inverse dynamics model as reward model to align video world models with executable robot actions. Evaluates generated videos through action sequences they induce. Doesn't generate video itself but improves existing video models. **RELEVANT**: Addresses synthetic video executability for humanoids.
  
- **DeFI (arXiv:2604.16391)** - Disentangled robot learning via separate forward/inverse dynamics pretraining. Creates General Forward Dynamics Model (GFDM) and General Inverse Dynamics Model (GIDM). ICLR 2026 paper. **RELEVANT**: IDM training framework that could work with video-generated data.

- **MotuBrain (arXiv:2604.27792)** - World action model supporting video generation + inverse dynamics + joint video-action prediction. Uses UniDiffuser for joint modeling.

---

### 4. **Kinematic Conditioning Video Diffusion Robot Manipulation 2026**

**Video Generation with Kinematics:**
- **Kinematics-Aware Diffusion Policy (KADP) (arXiv:2512.17568)** - NOT video generation. Uses diffusion for manipulation policies with kinematic constraints in 3D observation/action space. Different from your video generation approach but addresses kinematic feasibility.

**Video Generation with Action Conditioning:**
- **Learning Rigid Body Interactions with Video Diffusion (arXiv:2510.02284)** - Generates videos of rigid body interactions with kinematic control.
- **Learning Diverse Robot Striking Motions (arXiv:2409.15528)** - Diffusion with kinematically constrained gradient guidance for manipulation.
- **AnchorDream** (mentioned in results) - Embodiment-aware video generation that anchors diffusion in robot motion, preventing hallucinations.

---

### 5. **Whole Body Humanoid Data Generation Loco-Manipulation 2026**

**MAJOR COMPETITOR:**
- **OmniRetarget (arXiv:2509.26633)** - Generates interaction-preserving trajectory data for whole-body loco-manipulation on Unitree G1. Creates 8+ hours of synthetic trajectories. **NOT video-based** (trajectory-based). Targets exact same downstream task (humanoid loco-manipulation) but different data modality than you.

**Related Humanoid Loco-Manipulation Work:**
- **DemoHLM (arXiv:2510.11258)** - Generalizable humanoid loco-manipulation from single demonstration
- **VisualMimic (arXiv:2509.20322)** - Visual humanoid loco-manipulation with motion tracking and generation
- **WholeBodyVLA (arXiv:2512.11047)** - Unified vision-language-action for whole-body loco-manipulation control

---

### 6. **Action-Conditioned Video Generation Robot Training Data 2026**

**Direct Competitors for Synthetic Video+Action Data:**
- **VAG: Dual-Stream Video-Action Generation (arXiv:2604.09330)** - Flow-matching-based dual-stream that jointly generates video AND action pairs under visual/language conditioning. Synchronized denoising with adaptive 3D pooling. **VERY RELEVANT**: Generates aligned video-action pairs for robot training, similar goal to URDF-DiT.

- **MotuBrain (arXiv:2604.27792)** - Supports joint video-action prediction with unified scheduling.

- **CoVAR: Co-generation of Video and Action (arXiv:2512.16023)** - Multi-modal diffusion for robotic manipulation video+action generation.

**Other Video World Models for Robot Actions:**
- EVA (arXiv:2603.17808) - Already covered above
- Causal World Modeling (LingBot-VA, arXiv:2601.21998) - Autoregressive diffusion world model with unified video-action framework

---

### 7. **BridgeV2W ControlNet Robot Video - VERIFIED**

**CONFIRMED:** **BridgeV2W (arXiv:2602.03793)** published February 3, 2026

**What it does (DIRECT THREAT TO YOUR PROPOSAL):**
- Converts coordinate-space robot actions to **pixel-aligned embodiment masks rendered from URDF and camera parameters**
- Injects masks into pretrained video generation model via **ControlNet-style pathway**
- Aligns action control signals with predicted videos
- Adds view-specific conditioning for camera viewpoints
- Creates unified world model across embodiments (single-arm and dual-arm robots tested: DROID dataset, AgiBot-G1 dataset)
- Uses flow-based motion loss to prevent static background overfitting

**Comparison to Your URDF-DiT:**
- Both use URDF rendering for embodiment masking
- Both use ControlNet-style injection
- Both target video diffusion models
- **Key difference**: BridgeV2W appears focused on action-to-video world models for control, while URDF-DiT (based on your description) generates kinematic-conditioned training data for humanoid IDM/policy training
- BridgeV2W targets multi-embodiment (arm-based), URDF-DiT targets 29-DoF humanoid whole-body

---

## COMPETITIVE LANDSCAPE SUMMARY

### Closest Competitors (Same Problem Space)
1. **BridgeV2W (2602.03793)** - URDF + ControlNet + Video Diffusion (multi-embodiment)
2. **VAG (2604.09330)** - Video+Action co-generation with visual/language conditioning
3. **X-Humanoid (2512.04537)** - Humanoid-specific synthetic video generation at scale
4. **OmniRetarget (2509.26633)** - Whole-body humanoid data generation (trajectory, not video)

### Papers Using Similar Components
- **G-DReaM (2505.20857)** - URDF + diffusion (but for motion retargeting, not video)
- **EVA (2603.17808)** - Inverse dynamics + video alignment
- **MotuBrain (2604.27792)** - Joint video-action modeling with diffusion

### NOT Direct Competitors
- **KADP (2512.17568)** - Diffusion policies, not video generation
- **Humanoid Loco-Manipulation papers** - Task-specific but not video data generation focused

---

## GAPS & OPPORTUNITIES FOR YOUR PROPOSAL

Your URDF-DiT appears to occupy a specific niche:
- **Humanoid-specific** (29-DoF) vs BridgeV2W's multi-arm approach
- **Forward kinematics conditioning** of video diffusion vs BridgeV2W's action-to-mask approach
- **IDM/policy training data** focus vs world models for control
- Likely targets **whole-body locomanipulation** like OmniRetarget but via **video generation** rather than trajectory sampling

**Most threatening prior work:** BridgeV2W with its direct URDF+ControlNet+diffusion combination. You'll need to clearly articulate what makes humanoid-specific kinematic conditioning superior to their embodiment-mask approach.

Sources:
- [BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks](https://arxiv.org/abs/2602.03793)
- [VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis](https://arxiv.org/abs/2604.09330)
- [X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale](https://arxiv.org/abs/2512.04537)
- [OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction](https://arxiv.org/abs/2509.26633)
- [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808)
- [G-DReaM: Graph-conditioned Diffusion Retargeting across Multiple Embodiments](https://arxiv.org/abs/2505.20857)
- [Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation](https://arxiv.org/abs/2512.17568)
- [DeFI: Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining](https://arxiv.org/abs/2604.16391)
- [MotuBrain: An Advanced World Action Model for Robot Control](https://arxiv.org/abs/2604.27792)
- [FlowAct-R1: Towards Interactive Humanoid Video Generation](https://arxiv.org/abs/2601.10103)
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)
- [Video Generation Models in Robotics: Applications, Research Challenges, Future Directions](https://arxiv.org/abs/2601.07823)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "657a4ecd-ca2d-4b17-809a-c5c350206aad",
  "isSidechain": true,
  "agentId": "a2e7adaff6e2bf617",
  "requestId": "req_011CatwV7HoWmVUrD6SLuE9s",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e0179fa6-4501-44fa-a66f-b54e7db976a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c63b9de1-5079-4324-ba7f-fba53dc24e44",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CCd4LHwjQgaiSLAkaw2wnw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 285,
      "cache_creation_input_tokens": 868,
      "cache_read_input_tokens": 26068,
      "output_tokens": 2907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 868
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 285,
          "output_tokens": 2907,
          "cache_read_input_tokens": 26068,
          "cache_creation_input_tokens": 868,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 868,
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
