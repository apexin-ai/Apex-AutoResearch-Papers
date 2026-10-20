# Research conversation: You are helping with an ML paper review. I need to verify claims about "DreamZero" (arXiv 2602.15922, Feb 2026), a World

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4a78718ce6bd7e9e.jsonl`
- **Structured JSON:** [`496c59386315642acb9d.json`](../../sessions/49/496c59386315642acb9d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-10T18:34:07.990Z_

You are helping with an ML paper review. I need to verify claims about "DreamZero" (arXiv 2602.15922, Feb 2026), a World Action Model paper.

Specifically verify:
1. Does DreamZero implement velocity-based convergence caching within denoising? (cosine similarity threshold on successive predictions)
2. Does it achieve 16→4 effective steps (75% reduction)?
3. Is the caching mechanism fixed-threshold only (cannot extend computation)?
4. Does it operate on JOINT velocity (video+action combined) or per-modality?
5. Does DreamZero-Flash exist (1-step variant)?

Use WebSearch to find the paper and WebFetch to read relevant sections. Search for "DreamZero world action model velocity caching" and "arXiv 2602.15922". Report what you find with specific details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "ffb06599-ac6d-4bb7-81d9-03acbc701428",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:34:07.994Z_

```json
{
  "parentUuid": "ffb06599-ac6d-4bb7-81d9-03acbc701428",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
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
  "uuid": "21b12152-e05d-467f-9a8a-81e9914518cd",
  "timestamp": "2026-05-10T18:34:07.994Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:34:12.076Z_



I'll search for the paper and fetch it to verify these claims. Let me start by loading the necessary tools and searching for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21b12152-e05d-467f-9a8a-81e9914518cd",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNMvqy41cBQAFJBZ2YD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0323c2c-f14b-46a5-be8f-a4e028ab41cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBrS7uNScgah6Xdprw9Gcp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8973,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8973,
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

_source line 4 · 2026-05-10T18:34:12.576Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01V7HZmaExug5rf2quUnjzuh`</summary>

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
  "parentUuid": "f0323c2c-f14b-46a5-be8f-a4e028ab41cb",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNMvqy41cBQAFJBZ2YD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bebf26a2-89d4-4d89-aa53-8d1a90f95f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBrS7uNScgah6Xdprw9Gcp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8973,
      "cache_read_input_tokens": 0,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8973
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8973,
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

_source line 5 · 2026-05-10T18:34:12.584Z_

<details><summary>↩ Tool result · `toolu_01V7HZmaExug5rf2quUnjzuh`</summary>

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
  "parentUuid": "bebf26a2-89d4-4d89-aa53-8d1a90f95f7b",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "8fcc6bf3-23fc-4a14-bfbf-9580063c1473",
  "sourceToolAssistantUUID": "bebf26a2-89d4-4d89-aa53-8d1a90f95f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:34:15.292Z_



Now let me search for the paper using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fcc6bf3-23fc-4a14-bfbf-9580063c1473",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNNGqkLgAfzyd7DHmsb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "111b9feb-6310-47e4-bf96-56033fdb7c65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3nPEmqvJ7u89tKeYQJPGM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 8973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1918,
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

_source line 7 · 2026-05-10T18:34:16.369Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011YXZcfm7zR2TffBjiTbVtN`</summary>

```json
{
  "query": "DreamZero world action model velocity caching arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "111b9feb-6310-47e4-bf96-56033fdb7c65",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNNGqkLgAfzyd7DHmsb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dcf2225-8739-4529-8e7b-93b671828752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3nPEmqvJ7u89tKeYQJPGM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 8973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1918,
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

_source line 8 · 2026-05-10T18:34:16.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RU9cJBf7H2tCp5DkxYy94F`</summary>

```json
{
  "query": "arXiv 2602.15922 DreamZero"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dcf2225-8739-4529-8e7b-93b671828752",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNNGqkLgAfzyd7DHmsb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d0b775f-a090-406c-9aac-d1135789f38b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3nPEmqvJ7u89tKeYQJPGM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 8973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1918,
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

_source line 9 · 2026-05-10T18:34:17.166Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GvA9WbWKSwV84pdUir87RC`</summary>

```json
{
  "query": "\"DreamZero\" \"world action model\" denoising caching"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d0b775f-a090-406c-9aac-d1135789f38b",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNNGqkLgAfzyd7DHmsb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a8b5fc4-b05c-4887-b067-bc093c867582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3nPEmqvJ7u89tKeYQJPGM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 8973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1918,
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

### Tool result

_source line 10 · 2026-05-10T18:34:23.300Z_

<details><summary>↩ Tool result · `toolu_01RU9cJBf7H2tCp5DkxYy94F`</summary>

```text
Web search results for query: "arXiv 2602.15922 DreamZero"

Links: [{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"},{"title":"GitHub - dreamzero0/dreamzero: Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals · GitHub","url":"https://github.com/dreamzero0/dreamzero"},{"title":"2026-2-19 World Action Models are Zero-shot Policies Seonghyeon Ye† Yunhao Ge*","url":"https://arxiv.org/pdf/2602.15922"},{"title":"Paper page - World Action Models are Zero-shot Policies","url":"https://huggingface.co/papers/2602.15922"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"World Action Models are Zero-shot Policies (arXiv:2602.15922v1) - ScienceStack","url":"https://www.sciencestack.ai/paper/2602.15922"},{"title":"GEAR-Dreams/DreamZero-DROID · Hugging Face","url":"https://huggingface.co/GEAR-Dreams/DreamZero-DROID"},{"title":"World Action Models are Zero-shot Policies | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.15922"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922"},{"title":"dreamzero/README.md at main · dreamzero0/dreamzero","url":"https://github.com/dreamzero0/dreamzero/blob/main/README.md"}]

Based on the search results, here's information about arXiv paper 2602.15922 on DreamZero:

## Overview

DreamZero is a World Action Model (WAM) built upon a pretrained video diffusion backbone. Unlike Vision-Language-Action (VLA) models, WAMs learn physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves.

## Key Capabilities

By jointly modeling video and action, DreamZero learns diverse skills effectively from heterogeneous robot data without relying on repetitive demonstrations. This results in over 2x improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in real robot experiments.

Through model and system optimizations, the 14B autoregressive video diffusion model performs real-time closed-loop control at 7Hz.

## Transfer Learning

The model demonstrates strong transfer capabilities: Video-only demonstrations from other robots or humans yield a relative improvement of over 42% on unseen task performance with just 10-20 minutes of data. DreamZero enables few-shot embodiment adaptation, transferring to a new embodiment with only 30 minutes of play data while retaining zero-shot generalization.

The paper was submitted to arXiv on February 17, 2026, and a GitHub repository with code and pretrained models is available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d0b775f-a090-406c-9aac-d1135789f38b",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "a8a99a2c-d017-4d08-a2d6-e2f9a5f9d72c",
  "sourceToolAssistantUUID": "6d0b775f-a090-406c-9aac-d1135789f38b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T18:34:23.619Z_

<details><summary>↩ Tool result · `toolu_011YXZcfm7zR2TffBjiTbVtN`</summary>

```text
Web search results for query: "DreamZero world action model velocity caching arXiv 2026"

Links: [{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"World Action Models as Zero-Shot Policies","url":"https://www.emergentmind.com/papers/2602.15922"},{"title":"2026-2-4 World Action Models are Zero-shot Policies Seonghyeon Ye† Yunhao Ge*","url":"https://dreamzero0.github.io/DreamZero.pdf"},{"title":"GitHub - dreamzero0/dreamzero: Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals · GitHub","url":"https://github.com/dreamzero0/dreamzero"},{"title":"Paper page - World Action Models are Zero-shot Policies","url":"https://huggingface.co/papers/2602.15922"},{"title":"World Action Models are Zero-shot Policies | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.15922"},{"title":"[2602.15922v1] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922v1"}]

I found comprehensive information about DreamZero on arXiv 2026. Here's what the search revealed:

## Overview

DreamZero is a World Action Model (WAM) that learns diverse skills effectively from heterogeneous robot data by jointly modeling video and action without relying on repetitive demonstrations.

## Key Technical Features

**Architecture and Velocity Caching:**
DreamZero uses an autoregressive architecture that replaces predicted frames with ground-truth observations in the KV cache, eliminating compounding errors while enabling efficient inference via KV caching. Additionally, DiT Caching reuses previously computed diffusion velocities/steps to cut the number of expensive backbone passes.

**Model Details:**
DreamZero is a 14B autoregressive video diffusion model that performs real-time closed-loop control at 7Hz through model and system optimizations. The model employs a 14B parameter autoregressive diffusion transformer with decoupled noise schedules, enabling efficient closed-loop control and robust modality alignment.

## Performance

DreamZero results in over 2x improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in real robot experiments. Video-only demonstrations from other robots or humans yield a relative improvement of over 42% on unseen task performance with just 10-20 minutes of data, and DreamZero enables few-shot embodiment adaptation, transferring to a new embodiment with only 30 minutes of play data while retaining zero-shot generalization.

The paper (arXiv 2602.15922) was published in February 2026 and is available at https://arxiv.org/abs/2602.15922.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dcf2225-8739-4529-8e7b-93b671828752",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "18f71aed-ce8c-4ed7-b94b-5e6bf98f23d0",
  "sourceToolAssistantUUID": "3dcf2225-8739-4529-8e7b-93b671828752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:34:23.627Z_

<details><summary>↩ Tool result · `toolu_01GvA9WbWKSwV84pdUir87RC`</summary>

```text
Web search results for query: ""DreamZero" "world action model" denoising caching"

Links: [{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"(PDF) World Action Models are Zero-shot Policies","url":"https://www.researchgate.net/publication/400930242_World_Action_Models_are_Zero-shot_Policies"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"GitHub - dreamzero0/dreamzero: Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals · GitHub","url":"https://github.com/dreamzero0/dreamzero"},{"title":"NVIDIA's Two Papers Unveil New Paradigm for Embodied Intelligence Post-VLA","url":"https://eu.36kr.com/en/p/3678616267874953"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"[Literature Review] World Action Models are Zero-shot Policies","url":"https://www.themoonlight.io/en/review/world-action-models-are-zero-shot-policies"},{"title":"NVIDIA DreamZero. We introduce DreamZero, a World Action… | by Ranko Mosic | Feb, 2026 | Medium","url":"https://ranko-mosic.medium.com/nvidia-dreamzero-972fa95420b4"},{"title":"World Action Models are Zero-shot Policies (arXiv:2602.15922v1) - ScienceStack","url":"https://www.sciencestack.ai/paper/2602.15922"}]

Based on the search results, here's what I found about DreamZero, world action models, denoising, and caching:

## Overview

DreamZero is a 14B World Action Model (WAM) that jointly predicts video and actions. DreamZero is built upon a pretrained video diffusion backbone. Unlike VLAs, WAMs learn physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves.

## Denoising

During inference, DreamZero jointly denoises video and action chunks, leveraging KV caching for efficiency. DreamZero-Flash biases video toward high-noise states via a Beta distribution while keeping action noise uniform, training the model to predict clean actions from noisy visual context.

## KV Caching Strategy

After each action chunk is executed, DreamZero replaces predicted frames with ground-truth observations in the KV cache, eliminating compounding errors while enabling efficient inference via KV caching. DreamZero reuses cached velocities when the cosine similarity between successive velocities exceeds a threshold, reducing effective DiT steps from 16 to 4 with minimal quality loss on action prediction.

## Performance

System-, implementation-, and model-level optimizations achieve a 38× inference speedup without degrading performance, enabling DreamZero to generate action chunks at approximately 7Hz for smooth, real-time robotic control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a8b5fc4-b05c-4887-b067-bc093c867582",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "6fd978a1-7563-462f-9425-c9a177e412ad",
  "sourceToolAssistantUUID": "9a8b5fc4-b05c-4887-b067-bc093c867582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T18:34:27.704Z_

Good, I'm finding strong initial results. Let me now fetch the actual paper content to get precise details on the velocity caching mechanism, the threshold behavior, per-modality vs. joint operation, and DreamZero-Flash.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fd978a1-7563-462f-9425-c9a177e412ad",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNP6YeSjVZi84n57uAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3bd2c2e-205c-48c6-8ce1-adf7f451c6ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DtC62m1zeNit8EbxCxjJWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 10891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2715,
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

_source line 14 · 2026-05-10T18:34:33.763Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HocZwciaPBUKhw4EWe3RVf`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.15922v1",
  "prompt": "Extract ALL details about:\n1. Velocity caching / DiT caching mechanism - how does it work? Does it use cosine similarity on successive velocity predictions? What is the threshold? Is the threshold fixed or adaptive? Can computation be extended (more steps)?\n2. The step reduction - does it go from 16 to 4 steps? What metric is used to measure quality?\n3. Does the caching operate on JOINT velocity (video+action combined) or per-modality (separate for video and action)?\n4. DreamZero-Flash - what is it? Is it a 1-step variant? How does it work? Does it use a Beta distribution for video noise?\n5. Any details about the denoising process, noise schedules, and how video and action are handled together or separately.\nInclude exact quotes where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3bd2c2e-205c-48c6-8ce1-adf7f451c6ba",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNP6YeSjVZi84n57uAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77d312c6-1b83-4948-ba46-4cd2a6ade3c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DtC62m1zeNit8EbxCxjJWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 10891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2715,
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

_source line 15 · 2026-05-10T18:34:35.406Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JP1m79aRbrGSpBmhp1ewLG`</summary>

```json
{
  "url": "https://dreamzero0.github.io/",
  "prompt": "Extract ALL details about:\n1. Velocity caching / DiT caching - cosine similarity threshold, step reduction, fixed vs adaptive threshold\n2. DreamZero-Flash - what is it, how does it work, is it 1-step\n3. How video and action modalities are handled in denoising - joint or separate\n4. Any technical details about the inference acceleration or caching mechanism"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77d312c6-1b83-4948-ba46-4cd2a6ade3c3",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNP6YeSjVZi84n57uAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa601c3f-12e0-486c-8065-932579758423",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DtC62m1zeNit8EbxCxjJWq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 10891,
      "output_tokens": 468,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 468,
          "cache_read_input_tokens": 10891,
          "cache_creation_input_tokens": 2715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2715,
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

_source line 16 · 2026-05-10T18:34:40.186Z_

<details><summary>↩ Tool result · `toolu_01JP1m79aRbrGSpBmhp1ewLG`</summary>

```text
# DreamZero Technical Details - Limited Information

Based on the provided webpage content, I can offer only partial answers to your questions:

## 1. Velocity Caching / DiT Caching
**Not discussed.** The webpage contains no information about cosine similarity thresholds, step reduction strategies, or adaptive vs. fixed threshold mechanisms.

## 2. DreamZero-Flash
The document describes DreamZero-Flash as a variant achieving real-time performance. According to the content: "fewer steps reduce latency while DreamZero-Flash maintains performance even at single-step inference." The approach includes "model, system, and implementation optimizations" enabling "7Hz closed-loop control" with "150ms per action chunk." However, specific technical mechanisms aren't explained.

## 3. Video and Action Modality Handling
The webpage states the core concept: DreamZero involves "jointly predicting future world states and actions, using video as a dense representation." However, it doesn't clarify whether denoising occurs jointly or separately for these modalities.

## 4. Inference Acceleration Details
The document mentions "asynchronous inference and action chunk smoothing" as optimization techniques but provides no mechanistic details about how these work.

**Recommendation:** Consult the full paper (arxiv.org/abs/2602.15922) for comprehensive technical specifications on caching mechanisms, modality handling, and inference optimizations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa601c3f-12e0-486c-8065-932579758423",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "7b347d60-b0d6-4f95-92ed-d09fd3cbb369",
  "sourceToolAssistantUUID": "aa601c3f-12e0-486c-8065-932579758423",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T18:34:42.025Z_

<details><summary>↩ Tool result · `toolu_01HocZwciaPBUKhw4EWe3RVf`</summary>

```text
# DreamZero Velocity Caching and Optimization Details

## 1. DiT Caching Mechanism

**How it works:** The system exploits "directional consistency of velocity vectors learned during flow matching." During inference, the model tracks cosine similarity between successive velocity predictions. When this metric exceeds a predefined threshold, the model reuses cached velocity vectors instead of performing new forward passes.

**Step reduction:** The mechanism reduces "the average number of DiT steps from 16 to 4 with minimal degradation to predicted video and action fidelity."

**Threshold characteristics:** The document specifies a "predefined threshold (τ)" but does not disclose the exact numerical value or whether it's adaptive versus fixed. The optimization operates by "a window of a few steps" when the condition is met.

**Computation extension:** The paper doesn't address extending beyond cached steps; the focus is on reducing computational cost.

## 2. Joint vs. Per-Modality Caching

The caching operates on **joint velocity**: "the model tracks cosine similarity between successive velocity predictions." The velocity vector is defined as `[z_1^k, a_1^k] - [z_0^k, a_0^k]`—a combined representation of both video and action changes.

## 3. DreamZero-Flash Overview

**Definition:** A model-level optimization using decoupled noise schedules for video and action modalities during training to enable faster inference.

**How it works:** Rather than shared timesteps, Flash biases video toward high-noise states via a Beta distribution while keeping action noise uniform. This trains the model to "predict clean actions from noisy visual context," directly matching few-step inference regimes.

**Noise schedule:** Video timesteps follow `t_k^video = 1 - η, where η ~ Beta(7,1)`, yielding `E[t_k^video] = 0.125` (predominantly noisy). Action timesteps remain uniformly distributed `t_k^action ~ U(0,1)`.

**Speed achievement:** Reduces diffusion steps "from four to one, cutting inference from ~350ms to ~150ms."

## 4. Denoising Process

Standard DreamZero uses **coupled noise**: both modalities share timestep `t_k ~ U(0,1)`. The model denoises noisy latent vectors through flow matching, predicting velocity targets. Flash decoupling addresses a "train-test mismatch" where training assumes equal noise levels but inference uses fewer steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77d312c6-1b83-4948-ba46-4cd2a6ade3c3",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "36bfcb74-dddd-4ff8-b334-0cd3be357e06",
  "sourceToolAssistantUUID": "77d312c6-1b83-4948-ba46-4cd2a6ade3c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T18:34:51.911Z_

I have strong initial findings. Let me get more details by fetching the PDF and also searching for the specific threshold value and whether it's truly fixed-only.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36bfcb74-dddd-4ff8-b334-0cd3be357e06",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNQSPmp3x6abWJiSGTr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7e3f417-d079-4311-af13-3100158973b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7vgU8MqW6wfhLNxL1cxCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 346,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 13606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1066,
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

_source line 19 · 2026-05-10T18:35:02.838Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019Pboa8Cf61ifDE2cuFtdbH`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2602.15922",
  "prompt": "Find ALL details about:\n1. The DiT caching / velocity caching threshold tau - what is its exact numerical value? Is it fixed or adaptive? Can it be changed to extend computation (use more steps)?\n2. The exact formula for cosine similarity used in velocity caching\n3. How the joint velocity is computed - is it truly a concatenation of video and action velocities?\n4. DreamZero-Flash details - Beta(7,1) distribution, 1-step inference, noise schedule decoupling\n5. Any ablation results showing the 16 to 4 step reduction\n6. Any discussion of whether the threshold can be lowered to use MORE steps for harder cases\n\nExtract exact quotes and numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7e3f417-d079-4311-af13-3100158973b9",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNQSPmp3x6abWJiSGTr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20030b94-3f61-4e8e-9450-a086ff57bdd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7vgU8MqW6wfhLNxL1cxCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 346,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 13606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1066,
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

_source line 20 · 2026-05-10T18:35:03.129Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GvE3ZeYCkAHxD4dYfuon9o`</summary>

```json
{
  "query": "\"DreamZero\" \"DiT caching\" threshold tau cosine similarity velocity steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20030b94-3f61-4e8e-9450-a086ff57bdd1",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNQSPmp3x6abWJiSGTr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e508e332-d2c1-4df4-b816-4fe17c73bf15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7vgU8MqW6wfhLNxL1cxCC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 346,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 13606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1066,
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

### Tool result

_source line 21 · 2026-05-10T18:35:07.595Z_

<details><summary>↩ Tool result · `toolu_019Pboa8Cf61ifDE2cuFtdbH`</summary>

```text
# DiT Velocity Caching and DreamZero-Flash Details

Based on the PDF content provided, I cannot locate specific numerical values or detailed formulas for the following items:

1. **Caching Threshold τ (tau)**: No explicit numerical value for the velocity caching threshold is stated in the extracted text.

2. **Cosine Similarity Formula**: The exact mathematical formulation for the similarity metric used in velocity caching is not provided in the available content.

3. **Joint Velocity Computation**: There is no detailed explanation of how video and action velocities are combined in the extracted sections.

4. **DreamZero-Flash Distribution Details**: While the document title references "DreamZero," specific mentions of "Beta(7,1) distribution" or explicit "1-step inference" parameters do not appear in the extracted PDF content.

5. **Step Reduction Ablations**: I found no ablation studies explicitly showing "16 to 4 step reduction" in the provided text.

6. **Threshold Adaptability**: There is no discussion regarding lowering the threshold to enable additional computational steps for complex cases.

**Recommendation**: To obtain these specific technical details, you would need to access the full paper's methodology, ablation studies, and appendix sections, which may not be fully captured in the provided PDF excerpt. The complete arXiv paper (arxiv.org/abs/2602.15922v1) would contain these implementation specifics.

[Binary content (application/pdf, 8.7MB) also saved to /home/ubuntu/.claude-account-2/projects/-/0c2b0106-0381-4bbe-9b82-9ec3c390f9ce/tool-results/webfetch-1778438102913-a0gumf.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20030b94-3f61-4e8e-9450-a086ff57bdd1",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "1d74a89a-85c8-4322-a11f-c39ee8120c76",
  "sourceToolAssistantUUID": "20030b94-3f61-4e8e-9450-a086ff57bdd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T18:35:11.225Z_

<details><summary>↩ Tool result · `toolu_01GvE3ZeYCkAHxD4dYfuon9o`</summary>

```text
Web search results for query: ""DreamZero" "DiT caching" threshold tau cosine similarity velocity steps"

Links: [{"title":"GitHub - dreamzero0/dreamzero: Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals · GitHub","url":"https://github.com/dreamzero0/dreamzero"},{"title":"SpectralCache: Frequency-Aware Error-Bounded Caching for Accelerating Diffusion Transformers","url":"https://arxiv.org/html/2603.05315"},{"title":"SmoothCache: A Universal Inference Acceleration Technique for Diffusion Transformers","url":"https://arxiv.org/html/2411.10510v1"},{"title":"X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference","url":"https://arxiv.org/html/2604.20289v2"},{"title":"ProCache: Constraint-Aware Feature Caching with Selective Computation for Diffusion Transformer Acceleration","url":"https://arxiv.org/html/2512.17298"},{"title":"Cosine Similarity Threshold","url":"https://www.emergentmind.com/topics/cosine-similarity-threshold"},{"title":"Q&C: When Quantization Meets Cache in Efficient Image Generation","url":"https://arxiv.org/html/2503.02508"},{"title":"Diffusion Caching for Fast Inference","url":"https://www.emergentmind.com/topics/diffusion-caching"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"Zero Redundancy Optimizer - DeepSpeed","url":"https://www.deepspeed.ai/tutorials/zero/"}]

Based on the search results, I found information relevant to your query about DiT caching with cosine similarity thresholds and velocity steps. Here's what I found:

## DreamZero and DiT Caching

DreamZero is a World Action Model (WAM) built upon a pretrained video diffusion backbone that enables a 14B autoregressive video diffusion model to perform real-time closed-loop control at 7Hz through model and system optimizations. The GitHub repository shows DreamZero includes support for `--enable-dit-cache` in its inference implementation.

## DiT Caching Threshold (tau) and Cosine Similarity

Your search terms relate to several recent DiT caching optimization papers. SmoothCache leverages the observation that layer outputs from adjacent timesteps in any DiT-based model exhibit high cosine similarities, suggesting potential computational redundancies.

X-Cache introduces adaptive per-position thresholding to avoid hand-tuning a single global similarity threshold across all blocks and denoising steps, using a per-(denoising step, block) adaptive cosine threshold that auto-regulates from the block's own cross-chunk similarity history via an exponential moving average.

SpectralCache modulates caching thresholds using a cosine bell schedule aligned with the diffusion noise profile, enabling aggressive caching in tolerant middle timesteps while protecting sensitive endpoints.

## Velocity Steps

The search results contain information about denoising steps and timestep-aware caching strategies, but do not provide specific details about a "velocity steps" parameter in the context of DreamZero's DiT caching implementation.

For more specific technical details about DreamZero's particular implementation of these parameters, you may want to consult the DreamZero GitHub repository directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e508e332-d2c1-4df4-b816-4fe17c73bf15",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "11e48f38-bd19-4434-88cb-bf911b41332d",
  "sourceToolAssistantUUID": "e508e332-d2c1-4df4-b816-4fe17c73bf15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T18:35:13.815Z_

Let me fetch the GitHub repo and the full HTML paper for more specific details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11e48f38-bd19-4434-88cb-bf911b41332d",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNSbAgHYUiMczgKzdC7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53c2ef51-1e6f-40eb-81ba-49fc72872d55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EErLr4gjyTbLLGtL3ZirXK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1989,
      "cache_read_input_tokens": 14672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1989,
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

_source line 24 · 2026-05-10T18:35:17.705Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WNnwdL4asNxchYRRqmSUGP`</summary>

```json
{
  "url": "https://github.com/dreamzero0/dreamzero",
  "prompt": "Find ALL details about:\n1. DiT caching implementation - any code or flags related to --enable-dit-cache, cosine similarity threshold, velocity caching\n2. DreamZero-Flash - is it a 1-step variant? How is it configured?\n3. Any references to threshold tau, cosine similarity, velocity, step reduction\n4. Any configuration for adaptive vs fixed thresholds\n5. Noise schedule details - Beta distribution, decoupled noise"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53c2ef51-1e6f-40eb-81ba-49fc72872d55",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNSbAgHYUiMczgKzdC7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2a4d314-4f7b-4135-b124-4730d406e862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EErLr4gjyTbLLGtL3ZirXK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1989,
      "cache_read_input_tokens": 14672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1989,
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

_source line 25 · 2026-05-10T18:35:23.558Z_

<details><summary>↩ Tool result · `toolu_01WNnwdL4asNxchYRRqmSUGP`</summary>

```text
# DreamZero Technical Details Analysis

Based on the provided GitHub repository content, here's what I found:

## 1. DiT Caching Implementation
The documentation mentions **"--enable-dit-cache"** as a command-line flag for the inference server: "Enable caching in DiT layers for faster inference (recommended)." This optimization achieves approximately 0.6 seconds inference time on GB200 hardware. However, **no details about cosine similarity thresholds, velocity caching, or specific implementation code are provided** in this repository documentation.

## 2. DreamZero-Flash
There is **no mention of a DreamZero-Flash variant or 1-step model** anywhere in the provided content. The repository does not discuss step reduction techniques or single-step inference approaches.

## 3. Advanced Technical Parameters
The documentation does **not contain any references to**:
- Threshold tau values
- Cosine similarity metrics
- Velocity-based caching
- Step reduction mechanisms

## 4. Adaptive vs. Fixed Thresholds
**No configuration information is available** regarding adaptive versus fixed threshold approaches in the provided material.

## 5. Noise Schedule Details
The content provides **no details about beta distributions, decoupled noise schedules, or noise-related configurations**.

## Conclusion
This repository focuses on inference deployment, training pipelines, and dataset handling. The technical implementation details you're seeking appear to be in the referenced papers or internal implementation files not exposed in this README documentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2a4d314-4f7b-4135-b124-4730d406e862",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "1a119280-d731-4f4f-98d7-e69e940be942",
  "sourceToolAssistantUUID": "c2a4d314-4f7b-4135-b124-4730d406e862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T18:35:25.064Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016QLR3RULB7KnNow82quEW5`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.15922",
  "prompt": "I need to find VERY SPECIFIC details about:\n1. The exact threshold value tau used in velocity caching. Search for any number like 0.95, 0.99, 0.98 etc.\n2. Is the threshold FIXED only, or can it be adapted? Is there any mention of extending computation by lowering the threshold?\n3. The exact formula showing how the joint velocity vector is constructed from video latents and actions\n4. DreamZero-Flash: exact Beta distribution parameters, whether it truly does 1-step inference\n5. Any ablation table showing step reduction from 16 to 4\n\nLook especially in the Methods section, the System Optimization section, and the Appendix. Extract EXACT quotes with section numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a119280-d731-4f4f-98d7-e69e940be942",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNSbAgHYUiMczgKzdC7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5e9b1f1-57d6-434e-8f5b-6064631638e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EErLr4gjyTbLLGtL3ZirXK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1989,
      "cache_read_input_tokens": 14672,
      "output_tokens": 431,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1989
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 431,
          "cache_read_input_tokens": 14672,
          "cache_creation_input_tokens": 1989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1989,
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

_source line 27 · 2026-05-10T18:35:34.290Z_

<details><summary>↩ Tool result · `toolu_016QLR3RULB7KnNow82quEW5`</summary>

```text
# DreamZero Technical Details Analysis

## 1. Velocity Caching Threshold (τ)

**Finding:** The exact threshold value is **not specified** in the document.

The paper states in Section 3.2.3: "When cosine similarity between successive velocities exceeds a threshold, we reuse cached velocities, reducing effective DiT steps from 16 to 4 with minimal quality loss on action prediction."

However, in Appendix D.1, the implementation notes: "When this metric exceeds a predefined threshold (τ), the model bypasses the DiT forward pass for a window of a few steps by reusing the cached velocity vector."

**No numerical value for τ is provided anywhere in the document.**

## 2. Threshold Adaptation

**Finding:** The threshold is described as "predefined" but **no mention of adaptive adjustment or dynamic lowering** exists in the paper. It appears to be a fixed hyperparameter without discussion of flexibility.

## 3. Joint Velocity Vector Formula

**Exact quote from Equation 3 (Section 3.1):**

"the velocity 𝐯^k ≔ [𝐳₁^k, 𝐚₁^k] − [𝐳₀^k, 𝐚₀^k]"

The joint velocity concatenates clean video latent (𝐳₁^k) and clean action (𝐚₁^k), minus their noise counterparts.

## 4. DreamZero-Flash Parameters

**Beta distribution (Section 3.2.5):** "we use Beta(7,1) as an example configuration, yielding 𝔼[t_k^video] = 0.125"

**Single-step capability:** Table 3 shows DreamZero-Flash achieves "74% ±± 10.1%" task progress at **1 denoising step**, confirming true single-step inference is operational.

## 5. Step Reduction Ablation

**Table 1** (Section 3.2.6) provides cumulative speedups but no explicit ablation table comparing step counts. The progression shows DiT caching achieves "5.5×× speedup" on H100, implying reduction from 16 to approximately 4 steps, though this is stated qualitatively rather than tabled quantitatively.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5e9b1f1-57d6-434e-8f5b-6064631638e8",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "b1455473-aa6c-4b0d-8fe2-b40dfce424e2",
  "sourceToolAssistantUUID": "f5e9b1f1-57d6-434e-8f5b-6064631638e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T18:35:37.624Z_

Excellent. Now let me fetch one more source for additional detail on DreamZero-Flash and whether the caching truly cannot extend computation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1455473-aa6c-4b0d-8fe2-b40dfce424e2",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNUJMwd24BgyRj1K8Fa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da01f43b-34d1-4bb7-b10a-ad884ecafd27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyCCjnVzP1QhAetBMTxGDU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1369,
      "cache_read_input_tokens": 16661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1369,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-10T18:35:40.528Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XpBtvbP5qxbw8QLXhgK1Uv`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/world-action-models-are-zero-shot-policies",
  "prompt": "Find details about:\n1. DiT caching - is it fixed threshold only? Can it extend computation?\n2. DreamZero-Flash - 1-step variant details\n3. Joint vs per-modality velocity caching\n4. Any criticism or limitations of the caching approach"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da01f43b-34d1-4bb7-b10a-ad884ecafd27",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNUJMwd24BgyRj1K8Fa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fb67d78-13c0-4e12-9b4a-11f4397871ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyCCjnVzP1QhAetBMTxGDU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1369,
      "cache_read_input_tokens": 16661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1369,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-10T18:35:42.584Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018jqQ1nVaMGCM7D7Kqb7nrk`</summary>

```json
{
  "url": "https://www.emergentmind.com/papers/2602.15922",
  "prompt": "Find ALL technical details about:\n1. DiT caching mechanism - threshold, fixed vs adaptive, velocity-based convergence\n2. DreamZero-Flash - 1-step inference, Beta distribution\n3. Step reduction 16 to 4\n4. Joint velocity vector definition\n5. Any limitations or criticisms of the caching approach"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fb67d78-13c0-4e12-9b4a-11f4397871ee",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNUJMwd24BgyRj1K8Fa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36d3d4b6-e86a-4863-bc98-964deae36473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyCCjnVzP1QhAetBMTxGDU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1369,
      "cache_read_input_tokens": 16661,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1369
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 16661,
          "cache_creation_input_tokens": 1369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1369,
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

_source line 31 · 2026-05-10T18:35:48.070Z_

<details><summary>↩ Tool result · `toolu_01XpBtvbP5qxbw8QLXhgK1Uv`</summary>

```text
# DiT Caching and DreamZero-Flash Details

## DiT Caching Mechanism

The caching approach uses a **fixed similarity threshold** rather than adaptive computation:

"Reuses cached velocity predictions when the cosine similarity between successive velocities exceeds a threshold, reducing effective DiT steps from 16 to 4 with minimal quality loss."

This is a straightforward optimization—when consecutive velocity predictions are sufficiently similar, the system skips recomputation. The document doesn't indicate dynamic extension of computation based on complexity.

## DreamZero-Flash Details

The 1-step variant works through decoupled noise scheduling:

"DreamZero-Flash biases video timesteps towards high-noise states via $t_{video_k} = 1 - \eta$... while action timesteps remain uniform. This trains the model to predict clean actions from noisy visual context, aligning with few-step or single-step inference regimes."

Performance: "DreamZero-Flash with 1 denoising step achieves 74% task progress on table bussing" versus 83% for the 4-step baseline, yielding a 2.33× speedup.

## Joint vs. Per-Modality Caching

The document discusses a **unified velocity cache** approach rather than separate per-modality systems. Both video and action denoising share the same cached velocity predictions during inference.

## Limitations

The review notably **lacks explicit criticism** of the caching strategy. The only implied limitation is the 9% performance gap between Flash (1-step) and standard DreamZero (4-step), suggesting speed-accuracy tradeoffs remain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fb67d78-13c0-4e12-9b4a-11f4397871ee",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "20bd3573-0401-435e-8e65-b33f3c368f5a",
  "sourceToolAssistantUUID": "8fb67d78-13c0-4e12-9b4a-11f4397871ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T18:35:49.936Z_

<details><summary>↩ Tool result · `toolu_018jqQ1nVaMGCM7D7Kqb7nrk`</summary>

```text
# Technical Details on DiT Caching and DreamZero-Flash

Based on the provided content, here's what I found:

## DiT Caching Mechanism

The document mentions **"DiT Caching: Cached velocity predictions replace redundant forward passes for low-variance trajectory updates."** However, the specific technical details you requested—threshold values, fixed vs. adaptive strategies, and velocity-based convergence criteria—are **not included** in this web page content.

## DreamZero-Flash Training

The paper describes the approach as teaching the model to make clean action decisions even when visual input remains somewhat noisy. Specifically: **"the model biases video latents toward higher noise states during training while maintaining uniform action noise, exposing the model to infer actions from noisy visual context."**

The document notes this uses a Beta distribution but does not provide the specific mathematical formulation or distribution parameters.

## Step Reduction (16 to 4)

**This specific detail is not mentioned** in the provided content.

## Joint Velocity Vector Definition

**Not included** in the available text.

## Limitations or Criticisms

The content does not offer critical analysis of the caching approach's limitations. It presents the optimization as enabling **"smooth closed-loop control at 7Hz—without performance degradation,"** but does not discuss potential drawbacks or edge cases.

**Recommendation:** For these technical specifics, you'd need to access the full paper PDF (arxiv.org/pdf/2602.15922).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36d3d4b6-e86a-4863-bc98-964deae36473",
  "isSidechain": true,
  "promptId": "3fd0ddd3-18ac-453f-a240-34c6589c33da",
  "agentId": "a4a78718ce6bd7e9e",
  "type": "user",
  "uuid": "ac681cf2-b54c-4f1c-b610-bd0dc4d4dd3a",
  "sourceToolAssistantUUID": "36d3d4b6-e86a-4863-bc98-964deae36473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T18:36:22.248Z_

I now have comprehensive evidence to address all five claims. Here is my report:

---

## Verification Results for DreamZero (arXiv 2602.15922)

### Claim 1: Velocity-based convergence caching with cosine similarity threshold on successive predictions

**VERIFIED.** DreamZero implements exactly this. Per Section 3.2.3 of the paper: "When cosine similarity between successive velocities exceeds a threshold, we reuse cached velocities." The mechanism tracks directional consistency of velocity vectors learned during flow matching. When the cosine similarity metric exceeds a predefined threshold (tau), the model bypasses the DiT forward pass for a window of a few steps by reusing the cached velocity vector. The exact numerical value of tau is **not disclosed** in the paper.

### Claim 2: 16 to 4 effective steps (75% reduction)

**VERIFIED.** The paper explicitly states the mechanism reduces "the average number of DiT steps from 16 to 4 with minimal degradation to predicted video and action fidelity." This corresponds to a 75% reduction and contributes to a ~5.5x speedup on H100 hardware.

### Claim 3: Fixed-threshold only (cannot extend computation)

**MOSTLY VERIFIED, with nuance.** The threshold is described as "predefined" (i.e., a fixed hyperparameter). There is no discussion anywhere in the paper of adaptive adjustment, dynamic lowering, or extending computation for harder cases. The mechanism is purely a cost-reduction technique -- it can only skip steps when similarity is high, and the paper does not present any mechanism to allocate *more* than 16 steps when predictions diverge. So the claim that it "cannot extend computation" is accurate in the sense that the caching can only *reduce* steps (from 16 down toward 4 on average), never increase them beyond the baseline 16. However, note that the threshold is configurable as a hyperparameter -- it is "fixed" during inference but could presumably be tuned to be more or less aggressive.

### Claim 4: Joint velocity (video+action combined) or per-modality?

**JOINT velocity -- VERIFIED.** The velocity vector is explicitly defined in Equation 3 (Section 3.1) as:

**v^k := [z_1^k, a_1^k] - [z_0^k, a_0^k]**

This is a concatenation of clean video latent (z_1^k) and clean action (a_1^k) minus their noisy counterparts. The cosine similarity is computed on this **joint** vector, not per-modality. Multiple sources confirm it is a "unified velocity cache" operating on the combined video+action representation.

### Claim 5: DreamZero-Flash exists (1-step variant)

**VERIFIED.** DreamZero-Flash is a model-level optimization using decoupled noise schedules:
- Video timesteps are biased toward high noise via **t_video = 1 - eta, where eta ~ Beta(7,1)**, yielding E[t_video] = 0.125 (predominantly noisy)
- Action timesteps remain uniformly distributed: **t_action ~ U(0,1)**
- This trains the model to predict clean actions from noisy visual context, matching few-step or single-step inference regimes
- **Performance at 1 denoising step**: 74% +/- 10.1% task progress on table bussing (vs. 83% for 4-step baseline)
- Reduces inference from ~350ms to ~150ms per action chunk (2.33x speedup)
- DreamZero-Flash is confirmed as a true **1-step** variant

---

### Summary Table

| Claim | Verdict |
|-------|---------|
| Velocity-based convergence caching with cosine similarity | **Confirmed** |
| 16 to 4 effective steps (75% reduction) | **Confirmed** |
| Fixed-threshold only / cannot extend computation | **Confirmed** -- threshold is predefined; mechanism only reduces steps, never extends beyond baseline 16 |
| Operates on JOINT velocity (video+action) | **Confirmed** -- per Equation 3 |
| DreamZero-Flash (1-step variant) exists | **Confirmed** -- uses Beta(7,1) noise decoupling, achieves 74% task progress at 1 step |

One notable gap: the exact numerical value of tau is not disclosed in the paper.

Sources:
- [arXiv 2602.15922 HTML](https://arxiv.org/html/2602.15922v1)
- [arXiv 2602.15922 Abstract](https://arxiv.org/abs/2602.15922)
- [DreamZero Project Page](https://dreamzero0.github.io/)
- [DreamZero GitHub](https://github.com/dreamzero0/dreamzero)
- [Moonlight Review](https://www.themoonlight.io/en/review/world-action-models-are-zero-shot-policies)
- [EmergentMind Summary](https://www.emergentmind.com/papers/2602.15922)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac681cf2-b54c-4f1c-b610-bd0dc4d4dd3a",
  "isSidechain": true,
  "agentId": "a4a78718ce6bd7e9e",
  "requestId": "req_011CauNVVYfsaspVjH3rNUid",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7eca705-2e5b-4afd-8337-c5ffb045e49b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c2b0106-0381-4bbe-9b82-9ec3c390f9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtHdTnHisBmmFHRgYiwhrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 18030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1099,
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
