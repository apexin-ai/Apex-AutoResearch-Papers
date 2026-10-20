# Research conversation: I need to understand the feasibility of adding LIBERO benchmark tasks to a robot learning experiment that uses SmolVLA (

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7f0f63bdf2589c2f.jsonl`
- **Structured JSON:** [`7f110e978bff01a1eb93.json`](../../sessions/7f/7f110e978bff01a1eb93.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-13T19:23:18.749Z_

I need to understand the feasibility of adding LIBERO benchmark tasks to a robot learning experiment that uses SmolVLA (450M parameter VLA model from HuggingFace/lerobot).

1. Search for "LIBERO benchmark robot manipulation SmolVLA" and "lerobot LIBERO dataset"
2. Search for "SmolVLA LIBERO fine-tuning" to see if anyone has done this
3. Use WebFetch to check https://huggingface.co/datasets if LIBERO datasets are available in lerobot format
4. Search for "LIBERO demonstration dataset multimodal strategies operators" - I need to know if LIBERO has the multi-operator structure needed (different demonstrators with different strategies) similar to RoboMimic MH

Key questions:
- Is LIBERO data readily available in lerobot/SmolVLA-compatible format?
- Does LIBERO have multi-operator demonstrations with known quality labels? (This is critical - OT-Consensus needs demonstrations from multiple operators/strategies to test mode discovery)
- How many demonstrations per task? How many tasks?
- What would be the additional compute cost to add 1-2 LIBERO tasks?

Report concisely with practical feasibility assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "371b6f92-8c2f-4d5e-b2b7-e1b288938bcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T19:23:18.752Z_

```json
{
  "parentUuid": "371b6f92-8c2f-4d5e-b2b7-e1b288938bcb",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
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
  "uuid": "fb78e644-4723-44a4-b9d3-a22af4000e61",
  "timestamp": "2026-05-13T19:23:18.752Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T19:23:26.960Z_



I'll research this systematically. Let me start with web searches and fetching relevant pages in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb78e644-4723-44a4-b9d3-a22af4000e61",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17YBwco54WpDa4eF45g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fb71932-e02b-4637-b4bb-246eb1204f42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJeznL1Ex69iLep4BjNP4d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 828,
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

_source line 4 · 2026-05-13T19:23:27.348Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016V5fnu5o6749QWfwLj16wJ`</summary>

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
  "parentUuid": "7fb71932-e02b-4637-b4bb-246eb1204f42",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17YBwco54WpDa4eF45g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e767483b-6d92-491e-a8c3-57da17b991fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJeznL1Ex69iLep4BjNP4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 8223,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 828,
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

_source line 5 · 2026-05-13T19:23:27.352Z_

<details><summary>↩ Tool result · `toolu_016V5fnu5o6749QWfwLj16wJ`</summary>

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
  "parentUuid": "e767483b-6d92-491e-a8c3-57da17b991fe",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "52a423a2-26fa-4624-ba41-039c7839ce34",
  "sourceToolAssistantUUID": "e767483b-6d92-491e-a8c3-57da17b991fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T19:23:29.907Z_



Now let me run all the searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52a423a2-26fa-4624-ba41-039c7839ce34",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17YpwM8z3bzi2Pofmk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0376e8ae-52c2-4177-b75c-202a596fc4f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Nnw9p78VLD4o9rVju51Q9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9051,
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

_source line 7 · 2026-05-13T19:23:30.925Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018tnhw6E6x3gjk1PARFvTYS`</summary>

```json
{
  "query": "LIBERO benchmark robot manipulation SmolVLA lerobot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0376e8ae-52c2-4177-b75c-202a596fc4f6",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17YpwM8z3bzi2Pofmk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff4a0336-5a8e-4770-9427-3aa4fc30e362",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Nnw9p78VLD4o9rVju51Q9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9051,
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

_source line 8 · 2026-05-13T19:23:31.332Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011epLbtr9UzWtbEkdCxtTXd`</summary>

```json
{
  "query": "SmolVLA LIBERO fine-tuning lerobot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff4a0336-5a8e-4770-9427-3aa4fc30e362",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17YpwM8z3bzi2Pofmk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65726922-700b-47d8-bb47-66f9531cf8f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Nnw9p78VLD4o9rVju51Q9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9051,
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

_source line 9 · 2026-05-13T19:23:32.272Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BcPKpvca2xQjGpPTLRuLqz`</summary>

```json
{
  "query": "LIBERO demonstration dataset multi-operator strategies different demonstrators"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65726922-700b-47d8-bb47-66f9531cf8f1",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17YpwM8z3bzi2Pofmk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d8d0d42-1513-408f-ae2e-dc0591bd001c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Nnw9p78VLD4o9rVju51Q9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9051,
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

_source line 10 · 2026-05-13T19:23:32.752Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kxa3E2ErLfdRv6BiZHPXng`</summary>

```json
{
  "query": "lerobot LIBERO dataset huggingface format convert"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d8d0d42-1513-408f-ae2e-dc0591bd001c",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17YpwM8z3bzi2Pofmk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a2275ef-b25b-452c-b224-73b39ac72e56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Nnw9p78VLD4o9rVju51Q9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9051,
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

_source line 11 · 2026-05-13T19:23:34.591Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015zK1VBY8tHXTKoRtNTzxuD`</summary>

```json
{
  "url": "https://huggingface.co/datasets?search=libero+lerobot",
  "prompt": "List all datasets related to LIBERO in lerobot format. Show dataset names, descriptions, and sizes. Are there LIBERO datasets already converted to lerobot/LeRobotDataset format?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a2275ef-b25b-452c-b224-73b39ac72e56",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17YpwM8z3bzi2Pofmk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf6bf0e0-7f98-4c3c-a3a9-55e4f4a54aaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Nnw9p78VLD4o9rVju51Q9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9051,
      "output_tokens": 340,
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
          "output_tokens": 340,
          "cache_read_input_tokens": 9051,
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

_source line 12 · 2026-05-13T19:23:37.942Z_

<details><summary>↩ Tool result · `toolu_01BcPKpvca2xQjGpPTLRuLqz`</summary>

```text
Web search results for query: "LIBERO demonstration dataset multi-operator strategies different demonstrators"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"Embodied-CoT/embodied_features_and_demos_libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Embodied-CoT/embodied_features_and_demos_libero"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"LIBERO Datasets – LIBERO","url":"https://libero-project.github.io/datasets"}]

