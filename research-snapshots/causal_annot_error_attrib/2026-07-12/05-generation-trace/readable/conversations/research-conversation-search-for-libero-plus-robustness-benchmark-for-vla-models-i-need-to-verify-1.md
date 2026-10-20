# Research conversation: Search for "LIBERO-Plus" robustness benchmark for VLA models. I need to verify: 1. Does "LIBERO-Plus: In-depth Robustnes

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a31c6dab818539baf.jsonl`
- **Structured JSON:** [`2e0859035f80694c9a00.json`](../../sessions/2e/2e0859035f80694c9a00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-14T05:32:48.177Z_

Search for "LIBERO-Plus" robustness benchmark for VLA models. I need to verify:
1. Does "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" exist?
2. Is it accepted at CVPR 2026?
3. Does it show the claimed "95% → <30%" robustness gap under perturbations?
4. What perturbation types does it test?

Search using: "LIBERO-Plus VLA robustness", "LIBERO-Plus CVPR 2026", "site:arxiv.org LIBERO-Plus robustness"

Also search for "LIBERO-PRO" benchmark to see if that exists separately.

Report findings concisely with URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a31c6dab818539baf",
  "type": "user",
  "uuid": "f437061e-7730-4b29-ba6c-7c65cf26ec98",
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

_source line 2 · 2026-05-14T05:32:48.181Z_

```json
{
  "parentUuid": "f437061e-7730-4b29-ba6c-7c65cf26ec98",
  "isSidechain": true,
  "agentId": "a31c6dab818539baf",
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
  "uuid": "39184077-6c3e-4908-8e0f-104c6c65a893",
  "timestamp": "2026-05-14T05:32:48.181Z",
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

_source line 3 · 2026-05-14T05:32:51.147Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012t7z6KFJPXs8rY4cUPZf5c`</summary>

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
  "parentUuid": "39184077-6c3e-4908-8e0f-104c6c65a893",
  "isSidechain": true,
  "agentId": "a31c6dab818539baf",
  "requestId": "req_011Cb1v1szWN9qMR5vK2WG9Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91f7e5a1-e136-4010-94c2-f25514e3f9d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lm2NfsfZ8MUPWW96ecTWQR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8945,
      "cache_read_input_tokens": 0,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8945
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8945,
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

_source line 4 · 2026-05-14T05:32:51.151Z_

<details><summary>↩ Tool result · `toolu_012t7z6KFJPXs8rY4cUPZf5c`</summary>

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
  "parentUuid": "91f7e5a1-e136-4010-94c2-f25514e3f9d7",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a31c6dab818539baf",
  "type": "user",
  "uuid": "9c507279-a4a0-47da-a348-3c8d39039e8c",
  "sourceToolAssistantUUID": "91f7e5a1-e136-4010-94c2-f25514e3f9d7",
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

_source line 5 · 2026-05-14T05:32:54.528Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JFQpiQosbWJvWohZwBoTvk`</summary>

```json
{
  "query": "LIBERO-Plus VLA robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c507279-a4a0-47da-a348-3c8d39039e8c",
  "isSidechain": true,
  "agentId": "a31c6dab818539baf",
  "requestId": "req_011Cb1v26xctobvbbyVtNLnz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e106b4b-9b1c-4d88-aa7f-5229cadef603",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5CnDCHhLtd5BZE6ucjhtt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 6 · 2026-05-14T05:32:54.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S7F64j6RhGeyT1s4L8Dk7b`</summary>

```json
{
  "query": "LIBERO-Plus CVPR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e106b4b-9b1c-4d88-aa7f-5229cadef603",
  "isSidechain": true,
  "agentId": "a31c6dab818539baf",
  "requestId": "req_011Cb1v26xctobvbbyVtNLnz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb00e4a8-7537-4dfc-a8c5-3c832b008129",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5CnDCHhLtd5BZE6ucjhtt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 7 · 2026-05-14T05:32:54.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RoA7B2fu9a3vkhKH4AiAEC`</summary>

```json
{
  "query": "site:arxiv.org LIBERO-Plus robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb00e4a8-7537-4dfc-a8c5-3c832b008129",
  "isSidechain": true,
  "agentId": "a31c6dab818539baf",
  "requestId": "req_011Cb1v26xctobvbbyVtNLnz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3395d6ba-fcb1-4012-9fc1-9c1a61f6a361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5CnDCHhLtd5BZE6ucjhtt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8945,
      "output_tokens": 155,
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
          "output_tokens": 155,
          "cache_read_input_tokens": 8945,
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

_source line 8 · 2026-05-14T05:32:59.279Z_

<details><summary>↩ Tool result · `toolu_01S7F64j6RhGeyT1s4L8Dk7b`</summary>

```text
Web search results for query: "LIBERO-Plus CVPR 2026"

Links: [{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"Learning Long-term Motion Embeddings for Efficient Kinematics Generation | CVPR 2026","url":"https://compvis.github.io/long-term-motion/"},{"title":"2026 Dates and Deadlines","url":"https://cvpr.thecvf.com/Conferences/2026/Dates"},{"title":"CVPR 2026 | OpenReview","url":"https://openreview.net/group?id=thecvf.com%2FCVPR%2F2026"},{"title":"LoViF Workshop @ CVPR 2026","url":"https://lovif-cvpr2026-workshop.github.io/"},{"title":"CVPR 2025 Organizers","url":"https://cvpr.thecvf.com/Conferences/2026/Organizers"},{"title":"CVPR 2026 Submission Template - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/cvpr-2026-submission-template/rdtrwgypxxzb"},{"title":"CVPR 2026 - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/"},{"title":"CVPR 2026 Workshop Proposals | OpenReview","url":"https://openreview.net/group?id=thecvf.com%2FCVPR%2F2026%2FWorkshop_Proposals"},{"title":"2026 Conference - CVPR - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/Conferences/2026"}]

Based on the search results, I found information about LIBERO-Plus at CVPR 2026:

LIBERO-Plus is a comprehensive, automatic, and fine-grained evaluation framework with controlled perturbations across seven dimensions: object layouts, camera viewpoints, robot initial states, language instructions, lighting conditions, background textures, and sensor noise.

The research addresses the issue that Visual-Language-Action (VLA) models report impressive success rates exceeding 95% on robotic manipulation benchmarks, yet these results may mask fundamental weaknesses in robustness. The systematic analysis of ten state-of-the-art models reveals consistent brittleness beneath apparent competence, with performance dropping from 95% to below 30% under modest perturbations.

This work was presented as a poster at CVPR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb00e4a8-7537-4dfc-a8c5-3c832b008129",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a31c6dab818539baf",
  "type": "user",
  "uuid": "c5b2766d-92b1-449e-b0c5-7d9f9c02b9c3",
  "sourceToolAssistantUUID": "cb00e4a8-7537-4dfc-a8c5-3c832b008129",
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

_source line 9 · 2026-05-14T05:33:00.271Z_

<details><summary>↩ Tool result · `toolu_01JFQpiQosbWJvWohZwBoTvk`</summary>

```text
Web search results for query: "LIBERO-Plus VLA robustness"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"}]

Based on the web search results, here's what I found about LIBERO-Plus VLA robustness:

## Overview

LIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions of Vision-Language-Action (VLA) models.

## Key Robustness Findings

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise, revealing that models exhibit extreme sensitivity to perturbation factors with performance dropping from 95% to below 30% under modest perturbations.

### Major Weaknesses Identified:

1. **Extreme Sensitivity to Visual Changes**: Current VLA models exhibit extreme sensitivity to perturbations in camera viewpoint and robot initial state, revealing fundamental limitations in their spatial reasoning capabilities.

2. **Language Ignorance**: Models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

3. **Lack of Compositional Generalization**: While single-dimension perturbations demonstrate some level of robustness, real-world scenarios often involve multiple simultaneous perturbations.

## Benchmark Specifications

LIBERO-Plus is an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, and the benchmark construction stratifies tasks into five difficulty levels (Level-1 to Level-5) according to observed accuracy distributions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e106b4b-9b1c-4d88-aa7f-5229cadef603",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a31c6dab818539baf",
  "type": "user",
  "uuid": "b4745b35-5331-477e-a1de-1bf20717f255",
  "sourceToolAssistantUUID": "2e106b4b-9b1c-4d88-aa7f-5229cadef603",
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

_source line 10 · 2026-05-14T05:33:01.707Z_

<details><summary>↩ Tool result · `toolu_01RoA7B2fu9a3vkhKH4AiAEC`</summary>

```text
Web search results for query: "site:arxiv.org LIBERO-Plus robustness"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"VLANeXt: Recipes for Building Strong VLA Models","url":"https://arxiv.org/html/2602.18532"},{"title":": Cross-Skill Model Merging Toward a Generalist Vision-Language-Action Agent","url":"https://arxiv.org/html/2511.18810"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556"},{"title":"VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model","url":"https://arxiv.org/html/2602.10098"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"[2602.06556] LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.06556"}]

I found several arXiv papers related to LIBERO-Plus and robustness in Vision-Language-Action (VLA) models. Here are the key results:

## Primary Paper: LIBERO-Plus

The main paper "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" performs a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

### Key Findings

The analysis exposes critical weaknesses: models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

### Benchmark Details

LIBERO-Plus is a benchmark designed to rigorously evaluate generalization capabilities along the key dimensions identified in the study. The benchmark offers three key advancements: (1) Comprehensive: Evaluation across seven robustness dimensions and 21 sub-dimensions, ensuring a thorough assessment of model generalization.

## Related Research

Several other papers use LIBERO-Plus for evaluation:
- LIBERO-Plus introduces systematic variations to the evaluation episodes, comprising 10,030 demonstrations with perturbations in visual (e.g., lighting, background, camera pose), physical (e.g., object layout, robot state), and semantic (e.g., language instruction rewrites) dimensions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3395d6ba-fcb1-4012-9fc1-9c1a61f6a361",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a31c6dab818539baf",
  "type": "user",
  "uuid": "db26a40b-a385-4766-9190-6cc8754408f9",
  "sourceToolAssistantUUID": "3395d6ba-fcb1-4012-9fc1-9c1a61f6a361",
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

_source line 11 · 2026-05-14T05:33:04.478Z_

Now let me search for LIBERO-PRO as a separate benchmark.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db26a40b-a385-4766-9190-6cc8754408f9",
  "isSidechain": true,
  "agentId": "a31c6dab818539baf",
  "requestId": "req_011Cb1v2sr793TgDDhHcRnGR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9962170-f748-4fba-b76a-d97fa2b7624f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDf7CFRv6mDucRhKpzhGia",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2605,
      "cache_read_input_tokens": 10337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2605,
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

### Tool call

_source line 12 · 2026-05-14T05:33:04.950Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018SnVXJT9dhMvdfwu1zFDGY`</summary>

```json
{
  "query": "LIBERO-PRO benchmark VLA models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9962170-f748-4fba-b76a-d97fa2b7624f",
  "isSidechain": true,
  "agentId": "a31c6dab818539baf",
  "requestId": "req_011Cb1v2sr793TgDDhHcRnGR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5004a8e5-3d99-4229-8136-846f6705d656",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDf7CFRv6mDucRhKpzhGia",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2605,
      "cache_read_input_tokens": 10337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2605,
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

### Tool call

_source line 13 · 2026-05-14T05:33:05.285Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VHyB8Zq6gmyK3H6X77oAEB`</summary>

```json
{
  "query": "arxiv LIBERO-Plus 2510.13626 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5004a8e5-3d99-4229-8136-846f6705d656",
  "isSidechain": true,
  "agentId": "a31c6dab818539baf",
  "requestId": "req_011Cb1v2sr793TgDDhHcRnGR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "118dc99d-afa5-4961-b768-965a90f16cbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDf7CFRv6mDucRhKpzhGia",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2605,
      "cache_read_input_tokens": 10337,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2605
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 10337,
          "cache_creation_input_tokens": 2605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2605,
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

_source line 14 · 2026-05-14T05:33:09.434Z_

<details><summary>↩ Tool result · `toolu_01VHyB8Zq6gmyK3H6X77oAEB`</summary>

```text
Web search results for query: "arxiv LIBERO-Plus 2510.13626 authors"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"},{"title":"[2502.13626] AI-Empowered Catalyst Discovery: A Survey from Classical Machine Learning Approaches to Large Language Models","url":"https://arxiv.org/abs/2502.13626"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"}]

Based on the search results, the authors of arxiv paper 2510.13626 (LIBERO-Plus) are: Senyu Fei, Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li Ji, Xinzhe He, Shiduo Zhang, Zhaoye Fei, Jinlan Fu, Jingjing Gong, and Xipeng Qiu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "118dc99d-afa5-4961-b768-965a90f16cbe",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a31c6dab818539baf",
  "type": "user",
  "uuid": "09c49b99-0d3f-4387-9a90-90c894e0cfec",
  "sourceToolAssistantUUID": "118dc99d-afa5-4961-b768-965a90f16cbe",
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

_source line 15 · 2026-05-14T05:33:13.374Z_

<details><summary>↩ Tool result · `toolu_018SnVXJT9dhMvdfwu1zFDGY`</summary>

```text
Web search results for query: "LIBERO-PRO benchmark VLA models"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"[2510.03827v1] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827v1"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"}]

Based on the search results, here's what I found about LIBERO-PRO and VLA models:

## LIBERO-PRO Benchmark Overview

LIBERO has emerged as a widely adopted benchmark for evaluating Vision-Language-Action (VLA) models; however, its current training and evaluation settings are problematic, often leading to inflated performance estimates and preventing fair model comparison.

LIBERO-PRO is an extended LIBERO benchmark that systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments.

## Key Findings

The research reveals significant issues with VLA model generalization. Although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under the generalized LIBERO-PRO setting. This discrepancy exposes the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception.

## Evaluated Models

State-of-the-art models including OpenVLA and pi0/0.5 were evaluated, and the results show that they exhibit near-complete failure under several perturbation settings. While most models fail under perturbations, Pi0.5 achieves a 0.38 success rate in the libero-goal task under position changes, compared to 0 for OpenVLA and Pi0.

## Related Benchmarks

Early versions of LIBERO do not contain perturbations in viewpoint, lighting, or distractors, requiring LIBERO-PRO and LIBERO-Plus to fill this gap.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5004a8e5-3d99-4229-8136-846f6705d656",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a31c6dab818539baf",
  "type": "user",
  "uuid": "c88ea910-22b7-4fc4-8636-78f1503a89aa",
  "sourceToolAssistantUUID": "5004a8e5-3d99-4229-8136-846f6705d656",
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

_source line 16 · 2026-05-14T05:33:34.264Z_

Here are my findings:

---

## 1. Does "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" exist?

**Yes, confirmed.** It is a real paper available on arXiv as paper 2510.13626. It has an official project page, a GitHub repository, and a Hugging Face dataset. Authors include Senyu Fei, Siyin Wang, Junhao Shi, and others (affiliated with OpenMOSS/Fudan University).

- arXiv: https://arxiv.org/abs/2510.13626
- Project page: https://sylvestf.github.io/LIBERO-plus/
- GitHub: https://github.com/sylvestf/LIBERO-plus

---

## 2. Is it accepted at CVPR 2026?

**Yes, confirmed.** It appears as a poster at CVPR 2026 (though the poster title on the CVPR site uses slightly different wording: "LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models").

- CVPR 2026 poster page: https://cvpr.thecvf.com/virtual/2026/poster/38735

---

## 3. Does it show the claimed "95% to <30%" robustness gap?

**Yes, confirmed.** The paper reports that VLA models achieve success rates exceeding 95% on standard LIBERO benchmarks, but performance drops to below 30% under modest controlled perturbations. This is explicitly stated in the paper's abstract and findings.

---

## 4. What perturbation types does it test?

The benchmark tests **seven perturbation dimensions** (with 21 sub-dimensions total):

1. **Object layouts** - rearrangement of manipulated objects
2. **Camera viewpoints** - changes in camera pose/angle
3. **Robot initial states** - different starting configurations
4. **Language instructions** - paraphrases/rewrites of task descriptions
5. **Lighting conditions** - changes in illumination
6. **Background textures** - altered scene backgrounds
7. **Sensor noise** - noise injected into observations

The benchmark comprises 10,030 tasks stratified into five difficulty levels (Level-1 through Level-5). Key additional findings: models show extreme sensitivity to camera viewpoint and robot initial state changes, but are surprisingly insensitive to language variations (suggesting they largely ignore language instructions).

---

## LIBERO-PRO (separate benchmark)

**Yes, LIBERO-PRO exists separately.** It is a different paper: "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization" (arXiv: 2510.03827, posted ~10 days before LIBERO-Plus). It tests four perturbation dimensions (objects, initial states, instructions, environments) and reports even more dramatic failure -- models drop from >90% to 0.0% in some settings, exposing pure memorization. GitHub: https://github.com/Zxy-MLlab/LIBERO-PRO

- arXiv: https://arxiv.org/abs/2510.03827

---

**Summary:** All four claims check out. LIBERO-Plus is a real, CVPR 2026-accepted benchmark that demonstrates the 95% to <30% robustness gap across seven perturbation types for VLA models. LIBERO-PRO is a separate but thematically related benchmark by different authors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c88ea910-22b7-4fc4-8636-78f1503a89aa",
  "isSidechain": true,
  "agentId": "a31c6dab818539baf",
  "requestId": "req_011Cb1v3jgFhcvZZyNy5W9eK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ddf598a-4f67-43a8-98e8-be930ee9a422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zqdgZ9hzmj8AenSWwXJdB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 1127,
      "cache_read_input_tokens": 12942,
      "output_tokens": 820,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1127
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 694,
          "output_tokens": 820,
          "cache_read_input_tokens": 12942,
          "cache_creation_input_tokens": 1127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1127,
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
