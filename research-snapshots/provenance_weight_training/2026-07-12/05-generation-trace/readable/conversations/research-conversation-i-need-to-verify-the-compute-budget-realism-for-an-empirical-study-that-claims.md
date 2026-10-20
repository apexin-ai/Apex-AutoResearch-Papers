# Research conversation: I need to verify the compute budget realism for an empirical study that claims ~155-185 H100-hours total for: - Kimodo m

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a41d313cb1b0d8db5.jsonl`
- **Structured JSON:** [`5db6cfaa9a276ae92ffe.json`](../../sessions/5d/5db6cfaa9a276ae92ffe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-10T19:18:53.888Z_

I need to verify the compute budget realism for an empirical study that claims ~155-185 H100-hours total for:
- Kimodo motion generation on G1: ~2h
- Isaac Lab physics validation: ~8h
- Isaac Lab rendering (27 conditions + 9 ACT): ~22h
- Diffusion Policy training (27 conditions × 2 seeds × 1.5h = 81h)
- ACT training (9 conditions × 2 seeds × 1h = 18h)
- Evaluation rollouts: ~8h
- Pilot experiments: ~6h
- Debug: ~10h

Search for:
1. "Diffusion Policy training time GPU hours" - how long does it take to train a Diffusion Policy (1D U-Net) for robot control? Is 1.5h per condition on H100 realistic?
2. "ACT action chunking transformer training time" - how long does ACT training take?
3. "Isaac Lab rendering throughput humanoid" - how fast can Isaac Lab render humanoid environments?
4. "Kimodo inference speed motion generation" - how fast is Kimodo inference?

Also search for:
- "diffusion policy training cost robot manipulation"
- "Isaac Lab G1 humanoid environment setup"

Report what you find about typical training times for these components.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b0150ee4-e7f7-496d-afa5-c1d4cb4e7131",
  "agentId": "a41d313cb1b0d8db5",
  "type": "user",
  "uuid": "a1a2697a-2fae-45d2-8bad-4f97fa57525d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T19:18:55.237Z_

I'll search for information about the computational requirements and training times for these robot learning components.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1a2697a-2fae-45d2-8bad-4f97fa57525d",
  "isSidechain": true,
  "agentId": "a41d313cb1b0d8db5",
  "requestId": "req_011CauRmvCnkrcSmua2etfa7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e79e87e9-660b-41d4-b7e1-e82bae583ba2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Twvo7jbHVepGRYDe272Cvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 732,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T19:18:55.575Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EQ5hd6nH5oxT8xWXYXLLka`</summary>

```json
{
  "query": "Diffusion Policy training time GPU hours robot control"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e79e87e9-660b-41d4-b7e1-e82bae583ba2",
  "isSidechain": true,
  "agentId": "a41d313cb1b0d8db5",
  "requestId": "req_011CauRmvCnkrcSmua2etfa7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "139c3db6-7719-4390-b8ae-61511686aa0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Twvo7jbHVepGRYDe272Cvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 732,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:18:55.684Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015uPjKw7wHw2uw7TDHMG8r8`</summary>

```json
{
  "query": "ACT action chunking transformer training time GPU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "139c3db6-7719-4390-b8ae-61511686aa0a",
  "isSidechain": true,
  "agentId": "a41d313cb1b0d8db5",
  "requestId": "req_011CauRmvCnkrcSmua2etfa7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c0f7c139-be99-455b-9960-8deaa437dfd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Twvo7jbHVepGRYDe272Cvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 732,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:18:55.711Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FGMnr6B6GRHdVf1vzjEKAx`</summary>

```json
{
  "query": "Isaac Lab rendering throughput humanoid"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0f7c139-be99-455b-9960-8deaa437dfd9",
  "isSidechain": true,
  "agentId": "a41d313cb1b0d8db5",
  "requestId": "req_011CauRmvCnkrcSmua2etfa7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7eaba506-56de-491b-b8cf-db1dfcda2439",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Twvo7jbHVepGRYDe272Cvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 732,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T19:18:55.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WGJg1xo8Xow8ajv5sBoBcj`</summary>

