# Research conversation: I'm reviewing a paper idea about using Information Bottleneck for token-level pruning in Vision-Language-Action models t

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 123
- **Recorded user turns:** 1
- **Tool calls:** 53
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a39f9fcd5ae529f28.jsonl`
- **Structured JSON:** [`2d80db4c9a75ce03c220.json`](../../sessions/2d/2d80db4c9a75ce03c220.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

123 recorded events

### User

_source line 1 · 2026-05-14T06:13:27.669Z_

I'm reviewing a paper idea about using Information Bottleneck for token-level pruning in Vision-Language-Action models to improve robustness. I need to find ANY competing or concurrent work that the authors might have missed. Search for:

1. "token pruning robustness VLA 2025 2026" - any work combining token pruning with robustness for VLAs
2. "information bottleneck robot manipulation 2025 2026" - any IB work in robot manipulation beyond BC-IB
3. "visual token selection robust robotics 2025 2026" - token selection for robust robot policies
4. "adaptive token pruning vision language model robustness" - adaptive pruning for VLM robustness
5. "multi-view information bottleneck token selection" - combining multi-view IB with token selection
6. "LIBERO-Plus robustness methods 2026" - what methods have been evaluated on LIBERO-Plus
7. "token compression adversarial robustness vision language" - work on how token compression affects robustness
8. Search specifically for any papers from Physical Intelligence, UC Berkeley robotics, Stanford robotics, or Google DeepMind on VLA robustness in 2025-2026

For each search, use WebSearch. Report any papers that seem highly relevant and that are NOT already cited in this list:
- BC-IB, DRIBO, MIB, FTM/FLA, VLA-IAP, LightVLA, GridS, DTP, Compressor-VLA, RobustVLA, CRT, SRPO, ToBo, IBTM, arXiv 2601.21531, arXiv 2601.12042, arXiv 2505.18227

Be thorough - try different keyword combinations and check both arXiv and conference proceedings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "4837e279-05ea-4159-acc1-d82b6086837a",
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

_source line 2 · 2026-05-14T06:13:27.672Z_

```json
{
  "parentUuid": "4837e279-05ea-4159-acc1-d82b6086837a",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
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
  "uuid": "c26fe9db-6b7c-44a6-a8d8-62bb3bc6e05a",
  "timestamp": "2026-05-14T06:13:27.672Z",
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

_source line 3 · 2026-05-14T06:13:31.079Z_



I'll conduct a thorough search across all the specified queries. Let me start by loading the WebSearch tool and then running searches in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c26fe9db-6b7c-44a6-a8d8-62bb3bc6e05a",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y7hrL97WWxCquZLwR5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4d427a2-fbc3-440e-b359-fe1157512920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BzRYLRL36NdhWKr2EFxqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 974,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 974,
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

_source line 4 · 2026-05-14T06:13:31.345Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HbQEPz4XZs1skF279BkJ5L`</summary>

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
  "parentUuid": "d4d427a2-fbc3-440e-b359-fe1157512920",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y7hrL97WWxCquZLwR5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "069b5767-03f4-41dd-8f39-85dddca6b3ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BzRYLRL36NdhWKr2EFxqv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 974,
      "cache_read_input_tokens": 8223,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 974
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 974,
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

_source line 5 · 2026-05-14T06:13:31.348Z_

<details><summary>↩ Tool result · `toolu_01HbQEPz4XZs1skF279BkJ5L`</summary>

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
  "parentUuid": "069b5767-03f4-41dd-8f39-85dddca6b3ef",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "47c80efa-f683-404e-af22-0677091fcc8e",
  "sourceToolAssistantUUID": "069b5767-03f4-41dd-8f39-85dddca6b3ef",
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

_source line 6 · 2026-05-14T06:13:36.257Z_



Now let me run all 8 searches in parallel batches. I'll start with the first 4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47c80efa-f683-404e-af22-0677091fcc8e",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y7yuy6fcvdwD2di8Bd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "925c5e5b-3a8a-40f2-8f1e-9ea1c60d511d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJvpLCHGvQ6F41RYFEAVjf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 9197,
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

_source line 7 · 2026-05-14T06:13:36.892Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CBh5B2XcPoXvetJpFpFTPw`</summary>

```json
{
  "query": "token pruning robustness VLA vision language action 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "925c5e5b-3a8a-40f2-8f1e-9ea1c60d511d",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y7yuy6fcvdwD2di8Bd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f94d3051-8a24-4159-9e5a-2640f17bf0aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJvpLCHGvQ6F41RYFEAVjf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 9197,
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

_source line 8 · 2026-05-14T06:13:36.897Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KXSRKhc2jie3g3U8aPv1ob`</summary>

```json
{
  "query": "information bottleneck robot manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f94d3051-8a24-4159-9e5a-2640f17bf0aa",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y7yuy6fcvdwD2di8Bd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a467625-b1a4-4577-8001-ee44762849c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJvpLCHGvQ6F41RYFEAVjf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 9197,
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

_source line 9 · 2026-05-14T06:13:37.208Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MoR1ghDVWve618MKKXsvbr`</summary>

```json
{
  "query": "visual token selection robust robotics policy 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a467625-b1a4-4577-8001-ee44762849c2",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y7yuy6fcvdwD2di8Bd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35b689e9-cc7a-48f0-89fa-1974b66b6128",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJvpLCHGvQ6F41RYFEAVjf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 9197,
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

_source line 10 · 2026-05-14T06:13:37.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R3vHL164pb9UePaEzQMiHL`</summary>

```json
{
  "query": "adaptive token pruning vision language model robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35b689e9-cc7a-48f0-89fa-1974b66b6128",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y7yuy6fcvdwD2di8Bd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "662b7ca4-3659-445e-b59b-8500de167ffe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJvpLCHGvQ6F41RYFEAVjf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 9197,
      "output_tokens": 230,
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
          "output_tokens": 230,
          "cache_read_input_tokens": 9197,
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

_source line 11 · 2026-05-14T06:13:43.821Z_

<details><summary>↩ Tool result · `toolu_01KXSRKhc2jie3g3U8aPv1ob`</summary>

```text
Web search results for query: "information bottleneck robot manipulation 2025 2026"

Links: [{"title":"GitHub - BaiShuanghao/BC-IB: [ICML 2025] Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://github.com/BaiShuanghao/BC-IB"},{"title":"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=N2Dey442PJ"},{"title":"BC-IB for Robot Manipulation - GitHub Pages","url":"https://baishuanghao.github.io/BC-IB.github.io/"},{"title":"[2502.02853] Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/abs/2502.02853"},{"title":"Embodied intelligence for robot manipulation: development and challenges | Vicinagearth | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44336-025-00020-1"},{"title":"Behavioral Cloning in Imitation Learning","url":"https://www.emergentmind.com/topics/behavioral-cloning-bc"},{"title":"Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/html/2502.02853v1"},{"title":"The State of Robotics: Emerging Trends & Commercial Frontiers, Part I","url":"https://joannalichter.substack.com/p/the-state-of-robotics-emerging-trends"},{"title":"A framework for robotic manipulation tasks based on multiple zero shot models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-17015-z"},{"title":"Embodied large language models enable robots to complete complex tasks in unpredictable environments | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01005-x"}]

Based on the search results, here's what I found about information bottleneck approaches in robot manipulation:

## Key Research: BC-IB (2025)

The primary recent work is "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation," published at ICML 2025.

### What is BC-IB?

The approach incorporates the Information Bottleneck (IB) principle into Behavior Cloning (BC), which extends the idea of reducing redundancy by providing a structured framework for compressing irrelevant information while preserving task-relevant features.

### Key Findings

The researchers apply the Information Bottleneck principle to reduce the mutual information between the input and the latent space to remove task-irrelevant features, and by compressing input information, they suppress irrelevant information and improve performance in robotic manipulation tasks.

Empirically, minimizing redundancy in latent representations helps existing BC algorithms significantly improve generalization performance on the Cortexbench and LIBERO benchmarks across various settings, indirectly highlighting the considerable redundancy present in current robot trajectory datasets.

### Broader Impact

BC-IB integrates an information bottleneck into policy learning, compressing information irrelevant to tasks to maximize data utility, and BC-IB outperforms standard BC on widely used manipulation benchmarks like CortexBench and LIBERO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a467625-b1a4-4577-8001-ee44762849c2",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "5c0e8b6e-d213-4ccc-b6dd-c8b6d3ca7d29",
  "sourceToolAssistantUUID": "3a467625-b1a4-4577-8001-ee44762849c2",
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

_source line 12 · 2026-05-14T06:13:44.216Z_

<details><summary>↩ Tool result · `toolu_01R3vHL164pb9UePaEzQMiHL`</summary>

```text
Web search results for query: "adaptive token pruning vision language model robustness"

Links: [{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning Xue Li","url":"https://arxiv.org/pdf/2512.12701"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning","url":"https://arxiv.org/html/2512.12701v1"},{"title":"ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_ATP-LLaVA_Adaptive_Token_Pruning_for_Large_Vision_Language_Models_CVPR_2025_paper.pdf"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning | OpenReview","url":"https://openreview.net/forum?id=Vbqemx4YCC"},{"title":"[2512.12701] Efficient Vision-Language Reasoning via Adaptive Token Pruning","url":"https://arxiv.org/abs/2512.12701"},{"title":"AdaptInfer: Adaptive Token Pruning for Vision-Language ...","url":"https://arxiv.org/pdf/2508.06084"},{"title":"AdaptInfer: Adaptive Token Pruning for Vision–Language Model Inference with Dynamical Text Guidance","url":"https://arxiv.org/html/2508.06084"},{"title":"Revisiting Visual Token Pruning for Vision-Language Model ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Endo_Feather_the_Throttle_Revisiting_Visual_Token_Pruning_for_Vision-Language_Model_ICCV_2025_paper.pdf"},{"title":"LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models","url":"https://arxiv.org/html/2604.23950"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v1"}]

Based on the search results, here's what I found about adaptive token pruning in vision-language models and its robustness:

## Key Findings

**Adaptive Token Pruning (ATP)** is a dynamic inference mechanism that improves both efficiency and robustness of vision-language models (VLMs). ATP retains only the most informative tokens based on contextual relevance by assigning a hybrid importance score combining ViT CLS attention (intra-modal saliency) and CLIP text-image similarity (inter-modal relevance).

### Efficiency Gains
ATP reduces inference FLOPs by around 40% and achieves roughly 1.5x speedups in end-to-end latency with negligible accuracy loss (less than 1%). Unlike existing methods that require retraining or architectural modifications, ATP is a training-free module that can be easily integrated into existing VLM architectures.

### Robustness Benefits
Beyond computational efficiency, under Gaussian noise, blur, and occlusion, ATP prunes noisy background patches and retains more stable object regions, improving the model's ability to focus on important visual features, and when subjected to paraphrased questions or added distractor phrases, ATP removes irrelevant patches and appears to reduce hallucinated answers.

Observations suggest adaptive pruning suppresses spurious correlations, improving stability. These findings imply that resource-constrained inference and model reliability are not competing objectives.

### Related Approaches
Other recent work includes AdaptInfer and ATP-LLaVA, which employ different token pruning strategies while maintaining similar efficiency-robustness tradeoffs across various VLM architectures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "662b7ca4-3659-445e-b59b-8500de167ffe",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "287530b3-981b-4aa3-9e2b-e3f73579ce4a",
  "sourceToolAssistantUUID": "662b7ca4-3659-445e-b59b-8500de167ffe",
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

_source line 13 · 2026-05-14T06:13:44.336Z_

<details><summary>↩ Tool result · `toolu_01CBh5B2XcPoXvetJpFpFTPw`</summary>

```text
Web search results for query: "token pruning robustness VLA vision language action 2025 2026"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"GitHub - KwanWaiPang/Awesome-VLA: Paper Survey for Visual Language Action · GitHub","url":"https://github.com/KwanWaiPang/Awesome-VLA"},{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175v2"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"}]

I found several recent research papers on token pruning for Vision-Language-Action (VLA) models from 2025-2026. Here are the key findings:

## Recent VLA Token Pruning Research

### VLA-IAP (March 2026)
Vision-Language-Action (VLA) models have rapidly advanced embodied intelligence, but as model capacity and visual context length grow, the inference cost becomes a major bottleneck for real-world deployment on resource-constrained platforms. VLA-IAP (Interaction-Aligned Pruning) introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment. VLA-IAP achieves a 97.8% success rate with a 1.25x speedup on the LIBERO benchmark.

### Robustness Findings
VLA-IAP remains robust to sub-optimal grounding of the backbone by bypassing unreliable internal attention maps and utilizing explicit interaction alignment and geometric priors to preserve critical objects even under aggressive pruning ratios.

### VLA-Pruner (February 2026)
VLA-Pruner is a plug-and-play VLA-specific token pruning method that adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention for action-level importance.

### Other Recent Approaches
LightVLA is a differentiable token pruning framework that generates dynamic queries to evaluate visual token importance and adopts Gumbel softmax to enable differentiable token selection.

Recent work also includes research on adversarial robustness of large vision-language models under visual token compression.

These papers represent the cutting edge of efficient VLA model development, focusing on maintaining or improving task performance while reducing computational costs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f94d3051-8a24-4159-9e5a-2640f17bf0aa",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "575471c1-d264-4a91-80d3-fe265eb3f0c5",
  "sourceToolAssistantUUID": "f94d3051-8a24-4159-9e5a-2640f17bf0aa",
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

_source line 14 · 2026-05-14T06:13:45.232Z_

<details><summary>↩ Tool result · `toolu_01MoR1ghDVWve618MKKXsvbr`</summary>

```text
Web search results for query: "visual token selection robust robotics policy 2025 2026"

Links: [{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"2025-9-18 ThinkAct: Vision-Language-Action Reasoning via","url":"https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"}]

I've performed a web search for "visual token selection robust robotics policy 2025 2026" and found several relevant results about Vision-Language-Action (VLA) models and robotics research from 2025-2026.

Here are the key findings:

## Vision-Language-Action Models Overview

A vision-language-action model (VLA) is a class of multimodal foundation models that integrates vision, language and actions. Given an input image (or video) of the robot's surroundings and a text instruction, a VLA directly outputs low-level robot actions that can be executed to accomplish the requested task.

## Recent Developments (2025-2026)

Several state-of-the-art VLA models have been developed:

- The pi0 framework, from Physical Intelligence, uses a pre-trained VLM which connects to a smaller "action export" model, which uses a flow matching loss to predict actions.

- GR00T N1, released by NVIDIA in March 2025, is a VLA for humanoid robots that adopts a dual-system architecture.

- Gemini Robotics, introduced in 2025 by Google DeepMind, builds on top of the capabilities of Gemini 2.0 and extends these capabilities to the physical world, allowing robots to take actions.

## Robustness and Generalization

HybridVLA integrates diffusion and autoregressive decoding within a unified model and employs a "Collaborative Action Ensemble" mechanism to adaptively fuse them, selecting the most suitable generation strategy for different tasks, thereby improving control robustness.

There has been comprehensive analysis of 164 Vision-Language-Action (VLA) model submissions at ICLR 2026, discovering trends in discrete diffusion VLAs, reasoning models, and benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35b689e9-cc7a-48f0-89fa-1974b66b6128",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "bf6b2389-ef40-4be0-92f1-043a8d24d6c9",
  "sourceToolAssistantUUID": "35b689e9-cc7a-48f0-89fa-1974b66b6128",
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

_source line 15 · 2026-05-14T06:13:47.996Z_

Good, I'm finding several promising leads. Let me now run the next batch of searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf6b2389-ef40-4be0-92f1-043a8d24d6c9",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y8zwGKmF1UF8PG7kLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a3979ee-3dad-44f2-8c76-3a01deaf1dbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA13XMt1aeE9fso5P19ZVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 3219,
      "cache_read_input_tokens": 10622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3219,
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

_source line 16 · 2026-05-14T06:13:48.472Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QN1Lzpo1RXDJaSqfZJ5JE4`</summary>

```json
{
  "query": "multi-view information bottleneck token selection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a3979ee-3dad-44f2-8c76-3a01deaf1dbf",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y8zwGKmF1UF8PG7kLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8529560-0e5f-4344-b2ac-0ba912c34d86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA13XMt1aeE9fso5P19ZVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 3219,
      "cache_read_input_tokens": 10622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3219,
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

_source line 17 · 2026-05-14T06:13:49.414Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013d3dfz4grWmEVDFX59YLkt`</summary>

```json
{
  "query": "LIBERO-Plus robustness methods benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8529560-0e5f-4344-b2ac-0ba912c34d86",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y8zwGKmF1UF8PG7kLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6909975-5e60-4671-8a8d-c4fc28f1ee51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA13XMt1aeE9fso5P19ZVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 3219,
      "cache_read_input_tokens": 10622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3219,
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

_source line 18 · 2026-05-14T06:13:49.886Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019vKTvL9DH8STFuiYUv47od`</summary>

```json
{
  "query": "token compression adversarial robustness vision language model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6909975-5e60-4671-8a8d-c4fc28f1ee51",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y8zwGKmF1UF8PG7kLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce191a50-da8a-463c-ad0e-87b49b7fdd4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA13XMt1aeE9fso5P19ZVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 3219,
      "cache_read_input_tokens": 10622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3219,
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

_source line 19 · 2026-05-14T06:13:50.401Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QsVfa9saXnAdg6nM2Z3qNw`</summary>

```json
{
  "query": "Physical Intelligence UC Berkeley Stanford Google DeepMind VLA robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce191a50-da8a-463c-ad0e-87b49b7fdd4a",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1y8zwGKmF1UF8PG7kLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36fe8591-812d-4d8d-bd0e-15fe1b4cfa2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA13XMt1aeE9fso5P19ZVQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 3219,
      "cache_read_input_tokens": 10622,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3219
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 957,
          "output_tokens": 239,
          "cache_read_input_tokens": 10622,
          "cache_creation_input_tokens": 3219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3219,
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

_source line 20 · 2026-05-14T06:13:55.612Z_

<details><summary>↩ Tool result · `toolu_01QN1Lzpo1RXDJaSqfZJ5JE4`</summary>

```text
Web search results for query: "multi-view information bottleneck token selection 2025 2026"

