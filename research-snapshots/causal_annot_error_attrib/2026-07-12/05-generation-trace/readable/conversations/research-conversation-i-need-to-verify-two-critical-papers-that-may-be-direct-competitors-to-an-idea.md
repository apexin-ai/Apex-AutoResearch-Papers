# Research conversation: I need to verify two critical papers that may be direct competitors to an idea about using token pruning for VLA robustn

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a7ccdad9c05c6c6ff.jsonl`
- **Structured JSON:** [`f3b72664493faf36fe1d.json`](../../sessions/f3/f3b72664493faf36fe1d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

56 recorded events

### User

_source line 1 · 2026-05-14T06:18:25.205Z_

I need to verify two critical papers that may be direct competitors to an idea about using token pruning for VLA robustness:

1. **ATP - "Efficient Vision-Language Reasoning via Adaptive Token Pruning"** (arXiv 2512.12701): This paper allegedly shows that adaptive token pruning improves robustness under Gaussian noise, blur, and occlusion. I need to verify:
   - Does this paper exist?
   - Does it explicitly claim pruning improves robustness (not just efficiency)?
   - What robustness results does it show?
   - Is it for VLMs or VLAs specifically?

2. **"Visual Token Compression Enhances Model Robustness"** (found on OpenReview): This allegedly identifies "robust-pruning layers" where token pruning enhances robustness. Verify:
   - Does this paper exist?
   - What exactly does it claim about compression and robustness?
   - Is it about VLMs, VLAs, or general vision models?
   - Is it about adversarial robustness or distribution shift robustness?

3. Also search for "token pruning improves robustness" or "token compression robustness benefit" to find any other work claiming pruning/compression helps robustness.

Use WebSearch and WebFetch. This is critical because if these papers already demonstrate that token pruning improves robustness, it significantly reduces the novelty of the ACIBS idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "f61a1c3d-1994-42dc-9b19-13082ba1f474",
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

_source line 2 · 2026-05-14T06:18:25.206Z_

```json
{
  "parentUuid": "f61a1c3d-1994-42dc-9b19-13082ba1f474",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
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
  "uuid": "847dc20b-b6f7-477b-841d-47c98711c33f",
  "timestamp": "2026-05-14T06:18:25.206Z",
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

_source line 3 · 2026-05-14T06:18:28.325Z_



I'll search for both papers and related work systematically. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "847dc20b-b6f7-477b-841d-47c98711c33f",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yVdx3YCnWZve6Jwpnh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a36ca95-4f75-4082-9f96-b4f1552a8382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XipsTnd42WqJguFmzHBN9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 887,
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

_source line 4 · 2026-05-14T06:18:28.413Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013NaWnupws8RpDdfJB721gW`</summary>

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
  "parentUuid": "9a36ca95-4f75-4082-9f96-b4f1552a8382",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yVdx3YCnWZve6Jwpnh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6fc3fd5-cedb-45b0-992e-16f41408a86c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XipsTnd42WqJguFmzHBN9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 887,
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

### Tool result

_source line 5 · 2026-05-14T06:18:28.416Z_

<details><summary>↩ Tool result · `toolu_013NaWnupws8RpDdfJB721gW`</summary>

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
  "parentUuid": "b6fc3fd5-cedb-45b0-992e-16f41408a86c",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "0c659727-a5cd-4031-bc3c-4bae2a7bb3dd",
  "sourceToolAssistantUUID": "b6fc3fd5-cedb-45b0-992e-16f41408a86c",
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

_source line 6 · 2026-05-14T06:18:31.531Z_



Now let me search for both papers and related work in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c659727-a5cd-4031-bc3c-4bae2a7bb3dd",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yVt1sgMJjnkbqsFBjJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de88b0ed-79de-48ad-bf4e-8f2fa5c66c4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AC5Z4y1XwGxkuz2xWaBk8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 7 · 2026-05-14T06:18:32.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QZyzePmLJPtcisFzJ1JK6U`</summary>

```json
{
  "query": "arXiv 2512.12701 \"Adaptive Token Pruning\" vision-language reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de88b0ed-79de-48ad-bf4e-8f2fa5c66c4b",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yVt1sgMJjnkbqsFBjJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "430769d7-4e87-42e6-b5cb-bbc81e9c92d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AC5Z4y1XwGxkuz2xWaBk8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 8 · 2026-05-14T06:18:32.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LDjDH9xVog7kd7TVsASFXA`</summary>

```json
{
  "query": "\"Visual Token Compression Enhances Model Robustness\" OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "430769d7-4e87-42e6-b5cb-bbc81e9c92d0",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yVt1sgMJjnkbqsFBjJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b139e981-6761-42f0-a551-437bf621d571",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AC5Z4y1XwGxkuz2xWaBk8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 9 · 2026-05-14T06:18:32.886Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ApCzDbVbRD8QPcR3GTYFdk`</summary>

```json
{
  "query": "token pruning improves robustness vision language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b139e981-6761-42f0-a551-437bf621d571",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yVt1sgMJjnkbqsFBjJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "caeb59db-24aa-4b6b-b5b5-bd7aac402681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AC5Z4y1XwGxkuz2xWaBk8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 10 · 2026-05-14T06:18:33.178Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019tnZE7GJ14FGPrdtymS81g`</summary>

```json
{
  "query": "token compression robustness benefit vision transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caeb59db-24aa-4b6b-b5b5-bd7aac402681",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yVt1sgMJjnkbqsFBjJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b894955-a2d0-46f7-872d-dd74d89c08cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AC5Z4y1XwGxkuz2xWaBk8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 11 · 2026-05-14T06:18:39.348Z_

<details><summary>↩ Tool result · `toolu_019tnZE7GJ14FGPrdtymS81g`</summary>

```text
Web search results for query: "token compression robustness benefit vision transformer"

Links: [{"title":"Joint Token Pruning and Squeezing Towards More Aggressive Compression of","url":"https://openaccess.thecvf.com/content/CVPR2023/papers/Wei_Joint_Token_Pruning_and_Squeezing_Towards_More_Aggressive_Compression_of_CVPR_2023_paper.pdf"},{"title":"Efficient Token Compression for Vision Transformer with Spatial Information Preserved","url":"https://arxiv.org/html/2503.23455v1"},{"title":"Token Transforming: A Unified and Training-Free Token Compression Framework for Vision Transformer Acceleration","url":"https://arxiv.org/html/2506.05709"},{"title":"[2304.10716] Joint Token Pruning and Squeezing Towards More Aggressive Compression of Vision Transformers","url":"https://arxiv.org/abs/2304.10716"},{"title":"Token Compression Meets Compact Vision Transformers: A Survey and Comparative Evaluation for Edge AI","url":"https://arxiv.org/html/2507.09702"},{"title":"Vision Token Compression","url":"https://www.emergentmind.com/topics/vision-token-compression"},{"title":"LookupViT: Efficient Vision Transformer Compression","url":"https://www.emergentmind.com/papers/2407.12753"},{"title":"Token Compensator: Altering Inference Cost of Vision ...","url":"https://www.emergentmind.com/papers/2408.06798"},{"title":"[2507.09702] Token Compression Meets Compact Vision Transformers: A Survey and Comparative Evaluation for Edge AI","url":"https://arxiv.org/abs/2507.09702"},{"title":"Token Compression Meets Compact Vision Transformers: a Survey and Comparative Evaluation for Edge AI | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11249396/"}]

I've completed the web search for "token compression robustness benefit vision transformer". Here are the key findings:

## Overview of Token Compression in Vision Transformers

Token compression techniques have recently emerged as powerful tools for accelerating Vision Transformer (ViT) inference in computer vision. Due to the quadratic computational complexity with respect to the token sequence length, these methods aim to remove less informative tokens before the attention layers to improve inference throughput.

## Robustness Benefits

One notable finding regarding robustness is from the Token Pruning & Squeezing (TPS) approach: evaluations under the random token selection policy confirm the higher robustness of TPS. This is significant because errors caused by pruning strategies can lead to significant information loss.

TPS squeezes the information of pruned tokens into partial reserved tokens via the unidirectional nearest-neighbor matching and similarity-based fusing steps, which helps preserve information and improve robustness.

## Performance Results

While compressing GFLOPs of DeiT-small&tiny to 35%, TPS outperforms baselines with accuracy improvements of 1%-6%.

Additionally, LookupViT maintains lower deviations in feature representations under adversarial conditions, underscoring its robustness.

## Current Research Gaps

While token compression methods are effective for general-purpose ViTs, they often underperform when directly applied to compact designs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b894955-a2d0-46f7-872d-dd74d89c08cc",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "26da75f0-2af2-4d3e-a79d-0f4c63685dcf",
  "sourceToolAssistantUUID": "7b894955-a2d0-46f7-872d-dd74d89c08cc",
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

_source line 12 · 2026-05-14T06:18:39.401Z_

<details><summary>↩ Tool result · `toolu_01QZyzePmLJPtcisFzJ1JK6U`</summary>

```text
Web search results for query: "arXiv 2512.12701 "Adaptive Token Pruning" vision-language reasoning"

Links: [{"title":"[2512.12701] Efficient Vision-Language Reasoning via Adaptive Token Pruning","url":"https://arxiv.org/abs/2512.12701"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning","url":"https://arxiv.org/html/2512.12701"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning Xue Li","url":"https://arxiv.org/pdf/2512.12701"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning | OpenReview","url":"https://openreview.net/forum?id=Vbqemx4YCC"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2512.12701"},{"title":"[Literature Review] Efficient Vision-Language Reasoning via Adaptive Token Pruning","url":"https://www.themoonlight.io/en/review/efficient-vision-language-reasoning-via-adaptive-token-pruning"},{"title":"Visual Token Pruning for Efficient Vision Models","url":"https://www.emergentmind.com/topics/visual-token-pruning"},{"title":"AI News Clips by Morris Lee: News to help your R&D on X: \"Efficient Vision-Language Reasoning via Adaptive Token Pruning https://t.co/7TnOiLG2Ss --- Newsletter https://t.co/lLfwtmwvak More story https://t.co/THDNHTvSGq LinkedIn https://t.co/2KUI3AIrPl #AINewsClips #AI #ML #ArtificialIntelligence #MachineLearning #ComputerVision https://t.co/jHPTCagz14\" / X","url":"https://x.com/morris_phd/status/2002755688590868747"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://arxiv.org/list/cs.CV/2025?skip=26675&show=50"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=23500&show=25"}]

Based on the search results, here's information about arXiv paper 2512.12701:

## Paper Overview

The paper is titled "Efficient Vision-Language Reasoning via Adaptive Token Pruning" by Xue Li, Xiaonan Song, and Henry Hu, and was submitted on December 14, 2025.

## Core Contribution

The paper introduces Adaptive Token Pruning (ATP), a dynamic inference mechanism that retains only the most informative tokens based on contextual relevance. ATP operates at the vision-language interface, assigning a hybrid importance score combining ViT CLS attention (intra-modal saliency) and CLIP text-image similarity (inter-modal relevance) to keep top-K tokens for the LLM.

## Key Features

Unlike static compression, ATP adapts to each input without modifying the backbone. Proposed as a lightweight gating module, ATP is compatible with popular backbones like BLIP-2, LLaVA, and Flamingo.

## Performance Results

Preliminary evaluations across VQAv2, GQA, and COCO indicate that ATP reduces inference FLOPs by around 40% and achieves roughly 1.5x speedups in end-to-end latency with negligible accuracy loss (less than 1%).

This is an expanded version of an extended abstract accepted at NeurIPS 2025 Workshop on VLM4RWD.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "430769d7-4e87-42e6-b5cb-bbc81e9c92d0",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "65cb0746-1380-4346-8508-8b959c27fefb",
  "sourceToolAssistantUUID": "430769d7-4e87-42e6-b5cb-bbc81e9c92d0",
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

_source line 13 · 2026-05-14T06:18:39.633Z_

<details><summary>↩ Tool result · `toolu_01ApCzDbVbRD8QPcR3GTYFdk`</summary>

```text
Web search results for query: "token pruning improves robustness vision language models"

Links: [{"title":"Revisiting Visual Token Pruning for Vision-Language Model ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Endo_Feather_the_Throttle_Revisiting_Visual_Token_Pruning_for_Vision-Language_Model_ICCV_2025_paper.pdf"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning","url":"https://arxiv.org/html/2512.12701v1"},{"title":"LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models","url":"https://arxiv.org/html/2604.23950"},{"title":"[2512.12701] Efficient Vision-Language Reasoning via Adaptive Token Pruning","url":"https://arxiv.org/abs/2512.12701"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning Xue Li","url":"https://arxiv.org/pdf/2512.12701"},{"title":"HiPrune: Hierarchical Attention for Efficient Token Pruning in Vision-Language Models","url":"https://arxiv.org/html/2508.00553"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Token Pruning for Efficient NLP, Vision, and Speech Models[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202502.2098"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning | OpenReview","url":"https://openreview.net/forum?id=Vbqemx4YCC"},{"title":"[2502.11501] Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?","url":"https://arxiv.org/abs/2502.11501"}]

Based on the web search results, I found several recent papers discussing how token pruning improves robustness in vision-language models:

## Key Findings

Adaptive Token Pruning (ATP) not only improves computational efficiency but also enhances the robustness of VLMs under various visual corruptions and perturbations. More specifically, under Gaussian noise, blur, and occlusion, ATP prunes noisy background patches and retains more stable object regions, improving the model's ability to focus on important visual features.

When subjected to paraphrased questions or added distractor phrases, ATP removes irrelevant patches and appears to reduce hallucinated answers, potentially improving the model's interpretability and performance in real-world scenarios.

Observations suggest adaptive pruning suppresses spurious correlations, improving stability. Furthermore, adaptive pruning tends to suppress spurious correlations and hallucinated features, yielding improved stability across noise conditions.

## Efficiency with Robustness

Token pruning can be deployed in environments with limited resources while maintaining the stability and performance of the model. ATP reduces inference FLOPs by around 40% and achieves roughly 1.5x speedups in end-to-end latency with negligible accuracy loss (less than 1%).

The research suggests that resource-constrained inference and model reliability are not competing objectives, indicating that pruning can simultaneously improve both efficiency and robustness of vision-language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caeb59db-24aa-4b6b-b5b5-bd7aac402681",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "c3d7e267-e87f-4ac2-997b-6a842119edea",
  "sourceToolAssistantUUID": "caeb59db-24aa-4b6b-b5b5-bd7aac402681",
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

_source line 14 · 2026-05-14T06:18:40.039Z_

<details><summary>↩ Tool result · `toolu_01LDjDH9xVog7kd7TVsASFXA`</summary>

```text
Web search results for query: ""Visual Token Compression Enhances Model Robustness" OpenReview"

Links: [{"title":"VISUAL TOKEN COMPRESSION ENHANCES MODEL ...","url":"https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf"},{"title":"Can visual input Be Compressed? A visual input token compression benchmark for large multimodal models | OpenReview","url":"https://openreview.net/forum?id=Vu7iQO3f9u"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"Vision-centric Token Compression in Large Language Model","url":"https://openreview.net/pdf/0d7442c68e585e718f4a9edb5254177d2345bc5f.pdf"},{"title":"Less Is More, but Where? Dynamic Token Compression via LLM-Guided","url":"https://openreview.net/pdf/b4a33413bf051e6a2476bdf1b3f34a1cab246ff1.pdf"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Vision-centric Token Compression in Large Language Model | OpenReview","url":"https://openreview.net/forum?id=YdggdEL41C"},{"title":"A Survey of Token Compression for Efficient Multimodal Large Language Models | OpenReview","url":"https://openreview.net/forum?id=G2od9JVHkE"},{"title":"Task-Related Token Compression in Multimodal Large Language Models from an Explainability Perspective | OpenReview","url":"https://openreview.net/forum?id=YULeQtSyiW"},{"title":"Efficient Multi-modal Large Language Models via Visual Token Grouping | OpenReview","url":"https://openreview.net/forum?id=ym1dS37mZE"}]

Based on the search results, I found the paper "Visual Token Compression Enhances Model Robustness" on OpenReview. Here are the key findings:

## Overview

The paper proposes a visual token compression technique to enhance model robustness against jailbreak attacks and hallucinations.

## Method

To filter out-of-distribution visual tokens, the method measures the distance between each visual token and the language feature space, and prunes the top r% visual tokens with the largest distances at a selected layer. This pruning can be applied iteratively across multiple layers.

## Key Results

On jailbreak defense tasks (SafeBench, HADES, and MM-SafetyBench), the approach achieves an average improvement of 13.46% over the Qwen-2.5-VL baseline. For hallucination evaluation on COCO2014 and HallusionBench, the method outperforms Qwen-2.5-VL by 0.23% and 8.00% on CHAIRi and CHAIRs, and by 0.75% on HallusionBench.

## Important Finding

The authors identify robust-pruning layers—specific layers where visual token pruning can significantly enhance model robustness against jailbreak attacks and hallucinations, with pruning visual tokens in layers [13, 17] on SafeBench and [16, 21] on HallusionBench obviously enhancing model robustness.

The full PDF is available at: https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b139e981-6761-42f0-a551-437bf621d571",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "225ab2ff-9a3c-4cd5-8c82-075f006708c4",
  "sourceToolAssistantUUID": "b139e981-6761-42f0-a551-437bf621d571",
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

_source line 15 · 2026-05-14T06:18:43.210Z_

Good, both papers exist. Now let me fetch the actual content of both papers to verify the specific claims in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "225ab2ff-9a3c-4cd5-8c82-075f006708c4",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yWjK2h7xhHgnKcjJVL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9776be67-e371-47c5-b973-51ff4920d1e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pJ332CLKxKCJGW4s7G87U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1730,
      "cache_creation_input_tokens": 2179,
      "cache_read_input_tokens": 11026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2179,
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

_source line 16 · 2026-05-14T06:18:45.695Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QX3rTQwiDkUkAM5i9NZ1c7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.12701",
  "prompt": "Extract the full abstract and all claims about robustness. Does the paper explicitly claim that token pruning improves robustness (not just efficiency)? What specific robustness results are reported (Gaussian noise, blur, occlusion)? Is this for VLMs or VLAs? What benchmarks are used for robustness evaluation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9776be67-e371-47c5-b973-51ff4920d1e5",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yWjK2h7xhHgnKcjJVL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06c365fe-efa5-41fe-87c8-95b43be2eb32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pJ332CLKxKCJGW4s7G87U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1730,
      "cache_creation_input_tokens": 2179,
      "cache_read_input_tokens": 11026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2179,
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

_source line 17 · 2026-05-14T06:18:47.485Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Kae6edkC9WRtz9WCXS17Ki`</summary>

```json
{
  "url": "https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf",
  "prompt": "Extract the full abstract and all key claims. What does this paper claim about visual token compression and robustness? What type of robustness - adversarial, distribution shift, jailbreak, hallucination? Is it about VLMs, VLAs, or general vision models? What are the \"robust-pruning layers\"? What specific results are shown? What model architectures are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06c365fe-efa5-41fe-87c8-95b43be2eb32",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yWjK2h7xhHgnKcjJVL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8878a768-64d7-4b3a-a6a1-36813842d637",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pJ332CLKxKCJGW4s7G87U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1730,
      "cache_creation_input_tokens": 2179,
      "cache_read_input_tokens": 11026,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2179
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1730,
          "output_tokens": 352,
          "cache_read_input_tokens": 11026,
          "cache_creation_input_tokens": 2179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2179,
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

_source line 18 · 2026-05-14T06:18:50.766Z_

<details><summary>↩ Tool result · `toolu_01QX3rTQwiDkUkAM5i9NZ1c7`</summary>

```text
# Analysis of Robustness Claims in arXiv:2512.12701

## Full Abstract

The provided abstract states: "Real-world deployment of Vision-Language Models (VLMs) is hindered by high computational demands... ATP reduces inference FLOPs by around 40% and achieves roughly 1.5x speedups... with negligible accuracy loss (less than 1%). Qualitative analyses suggest ATP preserves visual grounding and enhances interpretability. Beyond efficiency, we investigate robustness under corruptions; observations suggest adaptive pruning suppresses spurious correlations, improving stability."

## Robustness Claims

**Does the paper explicitly claim token pruning improves robustness?**

Yes, but cautiously. The text states: "Beyond efficiency, we investigate robustness under corruptions; observations suggest adaptive pruning suppresses spurious correlations, improving stability."

## Specific Results

The abstract provides **no detailed robustness metrics**. It mentions only:
- Investigation of "robustness under corruptions"
- Observations that pruning may suppress "spurious correlations"
- Improvement in "stability"

**No specific corruption types are reported** (Gaussian noise, blur, occlusion are not mentioned in this content).

## Model Type & Benchmarks

- **Model type**: Vision-Language Models (VLMs), not VLAs
- **Robustness benchmarks**: Not specified in the abstract
- **Efficiency benchmarks**: VQAv2, GQA, COCO (mentioned for accuracy evaluation, not robustness)

## Conclusion

Robustness claims appear preliminary and lack quantitative details in this abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06c365fe-efa5-41fe-87c8-95b43be2eb32",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "627f7356-abff-4587-9746-e625bb5c3674",
  "sourceToolAssistantUUID": "06c365fe-efa5-41fe-87c8-95b43be2eb32",
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

_source line 19 · 2026-05-14T06:18:52.544Z_

<details><summary>↩ Tool result · `toolu_01Kae6edkC9WRtz9WCXS17Ki`</summary>

```text
I appreciate your request, but I need to be transparent: the content you've provided appears to be a PDF file rendered as raw binary data and PDF object streams. This format contains mostly unreadable compressed and encoded information rather than extractable text.

From what limited readable content I can discern, this appears to be an academic paper, but I cannot reliably extract:
- The abstract
- Key claims about visual token compression
- Specific robustness types being addressed
- Model architectures discussed
- Numerical results presented

**To assist you properly, I would need:**
1. A text-based version of the paper (TXT, or copy-pasted content)
2. A clearer PDF with extractable text layers
3. The paper's title or DOI so I can reference the work accurately

If you can provide the paper in a more accessible format or share specific sections you'd like analyzed, I'd be happy to address your questions about visual token compression, robustness mechanisms, and the architectural innovations described.

[Binary content (application/pdf, 4.2MB) also saved to /home/ubuntu/.claude-account-1/projects/-/a0e3a753-d9ef-4264-a82c-a92ffb3029a9/tool-results/webfetch-1778739528439-3uiull.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8878a768-64d7-4b3a-a6a1-36813842d637",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "59782004-6cb2-45b6-8ee3-374a19dec659",
  "sourceToolAssistantUUID": "8878a768-64d7-4b3a-a6a1-36813842d637",
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

_source line 20 · 2026-05-14T06:18:55.695Z_

The PDF didn't render. Let me try the HTML version of the ATP paper and search for the second paper differently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59782004-6cb2-45b6-8ee3-374a19dec659",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yXemTmoGkHED9xv3RX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2017f52-9213-4e3c-8acd-bf2ac5782a57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FaBv8nACuJqdakUjixTrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 13205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

_source line 21 · 2026-05-14T06:18:58.101Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J9dUjeYdjBGktx2iomZwVp`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.12701",
  "prompt": "Extract ALL sections related to robustness. Specifically: 1) Does the paper have a dedicated robustness evaluation section? 2) What corruptions are tested (Gaussian noise, blur, occlusion)? 3) What quantitative robustness results are reported with specific numbers? 4) Is this preliminary/qualitative or backed by thorough experiments? 5) Does it claim pruning IMPROVES robustness or just maintains it?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2017f52-9213-4e3c-8acd-bf2ac5782a57",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yXemTmoGkHED9xv3RX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f752713c-d1d8-4db8-b6b6-e0b79e8b3199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FaBv8nACuJqdakUjixTrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 13205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

_source line 22 · 2026-05-14T06:18:59.026Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AWP77n8VMBDM2oMuLHxGLy`</summary>

```json
{
  "query": "\"Visual Token Compression Enhances Model Robustness\" robust-pruning layers jailbreak hallucination Qwen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f752713c-d1d8-4db8-b6b6-e0b79e8b3199",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yXemTmoGkHED9xv3RX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9d56d2a-aecb-4ec0-8d34-8550062e8ac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FaBv8nACuJqdakUjixTrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 13205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

_source line 23 · 2026-05-14T06:18:59.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gx6kA3VfQHVLJxz1pWhawN`</summary>

```json
{
  "query": "VLA-IAP \"Vision-Language-Action\" token pruning robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9d56d2a-aecb-4ec0-8d34-8550062e8ac3",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yXemTmoGkHED9xv3RX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eea46fe9-125c-4e87-861a-946c4ec7da8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FaBv8nACuJqdakUjixTrw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 13205,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 13205,
          "cache_creation_input_tokens": 2913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2913,
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

_source line 24 · 2026-05-14T06:19:02.893Z_

<details><summary>↩ Tool result · `toolu_01J9dUjeYdjBGktx2iomZwVp`</summary>

```text
# Robustness Analysis in ATP Paper

## 1. Dedicated Robustness Evaluation Section
**No formal section exists.** Robustness discussion appears only in Section 5.2 "Robustness Hints (Ongoing)" and the abstract, explicitly labeled as preliminary and exploratory.

## 2. Corruptions Tested
The paper mentions three corruption types:
- **Gaussian noise**
- **Blur**
- **Occlusion**

Additionally, textual perturbations are mentioned (paraphrased questions, distractor phrases).

## 3. Quantitative Results
**None provided.** The paper explicitly states: "when subjected to paraphrased questions or added distractor phrases, ATP removes irrelevant patches" but offers no numerical metrics, accuracy percentages, or statistical comparisons.

## 4. Experimental Rigor
**Preliminary and qualitative only.** Section 5.2 is titled "Robustness Hints (Ongoing)" and the authors acknowledge: "our current experiments are limited in scale" and results "should be considered preliminary and exploratory."

## 5. Nature of Robustness Claim
**Improvement claim, not maintenance.** The abstract states ATP "tends to suppress spurious correlations and hallucinated features, yielding improved stability across noise conditions," suggesting enhanced robustness rather than merely preserved performance.

**Key limitation:** This represents speculative observation rather than validated empirical evidence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f752713c-d1d8-4db8-b6b6-e0b79e8b3199",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "26ecbce4-85aa-4ff8-8501-89466e19a75e",
  "sourceToolAssistantUUID": "f752713c-d1d8-4db8-b6b6-e0b79e8b3199",
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

_source line 25 · 2026-05-14T06:19:07.341Z_

<details><summary>↩ Tool result · `toolu_01Gx6kA3VfQHVLJxz1pWhawN`</summary>

```text
Web search results for query: "VLA-IAP "Vision-Language-Action" token pruning robustness"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/html/2602.20566"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2602.20566] BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/abs/2602.20566"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"},{"title":"GitHub - chen7086/VLA-ADP: Action aware Dynamic Pruning for Efficient Vision Language Action Manipulation · GitHub","url":"https://github.com/chen7086/VLA-ADP"}]

Based on the search results, I found comprehensive information about VLA-IAP and related Vision-Language-Action token pruning research. Here are the key findings:

## VLA-IAP Overview

VLA-IAP (Interaction-Aligned Pruning) is a training-free method that introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.

## Robustness Focus

The key innovation of VLA-IAP is addressing robustness concerns that plague existing token pruning approaches. Existing visual token pruning methods mainly rely on semantic saliency or simple temporal cues, overlooking the continuous physical interaction, a fundamental property of VLA tasks, which often leads to pruning visually sparse yet structurally critical regions that support manipulation, resulting in unstable behavior during early task phases.

VLA-IAP consistently outperforms other baselines, maintaining robust manipulation capabilities even under extreme visual compression.

## Performance Results

On the LIBERO benchmark, VLA-IAP achieves a state-of-the-art 97.8% success rate with a 1.54× speedup without performance degradation compared to the unpruned baseline. Additionally, real-world experiments demonstrate up to 1.48× inference acceleration while simultaneously improving the average manipulation success rate.

## Comparative Robustness

Under extreme pruning conditions, at an extreme 30% token retention rate, perception-first baselines such as FastV and SparseVLM suffer catastrophic failures, dropping to a 0% success rate on multiple tasks including select_flower and select_toy. VLA-IAP avoids this collapse through its interaction-first approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eea46fe9-125c-4e87-861a-946c4ec7da8d",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "f700d69a-5233-4a64-b4a2-88750a8e1408",
  "sourceToolAssistantUUID": "eea46fe9-125c-4e87-861a-946c4ec7da8d",
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

_source line 26 · 2026-05-14T06:19:07.889Z_

<details><summary>↩ Tool result · `toolu_01AWP77n8VMBDM2oMuLHxGLy`</summary>

```text
Web search results for query: ""Visual Token Compression Enhances Model Robustness" robust-pruning layers jailbreak hallucination Qwen"

Links: [{"title":"On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/html/2601.21531"},{"title":"HiPrune: Hierarchical Attention for Efficient Token Pruning in Vision-Language Models","url":"https://arxiv.org/html/2508.00553"},{"title":"[2601.21531] On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/abs/2601.21531"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"A Glimpse to Compress: Dynamic Visual Token Pruning for Large Vision-Language Models","url":"https://arxiv.org/html/2508.01548v1"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"},{"title":"ToDRE: Effective Visual Token Pruning via Token Diversity and Task Relevance","url":"https://arxiv.org/html/2505.18757"},{"title":"Revisiting Visual Token Pruning for Vision-Language Model ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Endo_Feather_the_Throttle_Revisiting_Visual_Token_Pruning_for_Vision-Language_Model_ICCV_2025_paper.pdf"},{"title":"ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling","url":"https://arxiv.org/html/2603.22911v1"}]

I've performed the web search for your query. Here are the key findings:

## Research on Visual Token Compression in Vision-Language Models

The search results reveal several recent research papers and projects focused on visual token compression and its effects on model robustness:

### Adversarial Robustness Under Token Compression

Visual token compression is widely used to accelerate large vision-language models (LVLMs) by pruning or merging visual tokens, yet its adversarial robustness remains unexplored. Existing encoder-based attacks can substantially overestimate the robustness of compressed LVLMs, due to an optimization-inference mismatch: perturbations are optimized on the full-token representation, while inference is performed through a token-compression bottleneck.

Researchers propose the Compression-AliGnEd attack (CAGE), which aligns perturbation optimization with compression inference without assuming access to the deployed compression mechanism or its token budget, combining expected feature disruption and rank distortion alignment.

### Methods and Performance

HiPrune maintains 99.3% of original performance while requiring only 1/3 tokens with a 58.7% FLOPs reduction, and with a tight budget of 1/9 tokens, HiPrune++ still preserves 96.1% accuracy score, accompanied by an outstanding hallucination reduction compared with baselines.

### Application to Qwen Models

HiPrune achieves state-of-the-art on Qwen with a different encoder and dynamic token length setting, confirming its versatility on various architectures.

GlimpsePrune achieves an average visual token pruning rate of 92.6% while retaining 100% of the original model's performance on free-form VQA tasks when integrated with Qwen2.5-VL-7B, and its fine-tuned version reaches 110% of the original performance while maintaining a high pruning rate.

The research indicates that visual token compression techniques can enhance efficiency while maintaining or even improving model robustness when properly designed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9d56d2a-aecb-4ec0-8d34-8550062e8ac3",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "1d7a8caa-1e1a-4de2-bad4-07dfeec94d57",
  "sourceToolAssistantUUID": "c9d56d2a-aecb-4ec0-8d34-8550062e8ac3",
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

_source line 27 · 2026-05-14T06:19:11.567Z_

Excellent findings. Now let me fetch the second paper's OpenReview page (not the PDF) and also the CAGE paper which seems highly relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d7a8caa-1e1a-4de2-bad4-07dfeec94d57",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yYnUqHwoi3zi3VRLbc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f641c91-64f4-4827-b437-889fe19cf073",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A32eYvBoUDBkUjyLQKEV1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 981,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 16118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1755,
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

_source line 28 · 2026-05-14T06:19:12.218Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LeZmGDdmQPGrNZnbXWrrfe`</summary>

```json
{
  "query": "site:openreview.net \"Visual Token Compression Enhances Model Robustness\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f641c91-64f4-4827-b437-889fe19cf073",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yYnUqHwoi3zi3VRLbc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6874f2bf-d42f-4eb1-8ba7-d9acff2d59cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A32eYvBoUDBkUjyLQKEV1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 981,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 16118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1755,
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

_source line 29 · 2026-05-14T06:19:13.495Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015BHdeDVhFW7ZKpWXhdg5ja`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.21531",
  "prompt": "Extract the full abstract. What does this paper claim about adversarial robustness of VLMs under visual token compression? Does compression help or hurt robustness? What key findings are reported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6874f2bf-d42f-4eb1-8ba7-d9acff2d59cb",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yYnUqHwoi3zi3VRLbc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ad08449-cd0d-485d-8752-037f902ba339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A32eYvBoUDBkUjyLQKEV1y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 981,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 16118,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1755
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 981,
          "output_tokens": 259,
          "cache_read_input_tokens": 16118,
          "cache_creation_input_tokens": 1755,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1755,
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

_source line 30 · 2026-05-14T06:19:13.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016NctZ5jqydagzd8aF36pWj`</summary>

```json
{
  "query": "token pruning noise robustness VLM distribution shift corruption benefit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ad08449-cd0d-485d-8752-037f902ba339",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yYnUqHwoi3zi3VRLbc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddb03cea-7f4b-438a-a205-bb20307ce501",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A32eYvBoUDBkUjyLQKEV1y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 981,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 16118,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1755
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 981,
          "output_tokens": 259,
          "cache_read_input_tokens": 16118,
          "cache_creation_input_tokens": 1755,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1755,
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

_source line 31 · 2026-05-14T06:19:15.335Z_

<details><summary>↩ Tool result · `toolu_01LeZmGDdmQPGrNZnbXWrrfe`</summary>

```text
Web search results for query: "site:openreview.net "Visual Token Compression Enhances Model Robustness""

No links found.

The search for that exact query on OpenReview.net did not return any results. This could mean:

1. The paper with that exact title may not be published on OpenReview.net
2. The title might be slightly different from what was specified
3. The paper may be on a different platform or not yet published

If you're looking for a specific paper about visual token compression and model robustness, I'd be happy to help you search for it with:
- A modified or partial title
- The author names (if you know them)
- A broader search across all of the web instead of just OpenReview.net
- Any other relevant details about the paper

Let me know how you'd like to proceed!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6874f2bf-d42f-4eb1-8ba7-d9acff2d59cb",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "6ea9263c-39da-4665-afa6-08f67a45940e",
  "sourceToolAssistantUUID": "6874f2bf-d42f-4eb1-8ba7-d9acff2d59cb",
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

_source line 32 · 2026-05-14T06:19:18.996Z_

<details><summary>↩ Tool result · `toolu_015BHdeDVhFW7ZKpWXhdg5ja`</summary>

```text
# Paper Summary: Adversarial Robustness of VLMs Under Visual Token Compression

## Full Abstract
"Visual token compression is widely used to accelerate large vision-language models (LVLMs) by pruning or merging visual tokens, yet its adversarial robustness remains unexplored. We show that existing encoder-based attacks can substantially overestimate the robustness of compressed LVLMs, due to an optimization-inference mismatch: perturbations are optimized on the full-token representation, while inference is performed through a token-compression bottleneck..."

## Key Claims About Compression and Robustness

**Compression hurts robustness.** The research demonstrates that token compression creates a critical vulnerability gap. The authors identify an "optimization-inference mismatch" where adversarial attacks designed for full models fail to account for the compression bottleneck, leading to overly optimistic robustness assessments.

## Major Findings

1. **Existing attacks are insufficient**: Standard encoder-based attacks substantially underestimate vulnerabilities in compressed models.

2. **New attack methodology**: The authors propose CAGE (Compression-AliGnEd attack) that aligns with actual compression processes without requiring knowledge of the deployed mechanism.

3. **Consistent vulnerability**: Across diverse compression mechanisms and datasets, CAGE achieves lower robust accuracy than baseline approaches, confirming compression introduces exploitable weaknesses.

4. **Research gap highlighted**: The work calls for "compression-aware security evaluation and defenses for efficient LVLMs," emphasizing that ignoring compression yields unrealistic robustness estimates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ad08449-cd0d-485d-8752-037f902ba339",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "4406989b-43c5-4d90-b68f-06973bc23355",
  "sourceToolAssistantUUID": "0ad08449-cd0d-485d-8752-037f902ba339",
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

_source line 33 · 2026-05-14T06:19:21.979Z_

<details><summary>↩ Tool result · `toolu_016NctZ5jqydagzd8aF36pWj`</summary>

```text
Web search results for query: "token pruning noise robustness VLM distribution shift corruption benefit"

Links: [{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning","url":"https://arxiv.org/html/2512.12701v1"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning | OpenReview","url":"https://openreview.net/forum?id=Vbqemx4YCC"},{"title":"The Model Knows Which Tokens Matter: Automatic Token Selection via Noise Gating","url":"https://arxiv.org/html/2603.07135"},{"title":"VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm","url":"https://arxiv.org/html/2512.02700v3"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning Xue Li","url":"https://arxiv.org/pdf/2512.12701"},{"title":"Is Less More? Exploring Token Condensation as Training-free ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Is_Less_More_Exploring_Token_Condensation_as_Training-free_Test-time_Adaptation_ICCV_2025_paper.pdf"},{"title":"[2603.07135] The Model Knows Which Tokens Matter: Automatic Token Selection via Noise Gating","url":"https://arxiv.org/abs/2603.07135"},{"title":"FlashVLM: Text-Guided Visual Token Selection for Large Multimodal Models","url":"https://arxiv.org/html/2512.20561"},{"title":"[Literature Review] Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference","url":"https://www.themoonlight.io/en/review/efficient-video-sampling-pruning-temporally-redundant-tokens-for-faster-vlm-inference"}]

Based on the search results, I found several recent works exploring token pruning in Vision-Language Models (VLMs) and its relationship to noise robustness, corruption handling, and distribution shift resilience:

## Key Findings:

### Token Pruning and Noise Robustness

Adaptive pruning tends to suppress spurious correlations and hallucinated features, yielding improved stability across noise conditions. This is a central finding of Adaptive Token Pruning (ATP), which demonstrates that token pruning can enhance robustness beyond just improving efficiency.

### Benefits Under Visual Corruption

Under Gaussian noise, blur, and occlusion, ATP prunes noisy background patches and retains more stable object regions, improving the model's ability to focus on important visual features. Additionally, by discarding noisy background tokens and retaining semantically meaningful regions, ATP helps VLMs focus on stable content, mitigating sensitivity to corruptions and clutter.

### Textual Perturbations

When subjected to paraphrased questions or added distractor phrases, ATP removes irrelevant patches and appears to reduce hallucinated answers, potentially improving the model's interpretability and performance in real-world scenarios.

### Training-Free Distribution Shift Resilience

Recent work like AutoSelect reformulates token pruning as "capacity constrained communication," using a variance preserving noise gate that modulates each token's information flow according to its predicted importance, which implicitly helps the model handle distribution shifts and corruptions.

### Token Condensation for Corrupted Data

Token Condensation as Adaptation (TCA) is a training-free adaptation method that condenses token representation through information-preserving token reduction and logits correction, achieving up to 21.4% performance improvement on corrupted datasets while reducing GFLOPs by 12.2% to 48.9%.

These approaches suggest that token pruning's ability to focus on semantically important tokens provides an incidental benefit for robustness against various types of visual and linguistic corruption.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddb03cea-7f4b-438a-a205-bb20307ce501",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "c06f8fa7-4323-4461-814f-1a0c7384caec",
  "sourceToolAssistantUUID": "ddb03cea-7f4b-438a-a205-bb20307ce501",
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

_source line 34 · 2026-05-14T06:19:26.197Z_

Let me now get more details on the "Visual Token Compression Enhances Model Robustness" paper since the PDF didn't parse, and also check the TCA paper which seems relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c06f8fa7-4323-4461-814f-1a0c7384caec",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yZpfKrt1Vkdy9L4kBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53eea8f8-45df-40a8-bcbe-bba4142f9993",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTbs4gZQBMiwkmxpYscSiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2909,
      "cache_read_input_tokens": 17873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2909,
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

_source line 35 · 2026-05-14T06:19:27.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MK4eHS7w5RBnoBm3hGEKob`</summary>

```json
{
  "query": "\"Visual Token Compression Enhances\" robustness jailbreak SafeBench HADES MM-SafetyBench pruning layers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53eea8f8-45df-40a8-bcbe-bba4142f9993",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yZpfKrt1Vkdy9L4kBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2285cd45-c6ed-44e9-a059-b62abf9f39cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTbs4gZQBMiwkmxpYscSiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2909,
      "cache_read_input_tokens": 17873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2909,
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

_source line 36 · 2026-05-14T06:19:28.559Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011kTNNSvKrBak6p1vsuG8UG`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.21531",
  "prompt": "Extract all key findings about whether token compression helps or hurts adversarial robustness. What are the quantitative results? Does compression act as a defense or create vulnerabilities? What models were tested?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2285cd45-c6ed-44e9-a059-b62abf9f39cc",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yZpfKrt1Vkdy9L4kBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2833943d-5d9a-4358-a5af-39ae3829210a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTbs4gZQBMiwkmxpYscSiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2909,
      "cache_read_input_tokens": 17873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2909,
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

_source line 37 · 2026-05-14T06:19:29.239Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014cM6UZwA21epSHd53oouvH`</summary>

```json
{
  "query": "\"token condensation\" adaptation corrupted robustness TCA test-time ICCV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2833943d-5d9a-4358-a5af-39ae3829210a",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yZpfKrt1Vkdy9L4kBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "068b03b4-b464-469b-b798-6eff8ef54a84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTbs4gZQBMiwkmxpYscSiU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2909,
      "cache_read_input_tokens": 17873,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 17873,
          "cache_creation_input_tokens": 2909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2909,
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

_source line 38 · 2026-05-14T06:19:34.803Z_

<details><summary>↩ Tool result · `toolu_01MK4eHS7w5RBnoBm3hGEKob`</summary>

```text
Web search results for query: ""Visual Token Compression Enhances" robustness jailbreak SafeBench HADES MM-SafetyBench pruning layers"

Links: [{"title":"How Jailbreak and Stealth Wrestle in Vision-Language ...","url":"https://openreview.net/pdf/236e102fe49cdbd77f2b0c6fef444be6240ea05c.pdf"},{"title":"MMJ-Bench: A Comprehensive Study on Jailbreak Attacks and Defenses for Vision","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34983/37138"},{"title":"GitHub - jiaxiaojunQAQ/OmniSafeBench-MM: A Unified Benchmark and Toolbox for Multimodal Jailbreak Attack–Defense Evaluation","url":"https://github.com/jiaxiaojunQAQ/OmniSafeBench-MM"},{"title":"MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/385383434_MM-SafetyBench_A_Benchmark_for_Safety_Evaluation_of_Multimodal_Large_Language_Models"},{"title":"SafePTR: Token-Level Jailbreak Defense in Multimodal LLMs via Prune-then-Restore Mechanism","url":"https://arxiv.org/html/2507.01513"},{"title":"GitHub - isXinLiu/MM-SafetyBench: Accepted by ECCV 2024 · GitHub","url":"https://github.com/isXinLiu/MM-SafetyBench"},{"title":"OmniSafeBench-MM: A Unified Benchmark and Toolbox for Multimodal","url":"https://www.arxiv.org/pdf/2512.06589"},{"title":"SafeBench: A Safety Evaluation Framework for Multimodal Large Language Models","url":"https://arxiv.org/html/2410.18927v1"},{"title":"MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models | Computer Vision – ECCV 2024","url":"https://dl.acm.org/doi/10.1007/978-3-031-72992-8_22"},{"title":"OmniSafeBench-MM: A Unified Benchmark and Toolbox for Multimodal Jailbreak Attack–Defense Evaluation","url":"https://arxiv.org/html/2512.06589v1"}]

Based on my web search results, I found information about the benchmarks and safety evaluation frameworks you mentioned, though the specific paper "Visual Token Compression Enhances" was not directly identified. However, I can provide context on the related concepts:

## Key Findings on the Benchmarks:

SafeBench comprises 500 harmful instructions across 10 prohibited categories, based on forbidden topics outlined in both OpenAI and Meta's LLaMA-2 Usage Policies.

MM-SafetyBench comprises 13 scenarios with 5,040 text-image pairs.

HADES leverages adversarial noises combined with optimized Stable Diffusion-generated images and typography blending to achieve high attack success rates.

## Related Defense Research:

There is relevant research on defense mechanisms against jailbreaks. SafePTR is a training-free and token-level defense framework that mitigates multimodal jailbreaks by pruning harmful tokens in vulnerable layers and restoring benign features to recover contextual information while preserving model utility, and it effectively enhances robustness against multimodal jailbreak attacks across 3 MLLMs on 3 safety benchmarks including MM-SafetyBench, FigStep, and Jailbreak28k.

The research area focuses on evaluating vision-language model safety against multimodal jailbreak attacks and developing robust defenses. If you're looking for a specific paper on visual token compression, you may want to search for more specific author names or publication venues, as the exact title didn't appear in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2285cd45-c6ed-44e9-a059-b62abf9f39cc",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "5cba4554-1780-4eab-a305-8eb4143639a1",
  "sourceToolAssistantUUID": "2285cd45-c6ed-44e9-a059-b62abf9f39cc",
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

_source line 39 · 2026-05-14T06:19:35.129Z_

<details><summary>↩ Tool result · `toolu_011kTNNSvKrBak6p1vsuG8UG`</summary>

```text
# Token Compression and Adversarial Robustness: Key Findings

## Main Discovery: Compression Creates Vulnerabilities Rather Than Defenses

The research reveals that visual token compression in Large Vision-Language Models (LVLMs) **does not defend against adversarial attacks**—instead, it creates new vulnerabilities. The authors identify a critical "optimization-inference mismatch" where existing attacks underestimate model vulnerability under compression.

## How Compression Affects Robustness

**Insight I - Distortion Concentration:** Under adversarial inputs, "compression behaves as a 'distortion concentrator'" rather than a denoiser. The mechanism preferentially retains heavily corrupted, high-importance tokens while discarding relatively clean, low-importance ones.

**Insight II - Optimization Mismatch:** Existing attacks optimize perturbations across the full token space, but deployed models use compressed representations, creating an effectiveness gap.

## Quantitative Results

Testing on LLaVA with five compression methods across three datasets revealed substantial robustness degradation:

- **TextVQA (most significant impact):** Baseline robust accuracy of 34.7% drops to 26.5% without compression; CAGE attack reduces it further to modest percentages depending on compression level
- **VQA-v2:** Robust accuracy decreases from 55.8% to 49.4% without compression
- **Across compression budgets:** When retaining 192 tokens, average robust accuracy dropped 11.3-30.1%; at 64 tokens, drops reached 13.2-39.2%

## Models Tested

- **Primary:** LLaVA
- **Secondary validation:** Qwen2.5-VL

## Compression Mechanisms Evaluated

- VisionZIP
- VisPruner
- DivPrune
- FlowCut
- PruMerge

**Conclusion:** Token compression amplifies adversarial vulnerability rather than providing defense.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2833943d-5d9a-4358-a5af-39ae3829210a",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "6e68ece1-ca17-4f8b-9505-78f4ccc35398",
  "sourceToolAssistantUUID": "2833943d-5d9a-4358-a5af-39ae3829210a",
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

_source line 40 · 2026-05-14T06:19:38.264Z_

<details><summary>↩ Tool result · `toolu_014cM6UZwA21epSHd53oouvH`</summary>

```text
Web search results for query: ""token condensation" adaptation corrupted robustness TCA test-time ICCV 2025"

Links: [{"title":"GitHub - Jo-wang/TCA: Official repo for ICCV 2025 paper \"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation\"","url":"https://github.com/Jo-wang/TCA"},{"title":"Is Less More? Exploring Token Condensation as Training-free ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Is_Less_More_Exploring_Token_Condensation_as_Training-free_Test-time_Adaptation_ICCV_2025_paper.pdf"},{"title":"Track: Poster Session 1 & Exhibit Hall","url":"https://iccv.thecvf.com/virtual/2025/session/2873"},{"title":"[2410.14729] Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/abs/2410.14729"},{"title":"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/html/2410.14729"},{"title":"[2410.14729v3] Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/abs/2410.14729v3"},{"title":"Tokens on Demand: Token Condensation as Training-free Test-time Adaptation | OpenReview","url":"https://openreview.net/forum?id=EK1yOLL7GA&noteId=aa1fhh8o1I"},{"title":"All Papers - ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/ICCV2025?day=all"},{"title":"bibtex - ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/ICCV2025?day=2025-10-21"},{"title":"ICCV 2025 Papers","url":"https://iccv.thecvf.com/virtual/2025/papers.html"}]

I found the research paper you're looking for! Here are the key findings from the search:

## Paper Overview

The paper "Exploring Token Condensation as Training-free Test-time Adaptation" has been accepted at ICCV 2025. This work explores efficient online test-time adaptation for real-world distribution shifts, focusing on robustness without retraining.

## Main Contribution

The paper proposes Token Condensation as Adaptation (TCA), a training-free adaptation method that takes a step beyond standard token condensation. Rather than passively discarding tokens, TCA condenses token representation by introducing reservoir-based domain anchor tokens for information-preserving token reduction and logits correction.

## Performance Results

TCA achieves up to a 21.4% performance improvement over the strongest baseline on cross-dataset benchmark and the CIFAR-100-Corrupted dataset while reducing GFLOPs by 12.2% to 48.9%, with minimal hyperparameter dependency on both CLIP and SigLIP series.

## Robustness to Corrupted Data

The proposed TCA consistently demonstrates improvements across corruption levels, highlighting the effectiveness of the DTR module in preserving informative and reliable token representations for logits correction.

The official repository is available at: https://github.com/Jo-wang/TCA


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "068b03b4-b464-469b-b798-6eff8ef54a84",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "bddc077c-ec92-44aa-91cd-5f918e6ad7ba",
  "sourceToolAssistantUUID": "068b03b4-b464-469b-b798-6eff8ef54a84",
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

_source line 41 · 2026-05-14T06:19:41.556Z_

Let me now try to access the "Visual Token Compression Enhances Model Robustness" paper through different means, and also check a couple more relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bddc077c-ec92-44aa-91cd-5f918e6ad7ba",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yb2JbRnHDcqrFS3xRX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "651f22e2-6802-4abc-9bbe-21b6f81fc264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXT3JznveSqzH9i7qGfTEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2800,
      "cache_read_input_tokens": 20782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2800,
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

_source line 42 · 2026-05-14T06:19:42.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GEXeorcDdxwMCo3NdrW47F`</summary>

```json
{
  "query": "\"Visual Token Compression Enhances Model Robustness\" arxiv OR openreview 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "651f22e2-6802-4abc-9bbe-21b6f81fc264",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yb2JbRnHDcqrFS3xRX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fd78fde-c6c8-4133-8c04-27b51f587bb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXT3JznveSqzH9i7qGfTEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2800,
      "cache_read_input_tokens": 20782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2800,
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

_source line 43 · 2026-05-14T06:19:44.023Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BrUeeTW8ycm9TbYbyeUsDN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.14729",
  "prompt": "Extract the abstract. What does this paper claim about token condensation helping with robustness to corruptions? Is this about VLMs, VLAs, or general vision models? What corruptions are tested?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fd78fde-c6c8-4133-8c04-27b51f587bb6",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yb2JbRnHDcqrFS3xRX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecd3d678-9896-4004-a61b-87f1974b9969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXT3JznveSqzH9i7qGfTEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2800,
      "cache_read_input_tokens": 20782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2800,
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

_source line 44 · 2026-05-14T06:19:44.566Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014C9Aoaa59cFEJa66u8TX53`</summary>

```json
{
  "query": "SafePTR \"prune-then-restore\" token pruning jailbreak defense robustness VLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecd3d678-9896-4004-a61b-87f1974b9969",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yb2JbRnHDcqrFS3xRX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "189a797b-f0c3-4e02-ba4c-9c1e68135d5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXT3JznveSqzH9i7qGfTEh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2800,
      "cache_read_input_tokens": 20782,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 20782,
          "cache_creation_input_tokens": 2800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2800,
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

_source line 45 · 2026-05-14T06:19:47.957Z_

<details><summary>↩ Tool result · `toolu_01BrUeeTW8ycm9TbYbyeUsDN`</summary>

```text
# Abstract and Key Claims

**Abstract:**
The paper proposes Token Condensation as Adaptation (TCA), stating it "achieves up to a 21.4% performance improvement over the strongest baseline on cross-dataset benchmark and the CIFAR-100-Corrupted dataset."

**Robustness Claims:**
The authors claim token condensation helps by improving visual-text alignment in vision-language models on unseen datasets. They demonstrate this through performance gains on corrupted image benchmarks while simultaneously reducing computational costs.

**Model Type:**
This work focuses on **Vision-Language Models (VLMs)**, specifically CLIP and SigLIP series. The research addresses how these multimodal models can be adapted at test time without training.

**Corruptions Tested:**
The paper explicitly mentions testing on **CIFAR-100-Corrupted** dataset. The abstract also references "cross-dataset benchmark" evaluations, which typically involve natural distribution shifts, though the specific corruption types aren't detailed in the provided content.

The core insight is that selectively condensing tokens—rather than simply removing them—preserves performance on in-distribution data while improving generalization to out-of-distribution scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecd3d678-9896-4004-a61b-87f1974b9969",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "e22ab8aa-db01-4d77-b6e3-306d5a97d00f",
  "sourceToolAssistantUUID": "ecd3d678-9896-4004-a61b-87f1974b9969",
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

_source line 46 · 2026-05-14T06:19:48.370Z_

<details><summary>↩ Tool result · `toolu_01GEXeorcDdxwMCo3NdrW47F`</summary>

```text
Web search results for query: ""Visual Token Compression Enhances Model Robustness" arxiv OR openreview 2025 2026"

Links: [{"title":"VISUAL TOKEN COMPRESSION ENHANCES MODEL ...","url":"https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf"},{"title":"[2605.08329] An Efficient Token Compression Framework for Visual Object Tracking","url":"https://arxiv.org/abs/2605.08329"},{"title":"An Efficient Token Compression Framework for Visual Object Tracking","url":"https://arxiv.org/html/2605.08329"},{"title":"[2601.21531] On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/abs/2601.21531"},{"title":"On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/html/2601.21531"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference | OpenReview","url":"https://openreview.net/forum?id=80faIPZ67S"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v3"},{"title":"GitHub - cokeshao/Awesome-Multimodal-Token-Compression: [TMLR 2026] Survey: https://arxiv.org/pdf/2507.20198 · GitHub","url":"https://github.com/cokeshao/Awesome-Multimodal-Token-Compression"},{"title":"[2502.00791] Vision-centric Token Compression in Large Language Model","url":"https://arxiv.org/abs/2502.00791"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"}]

I found the paper you're looking for! The paper "Visual Token Compression Enhances Model Robustness" presents an OOD-VTP algorithm that significantly improves model robustness while keeping strong performance on general datasets and enjoying higher efficiency. 

The paper is available on OpenReview at: https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf

The work investigates how visual token compression influences the robustness of Vision-Language Models (VLMs) against jailbreak attacks and hallucinations. The research evaluates robustness against jailbreak attacks using three datasets: SafeBench, MM-SafetyBench, and HADES.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fd78fde-c6c8-4133-8c04-27b51f587bb6",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "ba071ed2-495c-4e33-94f9-d4179cacfcc4",
  "sourceToolAssistantUUID": "8fd78fde-c6c8-4133-8c04-27b51f587bb6",
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

_source line 47 · 2026-05-14T06:19:53.087Z_

<details><summary>↩ Tool result · `toolu_014C9Aoaa59cFEJa66u8TX53`</summary>

```text
Web search results for query: "SafePTR "prune-then-restore" token pruning jailbreak defense robustness VLM"

Links: [{"title":"SafePTR: Token-Level Jailbreak Defense in Multimodal LLMs via Prune-then-Restore Mechanism","url":"https://arxiv.org/html/2507.01513"},{"title":"SafePTR : Token-Level Jailbreak Defense in Multimodal LLMs ...","url":"https://openreview.net/pdf?id=MNSiBGNAvx#:~:text=Based%20on%20our%20analysis,%20we,information%20while%20preserving%20model%20utility."},{"title":"SafePTR: Token-Level Jailbreak Defense in Multimodal ...","url":"https://arxiv.org/pdf/2507.01513"},{"title":"[2507.01513] SafePTR: Token-Level Jailbreak Defense in Multimodal LLMs via Prune-then-Restore Mechanism","url":"https://arxiv.org/abs/2507.01513"},{"title":"SafePTR: Token-Level Jailbreak Defense in Multimodal LLMs via Prune-then-Restore Mechanism | OpenReview","url":"https://openreview.net/forum?id=MNSiBGNAvx"},{"title":"(PDF) SafePTR: Token-Level Jailbreak Defense in Multimodal LLMs via Prune-then-Restore Mechanism","url":"https://www.researchgate.net/publication/393333732_SafePTR_Token-Level_Jailbreak_Defense_in_Multimodal_LLMs_via_Prune-then-Restore_Mechanism"},{"title":"NeurIPS Poster SafePTR: Token-Level Jailbreak Defense in Multimodal LLMs via Prune-then-Restore Mechanism","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118476"},{"title":"SafePTR-Token-Level-Jailbreak-Defense-in-Multimodal-LLMs- ...","url":"https://www.researchgate.net/publication/393333732_SafePTR_Token-Level_Jailbreak_Defense_in_Multimodal_LLMs_via_Prune-then-Restore_Mechanism/fulltext/6865f8c6e4632b045dc96fd8/SafePTR-Token-Level-Jailbreak-Defense-in-Multimodal-LLMs-via-Prune-then-Restore-Mechanism.pdf?origin=scientificContributions"},{"title":"Paper-Notes-en/docs/NeurIPS2025/llm_alignment/metadefense_defending_finetuning-based_jailbreak_attack_before_and_during_genera.md at main · zhaoyang97/Paper-Notes-en","url":"https://github.com/zhaoyang97/Paper-Notes-en/blob/main/docs/NeurIPS2025/llm_alignment/metadefense_defending_finetuning-based_jailbreak_attack_before_and_during_genera.md"},{"title":"Awesome-LM-SSP/collection/paper/safety/jailbreak.md at main · CryptoAILab/Awesome-LM-SSP","url":"https://github.com/CryptoAILab/Awesome-LM-SSP/blob/main/collection/paper/safety/jailbreak.md"}]

I found comprehensive information about SafePTR. Here's a summary of the research:

## SafePTR: Token-Level Jailbreak Defense

SafePTR is a training-free defense framework that selectively prunes harmful tokens at vulnerable layers while restoring benign features at subsequent layers.

### Key Finding

The research found that less than 1% of tokens in early-middle layers are responsible for inducing unsafe behaviors, highlighting that precisely removing a small subset of harmful tokens without requiring safety tuning can effectively improve safety against jailbreaks.

### How It Works

The framework uses two main components:

1. **Harmful Token Pruning (HTP)**: Applying HTP alone significantly reduces the Attack Success Rate (ASR) from 52.3 to 3.06, though at the expense of utility due to the removal of benign contextual information.

2. **Benign Feature Restoration (BFR)**: The Benign Feature Restoration module selectively reintegrates benign features while avoiding harmful semantics. By restoring previously pruned tokens at this stage, the model preserves functional performance without compromising safety.

### Performance Results

SafePTR achieves low Attack Success Rates across multiple models, for example 0.98 on LLaVA-1.5 versus 2.10 for Immune and 14.36 for AdaShield, and under strong adversarial conditions it significantly reduces ASR from over 70 to 2.71 on MiniGPT-4-7B.

### Efficiency Advantages

SafePTR requires no training and runs in 3.51 seconds with a one-pass pipeline, faster than multi-pass methods, offering strong robustness and generalization without additional training or runtime cost.

Extensive evaluations across three MLLMs and five benchmarks demonstrate SafePTR's state-of-the-art performance in mitigating jailbreak risks without compromising utility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "189a797b-f0c3-4e02-ba4c-9c1e68135d5e",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "9b2176e3-d341-41b1-9c85-a55bba51143f",
  "sourceToolAssistantUUID": "189a797b-f0c3-4e02-ba4c-9c1e68135d5e",
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

_source line 48 · 2026-05-14T06:19:56.107Z_

Now let me also look at the survey paper and the "Token Reduction Should Go Beyond Efficiency" paper, as these seem directly relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b2176e3-d341-41b1-9c85-a55bba51143f",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yc7faZtoaCddvskK3B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9ec6e31-7669-4498-9eb7-540d63be7c43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mQ9CeRphmoSncGaoT3Kdj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2692,
      "cache_read_input_tokens": 23582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2692,
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

_source line 49 · 2026-05-14T06:19:57.665Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VAZvoDqngAp9uW91nsdjbK`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.18227v3",
  "prompt": "Extract the abstract and key claims. Does this paper argue that token reduction provides benefits BEYOND efficiency (like robustness)? What specific non-efficiency benefits are identified? Is robustness one of them?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9ec6e31-7669-4498-9eb7-540d63be7c43",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yc7faZtoaCddvskK3B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2185b4a5-2633-49ff-bb42-214a1b7fe861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mQ9CeRphmoSncGaoT3Kdj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2692,
      "cache_read_input_tokens": 23582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2692,
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

_source line 50 · 2026-05-14T06:19:58.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q8tfbhJvTFb5zbC8EK624R`</summary>

```json
{
  "query": "\"token reduction beyond efficiency\" robustness vision language multimodal 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2185b4a5-2633-49ff-bb42-214a1b7fe861",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1yc7faZtoaCddvskK3B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c51defa-1d6d-40c2-be2b-b8d920017954",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mQ9CeRphmoSncGaoT3Kdj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2692,
      "cache_read_input_tokens": 23582,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2692
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 23582,
          "cache_creation_input_tokens": 2692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2692,
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

_source line 51 · 2026-05-14T06:20:02.404Z_

<details><summary>↩ Tool result · `toolu_01VAZvoDqngAp9uW91nsdjbK`</summary>

```text
# Token Reduction Beyond Efficiency: Abstract and Key Claims

## Abstract Summary

The paper argues that token reduction should transcend its traditional role as a mere efficiency optimization. Instead, it proposes token reduction as "a fundamental principle in generative modeling, critically influencing both model architecture and broader applications."

## Non-Efficiency Benefits Identified

The paper identifies several benefits beyond computational efficiency:

1. **Multimodal Integration**: "facilitate deeper multimodal integration and alignment"

2. **Reducing Overthinking**: The paper demonstrates how token reduction can "mitigate 'overthinking' and hallucinations" in language models, where models generate unnecessarily verbose reasoning chains.

3. **Long-Context Coherence**: Token reduction helps "maintain coherence over long inputs" by selectively preserving relevant information.

4. **Training Stability**: The paper shows token reduction can "enhance training stability" when integrated into pre-training phases.

5. **Visual Representation Quality**: Token reduction improves obtaining "informative visual representation" in multimodal models.

## Is Robustness Mentioned?

While the paper doesn't explicitly highlight robustness as a primary benefit, it briefly mentions that token reduction enables models to "simultaneously reduce computational load, improve robustness, and enhance interpretability and alignment." However, robustness receives minimal emphasis compared to the other identified benefits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2185b4a5-2633-49ff-bb42-214a1b7fe861",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "9409ff7b-cf33-4d70-9ba6-26d6e4ed90f8",
  "sourceToolAssistantUUID": "2185b4a5-2633-49ff-bb42-214a1b7fe861",
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

_source line 52 · 2026-05-14T06:20:04.517Z_

<details><summary>↩ Tool result · `toolu_01Q8tfbhJvTFb5zbC8EK624R`</summary>

```text
Web search results for query: ""token reduction beyond efficiency" robustness vision language multimodal 2025"

Links: [{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v1"},{"title":"[2505.18227v2] Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://arxiv.org/abs/2505.18227v2"},{"title":"[2505.18227] Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://arxiv.org/abs/2505.18227"},{"title":"Token Reduction Should Go Beyond Efficiency in ...","url":"https://arxiv.org/pdf/2505.18227"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning Xue Li","url":"https://arxiv.org/pdf/2512.12701"},{"title":"(PDF) Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://www.researchgate.net/publication/392104162_Token_Reduction_Should_Go_Beyond_Efficiency_in_Generative_Models_--_From_Vision_Language_to_Multimodality"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250518227K/abstract"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://www.catalyzex.com/paper/token-reduction-should-go-beyond-efficiency"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"}]

Based on the search results, I found a highly relevant paper that matches your query exactly:

## "Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality"

This paper reframes token reduction as more than an efficiency measure, positioning it as a fundamental principle in generative modeling that critically influences both model architecture and broader applications.

### Key Claims:

Across vision, language, and multimodal systems, token reduction can: (i) facilitate deeper multimodal integration and alignment, (ii) mitigate "overthinking" and hallucinations, (iii) maintain coherence over long inputs, and (iv) enhance training stability.

### Robustness and Performance Benefits:

The work highlights token reduction's potential to drive new model architectures and learning strategies that improve robustness, increase interpretability, and better align with the objectives of generative modeling.

By learning to intelligently select, merge, or compress tokens based on their contribution to generation objectives—rather than solely on raw redundancy—models can simultaneously reduce computational load, improve robustness, and enhance interpretability and alignment.

### Future Directions:

The paper outlines promising future directions, including algorithm design, reinforcement learning-guided token reduction, token optimization for in-context learning, and broader ML and scientific domains.

This paper (arXiv:2505.18227) was submitted in May 2025 and provides a comprehensive framework for understanding token reduction beyond mere computational efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c51defa-1d6d-40c2-be2b-b8d920017954",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "b4d761c3-303d-4203-8a5d-9ecb487797ed",
  "sourceToolAssistantUUID": "4c51defa-1d6d-40c2-be2b-b8d920017954",
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

_source line 53 · 2026-05-14T06:20:09.124Z_

Now I have a comprehensive picture. Let me do one final search specifically about whether the "Visual Token Compression Enhances Model Robustness" paper has an arXiv version or more metadata.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4d761c3-303d-4203-8a5d-9ecb487797ed",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1ycxYvguXRRPagHz6rb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7edd3ada-abc4-4053-92a4-7b87db0d1fb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAGGPGCRpuh6f8LxN39gUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 26274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 54 · 2026-05-14T06:20:10.652Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NccVxS4mjQ2cQU5WSxXnMg`</summary>

```json
{
  "query": "\"OOD-VTP\" visual token pruning out-of-distribution robustness jailbreak Qwen-2.5-VL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7edd3ada-abc4-4053-92a4-7b87db0d1fb7",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1ycxYvguXRRPagHz6rb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a6ad2a3-b6ce-41d8-a1a6-8886f29f15b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAGGPGCRpuh6f8LxN39gUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 26274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 55 · 2026-05-14T06:20:17.066Z_

<details><summary>↩ Tool result · `toolu_01NccVxS4mjQ2cQU5WSxXnMg`</summary>

```text
Web search results for query: ""OOD-VTP" visual token pruning out-of-distribution robustness jailbreak Qwen-2.5-VL"

Links: [{"title":"VISUAL TOKEN COMPRESSION ENHANCES MODEL ...","url":"https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf"},{"title":"When Token Pruning is Worse than Random: Understanding Visual Token Information in VLLMs","url":"https://arxiv.org/html/2512.07580"},{"title":"IDPruner: Harmonizing Importance and Diversity in Visual Token Pruning for MLLMs","url":"https://arxiv.org/html/2602.13315v1"},{"title":"ToDRE: Effective Visual Token Pruning via Token Diversity and Task Relevance","url":"https://arxiv.org/html/2505.18757"},{"title":"ERASE: Eliminating Redundant Visual Tokens via Adaptive Two-Stage Token Pruning","url":"https://arxiv.org/html/2605.09982v1"},{"title":"IVTP: Instruction-guided Visual Token Pruning for Large Vision-Language Models","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02577.pdf"},{"title":"LLM-VTP: LLM-Reasoned Visual Token Pruning for Efficient Multi-Modal Video Understanding | OpenReview","url":"https://openreview.net/forum?id=Acdd83rF1s"},{"title":"EvoPrune: Early-Stage Visual Token Pruning for Efficient MLLMs","url":"https://www.researchgate.net/publication/401564290_EvoPrune_Early-Stage_Visual_Token_Pruning_for_Efficient_MLLMs"},{"title":"A Glimpse to Compress: Dynamic Visual Token Pruning for Large Vision-Language Models","url":"https://arxiv.org/html/2508.01548v1"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"}]

I found research on OOD-VTP (Out-of-Distribution Visual Token Pruning). Here are the key findings:

## What is OOD-VTP?

OOD-VTP is a method that provides a robust and generalizable defense against jailbreak attacks by selectively pruning out-of-distribution visual tokens.

## Key Research Details

The approach has been validated using two vision-language model frameworks: LLaVA and Qwen2.5-VL.

### Performance Against Jailbreaks

OOD-VTP demonstrates superior performance in defending against jailbreak attacks, consistently improving model robustness. The effectiveness of this approach is particularly pronounced on the Qwen-2.5-VL model.

The vanilla Qwen-2.5-VL model demonstrates a substantially higher refusal rate against jailbreak attacks compared to LLaVA-1.5, achieving an average refusal rate of 20.21% across three safety datasets.

### Evaluation Benchmarks

The method was evaluated on three prominent datasets: SafeBench, MM-SafetyBench, and HADES.

The research appears to be part of recent work on defending vision-language models against adversarial attacks by intelligently pruning visual tokens that appear to be out-of-distribution, which helps the model maintain safety properties while maintaining general performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a6ad2a3-b6ce-41d8-a1a6-8886f29f15b0",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a7ccdad9c05c6c6ff",
  "type": "user",
  "uuid": "b519a443-1632-49f9-955f-8865d32bb1f2",
  "sourceToolAssistantUUID": "6a6ad2a3-b6ce-41d8-a1a6-8886f29f15b0",
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

_source line 56 · 2026-05-14T06:21:08.148Z_

I now have a thorough picture of the landscape. Here is my comprehensive analysis.

---

## Verification Results

### Paper 1: ATP - "Efficient Vision-Language Reasoning via Adaptive Token Pruning" (arXiv 2512.12701)

**Does it exist?** YES. This is a real paper by Xue Li, Xiaonan Song, and Henry Hu, submitted December 14, 2025. It was presented at the NeurIPS 2025 Workshop on VLM4RWD.

**Does it explicitly claim pruning improves robustness?** Yes, but the claims are extremely preliminary and hedged. The abstract states: *"Beyond efficiency, we investigate robustness under corruptions; observations suggest adaptive pruning suppresses spurious correlations, improving stability."* The operative word is "suggest."

**What robustness results does it show?** Essentially none that are quantitative. The robustness discussion appears in a section titled **"Robustness Hints (Ongoing)"** (Section 5.2). The authors explicitly state their experiments are "limited in scale" and results "should be considered preliminary and exploratory." Gaussian noise, blur, and occlusion are mentioned as corruption types, but **no numerical robustness metrics are reported**. There are no robustness benchmarks, no accuracy-under-corruption numbers, no comparison tables. This is qualitative speculation, not validated empirical evidence.

**VLMs or VLAs?** This is for **VLMs** (BLIP-2, LLaVA, Flamingo). It is NOT about VLAs or robotic manipulation.

**Bottom line for novelty threat: LOW.** ATP's robustness claims are preliminary hints without quantitative backing. It would be easy to cite this as "concurrent work that observed a similar trend" but it does not constitute a rigorous demonstration of pruning-for-robustness.

---

### Paper 2: "Visual Token Compression Enhances Model Robustness" (OpenReview)

**Does it exist?** YES. The paper is available as a PDF on OpenReview (`openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf`). It proposes a method called **OOD-VTP** (Out-of-Distribution Visual Token Pruning).

**What does it claim?** It claims that pruning visual tokens that are far from the language feature space (i.e., out-of-distribution tokens) enhances model robustness against **jailbreak attacks and hallucinations** -- NOT against natural corruptions or distribution shifts. The method measures the distance between each visual token and the language feature space, then prunes the top r% most distant tokens at specific layers.

**What are "robust-pruning layers"?** The paper identifies specific transformer layers where pruning is most beneficial for robustness: layers [13, 17] on SafeBench and [16, 21] on HallusionBench for Qwen-2.5-VL.

**Specific results:** On jailbreak defense tasks (SafeBench, HADES, MM-SafetyBench), OOD-VTP achieves an average improvement of 13.46% over the Qwen-2.5-VL baseline. For hallucination (COCO2014, HallusionBench), improvements of 0.23-8.00% on CHAIR metrics and 0.75% on HallusionBench.

**VLMs, VLAs, or general vision?** This is about **VLMs** (Qwen-2.5-VL, LLaVA-1.5). NOT VLAs.

**Type of robustness?** This is about **safety/jailbreak robustness and hallucination reduction**, NOT about distribution shift robustness or natural corruption robustness. This is a fundamentally different kind of "robustness" than what would be relevant for VLA deployment in noisy real-world environments.

**Bottom line for novelty threat: MODERATE but different domain.** The finding that pruning OOD tokens improves safety is interesting but addresses a completely different robustness axis (adversarial jailbreaks/hallucinations) than what ACIBS would target (natural corruptions, distribution shifts in robotic manipulation).

---

### Additional Relevant Papers Found

**3. CAGE - "On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression" (arXiv 2601.21531)**
This paper actually shows the **opposite** -- that token compression **hurts** adversarial robustness. Compression acts as a "distortion concentrator" that preferentially retains heavily corrupted high-importance tokens. Tested on LLaVA with 5 compression methods, robust accuracy dropped 11-39% depending on token budget. This is evidence AGAINST the pruning-helps-robustness narrative (at least for adversarial robustness).

**4. TCA - "Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation" (ICCV 2025, arXiv 2410.14729)**
Shows that token condensation improves robustness to distribution shifts on CIFAR-100-Corrupted (up to 21.4% improvement). This is for CLIP/SigLIP models (VLMs), not VLAs. Notably, this is about token condensation (merging), not pruning per se, and it's a test-time adaptation method.

**5. VLA-IAP (arXiv 2603.22991)**
This IS about VLAs specifically. It addresses token pruning for Vision-Language-Action models, achieving 97.8% success rate with 1.54x speedup on LIBERO. However, its "robustness" claim is about maintaining manipulation success under extreme pruning ratios, NOT about robustness to visual corruptions or distribution shifts.

**6. SafePTR (arXiv 2507.01513, NeurIPS 2025)**
Uses pruning as a jailbreak defense -- prunes harmful tokens at vulnerable layers and restores benign features. Reduces attack success rate from 52.3% to 3.06%. Again, safety robustness, not natural corruption robustness.

**7. "Token Reduction Should Go Beyond Efficiency" (arXiv 2505.18227)**
A survey/position paper that briefly mentions robustness as a benefit of token reduction, but provides no original experimental evidence. Claims token reduction can "simultaneously reduce computational load, improve robustness, and enhance interpretability."

---

### Summary Assessment for ACIBS Novelty

The landscape reveals an important nuance:

1. **No existing work rigorously demonstrates that token pruning improves VLA robustness to natural corruptions/distribution shifts.** The ATP paper hints at this for VLMs but provides zero quantitative evidence. No VLA-specific robustness-through-pruning work exists.

2. **The "robustness" in existing papers means different things:** jailbreak defense (OOD-VTP, SafePTR), maintaining performance under aggressive pruning (VLA-IAP), or test-time adaptation (TCA). None target the specific robustness axis of "VLA operating under visual noise, occlusion, and domain shift in robotic environments."

3. **One paper (CAGE) actually shows compression HURTS adversarial robustness**, providing a counternarrative.

4. **The novelty gap for ACIBS remains significant** if it can demonstrate quantitatively that adaptive token pruning improves VLA robustness to natural corruptions in robotic manipulation settings. The key differentiators would be: (a) VLA-specific rather than VLM, (b) natural corruption/distribution shift robustness rather than jailbreak safety, and (c) rigorous quantitative evidence rather than preliminary hints.

Sources:
- [ATP: Efficient Vision-Language Reasoning via Adaptive Token Pruning](https://arxiv.org/abs/2512.12701)
- [Visual Token Compression Enhances Model Robustness (PDF)](https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf)
- [CAGE: On the Adversarial Robustness of LVLMs under Visual Token Compression](https://arxiv.org/abs/2601.21531)
- [TCA: Is Less More? Token Condensation as Training-free Test-time Adaptation](https://arxiv.org/abs/2410.14729)
- [VLA-IAP: Training-Free Visual Token Pruning for VLA Models](https://arxiv.org/abs/2603.22991)
- [SafePTR: Token-Level Jailbreak Defense via Prune-then-Restore](https://arxiv.org/abs/2507.01513)
- [Token Reduction Should Go Beyond Efficiency](https://arxiv.org/abs/2505.18227)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b519a443-1632-49f9-955f-8865d32bb1f2",
  "isSidechain": true,
  "agentId": "a7ccdad9c05c6c6ff",
  "requestId": "req_011Cb1ydtJxma798J83aanFx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b27425ce-d835-4a52-8d05-2443d3bdc61b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RK2LDxMSZGMHdfbAiX2ohy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 27735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1001,
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
