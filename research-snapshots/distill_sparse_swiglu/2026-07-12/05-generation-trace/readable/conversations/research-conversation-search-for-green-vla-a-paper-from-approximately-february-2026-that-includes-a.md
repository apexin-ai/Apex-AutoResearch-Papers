# Research conversation: Search for "Green-VLA" - a paper from approximately February 2026 that includes a "DataQA" pipeline using heuristic metr

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab68eb3795eb14002.jsonl`
- **Structured JSON:** [`64fe0b5314dffcaa3d17.json`](../../sessions/64/64fe0b5314dffcaa3d17.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-13T11:41:06.874Z_

Search for "Green-VLA" - a paper from approximately February 2026 that includes a "DataQA" pipeline using heuristic metrics for demonstration filtering. I need to:

1. Use WebSearch with queries like "Green-VLA DataQA demonstration filtering 2026", "Green-VLA robot learning data quality", "Green-VLA vision language action"
2. Use WebFetch to read the abstract and key details
3. Report: full title, authors, venue/arXiv date, what DataQA does (heuristic metrics for filtering demonstrations?), and its relevance to principled demo curation.

Try alternative queries if the first ones don't work: "green VLA data quality assurance robot", "efficient VLA data filtering".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ab68eb3795eb14002",
  "type": "user",
  "uuid": "a65de73b-dee5-40be-a085-a1b4e7db29fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T11:41:06.877Z_

```json
{
  "parentUuid": "a65de73b-dee5-40be-a085-a1b4e7db29fa",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
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
  "uuid": "64b8b2b8-2bf6-4a98-8fca-4454102c8083",
  "timestamp": "2026-05-13T11:41:06.877Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T11:41:09.210Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then search for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64b8b2b8-2bf6-4a98-8fca-4454102c8083",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWHxKrVFqUKpvNaSHtx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd58e99f-0243-4fb7-8ebd-ac69c52477e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrfWBdEYXCo4zKANu9mirF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 710,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-13T11:41:09.778Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AjYJxgxX7LNuvTXtd7nYUa`</summary>

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
  "parentUuid": "cd58e99f-0243-4fb7-8ebd-ac69c52477e1",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWHxKrVFqUKpvNaSHtx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a1f9441-45d6-4e02-81dd-9f3ba23e189d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrfWBdEYXCo4zKANu9mirF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 8223,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 710
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 710,
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

_source line 5 · 2026-05-13T11:41:09.790Z_

<details><summary>↩ Tool result · `toolu_01AjYJxgxX7LNuvTXtd7nYUa`</summary>

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
  "parentUuid": "1a1f9441-45d6-4e02-81dd-9f3ba23e189d",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ab68eb3795eb14002",
  "type": "user",
  "uuid": "774dedff-0138-46d0-a84a-bd4bd890176c",
  "sourceToolAssistantUUID": "1a1f9441-45d6-4e02-81dd-9f3ba23e189d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T11:41:12.606Z_



Now let me run multiple search queries in parallel to find the "Green-VLA" paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "774dedff-0138-46d0-a84a-bd4bd890176c",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWJBEz5eTAYQExdrVfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d57d821f-d45f-4378-b05d-22a3aab4c27b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TokYbfvMPoBG7QfB1m8Kov",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-13T11:41:12.680Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01964ejpLqVzeqKVH1SCtcJY`</summary>

```json
{
  "query": "Green-VLA DataQA demonstration filtering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d57d821f-d45f-4378-b05d-22a3aab4c27b",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWJBEz5eTAYQExdrVfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12679063-e1ae-486a-a015-0a132e68ba66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TokYbfvMPoBG7QfB1m8Kov",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-13T11:41:13.078Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018YrpdZjTFDxx8uUj12Zd5M`</summary>

```json
{
  "query": "Green-VLA robot learning data quality 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12679063-e1ae-486a-a015-0a132e68ba66",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWJBEz5eTAYQExdrVfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98b44f21-9229-4d6a-b399-263558f3f0e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TokYbfvMPoBG7QfB1m8Kov",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 9 · 2026-05-13T11:41:13.258Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FrmqHo4K3ihNQvUDT56FWk`</summary>

```json
{
  "query": "Green-VLA vision language action model paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98b44f21-9229-4d6a-b399-263558f3f0e8",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWJBEz5eTAYQExdrVfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36522c0b-4079-4775-a881-1236ce522dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TokYbfvMPoBG7QfB1m8Kov",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8933,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1911
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 173,
          "cache_read_input_tokens": 8933,
          "cache_creation_input_tokens": 1911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1911,
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

_source line 10 · 2026-05-13T11:41:18.311Z_

<details><summary>↩ Tool result · `toolu_01964ejpLqVzeqKVH1SCtcJY`</summary>

```text
Web search results for query: "Green-VLA DataQA demonstration filtering 2026"

Links: [{"title":"Green-VLA: Staged Vision–Language–Action Model for Generalist Robots","url":"https://greenvla.github.io/"},{"title":"Green-VLA: Staged Vision–Language–Action Model for Generalist Robots","url":"https://arxiv.org/pdf/2602.00919"},{"title":"Paper page - Green-VLA: Staged Vision-Language-Action Model for Generalist Robots","url":"https://huggingface.co/papers/2602.00919"},{"title":"VLA Calibration Pipeline 2025.1.0.32; CASA version 6.6.6-17 and Pipeline 2025.1.036; CASA version 6.6.6-18 — NRAO Science Site","url":"https://science.nrao.edu/facilities/vla/data-processing/pipeline"},{"title":"[2602.00919] Green-VLA: Staged Vision-Language-Action Model for Generalist Robots","url":"https://arxiv.org/abs/2602.00919"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"VLA Observational Status Summary 2026B - NRAO","url":"https://science.nrao.edu/facilities/vla/docs/manuals/oss"},{"title":"Vision-Language-Action (VLA) Models: LLMs for robots","url":"https://www.blackcoffeerobotics.com/blog/vision-language-action-vla-models-llms-for-robots"},{"title":"Parallels Between VLA Model Post-Training and Human ...","url":"https://arxiv.org/pdf/2506.20966"}]

Based on the search results, I found relevant information about Green-VLA's DataQA demonstration filtering:

Green-VLA's DataQA pipeline auto-filters 3,000+ hours of demonstrations using jitter, sharpness, diversity, and state variance metrics plus optical-flow alignment to enable stable multi-embodiment training with improved data efficiency.

More specifically, Green-VLA couples a scalable data-processing pipeline of 3,000 hours of demonstrations with temporal alignment and quality filtering, and uses a unified, embodiment-aware action interface enabling a single policy to control humanoids, mobile manipulators, and fixed-base arms.

The work normalizes heterogeneous demonstration speeds via optical-flow–based temporal resampling to align motion statistics across datasets.

The Green-VLA research was published in February 2026, and this quality-filtering approach is a key component of their staged training pipeline designed to improve generalization across diverse robotic embodiments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12679063-e1ae-486a-a015-0a132e68ba66",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ab68eb3795eb14002",
  "type": "user",
  "uuid": "69e1e3bb-2722-49f1-b86d-de971686a204",
  "sourceToolAssistantUUID": "12679063-e1ae-486a-a015-0a132e68ba66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T11:41:19.927Z_

<details><summary>↩ Tool result · `toolu_01FrmqHo4K3ihNQvUDT56FWk`</summary>

```text
Web search results for query: "Green-VLA vision language action model paper"

Links: [{"title":"Paper page - Green-VLA: Staged Vision-Language-Action Model for Generalist Robots","url":"https://huggingface.co/papers/2602.00919"},{"title":"[2602.00919] Green-VLA: Staged Vision-Language-Action Model for Generalist Robots","url":"https://arxiv.org/abs/2602.00919"},{"title":"GitHub - greenvla/GreenVLA: Green-VLA: Staged Vision-Language-Action Model for Generalist Robots · GitHub","url":"https://github.com/greenvla/GreenVLA"},{"title":"Green-VLA: Staged Vision–Language–Action Model for Generalist Robots","url":"https://arxiv.org/pdf/2602.00919"},{"title":"[2505.04769] Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/abs/2505.04769"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"Green-VLA: Staged Vision–Language–Action Model for Generalist Robots","url":"https://greenvla.github.io/"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"}]

Based on the search results, here's what I found about the Green-VLA paper:

## Overview

Green-VLA is a staged Vision-Language-Action (VLA) framework for real-world deployment on the Green humanoid robot while maintaining generalization across diverse embodiments.

## Architecture and Training

Green-VLA follows a five-stage curriculum: (L0) foundational VLMs, (L1) multimodal grounding, (R0) multi-embodiment pretraining, (R1) embodiment-specific adaptation, and (R2) reinforcement-learning (RL) policy alignment.

The framework couples a scalable data-processing pipeline (3,000 hours of demonstrations) with temporal alignment and quality filtering, and uses a unified, embodiment-aware action interface enabling a single policy to control humanoids, mobile manipulators, and fixed-base arms.

## Key Results

The main results of Green-VLA demonstrate that a staged training pipeline emphasizing quality alignment, unified action spaces, and RL refinement outperforms raw scaling approaches across diverse embodiments and benchmarks.

## Model Details

Green-VLA is a ~4B-parameter Vision-Language-Action model built on a staged curriculum, trained on 3,000+ hours of demonstrations.

## Resources

- **Paper**: Available on arXiv (2602.00919)
- **Project Page**: https://greenvla.github.io/
- **Code**: https://github.com/greenvla/GreenVLA
- **Models**: Available on Hugging Face


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36522c0b-4079-4775-a881-1236ce522dcf",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ab68eb3795eb14002",
  "type": "user",
  "uuid": "fd458895-0711-47e2-98fd-a1f3aa1be3f3",
  "sourceToolAssistantUUID": "36522c0b-4079-4775-a881-1236ce522dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T11:41:24.469Z_

<details><summary>↩ Tool result · `toolu_018YrpdZjTFDxx8uUj12Zd5M`</summary>

```text
Web search results for query: "Green-VLA robot learning data quality 2026"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919v1"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"[2602.00919] Green-VLA: Staged Vision-Language-Action Model for Generalist Robots","url":"https://arxiv.org/abs/2602.00919"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"},{"title":"Paper page - Green-VLA: Staged Vision-Language-Action Model for Generalist Robots","url":"https://huggingface.co/papers/2602.00919"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"State of Robot Learning, Q1 2026: What Shipped, What Stalled | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/state-of-robot-learning-q1-2026"},{"title":"Generative AI in Industrial Robotics: 2026 Layers Guide","url":"https://www.evsint.com/generative-ai-industrial-robotics-foundation-models-code-generation-2026/"}]

Based on the search results, here's what I found about Green-VLA and robot learning data quality in 2026:

## Green-VLA Framework

Green-VLA is a framework that moves beyond data scaling by emphasizing quality alignment, action unification, and reinforcement learning refinement. Green-VLA is a staged Vision-Language-Action (VLA) framework for real-world deployment on the Green humanoid robot while maintaining generalization across diverse embodiments, following a five stage curriculum: (L0) foundational VLMs, (L1) multimodal grounding, (R0) multi-embodiment pretraining, (R1) embodiment-specific adaptation, and (R2) reinforcement-learning (RL) policy alignment.

## Data Quality Approach

The framework couples a scalable data-processing pipeline (3,000 hours of demonstrations) with temporal alignment and quality filtering, and uses a unified, embodiment-aware action interface enabling a single policy to control humanoids, mobile manipulators, and fixed-base arms. While the framework is embodiment-agnostic, the primary target platform is the Green humanoid robot, where the system controls 32 DoF of the full upper body (head, torso, dual arms, and dexterous hands) through the unified action interface, requiring coordinated bimanual manipulation, whole upper-body motion, and fine-grained fingertip control.

## Key Innovation: Quality Over Scale

The main results of Green-VLA demonstrate that a staged training pipeline emphasizing quality alignment, unified action spaces, and RL refinement outperforms raw scaling approaches across diverse embodiments and benchmarks. This represents a significant shift in 2026 robot learning, where the empirical consensus for robotics foundation models in 2026 is that efficiency matters more than scale beyond ~7B parameters, with a well-curated 500-demo fine-tune of a 7B VLA outperforming a poorly curated fine-tune of a 70B model on most manipulation benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98b44f21-9229-4d6a-b399-263558f3f0e8",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ab68eb3795eb14002",
  "type": "user",
  "uuid": "d1e7110e-1bd7-4ce3-b7c5-82e940aeb180",
  "sourceToolAssistantUUID": "98b44f21-9229-4d6a-b399-263558f3f0e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-13T11:41:27.959Z_

I found the paper. Now let me fetch the arXiv abstract page and the project page for detailed information about the authors, DataQA pipeline specifics, and heuristic metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1e7110e-1bd7-4ce3-b7c5-82e940aeb180",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWKFWVeeZyGhDvaLt1Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78b30548-af79-4d6c-9ede-5c8c36c875a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dbW6NkwVzGazbB1rLVsxP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 10844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2037,
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

_source line 14 · 2026-05-13T11:41:29.564Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xoiv9StvhuFiW8tB6SM5Q1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.00919",
  "prompt": "Extract the full title, all authors, submission date, and the complete abstract of this paper. Also note any venue information (conference, workshop, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78b30548-af79-4d6c-9ede-5c8c36c875a6",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWKFWVeeZyGhDvaLt1Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8195be2-193a-40bf-a1ff-cab288790106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dbW6NkwVzGazbB1rLVsxP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 10844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2037,
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

_source line 15 · 2026-05-13T11:41:31.789Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JQbAuE4V2syCcR5TzZvzG2`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.00919v1",
  "prompt": "Find and extract all details about the \"DataQA\" pipeline or data quality assurance process. What specific heuristic metrics are used for filtering demonstrations? Look for sections about data processing, data filtering, quality assurance, temporal alignment, jitter, sharpness, diversity, state variance, optical flow. Extract the exact metrics and methodology described."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8195be2-193a-40bf-a1ff-cab288790106",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWKFWVeeZyGhDvaLt1Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d72ddf8-5dce-42dd-964f-61d3353395c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dbW6NkwVzGazbB1rLVsxP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 10844,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 845,
          "output_tokens": 291,
          "cache_read_input_tokens": 10844,
          "cache_creation_input_tokens": 2037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2037,
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

_source line 16 · 2026-05-13T11:41:36.105Z_

<details><summary>↩ Tool result · `toolu_01Xoiv9StvhuFiW8tB6SM5Q1`</summary>

```text
# Paper Information Extract

**Full Title:**
"Green-VLA: Staged Vision-Language-Action Model for Generalist Robots"

**Authors:**
I. Apanasevich, M. Artemyev, R. Babakyan, P. Fedotova, D. Grankin, E. Kupryashin, A. Misailidi, D. Nerus, A. Nutalapati, G. Sidorov, I. Efremov, M. Gerasyov, D. Pikurov, Y. Senchenko, S. Davidenko, D. Kulikov, M. Sultankin, K. Askarbek, O. Shamanin, D. Statovoy, E. Zalyaev, I. Zorin, A. Letkin, E. Rusakov, A. Silchenko, V. Vorobyov, S. Sobolnikov, A. Postnikov (28 authors total)

**Submission Date:**
January 31, 2026 (v1); revised March 7, 2026 (v2)

**Complete Abstract:**
The authors present a staged framework combining vision, language, and action capabilities. Their five-stage approach progresses through foundational models, multimodal grounding, multi-embodiment pretraining, embodiment-specific adaptation, and reinforcement learning alignment. The system processes "3,000 hours of demonstrations" with temporal alignment and quality filtering, enabling a unified policy to control multiple robot types. At inference, safety features include "episode-progress prediction, out-of-distribution detection, and joint-prediction-based guidance." Testing demonstrates "strong generalization and performance gains from RL alignment."

**Venue Information:**
No conference or workshop venue is specified. This is an arXiv preprint in the Robotics (cs.RO) category.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8195be2-193a-40bf-a1ff-cab288790106",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ab68eb3795eb14002",
  "type": "user",
  "uuid": "ef6014c1-4e3f-4252-99eb-2aadcd1c5a72",
  "sourceToolAssistantUUID": "d8195be2-193a-40bf-a1ff-cab288790106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T11:41:38.281Z_

<details><summary>↩ Tool result · `toolu_01JQbAuE4V2syCcR5TzZvzG2`</summary>

```text
# DataQA Pipeline: Quality Assurance Metrics

The Green-VLA framework employs a comprehensive DataQA pipeline for filtering and curating robotic demonstrations. Here are the specific metrics used:

## Primary Filtering Criteria

The system removes problematic episodes based on:
- Missing cameras and frames
- Episodes that are too short or suspiciously long
- Motion activity thresholds ensuring meaningful robot movements

## Quantitative Quality Metrics

**Tremble Score (Jitter Detection):**
The pipeline identifies erratic motions using: `S_tremble = |ṡ_smooth - ṡ| / (|ṡ_smooth| + |ṡ|)`, where ṡ represents velocity trajectory and ṡ_smooth is its Gaussian-smoothed version.

**Sharpness (S_sharp):**
Image quality assessment uses Laplacian standard deviation scores computed on 4×4 pixel blocks, with max-pooling across 16×16 regions to identify sharp versus blurry areas. The median regional sharpness score represents overall episode quality.

**Visual Diversity (D_vis):**
Calculated through DINOv3 feature analysis: `D_vis = E_d[std_t(E_s[f_t,s,d])]`, measuring temporal variance of spatially-averaged feature representations.

**State-Space Diversity (D_state):**
Expressed as: `D_state = √tr(Cov(s))`, the Frobenius norm of the robot state covariance matrix.

## Additional Processing

The pipeline applies trajectory smoothing to reduce high-frequency noise and performs optical flow-based temporal alignment, resampling actions using "monotonic cubic splines to normalize effective motion per step."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d72ddf8-5dce-42dd-964f-61d3353395c6",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ab68eb3795eb14002",
  "type": "user",
  "uuid": "18002afb-6f1b-4d5f-9db3-4cd74aa1e38c",
  "sourceToolAssistantUUID": "5d72ddf8-5dce-42dd-964f-61d3353395c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-13T11:41:41.415Z_

Excellent. Now let me get the project page for any additional details about DataQA and its relevance to demonstration curation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18002afb-6f1b-4d5f-9db3-4cd74aa1e38c",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWLGcW5hwCV58E3CFC7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9d43bf8-30eb-4688-8eb0-bab0f9fa2661",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vpvqx3SanM5MFMr4Hq4sfZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2029,
      "cache_read_input_tokens": 12881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2029,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 19 · 2026-05-13T11:41:42.954Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DiJPJWjv8AuKAhDU3nZ1DD`</summary>

```json
{
  "url": "https://greenvla.github.io/",
  "prompt": "Extract details about the DataQA pipeline, data quality assurance, demonstration filtering, and any discussion of how quality filtering compares to or improves upon simply scaling data. Also look for the full list of authors and any affiliations mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9d43bf8-30eb-4688-8eb0-bab0f9fa2661",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWLGcW5hwCV58E3CFC7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5091cf82-d40b-4252-89c2-d76cf4db98f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vpvqx3SanM5MFMr4Hq4sfZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2029,
      "cache_read_input_tokens": 12881,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2029
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 12881,
          "cache_creation_input_tokens": 2029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2029,
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

_source line 20 · 2026-05-13T11:41:47.938Z_

<details><summary>↩ Tool result · `toolu_01DiJPJWjv8AuKAhDU3nZ1DD`</summary>

```text
# Green-VLA: DataQA Pipeline and Author Details

## DataQA Pipeline

The DataQA pipeline represents a key component of Green-VLA's data quality assurance approach. According to the documentation, it functions as an "Auto-filters 3,000+ hours using jitter, sharpness, diversity, and state variance metrics + optical-flow alignment."

The pipeline employs multiple filtering mechanisms:
- **Jitter detection** to identify unstable video frames
- **Sharpness analysis** to ensure visual clarity
- **Diversity metrics** to maintain varied training examples
- **State variance filtering** for meaningful state transitions
- **Optical-flow alignment** for temporal synchronization across demonstrations

This multi-metric filtering approach is positioned as enabling "stable multi-embodiment training with improved data efficiency," suggesting the authors view quality filtering as complementary to—rather than a substitute for—simply accumulating more data.

## Authors and Affiliations

The paper lists 35 authors from:
- **Sber Robotics Center** (primary affiliation)
- **Manipulation Team**

The work is dated February 2026 and published to arXiv as paper 2602.00919.

A complete author list appears in the BibTeX citation provided on the webpage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5091cf82-d40b-4252-89c2-d76cf4db98f7",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ab68eb3795eb14002",
  "type": "user",
  "uuid": "89f9bc74-4fe2-46af-bcb3-53878c50e16c",
  "sourceToolAssistantUUID": "5091cf82-d40b-4252-89c2-d76cf4db98f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T11:42:14.137Z_

I now have all the details needed. Here is the full report.

---

## Green-VLA Paper Report

**Full Title:** Green-VLA: Staged Vision-Language-Action Model for Generalist Robots

**Authors:** 28+ authors from **Sber Robotics Center**, including I. Apanasevich, M. Artemyev, R. Babakyan, P. Fedotova, D. Grankin, E. Kupryashin, A. Misailidi, D. Nerus, A. Nutalapati, G. Sidorov, I. Efremov, M. Gerasyov, D. Pikurov, Y. Senchenko, S. Davidenko, D. Kulikov, M. Sultankin, K. Askarbek, O. Shamanin, D. Statovoy, E. Zalyaev, I. Zorin, A. Letkin, E. Rusakov, A. Silchenko, V. Vorobyov, S. Sobolnikov, A. Postnikov, and others.

**Venue / Date:** arXiv preprint (cs.RO), arXiv ID **2602.00919**. Submitted January 31, 2026 (v1), revised March 7, 2026 (v2). No conference venue listed; it is a preprint.

---

### What Green-VLA Does (Overall)

Green-VLA is a ~4B-parameter staged VLA framework for generalist robots, with a five-stage curriculum: (L0) foundational VLM pretraining, (L1) multimodal grounding, (R0) multi-embodiment pretraining, (R1) embodiment-specific adaptation, and (R2) reinforcement-learning policy alignment. It targets the "Green" humanoid robot (32 DoF upper body) but generalizes across humanoids, mobile manipulators, and fixed-base arms via a unified, embodiment-aware action interface.

---

### The DataQA Pipeline -- Heuristic Metrics for Demonstration Filtering

DataQA is Green-VLA's automated data quality assurance pipeline that filters 3,000+ hours of raw demonstrations before training. It uses the following heuristic metrics:

1. **Basic sanity checks:** Removes episodes with missing cameras/frames, episodes that are too short or suspiciously long, and episodes lacking sufficient motion activity.

2. **Tremble Score (Jitter Detection):** Identifies erratic, jerky motions using the formula `S_tremble = |s_dot_smooth - s_dot| / (|s_dot_smooth| + |s_dot|)`, where `s_dot` is the velocity trajectory and `s_dot_smooth` is its Gaussian-smoothed version. High tremble scores indicate poor-quality teleoperator demonstrations.

3. **Sharpness (S_sharp):** Assesses image quality using Laplacian standard deviation scores computed on 4x4 pixel blocks, with max-pooling across 16x16 regions. The median regional sharpness score represents overall episode visual quality -- filtering out blurry or degraded visual data.

4. **Visual Diversity (D_vis):** Measures temporal variance of spatially-averaged DINOv3 feature representations: `D_vis = E_d[std_t(E_s[f_{t,s,d}])]`. This ensures episodes contain meaningful visual variation rather than static or repetitive scenes.

5. **State-Space Diversity (D_state):** Computed as `D_state = sqrt(tr(Cov(s)))` -- the square root of the trace of the robot state covariance matrix. Filters out episodes where the robot barely moves or repeats the same state.

6. **Optical-flow-based Temporal Alignment:** Resamples actions using monotonic cubic splines to normalize effective motion per step, aligning motion statistics across heterogeneous datasets collected at different speeds and frame rates.

7. **Trajectory Smoothing:** Applies smoothing to reduce high-frequency noise in action trajectories post-filtering.

---

### Relevance to Principled Demonstration Curation

Green-VLA's DataQA pipeline is highly relevant to principled demo curation for several reasons:

- **Quality over quantity thesis:** The paper's central argument is that a staged training pipeline emphasizing quality alignment, unified action spaces, and RL refinement outperforms raw data scaling. The broader 2026 consensus they cite is that a well-curated 500-demo fine-tune of a 7B VLA can outperform a poorly curated fine-tune of a 70B model.

- **Multi-metric, automated filtering:** Rather than relying on a single quality score or manual inspection, DataQA combines perceptual metrics (sharpness, visual diversity via DINOv3), kinematic metrics (jitter/tremble, state-space diversity), and temporal normalization (optical-flow alignment). This provides a principled, reproducible, multi-dimensional quality assessment.

- **Addresses real-world data messiness:** The pipeline explicitly handles problems endemic to large-scale teleoperation data collection -- jerky operators, camera failures, uninformative episodes, and speed mismatches across different data sources and embodiments.

- **Enables multi-embodiment training:** By normalizing and filtering across heterogeneous data sources, DataQA makes it feasible to train a single policy on demonstrations from very different robots without low-quality data from one source degrading performance on others.

- **Limitation -- heuristics, not learned:** The metrics are hand-designed heuristics rather than learned quality predictors. This is transparent and interpretable but may miss subtler quality dimensions (e.g., task relevance, strategy optimality). A more principled approach might learn quality scores end-to-end or use outcome-based filtering (success/failure labels).

---

Sources:
- [Green-VLA arXiv abstract](https://arxiv.org/abs/2602.00919)
- [Green-VLA full paper (HTML)](https://arxiv.org/html/2602.00919v1)
- [Green-VLA project page](https://greenvla.github.io/)
- [Green-VLA on HuggingFace Papers](https://huggingface.co/papers/2602.00919)
- [Green-VLA GitHub repository](https://github.com/greenvla/GreenVLA)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89f9bc74-4fe2-46af-bcb3-53878c50e16c",
  "isSidechain": true,
  "agentId": "ab68eb3795eb14002",
  "requestId": "req_011CazWLyqy7dGwQPxPyrjRT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51767941-4c20-4277-a29c-02d1a0168ec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Co2C8YeV81wGFby2TTAr6f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 14910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 446,
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