```json
{
  "query": "Kimodo inference speed motion generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eaba506-56de-491b-b8cf-db1dfcda2439",
  "isSidechain": true,
  "agentId": "a41d313cb1b0d8db5",
  "requestId": "req_011CauRmvCnkrcSmua2etfa7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "afa5b4ae-17f1-4841-a286-5f52b199fd72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Twvo7jbHVepGRYDe272Cvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 732,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T19:18:55.954Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M8fFh3cjhjBKwvSHPy3BJp`</summary>

```json
{
  "query": "diffusion policy training cost robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afa5b4ae-17f1-4841-a286-5f52b199fd72",
  "isSidechain": true,
  "agentId": "a41d313cb1b0d8db5",
  "requestId": "req_011CauRmvCnkrcSmua2etfa7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04044cf0-6856-4c75-8259-10895d8edb54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Twvo7jbHVepGRYDe272Cvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 732,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T19:18:56.052Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VP2ervbJfeEBdb9r7XoFbc`</summary>

```json
{
  "query": "Isaac Lab G1 humanoid environment setup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04044cf0-6856-4c75-8259-10895d8edb54",
  "isSidechain": true,
  "agentId": "a41d313cb1b0d8db5",
  "requestId": "req_011CauRmvCnkrcSmua2etfa7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff9756d4-55bd-4253-a985-774aaa0cd4f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Twvo7jbHVepGRYDe272Cvg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 13649,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 732
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 289,
          "cache_read_input_tokens": 13649,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 732,
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

_source line 9 · 2026-05-10T19:19:01.797Z_

<details><summary>↩ Tool result · `toolu_01FGMnr6B6GRHdVf1vzjEKAx`</summary>

```text
Web search results for query: "Isaac Lab rendering throughput humanoid"

Links: [{"title":"Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning","url":"https://arxiv.org/html/2511.04831v1"},{"title":"R²D²: Scaling Multimodal Robot Learning with NVIDIA Isaac Lab | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/r2d2-scaling-multimodal-robot-learning-with-nvidia-isaac-lab/"},{"title":"2025-9-28 Isaac Lab: A GPU-Accelerated Simulation Framework for","url":"https://d1qx31qr3h6wln.cloudfront.net/publications/Isaac%20Lab,%20A%20GPU-Accelerated%20Simulation%20Framework%20for%20Multi-Modal%20Robot%20Learning.pdf"},{"title":"NVIDIA Isaac Lab Open-Source Modular Framework","url":"https://developer.nvidia.com/isaac/lab"},{"title":"Releases · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/releases"},{"title":"Isaac Lab: GPU-Accelerated Multi-Modal Robot Simulation","url":"https://www.emergentmind.com/topics/isaac-lab"},{"title":"Introduction to Isaac Lab Reinforcement Learning with the Isaac Humanoid | by Justin Costa | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/introduction-to-isaac-lab-reinforcement-learning-with-the-isaac-humanoid-062a4c3f6b99"},{"title":"Redirecting to the latest Isaac Lab documentation","url":"https://isaac-sim.github.io/IsaacLab/"},{"title":"GitHub - isaac-sim/IsaacLab: Unified framework for robot learning built on NVIDIA Isaac Sim · GitHub","url":"https://github.com/isaac-sim/IsaacLab"},{"title":"Welcome to Isaac Lab! — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/index.html"}]

Based on the search results, here are key findings about Isaac Lab rendering throughput for humanoid robots:

## Rendering Throughput Performance

Isaac Lab achieves 135,000 FPS for humanoid locomotion (Unitree H1), demonstrating exceptional rendering performance for humanoid simulation tasks.

## How Isaac Lab Achieves High Throughput

Isaac Lab combines RTX rendering for photorealistic, scalable visuals with PhysX for high-fidelity physics simulation. To support massive parallel rendering, Isaac Lab uses the tiled rendering pipeline of the RTX renderer, batching multiple cameras into a single render pass by spatially arranging them as tiles within the GPU framebuffer.

## Key Rendering Capabilities

High-throughput GPU-accelerated rendering supports large-scale generation of RGB, depth, and segmentation data, facilitating policy training and sim-to-real transfer using exteroceptive information. Additionally, the "TiledCamera" aggregates views across thousands of environments into a single GPU framebuffer, supporting RGB, depth, normal, and semantic mask outputs.

