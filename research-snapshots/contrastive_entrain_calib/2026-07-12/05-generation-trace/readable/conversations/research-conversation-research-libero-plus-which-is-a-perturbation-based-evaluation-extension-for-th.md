# Research conversation: Research LIBERO-Plus, which is a perturbation-based evaluation extension for the LIBERO benchmark in robot manipulation.

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aada8a30ff0506204.jsonl`
- **Structured JSON:** [`661b2db3aa59c24d2043.json`](../../sessions/66/661b2db3aa59c24d2043.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-15T11:11:54.413Z_

Research LIBERO-Plus, which is a perturbation-based evaluation extension for the LIBERO benchmark in robot manipulation.

I need to find:
1. What LIBERO-Plus is — what it adds on top of LIBERO
2. GitHub repo or paper source
3. The 4 perturbation dimensions: camera perturbation, lighting change, texture swap, sensor noise — exact definitions
4. Installation and running instructions
5. How it integrates with standard LIBERO evaluation

Also research whether LIBERO's simulation environment has built-in randomization options (camera jitter, color/lighting changes, background texture randomization). If it does, how to configure them. If not, whether LIBERO-Plus perturbation implementations can be reused as training-time data augmentation.

Use WebSearch to find papers and repos related to "LIBERO-Plus" or "LIBERO perturbation evaluation" or "LIBERO robustness". Then use WebFetch to read relevant GitHub repos and paper details.

Report everything in structured format with exact commands and code paths where possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "4d5e06ef-c0fc-451a-a8a4-1ce7bda6a3f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T11:11:54.414Z_

```json
{
  "parentUuid": "4d5e06ef-c0fc-451a-a8a4-1ce7bda6a3f9",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "a175e9f7-21a6-47fe-9b9a-03e2ad593b95",
  "timestamp": "2026-05-15T11:11:54.414Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T11:11:57.183Z_



I'll research LIBERO-Plus and LIBERO's built-in randomization capabilities. Let me start by loading the web search and fetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a175e9f7-21a6-47fe-9b9a-03e2ad593b95",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FgbwfmzeGqWuQgL6GZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b10e8a52-afcc-4c7f-a07a-dba0903ac011",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HscfT99oUBNzjyHLLPNHFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6065,
      "cache_read_input_tokens": 8256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6065,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 4 · 2026-05-15T11:11:57.606Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XRqEnpJu6K7JtZjw3ZpdFZ`</summary>

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
  "parentUuid": "b10e8a52-afcc-4c7f-a07a-dba0903ac011",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FgbwfmzeGqWuQgL6GZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1493836-ecb4-4065-b6ea-583c92a55e87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HscfT99oUBNzjyHLLPNHFk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6065,
      "cache_read_input_tokens": 8256,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6065
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 8256,
          "cache_creation_input_tokens": 6065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6065,
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

_source line 5 · 2026-05-15T11:11:57.610Z_

<details><summary>↩ Tool result · `toolu_01XRqEnpJu6K7JtZjw3ZpdFZ`</summary>

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
  "parentUuid": "f1493836-ecb4-4065-b6ea-583c92a55e87",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "6f7afe10-0410-4333-8d30-7543a987318a",
  "sourceToolAssistantUUID": "f1493836-ecb4-4065-b6ea-583c92a55e87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T11:12:00.620Z_



Let me search for LIBERO-Plus across multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f7afe10-0410-4333-8d30-7543a987318a",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FgqtKNxFwHfxBqdd5Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1725956-be83-4b07-a0d7-c5d6a785acf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EUZP4boqB9ozLNdCRA5c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1969,
      "cache_read_input_tokens": 14321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1969,
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

_source line 7 · 2026-05-15T11:12:00.785Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A6mhyUFE9P8zgUTypbGNfp`</summary>

```json
{
  "query": "LIBERO-Plus perturbation evaluation robot manipulation benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1725956-be83-4b07-a0d7-c5d6a785acf0",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FgqtKNxFwHfxBqdd5Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d73fed2d-d301-4c16-82c3-acdc8b781030",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EUZP4boqB9ozLNdCRA5c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1969,
      "cache_read_input_tokens": 14321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1969,
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

_source line 8 · 2026-05-15T11:12:01.561Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013NKXDr4xSgfHfazRsFCode`</summary>

```json
{
  "query": "LIBERO-Plus GitHub repo robustness perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d73fed2d-d301-4c16-82c3-acdc8b781030",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FgqtKNxFwHfxBqdd5Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74154388-ae5d-43de-bd12-71c6cf7b70d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EUZP4boqB9ozLNdCRA5c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1969,
      "cache_read_input_tokens": 14321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1969,
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

_source line 9 · 2026-05-15T11:12:02.057Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017vWJBqAopQtDFKLeX5WN1b`</summary>

```json
{
  "query": "LIBERO benchmark robustness evaluation camera lighting texture noise perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74154388-ae5d-43de-bd12-71c6cf7b70d0",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FgqtKNxFwHfxBqdd5Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9902aecd-014b-4bf2-a1ed-9155db9ffe18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EUZP4boqB9ozLNdCRA5c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1969,
      "cache_read_input_tokens": 14321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1969,
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

_source line 10 · 2026-05-15T11:12:02.140Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UBf9UkKwZgRTuZfMUn2iFz`</summary>

```json
{
  "query": "LIBERO simulation environment randomization domain randomization options"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9902aecd-014b-4bf2-a1ed-9155db9ffe18",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FgqtKNxFwHfxBqdd5Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e28fea5-669f-4be0-8000-c3ed1c7b9fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EUZP4boqB9ozLNdCRA5c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1969,
      "cache_read_input_tokens": 14321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1969,
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

### Tool result

_source line 11 · 2026-05-15T11:12:07.845Z_

<details><summary>↩ Tool result · `toolu_01A6mhyUFE9P8zgUTypbGNfp`</summary>

```text
Web search results for query: "LIBERO-Plus perturbation evaluation robot manipulation benchmark"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"}]

Based on the search results, here's comprehensive information about LIBERO-Plus:

## Overview

LIBERO-plus is a generalized benchmark for in-depth robustness analysis of vision-language-action models. LIBERO-Plus is an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, and includes a diverse training dataset with over 20,000 successful trajectories collected under systematically varied conditions.

## Key Perturbation Dimensions

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Main Findings

The research exposes significant vulnerabilities in Vision-Language-Action models:

- **Extreme Sensitivity**: Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

- **Language Ignorance**: Models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

- **Compositional Failures**: Their learned representations are entangled and cannot handle the complex, multi-dimensional perturbations that characterize real-world environments.

## Benchmark Features

LIBERO-plus offers three key advancements: (1) Comprehensive evaluation across seven robustness dimensions and 21 sub-dimensions, ensuring a thorough assessment of model generalization, (2) Automated task generation, enabling the creation of a large number of diverse training and test samples, (3) Fine-grained incorporation of difficulty levels (L1–L5), providing detailed insights into when and how VLA models fail.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d73fed2d-d301-4c16-82c3-acdc8b781030",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "a6666c3d-3b6d-4c94-9e79-1dda43d8ed51",
  "sourceToolAssistantUUID": "d73fed2d-d301-4c16-82c3-acdc8b781030",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T11:12:07.877Z_

<details><summary>↩ Tool result · `toolu_013NKXDr4xSgfHfazRsFCode`</summary>

```text
Web search results for query: "LIBERO-Plus GitHub repo robustness perturbation"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"LIBERO-plus/index.html at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/index.html"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"}]

Based on the search results, here's information about the LIBERO-Plus GitHub repository and its robustness perturbation approach:

## Overview

LIBERO-Plus contains the official implementation and benchmark for a paper on "In-depth Robustness Analysis for Vision-Language-Action Models". LIBERO-Plus is a robustness benchmark for Vision-Language-Action (VLA) models built on top of LIBERO that systematically stress-tests policies by applying seven independent perturbation dimensions to the original LIBERO task set, exposing failure modes that standard benchmarks miss.

## Perturbation Dimensions

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Key Findings

VLA models exhibit extreme sensitivity to camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations, models largely ignore language instructions, and combined perturbations reveal complex interaction effects beyond independent factors.

## Benchmark Scale

The benchmark construction follows a systematic two-stage process of expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing, and evaluating the resulting tasks using four representative models and stratifying them into five difficulty levels.

The GitHub repository is located at: **https://github.com/sylvestf/LIBERO-plus**


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74154388-ae5d-43de-bd12-71c6cf7b70d0",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "84a4a192-264d-4b8a-92a4-3f2d373d248e",
  "sourceToolAssistantUUID": "74154388-ae5d-43de-bd12-71c6cf7b70d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T11:12:08.735Z_

<details><summary>↩ Tool result · `toolu_017vWJBqAopQtDFKLeX5WN1b`</summary>

```text
Web search results for query: "LIBERO benchmark robustness evaluation camera lighting texture noise perturbation"

Links: [{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Efficient Spatial Adaptation in VLA Models","url":"https://www.emergentmind.com/papers/2512.02902"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"}]

I found comprehensive information about the LIBERO benchmark and its robustness evaluation capabilities. Here's what the search revealed:

## LIBERO-Plus: Robustness Evaluation Framework

LIBERO-Plus is an in-depth robustness analysis framework for Visual-Language-Action (VLA) models that performs systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

### Key Findings

Analysis of VLA models reveals critical weaknesses, with models exhibiting extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

LIBERO-Plus offers a robust benchmarking framework with 7 perturbation dimensions and 21 sub-dimensions, providing a fine-grained difficulty scale from L1 to L5 for systematically assessing model performance across various challenges.

### Benchmark Composition

LIBERO-Plus was constructed as an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, created with a diverse training dataset with over 20,000 successful trajectories collected under systematically varied conditions.

### Specific Perturbation Types

The benchmark evaluates models across:
- Camera Viewpoints: changes to the viewpoint/pose and field-of-view of the third-person camera
- Light Conditions: variations in illumination intensity, direction, color, and shadow patterns
- Background Textures: scene and surface appearance changes, and Sensor Noise: photometric distortions and image degradation


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9902aecd-014b-4bf2-a1ed-9155db9ffe18",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "897e6a87-eea7-4ae6-8ee8-2365afde5624",
  "sourceToolAssistantUUID": "9902aecd-014b-4bf2-a1ed-9155db9ffe18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T11:12:09.238Z_

<details><summary>↩ Tool result · `toolu_01UBf9UkKwZgRTuZfMUn2iFz`</summary>

```text
Web search results for query: "LIBERO simulation environment randomization domain randomization options"

Links: [{"title":"Domain Randomization for Sim2Real Transfer | Lil'Log","url":"https://lilianweng.github.io/posts/2019-05-05-domain-randomization/"},{"title":"Continual Domain Randomization","url":"https://arxiv.org/pdf/2403.12193"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"Flow-based Domain Randomization for Learning and Sequencing Robotic Skills","url":"https://arxiv.org/html/2502.01800v1"},{"title":"9.4. Domain Randomization for RL — Omniverse IsaacSim latest documentation","url":"https://docs.isaacsim.omniverse.nvidia.com/2023.1.1/isaac_gym_tutorials/tutorial_gym_domain_randomization.html"},{"title":"A Domain Data Pattern Randomization based Deep Reinforcement Learning method for Sim-to-Real transfer","url":"https://dl.acm.org/doi/fullHtml/10.1145/3461353.3461373"},{"title":"Cyclic policy distillation: Sample-efficient sim-to-real reinforcement learning with domain randomization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0921889023000647"},{"title":"Flow-based Domain Randomization for Learning and Sequencing Robotic Skills | OpenReview","url":"https://openreview.net/forum?id=9JQXuyzdGL"},{"title":"2. Domain Randomization for RL — Omniverse IsaacSim latest documentation","url":"https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/tutorial_gym_domain_randomization.html"},{"title":"Domain Randomization","url":"https://stevengong.co/notes/Domain-Randomization"}]

Based on the search results, I found relevant information about LIBERO and domain randomization options. Here's what I discovered:

## LIBERO and Domain Randomization

LIBERO-PRO is a plug-and-play benchmark that incorporates carefully designed perturbations across four dimensions—manipulated objects, initial states, task instructions, and environments—and supports randomized combinations of these dimensions for more faithful evaluation.

### Specific Domain Randomization Dimensions in LIBERO:

The benchmark supports randomization across these key areas:

1. **Object Variation**: For object variation, new assets are created by modifying the appearance, size, and color of the original objects.

2. **Position Variation**: For position variation, alternative spatial regions are defined for all manipulable objects while strictly adhering to physical constraints and task definitions.

3. **Instruction Variation**: For instruction variation, three distinct paraphrased versions of each task description are provided.

4. **Task Variation**: For task variation, tasks are redesigned in a principled manner to ensure feasibility, and new sets of relevant objects and target states for each modified task are supplied.

5. **Environment Variation**: For environment variation, the five environment categories built into the LIBERO benchmark are leveraged and randomly substituted across tasks.

To avoid meaningless combinations, task variation is restricted from being combined with other types, while allowing all other dimensions of variation to be freely and randomly combined for more comprehensive evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e28fea5-669f-4be0-8000-c3ed1c7b9fd8",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "00f56bd1-d059-48e5-9c61-2db5045f3c07",
  "sourceToolAssistantUUID": "1e28fea5-669f-4be0-8000-c3ed1c7b9fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T11:12:12.331Z_

Good, I have the key sources. Now let me fetch the detailed content from the GitHub repo, the paper, and the project page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00f56bd1-d059-48e5-9c61-2db5045f3c07",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4Fhi6HLPCWDZoc1VczM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a3dd4b5-3c78-4ca1-bd46-f9ec2601ed2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hgbj1ouCgXrztWAeWRCTda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 16 · 2026-05-15T11:12:13.781Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L5mbVAKU4poVAfpeGpdbhC`</summary>

```json
{
  "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md",
  "prompt": "Extract the full README content including: installation instructions, perturbation dimensions with exact definitions, how to run evaluation, project structure, configuration options, and any code examples. Include all technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a3dd4b5-3c78-4ca1-bd46-f9ec2601ed2f",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4Fhi6HLPCWDZoc1VczM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9bcfb13-814e-49bd-92bb-ad42849f472b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hgbj1ouCgXrztWAeWRCTda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 17 · 2026-05-15T11:12:16.605Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ULA9B8PqczvmkX3LtiFQVR`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "Extract detailed information about: 1) All 7 perturbation dimensions and their exact definitions/sub-dimensions, 2) How perturbations are implemented in the simulation (MuJoCo/robosuite), 3) Difficulty levels L1-L5, 4) Training data augmentation details, 5) Integration with LIBERO's simulation environment, 6) Any details about camera, lighting, texture, sensor noise implementations specifically. Include technical specifics like parameter ranges."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9bcfb13-814e-49bd-92bb-ad42849f472b",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4Fhi6HLPCWDZoc1VczM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b42c9831-be67-4fb5-9f04-0d9a6cda15a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hgbj1ouCgXrztWAeWRCTda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 18 · 2026-05-15T11:12:17.536Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U23B7oC9XDUA1Q53BwWsAc`</summary>

```json
{
  "url": "https://sylvestf.github.io/LIBERO-plus/",
  "prompt": "Extract all technical details about LIBERO-Plus: perturbation dimensions, implementation details, benchmark construction, evaluation protocol, and any information about how perturbations are applied in the simulation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b42c9831-be67-4fb5-9f04-0d9a6cda15a0",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4Fhi6HLPCWDZoc1VczM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e39f9f1-ca24-4d39-9ac7-6d90b6cf049f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hgbj1ouCgXrztWAeWRCTda",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16290,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3840
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 435,
          "cache_read_input_tokens": 16290,
          "cache_creation_input_tokens": 3840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3840,
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

_source line 19 · 2026-05-15T11:12:22.453Z_

<details><summary>↩ Tool result · `toolu_01L5mbVAKU4poVAfpeGpdbhC`</summary>

```text
# LIBERO-Plus: Robustness Analysis Framework

## Overview

LIBERO-Plus is a comprehensive benchmark evaluating vision-language-action (VLA) models across multiple perturbation dimensions. The project functions as a drop-in replacement for the original LIBERO package, maintaining backward compatibility while adding extensive robustness testing capabilities.

## Installation

The setup process mirrors the original LIBERO system. Users should:

1. Clone the repository and navigate to the directory
2. Uninstall any existing LIBERO installation
3. Verify configuration paths at `/root/.libero/config.yaml`
4. Install via `pip install -e .`
5. Add system dependencies (libexpat1, libfontconfig1-dev, libmagickwand-dev)
6. Install additional Python packages from extra_requirements.txt

Assets must be downloaded from Hugging Face and extracted to `LIBERO-plus/libero/libero/assets/`, creating subdirectories for articulated objects, new objects, scenes, textures, and supporting files.

## Seven Perturbation Dimensions

The benchmark evaluates resilience across:

1. **Objects Layout** – "Confounding objects and target object displacement"
2. **Camera Viewpoints** – Position, orientation, and field-of-view modifications
3. **Robot Initial States** – Manipulator pose variations
4. **Language Instructions** – LLM-based instruction rewrites
5. **Light Conditions** – Intensity, direction, color, and shadow changes
6. **Background Textures** – Scene and surface appearance modifications
7. **Sensor Noise** – "Photometric distortions and image degradation"

## Evaluation Protocol

The evaluation methodology closely follows original LIBERO standards with one critical adjustment: modify `num_trials_per_task` from 50 to 1 in configuration files. Task classification mappings between IDs, perturbation categories, and difficulty levels are located in `.libero/libero/benchmark/task_classification.json`.

## Project Structure

The extracted asset directory should contain:
- articulated_objects/
- new_objects/
- scenes/
- stable_hope_objects/
- stable_scanned_objects/
- textures/
- turbosquid_objects/
- Supporting XML files (serving_region.xml, wall.xml, wall.stl)

## Key Findings

Research reveals that current VLA models demonstrate "extreme sensitivity to camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations." Additionally, models exhibit substantial language instruction ignorance and negative compositional generalization when multiple perturbations combine.

## Citation

For research using this benchmark, cite: Fei et al., "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models," arXiv:2510.13626 (2025).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9bcfb13-814e-49bd-92bb-ad42849f472b",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "085d2d76-0f6a-4b23-b237-c1f026d0ebfb",
  "sourceToolAssistantUUID": "b9bcfb13-814e-49bd-92bb-ad42849f472b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T11:12:24.619Z_

<details><summary>↩ Tool result · `toolu_01U23B7oC9XDUA1Q53BwWsAc`</summary>

```text
# LIBERO-Plus Technical Details

## Seven Perturbation Dimensions

The study introduces controlled perturbations across: "(i) objects layout, (ii) camera viewpoints, (iii) robot initial states, (iv) language instructions, (v) light conditions, (vi) background textures and (vii) sensor noise."

## Benchmark Construction

The researchers employed a "systematic two-stage process": first, they expanded the original LIBERO benchmark through seven distinct perturbation factors, then filtered tasks and balanced categories based on empirical findings. Subsequently, they evaluated results using four representative models and stratified tasks into five difficulty levels (Level-1 to Level-5) according to accuracy distributions.

## Key Implementation Findings

**Language Perturbations:**
- Blank instruction tests removed valid language input entirely
- Goal replacement tests substituted target objects with alternatives
- Results showed models degrade into vision-action patterns, largely disregarding language signals

**Visual Perturbations:**
- Camera changes (position, orientation, field-of-view) caused dramatic performance drops
- Robot initial pose variations significantly impacted success rates
- Background and lighting changes showed surprising resilience, attributed to wrist camera stability

**Compositional Testing:**
The study measured interaction effects using: "Δij = P(Di=1, Dj=1 | Y=1) - P(Di=1 | Y=1) · P(Dj=1 | Y=1)" where negative values indicate negative interactions between perturbation pairs.

## Benchmark Scale

LIBERO-Plus comprises "10,030 tasks spanning seven perturbation dimensions" with over 20,000 successful trajectories collected under systematically varied conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e39f9f1-ca24-4d39-9ac7-6d90b6cf049f",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "49ab52ce-af74-4ad0-a66c-1df43757a72a",
  "sourceToolAssistantUUID": "6e39f9f1-ca24-4d39-9ac7-6d90b6cf049f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T11:12:35.550Z_

<details><summary>↩ Tool result · `toolu_01ULA9B8PqczvmkX3LtiFQVR`</summary>

```text
# LIBERO-Plus: Perturbation Framework Technical Details

## 1. Seven Perturbation Dimensions

**Objects Layout (O1-O2):**
- O1 adds "n additional unseen objects into the task scene" from a set of 416 distractor objects via BDDL modifications
- O2 applies "random perturbations to the target object's initial position (x,y,z) and orientation" while preserving semantic relationships

**Background Textures (B1-B2):**
- B1 changes "scene texture of the environment" using 950 curated textures via XML scene definition files
- B2 randomly alters "texture of the working surface (e.g., tabletop or floor)"

**Light Conditions (L1-L4):**
- L1: Diffuse color adjustment via RGB channels
- L2: Parallel light source direction changes
- L3: Specular highlight intensity (affecting reflective surfaces)
- L4: Boolean shadow casting control

**Camera Viewpoints (C1-C3):**
- C1: Distance scaling from 1.01× to 2.00× original value along optical axis
- C2: Spherical position changes with azimuth (Δθ) and elevation (Δφ) within 15°–75° cones
- C3: Camera orientation perturbation (yaw, pitch, roll) within 2°–10°

**Robot Initial States:**
- "Random perturbations are applied to the robot arm's initial joint positions" with magnitudes 0.1–0.5 via Problem class interface modifications

**Language Instructions (R1-R3):**
- R1: Distraction rewrites adding task-irrelevant contextual information
- R2: Commonsense-based object description replacements
- R3: Reasoning complexity alterations for multi-step tasks

**Sensor Noise (N1-N5):**
- Motion Blur: kernel radius (r=5 to 35), Gaussian σ (2 to 20), angle θ ∈ U(-45°, 45°)
- Gaussian Blur: σ from 1 to 10
- Zoom Blur: scaling factors [s_min, s_max, step] from [1, 1.11, 0.01] to [1, 1.56, 0.03]
- Fog: density α (0.5–5.0), decay rate β (1.3–3.0)
- Glass Blur: σ (0.5–2.5), pixel displacement δ (1–5), iterations (1–3)

## 2. Simulation Implementation

**Environment Framework:** LIBERO benchmark built on MuJoCo physics engine via robosuite

**Implementation Methods:**
- Object layout modifications: "modifying the task description files (BDDL)"
- Background/lighting: "modifying scene XML definition files" and "registering new scene classes"
- Camera changes: "modifying the Problem class interface, with parameters derived from task filenames"
- Robot initial states: "modifying the Problem class interface"
- Sensor noise: Applied via image-space post-processing (albumentations-style transformations)

No wrist camera distortions noted; perturbations target third-person camera observations primarily.

## 3. Difficulty Levels L1-L5

Stratification based on multi-model consensus from OpenVLA-OFT, π0, π0-fast, and UniVLA:

- **L1:** Solved by all four models
- **L2:** Solved by exactly three models
- **L3:** Solved by exactly two models
- **L4:** Solved by exactly one model
- **L5:** Solved by none

"Figure 7 illustrates the proportion of tasks at each difficulty level for every dimension," showing imbalanced distributions across perturbation types.

## 4. Training Data Augmentation

**Dataset Scale:** "Over 20,000 successful trajectories" generated from expanded LIBERO base

**Generation Process:**
- Objects: 2,400 trajectories with distractor variations (non-overlapping with test set)
- Other dimensions: 4,000 trajectories each (light, camera, background, language, noise)
- Total before filtering: 22,400 trajectories; "over 20,000 high-quality trajectories retained"

**Filtering:** "Only successful trajectories were retained, and any actions corresponding to no-ops were filtered out"

**Storage Format:** "All trajectories are stored in the rlds format, consistent with standard practices"

## 5. LIBERO Integration

**Benchmark Construction:**
- Started with 40 evaluation tasks, generated 500 instances per LIBERO sub-task (Spatial, Object, Goal, Long)
- Initial pool: 14,000 candidates; final test set: "10,030 tasks spanning seven perturbation factors with twenty-one low-level components"

**Task Filtering:** Tasks solved by all or large majorities were excluded; remaining tasks balanced across sub-dimensions

**Distribution:** Final dataset spans all four LIBERO suites with representation shown in Table 7 (approximately 1,500-2,600 tasks per dimension)

## 6. Technical Implementation Details

**Lighting Parameters (from Table 5 context):** XML-based control enabling precise diffuse/specular/direction/shadow manipulation

**Camera Parameters:** Spherical coordinate system with degree-based precision; first-person wrist camera (when present) receives fewer perturbations than third-person view

**Noise Application:** Image-space transforms applied post-rendering; fog and blur effects use standard computer vision parameterization

**Language Perturbations:** "LLMs to rewrite original task instructions" (specific LLM model not disclosed in excerpt)

---

**Key Finding:** "Models are most vulnerable to changes in camera viewpoint and robot initial state," while "background variations...constitute more superficial, low-level visual changes," suggesting the framework effectively stratifies perturbation semantic depth.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b42c9831-be67-4fb5-9f04-0d9a6cda15a0",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "023485b5-f9d2-4082-87bf-9e2fc30b13c0",
  "sourceToolAssistantUUID": "b42c9831-be67-4fb5-9f04-0d9a6cda15a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-15T11:12:39.471Z_

Now let me get more details on the GitHub repo structure, LIBERO's original simulation capabilities, and LIBERO-PRO (since it also appeared in search results and may have relevant perturbation info).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "023485b5-f9d2-4082-87bf-9e2fc30b13c0",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FjdqMYQtRQ3pwso5PZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3dbb544-8bd3-4e25-8901-2871c5c097bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eJ2NyPG9VENPy3EL2HLdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 410,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 20130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2540,
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

_source line 23 · 2026-05-15T11:12:40.429Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PBsuwnMvyKfQdEfvR9YP4Q`</summary>

```json
{
  "url": "https://github.com/sylvestf/LIBERO-plus",
  "prompt": "Extract the full repository structure, installation commands, configuration details, how to run evaluation, and any code examples. Include exact pip install commands, asset download links, and configuration file paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3dbb544-8bd3-4e25-8901-2871c5c097bf",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FjdqMYQtRQ3pwso5PZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d7ed0d6-85c3-46ac-b444-2d73e070ee33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eJ2NyPG9VENPy3EL2HLdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 410,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 20130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2540,
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

_source line 24 · 2026-05-15T11:12:41.422Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016fwVuh2KUdmNnLe8tZkWZV`</summary>

```json
{
  "query": "LIBERO robosuite MuJoCo built-in camera randomization lighting randomization domain randomization config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d7ed0d6-85c3-46ac-b444-2d73e070ee33",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FjdqMYQtRQ3pwso5PZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5a2486e-7a44-4f63-8fd3-49c3ded605c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eJ2NyPG9VENPy3EL2HLdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 410,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 20130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2540,
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

_source line 25 · 2026-05-15T11:12:41.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JciYF7tRfPJRqeRRAcxXdu`</summary>

```json
{
  "query": "site:github.com Lifelong-Robot-Learning LIBERO domain randomization camera jitter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5a2486e-7a44-4f63-8fd3-49c3ded605c1",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FjdqMYQtRQ3pwso5PZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a60d5ca5-3f91-4570-bfd5-fb85b6aeda6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eJ2NyPG9VENPy3EL2HLdN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 410,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 20130,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2540
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 410,
          "output_tokens": 277,
          "cache_read_input_tokens": 20130,
          "cache_creation_input_tokens": 2540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2540,
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

_source line 26 · 2026-05-15T11:12:47.581Z_

<details><summary>↩ Tool result · `toolu_01JciYF7tRfPJRqeRRAcxXdu`</summary>

```text
Web search results for query: "site:github.com Lifelong-Robot-Learning LIBERO domain randomization camera jitter"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"Issues · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues"},{"title":"Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning"},{"title":"Technical details Regarding LIBERO Dataset · Issue #95 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/95"},{"title":"Issues with Playback · Issue #16 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/16"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO-Object image rendering issue: darker floors · Issue #88 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/88"},{"title":"LIBERO/README.md at master · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/blob/master/README.md"},{"title":"Activity · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/activity"},{"title":"collect_demonstrations.py · Issue #48 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/48"}]

The search returned results from the LIBERO GitHub repository and related pages. LIBERO is designed for studying knowledge transfer in multitask and lifelong robot learning problems. It provides a procedural generation pipeline that could generate an infinite number of manipulation tasks, with 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

While the search results contain general information about LIBERO, the specific terms "domain randomization" and "camera jitter" do not appear in the returned pages. The results show information about the benchmark structure, setup instructions, and some issues related to rendering and environment setup, but they don't specifically address domain randomization or camera jitter perturbations in LIBERO.

If you're looking for specific documentation about domain randomization or camera jitter features in LIBERO, you may need to check the actual LIBERO codebase files directly on the GitHub repository, or consult the paper or more detailed technical documentation associated with the project.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a60d5ca5-3f91-4570-bfd5-fb85b6aeda6e",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "e5e92419-de25-4f6a-893c-69a55d572236",
  "sourceToolAssistantUUID": "a60d5ca5-3f91-4570-bfd5-fb85b6aeda6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T11:12:47.914Z_

<details><summary>↩ Tool result · `toolu_01PBsuwnMvyKfQdEfvR9YP4Q`</summary>

````text
# LIBERO-Plus Repository Summary

## Overview
LIBERO-Plus is "a generalized benchmark for in-depth robustness analysis of vision-language-action models" offering comprehensive evaluation across 7 perturbation dimensions with 10,030 tasks.

## Installation Commands

```bash
# Clone repository
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus

# Uninstall existing LIBERO if present

# Install package
pip install -e .

# Install system dependencies
apt install libexpat1
apt install libfontconfig1-dev
apt install libpython3-stdlib
apt-get install libmagickwand-dev

# Install additional Python requirements
pip install -r extra_requirements.txt
```

## Asset Download & Configuration

**Assets Location:** Download from [Hugging Face LIBERO-plus dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main)

**Installation Path:** Extract `assets.zip` to `LIBERO-plus/libero/libero/`

**Configuration File:** `/root/.libero/config.yaml` (verify repo path in `libero/__init__.py`)

**Required Asset Structure:**
```
libero/libero/assets/
├── articulated_objects/
├── new_objects/
├── scenes/
├── stable_hope_objects/
├── stable_scanned_objects/
├── textures/
├── turbosquid_objects/
└── supporting XML/STL files
```

## Evaluation Setup

Modify configuration to set `num_trials_per_task: 1` (adjusted from original 50). Task mappings between IDs, perturbation categories, and difficulty levels are provided in `.libero/libero/benchmark/task_classification.json`.

## Additional Resources

- **RLDS Training Dataset:** Available on Hugging Face
- **Fine-tuned Model:** OpenVLA-OFT weights after mix-SFT provided
- **LeRobot Dataset:** Alternative training dataset available

## Key Performance Metrics

Top-performing model (OpenVLA-OFT+) achieves 79.6% average across perturbation categories, with particularly strong results in camera robustness (92.8%) and light conditions (94.9%).
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d7ed0d6-85c3-46ac-b444-2d73e070ee33",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "58463115-31e4-4adc-a26d-b5a467a2a9fc",
  "sourceToolAssistantUUID": "9d7ed0d6-85c3-46ac-b444-2d73e070ee33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T11:12:48.674Z_

<details><summary>↩ Tool result · `toolu_016fwVuh2KUdmNnLe8tZkWZV`</summary>

```text
Web search results for query: "LIBERO robosuite MuJoCo built-in camera randomization lighting randomization domain randomization config"

Links: [{"title":"Demo Showcases — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/demos.html"},{"title":"robosuite/robosuite/utils/mjmod.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py"},{"title":"Environments — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/modules/environments.html"},{"title":"Sim-to-Real Transfer — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/algorithms/sim2real.html"},{"title":"Changelog — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/changelog.html"},{"title":"robosuite.utils package — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/source/robosuite.utils.html"},{"title":"robosuite | robosuite: A Modular Simulation Framework and Benchmark for Robot Learning","url":"https://robosuite.ai/"},{"title":"GitHub - ARISE-Initiative/robosuite: robosuite: A Modular Simulation Framework and Benchmark for Robot Learning · GitHub","url":"https://github.com/ARISE-Initiative/robosuite"},{"title":"robosuite · PyPI","url":"https://pypi.org/project/robosuite/"},{"title":"GitHub - Robot-Learning-Library/robolite: This is a fork of Surreal Robotics Suite that enables support to domain randomization and inverse kinematics (IK).","url":"https://github.com/Robot-Learning-Library/robolite"}]

Based on the search results, here's what I found about LIBERO, robosuite, MuJoCo, and domain randomization features:

## Domain Randomization in Robosuite

Domain randomization can be easily enabled by wrapping an environment with the DomainRandomizationWrapper, with randomization functionality focusing on visual variations, including colors, textures, and camera viewpoints.

## Randomization Modders

Robosuite provides three main Modders: CameraModder for controlling camera parameters including FOV and pose, TextureModder for controlling visual objects' appearances including texture and material properties, and LightingModder for controlling lighting parameters including light source properties and pose.

## Camera Randomization Parameters

The randomization system includes parameters like camera_names (list of camera names to use for randomization, with all cameras used if not provided) and rotation_perturbation_size (magnitude of camera rotation perturbations in axis-angle, defaulting to around 5 degrees).

## Documentation and Examples

The demo_domain_randomization.py script showcases domain randomization functionality.

The search results provide information about robosuite's built-in camera, lighting, and visual randomization capabilities, but don't include specific information about LIBERO itself. LIBERO is a benchmark that builds on top of robosuite, so these randomization features would be available for use with LIBERO environments as well.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5a2486e-7a44-4f63-8fd3-49c3ded605c1",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "0c0bb3c2-d800-4325-bdad-a6e61f9a0b1d",
  "sourceToolAssistantUUID": "c5a2486e-7a44-4f63-8fd3-49c3ded605c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-15T11:12:51.782Z_

Now let me get the robosuite domain randomization details and also check the LIBERO-Plus implementation specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c0bb3c2-d800-4325-bdad-a6e61f9a0b1d",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4Fkc8SoGVqKtRgChsek",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77871654-2910-4707-8c1f-1648a4e33f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BagSeBG8mMDsQNn9y1Jgtg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 802,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 22670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
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

_source line 30 · 2026-05-15T11:12:53.272Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EQVJbHhLUGi7rXZfsu1QcS`</summary>

```json
{
  "url": "https://robosuite.ai/docs/algorithms/sim2real.html",
  "prompt": "Extract all details about domain randomization in robosuite: CameraModder, TextureModder, LightingModder parameters, DomainRandomizationWrapper usage, configuration options, parameter ranges, and code examples. Include exact API details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77871654-2910-4707-8c1f-1648a4e33f34",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4Fkc8SoGVqKtRgChsek",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b8b5a3f-9028-4087-91cb-c8b67d5f9d9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BagSeBG8mMDsQNn9y1Jgtg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 802,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 22670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
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

_source line 31 · 2026-05-15T11:12:55.116Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Dvd7vLwaSK4nd3scbSqZNa`</summary>

```json
{
  "url": "https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py",
  "prompt": "Extract the CameraModder, TextureModder, and LightingModder class definitions. Include all parameters they can modify, default values, and method signatures. Focus on what visual properties can be randomized."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b8b5a3f-9028-4087-91cb-c8b67d5f9d9d",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4Fkc8SoGVqKtRgChsek",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acf32032-82c0-47cf-beec-39552c1de4ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BagSeBG8mMDsQNn9y1Jgtg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 802,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 22670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
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

_source line 32 · 2026-05-15T11:12:56.198Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GPqQRYBRGsJeYhttZTzWCi`</summary>

```json
{
  "url": "https://huggingface.co/datasets/Sylvest/LIBERO-plus",
  "prompt": "Extract all details about the LIBERO-plus dataset: file structure, download instructions, dataset contents, how the training data is organized, and any usage instructions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acf32032-82c0-47cf-beec-39552c1de4ca",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4Fkc8SoGVqKtRgChsek",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1db165f1-52bd-464f-8c35-fa915fb533b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BagSeBG8mMDsQNn9y1Jgtg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 802,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 22670,
      "output_tokens": 391,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 802,
          "output_tokens": 391,
          "cache_read_input_tokens": 22670,
          "cache_creation_input_tokens": 2074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2074,
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

_source line 33 · 2026-05-15T11:12:58.982Z_

<details><summary>↩ Tool result · `toolu_01EQVJbHhLUGi7rXZfsu1QcS`</summary>

```text
# Domain Randomization in robosuite

Based on the documentation, robosuite provides three primary `Modder` classes for visual domain randomization:

## Visual Modders

**CameraModder**: Handles camera parameters including field of view and positioning adjustments.

**TextureModder**: Controls the appearance of simulation objects through texture and material property modifications.

**LightingModder**: Manages lighting environment by adjusting light source characteristics and their spatial placement.

The documentation notes that these tools enable users to either "directly override default simulation settings, or to randomize their respective properties mid-sim."

## Dynamics Randomization

The `DynamicsModder` class addresses physics parameter variation across four categories:

**Global Parameters** (Opt): density and viscosity of the medium

**Body Parameters**: position, quaternion orientation, inertia components, and mass

**Geom Parameters**: friction coefficients (sliding, torsional, rolling), contact solver values (solref), and impedance settings (solimp)

**Joint Parameters**: stiffness, friction loss, damping, and armature values

## API Usage Pattern

The basic workflow involves creating the modder instance, calling `.mod()` to adjust parameters, then invoking `.update()` to propagate changes into the simulation. The documentation includes a code example demonstrating modification of cube mass and friction values, followed by restoration of defaults.

The system includes "sanity checks to prevent presumably undesired / non-sensical behavior" such as preventing damping additions to free joints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b8b5a3f-9028-4087-91cb-c8b67d5f9d9d",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "6a5ffa9d-a3ea-46d4-913e-7125ae2bd719",
  "sourceToolAssistantUUID": "5b8b5a3f-9028-4087-91cb-c8b67d5f9d9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T11:13:01.308Z_

<details><summary>↩ Tool result · `toolu_01Dvd7vLwaSK4nd3scbSqZNa`</summary>

```text
# Visual Property Randomization in Robosuite

## LightingModder

The LightingModder class enables domain randomization for light sources. Key parameters include:

**Modifiable Properties:**
- Position (with `position_perturbation_size=0.1`)
- Direction (with `direction_perturbation_size=0.35`)
- Specular attribute (with `specular_perturbation_size=0.1`)
- Ambient attribute (with `ambient_perturbation_size=0.1`)
- Diffuse attribute (with `diffuse_perturbation_size=0.1`)
- Active status (on/off)

**Key Methods:** `randomize()`, `save_defaults()`, `restore_defaults()`, and individual getters/setters for each property.

## CameraModder

This modder adjusts camera viewing parameters during simulation. Configurable aspects are:

**Modifiable Properties:**
- Position (with `position_perturbation_size=0.01`)
- Rotation/orientation via quaternions (with `rotation_perturbation_size=0.087`)
- Field of view (fovy) in degrees (with `fovy_perturbation_size=5.0`)

**Key Methods:** `randomize()`, `_randomize_position()`, `_randomize_rotation()`, `_randomize_fovy()`, plus accessor methods for position, quaternion orientation, and fovy values.

## TextureModder

This comprehensive modder handles surface appearance changes. As noted, "in order for the textures to take full effect, you'll need to set the rgba values for all materials to [1, 1, 1, 1]."

**Modifiable Properties:**
- RGB colors (with `local_rgb_interpolation=0.1`)
- Texture patterns: RGB, checker, noise, gradient
- Material properties: reflectance, shininess, specular (with `local_material_interpolation=0.2`)
- Skybox textures (when `randomize_skybox=True`)

**Key Methods:** `randomize()`, `rand_rgb()`, `rand_checker()`, `rand_gradient()`, `rand_noise()`, plus material and texture management functions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acf32032-82c0-47cf-beec-39552c1de4ca",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "8249f956-94d0-469a-96a8-f0ac91e11816",
  "sourceToolAssistantUUID": "acf32032-82c0-47cf-beec-39552c1de4ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T11:13:07.228Z_

<details><summary>↩ Tool result · `toolu_01GPqQRYBRGsJeYhttZTzWCi`</summary>

````text
# LIBERO-plus Dataset Details

## Overview
LIBERO-plus is a comprehensive robustness benchmark for Vision-Language-Action (VLA) models containing **10,030 tasks** across 7 perturbation dimensions. It extends the original LIBERO benchmark with systematic robustness evaluation.

## File Structure

After extraction, the directory structure should be:

```
LIBERO-plus/
└── libero/
    └── libero/
        └── assets/
            ├── articulated_objects/
            ├── new_objects/
            ├── scenes/
            ├── stable_hope_objects/
            ├── stable_scanned_objects/
            ├── textures/
            ├── turbosquid_objects/
            ├── serving_region.xml
            ├── wall_frames.stl
            └── wall.xml
```

## Installation Instructions

```bash
# Clone the repository
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus

# Install system dependencies
apt install libexpat1
apt install libfontconfig1-dev
apt install libpython3-stdlib
apt-get install libmagickwand-dev

# Install Python package
pip install -e .
pip install -r extra_requirements.txt
```

**Note:** If you have the original LIBERO installed, uninstall it first. Update the config path at `/root/.libero/config.yaml`.

## Dataset Contents

### 7 Perturbation Dimensions

1. **Objects Layout** - Confounding objects and target object displacement
2. **Camera Viewpoints** - Position, orientation, and field-of-view changes
3. **Robot Initial States** - Manipulator initial pose variations
4. **Language Instructions** - LLM-based instruction rewriting
5. **Light Conditions** - Intensity, direction, color, and shadow variations
6. **Background Textures** - Scene and surface appearance changes
7. **Sensor Noise** - Photometric distortions and image degradation

### Total Size
**6.4 GB** with 1,591 downloads

## Training Data

**Location:** [LIBERO-plus RLDS Dataset](https://huggingface.co/datasets/Sylvest/libero_plus_rlds/tree/main)

**Pre-trained Model:** [OpenVLA-7B-OFT Fine-tuned](https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata/tree/main)

## Download Instructions

1. Download assets from the [Hugging Face LIBERO-plus repository](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main)
2. Unzip `assets.zip` to `LIBERO-plus/libero/libero/` path
3. Update config file path if needed

## Usage Instructions

### Evaluation

```python
# Modify your configuration
# Change: num_trials_per_task: 50 → num_trials_per_task: 1
```

The evaluation method is nearly identical to LIBERO; only adjust `num_trials_per_task` from 50 to 1 in your configuration.

### Key Usage Note

> "You can simply replace the original `libero` with a `pip install -e .` without modifying your code."

## Evaluated Models

- OpenVLA and variants (OFT, OFT_w, OFT_m)
- π₀ and π₀-fast
- Nora, WorldVLA, UniVLA, RIPT-VLA

## Resources

- 📄 **Paper:** [arXiv:2510.13626](https://arxiv.org/pdf/2510.13626v1)
- 🏗️ **Repository:** [GitHub](https://github.com/sylvestf/LIBERO-plus)
- 🌐 **Website:** [Project Page](https://sylvestf.github.io/LIBERO-plus)
- 📁 **Training Dataset:** [LIBERO-plus RLDS](https://huggingface.co/datasets/Sylvest/libero_plus_rlds)

## Citation

```bibtex
@article{fei25libero-plus,
    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},
    author={Senyu Fei and Siyin Wang and Junhao Shi and others},
    journal = {arXiv preprint arXiv:2510.13626},
    year={2025},
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1db165f1-52bd-464f-8c35-fa915fb533b8",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "ca567609-5b88-46b6-a5b4-97c1d6b9f928",
  "sourceToolAssistantUUID": "1db165f1-52bd-464f-8c35-fa915fb533b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-15T11:13:09.964Z_

Let me also check for the robosuite DomainRandomizationWrapper specifically to see how it can be used with LIBERO.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca567609-5b88-46b6-a5b4-97c1d6b9f928",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FmyJSau881yp2twDrX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f2d35a0-6b08-4466-be35-5751af7833da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcg3e7hKqM6XFSjemhxDjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 24744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3249,
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

_source line 37 · 2026-05-15T11:13:11.041Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BqbiFe79oqYoM9EKEEJnm2`</summary>

```json
{
  "query": "robosuite DomainRandomizationWrapper example code camera_names randomize_color randomize_camera"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f2d35a0-6b08-4466-be35-5751af7833da",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FmyJSau881yp2twDrX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40102fe4-9856-47f3-8836-2428a669a2d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcg3e7hKqM6XFSjemhxDjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 24744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3249,
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

_source line 38 · 2026-05-15T11:13:11.555Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011PMJHQNu2JmfTbUvAjCCtZ`</summary>

```json
{
  "query": "LIBERO-Plus training augmentation reuse perturbation training time data augmentation robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40102fe4-9856-47f3-8836-2428a669a2d1",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FmyJSau881yp2twDrX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0094bb74-c15f-4874-8be1-a4f8a924965b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcg3e7hKqM6XFSjemhxDjW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 24744,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3249
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 24744,
          "cache_creation_input_tokens": 3249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3249,
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

_source line 39 · 2026-05-15T11:13:17.872Z_

<details><summary>↩ Tool result · `toolu_01BqbiFe79oqYoM9EKEEJnm2`</summary>

````text
Web search results for query: "robosuite DomainRandomizationWrapper example code camera_names randomize_color randomize_camera"

Links: [{"title":"Demo Showcases — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/demos.html"},{"title":"robosuite/robosuite/utils/camera_utils.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/camera_utils.py"},{"title":"Sim-to-Real Transfer — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/algorithms/sim2real.html"},{"title":"robosuite/robosuite/demos/demo_segmentation.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/demos/demo_segmentation.py"},{"title":"GitHub - quantumiracle/robolite: This is a fork of Surreal Robotics Suite that enables support to domain randomization and inverse kinematics (IK). · GitHub","url":"https://github.com/quantumiracle/robolite"},{"title":"robosuite | robosuite: A Modular Simulation Framework and Benchmark for Robot Learning","url":"https://robosuite.ai/"},{"title":"robosuite/robosuite/environments/manipulation/stack.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/environments/manipulation/stack.py"},{"title":"robosuite.environments.manipulation package — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/source/robosuite.environments.manipulation.html"},{"title":"robosuite.utils package — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/source/robosuite.utils.html"},{"title":"Environments — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/modules/environments.html"}]

Based on the search results, here's what I found about the DomainRandomizationWrapper in robosuite:

## DomainRandomizationWrapper Overview

The randomization functionality focuses on visual variations, including colors, textures, and camera viewpoints.

## Example Code

Here's an example of using the DomainRandomizationWrapper with parameters:

```python
default_dr_args = {
    "seed": 1,
    "randomize_camera": False,
    "randomize_every_n_steps": 10,
}
default_dr_args.update(dr_args)
env = DomainRandomizationWrapper(
    env=self.env,
    **default_dr_args,
)
```


## Related Randomization Tools

robosuite provides various Modder classes to control different aspects of the visual environment, including: CameraModder for controlling camera parameters like FOV and pose, TextureModder for controlling visual objects' appearances including texture and material properties, and LightingModder for controlling lighting parameters.

The demo_domain_randomization.py script showcases all of these modders being applied to randomize an environment during every sim step.

## Camera Names Parameter

The camera_names parameter specifies the name of camera to be rendered, and should either be a single string if the same name is to be used for all cameras' rendering or a list of cameras to render.

The search results show example usage of the wrapper with basic parameters, though specific documentation on all the detailed parameters like `randomize_color` wasn't fully detailed in these results. For complete parameter documentation, you may want to check the official robosuite GitHub repository or API documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40102fe4-9856-47f3-8836-2428a669a2d1",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "b628a0f6-3291-4498-859c-53909ef27ee1",
  "sourceToolAssistantUUID": "40102fe4-9856-47f3-8836-2428a669a2d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T11:13:19.437Z_

<details><summary>↩ Tool result · `toolu_011PMJHQNu2JmfTbUvAjCCtZ`</summary>

```text
Web search results for query: "LIBERO-Plus training augmentation reuse perturbation training time data augmentation robustness"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"RL with LIBERO-Pro & LIBERO-Plus Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/liberoplus_pro.html"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"}]

I've found comprehensive information about LIBERO-Plus and related research. Here's what the search reveals:

## LIBERO-Plus Overview

LIBERO-Plus is an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, with a diverse training dataset containing over 20,000 successful trajectories collected under systematically varied conditions.

## Training Data Augmentation and Diversity

Training strategies that emphasize diversity and exposure to varied data distributions consistently yield more robust models across multiple perturbation types. The research demonstrates that an automated generalization pipeline was used to construct an extensive training dataset comprising over 20,000 successful trajectories through substantial expansion of the original LIBERO benchmark, greatly increasing the number of trajectories and scene diversity.

## Perturbation Robustness Testing

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise. Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

## Key Findings

Training data diversity significantly improves robustness. Additionally, models incorporating a first-person wrist camera demonstrate superior generalization compared to those reliant solely on a third-person view, and training strategies that emphasize diversity and co-training consistently yield more robust models across multiple perturbation types.

The research highlights that recent extensions reuse original training trajectories, introducing perturbations but model them independently, failing to capture complex distribution shifts, which LIBERO-Plus aims to address through its comprehensive augmentation approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0094bb74-c15f-4874-8be1-a4f8a924965b",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "96a55e22-9bcd-43b3-b555-ee69a6b2323e",
  "sourceToolAssistantUUID": "0094bb74-c15f-4874-8be1-a4f8a924965b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-15T11:13:22.300Z_

Let me get more details on the robosuite DomainRandomizationWrapper and also check LIBERO-X which appeared in results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96a55e22-9bcd-43b3-b555-ee69a6b2323e",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FnsUEUq6bTT1NdpaXv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32da33f6-18dd-4270-8acf-95c49f17ebab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nBBJpzXWbgJoCiqjarh4c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2026,
      "cache_read_input_tokens": 27993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2026,
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

_source line 42 · 2026-05-15T11:13:23.640Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RiDfFZebcFLHam2jDutLqe`</summary>

```json
{
  "url": "https://robosuite.ai/docs/demos.html",
  "prompt": "Extract the full domain randomization demo details: DomainRandomizationWrapper parameters, how to use it, what it randomizes (camera, texture, lighting, dynamics), code examples, and all configurable parameters with their defaults."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32da33f6-18dd-4270-8acf-95c49f17ebab",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FnsUEUq6bTT1NdpaXv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca9579e0-3a10-4ba7-a5be-1cfe8447ff37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nBBJpzXWbgJoCiqjarh4c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2026,
      "cache_read_input_tokens": 27993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2026,
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

_source line 43 · 2026-05-15T11:13:25.095Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AGdrLDS92VXhX7N9wUnxbB`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
  "prompt": "Extract all details about LIBERO-plus integration with LeRobot: setup instructions, how to use the dataset, training commands, and any code examples for using LIBERO-plus perturbations during training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca9579e0-3a10-4ba7-a5be-1cfe8447ff37",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FnsUEUq6bTT1NdpaXv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6eaa64f-e15e-4c38-a451-866993ac8943",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nBBJpzXWbgJoCiqjarh4c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2026,
      "cache_read_input_tokens": 27993,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2026
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 275,
          "cache_read_input_tokens": 27993,
          "cache_creation_input_tokens": 2026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2026,
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

_source line 44 · 2026-05-15T11:13:25.100Z_

<details><summary>↩ Tool result · `toolu_01AGdrLDS92VXhX7N9wUnxbB`</summary>

````text
# LIBERO-plus

LIBERO-plus is a **robustness benchmark** for Vision-Language-Action (VLA) models built on top of [LIBERO](./libero). It systematically stress-tests policies by applying **seven independent perturbation dimensions** to the original LIBERO task set, exposing failure modes that standard benchmarks miss.

- Paper: [In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626)
- GitHub: [sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)
- Dataset: [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

![An overview of the LIBERO-plus benchmark perturbation dimensions](https://github.com/sylvestf/LIBERO-plus/raw/main/static/images/libero-plus.jpg)

## Perturbation dimensions

LIBERO-plus creates ~10 000 task variants by perturbing each original LIBERO task along these axes:

| Dimension             | What changes                                          |
| --------------------- | ----------------------------------------------------- |
| Objects layout        | Target position, presence of confounding objects      |
| Camera viewpoints     | Camera position, orientation, field-of-view           |
| Robot initial states  | Manipulator start pose                                |
| Language instructions | LLM-rewritten task description (paraphrase / synonym) |
| Light conditions      | Intensity, direction, color, shadow                   |
| Background textures   | Scene surface and object appearance                   |
| Sensor noise          | Photometric distortions and image degradation         |

## Available task suites

LIBERO-plus covers the same five suites as LIBERO:

| Suite          | CLI name         | Tasks | Max steps | Description                                        |
| -------------- | ---------------- | ----- | --------- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | 280       | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | 280       | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | 300       | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | 400       | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | 520       | Long-horizon tasks from the LIBERO-100 collection  |

  Installing LIBERO-plus **replaces** vanilla LIBERO — it uninstalls `hf-libero`
  so that `import libero` resolves to the LIBERO-plus fork. You cannot have both
  installed at the same time. To switch back to vanilla LIBERO, uninstall the
  fork and reinstall with `pip install -e ".[libero]"`.

## Installation

### System dependencies (Linux only)

```bash
sudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev
```

### Python package

```bash
pip install -e ".[libero]" "robosuite==1.4.1" bddl easydict mujoco wand scikit-image gym
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus && pip install --no-deps -e .
pip uninstall -y hf-libero  # so `import libero` resolves to the fork
```

LIBERO-plus is installed from its GitHub fork rather than a pyproject extra — the fork ships as a namespace package that pip can't handle, so it must be cloned and added to `PYTHONPATH`. See `docker/Dockerfile.benchmark.libero_plus` for the canonical install. MuJoCo is required, so only Linux is supported.

Set the MuJoCo rendering backend before running evaluation:

```bash
export MUJOCO_GL=egl   # headless / HPC / cloud
```

### Download LIBERO-plus assets

LIBERO-plus ships its extended asset pack separately. Download `assets.zip` from the [Hugging Face dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) and extract it into the LIBERO-plus package directory:

```bash
# After installing the package, find where it was installed:
python -c "import libero; print(libero.__file__)"
# Then extract assets.zip into &lt;package_root>/libero/assets/
```

## Evaluation

### Default evaluation (recommended)

Evaluate across the four standard suites (10 episodes per task):

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

### Single-suite evaluation

Evaluate on one LIBERO-plus suite:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial \
  --eval.batch_size=1 \
  --eval.n_episodes=10
```

- `--env.task` picks the suite (`libero_spatial`, `libero_object`, etc.).
- `--env.task_ids` restricts to specific task indices (`[0]`, `[1,2,3]`, etc.). Omit to run all tasks in the suite.
- `--eval.batch_size` controls how many environments run in parallel.
- `--eval.n_episodes` sets how many episodes to run per task.

### Multi-suite evaluation

Benchmark a policy across multiple suites at once by passing a comma-separated list:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object \
  --eval.batch_size=1 \
  --eval.n_episodes=10
```

### Control mode

LIBERO-plus supports two control modes — `relative` (default) and `absolute`. Different VLA checkpoints are trained with different action parameterizations, so make sure the mode matches your policy:

```bash
--env.control_mode=relative   # or "absolute"
```

### Policy inputs and outputs

**Observations:**

- `observation.state` — 8-dim proprioceptive features (eef position, axis-angle orientation, gripper qpos)
- `observation.images.image` — main camera view (`agentview_image`), HWC uint8
- `observation.images.image2` — wrist camera view (`robot0_eye_in_hand_image`), HWC uint8

**Actions:**

- Continuous control in `Box(-1, 1, shape=(7,))` — 6D end-effector delta + 1D gripper

### Recommended evaluation episodes

For reproducible benchmarking, use **10 episodes per task** across all four standard suites (Spatial, Object, Goal, Long). This gives 400 total episodes and matches the protocol used for published results.

## Training

### Dataset

A LeRobot-format training dataset for LIBERO-plus is available at:

- [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

### Example training command

```bash
lerobot-train \
    --policy.type=smolvla \
    --policy.repo_id=${HF_USER}/smolvla_libero_plus \
    --policy.load_vlm_weights=true \
    --dataset.repo_id=lerobot/libero_plus \
    --env.type=libero_plus \
    --env.task=libero_spatial \
    --output_dir=./outputs/ \
    --steps=100000 \
    --batch_size=4 \
    --eval.batch_size=1 \
    --eval.n_episodes=1 \
    --eval_freq=1000
```

## Relationship to LIBERO

LIBERO-plus is a drop-in extension of LIBERO:

- Same Python gym interface (`LiberoEnv`, `LiberoProcessorStep`)
- Same camera names and observation/action format
- Same task suite names
- Installs under the same `libero` Python package name (different GitHub repo)

To use the original LIBERO benchmark, see [LIBERO](./libero) and use `--env.type=libero`.


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6eaa64f-e15e-4c38-a451-866993ac8943",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "de5cbc3b-e96b-4a27-b11e-1c90c1e10d39",
  "sourceToolAssistantUUID": "e6eaa64f-e15e-4c38-a451-866993ac8943",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T11:13:28.000Z_

<details><summary>↩ Tool result · `toolu_01RiDfFZebcFLHam2jDutLqe`</summary>

```text
# Domain Randomization Demo Details

Based on the provided documentation, the information available about the Domain Randomization demo is limited:

## What the Documentation States

The `demo_domain_randomization.py` script is described as showcasing "domain randomization functionality." According to the content, this feature "can be easily enabled by wrapping an environment with the DomainRandomizationWrapper."

The documentation specifies that **"the randomization functionality focuses on visual variations, including colors, textures, and camera viewpoints."**

## Limitations of Available Information

Unfortunately, the provided webpage content does not include:
- Specific parameters for the DomainRandomizationWrapper
- Code examples showing implementation
- Default values for any configurable settings
- Details on dynamics randomization (though it mentions visual variations only)
- Detailed usage instructions beyond wrapping an environment

## Recommendation

To obtain comprehensive details about DomainRandomizationWrapper parameters, code examples, and all configurable options, you would need to:
1. Consult the full robosuite source code repository
2. Review the `robosuite.wrappers` module documentation
3. Examine the actual `demo_domain_randomization.py` script in the [robosuite GitHub repository](https://github.com/ARISE-Initiative/robosuite)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca9579e0-3a10-4ba7-a5be-1cfe8447ff37",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "de363c52-98c1-424c-a0db-5b802d2dc8b3",
  "sourceToolAssistantUUID": "ca9579e0-3a10-4ba7-a5be-1cfe8447ff37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-15T11:13:30.881Z_

Now let me get the robosuite wrapper source code for exact parameters.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de363c52-98c1-424c-a0db-5b802d2dc8b3",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FoW4eXF2G8UDJBLMJW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2fb59eb-da6f-4d82-a135-99c233eec199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP6stPQt8vGELWxtjKhmDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2197,
      "cache_creation_input_tokens": 596,
      "cache_read_input_tokens": 30019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 596,
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

_source line 47 · 2026-05-15T11:13:31.728Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H5fcnANzeubgqZen5nvqc7`</summary>

```json
{
  "url": "https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/wrappers/domain_randomization_wrapper.py",
  "prompt": "Extract the complete DomainRandomizationWrapper class definition including all constructor parameters, their defaults, and descriptions. Include the full docstring and all randomization-related parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2fb59eb-da6f-4d82-a135-99c233eec199",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FoW4eXF2G8UDJBLMJW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ff26e6d-744d-410a-9146-f84207ace560",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP6stPQt8vGELWxtjKhmDR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2197,
      "cache_creation_input_tokens": 596,
      "cache_read_input_tokens": 30019,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 596
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2197,
          "output_tokens": 154,
          "cache_read_input_tokens": 30019,
          "cache_creation_input_tokens": 596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 596,
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

_source line 48 · 2026-05-15T11:13:38.303Z_

<details><summary>↩ Tool result · `toolu_01H5fcnANzeubgqZen5nvqc7`</summary>

```text
# DomainRandomizationWrapper Class Definition

## Class Overview
The `DomainRandomizationWrapper` is designed to "allow for domain randomization mid-simulation" in robosuite environments.

## Constructor Parameters

**Core Parameters:**
- `env` (MujocoEnv): The environment being wrapped
- `seed` (int, optional): Used to create isolated `np.random.RandomState` instance

**Randomization Toggles:**
- `randomize_color` (bool, default=True): Controls geom and texture color randomization
- `randomize_camera` (bool, default=True): Controls camera location and parameter changes
- `randomize_lighting` (bool, default=True): Controls light location and property modifications
- `randomize_dynamics` (bool, default=True): Controls physics parameter randomization

**Configuration Dictionaries:**
- `color_randomization_args`: Includes geom names, local color sampling, material properties, texture variations, and skybox settings
- `camera_randomization_args`: Includes camera names, position/rotation/fovy randomization with perturbation sizes
- `lighting_randomization_args`: Includes light names and randomization flags for position, direction, specular, ambient, and diffuse properties
- `dynamics_randomization_args`: Includes body, geom, and joint parameters with density, viscosity, friction, and inertia controls

**Execution Parameters:**
- `randomize_on_reset` (bool, default=True): Applies randomization at episode reset
- `randomize_every_n_steps` (int, default=1): Sets randomization frequency during steps

## Key Methods
- `reset()`: Restores defaults, resets environment, saves parameters, applies randomization if enabled
- `step()`: Calls step randomization before delegating to superclass
- `randomize_domain()`: Executes randomization across all active modders
- `save_default_domain()`: Preserves current simulation parameters
- `restore_default_domain()`: Reverts to saved parameters
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ff26e6d-744d-410a-9146-f84207ace560",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "6094e08e-0a36-4a5e-a28e-7db37e7c55ad",
  "sourceToolAssistantUUID": "9ff26e6d-744d-410a-9146-f84207ace560",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-15T11:13:40.838Z_

Now I have all the information needed. Let me compile the comprehensive report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6094e08e-0a36-4a5e-a28e-7db37e7c55ad",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FpG7n75XQBdWFWRMrF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c513d85-73b4-4ae8-a672-2819bba16b86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQBadPYzkj6nJYWNELNhC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 30615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2828,
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

_source line 50 · 2026-05-15T11:13:41.632Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0173q63qhK6XB8QeKNj4hQFQ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c513d85-73b4-4ae8-a672-2819bba16b86",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FpG7n75XQBdWFWRMrF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "289de43c-d20a-474d-bf1f-78bb0b40d5c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQBadPYzkj6nJYWNELNhC4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 30615,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 30615,
          "cache_creation_input_tokens": 2828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2828,
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

_source line 51 · 2026-05-15T11:13:41.634Z_

<details><summary>↩ Tool result · `toolu_0173q63qhK6XB8QeKNj4hQFQ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "289de43c-d20a-474d-bf1f-78bb0b40d5c7",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "aada8a30ff0506204",
  "type": "user",
  "uuid": "ab4add5b-f3a1-450c-ad6e-b1158428733b",
  "sourceToolAssistantUUID": "289de43c-d20a-474d-bf1f-78bb0b40d5c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-15T11:14:56.783Z_



Here is the structured research report.

---

## 1. What LIBERO-Plus Is

LIBERO-Plus is a robustness evaluation benchmark that extends the original LIBERO robot manipulation benchmark. It was published as "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" (arXiv:2510.13626, accepted at CVPR 2026).

**What it adds on top of LIBERO:**
- **10,030 task variants** generated by applying systematic perturbations to original LIBERO tasks
- **7 perturbation dimensions** with **21 sub-dimensions**
- **5 difficulty levels** (L1-L5) stratified by multi-model consensus (how many of 4 reference models solve the task)
- **20,000+ training trajectories** collected under varied conditions (stored in RLDS format)
- Drop-in replacement for vanilla LIBERO — same Python interface, same camera names, same observation/action format

## 2. Source

- **Paper:** [arXiv:2510.13626](https://arxiv.org/abs/2510.13626)
- **GitHub:** [github.com/sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)
- **Project page:** [sylvestf.github.io/LIBERO-plus](https://sylvestf.github.io/LIBERO-plus/)
- **Assets (HuggingFace):** [Sylvest/LIBERO-plus](https://huggingface.co/datasets/Sylvest/LIBERO-plus)
- **Training dataset (RLDS):** [Sylvest/libero_plus_rlds](https://huggingface.co/datasets/Sylvest/libero_plus_rlds)
- **LeRobot-format dataset:** [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

## 3. The 7 Perturbation Dimensions (Exact Definitions)

Note: The user asked about 4 dimensions. LIBERO-Plus actually defines **7**, not 4.

### 3.1 Objects Layout (O1, O2)
- **O1 — Confounding objects:** Adds n additional unseen distractor objects into the scene from a pool of 416 objects, implemented by modifying BDDL task description files.
- **O2 — Target displacement:** Applies random perturbations to the target object's initial position (x, y, z) and orientation while preserving semantic relationships.

### 3.2 Camera Viewpoints (C1, C2, C3)
- **C1 — Distance scaling:** Scales camera distance from 1.01x to 2.00x the original value along the optical axis.
- **C2 — Spherical position:** Changes azimuth (delta-theta) and elevation (delta-phi) within 15 to 75 degree cones.
- **C3 — Orientation perturbation:** Perturbs yaw, pitch, roll within 2 to 10 degrees.

Implementation: Modifies the `Problem` class interface; parameters derived from task filenames. Targets the third-person camera primarily (not wrist camera).

### 3.3 Robot Initial States
- Applies random perturbations to the robot arm's initial joint positions with magnitudes 0.1 to 0.5.
- Implementation: Modifies the `Problem` class interface.

### 3.4 Language Instructions (R1, R2, R3)
- **R1 — Distraction rewrites:** Adds task-irrelevant contextual information.
- **R2 — Commonsense substitution:** Replaces object descriptions with commonsense-based alternatives.
- **R3 — Reasoning complexity:** Alters reasoning complexity for multi-step tasks.
- Implementation: LLM-based instruction rewriting.

### 3.5 Light Conditions (L1, L2, L3, L4)
- **L1 — Diffuse color:** RGB channel adjustment of diffuse lighting.
- **L2 — Direction:** Parallel light source direction changes.
- **L3 — Specular intensity:** Specular highlight intensity (reflective surfaces).
- **L4 — Shadow casting:** Boolean shadow on/off control.
- Implementation: Modifies MuJoCo scene XML definition files, registers new scene classes.

### 3.6 Background Textures (B1, B2)
- **B1 — Scene texture:** Changes the environment scene texture using 950 curated textures via XML scene files.
- **B2 — Surface texture:** Randomly alters working surface texture (tabletop, floor).
- Implementation: Modifies XML scene definition files with new texture assets.

### 3.7 Sensor Noise (N1-N5)
Applied as image-space post-processing (not physics-level):
- **N1 — Motion blur:** Kernel radius r=5-35, Gaussian sigma=2-20, angle theta in U(-45, 45) degrees.
- **N2 — Gaussian blur:** Sigma from 1 to 10.
- **N3 — Zoom blur:** Scaling factors [s_min, s_max, step] from [1, 1.11, 0.01] to [1, 1.56, 0.03].
- **N4 — Fog:** Density alpha=0.5-5.0, decay rate beta=1.3-3.0.
- **N5 — Glass blur:** Sigma=0.5-2.5, pixel displacement delta=1-5, iterations=1-3.

### Difficulty Levels (L1-L5)
Stratified by how many of 4 reference models (OpenVLA-OFT, pi0, pi0-fast, UniVLA) solve each task:
- L1: All 4 solve it. L2: 3 solve. L3: 2 solve. L4: 1 solves. L5: None solve.

## 4. Installation and Running

### Installation

```bash
# System dependencies
sudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev

# Clone and install
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus
pip install -e .
pip install -r extra_requirements.txt

# If vanilla LIBERO was installed, uninstall first
pip uninstall -y hf-libero

# Set rendering backend
export MUJOCO_GL=egl
```

### Download assets

Download `assets.zip` from [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) and extract to `LIBERO-plus/libero/libero/assets/`.

Expected structure:
```
libero/libero/assets/
├── articulated_objects/
├── new_objects/
├── scenes/
├── stable_hope_objects/
├── stable_scanned_objects/
├── textures/
├── turbosquid_objects/
├── serving_region.xml
├── wall_frames.stl
└── wall.xml
```

### Configuration

Verify config at `/root/.libero/config.yaml`. Key change for evaluation: set `num_trials_per_task: 1` (instead of 50).

Task-to-perturbation-category mappings: `.libero/libero/benchmark/task_classification.json`.

### Evaluation via LeRobot

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

Observations: `observation.images.image` (agentview), `observation.images.image2` (wrist cam), `observation.state` (8-dim proprioception). Actions: `Box(-1, 1, shape=(7,))` — 6D EEF delta + 1D gripper. Control modes: `relative` (default) or `absolute`.

## 5. Integration with Standard LIBERO Evaluation

LIBERO-Plus is a **drop-in replacement** for vanilla LIBERO:
- Installs under the same `libero` Python package name (replaces it)
- Same `LiberoEnv` gym interface
- Same camera names (`agentview_image`, `robot0_eye_in_hand_image`)
- Same observation/action format
- Same task suite names (`libero_spatial`, `libero_object`, `libero_goal`, `libero_10`, `libero_90`)
- You can swap by doing `pip install -e .` in the LIBERO-plus repo without modifying evaluation code

**You cannot have both vanilla LIBERO and LIBERO-Plus installed simultaneously.** Switching back requires uninstalling the fork and reinstalling vanilla LIBERO.

## 6. LIBERO's Built-in Randomization (via robosuite)

LIBERO is built on **robosuite** (which uses MuJoCo). Robosuite **does** have built-in domain randomization via `DomainRandomizationWrapper` and three visual Modder classes. These are available to any robosuite-based environment, including LIBERO.

### DomainRandomizationWrapper

```python
from robosuite.wrappers import DomainRandomizationWrapper

env = DomainRandomizationWrapper(
    env=base_env,
    seed=42,
    randomize_color=True,        # Geom/texture color randomization
    randomize_camera=True,       # Camera position/orientation/FOV
    randomize_lighting=True,     # Light position/direction/color
    randomize_dynamics=True,     # Physics parameters
    randomize_on_reset=True,     # Randomize at episode reset
    randomize_every_n_steps=1,   # Frequency during rollout
    # Optional: pass detailed config dicts
    color_randomization_args={...},
    camera_randomization_args={...},
    lighting_randomization_args={...},
    dynamics_randomization_args={...},
)
```

### CameraModder (built-in)
- **Position** perturbation: default size 0.01
- **Rotation** perturbation (quaternion): default size 0.087 (~5 degrees)
- **FOV** perturbation: default size 5.0 degrees

### LightingModder (built-in)
- **Position** perturbation: default size 0.1
- **Direction** perturbation: default size 0.35
- **Specular** perturbation: default size 0.1
- **Ambient** perturbation: default size 0.1
- **Diffuse** perturbation: default size 0.1
- **Active** status: on/off toggle

### TextureModder (built-in)
- RGB color randomization (local interpolation 0.1)
- Texture patterns: RGB, checker, noise, gradient
- Material properties: reflectance, shininess, specular (local interpolation 0.2)
- Skybox randomization (optional)
- Note: For full effect, set all material RGBA to [1,1,1,1]

### Demo script
`robosuite/demos/demo_domain_randomization.py` showcases all modders.

## 7. Can LIBERO-Plus Perturbations Be Reused for Training-Time Augmentation?

**Yes, and the paper explicitly does this.** LIBERO-Plus provides both evaluation tasks AND a training dataset:

### What's already provided
- **22,400 training trajectories** (20,000+ after filtering) generated under varied perturbation conditions
- Breakdown: 2,400 with object layout variations + 4,000 each for light/camera/background/language/noise dimensions
- Stored in RLDS format, also available in LeRobot format at `lerobot/libero_plus`
- The paper shows that training with this diverse data ("mix-SFT") improves robustness — the OpenVLA-OFT+ model trained on this data achieves 79.6% average vs. much lower for vanilla-trained models

### Two paths for training-time augmentation

**Path A — Use LIBERO-Plus training data directly:**
```bash
lerobot-train \
    --policy.type=smolvla \
    --dataset.repo_id=lerobot/libero_plus \
    --env.type=libero_plus \
    ...
```

**Path B — Use robosuite's built-in DomainRandomizationWrapper for online augmentation during training:**
This covers camera jitter, lighting changes, texture/color randomization natively. Wrap the LIBERO environment:
```python
from robosuite.wrappers import DomainRandomizationWrapper
env = DomainRandomizationWrapper(env=libero_env, randomize_camera=True, randomize_lighting=True, randomize_color=True)
```

**Path C — Reuse LIBERO-Plus perturbation code for custom augmentation:**
- Lighting/texture perturbations: Modify scene XML files + register new scenes (same approach as LIBERO-Plus)
- Camera perturbations: Modify the `Problem` class interface
- Sensor noise (blur, fog, etc.): Image-space post-processing — trivially reusable as training-time augmentation since it's just image transforms applied after rendering

### Key distinction
- Robosuite's built-in randomization (Path B) is **online** — applies random perturbations every N steps during simulation. Good for training-time augmentation but less controllable.
- LIBERO-Plus perturbations (Path C) are **structured** with specific parameter ranges per sub-dimension and difficulty stratification. More suitable for systematic robustness training.
- Sensor noise (N1-N5) is pure image-space post-processing and can be applied as standard data augmentation on any stored trajectory without re-rendering.

### Paper's finding on augmentation effectiveness
Training strategies emphasizing diversity consistently yield more robust models. Models with wrist camera input show superior generalization. The paper demonstrates that combining perturbation-augmented training data with mix-SFT is the most effective approach.

---

Sources:
- [LIBERO-Plus paper (arXiv)](https://arxiv.org/abs/2510.13626)
- [LIBERO-Plus GitHub](https://github.com/sylvestf/LIBERO-plus)
- [LIBERO-Plus project page](https://sylvestf.github.io/LIBERO-plus/)
- [LIBERO-Plus HuggingFace dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus)
- [LIBERO-Plus LeRobot docs](https://huggingface.co/docs/lerobot/main/libero_plus)
- [robosuite Sim2Real / Domain Randomization](https://robosuite.ai/docs/algorithms/sim2real.html)
- [robosuite mjmod.py (Modder classes)](https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py)
- [Original LIBERO repo](https://github.com/Lifelong-Robot-Learning/LIBERO)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab4add5b-f3a1-450c-ad6e-b1158428733b",
  "isSidechain": true,
  "agentId": "aada8a30ff0506204",
  "requestId": "req_011Cb4FpWbRhBk53QgXHR1vc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa9b0c0a-a99a-419a-900f-f8be8844ee2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161wo5HoMeigrAV9CGC6eD5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 33443,
      "output_tokens": 3772,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3772,
          "cache_read_input_tokens": 33443,
          "cache_creation_input_tokens": 379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 379,
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