Links: [{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy","url":"https://arxiv.org/html/2605.07931v1"},{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"On The Multi-View Information Bottleneck Representation | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel7/9965754/9965755/09965818.pdf"},{"title":"[2507.01728] Token Communication in the Era of Large Models: An Information Bottleneck-Based Approach","url":"https://arxiv.org/abs/2507.01728"},{"title":"Deep Multi-view Information Bottleneck Qi Wang∗ Claire Boudreau∗ Qixing Luo∗","url":"https://epubs.siam.org/doi/pdf/10.1137/1.9781611975673.5"},{"title":"Adaptive multi-view information bottleneck for multi-omics data clustering | Briefings in Bioinformatics | Oxford Academic","url":"https://academic.oup.com/bib/article/27/1/bbaf717/8423998"},{"title":"On The Multi-View Information Bottleneck Representation","url":"https://arxiv.org/pdf/2202.02684"},{"title":"Proceedings of the 2019 SIAM International Conference on Data Mining (SDM) | Deep Multi-view Information Bottleneck","url":"https://epubs.siam.org/doi/10.1137/1.9781611975673.5"},{"title":"Token Communication in the Era of Large Models: An Information Bottleneck-Based Approach","url":"https://arxiv.org/html/2507.01728v1"},{"title":"LEARNING ROBUST REPRESENTATIONS VIA MULTI- ...","url":"https://openreview.net/pdf?id=B1xwcyHFDr"}]

Based on the search results, I found several recent and relevant papers on multi-view information bottleneck and token selection from 2025-2026:

## Key Findings:

### 1. **Information Bottleneck for Token Merging in Vision Transformers**
A novel transformer block called IBTM (Transformer with Information Bottleneck inspired Token Merging) has been proposed that performs token merging in a learnable scheme. IBTM is compatible with many popular compact transformer networks, such as MobileViT and EfficientViT, and reduces FLOPs and inference time while maintaining or improving prediction accuracy.

### 2. **Multi-View Information Bottleneck in Recent Applications**
An adaptive multi-view information bottleneck approach (scAMVIB) has been developed for multi-omics data clustering that incorporates a maximum entropy-based adaptive weighting scheme, dynamically assigning weights to each omics view proportional to its information content.

### 3. **Token Communication with Information Bottleneck**
A generative information bottleneck (GenIB) principle has been proposed that facilitates the learning of tokens that preserve essential information while supporting reliable generation across multiple modalities, improving communication efficiency and reducing computational complexity.

### 4. **Visual Bandwidth Optimization with Token Selection**
An Adaptive Attention Pooling mechanism has been developed that distills each view into a single semantic latent token per frame, holding per-frame visual bandwidth at one token.

These recent works (from 2025-2026) demonstrate active research combining information bottleneck principles with token selection across various applications including vision transformers, multimodal communication, and multi-omics analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8529560-0e5f-4344-b2ac-0ba912c34d86",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "61bd5ef5-7984-4866-94e7-d6a9e0f02b52",
  "sourceToolAssistantUUID": "d8529560-0e5f-4344-b2ac-0ba912c34d86",
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

_source line 21 · 2026-05-14T06:13:58.560Z_

<details><summary>↩ Tool result · `toolu_01QsVfa9saXnAdg6nM2Z3qNw`</summary>

```text
Web search results for query: "Physical Intelligence UC Berkeley Stanford Google DeepMind VLA robustness 2025 2026"

Links: [{"title":"Chelsea Finn 353 Jane Stanford Way Stanford, CA 94305 cbﬁnn@cs.stanford.edu","url":"https://ai.stanford.edu/~cbfinn/_files/cv.pdf"},{"title":"A Survey: Learning Embodied Intelligence from Physical Simulators and World Models","url":"https://arxiv.org/html/2507.00917v1"},{"title":"Physical Intelligence Company Overview","url":"https://www.grishinrobotics.com/post/physical-intelligence-company-overview"},{"title":"A Comprehensive Survey on Embodied Intelligence: Advancements, Challenges, and Future Perspectives","url":"https://www.sciopen.com/article/10.26599/AIR.2024.9150042"},{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"},{"title":"Sherry Yang's Homepage","url":"https://sherryy.github.io/"},{"title":"Google DeepMind Introduces AI Model That Runs Locally on Robots | PYMNTS.com","url":"https://www.pymnts.com/news/artificial-intelligence/2025/google-deepmind-introduces-ai-model-runs-locally-robots/"},{"title":"2025 AI Safety Index - Future of Life Institute","url":"https://futureoflife.org/ai-safety-index-summer-2025/"},{"title":"Artificial Intelligence Index Report 2025","url":"https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf"},{"title":"Research — Google DeepMind","url":"https://deepmind.google/research/"}]

Based on the search results, here's what I found about Physical Intelligence, VLA robustness, and related developments:

## Physical Intelligence Company

Physical Intelligence was founded by former Google DeepMind and Berkeley researchers who began working on cross-embodiment learning in Q3 2023, and the company emerged from stealth in March 2024 with a $70 million seed round. The company's core objective involves creating universal robotic intelligence through their flagship π-zero model, which represents a significant advancement in Vision-Language-Action (VLA) technology that allows robots to understand visual inputs, process natural language commands, and execute appropriate physical actions in real-world environments.

In October 2024, the team published its first public demo of π₀, showing the same policy folding laundry, assembling boxes and performing warehouse induction, and later π₀ was open-sourced. In February 2025, the research blog unveiled Hi Robot, a vision-language-action planner layered on π₀ that improves instruction following by roughly 40 percent in benchmark tasks. In May 2025, PI released early results on π 0.5, demonstrating open-world generalization to completely unseen environments.

## VLA Robustness Challenges

Although current VLA models have made significant progress, these models often struggle to reliably handle tasks or environments they have not encountered before.

## Recent Google DeepMind VLA Developments

Google DeepMind introduced a vision language action model that runs locally on robotic devices without accessing a data network, with the new Gemini Robotics On-Device robotics foundation model featuring general-purpose dexterity and fast task adaptation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36fe8591-812d-4d8d-bd0e-15fe1b4cfa2c",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "45208c2e-e06b-4492-bc76-77b7250c9bca",
  "sourceToolAssistantUUID": "36fe8591-812d-4d8d-bd0e-15fe1b4cfa2c",
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

_source line 22 · 2026-05-14T06:13:58.618Z_

<details><summary>↩ Tool result · `toolu_019vKTvL9DH8STFuiYUv47od`</summary>

```text
Web search results for query: "token compression adversarial robustness vision language model 2025 2026"

Links: [{"title":"Less Is More — Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models","url":"https://arxiv.org/html/2601.12042"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/html/2601.21531"},{"title":"[2601.21531] On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/abs/2601.21531"},{"title":"VISUAL TOKEN COMPRESSION ENHANCES MODEL ...","url":"https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf"},{"title":"Chain of Attack: On the Robustness of Vision-Language Models Against Transfer-Based Adversarial Attacks | Request PDF","url":"https://www.researchgate.net/publication/394575069_Chain_of_Attack_On_the_Robustness_of_Vision-Language_Models_Against_Transfer-Based_Adversarial_Attacks"},{"title":"Enhancing Adversarial Robustness of Vision-Language Models through Low-Rank Adaptation | Proceedings of the 2025 International Conference on Multimedia Retrieval","url":"https://dl.acm.org/doi/10.1145/3731715.3733324"},{"title":"Language-Guided Token Compression with Reinforcement Learning in Large","url":"https://arxiv.org/pdf/2603.13394"},{"title":"GitHub - yaolinli/MLLM-Token-Compression: Towards Efficient Multimodal Large Language Models: A Survey on Token Compression · GitHub","url":"https://github.com/yaolinli/MLLM-Token-Compression"},{"title":"GitHub - cokeshao/Awesome-Multimodal-Token-Compression: [TMLR 2026] Survey: https://arxiv.org/pdf/2507.20198 · GitHub","url":"https://github.com/cokeshao/Awesome-Multimodal-Token-Compression"}]

Based on the web search results, here are the key findings about token compression and adversarial robustness in vision language models from 2025-2026:

## Key Research Findings

### Security Vulnerabilities of Token Compression

While models are generally robust to small random perturbations under full-token inference, they become highly vulnerable once compression is activated, with vulnerability increasing as the token retention rate decreases. This presents a significant trade-off in efficient LVLM deployment.

Adversarial inputs may appear benign during standard (uncompressed) offline testing yet reliably induce failures when the system operates under resource constraints.

### The Optimization-Inference Mismatch Problem

Existing encoder-based attacks can substantially overestimate the robustness of compressed LVLMs, due to an optimization-inference mismatch: perturbations are optimized on the full-token representation, while inference is performed through a token-compression bottleneck.

### Proposed Solutions

Recent research has introduced defensive approaches:

- The Compression-AliGnEd attack (CAGE) aligns perturbation optimization with compression inference without assuming access to the deployed compression mechanism, combining expected feature disruption and rank distortion alignment.

- Researchers have begun investigating how visual token compression influences the robustness of VLMs against jailbreak attacks and hallucinations.

### Practical Implications

Token compression has become indispensable for deploying LVLMs in real-time, safety-critical applications (e.g., autonomous driving and robotics) due to strict latency and energy constraints.

### Need for Security-Aware Design

There is a need for security-aware compression mechanisms that balance efficiency and robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce191a50-da8a-463c-ad0e-87b49b7fdd4a",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "c9f74a3f-3873-4b09-8a82-72533981f4b2",
  "sourceToolAssistantUUID": "ce191a50-da8a-463c-ad0e-87b49b7fdd4a",
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

_source line 23 · 2026-05-14T06:13:59.870Z_

<details><summary>↩ Tool result · `toolu_013d3dfz4grWmEVDFX59YLkt`</summary>

```text
Web search results for query: "LIBERO-Plus robustness methods benchmark 2026"

Links: [{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"}]

Based on the search results, here's comprehensive information about LIBERO-Plus:

## Overview

LIBERO-Plus is a comprehensive, automatic, and fine-grained evaluation framework with controlled perturbations across seven dimensions: object layouts, camera viewpoints, robot initial states, language instructions, lighting conditions, background textures, and sensor noise.

## Key Findings

Systematic analysis of ten state-of-the-art models reveals consistent brittleness beneath apparent competence, with performance dropping from 95% to below 30% under modest perturbations.

Notably, models tend to ignore language instructions completely, despite their otherwise sophisticated capabilities.

## Benchmark Structure

LIBERO-Plus offers a robust benchmarking framework with 7 perturbation dimensions and 21 sub-dimensions, providing a fine-grained difficulty scale from L1 to L5, allowing users to systematically assess model performance across various challenges. The benchmark comprises 10,030 tasks organized across seven perturbation factors and twenty-one underlying components.

## Robustness Methods

The paper also demonstrates a robustness improvement approach: A proposed method achieves the highest overall success rate (79.6%), outperforming baseline models, and exhibits dramatic improvement in camera view robustness (92.8%), surpassing the next best model by 37.2 percentage points.

The research is available on arXiv (paper 2510.13626) and includes an official GitHub repository for implementation and benchmarking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6909975-5e60-4671-8a8d-c4fc28f1ee51",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "ac8fe02c-c07d-4d45-8127-93cd7b7e55be",
  "sourceToolAssistantUUID": "b6909975-5e60-4671-8a8d-c4fc28f1ee51",
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

_source line 24 · 2026-05-14T06:14:04.491Z_

I found several interesting leads. Let me now run more targeted follow-up searches to dig deeper into the specific papers and potential competitors I've identified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac8fe02c-c07d-4d45-8127-93cd7b7e55be",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yA5V8yNWFFrbSNws1i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e7ccaae-e5ee-4fc1-9d02-99a934136464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHEBBxGytqMA6xsRzDXBKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1940,
      "cache_creation_input_tokens": 3131,
      "cache_read_input_tokens": 13841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3131,
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

_source line 25 · 2026-05-14T06:14:05.450Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xmttd28xGLJjKkvWFjF1CJ`</summary>

```json
{
  "query": "VLA-Pruner temporal-aware dual-level visual token pruning arXiv 2511.16449"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e7ccaae-e5ee-4fc1-9d02-99a934136464",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yA5V8yNWFFrbSNws1i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cec86e4f-af7e-459b-ae88-f6ead43b9b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHEBBxGytqMA6xsRzDXBKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1940,
      "cache_creation_input_tokens": 3131,
      "cache_read_input_tokens": 13841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3131,
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

_source line 26 · 2026-05-14T06:14:06.380Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0111xe869mFN4Xo8e32xP5zu`</summary>

```json
{
  "query": "SpecPrune-VLA action-aware self-speculative pruning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cec86e4f-af7e-459b-ae88-f6ead43b9b5a",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yA5V8yNWFFrbSNws1i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7321ccb0-e72b-47f7-bb0e-5f51bc537717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHEBBxGytqMA6xsRzDXBKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1940,
      "cache_creation_input_tokens": 3131,
      "cache_read_input_tokens": 13841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3131,
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

_source line 27 · 2026-05-14T06:14:06.867Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NV72jdqk9ZAZcjQCXis5bo`</summary>

```json
{
  "query": "VLA-Cache adaptive token caching vision language action manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7321ccb0-e72b-47f7-bb0e-5f51bc537717",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yA5V8yNWFFrbSNws1i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "284a4ee5-862e-4c01-8caa-1336eceb72aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHEBBxGytqMA6xsRzDXBKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1940,
      "cache_creation_input_tokens": 3131,
      "cache_read_input_tokens": 13841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3131,
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

_source line 28 · 2026-05-14T06:14:07.459Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hr1jErxvfi6JXxQn4dgnzF`</summary>

```json
{
  "query": "ATP-LLaVA adaptive token pruning CVPR 2025 robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "284a4ee5-862e-4c01-8caa-1336eceb72aa",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yA5V8yNWFFrbSNws1i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d6afc49-d05e-4b5f-9ac2-9a33d54fe424",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHEBBxGytqMA6xsRzDXBKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1940,
      "cache_creation_input_tokens": 3131,
      "cache_read_input_tokens": 13841,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1940,
          "output_tokens": 268,
          "cache_read_input_tokens": 13841,
          "cache_creation_input_tokens": 3131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3131,
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

_source line 29 · 2026-05-14T06:14:12.112Z_

<details><summary>↩ Tool result · `toolu_01Xmttd28xGLJjKkvWFjF1CJ`</summary>

```text
Web search results for query: "VLA-Pruner temporal-aware dual-level visual token pruning arXiv 2511.16449"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"[2603.06480] History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/abs/2603.06480"},{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766"},{"title":"Efficient Token Pruning for LLaDA-V","url":"https://arxiv.org/html/2601.20168"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614"}]

I found the paper you're looking for! Here are the key details about VLA-Pruner:

## VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning

VLA-Pruner addresses the problem that Vision-Language-Action (VLA) models have shown great promise for embodied AI, yet the heavy computational cost of processing continuous visual streams severely limits their real-time deployment.

### The Problem It Solves

Existing VLM-specific token pruning methods select tokens based solely on semantic salience metrics (e.g., prefill attention), while overlooking the VLA's intrinsic dual-system nature of high-level semantic understanding and low-level action execution. Consequently, these methods bias token retention toward semantic cues, discard critical information for action generation, and significantly degrade VLA performance.

### The Proposed Solution

VLA-Pruner is a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation. 

VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance.

The paper was published on February 10, 2026, and is available on arXiv at [https://arxiv.org/abs/2511.16449](https://arxiv.org/abs/2511.16449).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cec86e4f-af7e-459b-ae88-f6ead43b9b5a",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "79ca923a-8572-4402-9783-432a547dae00",
  "sourceToolAssistantUUID": "cec86e4f-af7e-459b-ae88-f6ead43b9b5a",
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

_source line 30 · 2026-05-14T06:14:13.202Z_

<details><summary>↩ Tool result · `toolu_01NV72jdqk9ZAZcjQCXis5bo`</summary>

```text
Web search results for query: "VLA-Cache adaptive token caching vision language action manipulation 2025"

Links: [{"title":"[2502.02175] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/abs/2502.02175"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://vla-cache.github.io/"},{"title":"GitHub - siyuhsu/vla-cache: [NeurIPS 2025] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching · GitHub","url":"https://github.com/siyuhsu/vla-cache"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching | OpenReview","url":"https://openreview.net/forum?id=QZYZ0Xm58q"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175v2"},{"title":"NeurIPS Poster VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118121"},{"title":"Learning to Accelerate Vision-Language-Action Models through Adaptive Visual Token Caching - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260200686W/abstract"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-p81219/"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation ...","url":"https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf"}]

Based on the search results, here's comprehensive information about VLA-Cache:

## Overview

VLA-Cache is a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames. Vision-Language-Action (VLA) models have demonstrated strong multi-modal reasoning capabilities for action generation from visual perception and language instructions, but their substantial computational cost poses a challenge for real-time robotic control.

## Key Mechanisms

VLA-Cache employs two primary strategies:

1. **Static Token Reuse**: Exploiting temporal continuity in robotic manipulation, VLA-Cache identifies minimally changed tokens between adjacent frames and reuses their cached key-value representations, thereby circumventing redundant computations.

2. **Task-Relevance Filtering and Adaptive Layer Strategy**: VLA-Cache selectively re-computes task-relevant tokens that are environmentally sensitive, and introduces a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens for recomputation.

## Performance Results

Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7x speedup in CUDA latency and a 15% increase in control frequency, with negligible loss on task success rate.

## Publication Status

The work was presented as a poster at NeurIPS 2025 and is available on arXiv (2502.02175) with code and project information available at vla-cache.github.io.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "284a4ee5-862e-4c01-8caa-1336eceb72aa",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "663d42a2-5894-4cc8-af88-f9ee7b65cb5f",
  "sourceToolAssistantUUID": "284a4ee5-862e-4c01-8caa-1336eceb72aa",
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

_source line 31 · 2026-05-14T06:14:14.075Z_

<details><summary>↩ Tool result · `toolu_0111xe869mFN4Xo8e32xP5zu`</summary>

```text
Web search results for query: "SpecPrune-VLA action-aware self-speculative pruning 2025 2026"

Links: [{"title":"[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/abs/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | Request PDF","url":"https://www.researchgate.net/publication/395354566_SpecPrune-VLA_Accelerating_Vision-Language-Action_Models_via_Action-Aware_Self-Speculative_Pruning"},{"title":"Specprune-vla Boosts Vision-Language-Action Models, Avoiding Over 20% Success Rate Drops With Smart Pruning","url":"https://quantumzeitgeist.com/faster-models-performance-specprune-vla-boosts-vision-language-action-avoiding-success/"},{"title":"SPECPRUNE-VLA:","url":"https://openreview.net/pdf/f898de78034757b0bb38f30b7b6fd21bca97b4ad.pdf"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"},{"title":"GitHub - KwanWaiPang/Awesome-VLA: Paper Survey for Visual Language Action · GitHub","url":"https://github.com/KwanWaiPang/Awesome-VLA"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://arxiv.org/html/2507.22424"}]

Based on the search results, here's comprehensive information about SpecPrune-VLA:

## Overview

SpecPrune-VLA is a training-free, two-level pruning method with heuristic control designed to accelerate Vision-Language-Action (VLA) models. It has been applied to accelerate Vision-Language-Action (VLA) model inference, addressing limitations in existing acceleration methods that focus on local information from the current action step and ignore global context, leading to >20% success rate drop and limited speedup in some scenarios.

## Key Innovation

The method identifies spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and proposes the key insight that token selection should combine local information with global context of the model.

## Technical Components

The approach consists of three main components:

1. **Action-Level Static Pruning**: It leverages global history and local attention to statically reduce visual tokens per action.

2. **Layer-Level Dynamic Pruning**: It prunes tokens adaptively per layer based on layer-wise importance.

3. **Action-Aware Controller**: It classifies actions as coarse- or fine-grained by the speed of the end effector and adjusts pruning aggressiveness accordingly.

## Performance Results

SpecPrune-VLA achieves up to 1.57× speedup in LIBERO simulation and 1.70× on real-world tasks, with negligible success rate degradation.

## Publication Status

The paper was first submitted on September 6, 2025, with an updated version on February 9, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7321ccb0-e72b-47f7-bb0e-5f51bc537717",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "bc106f9b-daf7-44b9-ad0f-87cd0c612fcb",
  "sourceToolAssistantUUID": "7321ccb0-e72b-47f7-bb0e-5f51bc537717",
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

_source line 32 · 2026-05-14T06:14:17.110Z_

<details><summary>↩ Tool result · `toolu_01Hr1jErxvfi6JXxQn4dgnzF`</summary>

```text
Web search results for query: "ATP-LLaVA adaptive token pruning CVPR 2025 robustness"

Links: [{"title":"ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_ATP-LLaVA_Adaptive_Token_Pruning_for_Large_Vision_Language_Models_CVPR_2025_paper.pdf"},{"title":"CVPR Poster ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models","url":"https://cvpr.thecvf.com/virtual/2025/poster/33610"},{"title":"Adaptive Token Pruning for Large Vision Language Models","url":"https://openaccess.thecvf.com/content/CVPR2025/html/Ye_ATP-LLaVA_Adaptive_Token_Pruning_for_Large_Vision_Language_Models_CVPR_2025_paper.html"},{"title":"[2412.00447] ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models","url":"https://arxiv.org/abs/2412.00447"},{"title":"ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models","url":"https://arxiv.org/html/2412.00447v1"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning","url":"https://arxiv.org/html/2512.12701"},{"title":"Efficient Vision-Language Reasoning via Adaptive Token Pruning | OpenReview","url":"https://openreview.net/forum?id=Vbqemx4YCC"},{"title":"[2512.12701] Efficient Vision-Language Reasoning via Adaptive Token Pruning","url":"https://arxiv.org/abs/2512.12701"}]

I found comprehensive information about ATP-LLaVA. Here are the key findings:

## ATP-LLaVA Overview

ATP-LLaVA is a novel approach that adaptively determines instance-specific token pruning ratios for each LLM layer by introducing an Adaptive Token Pruning (ATP) module, which computes the importance score and pruning threshold based on input instance adaptively.

## Core Components

The ATP module can be seamlessly integrated between any two LLM layers with negligible computational overhead. Additionally, the approach develops a Spatial Augmented Pruning (SAP) strategy that prunes visual tokens with both token redundancy and spatial modeling perspectives.

## Performance and Efficiency

The approach reduces the average token count by 75% while maintaining performance, with only a minimal 1.9% degradation across seven widely used benchmarks.

## Robustness Findings

The impact of pruning ratio on performance is layer-wise, with shallower layers being more sensitive to pruning and deeper layers exhibiting greater robustness. Furthermore, the pruning ratio's impact is instance-wise, with fine-grained tasks such as instance counting and spatial relation demanding detailed visual information, necessitating the retention of more tokens at each layer to prevent performance degradation.

## Publication

This CVPR paper is the Open Access version, provided by the Computer Vision Foundation, and the final published version of the proceedings is available on IEEE Xplore.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d6afc49-d05e-4b5f-9ac2-9a33d54fe424",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "ea8e1de9-32e0-4333-830f-3a453d7020ee",
  "sourceToolAssistantUUID": "0d6afc49-d05e-4b5f-9ac2-9a33d54fe424",
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

_source line 33 · 2026-05-14T06:14:19.755Z_

Excellent - several new papers emerging. Let me search for more specific leads that appeared in those results, plus additional targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea8e1de9-32e0-4333-830f-3a453d7020ee",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yBMAjqchaQBXW7K9zK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41852040-ad38-4cd0-ae72-438d46861270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xcMYXek1L8qmLBx4pGSzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6099,
      "cache_read_input_tokens": 16972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6099,
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

_source line 34 · 2026-05-14T06:14:20.668Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BBihGTv7m39YRySMxxZgCx`</summary>

```json
{
  "query": "ETA-VLA efficient token adaptation temporal fusion intra-LLM sparsification arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41852040-ad38-4cd0-ae72-438d46861270",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yBMAjqchaQBXW7K9zK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c0f10f6-c683-4ece-82b3-7a86674332f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xcMYXek1L8qmLBx4pGSzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6099,
      "cache_read_input_tokens": 16972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6099,
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

_source line 35 · 2026-05-14T06:14:21.191Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L8ZkDYgHonsKkPgBRxUPXh`</summary>

```json
{
  "query": "SP-VLA joint model scheduling token pruning VLA acceleration arXiv 2506"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c0f10f6-c683-4ece-82b3-7a86674332f2",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yBMAjqchaQBXW7K9zK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ab6b023-01a2-4ef9-b0b4-f4e7f12dbf6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xcMYXek1L8qmLBx4pGSzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6099,
      "cache_read_input_tokens": 16972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6099,
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

_source line 36 · 2026-05-14T06:14:21.734Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011JjvCdoL3sSk7AwECk2W7i`</summary>

```json
{
  "query": "environment-aware adaptive pruning interleaved inference orchestration VLA arXiv 2602.00780"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ab6b023-01a2-4ef9-b0b4-f4e7f12dbf6b",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yBMAjqchaQBXW7K9zK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b00d466-28e7-4d01-b85f-31ecfc8f86db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xcMYXek1L8qmLBx4pGSzv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6099,
      "cache_read_input_tokens": 16972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6099,
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

_source line 37 · 2026-05-14T06:14:22.152Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PZBiZmCyNd35wDDgJzAxwP`</summary>

```json
{
  "query": "LearnPruner rethinking attention-based token pruning vision language models arXiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b00d466-28e7-4d01-b85f-31ecfc8f86db",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yBMAjqchaQBXW7K9zK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10f072c6-3e1f-4f74-b5b8-5cb07e70c982",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xcMYXek1L8qmLBx4pGSzv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6099,
      "cache_read_input_tokens": 16972,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6099
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 16972,
          "cache_creation_input_tokens": 6099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6099,
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

_source line 38 · 2026-05-14T06:14:27.718Z_

<details><summary>↩ Tool result · `toolu_01BBihGTv7m39YRySMxxZgCx`</summary>

```text
Web search results for query: "ETA-VLA efficient token adaptation temporal fusion intra-LLM sparsification arXiv 2603"

Links: [{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766v1"},{"title":"[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.25766"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"Efficient LLM Serving for Agentic Workflows:","url":"https://arxiv.org/pdf/2603.16104"},{"title":"ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time","url":"https://arxiv.org/html/2410.06625v1"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"[2508.19257] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.19257"}]

I found the paper you're looking for. Here's what I found:

## ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification

ETA-VLA is an Efficient Token Adaptation framework for VLA models that processes the past n frames of multi-view images and introduces a novel Intra-LLM Sparse Aggregator (ILSA).

### Key Components

The framework introduces two complementary components: a Temporal Fusion Module (TFM) and an Intra-LLM Sparse Aggregator (ILSA).

**Temporal Fusion Module**: TFM operates on the visual encoder features before the LLM, adaptively fusing multi-frame historical features into a concise representation via transformer and learnable weights, effectively compressing the temporal dimension while preserving critical motion cues.

**Intra-LLM Sparse Aggregator**: Drawing inspiration from human driver attention allocation, ILSA dynamically identifies and prunes redundant visual tokens guided by textual queries and temporal consistency, utilizing a text-guided scoring mechanism alongside a diversity-preserving sparsification strategy to select a sparse subset of critical tokens.

### Performance

ETA-VLA achieves driving performance comparable to state-of-the-art baselines while reducing computational FLOPs by approximately 32%, pruning 85% of visual tokens and reducing inference FLOPs by 61% while retaining 94% of the original accuracy on the NAVSIM v2 benchmark.

The paper was published on arXiv on March 26, 2026 with the identifier 2603.25766.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c0f10f6-c683-4ece-82b3-7a86674332f2",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "f07e2f9e-9bf7-4410-9f47-3ef66ad4956a",
  "sourceToolAssistantUUID": "6c0f10f6-c683-4ece-82b3-7a86674332f2",
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

_source line 39 · 2026-05-14T06:14:27.825Z_

<details><summary>↩ Tool result · `toolu_011JjvCdoL3sSk7AwECk2W7i`</summary>

```text
Web search results for query: "environment-aware adaptive pruning interleaved inference orchestration VLA arXiv 2602.00780"

Links: [{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"},{"title":"[2602.00780] Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.00780"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"RAP: Runtime-Adaptive Pruning for LLM Inference","url":"https://arxiv.org/html/2505.17138v1"},{"title":"[2602.07804] Pruning as a Cooperative Game: Surrogate-Assisted Layer Contribution Estimation for Large Language Models","url":"https://arxiv.org/abs/2602.07804"},{"title":"[2302.04089] ZipLM: Inference-Aware Structured Pruning of Language Models","url":"https://arxiv.org/abs/2302.04089"},{"title":"Runtime Adaptive Pruning for LLM Inference","url":"https://arxiv.org/html/2505.17138v4"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/html/2509.22093v1"},{"title":"Adaptive Pruning for Large Language Models with Structural Importance Awareness","url":"https://arxiv.org/html/2412.15127v1"}]

I found the arXiv paper you're searching for! Here are the key details:

**Paper Title:** Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models

**Main Contribution:** The paper proposes EcoVLA, a training-free, plug-and-play adaptive pruning framework that comprises two components: Environment-aware Adaptive Pruning (EAP) and Interleaved Inference Orchestration (I2O).

**Key Components:**
- EAP is a lightweight adaptive channel pruning method that incorporates the temporal consistency of the physical environment to update sparsity patterns
- I2O leverages the FLOPs bubbles inherent in VLA inference to schedule the pruning method in parallel, ensuring negligible impact on latency

**Performance:** EcoVLA delivers state-of-the-art performance, achieving up to 1.60× speedup with only a 0.5% degradation when combined with token pruning.

**Motivation:** While Vision-Language-Action (VLA) models hold promise in embodied intelligence, their large parameter counts lead to substantial inference latency. However, as the environment evolves during VLA execution, the optimal sparsity patterns change accordingly.

The paper was published on arXiv on January 31, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b00d466-28e7-4d01-b85f-31ecfc8f86db",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "75366aa7-a165-4d2c-b84c-7002d41366e4",
  "sourceToolAssistantUUID": "3b00d466-28e7-4d01-b85f-31ecfc8f86db",
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

_source line 40 · 2026-05-14T06:14:27.946Z_

<details><summary>↩ Tool result · `toolu_01L8ZkDYgHonsKkPgBRxUPXh`</summary>

```text
Web search results for query: "SP-VLA joint model scheduling token pruning VLA acceleration arXiv 2506"

Links: [{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"Preprint. SP-VLA: A JOINT MODEL SCHEDULING AND TOKEN","url":"https://arxiv.org/pdf/2506.12723"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration | OpenReview","url":"https://openreview.net/forum?id=RwdGIIjPlC"},{"title":"[2506.12723] SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/abs/2506.12723"},{"title":"(PDF) SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://www.researchgate.net/publication/392736853_SP-VLA_A_Joint_Model_Scheduling_and_Token_Pruning_Approach_for_VLA_Model_Acceleration"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.12723v3"},{"title":"dblp: SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration.","url":"https://dblp.org/rec/journals/corr/abs-2506-12723.html"},{"title":"GitHub - ChildTang/SP-VLA · GitHub","url":"https://github.com/ChildTang/SP-VLA"},{"title":"Publications - Jiajun Fan","url":"https://www.jiajunfan.com/publications/"},{"title":"[Literature Review] SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://www.themoonlight.io/en/review/sp-vla-a-joint-model-scheduling-and-token-pruning-approach-for-vla-model-acceleration"}]

I found the paper you're looking for! Here's a summary of the research:

## SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration

Vision-Language-Action (VLA) models have attracted increasing attention for their strong control capabilities. However, their high computational cost and low execution frequency hinder their suitability for real-time tasks such as robotic manipulation and autonomous navigation.

### Key Approach

SP-VLA is a unified framework that accelerates VLA models by jointly scheduling models and pruning tokens. The method addresses two main types of redundancy:

1. **Temporal Redundancy**: The framework designs an action-aware model scheduling mechanism that reduces temporal redundancy by dynamically switching between VLA model and a lightweight generator. VLA actions are categorized into deliberative and intuitive, assigning the former to the VLA model and the latter to the lightweight generator, enabling frequency-adaptive execution.

2. **Spatial Redundancy**: A spatio-semantic dual-aware token pruning method is developed where tokens are classified into spatial and semantic types and pruned based on their dual-aware importance to accelerate VLA inference.

### Results

The method achieves 1.5× lossless acceleration in LIBERO and 2.4× in SimplerEnv, with up to 6% average performance gain.

The paper (arXiv:2506.12723) was authored by Ye Li, Yuan Meng, Zewen Sun, and collaborators, and has been accepted to ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ab6b023-01a2-4ef9-b0b4-f4e7f12dbf6b",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "8491825a-b9c1-4a46-b0a4-7ce9f8811e07",
  "sourceToolAssistantUUID": "7ab6b023-01a2-4ef9-b0b4-f4e7f12dbf6b",
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

_source line 41 · 2026-05-14T06:14:30.242Z_

<details><summary>↩ Tool result · `toolu_01PZBiZmCyNd35wDDgJzAxwP`</summary>

```text
Web search results for query: "LearnPruner rethinking attention-based token pruning vision language models arXiv 2604"

Links: [{"title":"[2604.23950] LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models","url":"https://arxiv.org/abs/2604.23950"},{"title":"LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models","url":"https://arxiv.org/html/2604.23950"},{"title":"LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models | OpenReview","url":"https://openreview.net/forum?id=Dxb6gBJHby"},{"title":"RETHINKING ATTENTION-BASED TOKEN PRUNING IN ...","url":"https://openreview.net/pdf/e94a30dd71e7b6a0a1a27082eb13b96f3442bf87.pdf"},{"title":"[2603.01236] AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models","url":"https://arxiv.org/abs/2603.01236"},{"title":"LVPruning: An Effective yet Simple Language-Guided Vision Token Pruning Approach for Multi-modal Large Language Models","url":"https://arxiv.org/html/2501.13652"},{"title":"AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models","url":"https://arxiv.org/html/2603.01236v1"},{"title":"Attention Debiasing for Token Pruning in Vision–Language Models","url":"https://arxiv.org/html/2508.17807"},{"title":"Attention Debiasing for Token Pruning in Vision Language Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2508.17807v2"},{"title":"[2508.17807] Attention Debiasing for Token Pruning in Vision Language Models","url":"https://arxiv.org/abs/2508.17807"}]

I found the paper you're looking for! Here's information about LearnPruner:

## LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models

LearnPruner addresses the computational challenges of Vision-Language Models (VLMs) which impose significant computational burdens due to long visual sequence inputs. The paper is available on arXiv as paper 2604.23950.

### Key Findings and Approach

The authors find that vision encoders suffer from attention sink, leading to poor focus on informative foreground regions, while in LLMs, text-to-vision attention demonstrates resistance to attention bias and enables effective pruning guidance in middle layers.

Based on these observations, LearnPruner proposes a two-stage token pruning framework that first removes redundant vision tokens via a learnable pruning module after the vision encoder, then retains only task-relevant tokens in the LLM's middle layer.

### Results

Experimental results show that LearnPruner can preserve approximately 95% of the original performance while using only 5.5% of vision tokens, and achieve 3.2× inference acceleration, demonstrating a superior accuracy-efficiency trade-off.

The paper was authored by Rinyoichi Takezoe and colleagues and was submitted on April 27, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10f072c6-3e1f-4f74-b5b8-5cb07e70c982",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "607cca49-6f93-40a6-81ea-d97f7c42374b",
  "sourceToolAssistantUUID": "10f072c6-3e1f-4f74-b5b8-5cb07e70c982",
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

_source line 42 · 2026-05-14T06:14:36.339Z_

Good, finding many relevant papers. Let me continue with more targeted searches to find papers specifically on robustness (not just efficiency) and IB-related approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "607cca49-6f93-40a6-81ea-d97f7c42374b",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yCKMsMfKaf8QxR48Ty",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "177117cd-2c2c-4c7f-b53c-a5cf064627b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUB7zF4fmPStGY5g4QCTUa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4004,
      "cache_read_input_tokens": 23071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4004,
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

_source line 43 · 2026-05-14T06:14:36.538Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HAb73SCPnG74rxFZ8rGa7v`</summary>

```json
{
  "query": "\"visual token compression enhances model robustness\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "177117cd-2c2c-4c7f-b53c-a5cf064627b9",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yCKMsMfKaf8QxR48Ty",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3c87902-b068-45cb-b4c5-114c6d151e44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUB7zF4fmPStGY5g4QCTUa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4004,
      "cache_read_input_tokens": 23071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4004,
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

_source line 44 · 2026-05-14T06:14:36.654Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M5wWYVjYUPL3aEDr7Lyqrz`</summary>

```json
{
  "query": "CAGE compression-aligned attack adversarial robustness token compression VLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3c87902-b068-45cb-b4c5-114c6d151e44",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yCKMsMfKaf8QxR48Ty",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb9d1bd6-f4da-474c-aa92-f0be15911038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUB7zF4fmPStGY5g4QCTUa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4004,
      "cache_read_input_tokens": 23071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4004,
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

_source line 45 · 2026-05-14T06:14:36.811Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KsafVs9vmq4qajYLaRqtwx`</summary>

```json
{
  "query": "GenIB generative information bottleneck token communication large models arXiv 2507"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb9d1bd6-f4da-474c-aa92-f0be15911038",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yCKMsMfKaf8QxR48Ty",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e26cb55b-49af-4357-8fbc-496a2a554492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUB7zF4fmPStGY5g4QCTUa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4004,
      "cache_read_input_tokens": 23071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4004,
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

_source line 46 · 2026-05-14T06:14:37.164Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015wzoJd1zvSxfhaMcDfnD5T`</summary>

```json
{
  "query": "IBTM information bottleneck token merging vision transformer 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e26cb55b-49af-4357-8fbc-496a2a554492",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yCKMsMfKaf8QxR48Ty",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7445ae23-f13a-4336-91c0-3193ec88ad2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUB7zF4fmPStGY5g4QCTUa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4004,
      "cache_read_input_tokens": 23071,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 23071,
          "cache_creation_input_tokens": 4004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4004,
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

_source line 47 · 2026-05-14T06:14:42.962Z_

<details><summary>↩ Tool result · `toolu_01KsafVs9vmq4qajYLaRqtwx`</summary>

```text
Web search results for query: "GenIB generative information bottleneck token communication large models arXiv 2507"

Links: [{"title":"Token Communication in the Era of Large Models: An Information Bottleneck-Based Approach","url":"https://arxiv.org/html/2507.01728v1"},{"title":"[2507.01728] Token Communication in the Era of Large Models: An Information Bottleneck-Based Approach","url":"https://arxiv.org/abs/2507.01728"},{"title":"Token Communication in the Era of Large Models","url":"https://arxiv.org/pdf/2507.01728"},{"title":"Token Communication in the Era of Large Models: An Information Bottleneck-Based Approach | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11215621/"},{"title":"Deconstructing Generative Diversity: An Information Bottleneck Analysis of Discrete Latent Generative Models","url":"https://arxiv.org/html/2512.01831"},{"title":"When Tokens Talk Too Much: A Survey of Multimodal Long-Context Token Compression across Images, Videos, and Audios","url":"https://arxiv.org/html/2507.20198v4"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v1"},{"title":"[2512.01831] Deconstructing Generative Diversity: An Information Bottleneck Analysis of Discrete Latent Generative Models","url":"https://arxiv.org/abs/2512.01831"},{"title":"Computer Science Jul 2025","url":"https://www.arxiv.org/list/cs/2025-07?skip=2975&show=25"},{"title":"Token Communications: A Large Model-Driven Framework for Cross-modal Context-aware Semantic Communications","url":"https://arxiv.org/html/2502.12096v3"}]

I found the paper you're looking for! Here's what I found:

## Paper Summary

The paper "Token Communication in the Era of Large Models: An Information Bottleneck-Based Approach" proposes UniToCom, a unified token communication paradigm that treats tokens as the fundamental units for both processing and wireless transmission, and proposes a generative information bottleneck (GenIB) principle, which facilitates the learning of tokens that preserve essential information while supporting reliable generation across multiple modalities.

## Key Contributions

GenIB-based tokenization is conducive to improving communication efficiency and reducing computational complexity. Additionally, the paper develops σ-GenIB to address the challenges of variance collapse in autoregressive modeling, maintaining representational diversity and stability.

The work employs a causal Transformer-based multimodal large language model (MLLM) at the receiver to unify the processing of both discrete and continuous tokens under the next-token prediction paradigm.

The paper (arXiv:2507.01728) was published on July 2, 2025, and demonstrates the effectiveness of the GenIB principle and MLLM integration for improving both multimodal understanding and generation performance in wireless communication networks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e26cb55b-49af-4357-8fbc-496a2a554492",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "c59a0e0d-bb0f-4da9-883b-19689f02724c",
  "sourceToolAssistantUUID": "e26cb55b-49af-4357-8fbc-496a2a554492",
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

_source line 48 · 2026-05-14T06:14:43.120Z_

<details><summary>↩ Tool result · `toolu_01HAb73SCPnG74rxFZ8rGa7v`</summary>

```text
Web search results for query: ""visual token compression enhances model robustness" ICLR 2026"

Links: [{"title":"VISUAL TOKEN COMPRESSION ENHANCES MODEL ...","url":"https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf"},{"title":"ICLR Poster Prune Redundancy, Preserve Essence: Vision Token Compression in VLMs via Synergistic Importance-Diversity","url":"https://iclr.cc/virtual/2026/poster/10008000"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"GitHub - cokeshao/Awesome-Multimodal-Token-Compression: [TMLR 2026] Survey: https://arxiv.org/pdf/2507.20198 · GitHub","url":"https://github.com/cokeshao/Awesome-Multimodal-Token-Compression"},{"title":"An Efficient Token Compression Framework for Visual Object Tracking","url":"https://arxiv.org/html/2605.08329v1"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"[2605.08329] An Efficient Token Compression Framework for Visual Object Tracking","url":"https://arxiv.org/abs/2605.08329"},{"title":"GitHub - yaolinli/MLLM-Token-Compression: Towards Efficient Multimodal Large Language Models: A Survey on Token Compression · GitHub","url":"https://github.com/yaolinli/MLLM-Token-Compression"},{"title":"Can visual input Be Compressed? A visual input token compression benchmark for large multimodal models | OpenReview","url":"https://openreview.net/forum?id=Vu7iQO3f9u"},{"title":"Efficient Multi-modal Large Language Models via Visual Token Grouping | OpenReview","url":"https://openreview.net/forum?id=ym1dS37mZE"}]

Based on the web search results, I found relevant research on visual token compression and model robustness, particularly related to ICLR 2026:

## Key Findings

A research focus has been to enhance model robustness against jailbreaks and hallucinations by selectively reducing visual tokens, while also reducing inference cost as a side benefit.

### Specific ICLR 2026 Work

PruneSID is a training-free Synergistic Importance-Diversity approach featuring a two-stage pipeline: (1) Principle Semantic Components Analysis for clustering tokens into semantically coherent groups, and (2) Intra-group Non-Maximum Suppression for pruning redundant tokens while preserving key representative tokens, with an information-aware dynamic compression ratio mechanism that optimizes token compression rates based on image complexity.

### Broader Context on Token Compression

Visual token compression methods enhance VLMs efficiency through both training-based approaches which optimize token reduction during model training, and training-free approaches which achieve efficiency without requiring model retraining.

Moderate pruning can improve robustness by mitigating overfitting and encouraging stable representations, whereas aggressive pruning tends to degrade robustness by eliminating critical redundancy and increasing vulnerability.

The search results indicate that visual token compression is an active area of research at ICLR 2026, with several papers exploring how compression techniques can simultaneously improve model robustness and efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3c87902-b068-45cb-b4c5-114c6d151e44",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "84d9a671-01f9-49c1-adb9-b96fd14973ce",
  "sourceToolAssistantUUID": "f3c87902-b068-45cb-b4c5-114c6d151e44",
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

_source line 49 · 2026-05-14T06:14:44.128Z_

<details><summary>↩ Tool result · `toolu_015wzoJd1zvSxfhaMcDfnD5T`</summary>

```text
Web search results for query: "IBTM information bottleneck token merging vision transformer 2025 2026"

Links: [{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"EFFICIENT VISION TRANSFORMER BY INFORMATION ...","url":"https://openreview.net/pdf?id=Jwgw3znxT3"},{"title":"Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/html/2407.15219v1"},{"title":"Efficient Visual Transformer by Learnable Token Merging - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40663671/"},{"title":"1 Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/pdf/2407.15219"},{"title":"Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950v1"},{"title":"Efficient Vision Transformer via Token Merger","url":"https://www.researchgate.net/publication/372343417_Efficient_Vision_Transformer_via_Token_Merger"},{"title":"[2407.15219] Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/abs/2407.15219"},{"title":"Efficient Vision Transformer via Token Merger | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10183862/"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"}]

Based on the search results, here's what I found about IBTM (Information Bottleneck inspired Token Merging) for vision transformers:

## Overview

IBTM is a novel and compact transformer block that performs token merging in a learnable scheme inspired by the information bottleneck principle. 

## Key Technical Details

The IBTM is motivated by the reduction of the Information Bottleneck (IB), and a novel and separable variational upper bound for the IB loss is derived. The architecture of mask module in IBTM blocks which generate the token merging mask is designed to reduce the derived upper bound for the IB loss.

The principle of IB is to maximize the mutual information between merged tokens and class labels while minimizing the mutual information between merged tokens and input. That is, IB encourages the network to learn the merged tokens more correlated with the class labels while reducing their correlation with the input.

## Compatibility and Performance

IBTM is compatible with many popular and compact transformer networks, such as MobileViT and EfficientViT, and it reduces the FLOPs and the inference time of the vision transformers while maintaining or even improving the prediction accuracy.

In experiments, all the transformer blocks in popular vision transformers, including MobileViT, EfficientViT, ViT, and Swin, have been replaced with IBTM blocks.

## Publication Status

The work was submitted to ICLR 2025 and was modified on January 22, 2025, but was withdrawn from the conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7445ae23-f13a-4336-91c0-3193ec88ad2e",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "c7f2f31f-46a7-41b2-8771-3f9e4f8cd91e",
  "sourceToolAssistantUUID": "7445ae23-f13a-4336-91c0-3193ec88ad2e",
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

_source line 50 · 2026-05-14T06:14:44.297Z_

<details><summary>↩ Tool result · `toolu_01M5wWYVjYUPL3aEDr7Lyqrz`</summary>

```text
Web search results for query: "CAGE compression-aligned attack adversarial robustness token compression VLM 2025 2026"

Links: [{"title":"On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/html/2601.21531"},{"title":"[2601.21531] On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/abs/2601.21531"},{"title":"Chain of Attack: On the Robustness of Vision-Language Models Against","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Xie_Chain_of_Attack_On_the_Robustness_of_Vision-Language_Models_Against_CVPR_2025_paper.pdf"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Less Is More — Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models","url":"https://arxiv.org/html/2601.12042"},{"title":"A Survey of Recent Advances in Adversarial Attack and Defense on Vision-Language Models[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202511.1363"},{"title":"Pay Less Attention to Function Words for Free Robustness of Vision-Language Models","url":"https://arxiv.org/html/2512.07222"},{"title":"Enhancing Adversarial Robustness of Vision-Language Models through Low-Rank Adaptation | Proceedings of the 2025 International Conference on Multimedia Retrieval","url":"https://dl.acm.org/doi/10.1145/3731715.3733324"},{"title":"GitHub - chs20/RobustVLM: [ICML 2024] Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Large Vision-Language Models · GitHub","url":"https://github.com/chs20/RobustVLM"},{"title":"Visual Adversarial Attack on Vision-Language Models for Autonomous Driving","url":"https://arxiv.org/html/2411.18275v1"}]

Based on the web search results, I found relevant information about CAGE and related research on adversarial robustness of vision-language models under token compression:

## Key Findings

The Compression-AliGnEd attack (CAGE) is designed to align perturbation optimization with compression inference without assuming access to the deployed compression mechanism or its token budget.

### The Problem CAGE Addresses

Existing attacks can overestimate the robustness of compressed LVLMs due to an optimization-inference mismatch: perturbations are optimized in the full-token space, whereas model inference operates on the compressed token representation. While existing attacks perturb all visual tokens, CAGE concentrates the distortion on the surviving tokens.

### Context: Token Compression in Vision-Language Models

State-of-the-art models like LLaVA-NeXT and InternVL process hundreds to thousands of visual tokens per image, creating significant efficiency bottlenecks. Plug-and-play methods such as VisionZip and VisPruner identify a compact set of "informative" tokens using importance scores and optionally merge additional tokens via similarity-based merging.

### Broader Security Concerns

The adversarial robustness of these compressed LVLMs remains unexplored. A related study found that visual token compression significantly undermines model robustness, exposing a previously overlooked trade-off between efficiency and security.

The research papers were published in early 2026, addressing critical security vulnerabilities in efficient Vision-Language Models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb9d1bd6-f4da-474c-aa92-f0be15911038",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "cff60482-bf4d-42bc-bdec-ee36ef92b610",
  "sourceToolAssistantUUID": "eb9d1bd6-f4da-474c-aa92-f0be15911038",
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

_source line 51 · 2026-05-14T06:14:47.245Z_

Let me search for more specific papers, especially focusing on robustness aspects and newer work from major labs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cff60482-bf4d-42bc-bdec-ee36ef92b610",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yDMTA2B7vQSiCz4kJA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56344be0-4f3e-4c18-8d9c-fd520558f046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzyoQ6AxHvCNZZ2ji8VyVg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1685,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 27075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2210,
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

_source line 52 · 2026-05-14T06:14:48.241Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UqVEaTrVKavPbB9nFTeff5`</summary>

```json
{
  "query": "TTF-VLA temporal token fusion pixel attention VLA arXiv 2508.19257"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56344be0-4f3e-4c18-8d9c-fd520558f046",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yDMTA2B7vQSiCz4kJA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d864a0cf-572e-489e-8ab2-e8d0a1cf4d1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzyoQ6AxHvCNZZ2ji8VyVg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1685,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 27075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2210,
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

_source line 53 · 2026-05-14T06:14:49.184Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016mfmt8rkpe11en6m7dVk7D`</summary>

```json
{
  "query": "EfficientVLA training-free acceleration compression vision language action 2506"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d864a0cf-572e-489e-8ab2-e8d0a1cf4d1f",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yDMTA2B7vQSiCz4kJA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfa4974a-1002-4ec6-b1ac-3285693c915c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzyoQ6AxHvCNZZ2ji8VyVg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1685,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 27075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2210,
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

_source line 54 · 2026-05-14T06:14:50.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LAWFUkfZgCgxjtD4zLXJFz`</summary>

```json
{
  "query": "\"one token per frame\" reconsidering visual bandwidth world models VLA policy arXiv 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfa4974a-1002-4ec6-b1ac-3285693c915c",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yDMTA2B7vQSiCz4kJA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f838109-e904-4b25-84c0-4a0f25ba9f90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzyoQ6AxHvCNZZ2ji8VyVg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1685,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 27075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2210,
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

_source line 55 · 2026-05-14T06:14:50.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0123o9Cgd1r7p57SZi7vpGvC`</summary>

```json
{
  "query": "HybridVLA diffusion autoregressive decoding collaborative action ensemble robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f838109-e904-4b25-84c0-4a0f25ba9f90",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yDMTA2B7vQSiCz4kJA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3cdf2f4-ccec-4542-b48f-6490e477991a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzyoQ6AxHvCNZZ2ji8VyVg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1685,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 27075,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2210
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1685,
          "output_tokens": 259,
          "cache_read_input_tokens": 27075,
          "cache_creation_input_tokens": 2210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2210,
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

_source line 56 · 2026-05-14T06:14:54.222Z_

<details><summary>↩ Tool result · `toolu_016mfmt8rkpe11en6m7dVk7D`</summary>

```text
Web search results for query: "EfficientVLA training-free acceleration compression vision language action 2506"

Links: [{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"[2506.10100] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.10100"},{"title":"Paper page - EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"[PDF] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/310b6b4048e36d5948de19fd26e112cbf05fa754"},{"title":"[Literature Review] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/efficientvla-training-free-acceleration-and-compression-for-vision-language-action-models"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=SELYlDHZk2"},{"title":"NeurIPS Poster EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://neurips.cc/virtual/2025/poster/117949"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"}]

I found detailed information about EfficientVLA. Here are the key results:

## Overview

EfficientVLA is a novel training-free, structured inference acceleration framework that synergistically prunes redundant layers from the language module based on their informational impact and strategically selects a compact, task-focused subset of visual tokens by considering both VLA task relevance and inherent image feature diversity.

## Three Core Strategies

EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features.

## Performance Results

When applied to a standard VLA model CogACT, the method yields a 1.93× inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

## Motivation

Vision-Language-Action models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies. While existing acceleration efforts often target isolated inefficiencies, such piecemeal solutions typically fail to holistically address the varied computational and memory bottlenecks across the entire VLA pipeline, thereby limiting practical deployability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfa4974a-1002-4ec6-b1ac-3285693c915c",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "4f6117a7-8ec2-4f2b-8ab6-ebdf894d5369",
  "sourceToolAssistantUUID": "cfa4974a-1002-4ec6-b1ac-3285693c915c",
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

_source line 57 · 2026-05-14T06:14:55.616Z_

<details><summary>↩ Tool result · `toolu_01UqVEaTrVKavPbB9nFTeff5`</summary>

```text
Web search results for query: "TTF-VLA temporal token fusion pixel attention VLA arXiv 2508.19257"

Links: [{"title":"[2508.19257] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.19257"},{"title":"[PDF] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TTF-VLA:-Temporal-Token-Fusion-via-Pixel-Attention-Liu-Zhang/02462f0f53d1b48867e35eae8901d75996e5a662"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/395033880_TTF-VLA_Temporal_Token_Fusion_via_Pixel-Attention_Integration_for_Vision-Language-Action_Models"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257v1"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for","url":"https://arxiv.org/pdf/2508.19257"},{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766"},{"title":"[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.25766"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"Pure Vision-Language-Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v3"},{"title":"From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models","url":"https://arxiv.org/html/2605.04678v1"}]

I found the paper you're looking for. Here's the information about TTF-VLA:

## TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models

TTF-VLA proposes Temporal Token Fusion (TTF), a training-free approach that intelligently integrates historical and current visual representations to enhance VLA inference quality.

### Problem Statement
Vision-Language-Action (VLA) models process visual inputs independently at each timestep, discarding valuable temporal information inherent in robotic manipulation tasks, making models vulnerable to visual noise while ignoring the substantial coherence between consecutive frames in manipulation sequences.

### Methodology
The method employs dual-dimension detection combining efficient grayscale pixel difference analysis with attention-based semantic relevance assessment, enabling selective temporal token fusion through hard fusion strategies and keyframe anchoring to prevent error accumulation.

### Key Results
Comprehensive experiments across LIBERO, SimplerEnv, and real robot tasks demonstrate consistent improvements: 4.0 percentage points average on LIBERO (72.4% vs 68.4% baseline).

**ArXiv ID**: 2508.19257  
**Submission Date**: August 15, 2025 (with latest revision on November 14, 2025)  
**Authors**: Chenghao Liu, Jiachen Zhang, Chengxuan Li, Zhimu Zhou, Shixin Wu, Songfang Huang, and Huiling Duan

You can access the paper directly at: https://arxiv.org/abs/2508.19257


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d864a0cf-572e-489e-8ab2-e8d0a1cf4d1f",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "e86d8b01-4e0e-4c54-b9a1-44698404e9cc",
  "sourceToolAssistantUUID": "d864a0cf-572e-489e-8ab2-e8d0a1cf4d1f",
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

_source line 58 · 2026-05-14T06:14:56.807Z_

<details><summary>↩ Tool result · `toolu_01LAWFUkfZgCgxjtD4zLXJFz`</summary>

```text
Web search results for query: ""one token per frame" reconsidering visual bandwidth world models VLA policy arXiv 2605"

Links: [{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy","url":"https://arxiv.org/html/2605.07931v1"},{"title":"[2605.07931v1] One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy","url":"https://arxiv.org/abs/2605.07931v1"},{"title":"[2604.14149] One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding","url":"https://arxiv.org/abs/2604.14149"},{"title":"One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding","url":"https://arxiv.org/html/2604.14149"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175v2"},{"title":"Inference Optimal VLMs Need Only One Visual Token but Larger Models","url":"https://arxiv.org/html/2411.03312v1"},{"title":"FLARE: Robot Learning with Implicit World Modeling","url":"https://arxiv.org/html/2505.15659v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"One Token per Highly Selective Frame: Towards","url":"https://arxiv.org/pdf/2604.14149"},{"title":"[2604.04913v1] A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens","url":"https://arxiv.org/abs/2604.04913v1"}]

I found the paper you're looking for! Here's what I found:

The paper "One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy" addresses how Vision-Language-Action (VLA) models should be parameterized with auxiliary world modules, noting that existing approaches pass per-frame visual streams at high bandwidth while treating rollouts as side products of action prediction.

The authors introduce OneWM-VLA, which compresses each view into a single semantic token per frame through Adaptive Attention Pooling and produces the latent stream and action trajectory under a single flow-matching objective.

The key finding is that per-frame visual bandwidth can be reduced to a single token without compromising long-horizon performance. Trained with 14.71M LoRA parameters on a π₀ (2B) backbone, OneWM-VLA improves the average success rate from 47.9% to 61.3% on MetaWorld MT50, reaches 95.6% on LIBERO-Long, and reaches 60.0% on the long-horizon Fold Cloth task on a real Piper arm.

The paper was published on arXiv as 2605.07931 approximately 6 days ago.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f838109-e904-4b25-84c0-4a0f25ba9f90",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "d25881a9-3479-4de0-8c96-ef488bd5f4db",
  "sourceToolAssistantUUID": "7f838109-e904-4b25-84c0-4a0f25ba9f90",
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

_source line 59 · 2026-05-14T06:14:56.872Z_

<details><summary>↩ Tool result · `toolu_0123o9Cgd1r7p57SZi7vpGvC`</summary>

```text
Web search results for query: "HybridVLA diffusion autoregressive decoding collaborative action ensemble robustness 2025 2026"

Links: [{"title":"[2503.10631] HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model","url":"https://arxiv.org/abs/2503.10631"},{"title":"HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model","url":"https://arxiv.org/html/2503.10631v1"},{"title":"arXiv:2503.10631v3 [cs.CV] 23 Jun 2025","url":"https://arxiv.org/pdf/2503.10631"},{"title":"HybridVLA: Collaborative Autoregression and Diffusion in a Unified Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=8VyjwyLuSl"},{"title":"HybridVLA: A Collaborative Diffusion and Autoregressive Vision-Language-Action Model for Generalizable Robotic Manipulation","url":"https://hybrid-vla.github.io/"},{"title":"Paper page - HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model","url":"https://huggingface.co/papers/2503.10631"},{"title":"[2503.10631v2] HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model","url":"https://arxiv.org/abs/2503.10631v2"},{"title":"HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250310631L/abstract"},{"title":"HYBRIDVLA: COLLABORATIVE DIFFUSION AND AU","url":"https://openreview.net/pdf/e0f302b8fa2f6a377033c7893a72a151c4d14802.pdf"},{"title":"HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model - Paper Detail","url":"https://deeplearn.org/arxiv/586459/hybridvla:-collaborative-diffusion-and-autoregression-in-a-unified-vision-language-action-model"}]

I found comprehensive information about HybridVLA. Here are the key details:

## Overview

HybridVLA is a unified framework that absorbs the continuous nature of diffusion-based actions and the contextual reasoning of autoregression within a single large language model.

## Problem It Addresses

Autoregressive VLA methods quantize actions into discrete bins, which disrupts the continuity required for precise control. Meanwhile, existing diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions solely conditioned on feature representations extracted by the VLM, without fully leveraging the VLM's pretrained reasoning capabilities through token-level generation.

## Key Technical Innovations

A collaborative training recipe seamlessly incorporates diffusion denoising into the next-token prediction process. With this recipe, the two action prediction methods reinforce each other but also exhibit varying strength across different tasks. Therefore, a collaborative action ensemble mechanism adaptively fuses both predictions, leading to more robust control.

## Performance

HybridVLA outperforms previous state-of-the-art VLA methods by 14% and 19% in mean success rate on simulation and real-world tasks, respectively, while demonstrating stable manipulation in unseen configurations.

The paper (arXiv:2503.10631) was published in March 2025, with the latest version dated June 23, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3cdf2f4-ccec-4542-b48f-6490e477991a",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "01784544-2b8b-4a30-b87e-cdfdcdeed43c",
  "sourceToolAssistantUUID": "b3cdf2f4-ccec-4542-b48f-6490e477991a",
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

_source line 60 · 2026-05-14T06:15:00.125Z_

Let me now search for a few more specific angles - particularly robustness-focused work, DRIBO-related work, and papers from specific labs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01784544-2b8b-4a30-b87e-cdfdcdeed43c",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yEHDCLeuiZNtrQpaf5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41851be2-c0ec-41b5-b29f-c32103ccb91c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyRLjnL1MN2Wzf7xYsEFtM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5774,
      "cache_read_input_tokens": 29285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5774,
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

_source line 61 · 2026-05-14T06:15:01.241Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q5Rv92o7sTdVJaPM7ebVYc`</summary>

```json
{
  "query": "action-aware dynamic pruning efficient VLA manipulation arXiv 2509.22093"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41851be2-c0ec-41b5-b29f-c32103ccb91c",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yEHDCLeuiZNtrQpaf5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "886d1488-9542-47fd-9c99-c296c8572aa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyRLjnL1MN2Wzf7xYsEFtM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5774,
      "cache_read_input_tokens": 29285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5774,
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

_source line 62 · 2026-05-14T06:15:02.251Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cn1neJSTYF12Cy3vnMdk6g`</summary>

```json
{
  "query": "Feather Throttle revisiting visual token pruning VLM inference ICCV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "886d1488-9542-47fd-9c99-c296c8572aa8",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yEHDCLeuiZNtrQpaf5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a480f6a-a50b-4038-b593-219f720a7742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyRLjnL1MN2Wzf7xYsEFtM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5774,
      "cache_read_input_tokens": 29285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5774,
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

_source line 63 · 2026-05-14T06:15:03.191Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HiNWSpSHECxFDfSqETpDmx`</summary>

```json
{
  "query": "token reduction beyond efficiency generative models vision language multimodality arXiv 2505.18227"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a480f6a-a50b-4038-b593-219f720a7742",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yEHDCLeuiZNtrQpaf5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03b4f34f-623e-4ce7-9290-19c8abd230cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyRLjnL1MN2Wzf7xYsEFtM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5774,
      "cache_read_input_tokens": 29285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5774,
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

_source line 64 · 2026-05-14T06:15:03.794Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01114MS4ELTyiXejyoSZmUY9`</summary>

```json
{
  "query": "pi0 pi0.5 robustness perturbation physical intelligence 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03b4f34f-623e-4ce7-9290-19c8abd230cf",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yEHDCLeuiZNtrQpaf5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb5b09de-361b-429a-ade6-1221e99f4f19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyRLjnL1MN2Wzf7xYsEFtM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5774,
      "cache_read_input_tokens": 29285,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5774
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 29285,
          "cache_creation_input_tokens": 5774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5774,
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

_source line 65 · 2026-05-14T06:15:08.264Z_

<details><summary>↩ Tool result · `toolu_01Q5Rv92o7sTdVJaPM7ebVYc`</summary>

```text
Web search results for query: "action-aware dynamic pruning efficient VLA manipulation arXiv 2509.22093"

Links: [{"title":"[2509.22093] Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/abs/2509.22093"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/html/2509.22093v1"},{"title":"GitHub - chen7086/VLA-ADP: Action aware Dynamic Pruning for Efficient Vision Language Action Manipulation · GitHub","url":"https://github.com/chen7086/VLA-ADP"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation | OpenReview","url":"https://openreview.net/forum?id=ea6j8k8Rnw"},{"title":"(PDF) Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://www.researchgate.net/publication/395944757_Action-aware_Dynamic_Pruning_for_Efficient_Vision-Language-Action_Manipulation"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"}]

Based on the search results, here's what I found about arXiv paper 2509.22093:

## Title
Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation

## Authors
Xiaohuan Pei, Yuxing Chen, Siyu Xu, Yunke Wang, Yuheng Shi, Chang Xu

## Overview
Robotic manipulation with Vision-Language-Action models requires efficient inference over long-horizon multi-modal context, where attention to dense visual tokens dominates computational cost.

## Key Contribution
The paper proposes Action-aware Dynamic Pruning (ADP), a multi-modal pruning framework that integrates text-driven token selection with action-aware trajectory gating.

## Main Insight
Existing methods overlook the varying redundancy across robotic manipulation stages. The authors observe that visual token redundancy is higher in coarse manipulation phase than in fine-grained operations, and is strongly correlated with the action dynamic.

## Method
The method introduces a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics.

## Results
Across simulation and real-world evaluations, the method maintains or improves task success, reduces compute, and shortens inference latency.

The paper was submitted on 26 Sep 2025 to arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "886d1488-9542-47fd-9c99-c296c8572aa8",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "d39d2f18-fe65-4c25-a9e6-1779687e199c",
  "sourceToolAssistantUUID": "886d1488-9542-47fd-9c99-c296c8572aa8",
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

_source line 66 · 2026-05-14T06:15:10.761Z_

<details><summary>↩ Tool result · `toolu_01Cn1neJSTYF12Cy3vnMdk6g`</summary>

```text
Web search results for query: "Feather Throttle revisiting visual token pruning VLM inference ICCV 2025"

Links: [{"title":"Feather the Throttle: Revisiting Visual Token Pruning for","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Endo_Feather_the_Throttle_Revisiting_Visual_Token_Pruning_for_Vision-Language_Model_ICCV_2025_paper.pdf"},{"title":"FEATHER","url":"https://web.stanford.edu/~markendo/projects/feather.html"},{"title":"GitHub - markendo/FEATHER: Revisiting Visual Token Pruning for Vision-Language Model Acceleration","url":"https://github.com/markendo/FEATHER"},{"title":"Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration","url":"https://arxiv.org/html/2412.13180"},{"title":"Paper page - Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration","url":"https://huggingface.co/papers/2412.13180"},{"title":"[2412.13180] Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration","url":"https://arxiv.org/abs/2412.13180"},{"title":"TopV: Compatible Token Pruning with Inference Time Optimization for Fast","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_TopV_Compatible_Token_Pruning_with_Inference_Time_Optimization_for_Fast_CVPR_2025_paper.pdf"},{"title":"Exploiting Visual Cues for Effective Token Pruning in VLMs","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Beyond_Text-Visual_Attention_Exploiting_Visual_Cues_for_Effective_Token_Pruning_ICCV_2025_paper.pdf"},{"title":"[Literature Review] Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration","url":"https://www.themoonlight.io/en/review/feather-the-throttle-revisiting-visual-token-pruning-for-vision-language-model-acceleration"},{"title":"CVPR Poster TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model","url":"https://cvpr.thecvf.com/virtual/2025/poster/33168"}]

I've found comprehensive information about "Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration" presented at ICCV 2025.

## Overview

The paper is authored by Mark Endo, Xiaohan Wang, and Serena Yeung-Levy and was published at ICCV in 2025.

## Research Focus

The work examines the popular acceleration approach of early pruning of visual tokens inside the language model, and finds that while strong performance is maintained across many tasks, it exhibits drastically different behavior for a subset of vision-centric tasks such as localization.

## Key Findings

Upon further investigation, the authors uncover a core issue with the acceleration approach where most tokens towards the top of the image are pruned away. When analyzing the approach's poor performance, they uncover a fundamental issue with the pruning criteria in early layers where tokens towards the top of the image are disproportionally removed due to the long-term decay property of RoPE.

## Proposed Solution: FEATHER

FEATHER (Fast and Effective Acceleration wiTH Ensemble cRiteria) is a straightforward approach that resolves the existing issue of selecting bottom tokens, additionally maintains uniformly sampled tokens to ensure good coverage over the whole image, and prunes in two stages.

FEATHER results in substantial performance gains compared to the original acceleration approach, improving localization performance more than 5× with comparable computational savings, while only retaining 3.3% of visual tokens for the second half of LLM layers.

The paper and code are publicly available through the Open Access Computer Vision Foundation and GitHub repositories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a480f6a-a50b-4038-b593-219f720a7742",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "1e0e1823-94a2-4237-8c22-945bb6b5b3e5",
  "sourceToolAssistantUUID": "5a480f6a-a50b-4038-b593-219f720a7742",
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

_source line 67 · 2026-05-14T06:15:10.936Z_

<details><summary>↩ Tool result · `toolu_01HiNWSpSHECxFDfSqETpDmx`</summary>

```text
Web search results for query: "token reduction beyond efficiency generative models vision language multimodality arXiv 2505.18227"

Links: [{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v1"},{"title":"[2505.18227] Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://arxiv.org/abs/2505.18227"},{"title":"[2505.18227v2] Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://arxiv.org/abs/2505.18227v2"},{"title":"Token Reduction Should Go Beyond Efficiency in ...","url":"https://arxiv.org/pdf/2505.18227"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250518227K/abstract"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.18227v2"},{"title":"(PDF) Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://www.researchgate.net/publication/392104162_Token_Reduction_Should_Go_Beyond_Efficiency_in_Generative_Models_--_From_Vision_Language_to_Multimodality"},{"title":"Token Transforming: A Unified and Training-Free Token Compression Framework for Vision Transformer Acceleration","url":"https://arxiv.org/html/2506.05709v1"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=1850&show=2000"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

## Overview

This is a paper titled "Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality" with arXiv ID 2505.18227.

## Main Argument

Traditionally, token reduction has primarily been used as an efficiency strategy, especially in vision and language domains, to balance computational costs, memory usage, and inference latency. However, the paper argues that token reduction should transcend its traditional efficiency-oriented role in the era of large generative models.

## Key Contributions

The authors position token reduction as a fundamental principle in generative modeling, critically influencing both model architecture and broader applications. Specifically, they contend that across vision, language, and multimodal systems, token reduction can: (i) facilitate deeper multimodal integration and alignment, (ii) mitigate "overthinking" and hallucinations, (iii) maintain coherence over long inputs, and (iv) enhance training stability.

## Future Directions

The paper outlines promising future directions, including algorithm design, reinforcement learning-guided token reduction, token optimization for in-context learning, agentic framework design, and broader ML and scientific domains.

The paper presents a comprehensive position on how token reduction techniques can go beyond mere computational efficiency to improve various aspects of generative model performance across different modalities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03b4f34f-623e-4ce7-9290-19c8abd230cf",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "dd6914ed-8eaf-4d93-b702-af74ae209945",
  "sourceToolAssistantUUID": "03b4f34f-623e-4ce7-9290-19c8abd230cf",
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

_source line 68 · 2026-05-14T06:15:13.239Z_

<details><summary>↩ Tool result · `toolu_01114MS4ELTyiXejyoSZmUY9`</summary>

```text
Web search results for query: "pi0 pi0.5 robustness perturbation physical intelligence 2025 2026"

Links: [{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"[2410.24164] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164"},{"title":"[Paper Review] Pi0, Pi0.5, Pi0-FAST - Tracing the Path of Physical Intelligence (PI)","url":"https://bequiet-log.vercel.app/pi-review"},{"title":"Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies","url":"https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"},{"title":"Physical Intelligence (π)","url":"https://www.pi.website/"},{"title":"A VLA with Open-World Generalization","url":"https://www.physicalintelligence.company/blog/pi05"},{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"},{"title":"[2504.16054] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054"},{"title":"π 0 : Our First Generalist Policy","url":"https://www.pi.website/blog/pi0"}]

Based on the web search results, here's what I found regarding π₀, π₀.₅, robustness, perturbation, and physical intelligence:

## π₀ and π₀.₅ Models

π₀ is a vision-language-action flow model developed by Physical Intelligence, a company founded in 2024 by Chelsea Finn, Sergey Levine, Karol Hausman, Brian Ichter, and Lachy Groom.

In September 2025, π₀.₅ was released as an upgraded version of π₀ with better open-world generalization. π₀.₅ uses co-training on heterogeneous tasks to enable broad generalization, and uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation.

## Robustness and Perturbation

The policies are reactive, and can handle both variability in the environment and perturbations. Regarding robustness to visual disruptions, questions about π₀'s robustness when its visual inputs are disrupted were tested by blocking cameras.

Powered by PaliGemma, a 3B vision-language model, π₀ demonstrates robust scene comprehension and adaptability despite relying solely on uncalibrated monocular RGB inputs (224x224 pixels).

## Recent Developments (2025-2026)

π*₀.₆: a VLA that learns from experience was announced in November 2025, representing a method for training generalist policies with reinforcement learning. In December 2025, Physical Intelligence demonstrated solutions to difficult manipulation challenge tasks through fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb5b09de-361b-429a-ade6-1221e99f4f19",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "ac9c61ff-466b-41f7-ad1e-f121b8392682",
  "sourceToolAssistantUUID": "fb5b09de-361b-429a-ade6-1221e99f4f19",
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

_source line 69 · 2026-05-14T06:15:16.083Z_

Let me search for a few more critical areas - particularly adversarial robustness in VLAs and more IB-related papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac9c61ff-466b-41f7-ad1e-f121b8392682",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yFVD3DTB1e8tY4gMzZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb54d29a-5298-43aa-8cad-a0283a69a7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHkw4kad2q5BvjpxBJkX1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4070,
      "cache_read_input_tokens": 35059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 70 · 2026-05-14T06:15:16.737Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JuV9EMKF5mpJpkkee8s3BH`</summary>

```json
{
  "query": "language-guided token compression reinforcement learning VLM arXiv 2603.13394"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb54d29a-5298-43aa-8cad-a0283a69a7a3",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yFVD3DTB1e8tY4gMzZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54973e44-9b8d-4676-bef8-f22f70e6ed27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHkw4kad2q5BvjpxBJkX1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4070,
      "cache_read_input_tokens": 35059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 71 · 2026-05-14T06:15:17.544Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DABby4ZxEo1JsHMd9sbPL7`</summary>

```json
{
  "query": "AgilePruner empirical study attention diversity adaptive visual token pruning VLM arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54973e44-9b8d-4676-bef8-f22f70e6ed27",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yFVD3DTB1e8tY4gMzZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71d2d0ce-3538-4547-9318-fe941d3d367d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHkw4kad2q5BvjpxBJkX1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4070,
      "cache_read_input_tokens": 35059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 72 · 2026-05-14T06:15:18.672Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AUR6LXS7KvBT5QDwtPPFu4`</summary>

```json
{
  "query": "attention debiasing token pruning vision language models arXiv 2508.17807"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71d2d0ce-3538-4547-9318-fe941d3d367d",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yFVD3DTB1e8tY4gMzZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5693f762-635a-43a9-871a-7cd98e8dede2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHkw4kad2q5BvjpxBJkX1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4070,
      "cache_read_input_tokens": 35059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 73 · 2026-05-14T06:15:19.187Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019efQ4yz6jb9WiturmtdqKA`</summary>

```json
{
  "query": "Gemini Robotics robustness perturbation DeepMind 2025 2026 VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5693f762-635a-43a9-871a-7cd98e8dede2",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yFVD3DTB1e8tY4gMzZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a2497ad-4021-4837-a086-5e1fe4052813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHkw4kad2q5BvjpxBJkX1E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4070,
      "cache_read_input_tokens": 35059,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4070
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 35059,
          "cache_creation_input_tokens": 4070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4070,
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

_source line 74 · 2026-05-14T06:15:22.002Z_

<details><summary>↩ Tool result · `toolu_01JuV9EMKF5mpJpkkee8s3BH`</summary>

```text
Web search results for query: "language-guided token compression reinforcement learning VLM arXiv 2603.13394"

Links: [{"title":"Language-Guided Token Compression with Reinforcement Learning in Large","url":"https://arxiv.org/pdf/2603.13394"},{"title":"[2603.13394] Language-Guided Token Compression with Reinforcement Learning in Large Vision-Language Models","url":"https://arxiv.org/abs/2603.13394"},{"title":"Language-Guided Token Compression with Reinforcement Learning in Large Vision-Language Models","url":"https://arxiv.org/html/2603.13394"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"When Tokens Talk Too Much: A Survey of Multimodal Long-Context Token Compression across Images, Videos, and Audios","url":"https://arxiv.org/html/2507.20198v4"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Large Language Model as Token Compressor and Decompressor","url":"https://arxiv.org/html/2603.25340v1"},{"title":"A Survey of Token Compression for Efficient Multimodal Large Language Models","url":"https://arxiv.org/html/2507.20198v5"},{"title":"GitHub - cokeshao/Awesome-Multimodal-Token-Compression: [TMLR 2026] Survey: https://arxiv.org/pdf/2507.20198 · GitHub","url":"https://github.com/cokeshao/Awesome-Multimodal-Token-Compression"},{"title":"Dynamic Token Compression for Efficient Video Understanding through Reinforcement Learning","url":"https://arxiv.org/html/2603.26365"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

TPRL is a reinforcement learning framework that learns adaptive pruning trajectories through language-guided sequential optimization tied directly to end-task performance. The paper is titled "Language-Guided Token Compression with Reinforcement Learning in Large Vision-Language Models" by Sihan Cao and 8 other authors, submitted on March 11, 2026.

The paper addresses the problem that Large Vision-Language Models (LVLMs) incur substantial inference costs due to the processing of a vast number of visual tokens. Existing methods typically struggle to model progressive visual token reduction as a multi-step decision process with sequential dependencies and often rely on hand-engineered scoring rules that lack adaptive optimization for complex reasoning trajectories.

You can access the paper at https://arxiv.org/abs/2603.13394 or https://arxiv.org/pdf/2603.13394.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54973e44-9b8d-4676-bef8-f22f70e6ed27",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "d9664635-6d64-4216-801d-fe0fd8c1e3b9",
  "sourceToolAssistantUUID": "54973e44-9b8d-4676-bef8-f22f70e6ed27",
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

_source line 75 · 2026-05-14T06:15:26.164Z_

<details><summary>↩ Tool result · `toolu_019efQ4yz6jb9WiturmtdqKA`</summary>

```text
Web search results for query: "Gemini Robotics robustness perturbation DeepMind 2025 2026 VLA"

Links: [{"title":"Gemini Robotics — Google DeepMind","url":"https://deepmind.google/models/gemini-robotics/"},{"title":"Gemini Robotics On-Device brings AI to local robotic devices — Google DeepMind","url":"https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/"},{"title":"Gemini Robotics: Bringing AI into the Physical World","url":"https://arxiv.org/html/2503.20020v1"},{"title":"[2503.20020] Gemini Robotics: Bringing AI into the Physical World","url":"https://arxiv.org/abs/2503.20020"},{"title":"Introducing Gemini Robotics and Gemini Robotics-ER, AI models designed for robots to understand, act and react to the physical world. — Google DeepMind","url":"https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/"},{"title":"Gemini Robotics 1.5: Pushing the Frontier of Generalist ...","url":"https://storage.googleapis.com/deepmind-media/gemini-robotics/Gemini-Robotics-1-5-Tech-Report.pdf"},{"title":"Google DeepMind Announces Robotics Foundation Model Gemini Robotics On-Device - InfoQ","url":"https://www.infoq.com/news/2025/07/google-gemini-robotics/"},{"title":"Gemini Robotics 1.5 brings AI agents into the physical world — Google DeepMind","url":"https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/"},{"title":"Gemini Robotics: A new era of AI-Powered RobotsPlain Concepts","url":"https://www.plainconcepts.com/gemini-robotics/"},{"title":"Gemini Robotics ER 1.6: Enhanced Embodied Reasoning — Google DeepMind","url":"https://deepmind.google/blog/gemini-robotics-er-1-6/"}]

Based on the search results, here's what I found about Gemini Robotics from DeepMind in 2025-2026:

## Overview

Gemini Robotics is an advanced Vision-Language-Action (VLA) generalist model capable of directly controlling robots, built on Gemini 2.0 with the addition of physical actions as a new output modality for the purpose of directly controlling robots.

## Robustness and Generalization

The model demonstrates notable robustness capabilities. Gemini Robotics executes smooth and reactive movements to tackle a wide range of complex manipulation tasks while also being robust to variations in object types and positions, handling unseen environments as well as following diverse, open vocabulary instructions.

Regarding robustness evaluation, the research evaluates Gemini Robotics's ability to deal with variations along three axes: Visual Generalization (invariance to visual changes like variations in background, lighting conditions, distractor objects or textures), Instruction Generalization (understanding invariance and equivalence in natural language instructions, including paraphrasing, robustness to typos, different languages, and varying levels of specificities).

## Recent Developments

Gemini Robotics 1.5 shows a remarkable ability to learn across different embodiments and can transfer motions learned from one robot to another, without needing to specialize the model to each new embodiment.

The most recent version, Gemini Robotics-ER 1.6 shows significant improvement over both Gemini Robotics-ER 1.5 and Gemini 3.0 Flash, specifically enhancing spatial and physical reasoning capabilities such as pointing, counting, and success detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a2497ad-4021-4837-a086-5e1fe4052813",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "1da73a5b-2a8a-4b4f-b6c5-e9edb20697ce",
  "sourceToolAssistantUUID": "9a2497ad-4021-4837-a086-5e1fe4052813",
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

_source line 76 · 2026-05-14T06:15:26.383Z_

<details><summary>↩ Tool result · `toolu_01AUR6LXS7KvBT5QDwtPPFu4`</summary>

```text
Web search results for query: "attention debiasing token pruning vision language models arXiv 2508.17807"

Links: [{"title":"[2508.17807] Attention Debiasing for Token Pruning in Vision Language Models","url":"https://arxiv.org/abs/2508.17807"},{"title":"Attention Debiasing for Token Pruning in Vision–Language Models","url":"https://arxiv.org/html/2508.17807"},{"title":"[2508.17807v2] Attention Debiasing for Token Pruning in Vision Language Models","url":"https://arxiv.org/abs/2508.17807v2"},{"title":"Paper page - Attention Debiasing for Token Pruning in Vision Language Models","url":"https://huggingface.co/papers/2508.17807"},{"title":"Attention Debiasing for Token Pruning in Vision Language Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2508.17807v2"},{"title":"GitHub - intcomp/attention-bias: Official implementation of the paper: Attention Debiasing for Token Pruning in Vision–Language Models.","url":"https://github.com/intcomp/attention-bias"},{"title":"PoRe: Position-Reweighted Visual Token Pruning for ...","url":"https://arxiv.org/pdf/2508.17807"},{"title":"LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models","url":"https://arxiv.org/html/2604.23950"},{"title":"LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models | OpenReview","url":"https://openreview.net/forum?id=Dxb6gBJHby"},{"title":"AdaTP: Attention-Debiased Token Pruning for Video Large Language Models","url":"https://arxiv.org/html/2505.20100"}]

I found the arXiv paper 2508.17807. Here's what it's about:

## Paper Summary

The paper titled "Attention Debiasing for Token Pruning in Vision Language Models" was submitted on August 25, 2025, with the latest version (v2) revised on January 16, 2026. It is authored by Kai Zhao, Wubang Yuan, Yuchen Lin, Liting Ruan, Xiaofeng Lu, Deng-Ping Fan, Ming-Ming Cheng, and Dan Zeng.

## Key Problem

Vision-language models typically encode substantially more visual tokens than text tokens, resulting in significant token redundancy. However, the paper finds that attention in VLMs is systematically biased, disproportionately favoring tokens appearing later in the sequence, manifesting as over-attention to lower image regions, and assigning inflated scores to semantically empty padding tokens.

## Proposed Solution

To address these biases, the authors propose two simple yet effective techniques: first, to remove recency bias, they statistically model the positional trend of attention and construct an exponential recency-bias function by normalizing attention with this learned function to obtain a position-agnostic, content-dependent importance criterion; second, to eliminate attention sink in the padding image area, they simply zero out the attention scores of padding visual tokens.

## Results

Extensive experiments on ten image-based and three video-based vision-language benchmarks, across multiple VLM architectures, demonstrate that the approach consistently and significantly improves six representative attention-based visual token pruning methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5693f762-635a-43a9-871a-7cd98e8dede2",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "8aa7653d-6a40-457e-be82-00bb0e76403e",
  "sourceToolAssistantUUID": "5693f762-635a-43a9-871a-7cd98e8dede2",
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

_source line 77 · 2026-05-14T06:15:26.752Z_

<details><summary>↩ Tool result · `toolu_01DABby4ZxEo1JsHMd9sbPL7`</summary>

```text
Web search results for query: "AgilePruner empirical study attention diversity adaptive visual token pruning VLM arXiv 2603"

Links: [{"title":"[2603.01236] AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models","url":"https://arxiv.org/abs/2603.01236"},{"title":"AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models","url":"https://arxiv.org/html/2603.01236v1"},{"title":"Paper page - AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models","url":"https://huggingface.co/papers/2603.01236"},{"title":"[ICLR 2026] AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models","url":"https://paper.pnu-cvsp.com/AgilePruner/"},{"title":"agilepruner: an empirical study of atten","url":"https://arxiv.org/pdf/2603.01236"},{"title":"(PDF) AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models","url":"https://www.researchgate.net/publication/401470055_AgilePruner_An_Empirical_Study_of_Attention_and_Diversity_for_Adaptive_Visual_Token_Pruning_in_Large_Vision-Language_Models"},{"title":"An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models | OpenReview","url":"https://openreview.net/forum?id=2NLkhPex1M"},{"title":"GitHub - cvsp-lab/AgilePruner: [ICLR 2026] AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models · GitHub","url":"https://github.com/cvsp-lab/AgilePruner"},{"title":"AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models [Quick Review]","url":"https://liner.com/review/agilepruner-an-empirical-study-of-attention-and-diversity-for-adaptive"},{"title":"Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs","url":"https://arxiv.org/html/2604.12035"}]

I found the paper! Here are the key details about **AgilePruner**:

## Overview
AgilePruner addresses how Large Vision-Language Models (LVLMs) have adopted visual token pruning strategies to mitigate substantial computational overhead incurred by extensive visual token sequences.

## Main Contributions
The work conducts thorough empirical analysis using effective rank (erank) as a measure of feature diversity and attention score entropy to investigate visual token processing mechanisms and analyze the strengths and weaknesses of each approach.

## Key Findings
The erank-based quantitative analysis shows that many diversity-oriented pruning methods preserve substantially less feature diversity than intended; moreover, analysis using the CHAIR dataset reveals that the diversity they do retain is closely tied to increased hallucination frequency compared to attention-based pruning.

Additionally, attention-based approaches are more effective on simple images where visual evidence is concentrated, while diversity-based methods better handle complex images with distributed features.

## Proposed Solution
Incorporating image-aware adjustments into existing hybrid pruning strategies consistently improves their performance, and a minimal instantiation through a simple adaptive pruning mechanism achieves strong and reliable performance across standard benchmarks as well as hallucination-specific evaluations.

## Publication
The paper was accepted at ICLR 2026, and the arXiv preprint is available as 2603.01236.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71d2d0ce-3538-4547-9318-fe941d3d367d",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "63ac344c-bda5-4db9-9537-fdd9c19e1147",
  "sourceToolAssistantUUID": "71d2d0ce-3538-4547-9318-fe941d3d367d",
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

_source line 78 · 2026-05-14T06:15:29.778Z_

Let me do a few more targeted searches to ensure comprehensive coverage, especially for IB-related work and robustness-specific approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63ac344c-bda5-4db9-9537-fdd9c19e1147",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yGVEoYvpxL9MrKCmUK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03fe3a94-bc16-4b90-a67e-915def5ea3b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4EFsbsxLF4kj746B7seJ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1881,
      "cache_creation_input_tokens": 2174,
      "cache_read_input_tokens": 39129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2174,
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

_source line 79 · 2026-05-14T06:15:30.247Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ZPjsJXi6MeVJbQcBuyjdv`</summary>

```json
{
  "query": "\"visual token pruning\" robustness hallucination calibration VLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03fe3a94-bc16-4b90-a67e-915def5ea3b3",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yGVEoYvpxL9MrKCmUK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25202c0d-e8fd-4e91-a2cb-8e39d372cfe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4EFsbsxLF4kj746B7seJ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1881,
      "cache_creation_input_tokens": 2174,
      "cache_read_input_tokens": 39129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2174,
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

_source line 80 · 2026-05-14T06:15:31.173Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Na99nPsvdxsFeqgrAoFoi7`</summary>

```json
{
  "query": "DRIBO multi-view information bottleneck representation learning reinforcement learning robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25202c0d-e8fd-4e91-a2cb-8e39d372cfe0",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yGVEoYvpxL9MrKCmUK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e645c44b-15ef-4551-a822-84cfbdac90ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4EFsbsxLF4kj746B7seJ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1881,
      "cache_creation_input_tokens": 2174,
      "cache_read_input_tokens": 39129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2174,
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

_source line 81 · 2026-05-14T06:15:32.110Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GjnyLngwKL2pXRFAxwVfpv`</summary>

```json
{
  "query": "Spec-VLA speculative decoding VLA relaxed acceptance arXiv 2507.22424"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e645c44b-15ef-4551-a822-84cfbdac90ca",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yGVEoYvpxL9MrKCmUK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2ea02c5-c6e8-413f-ab03-6df91adc81ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4EFsbsxLF4kj746B7seJ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1881,
      "cache_creation_input_tokens": 2174,
      "cache_read_input_tokens": 39129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2174,
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

_source line 82 · 2026-05-14T06:15:32.719Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qv3FG7NtB37wMkPZ2Qp7WS`</summary>

```json
{
  "query": "\"information bottleneck\" visual representation robust policy learning embodied 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2ea02c5-c6e8-413f-ab03-6df91adc81ea",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yGVEoYvpxL9MrKCmUK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e0750a3-19b7-4b51-90cc-30bdae9d1b9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4EFsbsxLF4kj746B7seJ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1881,
      "cache_creation_input_tokens": 2174,
      "cache_read_input_tokens": 39129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2174,
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

### Tool result

_source line 83 · 2026-05-14T06:15:37.044Z_

<details><summary>↩ Tool result · `toolu_01Na99nPsvdxsFeqgrAoFoi7`</summary>

```text
Web search results for query: "DRIBO multi-view information bottleneck representation learning reinforcement learning robotics"

Links: [{"title":"[2102.13268] DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://arxiv.org/abs/2102.13268"},{"title":"DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://proceedings.mlr.press/v162/fan22b/fan22b.pdf"},{"title":"GitHub - JmfanBU/DRIBO: DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://github.com/JmfanBU/DRIBO"},{"title":"DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=Py8WbvKH_wv"},{"title":"Robust Deep Reinforcement Learning via MultiView Infomration BOttleneck... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Robust-Deep-Reinforcement-Learning-via-MultiView-Infomration-BOttleneck-DRIBO_fig1_349682874"},{"title":"ICML Poster DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://icml.cc/virtual/2022/poster/16441"},{"title":"(PDF) Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://www.researchgate.net/publication/349682874_Robust_Deep_Reinforcement_Learning_via_Multi-View_Information_Bottleneck"},{"title":"GitHub - BU-DEPEND-Lab/DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck · GitHub","url":"https://github.com/BU-DEPEND-Lab/DRIBO"},{"title":"Multimodal information bottleneck for deep reinforcement learning with multiple sensors | Neural Networks","url":"https://dl.acm.org/doi/10.1016/j.neunet.2024.106347"},{"title":"Track: MISC: Representation Learning/Causality","url":"https://icml.cc/virtual/2022/session/20088"}]

Based on the search results, here's information about DRIBO:

## DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck

DRIBO incorporates the inherent sequential structure of reinforcement learning and multi-view information bottleneck principle into robust representation learning in RL.

### Key Problem and Approach

Deep reinforcement learning (DRL) agents are often sensitive to visual changes that were unseen in their training environments. DRIBO introduces a novel contrastive version of the Multi-View Information Bottleneck (MIB) objective for temporal data, and trains RL agents from pixels with this auxiliary objective to learn robust representations that can compress away task-irrelevant information and are predictive of task-relevant dynamics.

### Results and Performance

This approach enables training high-performance policies that are robust to visual distractions and can generalize well to unseen environments. The approach can achieve state-of-the-art performance on diverse visual control tasks on the DeepMind Control Suite when the background is replaced with natural videos.

### Implementation

The research team has made an official implementation available, based on CURL by Misha Laskin and SAC+AE by Denis Yarats. The paper was published in 2022 and is available through multiple academic venues including arXiv and ICML.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e645c44b-15ef-4551-a822-84cfbdac90ca",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "f6795d4f-1a55-4350-bd9d-e8810785e78f",
  "sourceToolAssistantUUID": "e645c44b-15ef-4551-a822-84cfbdac90ca",
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

_source line 84 · 2026-05-14T06:15:38.825Z_

<details><summary>↩ Tool result · `toolu_01GjnyLngwKL2pXRFAxwVfpv`</summary>

```text
Web search results for query: "Spec-VLA speculative decoding VLA relaxed acceptance arXiv 2507.22424"

Links: [{"title":"[2507.22424] Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://arxiv.org/abs/2507.22424"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with","url":"https://arxiv.org/pdf/2507.22424"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://arxiv.org/html/2507.22424"},{"title":"[2507.22424v1] Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://arxiv.org/abs/2507.22424v1"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance | alphaXiv","url":"https://www.alphaxiv.org/resources/2507.22424v1"},{"title":"[PDF] Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Spec-VLA:-Speculative-Decoding-for-Models-with-Wang-Yu/62bce1eb0a1d29a709c446530e89da51f4fd8c25"},{"title":"(PDF) Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://www.researchgate.net/publication/394121107_Spec-VLA_Speculative_Decoding_for_Vision-Language-Action_Models_with_Relaxed_Acceptance"},{"title":"KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models","url":"https://arxiv.org/html/2603.01581"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with","url":"https://openreview.net/pdf?id=P3X72HSH4g"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language ...","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2507.22424"}]

I found the paper! Here's what the search revealed about arXiv paper 2507.22424:

## Spec-VLA: Speculative Decoding for Vision-Language-Action Models

Spec-VLA is an SD (Speculative Decoding) framework designed to accelerate VLA (Vision-Language-Action) models.

### Problem Addressed
Vision-Language-Action models leverage the capabilities of Visual Language Models, but VLMs' significant parameter size and autoregressive decoding nature impose considerable computational demands on VLA models. While Speculative Decoding has shown efficacy in accelerating Large Language Models, its application to VLA models remains unexplored.

### Key Innovation
Due to the difficulty of the action prediction task and the greedy decoding mechanism of VLA models, direct application of advanced SD frameworks yields minor speed improvement, so the authors propose an effective mechanism to relax acceptance utilizing the relative distances represented by the action tokens.

### Results
Empirical results show 1.42× speedup compared with the OpenVLA baseline, without compromising the success rate.

### Authors & Availability
The paper is authored by Songsheng Wang, Rucheng Yu, Zhihang Yuan, Chao Yu, Feng Gao, Yu Wang, and Derek F. Wong. The code and data are publicly available at https://github.com/PineTreeWss/SpecVLA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2ea02c5-c6e8-413f-ab03-6df91adc81ea",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "be9fdc75-b7e0-4048-8d71-54fa6f1696f1",
  "sourceToolAssistantUUID": "c2ea02c5-c6e8-413f-ab03-6df91adc81ea",
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

_source line 85 · 2026-05-14T06:15:39.970Z_

<details><summary>↩ Tool result · `toolu_015ZPjsJXi6MeVJbQcBuyjdv`</summary>

```text
Web search results for query: ""visual token pruning" robustness hallucination calibration VLM 2025 2026"

Links: [{"title":"ICML Poster The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering","url":"https://icml.cc/virtual/2025/poster/46338"},{"title":"Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs","url":"https://arxiv.org/html/2604.12035"},{"title":"VISUAL TOKEN COMPRESSION ENHANCES MODEL ...","url":"https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering | OpenReview","url":"https://openreview.net/forum?id=7BKcLeHQsm"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"HiPP-Prune: Hierarchical Preference-Conditioned Structured Pruning for Vision-Language Models","url":"https://arxiv.org/html/2603.06270"},{"title":"Revisiting Visual Token Pruning for Vision-Language Model ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Endo_Feather_the_Throttle_Revisiting_Visual_Token_Pruning_for_Vision-Language_Model_ICCV_2025_paper.pdf"},{"title":"ERASE: Eliminating Redundant Visual Tokens via Adaptive Two-Stage Token Pruning","url":"https://arxiv.org/html/2605.09982v1"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://arxiv.org/pdf/2502.11501"}]

I've found relevant research on visual token pruning with connections to robustness, hallucination, and calibration in Vision-Language Models (VLMs) from 2025-2026. Here are the key findings:

## Recent Research Highlights

**Calibration and Hallucination:**

A study examines how visual token pruning affects model calibration, that is, whether predicted confidence matches actual correctness. Calibration has received increasing attention in multimodal large language models, especially in relation to overconfidence and hallucination.

**Robustness to Jailbreaks and Hallucinations:**

While prior work has focused on pruning visual tokens to accelerate inference and improve efficiency, newer research aims to enhance the robustness of VLMs via visual token compression. Intrinsically misaligned visual tokens can serve as out-of-distribution inputs, leading VLMs to produce highly uncertain responses, increasing the risk of jailbreak attacks and hallucinations.

**Hallucination Reduction Through Token Analysis:**

Research reveals key patterns in how LVLMs process information: gradual visual information loss—visually grounded tokens gradually become less favored throughout generation, and early excitation—semantically meaningful tokens achieve peak activation in the layers earlier than the final layer.

**Emerging Methods:**

Several 2025-2026 papers address these interconnected challenges:
- A 2026 work on vision token compression in VLMs via synergistic importance-diversity
- AgilePruner: a 2026 empirical study of attention and diversity for adaptive visual token pruning in large vision-language models
- ERASE jointly addresses visual redundancy and contextual relevance through entropy-guided image-level pruning and adaptive text-conditioned token pruning, dynamically adjusting pruning ratio and layer according to image complexity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25202c0d-e8fd-4e91-a2cb-8e39d372cfe0",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "8d7f3ac6-d217-463a-b81e-56d0634c465a",
  "sourceToolAssistantUUID": "25202c0d-e8fd-4e91-a2cb-8e39d372cfe0",
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

_source line 86 · 2026-05-14T06:15:40.161Z_

<details><summary>↩ Tool result · `toolu_01Qv3FG7NtB37wMkPZ2Qp7WS`</summary>

```text
Web search results for query: ""information bottleneck" visual representation robust policy learning embodied 2025 2026"

Links: [{"title":"Learning Primitive Embodied World Models: Towards Scalable Robotic Learning | OpenReview","url":"https://openreview.net/forum?id=W0AY49wWrb"},{"title":"Frontiers | A review of embodied intelligence systems: a three-layer framework integrating multimodal perception, world modeling, and structured strategies","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1668910/full"},{"title":"Representation Learning in Deep RL via Discrete Information Bottleneck","url":"https://proceedings.mlr.press/v206/islam23a/islam23a.pdf"},{"title":"Information Bottleneck-Enhanced Reinforcement Learning for Solving Operation Research Problems","url":"https://www.mdpi.com/1424-8220/25/24/7572"},{"title":"Publications | Chenjia Bai","url":"http://baichenjia.cn/publication/"},{"title":"Embodied intelligence for robot manipulation: development and challenges | Vicinagearth | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44336-025-00020-1"},{"title":"A Survey of Embodied Learning for Object-centric Robotic Manipulation | Machine Intelligence Research | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11633-025-1542-8"},{"title":"Multimodal information bottleneck for deep reinforcement learning with multiple sensors - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608024002715"},{"title":"Revisiting the Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=w10KdRwcMk"},{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"}]

Based on the web search results, I found several relevant papers and research directions connecting information bottleneck, visual representation, robust policy learning, and embodied AI in 2025-2026:

## Key Findings

**Information Bottleneck in Embodied Learning:**

BC-IB integrates an information bottleneck into policy learning, compressing information irrelevant to tasks to maximize data utility. This approach directly addresses robustness in embodied manipulation tasks.

**Information Bottleneck for Robust Representations:**

Information bottlenecks can filter out irrelevant information from observations, and discrete bottleneck representations with REPDIB can be an effective approach for learning robust representations in RL.

**Multimodal Information Bottleneck:**

A multimodal information bottleneck model learns task-relevant joint representations from egocentric images and proprioception, compressing and retaining predictive information while filtering out task-irrelevant information. This method achieves better sample efficiency and zero-shot robustness to unseen noise on locomotion tasks.

**Visual Representation in Embodied AI (2025-2026):**

Recent work addresses embodied learning through multiple approaches. A novel study proposes the Historical Information Bottleneck (HIB) to narrow the sim-to-real gap for legged locomotion through privileged knowledge distillation.

**Information Bottleneck for Robust RL:**

Information Bottleneck-Enhanced Reinforcement Learning (IBE) integrates information-theoretic regularization into attention-based RL architectures to enhance both representation learning and exploration efficiency.

The search results show active research combining information bottleneck theory with visual representations and robust policy learning for embodied AI systems in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e0750a3-19b7-4b51-90cc-30bdae9d1b9a",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "0234c152-23a4-465e-b0ec-64056b02da78",
  "sourceToolAssistantUUID": "5e0750a3-19b7-4b51-90cc-30bdae9d1b9a",
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

_source line 87 · 2026-05-14T06:15:44.383Z_

Let me search for a few more specific papers that came up as leads and some final targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0234c152-23a4-465e-b0ec-64056b02da78",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yHULWg3mt2GrWFSDfZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b7c0de6-28fb-4105-8482-6019631c421e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JWZ3yyXj4QtXqRDSZy1U4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6083,
      "cache_read_input_tokens": 41303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6083,
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

_source line 88 · 2026-05-14T06:15:44.976Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AXnKhBA5jjaLKjoTCs8bNA`</summary>

```json
{
  "query": "\"does visual token pruning improve calibration\" empirical study confidence MLLMs arXiv 2604.12035"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b7c0de6-28fb-4105-8482-6019631c421e",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yHULWg3mt2GrWFSDfZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe61cc41-566e-4c22-bf81-a418ce4fc7df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JWZ3yyXj4QtXqRDSZy1U4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6083,
      "cache_read_input_tokens": 41303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6083,
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

_source line 89 · 2026-05-14T06:15:45.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0141s5YQgveV5CZj1p5vD6LU`</summary>

```json
{
  "query": "\"visual token compression enhances model robustness\" jailbreak hallucination VLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe61cc41-566e-4c22-bf81-a418ce4fc7df",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yHULWg3mt2GrWFSDfZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74de4d2c-01cb-459c-af2d-65088f60d00d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JWZ3yyXj4QtXqRDSZy1U4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6083,
      "cache_read_input_tokens": 41303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6083,
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

_source line 90 · 2026-05-14T06:15:46.338Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A9aneUmWTmpyr8eJRkueEX`</summary>

```json
{
  "query": "\"multimodal information bottleneck\" deep reinforcement learning multiple sensors robotics 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74de4d2c-01cb-459c-af2d-65088f60d00d",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yHULWg3mt2GrWFSDfZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb6803a0-7b2a-4729-8eef-dbf8a0899e17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JWZ3yyXj4QtXqRDSZy1U4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6083,
      "cache_read_input_tokens": 41303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6083,
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

_source line 91 · 2026-05-14T06:15:46.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ThNnh5Pvpb1UEA1yTDnppC`</summary>

```json
{
  "query": "CoA-VLA chain-of-affordance vision language action robustness ICCV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb6803a0-7b2a-4729-8eef-dbf8a0899e17",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yHULWg3mt2GrWFSDfZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb0a4c21-c771-436e-94c7-fb7e37222c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JWZ3yyXj4QtXqRDSZy1U4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6083,
      "cache_read_input_tokens": 41303,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 41303,
          "cache_creation_input_tokens": 6083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6083,
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

_source line 92 · 2026-05-14T06:15:52.509Z_

<details><summary>↩ Tool result · `toolu_01AXnKhBA5jjaLKjoTCs8bNA`</summary>

```text
Web search results for query: ""does visual token pruning improve calibration" empirical study confidence MLLMs arXiv 2604.12035"

Links: [{"title":"[2604.12035] Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs","url":"https://arxiv.org/abs/2604.12035"},{"title":"Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs","url":"https://arxiv.org/html/2604.12035"},{"title":"IDPruner: Harmonizing Importance and Diversity in Visual Token Pruning for MLLMs","url":"https://arxiv.org/html/2602.13315"},{"title":"QAPruner: Quantization-Aware Vision Token Pruning for Multimodal Large Language Models","url":"https://arxiv.org/html/2604.02816"},{"title":"A Comprehensive Study on Visual Token Redundancy for Discrete Diffusion-based Multimodal Large Language Models","url":"https://arxiv.org/html/2511.15098"},{"title":"EVTP-IVS: Effective Visual Token Pruning For Unifying Instruction Visual Segmentation In Multi-Modal Large Language Models","url":"https://arxiv.org/html/2508.11886v1"},{"title":"EvoPrune: Early-Stage Visual Token Pruning for Efficient MLLMs","url":"https://arxiv.org/html/2603.03681"},{"title":"Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs","url":"https://arxiv.org/html/2506.10967v1"},{"title":"GridPrune: From “Where to Look” to “What to Select” in Visual Token Pruning for MLLMs","url":"https://arxiv.org/html/2511.10081"},{"title":"Fast-Slow Efficient Training for Multimodal Large Language Models via Visual Token Pruning","url":"https://arxiv.org/html/2602.03815"}]

Based on the search results, I found the paper you're looking for. Here's the information about the arXiv paper 2604.12035:

## "Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs"

This paper studies how visual token pruning affects model calibration, that is, whether predicted confidence matches actual correctness.

**Key Details:**
- **Author:** Kaizhen Tan from Carnegie Mellon University
- **Submission Date:** April 13, 2026

**Research Scope:**
Using LLaVA-1.5-7B on POPE and ScienceQA-IMG, the paper evaluates Expected Calibration Error (ECE), Brier score, and AURC under several pruning strategies, including SCOPE with different saliency weights, saliency-only pruning, FastV, and random pruning, across multiple token budgets.

**Main Findings:**
The results show that pruning does not simply trade reliability for efficiency. On POPE, a pure-coverage setting in SCOPE achieves substantially lower ECE than the full unpruned model while maintaining similar accuracy. An internal alpha-sweep further shows a consistent trend: reducing the saliency weight improves calibration at all tested token budgets, while accuracy changes only slightly.

The paper contributes "the first empirical study of how visual token pruning affects calibration in MLLMs, moving the evaluation of pruning beyond accuracy alone."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe61cc41-566e-4c22-bf81-a418ce4fc7df",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "405e4789-b257-4141-96cf-99f3454beb4a",
  "sourceToolAssistantUUID": "fe61cc41-566e-4c22-bf81-a418ce4fc7df",
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

_source line 93 · 2026-05-14T06:15:52.947Z_

<details><summary>↩ Tool result · `toolu_01A9aneUmWTmpyr8eJRkueEX`</summary>

```text
Web search results for query: ""multimodal information bottleneck" deep reinforcement learning multiple sensors robotics 2024 2025"

Links: [{"title":"Multimodal information bottleneck for deep reinforcement learning with multiple sensors - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/38688069/"},{"title":"[2410.17551] Multimodal Information Bottleneck for Deep Reinforcement Learning with Multiple Sensors","url":"https://arxiv.org/abs/2410.17551"},{"title":"Multimodal information bottleneck for deep reinforcement learning with multiple sensors - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608024002715"},{"title":"Multimodal Information Bottleneck for Deep Reinforcement Learning with Multiple Sensors","url":"https://arxiv.org/html/2410.17551"},{"title":"Deep Reinforcement Learning of Mobile Robot Navigation in Dynamic Environment: A Review","url":"https://www.mdpi.com/1424-8220/25/11/3394"},{"title":"Multimodal information bottleneck for deep reinforcement learning with multiple sensors | Neural Networks","url":"https://dl.acm.org/doi/10.1016/j.neunet.2024.106347"},{"title":"Publications | Chenjia Bai","url":"http://baichenjia.cn/publication/"},{"title":"Deep Reinforcement Learning of Mobile Robot Navigation in Dynamic Environment: A Review - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12158180/"},{"title":"A review of embodied intelligence systems: a three-layer framework integrating multimodal perception, world modeling, and structured strategies - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12631203/"},{"title":"Multimodal Reinforcement Learning for Robots Collaborating with Humans | International Journal of Social Robotics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s12369-025-01287-6"}]

Based on the search results, I found highly relevant research on multimodal information bottleneck in deep reinforcement learning with multiple sensors for robotics. Here are the key findings:

## Main Research

Reinforcement learning has achieved promising results on robotic control tasks but struggles to leverage information effectively from multiple sensory modalities that differ in many characteristics. Researchers propose a multimodal information bottleneck model to learn task-relevant joint representations from egocentric images and proprioception.

## Core Problem and Solution

Recent works construct auxiliary losses based on reconstruction or mutual information to extract joint representations from multiple sensory inputs to improve the sample efficiency and performance of reinforcement learning algorithms. However, the representations learned by these methods could capture information irrelevant to learning a policy and may degrade the performance.

The approach compresses and retains the predictive information in multimodal observations for learning a compressed joint representation, which fuses complementary information from visual and proprioceptive feedback and meanwhile filters out task-irrelevant information in raw multimodal observations.

## Performance Results

Experimental evaluations on several challenging locomotion tasks with egocentric images and proprioception show that the method achieves better sample efficiency and zero-shot robustness to unseen white noise than leading baselines.

## Publication Timeline

The research was published on October 23, 2024, with the work also appearing in Neural Networks journal in 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb6803a0-7b2a-4729-8eef-dbf8a0899e17",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "114e68a3-c00a-49a1-b8e0-00cef2b52f2e",
  "sourceToolAssistantUUID": "eb6803a0-7b2a-4729-8eef-dbf8a0899e17",
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

_source line 94 · 2026-05-14T06:15:53.455Z_

<details><summary>↩ Tool result · `toolu_0141s5YQgveV5CZj1p5vD6LU`</summary>

```text
Web search results for query: ""visual token compression enhances model robustness" jailbreak hallucination VLM 2026"

Links: [{"title":"VISUAL TOKEN COMPRESSION ENHANCES MODEL ...","url":"https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"Revisiting Visual Token Pruning for Vision-Language Model ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Endo_Feather_the_Throttle_Revisiting_Visual_Token_Pruning_for_Vision-Language_Model_ICCV_2025_paper.pdf"},{"title":"FlashVLM: Text-Guided Visual Token Selection for Large Multimodal Models","url":"https://arxiv.org/html/2512.20561"},{"title":"Lightweight Visual Language Models","url":"https://www.emergentmind.com/topics/lightweight-visual-language-model-vlm"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models via Visual Information Steering","url":"https://arxiv.org/html/2502.03628v2"},{"title":"(PDF) HybridToken-VLM: Hybrid Token Compression for Vision-Language Models","url":"https://www.researchgate.net/publication/398512398_HybridToken-VLM_Hybrid_Token_Compression_for_Vision-Language_Models"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering | OpenReview","url":"https://openreview.net/forum?id=7BKcLeHQsm"},{"title":"HybridToken-VLM: Hybrid Token Compression for Vision-Language Models","url":"https://arxiv.org/html/2512.08240v1"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"}]

Based on the search results, I found highly relevant research on visual token compression and its relationship to VLM robustness. Here's what the recent research shows:

## Visual Token Compression and VLM Robustness

Recent work investigates how visual token compression influences the robustness of VLMs against jailbreak attacks and hallucinations. The key insight is that intrinsically misaligned visual tokens can serve as out-of-distribution inputs, leading VLMs to produce highly uncertain responses, which increases the risk of jailbreak attacks and hallucinations.

## Practical Solutions in 2026

Researchers have identified "robust-pruning layers"—specific layers where visual token pruning can significantly enhance model robustness against jailbreak attacks and hallucinations, with optimal pruning occurring in layers [13, 17] on SafeBench and [16, 21] on HallusionBench.

Several advanced approaches are being developed:

- FlashVLM achieves beyond-lossless compression while pruning up to 77.8% of visual tokens on LLaVA-1.5, and maintains strong robustness across mainstream VLMs.

- HybridToken-VLM introduces a hybrid framework that disentangles semantics and appearance through dual channels, compressed into a single voco token via a disentanglement attention mask and bottleneck.

- VISTA (Visual Information Steering with Token-logit Augmentation) reveals that visual information gradually attenuates during text generation but can be effectively restored through visual information steering.

This emerging field demonstrates that strategic visual token compression is not just an efficiency technique—it actively enhances safety against adversarial attacks and reduces hallucinations in vision-language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74de4d2c-01cb-459c-af2d-65088f60d00d",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "755935d1-8a8a-4952-847e-c70356d5a5a7",
  "sourceToolAssistantUUID": "74de4d2c-01cb-459c-af2d-65088f60d00d",
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

_source line 95 · 2026-05-14T06:15:53.833Z_

<details><summary>↩ Tool result · `toolu_01ThNnh5Pvpb1UEA1yTDnppC`</summary>

```text
Web search results for query: "CoA-VLA chain-of-affordance vision language action robustness ICCV 2025"

Links: [{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://chain-of-affordance.github.io/"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"},{"title":"ICCV Poster CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance","url":"https://iccv.thecvf.com/virtual/2025/poster/542"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"Add CoA-VLA (Chain-of-Affordance) · Issue #5 · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/issues/5"},{"title":"[PDF] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoA-VLA:-Improving-Vision-Language-Action-Models-Li-Zhu/5760cc722b5eabc14487e9c497a78038ab46f37d"},{"title":"bibtex - ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/ICCV2025?day=2025-10-21"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"}]

Based on the search results, here's what I found about CoA-VLA:

## Overview

CoA-VLA (Chain-of-Affordance VLA) is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion. The paper was presented at ICCV 2025 by Li, Jinming and colleagues.

## Four Types of Affordances

The model considers four types of affordances before taking action: (1) object affordance - what object to manipulate and where it is; (2) grasp affordance - the specific object part to grasp; (3) spatial affordance - the optimal space to place the object; and (4) movement affordance - the collision-free path for movement.

## Technical Approach

Each affordance is transformed into two prompting formats: visual affordance and textual affordance, and a novel vision-language co-injection module integrates this knowledge into the policy network. This allows the robot to leverage essential contextual information during action inference, resulting in improved precision and robustness.

## Performance Results

CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks, and exhibits strong generalization capabilities, including recognizing unseen object poses, identifying free space, and avoiding obstacles in novel environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb0a4c21-c771-436e-94c7-fb7e37222c08",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "5976d7fc-ff06-49fd-9cf8-3245505c7da8",
  "sourceToolAssistantUUID": "eb0a4c21-c771-436e-94c7-fb7e37222c08",
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

_source line 96 · 2026-05-14T06:15:57.224Z_

Let me do a final batch of searches to cover remaining angles - Berkeley RAIL lab VLA work, LIBERO-PRO, and any additional IB-robustness connections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5976d7fc-ff06-49fd-9cf8-3245505c7da8",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yJUn5iN9ZuPrdA1t8V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c3358c0-f8d2-4ff7-9dc2-0d39a081f24f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyFQ5YyTiTVhguEc2Ayr5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4170,
      "cache_read_input_tokens": 47386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4170,
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

_source line 97 · 2026-05-14T06:15:58.249Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016e2HFDmaj8DBwtYQ7yR98i`</summary>

```json
{
  "query": "LIBERO-PRO towards robust fair evaluation VLA models arXiv 2510.03827"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c3358c0-f8d2-4ff7-9dc2-0d39a081f24f",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yJUn5iN9ZuPrdA1t8V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecfeca37-251b-467c-911e-62f4efe62b6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyFQ5YyTiTVhguEc2Ayr5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4170,
      "cache_read_input_tokens": 47386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4170,
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

_source line 98 · 2026-05-14T06:15:59.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018uoYKGgS5xAEiscL7SqoAF`</summary>

```json
{
  "query": "\"historical information bottleneck\" sim-to-real gap privileged knowledge distillation robotics 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecfeca37-251b-467c-911e-62f4efe62b6e",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yJUn5iN9ZuPrdA1t8V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b89cc1ab-88e7-4013-8f88-5400ccb46206",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyFQ5YyTiTVhguEc2Ayr5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4170,
      "cache_read_input_tokens": 47386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4170,
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

_source line 99 · 2026-05-14T06:16:00.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013817cayjmENHX9nRQCKCvF`</summary>

```json
{
  "query": "Berkeley RAIL Sergey Levine VLA robustness token efficiency 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b89cc1ab-88e7-4013-8f88-5400ccb46206",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yJUn5iN9ZuPrdA1t8V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aebf8b85-aee2-44e6-99c3-549a23b5d583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyFQ5YyTiTVhguEc2Ayr5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4170,
      "cache_read_input_tokens": 47386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4170,
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

_source line 100 · 2026-05-14T06:16:01.098Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014izPShj4vJo5V9SYP2gMjE`</summary>

```json
{
  "query": "\"Compressor-VLA\" OR \"RobustVLA\" OR \"CRT\" OR \"SRPO\" VLA robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aebf8b85-aee2-44e6-99c3-549a23b5d583",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yJUn5iN9ZuPrdA1t8V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da79dd14-ab52-4773-8975-1a49ed4270e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyFQ5YyTiTVhguEc2Ayr5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4170,
      "cache_read_input_tokens": 47386,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4170
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 47386,
          "cache_creation_input_tokens": 4170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4170,
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

_source line 101 · 2026-05-14T06:16:04.062Z_

<details><summary>↩ Tool result · `toolu_016e2HFDmaj8DBwtYQ7yR98i`</summary>

```text
Web search results for query: "LIBERO-PRO towards robust fair evaluation VLA models arXiv 2510.03827"

Links: [{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"[2510.03827v1] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827v1"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"Paper page - LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://huggingface.co/papers/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization | alphaXiv","url":"https://www.alphaxiv.org/abs/2510.03827v1"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251003827Z/abstract"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"}]

I found the paper! Here's the information about LIBERO-PRO:

## LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization

**ArXiv ID:** 2510.03827  
**Submitted:** October 4, 2025

### Overview

LIBERO has emerged as a widely adopted benchmark for evaluating Vision-Language-Action (VLA) models; however, its current training and evaluation settings are problematic, often leading to inflated performance estimates and preventing fair model comparison.

### Key Contribution

LIBERO-PRO is an extended LIBERO benchmark that systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments.

### Major Findings

Although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under the generalized setting. This discrepancy exposes the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception.

### Authors

The paper is authored by Xueyang Zhou, Yangming Xu, Guiyao Tie, Yongchao Chen, Guowen Zhang, Duanfeng Chu, Pan Zhou, and Lichao Sun.

The paper includes an official GitHub repository at https://github.com/Zxy-MLlab/LIBERO-PRO for the evaluation suite and code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecfeca37-251b-467c-911e-62f4efe62b6e",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "08c387bd-d2ea-412d-89d4-c6a764ed5893",
  "sourceToolAssistantUUID": "ecfeca37-251b-467c-911e-62f4efe62b6e",
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

_source line 102 · 2026-05-14T06:16:06.604Z_

<details><summary>↩ Tool result · `toolu_018uoYKGgS5xAEiscL7SqoAF`</summary>

```text
Web search results for query: ""historical information bottleneck" sim-to-real gap privileged knowledge distillation robotics 2025"

Links: [{"title":"[2305.18464] Bridging the Sim-to-Real Gap from the Information Bottleneck Perspective","url":"https://arxiv.org/abs/2305.18464"},{"title":"Bridging the Sim-to-Real Gap from the Information Bottleneck Perspective","url":"https://arxiv.org/html/2305.18464v2"},{"title":"Bridging the Sim-to-Real Gap from the Information Bottleneck Perspective","url":"https://proceedings.mlr.press/v270/he25a.html"},{"title":"Bridging the Sim-to-Real Gap from the Information Bottleneck Perspective | OpenReview","url":"https://openreview.net/forum?id=Bq4XOaU4sV"},{"title":"Bridging the Sim-to-Real Gap from the Information Bottleneck Perspective. | Chenjia Bai","url":"http://baichenjia.cn/publication/privileged-knowledge-distillation/"},{"title":"Bridging the Sim-to-Real Gap from the Information Bottleneck Perspective - The Hong Kong University of Science and Technology","url":"https://researchportal.hkust.edu.hk/en/publications/bridging-the-sim-to-real-gap-from-the-information-bottleneck-pers-2/"},{"title":"Bridging the Sim-to-Real Gap from the Information Bottleneck ...","url":"https://raw.githubusercontent.com/mlresearch/v270/main/assets/he25a/he25a.pdf"},{"title":"Publications | Chenjia Bai","url":"http://baichenjia.cn/publication/"},{"title":"Real-is-Sim: Bridging the Sim-to-Real Gap with a Dynamic Digital Twin for Real-World Robot Policy Evaluation","url":"https://arxiv.org/html/2504.03597v1"},{"title":"Learning-based legged locomotion: State of the art and future perspectives - Sehoon Ha, Joonho Lee, Michiel van de Panne, Zhaoming Xie, Wenhao Yu, Majid Khadiv, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649241312698"}]

Based on the search results, I found comprehensive information about the Historical Information Bottleneck (HIB) method for bridging the sim-to-real gap in robotics.

## Key Findings

The Historical Information Bottleneck (HIB) is a novel privileged knowledge distillation method that formulates the sim-to-real gap as an information bottleneck problem.

### The Problem

Most RL works operate in simulated environments where privileged knowledge (e.g., dynamics, surroundings, terrains) is readily available, but in real-world scenarios, robot agents usually rely solely on local states to select actions, leading to a significant sim-to-real gap. Existing methods address this gap by either gradually reducing reliance on privileged knowledge or performing two-stage policy imitation, but these methods are limited in their ability to fully leverage available privileged knowledge, resulting in suboptimal performance.

### The HIB Solution

HIB learns a privileged knowledge representation from historical trajectories by capturing the underlying changeable dynamic information. HIB takes advantage of historical information that contains previous local states and actions to learn a history representation, which is trained by maximizing the mutual information between the representation and the privileged knowledge.

### Theoretical and Practical Results

Theoretical analysis shows that the learned privileged knowledge representation helps reduce the value discrepancy between the oracle and learned policies. Empirical experiments on both simulated and real-world tasks demonstrate that HIB yields improved generalizability compared to previous methods.

The work was published in the Proceedings of The 8th Conference on Robot Learning in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b89cc1ab-88e7-4013-8f88-5400ccb46206",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "0ea8b35b-51b8-47fc-ae0b-3114f78a84c0",
  "sourceToolAssistantUUID": "b89cc1ab-88e7-4013-8f88-5400ccb46206",
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

_source line 103 · 2026-05-14T06:16:07.971Z_

<details><summary>↩ Tool result · `toolu_013817cayjmENHX9nRQCKCvF`</summary>

```text
Web search results for query: "Berkeley RAIL Sergey Levine VLA robustness token efficiency 2025 2026"

Links: [{"title":"Sergey Levine's research works | University of California, Berkeley and other places","url":"https://www.researchgate.net/scientific-contributions/Sergey-Levine-2162794215"},{"title":"[2604.23073] RL Token: Bootstrapping Online RL with Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.23073"},{"title":"Sergey Levine","url":"https://scholar.google.com/citations?user=8R35rCwAAAAJ&hl=en"},{"title":"Sergey Levine (@svlevine) / Posts / X","url":"https://x.com/svlevine"},{"title":"GitHub - rail-berkeley/serl: SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning · GitHub","url":"https://github.com/rail-berkeley/serl"},{"title":"Sergey Levine | EECS at UC Berkeley","url":"https://www2.eecs.berkeley.edu/Faculty/Homepages/svlevine.html"},{"title":"Sergey Levine on IROS 2025 Workshop: Robotic Fine Manipulation: Integrating Tactile, Visual, and Intelligent Control | by Rinn | Jan, 2026 | Medium","url":"https://medium.com/@zlf465074419/sergey-levine-on-iros-2025-workshop-robotic-fine-manipulation-integrating-tactile-visual-and-d1f31f133acb"},{"title":"CS 285","url":"https://rail.eecs.berkeley.edu/deeprlcourse-fa19/"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language- ...","url":"https://aclanthology.org/2025.emnlp-main.1367.pdf"},{"title":"Insights: Robotic Foundation Models, a talk by Sergey Levine from UC Berkeley & Physical Intelligence | by Rinn | Medium","url":"https://medium.com/@zlf465074419/insights-robotic-foundation-models-a-talk-by-prof-32f25b309bce"}]

I found several relevant results about research from UC Berkeley's RAIL lab involving Sergey Levine and VLA (Vision-Language-Action) models. Here are the key findings:

## Recent Research on VLAs and Token Efficiency

A recent paper titled "RL Token: Bootstrapping Online RL with Vision-Language-Action Models" was authored by Charles Xu, Jost Tobias Springenberg, Michael Equi, Ali Amin, Adnan Esmail, Sergey Levine, and Liyiming Ke.

This work introduces a lightweight method that enables sample-efficient online RL fine-tuning of pretrained VLAs using just a few hours of real-world practice. The method adapts the VLA to expose an "RL token," a compact readout representation that preserves task-relevant pretrained knowledge while serving as an efficient interface for online RL.

Across four real-robot tasks (screw installation, zip tie fastening, charger insertion, and Ethernet insertion), RLT improves the speed on the hardest part of the task by up to 3x and raises success rates significantly within minutes to a few hours of practice.

## VLA Robustness Concerns

Current VLA models have so far been evaluated mainly through imitation learning, without explicit optimization for task success rate, robustness, or execution speed. A promising direction is to integrate VLA-style imitation learning with RL-based post-training, enabling joint optimization for improved robustness, adaptability, and real-world performance.

The research suggests that both token efficiency and robustness are active areas of development in the RAIL lab's VLA research in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aebf8b85-aee2-44e6-99c3-549a23b5d583",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "c269777e-a471-42ce-9203-534df305fe19",
  "sourceToolAssistantUUID": "aebf8b85-aee2-44e6-99c3-549a23b5d583",
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

_source line 104 · 2026-05-14T06:16:07.998Z_

<details><summary>↩ Tool result · `toolu_014izPShj4vJo5V9SYP2gMjE`</summary>

```text
Web search results for query: ""Compressor-VLA" OR "RobustVLA" OR "CRT" OR "SRPO" VLA robustness 2025 2026"

Links: [{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037"},{"title":"Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/html/2602.01158"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=9g7UXLqD4B"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"SRPO Code Implementation Explained — siiRL documentation","url":"https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/397231717_RobustVLA_Robustness-Aware_Reinforcement_Post-Training_for_Vision-Language-Action_Models"},{"title":"VLA-RISK: BENCHMARKING VISION-LANGUAGE","url":"https://openreview.net/pdf/2b0044c5e9586d1b0dce44c7f3a73dbc43d13da0.pdf"}]

Based on the web search results, I found relevant information about VLA robustness research from 2025-2026. Here are the key findings:

## Key Research Methods Found

### **RobustVLA**
RobustVLA is a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models. Through a systematic robustness analysis, it identifies two key regularizations: Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations. Extensive experiments across diverse robotic environments demonstrate that RobustVLA significantly outperforms prior state-of-the-art methods in robustness and reliability.

### **Corruption Restoration Transformer (CRT)**
The Corruption Restoration Transformer (CRT) is introduced to handle visual disturbances, serving as a plug-and-play and model-agnostic vision transformer designed to immunize VLA models against sensor disturbances. CRT restores clean observations from corrupted inputs without requiring computationally expensive fine-tuning, and extensive experiments demonstrate that CRT effectively recovers lost performance across the LIBERO and Meta-World benchmarks.

### **SRPO (Supervised Reinforcement Policy Optimization)**
Starting from a supervised baseline with a 48.9% success rate, SRPO achieves a 99.2% success rate on novel states within only 200 RL steps. Furthermore, SRPO shows significant robustness on the LIBERO-Plus benchmark, achieving a 167% performance gain.

These approaches represent recent advances in improving VLA robustness against environmental perturbations, sensor noise, and out-of-distribution scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da79dd14-ab52-4773-8975-1a49ed4270e0",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "a38c89ed-8cfc-4a43-aa7f-dc0388f2dfda",
  "sourceToolAssistantUUID": "da79dd14-ab52-4773-8975-1a49ed4270e0",
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

_source line 105 · 2026-05-14T06:16:10.464Z_

Let me search for a few more critical papers that emerged from these searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a38c89ed-8cfc-4a43-aa7f-dc0388f2dfda",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yKXLPfAfW3jfSRXwQG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cda8c2c1-9378-4e5f-a5fc-f13a60cc775e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RECodkyP1V9eBkjAdRhNKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4232,
      "cache_read_input_tokens": 51556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4232,
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

_source line 106 · 2026-05-14T06:16:11.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ct9adTPqmXVz5yxjRzKpaZ`</summary>

```json
{
  "query": "LIBERO-X robustness litmus VLA models arXiv 2602.06556"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cda8c2c1-9378-4e5f-a5fc-f13a60cc775e",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yKXLPfAfW3jfSRXwQG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e2488b1-2521-4ae5-9e04-444f693ee0d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RECodkyP1V9eBkjAdRhNKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4232,
      "cache_read_input_tokens": 51556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4232,
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

_source line 107 · 2026-05-14T06:16:12.023Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TfYqkPMeVvAmHZGv8WSU7r`</summary>

```json
{
  "query": "VLA-RISK benchmarking vision language action robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e2488b1-2521-4ae5-9e04-444f693ee0d0",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yKXLPfAfW3jfSRXwQG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc3ffbf7-7614-430f-aa4a-efd1c63b4e72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RECodkyP1V9eBkjAdRhNKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4232,
      "cache_read_input_tokens": 51556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4232,
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

_source line 108 · 2026-05-14T06:16:13.024Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R1s6A7QYUeQ3FnfNWuSKMY`</summary>

```json
{
  "query": "\"Bottlenecked Transformers\" periodic KV cache abstraction generalised reasoning arXiv 2505.16950"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc3ffbf7-7614-430f-aa4a-efd1c63b4e72",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yKXLPfAfW3jfSRXwQG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecfa21d0-857f-4fca-9c9b-bdb9ce4ca98f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RECodkyP1V9eBkjAdRhNKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4232,
      "cache_read_input_tokens": 51556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4232,
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

_source line 109 · 2026-05-14T06:16:13.691Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014LJ95D4tBVLnX5Y3FFanrQ`</summary>

```json
{
  "query": "\"token pruning\" OR \"token compression\" \"information bottleneck\" VLA OR VLM robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecfa21d0-857f-4fca-9c9b-bdb9ce4ca98f",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yKXLPfAfW3jfSRXwQG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d6908c4-8ac6-48cc-a6c1-7c8bbf87ff4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RECodkyP1V9eBkjAdRhNKT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4232,
      "cache_read_input_tokens": 51556,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4232
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 51556,
          "cache_creation_input_tokens": 4232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4232,
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

_source line 110 · 2026-05-14T06:16:17.531Z_

<details><summary>↩ Tool result · `toolu_01Ct9adTPqmXVz5yxjRzKpaZ`</summary>

```text
Web search results for query: "LIBERO-X robustness litmus VLA models arXiv 2602.06556"

Links: [{"title":"[2602.06556] LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.06556"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/html/2512.02902"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/html/2602.01158"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"VLANeXt: Recipes for Building Strong VLA Models","url":"https://arxiv.org/html/2602.18532"}]

## Search Results for LIBERO-X arXiv 2602.06556

I found the paper! Here are the key findings:

**Paper Overview:**
LIBERO-X is about reliable benchmarking for Vision-Language-Action (VLA) models, as it reveals their generalization, robustness, and alignment of perception with language-driven manipulation tasks.

**Key Contributions:**

1. **Hierarchical Evaluation Protocol:** The benchmark features a hierarchical evaluation protocol with progressive difficulty levels targeting three core capabilities: spatial generalization, object recognition, and task instruction understanding. This design enables fine-grained analysis of performance degradation under increasing environmental and task complexity.

2. **High-Diversity Training Dataset:** The benchmark includes a high-diversity training dataset collected via human teleoperation, where each scene supports multiple fine-grained manipulation objectives to bridge the train-evaluation gap.

3. **Key Findings:** Experiments with representative VLA models reveal significant performance drops under cumulative perturbations, exposing persistent limitations in scene comprehension and instruction grounding.

The paper was submitted on February 6, 2026, and proposes that by combining hierarchical evaluation protocols with diverse training data, LIBERO-X provides a more reliable foundation for assessing and advancing VLA development.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e2488b1-2521-4ae5-9e04-444f693ee0d0",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "5ef051a8-4bc1-4c35-acc5-bec87532f6d0",
  "sourceToolAssistantUUID": "9e2488b1-2521-4ae5-9e04-444f693ee0d0",
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

_source line 111 · 2026-05-14T06:16:18.311Z_

<details><summary>↩ Tool result · `toolu_01TfYqkPMeVvAmHZGv8WSU7r`</summary>

```text
Web search results for query: "VLA-RISK benchmarking vision language action robustness 2026"

Links: [{"title":"VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness | OpenReview","url":"https://openreview.net/forum?id=31EjDFwFEe"},{"title":"VLA-RISK: BENCHMARKING VISION-LANGUAGE","url":"https://openreview.net/pdf/2b0044c5e9586d1b0dce44c7f3a73dbc43d13da0.pdf"},{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/html/2604.23775"},{"title":"In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=6mEfYoMRpF"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Benchmarking Vision, Language, & Action Models on ...","url":"https://www.preprints.org/manuscript/202411.0494"},{"title":"Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming","url":"https://arxiv.org/html/2604.05595"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations | OpenReview","url":"https://openreview.net/forum?id=cS6xizdYD5"}]

## Search Results

Based on your search query, here's what I found about VLA-RISK:

### Overview
VLA-Risk is a benchmark for assessing the risks of Vision-Language-Action (VLA) models across different input modalities (such as image and instruction) and along three fundamental task dimensions: object, action, and space. The benchmark spans 296 scenarios and 3784 episodes, covering diverse settings such as simple manipulation, semantic reasoning, and autonomous driving.

### Purpose and Scope
VLA models have demonstrated impressive capabilities in unifying visual perception, natural language understanding, and physical action execution, but they introduce new attack surfaces and vulnerabilities across both instruction execution and visual understanding. The field still lacked a unified benchmark to systematically evaluate risk across different modalities.

### Key Findings
Extensive empirical evaluation shows that current state-of-the-art VLA models face substantial challenges under the attack tasks presented in VLA-Risk. By structuring attacks around these dimensions, VLA-Risk provides a principled framework for analyzing vulnerabilities and guiding the development of safer and more robust embodied agents.

### Conference Context
The paper is under review as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc3ffbf7-7614-430f-aa4a-efd1c63b4e72",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "a8ad0b9a-bbc1-41ba-a7c2-1da07dfb66a8",
  "sourceToolAssistantUUID": "fc3ffbf7-7614-430f-aa4a-efd1c63b4e72",
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

_source line 112 · 2026-05-14T06:16:20.045Z_

<details><summary>↩ Tool result · `toolu_01R1s6A7QYUeQ3FnfNWuSKMY`</summary>

```text
Web search results for query: ""Bottlenecked Transformers" periodic KV cache abstraction generalised reasoning arXiv 2505.16950"

Links: [{"title":"[2505.16950] Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning","url":"https://arxiv.org/abs/2505.16950"},{"title":"Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950v2"},{"title":"Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950"},{"title":"(PDF) Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning","url":"https://www.researchgate.net/publication/391991496_Bottlenecked_Transformers_Periodic_KV_Cache_Abstraction_for_Generalised_Reasoning"},{"title":"Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning","url":"https://www.catalyzex.com/paper/bottlenecked-transformers-periodic-kv-cache"},{"title":"Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning | OpenReview","url":"https://openreview.net/forum?id=fWgKnl4itC"},{"title":"[Literature Review] Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning","url":"https://www.themoonlight.io/en/review/bottlenecked-transformers-periodic-kv-cache-abstraction-for-generalised-reasoning"},{"title":"Periodic KV Cache Consolidation for Generalised Reasoning","url":"https://arxiv.org/pdf/2505.16950"},{"title":"Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning","url":"https://powerdrill.ai/discover/summary-bottlenecked-transformers-periodic-kv-cache-cmb1abkzreqv807svnutgrrvr"},{"title":"How Much Cache Does Reasoning Need? Depth–Cache Tradeoffs in KV-Compressed Transformers","url":"https://arxiv.org/html/2604.17935v1"}]

I found the paper! Here's what the search revealed about arXiv paper 2505.16950:

## Paper Overview

The paper introduces the Bottlenecked Transformer, which augments a backbone LLM with a Cache Processor, an auxiliary Transformer that performs periodic, non-causal, in-place KV rewrites at newline-delimited reasoning step boundaries.

## Theoretical Foundation

The authors provide theoretical justification through the lens of Information Bottleneck (IB) theory, which posits that model generalisation emerges from an optimal balance between input information compression and retention of predictive information in latent representations.

## Key Technical Approach

The Processor consolidates recently written KV entries and reconsolidates a small, top-k attention-selected set of prior entries. The paper shows that in autoregressively trained models, the KV cache is incentivised to preserve information from the sequence history that is unnecessary for future sequence-level prediction, potentially hindering generalisation.

## Authors and Publication Details

The paper was authored by Adnan Oomerjee (University College London), Zafeirios Fountas, and Haitham Bou-Ammar. It was submitted on May 22, 2025, with the latest revision on March 25, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecfa21d0-857f-4fca-9c9b-bdb9ce4ca98f",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "abf6108f-6675-4440-9556-80869a7be25b",
  "sourceToolAssistantUUID": "ecfa21d0-857f-4fca-9c9b-bdb9ce4ca98f",
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

_source line 113 · 2026-05-14T06:16:30.841Z_

<details><summary>↩ Tool result · `toolu_014LJ95D4tBVLnX5Y3FFanrQ`</summary>

```text
Web search results for query: ""token pruning" OR "token compression" "information bottleneck" VLA OR VLM robustness 2025 2026"

Links: [{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"VFlowOpt: A Token Pruning Framework for LMMs with Visual Information","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Yang_VFlowOpt_A_Token_Pruning_Framework_for_LMMs_with_Visual_Information_ICCV_2025_paper.pdf"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/html/2601.21531"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"},{"title":"TopV: Compatible Token Pruning with Inference Time Optimization for Fast","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_TopV_Compatible_Token_Pruning_with_Inference_Time_Optimization_for_Fast_CVPR_2025_paper.pdf"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"}]

I've completed a web search for your query about token pruning, token compression, information bottleneck, VLA/VLM, and robustness in 2025-2026. Here are the key findings:

## Token Reduction in VLMs and VLAs (2025-2026)

Recent work includes "CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking" accepted at AAAI'26, which directly combines information bottleneck concepts with token compression.

### VLA-Specific Robustness Research

VLA-IAP demonstrates superior robustness compared to other methods, with at 70% retention achieving a 4.45 average sequence length on CALVIN and 46.3% success rate on VLABench. The dynamic alignment strategy accelerates inference while filtering visual noise to enhance policy focus.

Under extreme compression, existing methods like FastV and SparseVLM suffer catastrophic failures, exposing a fundamental flaw in perception-first methods inherited from traditional VLMs.

### Token Compression Approaches (2025-2026)

LightVLA dynamically selects necessary tokens for each task scenario, leading to improved performance while maintaining significant computational efficiency. Compressor-VLA uses a fixed set of queries as an information bottleneck for token compression, with a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models.

### Adversarial Robustness Concerns

Visual token compression is widely used to accelerate large vision-language models by pruning or merging visual tokens, yet its adversarial robustness remains unexplored.

The research landscape shows extensive recent activity (2025-2026) on token compression for both VLMs and VLAs, with particular focus on robustness, information preservation, and task-specific compression strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d6908c4-8ac6-48cc-a6c1-7c8bbf87ff4e",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "3aaf8aa0-5fbd-41a1-8be4-5e8c2dcfe50d",
  "sourceToolAssistantUUID": "8d6908c4-8ac6-48cc-a6c1-7c8bbf87ff4e",
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

_source line 114 · 2026-05-14T06:16:34.160Z_

Let me do a final round of searches for a few more specific papers that appeared in results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aaf8aa0-5fbd-41a1-8be4-5e8c2dcfe50d",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yMCze2eDrp1tym4yZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5110cf71-aa59-48a5-b011-b605ab8225e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HsNHY2pXGC2ZZmr7yFv2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4078,
      "cache_read_input_tokens": 55788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4078,
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

_source line 115 · 2026-05-14T06:16:34.619Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NGTDve8T7A8QrRtBEXKm4v`</summary>

```json
{
  "query": "VFlowOpt token pruning LMMs visual information flow ICCV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5110cf71-aa59-48a5-b011-b605ab8225e4",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yMCze2eDrp1tym4yZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25b9b898-e253-43c4-b53b-e919a11da17d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HsNHY2pXGC2ZZmr7yFv2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4078,
      "cache_read_input_tokens": 55788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4078,
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

_source line 116 · 2026-05-14T06:16:35.065Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WQFcBpH1MpVPWd48J42a9f`</summary>

```json
{
  "query": "\"CompTrack\" information bottleneck low-rank dynamic token compression AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25b9b898-e253-43c4-b53b-e919a11da17d",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yMCze2eDrp1tym4yZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93bb92c0-971c-4eef-b076-763c1f538c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HsNHY2pXGC2ZZmr7yFv2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4078,
      "cache_read_input_tokens": 55788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4078,
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

_source line 117 · 2026-05-14T06:16:36.037Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014v3K5Z9SuTubC2KJP7qg8s`</summary>

```json
{
  "query": "LIBERO-Para diagnostic benchmark paraphrase robustness VLA models arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93bb92c0-971c-4eef-b076-763c1f538c37",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yMCze2eDrp1tym4yZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ab5f8fa-4b90-45a5-99b8-576cc8e0d8db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HsNHY2pXGC2ZZmr7yFv2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4078,
      "cache_read_input_tokens": 55788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4078,
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

_source line 118 · 2026-05-14T06:16:36.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012sk3h9Jrg9CKSZ84bVkFQS`</summary>

```json
{
  "query": "\"on robustness of vision-language-action model\" \"multi-modal perturbations\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ab5f8fa-4b90-45a5-99b8-576cc8e0d8db",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yMCze2eDrp1tym4yZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9ae2fd4-4503-479f-ae9c-f750d0fa5666",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HsNHY2pXGC2ZZmr7yFv2C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4078,
      "cache_read_input_tokens": 55788,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4078
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 55788,
          "cache_creation_input_tokens": 4078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4078,
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

_source line 119 · 2026-05-14T06:16:40.986Z_

<details><summary>↩ Tool result · `toolu_01NGTDve8T7A8QrRtBEXKm4v`</summary>

```text
Web search results for query: "VFlowOpt token pruning LMMs visual information flow ICCV 2025"

Links: [{"title":"GitHub - sihany077/VFlowOpt: [ICCV 2025] VFlowOpt: A Token Pruning Framework for LMMs with Visual Information Flow-Guided Optimization","url":"https://github.com/sihany077/VFlowOpt"},{"title":"VFlowOpt: A Token Pruning Framework for LMMs with Visual Information","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Yang_VFlowOpt_A_Token_Pruning_Framework_for_LMMs_with_Visual_Information_ICCV_2025_paper.pdf"},{"title":"[2508.05211] VFlowOpt: A Token Pruning Framework for LMMs with Visual Information Flow-Guided Optimization","url":"https://arxiv.org/abs/2508.05211"},{"title":"VFlowOpt: A Token Pruning Framework for LMMs with Visual Information Flow-Guided Optimization","url":"https://arxiv.org/html/2508.05211"},{"title":"Paper page - VFlowOpt: A Token Pruning Framework for LMMs with Visual Information Flow-Guided Optimization","url":"https://huggingface.co/papers/2508.05211"},{"title":"VFlowOpt: A Token Pruning Framework for LMMs with Visual Information","url":"https://arxiv.org/pdf/2508.05211"},{"title":"GitHub - Theia-4869/VisPruner: [ICCV 2025] Official code for paper: Beyond Text-Visual Attention: Exploiting Visual Cues for Effective Token Pruning in VLMs","url":"https://github.com/Theia-4869/VisPruner"},{"title":"[PDF] ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ATP-LLaVA:-Adaptive-Token-Pruning-for-Large-Vision-Ye-Gan/134a66cc64344b9ef913e0f25c2fab6f4ff92c94"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"About Me - Runsen Xu’s Homepage","url":"https://runsenxu.com/"}]

Based on the search results, here's information about VFlowOpt:

## Overview

VFlowOpt is a novel, training-free token pruning framework designed to enhance the efficiency of Large Multimodal Models (LMMs) by addressing high computational costs from excessive visual tokens. The paper was presented at ICCV 2025.

## Key Technical Approach

VFlowOpt introduces an importance map derivation process and a progressive pruning module with a recycling mechanism. Specifically:

- It computes an importance map for image tokens based on their attention-derived context relevance and patch-level information entropy.
- Pruned tokens are aggregated as recycled tokens to avoid potential information loss.
- A visual information flow-guided method regards the last token in the LMM as the most representative signal of text-visual interactions, minimizing the discrepancy between token representations in LMMs with and without pruning.

## Performance Results

VFlowOpt can prune 90% of visual tokens while maintaining comparable performance, leading to an 89% reduction in KV-Cache memory and 3.8 times faster inference. It achieves zero performance degradation when reducing 50% of visual tokens.

The code is available on GitHub at the sihany077/VFlowOpt repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25b9b898-e253-43c4-b53b-e919a11da17d",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "ed0dd865-ae0b-4acd-b8a6-a924a76a70e5",
  "sourceToolAssistantUUID": "25b9b898-e253-43c4-b53b-e919a11da17d",
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

_source line 120 · 2026-05-14T06:16:41.576Z_

<details><summary>↩ Tool result · `toolu_01WQFcBpH1MpVPWd48J42a9f`</summary>

```text
Web search results for query: ""CompTrack" information bottleneck low-rank dynamic token compression AAAI 2026"

Links: [{"title":"[2511.15580] CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking","url":"https://arxiv.org/abs/2511.15580"},{"title":"Information Bottleneck-Guided Low-Rank Dynamic Token ...","url":"https://ojs.aaai.org/index.php/AAAI/article/view/38385/42347"},{"title":"CompTrack: Information Bottleneck-Guided Low-Rank","url":"https://ojs.aaai.org/index.php/AAAI/article/download/38385/42347"},{"title":"CompTrack: Information Bottleneck‑Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking","url":"https://arxiv.org/html/2511.15580"},{"title":"Date Session Title Paper ID Paper Title Authors 22397 18021 5718 13962 11117","url":"https://aaai.org/wp-content/uploads/2026/01/Main-track-oral-talks.pdf"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"CompTrack: Information Bottleneck-Guided Low-Rank ...","url":"https://arxiv.org/pdf/2511.15580"},{"title":"CompTrack: Information Bottleneck-Guided Low-Rank ...","url":"https://www.researchgate.net/publication/402625478_CompTrack_Information_Bottleneck-Guided_Low-Rank_Dynamic_Token_Compression_for_Point_Cloud_Tracking"},{"title":"Dynamic Token Compression for Efficient Video Understanding through Reinforcement Learning","url":"https://arxiv.org/html/2603.26365v1"},{"title":"An Efficient Token Compression Framework for Visual Object Tracking","url":"https://arxiv.org/html/2605.08329"}]

Based on the search results, here's what I found about CompTrack:

## CompTrack Overview

CompTrack is a novel end-to-end framework that systematically eliminates both forms of redundancy in point clouds for 3D single object tracking in LiDAR-based applications.

## Key Components

The framework consists of two main modules:

1. **Spatial Foreground Predictor (SFP)**: CompTrack incorporates a Spatial Foreground Predictor (SFP) module to filter out irrelevant background noise based on information entropy, addressing spatial redundancy.

2. **Information Bottleneck-guided Dynamic Token Compression (IB-DTC)**: An Information Bottleneck-guided Dynamic Token Compression (IB-DTC) module that eliminates the informational redundancy within the foreground. Theoretically grounded in low-rank approximation, this module leverages an online SVD analysis to adaptively compress the redundant foreground into a compact and highly informative set of proxy tokens.

## Performance

Extensive experiments on KITTI, nuScenes and Waymo datasets demonstrate that CompTrack achieves top-performing tracking performance with superior efficiency, running at a real-time 90 FPS on a single RTX 3090 GPU.

## AAAI 2026

The paper was accepted to AAAI 2026 with authors Sifan Zhou, Yichao Cao, Jiahao Nie, Yuqian Fu, Ziyu Zhao, Xiaobo Lu, and Shuo Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93bb92c0-971c-4eef-b076-763c1f538c37",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "2ba1cf1f-0c45-475a-952f-83a55546702f",
  "sourceToolAssistantUUID": "93bb92c0-971c-4eef-b076-763c1f538c37",
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

_source line 121 · 2026-05-14T06:16:44.076Z_

<details><summary>↩ Tool result · `toolu_014v3K5Z9SuTubC2KJP7qg8s`</summary>

```text
Web search results for query: "LIBERO-Para diagnostic benchmark paraphrase robustness VLA models arXiv 2603"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://cau-hai-lab.github.io/LIBERO-Para/"},{"title":"Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://huggingface.co/papers/2603.28301"},{"title":"GitHub - cau-hai-lab/LIBERO-Para · GitHub","url":"https://github.com/cau-hai-lab/LIBERO-Para"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"}]

I found information about LIBERO-Para. Here's what the search revealed:

## LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models

LIBERO-Para is a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization.

### Key Findings

Across seven VLA configurations (0.6B–7.5B), there is consistent performance degradation of 22–52 pp under paraphrasing. This degradation is primarily driven by object-level lexical variation: even simple synonym substitutions cause large drops, indicating reliance on surface-level matching rather than semantic grounding.

### Motivation

Vision–Language–Action (VLA) models achieve strong performance in robotic manipulation by leveraging pre-trained vision–language backbones. However, in downstream robotic settings, they are typically fine-tuned with limited data, leading to overfitting to specific instruction formulations and leaving robustness to paraphrased instructions underexplored.

### The PRIDE Metric

The paper introduces PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation), a metric that combines keyword similarity (lexical shift) and structural similarity (syntactic variation) with task success to enable fine-grained robustness analysis.

### Benchmark Design

LIBERO-Para is grounded in the linguistic structure of robotic manipulation instructions—where actions and objects serve as core semantic elements—and adopts a two-axis design that independently varies action expressions and object references. The benchmark includes 4,000+ paraphrased instructions across 10 evaluation scenarios.

The paper (arXiv 2603.28301) reveals critical vulnerabilities in current VLA models regarding their ability to handle paraphrased instructions, highlighting the gap between apparent capability and actual robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ab5f8fa-4b90-45a5-99b8-576cc8e0d8db",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "89f3ecc5-c4e7-4f2d-bbe1-8196664d00fa",
  "sourceToolAssistantUUID": "7ab5f8fa-4b90-45a5-99b8-576cc8e0d8db",
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

_source line 122 · 2026-05-14T06:16:44.998Z_

<details><summary>↩ Tool result · `toolu_012sk3h9Jrg9CKSZ84bVkFQS`</summary>

```text
Web search results for query: ""on robustness of vision-language-action model" "multi-modal perturbations" ICLR 2026"

Links: [{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"ON ROBUSTNESS OF VISION-LANGUAGE-ACTION ...","url":"https://openreview.net/pdf/4c9de20f29e6aad53dfd1f3b339230208e43a2ff.pdf"},{"title":"ON ROBUSTNESS OF VISION-LANGUAGE-ACTION MODEL ...","url":"https://openreview.net/pdf/24afaa89d3b5edf893bafacccbf39c79e5ed2973.pdf"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=6mEfYoMRpF"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations | OpenReview","url":"https://openreview.net/forum?id=cS6xizdYD5"},{"title":"[2510.00037] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037"},{"title":"[2510.00037v4] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037v4"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/460a1d8eac34125dad453b28d6d64446-Paper-Conference.pdf"},{"title":"Chain of Attack: On the Robustness of Vision-Language Models Against","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Xie_Chain_of_Attack_On_the_Robustness_of_Vision-Language_Models_Against_CVPR_2025_paper.pdf"}]

I found several highly relevant papers for your search query. Here are the key results:

## Primary Match: "On Robustness of Vision-Language-Action Model Against Multi-Modal Perturbations"

This paper, under review at ICLR 2026, addresses robustness of Vision–Language–Action (VLA) models to real-world perturbations critical for deployment. 

The work notes that existing methods target simple visual disturbances, overlooking broader multi-modal perturbations in actions, instructions, environments, and observations, and evaluates the robustness of mainstream VLAs under 17 perturbations across four modalities.

Key findings include: (1) actions as the most fragile modality, (2) existing visual-robust VLAs do not gain robustness in other modalities, and (3) π0 demonstrates superior robustness. The paper proposes RobustVLA against perturbations in VLA inputs and outputs.

On the LIBERO benchmark, RobustVLA achieves absolute gains of 12.6% on the π0 backbone and 10.4% on the OpenVLA backbone across 17 perturbations, being 50.6x faster than visual-robust BYOVLA that requires external LLMs.

## Secondary Match: "In-Depth Robustness Analysis for Vision-Language-Action Models"

Another ICLR 2026 submission performs systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

This analysis exposes critical weaknesses where models exhibit extreme sensitivity to perturbation factors including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9ae2fd4-4503-479f-ae9c-f750d0fa5666",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a39f9fcd5ae529f28",
  "type": "user",
  "uuid": "da5e0100-2878-4efc-bdb7-5f6c7842853b",
  "sourceToolAssistantUUID": "d9ae2fd4-4503-479f-ae9c-f750d0fa5666",
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

_source line 123 · 2026-05-14T06:18:06.900Z_

Now I have a comprehensive picture. Let me compile my findings into a thorough report.

---

Here is my comprehensive report of potentially competing or concurrent work that is NOT already in your cited list. I have organized them by relevance tier.

## TIER 1: HIGHLY RELEVANT -- Directly combine token pruning/compression with robustness or IB in VLAs/VLMs

### 1. "Visual Token Compression Enhances Model Robustness" (2026)
- **Venue**: Under review / OpenReview
- **URL**: https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf
- **Why relevant**: Directly studies how visual token compression enhances VLM robustness against jailbreaks and hallucinations. Identifies "robust-pruning layers" -- specific layers where token pruning significantly enhances robustness. This is the most directly competing idea: that token compression itself IS a robustness mechanism, not just an efficiency one.

### 2. "Efficient Vision-Language Reasoning via Adaptive Token Pruning" (ATP) (arXiv 2512.12701)
- **Venue**: OpenReview (under review)
- **URL**: https://arxiv.org/abs/2512.12701
- **Why relevant**: Shows that adaptive token pruning in VLMs improves robustness under Gaussian noise, blur, and occlusion by pruning noisy background patches. Explicitly argues "resource-constrained inference and model reliability are not competing objectives" -- very close to the IB-for-robustness thesis.

### 3. "Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs" (arXiv 2604.12035, April 2026)
- **URL**: https://arxiv.org/abs/2604.12035
- **Why relevant**: First empirical study of how visual token pruning affects calibration in MLLMs. Finds pruning can actually improve calibration (reduce ECE). Directly relevant to the robustness-through-compression argument.

### 4. "Multimodal Information Bottleneck for Deep Reinforcement Learning with Multiple Sensors" (Neural Networks 2024, arXiv 2410.17551)
- **URL**: https://arxiv.org/abs/2410.17551
- **Why relevant**: Proposes a multimodal IB model for learning task-relevant joint representations from egocentric images and proprioception in robotics. Achieves zero-shot robustness to unseen noise. Directly extends IB to multimodal robotics -- a close conceptual neighbor to your paper's approach.

### 5. "Bridging the Sim-to-Real Gap from the Information Bottleneck Perspective" (HIB) (CoRL 2025, arXiv 2305.18464)
- **URL**: https://arxiv.org/abs/2305.18464
- **Why relevant**: Uses an information bottleneck (Historical Information Bottleneck, HIB) for privileged knowledge distillation in robot locomotion. Directly applies IB to robustness in robotics (sim-to-real gap). Published at CoRL 2025.

### 6. "Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning" (arXiv 2505.16950)
- **URL**: https://arxiv.org/abs/2505.16950
- **Why relevant**: Provides theoretical justification through Information Bottleneck theory for KV cache compression in Transformers, arguing that periodic information compression improves generalization. While not robotics-specific, the IB-based theoretical framework for token-level compression is directly relevant.

## TIER 2: VERY RELEVANT -- VLA token pruning methods (competing on the pruning side, may be combinable or competing baselines)

### 7. VLA-Pruner (arXiv 2511.16449, Feb 2026)
- **URL**: https://arxiv.org/abs/2511.16449
- **Why relevant**: Dual-level (semantic + action) token pruning for VLAs with temporal awareness. Addresses the specific issue that VLM pruning methods fail in VLAs because they ignore action-level importance.

### 8. SpecPrune-VLA (arXiv 2509.05614)
- **URL**: https://arxiv.org/abs/2509.05614
- **Why relevant**: Action-aware self-speculative pruning that classifies actions as coarse vs. fine-grained to adjust pruning aggressiveness. 1.57x speedup on LIBERO.

### 9. EcoVLA / Environment-Aware Adaptive Pruning (arXiv 2602.00780, Jan 2026)
- **URL**: https://arxiv.org/abs/2602.00780
- **Why relevant**: Training-free adaptive channel pruning for VLAs that adapts sparsity patterns based on temporal consistency of the physical environment. Up to 1.60x speedup.

### 10. SP-VLA (arXiv 2506.12723, ICLR 2026)
- **URL**: https://arxiv.org/abs/2506.12723
- **Why relevant**: Joint model scheduling + spatio-semantic dual-aware token pruning. Accepted at ICLR 2026. Achieves 1.5x lossless acceleration on LIBERO.

### 11. ETA-VLA (arXiv 2603.25766, March 2026)
- **URL**: https://arxiv.org/abs/2603.25766
- **Why relevant**: Temporal fusion + intra-LLM sparse aggregation with text-guided scoring and diversity-preserving sparsification. Prunes 85% of visual tokens.

### 12. Action-aware Dynamic Pruning (ADP) (arXiv 2509.22093)
- **URL**: https://arxiv.org/abs/2509.22093
- **Why relevant**: Multi-modal pruning framework with action trajectory gating -- adjusts token retention based on action dynamics (coarse vs. fine manipulation).

### 13. TTF-VLA (arXiv 2508.19257)
- **URL**: https://arxiv.org/abs/2508.19257
- **Why relevant**: Temporal token fusion that addresses vulnerability to visual noise by fusing historical and current visual representations. Improves LIBERO by 4.0pp.

### 14. EfficientVLA (arXiv 2506.10100, NeurIPS 2025)
- **URL**: https://arxiv.org/abs/2506.10100
- **Why relevant**: Holistic framework combining layer pruning, task-aware visual token selection, and diffusion head caching. 1.93x speedup.

### 15. OneWM-VLA (arXiv 2605.07931, May 2026)
- **URL**: https://arxiv.org/abs/2605.07931
- **Why relevant**: Extreme token compression (one token per frame per view) via Adaptive Attention Pooling. Achieves 95.6% on LIBERO-Long despite extreme compression.

### 16. VLA-Cache (arXiv 2502.02175, NeurIPS 2025)
- **URL**: https://arxiv.org/abs/2502.02175
- **Why relevant**: Adaptive token caching exploiting temporal continuity. 1.7x speedup.

### 17. Spec-VLA (arXiv 2507.22424)
- **URL**: https://arxiv.org/abs/2507.22424
- **Why relevant**: Speculative decoding for VLAs with relaxed acceptance criteria. Different approach (decoding, not pruning) but competing on VLA efficiency.

## TIER 3: RELEVANT -- VLA robustness benchmarks and methods (context papers)

### 18. "On Robustness of VLA Model against Multi-Modal Perturbations" (arXiv 2510.00037, ICLR 2026)
- **URL**: https://arxiv.org/abs/2510.00037
- **Why relevant**: Systematic robustness evaluation of VLAs under 17 perturbations across 4 modalities. Finds actions are the most fragile modality. Published at ICLR 2026.

### 19. LIBERO-X (arXiv 2602.06556, Feb 2026)
- **URL**: https://arxiv.org/abs/2602.06556
- **Why relevant**: Another LIBERO robustness benchmark with hierarchical evaluation and progressive difficulty levels. Complements LIBERO-Plus.

### 20. LIBERO-PRO (arXiv 2510.03827)
- **URL**: https://arxiv.org/abs/2510.03827
- **Why relevant**: Shows VLA performance collapses to 0% under generalized settings, exposing memorization. Relevant robustness benchmark.

### 21. LIBERO-Para (arXiv 2603.28301, March 2026)
- **URL**: https://arxiv.org/abs/2603.28301
- **Why relevant**: Benchmark for paraphrase robustness showing 22-52pp degradation under simple synonym substitutions.

### 22. VLA-RISK (OpenReview, under review at ICLR 2026)
- **URL**: https://openreview.net/forum?id=31EjDFwFEe
- **Why relevant**: Benchmark spanning 296 scenarios evaluating VLA robustness across object, action, and space dimensions.

### 23. HybridVLA (arXiv 2503.10631)
- **URL**: https://arxiv.org/abs/2503.10631
- **Why relevant**: Collaborative action ensemble for "more robust control" by adaptively fusing diffusion and autoregressive action predictions.

### 24. CoA-VLA (arXiv 2412.20451, ICCV 2025)
- **URL**: https://arxiv.org/abs/2412.20451
- **Why relevant**: Chain-of-affordance approach improving VLA robustness through explicit affordance reasoning.

## TIER 4: RELEVANT VLM TOKEN PRUNING (not VLA-specific, but methodologically relevant)

### 25. FEATHER (arXiv 2412.13180, ICCV 2025) -- Stanford
- **URL**: https://arxiv.org/abs/2412.13180
- **Why relevant**: Discovers RoPE-induced positional bias in attention-based token pruning. Proposes ensemble criteria. From Stanford (Serena Yeung-Levy's group).

### 26. AgilePruner (arXiv 2603.01236, ICLR 2026)
- **URL**: https://arxiv.org/abs/2603.01236
- **Why relevant**: Empirical study showing diversity-preserving pruning increases hallucination, while attention-based pruning reduces it. Proposes image-aware adaptive pruning.

### 27. LearnPruner (arXiv 2604.23950, April 2026)
- **URL**: https://arxiv.org/abs/2604.23950
- **Why relevant**: Two-stage pruning framework leveraging attention sink analysis. Retains only 5.5% of vision tokens with 95% performance.

### 28. Attention Debiasing for Token Pruning (PoRe) (arXiv 2508.17807)
- **URL**: https://arxiv.org/abs/2508.17807
- **Why relevant**: Identifies systematic attention bias in VLMs (recency bias, attention sink in padding) that causes bad pruning decisions. Proposes debiasing.

### 29. ATP-LLaVA (CVPR 2025, arXiv 2412.00447)
- **URL**: https://arxiv.org/abs/2412.00447
- **Why relevant**: Instance-adaptive pruning ratios per LLM layer with spatial augmentation. 75% token reduction.

### 30. TPRL (arXiv 2603.13394, March 2026)
- **URL**: https://arxiv.org/abs/2603.13394
- **Why relevant**: Uses reinforcement learning to learn adaptive pruning trajectories for VLMs. Interesting methodological alternative.

### 31. RL Token (arXiv 2604.23073) -- UC Berkeley (Sergey Levine)
- **URL**: https://arxiv.org/abs/2604.23073
- **Why relevant**: From Berkeley RAIL lab. Bootstraps online RL with VLAs using compact "RL token" readout. Not directly on pruning-for-robustness but from a key lab.

### 32. Token Communication via GenIB (arXiv 2507.01728)
- **URL**: https://arxiv.org/abs/2507.01728
- **Why relevant**: Proposes Generative Information Bottleneck (GenIB) for token-level communication in multimodal models. Relevant IB + token methodology.

### 33. CompTrack (arXiv 2511.15580, AAAI 2026)
- **URL**: https://arxiv.org/abs/2511.15580
- **Why relevant**: Information Bottleneck-guided dynamic token compression (for point cloud tracking, not VLAs, but the IB-guided token compression methodology is directly relevant).

---

## Summary of Most Critical Missing References

The papers I would flag as **highest priority** to check against your cited list:

1. **"Visual Token Compression Enhances Model Robustness"** -- Directly argues compression improves robustness (jailbreaks, hallucinations), identifying optimal pruning layers.
2. **"Efficient Vision-Language Reasoning via Adaptive Token Pruning" (ATP, 2512.12701)** -- Empirically shows adaptive pruning improves noise/blur/occlusion robustness in VLMs.
3. **"Multimodal Information Bottleneck for Deep RL with Multiple Sensors" (2410.17551)** -- IB for multimodal robotics with zero-shot noise robustness.
4. **"Bridging the Sim-to-Real Gap from the Information Bottleneck Perspective" (HIB, CoRL 2025)** -- IB for robust robot policy transfer.
5. **VLA-Pruner (2511.16449)**, **EcoVLA (2602.00780)**, **SP-VLA (2506.12723)**, **ETA-VLA (2603.25766)** -- Recent VLA-specific token pruning methods that should be compared against.
6. **"On Robustness of VLA Model against Multi-Modal Perturbations" (2510.00037, ICLR 2026)** -- Major robustness study at a top venue.
7. **"Does Visual Token Pruning Improve Calibration?" (2604.12035)** -- First study linking token pruning to calibration improvement.
8. **OneWM-VLA (2605.07931)** -- Extreme one-token-per-frame compression for VLAs (May 2026, very recent).

Sources:
- [VLA-Pruner](https://arxiv.org/abs/2511.16449)
- [SpecPrune-VLA](https://arxiv.org/abs/2509.05614)
- [EcoVLA](https://arxiv.org/abs/2602.00780)
- [SP-VLA](https://arxiv.org/abs/2506.12723)
- [ETA-VLA](https://arxiv.org/abs/2603.25766)
- [ADP](https://arxiv.org/abs/2509.22093)
- [TTF-VLA](https://arxiv.org/abs/2508.19257)
- [EfficientVLA](https://arxiv.org/abs/2506.10100)
- [OneWM-VLA](https://arxiv.org/abs/2605.07931)
- [VLA-Cache](https://arxiv.org/abs/2502.02175)
- [Spec-VLA](https://arxiv.org/abs/2507.22424)
- [ATP](https://arxiv.org/abs/2512.12701)
- [Visual Token Compression Enhances Robustness](https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf)
- [Does Token Pruning Improve Calibration](https://arxiv.org/abs/2604.12035)
- [Multimodal IB for RL](https://arxiv.org/abs/2410.17551)
- [HIB (CoRL 2025)](https://arxiv.org/abs/2305.18464)
- [Bottlenecked Transformers](https://arxiv.org/abs/2505.16950)
- [On Robustness of VLA (ICLR 2026)](https://arxiv.org/abs/2510.00037)
- [LIBERO-X](https://arxiv.org/abs/2602.06556)
- [LIBERO-PRO](https://arxiv.org/abs/2510.03827)
- [LIBERO-Para](https://arxiv.org/abs/2603.28301)
- [VLA-RISK](https://openreview.net/forum?id=31EjDFwFEe)
- [HybridVLA](https://arxiv.org/abs/2503.10631)
- [CoA-VLA](https://arxiv.org/abs/2412.20451)
- [FEATHER (ICCV 2025)](https://arxiv.org/abs/2412.13180)
- [AgilePruner (ICLR 2026)](https://arxiv.org/abs/2603.01236)
- [LearnPruner](https://arxiv.org/abs/2604.23950)
- [Attention Debiasing / PoRe](https://arxiv.org/abs/2508.17807)
- [ATP-LLaVA (CVPR 2025)](https://arxiv.org/abs/2412.00447)
- [TPRL](https://arxiv.org/abs/2603.13394)
- [RL Token (Berkeley)](https://arxiv.org/abs/2604.23073)
- [GenIB Token Communication](https://arxiv.org/abs/2507.01728)
- [CompTrack (AAAI 2026)](https://arxiv.org/abs/2511.15580)
- [Gemini Robotics](https://arxiv.org/abs/2503.20020)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da5e0100-2878-4efc-bdb7-5f6c7842853b",
  "isSidechain": true,
  "agentId": "a39f9fcd5ae529f28",
  "requestId": "req_011Cb1yNFZhGgAAS1KafCF27",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a563b130-eafc-4a67-bcc5-808c702ad6d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPZy9KsbagGFA2wnvndnfR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4254,
      "cache_read_input_tokens": 59866,
      "output_tokens": 4594,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4254
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4594,
          "cache_read_input_tokens": 59866,
          "cache_creation_input_tokens": 4254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4254,
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