This architecture enables Isaac Lab to efficiently scale rendering across thousands of parallel simulation environments, making it ideal for large-scale multi-modal robot learning workflows with humanoid robots.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eaba506-56de-491b-b8cf-db1dfcda2439",
  "isSidechain": true,
  "promptId": "b0150ee4-e7f7-496d-afa5-c1d4cb4e7131",
  "agentId": "a41d313cb1b0d8db5",
  "type": "user",
  "uuid": "69d69bb2-ccc6-4f60-bee8-fe66cee93300",
  "sourceToolAssistantUUID": "7eaba506-56de-491b-b8cf-db1dfcda2439",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T19:19:01.995Z_

<details><summary>↩ Tool result · `toolu_01M8fFh3cjhjBKwvSHPy3BJp`</summary>

```text
Web search results for query: "diffusion policy training cost robot manipulation"

Links: [{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion Policy: How Diffusion Models Are Transforming Robot Learning from Demonstration | by Isaac Kargar | Medium","url":"https://kargarisaac.medium.com/diffusion-policy-how-diffusion-models-are-transforming-robot-learning-from-demonstration-32c27ba829cf"},{"title":"3D Diffusion Policy","url":"https://3d-diffusion-policy.github.io/"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"},{"title":"Diffusion Trajectory-guided Policy for Long-horizon Robot Manipulation","url":"https://arxiv.org/html/2502.10040v1"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Diffusion Trajectory-guided Policy: A Novel Framework for Long-Horizon Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=VaoeAi5CW8"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion","url":"https://www.researchgate.net/publication/384857010_Diffusion_policy_Visuomotor_policy_learning_via_action_diffusion"},{"title":"GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub","url":"https://github.com/real-stanford/diffusion_policy"},{"title":"Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning","url":"https://arxiv.org/html/2507.05695"}]

Based on the search results, here's what I found about diffusion policy training costs and robot manipulation:

## Performance and Training Overview

Diffusion Policy consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9% across 12 different tasks from 4 different robot manipulation benchmarks.

## Computational Cost Challenges

While there are challenges such as computational cost and the need for high-quality demonstrations, researchers are actively working to address these issues. Despite the success of diffusion policy methods, they often require extensive fine-tuning and are computationally expensive, limiting their deployment on resource-constrained devices.

## Efficiency Solutions

However, recent work has made progress on reducing training costs. One approach is computationally cost-effective, requiring only consumer-grade GPUs. Additionally, while hPGA-DP (a hybrid diffusion policy) requires more training time than Transformer and U-Net baselines, those baselines need to be trained for twice as many epochs to match hPGA-DP's performance, resulting in 21% to 36% higher total training time, demonstrating superior training efficiency over traditional diffusion backbones.

## Key Bottleneck

Since the diffusion transformer requires multiple denoising steps to generate the action prediction, this leads to a high latency of the model, which is a primary computational bottleneck during both training and inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04044cf0-6856-4c75-8259-10895d8edb54",
  "isSidechain": true,
  "promptId": "b0150ee4-e7f7-496d-afa5-c1d4cb4e7131",
  "agentId": "a41d313cb1b0d8db5",
  "type": "user",
  "uuid": "d2514f35-339f-4fee-9835-e60d6f16858d",
  "sourceToolAssistantUUID": "04044cf0-6856-4c75-8259-10895d8edb54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T19:19:02.915Z_

<details><summary>↩ Tool result · `toolu_01WGJg1xo8Xow8ajv5sBoBcj`</summary>

```text
Web search results for query: "Kimodo inference speed motion generation"

