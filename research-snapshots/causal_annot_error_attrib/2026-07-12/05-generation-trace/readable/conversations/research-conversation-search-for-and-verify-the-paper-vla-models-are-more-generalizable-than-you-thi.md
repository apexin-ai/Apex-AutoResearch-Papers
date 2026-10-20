# Research conversation: Search for and verify the paper "VLA Models Are More Generalizable Than You Think" (arXiv 2512.02902) which describes Fe

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ad4938e7e2fc02063.jsonl`
- **Structured JSON:** [`f461be0975f5c65da786.json`](../../sessions/f4/f461be0975f5c65da786.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-14T06:11:22.275Z_

Search for and verify the paper "VLA Models Are More Generalizable Than You Think" (arXiv 2512.02902) which describes Feature Token Modulation (FTM). I need to verify:
1. Does this paper exist and what are its exact claims?
2. Does FTM really achieve 87.1% viewpoint robustness on LIBERO with only 4K parameters?
3. Is FTM really "input-independent" (same affine transformation for all inputs)?
4. What model does it use (π0.5)?
5. What are its limitations as stated by the authors?

Use WebSearch and WebFetch to find and read this paper. Report the exact numbers and methodology. Be thorough - read the actual paper abstract and key sections, don't just rely on search snippets.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ad4938e7e2fc02063",
  "type": "user",
  "uuid": "efc1201c-8bab-4e84-aeb9-c5b659dd007a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T06:11:22.278Z_

```json
{
  "parentUuid": "efc1201c-8bab-4e84-aeb9-c5b659dd007a",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
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
      "TodoWrite",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "98887ce1-fcb1-4415-8d50-e92078dc0fb1",
  "timestamp": "2026-05-14T06:11:22.278Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T06:11:24.344Z_



I'll search for this paper and verify the claims. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98887ce1-fcb1-4415-8d50-e92078dc0fb1",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xxTg3QdU5brB4HPeHC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ff8d229-d352-4290-88c2-5e2ba483825e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VbuZ9r7a8UCUHaYfDveMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8956,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8956,
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

_source line 4 · 2026-05-14T06:11:24.765Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DaBBEUGLBPg3Ls7PRp4bka`</summary>

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
  "parentUuid": "3ff8d229-d352-4290-88c2-5e2ba483825e",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xxTg3QdU5brB4HPeHC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a337285-919c-4afd-a699-84445786ff52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VbuZ9r7a8UCUHaYfDveMR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8956,
      "cache_read_input_tokens": 0,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8956,
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

_source line 5 · 2026-05-14T06:11:24.770Z_

<details><summary>↩ Tool result · `toolu_01DaBBEUGLBPg3Ls7PRp4bka`</summary>

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
  "parentUuid": "0a337285-919c-4afd-a699-84445786ff52",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ad4938e7e2fc02063",
  "type": "user",
  "uuid": "3c9c2fe5-c295-4ed6-9315-7e26cc64b397",
  "sourceToolAssistantUUID": "0a337285-919c-4afd-a699-84445786ff52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T06:11:27.831Z_



Now let me search for this paper and fetch the actual arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c9c2fe5-c295-4ed6-9315-7e26cc64b397",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xxf9rgRTKMnU2BDtPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afeab16b-0010-4175-b238-52cded973ef1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQ6pFjnRGrHSnAMLLw6d1d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-14T06:11:28.787Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019aMAhCNBkhsykMXGmqJPQ7`</summary>

```json
{
  "query": "arXiv 2512.02902 \"VLA Models Are More Generalizable Than You Think\" Feature Token Modulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afeab16b-0010-4175-b238-52cded973ef1",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xxf9rgRTKMnU2BDtPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "559517a3-c1c7-4911-89c8-4630077b4d2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQ6pFjnRGrHSnAMLLw6d1d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-14T06:11:29.113Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AoMLjM8QT8MhuFh2fzaLLk`</summary>

```json
{
  "query": "\"Feature Token Modulation\" FTM VLA robustness LIBERO pi0.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "559517a3-c1c7-4911-89c8-4630077b4d2f",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xxf9rgRTKMnU2BDtPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b19646ea-2644-41e7-a603-4b319a698476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQ6pFjnRGrHSnAMLLw6d1d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8956,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 153,
          "cache_read_input_tokens": 8956,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-14T06:11:33.204Z_

<details><summary>↩ Tool result · `toolu_01AoMLjM8QT8MhuFh2fzaLLk`</summary>

```text
Web search results for query: ""Feature Token Modulation" FTM VLA robustness LIBERO pi0.5"

Links: [{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/html/2512.02902"}]

Based on the web search results, here's what I found:

Feature Token Modulation (FTM) applies a global affine transformation to visual tokens and improves LIBERO viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. 

The FTM variant achieves an average success rate of 87.2%, closely approaching the π₀ baseline (83.6%) despite updating only a pair of global affine parameters.

These results reveal substantial untapped robustness in pretrained VLA models and demonstrate that targeted, minimal visual adaptation is sufficient to restore viewpoint generalization. This method was developed as part of research addressing how Vision-Language-Action (VLA) models can be made more robust to novel camera viewpoints and visual perturbations while maintaining parameter efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b19646ea-2644-41e7-a603-4b319a698476",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ad4938e7e2fc02063",
  "type": "user",
  "uuid": "dee79f04-9e6a-492c-98fd-5984d0b44a61",
  "sourceToolAssistantUUID": "b19646ea-2644-41e7-a603-4b319a698476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T06:11:35.841Z_

<details><summary>↩ Tool result · `toolu_019aMAhCNBkhsykMXGmqJPQ7`</summary>

```text
Web search results for query: "arXiv 2512.02902 "VLA Models Are More Generalizable Than You Think" Feature Token Modulation"

Links: [{"title":"[2512.02902] VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/abs/2512.02902"},{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/html/2512.02902"},{"title":"awesome-daily-AI-arxiv/hot_topic/Embodied_AI.md at main · Tavish9/awesome-daily-AI-arxiv","url":"https://github.com/Tavish9/awesome-daily-AI-arxiv/blob/main/hot_topic/Embodied_AI.md"},{"title":"Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.09927"},{"title":"When LLaVA Meets Objects: Token Composition for Vision-Language-Models","url":"https://arxiv.org/html/2602.04864v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"[2512.18496] Adaptive-VoCo: Complexity-Aware Visual Token Compression for Vision-Language Models","url":"https://arxiv.org/abs/2512.18496"},{"title":"TokenFLEX: Unified VLM Training for Flexible Visual Tokens Inference","url":"https://arxiv.org/html/2504.03154v1"},{"title":"[2512.09927] Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2512.09927"},{"title":"Adaptive-VoCo: Complexity-Aware Visual Token Compression for Vision-Language Models","url":"https://arxiv.org/html/2512.18496"}]

Based on the search results, here's information about arXiv paper 2512.02902:

## Overview

The paper "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling" (arXiv:2512.02902) addresses how Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations.

## Key Finding

The research shows that this brittleness primarily arises from misalignment in Spatial Modeling, rather than Physical Modeling.

## Feature Token Modulation (FTM) Method

The first method, Feature Token Modulation (FTM), applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Specifically, FTM applies a global affine transformation to visual token embeddings using only two learnable parameter vectors, which re-scales and re-centers feature distributions, allowing the model to adapt rapidly to new visual domains.

## Proposed Framework

To address this brittleness, the authors propose a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates. Building on FTM, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters—matching LoRA-scale finetuning at far lower cost.

The paper was submitted on December 2, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "559517a3-c1c7-4911-89c8-4630077b4d2f",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ad4938e7e2fc02063",
  "type": "user",
  "uuid": "96507d79-dd17-48cd-ac78-d2d3830aacfb",
  "sourceToolAssistantUUID": "559517a3-c1c7-4911-89c8-4630077b4d2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-14T06:11:38.690Z_

Good, the paper exists. Now let me fetch the actual paper content to verify specific claims in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96507d79-dd17-48cd-ac78-d2d3830aacfb",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xyTjYNWE3kJT6LJeet",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d198077-bb63-46b2-93ca-d5b305745d66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsNzkgW7X4VytKbkpQMrNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 306,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 10866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
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

_source line 12 · 2026-05-14T06:11:41.294Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X8TtbBLqRdH98dQS9YawxD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.02902",
  "prompt": "Extract the complete abstract, the list of authors, the submission date, and any key claims about Feature Token Modulation (FTM), Feature Linear Adaptation (FLA), parameter counts, accuracy numbers, and the base model used (pi0, pi0.5, or other). Also extract any mentions of \"input-independent\" or how FTM works mechanically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d198077-bb63-46b2-93ca-d5b305745d66",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xyTjYNWE3kJT6LJeet",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dbed4c1-364e-4be9-9e0c-90bd7b7957c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsNzkgW7X4VytKbkpQMrNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 306,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 10866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
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

_source line 13 · 2026-05-14T06:11:44.734Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V56KYL6QqddpZud4ZCv4Z6`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.02902",
  "prompt": "Extract the following information in detail: 1) The full abstract. 2) What base VLA model is used (pi0, pi0.5, OpenVLA, or other)? 3) Exact FTM methodology - is it described as 'input-independent'? Does the same affine transformation apply to all inputs? 4) The exact numbers: FTM parameter count (4K?), viewpoint robustness on LIBERO (87.1%?), baseline numbers. 5) FLA details and numbers. 6) The Limitations section - what do the authors say are limitations of their work? 7) Any discussion of Physical Modeling vs Spatial Modeling distinction. 8) What datasets and benchmarks are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dbed4c1-364e-4be9-9e0c-90bd7b7957c2",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xyTjYNWE3kJT6LJeet",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36e385f4-a953-4d76-a971-1601e39c81db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsNzkgW7X4VytKbkpQMrNd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 306,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 10866,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1076
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 306,
          "output_tokens": 411,
          "cache_read_input_tokens": 10866,
          "cache_creation_input_tokens": 1076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1076,
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

_source line 14 · 2026-05-14T06:11:46.902Z_

<details><summary>↩ Tool result · `toolu_01X8TtbBLqRdH98dQS9YawxD`</summary>

```text
# Research Paper Summary

**Title:** VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling

**Authors:** Weiqi Li, Quande Zhang, Ruifeng Zhai, Liang Lin, Guangrun Wang

**Submission Date:** December 2, 2025 (v1); revised March 31, 2026 (v2)

## Abstract
The authors demonstrate that vision-language-action models experience brittleness primarily due to spatial misalignment rather than physical modeling issues. They propose "a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates."

## Key Technical Findings

**Feature Token Modulation (FTM):**
- Employs "a global affine transformation to visual tokens"
- Parameter count: 4K parameters only
- Performance: Improves Libero viewpoint accuracy from 48.5% to 87.1%

**Feature Linear Adaptation (FLA):**
- Introduces low-rank updates to the ViT encoder
- Parameter count: 4.7M parameters
- Performance: Achieves 90.8% success rate
- Matches LoRA-scale finetuning effectiveness "at far lower cost"

## Notable Claims
The research reveals "substantial untapped robustness in pretrained VLA models" and indicates that "targeted, minimal visual adaptation is sufficient to restore viewpoint generalization."

**Note:** The page does not specify which base VLA model (pi0, pi0.5, etc.) was used, nor does it mention "input-independent" mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dbed4c1-364e-4be9-9e0c-90bd7b7957c2",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ad4938e7e2fc02063",
  "type": "user",
  "uuid": "4f987c31-9479-4388-b6fe-5118b040a13d",
  "sourceToolAssistantUUID": "8dbed4c1-364e-4be9-9e0c-90bd7b7957c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T06:11:55.848Z_

<details><summary>↩ Tool result · `toolu_01V56KYL6QqddpZud4ZCv4Z6`</summary>

```text
# Research Paper Analysis: VLA Models Generalization

## 1. Full Abstract

"Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations. We show that this brittleness primarily arises from misalignment in Spatial Modeling, rather than Physical Modeling. To address this, we propose a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates. Our first method, Feature Token Modulation (FTM), applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters."

## 2. Base VLA Model

The research uses **π0.5** as the primary base model, with comparisons to **π0** and **OpenVLA** variants.

## 3. FTM Methodology

FTM applies a global, input-independent affine transformation described as: **F̂ = (1+γ)⊙F+β**, where the same two learnable parameter vectors apply uniformly across all visual tokens regardless of input content. The authors note this is "globally applied yet learnable" with no input-dependent modulation.

## 4. Exact Numbers

**FTM Performance:**
- Parameter count: 4,096 parameters (4K)
- Novel viewpoint accuracy: 87.1% (up from 48.5% baseline)
- Libero-V visual benchmark: 90.5%

**Baseline Comparisons (LIBERO novel viewpoints):**
- π0.5 zero-shot: 48.5%
- π0.5 one-shot LoRA: 90.3%
- GeoAware-VLA: 77.9%

## 5. FLA Details and Numbers

**Feature Linear Adaptation** applies low-rank LoRA updates to ViT encoder linear layers:
- Parameter count: 4.7M parameters
- Novel viewpoint success rate: 90.8%
- Libero-V visual benchmark: 94.8%
- Rank 16 baseline configuration
- Achieves 99× parameter reduction versus standard LoRA (467M parameters)

## 6. Limitations Section

**The paper contains no dedicated "Limitations" section.** The authors acknowledge their results require "mild and empirically verifiable assumptions" in theoretical analysis but do not explicitly discuss limitations of their methodology.

## 7. Physical vs. Spatial Modeling Distinction

The authors decompose VLA models into two conceptual components:

- **Spatial Modeling** (visual encoder): "constructs spatial relationships between objects—such as positions, orientations, contact relations, and occlusion structure"
- **Physical Modeling** (VLM and action expert): "integrates task language, spatial representations, and action history to perform high-level reasoning"

They argue viewpoint shifts primarily cause "misalignment in Spatial Modeling" while "Physical Modeling components remain functionally competent."

## 8. Datasets and Benchmarks

- **LIBERO benchmark**: Four task suites (Spatial, Object, Goal, Long) with 10 tasks each
- **Libero-V (Visual)** benchmark: Extends LIBERO with four perturbation types: camera viewpoints, lighting, background texture, and sensor noise
- **Libero-Plus**: Source for visual perturbation data
- **Real-world validation**: Custom Franka Emika Panda setup with five manipulation tasks (block stacking, drawer pulling, button pressing, object pickup, door closing)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36e385f4-a953-4d76-a971-1601e39c81db",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ad4938e7e2fc02063",
  "type": "user",
  "uuid": "adebb9eb-6731-4c24-a508-bb1e79de9ddd",
  "sourceToolAssistantUUID": "36e385f4-a953-4d76-a971-1601e39c81db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-14T06:11:59.203Z_

Excellent, I'm getting detailed information. Let me now fetch more specific sections of the paper to verify the "input-independent" claim and look for any limitations discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adebb9eb-6731-4c24-a508-bb1e79de9ddd",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xzwEJEdaBkok7kMnoU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1f8382c-28a7-435c-9b5e-7cc04d319a11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aSxEt7EKDTNmwePinRhXG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1966,
      "cache_read_input_tokens": 11942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1966,
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

_source line 17 · 2026-05-14T06:12:03.874Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011uD7jgUHNPsvyEY48eHv3r`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.02902",
  "prompt": "Focus on extracting: 1) The exact FTM formula and any text describing whether the gamma and beta parameters are 'input-independent', 'instance-independent', or 'global' - meaning the same transformation is applied regardless of the input image. 2) Any discussion of why this input-independence is surprising or significant. 3) Any limitations, failure cases, or future work sections. 4) The exact experimental setup for the 87.1% number - how many demonstrations were used for one-shot adaptation? 5) Any ablation studies on FTM. 6) The exact pi0.5 model details - what version, what size?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1f8382c-28a7-435c-9b5e-7cc04d319a11",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xzwEJEdaBkok7kMnoU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b650516-f2e7-4c68-b1dc-ea9e529a1aac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aSxEt7EKDTNmwePinRhXG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1966,
      "cache_read_input_tokens": 11942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1966,
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

_source line 18 · 2026-05-14T06:12:09.254Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HyAdzWWVxhLEzxKsx1eWQn`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.02902",
  "prompt": "Find and extract: 1) The conclusion section of the paper. 2) Any 'broader impact' or 'limitations' or 'future work' paragraphs. 3) How exactly is the one-shot adaptation done - what does 'one-shot' mean here (one demonstration? one episode?). 4) Real-world experiment results and details. 5) Any theoretical analysis or propositions about FTM. 6) Table 1 or Table 2 results with exact numbers for all methods compared."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b650516-f2e7-4c68-b1dc-ea9e529a1aac",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1xzwEJEdaBkok7kMnoU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "648e0607-79b9-497a-834b-17cc667e830c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aSxEt7EKDTNmwePinRhXG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1966,
      "cache_read_input_tokens": 11942,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1966
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 440,
          "cache_read_input_tokens": 11942,
          "cache_creation_input_tokens": 1966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1966,
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

_source line 19 · 2026-05-14T06:12:11.865Z_

<details><summary>↩ Tool result · `toolu_011uD7jgUHNPsvyEY48eHv3r`</summary>

```text
# Analysis of VLA Feature Token Modulation Paper

## 1. FTM Formula & Parameter Independence

**Formula:** The exact equation is F̂ = (1+γ)⊙F+β, where γ,β ∈ ℝ^D_ViT are learnable parameters.

**Input-Independence Confirmation:** The authors explicitly state these parameters are "globally applied yet learnable" rather than "input-dependent." They note: "unlike conditional modulation methods that generate input-dependent parameters, our γ and β are globally applied yet learnable, jointly optimized during adaptation while keeping the backbone frozen."

This means the same transformation applies to every image processed, regardless of its content.

## 2. Significance of Global Application

The authors present this as a controlled hypothesis test: "We treat this modulation as a controlled probe to examine whether viewpoint brittleness primarily originates from embedding misalignment rather than insufficient model capacity."

The surprising finding is that such minimal, image-agnostic adjustment (only 4K parameters total) substantially recovers robustness.

## 3. Limitations & Future Work

The paper lacks a dedicated limitations section. However, Table 3 shows FTM achieves 90.5% on Libero-V while FLA reaches 94.8%, suggesting token-level modulation alone has constraints that linear encoder adaptation overcomes.

## 4. One-Shot Adaptation Setup for 87.1%

The 87.1% viewpoint accuracy uses "only a single human demonstration per task to adapt to the new visual domain" according to section 4.1. Training specifics: 2000 steps, batch size 32, Adam optimizer (section 4.3).

## 5. FTM Ablation Studies

No dedicated FTM ablations appear in the main paper. Table 5 focuses on FLA rank variations. Table 4 compares FTM (0.004M parameters, 90.5% success) against Prompt Learning (0.131M, 75.1%) and FLA (4.7M, 94.8%).

## 6. π0.5 Model Details

The paper references π0.5 as their base model but provides minimal architectural specifics in the main text. Section 11 (supplementary) contains "Model Details" but remains limited in the provided excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b650516-f2e7-4c68-b1dc-ea9e529a1aac",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ad4938e7e2fc02063",
  "type": "user",
  "uuid": "0ec767f6-6632-4a2f-a82a-3db1aaad2cb0",
  "sourceToolAssistantUUID": "9b650516-f2e7-4c68-b1dc-ea9e529a1aac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T06:12:16.521Z_

<details><summary>↩ Tool result · `toolu_01HyAdzWWVxhLEzxKsx1eWQn`</summary>

```text
# Research Paper Analysis: VLA Models Robustness

## 1) Conclusion Section

The paper concludes that visual brittleness in VLA models stems from "misalignment in Spatial Modeling rather than limitations in Physical Modeling." The authors propose lightweight mechanisms (FTM and FLA) achieving "state-of-the-art generalization to unseen camera viewpoints and visual perturbations" while being "up to 99× more parameter-efficient than LoRA fine-tuning."

## 2) Broader Impact / Limitations / Future Work

The provided content does not include explicit broader impact, limitations, or future work sections. Section 6 contains only acknowledgments of funding sources.

## 3) One-Shot Adaptation Explanation

"One-shot" means the model receives "only a single human demonstration per task to adapt to the new visual domain." In real-world experiments, adaptation uses one collected trajectory from the novel viewpoint via teleoperation, trained for 750 steps with batch size 32.

## 4) Real-World Experiment Results

The method was tested on a Franka Emika Panda robot across five tasks: stacking blocks, drawer manipulation, button pressing, object pickup, and microwave door closure. Results show "strong robustness to spatial misalignment and consistent success across all five tasks." FLA maintained "90.7% success rate" even with "sub-optimal trajectories" and successfully "adjusts trajectories in real-time against manual target disturbances."

## 5) Theoretical Analysis of FTM

**Theorem 1** establishes that "performance degradation under viewpoint perturbations is controlled by the drift of visual representations." The analysis assumes: (A1) locally Lipschitz policy behavior, (A2) task semantic invariance, and (A3) locally affine/low-rank structure between source and target distributions.

## 6) Table 1 & Table 2 Key Results

**Table 1 (Novel Camera Viewpoints - Average Across Suites):**
- π0.5 LoRA: 90.3%
- π0.5 FTM (ours): 87.1%
- π0.5 FLA (ours): 90.8%

**Table 2 (Novel View Performance):**
- π0.5 LoRA: 90.3%
- Ours (FLA): 90.8%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "648e0607-79b9-497a-834b-17cc667e830c",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ad4938e7e2fc02063",
  "type": "user",
  "uuid": "1e6ee43d-4d15-4cb4-8d89-bd51ceac88d2",
  "sourceToolAssistantUUID": "648e0607-79b9-497a-834b-17cc667e830c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-14T06:12:19.664Z_

Let me get a few more details, particularly about the pi0.5 model and check for the PDF for any limitations section that might be in the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e6ee43d-4d15-4cb4-8d89-bd51ceac88d2",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1y2TdRsbwnqfU5yAzms",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57b8796a-40ac-4703-89d9-47e0bb45d9e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NerRKxzkfYMyPazCjurxns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 13908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1684,
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

_source line 22 · 2026-05-14T06:12:20.145Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CJJZk7gMukTiprVuq9gG2V`</summary>

```json
{
  "query": "pi0.5 model Physical Intelligence VLA robot foundation model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57b8796a-40ac-4703-89d9-47e0bb45d9e6",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1y2TdRsbwnqfU5yAzms",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "368d828a-8a26-46a0-b9a0-90345b2ac151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NerRKxzkfYMyPazCjurxns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 13908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1684,
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

_source line 23 · 2026-05-14T06:12:23.053Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PEmqWDs1xo7BNP1TfDweU1`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.02902",
  "prompt": "Extract: 1) Any supplementary or appendix content about limitations, broader impacts, or societal impacts. 2) The exact content of Section 6 (conclusion or acknowledgments). 3) Details about the pi0.5 model - what is it exactly? Is it from Physical Intelligence? What size is it? 4) Table 3 complete results (Libero-V benchmark). 5) Table 4 complete results (comparison of adaptation methods). 6) Any mentions of failure modes, when FTM does NOT work well, or tasks where performance is poor."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "368d828a-8a26-46a0-b9a0-90345b2ac151",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1y2TdRsbwnqfU5yAzms",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbb75c4a-2d8d-4591-8728-aca30bb573f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NerRKxzkfYMyPazCjurxns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 13908,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 13908,
          "cache_creation_input_tokens": 1684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1684,
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

_source line 24 · 2026-05-14T06:12:26.834Z_

<details><summary>↩ Tool result · `toolu_01CJJZk7gMukTiprVuq9gG2V`</summary>

```text
Web search results for query: "pi0.5 model Physical Intelligence VLA robot foundation model"

Links: [{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"},{"title":"A VLA with Open-World Generalization","url":"https://www.pi.website/blog/pi05"},{"title":"π 0 : Our First Generalist Policy","url":"https://www.pi.website/blog/pi0"},{"title":"[2504.16054] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054"},{"title":"Physical Intelligence (π)","url":"https://www.pi.website/"},{"title":"π0 and π0-FAST: Vision-Language-Action Models for General Robot Control","url":"https://huggingface.co/blog/pi0"},{"title":"Robotics Foundation Models by Physical Intelligence: OpenPi | by Siamak Yousefi | Medium","url":"https://medium.com/@siamak.yousefi.1984_58741/robotics-foundation-models-by-physical-intelligence-openpi-663dc55aa9d3"},{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"},{"title":"[Paper Review] Pi0, Pi0.5, Pi0-FAST - Tracing the Path of Physical Intelligence (PI)","url":"https://bequiet-log.vercel.app/pi-review"},{"title":"Physical Intelligence (π) – Blog","url":"https://www.pi.website/blog"}]

Based on the search results, here's information about the π0.5 model from Physical Intelligence:

## Overview

π0.5 is a Vision-Language-Action (VLA) model that exhibits meaningful generalization to entirely new environments. It is a new model based on π0 that uses co-training on heterogeneous tasks to enable broad generalization.

## Key Features

π0.5 uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. The system uses a combination of co-training and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions.

## Capabilities

π0.5 can perform a variety of tasks in entirely new homes. It demonstrates that an end-to-end learning-enabled robotic system can perform long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes.

## Training Approach

The main principle behind π0.5 is co-training on heterogeneous data: by training the VLA model on a variety of different data sources, it can teach robots how to physically perform diverse skills, understand the semantic context of each skill, infer the high-level structure of a task, and transfer physical behaviors from other robots.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "368d828a-8a26-46a0-b9a0-90345b2ac151",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ad4938e7e2fc02063",
  "type": "user",
  "uuid": "707865ab-67d9-4bd9-9f5c-394b4ddc305d",
  "sourceToolAssistantUUID": "368d828a-8a26-46a0-b9a0-90345b2ac151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T06:12:34.196Z_

<details><summary>↩ Tool result · `toolu_01PEmqWDs1xo7BNP1TfDweU1`</summary>

```text
# Research Paper Analysis: VLA Models Generalizability

## 1. Supplementary/Appendix Content on Limitations and Broader Impacts

The provided content does not include explicit sections on limitations, broader impacts, or societal impacts. The paper focuses on technical contributions without dedicated discussion of these dimensions.

## 2. Section 6: Conclusion and Acknowledgments

**Conclusion excerpt:** The authors conclude that "brittleness primarily arises from misalignment in Spatial Modeling rather than limitations in Physical Modeling." They emphasize that enhancing robustness "does not require larger models or more data; instead, efficient, targeted adaptation can unlock the inherent generalization potential of existing VLA architectures."

**Acknowledgments:** Funding came from the National High-Level Young Talent Program, Fundamental Research Funds for Higher Education at Sun Yat-sen University, Guangdong Provincial programs, and Huawei Strategic Research Institute.

## 3. Details About π₀.₅ Model

The paper identifies π₀.₅ as "a vision-language-action model with open-world generalization." It represents an evolution from the earlier π₀ model. The architecture decomposes into three modules: visual encoder fᵥ, language encoder fℓ, and multimodal transformer decoder. However, the provided content does not specify the exact model size or confirm Physical Intelligence as the developer.

## 4. Table 3 Complete Results (LIBERO-V Benchmark)

| Model | Camera | Light | Texture | Noise | Average |
|-------|--------|-------|---------|-------|---------|
| OpenVLA-OFT | 50.3% | 92.7% | 92.3% | 78.6% | 78.5% |
| OpenVLA-OFT-m (fine-tuned) | 65.2% | 94.9% | 93.9% | 89.9% | 86.0% |
| π₀ (One-Shot LoRA) | 83.6% | 90.7% | 86.7% | 87.0% | 87.0% |
| π₀.₅ (Zero-Shot) | 48.5% | 96.2% | 96.0% | 93.5% | 83.6% |
| π₀.₅ (One-Shot LoRA) | 90.3% | 96.5% | 97.2% | 94.5% | 94.6% |
| π₀.₅ (FTM) | 87.1% | 96.0% | 96.0% | 93.6% | 90.5% |
| π₀.₅ (FLA) | 90.8% | 96.8% | 97.1% | 94.6% | 94.8% |

## 5. Table 4 Complete Results (Adaptation Method Comparison)

| Method | Parameters (M) | Libero-V Success (%) |
|--------|----------------|----------------------|
| π₀ (One-Shot LoRA) | 468.04 | 87.0 |
| Prompt Learning | 0.131 | 75.1 |
| π₀.₅ (One-Shot LoRA) | 466.96 | 94.6 |
| FTM (ours) | 0.004 | 90.5 |
| FLA (ours) | 4.7 | 94.8 |

## 6. Failure Modes and Performance Limitations

The document does not explicitly discuss failure modes or scenarios where FTM/FLA underperform. However, implicit observations include:

- **FTM limitations:** Achieves 87.1% on viewpoint shifts versus 90.8% with FLA, suggesting "global affine transformations have reduced capacity" compared to encoder-level updates
- **Zero-shot brittleness:** π₀.₅ drops to 48.5% success under novel camera viewpoints without adaptation
- **Task-specific variation:** Performance varies across LIBERO suites (Spatial 95.5%, Object 97.5%, Goal 91.7%, Long 77.5% for FLA)

The paper does not identify specific task categories or conditions where adapted models systematically fail.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbb75c4a-2d8d-4591-8728-aca30bb573f1",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ad4938e7e2fc02063",
  "type": "user",
  "uuid": "b70677f5-c68b-4918-9180-4cfe50e812d2",
  "sourceToolAssistantUUID": "fbb75c4a-2d8d-4591-8728-aca30bb573f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T06:13:08.438Z_

Now I have comprehensive information. Let me compile the full verified report.

---

Here is a thorough verification of the paper and its claims:

## 1. Paper Existence and Claims

**The paper exists.** Full title: "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling" (arXiv:2512.02902). Authors: Weiqi Li, Quande Zhang, Ruifeng Zhai, Liang Lin, Guangrun Wang (Sun Yat-sen University, funded partly by Huawei Strategic Research Institute). Originally submitted December 2, 2025; revised March 31, 2026.

**Core thesis:** The brittleness of VLA models under novel viewpoints stems from misalignment in *Spatial Modeling* (the visual encoder's spatial representations), NOT from *Physical Modeling* (the VLM reasoning and action generation). They argue that enhancing robustness "does not require larger models or more data; instead, efficient, targeted adaptation can unlock the inherent generalization potential of existing VLA architectures."

## 2. FTM 87.1% Viewpoint Robustness Claim -- VERIFIED (with caveats)

**The 87.1% number is real, but context matters:**

- The baseline pi0.5 zero-shot accuracy on novel camera viewpoints in LIBERO is **48.5%**.
- FTM improves this to **87.1%** using only **4,096 parameters (4K)** -- this is confirmed.
- However, this is specifically the *novel camera viewpoint* column of the LIBERO-V benchmark, not the overall LIBERO-V average.
- The overall LIBERO-V average for FTM is **90.5%** (because the model already performs well on lighting, texture, and noise perturbations without adaptation -- 96.0%, 96.0%, and 93.6% respectively).
- For comparison, full LoRA fine-tuning of pi0.5 achieves **90.3%** on viewpoints with **467M parameters**, making FTM roughly 117,000x more parameter-efficient for a similar viewpoint result.

## 3. "Input-Independent" Claim -- VERIFIED

**FTM is explicitly input-independent.** The paper states: "unlike conditional modulation methods that generate input-dependent parameters, our gamma and beta are globally applied yet learnable, jointly optimized during adaptation while keeping the backbone frozen."

The formula is: **F_hat = (1 + gamma) . F + beta**, where gamma and beta are in R^{D_ViT}. These are two fixed learnable vectors that apply the exact same affine transformation to every visual token of every input image. There is no conditioning on the input whatsoever. The authors frame this as "a controlled probe to examine whether viewpoint brittleness primarily originates from embedding misalignment rather than insufficient model capacity."

This is indeed surprising -- the same global shift/scale applied to all inputs nearly recovers full viewpoint robustness.

## 4. Base Model -- pi0.5, VERIFIED

The paper uses **pi0.5** (from Physical Intelligence) as the primary base model, with comparisons to **pi0** and **OpenVLA**. The pi0.5 architecture is decomposed into three modules: visual encoder f_v, language encoder f_l, and multimodal transformer decoder. The paper references pi0.5 as "a vision-language-action model with open-world generalization" (arXiv:2504.16054). The exact model size is not specified in the paper.

## 5. Limitations -- THE PAPER HAS NO DEDICATED LIMITATIONS SECTION

This is notable. The paper does **not** contain an explicit "Limitations," "Broader Impact," or "Future Work" section. Section 6 is the conclusion followed by acknowledgments and references. However, implicit limitations can be inferred:

- **FTM has a performance ceiling:** 87.1% viewpoint accuracy vs. 90.8% for FLA and 90.3% for LoRA. The global affine transform cannot capture all viewpoint-induced changes.
- **One-shot requirement:** Adaptation still requires one human demonstration per task from the new viewpoint (trained for 2000 steps, batch size 32, or 750 steps for real-world).
- **Theoretical assumptions:** Their Theorem 1 relies on assumptions of locally Lipschitz policy behavior, task semantic invariance, and locally affine/low-rank structure between source and target distributions -- described as "mild and empirically verifiable" but still assumptions.
- **Task-specific variation:** FLA performance varies: Spatial 95.5%, Object 97.5%, Goal 91.7%, but Long-horizon tasks only 77.5%.
- **No zero-shot generalization:** FTM/FLA require adaptation data; they do not solve the zero-shot viewpoint generalization problem.

## Key Tables for Reference

**LIBERO-V benchmark (Table 3):**

| Method | Params | Camera | Light | Texture | Noise | Avg |
|---|---|---|---|---|---|---|
| pi0.5 Zero-Shot | 0 | 48.5% | 96.2% | 96.0% | 93.5% | 83.6% |
| pi0.5 LoRA | 467M | 90.3% | 96.5% | 97.2% | 94.5% | 94.6% |
| pi0.5 FTM (theirs) | 0.004M | 87.1% | 96.0% | 96.0% | 93.6% | 90.5% |
| pi0.5 FLA (theirs) | 4.7M | 90.8% | 96.8% | 97.1% | 94.6% | 94.8% |

**Adaptation method comparison (Table 4):**

| Method | Parameters | LIBERO-V Success |
|---|---|---|
| Prompt Learning | 0.131M | 75.1% |
| FTM | 0.004M | 90.5% |
| FLA | 4.7M | 94.8% |
| pi0.5 LoRA | 467M | 94.6% |

## Summary Verdict

All five of the specific claims you asked about are substantively accurate:
1. The paper exists and is a real arXiv publication (revised as recently as March 2026).
2. The 87.1% viewpoint number with 4K parameters is correct -- specifically for the camera viewpoint column on LIBERO-V.
3. FTM is genuinely input-independent -- same gamma/beta vectors for all inputs, confirmed by the authors' own description.
4. The base model is pi0.5 (Physical Intelligence), confirmed.
5. The paper has **no dedicated limitations section**, which is itself a limitation of the paper. Implicit limitations include the performance gap vs. FLA/LoRA on viewpoints, the one-shot data requirement, and weaker results on long-horizon tasks.

Sources:
- [arXiv:2512.02902 Abstract](https://arxiv.org/abs/2512.02902)
- [arXiv:2512.02902 Full HTML](https://arxiv.org/html/2512.02902)
- [pi0.5 Paper (arXiv:2504.16054)](https://arxiv.org/abs/2504.16054)
- [Physical Intelligence pi0.5 Blog](https://www.pi.website/blog/pi05)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b70677f5-c68b-4918-9180-4cfe50e812d2",
  "isSidechain": true,
  "agentId": "ad4938e7e2fc02063",
  "requestId": "req_011Cb1y3mCPHacTV9dVWz2Q6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27a26ca1-7a56-4253-92e6-a524ad0c4a6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJxvxpvRfDzUp9mCG2kD41",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 15592,
      "output_tokens": 1793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1793,
          "cache_read_input_tokens": 15592,
          "cache_creation_input_tokens": 2131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2131,
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
