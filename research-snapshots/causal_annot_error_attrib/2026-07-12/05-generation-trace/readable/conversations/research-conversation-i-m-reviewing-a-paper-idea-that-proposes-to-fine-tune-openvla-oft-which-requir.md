# Research conversation: I'm reviewing a paper idea that proposes to fine-tune OpenVLA-OFT (which requires 8 A100 GPUs) with additional token pru

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2998830578fb4646.jsonl`
- **Structured JSON:** [`ce9a2f2b6b4fb6bb64e8.json`](../../sessions/ce/ce9a2f2b6b4fb6bb64e8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-14T05:36:01.294Z_

I'm reviewing a paper idea that proposes to fine-tune OpenVLA-OFT (which requires 8 A100 GPUs) with additional token pruning heads. The user's HARD CONSTRAINT is ≤200 H100-hours total, fine-tuning from open checkpoints.

Please verify:
1. Search for "OpenVLA-OFT training cost" or "OpenVLA-OFT fine-tuning" — how many GPU hours does it take to fine-tune OpenVLA-OFT on LIBERO? Check the paper or GitHub repo for training details.

2. Search for "LIBERO-Plus evaluation cost" — how long does it take to evaluate across 7 perturbation dimensions and 5 difficulty levels (10,030 tasks)?

3. The idea's resource_estimate claims 2000-3000 A100 hours for manual mode. But the user's constraint is ≤200 H100-hours. This seems like a MASSIVE discrepancy. Verify whether the training runs described (8 GPUs × 24-48h × 8-12 runs) can possibly fit in 200 H100-hours.

4. Also search for "SmolVLA" and "OpenPi" as potential lighter-weight alternatives that might actually fit in 200 H100-hours.

5. Search for "LeRobot framework VLA training" to verify the framework is available and compatible.

Report findings. This is critical — if 200 H100-hours is not enough, the idea fails the user's hard constraint.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "cd68f62b-6d15-4051-9b41-5409c2d49f55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T05:36:01.296Z_

```json
{
  "parentUuid": "cd68f62b-6d15-4051-9b41-5409c2d49f55",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
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
  "uuid": "db513b9d-f0d8-49ea-acb6-bfca2bcc73b3",
  "timestamp": "2026-05-14T05:36:01.296Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-14T05:36:03.881Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015MCYSwc5wQVPtRt69nB1jc`</summary>

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
  "parentUuid": "db513b9d-f0d8-49ea-acb6-bfca2bcc73b3",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vG7dSSkk51J27qfZ2p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f052398e-5c6c-4d6a-8c1c-2ef25ca5178c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4NT7LBe721HWZVXzFjNrZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 903,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T05:36:03.884Z_

<details><summary>↩ Tool result · `toolu_015MCYSwc5wQVPtRt69nB1jc`</summary>

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
  "parentUuid": "f052398e-5c6c-4d6a-8c1c-2ef25ca5178c",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "4cbe2d30-7777-44bb-9533-b36917b3b675",
  "sourceToolAssistantUUID": "f052398e-5c6c-4d6a-8c1c-2ef25ca5178c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T05:36:08.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014CRceX6pDqT6efeqTQKxWS`</summary>

```json
{
  "query": "OpenVLA-OFT training cost GPU hours fine-tuning LIBERO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cbe2d30-7777-44bb-9533-b36917b3b675",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vGJx5WNV8UkN1whz7R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f4ccd3c-e372-4530-a380-df8352154c9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JUxEvj2kJwqULtZXMA8WPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T05:36:08.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DoWLbmVn1ijQCihqdXYfnc`</summary>

```json
{
  "query": "LIBERO-Plus evaluation cost perturbation dimensions benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f4ccd3c-e372-4530-a380-df8352154c9f",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vGJx5WNV8UkN1whz7R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1479ce72-477d-4b9c-9b7e-ddb3ce08bc2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JUxEvj2kJwqULtZXMA8WPV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9126,
      "output_tokens": 161,
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
          "output_tokens": 161,
          "cache_read_input_tokens": 9126,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T05:36:08.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BSAxuykCYg4iZN9xXC74Vk`</summary>

```json
{
  "query": "SmolVLA training cost GPU hours lightweight VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1479ce72-477d-4b9c-9b7e-ddb3ce08bc2d",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vGJx5WNV8UkN1whz7R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c420feb-e5ff-4d74-b610-4729b9e101b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JUxEvj2kJwqULtZXMA8WPV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9126,
      "output_tokens": 161,
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
          "output_tokens": 161,
          "cache_read_input_tokens": 9126,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T05:36:14.416Z_

<details><summary>↩ Tool result · `toolu_01BSAxuykCYg4iZN9xXC74Vk`</summary>

```text
Web search results for query: "SmolVLA training cost GPU hours lightweight VLA"

Links: [{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"Hugging Face says its new robotics model is so efficient it can run on a MacBook | TechCrunch","url":"https://techcrunch.com/2025/06/04/hugging-face-says-its-new-robotics-model-is-so-efficient-it-can-run-on-a-macbook/"}]

Based on the search results, here's what I found about SmolVLA's training cost and GPU hours:

## Training Cost and GPU Hours

The model was trained on 4 GPUs, corresponding to 30k GPU hours. This represents a significant efficiency advantage compared to larger VLA models.

## Fine-tuning Specifications

For fine-tuning SmolVLA on custom data, training the model for 20k steps will roughly take ~4 hours on a single A100 GPU. This demonstrates the model's lightweight nature and accessibility for practitioners.

## Model Size and Efficiency

SmolVLA is 450 million parameters in size, making it an order of magnitude smaller than frontier robotics models (which can exceed 5–7 billion parameters). 

SmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. It is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs.

Despite using fewer than 30k training episodes—an order of magnitude less than other VLAs—SmolVLA matches or exceeds the performance of much larger models, both in simulation and the real world.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c420feb-e5ff-4d74-b610-4729b9e101b6",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "5d7f4e58-dbcd-47ae-9ff1-8424a339a8f2",
  "sourceToolAssistantUUID": "2c420feb-e5ff-4d74-b610-4729b9e101b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T05:36:14.622Z_

<details><summary>↩ Tool result · `toolu_014CRceX6pDqT6efeqTQKxWS`</summary>

```text
Web search results for query: "OpenVLA-OFT training cost GPU hours fine-tuning LIBERO"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"MetaVLA: Unified Meta Co-Training for Efficient Embodied Adaptation","url":"https://arxiv.org/html/2510.05580"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=OpenVLA-OFT"}]

Based on the search results, here's what I found about OpenVLA-OFT training cost in terms of GPU hours for fine-tuning on LIBERO:

## Training Configuration and GPU Hours

OpenVLA-OFT training uses 50-150K gradient steps for non-diffusion methods and 100-250K steps for diffusion methods, across 8 A100/H100 GPUs with batch sizes of 64-128.

OpenVLA-OFT demands approximately 150K to 500K steps for fine-tuning across all four LIBERO suites, including both diffusion and non-diffusion variants.

## GPU Memory Requirements

For training OpenVLA-OFT on LIBERO specifically, the minimum GPU memory needed for LIBERO with 1 input image (third-person camera), 7 action dimensions, and action chunk size 8 with batch size 1 is 25.6 GB, while the recommended GPU memory with batch size 8 per device is 44.1 GB.

## Comparison to Standard Fine-tuning

For context, with LoRA fine-tuning, OpenVLA can be fine-tuned for a specific robot and task set within 10-15 hours on a single A100 GPU, though this is parameter-efficient fine-tuning rather than the full OpenVLA-OFT recipe.

The search results don't provide an exact total GPU-hour cost for the full OpenVLA-OFT training on LIBERO, but the configuration details suggest it requires substantial compute across multiple high-end GPUs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f4ccd3c-e372-4530-a380-df8352154c9f",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "ea52b50d-ac18-4d60-9660-6d64e2b7a1a2",
  "sourceToolAssistantUUID": "8f4ccd3c-e372-4530-a380-df8352154c9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T05:36:14.662Z_

<details><summary>↩ Tool result · `toolu_01DoWLbmVn1ijQCihqdXYfnc`</summary>

```text
Web search results for query: "LIBERO-Plus evaluation cost perturbation dimensions benchmark"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"}]

Based on the search results, here's information about LIBERO-Plus:

## Overview

LIBERO-plus is an official implementation and benchmark for the paper "In-depth Robustness Analysis for Vision-Language-Action Models". It systematically exposes the hidden vulnerabilities of contemporary VLA models through comprehensive robustness evaluation across seven perturbation dimensions.

## Benchmark Specifications

LIBERO-Plus comprises an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions. The evaluation covers seven robustness dimensions and 21 sub-dimensions, ensuring a thorough assessment of model generalization.

## Perturbation Dimensions

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Benchmark Construction

The benchmark construction follows a systematic two-stage process: (1) expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing based on empirical findings; and (2) evaluating the resulting tasks using four representative models and stratifying them into five difficulty levels (Level-1 to Level-5) according to observed accuracy distributions.

## Key Findings

VLA models exhibit extreme sensitivity to camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations, and models largely ignore language instructions and exhibit positional bias rather than genuine semantic understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1479ce72-477d-4b9c-9b7e-ddb3ce08bc2d",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "47d71bbd-11aa-4572-844a-f44b1a80468a",
  "sourceToolAssistantUUID": "1479ce72-477d-4b9c-9b7e-ddb3ce08bc2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T05:36:19.507Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0117pb63vZNzE6w1V7nPgJsj`</summary>

```json
{
  "query": "OpenVLA-OFT paper training details \"8 GPUs\" hours steps LIBERO 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d71bbd-11aa-4572-844a-f44b1a80468a",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vH6je9kzuMAs6W9ryw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42bab928-33fe-49b0-b181-5778436314ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgLyo9qDHS4pgZbY99yrZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 889,
      "cache_creation_input_tokens": 1898,
      "cache_read_input_tokens": 10518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1898,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T05:36:20.434Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WBQtokJidf42jFxUdZBAjo`</summary>

```json
{
  "query": "OpenPi VLA training cost GPU hours Physical Intelligence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42bab928-33fe-49b0-b181-5778436314ca",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vH6je9kzuMAs6W9ryw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31372d49-5f1a-405d-bcb7-a19b5ffbe9b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgLyo9qDHS4pgZbY99yrZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 889,
      "cache_creation_input_tokens": 1898,
      "cache_read_input_tokens": 10518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1898,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T05:36:20.744Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NcFDDdGkyuN7YLZqwDpkcM`</summary>

```json
{
  "query": "LeRobot framework VLA training compatible OpenVLA SmolVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31372d49-5f1a-405d-bcb7-a19b5ffbe9b9",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vH6je9kzuMAs6W9ryw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1250c1f-1e4b-4188-b5cf-5deb76191d41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgLyo9qDHS4pgZbY99yrZB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 889,
      "cache_creation_input_tokens": 1898,
      "cache_read_input_tokens": 10518,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1898
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 889,
          "output_tokens": 170,
          "cache_read_input_tokens": 10518,
          "cache_creation_input_tokens": 1898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1898,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T05:36:26.213Z_

<details><summary>↩ Tool result · `toolu_0117pb63vZNzE6w1V7nPgJsj`</summary>

```text
Web search results for query: "OpenVLA-OFT paper training details "8 GPUs" hours steps LIBERO 2025"

Links: [{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"GitHub - OpenDriveLab/UniVLA: [RSS 2025] Learning to Act Anywhere with Task-centric Latent Actions · GitHub","url":"https://github.com/OpenDriveLab/UniVLA"},{"title":"openvla-oft/README.md at main · moojink/openvla-oft","url":"https://github.com/moojink/openvla-oft/blob/main/README.md"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation.","url":"https://github.com/openvla/openvla?tab=readme-ov-file"}]

Based on the search results for the OpenVLA-OFT paper training details:

## OpenVLA-OFT Training Details

**GPU Requirements:** You can use 4 or 8 GPUs if possible, though you can use fewer GPUs and enable gradient accumulation; the training runs will just take longer.

**GPU Memory:** For LIBERO training with 2 input images (third-person + wrist camera) + proprioceptive state, 7 action dimensions, action chunk size 8, batch size 8 per device, you need 62.5 GB GPU memory with the default bfloat16 data type.

**Training Hours on 8 GPUs:** The search results reference historical training data from earlier OpenVLA work: The full fine-tuning runs of OpenVLA using 8 A100 GPUs took 5-15 hours per task (depending on the dataset size) to achieve high performance.

**LIBERO Results:** OpenVLA-OFT achieves SOTA results in LIBERO with 97.1% average success rate across 4 task suites.

For more detailed training specifications including exact optimization steps and hours for the specific OFT recipe, you may want to consult the full paper directly (arXiv:2502.19645) or the project's LIBERO.md documentation in the GitHub repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42bab928-33fe-49b0-b181-5778436314ca",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "35389025-7bb4-4c33-9f3c-17f33f956882",
  "sourceToolAssistantUUID": "42bab928-33fe-49b0-b181-5778436314ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T05:36:28.060Z_

<details><summary>↩ Tool result · `toolu_01NcFDDdGkyuN7YLZqwDpkcM`</summary>

```text
Web search results for query: "LeRobot framework VLA training compatible OpenVLA SmolVLA"

Links: [{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"SmolVLA — RoboVerse 0.1.0 documentation","url":"https://roboverse.wiki/roboverse_learn/imitation_learning/smolvla"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/guides/vla-models-comparison"},{"title":"GitHub - huggingface/VLAb · GitHub","url":"https://github.com/huggingface/VLAb"},{"title":"Generalist Robot Policy Evaluation in Simulation with NVIDIA Isaac Lab-Arena and LeRobot","url":"https://huggingface.co/blog/nvidia/generalist-robotpolicy-eval-isaaclab-arena-lerobot"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"}]

Based on the search results, here's what I found about the LeRobot framework's VLA training compatibility with OpenVLA and SmolVLA:

## LeRobot Framework Overview

LeRobot is a platform designed to make real-world robotics more accessible for everyone. It provides pre-trained models, datasets, and tools in PyTorch and focuses on state-of-the-art approaches in imitation learning and reinforcement learning.

## SmolVLA Training Compatibility

SmolVLA is a lightweight Vision-Language-Action (VLA) model from Hugging Face's LeRobot framework that provides a faster and more efficient alternative to larger VLA models like OpenVLA. SmolVLA uses the same LeRobot data format as the pi0 models, enabling data reuse between these implementations.

SmolVLA is trained on the open community LeRobot dataset and truly embodies the power of open-source collaboration, with performance that matches or exceeds larger proprietary models.

## Data Format Compatibility

Importantly, LeRobot format is HuggingFace's format for SmolVLA and the LeRobot training framework, where each episode is stored as a Parquet file with synchronized image and action columns, plus a metadata JSON file. In contrast, RLDS (Reinforcement Learning Datasets) is the standard for Open X-Embodiment models used by Octo, OpenVLA, and RT-2, where each episode is stored as a sequence of (observation, action, reward) tuples in TFRecord format.

The LeRobot framework is specifically optimized for training SmolVLA and other compatible VLA models using the LeRobot data format rather than OpenVLA's RLDS format.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1250c1f-1e4b-4188-b5cf-5deb76191d41",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "addea984-1ce9-4646-8415-d8d1a92c6f0f",
  "sourceToolAssistantUUID": "c1250c1f-1e4b-4188-b5cf-5deb76191d41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T05:36:28.902Z_

<details><summary>↩ Tool result · `toolu_01WBQtokJidf42jFxUdZBAjo`</summary>

```text
Web search results for query: "OpenPi VLA training cost GPU hours Physical Intelligence"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"OpenPI - Open Source Vision-Language-Action Model Library","url":"https://www.openpi.net/english.html"},{"title":"openpi/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/README.md"},{"title":"GitHub - Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi?tab=readme-ov-file"},{"title":"GitHub - Tonghe-Zhang/openpi-physical-intelligence · GitHub","url":"https://github.com/Tonghe-Zhang/openpi-physical-intelligence"},{"title":"GitHub - Merlyn-Labs/openpi: VLA training code for BEHAVIOR-1K challenge - fork of Physical Intelligence openpi repurposed for the challenge and including our specific contributions (proprioceptive dropout, receding horizon control, task embeddings, etc.) · GitHub","url":"https://github.com/Merlyn-Labs/openpi"},{"title":"GitHub - gist-ailab/contact-openpi · GitHub","url":"https://github.com/gist-ailab/contact-openpi"},{"title":"Physical-Intelligence/openpi | DeepWiki","url":"https://deepwiki.com/Physical-Intelligence/openpi"},{"title":"GitHub - allenzren/open-pi-zero: Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence · GitHub","url":"https://github.com/allenzren/open-pi-zero"},{"title":"GitHub - chancharikmitra/openpi_robotv · GitHub","url":"https://github.com/chancharikmitra/openpi_robotv"}]

Based on the search results, I found information about OpenPi VLA training. Here's what I discovered:

## Training Time and GPU Hours

Training takes roughly 1.5-2 days on one L40 node (per-GPU batch size 16 and thus gradient accumulation step 8), or 8-12 hours with H100s (batch size 32). This information comes from a re-implementation of the π₀ model, which provides concrete estimates of GPU compute requirements.

## Training Data

The base model checkpoints have been pre-trained on 10k+ hours of robot data, and the open-source implementation is described as an approximate open-source implementation of the training pipeline used to train pi0-FAST-DROID.

## GPU Requirements

torch.compile, bfloat16, and 8-bit optimizer were used to reduce VRAM usage (peak 40GB with batch size 16). The training can be configured to use multiple GPUs with model parallelism to reduce per-GPU memory requirements by configuring fsdp_devices in the training config.

The search results don't provide specific total GPU hour costs or pricing information, but the timing estimates show that training is feasible on modern GPUs within a reasonable timeframe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31372d49-5f1a-405d-bcb7-a19b5ffbe9b9",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "ffc2d939-fe62-496b-b3eb-3136638a3543",
  "sourceToolAssistantUUID": "31372d49-5f1a-405d-bcb7-a19b5ffbe9b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T05:36:31.873Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01STt9WqdKu7CWNPGfYiYC6t`</summary>

```json
{
  "query": "OpenVLA-OFT arxiv 2502.19645 training time wall clock hours per run"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffc2d939-fe62-496b-b3eb-3136638a3543",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vJ9fnJeD4Ykt3RjRyT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e995415f-2935-4e3d-a1ad-d2184af82b07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCbcQSAytr5d66GcD8ikxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 12416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2711,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T05:36:32.800Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015uCq58cBDDUFSQdmGsurDa`</summary>

```json
{
  "query": "LIBERO-Plus evaluation simulation time rollouts per task episodes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e995415f-2935-4e3d-a1ad-d2184af82b07",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vJ9fnJeD4Ykt3RjRyT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75a49825-0902-4a71-9e2d-23906a926f87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCbcQSAytr5d66GcD8ikxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 12416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2711,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T05:36:33.370Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C5HwJ3W8bbSGJXDEk5cM43`</summary>

```json
{
  "query": "OpenPi fine-tuning single task hours \"8 hours\" OR \"12 hours\" OR \"24 hours\" GPU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75a49825-0902-4a71-9e2d-23906a926f87",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vJ9fnJeD4Ykt3RjRyT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e50bf26-1fe7-4d89-ad3d-e63fe7c8c700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCbcQSAytr5d66GcD8ikxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 12416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2711,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T05:36:36.205Z_

<details><summary>↩ Tool result · `toolu_01STt9WqdKu7CWNPGfYiYC6t`</summary>

```text
Web search results for query: "OpenVLA-OFT arxiv 2502.19645 training time wall clock hours per run"

Links: [{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2502.19645"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"},{"title":"openvla-oft/README.md at main · moojink/openvla-oft","url":"https://github.com/moojink/openvla-oft/blob/main/README.md"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"},{"title":"Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action Models","url":"https://arxiv.org/html/2509.23655v1"}]

Based on the search results, I found the training time information for OpenVLA-OFT from the arxiv paper 2502.19645:

For the OpenVLA-OFT training, each training job was run with 8 A100 or H100 GPUs with 80 GB memory and trained for 50K to 150K gradient steps, depending on the fine-tuning dataset size, which took 1-2 days.

Converting this to wall clock hours per run: **1-2 days translates to approximately 24-48 hours per training run** on 8 GPUs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e995415f-2935-4e3d-a1ad-d2184af82b07",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "95357c85-07a3-4235-958d-b7b82e6dafe2",
  "sourceToolAssistantUUID": "e995415f-2935-4e3d-a1ad-d2184af82b07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T05:36:38.024Z_

<details><summary>↩ Tool result · `toolu_015uCq58cBDDUFSQdmGsurDa`</summary>

```text
Web search results for query: "LIBERO-Plus evaluation simulation time rollouts per task episodes"

Links: [{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"Post-train on LIBERO Benchmark · Issue #30 · Robbyant/lingbot-va","url":"https://github.com/Robbyant/lingbot-va/issues/30"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"}]

Based on the search results, here's what I found regarding LIBERO-Plus evaluation parameters:

## LIBERO-Plus Evaluation Parameters

For reproducible benchmarking, LIBERO-Plus uses 10 episodes per task across all four standard suites (Spatial, Object, Goal, Long), which gives 400 total episodes and matches the protocol used for published results.

### Standard Evaluation Command

The evaluation command across the four standard suites uses 10 episodes per task with the following structure: `lerobot-eval --env.type=libero_plus --env.task=libero_spatial,libero_object,libero_goal,libero_10 --eval.batch_size=1 --eval.n_episodes=10 --env.max_parallel_tasks=1`

### Configurable Parameters

The `--eval.batch_size` controls how many environments run in parallel, and `--eval.n_episodes` sets how many episodes to run per task.

### LIBERO-Plus Specific Note

The evaluation method for LIBERO-Plus is almost identical to LIBERO, with the only required modification being to adjust `num_trials_per_task` from 50 to 1 in the configuration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75a49825-0902-4a71-9e2d-23906a926f87",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "3189a18c-0d3d-4563-8a7d-92d2acc7b91a",
  "sourceToolAssistantUUID": "75a49825-0902-4a71-9e2d-23906a926f87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T05:36:38.992Z_

<details><summary>↩ Tool result · `toolu_01C5HwJ3W8bbSGJXDEk5cM43`</summary>

```text
Web search results for query: "OpenPi fine-tuning single task hours "8 hours" OR "12 hours" OR "24 hours" GPU"

Links: [{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"GitHub - ntini773/OpenPI-finetuning","url":"https://github.com/ntini773/OpenPI-finetuning"},{"title":"GitHub - peek-robot/openpi: Pi0 training/inference code for PEEK · GitHub","url":"https://github.com/peek-robot/openpi"},{"title":"GitHub - gist-ailab/contact-openpi · GitHub","url":"https://github.com/gist-ailab/contact-openpi"},{"title":"[Feature Proposal] Add LoRA training support for pi0.5 (PyTorch backend) · Issue #842 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/842"},{"title":"GitHub - chancharikmitra/openpi_robotv · GitHub","url":"https://github.com/chancharikmitra/openpi_robotv"},{"title":"openpi/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/README.md"},{"title":"Fine-Tuning Open Source Models - Research Computing Resources","url":"https://rcpedia.stanford.edu/blog/2025/11/07/fine-tuning-open-source-models/"},{"title":"Trendshift - Ask AI","url":"https://trendshift.io/admin/repository/ask-ai/12902"}]

I've performed the web search for information about OpenPi fine-tuning with specific time parameters. Based on the search results, I found relevant information about OpenPi fine-tuning, though the specific time durations you mentioned (8 hours, 12 hours, or 24 hours) don't appear explicitly in these results.

The search results show that:

OpenPI can use either single-GPU LoRA or multi-GPU FSDP based on GPU count, and this implementation enables high-performance fine-tuning on a single GPU. 

The documentation indicates that you will need an NVIDIA GPU with at least specific specifications, with estimations assuming a single GPU, but you can also use multiple GPUs with model parallelism to reduce memory requirements.

However, the specific training time estimates (8, 12, or 24 hours for single-task fine-tuning) are not mentioned in the available search results. If you need more detailed information about training time estimates for specific tasks or GPU configurations, you may want to check the official OpenPI repository documentation or training configuration files directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e50bf26-1fe7-4d89-ad3d-e63fe7c8c700",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "de07d465-9aa8-4e92-ab9d-840f2ec62a62",
  "sourceToolAssistantUUID": "8e50bf26-1fe7-4d89-ad3d-e63fe7c8c700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T05:36:42.776Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QyLVhfovPp1Ct2RirTRrgp`</summary>

```json
{
  "query": "OpenVLA-OFT LIBERO training \"150K steps\" OR \"100K steps\" time hours 8 A100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de07d465-9aa8-4e92-ab9d-840f2ec62a62",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vJtnrhiFSUJWRtuaPe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6df13fe4-81b0-44d0-93cc-fd6d32bba88f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWMUp4Mq6eRhHbctujztvh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 15127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3326,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T05:36:43.141Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ut9ycYf7qMhoyV57ozzQc`</summary>

```json
{
  "query": "SmolVLA fine-tuning \"4 hours\" single GPU LIBERO evaluation benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6df13fe4-81b0-44d0-93cc-fd6d32bba88f",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vJtnrhiFSUJWRtuaPe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c68faa2-c8f0-4a2f-b281-3844e630e373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWMUp4Mq6eRhHbctujztvh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 15127,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3326
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 15127,
          "cache_creation_input_tokens": 3326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3326,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T05:36:47.110Z_

<details><summary>↩ Tool result · `toolu_01QyLVhfovPp1Ct2RirTRrgp`</summary>

```text
Web search results for query: "OpenVLA-OFT LIBERO training "150K steps" OR "100K steps" time hours 8 A100"

Links: [{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"METAVLA: UNIFIED META CO-TRAINING FOR EFFI","url":"https://openreview.net/pdf/632eabbeb75425035a6f42fc50ac3f7e59644d7d.pdf"},{"title":"MetaVLA: Unified Meta Co-Training for Efficient Embodied Adaptation","url":"https://arxiv.org/html/2510.05580"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting","url":"https://arxiv.org/html/2507.05116v3"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"OpenVLA · OFT | Konnex Docs","url":"https://docs.konnex.world/supported-ai-models/openvla-oft"}]

Based on the search results, I found relevant information about OpenVLA-OFT training time on LIBERO with 8 A100 GPUs:

OpenVLA-OFT training runs with 8 A100 or H100 GPUs with 80 GB memory and trains for 50K to 150K gradient steps, depending on the fine-tuning dataset size, which took 1-2 days.

More specifically, OpenVLA-OFT requires approximately 24 hours to fine-tune across all four LIBERO suites using 8 A100 80GB GPUs.

Additionally, The 150K checkpoint achieves best performance in all task suites except for LIBERO-Goal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6df13fe4-81b0-44d0-93cc-fd6d32bba88f",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "dacf9ac3-57db-458f-8aa6-5c754edddafa",
  "sourceToolAssistantUUID": "6df13fe4-81b0-44d0-93cc-fd6d32bba88f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T05:36:50.912Z_

<details><summary>↩ Tool result · `toolu_015ut9ycYf7qMhoyV57ozzQc`</summary>

```text
Web search results for query: "SmolVLA fine-tuning "4 hours" single GPU LIBERO evaluation benchmark"

Links: [{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2354"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"fine tune SmolVLA in libero with tensor shape mismatch · Issue #2418 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2418"}]

Based on the search results, here's what I found about SmolVLA fine-tuning with the specifications you mentioned:

SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. The model is 450 million parameters, with approximately 100 million dedicated to the action expert.

Regarding fine-tuning on LIBERO benchmarks, for fine-tuning on simulation benchmarks, the model is trained for 100,000 steps with a batch size of 64, while for real-world tasks, it is fine-tuned for 200,000 steps. However, the model can be trained for a much smaller number of steps without sacrificing significant performance levels.

The paper reports that the 0.45B model achieves success rates of approximately 90%, 96%, 92%, 71% (Spatial, Object, Goal, Long), averaging 87.3% on the LIBERO benchmark.

The search results don't contain specific information about a "4 hours" fine-tuning time on a single GPU. The training specifications mentioned in the paper focus on step counts and batch sizes rather than wall-clock training time. For detailed information about the exact timing, you may want to check the full SmolVLA paper or the official HuggingFace LeRobot documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c68faa2-c8f0-4a2f-b281-3844e630e373",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "3ca27413-8b71-4b6e-b471-26e4f9358dfb",
  "sourceToolAssistantUUID": "9c68faa2-c8f0-4a2f-b281-3844e630e373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T05:36:54.289Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ecz8D9UZCLwv37mfwog5LB`</summary>

```json
{
  "query": "\"token pruning\" VLA vision-language-action model efficiency inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ca27413-8b71-4b6e-b471-26e4f9358dfb",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vKmiEm8qgrmjXrXUVm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a725c291-1ee4-4c87-9f15-782aa46c35fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rGVRn4Ke94LSfPEuN2h38",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 18453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1729,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T05:36:54.979Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MJNydyvbvZNuh9iaKC1EzQ`</summary>

```json
{
  "query": "OpenPi pi0 fine-tuning LIBERO time GPU \"single GPU\" OR \"4 GPU\" hours training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a725c291-1ee4-4c87-9f15-782aa46c35fc",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vKmiEm8qgrmjXrXUVm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8bd96d4-29af-4414-81dd-bb09e18f1bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rGVRn4Ke94LSfPEuN2h38",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 18453,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1729
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 18453,
          "cache_creation_input_tokens": 1729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1729,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T05:37:01.183Z_

<details><summary>↩ Tool result · `toolu_01MJNydyvbvZNuh9iaKC1EzQ`</summary>

```text
Web search results for query: "OpenPi pi0 fine-tuning LIBERO time GPU "single GPU" OR "4 GPU" hours training"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"GitHub - Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi?tab=readme-ov-file"},{"title":"GitHub - ntini773/OpenPI-finetuning","url":"https://github.com/ntini773/OpenPI-finetuning"},{"title":"GitHub - gist-ailab/contact-openpi · GitHub","url":"https://github.com/gist-ailab/contact-openpi"},{"title":"[Feature Proposal] Add LoRA training support for pi0.5 (PyTorch backend) · Issue #842 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/842"},{"title":"openpi/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/README.md"},{"title":"GitHub - chancharikmitra/openpi_robotv · GitHub","url":"https://github.com/chancharikmitra/openpi_robotv"},{"title":"question about lora fine-tuning for pi0.5 · Issue #672 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/672"},{"title":"GitHub - qrafty-ai/pi-openpi: OpenPIE - Open source Pi0 implementation with RECAP training · GitHub","url":"https://github.com/qrafty-ai/pi-openpi"}]

Based on the web search results, I found information about OpenPi π₀ fine-tuning on LIBERO, though the specific training time data you're looking for (in hours for single GPU vs 4 GPU) is not explicitly provided in the search results.

Here's what I found about OpenPi fine-tuning on LIBERO:

**Fine-tuning Configuration:**
The OpenPi project provides example fine-tuning configs for π₀, π₀-FAST, and π₀.₅ on LIBERO data.

**GPU Setup:**
The estimations assume a single GPU, but you can also use multiple GPUs with model parallelism to reduce per-GPU memory requirements by configuring fsdp_devices in the training config. The system picks single-GPU LoRA vs multi-GPU FSDP based on GPU count.

**Training Details:**
To fine-tune a base model on your own data, you need to define configs for data processing and training, with a TrainConfig that defines fine-tuning hyperparameters, data config, and weight loader.

However, the specific training times (e.g., "X hours on single GPU" or "Y hours on 4 GPUs") are not documented in the available search results. For exact training time benchmarks, you may need to check the official OpenPI GitHub repository directly or the LIBERO README that the documentation references.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8bd96d4-29af-4414-81dd-bb09e18f1bb1",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "cf33b25b-6747-4f83-91ef-800d14fa483c",
  "sourceToolAssistantUUID": "b8bd96d4-29af-4414-81dd-bb09e18f1bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T05:37:03.302Z_

<details><summary>↩ Tool result · `toolu_01Ecz8D9UZCLwv37mfwog5LB`</summary>

```text
Web search results for query: ""token pruning" VLA vision-language-action model efficiency inference"

Links: [{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/html/2602.20566"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"[2602.20566] BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/abs/2602.20566"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"}]

Based on the search results, here's an overview of token pruning for Vision-Language-Action (VLA) models and inference efficiency:

## Token Pruning for VLA Models

Token pruning (keeping salient visual tokens and dropping redundant ones) has emerged as an effective approach for accelerating Vision-Language Models (VLMs), offering a solution for efficient VLA.

### How Token Pruning Works

During forward inference, visual tokens are scored based on importance metrics, and less informative tokens are pruned to reduce computation. This pruning can occur either before entering the LLM backbone or within its internal layers.

### Key Challenge: The Dual-System Nature of VLAs

A critical limitation of adapting standard token pruning methods to VLAs is that these VLM-specific token pruning methods select tokens based solely on semantic salience metrics (e.g., prefill attention), while overlooking the VLA's intrinsic dual-system nature of high-level semantic understanding and low-level action execution.

### Recent Methods

Several recent approaches have been developed to address these challenges:

1. **VLA-Pruner**: VLA-Pruner employs a dual-objective importance criterion that integrates semantic-level relevance and action-level importance. Based on this, the proposed dual-level token selection strategy adaptively retains visual tokens.

2. **LightVLA**: Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously. Specifically, LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.6% improvement in task success rate.

3. **BFA++**: BFA++ introduces a hierarchical pruning strategy guided by two-level importance predictors: an intra-view predictor highlights task-relevant regions within each image to suppress spatial noise, while an inter-view predictor identifies critical camera views throughout different manipulation phases to reduce cross-view redundancy.

4. **VLA-IAP**: VLA-IAP (Interaction-Aligned Pruning), introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on interaction dynamics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a725c291-1ee4-4c87-9f15-782aa46c35fc",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "c0b5e1b7-d822-4978-8430-488f09eaf787",
  "sourceToolAssistantUUID": "a725c291-1ee4-4c87-9f15-782aa46c35fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T05:37:06.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NQde6DJ1oLD7xJ4ttfBkga`</summary>

```json
{
  "query": "VLA-Pruner LightVLA training cost \"fine-tuning\" hours GPU token pruning heads"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0b5e1b7-d822-4978-8430-488f09eaf787",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vLgyFyDDKcRtmLLsWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1371ef17-2371-47eb-8776-d08bd3617964",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016kEUiVNwVCE9wY46heQGWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 838,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 20182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T05:37:07.456Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B5WQNFvGUiqnwopj5CN7PJ`</summary>

```json
{
  "query": "LIBERO simulation evaluation speed rollouts per hour GPU time 10000 tasks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1371ef17-2371-47eb-8776-d08bd3617964",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vLgyFyDDKcRtmLLsWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d72a7e74-768f-4128-bb0c-196f3353ba97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016kEUiVNwVCE9wY46heQGWr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 838,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 20182,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 838,
          "output_tokens": 126,
          "cache_read_input_tokens": 20182,
          "cache_creation_input_tokens": 1291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1291,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T05:37:13.789Z_

<details><summary>↩ Tool result · `toolu_01B5WQNFvGUiqnwopj5CN7PJ`</summary>

```text
Web search results for query: "LIBERO simulation evaluation speed rollouts per hour GPU time 10000 tasks"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"Libero performance evaluation on simulation envrionment · Issue #136 · NVIDIA/Isaac-GR00T","url":"https://github.com/NVIDIA/Isaac-GR00T/issues/136"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"}]

Based on the web search results, I found relevant information about LIBERO simulation evaluation. Here's what I discovered:

OpenVLA-OFT achieves 26x faster action generation speed and 3x lower latency than the base OpenVLA model through parallel decoding and action chunking when evaluating on LIBERO tasks.

Regarding evaluation details, the agent's average success rate is evaluated over 20 test rollout trajectories of a maximum length of 600 every 5 epochs.

For GPU memory requirements on LIBERO tasks, LIBERO with 1 input image (third-person camera), 7 action dimensions, action chunk size 8, batch size 1 requires 25.6 GB GPU memory, while inference on the same configuration requires 15.9 GB.

However, the search results don't contain specific information about rollouts per hour, the exact performance metrics for 10,000 tasks, or more detailed GPU timing specifications matching your exact query. If you need more specific metrics about simulation speed (rollouts per hour) or evaluation performance on 10,000 tasks, you may want to check the original LIBERO paper or more recent technical documentation from the LIBERO team.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d72a7e74-768f-4128-bb0c-196f3353ba97",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "c831cd42-a4bf-4e5b-b5f4-38c7541988b4",
  "sourceToolAssistantUUID": "d72a7e74-768f-4128-bb0c-196f3353ba97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T05:37:14.132Z_

<details><summary>↩ Tool result · `toolu_01NQde6DJ1oLD7xJ4ttfBkga`</summary>

```text
Web search results for query: "VLA-Pruner LightVLA training cost "fine-tuning" hours GPU token pruning heads"

Links: [{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449v1"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"LightVLA","url":"https://liauto-research.github.io/LightVLA/"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration | OpenReview","url":"https://openreview.net/forum?id=RwdGIIjPlC"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"[2506.12723] SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/abs/2506.12723"}]

I found information about both LightVLA and VLA-Pruner. Here's what the search results reveal:

## LightVLA

LightVLA is a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. LightVLA addresses efficiency challenges through adaptive, performance-driven pruning of visual tokens using dynamic queries and Gumbel softmax for differentiable token selection. Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously.

LightVLA requires no heuristic "magic numbers" and introduces no additional trainable parameters, making it compatible with modern inference frameworks. LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.9% improvement in task success rate.

## VLA-Pruner

VLA-Pruner is a versatile plug-and-play VLA-specific token pruning method that aligns with the dual-system nature of VLA models. It adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention for action-level importance, proposing a novel dual-level token selection strategy that adaptively preserves a compact, informative set of visual tokens for both semantic understanding and action execution under given compute budget.

Even at a 12.5% retention ratio, VLA-Pruner maintains 88.9% and 88.27% relative accuracy on OpenVLA and OpenVLA-OFT, respectively.

However, the search results do not contain specific information about training costs in terms of fine-tuning hours or GPU requirements for either method.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1371ef17-2371-47eb-8776-d08bd3617964",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "17380502-b29b-427c-b454-079d3d884f03",
  "sourceToolAssistantUUID": "1371ef17-2371-47eb-8776-d08bd3617964",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T05:37:17.172Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011LE4wadRwYc4nRDEH6TF8c`</summary>

```json
{
  "query": "LightVLA arxiv 2509.12594 training details fine-tuning steps GPU cost"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17380502-b29b-427c-b454-079d3d884f03",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vMV1hWmt7tUcRF7tbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7eb67798-667f-4361-a943-ac415ab9e2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZG6jo9KpEP81FwqexGHvU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 811,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 21473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T05:37:18.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nrp1vtsNaZrjCYhEnmaFmZ`</summary>

```json
{
  "query": "OpenVLA-OFT LIBERO four suites fine-tune separately each suite training runs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eb67798-667f-4361-a943-ac415ab9e2ae",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vMV1hWmt7tUcRF7tbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0e7c3da-bc9b-4166-b640-aeea27330716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZG6jo9KpEP81FwqexGHvU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 811,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 21473,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 811,
          "output_tokens": 128,
          "cache_read_input_tokens": 21473,
          "cache_creation_input_tokens": 2019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2019,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T05:37:22.529Z_

<details><summary>↩ Tool result · `toolu_011LE4wadRwYc4nRDEH6TF8c`</summary>

```text
Web search results for query: "LightVLA arxiv 2509.12594 training details fine-tuning steps GPU cost"

Links: [{"title":"Understanding the Performance and Estimating the Cost of LLM Fine-Tuning","url":"https://arxiv.org/html/2408.04693v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"The Complete Guide to GPU Requirements for LLM Fine-Tuning | Runpod Blog","url":"https://www.runpod.io/blog/llm-fine-tuning-gpu-guide"},{"title":"A Study of Optimizations for Fine-tuning Large Language Models","url":"https://arxiv.org/html/2406.02290v2"},{"title":"LoHan: Low-Cost High-Performance Framework to Fine-Tune 100B Model on a Consumer GPU","url":"https://arxiv.org/html/2403.06504v2"},{"title":"[2408.04693] Understanding the Performance and Estimating the Cost of LLM Fine-Tuning","url":"https://arxiv.org/abs/2408.04693"},{"title":"[2403.06504] LoHan: Low-Cost High-Performance Framework to Fine-Tune 100B Model on a Consumer GPU","url":"https://arxiv.org/abs/2403.06504"},{"title":"[2509.12229] Profiling LoRA/QLoRA Fine-Tuning Efficiency on Consumer GPUs: An RTX 4060 Case Study","url":"https://arxiv.org/abs/2509.12229"},{"title":"Profiling LoRA/QLoRA Fine-Tuning Efficiency on Consumer GPUs: An RTX 4060 Case Study","url":"https://arxiv.org/html/2509.12229v1"}]

I found the LightVLA paper (arxiv 2509.12594). Here's what the search revealed about the paper:

LightVLA is a differentiable token pruning framework for vision-language-action (VLA) models that uses dynamic queries to evaluate visual token importance and Gumbel softmax for differentiable token selection, learning through fine-tuning to preserve the most informative visual tokens while pruning others.

However, the search results don't contain the specific training details you're looking for, such as the exact number of fine-tuning steps, specific GPU costs, or detailed hardware requirements for training LightVLA. The search results show the abstract and general overview of the paper, but not the detailed experimental setup and training specifications sections that would typically contain this information.

To find those specific details, you would need to access the full PDF of the paper on arxiv.org/abs/2509.12594 or arxiv.org/html/2509.12594 and look at the experimental setup or appendix sections where training hyperparameters and computational requirements are typically documented.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eb67798-667f-4361-a943-ac415ab9e2ae",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "ff2f805a-e38e-4eb6-b9b2-52ce40cb899c",
  "sourceToolAssistantUUID": "7eb67798-667f-4361-a943-ac415ab9e2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T05:37:24.073Z_

<details><summary>↩ Tool result · `toolu_01Nrp1vtsNaZrjCYhEnmaFmZ`</summary>

```text
Web search results for query: "OpenVLA-OFT LIBERO four suites fine-tune separately each suite training runs"

Links: [{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"}]

Based on the search results, here's what I found about OpenVLA-OFT and fine-tuning on LIBERO's four suites:

## Fine-Tuning Approach

OpenVLA is fine-tuned via LoRA on each task suite independently. The four task suites—LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long—each provide 500 expert demonstrations across 10 tasks to assess policy generalization to different spatial layouts, objects, goals, and long-horizon tasks.

## Training Configuration

Training uses 50-150K gradient steps for non-diffusion methods and 100-250K steps for diffusion methods (which converge slower), with a batch size of 64-128 across 8 A100/H100 GPUs. Checkpoints are tested every 50K steps and the best performance for each run is reported.

## Performance Results

The results of this separate fine-tuning approach are impressive: OpenVLA-OFT achieves 97.1% average success rate across 4 task suites, outperforming π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0e7c3da-bc9b-4166-b640-aeea27330716",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a2998830578fb4646",
  "type": "user",
  "uuid": "2a641c57-73ee-42d1-8025-6d6edae41868",
  "sourceToolAssistantUUID": "f0e7c3da-bc9b-4166-b640-aeea27330716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-14T05:38:07.417Z_

Now I have enough information to provide a comprehensive analysis. Let me compile my findings.

---

## Summary of Findings

### 1. OpenVLA-OFT Training Cost

Based on the paper (arXiv:2502.19645) and GitHub repository:

- **Hardware**: 8 A100 or H100 GPUs (80GB each)
- **Training steps**: 50K-150K gradient steps (non-diffusion), 100K-250K (diffusion variants)
- **Batch size**: 64-128 across 8 GPUs
- **Wall-clock time**: **24-48 hours per training run** on 8 GPUs
- **Per-suite training**: Each of the 4 LIBERO suites is fine-tuned independently
- **GPU-hours per run**: 8 GPUs x 24-48h = **192-384 GPU-hours per run**

This means fine-tuning OpenVLA-OFT on just ONE LIBERO suite already consumes 192-384 A100-hours. Training on all 4 suites = **768-1536 A100-hours** minimum, for a single configuration.

### 2. LIBERO-Plus Evaluation Cost

LIBERO-Plus has 10,030 tasks across 7 perturbation dimensions and 5 difficulty levels. Each evaluation rollout runs up to 600 steps in simulation. Even at 1 trial per task (the LIBERO-Plus protocol), that is 10,030 rollouts. With model inference on a GPU (inference requires ~16-26 GB VRAM) and sequential simulation steps, this is a substantial evaluation cost. For a 7B model like OpenVLA-OFT, each rollout likely takes 1-3 minutes depending on parallelization. At ~2 min/rollout, 10,030 tasks would take **~330 GPU-hours** per evaluation pass. Multiple evaluations during hyperparameter tuning multiply this.

### 3. The Critical Budget Discrepancy

The proposed idea claims 2000-3000 A100-hours for "manual mode" with:
- 8 GPUs x 24-48h x 8-12 runs = **1,536-4,608 GPU-hours**

This is actually a reasonable estimate for the proposed work. Now let's check against the user's constraint:

**User constraint: <=200 H100-hours total**

Even being extremely generous:
- A single OpenVLA-OFT fine-tuning run on 8 H100s for 24h = **192 H100-hours** -- this consumes nearly the ENTIRE budget on a SINGLE training run
- Adding token pruning heads adds complexity (extra modules to train), so training time would likely increase
- There is ZERO budget remaining for hyperparameter tuning, ablation studies, evaluation, or multiple configurations
- The LIBERO-Plus evaluation alone (10,030 tasks) would consume additional dozens of GPU-hours per pass

**Verdict: 200 H100-hours is COMPLETELY INSUFFICIENT for the proposed approach with OpenVLA-OFT. The idea's own estimate of 2000-3000 hours is 10-15x the budget. Even a single training run barely fits.**

### 4. Lighter-Weight Alternatives

**SmolVLA** (Hugging Face / LeRobot):
- **450M parameters** (vs 7B for OpenVLA-OFT) -- ~15x smaller
- Fine-tuning: ~4 hours on a single A100 for 20K steps
- Full training for LIBERO benchmarks: 100K steps, batch size 64 -- likely ~20 hours on a single A100 = **~20 GPU-hours per suite**
- All 4 LIBERO suites: ~80 GPU-hours
- Multiple experimental runs (e.g., 3 configs with ablations): feasible within 200 H100-hours
- Performance on LIBERO: 87.3% average (vs 97.1% for OpenVLA-OFT)
- Built on LeRobot framework, open checkpoints available

**OpenPi (pi0)**:
- Fine-tuning takes ~8-12 hours on H100s
- Supports single-GPU LoRA or multi-GPU FSDP
- Base model is ~3B parameters
- Could feasibly do several runs within 200 H100-hours, but less headroom than SmolVLA

### 5. LeRobot Framework Compatibility

- LeRobot is available and actively maintained by Hugging Face
- SmolVLA is **natively supported** in LeRobot
- However, LeRobot uses its own data format (Parquet-based), while OpenVLA/OpenVLA-OFT uses RLDS format (TFRecords)
- OpenVLA-OFT is NOT directly compatible with LeRobot -- it has its own training codebase
- SmolVLA and pi0 models use LeRobot format

### 6. Existing Token Pruning Work for VLAs

Critically, there is already significant prior work on VLA token pruning:
- **LightVLA** (arXiv:2509.12594) -- differentiable token pruning, reduces FLOPs by 59.1%
- **VLA-Pruner** (arXiv:2511.16449) -- dual-level visual token pruning, plug-and-play
- **VLA-IAP** (arXiv:2603.22991) -- training-FREE visual token pruning
- **BFA++** (arXiv:2602.20566) -- hierarchical token pruning for multi-view VLA

This suggests the proposed idea (adding token pruning heads to OpenVLA-OFT) may have significant novelty overlap with existing work.

---

## Conclusion

**The idea FAILS the user's hard constraint of <=200 H100-hours.** Here is why:

1. A single OpenVLA-OFT training run on LIBERO uses ~192-384 GPU-hours on 8 GPUs. That is the ENTIRE budget for just ONE run.
2. The proposed work requires 8-12 experimental runs (different pruning configurations, ablations), which would need 1,536-4,608 GPU-hours.
3. LIBERO-Plus evaluation (10,030 tasks) adds substantial additional cost.
4. The 200 H100-hour budget is 10-15x too small for the proposed approach.

**Viable alternatives that COULD fit in 200 H100-hours:**
- Use **SmolVLA** (450M params, ~20 GPU-hours per LIBERO suite) instead of OpenVLA-OFT
- Use **training-free** pruning methods (VLA-IAP) that require no fine-tuning at all
- Use OpenPi with LoRA fine-tuning on a single GPU (~8-12 hours per run)

Sources:
- [OpenVLA-OFT Paper](https://arxiv.org/html/2502.19645v1)
- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)
- [LIBERO-Plus Paper](https://arxiv.org/html/2510.13626v1)
- [LIBERO-Plus GitHub](https://github.com/sylvestf/LIBERO-plus)
- [SmolVLA Paper](https://arxiv.org/abs/2506.01844)
- [SmolVLA Blog](https://huggingface.co/blog/smolvla)
- [OpenPi GitHub](https://github.com/Physical-Intelligence/openpi)
- [LightVLA (Differentiable Token Pruning)](https://arxiv.org/html/2509.12594v1)
- [VLA-Pruner](https://arxiv.org/abs/2511.16449)
- [VLA-IAP (Training-Free Pruning)](https://arxiv.org/abs/2603.22991v1)
- [BFA++](https://arxiv.org/abs/2602.20566)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a641c57-73ee-42d1-8025-6d6edae41868",
  "isSidechain": true,
  "agentId": "a2998830578fb4646",
  "requestId": "req_011Cb1vNDZJYqU1TeAsL3Yxj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35029747-768e-43c5-90a6-45b8816ae2ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg6myMQRR2C4cfKRb79HtV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2660,
      "cache_read_input_tokens": 23492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2660,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
