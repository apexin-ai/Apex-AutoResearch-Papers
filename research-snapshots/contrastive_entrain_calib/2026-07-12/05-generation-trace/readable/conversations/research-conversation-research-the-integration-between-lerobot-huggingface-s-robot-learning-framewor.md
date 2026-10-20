# Research conversation: Research the integration between LeRobot (HuggingFace's robot learning framework) and the LIBERO benchmark. I need to fi

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a1a91bef0d6739352.jsonl`
- **Structured JSON:** [`57d9510aefff88feb0bb.json`](../../sessions/57/57d9510aefff88feb0bb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-15T11:11:58.759Z_

Research the integration between LeRobot (HuggingFace's robot learning framework) and the LIBERO benchmark.

I need to find:
1. Does LeRobot natively support LIBERO datasets?
2. If yes, what are the dataset names on HuggingFace Hub?
3. What is the data conversion pipeline from LIBERO's native HDF5 format to LeRobot format?
4. Any conversion scripts or utilities available

Use WebSearch to search for:
- "LeRobot LIBERO" 
- "lerobot libero dataset"
- HuggingFace Hub LIBERO datasets
- "lerobot convert libero"

Then use WebFetch to check:
- The LeRobot GitHub repo for LIBERO-related code
- HuggingFace Hub for LIBERO datasets in LeRobot format
- Any conversion scripts or documentation

Report everything in structured format with exact dataset names, commands, and code paths.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "8baa9b97-d89a-4a32-a36b-6d5f31ef8555",
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

_source line 2 · 2026-05-15T11:11:58.766Z_

```json
{
  "parentUuid": "8baa9b97-d89a-4a32-a36b-6d5f31ef8555",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
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
  "uuid": "aba7bff7-14f1-4aa1-adef-44a974724519",
  "timestamp": "2026-05-15T11:11:58.766Z",
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

_source line 3 · 2026-05-15T11:12:01.591Z_



I'll research the LeRobot-LIBERO integration systematically. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aba7bff7-14f1-4aa1-adef-44a974724519",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fgva6HYqkfrwUNz17U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "554bd824-d504-477e-95cc-9c0cc8984a6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BF1e1vNWu6V2MBHTN3X6P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6051,
      "cache_read_input_tokens": 8256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6051,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-15T11:12:01.751Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01S7kCrojDyrKsWoT2q9hKUA`</summary>

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
  "parentUuid": "554bd824-d504-477e-95cc-9c0cc8984a6e",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fgva6HYqkfrwUNz17U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d1bae40-fb64-4e92-94db-b8bb43d56445",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BF1e1vNWu6V2MBHTN3X6P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6051,
      "cache_read_input_tokens": 8256,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6051
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 8256,
          "cache_creation_input_tokens": 6051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6051,
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

_source line 5 · 2026-05-15T11:12:01.754Z_

<details><summary>↩ Tool result · `toolu_01S7kCrojDyrKsWoT2q9hKUA`</summary>

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
  "parentUuid": "9d1bae40-fb64-4e92-94db-b8bb43d56445",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "f48ad771-ecd0-477d-b627-a5f93c53641a",
  "sourceToolAssistantUUID": "9d1bae40-fb64-4e92-94db-b8bb43d56445",
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

_source line 6 · 2026-05-15T11:12:03.992Z_



Now let me run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f48ad771-ecd0-477d-b627-a5f93c53641a",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fh9dQYH8wbAjnugf33",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84e0b984-3588-4a26-ae15-061a414474ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLtz1ND2hrDD45QCGY59m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 14307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 7 · 2026-05-15T11:12:04.587Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TsJz2ccCooccZUGmvNiuQL`</summary>

```json
{
  "query": "LeRobot LIBERO dataset integration HuggingFace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84e0b984-3588-4a26-ae15-061a414474ab",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fh9dQYH8wbAjnugf33",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a64c383-5c03-4ddb-a10a-5f9e40bfb190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLtz1ND2hrDD45QCGY59m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 14307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 8 · 2026-05-15T11:12:05.019Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018nr9gPtTUj5f9mGc3FUhLf`</summary>

```json
{
  "query": "lerobot convert libero HDF5 dataset script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a64c383-5c03-4ddb-a10a-5f9e40bfb190",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fh9dQYH8wbAjnugf33",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa70719f-368b-4cdf-8e0e-622b2adef4b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLtz1ND2hrDD45QCGY59m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 14307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 9 · 2026-05-15T11:12:05.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BsBVPQpLgjmLPH42upLSR9`</summary>

```json
{
  "query": "huggingface hub lerobot libero dataset names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa70719f-368b-4cdf-8e0e-622b2adef4b5",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fh9dQYH8wbAjnugf33",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f1065b6-14d0-4633-b7bc-95612b2a0bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLtz1ND2hrDD45QCGY59m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 14307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 10 · 2026-05-15T11:12:05.967Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y4bSZpfheLgMAxaQoBJPgR`</summary>

```json
{
  "query": "github huggingface lerobot libero conversion pipeline 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f1065b6-14d0-4633-b7bc-95612b2a0bba",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fh9dQYH8wbAjnugf33",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a06954c5-7ea2-4471-bd1e-d577a41df88f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLtz1ND2hrDD45QCGY59m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 14307,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1962
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 221,
          "cache_read_input_tokens": 14307,
          "cache_creation_input_tokens": 1962,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1962,
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

_source line 11 · 2026-05-15T11:12:10.560Z_

<details><summary>↩ Tool result · `toolu_01TsJz2ccCooccZUGmvNiuQL`</summary>

```text
Web search results for query: "LeRobot LIBERO dataset integration HuggingFace"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"LeRobotDataset v3.0 · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"LeRobot v0.4.0: Supercharging OSS Robot Learning","url":"https://huggingface.co/blog/lerobot-release-v040"}]

Based on the search results, here's what I found about LeRobot LIBERO dataset integration with HuggingFace:

## Overview

The LIBERO benchmark repository is now maintained by the Hugging Face team, with modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments.

## Dataset Integration

LeRobot supports standard benchmarks like LIBERO and more, and LeRobot now officially supports LIBERO, one of the largest open benchmarks for Vision-Language-Action (VLA) policies, boasting over 130 tasks.

## Available Datasets

A preprocessed LIBERO dataset is provided that is fully compatible with the current LeRobot codebase and requires no additional manipulation, available at HuggingFaceVLA/libero. Additionally, datasets are chosen from libero_spatial, libero_object, libero_100, and libero_goal.

## Training and Evaluation

LeRobot uses a LeRobotDataset format with synchronized MP4 videos (or images) for vision and Parquet files for state/action data. The integration allows seamless training and evaluation through unified command-line interfaces for policy training and benchmarking on LIBERO tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a64c383-5c03-4ddb-a10a-5f9e40bfb190",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "1dccf7a4-d1c5-4778-bfc1-bccc2a14d9e2",
  "sourceToolAssistantUUID": "8a64c383-5c03-4ddb-a10a-5f9e40bfb190",
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

_source line 12 · 2026-05-15T11:12:10.928Z_

<details><summary>↩ Tool result · `toolu_01BsBVPQpLgjmLPH42upLSR9`</summary>

```text
Web search results for query: "huggingface hub lerobot libero dataset names"

Links: [{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"LeRobotDataset v3.0 · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"lerobot/libero_10_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_10_image"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"}]

Based on the web search results, here are the LIBERO dataset names available on the Hugging Face Hub for LeRobot:

## LIBERO Task Suites

LIBERO provides 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## Raw Dataset Names

The raw dataset names include "libero_10_no_noops", "libero_goal_no_noops", "libero_object_no_noops", and "libero_spatial_no_noops".

## LeRobot Processed Datasets

Several preprocessed datasets are available on the Hugging Face Hub:

1. "HuggingFaceVLA/libero" - a preprocessed LIBERO dataset fully compatible with the current LeRobot codebase
2. **lerobot/libero** - contains 40 tasks with 1,693 episodes
3. **lerobot/libero_10_image** - contains 10 tasks with 379 episodes
4. **lerobot/libero_object_image** - contains 10 tasks with 454 episodes

These datasets are designed for training and evaluating robot policies using LeRobot's framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f1065b6-14d0-4633-b7bc-95612b2a0bba",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "bfbb85f0-8de2-4449-8dc7-ddfd6418e8e6",
  "sourceToolAssistantUUID": "2f1065b6-14d0-4633-b7bc-95612b2a0bba",
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

_source line 13 · 2026-05-15T11:12:11.408Z_

<details><summary>↩ Tool result · `toolu_018nr9gPtTUj5f9mGc3FUhLf`</summary>

```text
Web search results for query: "lerobot convert libero HDF5 dataset script"

Links: [{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"IPEC-COMMUNITY/libero_90_no_noops_lerobot · Dataset converted ideas","url":"https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2"},{"title":"GitHub - anarnuri/hdf5_to_lerobot_converter · GitHub","url":"https://github.com/anarnuri/hdf5_to_lerobot_converter"},{"title":"GitHub - muhamuttaqien/ALOHADataConverter: This repository contains scripts for converting an ALOHA HDF5 dataset into the Lerobot, RMB and GR00T formats.","url":"https://github.com/muhamuttaqien/ALOHADataConverter"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"Policy Post-training — isaaclab_arena 0.2","url":"https://isaac-sim.github.io/IsaacLab-Arena/main/pages/example_workflows/static_manipulation/step_4_policy_training.html"},{"title":"Question: Is There an Official or Recommended Way to Convert Isaac Lab HDF5 Data to LeRobot Schema? · Issue #2739 · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/issues/2739"},{"title":"How to convert my own dataset to LerobotDataset format? · Issue #846 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/846"},{"title":"[Question] HDF5 to LeRobot convert pipeline in new release · Issue #2941 · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/issues/2941"},{"title":"openvla/experiments/robot/libero/regenerate_libero_dataset.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py"}]

Based on the search results, I found several relevant resources for converting LIBERO HDF5 datasets to LeRobot format:

## Primary LeRobot Conversion Script

There is a minimal example script for converting a dataset to LeRobot format in the Physical Intelligence OpenPi repository. You can run it with: `uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/your/data --push_to_hub`

To run the script, you need to install tensorflow_datasets with `uv pip install tensorflow tensorflow_datasets`, and you can download the raw Libero datasets from https://huggingface.co/datasets/openvla/modified_libero_rlds.

## Alternative Tools

The "any4lerobot" tool can be used to convert LIBERO hdf5 data to lerobot format, though it showed bugs sometimes related to videos decode.

There's also a general HDF5 to LeRobot converter that converts robotics datasets stored in custom HDF5 formats into the standardized LeRobot structure available at the GitHub repository `anarnuri/hdf5_to_lerobot_converter`.

## Processing Time

Running the conversion script will take approximately 30 minutes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa70719f-368b-4cdf-8e0e-622b2adef4b5",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "5f2e627d-4a87-40e5-abd7-c9cf80a1c306",
  "sourceToolAssistantUUID": "aa70719f-368b-4cdf-8e0e-622b2adef4b5",
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

_source line 14 · 2026-05-15T11:12:15.649Z_

<details><summary>↩ Tool result · `toolu_01Y4bSZpfheLgMAxaQoBJPgR`</summary>

```text
Web search results for query: "github huggingface lerobot libero conversion pipeline 2025 2026"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - OpenDriveLab/AgiBot-World: [IROS 2025 Best Paper Award Finalist & IEEE TRO 2026] The Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems · GitHub","url":"https://github.com/OpenDriveLab/AgiBot-World"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"Releases · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/releases"},{"title":"GitHub - starVLA/starVLA: StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing · GitHub","url":"https://github.com/starVLA/starVLA"},{"title":"lerobot/docs/source/pi05.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/pi05.mdx"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"},{"title":"LeRobot · Hugging Face","url":"https://huggingface.co/docs/lerobot/index"}]

Based on the search results, here's what I found about the LeRobot LIBERO conversion pipeline:

## Overview

LIBERO provides a procedural generation pipeline that could in principle generate an infinite number of manipulation tasks, with 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## LeRobot Integration

LeRobot ported LIBERO into its framework and used it mainly to evaluate SmolVLA, its lightweight Vision-Language-Action model. LeRobot supports standard benchmarks like LIBERO, MetaWorld and more to come.

## Data Conversion Pipeline

The pipeline involves downloading the raw LIBERO dataset from OpenVLA, then running a script to convert it into LeRobot dataset format. There's a referenced script `convert_libero_data_to_lerobot.py` that handles this conversion.

## Dataset Preprocessing

A preprocessed LIBERO dataset is provided that is fully compatible with the current LeRobot codebase and requires no additional manipulation.

## Key Resources

- The datasets hosted on HuggingFace are available
- The official GitHub repository: [huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero) - described as "A fork of the official LIBERO benchmark, extended for Hugging Face's LeRobot integration"


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a06954c5-7ea2-4471-bd1e-d577a41df88f",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "6c017f0c-66c5-4a71-b8e9-09d6b163d78d",
  "sourceToolAssistantUUID": "a06954c5-7ea2-4471-bd1e-d577a41df88f",
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

_source line 15 · 2026-05-15T11:12:18.417Z_

Good initial results. Now let me fetch detailed information from the key pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c017f0c-66c5-4a71-b8e9-09d6b163d78d",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FiAmeNDNTCLKH1Pbya",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3465703-3ff1-4763-8dec-d919245c43ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcfN1RbSebvjnN3rA6VGUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3772,
      "cache_read_input_tokens": 16269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3772,
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

_source line 16 · 2026-05-15T11:12:19.936Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YFwoauSxTJ6sK13QtqBFCR`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/libero",
  "prompt": "Extract ALL information about LIBERO integration: dataset names, conversion commands, training commands, evaluation commands, task suite names, dataset structure, any code examples. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3465703-3ff1-4763-8dec-d919245c43ab",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FiAmeNDNTCLKH1Pbya",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab70e452-7d67-44e7-bd53-c8dbb345f840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcfN1RbSebvjnN3rA6VGUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3772,
      "cache_read_input_tokens": 16269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3772,
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

### Tool result

_source line 17 · 2026-05-15T11:12:20.434Z_

<details><summary>↩ Tool result · `toolu_01YFwoauSxTJ6sK13QtqBFCR`</summary>

````text
# LIBERO

LIBERO is a benchmark designed to study **lifelong robot learning** — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once. It provides a set of standardized manipulation tasks that focus on **knowledge transfer**: how well a robot can apply what it has already learned to new situations. By evaluating on LIBERO, different algorithms can be compared fairly and researchers can build on each other's work.

- Paper: [Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)
- GitHub: [Lifelong-Robot-Learning/LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
- Project website: [libero-project.github.io](https://libero-project.github.io)

![An overview of the LIBERO benchmark](https://libero-project.github.io/assets/img/libero/fig1.png)

## Available tasks

LIBERO includes **five task suites** covering **130 tasks**, ranging from simple object manipulations to complex multi-step scenarios:

| Suite          | CLI name         | Tasks | Description                                        |
| -------------- | ---------------- | ----- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | Long-horizon tasks from the LIBERO-100 collection  |

## Installation

After following the LeRobot installation instructions:

```bash
pip install -e ".[libero]"
```

LIBERO requires Linux (`sys_platform == 'linux'`). LeRobot uses MuJoCo for simulation — set the rendering backend before training or evaluation:

```bash
export MUJOCO_GL=egl  # for headless servers (HPC, cloud)
```

## Evaluation

### Default evaluation (recommended)

Evaluate across the four standard suites (10 episodes per task):

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

### Single-suite evaluation

Evaluate on one LIBERO suite:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_object \
  --eval.batch_size=2 \
  --eval.n_episodes=3
```

- `--env.task` picks the suite (`libero_object`, `libero_spatial`, etc.).
- `--env.task_ids` restricts to specific task indices (`[0]`, `[1,2,3]`, etc.). Omit to run all tasks in the suite.
- `--eval.batch_size` controls how many environments run in parallel.
- `--eval.n_episodes` sets how many episodes to run per task.

### Multi-suite evaluation

Benchmark a policy across multiple suites at once by passing a comma-separated list:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_object,libero_spatial \
  --eval.batch_size=1 \
  --eval.n_episodes=2
```

### Control mode

LIBERO supports two control modes — `relative` (default) and `absolute`. Different VLA checkpoints are trained with different action parameterizations, so make sure the mode matches your policy:

```bash
--env.control_mode=relative   # or "absolute"
```

### Policy inputs and outputs

**Observations:**

- `observation.state` — 8-dim proprioceptive features (eef position, axis-angle orientation, gripper qpos)
- `observation.images.image` — main camera view (`agentview_image`), HWC uint8
- `observation.images.image2` — wrist camera view (`robot0_eye_in_hand_image`), HWC uint8

  LeRobot enforces the `.images.*` prefix for visual features. Ensure your
  policy config `input_features` use the same naming keys, and that your dataset
  metadata keys follow this convention. If your data contains different keys,
  you must rename the observations to match what the policy expects, since
  naming keys are encoded inside the normalization statistics layer.

**Actions:**

- Continuous control in `Box(-1, 1, shape=(7,))` — 6D end-effector delta + 1D gripper

### Recommended evaluation episodes

For reproducible benchmarking, use **10 episodes per task** across all four standard suites (Spatial, Object, Goal, Long). This gives 400 total episodes and matches the protocol used for published results.

## Training

### Dataset

We provide a preprocessed LIBERO dataset fully compatible with LeRobot:

- [HuggingFaceVLA/libero](https://huggingface.co/datasets/HuggingFaceVLA/libero)

For reference, the original dataset published by Physical Intelligence:

- [physical-intelligence/libero](https://huggingface.co/datasets/physical-intelligence/libero)

### Example training command

```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.repo_id=${HF_USER}/libero-test \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task=libero_10 \
  --output_dir=./outputs/ \
  --steps=100000 \
  --batch_size=4 \
  --eval.batch_size=1 \
  --eval.n_episodes=1 \
  --eval_freq=1000
```

## Reproducing published results

We reproduce the results of Pi0.5 on the LIBERO benchmark. We take the Physical Intelligence LIBERO base model (`pi05_libero`) and finetune for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the [HuggingFace LIBERO dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero).

The finetuned model: [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned)

### Evaluation command

```bash
lerobot-eval \
  --output_dir=./eval_logs/ \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --policy.path=pi05_libero_finetuned \
  --policy.n_action_steps=10 \
  --env.max_parallel_tasks=1
```

We set `n_action_steps=10`, matching the original OpenPI implementation.

### Results

| Model               | LIBERO Spatial | LIBERO Object | LIBERO Goal | LIBERO 10 | Average  |
| ------------------- | -------------- | ------------- | ----------- | --------- | -------- |
| **Pi0.5 (LeRobot)** | 97.0           | 99.0          | 98.0        | 96.0      | **97.5** |

These results are consistent with the [original results](https://github.com/Physical-Intelligence/openpi/tree/main/examples/libero#results) reported by Physical Intelligence:

| Model              | LIBERO Spatial | LIBERO Object | LIBERO Goal | LIBERO 10 | Average   |
| ------------------ | -------------- | ------------- | ----------- | --------- | --------- |
| **Pi0.5 (OpenPI)** | 98.8           | 98.2          | 98.0        | 92.4      | **96.85** |


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab70e452-7d67-44e7-bd53-c8dbb345f840",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "7506bc69-1c71-4d44-a370-6948ac2c9626",
  "sourceToolAssistantUUID": "ab70e452-7d67-44e7-bd53-c8dbb345f840",
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

### Tool call

_source line 18 · 2026-05-15T11:12:21.333Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RRxe6Mx6qGds5WgQ7Jrzp3`</summary>

```json
{
  "url": "https://huggingface.co/datasets/lerobot/libero",
  "prompt": "Extract the full dataset card: dataset name, size, number of episodes, number of tasks, data format, column names, how to load it, any usage examples. Include all metadata."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7506bc69-1c71-4d44-a370-6948ac2c9626",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FiAmeNDNTCLKH1Pbya",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12de8fef-e160-4c06-b2d8-916ede2bfd18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcfN1RbSebvjnN3rA6VGUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3772,
      "cache_read_input_tokens": 16269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3772,
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

_source line 19 · 2026-05-15T11:12:23.382Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XkrtTrt73iJhaJanKR9dzU`</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py",
  "prompt": "Extract the FULL conversion script code. Show all imports, functions, the main conversion logic, command-line arguments, and how it maps LIBERO HDF5 fields to LeRobot format. Include every detail of the data mapping."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12de8fef-e160-4c06-b2d8-916ede2bfd18",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FiAmeNDNTCLKH1Pbya",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4733bdee-7b38-4e53-a61a-f160210f368a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcfN1RbSebvjnN3rA6VGUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3772,
      "cache_read_input_tokens": 16269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3772,
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

_source line 20 · 2026-05-15T11:12:24.206Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BqhEA6bS8fXEvnN2egxkJH`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot-libero",
  "prompt": "Extract all information about this repository: what it does, how it integrates with LeRobot, installation instructions, usage, any conversion scripts or utilities. Include all README content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4733bdee-7b38-4e53-a61a-f160210f368a",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FiAmeNDNTCLKH1Pbya",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f222f75-53f5-4545-aa1b-b2604f9ba804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcfN1RbSebvjnN3rA6VGUj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3772,
      "cache_read_input_tokens": 16269,
      "output_tokens": 484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3772
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 484,
          "cache_read_input_tokens": 16269,
          "cache_creation_input_tokens": 3772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3772,
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

_source line 21 · 2026-05-15T11:12:29.466Z_

<details><summary>↩ Tool result · `toolu_01RRxe6Mx6qGds5WgQ7Jrzp3`</summary>

````text
# LeRobot LIBERO Dataset Card

## Dataset Overview
**Name:** `lerobot/libero`  
**Task:** Robotics  
**License:** Apache 2.0  
**Created by:** LeRobot

## Dataset Statistics
- **Total Episodes:** 1,693
- **Total Frames:** 273,465
- **Total Tasks:** 40
- **Rows:** 273,465 (273K)
- **Total Size:** 1.94 GB
- **Video Files Size:** ~500 MB
- **Data Files Size:** ~100 MB
- **FPS:** 10.0

## Data Format & Structure
- **Format:** Parquet (auto-converted)
- **Robot Type:** Panda
- **Chunks Size:** 1,000
- **Split:** Train (0:1693)

## Column Names & Features

### Observation Features
- `observation.images.image` - Video (256×256×3 RGB, AV1 codec, yuv420p)
- `observation.images.image2` - Video (256×256×3 RGB, AV1 codec, yuv420p)
- `observation.state` - Float32, shape [8] (robot state vector)

### Action & Metadata
- `action` - Float32, shape [7] (action vector)
- `timestamp` - Float32
- `frame_index` - Int64
- `episode_index` - Int64
- `task_index` - Int64 (0-39)
- `index` - Int64 (row index)

## How to Load

### Using Hugging Face Datasets Library
```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("lerobot/libero")

# Access training split
train_split = dataset["train"]

# View sample
print(train_split[0])
```

### Using Polars/Dask
The dataset is compatible with Polars and Dask libraries for distributed processing.

## Data Studio Access
- **Viewer:** Available at [Data Studio](/datasets/lerobot/libero/viewer/)
- **Interactive exploration** of all 273K rows

## Modalities
- **Tabular** (state vectors, actions, metadata)
- **Time-series** (sequential frame data)
- **Video** (RGB camera streams)

## Usage Notes
- Data is organized in parquet chunks for efficient loading
- Videos stored separately from structured data
- Each row represents a single timestep with corresponding observations and actions
- Suitable for training imitation learning and robotic control models

## Related Models
11+ models trained on this dataset, including:
- `lerobot/smolvla_libero`
- `alexanta/pi0.5_libero`
- Various fine-tuned variants
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12de8fef-e160-4c06-b2d8-916ede2bfd18",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "da505ef0-5246-4d8c-aca6-9fd73c3e48cf",
  "sourceToolAssistantUUID": "12de8fef-e160-4c06-b2d8-916ede2bfd18",
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

_source line 22 · 2026-05-15T11:12:29.761Z_

<details><summary>↩ Tool result · `toolu_01XkrtTrt73iJhaJanKR9dzU`</summary>

````text
# LIBERO to LeRobot Conversion Script

## Overview
The script converts LIBERO dataset (stored in RLDS format via TensorFlow Datasets) to LeRobot format for robotics training.

## Full Code Structure

**Imports:**
```python
import shutil
from lerobot.common.datasets.lerobot_dataset import HF_LEROBOT_HOME
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
import tensorflow_datasets as tfds
import tyro
```

**Configuration:**
- `REPO_NAME`: "your_hf_username/libero" (output dataset identifier)
- `RAW_DATASET_NAMES`: Four LIBERO variants ("libero_10_no_noops", "libero_goal_no_noops", "libero_object_no_noops", "libero_spatial_no_noops")

## Data Mapping Details

The script maps LIBERO fields to LeRobot features as follows:

| LIBERO Field | LeRobot Feature | Type | Shape | Purpose |
|---|---|---|---|---|
| observation["image"] | image | image | (256, 256, 3) | Primary camera view |
| observation["wrist_image"] | wrist_image | image | (256, 256, 3) | Wrist camera view |
| observation["state"] | state | float32 | (8,) | Proprioceptive data |
| action | actions | float32 | (7,) | Robot joint commands |
| language_instruction | task | string | N/A | Task description |

## Main Conversion Logic

1. Cleans existing output directory
2. Creates LeRobot dataset with specified features and metadata (robot_type="panda", fps=10)
3. Iterates through four raw LIBERO datasets
4. For each episode and step, extracts observation and action data
5. Calls `dataset.add_frame()` with mapped fields
6. Saves completed episodes with `dataset.save_episode()`
7. Optionally pushes to Hugging Face Hub with tags and metadata

## Command-Line Interface

Uses `tyro.cli(main)` with arguments:
- `data_dir`: Path to LIBERO dataset directory (required)
- `push_to_hub`: Boolean flag for Hugging Face Hub upload (optional)

**Note:** Requires TensorFlow and tensorflow_datasets installation; processing takes ~30 minutes.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4733bdee-7b38-4e53-a61a-f160210f368a",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "76881ec9-473c-4c85-81e8-f6622bd9b992",
  "sourceToolAssistantUUID": "4733bdee-7b38-4e53-a61a-f160210f368a",
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

_source line 23 · 2026-05-15T11:12:32.818Z_

<details><summary>↩ Tool result · `toolu_01BqhEA6bS8fXEvnN2egxkJH`</summary>

```text
# LIBERO-LeRobot Repository Summary

## Overview
This is Hugging Face's fork of the official LIBERO benchmark, designed for studying knowledge transfer in multitask and lifelong robot learning. The repository extends the original LIBERO framework with "modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments."

## Core Purpose
LIBERO provides a benchmarking framework that includes:
- A procedural generation pipeline for manipulation tasks
- 130 tasks organized into four suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100
- Five research topics and three visuomotor policy architectures
- Three lifelong learning algorithms with baseline implementations

## Installation
The setup requires:
1. Creating a conda environment with Python 3.8.13
2. Cloning the repository
3. Installing dependencies via `pip install -r requirements.txt`
4. Installing PyTorch with CUDA 11.3 support
5. Installing the package in editable mode: `pip install -e .`

## Dataset Acquisition
Datasets can be downloaded via:
- `python benchmark_scripts/download_libero_datasets.py` (default storage)
- Alternative: `python benchmark_scripts/download_libero_datasets.py --use-huggingface` (from Hugging Face hub)
- Specific dataset selection available through the `--datasets` flag

## Usage Workflow

**Task Retrieval:** Users import from `libero.libero` to access benchmark dictionaries and instantiate task suites, then retrieve specific tasks with associated BDDL files and language descriptions.

**Training:** Lifelong learning experiments require selecting a benchmark, policy type (bc_rnn_policy, bc_transformer_policy, bc_vilt_policy), and algorithm (base, er, ewc, packnet, multitask), then executing the training script with specified parameters.

**Evaluation:** Separate evaluation script available for resource-constrained scenarios, accepting benchmark name, task ID, algorithm, policy type, seed, epoch, and CUDA device specifications.

## Key Features
- Sparse reward functions (agent receives +1 upon task completion)
- Fixed initial states for benchmarking consistency
- Support for 128x128 off-screen rendered observations
- Focus on lifelong imitation learning rather than pure RL

## Licensing
- Codebase: MIT License
- Datasets: Creative Commons Attribution 4.0 International (CC BY 4.0)

## Repository Statistics
- 18 stars, 17 forks, 1 open issue
- 58 commits on main branch
- Composed of 53.9% Jupyter Notebooks and 46.1% Python code
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f222f75-53f5-4545-aa1b-b2604f9ba804",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "181bbecf-91b6-4601-bf10-3deb75dcbe93",
  "sourceToolAssistantUUID": "0f222f75-53f5-4545-aa1b-b2604f9ba804",
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

_source line 24 · 2026-05-15T11:12:35.738Z_

Now let me get more specific dataset names and the LIBERO-plus documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "181bbecf-91b6-4601-bf10-3deb75dcbe93",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FjSLJNGfKiSRmvGRTg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82f12acf-6620-47ad-bb5f-2862454b1c99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ejiv15JiBk44Et2gVNZ5Vg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4594,
      "cache_read_input_tokens": 20041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4594,
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

_source line 25 · 2026-05-15T11:12:37.804Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012up7eAufC6DCPqD75Gt5GZ`</summary>

```json
{
  "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero",
  "prompt": "Extract the full dataset card: exact dataset name, size, number of episodes, task suites included, how to load, data format, any instructions on usage with LeRobot. Include all metadata and statistics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82f12acf-6620-47ad-bb5f-2862454b1c99",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FjSLJNGfKiSRmvGRTg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22105923-cdce-4222-8312-d0da1d398355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ejiv15JiBk44Et2gVNZ5Vg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4594,
      "cache_read_input_tokens": 20041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4594,
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

_source line 26 · 2026-05-15T11:12:39.256Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FZ3ftyF8G5PyBo2B5gzzTZ`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
  "prompt": "Extract ALL information about LIBERO-plus: what it is, how it differs from standard LIBERO, any new datasets, new tasks, commands, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22105923-cdce-4222-8312-d0da1d398355",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FjSLJNGfKiSRmvGRTg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0709c693-308c-4f9d-bfe0-e7f7b37adde0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ejiv15JiBk44Et2gVNZ5Vg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4594,
      "cache_read_input_tokens": 20041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4594,
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

### Tool result

_source line 27 · 2026-05-15T11:12:39.660Z_

<details><summary>↩ Tool result · `toolu_01FZ3ftyF8G5PyBo2B5gzzTZ`</summary>

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
  "parentUuid": "0709c693-308c-4f9d-bfe0-e7f7b37adde0",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "014b9c87-a47e-46fc-9d8a-e1da87c763c9",
  "sourceToolAssistantUUID": "0709c693-308c-4f9d-bfe0-e7f7b37adde0",
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

### Tool call

_source line 28 · 2026-05-15T11:12:39.783Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015edgA3Z36xavAcV451e7Af`</summary>

```json
{
  "query": "huggingface datasets \"lerobot/libero_spatial\" OR \"lerobot/libero_object\" OR \"lerobot/libero_goal\" OR \"lerobot/libero_90\" site:huggingface.co"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "014b9c87-a47e-46fc-9d8a-e1da87c763c9",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FjSLJNGfKiSRmvGRTg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5fc8004-6214-41a2-ad4d-f1d7c9cd8fdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ejiv15JiBk44Et2gVNZ5Vg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4594,
      "cache_read_input_tokens": 20041,
      "output_tokens": 346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4594
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 346,
          "cache_read_input_tokens": 20041,
          "cache_creation_input_tokens": 4594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4594,
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

_source line 29 · 2026-05-15T11:12:44.125Z_

<details><summary>↩ Tool result · `toolu_015edgA3Z36xavAcV451e7Af`</summary>

```text
Web search results for query: "huggingface datasets "lerobot/libero_spatial" OR "lerobot/libero_object" OR "lerobot/libero_goal" OR "lerobot/libero_90" site:huggingface.co"

Links: [{"title":"IPEC-COMMUNITY/libero_90_no_noops_lerobot · Dataset converted ideas","url":"https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot/libero_spatial_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_spatial_image"},{"title":"Commits · lerobot/libero_goal_image","url":"https://huggingface.co/datasets/lerobot/libero_goal_image/commits/main"}]

Based on the web search results, I found references to LeRobot LIBERO datasets on Hugging Face. The search revealed:

1. lerobot/libero_object_image dataset was created using LeRobot

2. lerobot/libero_spatial_image dataset was created using LeRobot

3. lerobot/libero_goal_image is available on Hugging Face

These datasets appear to be part of the LeRobot framework's LIBERO dataset collection on Hugging Face. The search results also mention discussions about converting LIBERO datasets and comparisons between different LIBERO variants (spatial, goal, object, and the 90-task version). The results indicate that LIBERO has different variants including LIBERO 10, spatial, goal and object datasets.

If you need more specific information about any of these datasets, their documentation, or how to access them, I can search for additional details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5fc8004-6214-41a2-ad4d-f1d7c9cd8fdc",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "3489cfd3-cbf0-4fc4-a42f-74aba40c2d34",
  "sourceToolAssistantUUID": "e5fc8004-6214-41a2-ad4d-f1d7c9cd8fdc",
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

_source line 30 · 2026-05-15T11:12:54.792Z_

<details><summary>↩ Tool result · `toolu_012up7eAufC6DCPqD75Gt5GZ`</summary>

````text
# LIBERO Dataset Card

## Dataset Overview

**Dataset Name:** `HuggingFaceVLA/libero`

**Source:** Hugging Face Datasets

**Task Category:** Robotics

**Modalities:** Image, Time-series

**Format:** Parquet

**License:** Apache 2.0

---

## Dataset Statistics

| Metric | Value |
|--------|-------|
| **Total Rows** | 273,000 |
| **Size Category** | 100K - 1M |
| **Splits** | 1 (train) |
| **Episodes** | 148 |
| **Tasks** | 10 |
| **Subset** | default |

---

## Data Structure

### Observation Fields
- **observation.images.image** - Primary camera image (256×256 pixels)
- **observation.images.image2** - Secondary camera image (256×256 pixels)
- **observation.state** - Robot state vector (8 floating-point values)

### Action Fields
- **action** - Action vector (7 elements representing robot control commands)

### Metadata Fields
- **timestamp** - float32 (0-45.4 range)
- **frame_index** - int64 (frame within episode)
- **episode_index** - int64 (0-147, 148 total episodes)
- **task_index** - int64 (0-9, 10 tasks)
- **index** - int64 (global row index)

---

## Sample Data Examples

From the viewer, sample observations show:
- Robot arm in tabletop manipulation scenario
- Dual RGB camera views of workspace
- Continuous 7-DOF joint commands
- State includes position, orientation, and gripper status

**Example action structure:** `[0.016, 0, 0, 0, 0, 0, -1]` (normalized joint velocities + gripper)

---

## How to Load the Dataset

### Using Hugging Face Datasets Library

```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("HuggingFaceVLA/libero")

# Access train split
train_data = dataset['train']

# Inspect a sample
sample = train_data[0]
print(sample.keys())
# Output: dict_keys(['observation.images.image', 'observation.images.image2', 
#                     'observation.state', 'action', 'timestamp', 'frame_index', 
#                     'episode_index', 'task_index', 'index'])
```

### Using LeRobot Integration

```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

# Load with LeRobot
dataset = LeRobotDataset("HuggingFaceVLA/libero")

# Iterate through episodes
for episode in dataset:
    observations = episode['observation']
    actions = episode['action']
    # Process episode data
```

---

## Data Format Details

### Image Data
- **Resolution:** 256×256 pixels
- **Format:** RGB images
- **Encoding:** JPEG (auto-converted to Parquet)
- **Camera Count:** 2 (primary + secondary views)

### State Vector (8-dim)
Typically represents:
- 3D end-effector position (x, y, z)
- 4D orientation (quaternion or similar)
- Gripper state or additional joint angles

### Action Vector (7-dim)
Typically represents:
- 6 DOF continuous control (xyz position + rotation)
- 1 gripper binary/continuous command (-1 to 1)

---

## Tags & Libraries

- **Associated Library:** LeRobot
- **Data Format Support:** 
  - Datasets (HuggingFace)
  - Dask (for distributed processing)
  - Croissant (metadata format)

---

## Dataset Features

✅ **Multi-episode structure** - 148 episodes organized by task  
✅ **Dual camera views** - Enriched visual observations  
✅ **Long horizons** - Up to 454 frames per episode  
✅ **Parquet format** - Efficient columnar storage  
✅ **LeRobot compatible** - Integrated with robot learning framework  

---

## Usage Recommendations

### For Training Vision-Language-Action Models
```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
from torch.utils.data import DataLoader

# Load dataset
dataset = LeRobotDataset("HuggingFaceVLA/libero")

# Create dataloader for training
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

for batch in dataloader:
    images = batch['observation']['images']  # [B, T, 2, 256, 256, 3]
    actions = batch['action']                # [B, T, 7]
    # Train your model
```

### For Episode-Level Analysis
```python
dataset = load_dataset("HuggingFaceVLA/libero", split="train")

# Filter by task
task_0_data = dataset.filter(lambda x: x['task_index'] == 0)

# Group by episode
episodes = {}
for sample in dataset:
    ep_id = sample['episode_index']
    if ep_id not in episodes:
        episodes[ep_id] = []
    episodes[ep_id].append(sample)
```

---

## Key References

- **Organization:** HuggingFaceVLA (Vision Language Action Models Research)
- **Related Work:** LIBERO - Long Horizon Vision-Language-Action Benchmark
- **Community:** [Discussions](https://huggingface.co/datasets/HuggingFaceVLA/libero/discussions) available on dataset page
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22105923-cdce-4222-8312-d0da1d398355",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "ace411ce-3a5b-41d0-b3fb-cb120e7bb8b9",
  "sourceToolAssistantUUID": "22105923-cdce-4222-8312-d0da1d398355",
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

_source line 31 · 2026-05-15T11:12:57.547Z_

Let me get a few more details on the additional dataset variants and the conversion script in the main LeRobot repo.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ace411ce-3a5b-41d0-b3fb-cb120e7bb8b9",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fm46e5SmAEpa9zUYfw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61f3198c-da11-4d67-b7bf-ce491d0624ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGAKNCL7NpNnAWgFQfpZeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 24635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1776,
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

_source line 32 · 2026-05-15T11:12:58.022Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GX3R96zx3DnErZrK1jjrDn`</summary>

```json
{
  "query": "site:huggingface.co/datasets/lerobot libero"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61f3198c-da11-4d67-b7bf-ce491d0624ce",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fm46e5SmAEpa9zUYfw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "833cea9b-343c-40ef-a0fe-e73035cefaf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGAKNCL7NpNnAWgFQfpZeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 24635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1776,
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

_source line 33 · 2026-05-15T11:12:58.940Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JPTXTejJTpeKuxxGb1Yfdh`</summary>

```json
{
  "query": "site:huggingface.co/datasets/physical-intelligence/libero lerobot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "833cea9b-343c-40ef-a0fe-e73035cefaf0",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fm46e5SmAEpa9zUYfw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac743b7a-1cfa-47fc-b7ad-aed10c8784cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGAKNCL7NpNnAWgFQfpZeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 24635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1776,
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

_source line 34 · 2026-05-15T11:12:59.729Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013HpVbFEdpAw7pEi2TEpows`</summary>

```json
{
  "url": "https://huggingface.co/datasets/lerobot/libero_10_image",
  "prompt": "Extract dataset card info: name, size, episodes, tasks, features, format. Include all metadata."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac743b7a-1cfa-47fc-b7ad-aed10c8784cf",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fm46e5SmAEpa9zUYfw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcfa64b7-1bc0-4412-8652-d89d2138cf97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGAKNCL7NpNnAWgFQfpZeY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 24635,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2721,
          "output_tokens": 239,
          "cache_read_input_tokens": 24635,
          "cache_creation_input_tokens": 1776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1776,
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

_source line 35 · 2026-05-15T11:13:02.920Z_

<details><summary>↩ Tool result · `toolu_01JPTXTejJTpeKuxxGb1Yfdh`</summary>

```text
Web search results for query: "site:huggingface.co/datasets/physical-intelligence/libero lerobot"

Links: [{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"README.md · physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/blob/main/README.md"},{"title":"physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/tree/main"},{"title":"physical-intelligence/libero · Description of the dataset features","url":"https://huggingface.co/datasets/physical-intelligence/libero/discussions/1"}]

I found results for the physical-intelligence/libero dataset on Hugging Face. Here's what the search revealed:

The libero dataset was created using LeRobot and combines four individual Libero datasets: Libero-Spatial, Libero-Object, Libero-Goal and Libero-10, all converted into LeRobot format. The dataset is available at https://huggingface.co/datasets/physical-intelligence/libero and has a size of approximately 34.9 GB.

The dataset is licensed under CC-BY-4.0 and is categorized as a robotics dataset with tags for LeRobot, libero, panda, and rlds. The data is stored in Parquet format.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac743b7a-1cfa-47fc-b7ad-aed10c8784cf",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "28bab1c7-a00c-40a6-b01b-c03a8247d371",
  "sourceToolAssistantUUID": "ac743b7a-1cfa-47fc-b7ad-aed10c8784cf",
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

_source line 36 · 2026-05-15T11:13:03.220Z_

<details><summary>↩ Tool result · `toolu_01GX3R96zx3DnErZrK1jjrDn`</summary>

```text
Web search results for query: "site:huggingface.co/datasets/lerobot libero"

Links: [{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot/libero_10_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_10_image"},{"title":"lerobot/libero_spatial_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_spatial_image"},{"title":"Commits · lerobot/libero_goal_image","url":"https://huggingface.co/datasets/lerobot/libero_goal_image/commits/main"},{"title":"lerobot/xarm_lift_medium at main","url":"https://huggingface.co/datasets/lerobot/xarm_lift_medium/tree/main"},{"title":"lerobot/config_examples · add_configs","url":"https://huggingface.co/datasets/lerobot/config_examples/discussions/1/files"},{"title":"lerobot/droid_1.0.1 at main","url":"https://huggingface.co/datasets/lerobot/droid_1.0.1/tree/main"},{"title":"lerobot/example_hil_serl_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/example_hil_serl_dataset"},{"title":"lerobot/austin_sirius_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/austin_sirius_dataset"}]

The search results show that there are several LIBERO-related datasets available on Hugging Face under the LeRobot organization. The search found:

1. **lerobot/libero** - The main LIBERO dataset
2. **lerobot/libero_object_image** - An image variant of the LIBERO dataset
3. **lerobot/libero_10_image** - Another image-based variant (last updated August 3, 2025)
4. **lerobot/libero_spatial_image** - A spatial image variant (last updated August 21, 2025)
5. **lerobot/libero_goal_image** - A goal-based image variant (last updated February 27, 2025)

All of these datasets are hosted on the Hugging Face platform as part of the LeRobot project. The search results indicate that they are advancing and democratizing artificial intelligence through open source and open science.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "833cea9b-343c-40ef-a0fe-e73035cefaf0",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "a904f30c-8c50-4766-9940-59a08764de11",
  "sourceToolAssistantUUID": "833cea9b-343c-40ef-a0fe-e73035cefaf0",
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

_source line 37 · 2026-05-15T11:13:08.722Z_

<details><summary>↩ Tool result · `toolu_013HpVbFEdpAw7pEi2TEpows`</summary>

````text
# LeRobot LIBERO-10 Dataset Card

## Basic Information
- **Name**: lerobot/libero_10_image
- **Organization**: LeRobot
- **License**: Apache 2.0
- **Repository**: Hugging Face Datasets

## Dataset Size & Structure
- **Total Rows**: 101,000 (101k rows)
- **Size Category**: 100K - 1M
- **Format**: Parquet (auto-converted)
- **Split**: Single training split

## Metadata

### Tasks
- **Primary Task**: Robotics
- **Task Count**: 10 tasks (indices 0-9)
- **Episodes**: 148 episodes (episode_index range: 0-147)

### Modalities
- Image (observation cameras)
- Time-series (state and action sequences)

### Features

#### Observations
- **observation.images.image**: 256×256 pixel RGB images (main camera)
- **observation.images.wrist_image**: 256×256 pixel RGB images (wrist camera)
- **observation.state**: List of 8 float values (robot state/joint positions)

#### Actions
- **action**: List of 7 float values (robot control commands)
  - Typically includes 6 continuous values + 1 discrete gripper value (-1, 0, 1)

#### Metadata
- **timestamp**: Float32 (0-45.4 range, in seconds)
- **frame_index**: Int64 (frame number within episode, 0-454)
- **episode_index**: Int64 (which episode, 0-147)
- **task_index**: Int64 (which task, 0-9)
- **index**: Int64 (global row index, 0-40.3k)

## Data Characteristics

### Sample Data Structure
```
Frame 0:
  - Timestamp: 0.0
  - State: [-0.053, 0.007, 0.678, 3.141, 0.002, -0.090, 0.039, -0.039]
  - Action: [0.016, 0, 0, 0, 0, 0, -1]
  - Episode: 0, Task: 0
```

### Action Space Pattern
- First 6 values: continuous control (typically normalized)
- Last value: discrete gripper control (-1 = open, 0 = maintain, 1 = close)

## Libraries & Tools
- **Datasets**: Hugging Face Datasets library
- **Dask**: Distributed computing support
- **Polars**: DataFrames support

## Availability
- **Viewer**: Interactive Data Studio available
- **Community**: 4 discussions/comments
- **Download**: Available via Hugging Face Hub (xet protocol supported)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcfa64b7-1bc0-4412-8652-d89d2138cf97",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "ac53395d-c0b4-4f84-8ae4-92f092956a81",
  "sourceToolAssistantUUID": "fcfa64b7-1bc0-4412-8652-d89d2138cf97",
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

_source line 38 · 2026-05-15T11:13:11.465Z_

Now let me check for the native conversion script within the LeRobot repo itself.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac53395d-c0b4-4f84-8ae4-92f092956a81",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fn5gvHKXkBTugcCq3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8962841d-1d73-4cea-b00c-acf7e84b707e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6kg8aZEahtsqAK8vVoKJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4806,
      "cache_read_input_tokens": 26411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4806,
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

_source line 39 · 2026-05-15T11:13:12.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012cLX94GQVwoky5nrzNScrZ`</summary>

```json
{
  "query": "github huggingface lerobot \"convert_libero\" OR \"libero\" path:lerobot/common/datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8962841d-1d73-4cea-b00c-acf7e84b707e",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fn5gvHKXkBTugcCq3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e4a15a2-4f42-4799-a8c0-aadccdb5dd67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6kg8aZEahtsqAK8vVoKJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4806,
      "cache_read_input_tokens": 26411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4806,
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

_source line 40 · 2026-05-15T11:13:14.028Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014cy6kCYGqqeUJBrfdN3cE5`</summary>

```json
{
  "url": "https://huggingface.co/datasets/physical-intelligence/libero",
  "prompt": "Extract the full dataset card: how this dataset was created, what raw datasets it combines, size, format, features, conversion process details. Include everything about how it maps to LeRobot format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e4a15a2-4f42-4799-a8c0-aadccdb5dd67",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fn5gvHKXkBTugcCq3o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a93b86f-7f45-48f1-afb8-0b42e1ffb462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6kg8aZEahtsqAK8vVoKJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4806,
      "cache_read_input_tokens": 26411,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4806
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 26411,
          "cache_creation_input_tokens": 4806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4806,
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

_source line 41 · 2026-05-15T11:13:18.333Z_

<details><summary>↩ Tool result · `toolu_012cLX94GQVwoky5nrzNScrZ`</summary>

```text
Web search results for query: "github huggingface lerobot "convert_libero" OR "libero" path:lerobot/common/datasets"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero/viewer/default/train"},{"title":"README.md · physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/blob/main/README.md"}]

Based on the web search results, I found relevant information about LIBERO dataset conversion and LeRobot integration:

## Key Findings

LeRobot supports standard benchmarks like LIBERO, which is a benchmark for studying robot learning.

### LIBERO Dataset Resources

The dataset combines four individual Libero datasets: Libero-Spatial, Libero-Object, Libero-Goal and Libero-10, and all datasets were converted into LeRobot format.

### Conversion Scripts

For converting LIBERO data to LeRobot format, there's a conversion script available in the Physical Intelligence OpenPI repository. The script can be run with command `uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/your/data`, and running this conversion script will take approximately 30 minutes.

### Available Datasets

The LeRobot LIBERO repository is maintained by the Hugging Face team, with modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments. Multiple converted LIBERO datasets are now available on the Hugging Face Hub, including libero_object_image, libero_spatial, libero_goal, and libero_10 variants.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e4a15a2-4f42-4799-a8c0-aadccdb5dd67",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "c7e9317b-c3e1-499e-8827-c87562cb9d7b",
  "sourceToolAssistantUUID": "7e4a15a2-4f42-4799-a8c0-aadccdb5dd67",
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

_source line 42 · 2026-05-15T11:13:27.871Z_

<details><summary>↩ Tool result · `toolu_014cy6kCYGqqeUJBrfdN3cE5`</summary>

````text
# LIBERO Dataset Card

## Overview
The LIBERO dataset is a robotic manipulation dataset published by Physical Intelligence and hosted on Hugging Face. It contains demonstration data for learning robot control policies.

## Dataset Statistics
- **Size**: 273,000 rows
- **Format**: Parquet (auto-converted from original format)
- **Task Categories**: Robotics
- **Modalities**: Image, Time-series
- **License**: CC-BY-4.0
- **ArXiv Reference**: 2306.03310

## Data Structure

### Raw Format
The dataset is organized hierarchically:
- **Subsets**: 1 (default)
- **Splits**: 1 (train)
- **Episodes**: 147 episodes
- **Total Frames**: ~273k frames

### Features

The dataset contains the following fields per frame:

| Field | Type | Description |
|-------|------|-------------|
| `image` | Image (256×256px) | RGB observation from main camera |
| `wrist_image` | Image (256×256px) | RGB observation from wrist-mounted camera |
| `state` | List (8 floats) | Robot joint positions/states |
| `actions` | List (7 floats) | Robot action command (likely 6-DOF + gripper) |
| `timestamp` | float32 | Frame timestamp |
| `frame_index` | int64 | Frame number within episode (0-454) |
| `episode_index` | int64 | Episode identifier (0-146) |
| `index` | int64 | Global row index (0-40.1k) |
| `task_index` | int64 | Task identifier (0-9, suggesting 10 tasks) |

### Data Example

```python
# Frame sample structure
{
  "image": <256×256 RGB image>,
  "wrist_image": <256×256 RGB wrist view>,
  "state": [-0.0534, 0.0070, 0.6783, 3.1408, 0.0018, -0.0899, 0.0388, -0.0388],
  "actions": [0.0161, 0, 0, 0, 0, 0, -1],
  "timestamp": 45.4,
  "frame_index": 0,
  "episode_index": 0,
  "task_index": 0
}
```

## Robot Hardware
- **Robot**: Franka Panda (indicated by "panda" tag)
- **State Dimension**: 8 (7 joint angles + gripper state)
- **Action Dimension**: 7 (6-DOF end-effector control + gripper command)

## LeRobot Integration

### Format Compatibility
The dataset includes tags for **LeRobot** integration:
- Supported by LeRobot framework
- Stored in RLDS format (standardized robot learning dataset format)
- Auto-converted to Parquet for accessibility

### Suggested LeRobot Mapping

```python
# Typical LeRobot episode structure
{
  "observations": {
    "image": [...],           # Main camera RGB
    "wrist_image": [...]      # Wrist camera RGB
  },
  "states": [...],            # Robot joint states
  "actions": [...],           # Control commands
  "episode_index": 0,
  "frame_index": [...],
  "timestamp": [...]
}
```

## Tasks
The dataset covers **10 different manipulation tasks** (task_index: 0-9), likely including:
- Grasping and placing objects
- Opening/closing drawers or containers
- Pushing or sliding objects
- Contact-rich manipulation tasks

## Access Methods

### HuggingFace Datasets Library
```python
from datasets import load_dataset

# Load the full dataset
libero = load_dataset("physical-intelligence/libero")

# Access training split
train_data = libero["train"]

# Iterate through episodes
for sample in train_data:
    episode_id = sample["episode_index"]
    image = sample["image"]
    action = sample["actions"]
    state = sample["state"]
```

### Direct Access
- **Dataset Viewer**: [HuggingFace Data Studio](https://huggingface.co/datasets/physical-intelligence/libero/viewer/)
- **Files**: Available via Git XET for efficient version control
- **Community**: 4 discussions available

## Related Tags
- `libero` - Dataset identifier
- `panda` - Franka Panda robot
- `rlds` - Robot Learning Dataset Standard format
- `LeRobot` - Integration framework

## Conversion Details
- Original format: RLDS (Robot Learning Dataset Standard)
- Converted to: Parquet (for accessibility and querying)
- Conversion maintains full compatibility with LeRobot framework
- Query support: SQL-based queries available via HuggingFace platform

## Use Cases
- Training imitation learning policies
- Behavior cloning models
- Multi-task robot learning
- Vision-based manipulation research
- Learning from demonstrations (LfD)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a93b86f-7f45-48f1-afb8-0b42e1ffb462",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "fe30dccd-7b29-4dc7-8bad-0718b2fb0c39",
  "sourceToolAssistantUUID": "3a93b86f-7f45-48f1-afb8-0b42e1ffb462",
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

_source line 43 · 2026-05-15T11:13:30.528Z_

Now let me save the research findings to the project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe30dccd-7b29-4dc7-8bad-0718b2fb0c39",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FoVYtUczTopU9FxoZU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbdc569c-6322-41a6-b9f2-a498ccc17bc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01679sPaXRnePAq8gb7CDKX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2348,
      "cache_read_input_tokens": 31217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2348,
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

_source line 44 · 2026-05-15T11:13:31.305Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AgPifgvWFLAWJvyGCXz3Jx`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbdc569c-6322-41a6-b9f2-a498ccc17bc4",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4FoVYtUczTopU9FxoZU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fe8a956-bacf-49c4-851b-aef2f7ac19d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01679sPaXRnePAq8gb7CDKX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2348,
      "cache_read_input_tokens": 31217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2348,
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

### Tool result

_source line 45 · 2026-05-15T11:13:31.307Z_

<details><summary>↩ Tool result · `toolu_01AgPifgvWFLAWJvyGCXz3Jx`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fe8a956-bacf-49c4-851b-aef2f7ac19d6",
  "isSidechain": true,
  "promptId": "d2c42f79-e375-4b9b-b7c3-7e1496f88b5b",
  "agentId": "a1a91bef0d6739352",
  "type": "user",
  "uuid": "197f873b-1415-4b1b-9a99-7f8936036067",
  "sourceToolAssistantUUID": "9fe8a956-bacf-49c4-851b-aef2f7ac19d6",
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

_source line 46 · 2026-05-15T11:14:16.656Z_



Here is the structured research report.

---

## 1. Does LeRobot Natively Support LIBERO?

**Yes.** LIBERO is a first-class benchmark in LeRobot. It is installed via:

```bash
pip install -e ".[libero]"
```

LeRobot provides native environment wrappers (`--env.type=libero`), official documentation at [huggingface.co/docs/lerobot/en/libero](https://huggingface.co/docs/lerobot/en/libero), and a dedicated fork of the LIBERO codebase at [github.com/huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero).

LIBERO covers **130 tasks** across **5 task suites**:

| Suite | CLI name | Tasks | Description |
|-------|----------|-------|-------------|
| LIBERO-Spatial | `libero_spatial` | 10 | Spatial relation reasoning |
| LIBERO-Object | `libero_object` | 10 | Object manipulation |
| LIBERO-Goal | `libero_goal` | 10 | Goal-conditioned tasks |
| LIBERO-90 | `libero_90` | 90 | Short-horizon tasks |
| LIBERO-Long | `libero_10` | 10 | Long-horizon tasks |

There is also **LIBERO-plus** (`--env.type=libero_plus`), a robustness extension with ~10,000 perturbed task variants across 7 dimensions (camera, lighting, layout, language, etc.).

---

## 2. Dataset Names on HuggingFace Hub

### Primary datasets (recommended for training)

| Dataset ID | Episodes | Tasks | Size | Notes |
|------------|----------|-------|------|-------|
| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | Official preprocessed dataset, recommended by LeRobot docs |
| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | All 4 standard suites combined (video format, AV1 codec) |
| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI's conversion, RLDS-origin, CC-BY-4.0 |
| `lerobot/libero_plus` | — | — | — | LIBERO-plus training data |

### Per-suite image datasets

| Dataset ID | Tasks | Episodes |
|------------|-------|----------|
| `lerobot/libero_10_image` | 10 | 148 |
| `lerobot/libero_object_image` | 10 | 454 |
| `lerobot/libero_spatial_image` | 10 | — |
| `lerobot/libero_goal_image` | 10 | — |

### Community datasets

| Dataset ID | Notes |
|------------|-------|
| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 with no-ops removed |

---

## 3. Data Format Mapping (LIBERO HDF5/RLDS to LeRobot)

### Observation/Action schema

| LIBERO Field | LeRobot Feature | Type | Shape |
|---|---|---|---|
| `observation["image"]` / `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |
| `observation["wrist_image"]` / `robot0_eye_in_hand_image` | `observation.images.image2` (or `.wrist_image`) | Video/Image | (256, 256, 3) |
| `observation["state"]` | `observation.state` | float32 | (8,) |
| `action` | `action` | float32 | (7,) |
| `language_instruction` | `task` (task_index) | string/int | — |

### LeRobot dataset metadata

- **robot_type**: `panda`
- **fps**: `10`
- **Video codec**: AV1, yuv420p (for video datasets)
- **Storage**: Parquet for tabular data + MP4 for video streams

### State vector (8-dim)
End-effector position (3) + axis-angle orientation (3) + gripper qpos (2)

### Action vector (7-dim)
6D end-effector delta + 1D gripper command. Range: `Box(-1, 1, shape=(7,))`

---

## 4. Conversion Scripts and Utilities

### A. Physical Intelligence's OpenPI conversion script (primary)

**Path**: [`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)

**Prerequisites**:
```bash
uv pip install tensorflow tensorflow_datasets
```

**Raw data source**: Download from `https://huggingface.co/datasets/openvla/modified_libero_rlds`

**Usage**:
```bash
uv run examples/libero/convert_libero_data_to_lerobot.py \
  --data_dir /path/to/your/data \
  --push_to_hub
```

**What it does**:
1. Reads 4 raw RLDS datasets: `libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`
2. Creates a `LeRobotDataset` with robot_type=panda, fps=10
3. Iterates episodes, calling `dataset.add_frame()` per step
4. Calls `dataset.save_episode()` per episode
5. Optionally pushes to HuggingFace Hub

**Processing time**: ~30 minutes.

**Key imports**:
```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
import tensorflow_datasets as tfds
```

### B. Generic HDF5 to LeRobot converter

**Repo**: [github.com/anarnuri/hdf5_to_lerobot_converter](https://github.com/anarnuri/hdf5_to_lerobot_converter)

Works with custom HDF5 formats including LIBERO's native format.

### C. Using pre-converted datasets (no conversion needed)

The simplest path is to use the already-converted datasets directly:

```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

dataset = LeRobotDataset("HuggingFaceVLA/libero")
# or
dataset = LeRobotDataset("lerobot/libero")
```

### D. Training command (end-to-end example)

```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.repo_id=${HF_USER}/libero-test \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task=libero_10 \
  --output_dir=./outputs/ \
  --steps=100000 \
  --batch_size=4 \
  --eval.batch_size=1 \
  --eval.n_episodes=1 \
  --eval_freq=1000
```

### E. Evaluation command

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

---

## Key Takeaways for This Project

1. **No conversion work needed** if using the pre-converted `HuggingFaceVLA/libero` or `lerobot/libero` datasets.
2. If you need LIBERO-90 data specifically, it is NOT in the standard pre-converted datasets. You would need the OpenPI conversion script or the community `IPEC-COMMUNITY/libero_90_no_noops_lerobot` dataset.
3. The LeRobot LIBERO env wrapper handles MuJoCo simulation natively (Linux only, `MUJOCO_GL=egl` for headless).
4. Control modes: `relative` (default) vs `absolute` -- must match your policy's action parameterization.

Sources:
- [LeRobot LIBERO Documentation](https://huggingface.co/docs/lerobot/en/libero)
- [LeRobot LIBERO-plus Documentation](https://huggingface.co/docs/lerobot/main/libero_plus)
- [lerobot/libero dataset](https://huggingface.co/datasets/lerobot/libero)
- [HuggingFaceVLA/libero dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero)
- [physical-intelligence/libero dataset](https://huggingface.co/datasets/physical-intelligence/libero)
- [OpenPI LIBERO conversion script](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)
- [huggingface/lerobot-libero fork](https://github.com/huggingface/lerobot-libero)
- [huggingface/lerobot main repo](https://github.com/huggingface/lerobot)
- [lerobot/libero_10_image](https://huggingface.co/datasets/lerobot/libero_10_image)
- [lerobot/libero_object_image](https://huggingface.co/datasets/lerobot/libero_object_image)
- [lerobot/libero_spatial_image](https://huggingface.co/datasets/lerobot/libero_spatial_image)
- [HDF5 to LeRobot converter](https://github.com/anarnuri/hdf5_to_lerobot_converter)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "197f873b-1415-4b1b-9a99-7f8936036067",
  "isSidechain": true,
  "agentId": "a1a91bef0d6739352",
  "requestId": "req_011Cb4Fokov25c8JbNCST9it",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b021c07-1238-48d6-82aa-275c50f3ca96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "sessionId": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH2NBJk1ZWxu9uvp5cJNoH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 33565,
      "output_tokens": 2598,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 305
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2598,
          "cache_read_input_tokens": 33565,
          "cache_creation_input_tokens": 305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 305,
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
