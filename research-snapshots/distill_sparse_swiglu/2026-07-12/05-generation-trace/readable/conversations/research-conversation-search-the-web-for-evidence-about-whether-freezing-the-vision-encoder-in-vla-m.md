# Research conversation: Search the web for evidence about whether freezing the vision encoder in VLA models hurts performance. Specifically: 1. 

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8b29b3dd5b66853e.jsonl`
- **Structured JSON:** [`cae91fd7bcf1a6023eb7.json`](../../sessions/ca/cae91fd7bcf1a6023eb7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-13T19:43:43.738Z_

Search the web for evidence about whether freezing the vision encoder in VLA models hurts performance. Specifically:

1. Search "OpenVLA frozen encoder performance" and "OpenVLA-OFT frozen vision encoder"
2. Search "VLA fine-tuning frozen vs unfrozen encoder"
3. Search "SigLIP DinoV2 frozen fine-tuning robot"
4. Search "OpenVLA ablation vision encoder freezing"

I need to understand: Does the CDR-VLA proposal's two-stage approach (frozen encoder for quality assessment, unfrozen for training) make sense? The prior review raised that "freezing the vision encoder leads to poor performance." I need to verify whether this is still a concern given the revised approach where the encoder is only frozen for computing quality weights, NOT for actual policy training.

Also search for "frozen encoder feature extraction quality estimation" and "representation quality scoring frozen pretrained" to see if there's precedent for using frozen encoder features for quality/scoring purposes even when the encoder is unfrozen during training.

Report findings with specific numbers and citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "fe1dd7af-778a-4ba7-a358-feacae6af7f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T19:43:43.740Z_

```json
{
  "parentUuid": "fe1dd7af-778a-4ba7-a358-feacae6af7f3",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
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
  "uuid": "94a3b22f-8720-4ee0-8f23-32aa173eeda2",
  "timestamp": "2026-05-13T19:43:43.740Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T19:43:47.257Z_



I'll conduct a comprehensive web search across all the queries you specified. Let me start by loading the WebSearch tool and then running the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94a3b22f-8720-4ee0-8f23-32aa173eeda2",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb196VJQMmzqHKFAUXpC4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af608ea6-4ba2-4dc6-8451-1c7f9a269704",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFGwYRWnKjJbZeCHd1omzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 784,
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

_source line 4 · 2026-05-13T19:43:47.820Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CPiFNDDkvtgyLHV8j3ZmjV`</summary>

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
  "parentUuid": "af608ea6-4ba2-4dc6-8451-1c7f9a269704",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb196VJQMmzqHKFAUXpC4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6275c7a-3757-4cc6-85bb-afeed2cf12df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFGwYRWnKjJbZeCHd1omzX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 8223,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 784,
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

_source line 5 · 2026-05-13T19:43:47.826Z_

<details><summary>↩ Tool result · `toolu_01CPiFNDDkvtgyLHV8j3ZmjV`</summary>

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
  "parentUuid": "e6275c7a-3757-4cc6-85bb-afeed2cf12df",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "80781e4d-744f-4a5a-8176-d0d8723912ac",
  "sourceToolAssistantUUID": "e6275c7a-3757-4cc6-85bb-afeed2cf12df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T19:43:50.328Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80781e4d-744f-4a5a-8176-d0d8723912ac",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb196noNM7772UcC7qsha",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5891397d-ea0f-4922-99e1-0ef87ed598fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqVZ8eDcbyL7AdbMSgRSZv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 9007,
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

_source line 7 · 2026-05-13T19:43:50.873Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JrA1ySNmmNc1Xu22ktLRD6`</summary>

```json
{
  "query": "OpenVLA frozen encoder performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5891397d-ea0f-4922-99e1-0ef87ed598fb",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb196noNM7772UcC7qsha",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef278aaf-77b7-414a-94db-8ed2574a62f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqVZ8eDcbyL7AdbMSgRSZv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 9007,
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

_source line 8 · 2026-05-13T19:43:51.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AVaDMV6neaUfrWEHSTEueE`</summary>

```json
{
  "query": "OpenVLA-OFT frozen vision encoder"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef278aaf-77b7-414a-94db-8ed2574a62f4",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb196noNM7772UcC7qsha",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d22a822c-7132-4cc2-af7e-a63fbf13012d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqVZ8eDcbyL7AdbMSgRSZv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 9007,
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

_source line 9 · 2026-05-13T19:43:51.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018XALv6QfkZHe7mz26hq6sC`</summary>

```json
{
  "query": "VLA fine-tuning frozen vs unfrozen encoder"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d22a822c-7132-4cc2-af7e-a63fbf13012d",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb196noNM7772UcC7qsha",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "311262f5-329b-4ad0-98c4-f13c027f830c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqVZ8eDcbyL7AdbMSgRSZv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 9007,
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

_source line 10 · 2026-05-13T19:43:52.276Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ACVQ1s81ZmVmFQf8yNPqkt`</summary>

```json
{
  "query": "SigLIP DinoV2 frozen fine-tuning robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "311262f5-329b-4ad0-98c4-f13c027f830c",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb196noNM7772UcC7qsha",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aeb85c0d-0f3b-4044-9816-32bb1ed49840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqVZ8eDcbyL7AdbMSgRSZv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 9007,
      "output_tokens": 208,
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
          "output_tokens": 208,
          "cache_read_input_tokens": 9007,
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

_source line 11 · 2026-05-13T19:43:57.102Z_

<details><summary>↩ Tool result · `toolu_01JrA1ySNmmNc1Xu22ktLRD6`</summary>

```text
Web search results for query: "OpenVLA frozen encoder performance"

Links: [{"title":"Understanding OpenVLA: A Simple Guide - Hankyu Kim","url":"https://hankyukim.com/openvla/"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://arxiv.org/html/2511.06202"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through","url":"https://arxiv.org/pdf/2511.06202"},{"title":"BitVLA: 1-bit Vision-Language-Action Models for Robotics ...","url":"https://arxiv.org/pdf/2506.07530"},{"title":"Enhancing Generalization in Vision–Language–Action Models by","url":"https://arxiv.org/pdf/2509.11417"},{"title":"openvla/prismatic/conf/vla.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/prismatic/conf/vla.py"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950"}]

Based on the search results, here's what I found about OpenVLA frozen encoder performance:

## Key Finding: Freezing the Encoder Leads to Poor Performance

Freezing the vision encoder leads to poor performance in OpenVLA, suggesting that further adaptation of the visual features to the target scene is crucial. This finding is consistent across multiple research approaches studying OpenVLA.

## Context on the Frozen Encoder Issue

While freezing vision encoders during VLM training typically leads to higher performance because a frozen vision encoder may better preserve the robust features learned from its Internet-scale pretraining, this principle does not apply well to robotic action prediction with OpenVLA.

## Research Addressing the Frozen Encoder Problem

Recent work has explored alternatives to maintain performance while keeping encoders partially frozen:

- A partially-frozen dual encoder improves OpenVLA performance from 35.03% to 55.55%, which is significantly better than full freezing but still below the best approaches.

- Fine-tuning the vision encoder versus freezing is crucial for robotic control, with "sandwich fine-tuning" (fine-tune vision encoder + LLM last layer only) achieving strong performance with moderate compute.

The consensus is that for robotics tasks specifically, OpenVLA requires fine-tuning of the vision encoder rather than keeping it frozen to achieve good performance on robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef278aaf-77b7-414a-94db-8ed2574a62f4",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "eded792c-2bf8-469c-bad2-dea177977756",
  "sourceToolAssistantUUID": "ef278aaf-77b7-414a-94db-8ed2574a62f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T19:43:57.582Z_

<details><summary>↩ Tool result · `toolu_01AVaDMV6neaUfrWEHSTEueE`</summary>

```text
Web search results for query: "OpenVLA-OFT frozen vision encoder"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://arxiv.org/html/2511.06202v2"},{"title":"BitVLA: 1-bit Vision-Language-Action Models for Robotics ...","url":"https://arxiv.org/pdf/2506.07530"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"Understanding OpenVLA: A Simple Guide - Hankyu Kim","url":"https://hankyukim.com/openvla/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"}]

Based on the search results, here's information about OpenVLA-OFT and its frozen vision encoder:

## OpenVLA-OFT Overview

OpenVLA-OFT enables 25-50x faster inference speed, higher task success rates, multiple input images, and high-frequency bimanual robot control compared to vanilla OpenVLA fine-tuning. Through parallel decoding and action chunking, OpenVLA-OFT obtains 26x faster action generation speed and 3x lower latency than the base OpenVLA model.

## Frozen Vision Encoder in Related Work

While OpenVLA-OFT itself uses specific technical approaches, research on frozen vision encoders in the OpenVLA ecosystem shows interesting findings. Only fine-tuning the network's last layer or freezing the vision encoder leads to poor performance, suggesting that further adaptation of the visual features to the target scene is crucial. 

In contrast, sandwich fine-tuning achieves better performance since it fine-tunes the vision encoder, and it consumes less GPU memory since it does not fine-tune the full LLM backbone.

Additionally, recent research has leveraged OpenVLA's frozen vision encoder for efficient memory storage: A memory-efficient buffer maintains stored extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d22a822c-7132-4cc2-af7e-a63fbf13012d",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "1516977a-ae4c-4148-ae95-74f904336c01",
  "sourceToolAssistantUUID": "d22a822c-7132-4cc2-af7e-a63fbf13012d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T19:43:58.892Z_

<details><summary>↩ Tool result · `toolu_018XALv6QfkZHe7mz26hq6sC`</summary>

```text
Web search results for query: "VLA fine-tuning frozen vs unfrozen encoder"

Links: [{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"[2512.11921] Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/abs/2512.11921"},{"title":"(PDF) Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://www.researchgate.net/publication/398721162_Towards_Accessible_Physical_AI_LoRA-Based_Fine-Tuning_of_VLA_Models_for_Real-World_Robot_Control"},{"title":"🔧 Introduction to Multimodal Learning — Part 3: Projectors and Fine-Tuning Strategies in VLMs | by Wenyi Li | Medium","url":"https://medium.com/@zdj0712/introduction-to-multimodal-learning-part-3-projectors-and-fine-tuning-strategies-in-vlms-71feaceb698d"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.11921v1"},{"title":"LLaVA Architecture: From Frozen ViT to Fine-Tuned LLM","url":"https://learnopencv.com/llava-training-a-visual-assistant/"},{"title":"Parallels Between VLA Model Post-Training and Human ...","url":"https://arxiv.org/pdf/2506.20966"},{"title":"Parallels Between VLA Model Post-Training and Human Motor Learning: Progress, Challenges, and Trends Tian-Yu Xiang, Ao-Qun Jin, Xiao-Hu Zhou, Mei-Jiang Gui, Xiao-Liang Xie, Shi-Qi Liu, Shuang-Yi Wang, Sheng-Bin Duan, Fu-Chao Xie, Wen-Kai Wang, Si-Chang Wang, and Ling-Yun Li are with the State Key Laboratory of Multimodal Artificial Intelligence Systems, Institute of Automation, Chinese Academy of Sciences, Beijing 100190, China, and also with the School of Artificial Intelligence, University of Chinese Acad","url":"https://arxiv.org/html/2506.20966"},{"title":"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/html/2605.06175v1"},{"title":"Frozen Transformers in Language Models Are Effective Visual Encoder Layers","url":"https://arxiv.org/html/2310.12973v2"}]

Based on the search results, here's an overview of the key differences between frozen and unfrozen vision encoders in VLA (Vision-Language-Action) fine-tuning:

## Frozen Vision Encoder

Freezing the vision encoder reduces computational requirements and trainable parameters but may limit adaptation to robot-specific visual characteristics. More specifically:

- The visual encoder remains frozen during fine-tuning, with only the language model and action head being adapted, requiring approximately 8.4M trainable parameters and enabling faster training with lower memory usage.
- This approach assumes that the pre-trained visual features are sufficient for the target robot's visual environment.

## Unfrozen Vision Encoder

Unfreezing allows the vision encoder to adapt to the specific camera setup and visual environment but increases computational requirements. Specifically:

- The visual encoder is fine-tuned along with the language model, requiring approximately 33M trainable parameters (8.4M for language model + action head, plus 25M for vision encoder LoRA adapters).

## Performance Trade-offs

Research on real-world robot control found that while unfrozen vision generally achieves slightly better performance (76% vs 74% success rate with 200 episodes), the improvement is modest relative to the significant computational savings of the frozen approach, and for the button-pressing task evaluated, both configurations demonstrate reliable performance when provided with sufficient training data.

The choice between these approaches depends on your computational constraints and whether you have sufficient training data to achieve good performance with the frozen encoder.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "311262f5-329b-4ad0-98c4-f13c027f830c",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "933a5b65-c33c-4386-b495-083213d1af6a",
  "sourceToolAssistantUUID": "311262f5-329b-4ad0-98c4-f13c027f830c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T19:43:59.266Z_

<details><summary>↩ Tool result · `toolu_01ACVQ1s81ZmVmFQf8yNPqkt`</summary>

```text
Web search results for query: "SigLIP DinoV2 frozen fine-tuning robot"

Links: [{"title":"GitHub - NMS05/DinoV2-SigLIP-Phi3-LoRA-VLM · GitHub","url":"https://github.com/NMS05/DinoV2-SigLIP-Phi3-LoRA-VLM"},{"title":"Learning Robust Visual Features for Object Understanding","url":"https://itcanthink.substack.com/p/learning-robust-visual-features-for"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"TraceGen: World Modeling in 3D Trace-Space Enables Learning from Cross-Embodiment Videos","url":"https://arxiv.org/html/2511.21690"},{"title":"Bombek1/ai-image-detector-siglip-dinov2 · Hugging Face","url":"https://huggingface.co/Bombek1/ai-image-detector-siglip-dinov2"},{"title":"Vision Transformers: CLIP, SigLIP, DINOv2, DINOv3 ...","url":"https://www.linkedin.com/posts/karthik-gogisetty-a6772915b_computervision-deeplearning-machinelearning-activity-7403869504721661952-57gS"},{"title":"DINOv2 is now available in HF Transformers (with tutorial) · Issue #153 · facebookresearch/dinov2","url":"https://github.com/facebookresearch/dinov2/issues/153"},{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/guides/vla-models-comparison"},{"title":"SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features","url":"https://arxiv.org/html/2502.14786v1"},{"title":"DINOv2 Meets Text: A Unified Framework for Image- and Pixel-Level Vision-Language Alignment","url":"https://arxiv.org/html/2412.16334v1"}]

Based on the search results, here's what I found about SigLIP, DinoV2, frozen fine-tuning, and robotics:

## Key Applications in Robotics

SigLIP and DinoV2 backbones are used together as a fused visual encoder in robotics models, mapping image inputs to image patch embeddings. A prominent example is OpenVLA, which is trained by fine-tuning a pretrained Prismatic-7B VLM using a dataset of 970k robot manipulation trajectories from the Open X-Embodiment dataset spanning a wide range of tasks, scenes and robot embodiments.

## Frozen Encoder Strategy

The practice of keeping these encoders frozen during training is well-established in robotics applications. When leveraging pretrained representations efficiently, all encoders (DINOv2, SigLIP, T5) are kept frozen throughout training with only the fusion layer and decoder trained, following the Prismatic VLM approach which demonstrated that finetuning visual backbones significantly degrades performance.

## Performance Benefits

The dual vision encoder (SigLIP for semantic features + DinoV2 for spatial features) gives OpenVLA stronger visual grounding than single-encoder designs. Fine-tuning requires as few as 100–200 demonstrations for a new task on a specific robot, with fine-tuned OpenVLA achieving 85–95% success on the LIBERO benchmark depending on task difficulty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aeb85c0d-0f3b-4044-9816-32bb1ed49840",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "8e2efb18-0187-4cda-9e15-ead98d9334f9",
  "sourceToolAssistantUUID": "aeb85c0d-0f3b-4044-9816-32bb1ed49840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-13T19:44:03.057Z_

Good, I'm getting useful results. Let me now run the remaining searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e2efb18-0187-4cda-9e15-ead98d9334f9",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb197dfy8zUWAUC6N5jCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "094554ef-4ced-4b4a-96e7-f4776b5b92b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKT9SXXv2fJ2RWdAtVSLay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 10432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3884,
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

_source line 16 · 2026-05-13T19:44:03.536Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015nvSSEt4mbwyZmhzVNZECj`</summary>

```json
{
  "query": "OpenVLA ablation vision encoder freezing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "094554ef-4ced-4b4a-96e7-f4776b5b92b3",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb197dfy8zUWAUC6N5jCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2358cb71-c05a-439a-9ee6-749f37ad5d17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKT9SXXv2fJ2RWdAtVSLay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 10432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3884,
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

_source line 17 · 2026-05-13T19:44:04.006Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RvMmkSGp1izqbLcYHZ2c6o`</summary>

```json
{
  "query": "frozen encoder feature extraction quality estimation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2358cb71-c05a-439a-9ee6-749f37ad5d17",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb197dfy8zUWAUC6N5jCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfa698c3-409e-4109-92ee-69afbf3ea38e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKT9SXXv2fJ2RWdAtVSLay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 10432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3884,
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

_source line 18 · 2026-05-13T19:44:04.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TgYia2Fy7fvWsud5qA7uhK`</summary>

```json
{
  "query": "representation quality scoring frozen pretrained"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfa698c3-409e-4109-92ee-69afbf3ea38e",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb197dfy8zUWAUC6N5jCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96d0aed5-8bd8-49e1-b852-0f036f78d560",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKT9SXXv2fJ2RWdAtVSLay",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 10432,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 10432,
          "cache_creation_input_tokens": 3884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3884,
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

_source line 19 · 2026-05-13T19:44:10.447Z_

<details><summary>↩ Tool result · `toolu_015nvSSEt4mbwyZmhzVNZECj`</summary>

```text
Web search results for query: "OpenVLA ablation vision encoder freezing"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models","url":"https://arxiv.org/html/2601.03309v1"},{"title":"Understanding OpenVLA: A Simple Guide - Hankyu Kim","url":"https://hankyukim.com/openvla/"},{"title":"LLaVA Architecture: From Frozen ViT to Fine-Tuned LLM","url":"https://learnopencv.com/llava-training-a-visual-assistant/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"VLA: Part 2: OpenVLA","url":"https://medium.com/@yianyao1994/vla-part-2-openvla-b631a29efecc"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"VLA-Adapter","url":"https://vla-adapter.github.io/"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"}]

Based on the search results, I found relevant information about OpenVLA's ablation studies on vision encoder freezing. Here are the key findings:

## OpenVLA Ablation Study: Vision Encoder Freezing

Freezing the vision encoder leads to poor performance, suggesting that further adaptation of the visual features to the target scene is crucial.

### Comparison of Fine-Tuning Approaches

OpenVLA researchers compared several fine-tuning approaches including: full fine-tuning (updates all weights), last layer only (fine-tunes only the last layer and token embedding), frozen vision (freezes the vision encoder but fine-tunes all other weights), sandwich fine-tuning (unfreezes the vision encoder, token embedding matrix, and last layer), and LoRA.

### Key Finding

"Sandwich fine-tuning" achieves better performance since it fine-tunes the vision encoder, and it consumes less GPU memory since it does not fine-tune the full LLM backbone.

### Why Vision Encoder Fine-Tuning Matters

Fine-tuning the vision encoder during VLA training is crucial for good VLA performance. The researchers hypothesize that the pretrained vision backbone may not capture sufficient fine-grained spatial details about important parts of the scene to enable precise robotic control.

This contrasts with vision-language models (VLMs) in general, where freezing vision encoders during VLM training typically leads to higher performance, as a frozen vision encoder may better preserve the robust features learned from its Internet-scale pretraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2358cb71-c05a-439a-9ee6-749f37ad5d17",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "60cf3d7c-7412-4252-9fc3-7ea7307716d6",
  "sourceToolAssistantUUID": "2358cb71-c05a-439a-9ee6-749f37ad5d17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T19:44:11.140Z_

<details><summary>↩ Tool result · `toolu_01RvMmkSGp1izqbLcYHZ2c6o`</summary>

```text
Web search results for query: "frozen encoder feature extraction quality estimation"

Links: [{"title":"Frozen DINOv2 Encoder","url":"https://www.emergentmind.com/topics/frozen-dinov2-encoder"},{"title":"Parameter-Efficient Quality Estimation via Frozen Recursive Models","url":"https://arxiv.org/html/2603.14593"},{"title":"Frozen Whisper Encoder Features","url":"https://www.emergentmind.com/topics/frozen-whisper-encoder-features"},{"title":"GitHub - m-bain/frozen-in-time: Frozen in Time: A Joint Video and Image Encoder for End-to-End Retrieval [ICCV'21] · GitHub","url":"https://github.com/m-bain/frozen-in-time"},{"title":"Frozen Encoders: Foundations, Applications, and Advanced Techniques | by Utsavsharma | Medium","url":"https://medium.com/@utsavsharma1990/frozen-encoders-foundations-applications-and-advanced-techniques-5b17688dd09a"},{"title":"Freezing pre-trained parameters of encoders for denoisers: Expanding pixel involvement and filtering out high-frequency noise - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S089360802600256X"},{"title":"Frozen in Time: A Joint Video and Image Encoder for End-to-End Retrieval","url":"https://openaccess.thecvf.com/content/ICCV2021/papers/Bain_Frozen_in_Time_A_Joint_Video_and_Image_Encoder_for_ICCV_2021_paper.pdf"},{"title":"Using VJEPA2 Frozen Encoder as Video Feature Extractor · Issue #120 · facebookresearch/vjepa2","url":"https://github.com/facebookresearch/vjepa2/issues/120"},{"title":"Frozen Encoder – Your Gateway to Data Mastery","url":"https://insightful-data-lab.com/2025/08/23/frozen-encoder/"},{"title":"Frozen encoder results. Using an encoder that was pre-trained by depth... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Frozen-encoder-results-Using-an-encoder-that-was-pre-trained-by-depth-significantly_fig4_359517806"}]

I've completed the web search for "frozen encoder feature extraction quality estimation." Here are the key findings:

## Overview

A frozen encoder means using a pretrained encoder model (like BERT, ResNet, or a sentence transformer) but not updating its weights during training on your task, with the encoder's parameters being fixed.

## Feature Extraction Quality

Several approaches demonstrate how frozen encoders maintain high-quality feature extraction:

- **DINOv2 Vision Encoders**: The frozen DINOv2 encoder is a vision transformer with fixed weights that extracts robust features using large-scale self-supervised learning. Frozen encoder deployments result in feature vectors with demonstrable generalization across both natural and specialized downstream domains, including pixel-level and instance-level tasks.

- **Whisper Audio Encoders**: Frozen Whisper encoder features yield state-of-the-art performance across a broad spectrum of speech tasks, from low-bitrate coding to dysarthria detection, continual learning, and speech quality prediction.

- **Quality Estimation for Translation**: Frozen pretrained embeddings match fine-tuned performance while reducing trainable parameters by 37×, with frozen XLM-R embeddings achieving a Spearman's correlation of 0.370.

## Key Advantages

Frozen features allow linear probes to reveal what information is already encoded, training is stable and requires minimal hyperparameter tuning, and strong linear-probe accuracy signals that the encoder's representations are already discriminative.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfa698c3-409e-4109-92ee-69afbf3ea38e",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "5d48b3f9-ef8b-41fe-84af-d2e9b019c570",
  "sourceToolAssistantUUID": "dfa698c3-409e-4109-92ee-69afbf3ea38e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T19:44:11.988Z_

<details><summary>↩ Tool result · `toolu_01TgYia2Fy7fvWsud5qA7uhK`</summary>

```text
Web search results for query: "representation quality scoring frozen pretrained"

Links: [{"title":"Parameter-Efficient Quality Estimation via Frozen Recursive Models","url":"https://arxiv.org/html/2603.14593"},{"title":"Lost in State Space: Probing Frozen Mamba Representations","url":"https://arxiv.org/html/2605.00253"},{"title":"[2603.14593] Parameter-Efficient Quality Estimation via Frozen Recursive Models","url":"https://arxiv.org/abs/2603.14593"},{"title":"Leveraging Frozen Pretrained Written Language Models for Neural Sign Language Translation | MDPI","url":"https://www.mdpi.com/2078-2489/13/5/220"},{"title":"Can Pretrained Models Really Learn Better Molecular Representations for AI-Aided Drug Discovery? - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11005046/"},{"title":"Can Pretrained Models Really Learn Better Molecular Representations for AI-Aided Drug Discovery? | Journal of Chemical Information and Modeling","url":"https://pubs.acs.org/doi/10.1021/acs.jcim.3c01707"},{"title":"Rethinking JEPA: Compute‑Efficient Video SSL with Frozen Teachers","url":"https://arxiv.org/html/2509.24317"},{"title":"Benchmarking Pretrained Molecular Embedding Models For Molecular Representation Learning","url":"https://arxiv.org/html/2508.06199v2"},{"title":"A Dive into Vision-Language Models","url":"https://huggingface.co/blog/vision_language_pretraining"},{"title":"The (Un)Surprising Effectiveness of Pre-Trained Vision Models for Control","url":"https://proceedings.mlr.press/v162/parisi22a/parisi22a.pdf"}]

Based on the web search results, here are some key findings related to representation quality scoring with frozen pretrained models:

## Quality Estimation and Frozen Embeddings

Research shows that representation quality dominates architectural choices, and frozen pretrained embeddings can match fine-tuned performance while reducing trainable parameters by 37 times. In the context of machine translation quality estimation, frozen embeddings with XLM-R achieve a Spearman correlation of 0.370, matching fine-tuned variants.

## Evaluating Representation Quality

A method called Representation-Property Relationship Analysis (RePRA) has been proposed to evaluate the quality of representations extracted by self-supervised pretrained models, including a map to visualize the quality and two scores to quantitatively evaluate it.

A frozen pretrained model will generate fixed representations, so that the quality of the representations on a specific target task should be a constant conclusion, making it useful for unbiased evaluation compared to fine-tuned models where quality is affected by task layers.

## Challenges with Frozen Representations

Research also identifies challenges: Frozen representations can exhibit severe anisotropy, with mean pairwise cosine similarity as low as 0.000044, meaning sentences produce vectors pointing in essentially the same direction regardless of content.

These findings suggest that while frozen pretrained representations can be efficient, their quality depends significantly on factors like the pretraining approach and the internal geometric properties of the learned representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96d0aed5-8bd8-49e1-b852-0f036f78d560",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "b0ed1be1-3bb1-4435-b8d3-d9831edbbb7a",
  "sourceToolAssistantUUID": "96d0aed5-8bd8-49e1-b852-0f036f78d560",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-13T19:44:14.500Z_

Let me run a few more targeted searches to get more specific numbers and details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0ed1be1-3bb1-4435-b8d3-d9831edbbb7a",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb198a5wou55GCUmeLucV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53f9d818-1d4a-4984-a8bd-e47f3384c7b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Do63EdZN1EU5qXvKY3rMRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2756,
      "cache_read_input_tokens": 14316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2756,
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

_source line 23 · 2026-05-13T19:44:15.022Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HsPK2gB6EYQ473gZVkza1q`</summary>

```json
{
  "query": "OpenVLA ablation frozen vision encoder success rate table results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53f9d818-1d4a-4984-a8bd-e47f3384c7b6",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb198a5wou55GCUmeLucV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56d1f9bf-5759-41b2-90da-aac70d67280c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Do63EdZN1EU5qXvKY3rMRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2756,
      "cache_read_input_tokens": 14316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2756,
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

_source line 24 · 2026-05-13T19:44:15.917Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YbPAAV7D72mGiur9FYs3yd`</summary>

```json
{
  "query": "OpenVLA-OFT sandwich fine-tuning vision encoder performance numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56d1f9bf-5759-41b2-90da-aac70d67280c",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb198a5wou55GCUmeLucV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c66fd76-8317-451e-96ea-cc9e0ba81ab4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Do63EdZN1EU5qXvKY3rMRY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2756,
      "cache_read_input_tokens": 14316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2756,
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

_source line 25 · 2026-05-13T19:44:16.199Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CcNMypebHqx6MrmfPdiH9x`</summary>

```json
{
  "query": "frozen pretrained features data quality scoring curriculum learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c66fd76-8317-451e-96ea-cc9e0ba81ab4",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb198a5wou55GCUmeLucV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4b69e96-3d99-4531-8016-75fca9811ebe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Do63EdZN1EU5qXvKY3rMRY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2756,
      "cache_read_input_tokens": 14316,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2756
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 14316,
          "cache_creation_input_tokens": 2756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2756,
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

_source line 26 · 2026-05-13T19:44:20.764Z_

<details><summary>↩ Tool result · `toolu_01HsPK2gB6EYQ473gZVkza1q`</summary>

```text
Web search results for query: "OpenVLA ablation frozen vision encoder success rate table results"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"VLA-Adapter","url":"https://vla-adapter.github.io/"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"(PDF) OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://www.researchgate.net/publication/381404911_OpenVLA_An_Open-Source_Vision-Language-Action_Model"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"}]

Based on the search results, I found relevant information about OpenVLA's ablation study on frozen vision encoder success rates:

Freezing the vision encoder leads to poor performance, suggesting that further adaptation of the visual features to the target scene is crucial. This finding comes from OpenVLA's parameter-efficient fine-tuning evaluation.

The research compared several fine-tuning approaches including frozen vision (which freezes the vision encoder but fine-tunes all other weights) and reports fine-tuning success rates across multiple Franka-Tabletop tasks in Table 1.

The key insight is that sandwich fine-tuning achieves better performance since it fine-tunes the vision encoder, and it consumes less GPU memory since it does not fine-tune the full LLM backbone. Additionally, LoRA fine-tuning achieves the best performance-compute trade-off, matching full fine-tuning performance while training only 1.4% of the model parameters.

The ablation study demonstrates that for OpenVLA specifically, keeping the vision encoder frozen during fine-tuning is not effective for robot manipulation tasks, unlike in standard vision-language models where frozen encoders often work well. This is an important distinction highlighted in the paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56d1f9bf-5759-41b2-90da-aac70d67280c",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "21e4b426-11ad-46cf-a9e1-f7575f09b638",
  "sourceToolAssistantUUID": "56d1f9bf-5759-41b2-90da-aac70d67280c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-13T19:44:22.985Z_

<details><summary>↩ Tool result · `toolu_01YbPAAV7D72mGiur9FYs3yd`</summary>

```text
Web search results for query: "OpenVLA-OFT sandwich fine-tuning vision encoder performance numbers"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"Understanding OpenVLA: A Simple Guide - Hankyu Kim","url":"https://hankyukim.com/openvla/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"}]

Based on the search results, I found relevant information about OpenVLA-OFT and sandwich fine-tuning vision encoder performance:

## OpenVLA-OFT Performance

OpenVLA-OFT achieves state-of-the-art results in LIBERO with 97.1% average success rate across 4 task suites, outperforming π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy.

## Sandwich Fine-Tuning Vision Encoder Performance

Regarding sandwich fine-tuning specifically, sandwich fine-tuning achieves better performance since it fine-tunes the vision encoder, and it consumes less GPU memory since it does not fine-tune the full LLM backbone. 

More detailed performance data indicates that LoRA achieves the best trade-off between performance and training memory consumption, outperforming sandwich fine-tuning and matching full fine-tuning performance while fine-tuning only 1.4% of the parameters.

## Training Details

Training was run with 8 A100 or H100 GPUs with 80 GB memory and trained for 50K to 150K gradient steps, depending on the fine-tuning dataset size, which took 1-2 days.

The results demonstrate that while sandwich fine-tuning (which fine-tunes both the vision encoder and the language model's last layer) provides a good balance of performance and efficiency, LoRA fine-tuning offers even better efficiency with minimal parameter updates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c66fd76-8317-451e-96ea-cc9e0ba81ab4",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "7b3385be-35a9-4f1c-a420-d8d2972ae689",
  "sourceToolAssistantUUID": "5c66fd76-8317-451e-96ea-cc9e0ba81ab4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T19:44:24.243Z_

<details><summary>↩ Tool result · `toolu_01CcNMypebHqx6MrmfPdiH9x`</summary>

```text
Web search results for query: "frozen pretrained features data quality scoring curriculum learning"

Links: [{"title":"Curriculum Learning with Quality-Driven Data Selection","url":"https://arxiv.org/html/2407.00102v1"},{"title":"FastDINOv2: Frequency Based Curriculum Learning Improves Robustness and Training Speed","url":"https://arxiv.org/html/2507.03779"},{"title":"[2407.00102] Curriculum Learning with Quality-Driven Data Selection","url":"https://arxiv.org/abs/2407.00102"},{"title":"How Learning Rate Decay Wastes Your Best Data in Curriculum-Based LLM Pretraining","url":"https://arxiv.org/html/2511.18903v1"},{"title":"Selective Freezing for Efﬁcient Continual Learning","url":"https://openaccess.thecvf.com/content/ICCV2023W/VCL/papers/Sorrenti_Selective_Freezing_for_Efficient_Continual_Learning_ICCVW_2023_paper.pdf"},{"title":"Strategic Data Ordering: Enhancing Large Language Model Performance through Curriculum Learning","url":"https://arxiv.org/html/2405.07490v1"},{"title":"LLMs Should Always Be Pretrained on Their Preferred Data","url":"https://aclanthology.org/2025.findings-acl.1091.pdf"},{"title":"How can you determine which layers to freeze when fine-tuning a pre-trained model?","url":"https://www.linkedin.com/advice/0/how-can-you-determine-which-layers-freeze-when-okd8f"},{"title":"[2301.12589] Confidence-Aware Calibration and Scoring Functions for Curriculum Learning","url":"https://arxiv.org/abs/2301.12589"},{"title":"Privacy-Preserved Automated Scoring using Federated Learning for Educational Research","url":"https://arxiv.org/html/2503.11711"}]

I found several relevant research papers on your query. Here are the key findings:

## Curriculum Learning with Quality-Driven Data Selection

A novel approach proposes using image-text correlation and model perplexity to evaluate and select data of varying quality, leveraging the distinct distribution of these two attributes to map data quality into a two-dimensional space that allows for data selection based on their location within this distribution.

This method introduces a curriculum learning strategy that involves multiple training stages, each using progressively higher-quality data. Specifically, the method calculates each sample's clip score and model loss, using them as two-dimensional coordinates, and by dividing key areas, obtains subsets of data with varying quality.

## Frozen Pretrained Features in Training

In some implementations, the visual encoder, projector, and LLM weights are kept frozen, with only trainable parameters of LoRA being optimized. Freezing pre-trained features helps reduce forgetting while reusing already good features, at the cost of giving up learning task-specific low-level features.

## Additional Curriculum Learning Applications

Recent work on FastDINOv2 combines a 112-224 curriculum with Gaussian noise patching, allocating 150 epochs to downsampled inputs followed by 50 epochs of full-resolution training, with evaluation including linear probing on clean data and robustness assessment using frozen backbones.

Current LLM pretraining pipelines employ sophisticated data curation procedures including rule-based filtering, quality scoring (model-based labeling), and score-based data selection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4b69e96-3d99-4531-8016-75fca9811ebe",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "caff4f43-7e99-4c40-abe5-c300f4ffecde",
  "sourceToolAssistantUUID": "a4b69e96-3d99-4531-8016-75fca9811ebe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-13T19:44:29.482Z_

Let me do a few final targeted searches to get the specific ablation numbers from the OpenVLA paper and more on the distinction between frozen-for-scoring vs frozen-for-training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caff4f43-7e99-4c40-abe5-c300f4ffecde",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb199UvREQAYuVyPycNqc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d936fc3e-fba3-4862-b823-4a542633f984",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QsXNeQecv5nCL5sK6UQEs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 17072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2638,
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

_source line 30 · 2026-05-13T19:44:30.905Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GnCTDKr1htUmeMdspDzNhs`</summary>

```json
{
  "query": "OpenVLA Table 1 frozen vision 35% sandwich fine-tuning 55% success rate ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d936fc3e-fba3-4862-b823-4a542633f984",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb199UvREQAYuVyPycNqc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcc520a9-6b6b-466b-abf0-756aa777b223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QsXNeQecv5nCL5sK6UQEs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 17072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2638,
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

_source line 31 · 2026-05-13T19:44:31.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NaKXrsUjA888oU8EpKvoHt`</summary>

```json
{
  "query": "frozen encoder data selection weighting not training reward model quality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcc520a9-6b6b-466b-abf0-756aa777b223",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb199UvREQAYuVyPycNqc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69ee31e9-e29a-4464-a349-e0caceae5a73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QsXNeQecv5nCL5sK6UQEs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 17072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2638,
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

_source line 32 · 2026-05-13T19:44:32.128Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EHeqdRnEhbhbPSJ11Lagur`</summary>

```json
{
  "query": "ExpReS-VLA frozen vision backbone embeddings memory buffer experience replay"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69ee31e9-e29a-4464-a349-e0caceae5a73",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb199UvREQAYuVyPycNqc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b03e89c1-3fdf-4a19-bd4b-2337ee6a1a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QsXNeQecv5nCL5sK6UQEs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 17072,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2638
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 17072,
          "cache_creation_input_tokens": 2638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2638,
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

_source line 33 · 2026-05-13T19:44:36.433Z_

<details><summary>↩ Tool result · `toolu_01GnCTDKr1htUmeMdspDzNhs`</summary>

```text
Web search results for query: "OpenVLA Table 1 frozen vision 35% sandwich fine-tuning 55% success rate ablation"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"VLA-Adapter","url":"https://vla-adapter.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Understanding OpenVLA: A Simple Guide - Hankyu Kim","url":"https://hankyukim.com/openvla/"}]

I found relevant information about OpenVLA and its ablation studies. Based on the search results, I can provide you with information about the fine-tuning approaches mentioned in your query:

OpenVLA includes comparisons of different fine-tuning approaches: full fine-tuning updates all weights during fine-tuning; last layer only fine-tunes only the last layer of OpenVLA's transformer backbone and the token embedding matrix; frozen vision freezes the vision encoder but fine-tunes all other weights; and sandwich fine-tuning unfreezes the vision encoder, token embedding matrix, and last layer.

Regarding the specific performance metrics you mentioned, sandwich fine-tuning can fine-tune the vision encoder + LLM last layer only, providing strong performance with moderate compute, though the exact percentages from Table 1 you referenced (35% for frozen vision, 55% for sandwich fine-tuning) are not directly quoted in these search results.

The search results contain references to ablation studies in the OpenVLA papers, particularly comparing different fine-tuning strategies on benchmarks like LIBERO, but the specific success rate percentages from Table 1 you're looking for don't appear in these particular search result excerpts. For the exact figures from Table 1, you may need to refer directly to the OpenVLA paper or technical documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcc520a9-6b6b-466b-abf0-756aa777b223",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "1370a2ee-74f3-4348-b5f0-5593a34f44a7",
  "sourceToolAssistantUUID": "bcc520a9-6b6b-466b-abf0-756aa777b223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T19:44:38.178Z_

<details><summary>↩ Tool result · `toolu_01NaKXrsUjA888oU8EpKvoHt`</summary>

```text
Web search results for query: "frozen encoder data selection weighting not training reward model quality"

Links: [{"title":"Frozen Encoder – Your Gateway to Data Mastery","url":"https://insightful-data-lab.com/2025/08/23/frozen-encoder/"},{"title":"A Multi-Encoder Frozen-Decoder Approach for Fine-Tuning Large Language Models","url":"https://arxiv.org/html/2501.07818v1"},{"title":"Frozen-Encoder Protocol in ML","url":"https://www.emergentmind.com/topics/frozen-encoder-protocol"},{"title":"Trained Persistent Memory for Frozen Encoder–Decoder LLMs: Six Architectural Methods","url":"https://arxiv.org/html/2603.16413v1"},{"title":"Freezing Layers and Fine-Tuning Transformer Models in PyTorch: A Simple Guide | by Prabhatzade | Medium","url":"https://medium.com/@prabhatzade/freezing-layers-and-fine-tuning-transformer-models-in-pytorch-a-simple-guide-119cad0980c6"},{"title":"Frozen Encoders: Foundations, Applications, and Advanced Techniques | by Utsavsharma | Medium","url":"https://medium.com/@utsavsharma1990/frozen-encoders-foundations-applications-and-advanced-techniques-5b17688dd09a"},{"title":"Training and fine-tuning — transformers 4.2.0 documentation","url":"https://huggingface.co/transformers/v4.2.2/training.html"},{"title":"Transfer learning & fine-tuning | TensorFlow Core","url":"https://www.tensorflow.org/guide/keras/transfer_learning"},{"title":"Don’t freeze: Finetune encoders for better Self-Supervised HAR","url":"https://arxiv.org/html/2307.01168"},{"title":"Variational Feature Compression for Model-Specific Representations","url":"https://arxiv.org/html/2604.06644"}]

I've performed the web search for you. The results provide comprehensive information about frozen encoders in machine learning. Here's what I found:

## Key Findings

**What is a Frozen Encoder:**
A frozen encoder means using a pretrained encoder model (like BERT, ResNet, or a sentence transformer) but not updating its weights during training on your task. During training, all foundation (encoder) networks' weights are fixed (no gradients propagated or updated), and only the adapter/projection/top-layer/bridging parameters are updated.

**Benefits and Applications:**
Frozen encoders prevent overfitting when you don't have much labeled data and leverage general knowledge from large pretrained models. The frozen-encoder protocol typically achieves near–state-of-the-art or SOTA on benchmarks while requiring significantly less data, compute, and training time, with empirical evaluations across domains confirming stable learning, sample efficiency, and robust generalization.

**Advanced Techniques:**
Six trained memory adapters span three injection points (before the encoder, between encoder and decoder, inside the decoder) and four write mechanisms (attention-coupled update, Hebbian outer product, gated cross-attention, sparse slot addressing), while keeping every encoder and decoder weight frozen.

The search results cover frozen encoders across multiple domains including NLP, vision, multimodal learning, and scientific applications, with detailed discussions of implementation techniques and architectural considerations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69ee31e9-e29a-4464-a349-e0caceae5a73",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "7020f6d7-ccaa-431e-8cab-83706fb0a49e",
  "sourceToolAssistantUUID": "69ee31e9-e29a-4464-a349-e0caceae5a73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-13T19:44:38.536Z_

<details><summary>↩ Tool result · `toolu_01EHeqdRnEhbhbPSJ11Lagur`</summary>

```text
Web search results for query: "ExpReS-VLA frozen vision backbone embeddings memory buffer experience replay"

Links: [{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://arxiv.org/html/2511.06202v1"},{"title":"[2511.06202] ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://arxiv.org/abs/2511.06202"},{"title":"(PDF) ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://www.researchgate.net/publication/397480729_ExpReS-VLA_Specializing_Vision-Language-Action_Models_Through_Experience_Replay_and_Retrieval"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through","url":"https://arxiv.org/pdf/2511.06202"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.06202v1"},{"title":"(PDF) Residual Policy Adaptation for Vision-Language-Action Models in Precision Robotic Assembly","url":"https://www.researchgate.net/publication/401122606_Residual_Policy_Adaptation_for_Vision-Language-Action_Models_in_Precision_Robotic_Assembly"},{"title":"Prioritized Experience Replay | Request PDF","url":"https://www.researchgate.net/publication/319770330_Prioritized_Experience_Replay"},{"title":"MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=54U3XHf7qq"},{"title":"Compute- and Memory-Efficient Reinforcement Learning with Latent Experience Replay | OpenReview","url":"https://openreview.net/forum?id=J7bUsLCb0zf"},{"title":"Replay Memory Explained - Experience for Deep Q-Network Training - deeplizard","url":"https://deeplizard.com/learn/video/Bcuj2fTH4_4"}]

Based on the search results, here's what I found about ExpReS-VLA:

## ExpReS-VLA Overview

ExpReS-VLA is a method that enables rapid on-device adaptation of pre-trained Vision-Language-Action (VLA) models to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation.

## Frozen Vision Backbone & Embeddings

The frozen encoder extracts embeddings from RGB frames using fused SigLIP and DINOv2 features, which are stored in a compressed replay buffer. The approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs.

## Memory Buffer & Experience Replay

During deployment, ExpReS-VLA retrieves the k most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. During adaptation, the system retrieves the top-k most similar experiences via RAG and combines them with current observations.

## Key Features

The method introduces Thresholded Hybrid Contrastive Loss (THCL), which adaptively switches between triplet and InfoNCE objectives based on failure complexity, transforming unsuccessful attempts into learning signals. This enables learning from both successes and failures during the adaptation process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b03e89c1-3fdf-4a19-bd4b-2337ee6a1a3d",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "6ddc5dda-b5d6-4d93-8ef5-57106c2d37dd",
  "sourceToolAssistantUUID": "b03e89c1-3fdf-4a19-bd4b-2337ee6a1a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T19:44:41.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EKBSTQnMjDyMuB26AehFqY`</summary>

```json
{
  "query": "OpenVLA paper Table 1 fine-tuning comparison frozen vision LoRA full results percentage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ddc5dda-b5d6-4d93-8ef5-57106c2d37dd",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb19AXbgUEyMLdELYKKze",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9e7ade0-a2db-46a9-929c-3160f0f6d65b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADobYXBuFQoNVHDnpEZ3iG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2757,
      "cache_read_input_tokens": 19710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2757,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 37 · 2026-05-13T19:44:42.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017zDhLaGGCSYspLpb92hm9x`</summary>

```json
{
  "query": "\"Enhancing Generalization Vision-Language-Action\" \"partially frozen\" dual encoder 35 55 performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9e7ade0-a2db-46a9-929c-3160f0f6d65b",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb19AXbgUEyMLdELYKKze",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6dff019-3ce6-4bb5-97b3-5e53aa5c1f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADobYXBuFQoNVHDnpEZ3iG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2757,
      "cache_read_input_tokens": 19710,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2757
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 19710,
          "cache_creation_input_tokens": 2757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2757,
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

_source line 38 · 2026-05-13T19:44:47.072Z_

<details><summary>↩ Tool result · `toolu_01EKBSTQnMjDyMuB26AehFqY`</summary>

```text
Web search results for query: "OpenVLA paper Table 1 fine-tuning comparison frozen vision LoRA full results percentage"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"(PDF) Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://www.researchgate.net/publication/398721162_Towards_Accessible_Physical_AI_LoRA-Based_Fine-Tuning_of_VLA_Models_for_Real-World_Robot_Control"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model Moo Jin Kim∗,1","url":"https://groups.csail.mit.edu/robotics-center/public_papers/Kim24.pdf"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"}]

Based on the search results, I found information about the OpenVLA paper's fine-tuning comparisons. The paper reports fine-tuning success rates across multiple Franka-Tabletop tasks in Table 1, and finds that only fine-tuning the network's last layer or freezing the vision encoder leads to poor performance.

In contrast, "sandwich fine-tuning" achieves better performance since it fine-tunes the vision encoder, and it consumes less GPU memory since it does not fine-tune the full LLM backbone. LoRA achieves strong results, enabling OpenVLA to be fine-tuned on a new task within 10-15 hours on a single A100 GPU – an 8x reduction in compute compared to full fine-tuning.

However, the specific percentage values from Table 1 are not visible in the search results I retrieved. To access the exact numerical results comparing frozen vision, LoRA, and full fine-tuning performance percentages, you would need to view the actual paper directly at https://arxiv.org/html/2406.09246v1 or the PDF version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9e7ade0-a2db-46a9-929c-3160f0f6d65b",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "076667d1-c0f1-445c-9833-0edc50dfdc92",
  "sourceToolAssistantUUID": "c9e7ade0-a2db-46a9-929c-3160f0f6d65b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T19:44:49.267Z_

<details><summary>↩ Tool result · `toolu_017zDhLaGGCSYspLpb92hm9x`</summary>

```text
Web search results for query: ""Enhancing Generalization Vision-Language-Action" "partially frozen" dual encoder 35 55 performance"

Links: [{"title":"Enhancing Generalization in Vision-Language-Action ...","url":"https://arxiv.org/pdf/2509.11417"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"Enhancing Generalization in Vision-Language-Action Models","url":"https://gen-vla.github.io/"},{"title":"[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/abs/2509.11417"},{"title":"Vision-Language-Action Pretraining","url":"https://www.emergentmind.com/topics/vision-language-action-model-pretraining"},{"title":"Freezing pre-trained parameters of encoders for denoisers: Expanding pixel involvement and filtering out high-frequency noise - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S089360802600256X"},{"title":"Imperfect Vision Encoders: Efficient and Robust Tuning for Vision-Language Models","url":"https://arxiv.org/html/2407.16526v1"},{"title":"Unveiling Encoder-Free Vision-Language Models","url":"https://arxiv.org/html/2406.11832v1"},{"title":"[2501.07818] A Multi-Encoder Frozen-Decoder Approach for Fine-Tuning Large Language Models","url":"https://arxiv.org/abs/2501.07818"},{"title":"VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models","url":"https://arxiv.org/html/2601.03309v1"}]

Based on the search results, I found information about the paper "Enhancing Generalization in Vision-Language-Action Models" that matches your query.

## Key Findings:

Utilizing a partially-frozen dual encoder alone improves OpenVLA performance from 35.03% to 55.55%.

The paper introduces two siamese encoders: a frozen one that serves as an "anchor" to retain the robust, semantically rich representations from VLM pretraining, and a finetuned one that keeps the full flexibility to be specialized to robotic actions prediction.

When combined with string tokenizer and co-training approaches, the performance further rises to 78.46%, though the gain over only using String Tokenizer + co-training is marginal (78.17% vs. 78.46%).

The research proposes a comprehensive framework that includes a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances.

The 35→55 performance improvement you mentioned refers to the baseline OpenVLA performance (35.03%) improving to 55.55% with the partially-frozen dual encoder approach alone.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6dff019-3ce6-4bb5-97b3-5e53aa5c1f4b",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "3fc6cd39-8d29-4deb-803d-5a57aafc3fb6",
  "sourceToolAssistantUUID": "c6dff019-3ce6-4bb5-97b3-5e53aa5c1f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-13T19:44:52.103Z_

Now let me get one final search to read the actual OpenVLA paper's ablation table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fc6cd39-8d29-4deb-803d-5a57aafc3fb6",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb19BKUwmajCyQMpfstkh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "822eb3ee-6ea4-47a2-b396-13cd6d1ee695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNrRD2bK2JW7cfauyenNi7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1785,
      "cache_read_input_tokens": 22467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1785,
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

_source line 41 · 2026-05-13T19:44:53.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GoPCSFRBbfNjStHxQ5Cdoh`</summary>

```json
{
  "query": "site:arxiv.org OpenVLA 2406.09246 \"frozen vision\" \"last layer\" fine-tuning success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "822eb3ee-6ea4-47a2-b396-13cd6d1ee695",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb19BKUwmajCyQMpfstkh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d4179d9-a507-4b01-9bc0-26eaccee60b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNrRD2bK2JW7cfauyenNi7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1785,
      "cache_read_input_tokens": 22467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1785,
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

_source line 42 · 2026-05-13T19:44:53.989Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S6LkfLkqxLtakNUXQqNUP1`</summary>

```json
{
  "query": "CLIP frozen features reward model data quality scoring pretrained representations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d4179d9-a507-4b01-9bc0-26eaccee60b2",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb19BKUwmajCyQMpfstkh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f3556a7-4a26-4d50-9fe7-e0500c9ebc9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNrRD2bK2JW7cfauyenNi7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1785,
      "cache_read_input_tokens": 22467,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 22467,
          "cache_creation_input_tokens": 1785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1785,
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

_source line 43 · 2026-05-13T19:45:00.067Z_

<details><summary>↩ Tool result · `toolu_01S6LkfLkqxLtakNUXQqNUP1`</summary>

```text
Web search results for query: "CLIP frozen features reward model data quality scoring pretrained representations"

Links: [{"title":"[2208.03550] Frozen CLIP Models are Efficient Video Learners","url":"https://arxiv.org/abs/2208.03550"},{"title":"[2208.03550v1] Frozen CLIP Models are Efficient Video Learners","url":"https://arxiv.org/abs/2208.03550v1"},{"title":"Frozen CLIP Models are Efficient Video Learners | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-19833-5_23"},{"title":"(PDF) Frozen CLIP Models are Efficient Video Learners","url":"https://www.researchgate.net/publication/362567981_Frozen_CLIP_Models_are_Efficient_Video_Learners"},{"title":"Frozen CLIP Models are Efficient Video Learners | Request PDF","url":"https://www.researchgate.net/publication/365100893_Frozen_CLIP_Models_are_Efficient_Video_Learners"},{"title":"Frozen CLIP Models are Efficient Video Learners","url":"https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136950384.pdf"},{"title":"Frozen CLIP Models are Efficient Video Learners | DeepAI","url":"https://deepai.org/publication/frozen-clip-models-are-efficient-video-learners"},{"title":"Frozen CLIP Models are Efficient Video Learners - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220803550L/abstract"},{"title":"Towards Fine-Grained Adaptation of CLIP via a Self-Trained Alignment Score","url":"https://arxiv.org/html/2507.09615v1"},{"title":"[2208.03550] Frozen CLIP Models are Efficient Video Learners","url":"https://arxiv-export1.library.cornell.edu/abs/2208.03550"}]

I've found relevant research on the topic. Here's a summary of what the search results show:

## Key Findings

**Frozen CLIP Features for Efficient Learning:**
The Efficient Video Learning (EVL) framework enables direct training of high-quality video recognition models with frozen CLIP features. Recent advances in Contrastive Vision-Language Pre-training (CLIP) pave the way for visual recognition tasks, with models pretrained on large open-vocabulary image-text pair data that learn powerful visual representations with rich semantics.

**Using Frozen vs. Finetuned Representations:**
While directly using pretrained image features without finetuning the image backbone leads to subpar results, this approach avoids the substantial computation and memory resources required for finetuning on videos. Interestingly, frozen backbone is more efficient when pretraining quality is higher.

**CLIP as a Feature Extractor:**
A pretrained CLIP model can be used for transfer learning or as a frozen feature extractor and has been shown to perform well for many computer vision tasks, including video action recognition, keypoint detection, semantic image segmentation, point cloud recognition and camera-trap image retrieval.

**Adaptation Approaches:**
The search also found recent work on Fine-grained Alignment and Interaction Refinement (FAIR), a novel unsupervised adaptation framework for CLIP that introduces a Learned Alignment Score based on selected local image crops and adaptive class representations.

The results primarily focus on using frozen CLIP representations for downstream video learning tasks rather than specific reward model or data quality scoring applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f3556a7-4a26-4d50-9fe7-e0500c9ebc9e",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "f9170ff0-ea38-4d1f-9ecc-6f7aeeb73c92",
  "sourceToolAssistantUUID": "4f3556a7-4a26-4d50-9fe7-e0500c9ebc9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-13T19:45:01.571Z_

<details><summary>↩ Tool result · `toolu_01GoPCSFRBbfNjStHxQ5Cdoh`</summary>

```text
Web search results for query: "site:arxiv.org OpenVLA 2406.09246 "frozen vision" "last layer" fine-tuning success rate"

Links: [{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Paper page - OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://huggingface.co/papers/2406.09246"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"[2406.09246v3] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246v3"},{"title":"openvla/openvla-7b · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://www.emergentmind.com/papers/2406.09246"},{"title":"[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"}]

I found results for the OpenVLA paper (2406.09246), but the search results don't contain specific information about "frozen vision," "last layer" fine-tuning, or specific fine-tuning success rates with those configurations. Let me search more specifically for those details.

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models","url":"https://arxiv.org/html/2601.03309v1"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"BRAVE : Broadening the visual encoding of vision-language models","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02433.pdf"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"FastVLM: Efﬁcient Vision Encoding for Vision Language Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Vasu_FastVLM_Efficient_Vision_Encoding_for_Vision_Language_Models_CVPR_2025_paper.pdf"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/vision-language-action-finetuning-robotics"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"}]

Great! I found the specific information from the OpenVLA paper. Based on my search results, I found the relevant details from the arxiv paper on OpenVLA fine-tuning strategies.

## OpenVLA Fine-Tuning Results for "Frozen Vision" and "Last Layer" Approaches

According to the OpenVLA paper (arXiv:2406.09246), only fine-tuning the network's last layer or freezing the vision encoder leads to poor performance, suggesting that further adaptation of the visual features to the target scene is crucial. 

The paper doesn't provide specific numerical success rates for the frozen vision or last-layer-only approaches in the search results I found. However, the results indicate that sandwich fine-tuning achieves better performance since it fine-tunes the vision encoder, and it consumes less GPU memory since it does not fine-tune the full LLM backbone.

The key finding is that these parameter-efficient approaches that keep the vision encoder frozen perform significantly worse than methods that allow the vision encoder to be fine-tuned, suggesting that adapting visual representations to the target robot domain is critical for successful task performance.

If you need the exact numerical success rates for the frozen vision configuration, those specific numbers may be in the full paper tables that weren't captured in the web search results. I'd recommend checking Table 1 in the OpenVLA paper directly for the complete fine-tuning results comparison.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d4179d9-a507-4b01-9bc0-26eaccee60b2",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "a8b29b3dd5b66853e",
  "type": "user",
  "uuid": "d0b3223f-d4f3-4671-a618-b6b9089af20c",
  "sourceToolAssistantUUID": "0d4179d9-a507-4b01-9bc0-26eaccee60b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-13T19:45:56.552Z_

Now I have comprehensive findings. Here is my synthesis:

---

## Findings: Frozen Vision Encoder in VLA Models and CDR-VLA's Two-Stage Approach

### 1. The Core Evidence: Freezing the Vision Encoder During VLA Policy Training Hurts Performance

The OpenVLA paper (Kim et al., arXiv:2406.09246) includes an explicit ablation study (Table 1) comparing fine-tuning strategies. The key findings:

- **Frozen vision encoder** (freeze encoder, fine-tune everything else): leads to **poor performance**. The paper states: "only fine-tuning the network's last layer or freezing the vision encoder leads to poor performance, suggesting that further adaptation of the visual features to the target scene is crucial."
- **Sandwich fine-tuning** (fine-tune vision encoder + LLM last layer only): achieves better performance than frozen vision while consuming less GPU memory than full fine-tuning.
- **LoRA fine-tuning** (1.4% of parameters): matches full fine-tuning performance, representing the best performance-compute trade-off.
- The paper explicitly notes this is **opposite** to standard VLM practice: "freezing vision encoders during VLM training typically leads to higher performance because a frozen vision encoder may better preserve the robust features learned from its Internet-scale pretraining" -- but this does **not** hold for robotics action prediction.

The hypothesis is that pretrained vision backbones (SigLIP, DINOv2) do not capture sufficient fine-grained spatial details for precise robotic control without adaptation.

### 2. Specific Numbers from Gen-VLA (arXiv:2509.11417)

The paper "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" provides the most specific numbers:

- **Baseline OpenVLA**: 35.03% success rate
- **With partially-frozen dual encoder** (one frozen + one trainable): **55.55%** success rate (a +20.52 percentage point improvement)
- **Full framework** (dual encoder + string tokenizer + co-training): **78.46%**

This paper's architecture is directly relevant to CDR-VLA's design philosophy: it uses **two siamese encoders** -- a frozen one serving as an "anchor" to retain robust pretrained representations, and a finetuned one with full flexibility for robotic action prediction. This demonstrates that using frozen encoder features alongside trainable encoder features is a validated design pattern.

### 3. Real-World Frozen vs. Unfrozen Comparison (arXiv:2512.11921)

LoRA-based fine-tuning research on real robots found:
- **Frozen vision encoder**: ~74% success rate (8.4M trainable parameters)
- **Unfrozen vision encoder**: ~76% success rate (33M trainable parameters)
- The difference is modest (2 percentage points) with sufficient training data, but the unfrozen approach is generally preferred.

### 4. ExpReS-VLA: Precedent for Using Frozen Encoder Features for Scoring/Selection

ExpReS-VLA (arXiv:2511.06202) provides a **direct precedent** for what CDR-VLA proposes. It uses OpenVLA's **frozen vision backbone** to:
- Extract embeddings from RGB frames (fused SigLIP + DINOv2 features)
- Store them in a compressed replay buffer (97% storage reduction vs. raw images)
- Use **cosine similarity** on these frozen embeddings to retrieve the k most similar past experiences via RAG
- Employ these for prioritized experience replay and retrieval-augmented training

This is architecturally analogous to CDR-VLA's approach: frozen encoder features are used for **scoring/selection** (quality assessment in CDR-VLA, similarity retrieval in ExpReS-VLA), while the actual policy training can proceed with unfrozen parameters.

### 5. Broader Precedent for Frozen Features in Quality/Scoring Roles

Multiple research directions validate using frozen pretrained features for scoring and quality assessment:

- **Curriculum Learning with Quality-Driven Data Selection** (arXiv:2407.00102): Uses CLIP scores (from frozen CLIP) and model loss as two-dimensional quality coordinates for data selection and curriculum staging.
- **Parameter-Efficient Quality Estimation** (arXiv:2603.14593): Frozen XLM-R embeddings achieve Spearman correlation of 0.370 for quality estimation, matching fine-tuned variants while reducing trainable parameters by 37x.
- **Frozen DINOv2 features**: Demonstrate "generalization across both natural and specialized downstream domains" for feature extraction, with strong linear-probe accuracy signaling that representations are already discriminative.
- **Frozen CLIP for video learning**: The EVL framework shows frozen CLIP features enable direct training of high-quality recognition models, with the finding that "frozen backbone is more efficient when pretraining quality is higher."
- **RepRA (Representation-Property Relationship Analysis)**: Proposes that "a frozen pretrained model will generate fixed representations, so that the quality of the representations on a specific target task should be a constant conclusion" -- making frozen features ideal for unbiased quality evaluation.

### 6. Assessment of CDR-VLA's Two-Stage Approach

The reviewer's concern that "freezing the vision encoder leads to poor performance" is **valid for policy training** but is a **misapplication** when applied to CDR-VLA's quality assessment stage. Here is the critical distinction:

**What the evidence says is bad:**
- Freezing the vision encoder **during policy training** (i.e., the encoder stays frozen while the model learns to predict actions). This is the OpenVLA ablation finding.

**What CDR-VLA actually proposes (if I understand correctly):**
- Stage 1: Use **frozen** encoder features to compute quality weights/scores for training data (analogous to using CLIP scores for data selection, or ExpReS-VLA using frozen embeddings for retrieval)
- Stage 2: Train the policy with the encoder **unfrozen**, using the quality weights from Stage 1

This two-stage design is well-supported by existing work:
1. **Gen-VLA** explicitly uses a frozen encoder as an "anchor" alongside a trainable encoder
2. **ExpReS-VLA** uses frozen encoder embeddings for retrieval/scoring while the policy adapts
3. **Curriculum learning** literature routinely uses frozen model features (CLIP scores, perplexity) to score data quality before training
4. The RepRA framework argues frozen features are actually **preferable** for quality evaluation because they provide consistent, unbiased representations

**Bottom line:** The prior review's concern conflates two different uses of frozen encoders. Using frozen features for quality scoring is standard practice with strong precedent. The concern would only be valid if CDR-VLA froze the encoder during actual policy training, which (based on your description) it does not.

---

Sources:
- [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/html/2406.09246v3)
- [OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models](https://openvla-oft.github.io/)
- [Enhancing Generalization in VLA Models (Gen-VLA)](https://arxiv.org/html/2509.11417v1)
- [ExpReS-VLA: Experience Replay and Retrieval for VLA](https://arxiv.org/html/2511.06202v2)
- [LoRA-Based Fine-Tuning of VLA Models](https://arxiv.org/html/2512.11921v1)
- [Curriculum Learning with Quality-Driven Data Selection](https://arxiv.org/html/2407.00102v1)
- [Parameter-Efficient Quality Estimation via Frozen Recursive Models](https://arxiv.org/html/2603.14593)
- [Frozen DINOv2 Encoder (Emergent Mind)](https://www.emergentmind.com/topics/frozen-dinov2-encoder)
- [Frozen CLIP Models are Efficient Video Learners](https://arxiv.org/abs/2208.03550)
- [VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA](https://arxiv.org/html/2605.06175v1)
- [VLM4VLA: Revisiting Vision-Language-Models in VLA](https://arxiv.org/html/2601.03309v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0b3223f-d4f3-4671-a618-b6b9089af20c",
  "isSidechain": true,
  "agentId": "a8b29b3dd5b66853e",
  "requestId": "req_011Cb19CE8FvfUGF7mqmgj6y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbac283f-dcc8-4d7e-a964-14ca17b6a70b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lr2NQUrNKDi7L2rLfEjd4X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 904,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 24252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
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
