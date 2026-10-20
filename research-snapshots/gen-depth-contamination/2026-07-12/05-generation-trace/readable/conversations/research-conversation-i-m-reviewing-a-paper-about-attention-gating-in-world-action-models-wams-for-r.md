# Research conversation: I'm reviewing a paper about attention gating in World Action Models (WAMs) for robotics. I need to find concurrent/compe

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-abfdef84665fcf466.jsonl`
- **Structured JSON:** [`56f9e45e2dd7a5c88e5d.json`](../../sessions/56/56f9e45e2dd7a5c88e5d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-10T18:56:58.023Z_

I'm reviewing a paper about attention gating in World Action Models (WAMs) for robotics. I need to find concurrent/competing work from the last 3 months (March-May 2026) that the proposal might have missed.

Please search for the following, using WebSearch:

1. "EA-WM event-aware world model arxiv 2026" — verify this paper exists and check its approach (claimed to use event-saliency gating for cross-modal attention)

2. "CKT-WAM parameter-efficient adapter world action model arxiv 2026" — verify existence

3. "OA-WAM object-addressable world action model arxiv 2026" — verify existence

4. "VAG dual-stream video-action generation arxiv 2026" — verify existence (arXiv 2604.09330)

5. "world action model attention gating noise level arxiv 2026" — find any work doing noise-level conditioned attention gating

6. "adaptive attention diffusion transformer noise level 2026" — find any work conditioning attention on noise/timestep in diffusion models

7. "cross-modal attention gating diffusion independent timesteps 2026" — find the most directly competitive work

8. "Do World Action Models Generalize Better than VLAs arxiv 2603.22078" — verify this robustness study exists and what it says about WAM robustness

9. "LIBERO-PRO robustness evaluation VLA arxiv 2025" — verify benchmark exists and current SOTA

10. "CoRL 2026 submission deadline" — verify the abstract deadline is May 26, 2026

For each search, report what you find. If a paper exists, note its key contribution and how it relates to noise-pair conditioned attention gating in WAMs. Be thorough — I need to know if the proposed novelty (learned per-head attention gating conditioned on (t_o, t_a) noise pairs) has already been done.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "a7ffd864-4262-4cf7-a14b-c641a37b519f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:56:58.027Z_

```json
{
  "parentUuid": "a7ffd864-4262-4cf7-a14b-c641a37b519f",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
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
  "uuid": "488c3a76-38f8-4472-99a2-f6daf3ae1c1f",
  "timestamp": "2026-05-10T18:56:58.027Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:57:00.589Z_



I'll conduct all 10 searches in parallel to find the relevant papers and information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "488c3a76-38f8-4472-99a2-f6daf3ae1c1f",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQ6vKmxEhVqkBov15EM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9378286c-b9de-4f70-a7aa-62baf7e971ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VjE4qGhxP2JnjvuRMNRA1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1001,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T18:57:00.694Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015jbybPEmP3WPpWBvqi6KPU`</summary>

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
  "parentUuid": "9378286c-b9de-4f70-a7aa-62baf7e971ee",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQ6vKmxEhVqkBov15EM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c07ca89-8c02-4c8d-9091-125a0d02f0f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VjE4qGhxP2JnjvuRMNRA1S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 8223,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1001
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1001,
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

_source line 5 · 2026-05-10T18:57:00.697Z_

<details><summary>↩ Tool result · `toolu_015jbybPEmP3WPpWBvqi6KPU`</summary>

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
  "parentUuid": "0c07ca89-8c02-4c8d-9091-125a0d02f0f6",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "c0dd3bab-dd55-4af8-8b1a-3229be5fc2bf",
  "sourceToolAssistantUUID": "0c07ca89-8c02-4c8d-9091-125a0d02f0f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:57:03.001Z_



Now let me run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0dd3bab-dd55-4af8-8b1a-3229be5fc2bf",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQ782jPHiM8Ab4bzgzv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c1d7d76-1fe3-4fca-8178-1d843f594aef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2RMd91XAdDAGmiVW4sbbW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 9224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1412,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T18:57:03.463Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Heg2AG9rEgAtuCKsGWjVkj`</summary>

```json
{
  "query": "EA-WM event-aware world model arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c1d7d76-1fe3-4fca-8178-1d843f594aef",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQ782jPHiM8Ab4bzgzv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "670ad75e-75c5-4486-ab2b-4bd33c0e3c5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2RMd91XAdDAGmiVW4sbbW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 9224,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1412
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 79,
          "cache_read_input_tokens": 9224,
          "cache_creation_input_tokens": 1412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1412,
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

_source line 8 · 2026-05-10T18:57:10.162Z_

<details><summary>↩ Tool result · `toolu_01Heg2AG9rEgAtuCKsGWjVkj`</summary>

```text
Web search results for query: "EA-WM event-aware world model arxiv 2026"

Links: [{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/Awesome-World-Models"},{"title":"GitHub - lucas-maes/le-wm: Official code base for LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels · GitHub","url":"https://github.com/lucas-maes/le-wm"},{"title":"A Comprehensive Survey on World Models for Embodied AI","url":"https://arxiv.org/html/2510.16732v1"},{"title":"Kai Xu1, Hang Zhao1,2, Ruizhen Hu3, Yuhang Huang1,4 ...","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/300568/preprint_pdf/ffcbb413e3a2622b5be3ba098a32292f.pdf"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"WorldArena: A Unified Benchmark for Evaluating Perception","url":"https://arxiv.org/pdf/2602.08971"},{"title":"Web World Models","url":"https://arxiv.org/html/2512.23676v1"},{"title":"Article Not peer-reviewed version Learning to Model the World: A Survey","url":"https://www.preprints.org/frontend/manuscript/5086594a01b6a0b251820cb03ea9a8f6/download_pub"},{"title":"Awesome-World-Model/README.md at main · LMD0311/Awesome-World-Model","url":"https://github.com/LMD0311/Awesome-World-Model/blob/main/README.md"}]

Based on the search results, I found information about the EA-WM paper:

## EA-WM: Event-Aware Generative World Model

EA-WM is an event-aware robotic video world model conditioned on Structured Kinematic-to-Visual Action Fields (KVAFs).

### Key Features:

**Architecture and Representation:**
EA-WM constructs KVAFs by lifting low-dimensional robot actions and kinematic states into the target camera view through robot kinematics and camera projection, specifically rendering depth-aware arm structures, joint landmarks, gripper geometry, end-effector heatmaps, and pose cues as temporally aligned visual fields.

**Event-Aware Mechanism:**
The model introduces an event-aware bidirectional fusion mechanism driven by Event-Difference Latent Supervision (EDLS), which supervises event predictions with VAE-encoded temporal difference latents to compel the model to dynamically allocate attention to regions undergoing state transitions and interaction dynamics.

### Performance:

Compared to existing state-of-the-art baselines, EA-WM significantly enhances the physical adherence, 3D geometric accuracy, and fine-grained controllability of generated rollouts, establishing a new standard for robotic video modeling.

The paper addresses the challenge of preserving precise robot spatial geometry and fine-grained robot-object interaction dynamics in generated rollouts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "670ad75e-75c5-4486-ab2b-4bd33c0e3c5b",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "0535a34a-b31b-4deb-a110-525757bbef50",
  "sourceToolAssistantUUID": "670ad75e-75c5-4486-ab2b-4bd33c0e3c5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T18:57:19.923Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PautDijTiRWXyCNXcFFCmh`</summary>

```json
{
  "query": "CKT-WAM parameter-efficient adapter world action model arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0535a34a-b31b-4deb-a110-525757bbef50",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQ7pDwqi1GeW9ZaT6wF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8636c6b7-7c05-42f3-a66d-399b9cfa9ac9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178zzFCfAj3EcQompKxp1CU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 10636,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1012
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 10636,
          "cache_creation_input_tokens": 1012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1012,
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

_source line 10 · 2026-05-10T18:57:27.236Z_

<details><summary>↩ Tool result · `toolu_01PautDijTiRWXyCNXcFFCmh`</summary>

```text
Web search results for query: "CKT-WAM parameter-efficient adapter world action model arxiv 2026"

Links: [{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"[2603.28955] Enhancing Policy Learning with World-Action Model","url":"https://arxiv.org/abs/2603.28955"},{"title":"[2603.24581] Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving","url":"https://arxiv.org/abs/2603.24581"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"}]

I found the paper you were looking for! Here's what I found:

## CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models

CKT-WAM is a method that uses routed context tokens to preserve task-relevant sufficient statistics while avoiding the cost of transferring full representations, injecting this knowledge into the conditioning textual embeddings of a student world action model with minimal architectural modification.

### Key Results

The method consistently improves zero-shot generalization and achieves the best overall performance on LIBERO-Plus, reaching 86.1% total success rate with only 1.17% trainable parameters, while approaching full fine-tuning performance. 

Beyond simulation, CKT-WAM also demonstrates strong real-world long-horizon manipulation ability, achieving the best average success rate of 83.3% across four multi-step tasks.

### Technical Approach

CKT-WAM transfers compact intermediate context tokens through the student's native conditioning pathway, enabling flexible transfer across heterogeneous world action model pairs.

The paper is available at: https://github.com/YuhuaJiang2002/CKT-WAM


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8636c6b7-7c05-42f3-a66d-399b9cfa9ac9",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "1254ccb3-66e7-4ac1-9b98-00243f035773",
  "sourceToolAssistantUUID": "8636c6b7-7c05-42f3-a66d-399b9cfa9ac9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T18:57:29.776Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019bM4MExc9eD46STXT5Gktt`</summary>

```json
{
  "query": "OA-WAM object-addressable world action model arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1254ccb3-66e7-4ac1-9b98-00243f035773",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQ95J62PNGfqGUkEnQ9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c91b2d7-5e4a-4ab0-87a9-0d71333bc737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015X6t7uMAf93xUwM2n9dQxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 811,
      "cache_read_input_tokens": 11648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 811,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:57:37.861Z_

<details><summary>↩ Tool result · `toolu_019bM4MExc9eD46STXT5Gktt`</summary>

```text
Web search results for query: "OA-WAM object-addressable world action model arxiv 2026"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"Robotics","url":"https://arxiv.org/list/cs.RO/recent"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"Robotics | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/cs.RO"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"}]

I found the paper! Here's what the search results reveal about OA-WAM:

## OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation

OA-WAM is an Object-Addressable World Action Model for robust robot manipulation. OA-WAM decomposes each frame into N+1 slot states, with one robot slot and N object slots, where each slot contains a persistent address vector and a time-varying content vector, fused with text, image, proprioception, and past-action tokens in a block-causal sequence.

### Key Innovation

OA-WAM closes this gap by partitioning each slot into a frozen identity address and a time-varying content subvector. Addressability is enforced by routing cross-slot attention through address-only keys and resetting the address slice at every transformer layer, separating which object to act on from what that object currently is without adding extra tokens.

### Performance

OA-WAM matches strong VLA and WAM baselines on LIBERO (97.8%) and SimplerEnv (79.3%), reaches state-of-the-art performance on the most relevant LIBERO-Plus geometric axes, and remains competitive on the seven-axis aggregate. A causal slot-intervention test yields a swap-binding cosine of 0.87, versus at most 0.09 for holistic baselines.

OA-WAM sets a new SOTA on the geometric LIBERO-Plus axes.

The paper (arXiv:2605.06481) was recently published on arXiv, just 2 days ago according to the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c91b2d7-5e4a-4ab0-87a9-0d71333bc737",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "24f382f5-148d-4b7f-acd9-64fd0acdf5dc",
  "sourceToolAssistantUUID": "3c91b2d7-5e4a-4ab0-87a9-0d71333bc737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T18:57:40.306Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K4613og34A3dHdxiduZcZi`</summary>

```json
{
  "query": "VAG dual-stream video-action generation arxiv 2604.09330"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24f382f5-148d-4b7f-acd9-64fd0acdf5dc",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQ9rdrvyWBpfUpsW3Qi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dfa56e5-67b1-4bbc-bb9a-1aeef3f3147e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Jih9wuZeqRJB4mRq9QUPs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 12459,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 12459,
          "cache_creation_input_tokens": 873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 873,
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

_source line 14 · 2026-05-10T18:57:46.287Z_

<details><summary>↩ Tool result · `toolu_01K4613og34A3dHdxiduZcZi`</summary>

```text
Web search results for query: "VAG dual-stream video-action generation arxiv 2604.09330"

Links: [{"title":"[2604.09330] VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis","url":"https://arxiv.org/abs/2604.09330"},{"title":"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis","url":"https://arxiv.org/html/2604.09330"},{"title":"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis | alphaXiv","url":"https://www.alphaxiv.org/abs/2604.09330"},{"title":"GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub","url":"https://github.com/iszhanjiawei/flow_matching_arxiv_daily"},{"title":"ActionParty: Multi-Subject Action Binding in Generative Video Games","url":"https://arxiv.org/html/2604.02330"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/awesome-world-models"},{"title":"Dual-Stream Diffusion Net for Text-to-Video Generation","url":"https://arxiv.org/html/2308.08316v3"},{"title":"[2604.04198v1] DriveVA: Video Action Models are Zero-Shot Drivers","url":"https://arxiv.org/abs/2604.04198v1"},{"title":"Action Images: End-to-End Policy Learning via Multiview Video Generation","url":"https://arxiv.org/html/2604.06168"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"}]

Based on the search results, here's what I found about VAG (arxiv 2604.09330):

VAG is a unified flow-matching-based dual-stream framework that jointly generates video and action under visual and language conditioning.

**Background:**
Recent advances in robot foundation models trained on large-scale human teleoperation data have enabled robots to perform increasingly complex real-world tasks. However, scaling these systems remains difficult because collecting task-specific demonstrations is expensive and labor-intensive.

**Problem It Addresses:**
Existing World Models (WMs) are not directly suitable for policy learning since they do not provide paired action trajectories. World-Action (WA) models partially address this by predicting actions with visual outputs, yet often lack strong video-action alignment, while two-stage pipelines that generate video first and then infer actions introduce inefficiency and error accumulation.

The paper was submitted on April 10, 2026, and is authored by researchers from GigaAI, Zhejiang University, Peking University, and other institutions. The full paper is available on arXiv at https://arxiv.org/abs/2604.09330.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dfa56e5-67b1-4bbc-bb9a-1aeef3f3147e",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "5b441c72-4c00-40bf-8b3d-00c1fa5a4eb3",
  "sourceToolAssistantUUID": "0dfa56e5-67b1-4bbc-bb9a-1aeef3f3147e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T18:57:49.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hi51GqnTQQwfyAzY4i9vVB`</summary>

```json
{
  "query": "world action model attention gating noise level arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b441c72-4c00-40bf-8b3d-00c1fa5a4eb3",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQAUj1ciCkQzdUyrCAi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f02e9f0-b7c6-410c-b639-71e0ce50d4c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfECdot6hobnPBSkHhcXxF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 862,
      "cache_read_input_tokens": 13332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 862,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:57:57.249Z_

<details><summary>↩ Tool result · `toolu_01Hi51GqnTQQwfyAzY4i9vVB`</summary>

```text
Web search results for query: "world action model attention gating noise level arxiv 2026"

Links: [{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"Gated Attention for Large Language Models: Non-linearity, ...","url":"https://arxiv.org/pdf/2505.06708"},{"title":"[2505.06708] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiv.org/abs/2505.06708"},{"title":"[2506.21539] WorldVLA: Towards Autoregressive Action World Model","url":"https://arxiv.org/abs/2506.21539"},{"title":"WorldVLA: Towards Autoregressive Action World Model","url":"https://arxiv.org/html/2506.21539v1"},{"title":"The Model Knows Which Tokens Matter: Automatic Token Selection via Noise Gating","url":"https://arxiv.org/html/2603.07135"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/new"}]

Based on the search results, I found several recent arxiv papers from 2026 related to world action models with attention mechanisms and noise handling. Here are the most relevant findings:

## Recent World Action Model Papers with Attention and Noise Elements:

1. **Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising** - This work introduces "unilateral attention" where the depth branch can read from the main branch, but not vice versa, preserving the integrity of pretrained weights.

2. **MotuBrain: An Advanced World Action Model for Robot Control** - MotuBrain introduces a three-stream Mixture-of-Transformers (MoT) architecture with a text stream, a video stream, and an action stream. It further uses an H-bridge attention design to balance cross-modal interaction and efficiency, while supporting flexible multiview inputs through view-dependent 3D RoPE offsets.

3. **EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields** - The event gate modulates the strength of bidirectional cross-attention. The paper introduces an event-aware bidirectional fusion mechanism driven by Event-Difference Latent Supervision (EDLS), which supervises event predictions with VAE-encoded temporal difference latents.

4. **Being-H0.7: A Latent World-Action Model from Egocentric Videos** - Being-H0.7 implements the dual-branch design by packing both branches into a single Mixture-of-Transformers sequence with a dual-branch attention mask.

These papers represent the cutting edge of world action modeling research with various attention gating mechanisms and noise-handling approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f02e9f0-b7c6-410c-b639-71e0ce50d4c7",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "a797ce57-d9e7-4a93-a979-3b2e31f02c32",
  "sourceToolAssistantUUID": "1f02e9f0-b7c6-410c-b639-71e0ce50d4c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T18:58:00.200Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HEKRDgRPKmRYGzPbk3N3xk`</summary>

```json
{
  "query": "adaptive attention diffusion transformer noise level timestep conditioning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a797ce57-d9e7-4a93-a979-3b2e31f02c32",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQBHZqBYtbuCCEAmgQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c54ec30-910c-44f6-864e-675d8519829f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132gAGchWBmVYKL5gozt5rZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 14194,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 924
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 14194,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 924,
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

_source line 18 · 2026-05-10T18:58:07.410Z_

<details><summary>↩ Tool result · `toolu_01HEKRDgRPKmRYGzPbk3N3xk`</summary>

```text
Web search results for query: "adaptive attention diffusion transformer noise level timestep conditioning 2026"

Links: [{"title":"Normalization Techniques (GroupNorm, AdaLN)","url":"https://apxml.com/courses/advanced-diffusion-architectures/chapter-2-advanced-unet-architectures/unet-normalization-techniques"},{"title":"Conditioning in Diffusion Transformers","url":"https://apxml.com/courses/advanced-diffusion-architectures/chapter-3-transformer-diffusion-models/dit-conditioning"},{"title":"Published as a conference paper at ICLR 2025 DYNAMIC DIFFUSION TRANSFORMER","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a44a70acd5d0abc1a252ada9719dd06d-Paper-Conference.pdf"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/15f4cefb0e143c7ad9d40e879b0a9d0c-Paper-Conference.pdf"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://avdit2024.github.io/"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://arxiv.org/html/2405.13762v1"},{"title":"Diffusion Transformer (DiT) Architecture","url":"https://www.emergentmind.com/topics/diffusion-transformer-dit-architecture"},{"title":"Layer- and Timestep-Adaptive Differentiable Token Compression Ratios for Efficient Diffusion Transformers","url":"https://arxiv.org/html/2412.16822v2"},{"title":"Scalable Diffusion Models with Transformers William Peebles* UC Berkeley","url":"https://openaccess.thecvf.com/content/ICCV2023/papers/Peebles_Scalable_Diffusion_Models_with_Transformers_ICCV_2023_paper.pdf"},{"title":"Layer-and Timestep-Adaptive Differentiable Token Compression Ratios for Efficient Diffusion Transformers | Request PDF","url":"https://www.researchgate.net/publication/394633319_Layer-and_Timestep-Adaptive_Differentiable_Token_Compression_Ratios_for_Efficient_Diffusion_Transformers"}]

Based on the web search results, I found several relevant papers and resources about adaptive attention in diffusion transformers with noise level and timestep conditioning. Here are the key findings:

## Adaptive Timestep Conditioning in Diffusion Transformers

Recent work introduces a Timestep-wise Dynamic Width (TDW) mechanism, where the model learns to adjust the width of the attention and MLP blocks based on the current timestep. This addresses the varying computational needs at different stages of the diffusion process.

## Noise Level and Timestep Parameterization

A key contribution involves how the diffusion timestep is parameterized in the forward diffusion process. Instead of the standard fixed diffusion timestep, researchers propose applying variable diffusion timesteps across the temporal dimension and across modalities of the inputs, introducing a mixture of noise levels (MoNL) to effectively learn arbitrary conditional distributions.

## Adaptive Layer Normalization (AdaLN)

AdaLN (or AdaLN-Zero) is particularly effective in diffusion U-Nets because it allows the network to tailor its feature processing based on the noise level (timestep). By employing adaptive normalization schemes like AdaLN-Zero, Diffusion Transformers can effectively incorporate conditioning information, enabling the generation of high-fidelity images guided by various inputs.

## Layer and Timestep-Adaptive Compression

A timestep-wise differentiable ratio mechanism enables each layer and denoising timestep to learn its own compression ratio, resulting in a pattern where noisier timesteps adopt higher compression ratios, while clearer stages maintain lower ratios.

These approaches represent the current state of adaptive attention mechanisms in diffusion transformers, with specific focus on how models can dynamically adjust their computation and processing based on noise levels throughout the generation process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c54ec30-910c-44f6-864e-675d8519829f",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "7b538c56-22a6-480c-81ea-de91d8d75434",
  "sourceToolAssistantUUID": "0c54ec30-910c-44f6-864e-675d8519829f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T18:58:11.222Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018V2wALt3W2XwvecnGUgfaw`</summary>

```json
{
  "query": "cross-modal attention gating diffusion independent timesteps robotics 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b538c56-22a6-480c-81ea-de91d8d75434",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQC2xmtXxAudVymz2MP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37ec17c0-6baf-4fac-af4d-dc6b6c700a73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YaWRPZS9S1ZRHhqz9kZmyT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 15118,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 15118,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1121,
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

_source line 20 · 2026-05-10T18:58:17.895Z_

<details><summary>↩ Tool result · `toolu_018V2wALt3W2XwvecnGUgfaw`</summary>

```text
Web search results for query: "cross-modal attention gating diffusion independent timesteps robotics 2026"

Links: [{"title":"Article Not peer-reviewed version Cross-Modal Temporal Attention for","url":"https://www.preprints.org/frontend/manuscript/5abea80803d5705bca6fb11bdd4cfeac/download_pub"},{"title":"Unified Multimodal Understanding and Generation Models","url":"https://arxiv.org/pdf/2505.02567"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Multimodal Fusion and Vision-Language Models: A Survey for Robot Vision","url":"https://arxiv.org/html/2504.02477v1"},{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Lv_Rethinking_Cross-Modal_Interaction_in_Multimodal_Diffusion_Transformers_ICCV_2025_paper.pdf"},{"title":"Cross-Attention for Explainable Visuomotor Prediction in Robotic ...","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176704503.34542562/v1"},{"title":"Why Cross-Attention is the Secret Sauce of Multimodal Models | by Jakub Strawa | Medium","url":"https://medium.com/@jakubstrawadev/why-cross-attention-is-the-secret-sauce-of-multimodal-models-f8ec77fc089b"},{"title":"Cross-modal gated feature enhancement for multimodal emotion recognition in conversations | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-11989-6"},{"title":"Research Progress Review on Diffusion Models: Cross-Domain Applications and Technological Evolution - Oreate AI Blog","url":"https://www.oreateai.com/blog/research-progress-review-on-diffusion-models-crossdomain-applications-and-technological-evolution/550699ce2bebb9eadfbcaed334db56dd"},{"title":"CROSS-GAiT: Cross-Attention-Based Multimodal Representation Fusion for Parametric Gait Adaptation in Complex Terrains","url":"https://arxiv.org/html/2409.17262v2"}]

The search results show relevant research on cross-modal attention, diffusion models, and robotics. Here's a summary of the key findings:

## Cross-Modal Attention and Robotics

CROSS-GAiT is a novel algorithm for quadruped robots that uses Cross Attention to fuse terrain representations derived from visual and time-series inputs, including linear accelerations, angular velocities, and joint efforts, enabling adaptive gaits that respond dynamically to varying terrain conditions.

## Attention Gating Mechanisms

A gating mechanism using a learned scalar gating the cross-attention output via a tanh function is used to gradually inject visual information without destabilizing the pretrained language model.

## Diffusion Models in Robotics

Diffusion models have recently emerged as a promising approach in robotics, especially in robot manipulations, and leverage a probabilistic framework with the ability to model multi-modal distributions and robustness to high-dimensional input and output spaces.

## Multimodal Diffusion Transformers

Recent research has focused on TACA, a parameter-efficient method that dynamically rebalances cross-modal attention in multimodal diffusion.

The search results reflect current research progress in these areas as of 2025-2026, with particular emphasis on practical robotics applications combining cross-attention mechanisms with diffusion-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37ec17c0-6baf-4fac-af4d-dc6b6c700a73",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "6966bfe7-7f64-4cf9-95a2-5dcb1c209e49",
  "sourceToolAssistantUUID": "37ec17c0-6baf-4fac-af4d-dc6b6c700a73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T18:58:20.788Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XgadMov8jDURSqo5xNgJLq`</summary>

```json
{
  "query": "\"Do World Action Models Generalize Better than VLAs\" arxiv 2603.22078 robustness study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6966bfe7-7f64-4cf9-95a2-5dcb1c209e49",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQCopHGvKCsvFx76AJE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b16489d4-95d5-4b0b-beb1-0f4879c0fd4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pn5CsjrgTzqTw83E6E9WV8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 16239,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 16239,
          "cache_creation_input_tokens": 1030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1030,
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

_source line 22 · 2026-05-10T18:58:28.222Z_

<details><summary>↩ Tool result · `toolu_01XgadMov8jDURSqo5xNgJLq`</summary>

```text
Web search results for query: ""Do World Action Models Generalize Better than VLAs" arxiv 2603.22078 robustness study"

Links: [{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078"},{"title":"Paper page - Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://huggingface.co/papers/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]","url":"https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.20607"},{"title":"WorldVLA: Towards Autoregressive Action World Model","url":"https://arxiv.org/html/2506.21539v1"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://www.wispaper.ai/en/blog/world-action-models-generalize-better-than-vlas-20260324/eng"},{"title":"World Action Models are Zero-shot Policies | OpenReview","url":"https://openreview.net/forum?id=cd33uUB609"}]

I found the paper you're looking for. Here's a summary of the research:

## Overview

The paper addresses the challenge of robot action planning in the real world, which requires understanding the current state of the environment and predicting how it will evolve in response to actions.

## Key Comparison

Vision-language-action (VLA) models have achieved notable success across various robotic tasks, but their performance remains constrained by training data scope, with limited generalization to unseen scenarios and vulnerability to contextual perturbations. In contrast, World action models (WAMs) are built upon world models trained on large video corpora to predict future states, with their latent representations decoded into robot actions with minor adaptations.

## Main Findings

The researchers evaluated performance on LIBERO-Plus and RoboTwin 2.0-Plus benchmarks under various visual and language perturbations, finding that WAMs achieved strong robustness, with LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus.

However, VLAs such as π₀.₅ can achieve comparable robustness on certain tasks, though they typically require extensive training with diverse robotic datasets and varied learning objectives.

The performance advantage of WAMs is highly consistent across visually-based perturbations, with LingBot-VA achieving 89.0% under light, 80.9% under noise, and 87.9% under layout perturbations on RoboTwin 2.0-Plus, significantly outperforming VLAs like π₀.₅.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b16489d4-95d5-4b0b-beb1-0f4879c0fd4e",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "ec9d36d9-2aec-41ae-8dd6-2445085e7539",
  "sourceToolAssistantUUID": "b16489d4-95d5-4b0b-beb1-0f4879c0fd4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T18:58:30.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BwUT73V7MnyLHEvX881g49`</summary>

```json
{
  "query": "LIBERO-PRO robustness evaluation VLA benchmark arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec9d36d9-2aec-41ae-8dd6-2445085e7539",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQDZvdrFTbBZuUVYKbq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d592ffc4-b321-4742-9345-7d4f37efc00b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K82Qf9GiVaa8NMsjTqJopN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 17269,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 966
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 17269,
          "cache_creation_input_tokens": 966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 966,
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

_source line 24 · 2026-05-10T18:58:37.694Z_

<details><summary>↩ Tool result · `toolu_01BwUT73V7MnyLHEvX881g49`</summary>

```text
Web search results for query: "LIBERO-PRO robustness evaluation VLA benchmark arxiv 2025 2026"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"}]

Based on the search results, here's what I found about LIBERO-PRO robustness evaluation for VLA benchmarks:

## LIBERO-PRO Overview

LIBERO has emerged as a widely adopted benchmark for evaluating Vision-Language-Action (VLA) models; however, its current training and evaluation settings are problematic, often leading to inflated performance estimates and preventing fair model comparison. To address these issues, LIBERO-PRO is an extended LIBERO benchmark that systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments.

## Key Findings

Experimental results reveal that, although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under LIBERO-PRO's generalized setting. This discrepancy exposes the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception.

Models persist in executing grasping actions when the target object is replaced with irrelevant items, and their outputs remain unchanged even when given corrupted instructions or even messy tokens.

## Related Work

The search also found related robustness evaluation benchmarks. LIBERO-Plus performs a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise. Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d592ffc4-b321-4742-9345-7d4f37efc00b",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "5b384173-b0f6-4062-97c7-6235d39b82ec",
  "sourceToolAssistantUUID": "d592ffc4-b321-4742-9345-7d4f37efc00b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T18:58:40.216Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VT6C83bZ9p6Ff61R7tvWYW`</summary>

```json
{
  "query": "CoRL 2026 submission deadline abstract"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b384173-b0f6-4062-97c7-6235d39b82ec",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQEGSh7Z1gMqr3Zq6cd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a07d2d0b-64e0-4fc6-8c90-475d403973ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SGEYMFnmcG7MvX4fXfwe62",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 18235,
      "output_tokens": 60,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 976
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 60,
          "cache_read_input_tokens": 18235,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 976,
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

_source line 26 · 2026-05-10T18:58:45.274Z_

<details><summary>↩ Tool result · `toolu_01VT6C83bZ9p6Ff61R7tvWYW`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline abstract"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"Vincent Vanhoucke's Post","url":"https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"}]

Based on the search results, here are the CoRL 2026 submission deadlines:

**Abstract Submission Deadline:** May 26, 2026 11:59 UTC

**Paper Submission Deadline:** May 29, 2026 11:59 UTC

The conference itself will be held November 9-12, 2026 in Austin, Texas, US.

It's important to note that the deadlines are final, and accommodations cannot be made for missing the abstract deadline or paper deadline. Additionally, authors may update the title and abstract on OpenReview after the abstract submission deadline, however, authors cannot be added or removed after this deadline, as this information is required to facilitate reviewer assignments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a07d2d0b-64e0-4fc6-8c90-475d403973ef",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "7133a878-0180-4d23-b381-ced35a2551a8",
  "sourceToolAssistantUUID": "a07d2d0b-64e0-4fc6-8c90-475d403973ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T18:58:48.762Z_

Now let me do a few follow-up searches to get more details on the most directly competitive work -- particularly the asynchronous denoising paper and the TACA cross-modal attention rebalancing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7133a878-0180-4d23-b381-ced35a2551a8",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQEpsLP2ZY2TvcCMjyZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ece14aea-b029-4128-bf50-2a208b533858",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsgNs91PGdUPe8h4iyTLUv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 19211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 665,
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

_source line 28 · 2026-05-10T18:58:49.459Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bp4ybiy9L9Z3kvvyvQAR6v`</summary>

```json
{
  "query": "asynchronous denoising independent noise schedules video action world model arxiv 2604.26694"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ece14aea-b029-4128-bf50-2a208b533858",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQEpsLP2ZY2TvcCMjyZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28f11c4e-520f-4004-be58-23c118650183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsgNs91PGdUPe8h4iyTLUv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 19211,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 665
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 19211,
          "cache_creation_input_tokens": 665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 665,
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

_source line 29 · 2026-05-10T18:58:58.852Z_

<details><summary>↩ Tool result · `toolu_01Bp4ybiy9L9Z3kvvyvQAR6v`</summary>

```text
Web search results for query: "asynchronous denoising independent noise schedules video action world model arxiv 2604.26694"

Links: [{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"Not All Frames Deserve Full Computation: Accelerating Autoregressive Video Generation via Selective Computation and Predictive Extrapolation","url":"https://arxiv.org/html/2604.02979"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Request PDF","url":"https://www.researchgate.net/publication/395371959_Unified_World_Models_Coupling_Video_and_Action_Diffusion_for_Pretraining_on_Large_Robotic_Datasets"},{"title":"AR-Diffusion: Asynchronous Video Generation with Auto-Regressive Diffusion","url":"https://arxiv.org/html/2503.07418v1"},{"title":"A Systematic Post-Train Framework for Video Generation","url":"https://arxiv.org/html/2604.25427"},{"title":"Unified Video Action Model","url":"https://arxiv.org/html/2503.00200"},{"title":"A Comprehensive Review on Noise Control of Diffusion Model","url":"https://arxiv.org/html/2502.04669v1"},{"title":"Asynchronous Denoising Diffusion Models for Aligning Text-to-Image Generation","url":"https://arxiv.org/html/2510.04504"}]

Based on the web search results, I found information about the paper with arxiv ID 2604.26694. Here's what the search revealed:

The paper is titled "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising" by Guo, Jun and colleagues, published on arXiv as arXiv:2604.26694.

## Key Contributions:

X-WAM is a unified 4D World Action Model that simultaneously targets high-fidelity video generation, 3D spatial reconstruction, and real-time policy execution.

The paper introduces two main technical innovations:

1. **Lightweight Depth Adaptation**: The model replicates the final few DiT blocks into a dedicated depth branch that runs in an interleaved fashion with the main RGB branch, where the depth branch reads from the main branch via cross-attention but does not affect it, preserving pretrained visual priors while enabling high-quality spatial reconstruction.

2. **Asynchronous Noise Sampling (ANS)**: ANS is proposed to jointly optimize generation quality and action decoding efficiency by applying a specialized asynchronous denoising schedule during inference, which rapidly decodes actions with fewer steps to enable efficient real-time execution, while dedicating the full sequence of steps to generate high-fidelity video. Additionally, to align training with this inference behavior, the model samples video and action noise levels from a coupled joint distribution rather than independently, ensuring the model is trained on configurations it actually encounters at test time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28f11c4e-520f-4004-be58-23c118650183",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "917cba16-50aa-4edb-bcd4-eb4c5e5b6d66",
  "sourceToolAssistantUUID": "28f11c4e-520f-4004-be58-23c118650183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-10T18:59:01.885Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AsmzbXpWhkHEw6JnVdCCuo`</summary>

```json
{
  "query": "TACA cross-modal attention rebalancing diffusion transformer 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "917cba16-50aa-4edb-bcd4-eb4c5e5b6d66",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQFpw5eQcSwbvAD8V72",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00c27ec3-1874-4db5-9d6d-2f5c0c0655d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDresTwd5HyHpXj4PqNnvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 19876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 951,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T18:59:08.351Z_

<details><summary>↩ Tool result · `toolu_01AsmzbXpWhkHEw6JnVdCCuo`</summary>

```text
Web search results for query: "TACA cross-modal attention rebalancing diffusion transformer 2026"

Links: [{"title":"TACA: Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://arxiv.org/html/2506.07986v1"},{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Lv_Rethinking_Cross-Modal_Interaction_in_Multimodal_Diffusion_Transformers_ICCV_2025_paper.pdf"},{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://arxiv.org/html/2506.07986"},{"title":"GitHub - Vchitect/TACA: TACA: Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://github.com/Vchitect/TACA"},{"title":"Paper page - Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://huggingface.co/papers/2506.07986"},{"title":"[2506.07986] Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://arxiv.org/abs/2506.07986"},{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://i.cs.hku.hk/~kykwong/publications/zlv_iccv2025_taca.pdf"},{"title":"Cross-modal Transformers","url":"https://www.emergentmind.com/topics/cross-modal-transformers"},{"title":"TACFN: Transformer-based Adaptive Cross-modal Fusion Network for Multimodal Emotion Recognition","url":"https://arxiv.org/html/2505.06536v1"},{"title":"Why Cross-Attention is the Secret Sauce of Multimodal Models | by Jakub Strawa | Medium","url":"https://medium.com/@jakubstrawadev/why-cross-attention-is-the-secret-sauce-of-multimodal-models-f8ec77fc089b"}]

Based on the search results, here's what I found about TACA:

## TACA: Temperature-Adjusted Cross-Modal Attention

TACA (Temperature-Adjusted Cross-modal Attention) is a simple yet effective modification to the attention mechanism of multimodal diffusion transformers (MM-DiT).

### Key Features

The approach introduces two key innovations: modality-specific temperature scaling and timestep-dependent adjustment of cross-modal interactions. To mitigate the suppression of cross-attention caused by the dominance of visual tokens, the method amplifies the logits of visual-text interactions through a temperature coefficient, which effectively rebalances the competition in softmax by increasing the relative weight of cross-modal interactions.

### Performance Results

For FLUX.1-Dev, incorporating TACA results in substantial improvements, yielding relative gains of 16.4% in spatial relationship understanding and 5.9% in shape accuracy. When applied to SD3.5-Medium, TACA boosts spatial relationship accuracy by 28.3% and shape accuracy by 2.9%.

### Implementation

TACA only requires a temperature coefficient that adapts to the denoising timesteps, allowing for easy implementation with minimal code modifications.

The code is publicly available on GitHub at https://github.com/Vchitect/TACA, and the research was presented as an ICCV 2025 paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00c27ec3-1874-4db5-9d6d-2f5c0c0655d7",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "ac7c677e-68ca-4f5f-8786-da5cebb5c3e6",
  "sourceToolAssistantUUID": "00c27ec3-1874-4db5-9d6d-2f5c0c0655d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-10T18:59:11.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012pa9Ha1Z61HpMX6jLpoarF`</summary>

```json
{
  "query": "noise-pair conditioned per-head attention gating diffusion transformer arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac7c677e-68ca-4f5f-8786-da5cebb5c3e6",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQGXWN7bpKdR7F6aXGw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c46b690-6735-450b-93a4-c0dd91f37ae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F1WdiDx34M6J1rvtK9uwyE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 988,
      "cache_read_input_tokens": 20827,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 988
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 20827,
          "cache_creation_input_tokens": 988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 988,
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

_source line 33 · 2026-05-10T18:59:16.891Z_

<details><summary>↩ Tool result · `toolu_012pa9Ha1Z61HpMX6jLpoarF`</summary>

```text
Web search results for query: "noise-pair conditioned per-head attention gating diffusion transformer arxiv 2026"

Links: [{"title":"Differential Gated Self-Attention","url":"https://arxiv.org/html/2505.24054"},{"title":"DGTN: Graph-Enhanced Transformer with Diffusive Attention Gating Mechanism for Enzyme Δ⁢Δ⁢𝐺 Prediction","url":"https://arxiv.org/html/2511.05483"},{"title":"1 Attention in Diffusion Model: A Survey","url":"https://arxiv.org/pdf/2504.03738"},{"title":"Analysis of Attention in Video Diffusion Transformers","url":"https://arxiv.org/html/2504.10317v1"},{"title":"[2511.05483v1] DGTN: Graph-Enhanced Transformer with Diffusive Attention Gating Mechanism for Enzyme DDG Prediction","url":"https://arxiv.org/abs/2511.05483v1"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://arxiv.org/html/2405.13762v1"},{"title":"Efficient Diffusion Transformer with Step-wise Dynamic Attention Mediators","url":"https://arxiv.org/html/2408.05710v1"},{"title":"[2405.13762] A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://arxiv.org/abs/2405.13762"},{"title":"Shared DIFF Transformer","url":"https://arxiv.org/html/2501.17900v1"},{"title":"[2506.03790] Attention-Only Transformers via Unrolled Subspace Denoising","url":"https://arxiv.org/abs/2506.03790"}]

Based on the search results, I found several papers related to diffusion transformers and attention mechanisms, but I did not find a specific paper titled exactly "noise-pair conditioned per-head attention gating diffusion transformer" on arXiv. 

However, the search results do reveal related work in this area:

1. **Differential Gated Self-Attention (2025)**: This work introduces a per-head, input-conditioned gating mechanism that dynamically fuses two parallel attention streams, enabling fine-grained, token-wise noise suppression.

2. **Other Relevant Diffusion Transformer Papers**:
   - A diffusion transformer architecture with mediator tokens that interact with query and key tokens separately, compressing redundant query-key interaction during the denoising generation process
   - A versatile diffusion transformer that applies variable diffusion timesteps across the temporal dimension and across modalities, introducing variable noise levels for various portions of the input

The search results don't contain a paper with the exact phrase "noise-pair conditioned per-head attention gating" in the query. If you're looking for a specific paper, it may be helpful to check the arXiv website directly with the exact paper ID or search for variations of the title.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c46b690-6735-450b-93a4-c0dd91f37ae3",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "5d82ee0f-f4e4-4f21-85b4-89e5b0f97872",
  "sourceToolAssistantUUID": "5c46b690-6735-450b-93a4-c0dd91f37ae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T18:59:19.185Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AKLq18GGmkCe7NwfcoWoLX`</summary>

```json
{
  "query": "AVDiT mixture of noise levels audiovisual diffusion transformer per-head gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d82ee0f-f4e4-4f21-85b4-89e5b0f97872",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQHA43xa1Msx5xVisLk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6638ebdf-aaba-4c5f-a87a-806c0869ba5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175wcoA5ZTEwF5my6W2Mer5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 21815,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 21815,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 841,
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

_source line 35 · 2026-05-10T18:59:27.043Z_

<details><summary>↩ Tool result · `toolu_01AKLq18GGmkCe7NwfcoWoLX`</summary>

```text
Web search results for query: "AVDiT mixture of noise levels audiovisual diffusion transformer per-head gating"

Links: [{"title":"A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://avdit2024.github.io/"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://arxiv.org/html/2405.13762v1"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation | OpenReview","url":"https://openreview.net/forum?id=cs1HISJkLU"},{"title":"[2405.13762] A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://arxiv.org/abs/2405.13762"},{"title":"[Quick Review] A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://liner.com/review/a-versatile-diffusion-transformer-with-mixture-of-noise-levels-for"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=AV-DiT"},{"title":"[2406.07686] AV-DiT: Efficient Audio-Visual Diffusion Transformer for Joint Audio and Video Generation","url":"https://arxiv.org/abs/2406.07686"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/15f4cefb0e143c7ad9d40e879b0a9d0c-Paper-Conference.pdf"},{"title":"[Literature Review] A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://www.themoonlight.io/en/review/a-versatile-diffusion-transformer-with-mixture-of-noise-levels-for-audiovisual-generation"},{"title":"A versatile diffusion transformer with mixture of noise levels for audiovisual generation | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738294"}]

I found information about AVDiT and the Mixture of Noise Levels (MoNL) approach. Here's a summary of the research:

## AVDiT with Mixture of Noise Levels

AVDiT trained with Mixture of Noise Levels (MoNL) tackles diverse audiovisual generation tasks in a single model.

### Core Innovation

The novel mixture of noise levels effectively learns arbitrary conditional distributions in the audiovisual space by applying variable noise levels across the temporal dimension and across modalities of the inputs. The key contribution lies in how the diffusion timestep is parameterized in the forward diffusion process, proposing variable diffusion timesteps across the temporal dimension and across modalities of the inputs instead of using the standard fixed diffusion timestep.

### Model Architecture

MoNL is implemented in the low-dimensional latent space learned by MAGVIT-v2 for video and SoundStream for audio to address computational complexity of high-dimensional signals. AVDiT utilizes a transformer-based network for joint noise prediction, leveraging its ability to model multimodal data and capture complex spatiotemporal and cross-modal relationships.

### Capabilities

The capability of MoNL is assessed by evaluating cross-modal tasks (audio-to-video and video-to-audio generation), and conditioning on small portions (audiovisual continuation and interpolation tasks). The proposed approach surpasses baselines in generating temporally and perceptually consistent samples conditioned on the input.

Regarding the "per-head gating" aspect of your query—the search results don't specifically mention per-head gating mechanisms in the AVDiT architecture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6638ebdf-aaba-4c5f-a87a-806c0869ba5e",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "0ee34e4b-e57b-4751-8ab4-672fb4703598",
  "sourceToolAssistantUUID": "6638ebdf-aaba-4c5f-a87a-806c0869ba5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-10T18:59:30.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Ti4ctPWUd5Jvvrpg6smGM`</summary>

```json
{
  "query": "MotuBrain H-bridge attention world action model arxiv 2604.27792"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ee34e4b-e57b-4751-8ab4-672fb4703598",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQHuS1ZF4NsrR7LxikS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "352d1464-ee06-4b70-93c9-0be15808d8bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETGipLdVLwkWXKKpF4cNYe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 22656,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 22656,
          "cache_creation_input_tokens": 1048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1048,
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

_source line 37 · 2026-05-10T18:59:37.685Z_

<details><summary>↩ Tool result · `toolu_013Ti4ctPWUd5Jvvrpg6smGM`</summary>

```text
Web search results for query: "MotuBrain H-bridge attention world action model arxiv 2604.27792"

Links: [{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Robotics Papers on X: \"MotuBrain: An Advanced World Action Model for Robot Control MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan, Hongzhe Bi, James Li, Jiabao Liu, Jingrui Pang, Kiro Jing, Louis Liu, Mengchen Cai, Rongxu Cui, Ruowen Zhao, … https://t.co/oZbprFxWT8 [𝚌𝚜.𝚁𝙾] https://t.co/s7cd8REIkf\" / X","url":"https://x.com/OWW/status/2050111551198105787"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/26497/"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/awesome-world-models"},{"title":"Motubrain: a World Action Model by Shengshu Technology and Tsinghua University","url":"https://chinaresearchcollective.substack.com/p/motubrain-a-world-action-model-by"},{"title":"[2512.13030] Motus: A Unified Latent Action World Model","url":"https://arxiv.org/abs/2512.13030"},{"title":"MotuBrain World Model Tops Two Global Benchmarks — A Breakthrough in Robot Intelligence - DeepInsightAI","url":"https://deepinsightai.io/motubrain-world-model/"},{"title":"Grounded World Model for Semantically Generalizable Planning","url":"https://arxiv.org/html/2604.11751"},{"title":"OmniVLA-RL: A Vision-Language-Action Model with Spatial Understanding and Online RL","url":"https://arxiv.org/html/2604.17706"},{"title":"Action Images: End-to-End Policy Learning via Multiview Video Generation","url":"https://arxiv.org/html/2604.06168"}]

I found detailed information about MotuBrain (arxiv 2604.27792). Here's what the paper covers:

## Overview

MotuBrain adopts UniDiffuser to jointly model and schedule video and action, and uses a three-stream Mixture-of-Transformers architecture to integrate video generation, action modeling, and language conditioning within one system.

## Key Capabilities

This unified formulation supports inference over five distributions with the same model: vision-language-action policy modeling, world modeling, video generation, inverse dynamics, and joint video-action prediction.

The model can learn from a much broader family of multimodal data, including video-only data without action labels, interaction data without explicit task language, and heterogeneous robot trajectories collected from different embodiments.

## Architectural Innovations

MotuBrain introduces a unified multiview representation supporting an arbitrary number of camera views, uses an independent text stream to couple high-level semantics with low-level control, and adopts a unified action representation across embodiments.

## Performance

On RoboTwin 2.0, MotuBrain achieves average success rates of 95%, and on WorldArena, it attains the strongest reported EWMScore. MotuBrain can be adapted to new humanoid embodiments with only 50–100 same-embodiment trajectories while retaining the ability to solve long-horizon and dexterous manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "352d1464-ee06-4b70-93c9-0be15808d8bb",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "4f93faa4-4f9c-4f8e-a50f-c84d108c91b2",
  "sourceToolAssistantUUID": "352d1464-ee06-4b70-93c9-0be15808d8bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-10T18:59:40.618Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XibzA3TuwZBXW12rG89DHZ`</summary>

```json
{
  "query": "Being-H0.7 latent world action model dual-branch attention mask egocentric arxiv 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f93faa4-4f9c-4f8e-a50f-c84d108c91b2",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQJgvD9bxqsriNFCzNM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7363ae6a-32db-48e9-9e98-bca348d44ee8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017smN4FEraVDyGBS1uQskTt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 23704,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 23704,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1129,
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

_source line 39 · 2026-05-10T18:59:47.525Z_

<details><summary>↩ Tool result · `toolu_01XibzA3TuwZBXW12rG89DHZ`</summary>

```text
Web search results for query: "Being-H0.7 latent world action model dual-branch attention mask egocentric arxiv 2605"

Links: [{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"GitHub - BeingBeyond/Being-H: Being-H is BeingBeyond's family of human-centric embodied foundation models. · GitHub","url":"https://github.com/BeingBeyond/Being-H"},{"title":"Being-H0.7: A Latent World-Action Model from ... - BeingBeyond","url":"https://research.beingbeyond.com/being-h07"},{"title":"Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization","url":"https://arxiv.org/html/2601.12993v1"},{"title":"human-motion-arxiv-daily/README.md at main · AndrewDing616/human-motion-arxiv-daily","url":"https://github.com/AndrewDing616/human-motion-arxiv-daily/blob/main/README.md"},{"title":"[2605.01694] Latent State Design for World Models under Sufficiency Constraints","url":"https://arxiv.org/abs/2605.01694"},{"title":"Deep Dual Relation Modeling for Egocentric Interac- tion Recognition","url":"https://arxiv.org/pdf/1905.13586"},{"title":"Egocentric Vision Language Planning","url":"https://arxiv.org/html/2408.05802"},{"title":"MobileEgo Anywhere: Open Infrastructure for long horizon egocentric data on commodity hardware","url":"https://arxiv.org/html/2605.05945"},{"title":"Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling","url":"https://arxiv.org/html/2605.00412"}]

I found the paper! Here are the search results for your query:

## Being-H0.7: A Latent World-Action Model from Egocentric Videos

Being-H0.7 is a latent world-action model pretrained from large-scale egocentric videos. It is trained on 200,000 hours of egocentric human videos together with 15,000 hours of robot demonstrations.

### Key Technical Features:

**Dual-Branch Architecture:**
The dual-branch design is implemented by packing both branches into a single Mixture-of-Transformers sequence with a dual-branch attention mask, which shares context computation while keeping the two reasoning pathways structurally aligned. A dual-branch attention mask is applied where shared context tokens are visible to both branches, while the prior and posterior branch tokens are not allowed to attend to each other.

**Latent Reasoning:**
Being-H0.7 introduces a small set of learnable latent queries between the multimodal context and the action tokens that attend to the instruction, observation history, and robot state, aggregate task- and interaction-relevant information, and form a compact latent state before actions are generated.

**Training and Deployment Efficiency:**
At inference, the posterior branch is removed entirely: Being-H0.7 performs no future-frame generation or pixel-space rollout before acting.

The paper is available on arXiv (2605.00078) and was published in May 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7363ae6a-32db-48e9-9e98-bca348d44ee8",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "46a3b774-e88b-457f-a411-a9f8bf1fac82",
  "sourceToolAssistantUUID": "7363ae6a-32db-48e9-9e98-bca348d44ee8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-10T18:59:51.905Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BZrgEJY2FPpHcLpxXAR3M2`</summary>

```json
{
  "query": "\"When to Trust Imagination\" adaptive action execution world action models arxiv 2605.06222"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46a3b774-e88b-457f-a411-a9f8bf1fac82",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQKR3G3iVzJ31ah2nxc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a27ad43a-10f9-41f9-8963-0025742bb5be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARfHAKEM3FiukmcefDTr4y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 926,
      "cache_read_input_tokens": 24833,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 926
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 24833,
          "cache_creation_input_tokens": 926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 926,
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

_source line 41 · 2026-05-10T19:00:00.084Z_

<details><summary>↩ Tool result · `toolu_01BZrgEJY2FPpHcLpxXAR3M2`</summary>

```text
Web search results for query: ""When to Trust Imagination" adaptive action execution world action models arxiv 2605.06222"

Links: [{"title":"[2605.06222] When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/abs/2605.06222"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling","url":"https://arxiv.org/html/2605.00412"},{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"A Comprehensive Survey on World Models for Embodied AI","url":"https://arxiv.org/html/2510.16732v1"},{"title":"ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC","url":"https://arxiv.org/html/2605.04709"},{"title":"[2105.05716v2] Acting upon Imagination: when to trust imagined trajectories in model based reinforcement learning","url":"https://arxiv.org/abs/2105.05716v2"},{"title":"A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://arxiv.org/html/2511.02097v1"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"}]

I found the paper! Here's the information about "When to Trust Imagination: Adaptive Action Execution for World Action Models" (arXiv 2605.06222):

## Summary

This paper, authored by Rui Wang, Yue Zhang, Jiehong Lin, Kuncheng Luo, Jianan Wang, Zhongrui Wang, and Xiaojuan Qi, addresses World Action Models (WAMs) which have recently emerged as a promising paradigm for robotic manipulation by jointly predicting future visual observations and future actions.

## The Problem

Current WAMs typically execute a fixed number of predicted actions after each model inference, leaving the robot blind to whether the imagined future remains consistent with the actual physical rollout.

## The Solution

The paper formulates adaptive WAM execution as a future-reality verification problem: the robot should execute longer when the WAM-predicted future remains reliable, and replan earlier when reality deviates from imagination. The proposed method is called Future Forward Dynamics Causal Attention (FFDC), a lightweight verifier that jointly reasons over predicted future actions, predicted visual dynamics, real observations, and language instructions to estimate whether the remaining action rollout can still be trusted.

## Results

Experiments on the RoboTwin benchmark and in the real world demonstrate that the method achieves a strong robustness-efficiency trade-off: on RoboTwin, it reduces WAM forward passes by 69.10% and execution time by 34.02%, while improving success rate by 2.54% over the short-chunk baseline; in real-world experiments, it improves success rate by 35%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a27ad43a-10f9-41f9-8963-0025742bb5be",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "91020e65-129a-41a6-bc2a-d94d5205f18a",
  "sourceToolAssistantUUID": "a27ad43a-10f9-41f9-8963-0025742bb5be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T19:00:07.442Z_

Now let me do one final targeted search to make sure we haven't missed the most directly competitive work -- specifically something that conditions attention gates on noise-level pairs in a WAM.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91020e65-129a-41a6-bc2a-d94d5205f18a",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQLLiLdihupS5feWVHg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e40145c7-dc08-405e-8914-9e3e930828ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjxXb7921LYDB57xLFteUw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 908,
      "cache_read_input_tokens": 25759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 908,
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

_source line 43 · 2026-05-10T19:00:07.785Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F9CfGuRSiYuebSRVr8zRmx`</summary>

```json
{
  "query": "learned attention gate noise schedule diffusion action video robot manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e40145c7-dc08-405e-8914-9e3e930828ac",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQLLiLdihupS5feWVHg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44974fa4-3635-4fbd-b524-9bf10485066a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjxXb7921LYDB57xLFteUw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 908,
      "cache_read_input_tokens": 25759,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 908
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 25759,
          "cache_creation_input_tokens": 908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 908,
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

_source line 44 · 2026-05-10T19:00:15.692Z_

<details><summary>↩ Tool result · `toolu_01F9CfGuRSiYuebSRVr8zRmx`</summary>

```text
Web search results for query: "learned attention gate noise schedule diffusion action video robot manipulation 2026"

Links: [{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation","url":"https://arxiv.org/html/2503.07135v2"},{"title":"Diffusion Policy: Teaching Robots to Act by Denoising","url":"https://vizuara.substack.com/p/diffusion-policy-teaching-robots"},{"title":"LEARNING TO ACT FROM ACTIONLESS VIDEOS THROUGH DENSE CORRESPONDENCES","url":"https://flow-diffusion.github.io/AVDC.pdf"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Video Generators are Robot Policies - Columbia University","url":"https://videopolicy.cs.columbia.edu/assets/video_policy.pdf"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"}]

The search has returned comprehensive results on diffusion models for robot manipulation. Here's a summary of the key findings:

## Diffusion Models in Robot Manipulation

Diffusion generative models have demonstrated remarkable success in visual domains such as image and video generation and have recently emerged as a promising approach in robotics, especially in robot manipulations.

### Architecture and Components

Transformers are commonly used as the denoising network, with a history of observations, the current denoising time step, and the (partially denoised) action as input tokens, with additional conditions integrated via self-and cross-attention. The more commonly used model is a multi-head cross-attention transformer as the denoising network.

### Video and Action Generation

VidBot is a framework that enables zero-shot robotic manipulation using learned 3D affordance from in-the-wild monocular RGB-only human videos, extracting explicit representations like 3D hand trajectories and combining depth foundation models with structure-from-motion techniques.

### Noise Scheduling

The cosine_beta_schedule function computes a noise schedule where the amount of noise added at each step follows a cosine curve, giving a smoother transition than a linear schedule.

### Diffusion Policy Framework

Diffusion Policy represents a robot's visuomotor policy as a conditional denoising diffusion process that learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference.

The search results contain recent research from 2025-2026 covering the latest developments in applying diffusion models to robotic manipulation tasks with action prediction from video data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44974fa4-3635-4fbd-b524-9bf10485066a",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "3fd070c5-f94e-44e7-bf53-8747776091e8",
  "sourceToolAssistantUUID": "44974fa4-3635-4fbd-b524-9bf10485066a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-10T19:00:18.323Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MtGwSs7UD2DePuBhzmbNXq`</summary>

```json
{
  "query": "LIBERO-Plus current state of the art success rate 2026 WAM VLA benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fd070c5-f94e-44e7-bf53-8747776091e8",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQMVTUWmL5kc7CZNkUG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "337d11ab-8b47-4127-aaec-814e4a1b5edb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbpNcVLqohn4TjBweJaQ54",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 26667,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1007
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 26667,
          "cache_creation_input_tokens": 1007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1007,
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

_source line 46 · 2026-05-10T19:00:23.930Z_

<details><summary>↩ Tool result · `toolu_01MtGwSs7UD2DePuBhzmbNXq`</summary>

```text
Web search results for query: "LIBERO-Plus current state of the art success rate 2026 WAM VLA benchmark"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]","url":"https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"}]

Based on the search results, here's what I found regarding LIBERO-Plus and WAM performance on the benchmark in 2026:

## LIBERO-Plus Benchmark Overview

LIBERO-Plus is an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, created to evaluate Vision-Language-Action (VLA) models under systematically varied conditions.

## WAM Success Rates on LIBERO-Plus

Regarding World Action Models (WAMs) performance, Cosmos-Policy achieved 82.2% success rate on LIBERO-Plus. This appears to represent a current state-of-the-art result for WAMs on this benchmark as of 2026.

For additional context, Cosmos-Policy demonstrated high robustness with 96.5% in light perturbations, 92.7% in noise perturbations, and 82.2% in layout perturbations on LIBERO-Plus.

## Key Findings About VLA Models

It's important to note that VLA models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations, which is why robust benchmarks like LIBERO-Plus are essential for understanding true model capabilities beyond headline numbers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "337d11ab-8b47-4127-aaec-814e4a1b5edb",
  "isSidechain": true,
  "promptId": "487ab960-dd01-4e39-b073-0997612b1c41",
  "agentId": "abfdef84665fcf466",
  "type": "user",
  "uuid": "8952a3fa-c404-4ffa-8d0a-6cf30de66b08",
  "sourceToolAssistantUUID": "337d11ab-8b47-4127-aaec-814e4a1b5edb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-10T19:01:38.790Z_

Here is a comprehensive report on all 10 searches:

---

## Search Results Summary

### 1. EA-WM (Event-Aware World Model) -- CONFIRMED EXISTS

**Paper:** [EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields](https://arxiv.org/html/2605.06192v1) (arXiv 2605.06192, May 2026)

**Key contribution:** Uses "event-saliency gating" via an Event-Difference Latent Supervision (EDLS) mechanism. The event gate modulates the strength of bidirectional cross-attention, forcing the model to dynamically allocate attention to regions undergoing state transitions and interaction dynamics. It also constructs Kinematic-to-Visual Action Fields (KVAFs) for precise spatial geometry.

**Relevance to your proposal:** EA-WM's event gate modulates cross-attention strength, but it is conditioned on *spatial event saliency* (temporal differences), NOT on noise-level pairs (t_o, t_a). It is a content-driven gate, not a denoising-schedule-driven gate. Your per-head noise-pair conditioning remains distinct.

---

### 2. CKT-WAM (Parameter-Efficient Adapter) -- CONFIRMED EXISTS

**Paper:** [CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models](https://arxiv.org/html/2605.06247v1) (arXiv 2605.06247, May 2026)

**Key contribution:** Routes compact context tokens from a teacher WAM into a student WAM's text conditioning pathway. Achieves 86.1% total success on LIBERO-Plus with only 1.17% trainable parameters, and 83.3% average real-world success across four multi-step tasks.

**Relevance:** This is about transfer/adaptation efficiency, not about attention gating. Orthogonal to your proposal -- could actually be combined with noise-pair gating.

---

### 3. OA-WAM (Object-Addressable WAM) -- CONFIRMED EXISTS

**Paper:** [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/html/2605.06481v1) (arXiv 2605.06481, May 2026)

**Key contribution:** Decomposes frames into N+1 slot states (1 robot + N objects), each with a frozen identity "address" vector and a time-varying content vector. Cross-slot attention is routed through address-only keys. Achieves 97.8% on LIBERO, 79.3% on SimplerEnv, and new SOTA on geometric LIBERO-Plus axes.

**Relevance:** OA-WAM modifies *what* attention attends to (object-addressable slots), not *how much* attention flows as a function of noise level. Complementary to your approach.

---

### 4. VAG (Dual-Stream Video-Action Generation) -- CONFIRMED EXISTS

**Paper:** [VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis](https://arxiv.org/abs/2604.09330) (arXiv 2604.09330, April 2026)

**Key contribution:** A unified flow-matching-based dual-stream framework that jointly generates video and action under visual and language conditioning. Addresses the problem that existing WMs lack paired action trajectories, and two-stage pipelines introduce error accumulation.

**Relevance:** VAG uses flow matching (not diffusion) with a dual-stream design. It does not appear to introduce noise-pair-conditioned attention gating. It is a data synthesis framework rather than a policy architecture, though the dual-stream concept is related.

---

### 5. Noise-Level Conditioned Attention Gating in WAMs -- NO EXACT MATCH FOUND

No paper specifically doing "noise-level conditioned attention gating" within WAMs was found. However, the closest related work is:

- **X-WAM (arXiv 2604.26694):** Uses Asynchronous Noise Sampling (ANS) where video and action noise levels are sampled from a *coupled joint distribution* rather than independently. This is the most directly relevant prior work -- it acknowledges that the relationship between video and action noise levels matters, but it uses this for *inference scheduling* (fewer action denoising steps), NOT for learned per-head attention gating.

- **MotuBrain (arXiv 2604.27792):** Uses a three-stream Mixture-of-Transformers with "H-bridge attention" design, but this is a fixed architectural pattern, not noise-conditioned.

**Critical finding for your proposal:** X-WAM's ANS samples (t_o, t_a) from a joint distribution, which is conceptually close to your noise-pair conditioning. However, X-WAM uses this to determine *how many* denoising steps each modality gets, not to dynamically gate attention *within* the transformer layers. Your learned per-head gating conditioned on the noise pair is a distinct mechanism.

---

### 6. Adaptive Attention Conditioned on Noise/Timestep in Diffusion Models -- RELATED WORK EXISTS

Several relevant pieces of prior art:

- **TACA (ICCV 2025):** Temperature-Adjusted Cross-modal Attention for MM-DiT. Introduces modality-specific temperature scaling AND timestep-dependent adjustment of cross-modal interactions. 16.4% improvement in spatial relationship understanding. This is the closest existing mechanism to your proposal in the image generation domain -- it adjusts cross-modal attention strength based on timestep. However, it uses a single scalar temperature (not per-head gates), operates on text-image (not video-action), and doesn't handle independent noise levels for two denoised modalities.

- **AVDiT / MoNL (NeurIPS 2024):** Mixture of Noise Levels for audiovisual generation. Applies variable noise levels across modalities. This establishes the idea of independent noise schedules per modality but does not introduce per-head attention gating conditioned on the noise pair.

- **Dynamic Diffusion Transformer (ICLR 2025):** Timestep-wise Dynamic Width (TDW) -- adjusts width of attention/MLP blocks based on timestep. Single-modality focus.

**Key gap your proposal fills:** None of these combine (a) per-head granularity, (b) conditioning on a *pair* of noise levels from two independently denoised streams, and (c) application to WAMs for robotics.

---

### 7. Most Directly Competitive Work -- X-WAM IS THE CLOSEST

Based on all searches, **X-WAM (arXiv 2604.26694, "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising")** is the most directly competitive work. It:
- Jointly models video and action denoising
- Uses independent/asynchronous noise schedules for video vs. action
- Samples noise levels from a coupled joint distribution

However, X-WAM's innovation is at the *inference scheduling* level (asynchronous denoising steps), not at the *attention mechanism* level. It does NOT learn per-head gates conditioned on (t_o, t_a). Your proposal operates at a finer granularity (per-head, within the transformer) and is learned end-to-end.

**TACA** is also competitive conceptually (timestep-dependent cross-modal attention adjustment) but operates in a different domain (text-to-image) and uses scalar temperature, not per-head gating.

---

### 8. "Do World Action Models Generalize Better than VLAs?" -- CONFIRMED EXISTS

**Paper:** [Do World Action Models Generalize Better than VLAs? A Robustness Study](https://arxiv.org/html/2603.22078v1) (arXiv 2603.22078, March 2026)

**Key findings:**
- WAMs show strong robustness advantage over VLAs on visual perturbations
- LingBot-VA: 74.2% on RoboTwin 2.0-Plus; Cosmos-Policy: 82.2% on LIBERO-Plus
- LingBot-VA achieves 89.0% under light, 80.9% under noise, 87.9% under layout perturbations
- VLAs like pi-0.5 can match on certain tasks but require extensive diverse training data
- The robustness advantage is "highly consistent across visually-based perturbations"

**Relevance:** This paper provides the motivation for improving WAMs -- they already generalize better than VLAs, and attention gating could further improve this advantage.

---

### 9. LIBERO-PRO Benchmark -- CONFIRMED EXISTS

**Paper:** [LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](https://arxiv.org/abs/2510.03827) (arXiv 2510.03827, October 2025)

**Key findings:**
- Models achieving >90% on standard LIBERO collapse to **0.0%** under LIBERO-PRO's generalized setting
- Exposes reliance on rote memorization of action sequences and environment layouts
- Models persist in grasping when target objects are replaced; outputs unchanged with corrupted instructions
- Related benchmark: **LIBERO-Plus** (arXiv 2510.13626) tests 7 perturbation dimensions with 10,030 tasks

**Current SOTA on LIBERO-Plus:** Cosmos-Policy at 82.2% (WAM); CKT-WAM at 86.1%; OA-WAM at 97.8% on standard LIBERO, competitive on LIBERO-Plus geometric axes.

---

### 10. CoRL 2026 Deadline -- CONFIRMED

- **Abstract deadline: May 26, 2026, 11:59 UTC**
- **Paper deadline: May 29, 2026, 11:59 UTC**
- **Conference: November 9-12, 2026, Austin, Texas**
- Deadlines are firm; no extensions. Authors cannot be added/removed after abstract deadline.

You have **16 days** until the abstract deadline.

---

## Bottom Line on Novelty

**Your proposed mechanism -- learned per-head attention gating conditioned on (t_o, t_a) noise pairs -- has NOT been done.** The closest work is:

1. **X-WAM** (April 2026): couples video/action noise levels via joint sampling for asynchronous inference scheduling, but does not gate attention per-head based on noise pairs.
2. **TACA** (ICCV 2025): timestep-dependent cross-modal attention temperature scaling in MM-DiT, but uses a single scalar (not per-head), single timestep (not noise pairs), and targets image generation (not WAMs).
3. **EA-WM** (May 2026): event-saliency gating of cross-attention, but conditioned on spatial content, not noise levels.
4. **AVDiT/MoNL** (NeurIPS 2024): independent noise levels per modality, but no attention gating mechanism.

Your novelty claim appears solid, but you MUST cite X-WAM and TACA as the nearest related work, and clearly articulate the distinction: X-WAM conditions inference scheduling on noise pairs, TACA conditions attention on single timesteps -- you condition per-head attention gates on noise *pairs* within the transformer, which is a finer-grained and more expressive mechanism.

Sources:
- [EA-WM: Event-Aware Generative World Model](https://arxiv.org/html/2605.06192v1)
- [CKT-WAM: Parameter-Efficient Context Knowledge Transfer](https://arxiv.org/html/2605.06247v1)
- [OA-WAM: Object-Addressable World Action Model](https://arxiv.org/html/2605.06481v1)
- [VAG: Dual-Stream Video-Action Generation](https://arxiv.org/abs/2604.09330)
- [X-WAM: Unified 4D World Action Modeling with Asynchronous Denoising](https://arxiv.org/html/2604.26694v2)
- [MotuBrain: An Advanced World Action Model](https://arxiv.org/html/2604.27792v2)
- [Being-H0.7: A Latent World-Action Model](https://arxiv.org/html/2605.00078v1)
- [When to Trust Imagination: Adaptive Action Execution for WAMs](https://arxiv.org/abs/2605.06222)
- [TACA: Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers](https://arxiv.org/html/2506.07986v1)
- [AVDiT: Mixture of Noise Levels for Audiovisual Generation](https://arxiv.org/abs/2405.13762)
- [Do World Action Models Generalize Better than VLAs?](https://arxiv.org/html/2603.22078v1)
- [LIBERO-PRO: Robust and Fair Evaluation Beyond Memorization](https://arxiv.org/abs/2510.03827)
- [LIBERO-Plus: In-depth Robustness Analysis of VLAs](https://arxiv.org/abs/2510.13626)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Homepage](https://www.corl.org/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8952a3fa-c404-4ffa-8d0a-6cf30de66b08",
  "isSidechain": true,
  "agentId": "abfdef84665fcf466",
  "requestId": "req_011CauQN6f46ZtSe1xwvfhVA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b228f21c-ef2f-4778-b6ba-24924d8d15d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1526abb1-5686-488f-90f2-4dba47e32913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XR6r9xrDEwnryRiBa4Kyd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 27674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 907,
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
