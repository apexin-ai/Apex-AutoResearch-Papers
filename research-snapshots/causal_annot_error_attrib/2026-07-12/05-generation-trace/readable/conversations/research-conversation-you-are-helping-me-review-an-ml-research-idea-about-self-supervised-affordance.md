# Research conversation: You are helping me review an ML research idea about "self-supervised affordance learning in Vision-Language-Action model

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 97
- **Recorded user turns:** 1
- **Tool calls:** 42
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae1282733b41002fe.jsonl`
- **Structured JSON:** [`f790b727a58b88493f00.json`](../../sessions/f7/f790b727a58b88493f00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

97 recorded events

### User

_source line 1 · 2026-05-18T20:02:28.129Z_

You are helping me review an ML research idea about "self-supervised affordance learning in Vision-Language-Action models using instruction paraphrase invariance." The core idea is: for a given robot manipulation scene, different paraphrases of the same instruction (e.g., "pick up the cup" vs "grab the mug") should activate the same affordance regions in the visual features. This consistency signal is used as self-supervision to train an affordance decoder within a VLA, eliminating the need for affordance annotations.

I need you to search thoroughly for competing/overlapping work that may undermine the novelty of this idea. Use WebSearch extensively. Search for:

1. "paraphrase invariance" + "affordance" or "robot manipulation" - any work using paraphrase consistency for affordance learning
2. "instruction invariance" + "robot" or "manipulation" - any work using instruction invariance as self-supervision
3. "self-supervised affordance" + "VLA" or "vision language action" - any self-supervised affordance work in VLA context
4. "consistency regularization" + "affordance" + "robot" - consistency-based affordance training
5. "language grounding consistency" + "manipulation" - language grounding consistency in manipulation
6. "open vocabulary affordance" + "end-to-end" + "VLA" 2025 2026 - the core claimed gap
7. Search for the most recent affordance + VLA papers from 2025-2026
8. Search for "affordance VLA" on arXiv for anything from the last 6 months
9. "contrastive affordance learning language" 2025 2026
10. "instruction augmentation robot policy" self-supervised 2025 2026

For each search, report: the query used, key results found, and whether any result threatens the novelty of the proposed idea. Be thorough and skeptical.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "f55e335d-7882-4efc-b291-daf0c5d5e635",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T20:02:28.134Z_

```json
{
  "parentUuid": "f55e335d-7882-4efc-b291-daf0c5d5e635",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "46308422-817e-4343-951a-881536079abb",
  "timestamp": "2026-05-18T20:02:28.134Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T20:02:31.171Z_



I'll conduct a thorough literature search across all 10 queries. Let me start by loading the WebSearch tool and then executing searches in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46308422-817e-4343-951a-881536079abb",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdZxDTYAPtEeSMNJmAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9ca6481-7c86-4ba0-aafc-a8f4f460f224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AriBi8PQE5hL7RaB7PZbzt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 954,
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

_source line 4 · 2026-05-18T20:02:31.317Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016SteGBy51HM4pKumkYivNC`</summary>

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
  "parentUuid": "f9ca6481-7c86-4ba0-aafc-a8f4f460f224",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdZxDTYAPtEeSMNJmAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a68f066-5d40-43fd-8da5-5375a45aeca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AriBi8PQE5hL7RaB7PZbzt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 7304,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 954
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 954,
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

_source line 5 · 2026-05-18T20:02:31.320Z_

<details><summary>↩ Tool result · `toolu_016SteGBy51HM4pKumkYivNC`</summary>

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
  "parentUuid": "0a68f066-5d40-43fd-8da5-5375a45aeca4",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "011910ae-4bd5-43dd-bfb5-f40fb05ae0dc",
  "sourceToolAssistantUUID": "0a68f066-5d40-43fd-8da5-5375a45aeca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T20:02:34.126Z_



Now let me execute all 10 searches. I'll batch them in groups to be efficient.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "011910ae-4bd5-43dd-bfb5-f40fb05ae0dc",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdaBxCdZfgQ1Yfn63Um",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e207504-b6ce-432c-b20d-dfeb6313ff3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa2bYpY6aCCdccwnXsyFPX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 7 · 2026-05-18T20:02:34.661Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LHJhYcuphn3YZNHGXMgLuw`</summary>

```json
{
  "query": "\"paraphrase invariance\" affordance robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e207504-b6ce-432c-b20d-dfeb6313ff3a",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdaBxCdZfgQ1Yfn63Um",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "214de039-3dd8-486c-bba3-98be4c31282b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa2bYpY6aCCdccwnXsyFPX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 8 · 2026-05-18T20:02:34.669Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ADyiHsnFVDTWLtWg554J2Q`</summary>

```json
{
  "query": "\"instruction invariance\" robot manipulation self-supervision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "214de039-3dd8-486c-bba3-98be4c31282b",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdaBxCdZfgQ1Yfn63Um",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6dfa6de2-a767-489b-928f-3bda20de1466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa2bYpY6aCCdccwnXsyFPX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 9 · 2026-05-18T20:02:35.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0142rmAqrfDASoGhrQyepuip`</summary>

```json
{
  "query": "\"self-supervised affordance\" VLA \"vision language action\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dfa6de2-a767-489b-928f-3bda20de1466",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdaBxCdZfgQ1Yfn63Um",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc842560-17ca-4318-9ef6-f4e27fda799f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa2bYpY6aCCdccwnXsyFPX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 10 · 2026-05-18T20:02:35.600Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0178yYFH8M5j1KGB3V7P9EHc`</summary>

```json
{
  "query": "\"consistency regularization\" affordance robot manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc842560-17ca-4318-9ef6-f4e27fda799f",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdaBxCdZfgQ1Yfn63Um",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53beafe8-2e44-49af-aae3-7cac38482221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa2bYpY6aCCdccwnXsyFPX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 11 · 2026-05-18T20:02:35.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014AtUsuegH6xtYCVzgzw14s`</summary>

```json
{
  "query": "\"language grounding consistency\" manipulation robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53beafe8-2e44-49af-aae3-7cac38482221",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdaBxCdZfgQ1Yfn63Um",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cca99ab-dc9d-4b5f-a7bb-2808f7f240db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qa2bYpY6aCCdccwnXsyFPX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 12 · 2026-05-18T20:02:41.086Z_

<details><summary>↩ Tool result · `toolu_01ADyiHsnFVDTWLtWg554J2Q`</summary>

```text
Web search results for query: ""instruction invariance" robot manipulation self-supervision"

Links: [{"title":"Self-Supervised Learning For Robust Robotic Grasping In Dynamic   Environment","url":"https://arxiv.org/pdf/2410.11229"},{"title":"Learning Dense Visual Descriptors using Image Augmentations for Robot   Manipulation Tasks","url":"https://arxiv.org/pdf/2209.05213"},{"title":"Self-Supervised Learning of Multi-Object Keypoints for Robotic   Manipulation","url":"https://arxiv.org/pdf/2205.08316"},{"title":"LaVA-Man: Learning Visual Action Representations for Robot Manipulation","url":"https://arxiv.org/pdf/2508.19391"},{"title":"[2205.08316] Self-Supervised Learning of Multi-Object Keypoints for Robotic Manipulation","url":"https://arxiv.org/abs/2205.08316"},{"title":"Learning from Imperfect Demonstrations with Self-Supervision for Robotic   Manipulation","url":"https://arxiv.org/pdf/2401.08957"}]

I've found several research papers related to self-supervised learning for robot manipulation. Here are the key findings:

## Self-Supervised Learning for Robot Manipulation

The search results cover several important approaches:

**Language-Guided Visual Representations:**
LaVA-Man is a self-supervised learning approach for learning language-guided visual-action representations for robot manipulation, which masks goal images and trains models to predict masked content conditioned on input images and language instructions.

**Robust Grasping in Dynamic Environments:**
The general problem of realizing robot grasp in uncertain and changing contexts is essential for robotic manipulation in areas of industrial automation, healthcare, and autonomous robotics.

**Learning from Keypoints:**
Learning image keypoints via Dense Correspondence pretext tasks can be used for downstream policy learning, and models can be trained to handle scale-invariance and occlusion in multi-object scenes.

**Learning from Imperfect Data:**
A Self-Supervised Data Filtering framework combines expert and imperfect data to compute quality scores for failed trajectory segments, with high-quality segments used to expand the training dataset.

These papers demonstrate that self-supervised learning approaches are becoming increasingly important for robotic manipulation because they reduce dependence on labeled data and enable robots to learn more efficiently from various types of observations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dfa6de2-a767-489b-928f-3bda20de1466",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "73155d40-968e-4263-811e-fb4de8452e7d",
  "sourceToolAssistantUUID": "6dfa6de2-a767-489b-928f-3bda20de1466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T20:02:41.684Z_

<details><summary>↩ Tool result · `toolu_01LHJhYcuphn3YZNHGXMgLuw`</summary>

```text
Web search results for query: ""paraphrase invariance" affordance robot manipulation"

Links: [{"title":"EqvAfford: SE(3) Equivariance for Point-Level Affordance Learning","url":"https://arxiv.org/pdf/2408.01953"},{"title":"Affordance-Centric Policy Learning: Sample Efficient and Generalisable Robot Policy Learning using Affordance-Centric Task Frames","url":"https://arxiv.org/html/2410.12124v1"},{"title":"(PDF) A brief review of affordance in robotic manipulation research","url":"https://www.researchgate.net/publication/320746555_A_brief_review_of_affordance_in_robotic_manipulation_research"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/html/2411.02704v1"},{"title":"[2411.02704] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/abs/2411.02704"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/pdf/2409.01083"}]

Based on the search results, here's what I found about paraphrase invariance and affordance in robot manipulation:

The search results don't contain specific information about "paraphrase invariance" in the context of robot manipulation affordances. However, the results do highlight several important concepts related to affordances and invariance in robot manipulation:

**Invariance in Robot Manipulation:**

One approach focuses on achieving intra-category invariance – where policies can generalize across different instances within the same object category – and spatial invariance, which enables consistent performance regardless of object placement in the environment.

**Affordance-Based Approaches:**

Affordances are central to robotic manipulation, where most tasks can be simplified to interactions with task-specific regions on objects. By focusing on these key regions, we can abstract away task-irrelevant information, simplifying the learning process, and enhancing generalisation.

**SE(3) Equivariance:**

Some research focuses on object manipulation tasks with certain spatial symmetry, where the manipulation strategy is equivariant to the object's 6D pose, which is called SE(3) Equivariance (a group consisting of 3D translation and rotation).

The search results primarily discuss equivariance and spatial invariance rather than "paraphrase invariance" specifically. If you're looking for more targeted information about paraphrase invariance in this context, a more specific search query might help.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "214de039-3dd8-486c-bba3-98be4c31282b",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "3732033a-28c0-4cc7-b662-60c6d57309fa",
  "sourceToolAssistantUUID": "214de039-3dd8-486c-bba3-98be4c31282b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T20:02:42.135Z_

<details><summary>↩ Tool result · `toolu_014AtUsuegH6xtYCVzgzw14s`</summary>

```text
Web search results for query: ""language grounding consistency" manipulation robot"

Links: [{"title":"RoboGround: Robotic Manipulation with Grounded Vision-Language Priors","url":"https://arxiv.org/html/2504.21530v1"},{"title":"Language-Grounded Decoupled Action Representation for Robotic Manipulation","url":"https://arxiv.org/pdf/2603.12967"},{"title":"LACY: A Vision-Language Model-based Language-Action Cycle for Self-Improving Robotic Manipulation","url":"https://arxiv.org/pdf/2511.02239"},{"title":"STEER: Flexible Robotic Manipulation via Dense Language Grounding","url":"https://arxiv.org/pdf/2411.03409"},{"title":"RoboGround: Robotic Manipulation with Grounded Vision-Language Priors","url":"https://arxiv.org/pdf/2504.21530"},{"title":"Knowledge enhanced bottom-up affordance grounding for robotic interaction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11232630/"},{"title":"Visually Grounding Language Instruction for History-Dependent   Manipulation","url":"https://arxiv.org/pdf/2012.08977"},{"title":"Language Movement Primitives: Grounding Language Models in Robot Motion","url":"https://arxiv.org/pdf/2602.02839"}]

Based on the search results, here's what I found about language grounding consistency in robotic manipulation:

## Key Research Areas

Several recent approaches address language grounding and consistency in robotic manipulation:

**RoboGround System**: RoboGround is a grounding-aware robotic manipulation system that leverages grounding masks as an intermediate representation to guide policy networks in object manipulation tasks. The system investigates the effectiveness of grounding mask representations in maintaining consistent performance across diverse scenarios and instructions.

**Language-Grounded Action Representation (LaDA)**: By representing low-level actions through language-grounded primitives, robots can endow control trajectories with explicit semantics, enabling consistent alignment between visual, linguistic, and motor representations. The LaDA framework leverages language as a semantic bridge to unify high-level visual-linguistic understanding with low-level control.

**Language Movement Primitives (LMP)**: Language Movement Primitives ground VLM reasoning in Dynamic Movement Primitive parameterization, with VLMs reasoning over freeform natural language task descriptions and semantically grounding their desired motions into DMPs — bridging the gap between high-level task reasoning and low-level position and velocity control.

**LACY Framework**: LACY substantially improves task success rates and yields more robust language-action grounding for robotic manipulation.

These approaches all focus on maintaining consistency between language understanding and robot motion execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cca99ab-dc9d-4b5f-a7bb-2808f7f240db",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "bc5c5cc7-cb75-4165-861a-141ac31f5afb",
  "sourceToolAssistantUUID": "7cca99ab-dc9d-4b5f-a7bb-2808f7f240db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T20:02:45.645Z_

<details><summary>↩ Tool result · `toolu_0142rmAqrfDASoGhrQyepuip`</summary>

```text
Web search results for query: ""self-supervised affordance" VLA "vision language action""

Links: [{"title":"Vision-Language-Action Models in Robotics","url":"https://www.emergentmind.com/papers/2510.07077"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"[2511.16166] EvoVLA: Self-Evolving Vision-Language-Action Model","url":"https://arxiv.org/abs/2511.16166"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.19752"},{"title":"Vision-Language-Action Pretraining","url":"https://www.emergentmind.com/topics/vision-language-action-model-pretraining"},{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/html/2507.01925v1"}]

I found several relevant results about self-supervised approaches and affordances in Vision-Language-Action (VLA) models. Here's what the search revealed:

## Self-Supervised Learning in VLAs

Self-supervised objectives are used for modality alignment (contrastive learning), visual representation learning (MAE, CLIP, DINOv2), and latent action extraction (LAPA, UniVLA).

## Affordance-Based Approaches

Recent research has developed methods that integrate affordances into VLA models:

- **CoA-VLA**: This approach prompts models to consider four types of affordances before taking action: object affordance, grasp affordance, spatial affordance, and movement affordance, transformed into visual and textual formats.

- **EvoVLA**: This is a self-supervised VLA framework that addresses long-horizon manipulation through Stage-Aligned Reward using triplet contrastive learning, Pose-Based Object Exploration grounding curiosity in object-gripper pose, and Long-Horizon Memory.

- **LITEN**: This method allows VLMs to progressively learn affordances—what the robot can or cannot do—and improve high-level task reasoning as experience is accumulated.

## Data and Training

Unlabeled or action-less videos from human-centric corpora like Something-Something V2 and Ego4D are leveraged for self-supervised or latent action coding in VLA pretraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc842560-17ca-4318-9ef6-f4e27fda799f",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "9e1a0f96-c915-46ab-8baa-f0469a0ccd6a",
  "sourceToolAssistantUUID": "cc842560-17ca-4318-9ef6-f4e27fda799f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T20:02:47.973Z_

<details><summary>↩ Tool result · `toolu_0178yYFH8M5j1KGB3V7P9EHc`</summary>

```text
Web search results for query: ""consistency regularization" affordance robot manipulation"

Links: [{"title":"EqvAfford: SE(3) Equivariance for Point-Level Affordance Learning","url":"https://arxiv.org/pdf/2408.01953"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/pdf/2409.01083"},{"title":"RoboPCA: Pose-centered Affordance Learning from Human Demonstrations for Robot Manipulation","url":"https://arxiv.org/html/2603.07691v1"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.researchgate.net/publication/385560182_RT-Affordance_Affordances_are_Versatile_Intermediate_Representations_for_Robot_Manipulation"},{"title":"Affordance-Centric Policy Learning: Sample Efficient and Generalisable Robot Policy Learning using Affordance-Centric Task Frames","url":"https://arxiv.org/html/2410.12124v1"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/html/2409.01083v4"},{"title":"Paper page - Affordance-based Robot Manipulation with Flow Matching","url":"https://huggingface.co/papers/2409.01083"},{"title":"Robo-ABC: Affordance Generalization Beyond Categories via Semantic   Correspondence for Robot Manipulation","url":"https://arxiv.org/pdf/2401.07487"}]

I found several recent research papers on affordance learning for robot manipulation. Here's what the search returned:

The results cover several approaches to affordance-based robot manipulation:

**Key Research Areas:**

1. **SE(3) Equivariance**: EqvAfford proposes a framework that leverages SE(3) equivariance to predict per-point affordance and downstream manipulation strategy on each point, with theoretical guarantees.

2. **Flow Matching Methods**: Flow matching represents a robot visuomotor policy as a conditional process of flowing random waypoints to desired robot trajectories. The proposed prompt tuning method for learning manipulation affordance with language prompter achieves competitive performance across data scales, while satisfying parameter efficiency.

3. **Pose-Centered Affordance**: RoboPCA is a pose-centered affordance prediction model that jointly predicts the contact points and poses given task instructions.

4. **Affordances as Policy Representations**: Affordances capture the pose of the robot at key stages of the task and offer expressive yet lightweight abstractions that are easy for users to specify.

5. **Affordance-Centric Policy Learning**: Affordances are central to robotic manipulation, and by focusing on task-specific regions, robots can abstract away task-irrelevant information, simplifying the learning process and enhancing generalization.

However, the search results don't contain specific information about "consistency regularization" as a technique in affordance learning. Would you like me to search more specifically for consistency regularization in machine learning or robotics?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53beafe8-2e44-49af-aae3-7cac38482221",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "432691c8-c6d5-431b-a1b5-f8822949af30",
  "sourceToolAssistantUUID": "53beafe8-2e44-49af-aae3-7cac38482221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-18T20:02:53.276Z_

Good, first batch complete. Let me run the remaining 5 searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "432691c8-c6d5-431b-a1b5-f8822949af30",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdbQw5gvqMdzeTzo4Mg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c28ebd84-fe78-4dee-9a9c-cb5e07694845",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K52nx4UZW895imE8THkxcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 709,
      "cache_creation_input_tokens": 3110,
      "cache_read_input_tokens": 9685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3110,
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

_source line 18 · 2026-05-18T20:02:54.211Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01So8kUUtEPxgJzxcCDuzzoA`</summary>

```json
{
  "query": "\"open vocabulary affordance\" end-to-end VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c28ebd84-fe78-4dee-9a9c-cb5e07694845",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdbQw5gvqMdzeTzo4Mg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bc3c75f-4b0b-488a-836b-71105fa6e0cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K52nx4UZW895imE8THkxcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 709,
      "cache_creation_input_tokens": 3110,
      "cache_read_input_tokens": 9685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3110,
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

_source line 19 · 2026-05-18T20:02:54.684Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016U3UHefQt6EvcuGTtct41m`</summary>

```json
{
  "query": "affordance VLA vision-language-action model 2025 2026 recent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bc3c75f-4b0b-488a-836b-71105fa6e0cf",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdbQw5gvqMdzeTzo4Mg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "937aa694-bf63-4871-87de-558fa3453458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K52nx4UZW895imE8THkxcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 709,
      "cache_creation_input_tokens": 3110,
      "cache_read_input_tokens": 9685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3110,
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

_source line 20 · 2026-05-18T20:02:55.143Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BM4cErjAgSh9P268BhWoxs`</summary>

```json
{
  "query": "arxiv affordance VLA robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "937aa694-bf63-4871-87de-558fa3453458",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdbQw5gvqMdzeTzo4Mg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28be1fb6-909e-4392-ab97-294170835104",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K52nx4UZW895imE8THkxcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 709,
      "cache_creation_input_tokens": 3110,
      "cache_read_input_tokens": 9685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3110,
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

_source line 21 · 2026-05-18T20:02:56.094Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X1MzBesC9kDLyijPLr5C2N`</summary>

```json
{
  "query": "\"contrastive affordance learning\" language robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28be1fb6-909e-4392-ab97-294170835104",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdbQw5gvqMdzeTzo4Mg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "922b22d1-ff15-49ba-a6d7-1bbff1ce64b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K52nx4UZW895imE8THkxcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 709,
      "cache_creation_input_tokens": 3110,
      "cache_read_input_tokens": 9685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3110,
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

_source line 22 · 2026-05-18T20:02:56.419Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TpL4FthpyFDpR9s2uuKkSZ`</summary>

```json
{
  "query": "\"instruction augmentation\" robot policy self-supervised 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "922b22d1-ff15-49ba-a6d7-1bbff1ce64b7",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdbQw5gvqMdzeTzo4Mg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe6e8594-b54d-4d95-8171-7d134d762de7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K52nx4UZW895imE8THkxcS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 709,
      "cache_creation_input_tokens": 3110,
      "cache_read_input_tokens": 9685,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3110
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 709,
          "output_tokens": 286,
          "cache_read_input_tokens": 9685,
          "cache_creation_input_tokens": 3110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3110,
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

_source line 23 · 2026-05-18T20:03:01.092Z_

<details><summary>↩ Tool result · `toolu_016U3UHefQt6EvcuGTtct41m`</summary>

```text
Web search results for query: "affordance VLA vision-language-action model 2025 2026 recent"

Links: [{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"VTLA: Vision-Tactile-Language-Action model with preference learning for insertion manipulation | Request PDF","url":"https://www.researchgate.net/publication/403926332_VTLA_Vision-Tactile-Language-Action_model_with_preference_learning_for_insertion_manipulation"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://chain-of-affordance.github.io/"}]

Based on the search results, here's what I found about affordance in Vision-Language-Action (VLA) models in 2025-2026:

## Recent VLA Research with Affordance

Vision-Language-Action (VLA) models have garnered significant attention for their ability to enhance robot policy learning, greatly improving robot's generalization and robustness.

### Chain-of-Affordance (CoA-VLA)

A notable recent development is CoA-VLA, which was presented at ICCV 2025. Chain-of-Affordance (CoA-VLA) is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion.

The model considers four types of affordances before taking action: (1) object affordance - what object to manipulate and where it is; (2) grasp affordance - the specific object part to grasp; (3) spatial affordance - the optimal space to place the object; and (4) movement affordance - the collision-free path for movement.

CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks.

### Other Affordance-Related Work

Recent 2025 work includes UAD (Unsupervised Affordance Distillation) for Generalization in Robotic Manipulation and 3D-AffordanceLLM for Open-Vocabulary Affordance Detection in 3D Worlds.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "937aa694-bf63-4871-87de-558fa3453458",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "ecbb19ab-8a76-4aaf-98c4-59ab93e8d0f7",
  "sourceToolAssistantUUID": "937aa694-bf63-4871-87de-558fa3453458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T20:03:02.086Z_

<details><summary>↩ Tool result · `toolu_01So8kUUtEPxgJzxcCDuzzoA`</summary>

```text
Web search results for query: ""open vocabulary affordance" end-to-end VLA 2025 2026"

Links: [{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"},{"title":"Open-Vocabulary Affordance Detection in 3D Point Clouds","url":"https://arxiv.org/pdf/2303.02401"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot   Manipulation through LLM Affordance-Grounding","url":"https://arxiv.org/pdf/2404.11000"},{"title":"Open-Vocabulary 3D Affordance Understanding via ...","url":"https://eprints.gla.ac.uk/360521/2/360521.pdf"},{"title":"Affordance-Guided Coarse-to-Fine Exploration for Base Placement in Open-Vocabulary Mobile Manipulation","url":"https://arxiv.org/pdf/2511.06240"}]

Based on the search results, here are some key findings related to open vocabulary affordance and end-to-end VLA models from 2025-2026:

## Recent Research

Recent work in 2025 includes 3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds, which represents an emerging direction in combining language models with affordance understanding.

Open-Vocabulary 3D Affordance Understanding via Functional Text Enhancement and Multilevel Representation Alignment was presented at the 33rd ACM International Conference on Multimedia in October 2025.

## Vision-Language-Action (VLA) Models

Recent advancements in Vision-Language-Action (VLA) models have shown that training with internet-scale data can empower end-to-end policy learning models to outperform non-VLA models. 

Several efficiency-focused VLA variants have been developed in 2025, including BitVLA (1-bit Vision-Language-Action Models for Robotics), QuaRT-VLA (Quantized Robotics Transformers for Vision-Language-Action Models), and PDVLA (Parallel Decoding for Vision-Language-Action Models).

## Open-Vocabulary Affordance Applications

The OVAL-Prompt algorithm has been introduced to perform open-vocabulary affordance localization, using a LLM to ground part-segments generated by a VLM with corresponding action-affordances.

Research on open-vocabulary mobile manipulation involves robots reasoning jointly about geometric feasibility and semantic intent, identifying collision-free locations that align with task-relevant affordances, such as positioning itself in front of a cabinet with enough clearance for effective interaction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bc3c75f-4b0b-488a-836b-71105fa6e0cf",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "ad6f1f50-2add-43e3-afc2-ea42563d0a68",
  "sourceToolAssistantUUID": "7bc3c75f-4b0b-488a-836b-71105fa6e0cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T20:03:03.840Z_

<details><summary>↩ Tool result · `toolu_01X1MzBesC9kDLyijPLr5C2N`</summary>

```text
Web search results for query: ""contrastive affordance learning" language robot 2025 2026"

Links: [{"title":"Language-Driven Representation Learning for Robotics","url":"https://arxiv.org/pdf/2302.12766"},{"title":"RoboAfford: A Dataset and Benchmark for Enhancing Object and Spatial Affordance Learning in Robot Manipulation | Request PDF","url":"https://www.researchgate.net/publication/396941670_RoboAfford_A_Dataset_and_Benchmark_for_Enhancing_Object_and_Spatial_Affordance_Learning_in_Robot_Manipulation"},{"title":"Contrastive Language, Action, and State Pre-training for Robot Learning","url":"https://arxiv.org/pdf/2304.10782"},{"title":"GitHub - hk-zh/language-conditioned-robot-manipulation-models: https://arxiv.org/abs/2312.10807 · GitHub","url":"https://github.com/hk-zh/language-conditioned-robot-manipulation-models"},{"title":"Affordance Perception by a Knowledge-Guided Vision-Language Model with   Efficient Error Correction","url":"https://arxiv.org/pdf/2407.13368"},{"title":"Gu Zhang | Homepage","url":"https://www.gu-zhang.com/"}]

Based on the search results, I found several relevant works on contrastive learning in robot manipulation and language-conditioned robotics from 2024-2026:

## Key Findings

**Recent Frameworks and Methods:**

PRTS (Primitive Reasoning and Tasking System) is a Vision-Language-Action (VLA) foundation model that reformulates pretraining through Goal-Conditioned Reinforcement Learning, employing contrastive reinforcement learning to learn a unified embedding space where language instructions serve as goals.

CLASP (Contrastive Language, Action, and State Pretraining) is a method for unifying language, action, and state information in a shared embedding space, extending the CLIP formulation by incorporating distributional learning to capture one-to-many relationships in behaviour-text alignment.

**Current Research Direction:**

Vision-Language-Action (VLA) models advance robotic control via strong visual-linguistic priors, but existing VLAs predominantly frame pretraining as supervised behavior cloning, overlooking robot learning as a goal-reaching process.

A comprehensive survey on language-conditioned robot manipulation was extended in November 2025 with new structures and more recent works from 2024-2025.

These recent works show an active focus on combining contrastive learning techniques with language models for robotic affordance understanding and manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "922b22d1-ff15-49ba-a6d7-1bbff1ce64b7",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "117ac3e3-d48c-495d-aeb6-9ceae33f7e43",
  "sourceToolAssistantUUID": "922b22d1-ff15-49ba-a6d7-1bbff1ce64b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T20:03:04.323Z_

<details><summary>↩ Tool result · `toolu_01BM4cErjAgSh9P268BhWoxs`</summary>

```text
Web search results for query: "arxiv affordance VLA robot 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.10109"},{"title":"VLA-Thinker: Boosting Vision-Language-Action Models through","url":"https://arxiv.org/pdf/2603.14523"},{"title":"RoboAlign: Learning Test-Time Reasoning for Language- ...","url":"https://arxiv.org/pdf/2603.21341"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919v1"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/pdf/2409.01083"}]

Based on the search results, I found several recent papers from arXiv related to affordance, Vision-Language-Action (VLA) models, and robotics from 2025-2026:

**Recent VLA and Affordance Papers:**

1. **VLA-Thinker** - A paper on robotic affordances from a recent conference on robot learning, published in March 2026.

2. **RoboAlign** - A preprint from March 24, 2026 on learning test-time reasoning for language-action alignment in Vision-Language-Action models.

3. **Affordance Field Intervention** - A work on Vision-Language-Action models for robotic manipulation that maps visual observations and linguistic instructions to executable action sequences.

4. **CoA-VLA (Chain-of-Affordance)** - A novel approach on generalizing model reasoning at test-time, leveraging visual affordance in robot learning to conceptualize various actions and interactions with objects.

5. **Green-VLA** - A robot-specific VLA model using visual question answering and robotics data that captures affordance priors for robot adaptation and specialization.

These papers represent the current frontier of research in combining affordance understanding with Vision-Language-Action models for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28be1fb6-909e-4392-ab97-294170835104",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "0db2e32a-b516-48aa-86f2-8e7a599cc753",
  "sourceToolAssistantUUID": "28be1fb6-909e-4392-ab97-294170835104",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T20:03:04.930Z_

<details><summary>↩ Tool result · `toolu_01TpL4FthpyFDpR9s2uuKkSZ`</summary>

```text
Web search results for query: ""instruction augmentation" robot policy self-supervised 2025 2026"

Links: [{"title":"Data Augmentation for Instruction Following Policies via Trajectory   Segmentation","url":"https://arxiv.org/pdf/2503.01871"},{"title":"Robotic Skill Acquisition via Instruction Augmentation with   Vision-Language Models","url":"https://arxiv.org/pdf/2211.11736"},{"title":"Object-Centric Instruction Augmentation for Robotic Manipulation","url":"https://arxiv.org/pdf/2401.02814"},{"title":"[2509.09893] Self-Augmented Robot Trajectory: Efficient Imitation Learning via Safe Self-augmentation with Demonstrator-annotated Precision","url":"https://arxiv.org/abs/2509.09893"},{"title":"GUIDES: Guidance Using Instructor-Distilled Embeddings for Pre-trained Robot Policy Enhancement","url":"https://arxiv.org/pdf/2511.03400"},{"title":"Robot policy learning from demonstrations and visual rewards for sequential manipulation tasks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0921889025004087"},{"title":"Autonomous Improvement of Instruction Following Skills via Foundation   Models","url":"https://arxiv.org/pdf/2407.20635"}]

The search returned several relevant papers on instruction augmentation for robot policies from 2025-2026:

1. **Data Augmentation via Trajectory Segmentation (2025)**: A method called Play Segmentation finds maximum likely segmentations of extended subsegments while trained on individual instruction segments, improving policy performance to the level of a policy trained on twice the amount of labelled data.

2. **DIAL - Instruction Augmentation with Vision-Language Models**: Data-driven Instruction Augmentation for Language-conditioned control utilizes semi-supervised language labels leveraging CLIP's semantic understanding to propagate knowledge onto large datasets of unlabelled demonstration data, enabling cheaper acquisition of useful language descriptions compared to expensive human labels.

3. **Object-Centric Instruction Augmentation (2024)**: A method that uses a Multi-modal Large Language Model to weave knowledge of object locations into natural language instructions, with augmented instructions enabling imitation policies to outperform those relying solely on traditional language instructions.

4. **Self-Augmented Robot Trajectory (February 2026)**: SART is a framework that enables policy learning from a single human demonstration while safely expanding the dataset through autonomous augmentation.

5. **GUIDES (2025)**: An approach where a large language model-based Reflector monitors confidence and augments context to refine actions, offering a practical pathway to upgrade validated robot policies.

6. **Autonomous Improvement via Foundation Models (SOAR)**: SOAR is a system for autonomous improvement of multi-task language-conditioned policies, demonstrating effectiveness in utilizing autonomously collected data to improve policy performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe6e8594-b54d-4d95-8171-7d134d762de7",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "e41b88c3-c4d6-4a4c-b6ca-7e9f3e5d0953",
  "sourceToolAssistantUUID": "fe6e8594-b54d-4d95-8171-7d134d762de7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-18T20:03:08.286Z_

Good. Now let me do deeper dives on the most threatening papers I've identified so far. Let me search for more details on the key papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e41b88c3-c4d6-4a4c-b6ca-7e9f3e5d0953",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdcfRk1qw7Gpf9bQBdz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd6b16e5-4e42-428c-80a2-8af7dc4892dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MtBR8Lnb5nLA3q95RWc8u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 12795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4699,
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

_source line 29 · 2026-05-18T20:03:08.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QdMZwuc5LKFim5s4TraXeY`</summary>

```json
{
  "query": "CoA-VLA chain-of-affordance visual textual affordance VLA self-supervised paraphrase"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd6b16e5-4e42-428c-80a2-8af7dc4892dd",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdcfRk1qw7Gpf9bQBdz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bac28139-8b1f-4bd4-8a0b-626abbbf7428",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MtBR8Lnb5nLA3q95RWc8u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 12795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4699,
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

_source line 30 · 2026-05-18T20:03:09.717Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GwCb2AoFGhiF7vpUt5XpeQ`</summary>

```json
{
  "query": "RT-Affordance language conditioned affordance robot manipulation intermediate representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bac28139-8b1f-4bd4-8a0b-626abbbf7428",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdcfRk1qw7Gpf9bQBdz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "957d1aca-e72c-467a-bc8b-abc5ba8ac176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MtBR8Lnb5nLA3q95RWc8u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 12795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4699,
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

_source line 31 · 2026-05-18T20:03:10.179Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012xj1Dmg11Q2vgv1UNT4xQu`</summary>

```json
{
  "query": "DIAL instruction augmentation CLIP language labels robot manipulation semi-supervised"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "957d1aca-e72c-467a-bc8b-abc5ba8ac176",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdcfRk1qw7Gpf9bQBdz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "930e66ce-c2eb-4522-9364-6b695d9d3d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MtBR8Lnb5nLA3q95RWc8u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 12795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4699,
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

_source line 32 · 2026-05-18T20:03:10.653Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01815zJD6xjMFMLWDqHNbn2s`</summary>

```json
{
  "query": "\"affordance field intervention\" VLA escape memory traps 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "930e66ce-c2eb-4522-9364-6b695d9d3d64",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdcfRk1qw7Gpf9bQBdz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7900839f-d33d-4c6a-bcb7-5dd5a78590ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MtBR8Lnb5nLA3q95RWc8u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 12795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4699,
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

_source line 33 · 2026-05-18T20:03:11.225Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RjGErFbpki6pCNqSptGzkV`</summary>

```json
{
  "query": "STEER dense language grounding robotic manipulation affordance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7900839f-d33d-4c6a-bcb7-5dd5a78590ce",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdcfRk1qw7Gpf9bQBdz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29de2bfe-cf7e-4617-be07-f44d9a3d2c98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MtBR8Lnb5nLA3q95RWc8u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 12795,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4699
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 12795,
          "cache_creation_input_tokens": 4699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4699,
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

_source line 34 · 2026-05-18T20:03:15.390Z_

<details><summary>↩ Tool result · `toolu_01QdMZwuc5LKFim5s4TraXeY`</summary>

```text
Web search results for query: "CoA-VLA chain-of-affordance visual textual affordance VLA self-supervised paraphrase"

Links: [{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"[PDF] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoA-VLA:-Improving-Vision-Language-Action-Models-Li-Zhu/5760cc722b5eabc14487e9c497a78038ab46f37d"},{"title":"Add CoA-VLA (Chain-of-Affordance) · Issue #5 · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/issues/5"}]

Based on the search results, I found comprehensive information about CoA-VLA:

## CoA-VLA: Chain-of-Affordance Vision-Language-Action Model

CoA-VLA is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion.

### Four Types of Affordances

The model prompts the VLA to consider four types of affordances before taking action: (1) object affordance — what object to manipulate and where it is; (2) grasp affordance — the specific object part to grasp; (3) spatial affordance — the optimal space to place the object; and (4) movement affordance — the collision-free path for movement.

### Visual-Textual Integration

Each affordance is transformed into two prompting formats: visual affordance and textual affordance. A novel vision-language co-injection module integrates this knowledge into the policy network, allowing the robot to leverage essential contextual information during action inference, resulting in improved precision and robustness.

### Performance

CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks. Furthermore, CoA-VLA exhibits strong generalization capabilities, including recognizing unseen object poses, identifying free space, and avoiding obstacles in novel environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bac28139-8b1f-4bd4-8a0b-626abbbf7428",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "044247c8-30e2-41bc-9e02-0478689e1581",
  "sourceToolAssistantUUID": "bac28139-8b1f-4bd4-8a0b-626abbbf7428",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T20:03:16.221Z_

<details><summary>↩ Tool result · `toolu_012xj1Dmg11Q2vgv1UNT4xQu`</summary>

```text
Web search results for query: "DIAL instruction augmentation CLIP language labels robot manipulation semi-supervised"

Links: [{"title":"Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2211.11736"},{"title":"[2211.11736] Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models","url":"https://arxiv.org/abs/2211.11736"},{"title":"Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models","url":"https://arxiv.org/html/2211.11736"},{"title":"Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models | DeepAI","url":"https://deepai.org/publication/robotic-skill-acquisition-via-instruction-augmentation-with-vision-language-models"},{"title":"Robotic Skill Acquisition via Instruction Augmentation with   Vision-Language Models","url":"https://arxiv.org/pdf/2211.11736"},{"title":"Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv221111736X/abstract"},{"title":"DIAL","url":"https://instructionaugmentation.github.io/"},{"title":"Robotic Skill Acquisition via Instruction Augmentation with ...","url":"https://openreview.net/pdf?id=uztKyepCdd"},{"title":"Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models - Paper Detail","url":"https://deeplearn.org/arxiv/392698/robotic-skill-acquisition-via-instruction-augmentation-with-vision-language-models"},{"title":"Robotic Skill Acquisition Via Instruction Augmentation With Vision-Language Models | PDF","url":"https://www.scribd.com/document/693544365/Robotic-Skill-Acquisition-via-Instruction-Augmentation-with-Vision-Language-Models"}]

Based on the search results, here's what I found about DIAL:

## DIAL: Data-driven Instruction Augmentation for Language-conditioned Control

DIAL is a method that utilizes semi-supervised language labels to propagate CLIP's semantic knowledge onto large datasets of unlabeled demonstration data, from which language-conditioned policies are then trained.

**Key Motivation:**
Large-scale pretrained vision-language models (VLMs) like CLIP have been applied to robotics, and the question is whether these pretrained models can serve as automatic labelers for robot data, effectively importing Internet-scale knowledge into existing datasets.

**Method Overview:**
DIAL consists of three steps: (1) Contrastive fine-tuning of a vision-language model such as CLIP on a small dataset of robot manipulation trajectories with crowd-sourced natural language annotation, (2) labeling a larger dataset of trajectories using the fine-tuned VLM, and (3) training a language-conditioned policy using behavior cloning on the original and relabeled dataset.

**Practical Application:**
DIAL was applied to a challenging real-world robotic manipulation domain where only 3.5% of the 80,000 demonstrations contain crowd-sourced language annotations. The method outperforms instruction augmentation methods that are not visually grounded and improves novel instruction performance when applied to either partially or fully labeled datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "930e66ce-c2eb-4522-9364-6b695d9d3d64",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "0542f159-a8e8-4e8c-b4af-65bfe1662c2a",
  "sourceToolAssistantUUID": "930e66ce-c2eb-4522-9364-6b695d9d3d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T20:03:16.233Z_

<details><summary>↩ Tool result · `toolu_01GwCb2AoFGhiF7vpUt5XpeQ`</summary>

```text
Web search results for query: "RT-Affordance language conditioned affordance robot manipulation intermediate representation"

Links: [{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/html/2411.02704v1"},{"title":"[2411.02704] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/abs/2411.02704"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/11127273/11127223/11127525.pdf"},{"title":"RT-Affordance: A New Approach by Google DeepMind to Robust Robot Manipulation with Versatile Policy Representations – AI Toolhouse Blog","url":"https://blog.aitoolhouse.com/rt-affordance-a-new-approach-by-google-deepmind-to-robust-robot-manipulation-with-versatile-policy-representations/"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot","url":"https://openreview.net/pdf?id=y4KugwU0qU"},{"title":"[Literature Review] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.themoonlight.io/en/review/rt-affordance-affordances-are-versatile-intermediate-representations-for-robot-manipulation"}]

Based on the search results, here's what I found about RT-Affordance:

## Overview

RT-Affordance is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation.

## Key Innovation

The approach conditions policies on intermediate affordance representations, which are expressive yet compact representations of tasks, making them easy to specify and to learn. The model first predicts the affordances given a task specification in language, and then leverages the affordances as an intermediate representation to steer the policy.

## What Affordances Capture

RT-Affordance conditions policies on affordances, which capture the pose of the robot at key stages of the task. More specifically, the affordance plan is defined as the sequence of robot end effector poses corresponding to key timesteps in the task when the robot contacts, grasps, pushes, or lets go of objects.

## Advantages

Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets. RT-Affordance exceeds the performance of existing methods by over 50% on a diverse set of novel tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "957d1aca-e72c-467a-bc8b-abc5ba8ac176",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "b993df56-832d-4d6b-b29c-16590f6cf9c6",
  "sourceToolAssistantUUID": "957d1aca-e72c-467a-bc8b-abc5ba8ac176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T20:03:16.648Z_

<details><summary>↩ Tool result · `toolu_01815zJD6xjMFMLWDqHNbn2s`</summary>

```text
Web search results for query: ""affordance field intervention" VLA escape memory traps 2025"

Links: [{"title":"[2512.07472] Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://www.arxiv.org/abs/2512.07472"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in","url":"https://www.arxiv.org/pdf/2512.07472"},{"title":"Robotics Dec 2025","url":"https://arxiv.org/list/cs.RO/2025-12?skip=225&show=25"},{"title":"Siyu Xu - Homepage","url":"https://siyuxu.com/"},{"title":"Paper page - VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://huggingface.co/papers/2512.11891"},{"title":"Paper page - VLS: Steering Pretrained Robot Policies via Vision-Language Models","url":"https://huggingface.co/papers/2602.03973"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/html/2512.07472v1"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"}]

Based on the search results, here's what I found about Affordance Field Intervention and VLA memory traps:

## Overview

Affordance Field Intervention (AFI) is a lightweight hybrid framework that uses Spatial Affordance Fields (SAFs) as an on-demand plug-in to guide VLA behavior.

## The Memory Trap Problem

Vision-Language-Action (VLA) models often fail under distribution shifts: when test scenarios change, VLAs often reproduce memorized trajectories instead of adapting to the updated scene, which is called the "Memory Trap". This limitation stems from the end-to-end design, which lacks explicit 3D spatial reasoning and prevents reliable identification of actionable regions in unfamiliar environments.

## The Solution: AFI Framework

The system detects memory traps through proprioception, repositions the robot to recent high-affordance regions, and proposes affordance-driven waypoints that anchor VLA-generated actions. A SAF-based scorer then selects trajectories with the highest cumulative affordance.

## Performance Results

The method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark.

## Publication

The paper "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation" was accepted to CVPR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7900839f-d33d-4c6a-bcb7-5dd5a78590ce",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "b99e8d34-5afb-4815-a742-e80fd72d5591",
  "sourceToolAssistantUUID": "7900839f-d33d-4c6a-bcb7-5dd5a78590ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T20:03:18.096Z_

<details><summary>↩ Tool result · `toolu_01RjGErFbpki6pCNqSptGzkV`</summary>

```text
Web search results for query: "STEER dense language grounding robotic manipulation affordance"

Links: [{"title":"STEER: Flexible Robotic Manipulation via Dense Language Grounding","url":"https://arxiv.org/pdf/2411.03409"},{"title":"STEER: Flexible Robotic Manipulation via Dense Language Grounding","url":"https://www.researchgate.net/publication/385595683_STEER_Flexible_Robotic_Manipulation_via_Dense_Language_Grounding"},{"title":"[2411.03409] STEER: Flexible Robotic Manipulation via Dense Language Grounding","url":"https://arxiv.org/abs/2411.03409"},{"title":"STEER: Flexible Robotic Manipulation via Dense Language Grounding","url":"https://arxiv.org/html/2411.03409v1"},{"title":"Empowering Large Language Models on Robotic Manipulation with Affordance   Prompting","url":"https://arxiv.org/pdf/2404.11027"},{"title":"Knowledge enhanced bottom-up affordance grounding for robotic interaction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232630/"},{"title":"Grounding Object Relations in Language-Conditioned Robotic Manipulation   with Semantic-Spatial Reasoning","url":"https://arxiv.org/pdf/2303.17919"},{"title":"Knowledge enhanced bottom-up affordance grounding for robotic interaction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11232630/"}]

Based on the search results, here's information about STEER:

## Overview

STEER is a robot learning framework that bridges high-level, commonsense reasoning with precise, flexible low-level control. The approach translates complex situational awareness into actionable low-level behavior through training language-grounded policies with dense annotation.

## Key Features

By structuring policy training around fundamental, modular manipulation skills expressed in natural language, STEER exposes an expressive interface for humans or Vision-Language Models (VLMs) to intelligently orchestrate the robot's behavior by reasoning about the task and context.

## Capabilities and Results

The skills learned via STEER can be combined to synthesize novel behaviors to adapt to new situations or perform completely new tasks without additional data collection or training. For example, densely labeled models adjust behavior when prompted to grasp objects from different angles, enabling new downstream tasks.

STEER can be steered to perform specific manipulation tasks, which in conjunction with the commonsense-reasoning afforded by a VLM agent can perform intelligent multi-step manipulation without ever collecting new data.

The framework was published in November 2024 and represents a novel approach to making robotic manipulation systems more adaptable and generalizable to new situations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29de2bfe-cf7e-4617-be07-f44d9a3d2c98",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "8e387950-aee2-4f93-8d14-293b115f453c",
  "sourceToolAssistantUUID": "29de2bfe-cf7e-4617-be07-f44d9a3d2c98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-18T20:03:21.238Z_

Let me now search for the most directly threatening work -- anything involving language paraphrase or synonym invariance for visual grounding or affordance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e387950-aee2-4f93-8d14-293b115f453c",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdddgbMQDwgdG9MZAMV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48e93cdd-b8a2-443a-bf82-e48acf5ba8df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRjtrpTQ7uvMUybVFkSM3Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4055,
      "cache_read_input_tokens": 17494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4055,
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

_source line 40 · 2026-05-18T20:03:21.714Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eaef1DBtugHQeMKUSvjy4G`</summary>

```json
{
  "query": "paraphrase synonym invariance visual grounding robot affordance self-supervised"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48e93cdd-b8a2-443a-bf82-e48acf5ba8df",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdddgbMQDwgdG9MZAMV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "daed55f6-9767-45f2-bb74-773cd75d503b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRjtrpTQ7uvMUybVFkSM3Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4055,
      "cache_read_input_tokens": 17494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4055,
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

_source line 41 · 2026-05-18T20:03:22.722Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HRokThJ8j2UBBiDcCYip1o`</summary>

```json
{
  "query": "language augmentation consistency loss visual features robot manipulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "daed55f6-9767-45f2-bb74-773cd75d503b",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdddgbMQDwgdG9MZAMV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28ad3170-1f36-47be-bb28-9764bcb6702a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRjtrpTQ7uvMUybVFkSM3Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4055,
      "cache_read_input_tokens": 17494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4055,
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

_source line 42 · 2026-05-18T20:03:23.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VXjMhmTnJ8813xNv7mKFjE`</summary>

```json
{
  "query": "OVAL-Prompt open vocabulary affordance localization robot LLM 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28ad3170-1f36-47be-bb28-9764bcb6702a",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdddgbMQDwgdG9MZAMV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "906a64b9-8023-4225-ba1d-b4fe9b9ed7d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRjtrpTQ7uvMUybVFkSM3Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4055,
      "cache_read_input_tokens": 17494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4055,
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

_source line 43 · 2026-05-18T20:03:24.177Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TSM6MLwiMxrhbjYqVzAXTM`</summary>

```json
{
  "query": "RoboGround grounding mask affordance VLA language consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "906a64b9-8023-4225-ba1d-b4fe9b9ed7d5",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdddgbMQDwgdG9MZAMV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d46be2e0-5e62-41af-892a-d531d56eb13c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRjtrpTQ7uvMUybVFkSM3Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4055,
      "cache_read_input_tokens": 17494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4055,
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

_source line 44 · 2026-05-18T20:03:24.447Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019J9crbkXMXxBnL1fHeQ9qu`</summary>

```json
{
  "query": "UAD unsupervised affordance distillation robot manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d46be2e0-5e62-41af-892a-d531d56eb13c",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdddgbMQDwgdG9MZAMV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12f96cc7-6689-4491-ba1b-d68ec72d4bb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRjtrpTQ7uvMUybVFkSM3Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4055,
      "cache_read_input_tokens": 17494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4055,
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

_source line 45 · 2026-05-18T20:03:29.630Z_

<details><summary>↩ Tool result · `toolu_019J9crbkXMXxBnL1fHeQ9qu`</summary>

```text
Web search results for query: "UAD unsupervised affordance distillation robot manipulation 2025"

Links: [{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11128868/;jsessionid=52BA349B68AC6A3C152B08FECD858BDD"},{"title":"[2506.09284] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/abs/2506.09284"},{"title":"[PDF] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/UAD:-Unsupervised-Affordance-Distillation-for-in-Tang-Huang/a7992218b0f8c8663e8ac144fcf58017a2a3c335"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | Request PDF","url":"https://www.researchgate.net/publication/395210639_UAD_Unsupervised_Affordance_Distillation_for_Generalization_in_Robotic_Manipulation"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/html/2506.09284v1"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | alphaXiv","url":"https://www.alphaxiv.org/resources/2506.09284v1"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://www.researchgate.net/publication/392597063_UAD_Unsupervised_Affordance_Distillation_for_Generalization_in_Robotic_Manipulation"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/pdf/2506.09284"}]

I found relevant search results for UAD (Unsupervised Affordance Distillation). Here's what the research shows:

## Overview

UAD is a method for distilling affordance knowledge from foundation models into a task-conditioned affordance model without any manual annotations. Understanding fine-grained object affordances is imperative for robots to manipulate objects in unstructured environments given open-ended task instructions.

## Key Approach

By leveraging the complementary strengths of large vision models and vision-language models, UAD automatically annotates a large-scale dataset with detailed instruction-affordance pairs. Training only a lightweight task-conditioned decoder atop frozen features, UAD exhibits notable generalization to in-the-wild robotic scenes and to various human activities, despite only being trained on rendered objects in simulation.

## Results and Generalization

The method demonstrates promising generalization to unseen object instances, object categories, and even variations in task instructions after training on as few as 10 demonstrations. The paper was published at the 2025 IEEE International Conference on Robotics and Automation (ICRA) in May 2025.

The research was authored by Yihe Tang, Wenlong Huang, and colleagues from Stanford University, with additional contributors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12f96cc7-6689-4491-ba1b-d68ec72d4bb9",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "3a74e7c2-f424-4379-b0f4-85b7557cc4de",
  "sourceToolAssistantUUID": "12f96cc7-6689-4491-ba1b-d68ec72d4bb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-18T20:03:29.891Z_

<details><summary>↩ Tool result · `toolu_01HRokThJ8j2UBBiDcCYip1o`</summary>

```text
Web search results for query: "language augmentation consistency loss visual features robot manipulation 2024 2025"

Links: [{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2602.20200"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"ACTLLM: Action Consistency Tuned Large Language Model","url":"https://arxiv.org/pdf/2506.21250"},{"title":"Object-Centric Instruction Augmentation for Robotic Manipulation","url":"https://arxiv.org/pdf/2401.02814"},{"title":"Contrastive Representation Regularization for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.01711"}]

Based on the search results, here are the key findings related to language augmentation, consistency loss, visual features, and robot manipulation from 2024-2025:

## Vision-Language-Action Models and Consistency

Recent VLA models preserve semantic consistency learned during pretraining, reducing overfitting and enhancing generalization, with EF-VLA demonstrating 20% performance improvement on compositional manipulation tasks.

## Consistency-Focused Approaches

OptimusVLA uses a dual-memory approach (Global Prior Meets Local Consistency) achieving 98.6% average success on LIBERO and outperforming prior models by 13.5% on CALVIN and 2.9× inference speedup in real-world evaluations.

A Contrastive Representation Regularization (RS-CL) approach enhanced control-relevant representation learning, improving pick-and-place tasks from 30.8% to 41.5% in RoboCasa-Kitchen and boosting real-robot manipulation success rates from 45.0% to 58.3%.

## Language Augmentation and Visual Features

Recent work uses Multi-modal Large Language Models to augment language instructions with object location knowledge and features reuse mechanisms to integrate vision-language features from pre-trained models into policy networks.

ACTLLM reformulated robotic manipulation as a multi-turn visual dialogue framework to model long-term task execution with enhanced contextual relevance, proving effective on challenging vision-based robot manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28ad3170-1f36-47be-bb28-9764bcb6702a",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "a2cdf98e-cb9d-473d-96ba-edee1ca2e3ce",
  "sourceToolAssistantUUID": "28ad3170-1f36-47be-bb28-9764bcb6702a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-18T20:03:29.923Z_

<details><summary>↩ Tool result · `toolu_01VXjMhmTnJ8813xNv7mKFjE`</summary>

```text
Web search results for query: "OVAL-Prompt open vocabulary affordance localization robot LLM 2024"

Links: [{"title":"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding","url":"https://ekjt.github.io/OVAL-Prompt/"},{"title":"[PDF] OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OVAL-Prompt:-Open-Vocabulary-Affordance-for-Robot-Tong-Opipari/b24f28e425957aadbf45d71fd6fdcc8325e5bdf2"},{"title":"[2404.11000] OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding","url":"https://arxiv.org/abs/2404.11000"},{"title":"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot   Manipulation through LLM Affordance-Grounding","url":"https://arxiv.org/pdf/2404.11000"},{"title":"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding | OpenReview","url":"https://openreview.net/forum?id=DlZxbx0tHC"},{"title":"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding","url":"https://arxiv.org/html/2404.11000v1"},{"title":"[Literature Review] OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding","url":"https://www.themoonlight.io/en/review/oval-prompt-open-vocabulary-affordance-localization-for-robot-manipulation-through-llm-affordance-grounding"},{"title":"GitHub - DirtyHarryLYL/LLM-in-Vision: Recent LLM-based CV and related works. Welcome to comment/contribute! · GitHub","url":"https://github.com/DirtyHarryLYL/LLM-in-Vision"}]

Based on the search results, here's what I found about OVAL-Prompt:

## Overview

OVAL-Prompt is a prompt-based approach for open-vocabulary affordance localization in RGB-D images. The research was presented at ICRA 2024 VLMNM Workshop and is authored by researchers from the University of Michigan and J.P. Morgan AI Research.

## Technical Approach

The method leverages a Vision Language Model (VLM) for open-vocabulary object part segmentation and a Large Language Model (LLM) to ground each part-segment-affordance, demonstrating generalizability to novel object instances, categories, and affordances without domain-specific finetuning.

## Key Results

Without any finetuning, OVAL-Prompt achieves localization accuracy that is competitive with supervised baseline models. Moreover, qualitative experiments show that OVAL-Prompt enables affordance-based robot manipulation of open-vocabulary object instances and categories.

## Core Concept

The robot can figure out what actions can be performed on an object (its affordances) and where to perform those actions, even if the robot hasn't been specifically trained on those objects or actions before.

The paper is available on arXiv (2404.11000) and has an associated project page at ekjt.github.io/OVAL-Prompt/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "906a64b9-8023-4225-ba1d-b4fe9b9ed7d5",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "2b60e9b8-3f95-40dd-b8b5-ad4dcf07aa06",
  "sourceToolAssistantUUID": "906a64b9-8023-4225-ba1d-b4fe9b9ed7d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T20:03:30.154Z_

<details><summary>↩ Tool result · `toolu_01TSM6MLwiMxrhbjYqVzAXTM`</summary>

```text
Web search results for query: "RoboGround grounding mask affordance VLA language consistency"

Links: [{"title":"RoboGround: Robotic Manipulation with Grounded Vision-Language Priors | Request PDF","url":"https://www.researchgate.net/publication/394625768_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors"},{"title":"(PDF) RoboGround: Robotic Manipulation with Grounded Vision-Language Priors","url":"https://www.researchgate.net/publication/391328688_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors"},{"title":"[Literature Review] RoboGround: Robotic Manipulation with Grounded Vision-Language Priors","url":"https://www.themoonlight.io/en/review/roboground-robotic-manipulation-with-grounded-vision-language-priors"},{"title":"RoboGround: Robotic Manipulation with Grounded Vision-Language Priors","url":"https://arxiv.org/html/2504.21530v1"},{"title":"RoboGround: Robotic Manipulation with Grounded Vision-Language Priors","url":"https://arxiv.org/pdf/2504.21530"},{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://arxiv.org/html/2401.06341v1"},{"title":"[2504.21530] RoboGround: Robotic Manipulation with Grounded Vision-Language Priors","url":"https://arxiv.org/abs/2504.21530"}]

Based on the search results, here's what I found about RoboGround:

## Overview

RoboGround is a grounding-aware robotic manipulation system that leverages grounding masks as an intermediate representation to guide policy networks in object manipulation tasks.

## Key Components

**Grounding Masks:** Grounding masks provide effective spatial guidance that specifies target objects and placement areas while conveying information about object shape and size, and broad generalization potential driven by large-scale vision-language models pretrained on diverse grounding datasets.

**Vision-Language Integration:** The system employs a grounded vision-language model to generate masks for both the target object and placement area, which are then seamlessly integrated into the policy network through channel-level and patch-level designs.

## Data and Training

An automated pipeline is proposed for generating large-scale, simulated data with a diverse set of objects and instructions. The data generation focuses on appearance-based instructions, spatial instructions, and common-sense instructions.

## Results

Extensive experiments show the value of the dataset and the effectiveness of grounding masks as intermediate guidance, significantly enhancing the generalization abilities of robot policies.

The approach addresses the challenge of maintaining consistent performance across diverse scenes and instructions while improving robot manipulation capabilities through grounded vision-language priors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d46be2e0-5e62-41af-892a-d531d56eb13c",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "19fc2016-6f3c-4676-bcc3-12a3099be2ed",
  "sourceToolAssistantUUID": "d46be2e0-5e62-41af-892a-d531d56eb13c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T20:03:31.036Z_

<details><summary>↩ Tool result · `toolu_01Eaef1DBtugHQeMKUSvjy4G`</summary>

```text
Web search results for query: "paraphrase synonym invariance visual grounding robot affordance self-supervised"

Links: [{"title":"WEAKLY-SUPERVISED AFFORDANCE GROUNDING ...","url":"https://openreview.net/pdf/2551c99500000f40bd07dc3c4c3d1111d11b9c1a.pdf"},{"title":"[PDF] Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Do-As-I-Can,-Not-As-I-Say:-Grounding-Language-in-Ahn-Brohan/cb5e3f085caefd1f3d5e08637ab55d39e61234fc"},{"title":"Affordance Grounding from Demonstration Video to Target Image","url":"https://arxiv.org/pdf/2303.14644"},{"title":"Unsupervised Affordance Distillation for Generalization in ...","url":"https://openreview.net/pdf?id=an953WOpo2"},{"title":"Grounding Language with Visual Affordances over Unstructured Data","url":"https://arxiv.org/pdf/2210.01911"},{"title":"Learning Affordance Grounding from Exocentric Images","url":"https://arxiv.org/pdf/2203.09905"},{"title":"Weakly-Supervised Affordance Grounding Guided by Part-Level Semantic Priors","url":"https://www.researchgate.net/publication/392314511_Weakly-Supervised_Affordance_Grounding_Guided_by_Part-Level_Semantic_Priors"}]

Based on the search results, I found several relevant research papers that combine these concepts:

**Key Research Areas:**

Self-supervised visuo-lingual affordance models are being used to learn language-conditioned robot skills from unstructured, offline data with minimal language annotation.

Affordance Invariance Mining modules have been developed to extract specific affordance clues by minimizing intra-class differences from interaction habits in exocentric images.

Recent work leverages vision-language model embeddings for flexible affordance grounding with text, including text-conditioned affordance map generation and text synonym augmentation to enhance robustness.

Self-supervised pre-training techniques like Masked Affordance Hand (MaskAHand) synthesize video-image data and simulate context changes to improve affordance grounding across different viewpoints.

Some approaches reformat visual affordance understanding as a visual question-answering problem and distill knowledge into specialized visual affordance models that provide fine-grained continuous predictions in visual space.

These papers collectively demonstrate how paraphrase/synonym robustness, invariance learning, visual grounding, robot affordances, and self-supervised learning are being integrated in current research on robotic perception and control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "daed55f6-9767-45f2-bb74-773cd75d503b",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "2c7bb0a6-4f7b-408b-abdd-c1af9c050177",
  "sourceToolAssistantUUID": "daed55f6-9767-45f2-bb74-773cd75d503b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-18T20:03:33.915Z_

UAD is particularly relevant. Let me dig deeper into it and also search for more threatening overlaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c7bb0a6-4f7b-408b-abdd-c1af9c050177",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdeb1tS3mnqmY4EFu2m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9de3082-6706-4e44-92b3-46fad25f535c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYZywWDMC1FcYqX7Y3yWyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3258,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 21549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1023,
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

_source line 51 · 2026-05-18T20:03:34.396Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0175nZkYnfkqjguxJ7Tp9L6K`</summary>

```json
{
  "query": "UAD unsupervised affordance distillation task instruction variation generalization decoder frozen features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9de3082-6706-4e44-92b3-46fad25f535c",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdeb1tS3mnqmY4EFu2m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "122a996a-8902-4a9d-834c-dee703f28adb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYZywWDMC1FcYqX7Y3yWyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3258,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 21549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1023,
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

_source line 52 · 2026-05-18T20:03:35.409Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T3M36KcLRB6YXPTEiGJbjf`</summary>

```json
{
  "query": "\"contrastive representation regularization\" VLA vision language action RS-CL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "122a996a-8902-4a9d-834c-dee703f28adb",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdeb1tS3mnqmY4EFu2m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ea2ed78-7ff3-4f9d-92f2-6abacaaaaea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYZywWDMC1FcYqX7Y3yWyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3258,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 21549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1023,
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

_source line 53 · 2026-05-18T20:03:35.808Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B9J5DqMwYyhz31oQt9SVmN`</summary>

```json
{
  "query": "language paraphrase augmentation robot policy invariance equivariance visual representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ea2ed78-7ff3-4f9d-92f2-6abacaaaaea9",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdeb1tS3mnqmY4EFu2m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16f6dfea-328a-40a8-b960-de384dab19d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYZywWDMC1FcYqX7Y3yWyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3258,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 21549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1023,
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

_source line 54 · 2026-05-18T20:03:36.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019UNH438DyfwQykUR6kEHyz`</summary>

```json
{
  "query": "LITEN VLA affordance inference-time learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16f6dfea-328a-40a8-b960-de384dab19d1",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdeb1tS3mnqmY4EFu2m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89a2a029-8a03-49d2-b207-c9f04de3b52f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYZywWDMC1FcYqX7Y3yWyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3258,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 21549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1023,
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

_source line 55 · 2026-05-18T20:03:37.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FnHU3VRRp6nRhHnHqews6Z`</summary>

```json
{
  "query": "\"text synonym augmentation\" affordance grounding robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89a2a029-8a03-49d2-b207-c9f04de3b52f",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdeb1tS3mnqmY4EFu2m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "457d741b-9879-4cee-a4b0-6fed5f211522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYZywWDMC1FcYqX7Y3yWyV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3258,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 21549,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1023
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3258,
          "output_tokens": 294,
          "cache_read_input_tokens": 21549,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1023,
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

_source line 56 · 2026-05-18T20:03:40.744Z_

<details><summary>↩ Tool result · `toolu_0175nZkYnfkqjguxJ7Tp9L6K`</summary>

```text
Web search results for query: "UAD unsupervised affordance distillation task instruction variation generalization decoder frozen features"

Links: [{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/pdf/2506.09284"},{"title":"[2506.09284] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/abs/2506.09284"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=an953WOpo2"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11128868/"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | alphaXiv","url":"https://www.alphaxiv.org/resources/2506.09284v1"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/html/2506.09284v1"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://www.researchgate.net/publication/392597063_UAD_Unsupervised_Affordance_Distillation_for_Generalization_in_Robotic_Manipulation"},{"title":"[Literature Review] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://www.themoonlight.io/en/review/uad-unsupervised-affordance-distillation-for-generalization-in-robotic-manipulation"},{"title":"[PDF] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/UAD:-Unsupervised-Affordance-Distillation-for-in-Tang-Huang/a7992218b0f8c8663e8ac144fcf58017a2a3c335"}]

I found comprehensive information about UAD. Here's what the search reveals:

## UAD: Unsupervised Affordance Distillation

UAD is a method for distilling affordance knowledge from foundation models into a task-conditioned affordance model without any manual annotations.

### Key Technical Approach

By leveraging the complementary strengths of large vision models and vision-language models, UAD automatically annotates a large-scale dataset with detailed instruction, visual affordance pairs. The method reuses and freezes the weights of DINOv2 and trains only a lightweight task-conditioned decoder.

### Generalization Capabilities

Training only a lightweight task-conditioned decoder atop frozen features, UAD exhibits notable generalization to in-the-wild robotic scenes and to various human activities, despite only being trained on rendered objects in simulation.

Using affordance provided by UAD as the observation space, an imitation learning policy demonstrates promising generalization to unseen object instances, object categories, and even variations in task instructions after training on as few as 10 demonstrations. As UAD is conditioned on task instructions while offering precise affordance prediction, it can also generalize to variations in instructions that control the objects of interaction via natural language.

The work addresses a significant challenge in robotic manipulation by enabling task-conditioned affordance prediction that generalizes across different objects, categories, and instruction variations without requiring manual annotations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "122a996a-8902-4a9d-834c-dee703f28adb",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "bbbee558-9186-4807-af3d-9579e0dd4817",
  "sourceToolAssistantUUID": "122a996a-8902-4a9d-834c-dee703f28adb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-18T20:03:41.050Z_

<details><summary>↩ Tool result · `toolu_01T3M36KcLRB6YXPTEiGJbjf`</summary>

```text
Web search results for query: ""contrastive representation regularization" VLA vision language action RS-CL 2025"

Links: [{"title":"CONTRASTIVE REPRESENTATION REGULARIZATION","url":"https://openreview.net/pdf/620347d848a1d02068b859e759f37dd50a4304b9.pdf"},{"title":"Contrastive Representation Regularization for Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01711v1"},{"title":"[2510.01711] Contrastive Representation Regularization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.01711"},{"title":"Contrastive Representation Regularization for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.01711"},{"title":"Contrastive Representation Regularization for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=hm2EcwFm2Q"}]

I found research on "Contrastive Representation Regularization for Vision-Language-Action Models." Here's what the search revealed:

## Overview

The paper introduces Robot State-aware Contrastive Loss (RS-CL), a simple and effective representation regularization for VLA models, designed to bridge the gap between VLM representations and robotic signals.

## The Problem Addressed

VLA representations remain suboptimal, lacking sensitivity to robotic signals such as control actions and proprioceptive states. VLM representations are typically trained on large-scale visual instruction datasets, but have not been explicitly exposed to robotic modalities, such as low-level control actions and proprioceptive information.

## Solution and Approach

RS-CL aligns the representations more closely with the robot's proprioceptive states, by using relative distances between the states as soft supervision, and effectively enhances control-relevant representation learning, while being lightweight and fully compatible with standard VLA training pipeline.

## Results

RS-CL substantially improves the manipulation performance of state-of-the-art VLA models; it pushes the prior art from 30.8% to 41.5% on pick-and-place tasks in RoboCasa-Kitchen, and boosts success rates from 45.0% to 58.3% on challenging real-robot manipulation tasks.

The paper was submitted in October 2025 and appears to be a recent research contribution in the robotics and vision-language-action domain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ea2ed78-7ff3-4f9d-92f2-6abacaaaaea9",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "85f0d75e-77c7-49c7-b81c-07bcf349bca5",
  "sourceToolAssistantUUID": "1ea2ed78-7ff3-4f9d-92f2-6abacaaaaea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T20:03:43.250Z_

<details><summary>↩ Tool result · `toolu_01B9J5DqMwYyhz31oQt9SVmN`</summary>

```text
Web search results for query: "language paraphrase augmentation robot policy invariance equivariance visual representation"

Links: [{"title":"Augmenting Imitation Experience via Equivariant Representations","url":"https://arxiv.org/pdf/2110.07668"},{"title":"EquivAct: SIM(3)-Equivariant Visuomotor Policies beyond Rigid Object   Manipulation","url":"https://arxiv.org/pdf/2310.16050"},{"title":"Canonical Policy: Learning Canonical 3D Representation for SE⁢(3)-Equivariant Policy","url":"https://arxiv.org/html/2505.18474"},{"title":"Invariance Co-training for Robot Visual Generalization","url":"https://arxiv.org/pdf/2512.05230"},{"title":"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations","url":"https://arxiv.org/html/2411.16959"},{"title":"Canonical Policy: Learning Canonical 3D Representation for Equivariant Policy","url":"https://arxiv.org/html/2505.18474v1"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"}]

Based on the search results, here's what I found on language paraphrase augmentation, robot policy, invariance, equivariance, and visual representation:

## Key Research Areas

**Equivariance in Robot Policy Learning:**
Policies can be designed as functions of equivariant embeddings that predict latent representations of images at nearby viewpoints using equivariance properties to augment training data. Adding equivariance to both visual object representation and policy architecture enables policies to generalize to novel object positions, orientations, and scales by construction.

**Invariance and Visual Representation:**
Research examines robot visual generalization by introducing auxiliary tasks for state similarity and invariance to observational perturbations. State similarity recognition involves mapping varied observation configurations to the same underlying state, while relative observation disentanglement involves understanding whether changes in observation were induced by state changes or state-invariant observation perturbations.

**Language and Instruction Robustness:**
Recent work evaluates policies under paraphrased instructions and tests training with instruction augmentations, indicating active research into making robot policies robust to language variations.

**Unified Framework:**
Some approaches formalize the relationship between invariance, equivariance, and causality using group theory and probabilistic graphical models to enhance data augmentation for imitation learning.

These results show that the intersection of language paraphrase augmentation, equivariance/invariance properties, and visual representation learning is an active research area in robot learning and manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16f6dfea-328a-40a8-b960-de384dab19d1",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "96de186c-8545-446f-aa39-9978fe91d148",
  "sourceToolAssistantUUID": "16f6dfea-328a-40a8-b960-de384dab19d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-18T20:03:43.402Z_

<details><summary>↩ Tool result · `toolu_019UNH438DyfwQykUR6kEHyz`</summary>

```text
Web search results for query: "LITEN VLA affordance inference-time learning 2025 2026"

Links: [{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/html/2510.19752"},{"title":"[2510.19752] Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.19752"},{"title":"LITEN: Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://liten-vla.github.io/"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.19752"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251019752S/abstract"},{"title":"[Literature Review] Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/learning-affordances-at-inference-time-for-vision-language-action-models"}]

I found comprehensive information about LITEN. Here are the search results:

## LITEN: Learning Affordances at Inference-Time for Vision-Language-Action Models

LITEN is a method that connects a VLA low-level policy to a high-level VLM that conditions on past experiences by including them in-context, allowing it to learn the affordances and capabilities of the low-level VLA.

### How It Works

The approach iterates between a reasoning phase that generates and executes plans for the low-level VLA, and an assessment phase that reflects on the resulting execution and draws useful conclusions to be included in future reasoning contexts.

### Key Innovation

LITEN introduces an inference-time learning method that enables robotic policies to reason through complex tasks, form plans, and then iteratively adjust those plans based on observed outcomes, without requiring additional training.

### Results

Experimental results demonstrate LITEN is able to effectively learn from past experience to generate plans that use high-affordance instructions to accomplish long-horizon tasks.

The paper was published in October 2025 and is authored by Ameesh Shah and colleagues from UC Berkeley. You can find more details on the project website at https://liten-vla.github.io/ or on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89a2a029-8a03-49d2-b207-c9f04de3b52f",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "c8f4ba46-6cc5-4e31-9253-507146f742ab",
  "sourceToolAssistantUUID": "89a2a029-8a03-49d2-b207-c9f04de3b52f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T20:03:44.233Z_

<details><summary>↩ Tool result · `toolu_01FnHU3VRRp6nRhHnHqews6Z`</summary>

```text
Web search results for query: ""text synonym augmentation" affordance grounding robustness"

Links: [{"title":"[2409.06210] INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding","url":"https://arxiv.org/abs/2409.06210"},{"title":"INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding","url":"https://arxiv.org/html/2409.06210v1"},{"title":"INTRA: Interaction Relationship-Aware Weakly Supervised Affordance Grounding | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-73039-9_2"},{"title":"ECCV Poster INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding","url":"https://eccv.ecva.net/virtual/2024/poster/747"},{"title":"Data Augmentation Methods for Enhancing Robustness in Text Classification Tasks","url":"https://www.mdpi.com/1999-4893/16/1/59"},{"title":"Resource-Efficient Affordance Grounding with Complementary Depth","url":"https://arxiv.org/pdf/2503.02600"},{"title":"Resource-Efficient Affordance Grounding with Complementary Depth and Semantic Prompts","url":"https://arxiv.org/html/2503.02600"},{"title":"CRAFT: A Neuro-Symbolic Framework for Visual Functional Affordance Grounding","url":"https://arxiv.org/pdf/2507.14426"}]

Based on the search results, I found highly relevant information about your query. The most prominent work on this topic is the INTRA framework:

## INTRA: Text Synonym Augmentation for Affordance Grounding

INTRA leverages vision-language model embeddings for performing affordance grounding flexibly with any text, designing text-conditioned affordance map generation to reflect interaction relationship for contrastive learning and enhancing robustness with text synonym augmentation.

INTRA actively leverages VLM text embedding in proposed text-conditioned affordance map generation for flexible affordance grounding, further bolstered by text synonym augmentation for robustness.

## Method Overview

INTRA recasts the affordance grounding problem as representation learning to identify unique features of interactions through contrastive learning with exocentric images only, eliminating the need for paired datasets.

## Performance

INTRA achieves state-of-the-art performance across diverse datasets, relying solely on exocentric images for training, unlike prior methods that also use egocentric images. The method demonstrates generalization feasibility on novel objects, interactions, and images with significant domain gaps.

The research paper was published in September 2024 and addresses challenges in weakly supervised affordance grounding by using text synonym augmentation as a key mechanism to enhance model robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "457d741b-9879-4cee-a4b0-6fed5f211522",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "274032fa-1a8e-4845-8560-28c512dee7b7",
  "sourceToolAssistantUUID": "457d741b-9879-4cee-a4b0-6fed5f211522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-18T20:03:46.937Z_

INTRA is very relevant. Let me dig deeper into it and a few other concerning papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "274032fa-1a8e-4845-8560-28c512dee7b7",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdfZY7gxeDTb5e8c7sN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebec851c-00c5-4c23-a262-9c82a5e2e3ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129Px89Hse6RhVQPwSxRTG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7203,
      "cache_read_input_tokens": 22572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7203,
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

_source line 62 · 2026-05-18T20:03:47.817Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HZcyAmmsnsJvkun6Ja1ykM`</summary>

```json
{
  "query": "INTRA interaction relationship affordance grounding text synonym augmentation contrastive learning VLM ECCV 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebec851c-00c5-4c23-a262-9c82a5e2e3ea",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdfZY7gxeDTb5e8c7sN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d63076ce-b485-486b-ab1c-7457e4468fff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129Px89Hse6RhVQPwSxRTG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7203,
      "cache_read_input_tokens": 22572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7203,
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

_source line 63 · 2026-05-18T20:03:48.795Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013xHa3xvAR2RdVER1Z8q1up`</summary>

```json
{
  "query": "\"Grounding Language with Visual Affordances\" HULC CLIP contrastive affordance language robot 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d63076ce-b485-486b-ab1c-7457e4468fff",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdfZY7gxeDTb5e8c7sN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50ed7d71-0514-49ad-a49b-ec201eecfa45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129Px89Hse6RhVQPwSxRTG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7203,
      "cache_read_input_tokens": 22572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7203,
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

_source line 64 · 2026-05-18T20:03:49.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DE4p52SebTBJdmvvbnNCP9`</summary>

```json
{
  "query": "Green-VLA visual question answering affordance priors robot adaptation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50ed7d71-0514-49ad-a49b-ec201eecfa45",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdfZY7gxeDTb5e8c7sN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29d33b9f-8b8e-4286-b715-4c70e630f94c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129Px89Hse6RhVQPwSxRTG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7203,
      "cache_read_input_tokens": 22572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7203,
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

_source line 65 · 2026-05-18T20:03:50.054Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SvK7qQxXme43Csof7bb9cT`</summary>

```json
{
  "query": "\"invariance co-training\" robot visual generalization 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29d33b9f-8b8e-4286-b715-4c70e630f94c",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdfZY7gxeDTb5e8c7sN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a21dfe43-979d-4755-9a53-1e939e352867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129Px89Hse6RhVQPwSxRTG8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7203,
      "cache_read_input_tokens": 22572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7203,
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

_source line 66 · 2026-05-18T20:03:50.803Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EHa7jB8kbHw5bQXxuUvzAs`</summary>

```json
{
  "query": "RoboPCA pose-centered affordance prediction task instructions 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a21dfe43-979d-4755-9a53-1e939e352867",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdfZY7gxeDTb5e8c7sN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf121437-b69a-44a3-aa61-69517761c141",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129Px89Hse6RhVQPwSxRTG8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7203,
      "cache_read_input_tokens": 22572,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7203
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 22572,
          "cache_creation_input_tokens": 7203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7203,
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

_source line 67 · 2026-05-18T20:03:53.107Z_

<details><summary>↩ Tool result · `toolu_01HZcyAmmsnsJvkun6Ja1ykM`</summary>

```text
Web search results for query: "INTRA interaction relationship affordance grounding text synonym augmentation contrastive learning VLM ECCV 2024"

Links: [{"title":"INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding","url":"https://jeeit17.github.io/INTRA/"},{"title":"INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding","url":"https://arxiv.org/html/2409.06210v1"},{"title":"[2409.06210] INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding","url":"https://arxiv.org/abs/2409.06210"},{"title":"ECCV Poster INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding","url":"https://eccv.ecva.net/virtual/2024/poster/747"},{"title":"INTRA: Interaction Relationship-Aware Weakly Supervised Affordance Grounding | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-73039-9_2"},{"title":"Paper page - INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding","url":"https://huggingface.co/papers/2409.06210"},{"title":"INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/intra-interaction-relationship-aware-weakly-supervised-affordance"}]

I found relevant information about INTRA, a paper presented at ECCV 2024. Here's what the search revealed:

## INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding

INTRA is a paper published at ECCV 2024 by Jang, Seo, and Chun that addresses weakly supervised affordance grounding.

**Key Approach:**
INTRA recasts the problem as representation learning to identify unique features of interactions through contrastive learning with exocentric images only, eliminating the need for paired datasets.

**Technical Components:**
The method leverages vision-language model embeddings for performing affordance grounding flexibly with any text, designing text-conditioned affordance map generation to reflect interaction relationship for contrastive learning and enhancing robustness with text synonym augmentation.

**Performance:**
The method outperformed prior arts on diverse datasets such as AGD20K, IIT-AFF, CAD and UMD. Experimental results demonstrate that the method has remarkable domain scalability for synthesized images/illustrations and is capable of performing affordance grounding for novel interactions and objects.

**Key Innovation:**
INTRA consists of text synonym augmentation and text-conditioned affordance map generation module along with interaction relationship-guided contrastive learning, so that inference on unseen interactions is possible.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d63076ce-b485-486b-ab1c-7457e4468fff",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "4da75fb9-7ab8-4a32-8496-b4fac7a5b2c4",
  "sourceToolAssistantUUID": "d63076ce-b485-486b-ab1c-7457e4468fff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-18T20:03:53.677Z_

<details><summary>↩ Tool result · `toolu_013xHa3xvAR2RdVER1Z8q1up`</summary>

```text
Web search results for query: ""Grounding Language with Visual Affordances" HULC CLIP contrastive affordance language robot 2022"

Links: [{"title":"Grounding Language with Visual Affordances over Unstructured Data | Request PDF","url":"https://www.researchgate.net/publication/364194863_Grounding_Language_with_Visual_Affordances_over_Unstructured_Data"},{"title":"GitHub - mees/hulc2: [ICRA2023] Grounding Language with Visual Affordances over Unstructured Data","url":"https://github.com/mees/hulc2"},{"title":"Grounding Language with Visual Affordances over Unstructured Data","url":"https://arxiv.org/pdf/2210.01911"},{"title":"[2210.01911] Grounding Language with Visual Affordances over Unstructured Data","url":"https://ar5iv.labs.arxiv.org/html/2210.01911"},{"title":"Grounding Language with Visual Affordances over Unstructured Data | Oier Mees","url":"https://www.oiermees.com/publication/hulc2/"},{"title":"Grounding Language with Visual Affordances over Unstructured Data","url":"http://hulc2.cs.uni-freiburg.de/"}]

Based on the search results, I found information about "Grounding Language with Visual Affordances over Unstructured Data":

This work presents HULC++ (Hierarchical Universal Language Conditioned Policies) 2.0, a novel approach to efficiently learn general-purpose language-conditioned robot skills from unstructured, offline and reset-free data by exploiting a self-supervised visuo-lingual affordance model, which requires annotating as little as 1% of the total data with language.

The approach leverages a visual affordance model to guide the robot to the vicinity of actionable regions referred by language. When paired with LLMs to break down abstract natural language instructions into subgoals via few-shot prompting, the method is capable of completing long-horizon, multi-tier tasks in the real world, while requiring an order of magnitude less data than previous approaches.

The method achieves state-of-the-art performance on the challenging CALVIN benchmark and learns over 25 distinct visuomotor manipulation tasks with a single policy in the real world. The research was published in the Proceedings of the IEEE International Conference on Robotics and Automation (ICRA) in 2023 by Oier Mees, Jessica Borja-Diaz, and Wolfram Burgard.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50ed7d71-0514-49ad-a49b-ec201eecfa45",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "36b55d14-9141-431c-9e6f-b99ee9f19f34",
  "sourceToolAssistantUUID": "50ed7d71-0514-49ad-a49b-ec201eecfa45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-18T20:03:56.808Z_

<details><summary>↩ Tool result · `toolu_01EHa7jB8kbHw5bQXxuUvzAs`</summary>

```text
Web search results for query: "RoboPCA pose-centered affordance prediction task instructions 2026"

Links: [{"title":"[2603.07691] RoboPCA: Pose-centered Affordance Learning from Human Demonstrations for Robot Manipulation","url":"https://arxiv.org/abs/2603.07691"},{"title":"RoboPCA: Pose-centered Affordance Learning from Human Demonstrations for Robot Manipulation","url":"https://arxiv.org/pdf/2603.07691"},{"title":"(PDF) RoboPCA: Pose-centered Affordance Learning from Human Demonstrations for Robot Manipulation","url":"https://www.researchgate.net/publication/401719442_RoboPCA_Pose-centered_Affordance_Learning_from_Human_Demonstrations_for_Robot_Manipulation"},{"title":"RoboPCA: Pose-centered Affordance Learning from Human Demonstrations for Robot Manipulation","url":"https://arxiv.org/html/2603.07691v1"},{"title":"RoboPoint: A Vision-Language Model for Spatial Affordance Prediction in Robotics | OpenReview","url":"https://openreview.net/forum?id=GVX6jpZOhU&noteId=GVX6jpZOhU"}]

Based on the search results, here's what I found about RoboPCA and the pose-centered affordance prediction task:

RoboPCA is a pose-centered affordance prediction framework that jointly predicts task-appropriate contact regions and poses conditioned on instructions. Unlike existing spatial affordance prediction methods that mainly focus on locating contact regions while delegating pose to independent pose estimation approaches, RoboPCA addresses inconsistencies that can occur between predicted contact regions and candidate poses.

The framework includes Human2Afford, a data curation pipeline that automatically recovers scene-level 3D information and infers pose-centered affordance annotations from human demonstrations by extracting scene depth and object masks for 3D context, while obtaining pose-centered affordance annotations through tracking object points and analyzing hand-object interaction patterns.

RoboPCA integrates geometry-appearance cues through an RGB-D encoder and incorporates mask-enhanced features into a diffusion-based framework, outperforming baseline methods on image datasets, simulation, and real robots, with strong generalization across tasks and categories.

The research paper was published in March 2026 (arxiv: 2603.07691) by Zhanqi Xiao, Ruiping Wang, and Xilin Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf121437-b69a-44a3-aa61-69517761c141",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "e10444f5-fe58-4dd1-966d-480851d38c83",
  "sourceToolAssistantUUID": "cf121437-b69a-44a3-aa61-69517761c141",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-18T20:03:56.976Z_

<details><summary>↩ Tool result · `toolu_01SvK7qQxXme43Csof7bb9cT`</summary>

```text
Web search results for query: ""invariance co-training" robot visual generalization 2025"

Links: [{"title":"[2512.05230] Invariance Co-training for Robot Visual Generalization","url":"https://arxiv.org/abs/2512.05230"},{"title":"Invariance Co-training for Robot Visual Generalization","url":"https://arxiv.org/pdf/2512.05230"},{"title":"Invariance Co-training for Robot Visual Generalization","url":"https://arxiv.org/html/2512.05230"},{"title":"Enhancing Generalization in Vision–Language–Action Models by","url":"https://arxiv.org/pdf/2509.11417"},{"title":"EmbodiedOneVision: Interleaved Vision-Text-Action Pretraining for General Robot Control","url":"https://arxiv.org/html/2508.21112v1"}]

I found a recent research paper on this topic. Here are the key findings:

The paper "Invariance Co-training for Robot Visual Generalization" is by Jonathan Yang, Chelsea Finn, and Dorsa Sadigh, and it was posted on December 4, 2025.

**Main Approach:**
The work introduces two key auxiliary tasks—state similarity and invariance to observational perturbations—applied to both demonstration data and static visual data, leveraging both robotic demonstration data and synthetic images from non-physics-based simulation (e.g., Unreal Engine) to improve generalization to unseen camera viewpoints, lighting configurations, and distractor conditions.

**Key Results:**
The results demonstrate that co-training on diverse data improves performance by 18% over existing generative augmentation methods.

**Problem Being Addressed:**
Despite recent advancements, many large-scale robotic policies remain sensitive to key sources of observational variation such as changes in camera perspective, lighting, and the presence of distractor objects, arising from the substantial diversity required to robustly cover these axes coupled with the current scarcity of large-scale robotic datasets.

You can find more information and videos at their project website referenced in the paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a21dfe43-979d-4755-9a53-1e939e352867",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "cbdd564e-265a-4095-9e9a-b2fca170bd97",
  "sourceToolAssistantUUID": "a21dfe43-979d-4755-9a53-1e939e352867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-18T20:03:58.456Z_

<details><summary>↩ Tool result · `toolu_01DE4p52SebTBJdmvvbnNCP9`</summary>

```text
Web search results for query: "Green-VLA visual question answering affordance priors robot adaptation 2025 2026"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919"},{"title":"Visual Affordance Prediction for Guiding Robot Exploration","url":"https://arxiv.org/pdf/2305.17783"},{"title":"Green-VLA: Staged Vision-Language-Action Model for Generalist Robots","url":"https://arxiv.org/pdf/2602.00919"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/pdf/2409.01083"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"Affordance Learning from Play for Sample-Efficient Policy Learning","url":"https://arxiv.org/pdf/2203.00352"},{"title":"Comprehensive Survey of VLA Models | PDF | Embodied Cognition | Computer Vision","url":"https://www.scribd.com/document/939026368/Pure-Vision-Language-Action-VLA-Models-A-Comprehensive-Survey"}]

Based on the web search results, here's what I found about Green-VLA and related topics:

## Green-VLA Overview

Green-VLA is a staged Vision-Language-Action framework for real-world deployment on the humanoid Green robot, while maintaining generalization across diverse embodiments.

## Training Architecture

Green-VLA follows a five-stage curriculum: (L0) foundational VLMs, (L1) multimodal grounding, (R0) multi-embodiment pretraining, (R1) embodiment-specific adaptation, and (R2) RL-based policy alignment. Progression builds semantic and physical priors, learns shared affordances, and aligns policies for long-horizon execution beyond behavior cloning.

## Role of Affordance Priors

Each stage addresses a distinct bottleneck: L1 enriches semantic grounding, R0 captures affordance priors, R1 adapts efficiently to embodiments, and R2 injects reward-based alignment for real-world robustness. Green-VLA's robot-specific training stages use visual question answering (VQA) and robotics data and enable robot adaptation and specialization for new embodiments, spatial reasoning, task generalization, dexterous manipulation, and failure recovery.

## Performance & Capabilities

Optimized for the Green humanoid, Green-VLA generalizes in a zero-shot manner to new embodiments and achieves state-of-the-art performance across bimanual systems and benchmarks, with RL alignment providing gains in success rate, robustness, and long-horizon efficiency.

The work was completed in February 2026 and includes a unified data processing pipeline and an embodiment-aware action interface for controlling diverse robot types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29d33b9f-8b8e-4286-b715-4c70e630f94c",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "7ee81677-f267-405d-9b3a-d6e6ce84c9bb",
  "sourceToolAssistantUUID": "29d33b9f-8b8e-4286-b715-4c70e630f94c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-18T20:04:01.353Z_

Let me do one final batch of searches to ensure completeness on the most directly threatening angles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ee81677-f267-405d-9b3a-d6e6ce84c9bb",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdgcmMozVV1wkK2qgiL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21b738c1-6294-4200-88b6-8d18a7688eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pUjMEtHSsEp2TiBE9NPwj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1162,
      "cache_creation_input_tokens": 2498,
      "cache_read_input_tokens": 29775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2498,
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

_source line 73 · 2026-05-18T20:04:02.339Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NjAZYpubLTyNETTkELqgZw`</summary>

```json
{
  "query": "HULC++ self-supervised visuo-lingual affordance model language annotated 1 percent robot skills"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21b738c1-6294-4200-88b6-8d18a7688eb8",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdgcmMozVV1wkK2qgiL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb6803a4-35f5-4e38-a513-c8e35de17957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pUjMEtHSsEp2TiBE9NPwj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1162,
      "cache_creation_input_tokens": 2498,
      "cache_read_input_tokens": 29775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2498,
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

_source line 74 · 2026-05-18T20:04:03.280Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AgUAarc9sWwV2iNmfS7wLv`</summary>

```json
{
  "query": "\"affordance decoder\" VLA \"vision language action\" end-to-end self-supervised 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb6803a4-35f5-4e38-a513-c8e35de17957",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdgcmMozVV1wkK2qgiL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8d8b2d9-d045-44ff-8e9a-23dd6c603b8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pUjMEtHSsEp2TiBE9NPwj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1162,
      "cache_creation_input_tokens": 2498,
      "cache_read_input_tokens": 29775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2498,
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

_source line 75 · 2026-05-18T20:04:04.222Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TNGybeabSZXbQcMQjQyQ98`</summary>

```json
{
  "query": "instruction rephrasing paraphrasing robustness robot policy training consistency signal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8d8b2d9-d045-44ff-8e9a-23dd6c603b8e",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdgcmMozVV1wkK2qgiL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d686753-746b-4c67-89a8-d43dada99a56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pUjMEtHSsEp2TiBE9NPwj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1162,
      "cache_creation_input_tokens": 2498,
      "cache_read_input_tokens": 29775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2498,
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

_source line 76 · 2026-05-18T20:04:04.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AunNbWuARmkk5F2GYWX6R6`</summary>

```json
{
  "query": "\"language invariant\" representation affordance manipulation visual features activation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d686753-746b-4c67-89a8-d43dada99a56",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdgcmMozVV1wkK2qgiL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0faa98df-f2ec-44f3-9aa7-da3aba6c98c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pUjMEtHSsEp2TiBE9NPwj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1162,
      "cache_creation_input_tokens": 2498,
      "cache_read_input_tokens": 29775,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2498
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1162,
          "output_tokens": 251,
          "cache_read_input_tokens": 29775,
          "cache_creation_input_tokens": 2498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2498,
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

_source line 77 · 2026-05-18T20:04:08.564Z_

<details><summary>↩ Tool result · `toolu_01NjAZYpubLTyNETTkELqgZw`</summary>

```text
Web search results for query: "HULC++ self-supervised visuo-lingual affordance model language annotated 1 percent robot skills"

Links: [{"title":"Foundation Models in Robotics: Applications, Challenges, and the Future","url":"https://arxiv.org/html/2312.07843v1"},{"title":"Grounding Language with Visual Affordances over Unstructured Data","url":"http://hulc2.cs.uni-freiburg.de/"},{"title":"[2210.01911] Grounding Language with Visual Affordances over Unstructured Data","url":"https://ar5iv.labs.arxiv.org/html/2210.01911"},{"title":"Grounding Language with Visual Affordances over Unstructured Data | Oier Mees","url":"https://www.oiermees.com/publication/hulc2/"},{"title":"GitHub - mees/hulc2: [ICRA2023] Grounding Language with Visual Affordances over Unstructured Data","url":"https://github.com/mees/hulc2"},{"title":"Grounding Language with Visual Affordances over Unstructured Data","url":"https://arxiv.org/pdf/2210.01911"},{"title":"Language-Conditioned Imitation Learning with Base Skill ...","url":"https://arxiv.org/pdf/2305.19075"}]

Based on the search results, here's what I found about HULC++ and the self-supervised visuo-lingual affordance model:

HULC++ (Hierarchical Universal Language Conditioned Policies 2.0) uses a self-supervised visuo-lingual affordance model to learn general-purpose language-conditioned robot skills from unstructured offline data in the real world, requiring annotation of as little as 1% of the total data with language.

The visuo-lingual affordance model has an encoder-decoder architecture with two decoder heads that share the same encoder and are conditioned on the input language instruction, with one head predicting a distribution over the image where each pixel likelihood represents an afforded point.

The method achieves state-of-the-art performance on the challenging CALVIN benchmark and learns over 25 distinct visuomotor manipulation tasks with a single policy in the real world. Additionally, when paired with Large Language Models to break down abstract natural language instructions into subgoals via few-shot prompting, the method is capable of completing long-horizon, multi-tier tasks in the real world while requiring an order of magnitude less data than previous approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb6803a4-35f5-4e38-a513-c8e35de17957",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "94734ed0-5f6b-4283-9831-9afd410c1317",
  "sourceToolAssistantUUID": "fb6803a4-35f5-4e38-a513-c8e35de17957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-18T20:04:11.252Z_

<details><summary>↩ Tool result · `toolu_01AgUAarc9sWwV2iNmfS7wLv`</summary>

```text
Web search results for query: ""affordance decoder" VLA "vision language action" end-to-end self-supervised 2025 2026"

Links: [{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA","url":"https://arxiv.org/pdf/2603.29844"},{"title":"VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving","url":"https://arxiv.org/pdf/2511.12405"}]

Based on the web search results, I found several relevant papers and research on Vision-Language-Action (VLA) models and affordance-related work from 2025-2026:

## Key Research Findings:

**Recent VLA Improvements:**
- Recent advancements in Vision-Language-Action (VLA) models have shown that training with internet-scale data can empower end-to-end policy learning models to outperform non-VLA models.

**Affordance-Related Work:**
- The A1 framework leverages pretrained VLMs that provide implicit affordance priors for action generation and releases the full training stack to enable end-to-end reproducibility.

- Recent 2025 research includes "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation" (ICRA 25 Best Paper Finalist) and "3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds".

**Challenges in End-to-End VLA:**
- VLA models encounter substantial challenges in generalization, frequently succumbing to a "Memory Trap" where in out-of-distribution scenarios, these models tend to rigidly reproduce trajectories memorized from the training data.

The search results show active research in combining affordance learning with VLA models, particularly focused on improving generalization and developing more efficient, self-supervised approaches for robotic manipulation and autonomous systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8d8b2d9-d045-44ff-8e9a-23dd6c603b8e",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "8033f1f8-126e-41e3-bd4f-c5e604c98b68",
  "sourceToolAssistantUUID": "f8d8b2d9-d045-44ff-8e9a-23dd6c603b8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-18T20:04:11.875Z_

<details><summary>↩ Tool result · `toolu_01TNGybeabSZXbQcMQjQyQ98`</summary>

```text
Web search results for query: "instruction rephrasing paraphrasing robustness robot policy training consistency signal"

Links: [{"title":"ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://arxiv.org/html/2505.10911v1"},{"title":"Contrast Sets for Evaluating Language-Guided Robot Policies","url":"https://arxiv.org/html/2406.13636v2"},{"title":"Investigating the Role of Instruction Variety and Task Difficulty in Robotic Manipulation Tasks","url":"https://arxiv.org/html/2407.03967v2"},{"title":"Quantification before Selection: Active Dynamics Preference for Robust   Reinforcement Learning","url":"https://arxiv.org/pdf/2209.11596"},{"title":"ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://openreview.net/pdf/fac8d6d9ce39a7af7a24ac30ddffb73b9634fdc0.pdf"},{"title":"Consistency Policy","url":"https://www.roboticsproceedings.org/rss20/p071.pdf"},{"title":"Guarding the Meaning: Self-Supervised Training for Semantic Robustness in Guard Models","url":"https://arxiv.org/pdf/2511.10665"},{"title":"ICR-Drive: Instruction Counterfactual Robustness for End-to-End Language-Driven Autonomous Driving","url":"https://arxiv.org/pdf/2604.05378"}]

Based on the web search results, I found several relevant papers and research on instruction rephrasing, paraphrasing, robustness in robot policy training, and consistency:

## Key Research Findings

**Instruction Robustness and Paraphrasing:**

Language-only perturbations change the wording of an instruction while preserving meaning—for example, rephrasing "go to a bed then to the couch" instruction. Models trained on original instructions show robustness to substitutivity in instructions, with this robustness likely stemming from using frozen pretrained language models like T5.

**Reward Model Training for Robot Policies:**

Research demonstrates creating multiple language instructions per task (e.g., "close the door" and "shut the door") paired with single demonstration videos to measure reward model consistency. Approaches like ReWiND achieve robustness with near-zero variance even without specialized training, aided by instruction augmentation approaches.

**Consistency Training and Signal Quality:**

Self-supervised training strategies enforce consistency across paraphrases, with a skew-aware target aggregation method providing more stable training signals than naïve averaging. During early-stage policy training, challenging tasks may provide no effective learning signal, so actively sampling systems with proper parameters during training can prevent over-conservative behavior and stabilize training.

**Instruction Counterfactual Robustness:**

Instruction variants span multiple perturbation families including Paraphrase, Ambiguity, Noise, and Misleading, where Misleading variants conflict with navigation goals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d686753-746b-4c67-89a8-d43dada99a56",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "1f835839-5be5-44fc-814b-b16ec5b37126",
  "sourceToolAssistantUUID": "1d686753-746b-4c67-89a8-d43dada99a56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-18T20:04:12.547Z_

<details><summary>↩ Tool result · `toolu_01AunNbWuARmkk5F2GYWX6R6`</summary>

```text
Web search results for query: ""language invariant" representation affordance manipulation visual features activation"

Links: [{"title":"Frontiers | Stable and variable affordances are both automatic and flexible","url":"https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2015.00351/full"},{"title":"Stable Language Guidance for Vision–Language–Action Models","url":"https://arxiv.org/html/2601.04052v1"},{"title":"[1901.10673] Invariant Feature Mappings for Generalizing Affordance Understanding Using Regularized Metric Learning","url":"https://arxiv.org/abs/1901.10673"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"Unsupervised Affordance Distillation for Generalization in ...","url":"https://openreview.net/pdf?id=an953WOpo2"},{"title":"Feature activation during word recognition: action, visual, and associative-semantic priming effects","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4444743/"},{"title":"Learning Intermediate Features of Object Affordances with a   Convolutional Neural Network","url":"https://arxiv.org/pdf/2002.08975"}]

Based on the search results, here are findings related to language invariant representations, affordances, manipulation, and visual features:

## Language-Invariant Representations

Recent work on Vision-Language-Action (VLA) models introduces training strategies that ensure policies are invariant to surface-level syntactic perturbations, addressing how language understanding can become independent of specific linguistic variations.

## Affordance and Manipulation

Research on invariant features for object affordance understanding enables more efficient manipulation, interchange of objects that visually might not be similar, transfer learning, and robot-to-human communication. Some recent approaches propose policies conditioned on both language specifications and visual affordances.

## Visual Features Activation

Visual encoders extract detailed feature representations from images, breaking them into multiple patches to capture finer levels of detail and spatial context, with visual tokens processed through neural layers. Advanced approaches isolate pure semantic signals by subtracting visual affordance distributions, effectively restoring the rank of linguistic features relative to visual dominators.

## Key Challenge

Vision-Language-Action agents frequently suffer from "instruction blindness," as dense high-frequency visual signals tend to overwhelm sparse linguistic tokens, making language-invariant representations particularly important for robust manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0faa98df-f2ec-44f3-9aa7-da3aba6c98c7",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "2a354fb2-a90e-4e4e-9eb0-cbd508a1bd38",
  "sourceToolAssistantUUID": "0faa98df-f2ec-44f3-9aa7-da3aba6c98c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-18T20:04:16.295Z_

The "Stable Language Guidance" paper looks very relevant. Let me search for it along with a few final threads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a354fb2-a90e-4e4e-9eb0-cbd508a1bd38",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdhexbfiidMTviiTUND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57b7f485-b63d-485d-8688-19c389af20d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKjapVCv17HfRwr6xF8tKP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4263,
      "cache_read_input_tokens": 32273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4263,
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

_source line 82 · 2026-05-18T20:04:16.684Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XpD6SHd6qQs6WDQupgxdM6`</summary>

```json
{
  "query": "\"Stable Language Guidance\" VLA vision language action models instruction blindness syntactic perturbations 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57b7f485-b63d-485d-8688-19c389af20d8",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdhexbfiidMTviiTUND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54e0d13c-b44d-48dc-80d0-f904eef3f308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKjapVCv17HfRwr6xF8tKP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4263,
      "cache_read_input_tokens": 32273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4263,
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

_source line 83 · 2026-05-18T20:04:17.569Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014nmumYfFjgn5FzBo1TLaCe`</summary>

```json
{
  "query": "\"Contrast Sets\" evaluating language-guided robot policies paraphrase perturbation 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54e0d13c-b44d-48dc-80d0-f904eef3f308",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdhexbfiidMTviiTUND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f2a0827-f4eb-4cb0-9790-497559e42cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKjapVCv17HfRwr6xF8tKP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4263,
      "cache_read_input_tokens": 32273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4263,
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

_source line 84 · 2026-05-18T20:04:18.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FPehGykk4CAubVRuGv9oGq`</summary>

```json
{
  "query": "ReWiND language-guided rewards robot policy instruction augmentation paraphrase consistency 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f2a0827-f4eb-4cb0-9790-497559e42cc2",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdhexbfiidMTviiTUND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb3d03d8-f82c-403c-8ac2-c6475b0f3aaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKjapVCv17HfRwr6xF8tKP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4263,
      "cache_read_input_tokens": 32273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4263,
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

_source line 85 · 2026-05-18T20:04:18.638Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016tFAEiLiDvEdv7ug7xP6Ns`</summary>

```json
{
  "query": "\"instruction blindness\" VLA visual dominance language token overwhelm 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb3d03d8-f82c-403c-8ac2-c6475b0f3aaf",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdhexbfiidMTviiTUND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a580246-4160-4f77-94a4-b63b242af658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKjapVCv17HfRwr6xF8tKP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4263,
      "cache_read_input_tokens": 32273,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4263
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 32273,
          "cache_creation_input_tokens": 4263,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4263,
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

_source line 86 · 2026-05-18T20:04:22.574Z_

<details><summary>↩ Tool result · `toolu_01XpD6SHd6qQs6WDQupgxdM6`</summary>

```text
Web search results for query: ""Stable Language Guidance" VLA vision language action models instruction blindness syntactic perturbations 2025 2026"

Links: [{"title":"Stable Language Guidance for Vision–Language–Action Models","url":"https://arxiv.org/html/2601.04052v1"},{"title":"Stable Language Guidance for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2601.04052"},{"title":"[2601.04052] Stable Language Guidance for Vision-Language-Action Models","url":"https://arxiv.org/abs/2601.04052"},{"title":"Stable Language Guidance for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/399559162_Stable_Language_Guidance_for_Vision-Language-Action_Models"},{"title":"VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models","url":"https://arxiv.org/html/2604.03956v2"}]

I found research on "Stable Language Guidance for Vision-Language-Action Models." Here are the key findings:

## Overview

The paper addresses how Vision-Language-Action (VLA) models remain brittle to linguistic perturbations, despite their impressive capabilities in robotic control.

## Key Problem

A critical "modality collapse" phenomenon occurs where strong visual priors overwhelm sparse linguistic signals, causing agents to overfit to specific instruction phrasings while ignoring the underlying semantic intent.

## Proposed Solution

The researchers propose Residual Semantic Steering (RSS), a probabilistic framework that disentangles physical affordance from semantic execution, introducing Monte Carlo Syntactic Integration to approximate the true semantic posterior via dense, LLM-driven distributional expansion, and Residual Affordance Steering, a dual-stream decoding mechanism that explicitly isolates the causal influence of language by subtracting the visual affordance prior.

## Results

By optimizing an Expected Semantic Loss over an expanded distribution, the policy becomes invariant to surface-level syntactic perturbations. RSS achieves state-of-the-art robustness, effectively mitigating "instruction blindness" and preventing rote pattern execution by decoupling semantic intent from visual affordances.

The paper was published in January 2026 and is available on arXiv (paper ID: 2601.04052).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54e0d13c-b44d-48dc-80d0-f904eef3f308",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "469270c7-f4c2-42c4-8fc1-d14f4341035f",
  "sourceToolAssistantUUID": "54e0d13c-b44d-48dc-80d0-f904eef3f308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-18T20:04:24.926Z_

<details><summary>↩ Tool result · `toolu_014nmumYfFjgn5FzBo1TLaCe`</summary>

```text
Web search results for query: ""Contrast Sets" evaluating language-guided robot policies paraphrase perturbation 2024"

Links: [{"title":"Contrast Sets for Evaluating Language-Guided Robot Policies | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/contrast-sets-evaluating-language-guided-robot-policies"},{"title":"[2406.13636] Contrast Sets for Evaluating Language-Guided Robot Policies","url":"https://arxiv.org/abs/2406.13636"},{"title":"Contrast Sets for Evaluating Language-Guided Robot Policies","url":"https://arxiv.org/html/2406.13636v1"},{"title":"Contrast Sets for Evaluating Language-Guided Robot Policies","url":"https://arxiv.org/pdf/2406.13636"},{"title":"Contrast Sets for Evaluating Language-Guided Robot Policies","url":"https://proceedings.mlr.press/v270/anwar25a.html"},{"title":"Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection","url":"https://arxiv.org/html/2502.09829v1"},{"title":"Robotics Jun 2024","url":"https://arxiv.org/list/cs.RO/2024-06?skip=300&show=100"},{"title":"ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://arxiv.org/html/2505.10911v1"}]

Based on the search results, here's what I found about "Contrast Sets for Evaluating Language-Guided Robot Policies":

This paper was published on October 28, 2024 by Abrar Anwar, Rohan Gupta, and Jesse Thomason, presenting a new approach for evaluating language-guided robot policies using contrast sets.

**Key Concept:**
Contrast sets are carefully constructed test cases that highlight specific capabilities or limitations of a system.

**Main Contribution:**
The work introduces contrast sets for robotics as an approach to make small, but specific, perturbations to otherwise independent, identically distributed (i.i.d.) test instances. Robot evaluations in language-guided, real world settings are time-consuming and often sample only a small space of potential instructions across complex scenes.

**Methodology:**
The contrast sets for language-guided robot evaluation comprise perturbation strategies based on the language, scene, and expected behavior of the robot. The researchers use the relative performance change of different contrast set perturbations to characterize policies at reduced experimenter effort in both a simulated manipulation task and a physical robot vision-and-language navigation task.

**Significance:**
The authors encourage the use of contrast set evaluations as a more informative alternative to small scale, i.i.d. demonstrations on physical robots, and as a scalable alternative to industry-scale real world evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f2a0827-f4eb-4cb0-9790-497559e42cc2",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "6fcd6717-0726-47d9-a50e-ce55ea3fc86d",
  "sourceToolAssistantUUID": "3f2a0827-f4eb-4cb0-9790-497559e42cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-18T20:04:26.073Z_

<details><summary>↩ Tool result · `toolu_016tFAEiLiDvEdv7ug7xP6Ns`</summary>

```text
Web search results for query: ""instruction blindness" VLA visual dominance language token overwhelm 2025 2026"

Links: [{"title":"Stable Language Guidance for Vision–Language–Action Models","url":"https://arxiv.org/html/2601.04052v2"},{"title":"Visual-Linguistic Agents (VLA)","url":"https://www.emergentmind.com/topics/visual-linguistic-agent-vla"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models","url":"https://arxiv.org/html/2604.03956v2"},{"title":"Unified Vision-Language-Action Tokenization","url":"https://www.emergentmind.com/topics/unified-vision-language-action-vla-tokenization"}]

Based on the search results, I found relevant information about "instruction blindness" in Vision-Language-Action (VLA) models:

## Key Findings

Recent audits on the Libero-Plus and Libero-Pro benchmarks reveal that VLA agents frequently suffer from "instruction blindness" or rote execution, as dense high-frequency visual signals tend to overwhelm sparse linguistic tokens.

Models frequently ignore language inputs entirely, defaulting to the most probable action given the scene alone.

When language is processed, models exhibit an overdependence on rote pattern execution rather than true semantic interpretation, leading to catastrophic failure when instructions deviate from training templates.

## Related Research

Additional evidence of this problem comes from other studies: VLA models trained on goal-driven datasets often learn a vision-only policy rather than a true language-conditioned policy. One experiment found that a vision-only model achieved a success rate of 44.6%, which is close to the language-conditioned baseline of 47.8%, demonstrating that language instructions may not be contributing meaningfully to model performance.

The research indicates that balancing multi-modal inputs remains a critical challenge in VLA development, with the visual tokens dominating over language tokens in practice despite architectural intentions for true language conditioning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a580246-4160-4f77-94a4-b63b242af658",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "e2e1513d-0536-4580-a47b-5efb17ace3a3",
  "sourceToolAssistantUUID": "8a580246-4160-4f77-94a4-b63b242af658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-18T20:04:31.573Z_

<details><summary>↩ Tool result · `toolu_01FPehGykk4CAubVRuGv9oGq`</summary>

```text
Web search results for query: "ReWiND language-guided rewards robot policy instruction augmentation paraphrase consistency 2025"

Links: [{"title":"ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/rewind-language-guided-rewards-teach-robot-policies"},{"title":"ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://arxiv.org/pdf/2505.10911"},{"title":"ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://proceedings.mlr.press/v305/zhang25a.html"},{"title":"ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://rewind-reward.github.io/"},{"title":"(PDF) ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://www.researchgate.net/publication/391857027_ReWiND_Language-Guided_Rewards_Teach_Robot_Policies_without_New_Demonstrations"},{"title":"[2505.10911] ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://arxiv.org/abs/2505.10911"},{"title":"Teaching robot policies without new demonstrations: interview with Jiahui Zhang and Jesse Zhang - Robohub","url":"https://robohub.org/teaching-robot-policies-without-new-demonstrations-interview-with-jiahui-zhang-and-jesse-zhang/"},{"title":"ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://liralab.usc.edu/pdfs/publications/zhang2025rewind.pdf"},{"title":"ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations","url":"https://arxiv.org/html/2505.10911v2"}]

I found comprehensive information about ReWiND. Here's what the search revealed:

## Overview

ReWiND is a framework for learning robot manipulation tasks solely from language instructions without per-task demonstrations. Instead of showing the robot exactly what to do, ReWiND uses natural language to explain the goal.

## Core Approach

ReWiND starts from a small demonstration dataset to learn: (1) a data-efficient, language-conditioned reward function that labels the dataset with rewards, and (2) a language-conditioned policy pre-trained with offline RL using these rewards. Given an unseen task variation, ReWiND fine-tunes the pre-trained policy using the learned reward function, requiring minimal online interaction.

## Key Technical Components

The system introduces video rewinding to automatically generate failure trajectories from successful demos, allowing ReWiND to provide dense feedback even when the policy is making mistakes. Additionally, when training the reward function, any time an observation sequence is sampled, its instruction is uniformly randomly sampled from all available matching instructions, generated or original. This instruction augmentation helps with robustness to diverse task instructions.

## Performance Results

Comprehensive success rate evaluations on Metaworld manipulation tasks and a real-world bimanual robot setup demonstrate ReWiND beats baselines by 2x in simulation and improves real-world pre-trained policies by 5x.

## Publication

The paper was published in Proceedings of The 9th Conference on Robot Learning, PMLR 305:460-488, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb3d03d8-f82c-403c-8ac2-c6475b0f3aaf",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "98c5df6d-1913-468c-869b-735ee7b143ec",
  "sourceToolAssistantUUID": "cb3d03d8-f82c-403c-8ac2-c6475b0f3aaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 90 · 2026-05-18T20:04:34.793Z_

This is extremely important. The "Stable Language Guidance" (RSS) paper is a significant threat. Let me get the final details on it and the LangForce paper, which also looked relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98c5df6d-1913-468c-869b-735ee7b143ec",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdj3sn4GNdpYwCTj5oZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e2e78ca-d41e-499e-a3d2-215d8a3a5b27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VziY9s8ceiqChKtL2jDekS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 552,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 36536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2461,
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

_source line 91 · 2026-05-18T20:04:35.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TWL2LbSzGXZcjn1vy8RCJf`</summary>

```json
{
  "query": "RSS \"Residual Semantic Steering\" \"Monte Carlo Syntactic Integration\" LLM distributional expansion affordance invariance paraphrase VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e2e78ca-d41e-499e-a3d2-215d8a3a5b27",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdj3sn4GNdpYwCTj5oZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d51f7211-c3d5-4c10-8e29-8089a4f03be0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VziY9s8ceiqChKtL2jDekS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 552,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 36536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2461,
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

_source line 92 · 2026-05-18T20:04:36.214Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UfMF5wgdSB9D6SyTsJ7ixB`</summary>

```json
{
  "query": "LangForce Bayesian decomposition vision language affordance 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d51f7211-c3d5-4c10-8e29-8089a4f03be0",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdj3sn4GNdpYwCTj5oZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1502cc8e-ac9f-4f1f-b970-53b1a29e5d6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VziY9s8ceiqChKtL2jDekS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 552,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 36536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2461,
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

_source line 93 · 2026-05-18T20:04:36.782Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L8czZYe7cmUugJSgwebwR6`</summary>

```json
{
  "query": "\"EF-VLA\" compositional manipulation pretrained representation preservation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1502cc8e-ac9f-4f1f-b970-53b1a29e5d6d",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdj3sn4GNdpYwCTj5oZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23b76d4f-6d95-4d59-a7e6-569ebb6c0e22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VziY9s8ceiqChKtL2jDekS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 552,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 36536,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2461
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 552,
          "output_tokens": 229,
          "cache_read_input_tokens": 36536,
          "cache_creation_input_tokens": 2461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2461,
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

_source line 94 · 2026-05-18T20:04:42.501Z_

<details><summary>↩ Tool result · `toolu_01L8czZYe7cmUugJSgwebwR6`</summary>

```text
Web search results for query: ""EF-VLA" compositional manipulation pretrained representation preservation 2025"

Links: [{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/pdf/2509.11417"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization","url":"https://arxiv.org/pdf/2510.25616"},{"title":"Preserving Multi-Modal Capabilities of Pre-trained VLMs for Improving   Vision-Linguistic Compositionality","url":"https://arxiv.org/pdf/2410.05210"}]

Based on the search results, I found relevant information about EF-VLA:

EF-VLA is a model presented by Huang et al. at the International Conference on Learning Representations (ICLR 2025), which exemplifies the Early Fusion approach by retaining the representational alignment established by CLIP. 

EF-VLA accepts image-text pairs, encodes them with CLIP's frozen encoders, and fuses the resulting embeddings early in the transformer backbone prior to action prediction. This design ensures that the semantic consistency learned during CLIP pretraining is preserved, reducing overfitting and enhancing generalization.

In terms of performance, EF-VLA demonstrated a 20% performance improvement on compositional manipulation tasks and reached 85% success on previously unseen goal descriptions. Additionally, by keeping the vision-language backbone frozen, this approach preserves computational efficiency and avoids catastrophic forgetting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23b76d4f-6d95-4d59-a7e6-569ebb6c0e22",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "c9936727-dcf3-497c-b4d1-d5a604b250a2",
  "sourceToolAssistantUUID": "23b76d4f-6d95-4d59-a7e6-569ebb6c0e22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-18T20:04:43.437Z_

<details><summary>↩ Tool result · `toolu_01TWL2LbSzGXZcjn1vy8RCJf`</summary>

```text
Web search results for query: "RSS "Residual Semantic Steering" "Monte Carlo Syntactic Integration" LLM distributional expansion affordance invariance paraphrase VLA"

Links: [{"title":"Stable Language Guidance for Vision–Language–Action Models","url":"https://arxiv.org/html/2601.04052v1"},{"title":"Stable Language Guidance for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2601.04052"},{"title":"Sequential Monte Carlo Steering of Large Language Models using   Probabilistic Programs","url":"https://arxiv.org/pdf/2306.03081"},{"title":"Causality $\\neq$ Invariance: Function and Concept Vectors in LLMs","url":"https://arxiv.org/pdf/2602.22424"},{"title":"LLM-Guided Task- and Affordance-Level Exploration in Reinforcement Learning","url":"https://arxiv.org/pdf/2509.16615"},{"title":"[2504.13139] Syntactic and Semantic Control of Large Language Models via Sequential Monte Carlo","url":"https://arxiv.org/abs/2504.13139"}]

I found highly relevant results! The search query matches a recent research paper on Vision-Language-Action (VLA) models. Here's what I found:

## Primary Result: Residual Semantic Steering (RSS)

Residual Semantic Steering (RSS) is a probabilistic framework that disentangles physical affordance from semantic execution. RSS introduces two theoretical innovations: (1) Monte Carlo Syntactic Integration, which approximates the true semantic posterior via dense, LLM-driven distributional expansion, and (2) Residual Affordance Steering, a dual-stream decoding mechanism that explicitly isolates the causal influence of language by subtracting the visual affordance prior.

## Key Components:

**Monte Carlo Syntactic Integration:** This component utilizes an Oracle Teacher to generate a dense linguistic neighborhood around a seed instruction, and optimizing over this distribution forces the policy to learn representations that are invariant to syntactic perturbations.

**Residual Affordance Steering:** This mitigates visual prior dominance by subtracting the unconditioned "visual instinct" (Base Affordance) from the standard prediction to isolate and amplify the residual semantic signal, ensuring the policy follows the specific user intent rather than generic visual attractors.

## Performance:

Empirical results across diverse manipulation benchmarks demonstrate that RSS achieves state-of-the-art robustness, maintaining performance even under adversarial linguistic perturbations.

The paper was published on January 7, 2026, and addresses robustness challenges in Vision-Language-Action models used for robotic manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d51f7211-c3d5-4c10-8e29-8089a4f03be0",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "73b52833-5f15-47eb-ab6e-2c3a06418c9d",
  "sourceToolAssistantUUID": "d51f7211-c3d5-4c10-8e29-8089a4f03be0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-18T20:04:43.514Z_

<details><summary>↩ Tool result · `toolu_01UfMF5wgdSB9D6SyTsJ7ixB`</summary>

```text
Web search results for query: "LangForce Bayesian decomposition vision language affordance 2026"

Links: [{"title":"GitHub - ZGC-EmbodyAI/LangForce · GitHub","url":"https://github.com/ZGC-EmbodyAI/LangForce"},{"title":"[2601.15197] LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://arxiv.org/abs/2601.15197"},{"title":"GitHub - ZGC-EmbodyAI/BayesianVLA","url":"https://github.com/ZGC-EmbodyAI/BayesianVLA"},{"title":"LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://arxiv.org/html/2601.15197"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Paper page - BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://huggingface.co/papers/2601.15197"},{"title":"[2601.15197v1] BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://arxiv.org/abs/2601.15197v1"}]

Based on the search results, here's what I found about LangForce:

## Overview

LangForce is a novel framework that enforces instruction following via Bayesian decomposition. It addresses a significant challenge in Vision-Language-Action (VLA) models used for robot manipulation.

## The Problem

The research identifies a critical pathology where goal-driven data collection creates a dataset bias, in which language instructions are highly predictable from visual observations alone, causing the conditional mutual information between instructions and actions to vanish—a phenomenon termed "Information Collapse." This causes models to degenerate into vision-only policies that ignore language constraints and fail in out-of-distribution settings.

## The Solution

By introducing learnable Latent Action Queries, the framework constructs a dual-branch architecture to estimate both a vision-only prior and a language-conditioned posterior. The policy is optimized to maximize the conditional Pointwise Mutual Information between actions and instructions, which effectively penalizes the vision shortcut and rewards actions that explicitly explain the language command.

## Key Features

Without requiring new data, LangForce significantly improves generalization. Notably, LangForce enables single-stage, end-to-end training (unlike some comparable approaches that require multi-stage training).

The paper was published on arXiv in January 2026 with contributions from authors including Shijie Lian, Bin Yu, and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1502cc8e-ac9f-4f1f-b970-53b1a29e5d6d",
  "isSidechain": true,
  "promptId": "368a6d71-f752-4551-b4e1-f266f043f883",
  "agentId": "ae1282733b41002fe",
  "type": "user",
  "uuid": "3e995153-0d22-4abf-aa50-5c0ed3e06eb0",
  "sourceToolAssistantUUID": "1502cc8e-ac9f-4f1f-b970-53b1a29e5d6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 97 · 2026-05-18T20:06:17.688Z_

Now I have a comprehensive picture. Let me compile my findings into a thorough report.

---

Here is a thorough analysis of competing and overlapping work, organized by search query, with novelty threat assessments.

---

## SEARCH 1: "paraphrase invariance" + "affordance" or "robot manipulation"

**Query:** `"paraphrase invariance" affordance robot manipulation`

**Key results:** No paper uses the exact term "paraphrase invariance" in the context of affordance learning for robot manipulation. The closest results were about SE(3) equivariance (spatial invariance) and general affordance-centric policy learning.

**Novelty threat: LOW for exact terminology, but see Searches 6-8 below for closely related concepts.**

---

## SEARCH 2: "instruction invariance" + "robot" or "manipulation"

**Query:** `"instruction invariance" robot manipulation self-supervision`

**Key results:** No direct match on the exact phrase. Results included LaVA-Man (self-supervised visual-action representations), self-supervised keypoint learning, and learning from imperfect demonstrations. None use instruction invariance as a self-supervisory signal for affordance.

**Novelty threat: LOW for this specific framing.**

---

## SEARCH 3: "self-supervised affordance" + "VLA" or "vision language action"

**Query:** `"self-supervised affordance" VLA "vision language action"`

**Key results -- HIGH RELEVANCE:**

- **CoA-VLA** (ICCV 2025, arxiv 2412.20451): Incorporates chain-of-affordance reasoning (object, grasp, spatial, movement affordances) into VLAs via visual and textual prompting. NOT self-supervised -- uses structured annotation. Does not use paraphrase invariance.
- **UAD -- Unsupervised Affordance Distillation** (ICRA 2025, arxiv 2506.09284): Distills affordance from foundation models (DINOv2 + VLMs) into a lightweight task-conditioned decoder **without manual annotations**. Trains on rendered objects in simulation, generalizes to real-world scenes **and to variations in task instructions**. This is the closest competitor -- it achieves annotation-free affordance learning conditioned on language.
- **LITEN** (Oct 2025, arxiv 2510.19752): Learns affordances at inference-time by iterating between planning and assessment phases. No training-time self-supervision from paraphrases.

**Novelty threat: MODERATE-HIGH.** UAD achieves unsupervised, language-conditioned affordance prediction with instruction variation robustness, which is a major overlap with the proposed idea's goals. However, UAD's mechanism is **distillation from foundation models** (automatically generating affordance labels via VLMs), NOT self-supervision via paraphrase consistency. The supervision signal is fundamentally different.

---

## SEARCH 4: "consistency regularization" + "affordance" + "robot"

**Query:** `"consistency regularization" affordance robot manipulation`

**Key results:** RoboPCA (March 2026), RT-Affordance (Nov 2024, Google DeepMind), Robo-ABC, EqvAfford. None of these use consistency regularization as a training mechanism for affordance. RT-Affordance uses affordances as intermediate representations between language and policy but does not enforce any consistency across instruction variants.

**Novelty threat: LOW for the specific consistency regularization mechanism.**

---

## SEARCH 5: "language grounding consistency" + "manipulation"

**Query:** `"language grounding consistency" manipulation robot`

**Key results:**

- **RoboGround** (April 2025, arxiv 2504.21530): Uses grounding masks from VLMs as intermediate representations for policy learning. Tests across diverse instructions but does not enforce consistency between paraphrases.
- **LaDA** (March 2026): Language-grounded decoupled action representation using language as a semantic bridge.
- **STEER** (Nov 2024): Dense language grounding for flexible manipulation using natural language skill specifications. Can compose skills without new data collection, steered by VLMs.

**Novelty threat: LOW-MODERATE.** These papers ground language in visual/action space but do not use consistency across paraphrases as a self-supervisory training signal.

---

## SEARCH 6: "open vocabulary affordance" + "end-to-end" + "VLA" 2025/2026

**Query:** `"open vocabulary affordance" end-to-end VLA 2025 2026`

**Key results:**

- **OVAL-Prompt** (ICRA 2024 Workshop): Open-vocabulary affordance localization using VLM part segmentation + LLM affordance grounding. No finetuning required. Competitive with supervised baselines.
- **3D-AffordanceLLM** (2025): Open-vocabulary affordance detection in 3D using LLMs.

**Novelty threat: MODERATE.** These demonstrate that open-vocabulary affordance is achievable without annotations by leveraging foundation models. However, they are **not** end-to-end within a VLA (they are separate modules), and they do not use paraphrase invariance. The proposed idea could still differentiate by being truly end-to-end within a VLA and using a novel self-supervised training signal.

---

## SEARCH 7: Most recent affordance + VLA papers (2025-2026)

**Query:** `arxiv affordance VLA robot 2025 2026`

**Key results -- CRITICAL FINDINGS:**

- **Affordance Field Intervention (AFI)** (CVPR 2026, arxiv 2512.07472): Uses Spatial Affordance Fields as a plug-in to rescue VLAs from "memory traps." Not about training but about inference-time intervention. Does not use paraphrase consistency.
- **Green-VLA** (Feb 2026): Five-stage curriculum including affordance prior capture. Uses VQA for affordance learning. Not self-supervised via paraphrases.
- **VLA-Thinker** (March 2026): Boosts VLA reasoning but affordance is not the core contribution.

**Novelty threat: LOW-MODERATE.** These are adjacent but mechanistically different from the proposed approach.

---

## SEARCH 8: arXiv affordance + VLA, last 6 months

This query surfaced the same papers as Search 7, plus **Contrastive Representation Regularization (RS-CL)** (Oct 2025, arxiv 2510.01711), which applies contrastive loss to align VLA representations with robot proprioceptive states. This is a consistency/contrastive mechanism in VLAs but targets proprioceptive alignment, not language-affordance consistency.

**Novelty threat: LOW for the specific idea, though it demonstrates that contrastive regularization within VLAs is an active research pattern.**

---

## SEARCH 9: "contrastive affordance learning language" 2025/2026

**Query:** `"contrastive affordance learning" language robot 2025 2026`

**Key results:**

- **CLASP** (2023): Contrastive Language, Action, and State Pretraining -- unifies language, action, and state in a shared embedding space. Extends CLIP to behavior-text alignment.
- **PRTS**: Uses contrastive RL to learn a unified embedding where language instructions serve as goals.

**Novelty threat: MODERATE.** CLASP and PRTS demonstrate contrastive learning linking language and robot behavior, but they do not learn affordance maps/regions specifically, and they do not use paraphrase consistency as the self-supervisory signal.

---

## SEARCH 10: "instruction augmentation robot policy" self-supervised 2025/2026

**Query:** `"instruction augmentation" robot policy self-supervised 2025 2026`

**Key results:**

- **DIAL** (2022, Google): Uses CLIP to semi-supervisedly label robot demonstrations with language, then trains language-conditioned policies. Uses contrastive fine-tuning of VLMs on robot data. Important precedent for using VLMs to bridge language and robot behavior without full annotation.
- **Object-Centric Instruction Augmentation** (2024): Augments instructions with object location information using MLLMs.
- **ReWiND** (CoRL 2025): Creates multiple language instructions per task (e.g., "close the door" and "shut the door") and uses instruction augmentation for reward model robustness. Demonstrates near-zero variance across paraphrased instructions.

**Novelty threat: MODERATE.** ReWiND explicitly uses paraphrased instructions for robustness, though in a reward model context rather than for affordance learning. DIAL shows VLMs can bridge language-affordance gaps semi-supervisedly.

---

## CRITICAL ADDITIONAL FINDINGS FROM FOLLOW-UP SEARCHES

### **INTRA (ECCV 2024)** -- **HIGH THREAT**
**Paper:** "INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding" (arxiv 2409.06210)

This paper uses **text synonym augmentation** combined with **contrastive learning** and **text-conditioned affordance map generation** using VLM embeddings. It specifically augments text with synonyms to make affordance grounding robust to language variations. The affordance maps are conditioned on text input, and synonym augmentation ensures invariance to phrasing. This is weakly supervised (exocentric images only, no paired datasets).

**Overlap with proposed idea:** INTRA uses text synonym augmentation for robustness in affordance grounding -- a conceptual ancestor of paraphrase invariance for affordance learning. However, INTRA operates on static images (not robot manipulation scenes), does not operate within a VLA, and uses augmentation for robustness rather than as a primary self-supervisory signal.

### **Stable Language Guidance / RSS (January 2026)** -- **HIGHEST THREAT**
**Paper:** "Stable Language Guidance for Vision-Language-Action Models" (arxiv 2601.04052)

This paper identifies "instruction blindness" in VLAs and proposes Residual Semantic Steering (RSS), which:
1. Uses **Monte Carlo Syntactic Integration** -- an LLM generates a **dense linguistic neighborhood** of paraphrases around a seed instruction
2. Optimizes an **Expected Semantic Loss over this expanded distribution**, forcing the policy to learn representations that are **invariant to syntactic perturbations**
3. Uses **Residual Affordance Steering** that explicitly separates visual affordance from semantic intent

**This is extremely close to the proposed idea.** RSS generates paraphrases of instructions using an LLM, trains the policy to be invariant across these paraphrases, and explicitly disentangles affordance from language. The key differences are: (a) RSS targets the full policy output (actions), not specifically affordance region activation in visual features; (b) RSS uses the invariance for robustness to "instruction blindness," not specifically to self-supervise an affordance decoder; (c) RSS subtracts visual affordance as a prior rather than learning affordance maps. But the core mechanism -- paraphrase-based invariance training in VLAs -- substantially overlaps.

### **LangForce / BayesianVLA (January 2026)** -- **MODERATE-HIGH THREAT**
**Paper:** "LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries" (arxiv 2601.15197)

LangForce addresses the same "information collapse" / "instruction blindness" problem. It constructs a dual-branch architecture estimating a vision-only prior and a language-conditioned posterior, optimizing conditional Pointwise Mutual Information between actions and instructions. This effectively penalizes the "vision shortcut" and rewards actions that explicitly depend on language.

**Overlap:** LangForce decomposes visual affordance from language conditioning -- similar in spirit to the proposed idea -- but uses Bayesian decomposition rather than paraphrase invariance.

### **HULC++ (ICRA 2023)** -- **MODERATE THREAT**
**Paper:** "Grounding Language with Visual Affordances over Unstructured Data" (arxiv 2210.01911)

Uses a **self-supervised visuo-lingual affordance model** with an encoder-decoder architecture that predicts pixel-level affordance distributions conditioned on language instructions. Requires only 1% of data to be language-annotated.

**Overlap:** Self-supervised affordance prediction conditioned on language for robot manipulation. However, it does not use paraphrase invariance -- its self-supervision comes from play data structure, not from instruction consistency.

---

## OVERALL NOVELTY ASSESSMENT

**The proposed idea has several genuinely novel elements but faces significant prior art pressure:**

**What IS novel:**
1. Using paraphrase invariance **specifically as a self-supervisory signal to train an affordance decoder** within a VLA -- no paper does exactly this
2. The specific mechanism of enforcing that different paraphrases activate the **same affordance regions in visual features** -- this spatial consistency constraint on visual feature maps is distinctive
3. Integrating this as an end-to-end module within a VLA (most affordance work is separate from VLAs)

**What is NOT novel (and must be carefully differentiated):**
1. **RSS / Stable Language Guidance (Jan 2026)** already uses LLM-generated paraphrase distributions to train VLAs for syntactic invariance, and explicitly disentangles affordance from language. This is the single biggest threat to novelty claims.
2. **INTRA (ECCV 2024)** uses text synonym augmentation for robust affordance grounding with contrastive learning.
3. **UAD (ICRA 2025)** achieves unsupervised, task-conditioned affordance prediction that generalizes across instruction variations.
4. **LangForce (Jan 2026)** decomposes vision-affordance from language conditioning in VLAs.
5. **HULC++ (ICRA 2023)** demonstrated self-supervised visuo-lingual affordance models.

**Recommendations:**
- The paper MUST cite and clearly differentiate from RSS (arxiv 2601.04052) -- this is the single most important related work. The differentiation should emphasize that your approach targets **spatial affordance region activation** in visual features (a structured intermediate representation), whereas RSS targets invariance at the action output level.
- Cite INTRA for synonym augmentation in affordance grounding and differentiate by VLA integration and self-supervision mechanism.
- Cite UAD for annotation-free affordance and differentiate by not requiring foundation model distillation.
- The "instruction blindness" problem (documented by RSS and LangForce) is actually **motivation** for your work -- frame it as addressing the same problem from the affordance learning angle.

Sources:
- [CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance](https://arxiv.org/abs/2412.20451)
- [UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation](https://arxiv.org/abs/2506.09284)
- [LITEN: Learning Affordances at Inference-Time for Vision-Language-Action Models](https://arxiv.org/abs/2510.19752)
- [Stable Language Guidance for Vision-Language-Action Models (RSS)](https://arxiv.org/abs/2601.04052)
- [LangForce: Bayesian Decomposition of Vision Language Action Models](https://arxiv.org/abs/2601.15197)
- [INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding](https://arxiv.org/abs/2409.06210)
- [RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation](https://arxiv.org/abs/2411.02704)
- [OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation](https://arxiv.org/abs/2404.11000)
- [Affordance Field Intervention: Enabling VLAs to Escape Memory Traps](https://arxiv.org/abs/2512.07472)
- [RoboGround: Robotic Manipulation with Grounded Vision-Language Priors](https://arxiv.org/abs/2504.21530)
- [Grounding Language with Visual Affordances over Unstructured Data (HULC++)](https://arxiv.org/abs/2210.01911)
- [DIAL: Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models](https://arxiv.org/abs/2211.11736)
- [Contrastive Representation Regularization for Vision-Language-Action Models](https://arxiv.org/abs/2510.01711)
- [STEER: Flexible Robotic Manipulation via Dense Language Grounding](https://arxiv.org/abs/2411.03409)
- [Contrast Sets for Evaluating Language-Guided Robot Policies](https://arxiv.org/abs/2406.13636)
- [ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations](https://arxiv.org/abs/2505.10911)
- [Invariance Co-training for Robot Visual Generalization](https://arxiv.org/abs/2512.05230)
- [RoboPCA: Pose-centered Affordance Learning from Human Demonstrations](https://arxiv.org/abs/2603.07691)
- [Green-VLA: Staged Vision-Language-Action Model for Generalist Robots](https://arxiv.org/abs/2602.00919)
- [CLASP: Contrastive Language, Action, and State Pre-training for Robot Learning](https://arxiv.org/abs/2304.10782)
- [Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations (EF-VLA)](https://arxiv.org/abs/2509.11417)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e995153-0d22-4abf-aa50-5c0ed3e06eb0",
  "isSidechain": true,
  "agentId": "ae1282733b41002fe",
  "requestId": "req_011CbAdjvw6D6nv72NBYcHU5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a9ab352-7bb3-4479-a4cd-fdaa2091c519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "96432cf7-4cdd-402b-a592-c3a1ae9f4f87",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GgpqjZD8xdRux5RYdduHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 541,
      "cache_creation_input_tokens": 2280,
      "cache_read_input_tokens": 38997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2280,
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
