# Research conversation: Search the web for the latest papers (2025-2026) on adaptive data curation / prioritized sampling for Vision-Language-Ac

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac555c0a3dba11f91.jsonl`
- **Structured JSON:** [`839287f908725c264bfd.json`](../../sessions/83/839287f908725c264bfd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-13T18:20:59.334Z_

Search the web for the latest papers (2025-2026) on adaptive data curation / prioritized sampling for Vision-Language-Action (VLA) model training. I need to know:

1. Search: "VLA training data curation 2026 site:arxiv.org"
2. Search: "action chunk loss decomposition VLA"
3. Search: "EMMA AdaMix VLA hard sample aware training"
4. Search: "chunk-decomposed adaptive prioritization VLA"
5. Search: "prioritized experience replay supervised fine-tuning 2026"

For each search, report what you find — paper titles, dates, key contributions. I'm particularly interested in anything published since April 2026 that might be concurrent/competing work to a method called "CDAP" (Chunk-Decomposed Adaptive Prioritization) for VLA training. Report in under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "ac555c0a3dba11f91",
  "type": "user",
  "uuid": "9312ac9e-2eb7-458e-87c9-a5ed6d280e74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T18:20:59.338Z_

```json
{
  "parentUuid": "9312ac9e-2eb7-458e-87c9-a5ed6d280e74",
  "isSidechain": true,
  "agentId": "ac555c0a3dba11f91",
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
  "uuid": "59754759-5323-4ddb-9dc2-85583d30642f",
  "timestamp": "2026-05-13T18:20:59.338Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T18:21:02.210Z_



I'll run all five web searches in parallel to gather the latest information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59754759-5323-4ddb-9dc2-85583d30642f",
  "isSidechain": true,
  "agentId": "ac555c0a3dba11f91",
  "requestId": "req_011Cb12nYLX1aFpWR8yubUUN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b483478-b3b7-49a6-9693-cbc9dceefcc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyFwCKgRic2YfbvVwLjEZt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8969,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8969,
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

_source line 4 · 2026-05-13T18:21:02.306Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01U8hQvnxTsG2FpGSeTuruni`</summary>

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
  "parentUuid": "0b483478-b3b7-49a6-9693-cbc9dceefcc1",
  "isSidechain": true,
  "agentId": "ac555c0a3dba11f91",
  "requestId": "req_011Cb12nYLX1aFpWR8yubUUN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "770cda61-54c3-49c8-8f94-49519f8ed214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyFwCKgRic2YfbvVwLjEZt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8969,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8969,
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

### Tool result

_source line 5 · 2026-05-13T18:21:02.316Z_

<details><summary>↩ Tool result · `toolu_01U8hQvnxTsG2FpGSeTuruni`</summary>

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
  "parentUuid": "770cda61-54c3-49c8-8f94-49519f8ed214",
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "ac555c0a3dba11f91",
  "type": "user",
  "uuid": "6d50e509-c245-4387-bf8a-efe2c5f04921",
  "sourceToolAssistantUUID": "770cda61-54c3-49c8-8f94-49519f8ed214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T18:21:05.179Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d50e509-c245-4387-bf8a-efe2c5f04921",
  "isSidechain": true,
  "agentId": "ac555c0a3dba11f91",
  "requestId": "req_011Cb12nmU3zdXZjaiGHuxrc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c6a7fd5-83d5-4255-a728-18328f619937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJmGvzXfheP1jXSLFjER1x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 7 · 2026-05-13T18:21:05.657Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TrPxPutC4iVjKS4jR7Aaid`</summary>

```json
{
  "query": "VLA training data curation 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c6a7fd5-83d5-4255-a728-18328f619937",
  "isSidechain": true,
  "agentId": "ac555c0a3dba11f91",
  "requestId": "req_011Cb12nmU3zdXZjaiGHuxrc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e4d370c-893e-48d2-b5f2-4800f2543be1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJmGvzXfheP1jXSLFjER1x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 8 · 2026-05-13T18:21:06.249Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gquw9e9JZ8Fs1gudTefbc8`</summary>

```json
{
  "query": "action chunk loss decomposition VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e4d370c-893e-48d2-b5f2-4800f2543be1",
  "isSidechain": true,
  "agentId": "ac555c0a3dba11f91",
  "requestId": "req_011Cb12nmU3zdXZjaiGHuxrc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c206673-0980-45a3-ac68-7e1bb3f9b7d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJmGvzXfheP1jXSLFjER1x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 9 · 2026-05-13T18:21:06.296Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0155QnWsFmfKpkaiRrwGyKbv`</summary>

```json
{
  "query": "EMMA AdaMix VLA hard sample aware training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c206673-0980-45a3-ac68-7e1bb3f9b7d3",
  "isSidechain": true,
  "agentId": "ac555c0a3dba11f91",
  "requestId": "req_011Cb12nmU3zdXZjaiGHuxrc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b72f5f61-3783-4818-9ae1-ca1f0ecfa03d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJmGvzXfheP1jXSLFjER1x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 10 · 2026-05-13T18:21:06.575Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011aH7YrR3P8Q8pYk3KL8BVN`</summary>

```json
{
  "query": "chunk-decomposed adaptive prioritization VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b72f5f61-3783-4818-9ae1-ca1f0ecfa03d",
  "isSidechain": true,
  "agentId": "ac555c0a3dba11f91",
  "requestId": "req_011Cb12nmU3zdXZjaiGHuxrc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e8442da-747b-4cc7-be33-18cf4bcdf5b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJmGvzXfheP1jXSLFjER1x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 11 · 2026-05-13T18:21:06.691Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Acvpt4v2LVSrpaS1TuHEJ`</summary>

```json
{
  "query": "prioritized experience replay supervised fine-tuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e8442da-747b-4cc7-be33-18cf4bcdf5b4",
  "isSidechain": true,
  "agentId": "ac555c0a3dba11f91",
  "requestId": "req_011Cb12nmU3zdXZjaiGHuxrc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e8c954b-5fb6-4378-bf4d-166a4ebade8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJmGvzXfheP1jXSLFjER1x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8969,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1409
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 254,
          "cache_read_input_tokens": 8969,
          "cache_creation_input_tokens": 1409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1409,
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

_source line 12 · 2026-05-13T18:21:12.685Z_

<details><summary>↩ Tool result · `toolu_0155QnWsFmfKpkaiRrwGyKbv`</summary>

```text
Web search results for query: "EMMA AdaMix VLA hard sample aware training"

Links: [{"title":"EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer","url":"https://arxiv.org/html/2509.22407v1"},{"title":"EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer | OpenReview","url":"https://openreview.net/forum?id=4eKEAeY6Tz"},{"title":"EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer","url":"https://www.catalyzex.com/paper/emma-generalizing-real-world-robot"},{"title":"Paper page - EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer","url":"https://huggingface.co/papers/2509.22407"},{"title":"EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer | Request PDF","url":"https://www.researchgate.net/publication/395943549_EMMA_Generalizing_Real-World_Robot_Manipulation_via_Generative_Visual_Transfer"},{"title":"[2509.22407] EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer","url":"https://arxiv.org/abs/2509.22407"},{"title":"AdaMix: Adaptive Resampling of Multiscale Object Mixup for Lidar Data Augmentation | Request PDF","url":"https://www.researchgate.net/publication/381172953_AdaMix_Adaptive_Resampling_of_Multiscale_Object_Mixup_for_Lidar_Data_Augmentation"},{"title":"What Is VLa Max and How Is It Used in Training?","url":"https://www.trainingpeaks.com/coach-blog/what-is-vla-max/"},{"title":"Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.695/"},{"title":"(PDF) AdaMix: Mixture-of-Adapter for Parameter-efficient Tuning of Large Language Models","url":"https://www.researchgate.net/publication/360859364_AdaMix_Mixture-of-Adapter_for_Parameter-efficient_Tuning_of_Large_Language_Models"}]

Based on the search results, here's what I found about EMMA, AdaMix, and VLA hard sample aware training:

## EMMA: Embodied Manipulation Media Adaptation

EMMA is a VLA policy enhancement framework that integrates a generative data engine with an effective training pipeline. The framework introduces DreamTransfer, a diffusion Transformer-based framework for generating multi-view consistent, geometrically grounded embodied manipulation videos.

## AdaMix: Hard-Sample-Aware Training Strategy

AdaMix is a hard-sample-aware training strategy that dynamically reweights training data based on policy performance. Unlike uniform sampling schemes that treat all samples equally, AdaMix continuously identifies challenging scenarios, particularly those in the long tail where policies typically struggle, and by up-weighting these hard samples during training, AdaMix achieves improved generalization.

The strategy evaluates the quality of predicted trajectories from the VLA policy and uses the performance score to drive an adaptive sampling mechanism.

## Performance Results

In real-world robotic tasks with zero-shot visual settings, the framework achieves a relative performance increase of over 92% compared to training with real data alone, and improves by an additional 17% with AdaMix.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b72f5f61-3783-4818-9ae1-ca1f0ecfa03d",
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "ac555c0a3dba11f91",
  "type": "user",
  "uuid": "c3beef27-a19f-4101-81b8-58e5128e0ea1",
  "sourceToolAssistantUUID": "b72f5f61-3783-4818-9ae1-ca1f0ecfa03d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T18:21:13.460Z_

<details><summary>↩ Tool result · `toolu_01Gquw9e9JZ8Fs1gudTefbc8`</summary>

```text
Web search results for query: "action chunk loss decomposition VLA"

Links: [{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning","url":"https://arxiv.org/html/2509.25718"},{"title":"Action Chunking for Robotics and AV | Igl's Blog","url":"https://www.maximilianigl.com/blog/action-chunking"},{"title":"Real-Time Execution of Action Chunking Flow Policies Kevin Black1,2,","url":"https://www.pi.website/download/real_time_chunking.pdf"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks | OpenReview","url":"https://openreview.net/forum?id=y5SGBsndWv"},{"title":"VLA Knows Its Limits","url":"https://arxiv.org/html/2602.21445v1"},{"title":"Mixture of Horizons in Action Chunking","url":"https://timsty1.github.io/moh/"},{"title":"GigaBrain-0: VLA Model for Robotic Autonomy","url":"https://www.emergentmind.com/topics/gigabrain-0"},{"title":"[2601.15197v1] BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://arxiv.org/abs/2601.15197v1"},{"title":"LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://arxiv.org/html/2601.15197"}]

Based on the search results, here's what I found about action chunk loss decomposition in Vision-Language-Action (VLA) models:

## Overview of Action Chunks in VLAs

VLA models often predict action chunks to improve efficiency and temporal coherence, where consecutive actions are aggregated into action chunks, increasing the effective density of informative feedback.

## Key Approaches to Action Chunk Loss

**Action-Chunked PPO with Self Behavior Cloning:**
An action-chunked PPO algorithm with self-generated demonstrations has been introduced for post-training VLA models, with an auxiliary behavior cloning loss applied alongside the RL objective. The relative weight between the action-chunked PPO objective and the self behavior clone auxiliary loss is adapted online to stabilize the post-training process.

**Loss Decomposition in Advanced Models:**
For example, GigaBrain-0 uses a joint loss over next-token prediction for CoT streams and a continuous flow-matching loss for action vector prediction.

## Challenge: The Horizon Problem

A significant challenge in action chunk loss decomposition involves determining the optimal execution horizon. VLA models' performance is sensitive to the action chunk length (horizon), with the single horizon inducing an inherent trade-off between long-term foresight and short-term precision.

## Recent Solutions

Mixture of Horizons (MoH) is a plug-and-play strategy that fuses multiple horizons within a single policy to inherit the strengths of both with minimal training or inference overhead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c206673-0980-45a3-ac68-7e1bb3f9b7d3",
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "ac555c0a3dba11f91",
  "type": "user",
  "uuid": "b97dba83-e7b8-46f6-b503-03f9886aca05",
  "sourceToolAssistantUUID": "7c206673-0980-45a3-ac68-7e1bb3f9b7d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T18:21:13.610Z_

<details><summary>↩ Tool result · `toolu_01TrPxPutC4iVjKS4jR7Aaid`</summary>

```text
Web search results for query: "VLA training data curation 2026 site:arxiv.org"

Links: [{"title":"Automated Data Curation Using GPS & NLP to Generate Instruction-Action Pairs for Autonomous Vehicle Vision-Language Navigation Datasets","url":"https://arxiv.org/html/2505.03174"},{"title":"[2602.16444] RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation","url":"https://arxiv.org/abs/2602.16444"},{"title":"A Pragmatic VLA Foundation Model","url":"https://arxiv.org/html/2601.18692"},{"title":"Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation","url":"https://arxiv.org/html/2603.08260"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.10109"},{"title":"Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures","url":"https://arxiv.org/html/2603.01063"},{"title":"[2501.05952] Scalable Vision Language Model Training via High Quality Data Curation","url":"https://arxiv.org/abs/2501.05952"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation","url":"https://arxiv.org/pdf/2509.15212"}]

I found several relevant papers from arXiv about VLA (Vision-Language-Action) training data curation from 2026. Here are the key results:

## Recent VLA Training Data Curation Papers (2026)

**1. RoboGene: Automated Task Generation Framework**
RoboGene is an agentic framework designed to automate the generation of diverse, physically plausible manipulation tasks across single-arm, dual-arm, and mobile robots, integrating diversity-driven sampling for broad task coverage, self-reflection mechanisms to enforce physical constraints, and human-in-the-loop refinement. (Submitted Feb 18, 2026)

**2. Seed2Scale: Self-Evolving Data Engine**
Seed2Scale enables large-scale data generation from as few as four initial human demonstrations, using a VLM-Guided Data Curation Pipeline that employs a lightweight VLA model for robust data collection and a pretrained VLM as a verifier to filter failed and low-quality trajectories. (March 9, 2026)

**3. LingBot-VLA: Pragmatic Foundation Model**
LingBot-VLA is developed with around 20,000 hours of real-world data from 9 popular dual-arm robot configurations, pre-trained on an extensive corpus of approximately 20,000 hours of multi-embodiment data characterized by high behavioral diversity. (February 26, 2026)

**4. ELF-VLA: Failure-Based Learning for Autonomous Driving**
ELF-VLA performs cost-effective data curation to maximize training efficiency, filtering samples to focus the agent on high-value, informative scenarios including both difficult samples where the model consistently fails and ambiguous samples where the model is most uncertain. (March 1, 2026)

All these papers emphasize automated and efficient data curation strategies to improve VLA model training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e4d370c-893e-48d2-b5f2-4800f2543be1",
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "ac555c0a3dba11f91",
  "type": "user",
  "uuid": "218c4a42-2516-4320-9592-173aabbecf9e",
  "sourceToolAssistantUUID": "9e4d370c-893e-48d2-b5f2-4800f2543be1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T18:21:14.101Z_

<details><summary>↩ Tool result · `toolu_019Acvpt4v2LVSrpaS1TuHEJ`</summary>

```text
Web search results for query: "prioritized experience replay supervised fine-tuning 2026"

Links: [{"title":"[1511.05952] Prioritized Experience Replay","url":"https://arxiv.org/abs/1511.05952"},{"title":"Understanding and Mitigating the Limitations of Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=HBlNGvIicg9"},{"title":"Prioritized Experience Replay (PER)","url":"https://apxml.com/courses/advanced-reinforcement-learning/chapter-2-deep-q-networks/prioritized-experience-replay"},{"title":"Prioritized Sequence Experience Replay","url":"https://arxiv.org/pdf/1905.12726"},{"title":"Uncertainty Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=aAxzDb0nlO"},{"title":"(PDF) Prioritized Experience Replay","url":"https://www.researchgate.net/publication/284219262_Prioritized_Experience_Replay"},{"title":"Model-augmented Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=WuEiafqdy9H"},{"title":"Prioritized Generative Replay | OpenReview","url":"https://openreview.net/forum?id=5IkDAfabuo"},{"title":"Investigating the Interplay of Prioritized Replay and Generalization","url":"https://arxiv.org/html/2407.09702v2"},{"title":"Prioritized experience replay based on dynamics priority - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10933423/"}]

Based on the search results, here's what I found regarding prioritized experience replay and supervised fine-tuning:

## Prioritized Experience Replay (PER)

Experience replay lets online reinforcement learning agents remember and reuse experiences from the past. Prioritized experience replay develops a framework for prioritizing experience, so as to replay important transitions more frequently, and therefore learn more efficiently.

Prioritized Experience Replay builds on the intuition that sampling transitions based on their significance gives preference to those from which the agent can learn the most, using the magnitude of the Temporal Difference (TD) error as a proxy for how "surprising" or informative a transition is.

## Recent Developments (2024-2026)

Several recent papers have explored variations and improvements to PER:

- Prioritized experience replay improves sample efficiency by selecting relevant transitions to update parameter estimates, and epistemic uncertainty has been proposed to guide the prioritization of transitions from the replay buffer, quantifying the uncertainty that can be reduced by learning.

- A prioritized generative replay approach constructs a conditional generative model of an agent's online memory allowing replay of high-priority data at large quantities, enabling densification of past experience with new generations that benefit from the generative model's generalization capacity, using conditional diffusion models and relevance functions.

## Supervised Fine-tuning Connection

Experience replay can be used to learn from human demonstrations (pre-filling the replay buffer with human data) allowing off-line pre-training and fine-tuning.

The search results don't reveal a specific 2026 paper combining these techniques, but show active research in both areas through 2024-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e8c954b-5fb6-4378-bf4d-166a4ebade8a",
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "ac555c0a3dba11f91",
  "type": "user",
  "uuid": "c40c7abd-41ac-4861-bd96-4e14f78847e5",
  "sourceToolAssistantUUID": "8e8c954b-5fb6-4378-bf4d-166a4ebade8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T18:21:14.477Z_

<details><summary>↩ Tool result · `toolu_011aH7YrR3P8Q8pYk3KL8BVN`</summary>

```text
Web search results for query: "chunk-decomposed adaptive prioritization VLA"

Links: [{"title":"PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation","url":"https://www.mdpi.com/2073-8994/18/3/394"},{"title":"Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding","url":"https://arxiv.org/html/2503.02310v1"},{"title":"Chunking Strategies to Improve LLM RAG Pipeline Performance | Weaviate","url":"https://weaviate.io/blog/chunking-strategies-for-rag"},{"title":"Adaptive chunking improves effective working memory capacity in a prefrontal cortex and basal ganglia circuit - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11870651/"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks | OpenReview","url":"https://openreview.net/forum?id=y5SGBsndWv"},{"title":"Chunking in RAG: Strategies for Optimal Text Splitting","url":"https://www.chitika.com/understanding-chunking-in-retrieval-augmented-generation-rag-strategies-techniques-and-applications/"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Unify VLA Paradigm: HKUST Open-Sources StarVLA Lego-Style Architecture, Drastically Reducing Reproduction Cost","url":"https://eu.36kr.com/en/p/3764865889125128"},{"title":"Real time action chunking for robot policies | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/real-time-action-chunking-for-robot-policies-4636cc085a6a"},{"title":"Time Optimal Execution of Action Chunk Policies Beyond Demonstration Speed | OpenReview","url":"https://openreview.net/forum?id=INsLvSCJ4z"}]

Based on the web search results, I found relevant information about Vision-Language-Action (VLA) models and action chunking techniques, though the exact term "chunk-decomposed adaptive prioritization VLA" doesn't appear as a single named method in the results.

However, I can provide context on related concepts:

## VLA Models and Action Chunking

Vision-Language-Action (VLA) models demonstrate remarkable potential for generalizable robotic manipulation, and their performance can be improved by integrating with action chunking, a critical technique for effective control.

## Adaptive Approaches for VLA Action Chunks

Several adaptive prioritization methods for VLA models with action chunks have been developed:

1. **Parallel Decoding Framework**: PD-VLA is the first parallel decoding framework for VLA models integrated with action chunking. This framework reformulates autoregressive decoding as a nonlinear system solved by parallel fixed-point iterations, preserving model performance with mathematical guarantees while significantly improving decoding speed.

2. **Real-time Chunk Correction**: Asynchronous Action Chunk Correction (A2C2) is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk.

3. **Prioritization Through Interaction Alignment**: VLA-IAP introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.

If you're looking for information about a specific paper or method with that exact name, it may be a very recent development or use specialized terminology that didn't appear in these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e8442da-747b-4cc7-be33-18cf4bcdf5b4",
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "ac555c0a3dba11f91",
  "type": "user",
  "uuid": "7dc72fc0-2a4d-4402-aa64-8137f9b00b63",
  "sourceToolAssistantUUID": "7e8442da-747b-4cc7-be33-18cf4bcdf5b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-13T18:21:34.085Z_

Here is a summary of findings across all five searches.

**Most relevant concurrent/competing work (2025-2026):**

1. **ELF-VLA** (arxiv, March 2026) -- "Unleashing VLA Potentials via Explicit Learning from Failures." Performs cost-effective data curation by filtering samples to focus training on hard cases (consistent failures) and ambiguous cases (high uncertainty). This is the closest competitor to a CDAP-style approach: it explicitly prioritizes informative/difficult samples during VLA fine-tuning.

2. **EMMA + AdaMix** (arxiv, Sept 2025 / ICLR-era) -- AdaMix is a hard-sample-aware training strategy that dynamically reweights VLA training data based on policy performance. It up-weights long-tail challenging scenarios, achieving a 17% boost over uniform sampling. This directly targets the same problem as CDAP (non-uniform sample prioritization for VLA), though it operates at the trajectory level rather than decomposing action chunks.

3. **Seed2Scale** (arxiv, March 2026) -- Uses a VLM-guided data curation pipeline with a pretrained VLM as a verifier to filter low-quality trajectories. More focused on data generation/filtering than loss-based prioritization.

4. **RoboGene** (arxiv, Feb 2026) -- Diversity-driven agentic framework for task generation; addresses curation at the task-design level, not the training-loss level.

**On "chunk-decomposed" loss and prioritized replay for SFT:** No paper matching the exact CDAP formulation (decomposing action-chunk loss for per-step prioritization during supervised fine-tuning) was found. Related action-chunk work (Mixture of Horizons, PD-VLA, A2C2) focuses on inference-time chunk execution, not training-time loss decomposition. Prioritized experience replay remains RL-focused; no 2026 paper was found applying it to VLA supervised fine-tuning specifically.

**Bottom line:** The two most relevant concurrent works are **ELF-VLA** (failure-aware curation) and **EMMA/AdaMix** (hard-sample reweighting). Neither decomposes the action-chunk loss itself for per-timestep prioritization, which would be CDAP's distinguishing contribution. Nothing published since April 2026 was found that directly overlaps with CDAP's specific formulation.

Sources:
- [ELF-VLA: Learning from Failures](https://arxiv.org/html/2603.01063)
- [EMMA: Generative Visual Transfer](https://arxiv.org/abs/2509.22407)
- [RoboGene: Diversity-Driven Task Generation](https://arxiv.org/abs/2602.16444)
- [Seed2Scale: Self-Evolving Data Engine](https://arxiv.org/html/2603.08260)
- [LingBot-VLA: Pragmatic Foundation Model](https://arxiv.org/html/2601.18692)
- [PD-VLA: Parallel Decoding for Action Chunking](https://arxiv.org/html/2503.02310v1)
- [VLA-IAP: Training-Free Visual Token Pruning](https://arxiv.org/html/2603.22991v1)
- [BayesianVLA: Bayesian Decomposition](https://arxiv.org/abs/2601.15197v1)
- [Scalable VLM Training via Data Curation](https://arxiv.org/abs/2501.05952)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dc72fc0-2a4d-4402-aa64-8137f9b00b63",
  "isSidechain": true,
  "agentId": "ac555c0a3dba11f91",
  "requestId": "req_011Cb12of5bsxWmM4BV4Awa1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1b35c63-a47f-4278-b5b0-564a5f2115cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAhBYbZ6JpHijcB1nxx4UH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 835,
      "cache_creation_input_tokens": 3877,
      "cache_read_input_tokens": 10378,
      "output_tokens": 863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 835,
          "output_tokens": 863,
          "cache_read_input_tokens": 10378,
          "cache_creation_input_tokens": 3877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3877,
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
