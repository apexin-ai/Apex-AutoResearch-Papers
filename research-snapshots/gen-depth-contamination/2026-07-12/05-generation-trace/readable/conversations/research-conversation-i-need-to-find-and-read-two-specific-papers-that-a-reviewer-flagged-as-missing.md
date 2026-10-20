# Research conversation: I need to find and read two specific papers that a reviewer flagged as missing related work: 1. "Dreaming the Unseen: Wo

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2db14817da9e1d4a.jsonl`
- **Structured JSON:** [`dda6cd7b400d2c91a7c5.json`](../../sessions/dd/dda6cd7b400d2c91a7c5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-10T20:18:59.215Z_

I need to find and read two specific papers that a reviewer flagged as missing related work:

1. "Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness" (DDP) - arXiv 2603.21017 (March 2026). Claims to achieve 73.8% OOD success on MetaWorld and 83.3% under severe real-world spatial shifts.

2. "Visual-Geometry Diffusion Policy" (VGDP) - arXiv 2511.22445 (November 2025). Claims 15.2% improvement in spatial perturbation settings via complementarity-aware multimodal fusion.

For each paper, please:
- Use WebSearch to find it
- Use WebFetch to read the abstract and method description
- Report: what problem they solve, their approach, key results, and how they relate to "test-time inference methods for geometric robustness of diffusion policies"

Also search for: "test-time augmentation diffusion policy robot" and "velocity field flow matching robot manipulation robustness" to find any other recent related work I might be missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "20e29db1-50d2-441f-b602-e693dc7eec01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:18:59.220Z_

```json
{
  "parentUuid": "20e29db1-50d2-441f-b602-e693dc7eec01",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
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
  "uuid": "66d23f90-8e0c-4f19-b4ff-76984b07ed42",
  "timestamp": "2026-05-10T20:18:59.220Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T20:19:03.964Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01V2rZbEEKuBeryjFiCqwp1B`</summary>

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
  "parentUuid": "66d23f90-8e0c-4f19-b4ff-76984b07ed42",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWMgXRksozSJu7auVAc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c7d10c2-f007-4f6a-8bb4-deb8186367f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StXxDQM3RuJKXB7vSHcczM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9036,
      "cache_read_input_tokens": 0,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9036
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9036,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-10T20:19:03.969Z_

<details><summary>↩ Tool result · `toolu_01V2rZbEEKuBeryjFiCqwp1B`</summary>

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
  "parentUuid": "5c7d10c2-f007-4f6a-8bb4-deb8186367f0",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "480b284c-19ae-4f5d-a978-d1c696e36339",
  "sourceToolAssistantUUID": "5c7d10c2-f007-4f6a-8bb4-deb8186367f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T20:19:07.786Z_

Now let me search for both papers and the additional topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "480b284c-19ae-4f5d-a978-d1c696e36339",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWN39f9H6ck9Dn8peXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb1e2d81-ab1e-428c-87ea-e3e1f8b6aede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KKQeaNyWQ6gTqcHj1bF9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T20:19:08.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014q7n3ehYtpWEoY9fNZGgph`</summary>

```json
{
  "query": "arXiv 2603.21017 \"Dreaming the Unseen\" world model diffusion policy out-of-distribution robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb1e2d81-ab1e-428c-87ea-e3e1f8b6aede",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWN39f9H6ck9Dn8peXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "824262fc-c3d1-4cef-ba03-73328f72c598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KKQeaNyWQ6gTqcHj1bF9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T20:19:08.939Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016mrYbJGqAFamzPxF3Q2zAB`</summary>

```json
{
  "query": "arXiv 2511.22445 \"Visual-Geometry Diffusion Policy\" VGDP multimodal fusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "824262fc-c3d1-4cef-ba03-73328f72c598",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWN39f9H6ck9Dn8peXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ec5b9c3-f826-4d04-8cf0-0ff14e974b79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KKQeaNyWQ6gTqcHj1bF9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T20:19:09.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N6vWsDXeQghCqDh4oSneca`</summary>

```json
{
  "query": "test-time augmentation diffusion policy robot manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ec5b9c3-f826-4d04-8cf0-0ff14e974b79",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWN39f9H6ck9Dn8peXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c8653ca-f5b7-4372-ac45-d6677a1018df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KKQeaNyWQ6gTqcHj1bF9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T20:19:09.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ubma4gnHc5sWXY28iLKg7j`</summary>

```json
{
  "query": "velocity field flow matching robot manipulation robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c8653ca-f5b7-4372-ac45-d6677a1018df",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWN39f9H6ck9Dn8peXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a6ecd36-859d-49e8-adff-278a0ab66882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KKQeaNyWQ6gTqcHj1bF9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T20:19:14.144Z_

<details><summary>↩ Tool result · `toolu_014q7n3ehYtpWEoY9fNZGgph`</summary>

```text
Web search results for query: "arXiv 2603.21017 "Dreaming the Unseen" world model diffusion policy out-of-distribution robustness"

Links: [{"title":"Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness","url":"https://arxiv.org/html/2603.21017v1"},{"title":"[2603.04715] Probabilistic Dreaming for World Models","url":"https://arxiv.org/abs/2603.04715"},{"title":"Probabilistic Dreaming for World Models","url":"https://arxiv.org/html/2603.04715v1"},{"title":"Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models","url":"https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"},{"title":"Dreaming of Many Worlds: Learning Contextual World Models Aids Zero-Shot Generalization","url":"https://arxiv.org/html/2403.10967v1"},{"title":"AdaWorldPolicy: World-Model-Driven Diffusion Policy with Online Adaptive Learning for Robotic Manipulation","url":"https://arxiv.org/html/2602.20057v1"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"[2312.08533] World Models via Policy-Guided Trajectory Diffusion","url":"https://arxiv.org/abs/2312.08533"},{"title":"[2604.26841] Language Diffusion Models are Associative Memories Capable of Retrieving Unseen Data","url":"https://arxiv.org/abs/2604.26841"},{"title":"(PDF) DreamWorld: Unified World Modeling in Video Generation","url":"https://www.researchgate.net/publication/401470991_DreamWorld_Unified_World_Modeling_in_Video_Generation"}]

I found the paper for you! Here's what I discovered about arXiv 2603.21017:

## "Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness"

The paper addresses how diffusion policies excel at visuomotor control but often fail catastrophically under severe out-of-distribution (OOD) disturbances, such as unexpected object displacements or visual corruptions.

**The Proposed Solution:**

The authors introduce the Dream Diffusion Policy (DDP), a framework that deeply integrates a diffusion world model into the policy's training objective via a shared 3D visual encoder. This co-optimization endows the policy with robust state-prediction capabilities, and when encountering sudden OOD anomalies during inference, DDP detects the real-imagination discrepancy and actively abandons the corrupted visual stream. Instead, it relies on its internal "imagination" to maintain performance.

The paper was published on March 22, 2026, and represents work from researchers at the Technical University of Munich and Nanjing University. You can access the full paper directly at https://arxiv.org/html/2603.21017v1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "824262fc-c3d1-4cef-ba03-73328f72c598",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "9e8c6623-509b-446d-8935-3c0d01368c67",
  "sourceToolAssistantUUID": "824262fc-c3d1-4cef-ba03-73328f72c598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T20:19:15.469Z_

<details><summary>↩ Tool result · `toolu_016mrYbJGqAFamzPxF3Q2zAB`</summary>

```text
Web search results for query: "arXiv 2511.22445 "Visual-Geometry Diffusion Policy" VGDP multimodal fusion"

Links: [{"title":"[2511.22445] Visual-Geometry Diffusion Policy: Robust Generalization via Complementarity-Aware Multimodal Fusion","url":"https://arxiv.org/abs/2511.22445"},{"title":"Visual-Geometry Diffusion Policy Robust Generalization via Complementarity-Aware Multimodal Fusion","url":"https://arxiv.org/html/2511.22445"},{"title":"Visual-Geometry Diffusion Policy: Robust Generalization ...","url":"https://arxiv.org/pdf/2511.22445"},{"title":"Visual-Geometry Diffusion Policy: Robust Generalization via Complementarity-Aware Multimodal Fusion | Request PDF","url":"https://www.researchgate.net/publication/398135918_Visual-Geometry_Diffusion_Policy_Robust_Generalization_via_Complementarity-Aware_Multimodal_Fusion"},{"title":"VO-DP: Semantic-Geometric Adaptive Diffusion Policy for Vision-Only Robotic Manipulation","url":"https://arxiv.org/html/2510.15530v1"},{"title":"GelFusion: Enhancing Robotic Manipulation under Visual Constraints via Visuotactile Fusion","url":"https://arxiv.org/html/2505.07455v1"},{"title":"Robotics Papers on X: \"Visual-Geometry Diffusion Policy: Robust Generalization via Complementarity-Aware Multimodal Fusion. https://t.co/1gDbjDJ8yW\" / X","url":"https://x.com/OWW/status/1995665749017248103"},{"title":"[2511.00859] Layer-Wise Modality Decomposition for Interpretable Multimodal Sensor Fusion","url":"https://arxiv.org/abs/2511.00859"},{"title":"[2511.21889] Exploring Fusion Strategies for Multimodal Vision-Language Systems","url":"https://arxiv.org/abs/2511.21889"},{"title":"Exploring Fusion Strategies for Multimodal Vision-Language Systems","url":"https://arxiv.org/html/2511.21889"}]

Based on the search results, I found the paper you're looking for. Here's what I found about arXiv 2511.22445:

## Visual-Geometry Diffusion Policy (VGDP)

The paper is titled "Visual-Geometry Diffusion Policy: Robust Generalization via Complementarity-Aware Multimodal Fusion" and was authored by Yikai Tang and 4 other authors.

### Overview

VGDP is a multimodal imitation learning framework built around a Complementarity-Aware Fusion Module where modality-wise dropout enforces balanced use of RGB and point-cloud cues, with cross-attention serving only as a lightweight interaction layer.

### Key Innovation

RGB and point-cloud features are first projected into a shared embedding space and then passed through a modality-dropout mechanism that randomly removes entire sensory streams during training, which forces the policy to learn modality-invariant and complementary structure.

### Performance Results

Across a benchmark of 18 simulated tasks and 4 real-world tasks, VGDP outperforms seven baseline policies with an average performance improvement of 39.1%, and demonstrates strong robustness under visual and spatial perturbations, surpassing baselines with an average improvement of 41.5% in different visual conditions and 15.2% in different spatial settings.

The paper was published on November 27, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ec5b9c3-f826-4d04-8cf0-0ff14e974b79",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "f9ad75b1-e1e3-4914-a042-f1c6a23676c2",
  "sourceToolAssistantUUID": "5ec5b9c3-f826-4d04-8cf0-0ff14e974b79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T20:19:17.794Z_

<details><summary>↩ Tool result · `toolu_01Ubma4gnHc5sWXY28iLKg7j`</summary>

```text
Web search results for query: "velocity field flow matching robot manipulation robustness 2025 2026"

Links: [{"title":"GitHub - zql-kk/FlowPolicy: [AAAI 2025 Oral] FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation · GitHub","url":"https://github.com/zql-kk/FlowPolicy"},{"title":"VFP: Variational Flow-Matching Policy for Multi-Modal Robot Manipulation","url":"https://arxiv.org/pdf/2508.01622"},{"title":"[Literature Review] FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation","url":"https://www.themoonlight.io/en/review/flowpolicy-enabling-fast-and-robust-3d-flow-based-policy-via-consistency-flow-matching-for-robot-manipulation"},{"title":"Published as a conference paper at ICLR 2026 FLOW MATCHING POLICY GRADIENTS","url":"https://openreview.net/pdf/376ea41422d8f63f58a4916b9a9783de90e8e461.pdf"},{"title":"ReinFlow: Fine-tuning Flow Matching Policy with Online ...","url":"https://nicsefc.ee.tsinghua.edu.cn//nics_file/pdf/09dbaac9-e1ab-4e18-abf2-99ec82476290.pdf"},{"title":"FLOW MATCHING POLICY GRADIENTS","url":"https://openreview.net/pdf/b709078b2a23b51e597b0480b3883259308c4a5b.pdf"},{"title":"FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/33617"},{"title":"Flow Matching Policy Gradients","url":"https://arxiv.org/html/2507.21053v2"},{"title":"FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation","url":"https://arxiv.org/html/2412.04987v2"},{"title":"[2412.04987] FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation","url":"https://arxiv.org/abs/2412.04987"}]

I've found several highly relevant papers and resources on velocity field flow matching for robot manipulation robustness. Here are the key findings:

## Recent Papers on Flow Matching for Robot Manipulation (2025-2026)

### FlowPolicy: Consistency Flow Matching (2025)

FlowPolicy is a novel framework for fast policy generation based on consistency flow matching and 3D vision that refines the flow dynamics by normalizing the self-consistency of the velocity field, enabling the model to derive task execution policies in a single inference step. This approach demonstrates a 7× increase in inference speed while maintaining competitive average success rates compared to state-of-the-art methods.

Consistency flow matching (Consistency-FM) can be trained to produce a robust flow model without the aid of distillation, which is valuable to robots performing unseen tasks, as it is difficult to find a robust teacher model in practical applications.

### Variational Flow Matching Policy (VFP)

Flow-matching policies can reduce sampling time to just 20% of that needed by diffusion models, making them highly attractive for time-sensitive applications. However, flow-matching policies often average over all demonstrated options, resulting in actions that do not correspond to any valid path, which leads to significant failures in imitation learning for manipulation tasks.

### Flow Matching Policy Gradients (ICLR 2026)

Flow Policy Optimization (FPO) is a policy gradient algorithm for optimizing flow-based generative models that reframes policy optimization as maximizing an advantage-weighted ratio computed from the conditional flow matching objective. FPO demonstrates robustness across tasks, enabling effective training of flow-based policies in high-dimensional domains.

### ReinFlow: Online RL Fine-tuning

ReinFlow is the first online reinforcement learning framework that stably fine-tunes a family of flow matching policies for continuous robotic control at arbitrarily few denoising steps, and surpasses existing methods that fine-tune diffusion or flow models using RL while reducing wall-clock time by 62.82%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a6ecd36-859d-49e8-adff-278a0ab66882",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "8118cd67-68c0-44cb-913e-4cb7bf1ae733",
  "sourceToolAssistantUUID": "3a6ecd36-859d-49e8-adff-278a0ab66882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T20:19:17.826Z_

<details><summary>↩ Tool result · `toolu_01N6vWsDXeQghCqDh4oSneca`</summary>

```text
Web search results for query: "test-time augmentation diffusion policy robot manipulation 2025 2026"

Links: [{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Diffusion Trajectory-guided Policy: A Novel Framework for Long-Horizon Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=VaoeAi5CW8"},{"title":"Learning force-conditioned visuomotor diffusion policy from human demonstrations for complex robotic assembly tasks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S221384632500207X"},{"title":"[2510.01068] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/abs/2510.01068"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11","url":"https://dl.acm.org/doi/10.1177/02783649241273668"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"},{"title":"[2506.09422] Time-Unified Diffusion Policy with Action Discrimination for Robotic Manipulation","url":"https://arxiv.org/abs/2506.09422"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising","url":"https://arxiv.org/pdf/2510.21991"}]

Based on the search results, here's what I found regarding test-time augmentation, diffusion policies, and robot manipulation in 2025-2026:

## Key Recent Work

Diffusion-based models for robotic control, including vision-language-action and vision-action policies, can be enhanced via test-time methods without additional model training. One approach establishes that the convex composition of distributional scores from multiple diffusion models can yield a superior objective compared to any individual score.

## Diffusion Policy Overview

Diffusion models have recently emerged as a promising approach in robotics, especially in robot manipulations. Diffusion Policy consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9% across 15 different tasks from 4 different robot manipulation benchmarks.

## Data Augmentation in Robot Manipulation

Many methodologies employ diffusion-based data augmentation in vision-based manipulation tasks to scale up datasets and reconstruct scenes. Additionally, recent work introduces data segmentation and augmentation methods to reduce the number of required demonstrations, enhancing the policy's robustness to task failures.

## Inference Efficiency

Common choices of noise levels are 50–100 during training, but only a subset of five to ten steps during inference. Still, only a few evaluations exist that compare DDPM-based, DDIM-based, or other samplers for robotic manipulation, and further investigation is required.

The search results indicate active research in test-time optimization methods for diffusion-based robot policies, with recent work focusing on composition techniques and efficiency improvements for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c8653ca-f5b7-4372-ac45-d6677a1018df",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "4b856f9f-1035-4023-9469-ace225b7adcd",
  "sourceToolAssistantUUID": "2c8653ca-f5b7-4372-ac45-d6677a1018df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T20:19:21.417Z_

Now let me fetch the full details from both papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b856f9f-1035-4023-9469-ace225b7adcd",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWP44WH7EibQrxEW5dj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16b25f46-911b-46b0-925f-28f254bf0669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KksSs3wDgGNjLBRPwJxRvs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1128,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 10924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T20:19:24.722Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JcYiRSgfCrsGb5reAwjB6K`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.21017v1",
  "prompt": "Extract the full abstract, the method/approach description (how DDP works - the world model regularization, 3D visual encoder, imagination mechanism, OOD detection), and the key quantitative results (especially MetaWorld OOD success rate of 73.8% and real-world spatial shift results of 83.3%). Also extract any details about how they handle geometric/spatial perturbations specifically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16b25f46-911b-46b0-925f-28f254bf0669",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWP44WH7EibQrxEW5dj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b130e0fe-6709-417c-83cc-c7391c70ba0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KksSs3wDgGNjLBRPwJxRvs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1128,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 10924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-10T20:19:26.664Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WasMRtJa5ohkBcjXez8B5w`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.22445",
  "prompt": "Extract the full abstract, the method/approach description (how VGDP works - the complementarity-aware fusion module, modality dropout, cross-attention, RGB and point-cloud fusion), and the key quantitative results (especially the 15.2% improvement in spatial perturbation settings and the 41.5% in visual conditions). Also extract details about how they handle geometric/spatial robustness specifically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b130e0fe-6709-417c-83cc-c7391c70ba0c",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWP44WH7EibQrxEW5dj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14ced800-d828-4fe3-a26f-69bfdf7a4e31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KksSs3wDgGNjLBRPwJxRvs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1128,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 10924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T20:19:28.294Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PQXj14LVCaSYziVPHmvpTB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.01068",
  "prompt": "Extract the full abstract and key method description. This paper is about composing policies at test-time for diffusion-based or flow-based robot policies via distribution-level composition. What problem does it solve, what is the approach, and what are the key results? Does it address geometric robustness or spatial perturbations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14ced800-d828-4fe3-a26f-69bfdf7a4e31",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWP44WH7EibQrxEW5dj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97b9651f-3769-439a-b81c-2b43c5d912d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KksSs3wDgGNjLBRPwJxRvs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1128,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 10924,
      "output_tokens": 468,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2988
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1128,
          "output_tokens": 468,
          "cache_read_input_tokens": 10924,
          "cache_creation_input_tokens": 2988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2988,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T20:19:33.651Z_

<details><summary>↩ Tool result · `toolu_01JcYiRSgfCrsGb5reAwjB6K`</summary>

```text
# Dream Diffusion Policy: Summary

## Abstract
The paper introduces DDP, a framework addressing catastrophic failures of diffusion policies under severe out-of-distribution (OOD) disturbances. When encountering visual corruption or unexpected object displacement, DDP "abandons the corrupted visual stream" and relies instead on "autoregressively forecasted latent dynamics" to maintain control. The system achieves 73.8% OOD success on MetaWorld (versus 23.9% without predictive imagination) and 83.3% under real-world spatial shifts (versus 3.3%).

## Method Overview

**Core Architecture:** DDP integrates three components through a unified 3D visual encoder:
- A diffusion policy for action generation
- A diffusion world model predicting future latent states
- A shared geometric representation processing point clouds and proprioception

**Training Approach:** The framework co-optimizes behavior cloning and world model objectives via a combined loss: "ℒ_total = ℒ_BC + λℒ_WM". The world model acts as a "geometric and dynamic regularizer" during training, embedding environmental physics into the shared representation.

**Inference Mechanism:** The system implements a three-stage OOD response:

1. **Detection:** Monitors "real-imagination discrepancy" (latent distance between actual observations and predicted states). When this metric exceeds a threshold, an OOD event is flagged.

2. **Imagination:** Rather than relying on corrupted visuals, the policy generates actions conditioned entirely on "previously predicted latent embedding[s]" while the world model autoregressively forecasts subsequent states.

3. **Recovery:** Once the displaced object settles, the system applies compensatory spatial corrections to realign with the environment, then re-evaluates whether to resume normal execution.

## Geometric Perturbation Handling

For spatial shifts, DDP employs direct pose estimation comparing current object positions against expected in-distribution states, computing "a single static spatial displacement" as an offset. This offset drives compensatory tracking actions. The system addresses perturbations through sequential subtask-based recovery rather than simultaneous global adjustments.

## Key Results

- **MetaWorld OOD:** 73.8% success (baseline with tracking: 23.9%)
- **Real-world spatial shifts:** 83.3% success (baseline: 3.3%)
- **Open-loop imagination stress test:** 76.7% real-world success rate without visual feedback post-initialization
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b130e0fe-6709-417c-83cc-c7391c70ba0c",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "3b2819b7-1428-49d0-a884-d710d54e2682",
  "sourceToolAssistantUUID": "b130e0fe-6709-417c-83cc-c7391c70ba0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T20:19:33.706Z_

<details><summary>↩ Tool result · `toolu_01PQXj14LVCaSYziVPHmvpTB`</summary>

```text
# Summary of "Compose Your Policies!"

## Problem Addressed
The paper tackles the challenge of enhancing robotic control policies without requiring additional costly data collection or model retraining. It focuses on improving diffusion-based and flow-based robot policies through a novel composition approach.

## Key Method: General Policy Composition (GPC)
GPC is a "training-free method that enhances performance by combining the distributional scores of multiple pre-trained policies via a convex combination and test-time search." The approach enables composition of heterogeneous policies (vision-action and vision-language-action models) regardless of underlying architecture or visual modalities.

## Theoretical Foundation
The authors establish theoretical guarantees showing that "the convex composition of distributional scores from multiple diffusion models can yield a superior one-step functional objective compared to any individual score." They use Grönwall-type bounds to demonstrate this improvement propagates through entire generation trajectories.

## Key Results
Experiments across Robomimic, PushT, and RoboTwin benchmarks plus real-world robot tasks demonstrate consistent performance improvements. Notably, composed policies can outperform either individual parent policy.

## Geometric Robustness
**No, this paper does not address geometric robustness or spatial perturbations.** It focuses exclusively on improving policy performance through score-level composition without modifying the policies' inherent robustness properties.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97b9651f-3769-439a-b81c-2b43c5d912d0",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "f89a06ac-e605-4200-990c-147dc028a577",
  "sourceToolAssistantUUID": "97b9651f-3769-439a-b81c-2b43c5d912d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T20:19:34.445Z_

<details><summary>↩ Tool result · `toolu_01WasMRtJa5ohkBcjXez8B5w`</summary>

```text
# Visual-Geometry Diffusion Policy: Summary

## Abstract

The paper proposes VGDP, a multimodal imitation learning framework designed to improve robustness and generalization in visuomotor tasks. The system combines RGB images and point clouds through a "Complementarity-Aware Fusion Module" featuring modality-wise dropout that enforces balanced use of both sensor modalities. Testing across 18 simulated and 4 real-world tasks, VGDP achieves an average 39.1% performance improvement over seven baseline policies.

## Method Overview

VGDP operates through three components:

**Perception:** Independent encoders process RGB (ResNet-18 producing 512-dim features), point clouds (DP3 yielding 64-dim features), and robot state through a lightweight MLP.

**Integration (Core Innovation):** The "Complementarity-Aware Fusion Module" implements modality dropout where "with probability p=0.2, the RGB or 3D branch is randomly disabled before fusion." This forces the policy to develop representations that work when either modality is unavailable. Features project into a shared 256-dimensional space, followed by bidirectional cross-attention with residual connections and element-wise dropout.

**Decision:** A diffusion policy head denoises actions conditioned on the fused representation.

## Key Quantitative Results

- **Spatial Generalization:** "average rise in the success rate of 15.2% in spatially randomized tasks"
- **Visual Robustness:** "average improvement of 41.5% in different visual conditions"
- **Stability:** Cross-randomization variance reduced to 2.53% versus 32.72% for competitors—approximately "11×" stability improvement
- **Out-of-Distribution Performance:** 55.3% higher mean success rate under severe randomization

## Geometric/Spatial Robustness Approach

The framework addresses spatial robustness by leveraging point cloud geometry. The FetchBottle real-world task demonstrates this through spatial generalization testing: policies trained on 30 grid locations transfer to 143 test positions. VGDP significantly outperforms point-cloud-only methods, which "fail dramatically" under noisy real-world depth conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14ced800-d828-4fe3-a26f-69bfdf7a4e31",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "313e438f-a698-4d01-bad2-dda9072e7336",
  "sourceToolAssistantUUID": "14ced800-d828-4fe3-a26f-69bfdf7a4e31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T20:19:37.397Z_

Now let me search for more specific related work on test-time inference for geometric robustness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "313e438f-a698-4d01-bad2-dda9072e7336",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWQH6riKTBoCR2YCEa5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f499c0c-61d7-4c3c-8d7b-689eed5bd93d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zwkVQXyZoSD3ykU8BHa8j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 2720,
      "cache_read_input_tokens": 13912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2720,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T20:19:38.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017cYcdPhf5ovzCVvyBiDipW`</summary>

```json
{
  "query": "\"test-time\" \"geometric\" OR \"spatial\" robustness diffusion policy manipulation 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f499c0c-61d7-4c3c-8d7b-689eed5bd93d",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWQH6riKTBoCR2YCEa5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9535ee1-7e42-4d67-9f7f-1eee3e87e5ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zwkVQXyZoSD3ykU8BHa8j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 2720,
      "cache_read_input_tokens": 13912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2720,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T20:19:38.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R5UEuBnS8xFe9xtJx3dhgP`</summary>

```json
{
  "query": "FlowPolicy consistency flow matching 3D robustness spatial generalization robot 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9535ee1-7e42-4d67-9f7f-1eee3e87e5ac",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWQH6riKTBoCR2YCEa5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53c9336f-9f15-4d18-9fe0-257d8dbe81e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zwkVQXyZoSD3ykU8BHa8j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 2720,
      "cache_read_input_tokens": 13912,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 337,
          "output_tokens": 154,
          "cache_read_input_tokens": 13912,
          "cache_creation_input_tokens": 2720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2720,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T20:19:45.335Z_

<details><summary>↩ Tool result · `toolu_017cYcdPhf5ovzCVvyBiDipW`</summary>

```text
Web search results for query: ""test-time" "geometric" OR "spatial" robustness diffusion policy manipulation 2025 2026 arXiv"

Links: [{"title":"NL2SpaTiaL: Generating Geometric Spatio-Temporal Logic Specifications from Natural Language for Manipulation Tasks","url":"https://arxiv.org/html/2512.13670"},{"title":"[2503.10743] Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation","url":"https://arxiv.org/abs/2503.10743"},{"title":"Spatial-Temporal Aware Visuomotor Diffusion Policy Learning","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_Spatial-Temporal_Aware_Visuomotor_Diffusion_Policy_Learning_ICCV_2025_paper.pdf"},{"title":"Diffusion Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2504.08438v1"},{"title":"Diffusion Policy Policy Optimization","url":"https://arxiv.org/html/2409.00588v3"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=3100&show=2000"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://arxiv.org/list/cs.CV/2025?skip=32225&show=1000"},{"title":"A Survey on Diffusion Policy for Robotic Manipulation","url":"https://www.techrxiv.org/users/908014/articles/1282755/master/file/data/TPAMI/TPAMI.pdf"},{"title":"Machine Learning Mar 2025","url":"https://www.arxiv.org/list/cs.LG/2025-03?skip=500&show=2000"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"}]

Based on the web search results, I found several relevant papers from arXiv related to diffusion policies and robotic manipulation in 2025 and 2026:

## Key Findings:

1. **"NL2SpaTiaL: Generating Geometric Spatio-Temporal Logic Specifications from Natural Language for Manipulation Tasks"** (December 2025)
   - This work simulates multiple short-horizon virtual rollouts at each inference step, with each rollout scored via SpaTiaL robustness to determine the executed action. The paper addresses geometric and spatial aspects of robotic manipulation.

2. **"Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation"** (March 2025, arXiv:2503.10743)
   - This paper proposes KStar Diffuser, which maintains a dynamic spatial-temporal graph according to physical bimanual joint motions at continuous timesteps.

3. **"Spatial-Temporal Aware Visuomotor Diffusion Policy Learning"** (ICCV 2025)
   - This paper from ICCV 2025 addresses spatial-temporal aspects of diffusion-based policy learning.

4. **"Diffusion Models for Robotic Manipulation: A Survey"** (April 2025, arXiv:2504.08438)
   - A comprehensive survey covering diffusion models in robotic manipulation, including discussion of robustness and geometric representations.

These papers focus on spatial and geometric properties of diffusion-based policies for robotic manipulation, though the search results don't specifically highlight papers focused on "test-time" robustness or adversarial manipulation attacks in the way your query suggested.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9535ee1-7e42-4d67-9f7f-1eee3e87e5ac",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "12826eeb-6930-46a3-a761-7bde453071fa",
  "sourceToolAssistantUUID": "c9535ee1-7e42-4d67-9f7f-1eee3e87e5ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T20:19:49.611Z_

<details><summary>↩ Tool result · `toolu_01R5UEuBnS8xFe9xtJx3dhgP`</summary>

```text
Web search results for query: "FlowPolicy consistency flow matching 3D robustness spatial generalization robot 2025"

Links: [{"title":"GitHub - zql-kk/FlowPolicy: [AAAI 2025 Oral] FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation · GitHub","url":"https://github.com/zql-kk/FlowPolicy"},{"title":"[2412.04987] FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation","url":"https://arxiv.org/abs/2412.04987"},{"title":"FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation","url":"https://arxiv.org/html/2412.04987v2"},{"title":"FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation | Request PDF","url":"https://www.researchgate.net/publication/390712735_FlowPolicy_Enabling_Fast_and_Robust_3D_Flow-Based_Policy_via_Consistency_Flow_Matching_for_Robot_Manipulation"},{"title":"FlowPolicy: Enabling Fast and Robust 3D Flow-based ...","url":"https://axi.lims.ac.uk/paper/2412.04987"},{"title":"FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/flowpolicy-enabling-fast-robust-3d-flow-based"},{"title":"FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation - Consensus","url":"https://consensus.app/papers/flowpolicy-enabling-fast-and-robust-3d-flowbased-policy-zeng-zhang/3bc06c65581c5562b8435e53e44bef3d/"},{"title":"[Literature Review] FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation","url":"https://www.themoonlight.io/en/review/flowpolicy-enabling-fast-and-robust-3d-flow-based-policy-via-consistency-flow-matching-for-robot-manipulation"},{"title":"FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/33617"},{"title":"Aaai","url":"https://ojs.aaai.org/index.php/AAAI/citationstylelanguage/get/apa?submissionId=33617&publicationId=31890"}]

Based on the search results, I found comprehensive information about FlowPolicy:

## Overview

FlowPolicy is the official implementation of an AAAI 2025 paper titled "FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation." The paper was selected for oral presentation at AAAI 2025.

## Core Approach

FlowPolicy is a novel framework for fast policy generation based on consistency flow matching and 3D vision that refines flow dynamics by normalizing the self-consistency of the velocity field, enabling the model to derive task execution policies in a single inference step.

FlowPolicy conditions on the observed 3D point cloud, where consistency flow matching directly defines straight-line flows from different time states to the same action space, while simultaneously constraining their velocity values.

## Key Performance Results

FlowPolicy demonstrates a 7x increase in inference speed while maintaining competitive average success rates compared to state-of-the-art methods. Among 3D-based baselines, the approach achieves the best success rate with the shortest inference time.

## Spatial Generalization

3D-based baselines generally outperform 2D-based ones, owing to the richer spatial representation offered by point clouds. The compact 3D representation leads to a richer spatial representation of the flow model.

## Validation

The effectiveness of FlowPolicy was validated in Adroit and Metaworld environments. The code is available on GitHub at https://github.com/zql-kk/FlowPolicy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53c9336f-9f15-4d18-9fe0-257d8dbe81e5",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "022f4d79-4ca0-44d4-b714-98d203ff1d6c",
  "sourceToolAssistantUUID": "53c9336f-9f15-4d18-9fe0-257d8dbe81e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T20:19:57.385Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LzcKKk35Myun9FeHC3dXR9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.04987",
  "prompt": "Extract the full abstract and key details about FlowPolicy. What problem does it solve? How does it handle robustness and spatial generalization? What are the key quantitative results? Does it address geometric perturbations or out-of-distribution spatial shifts?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "022f4d79-4ca0-44d4-b714-98d203ff1d6c",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWRPzsFFr38HuPffDtT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd2c4aac-f822-4156-9cd9-97b8bf4b5907",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018C5LR2cZbuA17JGb1bCriD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 16632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T20:19:57.599Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016JerDdvwfa4pGAhvSFGusr`</summary>

```json
{
  "query": "SE(3) equivariant diffusion policy robustness geometric transformation robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd2c4aac-f822-4156-9cd9-97b8bf4b5907",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWRPzsFFr38HuPffDtT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd3224f1-9c05-4a79-8bd4-ece7dcc30c8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018C5LR2cZbuA17JGb1bCriD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 16632,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2559
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 16632,
          "cache_creation_input_tokens": 2559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2559,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T20:20:04.283Z_

<details><summary>↩ Tool result · `toolu_01LzcKKk35Myun9FeHC3dXR9`</summary>

```text
# FlowPolicy: Summary and Key Details

## Full Abstract
"Robots can acquire complex manipulation skills by learning policies from expert demonstrations, which is often known as vision-based imitation learning. Generating policies based on diffusion and flow matching models has been shown to be effective, particularly in robotic manipulation tasks. However, recursion-based approaches are inference inefficient in working from noise distributions to policy distributions, posing a challenging trade-off between efficiency and quality. This motivates us to propose FlowPolicy, a novel framework for fast policy generation based on consistency flow matching and 3D vision. Our approach refines the flow dynamics by normalizing the self-consistency of the velocity field, enabling the model to derive task execution policies in a single inference step. Specifically, FlowPolicy conditions on the observed 3D point cloud, where consistency flow matching directly defines straight-line flows from different time states to the same action space, while simultaneously constraining their velocity values, that is, we approximate the trajectories from noise to robot actions by normalizing the self-consistency of the velocity field within the action space, thus improving the inference efficiency. We validate the effectiveness of FlowPolicy in Adroit and Metaworld, demonstrating a 7× increase in inference speed while maintaining competitive average success rates compared to state-of-the-art methods."

## Problem Solved
FlowPolicy addresses the inference inefficiency of recursive diffusion and flow-matching approaches by enabling single-step policy generation, dramatically reducing computational overhead in robotic manipulation.

## Key Quantitative Results
- **7× faster inference** compared to existing methods
- **Competitive success rates** maintained across benchmarks (Adroit and Metaworld environments)

## Spatial Generalization and Robustness
The provided content does not explicitly address geometric perturbations, out-of-distribution spatial shifts, or robustness to spatial variations. The abstract focuses on inference speed and success metrics but lacks detail on spatial generalization capabilities.

**Submission Details:** arXiv:2412.04987 [cs.RO], submitted December 6, 2024; code available on GitHub.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd2c4aac-f822-4156-9cd9-97b8bf4b5907",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "9ab33403-6bec-401a-80c0-eca5108eca78",
  "sourceToolAssistantUUID": "cd2c4aac-f822-4156-9cd9-97b8bf4b5907",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T20:20:06.434Z_

<details><summary>↩ Tool result · `toolu_016JerDdvwfa4pGAhvSFGusr`</summary>

```text
Web search results for query: "SE(3) equivariant diffusion policy robustness geometric transformation robot 2025 2026"

Links: [{"title":"Equivariant Diffusion Policy","url":"https://www.emergentmind.com/topics/equivariant-diffusion-policy"},{"title":"SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space | OpenReview","url":"https://openreview.net/forum?id=U5nRMOs8Ed"},{"title":"EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable and Data Efficient Learning","url":"https://arxiv.org/html/2407.01479v1"},{"title":"Canonical Policy: Learning Canonical 3D Representation for SE⁢(3)-Equivariant Policy","url":"https://arxiv.org/html/2505.18474"},{"title":"EquiForm: Noise-Robust SE⁢(3)-Equivariant Policy Learning from 3D Point Clouds","url":"https://arxiv.org/html/2601.17486"},{"title":"ReSeFlow: Rectifying SE(3)-Equivariant Policy Learning Flows","url":"https://arxiv.org/html/2509.22695v1"},{"title":"ET-SEED: Efficient Trajectory-Level SE(3) Equivariant Diffusion Policy","url":"https://arxiv.org/html/2411.03990v1"},{"title":"[2407.01479] EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable and Data Efficient Learning","url":"https://arxiv.org/abs/2407.01479"},{"title":"EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable and Data Efficient Learning | OpenReview","url":"https://openreview.net/forum?id=ueBmGhLOXP"},{"title":"[2507.01723] SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space","url":"https://arxiv.org/abs/2507.01723"}]

Based on the web search results, here's a comprehensive overview of SE(3) equivariant diffusion policies for robotic manipulation with focus on robustness and geometric transformations:

## Overview of SE(3) Equivariant Diffusion Policies

Equivariant diffusion policy is a framework that exploits symmetry groups (e.g., SE(3), SO(3)) to ensure that the policy's outputs transform consistently with its geometric inputs. It integrates denoising diffusion probabilistic models with group-equivariant neural architectures, using techniques like group convolutions and spherical harmonics to enhance data efficiency.

## Recent 2025-2026 Research

Several recent approaches have emerged:

**Spherical Diffusion Policy (SDP):** Spherical Diffusion Policy (SDP), an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene, achieving such equivariance by embedding the states, actions, and the denoising process in spherical Fourier space.

**EquiForm (Noise-Robust Approach):** EquiForm achieves an average improvement of 17.2% in simulation and 28.1% in real-world experiments, demonstrating strong noise robustness and spatial generalization.

**ReSeFlow:** ReSeFlow employs SE(3)-equivariant networks to preserve rotational and translational symmetry, enabling robust generalization under rigid-body motions, and circumvents the need for the iterative, multi-step refinement process inherent to diffusion-based models like ET-SEED.

## Performance and Robustness

Fully equivariant layers (e.g., escnn-based backbone) yield 9–21.9% higher average success across tasks with high pose variability. Equivariant policies generalize instantly to transformed poses without explicit data augmentation, and error rates under out-of-distribution transformations (e.g., scene tilts, reorientations) are substantially reduced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd3224f1-9c05-4a79-8bd4-ece7dcc30c8f",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "7c8014dd-8902-48da-95f7-d109b6b82d24",
  "sourceToolAssistantUUID": "bd3224f1-9c05-4a79-8bd4-ece7dcc30c8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-10T20:20:12.054Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DhTeSuepYCDhzvjrtt5hL8`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.17486",
  "prompt": "Extract the abstract and method summary for EquiForm. What problem does it solve? How does it achieve noise-robust SE(3)-equivariant policy learning? What are the key results regarding spatial generalization and robustness to geometric perturbations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c8014dd-8902-48da-95f7-d109b6b82d24",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWSdzmPV5R4h9w64x4n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba1228e1-e873-4521-ae43-fb9955525f2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZwX1zsKFqC1uBnGQgzgjk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1726,
      "cache_read_input_tokens": 19191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1726,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T20:20:12.759Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NhJjJJcdTWc881strdWGBc`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.22695v1",
  "prompt": "Extract the abstract and method summary for ReSeFlow. What problem does it solve? How does it rectify SE(3)-equivariant policy learning flows? What are the key results regarding robustness and generalization under geometric transformations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba1228e1-e873-4521-ae43-fb9955525f2d",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWSdzmPV5R4h9w64x4n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1db60eb3-7257-4a4c-8f9c-e1c20fe432fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZwX1zsKFqC1uBnGQgzgjk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1726,
      "cache_read_input_tokens": 19191,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1726
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 19191,
          "cache_creation_input_tokens": 1726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1726,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T20:20:18.233Z_

<details><summary>↩ Tool result · `toolu_01DhTeSuepYCDhzvjrtt5hL8`</summary>

```text
# EquiForm: Noise-Robust SE(3)-Equivariant Policy Learning

## Problem Statement

EquiForm addresses a critical challenge in robotic manipulation: point cloud-based policies remain highly sensitive to sensor noise, pose variations, and occlusions. While SE(3)-equivariant approaches theoretically enable spatial generalization, they break down under realistic sensor noise that disrupts the geometric consistency required for equivariance.

The paper formalizes how noise-induced distortions prevent observations that differ only by rigid transformations from mapping to consistent canonical representations, causing equivariance deviation in policy learning.

## Solution Approach

EquiForm combines two complementary mechanisms:

**1. Geometric Denoising Module:** A progressive two-stage point cloud correction addressing surface deviation (normal-direction) and sampling inconsistency (tangent-direction), restoring stable 3D structure before canonicalization.

**2. Equivariant Contrastive Learning:** An InfoNCE loss applied to intermediate equivariant features, encouraging representation consistency under both geometric perturbations and noise. This stabilizes transformation estimation while preserving SE(3) structure.

Built on SE(3) canonicalization, the framework transforms observations into a shared reference frame, enabling pose-invariant policy learning with improved robustness.

## Key Results

- **Overall improvement:** 17.2% average performance gain in simulation versus state-of-the-art baselines
- **Real-world performance:** 28.1% improvement across four manipulation tasks
- **MimicGen benchmark:** 34.5% advantage over non-equivariant DP3 baseline; 17.0% over Canonical Policy
- **Robustness validation:** Maintains performance under severe Gaussian noise and rigid transformations where baseline equivariant policies fail
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba1228e1-e873-4521-ae43-fb9955525f2d",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "3b551859-944b-4a72-88ef-36822842a2fb",
  "sourceToolAssistantUUID": "ba1228e1-e873-4521-ae43-fb9955525f2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T20:20:18.920Z_

<details><summary>↩ Tool result · `toolu_01NhJjJJcdTWc881strdWGBc`</summary>

```text
# ReSeFlow: SE(3)-Equivariant Policy Learning

## Problem Addressed

ReSeFlow tackles three key challenges in robotic manipulation policy learning:

1. **Geometric complexity**: Robotic actions exist in SE(3) space, and naive Euclidean approaches "fail to generalize to complex and challenging manipulation-involved scenarios."

2. **Computational efficiency**: Diffusion-based policies require iterative inference steps, creating bottlenecks for real-world deployment.

3. **Data efficiency**: Learning robust policies from limited demonstrations while generalizing across varying object poses and viewpoints.

## Method Summary

ReSeFlow combines two innovations:

**SE(3)-Equivariant Rectified Flow**: The framework introduces rectification to SE(3)-equivariant diffusion models, replacing the iterative denoising process with a flow-based approach that follows "straight, geodesic-like paths in the model's latent space."

**Two-Stage Pipeline**: 
- **Flow 1** learns straight paths using original demonstrations
- **Flow 2** refines these paths using synthetic data from Flow 1, further straightening the generation trajectories

## Key Results on Robustness and Generalization

The method demonstrates exceptional geometric invariance:

- **Single-step inference**: ReSeFlow achieves "better performance with lower geodesic distance than the baseline methods" while requiring only 1 inference step versus ET-SEED's 100 steps

- **Performance improvements**: Up to 48.5% error reduction on painting and 21.9% on rotating triangle tasks

- **Trajectory stability**: Maintains "consistently low geodesic error across all 10 action steps" across diverse manipulation scenarios, showing robust generalization under rigid-body transformations
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1db60eb3-7257-4a4c-8f9c-e1c20fe432fb",
  "isSidechain": true,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "agentId": "a2db14817da9e1d4a",
  "type": "user",
  "uuid": "af336b4f-83d6-4211-92a4-2084e735e550",
  "sourceToolAssistantUUID": "1db60eb3-7257-4a4c-8f9c-e1c20fe432fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-10T20:21:02.751Z_

I now have comprehensive information on both flagged papers and additional related work. Here is my full report:

---

## Paper 1: "Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness" (DDP)

**arXiv 2603.21017, March 2026**

**Problem:** Diffusion policies for visuomotor control fail catastrophically under severe OOD disturbances such as unexpected object displacements or visual corruptions during deployment.

**Approach:** DDP deeply integrates a diffusion world model into the policy via a shared 3D visual encoder, co-optimizing behavior cloning and world model objectives (L_total = L_BC + lambda * L_WM). At inference time, it implements a three-stage OOD response:
1. **Detection** - monitors "real-imagination discrepancy" (latent distance between actual observations and predicted states)
2. **Imagination** - when OOD is detected, abandons the corrupted visual stream and generates actions conditioned on autoregressively forecasted latent dynamics
3. **Recovery** - applies compensatory spatial corrections via pose estimation once the displaced object settles

**Key Results:**
- 73.8% OOD success on MetaWorld (vs. 23.9% baseline with tracking)
- 83.3% success under real-world spatial shifts (vs. 3.3% baseline)
- 76.7% real-world success in open-loop imagination (no visual feedback post-initialization)

**Relation to test-time geometric robustness of diffusion policies:** DDP is directly relevant as it uses a *test-time inference mechanism* (switching to imagined latent states) to handle geometric/spatial perturbations. However, it requires training a world model jointly with the policy -- it is not a pure test-time method. The spatial correction is computed as a static displacement offset rather than a continuous geometric transformation.

---

## Paper 2: "Visual-Geometry Diffusion Policy" (VGDP)

**arXiv 2511.22445, November 2025**

**Problem:** Visuomotor policies relying on single-modality inputs (RGB alone or point clouds alone) fail to generalize under visual and spatial perturbations.

**Approach:** VGDP introduces a Complementarity-Aware Fusion Module combining RGB (ResNet-18, 512-dim) and point cloud (DP3, 64-dim) features:
- Features project into a shared 256-dimensional space
- **Modality dropout** (p=0.2) randomly disables entire RGB or 3D branches during training, forcing modality-invariant representations
- Bidirectional cross-attention with residual connections enables lightweight modality interaction
- A diffusion policy head denoises actions conditioned on the fused representation

**Key Results:**
- 39.1% average improvement over 7 baselines (18 sim + 4 real tasks)
- 15.2% improvement under spatial perturbations
- 41.5% improvement under visual condition changes
- 11x stability improvement (variance 2.53% vs. 32.72% for competitors)
- 55.3% higher mean success under severe randomization

**Relation to test-time geometric robustness:** VGDP achieves spatial robustness through *training-time architectural design* (multimodal fusion + modality dropout) rather than test-time inference modifications. It demonstrates that point cloud geometry provides complementary spatial information that compensates for RGB failures under geometric shifts. This is a representational/training approach rather than a test-time inference method.

---

## Additional Related Work Discovered

### SE(3)-Equivariant Approaches (highly relevant to geometric robustness)

**EquiForm** (arXiv 2601.17486, January 2026): Noise-robust SE(3)-equivariant policy learning from 3D point clouds. Uses a geometric denoising module + equivariant contrastive learning to maintain SE(3) structure under realistic sensor noise. Achieves 17.2% improvement in sim, 28.1% in real-world. Directly addresses the breakdown of equivariance guarantees under noisy conditions.

**ReSeFlow** (arXiv 2509.22695, September 2025): Rectified SE(3)-equivariant flow matching. Replaces iterative diffusion denoising with straight geodesic-like paths in SE(3) space, enabling single-step inference. Up to 48.5% error reduction. Combines geometric invariance with flow-based efficiency.

**Spherical Diffusion Policy (SDP)** (arXiv 2507.01723): SE(3)-equivariant diffusion policy operating in spherical Fourier space, adapting trajectories according to 3D scene transformations.

### Flow Matching Approaches

**FlowPolicy** (AAAI 2025 Oral, arXiv 2412.04987): Consistency flow matching for single-step policy generation with 7x inference speedup. Uses 3D point clouds but does not explicitly address spatial robustness.

**Flow Matching Policy Gradients (FPO)** (ICLR 2026): Policy gradient algorithm for optimizing flow-based generative models via conditional flow matching objective reframing.

### Test-Time Composition

**General Policy Composition (GPC)** (arXiv 2510.01068): Training-free test-time composition of diffusion/flow policy scores via convex combination. Does NOT specifically address geometric robustness but provides a framework for test-time policy enhancement without retraining.

---

## Summary of Relevance to "Test-Time Inference Methods for Geometric Robustness of Diffusion Policies"

| Paper | Training-time? | Test-time? | Geometric Focus? |
|-------|---------------|-----------|-----------------|
| DDP | Yes (world model co-training) | Yes (imagination at inference) | Yes (spatial displacement recovery) |
| VGDP | Yes (modality dropout/fusion) | No | Yes (point cloud + RGB fusion) |
| EquiForm | Yes (denoising + contrastive) | No | Yes (SE(3) under noise) |
| ReSeFlow | Yes (rectified flow) | Partially (single-step) | Yes (SE(3) equivariance) |
| GPC | No | Yes (score composition) | No |

**DDP is the most directly relevant** as it is the only paper combining both a test-time inference mechanism (switching to imagined states) with explicit geometric/spatial perturbation handling. **VGDP** is relevant as a training-time baseline showing what multimodal fusion can achieve for spatial robustness. The **SE(3)-equivariant line of work** (EquiForm, ReSeFlow, SDP) provides an orthogonal approach to geometric robustness through architectural symmetry constraints rather than test-time adaptation.

Sources:
- [DDP - Dreaming the Unseen](https://arxiv.org/html/2603.21017v1)
- [VGDP - Visual-Geometry Diffusion Policy](https://arxiv.org/abs/2511.22445)
- [GPC - Compose Your Policies](https://arxiv.org/abs/2510.01068)
- [FlowPolicy](https://arxiv.org/abs/2412.04987)
- [EquiForm](https://arxiv.org/html/2601.17486)
- [ReSeFlow](https://arxiv.org/html/2509.22695v1)
- [Spherical Diffusion Policy](https://arxiv.org/abs/2507.01723)
- [Flow Matching Policy Gradients (ICLR 2026)](https://openreview.net/pdf/376ea41422d8f63f58a4916b9a9783de90e8e461.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af336b4f-83d6-4211-92a4-2084e735e550",
  "isSidechain": true,
  "agentId": "a2db14817da9e1d4a",
  "requestId": "req_011CauWTZGnHiU2zmdN3rqhS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5df4084b-7365-49b2-a5cc-2d7369ce599a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LA1k5Jf5wKWNYdgTps5Lfv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 20917,
      "output_tokens": 1872,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1872,
          "cache_read_input_tokens": 20917,
          "cache_creation_input_tokens": 1113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1113,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