Based on the web search results, here's what I found about the LIBERO demonstration dataset and its multi-operator and multi-demonstrator aspects:

## Overview of LIBERO Dataset

LIBERO is designed for studying knowledge transfer in multitask and lifelong robot learning problems. The dataset contains 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## Demonstration Data

To support sample-efficient learning, LIBERO provides high-quality human-teleoperated demonstration data for all tasks. More specifically, each task includes 50 high-quality teleoperated demonstrations (6,500 total).

## Multi-Demonstrator Strategies

While the search results confirm that LIBERO includes human-teleoperated demonstrations across multiple tasks, the specific details about different demonstrators and their individual strategies are not extensively covered in the available search results. The results focus more on the overall demonstration quality and the 50 demonstrations per task rather than analyzing variations across different human operators.

The emphasis appears to be on using these high-quality demonstrations to enable sample-efficient learning through behavior cloning approaches, rather than explicitly studying multi-operator strategies or differences between individual demonstrators.

If you need more detailed information about specific multi-demonstrator strategies or operator variations in LIBERO, you may want to consult the original LIBERO paper directly or the official documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d8d0d42-1513-408f-ae2e-dc0591bd001c",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "c7f997fb-bf79-4fb6-8cc5-eaba00c53c9c",
  "sourceToolAssistantUUID": "8d8d0d42-1513-408f-ae2e-dc0591bd001c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T19:23:38.493Z_

<details><summary>↩ Tool result · `toolu_018tnhw6E6x3gjk1PARFvTYS`</summary>

```text
Web search results for query: "LIBERO benchmark robot manipulation SmolVLA lerobot"

Links: [{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2354"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"LIBERO – LIBERO","url":"https://libero-project.github.io/main.html"},{"title":"Question about the HuggingFaceVLA/smolvla_libero Model Configuration · Issue #2294 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2294"}]

Based on the search results, here's what I found about LIBERO benchmark, robot manipulation, SmolVLA, and LeRobot:

## Overview

LIBERO is a benchmark designed to study lifelong robot learning, based on the idea that robots won't just be pretrained once but need to keep learning and adapting with their human users over time, called lifelong learning in decision making (LLDM).

## Connection to SmolVLA and LeRobot

At LeRobot, LIBERO was ported into their framework and used mainly to evaluate SmolVLA, their lightweight Vision-Language-Action model. SmolVLA is a Vision-Language-Action Model for Affordable and Efficient Robotics.

## Benchmark Structure

LIBERO includes several task suites: LIBERO-Goal (goal-conditioned tasks), LIBERO-90 (90 short-horizon tasks), and LIBERO-Long (10 long-horizon tasks), together covering 130 tasks ranging from simple object manipulations to complex multi-step scenarios.

## Performance

According to the SmolVLA paper, the 0.45B model achieves success rates of approximately 90%, 96%, 92%, 71% (Spatial, Object, Goal, Long), averaging 87.3%.

## Integration

LIBERO is now part of LeRobot's multi-eval supported simulation, meaning you can benchmark policies either on a single suite of tasks or across multiple suites at once.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff4a0336-5a8e-4770-9427-3aa4fc30e362",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "8bec2161-d72b-4dfa-a382-9e98aa2ad4b4",
  "sourceToolAssistantUUID": "ff4a0336-5a8e-4770-9427-3aa4fc30e362",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T19:23:39.776Z_

<details><summary>↩ Tool result · `toolu_011epLbtr9UzWtbEkdCxtTXd`</summary>

```text
Web search results for query: "SmolVLA LIBERO fine-tuning lerobot 2025 2026"

