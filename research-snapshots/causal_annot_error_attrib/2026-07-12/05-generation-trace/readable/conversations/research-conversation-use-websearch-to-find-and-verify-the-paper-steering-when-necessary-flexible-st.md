# Research conversation: Use WebSearch to find and verify the paper "Steering When Necessary: Flexible Steering Large Language Models with Backtr

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a15bddadf98884943.jsonl`
- **Structured JSON:** [`e2f91ac7db4e5e55b4dc.json`](../../sessions/e2/e2f91ac7db4e5e55b4dc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-16T08:48:02.517Z_

Use WebSearch to find and verify the paper "Steering When Necessary: Flexible Steering Large Language Models with Backtracking" which is claimed to be at NeurIPS 2025 (arxiv 2508.17621). I need to know:
1. Does it exist? (Note: arXiv 2508 means August 2025 submission)
2. Does it use activation-space probing to decide WHEN to apply steering?
3. Does it include a backtracking mechanism?
4. What is its actual intervention granularity (token-level, sentence-level, or something else)?
5. What benchmarks does it evaluate on?
6. Is it actually accepted at NeurIPS 2025?

Search for "Steering When Necessary Flexible Steering Backtracking" and "arxiv 2508.17621" and "FASB activation steering selective". Also search for "flexible activation steering backtracking NeurIPS 2025".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "dc79b3a7-f2ea-4e73-9072-86562132f5fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T08:48:02.520Z_

```json
{
  "parentUuid": "dc79b3a7-f2ea-4e73-9072-86562132f5fa",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
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
  "uuid": "7c95df2f-d217-4591-86be-8caaa8b575d5",
  "timestamp": "2026-05-16T08:48:02.520Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T08:48:06.952Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MPxkjwrjGLxZdKLRGNyazn`</summary>

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
  "parentUuid": "7c95df2f-d217-4591-86be-8caaa8b575d5",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xXE4ZSKhFVbCWLocNq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0196277-8f2d-4c95-be5e-320075de57ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pjn4mAuLcav5YfD18bAwZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 767,
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

### Tool result

_source line 4 · 2026-05-16T08:48:06.957Z_

<details><summary>↩ Tool result · `toolu_01MPxkjwrjGLxZdKLRGNyazn`</summary>

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
  "parentUuid": "e0196277-8f2d-4c95-be5e-320075de57ee",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "2ec8af77-7d8b-481e-9b17-8adf10445aa0",
  "sourceToolAssistantUUID": "e0196277-8f2d-4c95-be5e-320075de57ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T08:48:09.952Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DtUsUi8CgW1ToMX7NEEA72`</summary>

```json
{
  "query": "Steering When Necessary Flexible Steering Backtracking arxiv 2508.17621"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ec8af77-7d8b-481e-9b17-8adf10445aa0",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xXZkEUnRcr9BEvpdht",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e56433d5-4290-4694-9dcd-b2cd2dc74b66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A31Lrc31VgWCtrf8nCAgu6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 6 · 2026-05-16T08:48:10.454Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HMXqBhktxt51iMNqapxbWb`</summary>

```json
{
  "query": "\"arxiv 2508.17621\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e56433d5-4290-4694-9dcd-b2cd2dc74b66",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xXZkEUnRcr9BEvpdht",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd0059d9-6c3a-4b9f-b917-d53483bcb53e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A31Lrc31VgWCtrf8nCAgu6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 7 · 2026-05-16T08:48:10.460Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JLjn5dkvEXbmqTsnBfNvRS`</summary>

```json
{
  "query": "FASB activation steering selective NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd0059d9-6c3a-4b9f-b917-d53483bcb53e",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xXZkEUnRcr9BEvpdht",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63044b9d-0d41-4e57-ac65-6f605a5eb035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A31Lrc31VgWCtrf8nCAgu6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 8 · 2026-05-16T08:48:10.715Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V96fqoXtCkooHyGc7GkogM`</summary>

```json
{
  "query": "flexible activation steering backtracking NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63044b9d-0d41-4e57-ac65-6f605a5eb035",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xXZkEUnRcr9BEvpdht",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f00fc44d-5059-49bd-892a-59505e1faa8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A31Lrc31VgWCtrf8nCAgu6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8990,
      "output_tokens": 211,
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
          "output_tokens": 211,
          "cache_read_input_tokens": 8990,
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

_source line 9 · 2026-05-16T08:48:13.918Z_

<details><summary>↩ Tool result · `toolu_01HMXqBhktxt51iMNqapxbWb`</summary>

```text
Web search results for query: ""arxiv 2508.17621""

Links: [{"title":"[2508.17621] Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/abs/2508.17621"},{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/html/2508.17621"},{"title":"[2306.17621] Transient non-Fourier behavior of large surface bodies","url":"https://arxiv.org/abs/2306.17621"},{"title":"Computer Science Aug 2025","url":"https://www.arxiv.org/list/cs/2025-08?skip=9075&show=25"},{"title":"Complementary Reinforcement Learning","url":"https://arxiv.org/html/2603.17621v1"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2402.17621"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=4500&show=2000"},{"title":"A Combined Feature Embedding Tools for Multi-Class ...","url":"https://arxiv.org/pdf/2411.17621"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1911&show=1000"},{"title":"Computation and Language","url":"https://www.arxiv.org/list/cs.CL/recent?skip=84&show=500"}]

Based on the search results, I found the paper you're looking for:

**"Steering When Necessary: Flexible Steering Large Language Models with Backtracking"** - This paper discusses how large language models have achieved remarkable performance across many generation tasks, though effectively aligning them with desired behaviors remains a significant challenge.

The paper is published on arXiv (arxiv.org/abs/2508.17621) and appears to be from October 2025. The paper discusses activation steering as an effective and cost-efficient approach that directly modifies the activations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd0059d9-6c3a-4b9f-b917-d53483bcb53e",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "1ec93e93-a104-4b6d-a1c3-63c2eecfd88b",
  "sourceToolAssistantUUID": "fd0059d9-6c3a-4b9f-b917-d53483bcb53e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T08:48:14.477Z_

<details><summary>↩ Tool result · `toolu_01JLjn5dkvEXbmqTsnBfNvRS`</summary>

```text
Web search results for query: "FASB activation steering selective NeurIPS 2025"

Links: [{"title":"NeurIPS Poster Angular Steering: Behavior Control via Rotation in Activation Space","url":"https://neurips.cc/virtual/2025/poster/117017"},{"title":"NeurIPS Poster Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/116311"},{"title":"NeurIPS Poster LinEAS: End-to-end Learning of Activation Steering with a Distributional Loss","url":"https://neurips.cc/virtual/2025/poster/119154"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"NeurIPS Activation Steering for Chain-of-Thought Compression","url":"https://neurips.cc/virtual/2025/126680"},{"title":"ExpertLens: Activation Steering Features Are Highly Interpretable - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/expertlens-activation"},{"title":"NeurIPS Poster LayerNavigator: Finding Promising Intervention Layers for Efficient Activation Steering in Large Language Models","url":"https://neurips.cc/virtual/2025/poster/115305"},{"title":"LayerNavigator: Finding Promising Intervention Layers for Efficient Activation Steering in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=wj4lM45xQR"},{"title":"[2508.17621] Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/abs/2508.17621"},{"title":"NeurIPS Steering Large Language Models using Conceptors: Improving Addition-Based Activation Engineering","url":"https://neurips.cc/virtual/2024/104080"}]

Based on the search results, I found relevant information about FASB and activation steering at NeurIPS 2025:

## FASB Framework at NeurIPS 2025

The Flexible Activation Steering with Backtracking (FASB) framework dynamically determines both the necessity and strength of intervention by tracking the internal states of the LLMs during generation, considering both the question and the generated content.

Existing methods typically indiscriminately intervene to all generations or rely solely on the question to determine intervention, which limits the accurate assessment of the intervention strength. FASB addresses this limitation by providing a more selective approach.

Additionally, the backtracking mechanism can correct deviated tokens and steer the LLMs toward the desired behavior when intervention is needed during generation.

The framework was presented at NeurIPS 2025 and represents an advancement in activation steering that enables more targeted and adaptive control of language model behavior during inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63044b9d-0d41-4e57-ac65-6f605a5eb035",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "114fae33-4426-490d-8103-d8d5a315f294",
  "sourceToolAssistantUUID": "63044b9d-0d41-4e57-ac65-6f605a5eb035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T08:48:16.177Z_

<details><summary>↩ Tool result · `toolu_01DtUsUi8CgW1ToMX7NEEA72`</summary>

```text
Web search results for query: "Steering When Necessary Flexible Steering Backtracking arxiv 2508.17621"

Links: [{"title":"[2508.17621] Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/abs/2508.17621"},{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/html/2508.17621"},{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking | OpenReview","url":"https://openreview.net/forum?id=l75RyRcevf"},{"title":"Controllable LLM Reasoning via Sparse Autoencoder‑Based Steering","url":"https://arxiv.org/html/2601.03595"},{"title":"NeurIPS Poster Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/116311"},{"title":"Vector Steering Intervention in Neural Models","url":"https://www.emergentmind.com/topics/vector-steering-intervention"},{"title":"SREENIVASA INSTITUTE OF TECHNOLOGY AND MANAGEMENT STUDIES (AUTONOMOUS)","url":"https://sitams.ac.in/wp-content/uploads/2026/03/AI-Notes.pdf"},{"title":"A Unified Understanding and Evaluation of Steering Methods","url":"https://arxiv.org/html/2502.02716v2"},{"title":"(PDF) A Unified Understanding and Evaluation of Steering Methods","url":"https://www.researchgate.net/publication/388754740_A_Unified_Understanding_and_Evaluation_of_Steering_Methods"},{"title":"Distributed Intelligent Object Based Control System for ...","url":"http://www.hbni.ac.in/phdthesis/engg/ENGG03200704001.pdf"}]

Based on the search results, here's what I found about the paper arxiv 2508.17621:

## Paper Overview

The paper is titled "Steering When Necessary: Flexible Steering Large Language Models with Backtracking" by Zifeng Cheng and 7 other authors.

## Main Contribution

The paper proposes the Flexible Activation Steering with Backtracking (FASB) framework, which dynamically determines both the necessity and strength of intervention by tracking the internal states of the LLMs during generation, considering both the question and the generated content.

## Problem Addressed

Activation steering is an effective and cost-efficient approach that directly modifies the activations of LLMs during the inference stage. However, existing methods typically indiscriminately intervene to all generations or rely solely on the question to determine intervention, which limits the accurate assessment of the intervention strength.

## Key Innovation

The paper proposes a backtracking mechanism to correct the deviated tokens and steer the LLMs toward the desired behavior, since intervening after detecting a deviation from the desired behavior is often too late.

## Results

Extensive experiments on the TruthfulQA dataset and six multiple-choice datasets demonstrate that their method outperforms baselines.

The paper was submitted on August 25, 2025, with a revised version on October 1, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e56433d5-4290-4694-9dcd-b2cd2dc74b66",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "7e6883d9-e7ae-4145-bdf0-43ad22101429",
  "sourceToolAssistantUUID": "e56433d5-4290-4694-9dcd-b2cd2dc74b66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T08:48:17.631Z_

<details><summary>↩ Tool result · `toolu_01V96fqoXtCkooHyGc7GkogM`</summary>

```text
Web search results for query: "flexible activation steering backtracking NeurIPS 2025"

Links: [{"title":"NeurIPS Poster Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/116311"},{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking | OpenReview","url":"https://openreview.net/forum?id=l75RyRcevf"},{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/html/2508.17621v2"},{"title":"ExpertLens: Activation Steering Features Are Highly Interpretable - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/expertlens-activation"},{"title":"[2508.17621] Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/abs/2508.17621"},{"title":"NeurIPS Poster Angular Steering: Behavior Control via Rotation in Activation Space","url":"https://neurips.cc/virtual/2025/poster/117017"},{"title":"NeurIPS Activation Steering for Chain-of-Thought Compression","url":"https://neurips.cc/virtual/2025/126680"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"NeurIPS Poster LinEAS: End-to-end Learning of Activation Steering with a Distributional Loss","url":"https://neurips.cc/virtual/2025/poster/119154"},{"title":"NeurIPS Poster LayerNavigator: Finding Promising Intervention Layers for Efficient Activation Steering in Large Language Models","url":"https://neurips.cc/virtual/2025/poster/115305"}]

I found several search results for "flexible activation steering backtracking NeurIPS 2025". Here are the key findings:

## Main Result

The paper "Steering When Necessary: Flexible Steering Large Language Models with Backtracking" was presented as a poster at NeurIPS 2025 by Zifeng Cheng, Jinwei Gan, Zhiwei Jiang, Cong Wang, Yafeng Yin, Xiang Luo, Yuchen Fu, and Qing Gu.

## Framework Overview

Activation steering is an effective and cost-efficient approach that directly modifies the activations of LLMs during the inference stage, aligning their responses with the desired behaviors and avoiding the high cost of fine-tuning.

The Flexible Activation Steering with Backtracking (FASB) framework dynamically determines both the necessity and strength of intervention by tracking the internal state of the LLMs during generation.

## Key Innovation

Existing methods typically indiscriminately intervene to all generations or rely solely on the question to determine intervention, which limits the accurate assessment of the intervention strength. The FASB framework addresses this limitation.

The approach proposes a backtracking mechanism to step back a few tokens in order to apply intervention and regenerate them, allowing for more targeted and effective steering during generation.

## Evaluation

Extensive experiments were conducted on the TruthfulQA dataset and six multiple-choice datasets to demonstrate the effectiveness of the method.

You can find the full paper on OpenReview and arXiv for more detailed information about the methodology and results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f00fc44d-5059-49bd-892a-59505e1faa8a",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "5a22ec34-d9e8-403d-8b5a-c9eaa4130aff",
  "sourceToolAssistantUUID": "f00fc44d-5059-49bd-892a-59505e1faa8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-16T08:48:20.141Z_

Now let me get more details about the paper's methodology and benchmarks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a22ec34-d9e8-403d-8b5a-c9eaa4130aff",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xYLbVQPMsVPw1YRJLe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a4c56c6-5c77-4c0a-b41d-af8777d914a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2v4axHDbkGxf32hypFTup",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3261,
      "cache_read_input_tokens": 10382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3261,
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

_source line 14 · 2026-05-16T08:48:21.073Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016oo9EZyQZzmbvtXotNjmHH`</summary>

```json
{
  "query": "arxiv 2508.17621 FASB token-level intervention granularity TruthfulQA multiple choice datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a4c56c6-5c77-4c0a-b41d-af8777d914a0",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xYLbVQPMsVPw1YRJLe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7855853a-9a85-43b1-81d6-39d7efa87461",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2v4axHDbkGxf32hypFTup",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3261,
      "cache_read_input_tokens": 10382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3261,
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

_source line 15 · 2026-05-16T08:48:21.536Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019LDjZKtXvgPu3BJL1SXrAq`</summary>

```json
{
  "query": "site:openreview.net \"Steering When Necessary\" l75RyRcevf NeurIPS 2025 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7855853a-9a85-43b1-81d6-39d7efa87461",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xYLbVQPMsVPw1YRJLe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f21a143-0488-4863-89d7-f94a22733db3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2v4axHDbkGxf32hypFTup",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3261,
      "cache_read_input_tokens": 10382,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3261
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 10382,
          "cache_creation_input_tokens": 3261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3261,
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

_source line 16 · 2026-05-16T08:48:25.471Z_

<details><summary>↩ Tool result · `toolu_019LDjZKtXvgPu3BJL1SXrAq`</summary>

```text
Web search results for query: "site:openreview.net "Steering When Necessary" l75RyRcevf NeurIPS 2025 accepted"

No links found.

The search didn't return any results. This could mean that either the paper with that specific ID doesn't match those exact search terms, or the paper may not be publicly indexed yet on search engines. 

If you're looking for a specific paper on OpenReview, you might try:
1. Searching directly on openreview.net for "Steering When Necessary"
2. Using just the paper ID (l75RyRcevf) without other terms
3. Checking if the paper was actually accepted to NeurIPS 2025 (acceptance decisions and papers may not be fully published yet)

Would you like me to try a different search approach, such as searching for just the paper title or just the paper ID?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f21a143-0488-4863-89d7-f94a22733db3",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "f08900ff-9eb0-45e1-894c-ad820ee5c7d5",
  "sourceToolAssistantUUID": "7f21a143-0488-4863-89d7-f94a22733db3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T08:48:27.597Z_

<details><summary>↩ Tool result · `toolu_016oo9EZyQZzmbvtXotNjmHH`</summary>

```text
Web search results for query: "arxiv 2508.17621 FASB token-level intervention granularity TruthfulQA multiple choice datasets"

Links: [{"title":"[2508.17621] Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/abs/2508.17621"},{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/html/2508.17621"},{"title":"LayerCake: Token-Aware Contrastive Decoding within Large Language Model Layers","url":"https://arxiv.org/html/2507.04404v1"},{"title":"Multi-Attribute Steering of Language Models via Targeted Intervention","url":"https://arxiv.org/html/2502.12446"},{"title":"Fact-Checking the Output of Large Language Models via Token-Level Uncertainty Quantification","url":"https://arxiv.org/html/2403.04696v2"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=1875&show=2000"},{"title":"Retrieval-augmented Decoding for Improving Truthfulness in Open-ended Generation","url":"https://arxiv.org/html/2508.02184"},{"title":"Improve Decoding Factuality by Token-wise Cross Layer Entropy of Large","url":"https://arxiv.org/pdf/2502.03199"},{"title":"TASE: Token Awareness and Structured Evaluation for Multilingual Language Models","url":"https://arxiv.org/html/2508.05468"},{"title":"[2508.12811] Next Visual Granularity Generation","url":"https://arxiv.org/abs/2508.12811"}]

Based on the search results, I found the paper you're looking for. Here's the information about arxiv 2508.17621:

## Paper Overview

The paper is titled "Steering When Necessary: Flexible Steering Large Language Models with Backtracking"

## Key Contributions

The paper proposes the Flexible Activation Steering with Backtracking (FASB) framework, which dynamically determines both the necessity and strength of intervention by tracking the internal states of the LLMs during generation, considering both the question and the generated content.

Since intervening after detecting a deviation from the desired behavior is often too late, the authors further propose the backtracking mechanism to correct the deviated tokens and steer the LLMs toward the desired behavior.

## Evaluation

The authors conduct extensive experiments on the TruthfulQA dataset and six multiple-choice datasets to demonstrate the effectiveness of their method.

The paper addresses a key limitation in existing activation steering methods: existing methods typically indiscriminately intervene to all generations or rely solely on the question to determine intervention, which limits the accurate assessment of the intervention strength.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7855853a-9a85-43b1-81d6-39d7efa87461",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "2882d8ef-06fa-4705-a791-0390eca89a14",
  "sourceToolAssistantUUID": "7855853a-9a85-43b1-81d6-39d7efa87461",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T08:48:30.297Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012T6spxXjukB1d3QNMZVzcy`</summary>

```json
{
  "query": "openreview.net l75RyRcevf \"Steering When Necessary\" decision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2882d8ef-06fa-4705-a791-0390eca89a14",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xZ5E3uMdCecg9NLNX2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba86fd22-1d61-4e10-99df-751c350e20ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRXKrgN1NCFnN7qZNz62Zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 255,
      "cache_creation_input_tokens": 901,
      "cache_read_input_tokens": 13643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 901,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 19 · 2026-05-16T08:48:30.868Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XcZWnwkWjnKURRzJY9gDkv`</summary>

```json
{
  "query": "\"Steering When Necessary\" FASB \"activation probing\" OR \"probe\" OR \"classifier\" token-level intervention mechanism"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba86fd22-1d61-4e10-99df-751c350e20ae",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xZ5E3uMdCecg9NLNX2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55940416-2de8-4764-8b1a-7fc6a646f689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRXKrgN1NCFnN7qZNz62Zw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 255,
      "cache_creation_input_tokens": 901,
      "cache_read_input_tokens": 13643,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 901
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 255,
          "output_tokens": 134,
          "cache_read_input_tokens": 13643,
          "cache_creation_input_tokens": 901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 901,
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

_source line 20 · 2026-05-16T08:48:33.519Z_

<details><summary>↩ Tool result · `toolu_012T6spxXjukB1d3QNMZVzcy`</summary>

```text
Web search results for query: "openreview.net l75RyRcevf "Steering When Necessary" decision"

Links: [{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking | OpenReview","url":"https://openreview.net/forum?id=l75RyRcevf"}]

I found the paper! The paper proposes the Flexible Activation Steering with Backtracking (FASB) framework, which dynamically determines both the necessity and strength of intervention by tracking the internal states of LLMs during generation, considering both the question and the generated content.

Activation steering is an effective and cost-efficient approach that directly modifies the activations of LLMs during the inference stage, aligning their responses with the desired behaviors and avoiding the high cost of fine-tuning. Existing methods typically indiscriminately intervene to all generations or rely solely on the question to determine intervention, which limits the accurate assessment of the intervention strength.

The framework further proposes a backtracking mechanism to correct deviated tokens and steer the LLMs toward the desired behavior. Extensive experiments on the TruthfulQA dataset and six multiple-choice datasets demonstrate that the method outperforms baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba86fd22-1d61-4e10-99df-751c350e20ae",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "1c11e43e-349c-4c03-b8f5-0293f701891a",
  "sourceToolAssistantUUID": "ba86fd22-1d61-4e10-99df-751c350e20ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T08:48:38.044Z_

<details><summary>↩ Tool result · `toolu_01XcZWnwkWjnKURRzJY9gDkv`</summary>

```text
Web search results for query: ""Steering When Necessary" FASB "activation probing" OR "probe" OR "classifier" token-level intervention mechanism"

Links: [{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/html/2508.17621"},{"title":"Activation Steering in LLMs","url":"https://www.emergentmind.com/topics/activation-steering-method"},{"title":"Steering Awareness: Models Can Be Trained to Detect Activation Steering","url":"https://arxiv.org/html/2511.21399v2"},{"title":"Activation Steering With Mean Response Probes : A Case Study In Suppressing Sycophancy In Language Models During TTC","url":"https://huggingface.co/blog/TensorSlay/activation-steering-with-mean-response-probes"},{"title":"Vector Steering Intervention in Neural Models","url":"https://www.emergentmind.com/topics/vector-steering-intervention"},{"title":"ACTIVATION STEERING VIA GENERATIVE CAUSAL MEDIATION","url":"https://openreview.net/pdf/a041b1716bc888e0dd914c089c581a12e13b61d5.pdf"},{"title":"Do Large Language Models Plan Answer Positions? Position Bias in Multiple-Choice Question Generation","url":"https://arxiv.org/html/2605.01846"},{"title":"SteerVLM: Robust Model Control through Lightweight ...","url":"https://aclanthology.org/2025.findings-emnlp.1285.pdf"},{"title":"Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering","url":"https://arxiv.org/html/2601.19847v1"},{"title":"Steering Awareness: Models Can Be Trained to Detect ...","url":"https://www.lesswrong.com/posts/D7zQkrDjAKaa293EA/steering-awareness-models-can-be-trained-to-detect"}]

Based on the search results, I found comprehensive information about "Steering When Necessary" (FASB) and its token-level intervention mechanism:

## Overview

The "Flexible Activation Steering with Backtracking" (FASB) framework dynamically determines both the necessity and strength of intervention by tracking the internal states of LLMs during generation, considering both the question and the generated content.

## Activation Probing and Classifier

FASB employs two methods to identify internal states that are consistent with the desired behavior and derive the steering vector and classifier for state tracking. The framework uses the Probe method to identify attention heads and induce the classifiers and steering vectors, with an alternative Prototype method presented in the appendix.

## Token-Level Intervention Mechanism

The backtracking mechanism steps back a few tokens and performs activation steering to regenerate them, steering the generation toward the desired direction, with the intervention strength determined by the classifier. The classifier is used for state tracking to determine whether intervention is necessary and to adaptively set intervention strength.

## Key Innovation

FASB can dynamically determine whether intervention is necessary and the intervention strength based on the degree of deviation in the generation. This addresses a key limitation of prior approaches: Considering that intervening after detecting a deviation from the desired behavior is often too late, the backtracking mechanism was proposed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55940416-2de8-4764-8b1a-7fc6a646f689",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "70eb3687-9e1b-4adf-8183-779e2633c138",
  "sourceToolAssistantUUID": "55940416-2de8-4764-8b1a-7fc6a646f689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T08:48:47.615Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015mRg8eYadaM3ws6JpR6y9t`</summary>

```json
{
  "query": "neurips.cc 2025 poster 116311 \"Steering When Necessary\" accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70eb3687-9e1b-4adf-8183-779e2633c138",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xZqs9r8gDVeHFT4CdK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71bded65-4977-4d03-adc4-968f0c79e200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MatzpD6vAURs5JmFyMYTYh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 14544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 23 · 2026-05-16T08:48:48.309Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0138ve9iqLpM15pvj7iyCsNY`</summary>

```json
{
  "query": "\"Steering When Necessary\" FASB \"six multiple-choice datasets\" benchmark names MMLU ARC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71bded65-4977-4d03-adc4-968f0c79e200",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xZqs9r8gDVeHFT4CdK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d046223-cd4c-4097-ad88-943e24066bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MatzpD6vAURs5JmFyMYTYh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 14544,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1565
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 14544,
          "cache_creation_input_tokens": 1565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1565,
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

_source line 24 · 2026-05-16T08:48:50.685Z_

<details><summary>↩ Tool result · `toolu_015mRg8eYadaM3ws6JpR6y9t`</summary>

```text
Web search results for query: "neurips.cc 2025 poster 116311 "Steering When Necessary" accepted"

Links: [{"title":"NeurIPS Poster Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://neurips.cc/virtual/2025/poster/116311"}]

Based on the search results, I found the NeurIPS 2025 poster you're looking for. The poster presents work on large language models, addressing the challenge of aligning them with desired behaviors through activation steering—an approach that directly modifies the activations of LLMs during inference to align responses with desired behaviors while avoiding the high cost of fine-tuning.

The paper proposes the Flexible Activation Steering with Backtracking (FASB) framework, which dynamically determines both the necessity and strength of intervention by tracking the internal states of the LLMs during generation.

The poster is available at: https://neurips.cc/virtual/2025/poster/116311


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71bded65-4977-4d03-adc4-968f0c79e200",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "d14c18da-c41f-40c3-9e87-dc909a0513cc",
  "sourceToolAssistantUUID": "71bded65-4977-4d03-adc4-968f0c79e200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T08:48:54.367Z_

<details><summary>↩ Tool result · `toolu_0138ve9iqLpM15pvj7iyCsNY`</summary>

```text
Web search results for query: ""Steering When Necessary" FASB "six multiple-choice datasets" benchmark names MMLU ARC"

Links: [{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/html/2508.17621"},{"title":"[2508.17621] Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/abs/2508.17621"},{"title":"Training on the Test Task Confounds Evaluation and Emergence","url":"https://arxiv.org/pdf/2407.07890"},{"title":"What is MMLU? LLM Benchmark Explained and Why It Matters | DataCamp","url":"https://www.datacamp.com/blog/what-is-mmlu"},{"title":"A Simple Method to Make Multiple Choice Benchmarks ...","url":"https://aclanthology.org/2025.acl-short.94.pdf"},{"title":"Fasb","url":"https://www.fasb.org/standards/accounting-standard-updates"},{"title":"cais/mmlu · Datasets at Hugging Face","url":"https://huggingface.co/datasets/cais/mmlu"},{"title":"When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards","url":"https://arxiv.org/html/2402.01781"},{"title":"MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark","url":"https://arxiv.org/html/2406.01574v4"},{"title":"Improving Model Evaluation using SMART Filtering of Benchmark Datasets","url":"https://arxiv.org/html/2410.20245v2"}]

Based on the search results, I found information about the "Steering When Necessary" paper with the FASB framework. Here are the key findings:

## The Six Multiple-Choice Datasets

The paper evaluated FASB on six multiple-choice datasets: COPA (Gordon et al., 2012), StoryCloze (Mostafazadeh et al., 2016), NLI (Bowman et al., 2015), MMLU (Hendrycks et al., 2021), SST2 (Socher et al., 2013), and Winogrande (Sakaguchi et al., 2020).

So to clarify: **ARC is not one of the six datasets** used in the "Steering When Necessary" paper. The six benchmarks are COPA, StoryCloze, NLI, MMLU, SST2, and Winogrande. MMLU is the only one from your list that appears in this paper.

The paper's focus was on the Flexible Activation Steering with Backtracking (FASB) framework, which dynamically determines both the necessity and strength of intervention by tracking the internal states of LLMs during generation, considering both the question and the generated content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d046223-cd4c-4097-ad88-943e24066bae",
  "isSidechain": true,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "agentId": "a15bddadf98884943",
  "type": "user",
  "uuid": "ebb35c1d-ccc8-465b-b2f8-5c4c615a2fd9",
  "sourceToolAssistantUUID": "6d046223-cd4c-4097-ad88-943e24066bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-16T08:49:10.961Z_

Based on my comprehensive search, here are the findings for each of your questions:

---

## Results for "Steering When Necessary: Flexible Steering Large Language Models with Backtracking" (arXiv 2508.17621)

### 1. Does it exist?

**Yes.** The paper exists at arXiv 2508.17621, submitted August 25, 2025, with a revised version on October 1, 2025. The authors are Zifeng Cheng, Jinwei Gan, Zhiwei Jiang, Cong Wang, Yafeng Yin, Xiang Luo, Yuchen Fu, and Qing Gu. Since arXiv 2508 corresponds to August 2025 submissions, the timeline is consistent.

### 2. Does it use activation-space probing to decide WHEN to apply steering?

**Yes.** FASB uses a probe-based classifier trained on internal activation states (specifically attention heads) to dynamically determine whether intervention is necessary at any given point in generation. The classifier tracks the internal states of the LLM during generation, considering both the question and the generated content so far, to assess whether the model is deviating from desired behavior. This is explicitly called the "Probe method" in the paper.

### 3. Does it include a backtracking mechanism?

**Yes.** The paper explicitly proposes a backtracking mechanism. The key insight is that intervening *after* detecting a deviation is often too late. So when deviation is detected, the mechanism "steps back a few tokens" and then performs activation steering to regenerate those tokens, steering generation toward the desired direction.

### 4. What is its actual intervention granularity?

**Token-level.** The intervention operates at the token level. The classifier monitors internal states during token-by-token generation and determines both *whether* to intervene and the *strength* of intervention. The backtracking mechanism steps back a specific number of tokens to regenerate them with steering applied. The intervention strength is adaptively set based on the degree of deviation detected by the classifier.

### 5. What benchmarks does it evaluate on?

The paper evaluates on **7 benchmarks total**:
- **TruthfulQA** (the primary evaluation dataset)
- **Six multiple-choice datasets**: COPA, StoryCloze, NLI (SNLI/Bowman et al.), MMLU, SST2, and Winogrande

### 6. Is it actually accepted at NeurIPS 2025?

**Yes.** The paper was accepted as a poster at NeurIPS 2025 in San Diego. It has:
- A NeurIPS virtual poster page at `neurips.cc/virtual/2025/poster/116311`
- An OpenReview page at `openreview.net/forum?id=l75RyRcevf`

This is confirmed -- it is a legitimate NeurIPS 2025 poster paper.

---

Sources:
- [arXiv paper page](https://arxiv.org/abs/2508.17621)
- [arXiv HTML version](https://arxiv.org/html/2508.17621)
- [OpenReview page](https://openreview.net/forum?id=l75RyRcevf)
- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/116311)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebb35c1d-ccc8-465b-b2f8-5c4c615a2fd9",
  "isSidechain": true,
  "agentId": "a15bddadf98884943",
  "requestId": "req_011Cb5xb3drjzUNrCGULNL7D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baab2676-a7c8-4278-b6b1-5085b19c3588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0187NPeTX3gBp8VBJCNADCxV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 16109,
      "output_tokens": 803,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1170
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 803,
          "cache_read_input_tokens": 16109,
          "cache_creation_input_tokens": 1170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1170,
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
