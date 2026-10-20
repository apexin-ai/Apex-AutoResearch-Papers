# Research conversation: Search the web for "LIBERO-Plus" benchmark and verify: 1. "LIBERO-Plus CVPR 2026" - was it actually accepted at CVPR 202

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af0d1104a32db3e19.jsonl`
- **Structured JSON:** [`8d147b2cefa5405441b3.json`](../../sessions/8d/8d147b2cefa5405441b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-13T19:43:53.524Z_

Search the web for "LIBERO-Plus" benchmark and verify:

1. "LIBERO-Plus CVPR 2026" - was it actually accepted at CVPR 2026?
2. What exactly does LIBERO-Plus test? (perturbation dimensions, number of tasks, etc.)
3. "LIBERO-Plus robustness VLA benchmark"
4. Also search for "LIBERO-PRO" - arXiv 2510.03827 - verify it exists

I need to confirm that LIBERO-Plus is a real benchmark accepted at CVPR 2026 and that it tests what the proposal claims (7 perturbation dimensions, VLAs drop from 95% to below 30%).

Report with specific details and URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af0d1104a32db3e19",
  "type": "user",
  "uuid": "1f11c338-6d49-4a8a-9d50-8096b018588a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T19:43:53.525Z_

```json
{
  "parentUuid": "1f11c338-6d49-4a8a-9d50-8096b018588a",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
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
  "uuid": "fc0d821d-0d76-43fd-8383-3515121b5307",
  "timestamp": "2026-05-13T19:43:53.525Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T19:43:55.963Z_



I'll search for information about LIBERO-Plus and LIBERO-PRO to verify these claims. Let me run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc0d821d-0d76-43fd-8383-3515121b5307",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb197D8LwpUVi4TW6fLcj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45811f8a-e6e2-469a-847c-dd846955b563",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BP19JFMB9MHneeMZG75dZt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 717,
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

_source line 4 · 2026-05-13T19:43:56.436Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PLoDmJ1CpUKsg1icgs8sv7`</summary>

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
  "parentUuid": "45811f8a-e6e2-469a-847c-dd846955b563",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb197D8LwpUVi4TW6fLcj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc8008d8-86dd-40cb-aace-9fd9366ed72b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BP19JFMB9MHneeMZG75dZt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 8223,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 717
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 717,
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

_source line 5 · 2026-05-13T19:43:56.439Z_

<details><summary>↩ Tool result · `toolu_01PLoDmJ1CpUKsg1icgs8sv7`</summary>

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
  "parentUuid": "bc8008d8-86dd-40cb-aace-9fd9366ed72b",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af0d1104a32db3e19",
  "type": "user",
  "uuid": "8b7a3c58-0b83-4fde-b380-bf9a6429b1cc",
  "sourceToolAssistantUUID": "bc8008d8-86dd-40cb-aace-9fd9366ed72b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T19:43:59.535Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b7a3c58-0b83-4fde-b380-bf9a6429b1cc",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb197SJMg4uHgXMCCGDUm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1a975a8-61c2-492d-b238-8557185b2d82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NentDT7wobji3HBV8jEJEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1425,
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

_source line 7 · 2026-05-13T19:44:00.120Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GixcrDp2gJJgwrHZgSyFer`</summary>

```json
{
  "query": "LIBERO-Plus CVPR 2026 benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1a975a8-61c2-492d-b238-8557185b2d82",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb197SJMg4uHgXMCCGDUm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee069a27-c431-4333-8055-1506b644cee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NentDT7wobji3HBV8jEJEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1425,
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

_source line 8 · 2026-05-13T19:44:00.531Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KbEu5XRmQqB9CS8hhY3zMY`</summary>

```json
{
  "query": "LIBERO-Plus robustness VLA benchmark perturbation dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee069a27-c431-4333-8055-1506b644cee6",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb197SJMg4uHgXMCCGDUm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cdef810-d365-4b99-9623-dd6b8e7e61db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NentDT7wobji3HBV8jEJEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1425,
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

_source line 9 · 2026-05-13T19:44:00.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QdNMyiXmMAFAqPSPk6eEdm`</summary>

```json
{
  "query": "LIBERO-PRO arXiv 2510.03827"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cdef810-d365-4b99-9623-dd6b8e7e61db",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb197SJMg4uHgXMCCGDUm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d43b02aa-5b63-44f2-9b51-62ce0f000089",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NentDT7wobji3HBV8jEJEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1425,
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

_source line 10 · 2026-05-13T19:44:01.447Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LwYmenRaKQBYiEqGeWyfix`</summary>

```json
{
  "query": "\"LIBERO-Plus\" benchmark robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d43b02aa-5b63-44f2-9b51-62ce0f000089",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb197SJMg4uHgXMCCGDUm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d46edd1-b65e-4b81-abea-e5054850635e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NentDT7wobji3HBV8jEJEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8940,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1425
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 8940,
          "cache_creation_input_tokens": 1425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1425,
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

_source line 11 · 2026-05-13T19:44:06.142Z_

<details><summary>↩ Tool result · `toolu_01KbEu5XRmQqB9CS8hhY3zMY`</summary>

```text
Web search results for query: "LIBERO-Plus robustness VLA benchmark perturbation dimensions"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"}]

Based on the search results, here's what I found about LIBERO-Plus robustness VLA benchmark and its perturbation dimensions:

## Overview

LIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions for Vision-Language-Action (VLA) models.

## Perturbation Dimensions

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise. Additionally, the evaluation covers seven robustness dimensions and 21 sub-dimensions, ensuring a thorough assessment of model generalization.

## Benchmark Scale

LIBERO-Plus consists of an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, along with a diverse training dataset with over 20,000 successful trajectories collected under systematically varied conditions.

## Key Findings

The benchmark reveals significant robustness issues in current VLA models:

- Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

- Models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

- The benchmark includes difficulty levels (L1–L5), providing detailed insights into when and how VLA models fail.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cdef810-d365-4b99-9623-dd6b8e7e61db",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af0d1104a32db3e19",
  "type": "user",
  "uuid": "1d18a1a0-6519-4013-b48c-0284cb445613",
  "sourceToolAssistantUUID": "4cdef810-d365-4b99-9623-dd6b8e7e61db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T19:44:06.880Z_

<details><summary>↩ Tool result · `toolu_01GixcrDp2gJJgwrHZgSyFer`</summary>

```text
Web search results for query: "LIBERO-Plus CVPR 2026 benchmark"

Links: [{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"[2603.09292] See, Plan, Rewind: Progress-Aware Vision-Language-Action Models for Robust Robotic Manipulation","url":"https://arxiv.org/abs/2603.09292"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"}]

Based on the search results, here's what I found about LIBERO-Plus:

## Overview

LIBERO-Plus is the official implementation and benchmark for the paper "In-depth Robustness Analysis for Vision-Language-Action Models". It is an advanced robustness evaluation tool for Vision-Language-Action (VLA) models that allows researchers to understand how these models perform under various environmental perturbations, shedding light on their vulnerabilities in real-world settings.

## Benchmark Structure

The benchmark comprises 10,030 tasks spanning seven perturbation factors with twenty-one low-level components. LIBERO-Plus offers a robust benchmarking framework with 7 perturbation dimensions and 21 sub-dimensions, providing a fine-grained difficulty scale from L1 to L5.

## Key Findings

The analysis exposes critical weaknesses: models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

## CVPR 2026 Connection

The work was presented at CVPR 2026 as a poster on "LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee069a27-c431-4333-8055-1506b644cee6",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af0d1104a32db3e19",
  "type": "user",
  "uuid": "5e02d04f-9a9d-48d8-9238-5ca8aba7a182",
  "sourceToolAssistantUUID": "ee069a27-c431-4333-8055-1506b644cee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T19:44:08.502Z_

<details><summary>↩ Tool result · `toolu_01LwYmenRaKQBYiEqGeWyfix`</summary>

```text
Web search results for query: ""LIBERO-Plus" benchmark robot manipulation"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO – LIBERO","url":"https://libero-project.github.io/main.html"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning – Sony AI","url":"https://ai.sony/publications/LIBERO-Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learning/"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"}]

Based on the search results, here's information about the LIBERO-Plus benchmark for robot manipulation:

## Overview

LIBERO-Plus analyzes visual-language-action (VLA) models that report impressive success rates on robotic manipulation benchmarks, yet may mask fundamental weaknesses in robustness.

## Key Features

LIBERO-Plus performs systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise. 

The benchmark offers three key advancements: (1) Comprehensive evaluation across seven robustness dimensions and 21 sub-dimensions, ensuring thorough assessment of model generalization; (2) Automated task generation, enabling creation of diverse training and test samples; and (3) Fine-grained incorporation of difficulty levels (L1–L5), providing detailed insights into when and how VLA models fail.

## Key Findings

The analysis exposes critical weaknesses: models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. 

Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

## Relationship to LIBERO

Early versions of LIBERO do not contain perturbations in viewpoint, lighting, or distractors, requiring LIBERO-PRO and LIBERO-Plus to fill this gap.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d46edd1-b65e-4b81-abea-e5054850635e",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af0d1104a32db3e19",
  "type": "user",
  "uuid": "aec40c3c-26b2-4f5f-9e51-7c8e733c9f9d",
  "sourceToolAssistantUUID": "2d46edd1-b65e-4b81-abea-e5054850635e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T19:44:08.669Z_

<details><summary>↩ Tool result · `toolu_01QdNMyiXmMAFAqPSPk6eEdm`</summary>

```text
Web search results for query: "LIBERO-PRO arXiv 2510.03827"

Links: [{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"Paper page - LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://huggingface.co/papers/2510.03827"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"[2510.03827v1] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251003827Z/abstract"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization | alphaXiv","url":"https://www.alphaxiv.org/abs/2510.03827v1"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"}]

Based on the search results, here's information about LIBERO-PRO (arXiv 2510.03827):

## Overview

LIBERO-PRO is an extended LIBERO benchmark that systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments.

## Problem Statement

LIBERO has emerged as a widely adopted benchmark for evaluating Vision-Language-Action (VLA) models; however, its current training and evaluation settings are problematic, often leading to inflated performance estimates and preventing fair model comparison.

## Key Findings

The paper reveals a dramatic gap in model performance:

Although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under the generalized setting. This discrepancy exposes the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception.

Specifically, models persist in executing grasping actions when the target object is replaced with irrelevant items, and their outputs remain unchanged even when given corrupted instructions or even messy tokens.

## Authors and Availability

The paper was submitted on October 4, 2025, by authors including Xueyang Zhou, Yangming Xu, Guiyao Tie, Yongchao Chen, and others. The code is available at: https://github.com/Zxy-MLlab/LIBERO-PRO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d43b02aa-5b63-44f2-9b51-62ce0f000089",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af0d1104a32db3e19",
  "type": "user",
  "uuid": "e5e23312-7cd9-4ef1-aa00-c0935015782e",
  "sourceToolAssistantUUID": "d43b02aa-5b63-44f2-9b51-62ce0f000089",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-13T19:44:11.840Z_

Let me get a few more details to confirm the CVPR 2026 acceptance and the arXiv paper specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5e23312-7cd9-4ef1-aa00-c0935015782e",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb198KtB1JQhDxsZco5LV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e9b9f07-e65c-41a0-b049-0ce1b36f1d30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVPhfM8crkq3ry4osT2DMm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 905,
      "cache_creation_input_tokens": 2973,
      "cache_read_input_tokens": 10365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2973,
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

_source line 16 · 2026-05-13T19:44:12.375Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HVq7TjfobwjzoTKg8xTx8o`</summary>

```json
{
  "query": "arxiv 2510.13626 LIBERO-Plus authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e9b9f07-e65c-41a0-b049-0ce1b36f1d30",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb198KtB1JQhDxsZco5LV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbf746f3-00c9-4382-9e20-59a5fbebcd70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVPhfM8crkq3ry4osT2DMm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 905,
      "cache_creation_input_tokens": 2973,
      "cache_read_input_tokens": 10365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2973,
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

_source line 17 · 2026-05-13T19:44:12.527Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AkrdFSj8w7H6TEtPoxrEae`</summary>

```json
{
  "query": "CVPR 2026 accepted papers LIBERO-Plus poster"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbf746f3-00c9-4382-9e20-59a5fbebcd70",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb198KtB1JQhDxsZco5LV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1325641e-a95b-4ea2-9013-209e42974974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVPhfM8crkq3ry4osT2DMm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 905,
      "cache_creation_input_tokens": 2973,
      "cache_read_input_tokens": 10365,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2973
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 905,
          "output_tokens": 143,
          "cache_read_input_tokens": 10365,
          "cache_creation_input_tokens": 2973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2973,
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

_source line 18 · 2026-05-13T19:44:15.776Z_

<details><summary>↩ Tool result · `toolu_01HVq7TjfobwjzoTKg8xTx8o`</summary>

```text
Web search results for query: "arxiv 2510.13626 LIBERO-Plus authors"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"}]

The authors of arxiv paper 2510.13626 (LIBERO-Plus) are: Senyu Fei, Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li Ji, Xinzhe He, Shiduo Zhang, Zhaoye Fei, Jinlan Fu, Jingjing Gong, and Xipeng Qiu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbf746f3-00c9-4382-9e20-59a5fbebcd70",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af0d1104a32db3e19",
  "type": "user",
  "uuid": "d59de9e8-1aad-48d8-aebf-0c8240412b91",
  "sourceToolAssistantUUID": "bbf746f3-00c9-4382-9e20-59a5fbebcd70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T19:44:17.205Z_

<details><summary>↩ Tool result · `toolu_01AkrdFSj8w7H6TEtPoxrEae`</summary>

```text
Web search results for query: "CVPR 2026 accepted papers LIBERO-Plus poster"

Links: [{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"CVPR 2026 Accepted Papers: Trends, Big Tech Bets & Top Highlights","url":"https://www.bohrium.com/en/blog/research-notes/cvpr-2026-accepted-papers-highlights/"},{"title":"Paper Digest: CVPR 2026 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2026/04/cvpr-2026-papers-highlights/"},{"title":"GitHub - SkalskiP/top-cvpr-2026-papers: About This repository is a curated collection of the most exciting and influential CVPR 2026 papers. 🔥 [Paper + Code + Demo]","url":"https://github.com/SkalskiP/top-cvpr-2026-papers"},{"title":"CVPR 2026 Papers","url":"https://cvpr.thecvf.com/virtual/2026/papers.html"},{"title":"Paper Digest: CVPR 2026 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2026/04/cvpr-2026-papers-highlights/"},{"title":"Eleven papers accepted by CVPR 2026 - CCVL @ JHU","url":"https://ccvl.jhu.edu/news/2026/cvpr2026/"},{"title":"6 Papers Accepted at CVPR 2026","url":"https://www.a-star.edu.sg/cfar/news/news/features/6-papers-accepted-at-cvpr-2026"},{"title":"CVPR 2026 NAVER LABS Europe papers and presentations","url":"https://europe.naverlabs.com/updates/cvpr/"},{"title":"CVPR 2026 Call for Papers - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/Conferences/2026/CallForPapers"}]

Based on the search results, I found information about the LIBERO-Plus paper at CVPR 2026:

LIBERO-Plus is a comprehensive, automatic, and fine-grained evaluation framework for Visual-Language-Action (VLA) models with controlled perturbations across seven dimensions: object layouts, camera viewpoints, robot initial states, language instructions, lighting conditions, background textures, and sensor noise. 

The systematic analysis of ten state-of-the-art models reveals consistent brittleness beneath apparent competence, with performance dropping from 95% to below 30% under modest perturbations.

The paper is featured as a poster presentation at CVPR 2026, and you can access it directly at the official CVPR virtual conference portal (cvpr.thecvf.com/virtual/2026/poster/38735).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1325641e-a95b-4ea2-9013-209e42974974",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af0d1104a32db3e19",
  "type": "user",
  "uuid": "25461184-4844-4449-ace8-3cfd547cc62c",
  "sourceToolAssistantUUID": "1325641e-a95b-4ea2-9013-209e42974974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-13T19:44:42.504Z_

Here is a detailed verification report on both LIBERO-Plus and LIBERO-PRO:

---

## 1. LIBERO-Plus -- CVPR 2026 Acceptance: CONFIRMED

LIBERO-Plus was indeed accepted at CVPR 2026 as a **poster presentation**. The official CVPR virtual conference page lists it with the title **"LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models"** at `cvpr.thecvf.com/virtual/2026/poster/38735`.

- **arXiv ID:** 2510.13626
- **Full title:** "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
- **Authors:** Senyu Fei, Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li Ji, Xinzhe He, Shiduo Zhang, Zhaoye Fei, Jinlan Fu, Jingjing Gong, and Xipeng Qiu
- **GitHub:** `github.com/sylvestf/LIBERO-plus`
- **Project page:** `sylvestf.github.io/LIBERO-plus/`

---

## 2. What LIBERO-Plus Tests: VERIFIED

The benchmark introduces controlled perturbations across **7 dimensions** with **21 sub-dimensions**:

1. **Object layouts**
2. **Camera viewpoints**
3. **Robot initial states**
4. **Language instructions**
5. **Lighting conditions**
6. **Background textures**
7. **Sensor noise**

Additional details:
- **10,030 tasks** spanning those 7 perturbation dimensions
- **Fine-grained difficulty scale** from L1 to L5
- **20,000+ successful training trajectories** collected under systematically varied conditions
- **10 state-of-the-art VLA models** evaluated

---

## 3. Performance Drop Claim: VERIFIED

The claim that "VLAs drop from 95% to below 30%" is accurate. The paper states:

> "Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from **95% to below 30%** under modest perturbations."

An additional surprising finding: models are largely **insensitive to language variations**, with experiments revealing that models tend to **ignore language instructions completely**.

---

## 4. LIBERO-PRO (arXiv 2510.03827): CONFIRMED TO EXIST

LIBERO-PRO is a **separate, distinct benchmark** from LIBERO-Plus.

- **arXiv ID:** 2510.03827 (confirmed)
- **Full title:** "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization"
- **Authors:** Xueyang Zhou, Yangming Xu, Guiyao Tie, Yongchao Chen, and others
- **GitHub:** `github.com/Zxy-MLlab/LIBERO-PRO`
- **Submitted:** October 4, 2025
- **Focus:** Evaluates model performance under perturbations across **4 dimensions** (manipulated objects, initial states, task instructions, environments)
- **Key finding:** Models achieve over 90% accuracy under standard LIBERO evaluation but collapse to **0.0%** under generalized settings, exposing reliance on rote memorization

**Important distinction:** LIBERO-PRO and LIBERO-Plus are different papers by different author groups, tackling related but distinct aspects of VLA robustness evaluation. LIBERO-Plus has 7 perturbation dimensions; LIBERO-PRO has 4.

---

## Summary

All claims check out:
- LIBERO-Plus is real and accepted at CVPR 2026 (poster).
- It tests 7 perturbation dimensions across 10,030 tasks with difficulty levels L1-L5.
- The 95%-to-below-30% performance drop is an accurately quoted finding from the paper.
- LIBERO-PRO (arXiv 2510.03827) is a separate, confirmed paper with its own benchmark.

Sources:
- [CVPR 2026 Poster - LIBERO-Plus](https://cvpr.thecvf.com/virtual/2026/poster/38735)
- [arXiv 2510.13626 - LIBERO-Plus](https://arxiv.org/abs/2510.13626)
- [LIBERO-Plus Project Page](https://sylvestf.github.io/LIBERO-plus/)
- [LIBERO-Plus GitHub](https://github.com/sylvestf/LIBERO-plus)
- [LIBERO-Plus on Hugging Face](https://huggingface.co/papers/2510.13626)
- [arXiv 2510.03827 - LIBERO-PRO](https://arxiv.org/abs/2510.03827)
- [LIBERO-PRO GitHub](https://github.com/Zxy-MLlab/LIBERO-PRO)
- [LIBERO-PRO on Hugging Face](https://huggingface.co/papers/2510.03827)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25461184-4844-4449-ace8-3cfd547cc62c",
  "isSidechain": true,
  "agentId": "af0d1104a32db3e19",
  "requestId": "req_011Cb198xPt3kYtWettkDcjt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "307ea22d-b804-4eb4-82e0-27bc340b1e05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Po5tmEoqYyf9pU34Jh6uUo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2516,
      "cache_read_input_tokens": 13338,
      "output_tokens": 1273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2516
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1273,
          "cache_read_input_tokens": 13338,
          "cache_creation_input_tokens": 2516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2516,
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
