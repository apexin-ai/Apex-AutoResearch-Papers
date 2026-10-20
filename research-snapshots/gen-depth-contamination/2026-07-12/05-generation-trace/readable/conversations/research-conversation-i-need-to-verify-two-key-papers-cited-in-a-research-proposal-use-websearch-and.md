# Research conversation: I need to verify two key papers cited in a research proposal. Use WebSearch and WebFetch to check: 1. **DreamZero** (arX

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a15b98ed49a9f8d53.jsonl`
- **Structured JSON:** [`68951a81d8a471d8ea78.json`](../../sessions/68/68951a81d8a471d8ea78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-10T19:36:49.128Z_

I need to verify two key papers cited in a research proposal. Use WebSearch and WebFetch to check:

1. **DreamZero** (arXiv 2602.15922, Feb 2026) - "World Action Models are Zero-shot Policies". Claims: velocity-based convergence caching within flow-matching denoising, cosine similarity threshold on successive predictions, 75% step reduction (16→4), zero additional parameters, 14B parameter model using Wan2.1-I2V backbone, requires 2x GB200 for inference. I need to verify these specific claims.

2. **UWM** (arXiv 2504.02792, RSS 2025) - "Unified World Models: Coupling Video and Action Diffusion". Claims: 180M-parameter DiT-B architecture, DDPM-based training with SEPARATE diffusion timesteps for action and video, public code and DROID checkpoints. Verify these claims.

Search for both papers on arxiv.org, fetch the abstracts and key sections, and report what you find. Also check if UWM code is actually publicly available on GitHub/HuggingFace.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "3ef4d095-29a2-476a-b47b-28603a11063a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:36:49.131Z_

```json
{
  "parentUuid": "3ef4d095-29a2-476a-b47b-28603a11063a",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
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
  "uuid": "fad3dc6d-ed4d-4071-a146-b6cc13879f50",
  "timestamp": "2026-05-10T19:36:49.131Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:36:52.130Z_



I'll search for both papers simultaneously to verify the claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fad3dc6d-ed4d-4071-a146-b6cc13879f50",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauT9BMK8fjP6GnMZGjkQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6907ee62-3285-40de-8b2d-8fd394fc16da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDRKkNsuVqu9omknGCe7nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9035,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9035,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:36:52.653Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EScL21VPYx43RSoc5WxnQc`</summary>

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
  "parentUuid": "6907ee62-3285-40de-8b2d-8fd394fc16da",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauT9BMK8fjP6GnMZGjkQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "763b19ba-74d1-4b56-97c5-f227cdb8741c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDRKkNsuVqu9omknGCe7nr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9035,
      "cache_read_input_tokens": 0,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9035
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9035,
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

_source line 5 · 2026-05-10T19:36:52.657Z_

<details><summary>↩ Tool result · `toolu_01EScL21VPYx43RSoc5WxnQc`</summary>

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
  "parentUuid": "763b19ba-74d1-4b56-97c5-f227cdb8741c",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "4470108a-2d42-493c-bf40-75350213aa60",
  "sourceToolAssistantUUID": "763b19ba-74d1-4b56-97c5-f227cdb8741c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:36:54.806Z_



Now let me search for both papers and fetch their details simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4470108a-2d42-493c-bf40-75350213aa60",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauT9SfKPEpiviohhjoLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2503b3a4-044a-4e29-9bdd-c2a31d339e71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WK8BnLPV79hxVQGUEKAz4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 9035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 7 · 2026-05-10T19:36:56.208Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016nyP6iS3P3q8Xi4mrQwuP8`</summary>

```json
{
  "query": "arXiv 2602.15922 DreamZero World Action Models Zero-shot Policies"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2503b3a4-044a-4e29-9bdd-c2a31d339e71",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauT9SfKPEpiviohhjoLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "664488af-3798-4da9-9018-955b4d1e1e3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WK8BnLPV79hxVQGUEKAz4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 9035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 8 · 2026-05-10T19:36:57.291Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018dEQ2RhdptQV5eC6CamuzV`</summary>

```json
{
  "query": "arXiv 2504.02792 UWM Unified World Models Coupling Video Action Diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "664488af-3798-4da9-9018-955b4d1e1e3e",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauT9SfKPEpiviohhjoLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e35032f-498f-40ae-a393-8453a2511070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WK8BnLPV79hxVQGUEKAz4w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 9035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 9 · 2026-05-10T19:36:57.501Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JQ6A9i6bjeAMCfvBjFUzYh`</summary>

```json
{
  "query": "UWM Unified World Models code github DROID checkpoints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e35032f-498f-40ae-a393-8453a2511070",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauT9SfKPEpiviohhjoLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c57e84d7-d388-479e-9088-ba2d6b78fbd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WK8BnLPV79hxVQGUEKAz4w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 9035,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 194,
          "cache_read_input_tokens": 9035,
          "cache_creation_input_tokens": 1902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1902,
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

_source line 10 · 2026-05-10T19:37:01.604Z_

<details><summary>↩ Tool result · `toolu_016nyP6iS3P3q8Xi4mrQwuP8`</summary>

```text
Web search results for query: "arXiv 2602.15922 DreamZero World Action Models Zero-shot Policies"

Links: [{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"World Action Models are Zero-shot Policies | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.15922"},{"title":"Paper page - World Action Models are Zero-shot Policies","url":"https://huggingface.co/papers/2602.15922"},{"title":"2026-2-19 World Action Models are Zero-shot Policies Seonghyeon Ye† Yunhao Ge*","url":"https://arxiv.org/pdf/2602.15922"},{"title":"GitHub - dreamzero0/dreamzero: Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals · GitHub","url":"https://github.com/dreamzero0/dreamzero"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"World Action Models are Zero-shot Policies | OpenReview","url":"https://openreview.net/forum?id=cd33uUB609"},{"title":"[2602.15922v1] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922v1"},{"title":"World Action Models as Zero-Shot Policies","url":"https://www.emergentmind.com/papers/2602.15922"}]

Based on the search results for arXiv paper 2602.15922, here's what I found:

## Overview

The paper titled "World Action Models are Zero-shot Policies" was submitted on February 17, 2026, with authors led by Seonghyeon Ye and 35 co-authors.

## Key Contribution: DreamZero

DreamZero is a World Action Model (WAM) built upon a pretrained video diffusion backbone. Unlike VLAs (Vision-Language-Action models), WAMs learn physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves.

## Main Results

State-of-the-art Vision-Language-Action (VLA) models excel at semantic generalization but struggle to generalize to unseen physical motions in novel environments. In contrast, DreamZero results in over 2x improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in real robot experiments.

## Technical Innovation

Through model and system optimizations, DreamZero enables a 14B autoregressive video diffusion model to perform real-time closed-loop control at 7Hz.

## Cross-Embodiment Transfer

DreamZero demonstrates two forms of cross-embodiment transfer: video-only demonstrations from other robots or humans yield a relative improvement of over 42% on unseen task performance with just 10-20 minutes of data. More surprisingly, DreamZero enables few-shot embodiment adaptation, transferring to a new embodiment with only 30 minutes of play data while retaining zero-shot generalization.

The paper is available on arXiv and has an accompanying project page and GitHub repository with open-source code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "664488af-3798-4da9-9018-955b4d1e1e3e",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "8100077f-7d22-4ebc-9844-3f5ec9892dd8",
  "sourceToolAssistantUUID": "664488af-3798-4da9-9018-955b4d1e1e3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T19:37:03.052Z_

<details><summary>↩ Tool result · `toolu_018dEQ2RhdptQV5eC6CamuzV`</summary>

```text
Web search results for query: "arXiv 2504.02792 UWM Unified World Models Coupling Video Action Diffusion"

Links: [{"title":"[2504.02792] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"[2504.02792v1] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792v1"},{"title":"Paper page - Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://huggingface.co/papers/2504.02792"},{"title":"Unified World Models: A Scalable AI Framework For Video And Action Data","url":"https://quantumzeitgeist.com/unified-world-models-a-scalable-ai-framework-for-video-and-action-data/"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"[PDF] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-World-Models:-Coupling-Video-and-Action-for-Zhu-Yu/514b9977bdb57f6e9586461f36fcf6467a775b3c"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.02792/metadata"},{"title":"GitHub - WEIRDLabUW/unified-world-model: Unfied World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://github.com/WEIRDLabUW/unified-world-model"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets [Quick Review]","url":"https://liner.com/review/unified-world-models-coupling-video-and-action-diffusion-for-pretraining"}]

I found detailed information about arXiv paper 2504.02792. Here's what I found:

## Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets

The paper presents Unified World Models (UWM), a framework that leverages both video and action data for policy learning by integrating an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality.

### Key Capabilities

By controlling each diffusion timestep, UWM can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator.

### Main Results

Through simulated and real-world experiments, the work shows that: (1) UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning, (2) UWM naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies.

### Significance

The results suggest that UWM offers a promising step toward harnessing large, heterogeneous datasets for scalable robot learning, and provides a simple unification between the often disparate paradigms of imitation learning and world modeling.

### Availability

Videos and code are available at https://weirdlabuw.github.io/uwm/.

The paper was submitted on April 3, 2025 and authored by Chuning Zhu, Raymond Yu, Siyuan Feng, Benjamin Burchfiel, Paarth Shah, and Abhishek Gupta.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e35032f-498f-40ae-a393-8453a2511070",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "e8c7ca20-53d0-4277-9cf7-9198b88979b5",
  "sourceToolAssistantUUID": "3e35032f-498f-40ae-a393-8453a2511070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:37:03.614Z_

<details><summary>↩ Tool result · `toolu_01JQ6A9i6bjeAMCfvBjFUzYh`</summary>

```text
Web search results for query: "UWM Unified World Models code github DROID checkpoints"

Links: [{"title":"GitHub - WEIRDLabUW/unified-world-model: Unfied World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://github.com/WEIRDLabUW/unified-world-model"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"GitHub - thu-ml/Motus: Official code of Motus: A Unified Latent Action World Model · GitHub","url":"https://github.com/thu-ml/Motus"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/awesome-world-models"},{"title":"GitHub - SenseTime-FVG/OpenDWM: An open source code repository of driving world models, with training, inferencing, evaluation tools, and pretrained checkpoints. · GitHub","url":"https://github.com/sensetime-fvg/opendwm"},{"title":"GitHub - unitreerobotics/unifolm-world-model-action · GitHub","url":"https://github.com/unitreerobotics/unifolm-world-model-action"},{"title":"Paper page - Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://huggingface.co/papers/2504.02792"},{"title":"GitHub - World-In-World/world-in-world: Code implementation of the paper \"World-in-World: World Models in a Closed-Loop World\" (ICLR'26 Oral) · GitHub","url":"https://github.com/World-In-World/world-in-world"}]

Based on the search results, I found information about the UWM (Unified World Models) project:

## Overview

The repository provides a PyTorch implementation of Unified World Model (UWM) that combines action diffusion and video diffusion to enable scalable pretraining on large, heterogeneous robotics datasets.

## Code & Checkpoints

The official code is available on GitHub:
- **Repository**: The pretrained and cotrained DROID UWM checkpoints are released and can be downloaded and directly finetuned from.
- **GitHub Link**: https://github.com/WEIRDLabUW/unified-world-model
- **Project Page**: https://weirdlabuw.github.io/uwm/

## Repository Structure

The repository includes configuration files for pretraining and finetuning experiments, dataset wrappers for DROID, Robomimic, and LIBERO, with all datasets standardized using compressed Zarr buffers.

## Paper Citation

The work is titled "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets" by Zhu, Yu, Feng, Burchfiel, Shah, and Gupta, presented at Robotics: Science and Systems (RSS) in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c57e84d7-d388-479e-9088-ba2d6b78fbd8",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "2d6e6e16-21ce-4d11-831b-ce2c8b2b5f84",
  "sourceToolAssistantUUID": "c57e84d7-d388-479e-9088-ba2d6b78fbd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T19:37:09.057Z_

Good, I have initial search results. Now let me fetch the actual paper pages to verify the specific technical claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d6e6e16-21ce-4d11-831b-ce2c8b2b5f84",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTAFUPpYhnQpAcCVG4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9c502bd-7baa-4fbb-9430-8fa70ba807f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KggFv7mx8qKyw8sKSqKEXz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3104,
      "cache_read_input_tokens": 10937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3104,
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

_source line 14 · 2026-05-10T19:37:12.744Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UgBDtfaVf36VMvGKrQzNnA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.15922",
  "prompt": "Extract ALL technical details from the abstract and paper description: model size (parameters), backbone architecture, inference hardware requirements (GPUs), convergence caching details, flow-matching denoising, cosine similarity threshold, step reduction numbers (e.g. 16 to 4), whether zero additional parameters are needed, velocity-based convergence, and any claims about step reduction percentages. Be very precise with numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9c502bd-7baa-4fbb-9430-8fa70ba807f7",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTAFUPpYhnQpAcCVG4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d09c74eb-7153-499e-b8e0-7fd7c32f7aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KggFv7mx8qKyw8sKSqKEXz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3104,
      "cache_read_input_tokens": 10937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3104,
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

_source line 15 · 2026-05-10T19:37:16.992Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016sLyjSAhYSVYFGZvQaXpAo`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.15922v1",
  "prompt": "Extract ALL technical details about: (1) convergence caching - is it velocity-based? does it use cosine similarity threshold on successive predictions? what is the step reduction (e.g. 16 to 4 steps, 75% reduction)? (2) Does it require zero additional parameters? (3) Model size - 14B parameters? (4) Backbone - Wan2.1-I2V? (5) Inference hardware - 2x GB200? (6) Flow-matching denoising details. Be extremely precise with all numbers, thresholds, and technical specifics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d09c74eb-7153-499e-b8e0-7fd7c32f7aff",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTAFUPpYhnQpAcCVG4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86aafe01-ebb5-4be1-b45a-9e10cc76d49a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KggFv7mx8qKyw8sKSqKEXz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3104,
      "cache_read_input_tokens": 10937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3104,
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

_source line 16 · 2026-05-10T19:37:18.941Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Emkkiyb2dgG7QwDY7ZNkW3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.02792",
  "prompt": "Extract ALL technical details from the abstract and paper description: model architecture (DiT-B?), parameter count (180M?), training method (DDPM?), whether action and video use SEPARATE or shared diffusion timesteps, any details about architecture size, and whether it was accepted at RSS 2025."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86aafe01-ebb5-4be1-b45a-9e10cc76d49a",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTAFUPpYhnQpAcCVG4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e30ee99d-de08-48aa-8598-f1f0a18fb4c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KggFv7mx8qKyw8sKSqKEXz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3104,
      "cache_read_input_tokens": 10937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3104,
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

_source line 17 · 2026-05-10T19:37:22.540Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L2s3yDVWrqwKmURNZV6Jai`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.02792v1",
  "prompt": "Extract ALL technical details about: (1) Model architecture - is it DiT-B? How many parameters (180M)? (2) Training method - is it DDPM-based? (3) Diffusion timesteps - are action and video timesteps SEPARATE/independent? (4) Any specific architecture details, layer counts, dimensions. Be extremely precise with all numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e30ee99d-de08-48aa-8598-f1f0a18fb4c3",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTAFUPpYhnQpAcCVG4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77a8659b-ccd0-4985-b5b9-cccf9203ebac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KggFv7mx8qKyw8sKSqKEXz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3104,
      "cache_read_input_tokens": 10937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3104,
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

_source line 18 · 2026-05-10T19:37:23.046Z_

<details><summary>↩ Tool result · `toolu_01UgBDtfaVf36VMvGKrQzNnA`</summary>

```text
# Technical Details Extraction from arXiv:2602.15922

Based on the provided content, here are the technical specifications found:

**Model Architecture & Size:**
- "14B autoregressive video diffusion model" serving as the World Action Model backbone

**Inference Performance:**
- "real-time closed-loop control at 7Hz" achieved through model and system optimizations

**Training & Data:**
- Learns from "heterogeneous robot data without relying on repetitive demonstrations"
- Enables "few-shot embodiment adaptation" with "only 30 minutes of play data"

**Performance Improvements:**
- "over 2x improvement in generalization to new tasks and environments" versus state-of-the-art VLAs
- "relative improvement of over 42% on unseen task performance" via cross-embodiment transfer using 10-20 minutes of video-only demonstrations

**Learning Approach:**
- The model "jointly modeling video and action" predicts future world states
- Uses "video as a dense representation of how the world evolves"

**Notable Limitation:**
The abstract and description provided do not contain specifications regarding convergence caching, flow-matching denoising parameters, cosine similarity thresholds, step reduction numbers, or claims about zero additional parameters being required.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d09c74eb-7153-499e-b8e0-7fd7c32f7aff",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "00b93893-1168-4684-bd25-bd4d77a0091f",
  "sourceToolAssistantUUID": "d09c74eb-7153-499e-b8e0-7fd7c32f7aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T19:37:23.314Z_

<details><summary>↩ Tool result · `toolu_01Emkkiyb2dgG7QwDY7ZNkW3`</summary>

```text
# Technical Details from "Unified World Models" Paper

Based on the provided abstract and page content, here are the extractable technical details:

**Architecture & Parameters:**
- No specific model architecture designation (e.g., DiT-B) or parameter counts are mentioned in the available content.

**Diffusion Approach:**
- The framework employs "independent diffusion timesteps govern each modality," indicating that action and video use **SEPARATE diffusion timesteps** rather than shared ones.

**Training Method:**
- The abstract references "an action diffusion process and a video diffusion process" but does not specify whether DDPM or another training methodology was used.

**Unified Capability:**
- The model "can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator" through modality-specific diffusion timestep control.

**Conference Status:**
- The document does not indicate acceptance at RSS 2025 or any specific conference venue.

**Available Resources:**
- The authors note that "Videos and code are available" at their project website, though the full URL is not expanded in this page excerpt.

The abstract emphasizes the framework's ability to leverage heterogeneous datasets (both video and action data) for robot learning, but most architectural specifics are not detailed in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e30ee99d-de08-48aa-8598-f1f0a18fb4c3",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "63c4c53c-729d-4579-85dd-60c907ce1502",
  "sourceToolAssistantUUID": "e30ee99d-de08-48aa-8598-f1f0a18fb4c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T19:37:24.699Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QCtWFFLsX7C9KoqSfPXsTM`</summary>

```json
{
  "url": "https://github.com/WEIRDLabUW/unified-world-model",
  "prompt": "Extract details about: (1) Is the code publicly available and functional? (2) Are DROID checkpoints available for download? Where are they hosted? (3) What does the README say about available models/checkpoints? (4) What is the repository status - active, maintained? (5) Any model architecture details mentioned (DiT-B, parameter count, etc.)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63c4c53c-729d-4579-85dd-60c907ce1502",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTAFUPpYhnQpAcCVG4u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55377ebd-75cf-4b50-a555-1cadf360bc43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KggFv7mx8qKyw8sKSqKEXz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3104,
      "cache_read_input_tokens": 10937,
      "output_tokens": 820,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3104
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 820,
          "cache_read_input_tokens": 10937,
          "cache_creation_input_tokens": 3104,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3104,
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

_source line 21 · 2026-05-10T19:37:26.585Z_

<details><summary>↩ Tool result · `toolu_016sLyjSAhYSVYFGZvQaXpAo`</summary>

```text
# Technical Details Summary

## (1) Convergence Caching (DiT Caching)

**Mechanism**: Velocity-based with cosine similarity threshold
- "exploits the directional consistency of velocity vectors learned during flow matching"
- Tracks "cosine similarity between successive velocity predictions"
- When similarity exceeds threshold τ, "bypasses the DiT forward pass for a window of a few steps by reusing the cached velocity vector"

**Step Reduction**: 16 → 4 steps (75% reduction)
- "reducing the average number of DiT steps from 16 to 4 with minimal degradation to predicted video and action fidelity"
- Specific threshold value not disclosed in document

## (2) Additional Parameters

**Zero additional parameters**: No
- Introduces "state encoders, action encoders, and decoders" as "minimal additional parameters"
- Freezes "text encoder, image encoder, and VAE" while updating "all DiT blocks"

## (3) Model Size

**14 billion parameters**
- "14B robot foundation model built upon a pretrained image-to-video diffusion backbone"
- Ablation tested 5B variant showing inferior performance (21% vs 50% task progress)

## (4) Backbone

**Wan2.1-I2V-14B-480P**
- "image-to-video diffusion model" used as backbone
- Training uses flow-matching objective with teacher forcing

## (5) Inference Hardware

**2× GB200 GPUs**
- "38× inference speedup...on GB200" from Table 1
- CFG parallelism "distributed across two GPUs"

## (6) Flow-Matching Denoising

Training uses shared timestep tk ∼ U(0,1) for both modalities. Loss function: "∥𝐮θ([𝐳ᵗᵏᵏ,𝐚ᵗᵏᵏ];𝒞ₖ,𝐜,𝐪ₖ,tₖ)−𝐯ᵏ∥²"

**DreamZero-Flash**: Decouples schedules—tᵏᵥᵢ𝒹𝒆𝒐 = 1−η where η ∼ Beta(7,1), while tᵏᵃᶜᵗ ∼ U(0,1), achieving 1→4 denoising steps with "9% below 4-step baseline" performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86aafe01-ebb5-4be1-b45a-9e10cc76d49a",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "66f36ae3-5193-4f33-aa8c-857511b0cfe1",
  "sourceToolAssistantUUID": "86aafe01-ebb5-4be1-b45a-9e10cc76d49a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:37:30.185Z_

<details><summary>↩ Tool result · `toolu_01QCtWFFLsX7C9KoqSfPXsTM`</summary>

```text
# Unified World Models Repository Analysis

## (1) Public Availability & Functionality
Yes, the code is publicly available on GitHub under WEIRDLabUW/unified-world-model. Installation is straightforward: `pip install -e .` with a note about potential TensorFlow Datasets issues with DROID.

## (2) DROID Checkpoints Availability
The repository confirms that pretrained and cotrained DROID checkpoints are released and hosted on Google Drive. The documentation states: `"We release the pretrained and cotrained DROID UWM checkpoints here"` with a link to a shared Google Drive folder containing the models.

## (3) README Model/Checkpoint Information
The README explicitly mentions releasing two checkpoint sets:
- LIBERO-90 pretrained checkpoint available for direct download
- Pretrained and cotrained DROID checkpoints available via Google Drive

Users can download these and directly finetune from the released checkpoints without retraining from scratch.

## (4) Repository Status
The repository appears actively maintained with recent commit activity (11 commits on main branch). It has 221 stars and 14 forks, indicating community interest. The project includes comprehensive documentation for multiple datasets and experiments.

## (5) Model Architecture Details
The README provides no specific architecture specifications (no mention of DiT-B, parameter counts, layer configurations, or similar technical details). Architecture information would likely be available in the linked paper or on the project website, not in this README.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55377ebd-75cf-4b50-a555-1cadf360bc43",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "90291036-69df-4c43-8c1f-adad6635a0d9",
  "sourceToolAssistantUUID": "55377ebd-75cf-4b50-a555-1cadf360bc43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T19:37:31.755Z_

<details><summary>↩ Tool result · `toolu_01L2s3yDVWrqwKmURNZV6Jai`</summary>

```text
# Technical Details of Unified World Models (UWM)

## Model Architecture

**Architecture Type:** Diffusion Transformer (not specified as DiT-B)

**Parameters:** The document does not specify total parameter count or confirm 180M parameters.

**Key Components:**
- ResNet-18 encoder for frame processing from each camera view
- Transformer backbone with Adaptive Layer Normalization (AdaLN) conditioning
- Frozen SDXL VAE for latent image encoding: full-size (224,224,3) → latent (28,28,4)
- Spatiotemporal patchifier: (4,4,2) patch size
- "Randomly initialized register tokens" for multi-modal feature sharing

The architecture processes observations through separate encoding paths, with diffusion timesteps conditioning applied via AdaLN rather than concatenation.

## Training Method

**Framework:** Denoising Diffusion Probabilistic Models (DDPM)-based with independent diffusion processes for actions and observations.

**Training Objective (Equation 1):**
The model trains a coupled score network minimizing weighted losses for both modalities:

`ℓ(θ) = 𝔼[wa||ϵaθ−ϵa||²₂ + wo'||ϵo'θ−ϵo'||²₂]`

where ta and to' are independently sampled timesteps from U(0,T).

## Decoupled Diffusion Timesteps

**Critical Design Feature:** Action and video diffusion timesteps are **SEPARATE and INDEPENDENTLY CONTROLLED**.

The model uses: `sθ(o, ata, oto'', ta, to')`

This enables flexible inference:
- **Policy p(a|o):** Set to'=T (marginalize observations)
- **Forward Dynamics p(o'|o,a):** Set ta=0 (condition on clean actions)
- **Inverse Dynamics p(a|o,o'):** Set to'=0 (condition on clean observations)
- **Video p(o'|o):** Set ta=T (marginalize actions)

## Additional Architectural Details

**Conditioning:** Current observations encoded via ResNet-18 features concatenated with sinusoidal timestep embeddings, applied through AdaLN.

**Action Processing:** "Action chunks of length ha" encoded per-timestep using shallow MLPs.

**Observation Processing:** Frame-stacked observations of length ho from nc camera views.

**Training Scale:** Pretrained for 100K gradient steps on 2000 trajectories; finetuned for task-specific demonstrations.

The document does not provide layer counts, hidden dimensions, or confirm parameter specifications beyond architectural components described.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77a8659b-ccd0-4985-b5b9-cccf9203ebac",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "75c1372b-5ad7-4c95-bd57-fae4d4278586",
  "sourceToolAssistantUUID": "77a8659b-ccd0-4985-b5b9-cccf9203ebac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T19:37:34.297Z_

Now let me get more specific details about the DreamZero paper's claims on "zero additional parameters" and the UWM architecture specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75c1372b-5ad7-4c95-bd57-fae4d4278586",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTCKYGiYPxtrVrnQQ2Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a387c74e-7ebd-448f-9d16-62bf45257280",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqR9epbW6m4ocNFVPAptZ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 361,
      "cache_creation_input_tokens": 2834,
      "cache_read_input_tokens": 14041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2834,
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

_source line 25 · 2026-05-10T19:37:40.921Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JLGwd3p3cro2py5KQ54teG`</summary>

```json
{
  "url": "https://dreamzero0.github.io/",
  "prompt": "Extract any technical details about: convergence caching, velocity-based caching, cosine similarity threshold, step reduction, inference hardware (GB200), model parameters (14B), Wan2.1-I2V backbone, and whether it requires zero additional parameters or adds new parameters. Also look for any corrections vs what's in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a387c74e-7ebd-448f-9d16-62bf45257280",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTCKYGiYPxtrVrnQQ2Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0647c19-47c9-4d11-9152-5c6c9d4f4907",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqR9epbW6m4ocNFVPAptZ7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 361,
      "cache_creation_input_tokens": 2834,
      "cache_read_input_tokens": 14041,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2834
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 361,
          "output_tokens": 236,
          "cache_read_input_tokens": 14041,
          "cache_creation_input_tokens": 2834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2834,
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

### Tool call

_source line 26 · 2026-05-10T19:37:40.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EVq9iQGGs9EiyXWbZnMoP9`</summary>

```json
{
  "query": "UWM unified world models DiT-B 180M parameters architecture details RSS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0647c19-47c9-4d11-9152-5c6c9d4f4907",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTCKYGiYPxtrVrnQQ2Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a428237b-c6fc-4ce9-aed8-76b3396545b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqR9epbW6m4ocNFVPAptZ7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 361,
      "cache_creation_input_tokens": 2834,
      "cache_read_input_tokens": 14041,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2834
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 361,
          "output_tokens": 236,
          "cache_read_input_tokens": 14041,
          "cache_creation_input_tokens": 2834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2834,
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

_source line 27 · 2026-05-10T19:37:44.566Z_

<details><summary>↩ Tool result · `toolu_01JLGwd3p3cro2py5KQ54teG`</summary>

```text
# Technical Details Analysis

Based on the provided webpage content, I found **no mentions** of the following technical specifications:

- Convergence caching
- Velocity-based caching
- Cosine similarity threshold
- Step reduction techniques
- Inference hardware (GB200)
- Wan2.1-I2V backbone
- Whether the approach requires zero additional parameters or adds new parameters

## What IS documented on the page:

The webpage confirms:
- **Model size**: "14B autoregressive video diffusion model"
- **Real-time performance**: "7Hz closed-loop control" achieved through "38× speedup"
- **Inference optimization**: "16, 4, and 1 diffusion steps" with "action chunk smoothing" and "asynchronous inference"
- **Backbone**: References a "pretrained video diffusion backbone" but doesn't specify the model architecture by name

The technical details you're asking about appear to exist only in the full arXiv paper (referenced but not quoted in the webpage), not in this project summary. The webpage focuses on results and capabilities rather than implementation minutiae.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0647c19-47c9-4d11-9152-5c6c9d4f4907",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "b957bab0-5f82-4279-a190-3d1c2c223ddc",
  "sourceToolAssistantUUID": "b0647c19-47c9-4d11-9152-5c6c9d4f4907",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T19:37:48.546Z_

<details><summary>↩ Tool result · `toolu_01EVq9iQGGs9EiyXWbZnMoP9`</summary>

```text
Web search results for query: "UWM unified world models DiT-B 180M parameters architecture details RSS 2025"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets [Quick Review]","url":"https://liner.com/review/unified-world-models-coupling-video-and-action-diffusion-for-pretraining"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://liqing.io/mindflow/Papers/2504-UWM"},{"title":"Unified World Models: A Scalable AI Framework For Video And Action Data","url":"https://quantumzeitgeist.com/unified-world-models-a-scalable-ai-framework-for-video-and-action-data/"},{"title":"Unified World Model Specification","url":"https://www.emergentmind.com/topics/unified-design-specification-for-world-models"},{"title":"Towards Unified World Models for Visual Navigation via Memory-Augmented Planning and Foresight","url":"https://arxiv.org/html/2510.08713"},{"title":"UniDWM: Towards a Unified Driving World Model via Multifaceted Representation Learning","url":"https://arxiv.org/html/2602.01536"},{"title":"Paper page - Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://huggingface.co/papers/2504.02792"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.02792v1"}]

Based on the search results, here are the architecture details for UWM (Unified World Models) with the DiT-B 180M parameter configuration:

## Architecture Overview

UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality.

## DiT-B 180M Configuration

UWM is 180M parameters at the DiT-B scale, using a Diffusion Transformer (DiT) as the backbone architecture.

## Key Architectural Components

1. **Backbone**: DiT + AdaLN serves as the core architecture.

2. **Modal Information Exchange**: 8 register tokens act as a scratchpad for inter-modal information exchange, with register tokens facilitating information sharing between the action and image latent spaces.

3. **Video Encoding**: Frozen SDXL VAE is used as the image encoder.

4. **Diffusion Process**: UWM decouples diffusion timesteps for action and next-observation predictions, enabling flexible inference for policies, dynamics models, inverse models, and video prediction from a single model.

5. **Conditioning Method**: UWM uses decoupled timesteps with encoder-based conditioning for observation inputs.

The paper was published in April 2025 and demonstrates this 180M parameter model's effectiveness for robot learning tasks through pretraining on large-scale multitask datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a428237b-c6fc-4ce9-aed8-76b3396545b2",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "825ff0a0-cc6c-4a61-95ef-3ef843c5583c",
  "sourceToolAssistantUUID": "a428237b-c6fc-4ce9-aed8-76b3396545b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-10T19:37:52.170Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GbFNxFuZrZLPSScDRwCmWK`</summary>

```json
{
  "url": "https://weirdlabuw.github.io/uwm/",
  "prompt": "Extract: (1) Is this paper accepted at RSS 2025? (2) What is the model architecture - DiT-B? How many parameters - 180M? (3) Training method - DDPM? (4) Any specific technical details about the architecture, training, or results. Be precise."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "825ff0a0-cc6c-4a61-95ef-3ef843c5583c",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTDZLm1iUqzyuLvBG77",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca60b331-53cc-4a7d-9fd4-3f02cb86fb47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C8A8whbL52z7zd8AvvQ3W8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 16875,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1775
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 16875,
          "cache_creation_input_tokens": 1775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1775,
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

_source line 30 · 2026-05-10T19:37:57.765Z_

<details><summary>↩ Tool result · `toolu_01GbFNxFuZrZLPSScDRwCmWK`</summary>

```text
# Analysis of Unified World Models Paper

## (1) RSS 2025 Acceptance
Yes, the paper is accepted at **Robotics: Science and Systems (RSS) 2025**. It also received a "Best Paper Award" at the "ICML 2025 Workshop on Building Physically Plausible World Models."

## (2) Model Architecture and Parameters
The webpage provides **no specific details** about model architecture (e.g., DiT-B) or parameter counts (e.g., 180M). The only architectural description states: "Unified World Model (UWM) is a **multimodal diffusion transformer that uses separate diffusion timesteps for actions and videos**." No further specifications are disclosed in this content.

## (3) Training Method
The paper uses a diffusion-based approach but does not explicitly name "DDPM." The method employs: "separate timesteps for each modality" where "diffusion timesteps for actions and next observations are sampled independently at random." For video-only data, missing actions are treated as "fully noised, manually setting the action diffusion timestep to T."

## (4) Technical Details Provided
- **Key innovation**: Jointly trains on robot trajectories (with actions) and unlabeled videos (without actions)
- **Flexible inference**: Single model generates policies, forward dynamics, inverse dynamics, and video predictions
- **Data handling**: Missing actions masked as noise, enabling use of action-free video data

For complete architectural and training specifications, the [full paper](https://arxiv.org/abs/2504.02792) would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca60b331-53cc-4a7d-9fd4-3f02cb86fb47",
  "isSidechain": true,
  "promptId": "1e12b5d5-2db0-48a9-ac19-047a4c1f31ab",
  "agentId": "a15b98ed49a9f8d53",
  "type": "user",
  "uuid": "c1983dea-fe8a-4617-a398-3bb6c9e6028a",
  "sourceToolAssistantUUID": "ca60b331-53cc-4a7d-9fd4-3f02cb86fb47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T19:38:33.177Z_

I now have comprehensive information to provide a thorough verification report. Here is my analysis:

---

## Verification Report: DreamZero and UWM Papers

### Paper 1: DreamZero (arXiv 2602.15922, Feb 2026)

**Title:** "World Action Models are Zero-shot Policies" -- **CONFIRMED.** The paper exists on arXiv at the stated ID, submitted February 17, 2026.

Claim-by-claim verification:

| Claim | Status | Finding |
|---|---|---|
| **Velocity-based convergence caching within flow-matching denoising** | **CONFIRMED** | The paper describes caching that "exploits the directional consistency of velocity vectors learned during flow matching." |
| **Cosine similarity threshold on successive predictions** | **CONFIRMED** | The paper tracks "cosine similarity between successive velocity predictions" and when similarity exceeds threshold tau, it "bypasses the DiT forward pass for a window of a few steps by reusing the cached velocity vector." |
| **75% step reduction (16 to 4)** | **CONFIRMED** | The paper states: "reducing the average number of DiT steps from 16 to 4 with minimal degradation to predicted video and action fidelity." That is exactly 75%. |
| **Zero additional parameters** | **PARTIALLY INCORRECT** | The convergence caching itself requires zero additional parameters (it reuses cached velocity vectors). However, DreamZero as a whole does introduce "minimal additional parameters" in the form of "state encoders, action encoders, and decoders." The proposal's claim of "zero additional parameters" is misleading if it refers to the overall model rather than narrowly to the caching mechanism. |
| **14B parameter model** | **CONFIRMED** | The paper describes a "14B robot foundation model built upon a pretrained image-to-video diffusion backbone." Ablation with a 5B variant showed significantly worse performance (21% vs 50% task progress). |
| **Wan2.1-I2V backbone** | **CONFIRMED** | The backbone is identified as "Wan2.1-I2V-14B-480P," an image-to-video diffusion model. |
| **Requires 2x GB200 for inference** | **CONFIRMED** | The paper describes "38x inference speedup...on GB200" and CFG (Classifier-Free Guidance) parallelism "distributed across two GPUs," confirming 2x GB200 for inference. |

**Additional note on DreamZero:** The paper also describes a "DreamZero-Flash" variant that decouples video and action diffusion schedules, achieving 1-step denoising (down from 4) but at 9% below the 4-step baseline performance. Code is publicly available at `https://github.com/dreamzero0/dreamzero`.

---

### Paper 2: UWM (arXiv 2504.02792, April 2025)

**Title:** "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets" -- **CONFIRMED.** Paper exists at the stated arXiv ID.

Claim-by-claim verification:

| Claim | Status | Finding |
|---|---|---|
| **180M-parameter DiT-B architecture** | **CONFIRMED** | Multiple sources confirm UWM uses a DiT-B (Diffusion Transformer-B) backbone at approximately 180M parameters. The architecture uses AdaLN conditioning, a frozen SDXL VAE for image encoding, 8 register tokens for inter-modal information exchange, and ResNet-18 observation encoders. |
| **DDPM-based training** | **CONFIRMED** | The training objective is DDPM-based, with loss: `wa * ||eps_a_theta - eps_a||^2 + wo * ||eps_o_theta - eps_o||^2`, which is the standard DDPM epsilon-prediction loss formulation. |
| **SEPARATE diffusion timesteps for action and video** | **CONFIRMED** | This is the core design feature. Action timestep `ta` and observation timestep `to'` are "independently sampled" from `U(0,T)`. This enables flexible inference: setting `to'=T` gives a pure policy, setting `ta=0` gives forward dynamics, setting `to'=0` gives inverse dynamics, and setting `ta=T` gives a video generator. |
| **RSS 2025** | **CONFIRMED** | The paper is accepted at Robotics: Science and Systems (RSS) 2025. It also received a Best Paper Award at the ICML 2025 Workshop on Building Physically Plausible World Models. |
| **Public code** | **CONFIRMED** | Code is publicly available at `https://github.com/WEIRDLabUW/unified-world-model` (221 stars, 14 forks, 11 commits on main). |
| **DROID checkpoints** | **CONFIRMED** | Pretrained and cotrained DROID UWM checkpoints are released and hosted on Google Drive. LIBERO-90 pretrained checkpoints are also available. Users can download and directly finetune from them. |

---

### Summary

**DreamZero:** 6 of 7 claims verified. The one issue is the "zero additional parameters" claim -- the convergence caching mechanism itself adds no parameters, but DreamZero as a whole does add minimal parameters (state/action encoders and decoders). If the proposal attributes "zero additional parameters" to the caching scheme specifically, this is accurate; if it implies the entire DreamZero framework adds no parameters on top of the Wan2.1 backbone, that is incorrect.

**UWM:** All 6 claims fully verified. The paper, architecture, training method, separate timesteps, public code, and DROID checkpoints all match the proposal's description.

Sources:
- [DreamZero on arXiv](https://arxiv.org/abs/2602.15922)
- [DreamZero full paper HTML](https://arxiv.org/html/2602.15922v1)
- [DreamZero project page](https://dreamzero0.github.io/)
- [DreamZero GitHub](https://github.com/dreamzero0/dreamzero)
- [UWM on arXiv](https://arxiv.org/abs/2504.02792)
- [UWM full paper HTML](https://arxiv.org/html/2504.02792v1)
- [UWM project page](https://weirdlabuw.github.io/uwm/)
- [UWM GitHub](https://github.com/WEIRDLabUW/unified-world-model)
- [UWM on HuggingFace Papers](https://huggingface.co/papers/2504.02792)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1983dea-fe8a-4617-a398-3bb6c9e6028a",
  "isSidechain": true,
  "agentId": "a15b98ed49a9f8d53",
  "requestId": "req_011CauTEEkLu8TvQCSk7RZg5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e786ffc-5cc5-4ac0-8365-673af65fb499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "457e2ae8-268a-4527-8fc3-bb8d04ff217d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQf8DuzJWgYHo3xwCAp1k9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 18650,
      "output_tokens": 1623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 517
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1623,
          "cache_read_input_tokens": 18650,
          "cache_creation_input_tokens": 517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 517,
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