Links: [{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"fine tune SmolVLA in libero with tensor shape mismatch · Issue #2418 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2418"},{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/guides/vla-models-comparison"},{"title":"Hugging Face Releases SmolVLA, a Compact Open-Source Robotics Model -- Pure AI","url":"https://pureai.com/articles/2025/06/10/hugging-face-releases-smolvla.aspx"}]

Based on the search results, here's what I found about SmolVLA, LIBERO fine-tuning, and LeRobot:

## Overview

Since LIBERO is a common benchmark dataset, there's a pretrained SmolVLA checkpoint available, which provides a good starting point for fine-tuning. At only 450 million parameters, it's an order of magnitude smaller than frontier robotics models (which can exceed 5–7 billion parameters), meaning it can run on consumer hardware without needing to rent expensive GPU clusters.

## LeRobot Framework Integration

LeRobot provides tools that significantly accelerate AI-driven robotics development and handles everything from dataset management and model training to deployment, making it possible for individuals to accomplish what previously required entire research labs.

## Fine-tuning Performance

According to the paper, the 0.45B model achieves success rates of approximately 90%, 96%, 92%, 71% (Spatial, Object, Goal, Long), averaging 87.3% on LIBERO. However, some users attempting to reproduce the SmolVLA results on the LIBERO benchmark have observed gaps between their evaluation results and the published results, with suspicions that the discrepancy might be primarily due to the effective batch size.

## Fine-tuning Requirements

Fine-tuning requirements include 1x RTX 4090 (24 GB) for full fine-tuning; training time 4–12 hours for 200 demonstrations, making SmolVLA accessible to any lab with a modern consumer GPU.

## Recent Developments

LIBERO is the most common benchmark for VLA models and the same benchmark used by VLA-0 authors, with researchers describing their path to that milestone: the design choices made, the ablations run, and what they learned from them.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65726922-700b-47d8-bb47-66f9531cf8f1",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "c5cf41b6-38e7-4b25-a500-a4e2d9faf99e",
  "sourceToolAssistantUUID": "65726922-700b-47d8-bb47-66f9531cf8f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T19:23:39.923Z_

<details><summary>↩ Tool result · `toolu_015zK1VBY8tHXTKoRtNTzxuD`</summary>

```text
# LIBERO Datasets in LeRobot Format

Based on the Hugging Face Datasets page, **yes, there are multiple LIBERO datasets already converted to lerobot/LeRobotDataset format**. Here's a comprehensive list:

## Official LIBERO LeRobot Datasets

| Dataset Name | Size | Downloads | Last Updated |
|---|---|---|---|
| **lerobot/libero_10_image** | 101k | 4.41k | Mar 9 |
| **lerobot/libero_spatial_image** | 53k | 1.42k | Mar 9 |
| **lerobot/libero_goal_image** | 52k | 1.17k | Mar 9 |
| **lerobot/libero_object_image** | 67k | 1.28k | Mar 9 |

## Extended LeRobot Conversions

| Dataset Name | Size | Downloads | Last Updated |
|---|---|---|---|
| **jesbu1/libero_90_lerobot** | 575k | 361 | Mar 17, 2025 |
| **Felix-Zhenghao/libero-10-lerobot** | 101k | 1.24k | Apr 20, 2025 |
| **IPEC-COMMUNITY/libero_90_no_noops_lerobot** | 569k | 2.39k | Jul 1, 2025 |

## Latest Community Versions (v1.0.0)

The most recent conversions include:
- **IPEC-COMMUNITY/libero_goal_no_noops_1.0.0_lerobot** (52k rows, 7.76k downloads)
- **IPEC-COMMUNITY/libero_object_no_noops_1.0.0_lerobot** (67k rows, 7.74k downloads)
- **IPEC-COMMUNITY/libero_spatial_no_noops_1.0.0_lerobot** (53k rows, 9.44k downloads)
- **IPEC-COMMUNITY/libero_10_no_noops_1.0.0_lerobot** (101k rows, 8.65k downloads)

These datasets span the full range of LIBERO task variants (10, 90, goal, spatial, object) and include variants with depth masks, path masks, and RDP processing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf6bf0e0-7f98-4c3c-a3a9-55e4f4a54aaf",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "124277a7-7e92-40ac-b8dc-ebe27e40ad3e",
  "sourceToolAssistantUUID": "bf6bf0e0-7f98-4c3c-a3a9-55e4f4a54aaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T19:23:40.384Z_

<details><summary>↩ Tool result · `toolu_01Kxa3E2ErLfdRv6BiZHPXng`</summary>

```text
Web search results for query: "lerobot LIBERO dataset huggingface format convert"

Links: [{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LeRobotDataset v3.0 · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3"},{"title":"IPEC-COMMUNITY/libero_90_no_noops_lerobot · Dataset converted ideas","url":"https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2"},{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"`LeRobotDataset:v3.0`: Bringing large-scale datasets to `lerobot`","url":"https://huggingface.co/blog/lerobot-datasets-v3"},{"title":"Using Dataset Tools · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/using_dataset_tools"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"How to convert my own dataset to LerobotDataset format? · Issue #846 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/846"},{"title":"LIBERO lerobot format (mask, depth) - a binhng Collection","url":"https://huggingface.co/collections/binhng/libero-lerobot-format-mask-depth"}]

I found relevant information about converting LIBERO datasets to LeRobot format. Here's what I found:

## Converting LIBERO to LeRobot Format

LeRobot uses a standardized LeRobotDataset format that stores synchronized MP4 videos (or images) for vision and Parquet files for state/action data.

### Key Resources

1. **any4lerobot Tool**: Users have successfully used any4lerobot to convert LIBERO hdf5 data to lerobot format.

2. **Example Conversion Script**: There's a minimal example script for converting a dataset to LeRobot format available, with raw Libero datasets available from the openvla/modified_libero_rlds dataset. Running this conversion script takes approximately 30 minutes.

3. **Pre-processed Datasets**: LeRobot provides a preprocessed LIBERO dataset that is fully compatible with the current LeRobot codebase and requires no additional manipulation.

### Dataset Format Details

LeRobotDataset v3.0 is a standardized format for robot learning data that provides unified access to multi-modal time-series data, sensorimotor signals and multi-camera video, as well as rich metadata for indexing, search, and visualization on the Hugging Face Hub.

### Note on Video Encoding

Video decoding issues have been reported during conversion, though re-encoding problematic episodes back into video typically resolves the issue; AV1 encoding has shown occasional corruption problems, but X264 encoding hasn't shown similar issues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a2275ef-b25b-452c-b224-73b39ac72e56",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "10fd1e34-19e6-4ef5-9aff-affede1c72f8",
  "sourceToolAssistantUUID": "4a2275ef-b25b-452c-b224-73b39ac72e56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-13T19:23:43.857Z_

Good, I have substantial information. Let me now fetch more specific details on the critical question about multi-operator demonstrations, and check the LIBERO paper and the specific lerobot issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10fd1e34-19e6-4ef5-9aff-affede1c72f8",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17ZnSoVUQBrrdCZVMAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9136e38e-2721-451e-bf85-4004a41e1297",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTN8aYSr44xnMYWCJJJ9i8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 612,
      "cache_creation_input_tokens": 4057,
      "cache_read_input_tokens": 10962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4057,
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

_source line 18 · 2026-05-13T19:23:46.253Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PM5DzwUBXMJcRcxWfhpYNh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2306.03310",
  "prompt": "Extract details about: 1) How were demonstrations collected? Single operator or multiple operators? 2) Are there quality labels or strategy labels on demonstrations? 3) How many demonstrations per task? 4) Is there any multi-modal behavior (different strategies for same task)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9136e38e-2721-451e-bf85-4004a41e1297",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17ZnSoVUQBrrdCZVMAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0586b8be-345c-48a8-906f-3b23f56a8e56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTN8aYSr44xnMYWCJJJ9i8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 612,
      "cache_creation_input_tokens": 4057,
      "cache_read_input_tokens": 10962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4057,
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

_source line 19 · 2026-05-13T19:23:49.643Z_

<details><summary>↩ Tool result · `toolu_01PM5DzwUBXMJcRcxWfhpYNh`</summary>

```text
# LIBERO Demonstration Data Details

Based on the provided arXiv page content, I can only identify **one specific detail** about the demonstrations:

**Available Information:**
The abstract states the benchmark includes "high-quality human-teleoperated demonstration data for all tasks," confirming that demonstrations were collected through human teleoperation.

**Information Not Available:**
The webpage excerpt does not contain details regarding:
- Whether a single or multiple operators collected the demonstrations
- Quality labels or strategy labels on demonstrations
- The quantity of demonstrations per task
- Whether multi-modal behaviors (alternative strategies) exist for the same tasks

To obtain these specifics, you would need to access the full paper PDF or visit the project website mentioned in the abstract at https://libero-project.github.io.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0586b8be-345c-48a8-906f-3b23f56a8e56",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "d0793073-9dcd-4209-8a7d-0f8204fb24f9",
  "sourceToolAssistantUUID": "0586b8be-345c-48a8-906f-3b23f56a8e56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-13T19:23:50.237Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Sw7dNyYdeptEpZF85z49Z1`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/3287",
  "prompt": "Extract the training configuration details for SmolVLA on LIBERO: batch size, learning rate, number of training steps, GPU requirements, training time. What compute is needed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0793073-9dcd-4209-8a7d-0f8204fb24f9",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17ZnSoVUQBrrdCZVMAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85062320-a000-4093-ad73-090f8a605270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTN8aYSr44xnMYWCJJJ9i8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 612,
      "cache_creation_input_tokens": 4057,
      "cache_read_input_tokens": 10962,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4057
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 612,
          "output_tokens": 393,
          "cache_read_input_tokens": 10962,
          "cache_creation_input_tokens": 4057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4057,
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

_source line 21 · 2026-05-13T19:23:50.470Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016HawGRMnzdT4fp1KK8CiQS`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/libero",
  "prompt": "Extract all details about LIBERO integration with lerobot: how to train, evaluate, dataset names, task suites, number of tasks per suite, training commands, compute requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85062320-a000-4093-ad73-090f8a605270",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17ZnSoVUQBrrdCZVMAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0c837ef-2668-4712-ace3-ac3eaa5dcff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTN8aYSr44xnMYWCJJJ9i8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 612,
      "cache_creation_input_tokens": 4057,
      "cache_read_input_tokens": 10962,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4057
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 612,
          "output_tokens": 393,
          "cache_read_input_tokens": 10962,
          "cache_creation_input_tokens": 4057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4057,
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

_source line 22 · 2026-05-13T19:23:50.836Z_

<details><summary>↩ Tool result · `toolu_016HawGRMnzdT4fp1KK8CiQS`</summary>

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
  "parentUuid": "f0c837ef-2668-4712-ace3-ac3eaa5dcff9",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "bade6dab-731e-4ff7-9d6e-b8d8c07c3a6e",
  "sourceToolAssistantUUID": "f0c837ef-2668-4712-ace3-ac3eaa5dcff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-13T19:23:55.197Z_

<details><summary>↩ Tool result · `toolu_01Sw7dNyYdeptEpZF85z49Z1`</summary>

```text
# SmolVLA Training Configuration Details on LIBERO

Based on the GitHub issue, here are the confirmed training details:

**Explicitly Stated Parameters:**
- **Batch Size:** 64
- **Training Steps:** "100,000 training steps with batch size 64 for simulation benchmarks"
- **Training Setup:** Frozen VLM backbone, action expert trained from scratch

**Not Provided in This Issue:**
The document does not contain specific information about:
- Learning rate or scheduler details
- GPU count or compute requirements
- Training time duration
- Global/effective batch size calculations

**Key Context:**
The issue author explicitly requests these missing details from the LeRobot team, stating they need "exact reproduction details for the LIBERO experiments" including "learning rate and scheduler," "global/effective batch size and GPU count," and "specific commit hash used for the paper experiments."

The author achieved 44.8%-83% performance on various LIBERO suites but fell short of paper results (71%-96%), suggesting the missing configuration details may be critical for full reproduction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85062320-a000-4093-ad73-090f8a605270",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "4a2a4644-a2f0-4b47-a636-2f95d2cef1ea",
  "sourceToolAssistantUUID": "85062320-a000-4093-ad73-090f8a605270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-13T19:23:58.533Z_

Now let me get the critical detail about multi-operator structure and the LIBERO paper's data collection methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a2a4644-a2f0-4b47-a636-2f95d2cef1ea",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17atP2RYRyBE3HdK1tU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "785a70c8-2b26-42fa-ac23-14d6fdf874c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TtgmFV5Svdb5ixnJNjJHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2170,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 15019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
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

_source line 25 · 2026-05-13T19:24:00.997Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UKQpwDDPEiiess7HLh1trY`</summary>

```json
{
  "url": "https://libero-project.github.io/datasets",
  "prompt": "Extract all details about how demonstrations were collected: how many demonstrators/operators, were demonstrations collected by a single person or multiple people, is there any quality labeling (better/worse), any mention of different strategies or multi-modal demonstrations for the same task?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "785a70c8-2b26-42fa-ac23-14d6fdf874c5",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17atP2RYRyBE3HdK1tU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "876c568c-5145-416a-b220-fd8a6fabd0f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TtgmFV5Svdb5ixnJNjJHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2170,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 15019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
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

_source line 26 · 2026-05-13T19:24:03.844Z_

<details><summary>↩ Tool result · `toolu_01UKQpwDDPEiiess7HLh1trY`</summary>

```text
# LIBERO Datasets - Demonstration Collection Details

Based on the provided web page content, **no information is available** about how demonstrations were collected for the LIBERO datasets.

The page lists what is included in the datasets: "RGB images from workspace and wrist cameras, Proprioception, Language task specifications, PDDL scene descriptions." However, it contains no details regarding:

- Number of demonstrators or operators
- Whether data collection involved single or multiple people
- Quality labeling or assessment of demonstrations
- Different strategies or multi-modal demonstrations for tasks

The content directs users to "the LIBERO documentation" for "more detailed description," suggesting such information may exist in the full documentation rather than on this overview page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "876c568c-5145-416a-b220-fd8a6fabd0f1",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "cb82df2d-e3d5-463c-8ae7-0617c4c2996f",
  "sourceToolAssistantUUID": "876c568c-5145-416a-b220-fd8a6fabd0f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T19:24:04.939Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lc4eVBLjrPX2T7fHzsGA6q`</summary>

```json
{
  "url": "https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf",
  "prompt": "Extract details about: 1) How were demonstrations collected? Single operator or multiple operators? How many human demonstrators? 2) Are there quality labels or strategy labels? 3) How many demonstrations per task exactly? 4) Is there any discussion of multi-modal behavior or different strategies for the same task? 5) Any mention of demonstration diversity or operator variability?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb82df2d-e3d5-463c-8ae7-0617c4c2996f",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17atP2RYRyBE3HdK1tU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62c5d65a-6498-40b7-a6ef-83c958a5b271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TtgmFV5Svdb5ixnJNjJHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2170,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 15019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
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

_source line 28 · 2026-05-13T19:24:05.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KBBMbUjt4YYQAQrLG7sxcE`</summary>

```json
{
  "query": "LIBERO benchmark 50 demonstrations per task single operator teleoperation collection procedure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62c5d65a-6498-40b7-a6ef-83c958a5b271",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17atP2RYRyBE3HdK1tU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a839ef92-4988-4e50-897b-07552afce7fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TtgmFV5Svdb5ixnJNjJHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2170,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 15019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
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

_source line 29 · 2026-05-13T19:24:10.178Z_

<details><summary>↩ Tool result · `toolu_01Lc4eVBLjrPX2T7fHzsGA6q`</summary>

```text
I appreciate your request, but I need to be transparent: the content you've provided appears to be a PDF file encoded in binary/compressed format, not readable text. The page shows PDF structure markers (like "%PDF-1.3", "FlateDecode", "DCTDecode") and compressed stream data rather than extractable text about demonstrations.

To properly answer your questions about:
1. Demonstration collection methodology
2. Quality/strategy labels
3. Demonstrations per task
4. Multi-modal behavior
5. Diversity metrics

I would need either:
- A properly decoded text version of this document
- A direct link to the source paper
- The document title so I can locate it properly

If you can provide the text content or document details, I'd be happy to analyze it within the constraints you've specified (125-character quote limits, proper attribution, etc.).

[Binary content (application/pdf, 3.6MB) also saved to /home/ubuntu/.claude-account-2/projects/-/4b2e93a9-7a45-4028-badc-913d53ffd7bb/tool-results/webfetch-1778700246659-60o98y.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62c5d65a-6498-40b7-a6ef-83c958a5b271",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "e34c5a57-381b-49b4-b6e0-382b84549064",
  "sourceToolAssistantUUID": "62c5d65a-6498-40b7-a6ef-83c958a5b271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T19:24:11.809Z_

<details><summary>↩ Tool result · `toolu_01KBBMbUjt4YYQAQrLG7sxcE`</summary>

```text
Web search results for query: "LIBERO benchmark 50 demonstrations per task single operator teleoperation collection procedure"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Libero-Object Benchmark","url":"https://www.emergentmind.com/topics/libero-object-benchmark"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"}]

Based on the search results, I found detailed information about the LIBERO benchmark's demonstration collection procedure:

## LIBERO Benchmark Demonstration Collection

Each task includes 50 high-quality, human-teleoperated demonstrations per task (each a sequence of images, robot proprioception, and continuous 7-DoF end-effector/gripper actions), rendered using MuJoCo and robosuite.

The demonstrations are collected by human experts through teleoperation with 3Dconnexion Spacemouse. More specifically, demonstrations are collected using a SpaceMouse teleoperator at 20 Hz with automatic filtering and validation pipelines; available as HDF5 for reproducibility.

The benchmark is structured into four task suites, each with around 10 tasks and 50 teleoperation demonstrations per task, for a total of roughly 130 tasks and 6,500 trajectories.

This teleoperation collection procedure provides high-quality training data that enables sample-efficient learning for the robot manipulation tasks in the LIBERO benchmark, which focuses on lifelong learning and knowledge transfer in robotic systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a839ef92-4988-4e50-897b-07552afce7fa",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "ecf24701-f5c4-4697-9d24-54d4e24412fe",
  "sourceToolAssistantUUID": "a839ef92-4988-4e50-897b-07552afce7fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T19:24:27.208Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L9ZhdYVjYzUdFaokbzYkXb`</summary>

```json
{
  "url": "https://www.emergentmind.com/topics/libero",
  "prompt": "Find any details about: 1) How many human operators collected the demonstrations - was it one person or multiple? 2) Any mention of demonstration quality variation, operator differences, or multi-modal strategies. 3) Any comparison with RoboMimic's multi-human (MH) data structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecf24701-f5c4-4697-9d24-54d4e24412fe",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17c6nvJT92sB24JNP4z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "205d9895-e4bf-4611-a36e-6c155c4ce50c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzZchrup7LGs3UkXcxNfng",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 16481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3847,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 32 · 2026-05-13T19:24:27.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MQZzxBbSSLkXvN2szvroGW`</summary>

```json
{
  "query": "RoboMimic multi-human MH dataset multiple operators quality labels better worse proficient"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "205d9895-e4bf-4611-a36e-6c155c4ce50c",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17c6nvJT92sB24JNP4z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6acef2f4-506b-4e07-b38e-c0ca4b03903c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzZchrup7LGs3UkXcxNfng",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 16481,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 16481,
          "cache_creation_input_tokens": 3847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3847,
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

_source line 33 · 2026-05-13T19:24:31.577Z_

<details><summary>↩ Tool result · `toolu_01L9ZhdYVjYzUdFaokbzYkXb`</summary>

```text
# LIBERO Demonstration Collection: Analysis

Based on the provided content, I cannot find answers to your specific questions:

**1. Number of Human Operators:**
The document states demonstrations were "Collected using a SpaceMouse teleoperator at 20 Hz with automatic filtering and validation pipelines" but does **not specify** how many operators participated in this collection effort.

**2. Demonstration Quality Variation:**
No information is provided regarding operator differences, quality variation across operators, or multi-modal strategies employed by different collectors.

**3. RoboMimic Comparison:**
There is **no mention** of RoboMimic or its multi-human data structure anywhere in the content.

## What the Document Does Cover

The content confirms that LIBERO includes "50 high-quality, human-teleoperated demonstrations per task" but focuses on the *technical infrastructure* (HDF5 format storage, automatic validation pipelines) rather than operator-level details or comparative analysis with other benchmarks regarding human data collection strategies.

To address your questions comprehensively, you would need to consult the original LIBERO research papers referenced (particularly Liu et al., 2023, or Wu et al., 2025) rather than this overview document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "205d9895-e4bf-4611-a36e-6c155c4ce50c",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "a32dc0ed-1f4a-4740-b714-2370b11aea23",
  "sourceToolAssistantUUID": "205d9895-e4bf-4611-a36e-6c155c4ce50c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T19:24:33.770Z_

<details><summary>↩ Tool result · `toolu_01MQZzxBbSSLkXvN2szvroGW`</summary>

```text
Web search results for query: "RoboMimic multi-human MH dataset multiple operators quality labels better worse proficient"

Links: [{"title":"robomimic v0.1 (CoRL 2021) — robomimic 0.5 documentation","url":"https://robomimic.github.io/docs/datasets/robomimic_v0.1.html"},{"title":"What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | robomimic","url":"https://robomimic.github.io/study/"},{"title":"robomimic v0.1 (CoRL 2021) — robomimic 0.2.1 documentation","url":"https://robomimic.github.io/docs/v0.2/datasets/robomimic_v0.1.html"},{"title":"robomimic/docs/datasets/robomimic_v0.1.md at master · ARISE-Initiative/robomimic","url":"https://github.com/ARISE-Initiative/robomimic/blob/master/docs/datasets/robomimic_v0.1.md"},{"title":"MimicGen","url":"https://mimicgen.github.io/"},{"title":"What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | SAIL Blog","url":"https://ai.stanford.edu/blog/robomimic/"},{"title":"Towards Effective Utilization of Mixed-Quality Demonstrations in Robotic Manipulation via Segment-Level Selection and Optimization","url":"https://arxiv.org/html/2409.19917v2"},{"title":"robomimic","url":"https://robomimic.github.io/"},{"title":"GitHub - ARISE-Initiative/robomimic: robomimic: A Modular Framework for Robot Learning from Demonstration · GitHub","url":"https://github.com/ARISE-Initiative/robomimic"},{"title":"Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/html/2505.22626v1"}]

Based on the search results, here's what I found about the RoboMimic multi-human (MH) dataset:

## Dataset Overview

The multi-human dataset consists of 300 demonstrations collected from six human operators of varied proficiency, with each operator collecting 50 demonstrations per task.

## Operator Quality Labels

The operators were varied in proficiency – there were 2 "worse" operators, 2 "okay" operators, and 2 "better" operators, resulting in diverse, mixed quality datasets.

## Key Findings

While batch (offline) RL methods are proficient at dealing with mixed quality machine-generated data, they struggle to deal with mixed quality human data. Additionally, methods that make decisions based on history, such as BC-RNN and HBC, outperform other methods on human datasets.

The RoboMimic multi-human dataset has been widely used in research to study how learning algorithms handle data collected from multiple operators with different skill levels. The RoboMimic dataset divides demonstrators into three levels of expertise: better, okay, worse, and labels the demonstrations with the expertise of its demonstrator.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6acef2f4-506b-4e07-b38e-c0ca4b03903c",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "d5fbc57e-95bc-4bf4-a1f6-ee9f62e4013a",
  "sourceToolAssistantUUID": "6acef2f4-506b-4e07-b38e-c0ca4b03903c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-13T19:24:37.063Z_

Now I have a comprehensive picture. Let me do one final check on compute costs for SmolVLA training on LIBERO.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5fbc57e-95bc-4bf4-a1f6-ee9f62e4013a",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17difxGzGkR9eJGFnib",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb26fa13-7c02-4af7-b3c6-07bc6ec8c473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WB57EvNJmeyTkYdX1DnfBg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 20328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1296,
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

_source line 36 · 2026-05-13T19:24:39.326Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0156j6HkfbMr3eeFHHHTJrsz`</summary>

```json
{
  "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632",
  "prompt": "Extract specific compute details: GPU used, training time, batch size, number of steps, memory usage for fine-tuning SmolVLA. What hardware is needed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb26fa13-7c02-4af7-b3c6-07bc6ec8c473",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17difxGzGkR9eJGFnib",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91828c4f-1b33-4ab7-a8fb-e16d38f8ce06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WB57EvNJmeyTkYdX1DnfBg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 20328,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1296
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 20328,
          "cache_creation_input_tokens": 1296,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1296,
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

_source line 37 · 2026-05-13T19:24:47.565Z_

<details><summary>↩ Tool result · `toolu_0156j6HkfbMr3eeFHHHTJrsz`</summary>

```text
# SmolVLA Fine-Tuning Compute Details

## GPU & Hardware
- **GPU Used**: NVIDIA L4 GPU (via Google Colab)
- **Laptop GPU**: NVIDIA RTX 3050 Ti for inference
- **VRAM Required**: "The training required 22 GB of VRAM, which was just about as large as could be fit on this chip."

## Training Parameters
- **Batch Size**: 64
- **Training Steps**: 5,000
- **Learning Rate**: 1e-5
- **Training Time**: Approximately 4 hours on L4 GPU

## Inference Performance
- **Inference Time**: "approximately 10 seconds to compute each chunk" on RTX 3050 Ti laptop GPU
- **Action Chunk Size**: 30 (representing 3 seconds of movement at 10Hz execution frequency)

## Key Takeaway
The author successfully fine-tuned SmolVLA using consumer-grade hardware, demonstrating that "what once required a fully-equipped research lab can now be accomplished by a determined individual with consumer hardware and cloud credits." The work shows feasibility for researchers without access to expensive GPU clusters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91828c4f-1b33-4ab7-a8fb-e16d38f8ce06",
  "isSidechain": true,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "agentId": "a7f0f63bdf2589c2f",
  "type": "user",
  "uuid": "67ee176f-8ed6-4a37-87b7-382529013646",
  "sourceToolAssistantUUID": "91828c4f-1b33-4ab7-a8fb-e16d38f8ce06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-13T19:25:29.260Z_

I now have all the information needed to provide a comprehensive feasibility assessment.

---

## LIBERO + SmolVLA Feasibility Assessment for OT-Consensus Experiments

### 1. Data Availability in LeRobot Format

**Fully available and ready to use.** Multiple LIBERO datasets exist in LeRobot format on HuggingFace:

- Official: `lerobot/libero_10_image`, `lerobot/libero_spatial_image`, `lerobot/libero_goal_image`, `lerobot/libero_object_image`
- Community (cleaned, no-ops removed): `IPEC-COMMUNITY/libero_*_no_noops_1.0.0_lerobot`
- Full 90-task suite: `jesbu1/libero_90_lerobot`
- Official preprocessed: `HuggingFaceVLA/libero`

There is also a pretrained SmolVLA checkpoint specifically for LIBERO: `HuggingFaceVLA/smolvla_libero`. Training commands are documented in the [lerobot LIBERO docs](https://huggingface.co/docs/lerobot/en/libero). Integration is first-class -- `pip install -e ".[libero]"` and you're running.

### 2. CRITICAL BLOCKER: No Multi-Operator / Multi-Strategy Structure

**LIBERO does NOT have the multi-operator demonstration structure that OT-Consensus requires.** This is the key finding:

- LIBERO provides **50 demonstrations per task**, collected via SpaceMouse teleoperation at 20 Hz with automatic filtering and validation.
- The paper and documentation **never specify multiple operators**. The data appears to be collected by a single team/operator with a consistent strategy, then filtered for quality.
- There are **no quality labels** (no "better"/"okay"/"worse" operator tags).
- There are **no strategy labels** or any explicit multi-modal behavior structure.

**Contrast with RoboMimic MH**, which is explicitly designed for multi-operator research:
- RoboMimic MH has **300 demonstrations from 6 operators** (2 "better", 2 "okay", 2 "worse"), each collecting 50 demos per task.
- Demonstrations carry **explicit operator identity and proficiency labels**.
- This is exactly the structure OT-Consensus needs for mode discovery across different demonstrator strategies.

LIBERO's 50 demos per task are high-quality and relatively uniform -- the opposite of what you need to test mode discovery.

### 3. Dataset Scale

| Suite | Tasks | Demos/Task | Total Demos |
|-------|-------|-----------|-------------|
| LIBERO-Spatial | 10 | 50 | 500 |
| LIBERO-Object | 10 | 50 | 500 |
| LIBERO-Goal | 10 | 50 | 500 |
| LIBERO-90 | 90 | 50 | 4,500 |
| LIBERO-Long (libero_10) | 10 | 50 | 500 |
| **Total** | **130** | | **6,500** |

Observations: 7D action space (6D EEF delta + gripper), two camera views (workspace + wrist), 8D proprioceptive state.

### 4. Compute Cost Estimate for 1-2 LIBERO Tasks

Based on confirmed training configs and community reports:

- **SmolVLA on LIBERO**: 100,000 steps, batch size 64
- **Hardware**: 1x RTX 4090 (24GB) is sufficient; an L4 GPU (Google Colab) also works
- **Training time**: ~4-12 hours per fine-tuning run on a single consumer GPU
- **Fine-tuning from pretrained SmolVLA base**: Much cheaper -- one community report did 5,000 steps in ~4 hours on an L4
- **For 1-2 tasks** (50-100 demonstrations): On the lower end, likely 4-6 hours on a single 4090

The compute cost to add 1-2 LIBERO tasks is minimal -- a few GPU-hours.

### 5. Practical Feasibility Verdict

**Technically trivial, scientifically inappropriate for OT-Consensus.**

- Adding LIBERO tasks to a SmolVLA pipeline is straightforward. The datasets are ready, the training pipeline is documented, compute is cheap (single consumer GPU, a few hours).
- **However, LIBERO data lacks the multi-operator/multi-strategy structure that is fundamental to OT-Consensus.** The 50 demos per task appear to come from a single operator or a uniform collection protocol with quality filtering. There are no operator labels, no quality labels, and no known multi-modal behavior in the demonstrations.
- If you ran OT-Consensus on LIBERO data, you would likely find a single mode (or meaningless noise clusters), which would not validate the method's mode discovery capabilities.

### Recommendation

If you want a simulation benchmark with multi-operator structure for OT-Consensus, **stick with RoboMimic MH** (which was designed for exactly this). If you want to add LIBERO for other reasons (e.g., testing SmolVLA policy quality, evaluating transfer, or benchmarking against published VLA numbers), it is cheap and easy to add. But it won't serve the multi-operator mode discovery purpose.

An alternative path: you could **synthetically create multi-strategy LIBERO data** by collecting your own demonstrations with deliberately different strategies (e.g., different grasp approaches, different waypoints), but this requires manual effort and defeats the purpose of using an existing benchmark.

Sources:
- [LeRobot LIBERO Documentation](https://huggingface.co/docs/lerobot/en/libero)
- [LIBERO Paper (NeurIPS 2023)](https://arxiv.org/abs/2306.03310)
- [LIBERO GitHub](https://github.com/Lifelong-Robot-Learning/LIBERO)
- [SmolVLA LIBERO Training Issue #3287](https://github.com/huggingface/lerobot/issues/3287)
- [SmolVLA LIBERO Reproduction Issue #2354](https://github.com/huggingface/lerobot/issues/2354)
- [Fine-Tuning SmolVLA Guide (Medium)](https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632)
- [RoboMimic Multi-Human Dataset](https://robomimic.github.io/docs/datasets/robomimic_v0.1.html)
- [HuggingFaceVLA/smolvla_libero Checkpoint](https://huggingface.co/HuggingFaceVLA/smolvla_libero)
- [LIBERO Datasets on HuggingFace](https://huggingface.co/datasets?search=libero+lerobot)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67ee176f-8ed6-4a37-87b7-382529013646",
  "isSidechain": true,
  "agentId": "a7f0f63bdf2589c2f",
  "requestId": "req_011Cb17ejdXpeGJZGFR78vhF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25093187-86f1-4238-b7ba-f9e7a3eb7855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTx5fpDx4X2QBihFDzWosD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 21624,
      "output_tokens": 1699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 443
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1699,
          "cache_read_input_tokens": 21624,
          "cache_creation_input_tokens": 443,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 443,
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