Links: [{"title":"GitHub - nv-tlabs/kimodo: Official implementation of Kimodo, a kinematic motion diffusion model for high-quality human(oid) motion generation. · GitHub","url":"https://github.com/nv-tlabs/kimodo"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/"},{"title":"NVIDIA Kimodo Text-to-Motion: Open Code, Closed Data — What It Means for Robotics | Pebblous","url":"https://blog.pebblous.ai/blog/kimodo-text-to-motion/en/"},{"title":"[2603.15546] Kimodo: Scaling Controllable Human Motion Generation","url":"https://arxiv.org/abs/2603.15546"},{"title":"nvidia/Kimodo-SOMA-RP-v1.1 · Hugging Face","url":"https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1.1"},{"title":"Kimodo: Scaling Controllable Human Motion Generation","url":"https://arxiv.org/html/2603.15546v1"},{"title":"2026-3-16 Kimodo: Scaling Controllable Human Motion Generation","url":"https://research.nvidia.com/labs/sil/projects/kimodo/assets/kimodo_tech_report.pdf"},{"title":"Kimodo: Scaling Controllable Human Motion Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260315546R/abstract"},{"title":"Kimodo: Scaling Controllable Human Motion Generation | Request PDF","url":"https://www.researchgate.net/publication/402482316_Kimodo_Scaling_Controllable_Human_Motion_Generation"},{"title":"nvidia/Kimodo-SOMA-RP-v1 · Hugging Face","url":"https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1"}]

Based on the search results, here's what I found about Kimodo's inference speed for motion generation:

## Inference Speed

Kimodo requires 2 to 5 seconds of inference time for motion generation. More specifically, NVIDIA's Kimodo generates full-body Unitree G1 motion from plain English in 2–5 seconds.

## Motion Generation Capabilities

Kimodo is a kinematic motion diffusion model trained on a large-scale (700 hours) commercially-friendly optical motion capture dataset. The model generates high-quality 3D human and robot motions, and is controlled through text prompts and an extensive set of constraints such as full-body pose keyframes, end-effector positions/rotations, 2D paths, and 2D waypoints.

## Hardware Requirements

For the inference speed to be reasonable, Kimodo requires ~17GB of VRAM to generate locally entirely on GPU. If you have a smaller card, setting TEXT_ENCODER_DEVICE=cpu when running Kimodo commands forces text encoding to the CPU, which is slightly slower but reduces VRAM usage to <3 GB.

## Practical Limitations

It's worth noting that the maximum output is 10 seconds of motion. Most real tasks take longer, so Kimodo is better suited for generating individual motion primitives rather than long-horizon tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afa5b4ae-17f1-4841-a286-5f52b199fd72",
  "isSidechain": true,
  "promptId": "b0150ee4-e7f7-496d-afa5-c1d4cb4e7131",
  "agentId": "a41d313cb1b0d8db5",
  "type": "user",
  "uuid": "269c4893-db28-491e-8f9a-3b992b424bde",
  "sourceToolAssistantUUID": "afa5b4ae-17f1-4841-a286-5f52b199fd72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:19:03.121Z_

<details><summary>↩ Tool result · `toolu_01EQ5hd6nH5oxT8xWXYXLLka`</summary>

```text
Web search results for query: "Diffusion Policy training time GPU hours robot control"

Links: [{"title":"Diffusion Policy for Robot Learning: What It Is and How to Use It | SVRC","url":"https://www.roboticscenter.ai/blog/diffusion-policy-robots"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Mini Diffuser: Fast Multi-task Diffusion Policy Training Using Two-level Mini-batches","url":"https://arxiv.org/html/2505.09430v2"},{"title":"GitHub - YanjieZe/3D-Diffusion-Policy: [RSS 2024] 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations · GitHub","url":"https://github.com/YanjieZe/3D-Diffusion-Policy"},{"title":"Fine-tuning Diffusion Policy | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/DiffusionPolicy/"},{"title":"GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub","url":"https://github.com/real-stanford/diffusion_policy"},{"title":"Mini-diffuser reduces by an order of magnitude the time and memory needed to train multi-task vision-language robotic diffusion policies! | Renaud Detry","url":"https://renaud-detry.net/news/2025-06-09--mini-diffuser/"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Diffusion Policy in Robotics — Definition & Training Data | Claru","url":"https://claru.ai/glossary/diffusion-policy"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/html/2303.04137v5"}]

Based on the search results, here's what I found about Diffusion Policy training time and GPU hours for robot control:

## Training Time for Standard Diffusion Policy

Training on a single RTX 3090 or 4090 takes 4-12 hours for a 200-episode dataset, depending on observation resolution and action horizon length. Additionally, 500 episodes take about 12-24 hours on an RTX 3080.

## Training Time Comparison with Variants

The training duration varies significantly depending on the task complexity and approach:

- **3D Diffusion Policy (DP3)**: During training, DP3 takes ~10G gpu memory and ~3 hours on an Nvidia A40 gpu

- **Multi-task Policies**: While a single task policy can be trained within hours, multi-task policies normally take days, and generalist policies take weeks on a cluster of cards.

- **Mini-Diffuser (optimized)**: Mini-Diffuser can be trained end-to-end on a single RTX 4090 GPU in under 13 hours, or on a single A100 GPU in one day, whereas state-of-the-art baselines require multi-GPU clusters running for several days.

## Key Factors Affecting Training Time

Dataset size, model complexity, and the number of inference steps all affect training time. Key hyperparameters include the action horizon (typically 16-32 for tabletop tasks), the number of diffusion steps (100 for DDPM, 10-25 for DDIM), and the observation window (typically 2).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "139c3db6-7719-4390-b8ae-61511686aa0a",
  "isSidechain": true,
  "promptId": "b0150ee4-e7f7-496d-afa5-c1d4cb4e7131",
  "agentId": "a41d313cb1b0d8db5",
  "type": "user",
  "uuid": "3c62ad7e-00ab-4452-a72f-876fe756ab69",
  "sourceToolAssistantUUID": "139c3db6-7719-4390-b8ae-61511686aa0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:19:03.723Z_

<details><summary>↩ Tool result · `toolu_01VP2ervbJfeEBdb9r7XoFbc`</summary>

```text
Web search results for query: "Isaac Lab G1 humanoid environment setup"

Links: [{"title":"Available Environments — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html"},{"title":"Introduction to Isaac Lab Reinforcement Learning with the Isaac Humanoid | by Justin Costa | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/introduction-to-isaac-lab-reinforcement-learning-with-the-isaac-humanoid-062a4c3f6b99"},{"title":"Welcome to Isaac Lab Arena! — isaaclab_arena 0.2","url":"https://isaac-sim.github.io/IsaacLab-Arena/main/index.html"},{"title":"Meta Quest for Humanoid G1 teleoperation in isaac sim - Isaac Sim - NVIDIA Developer Forums","url":"https://forums.developer.nvidia.com/t/meta-quest-for-humanoid-g1-teleoperation-in-isaac-sim/360846"},{"title":"Modifying an existing Direct RL Environment — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/modify_direct_rl_env.html"},{"title":"Teleoperation and Imitation Learning with Isaac Lab Mimic — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/overview/imitation-learning/teleop_imitation.html"},{"title":"GitHub - unitreerobotics/unitree_sim_isaaclab: The Unitree simulation environment built based on Isaac Lab · GitHub","url":"https://github.com/unitreerobotics/unitree_sim_isaaclab"},{"title":"NVIDIA Isaac Lab Open-Source Modular Framework","url":"https://developer.nvidia.com/isaac/lab"},{"title":"Release Notes — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/refs/release_notes.html"},{"title":"Environments — Isaac Lab Documentation","url":"https://docs.robotsfan.com/isaaclab_official/v1.0.0/source/features/environments.html"}]

Based on the web search results, here's what I found about Isaac Lab G1 humanoid environment setup:

## Overview

Isaac Lab is an open-source modular framework for robot learning designed to simplify how robots learn and adapt to new skills in simulation. The G1 humanoid is one of the supported robot embodiments within this framework.

## G1 Environment Setup

A G1 humanoid robot can perform locomanipulation tasks like transporting a box to a tray. The same data generation and policy training steps can be applied to the G1 humanoid robot with locomanipulation capabilities.

## Configuration and Tasks

Unitree G1 robot task module contains various task implementations for the G1 robot, such as pick and place, motion control, etc. For example, environments can be registered with specific configurations like "Isaac-PickPlace-Cylinder-G129-Dex1-Joint" that specify the robot's DOF and hand type.

## Environment Decomposition

Isaac Lab Arena decomposes the environment into three independent sub-pieces: Scene (the physical environment layout), Embodiment (the robot embodiment, its observations, actions, sensors etc.), and Task (a definition of what is to be accomplished in the environment).

## Running Environments

To run a G1 task, you can use commands like `python sim_main.py --device cpu --enable_cameras --task Isaac-PickPlace-Cylinder-G129-Dex1-Joint --enable_dex1_dds --robot_type g129`.

For more detailed setup instructions and documentation, you can refer to the official Isaac Lab documentation and the Unitree simulation repository on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff9756d4-55bd-4253-a985-774aaa0cd4f3",
  "isSidechain": true,
  "promptId": "b0150ee4-e7f7-496d-afa5-c1d4cb4e7131",
  "agentId": "a41d313cb1b0d8db5",
  "type": "user",
  "uuid": "e422c0ca-a985-4f8e-a8f5-c4b518c8cd77",
  "sourceToolAssistantUUID": "ff9756d4-55bd-4253-a985-774aaa0cd4f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:19:04.391Z_

<details><summary>↩ Tool result · `toolu_015uPjKw7wHw2uw7TDHMG8r8`</summary>

```text
Web search results for query: "ACT action chunking transformer training time GPU"

Links: [{"title":"ACT (Action Chunking with Transformers) · Hugging Face","url":"https://huggingface.co/docs/lerobot/act"},{"title":"Dissecting Action Chunking with Transformers (ACT): Precision Imitation Learning for Robotic Manipulation","url":"https://blog.phospho.ai/dissecting-action-chunking-with-transformers-act-precision-imitation-learning-for-robotic-manipulation/"},{"title":"GitHub - Shaka-Labs/ACT: Action Chunking Transformer implementation for low cost robot · GitHub","url":"https://github.com/Shaka-Labs/ACT"},{"title":"Action Chunking with Transformer (ACT)","url":"https://www.emergentmind.com/topics/action-chunking-with-transformer-act"},{"title":"ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/act-policy-explained"},{"title":"Action Chunking with Transformers - ACT — Open Edge Platform Documentation","url":"https://docs.openedgeplatform.intel.com/dev/edge-ai-suites/robotics-ai-suite/embodied/developer_tools_tutorials/model_tutorials/model_act.html"},{"title":"Bi-ACT: Bilateral Control-Based Imitation Learning via Action Chunking with Transformer | Masato Kobayashi | 小林 聖人","url":"https://mertcookimg.github.io/bi-act/"},{"title":"Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"},{"title":"Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware","url":"https://tonyzhaozh.github.io/aloha/"},{"title":"An Introduction to the Action Chunking Transformer","url":"https://radekosmulski.com/how-to-train-your-robot-with-a-transformer/"}]

I found information about ACT (Action Chunking with Transformers) training time and GPU requirements. Here are the key findings:

## Training Time

The model has approximately 80 million parameters, trains in 5 hours on a single RTX 2080 Ti GPU. More generally, you can expect a few hours for 100k training steps on a single GPU.

Another source provides a different timeframe: training a baseline ACT policy requires a GPU with at least 16 GB VRAM and approximately 8 hours of training for a single task.

A third reference mentions that the sorting task in the video was trained with less than 30 demonstrations on an RTX 3080 and took less than 30 minutes.

## GPU Requirements

- A GPU with at least 16 GB VRAM is required
- Batch size: Start with batch size 8 and adjust based on your GPU memory

The training time varies significantly depending on the dataset size and GPU hardware, ranging from 30 minutes on high-end GPUs with small datasets to several hours with larger demonstrations on standard GPUs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0f7c139-be99-455b-9960-8deaa437dfd9",
  "isSidechain": true,
  "promptId": "b0150ee4-e7f7-496d-afa5-c1d4cb4e7131",
  "agentId": "a41d313cb1b0d8db5",
  "type": "user",
  "uuid": "2234cd93-b756-4595-ab2d-2e11afd3284b",
  "sourceToolAssistantUUID": "c0f7c139-be99-455b-9960-8deaa437dfd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T19:19:20.801Z_

Based on my search results, here's what I found about the computational realism of your empirical study's budget:

## Diffusion Policy Training Time (1.5h per condition on H100)

Your estimate of 1.5 hours per condition appears **optimistic but not unreasonable** for H100s, with important caveats:

- Standard Diffusion Policy on RTX 3090/4090 takes 4-12 hours for 200-episode datasets
- DP3 (3D variant) takes ~3 hours on an A40 GPU  
- Mini-Diffuser (optimized) trains in <13 hours on RTX 4090 or 1 day on A100
- Multi-task policies take days; generalist policies take weeks on multi-GPU clusters

H100s are substantially faster than these consumer/mid-range GPUs, so 1.5 hours per condition might be achievable if: (a) dataset sizes are modest, (b) you're using an optimized variant like Mini-Diffuser, and (c) the 1D U-Net architecture is relatively lightweight. However, 81 hours total for 27 conditions × 2 seeds seems tight—you may face overhead from data loading, validation, and checkpoint management that could push this higher.

## ACT (Action Chunking Transformer) Training Time (~1h per condition)

Your estimate of 1 hour per condition appears **realistic to slightly optimistic**:

- Standard ACT requires 5-8 hours on RTX 2080 Ti for full training
- Training can be as fast as <30 minutes on high-end GPUs (RTX 3080+) with small datasets
- 100k training steps on single GPU typically takes "a few hours"

Your 9 conditions × 2 seeds × 1h = 18 hours total is reasonable if conditions have relatively small datasets. On H100s with modest demonstration sets, 1 hour per condition is plausible.

## Isaac Lab Rendering Throughput

Isaac Lab achieves **135,000 FPS for humanoid locomotion** (Unitree H1), which is exceptionally high. Your 22 hours for rendering 27 conditions + 9 ACT variants appears **very realistic**:

- Isaac Lab uses GPU-accelerated tiled rendering via RTX, batching thousands of environments into single render passes
- The TiledCamera aggregates views across many environments efficiently
- This enables massive parallel rendering for policy training data generation

22 hours to render diverse conditions is actually quite reasonable given the high throughput.

## Kimodo Motion Generation Inference Speed (~2h for G1 motion)

Your 2-hour estimate for Kimodo on G1 is **plausible but worth scrutinizing**:

- Kimodo requires 2-5 seconds per inference call for motion generation
- Maximum output is 10 seconds of motion per inference
- Requires ~17GB VRAM (can run on smaller GPUs with CPU-offloaded text encoding)

If you're generating motion for 27 conditions with some diversity and accounting for failed generations, batch processing overhead, and possibly some iterative refinement, 2 hours is reasonable. However, this is one of the potential bottlenecks if your motion diversity requirements are high.

## Overall Budget Assessment

**Total from your breakdown: ~155h to 185h on H100**

This appears **moderately realistic** with these caveats:

1. **Diffusion Policy (81h)** - This is your biggest unknown. If using standard DP without optimization tricks, you might exceed this. Mini-Diffuser or other optimizations could help you stay within budget.

2. **ACT (18h)** - Reasonable, likely achievable on H100.

3. **Isaac Lab Rendering (22h)** - Well-grounded given Isaac Lab's exceptional rendering throughput.

4. **Kimodo (2h)** - Plausible but depends on motion generation complexity and diversity requirements.

5. **Evaluation + Pilot + Debug (24h)** - This overhead is realistic for comprehensive evaluation and iterative debugging.

**Risk factors:**
- Diffusion Policy training could exceed 81h if datasets are larger or models more complex than anticipated
- Real-world physics validation might take longer than 8h for 27 conditions
- Checkpoint saving, data I/O, and system overhead aren't always accounted for in theoretical estimates

The budget appears credible but somewhat optimistic on training times. You might expect closer to 200-220 H100-hours in practice if you encounter typical engineering overhead and don't use cutting-edge optimization techniques.

Sources:
- [Mini Diffuser: Fast Multi-task Diffusion Policy Training](https://arxiv.org/html/2505.09430v2)
- [3D Diffusion Policy](https://3d-diffusion-policy.github.io/)
- [ACT Hugging Face Documentation](https://huggingface.co/docs/lerobot/act)
- [Isaac Lab: A GPU-Accelerated Simulation Framework](https://arxiv.org/html/2511.04831v1)
- [Kimodo: Scaling Controllable Human Motion Generation](https://arxiv.org/html/2603.15546v1)
- [R²D² Scaling Multimodal Robot Learning with NVIDIA Isaac Lab](https://developer.nvidia.com/blog/r2d2-scaling-multimodal-robot-learning-with-nvidia-isaac-lab/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2234cd93-b756-4595-ab2d-2e11afd3284b",
  "isSidechain": true,
  "agentId": "a41d313cb1b0d8db5",
  "requestId": "req_011CauRnh6mh6sbwViHMtPLK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8ff3480c-fc5f-414d-8bb4-10da14047956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b9bb4059-e3b3-488b-9ce3-35bd9d7de68e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EKdbDqjeYdRdczAVk2nf4i",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3514,
      "cache_creation_input_tokens": 2836,
      "cache_read_input_tokens": 14381,
      "output_tokens": 1265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3514,
          "output_tokens": 1265,
          "cache_read_input_tokens": 14381,
          "cache_creation_input_tokens": 2836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2836,
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
