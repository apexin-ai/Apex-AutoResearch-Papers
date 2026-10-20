# Research conversation: The novelty search found that LTX-2 (a dual-stream audio-video diffusion transformer) has "post-attention AdaLN gate who

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a077ce1cbc27af79e.jsonl`
- **Structured JSON:** [`a654de400286a22ccbcc.json`](../../sessions/a6/a654de400286a22ccbcc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-10T19:28:36.966Z_

The novelty search found that LTX-2 (a dual-stream audio-video diffusion transformer) has "post-attention AdaLN gate whose parameters depend on the OTHER modality's timestep." This is potentially very close to DualGate's proposed approach.

Search for "LTX-2 dual stream audio video diffusion transformer" or "LTX-Video 2" and use WebFetch to read the paper's architecture section. I need to understand:

1. Is the gating truly conditioned on the other modality's timestep?
2. Is it per-head or per-layer?
3. Does it apply to attention weights or to post-attention features?
4. How does it differ from standard AdaLN-Zero gating?

This is critical for assessing whether DualGate's novelty claim holds. Report with specific architectural details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "e9ad3f8b-5ec1-49fc-9390-a24e99c3b1b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:28:36.967Z_

```json
{
  "parentUuid": "e9ad3f8b-5ec1-49fc-9390-a24e99c3b1b1",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
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
  "uuid": "a2cc9e50-2411-45a5-af7d-654993dced3a",
  "timestamp": "2026-05-10T19:28:36.967Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:28:40.478Z_



I'll search for the LTX-2 paper to understand its architecture details. Let me start by loading the WebSearch and WebFetch tools, then searching for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2cc9e50-2411-45a5-af7d-654993dced3a",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSWu71E8V9aZzdJdCFT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19a8426f-128c-4f66-87e1-fa9d4207a35c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJwo4JxYKiPbDZJKgCj47u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 743,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 743,
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

_source line 4 · 2026-05-10T19:28:40.593Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HkCoAakTpvpRkfEvWmpr7q`</summary>

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
  "parentUuid": "19a8426f-128c-4f66-87e1-fa9d4207a35c",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSWu71E8V9aZzdJdCFT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3577f2c8-242c-40e2-b62f-a5f6a34a0b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJwo4JxYKiPbDZJKgCj47u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 743,
      "cache_read_input_tokens": 8223,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 743
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 743,
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

_source line 5 · 2026-05-10T19:28:40.598Z_

<details><summary>↩ Tool result · `toolu_01HkCoAakTpvpRkfEvWmpr7q`</summary>

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
  "parentUuid": "3577f2c8-242c-40e2-b62f-a5f6a34a0b13",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "d8f0f9ee-b83a-4423-ae84-33c23d0c03c3",
  "sourceToolAssistantUUID": "3577f2c8-242c-40e2-b62f-a5f6a34a0b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:28:45.041Z_



Now let me search for the LTX-2 paper from multiple angles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8f0f9ee-b83a-4423-ae84-33c23d0c03c3",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSXArJX5nohyZiyMoss",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b25de11a-6f88-4df1-b5ee-f6133d2a1d3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9qWWwh7gGDKA1PcnV8A3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1928,
      "cache_read_input_tokens": 8966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1928,
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

_source line 7 · 2026-05-10T19:28:46.003Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VudWaiKE8axGVHi6afAdJN`</summary>

```json
{
  "query": "LTX-Video 2 dual stream audio video diffusion transformer paper 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b25de11a-6f88-4df1-b5ee-f6133d2a1d3c",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSXArJX5nohyZiyMoss",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fff532b9-c2fd-47e2-ab25-95d731f3904c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9qWWwh7gGDKA1PcnV8A3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1928,
      "cache_read_input_tokens": 8966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1928,
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

_source line 8 · 2026-05-10T19:28:46.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01McFNsGLE5pU1akPrdycwzi`</summary>

```json
{
  "query": "LTX-2 dual stream diffusion transformer AdaLN cross-modal timestep gating architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff532b9-c2fd-47e2-ab25-95d731f3904c",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSXArJX5nohyZiyMoss",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "195e1c02-b2b2-4bce-8893-98705201aa33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9qWWwh7gGDKA1PcnV8A3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1928,
      "cache_read_input_tokens": 8966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1928,
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

_source line 9 · 2026-05-10T19:28:47.524Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L6sgmAFUyxfiorvT5d2gNy`</summary>

```json
{
  "query": "\"LTX-Video\" audio video joint generation diffusion transformer arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "195e1c02-b2b2-4bce-8893-98705201aa33",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSXArJX5nohyZiyMoss",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d33ec17-f7d5-465e-a76b-bc679f7ccf79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9qWWwh7gGDKA1PcnV8A3F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1928,
      "cache_read_input_tokens": 8966,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1928
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 8966,
          "cache_creation_input_tokens": 1928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1928,
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

_source line 10 · 2026-05-10T19:28:53.433Z_

<details><summary>↩ Tool result · `toolu_01VudWaiKE8axGVHi6afAdJN`</summary>

```text
Web search results for query: "LTX-Video 2 dual stream audio video diffusion transformer paper 2025"

Links: [{"title":"Paper page - LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://huggingface.co/papers/2601.03233"},{"title":"LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://arxiv.org/html/2601.03233v1"},{"title":"[2601.03233] LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://arxiv.org/abs/2601.03233"},{"title":"LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://videos.ltx.io/LTX-2/grants/LTX_2_Technical_Report_compressed.pdf"},{"title":"LTX-2 Brings Open-Source Audio-Visual Generation that Finally Catches Up to Sora and VEO | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/ltx-2-video-generation-audio-video-model"},{"title":"LTX-2: Efficient Joint Audio-Visual Foundation Model | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2601.03233"},{"title":"(PDF) LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://www.researchgate.net/publication/399522516_LTX-2_Efficient_Joint_Audio-Visual_Foundation_Model"},{"title":"LTX-2: Efficient Joint Audio-Visual Foundation Model | Papers | HyperAI","url":"https://vercel.hyper.ai/en/papers/2601.03233"},{"title":"[2601.03233v1] LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://arxiv.org/abs/2601.03233v1"},{"title":"LTX-2: Open-Source Video Generation Finally Gets Sound Right | by Jingshan Li | Medium","url":"https://medium.com/@ljingshan6/ltx-2-open-source-video-generation-finally-gets-sound-right-64d23dfc2ff8"}]

## Search Results for LTX-Video 2 Paper

I found comprehensive information about the LTX-2 paper. Here's what the search revealed:

### Overview

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance. The paper was published in January 2025 (arXiv 2601.03233).

### Architecture

LTX-2 consists of an asymmetric dual-stream transformer with a 14B-parameter video stream and a 5B-parameter audio stream, coupled through bidirectional audio-video cross-attention layers with temporal positional embeddings and cross-modality AdaLN for shared timestep conditioning.

### Key Contributions

The paper presents four main contributions:

1. Efficient Asymmetric Dual-Stream Architecture: the transformer-based backbone featuring modality-specific streams linked via bidirectional cross-attention and cross-modality AdaLN for shared timestep conditioning.

2. Text Processing Blocks with Thinking Tokens: they developed a novel text-conditioning module that uses multi-token prediction to enhance prompt understanding and semantic stability.

3. Compact Neural Audio Representation: an efficient causal audio Variational AutoEncoder (VAE) that produces a high-fidelity, 1D latent space optimized for diffusion-based training and inference.

4. Modality-Aware Classifier-Free Guidance: A novel Bimodal CFG scheme that allows for independent control over cross-modal guidance scales, significantly improving audiovisual alignment.

### Performance

The model achieves state-of-the-art audiovisual quality and prompt adherence among open-source systems, while delivering results comparable to proprietary models at a fraction of their computational cost and inference time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fff532b9-c2fd-47e2-ab25-95d731f3904c",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "cfbff776-abb6-4c1b-b111-ecf1ef63f8b7",
  "sourceToolAssistantUUID": "fff532b9-c2fd-47e2-ab25-95d731f3904c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T19:28:53.758Z_

<details><summary>↩ Tool result · `toolu_01L6sgmAFUyxfiorvT5d2gNy`</summary>

```text
Web search results for query: ""LTX-Video" audio video joint generation diffusion transformer arxiv"

Links: [{"title":"[2601.03233] LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://arxiv.org/abs/2601.03233"},{"title":"LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://arxiv.org/html/2601.03233v1"},{"title":"Paper page - LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://huggingface.co/papers/2601.03233"},{"title":"LTX-2: The First Open-Source Model That Generates | Introl Blog","url":"https://introl.com/blog/ltx-2-audiovisual-diffusion-synchronized-video-audio-2026"},{"title":"[2501.00103] LTX-Video: Realtime Video Latent Diffusion","url":"https://arxiv.org/abs/2501.00103"},{"title":"[2601.03233v1] LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://arxiv.org/abs/2601.03233v1"},{"title":"LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://videos.ltx.io/LTX-2/grants/LTX_2_Technical_Report_compressed.pdf"},{"title":"LTX-2: Efficient Joint Audio-Visual Foundation Model | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2601.03233"},{"title":"LTX-Video: Realtime Video Latent Diffusion","url":"https://arxiv.org/html/2501.00103v1"},{"title":"(PDF) LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://www.researchgate.net/publication/399522516_LTX-2_Efficient_Joint_Audio-Visual_Foundation_Model"}]

I found information about LTX-Video and related models. Here's what I discovered:

## LTX-Video and LTX-2

LTX-Video is a transformer-based latent diffusion model that adopts a holistic approach to video generation by seamlessly integrating the responsibilities of the Video-VAE and the denoising transformer. It achieves faster-than-real-time generation, producing 5 seconds of 24 fps video at 768x512 resolution in just 2 seconds on an Nvidia H100 GPU.

The more recent model in this series is **LTX-2**, which extends the technology to audio-visual generation. LTX-2 is an open-source foundational model capable of generating high-quality, temporally synchronized audiovisual content in a unified manner. 

### Architecture

LTX-2 consists of an asymmetric dual-stream transformer with a 14B-parameter video stream and a 5B-parameter audio stream, coupled through bidirectional audio-video cross-attention layers with temporal positional embeddings and cross-modality AdaLN for shared timestep conditioning.

### Key Features

LTX-2 employs a multilingual text encoder for broader prompt understanding and introduces a modality-aware classifier-free guidance (modality-CFG) mechanism for improved audiovisual alignment and controllability. Beyond generating speech, LTX-2 produces rich, coherent audio tracks that follow the characters, environment, style, and emotion of each scene -- complete with natural background and foley elements.

The model achieves state-of-the-art audiovisual quality and prompt adherence among open-source systems, while delivering results comparable to proprietary models at a fraction of their computational cost and inference time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d33ec17-f7d5-465e-a76b-bc679f7ccf79",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "a35cf997-b6d0-4749-b8c7-52421ee2bf33",
  "sourceToolAssistantUUID": "7d33ec17-f7d5-465e-a76b-bc679f7ccf79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:28:53.903Z_

<details><summary>↩ Tool result · `toolu_01McFNsGLE5pU1akPrdycwzi`</summary>

```text
Web search results for query: "LTX-2 dual stream diffusion transformer AdaLN cross-modal timestep gating architecture"

Links: [{"title":"Paper page - LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://huggingface.co/papers/2601.03233"},{"title":"LTX-2/packages/ltx-core/README.md at main · Lightricks/LTX-2","url":"https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-core/README.md"},{"title":"[2601.03233] LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://arxiv.org/abs/2601.03233"},{"title":"LTX-2: Efficient Audio-Visual Diffusion Model","url":"https://www.emergentmind.com/papers/2601.03233"},{"title":"LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://videos.ltx.io/LTX-2/grants/LTX_2_Technical_Report_compressed.pdf"},{"title":"LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://arxiv.org/html/2601.03233v1"},{"title":"LTX-2 Brings Open-Source Audio-Visual Generation that Finally Catches Up to Sora and VEO | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/ltx-2-video-generation-audio-video-model"},{"title":"LTX-2/packages/ltx-core at main · Lightricks/LTX-2","url":"https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-core"},{"title":"LTX-2: The First Open-Source Model That Generates | Introl Blog","url":"https://introl.com/blog/ltx-2-audiovisual-diffusion-synchronized-video-audio-2026"},{"title":"(PDF) LTX-2: Efficient Joint Audio-Visual Foundation Model","url":"https://www.researchgate.net/publication/399522516_LTX-2_Efficient_Joint_Audio-Visual_Foundation_Model"}]

Based on the search results, here's what I found about LTX-2's architecture:

## LTX-2: Dual Stream Diffusion Transformer Architecture

LTX-2 consists of an asymmetric dual-stream transformer with a 14B-parameter video stream and a 5B-parameter audio stream, coupled through bidirectional audio-video cross-attention layers with temporal positional embeddings and cross-modality AdaLN for shared timestep conditioning.

### Cross-Modality AdaLN and Timestep Gating

The model employs cross-modality AdaLN gates, where the scaling and shift parameters for one modality are conditioned on the hidden states of the other. This allows the model to better synchronize audio and video features, particularly when their diffusion timesteps or temporal resolutions differ.

More specifically, an AdaLN modulation conditioned on the stream's diffusion timestep scales and shifts the Q and the (K,V) tensors independently, allowing each modality to control how much of its current representation is receptive or exposed to the other. The resulting attended representation is passed through an additional AdaLN gate, whose parameters depend on the other modality's timestep, effectively regulating how much cross-modal information is integrated at that stage of denoising.

### Positional Embeddings

In the video stream, a 3D RoPE injects positional information along spatial and temporal axes (x,y,t), preserving both motion and layout. In the audio stream, a 1D RoPE is applied along the temporal dimension only. During audio-visual interaction, only the temporal component of RoPE is used for queries and keys, enforcing that cross-modal attention focuses on synchronization in time rather than spatial alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "195e1c02-b2b2-4bce-8893-98705201aa33",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "eb2c38a6-5bea-46fb-81c6-fa76c24db624",
  "sourceToolAssistantUUID": "195e1c02-b2b2-4bce-8893-98705201aa33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T19:28:57.284Z_

Excellent. I found the paper (arXiv 2601.03233). The search results already reveal key details about cross-modality AdaLN gating. Now let me fetch the actual paper for precise architectural details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb2c38a6-5bea-46fb-81c6-fa76c24db624",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSY9VUBabi2u4XinCnJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a01213dd-e972-40f4-b07e-a908daf6e1f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6BC6RYyfwDmMxVczyGcmd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 931,
      "cache_creation_input_tokens": 2197,
      "cache_read_input_tokens": 10894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2197,
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

_source line 14 · 2026-05-10T19:29:02.116Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WVq2Mt3nbQEwbbjJ6gRSjj`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.03233v1",
  "prompt": "Extract ALL architectural details about:\n1. The cross-modality AdaLN gating mechanism - exactly how it works, what parameters are conditioned on what\n2. Whether gating is per-head or per-layer\n3. Whether it applies to attention weights or post-attention features\n4. How it differs from standard AdaLN-Zero\n5. The \"post-attention AdaLN gate whose parameters depend on the OTHER modality's timestep\" - find the exact description\n6. Any equations or formulas describing the gating mechanism\n7. The dual-stream transformer block structure in detail\n8. How diffusion timesteps are used in conditioning\n\nBe extremely detailed and include any mathematical notation, equations, or specific parameter descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a01213dd-e972-40f4-b07e-a908daf6e1f0",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSY9VUBabi2u4XinCnJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dd0b39e-aa2a-4322-9e49-a61937ea6218",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6BC6RYyfwDmMxVczyGcmd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 931,
      "cache_creation_input_tokens": 2197,
      "cache_read_input_tokens": 10894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2197,
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

_source line 15 · 2026-05-10T19:29:03.336Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0111cdyAB5pCsLt4inYv2tgC`</summary>

```json
{
  "url": "https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-core/README.md",
  "prompt": "Extract all architectural details about the cross-modality AdaLN gating mechanism, dual-stream transformer blocks, how timestep conditioning works across modalities, and any code references or implementation details about the gating."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dd0b39e-aa2a-4322-9e49-a61937ea6218",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSY9VUBabi2u4XinCnJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92272a43-3e04-419f-8d80-4500ccd44329",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6BC6RYyfwDmMxVczyGcmd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 931,
      "cache_creation_input_tokens": 2197,
      "cache_read_input_tokens": 10894,
      "output_tokens": 418,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2197
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 931,
          "output_tokens": 418,
          "cache_read_input_tokens": 10894,
          "cache_creation_input_tokens": 2197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2197,
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

_source line 16 · 2026-05-10T19:29:08.033Z_

<details><summary>↩ Tool result · `toolu_01WVq2Mt3nbQEwbbjJ6gRSjj`</summary>

```text
# LTX-2 Cross-Modality AdaLN Architecture Details

## Core Gating Mechanism

The cross-modality AdaLN operates in the audio-visual cross-attention module. According to the paper: "An AdaLN modulation conditioned on the stream's diffusion timestep scales and shifts the Q and the (K,V) tensors independently, allowing each modality to control how much of its current representation is receptive or exposed to the other."

## Pre-Attention Gating

Initial AdaLN scaling occurs before attention computation:
- Query, key, and value tensors receive separate AdaLN modulation
- Each stream's timestep conditions its own Q and complementary stream's (K,V)
- This enables asymmetric information flow during attention

## Post-Attention Gating (Cross-Modal Dependent)

After cross-attention computation: "The resulting attended representation is passed through an additional AdaLN gate, whose parameters depend on the other modality's timestep, effectively regulating how much cross-modal information is integrated at that stage of denoising."

This represents the key innovation—post-attention gates are **conditioned on the opposite stream's diffusion timestep**, not the current stream's timestep.

## Architectural Context

The dual-stream block executes sequentially:
1. Self-Attention (within modality)
2. Text Cross-Attention
3. Audio-Visual Cross-Attention (with bidirectional gating)
4. Feed-Forward Network

Both 14B video and 5B audio streams process through identical architectural blocks, with RMS normalization interleaved between operations.

## Key Distinction from Standard AdaLN-Zero

No equations explicitly differentiate this from standard AdaLN-Zero, but the cross-modal timestep conditioning represents a departure from typical approaches where scaling depends only on the current stream's denoising progress.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dd0b39e-aa2a-4322-9e49-a61937ea6218",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "5627ec91-a369-45b7-a37a-e149650bd041",
  "sourceToolAssistantUUID": "9dd0b39e-aa2a-4322-9e49-a61937ea6218",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T19:29:10.265Z_

<details><summary>↩ Tool result · `toolu_0111cdyAB5pCsLt4inYv2tgC`</summary>

```text
# Cross-Modality AdaLN and Dual-Stream Transformer Architecture

## Cross-Modality AdaLN Gating

The documentation describes that "Scaling/shift parameters conditioned on the other modality's hidden states" enable synchronization across differing diffusion timesteps and temporal resolutions. This mechanism allows each stream's normalization to be influenced by the complementary modality's representations.

## Dual-Stream Block Structure

Each transformer block implements four sequential operations:

1. **Self-Attention**: Within-modality attention per stream
2. **Text Cross-Attention**: Prompt conditioning for both streams
3. **Audio-Visual Cross-Attention**: Bidirectional inter-modal exchange using "1D temporal RoPE (synchronization only, no spatial alignment)"
4. **Feed-Forward Network**: Feature refinement

The architecture allocates "14B-parameter video stream (spatiotemporal dynamics) + 5B-parameter audio stream (1D temporal)" across 48 shared transformer blocks with stream-specific widths.

## Timestep Conditioning Mechanism

Timestep conditioning operates through AdaLN in cross-attention layers. The design enables "sub-frame alignment, mapping visual cues to auditory events (lip-sync, foley, environmental acoustics)" by conditioning normalization parameters on timesteps while maintaining 1D temporal RoPE synchronization.

## Implementation References

- **Transformer Block**: `src/ltx_core/model/transformer/transformer.py`
- **Main Model**: `src/ltx_core/model/transformer/model.py`
- **Perturbations** (selective attention skipping): `src/ltx_core/guidance/perturbations.py`

The system uses separate text embeddings for each modality, producing "Video context: [B, seq_len, 4096]" and "Audio context: [B, seq_len, 2048]" to enable modality-specific conditioning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92272a43-3e04-419f-8d80-4500ccd44329",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "a2f1303c-6727-4a0e-9f9b-9332d206685a",
  "sourceToolAssistantUUID": "92272a43-3e04-419f-8d80-4500ccd44329",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T19:29:14.774Z_

Good, I have substantial detail. Let me now look at the actual source code to get the precise implementation, and also fetch the technical report PDF and the Emergent Mind summary for any additional architectural equations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2f1303c-6727-4a0e-9f9b-9332d206685a",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSZMV4kQSt1BjmtT3E7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6061b58f-55bf-4634-abdc-ffebd52becab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNdShNAPRdcsNDj9uZiiGa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2277,
      "cache_read_input_tokens": 13091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2277,
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

_source line 19 · 2026-05-10T19:29:19.700Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KNGHgatoFSFp6LCm1rpT2t`</summary>

```json
{
  "url": "https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-core/src/ltx_core/model/transformer/transformer.py",
  "prompt": "Extract the COMPLETE implementation of the cross-modality AdaLN gating mechanism. I need to understand:\n1. How the AdaLN gate parameters are computed - what inputs condition them\n2. Whether the gate is per-head or per-layer (look at tensor dimensions)\n3. Whether it gates attention weights or post-attention output features\n4. The exact code for how the other modality's timestep is used\n5. Any scale/shift/gate parameters and their shapes\n6. How this differs from standard AdaLN-Zero (look for gate_msa, gate_mlp patterns)\n7. The full transformer block forward pass showing where gating happens\n\nInclude all relevant code snippets and class definitions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6061b58f-55bf-4634-abdc-ffebd52becab",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSZMV4kQSt1BjmtT3E7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7d0e96c-ed0b-4d79-a20a-f733ab6f7973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNdShNAPRdcsNDj9uZiiGa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2277,
      "cache_read_input_tokens": 13091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2277,
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

_source line 20 · 2026-05-10T19:29:21.640Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JdJpHWtYSaNWU4YTHEJQYH`</summary>

```json
{
  "url": "https://www.emergentmind.com/papers/2601.03233",
  "prompt": "Extract all architectural details about the cross-modality AdaLN gating in LTX-2, including any equations, diagrams descriptions, or specific technical details about how the gating is conditioned on the other modality's timestep. Also look for any comparison to standard AdaLN-Zero or discussion of per-head vs per-layer gating."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7d0e96c-ed0b-4d79-a20a-f733ab6f7973",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSZMV4kQSt1BjmtT3E7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12ba1c97-25b3-4037-b6f8-70d03771fb59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNdShNAPRdcsNDj9uZiiGa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2277,
      "cache_read_input_tokens": 13091,
      "output_tokens": 456,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2277
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 456,
          "cache_read_input_tokens": 13091,
          "cache_creation_input_tokens": 2277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2277,
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

_source line 21 · 2026-05-10T19:29:26.492Z_

<details><summary>↩ Tool result · `toolu_01JdJpHWtYSaNWU4YTHEJQYH`</summary>

```text
# Cross-Modality AdaLN Gating in LTX-2

## Available Information

The webpage provides limited technical specifics about cross-modality AdaLN implementation. Here's what is documented:

**Core Mechanism:**
The model employs "cross-modality AdaLN for shared timestep conditioning," enabling normalization parameters in one stream to be conditioned on the counterpart modality's hidden states and timestep information.

**Functional Role:**
"AdaLN gates parameterize both scaling and shifting via the counterpart modality's hidden states and timesteps," enforcing synchronization across divergent latent resolutions.

## Critical Gaps

The document explicitly notes in its Knowledge Gaps section that "cross-modality AdaLN gating" lacks ablation studies. Specifically: "No ablation or analysis of cross-modality AdaLN (placement, parameterization, timestep conditioning strategies)" exists, and the "contribution to alignment, stability, and convergence" remains unquantified.

**Missing Details:**
- No equations or mathematical formulations provided
- No comparison to standard AdaLN-Zero variants
- No specification of per-head versus per-layer gating strategies
- No architectural diagrams showing gating placement
- No ablation studies demonstrating component importance

The webpage indicates these represent opportunities for future research rather than disclosed technical specifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12ba1c97-25b3-4037-b6f8-70d03771fb59",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "61ca60d9-1571-4949-a30f-75ab682ad2ed",
  "sourceToolAssistantUUID": "12ba1c97-25b3-4037-b6f8-70d03771fb59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:29:33.699Z_

<details><summary>↩ Tool result · `toolu_01KNGHgatoFSFp6LCm1rpT2t`</summary>

````text
# Cross-Modality AdaLN Gating Mechanism in LTX-2

## 1. AdaLN Gate Parameter Computation

The gates are computed via `get_av_ca_ada_values()`, which extracts parameters from scale-shift tables conditioned on timesteps:

```python
def get_av_ca_ada_values(
    self,
    scale_shift_table: torch.Tensor,
    batch_size: int,
    scale_shift_timestep: torch.Tensor,
    gate_timestep: torch.Tensor,
    scale_shift_indices: slice,
    num_scale_shift_values: int = 4,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    scale_shift_ada_values = self.get_ada_values(
        scale_shift_table[:num_scale_shift_values, :], batch_size, 
        scale_shift_timestep, scale_shift_indices
    )
    gate_ada_values = self.get_ada_values(
        scale_shift_table[num_scale_shift_values:, :], batch_size, 
        gate_timestep, slice(None, None)
    )
    scale, shift = (t.squeeze(2) for t in scale_shift_ada_values)
    (gate,) = (t.squeeze(2) for t in gate_ada_values)
    return scale, shift, gate
```

**Key insight**: The gate uses `gate_timestep` (the OTHER modality's timestep), while scale/shift use `scale_shift_timestep`.

## 2. Gate Dimensionality: Per-Layer, Not Per-Head

The scale-shift tables are defined as:
```python
self.scale_shift_table_a2v_ca_video = torch.nn.Parameter(
    torch.empty(5, video.dim)  # 5 parameters total per dimension
)
```

This produces gates with shape `[batch_size, seq_len, dim]`—**per-layer gating**, not per-head. The gate modulates the full feature dimension.

## 3. Gate Application: Post-Attention Output Modulation

Gates multiply the attention output directly:

```python
vx = vx + (
    self.audio_to_video_attn(
        vx_scaled,
        context=ax_scaled,
        pe=video.cross_positional_embeddings,
        k_pe=audio.cross_positional_embeddings,
    )
    * gate_out_a2v  # Gate applied to attention output
    * a2v_mask
)
```

The gate applies to post-attention residual contributions, not individual attention weights.

## 4. Cross-Modality Timestep Conditioning

For audio-to-video (A2V) attention:
```python
scale_ca_video_a2v, shift_ca_video_a2v, gate_out_a2v = 
    self.get_av_ca_ada_values(
        self.scale_shift_table_a2v_ca_video,
        vx.shape[0],
        video.cross_scale_shift_timestep,
        video.cross_gate_timestep,  # Video's OTHER timestep for gate
        slice(0, 2),
    )
```

**Pattern**: Video's `cross_gate_timestep` conditions the gate for audio context. This creates modality-specific, timestep-dependent gating.

## 5. Parameter Shapes and Slicing

- **Scale-shift table**: `[5, dim]` 
  - Indices 0-3: Scale/shift/gate for CA (split: 0-1 for scale/shift, 4+ for gate)
  - Indices 2-4: Scale/shift for subsequent V2A cross-attention
- **Gate tensor**: `[batch_size, seq_len, dim]` after squeezing
- **Slicing pattern**: `slice(0, 2)` for A2V, `slice(2, 4)` for V2A (non-overlapping gate parameter sets)

## 6. Difference from Standard AdaLN-Zero

Standard AdaLN-Zero uses single-timestep conditioning. LTX-2's cross-modality variant:
- Uses **dual timesteps** (`cross_scale_shift_timestep` + `cross_gate_timestep`)
- Applies gates **selectively per cross-attention pair** (A2V vs. V2A)
- Uses **separate parameter tables** for each direction (`scale_shift_table_a2v_ca_video` vs. `_ca_audio`)
- Gates the **residual path**, not the normalized input

Standard MSA gating pattern comparison:
```python
# Standard self-attention gate
vx = vx + self.attn1(...) * vgate_msa

# Cross-modality gating (adaptive per timestep-pair)
vx = vx + self.audio_to_video_attn(...) * gate_out_a2v * a2v_mask
```

## 7. Full Forward Pass Control Flow

The transformer block:

1. **Self-attention + self-attention AdaLN**: `vx += attn1(norm(vx)) * vgate_msa`
2. **Cross-modal text attention**: `vx += attn2(norm(vx), context) * q_gate`
3. **Audio self-attention**: Parallel to video
4. **Cross-modality attention with dual-timestep gates**:
   - A2V: Gate from `video.cross_gate_timestep`
   - V2A: Gate from `audio.cross_gate_timestep`
5. **Feed-forward + MLP AdaLN**: `vx += ff(norm(vx)) * vgate_mlp`

Perturbation masks allow selective disabling of entire cross-attention operations via `PerturbationType.SKIP_A2V_CROSS_ATTN`.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7d0e96c-ed0b-4d79-a20a-f733ab6f7973",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "09a29ced-e818-47a9-858e-f18511ab4533",
  "sourceToolAssistantUUID": "c7d0e96c-ed0b-4d79-a20a-f733ab6f7973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T19:29:37.509Z_

The source code analysis is extremely revealing. Let me also check the technical report PDF for any formal equations, and look at the model code more carefully to confirm the `cross_gate_timestep` details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09a29ced-e818-47a9-858e-f18511ab4533",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSb5ed7aSQc3g3PuMos",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05cf601a-c56b-402d-86f9-c4a819785385",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmyXysuYhMRcPvqePzgMZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 1921,
      "cache_read_input_tokens": 15368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1921,
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

_source line 24 · 2026-05-10T19:29:41.986Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0155ZofryEoH3fcpFg25UCAB`</summary>

```json
{
  "url": "https://videos.ltx.io/LTX-2/grants/LTX_2_Technical_Report_compressed.pdf",
  "prompt": "Extract ALL details about:\n1. The cross-modality AdaLN mechanism - any equations, diagrams, or formal descriptions\n2. How the gating parameters depend on the other modality's timestep\n3. Any distinction between per-head vs per-layer gating\n4. Comparison to standard AdaLN-Zero\n5. The dual-stream transformer block structure\n6. Mathematical formulations of the attention and gating operations\n7. How diffusion timesteps are embedded and used for conditioning across modalities\n\nBe extremely thorough - include any equations, figure descriptions, or architectural details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05cf601a-c56b-402d-86f9-c4a819785385",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSb5ed7aSQc3g3PuMos",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bb0549f-afe3-4fbe-baa6-ed3d2328b9e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmyXysuYhMRcPvqePzgMZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 1921,
      "cache_read_input_tokens": 15368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1921,
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

_source line 25 · 2026-05-10T19:29:45.336Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RopVaBeDRb1RnhgRDQLKdw`</summary>

```json
{
  "url": "https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-core/src/ltx_core/model/transformer/model.py",
  "prompt": "Find how cross_gate_timestep and cross_scale_shift_timestep are set. I need to understand:\n1. What exactly is the \"cross_gate_timestep\" - is it literally the other modality's diffusion timestep embedding?\n2. How are the timestep embeddings computed and passed to transformer blocks?\n3. Any data classes or containers that hold these timestep values\n4. How the video and audio timesteps are separated and cross-assigned\n\nInclude all relevant code."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bb0549f-afe3-4fbe-baa6-ed3d2328b9e1",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSb5ed7aSQc3g3PuMos",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69b08c8b-aae4-455d-81f9-63ecf0e6c90d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmyXysuYhMRcPvqePzgMZM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 1921,
      "cache_read_input_tokens": 15368,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1921
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 337,
          "output_tokens": 469,
          "cache_read_input_tokens": 15368,
          "cache_creation_input_tokens": 1921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1921,
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

_source line 26 · 2026-05-10T19:29:46.773Z_

<details><summary>↩ Tool result · `toolu_0155ZofryEoH3fcpFg25UCAB`</summary>

```text
# Cross-Modality AdaLN Mechanism - Extraction Summary

I've reviewed the provided PDF content, which appears to be a binary/encoded document without clear readable text sections containing the technical details you're requesting.

The document content displays as compressed streams and encoded font/object data typical of PDF internal structure, making it impossible to extract:

1. **Specific equations** for cross-modality AdaLN gating parameters
2. **Mathematical formulations** showing timestep dependency relationships
3. **Architectural diagrams** or formal descriptions of dual-stream structures
4. **Comparison details** to AdaLN-Zero variants
5. **Attention operation specifications**
6. **Diffusion timestep embedding methods**

## Recommendation

To provide the thorough technical extraction you need, please provide:

- The **raw text or readable version** of the paper/document
- A **direct link** to the research paper
- The **title and authors** so I can reference the work accurately

If this is a specific paper on cross-modal diffusion models with adaptive layer normalization (e.g., work on image-audio or image-text generation), sharing those identifiers would help me locate and accurately extract the technical specifications you're seeking.

I'm unable to meaningfully parse the encoded content in the provided material.

[Binary content (application/pdf, 331.9KB) also saved to /home/ubuntu/.claude-account-2/projects/-/4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e/tool-results/webfetch-1778441150877-p4busq.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bb0549f-afe3-4fbe-baa6-ed3d2328b9e1",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "a015e94e-fd7e-436a-8cde-94c99ff8724f",
  "sourceToolAssistantUUID": "9bb0549f-afe3-4fbe-baa6-ed3d2328b9e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T19:29:51.534Z_

<details><summary>↩ Tool result · `toolu_01RopVaBeDRb1RnhgRDQLKdw`</summary>

````text
# Cross-Timestep Assignment in LTX-2

Based on the provided code, I cannot find explicit definitions of `cross_gate_timestep` or `cross_scale_shift_timestep` in this file. However, I can identify the relevant infrastructure:

## Key Components Found

**1. Timestep Embedding Storage:**
The code shows timestep-related AdaLayerNorm modules are initialized:
```python
self.av_ca_video_scale_shift_adaln_single = AdaLayerNormSingle(
    self.inner_dim, embedding_coefficient=num_scale_shift_values)
self.av_ca_a2v_gate_adaln_single = AdaLayerNormSingle(
    self.inner_dim, embedding_coefficient=1)
```

**2. Preprocessor Configuration:**
The `MultiModalTransformerArgsPreprocessor` is instantiated with separate configurations for video and audio, suggesting timesteps are handled per-modality before being passed to transformer blocks.

**3. Transformer Block Processing:**
The `_process_transformer_blocks` method passes `TransformerArgs` objects (containing presumably embedded timesteps) to each `BasicAVTransformerBlock`.

## What's Missing

To fully understand cross-modal timestep assignment, you need to examine:
- The `TransformerArgs` dataclass definition
- The `MultiModalTransformerArgsPreprocessor.prepare()` implementation
- The `BasicAVTransformerBlock` forward logic

These likely contain the actual cross-timestep logic where audio's timestep embedding gets assigned to video's cross-attention gates and vice versa.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69b08c8b-aae4-455d-81f9-63ecf0e6c90d",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "52d82f28-4762-45d2-abdd-643d7dc5d292",
  "sourceToolAssistantUUID": "69b08c8b-aae4-455d-81f9-63ecf0e6c90d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T19:29:54.939Z_

Let me dig deeper into the source code to find the exact dataclass definitions and the preprocessor that assigns the cross-modal timesteps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52d82f28-4762-45d2-abdd-643d7dc5d292",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauScPvVoBC4DzcFiMNJQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffcb3e45-41f6-4796-b768-19895d2edbc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBzy5BXxq75VFytkgVLMWC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1613,
      "cache_read_input_tokens": 17289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1613,
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

_source line 29 · 2026-05-10T19:29:55.899Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V9G7micVVx4EyhgcLMj9PW`</summary>

```json
{
  "query": "site:github.com/Lightricks/LTX-2 cross_gate_timestep TransformerArgs dataclass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffcb3e45-41f6-4796-b768-19895d2edbc7",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauScPvVoBC4DzcFiMNJQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b100ece7-fafa-43ae-a8c6-507b25c8670f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBzy5BXxq75VFytkgVLMWC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1613,
      "cache_read_input_tokens": 17289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1613,
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

_source line 30 · 2026-05-10T19:29:59.537Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Rx6iPRyJbR9d4FU7dyYkNB`</summary>

```json
{
  "url": "https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-core/src/ltx_core/model/transformer/transformer.py",
  "prompt": "Find the COMPLETE code for:\n1. The TransformerArgs or any dataclass that contains cross_gate_timestep and cross_scale_shift_timestep fields\n2. The get_av_ca_ada_values method - full implementation\n3. The get_ada_values method\n4. The BasicAVTransformerBlock forward method - specifically the cross-attention section\n5. How scale_shift_table parameters are defined (their shapes, nn.Parameter definitions)\n6. Any comments explaining the cross-modal timestep conditioning\n\nShow ALL relevant code, especially the forward pass of the cross-attention with gating."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b100ece7-fafa-43ae-a8c6-507b25c8670f",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauScPvVoBC4DzcFiMNJQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38f4c36e-cb9e-4a49-9e5f-9a3532d9d0ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBzy5BXxq75VFytkgVLMWC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1613,
      "cache_read_input_tokens": 17289,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1613
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 336,
          "cache_read_input_tokens": 17289,
          "cache_creation_input_tokens": 1613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1613,
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

_source line 31 · 2026-05-10T19:29:59.824Z_

<details><summary>↩ Tool result · `toolu_01V9G7micVVx4EyhgcLMj9PW`</summary>

```text
Web search results for query: "site:github.com/Lightricks/LTX-2 cross_gate_timestep TransformerArgs dataclass"

Links: [{"title":"GitHub - Lightricks/LTX-2: Official Python inference and LoRA trainer package for the LTX-2 audio–video generative model.","url":"https://github.com/lightricks/ltx-2"}]

The search returned the main repository page but didn't find the specific code elements you're looking for with that site-restricted query. The result shows that LTX-2 is an official Python inference and LoRA trainer package for the LTX-2 audio–video generative model, but the search didn't locate the specific `cross_gate_timestep` parameter or `TransformerArgs` dataclass definition within the GitHub repository.

This could be because:
1. The search engine didn't index those specific code elements with the site restriction
2. The code may be in a file that GitHub doesn't heavily index in search results
3. The specific terms might be in code within files that aren't as readily searchable

If you need to find these specific code elements, you might want to:
- Visit the repository directly at https://github.com/Lightricks/LTX-2 and use their code search feature
- Browse the repository structure to find the Python files containing the `TransformerArgs` dataclass
- Look in the inference or model configuration files where these parameters are likely defined


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b100ece7-fafa-43ae-a8c6-507b25c8670f",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "64276d66-aa49-4cb5-bc61-2d7c710a6f41",
  "sourceToolAssistantUUID": "b100ece7-fafa-43ae-a8c6-507b25c8670f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T19:30:05.660Z_

<details><summary>↩ Tool result · `toolu_01Rx6iPRyJbR9d4FU7dyYkNB`</summary>

````text
# Analysis of LTX-2 Transformer Cross-Attention Code

Based on the provided GitHub file, here's what I found:

## 1. TransformerArgs Dataclass
The code references `TransformerArgs` but **doesn't show its complete definition** in this file. However, it's imported and used with fields including:
- `x` (tensor)
- `timesteps`
- `context`
- `positional_embeddings`
- `cross_scale_shift_timestep`
- `cross_gate_timestep`
- `prompt_timestep`
- `context_mask`

## 2. get_av_ca_ada_values Method
**Full implementation shown** (lines 294-310):

```python
def get_av_ca_ada_values(self, scale_shift_table, batch_size,
    scale_shift_timestep, gate_timestep, 
    scale_shift_indices, num_scale_shift_values=4):
  scale_shift_ada = self.get_ada_values(
      scale_shift_table[:num_scale_shift_values, :], 
      batch_size, scale_shift_timestep, 
      scale_shift_indices)
  gate_ada = self.get_ada_values(
      scale_shift_table[num_scale_shift_values:, :], 
      batch_size, gate_timestep, slice(None, None))
```

Returns: scale, shift, and gate tensors after squeezing.

## 3. get_ada_values Method
Located at lines 283-290, it extracts timestep-conditioned parameters using indexing and reshaping operations.

## 4. Cross-Attention Forward Section
Lines 330-375 handle audio-to-video and video-to-audio cross-attention with gating, applying adaptive layer normalization through scale/shift tables.

## 5. Scale-Shift Parameters
Defined as `nn.Parameter` objects with shapes like `(5, dim)` and `(2, dim)` for different modalities and attention types.

**Note:** Complete `TransformerArgs` definition isn't provided in this excerpt.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38f4c36e-cb9e-4a49-9e5f-9a3532d9d0ba",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "a7c2f8eb-9383-4e23-8afe-cdabe2ab2b99",
  "sourceToolAssistantUUID": "38f4c36e-cb9e-4a49-9e5f-9a3532d9d0ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T19:30:08.265Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0198z5i8pAs86t1wb6fs6ZLa`</summary>

```json
{
  "query": "github Lightricks LTX-2 \"cross_gate_timestep\" \"cross_scale_shift_timestep\" preprocessor code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7c2f8eb-9383-4e23-8afe-cdabe2ab2b99",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSdSHuYFvCAAUcWzVDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a939fc3-2e3b-4148-a88e-b331dc9b37d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5o2wWT3GS7HLLqqSn6Khj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1257,
      "cache_read_input_tokens": 18902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1257,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T19:30:10.377Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017FMT2rssS7WKVNnuysu7r8`</summary>

```json
{
  "url": "https://github.com/Lightricks/LTX-2/search?q=cross_gate_timestep&type=code",
  "prompt": "Find all files and code snippets that reference cross_gate_timestep. I need to understand how this value is set - is it the other modality's timestep embedding? Show all relevant code references."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a939fc3-2e3b-4148-a88e-b331dc9b37d5",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSdSHuYFvCAAUcWzVDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35e84925-4952-4fee-869b-3bcfeaaccc1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5o2wWT3GS7HLLqqSn6Khj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1257,
      "cache_read_input_tokens": 18902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1257,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T19:30:13.686Z_

<details><summary>↩ Tool result · `toolu_0198z5i8pAs86t1wb6fs6ZLa`</summary>

```text
Web search results for query: "github Lightricks LTX-2 "cross_gate_timestep" "cross_scale_shift_timestep" preprocessor code"

Links: [{"title":"LTX-2/packages/ltx-core/README.md at main · Lightricks/LTX-2","url":"https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-core/README.md"},{"title":"GitHub - Lightricks/LTX-2: Official Python inference and LoRA trainer package for the LTX-2 audio–video generative model.","url":"https://github.com/Lightricks/LTX-2"},{"title":"Lightricks/LTX-2.3 · Hugging Face","url":"https://huggingface.co/Lightricks/LTX-2.3"},{"title":"LTX-2/packages/ltx-core at main · Lightricks/LTX-2","url":"https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-core"},{"title":"GitHub - Lightricks/LTX-Video: Official repository for LTX-Video · GitHub","url":"https://github.com/Lightricks/LTX-Video"},{"title":"Lightricks/LTX-2 · Hugging Face","url":"https://huggingface.co/Lightricks/LTX-2"},{"title":"Cannot train or sample (WSL2) · Issue #33 · Lightricks/LTX-2","url":"https://github.com/Lightricks/LTX-2/issues/33"},{"title":"LTX-2/packages/ltx-pipelines/README.md at main · Lightricks/LTX-2","url":"https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/README.md"},{"title":"GitHub - wildminder/awesome-ltx2: All available LTX-2 models, encoders, workflows, LoRAs for ComfyUI · GitHub","url":"https://github.com/wildminder/awesome-ltx2"},{"title":"awesome-ltx2/README.md at main · wildminder/awesome-ltx2","url":"https://github.com/wildminder/awesome-ltx2/blob/main/README.md"}]

The search results provide information about the LTX-2 model architecture and its capabilities, but don't show the specific preprocessor code you're looking for with those function names. Based on the search results, I can tell you that:

LTX-2 uses Cross-Modality AdaLN with Scaling/shift parameters conditioned on the other modality's hidden states for synchronization across differing diffusion timesteps/temporal resolutions.

However, the specific preprocessor code containing `cross_gate_timestep` and `cross_scale_shift_timestep` functions is not appearing in these search results. To find the actual implementation, you would need to:

1. Browse the GitHub repository directly at https://github.com/Lightricks/LTX-2
2. Look in the `packages/ltx-core/src/ltx_core/model/` directory where the model implementations are stored
3. Search within the conditioning or transformer-related files for these specific function names

The search results indicate the conditioning tools are in the `conditioning/` directory for preparing latent states and applying conditioning, so the preprocessor code you're looking for is likely there.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a939fc3-2e3b-4148-a88e-b331dc9b37d5",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "c881d976-882c-418d-ac52-07b84f969aeb",
  "sourceToolAssistantUUID": "8a939fc3-2e3b-4148-a88e-b331dc9b37d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T19:30:13.832Z_

<details><summary>↩ Tool result · `toolu_017FMT2rssS7WKVNnuysu7r8`</summary>

```text
I cannot provide the requested information about `cross_gate_timestep` and how it's set in the Lightricks/LTX-2 repository.

The webpage content you've provided only shows GitHub's search interface and navigation menus. It does not contain any actual code results, file references, or technical details about `cross_gate_timestep`. The page displays a login prompt stating "Sign in to search code on GitHub" rather than showing search results.

To find code references for `cross_gate_timestep` and understand whether it represents another modality's timestep embedding, you would need to:

1. Sign in to your GitHub account
2. Navigate to the Lightricks/LTX-2 repository directly
3. Use GitHub's code search or repository browsing features to locate relevant files

If you can access and share the actual code content from the repository, I'd be happy to help analyze it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35e84925-4952-4fee-869b-3bcfeaaccc1d",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "b656b8d1-9375-4d68-bad6-f65d5fff5f52",
  "sourceToolAssistantUUID": "35e84925-4952-4fee-869b-3bcfeaaccc1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-10T19:30:16.761Z_

Let me try to access the preprocessor and args files directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b656b8d1-9375-4d68-bad6-f65d5fff5f52",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSe3G6Fky8RLK23ywy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6d20889-8fe8-4995-a1ed-d85b49fa2de8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jqRAaiwqtyvEXZdztF19M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 20159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1321,
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

_source line 38 · 2026-05-10T19:30:20.113Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FKP2Fivp66qJk1fDnQ5fL1`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lightricks/LTX-2/main/packages/ltx-core/src/ltx_core/model/transformer/model.py",
  "prompt": "Find ALL code related to:\n1. cross_gate_timestep - how it is assigned/computed\n2. cross_scale_shift_timestep - how it is assigned/computed  \n3. TransformerArgs dataclass definition\n4. MultiModalTransformerArgsPreprocessor - its prepare() method\n5. How audio timestep and video timestep are cross-assigned to each other's gates\n\nShow the complete relevant code sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6d20889-8fe8-4995-a1ed-d85b49fa2de8",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSe3G6Fky8RLK23ywy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "264e41d9-0479-4f2b-9907-211e4f42cea5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jqRAaiwqtyvEXZdztF19M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 20159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1321,
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

_source line 39 · 2026-05-10T19:30:23.637Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01481ZJyx5J2y9tntWPe7sMT`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lightricks/LTX-2/main/packages/ltx-core/src/ltx_core/model/transformer/transformer.py",
  "prompt": "Extract the COMPLETE code for:\n1. The TransformerArgs dataclass (if defined here)\n2. The BasicAVTransformerBlock class - full forward method\n3. get_av_ca_ada_values and get_ada_values methods\n4. All nn.Parameter definitions for scale_shift_table \n5. The cross-attention section showing how gate_timestep is used\n6. Any imports that reveal where TransformerArgs comes from\n\nShow ALL code verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "264e41d9-0479-4f2b-9907-211e4f42cea5",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSe3G6Fky8RLK23ywy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6da69496-8722-4716-a02a-dfd7e5377eed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jqRAaiwqtyvEXZdztF19M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1321,
      "cache_read_input_tokens": 20159,
      "output_tokens": 420,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1321
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 420,
          "cache_read_input_tokens": 20159,
          "cache_creation_input_tokens": 1321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1321,
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

_source line 40 · 2026-05-10T19:30:25.239Z_

<details><summary>↩ Tool result · `toolu_01FKP2Fivp66qJk1fDnQ5fL1`</summary>

```text
# Code Analysis: Cross-Attention Timestep Handling

Based on the provided code, I can identify the following:

## What's Present in the Document

1. **cross_gate_adaln_single and cross_scale_shift_adaln_single**: These are initialized in `_init_audio_video()` as `AdaLayerNormSingle` objects with different embedding coefficients:
   - `av_ca_video_scale_shift_adaln_single` and `av_ca_audio_scale_shift_adaln_single` (coefficient=4)
   - `av_ca_a2v_gate_adaln_single` and `av_ca_v2a_gate_adaln_single` (coefficient=1)

2. **Preprocessor Integration**: These adaln layers are passed to `MultiModalTransformerArgsPreprocessor` as `cross_scale_shift_adaln` and `cross_gate_adaln` parameters in `_init_preprocessors()`.

## What's Missing from This Document

The document **does not contain**:

- The `TransformerArgs` dataclass definition
- The `MultiModalTransformerArgsPreprocessor.prepare()` method implementation
- How `cross_gate_timestep` and `cross_scale_shift_timestep` are computed or assigned
- The mechanism for cross-assigning audio/video timesteps to each other's gates

**Conclusion**: The actual computational logic resides in imported modules (e.g., `ltx_core.model.transformer.transformer_args`) not included in this code excerpt. The current document only shows initialization and parameter passing, not the timestep computation logic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "264e41d9-0479-4f2b-9907-211e4f42cea5",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "52d1c5f8-ae56-48ea-83d5-98c8bad82c2c",
  "sourceToolAssistantUUID": "264e41d9-0479-4f2b-9907-211e4f42cea5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T19:30:31.261Z_

<details><summary>↩ Tool result · `toolu_01481ZJyx5J2y9tntWPe7sMT`</summary>

````text
# Code Extraction from BasicAVTransformerBlock

## 1. TransformerArgs Import
```python
from ltx_core.model.transformer.transformer_args import TransformerArgs
```
**Note:** TransformerArgs is imported but not defined in this file.

## 2. TransformerConfig Dataclass (Defined Here)
```python
@dataclass
class TransformerConfig:
    dim: int
    heads: int
    d_head: int
    context_dim: int
    apply_gated_attention: bool = False
    cross_attention_adaln: bool = False
```

## 3. Key Methods from BasicAVTransformerBlock

**get_ada_values method:**
```python
def get_ada_values(
    self, scale_shift_table: torch.Tensor, batch_size: int, 
    timestep: torch.Tensor, indices: slice
) -> tuple[torch.Tensor, ...]:
    num_ada_params = scale_shift_table.shape[0]
    ada_values = (
        scale_shift_table[indices].unsqueeze(0).unsqueeze(0)
        .to(device=timestep.device, dtype=timestep.dtype)
        + timestep.reshape(batch_size, timestep.shape[1], 
                          num_ada_params, -1)[:, :, indices, :]
    ).unbind(dim=2)
    return ada_values
```

**get_av_ca_ada_values method:**
```python
def get_av_ca_ada_values(
    self, scale_shift_table: torch.Tensor, batch_size: int,
    scale_shift_timestep: torch.Tensor, gate_timestep: torch.Tensor,
    scale_shift_indices: slice, num_scale_shift_values: int = 4,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    scale_shift_ada_values = self.get_ada_values(
        scale_shift_table[:num_scale_shift_values, :], batch_size, 
        scale_shift_timestep, scale_shift_indices
    )
    gate_ada_values = self.get_ada_values(
        scale_shift_table[num_scale_shift_values:, :], batch_size, 
        gate_timestep, slice(None, None)
    )
    scale, shift = (t.squeeze(2) for t in scale_shift_ada_values)
    (gate,) = (t.squeeze(2) for t in gate_ada_values)
    return scale, shift, gate
```

## 4. nn.Parameter Definitions

```python
# Video parameters
self.scale_shift_table = torch.nn.Parameter(
    torch.empty(video_sst_size, video.dim))
self.prompt_scale_shift_table = torch.nn.Parameter(
    torch.empty(2, video.dim))
self.scale_shift_table_a2v_ca_video = torch.nn.Parameter(
    torch.empty(5, video.dim))

# Audio parameters
self.audio_scale_shift_table = torch.nn.Parameter(
    torch.empty(audio_sst_size, audio.dim))
self.audio_prompt_scale_shift_table = torch.nn.Parameter(
    torch.empty(2, audio.dim))
self.scale_shift_table_a2v_ca_audio = torch.nn.Parameter(
    torch.empty(5, audio.dim))
```

## 5. Cross-Attention Section with gate_timestep Usage

```python
if run_a2v and not perturbations.all_in_batch(...):
    scale_ca_video_a2v, shift_ca_video_a2v, gate_out_a2v = \
        self.get_av_ca_ada_values(
            self.scale_shift_table_a2v_ca_video,
            vx.shape[0],
            video.cross_scale_shift_timestep,
            video.cross_gate_timestep,  # gate_timestep parameter
            slice(0, 2),
        )
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6da69496-8722-4716-a02a-dfd7e5377eed",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "6c3a3476-c78c-4e95-ad48-f5427aad9106",
  "sourceToolAssistantUUID": "6da69496-8722-4716-a02a-dfd7e5377eed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T19:30:39.328Z_

Now let me find the TransformerArgs dataclass and the preprocessor to understand how `cross_gate_timestep` is actually assigned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c3a3476-c78c-4e95-ad48-f5427aad9106",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSfKnnXg1kv4rJEXzsR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9ce23e1-e937-4c26-86ad-6943b28718ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYxSavnevNLEfz6acAyKw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 21480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1872,
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

_source line 43 · 2026-05-10T19:30:40.905Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XphAigagB2W8tE6PNGdCvn`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lightricks/LTX-2/main/packages/ltx-core/src/ltx_core/model/transformer/transformer_args.py",
  "prompt": "Show the COMPLETE file contents. I need:\n1. The TransformerArgs dataclass definition with ALL fields\n2. How cross_gate_timestep is defined\n3. How cross_scale_shift_timestep is defined\n4. The MultiModalTransformerArgsPreprocessor class and its prepare() method\n5. How audio and video timesteps are cross-assigned\n\nShow ALL code verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9ce23e1-e937-4c26-86ad-6943b28718ac",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSfKnnXg1kv4rJEXzsR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b947a0e8-d55b-47ef-8563-7d8ff227cb58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYxSavnevNLEfz6acAyKw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 21480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1872,
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

_source line 44 · 2026-05-10T19:30:46.853Z_

<details><summary>↩ Tool result · `toolu_01XphAigagB2W8tE6PNGdCvn`</summary>

````text
# Complete File Contents Analysis

## 1. TransformerArgs Dataclass (ALL fields)

```python
@dataclass(frozen=True)
class TransformerArgs:
    x: torch.Tensor
    context: torch.Tensor
    context_mask: torch.Tensor
    timesteps: torch.Tensor
    embedded_timestep: torch.Tensor
    positional_embeddings: torch.Tensor
    cross_positional_embeddings: torch.Tensor | None
    cross_scale_shift_timestep: torch.Tensor | None
    cross_gate_timestep: torch.Tensor | None
    enabled: bool
    prompt_timestep: torch.Tensor | None = None
    self_attention_mask: torch.Tensor | None = None
```

## 2. cross_gate_timestep Definition

"gate_noise_timestep" is computed via `self.cross_gate_adaln()` applied to the scaled timestep multiplied by an audio-visual cross-attention factor, then reshaped to match batch dimensions.

## 3. cross_scale_shift_timestep Definition

"scale_shift_timestep" derives from `self.cross_scale_shift_adaln()` processing the scaled timestep, then reshape to batch size matching the primary modality.

## 4. MultiModalTransformerArgsPreprocessor Class & prepare() Method

The class wraps a `TransformerArgsPreprocessor` instance and extends functionality. The `prepare()` method processes primary modality through the simple preprocessor, then conditionally augments results with cross-modality embeddings and timestep values using `dataclasses.replace()`.

## 5. Audio-Video Timestep Cross-Assignment

The cross-modality sigma tensor undergoes reshaping and scaling. The timestep multiplier ratio creates an "av_ca_factor" applied asymmetrically: scale-shift uses base multiplier, while gate uses the factor-adjusted value, enabling differentiated processing of audio-visual interactions.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b947a0e8-d55b-47ef-8563-7d8ff227cb58",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "b133e381-0b72-47bb-9997-e98b5592758f",
  "sourceToolAssistantUUID": "b947a0e8-d55b-47ef-8563-7d8ff227cb58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-10T19:30:51.151Z_

This is getting closer but the response is summarized rather than verbatim. Let me try to get the raw content more precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b133e381-0b72-47bb-9997-e98b5592758f",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSgUVCVEMUDQdrC4Ae1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b06f92e1-8693-4359-aa5f-1d6bedc4d819",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CZ9cYD9h3bWDjgScmBdDZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 23352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 703,
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

_source line 46 · 2026-05-10T19:30:52.161Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014CzRgReARdd8vXKKkQc2fJ`</summary>

```json
{
  "command": "curl -sL \"https://raw.githubusercontent.com/Lightricks/LTX-2/main/packages/ltx-core/src/ltx_core/model/transformer/transformer_args.py\" 2>/dev/null | head -200",
  "description": "Fetch raw source code for transformer_args.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b06f92e1-8693-4359-aa5f-1d6bedc4d819",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSgUVCVEMUDQdrC4Ae1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d1a6d82-7a73-45fd-a56a-8e2aeb338d44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CZ9cYD9h3bWDjgScmBdDZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 23352,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 703
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 23352,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 703,
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

_source line 47 · 2026-05-10T19:30:52.176Z_

<details><summary>↩ Tool result · reported error · `toolu_014CzRgReARdd8vXKKkQc2fJ`</summary>

```text
This Bash command contains multiple operations. The following part requires approval: curl -sL "https://raw.githubusercontent.com/Lightricks/LTX-2/main/packages/ltx-core/src/ltx_core/model/transformer/transformer_args.py"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d1a6d82-7a73-45fd-a56a-8e2aeb338d44",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "4c8760c6-8146-4f26-95f2-450fe7974b86",
  "toolUseResult": "Error: This Bash command contains multiple operations. The following part requires approval: curl -sL \"https://raw.githubusercontent.com/Lightricks/LTX-2/main/packages/ltx-core/src/ltx_core/model/transformer/transformer_args.py\"",
  "sourceToolAssistantUUID": "8d1a6d82-7a73-45fd-a56a-8e2aeb338d44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-10T19:30:58.553Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DuHu4BNTQdBDNudmEsHy21`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lightricks/LTX-2/main/packages/ltx-core/src/ltx_core/model/transformer/transformer_args.py",
  "prompt": "I need the VERBATIM source code - do NOT summarize. Show every line of code in this file exactly as written. Specifically I need to see:\n1. The exact implementation of prepare() method showing how cross_gate_timestep gets its value\n2. Whether cross_gate_timestep uses the OTHER modality's timestep or the SAME modality's timestep\n3. Any variable like av_ca_factor, sigma, or cross-modal timestep that shows the source of the gate conditioning\n4. The complete prepare() method code word-for-word"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c8760c6-8146-4f26-95f2-450fe7974b86",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSgsZmCvvMEi1nR3yPM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f3cad8e-43c8-48e2-86c7-3fb74a8fdc26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjzY4hXfBpeS1iCHzU2PQ7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 24055,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 248
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 24055,
          "cache_creation_input_tokens": 248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 248,
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

_source line 49 · 2026-05-10T19:31:01.484Z_

<details><summary>↩ Tool result · `toolu_01DuHu4BNTQdBDNudmEsHy21`</summary>

````text
# Analysis of cross_gate_timestep Source

Based on the code provided, here are the key findings:

## Which modality does cross_gate_timestep use?

`cross_gate_timestep` uses the **OTHER modality's timestep** (the cross_modality). In the `prepare()` method:

```python
cross_timestep = cross_modality.sigma.view(
    modality.timesteps.shape[0], 1, *[1] * len(modality.timesteps.shape[2:])
)
```

The timestep originates from `cross_modality.sigma`, not from the primary modality.

## The prepare() method implementation

The complete relevant section shows:

```python
cross_scale_shift_timestep, cross_gate_timestep = self._prepare_cross_attention_timestep(
    timestep=cross_timestep,
    timestep_scale_multiplier=self.simple_preprocessor.timestep_scale_multiplier,
    batch_size=transformer_args.x.shape[0],
    hidden_dtype=modality.latent.dtype,
)
```

## The cross_gate_timestep derivation

Inside `_prepare_cross_attention_timestep()`:

```python
av_ca_factor = self.av_ca_timestep_scale_multiplier / timestep_scale_multiplier
gate_noise_timestep, _ = self.cross_gate_adaln(
    timestep.flatten() * av_ca_factor,
    hidden_dtype=hidden_dtype,
)
```

The gate conditioning applies a scaling factor (`av_ca_factor`) to the cross-modality's sigma before embedding.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f3cad8e-43c8-48e2-86c7-3fb74a8fdc26",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "b18ee38a-f6d1-4004-9d28-1f005ce6b86c",
  "sourceToolAssistantUUID": "9f3cad8e-43c8-48e2-86c7-3fb74a8fdc26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-10T19:31:13.689Z_

This is exactly what I needed. Now I have the complete picture. Let me do one final search to confirm if there are any per-head gating details or if DualGate has been published.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b18ee38a-f6d1-4004-9d28-1f005ce6b86c",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauShZ166haJ8p4NUVEyZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a679cb14-286c-4132-b892-94047c969a80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nWsf5s9i99udCPqkzCiyC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 636,
      "cache_read_input_tokens": 24303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 636,
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

_source line 51 · 2026-05-10T19:31:14.608Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016PA4Dczp9G5GQvqZKxArTK`</summary>

```json
{
  "query": "\"DualGate\" cross-modal gating diffusion transformer per-head timestep conditioned 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a679cb14-286c-4132-b892-94047c969a80",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauShZ166haJ8p4NUVEyZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a189e45-8e2f-45eb-acec-945f0b36cd6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nWsf5s9i99udCPqkzCiyC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 636,
      "cache_read_input_tokens": 24303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 636,
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

_source line 52 · 2026-05-10T19:31:20.298Z_

<details><summary>↩ Tool result · `toolu_016PA4Dczp9G5GQvqZKxArTK`</summary>

```text
Web search results for query: ""DualGate" cross-modal gating diffusion transformer per-head timestep conditioned 2025 2026"

Links: [{"title":"TAMING TEXT-TO-SOUNDING VIDEO GENERATION","url":"https://arxiv.org/pdf/2510.03117"},{"title":"Temporally-Aligned Diffusion Features for Cross-Modal Audio ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Haji-Ali_AV-Link_Temporally-Aligned_Diffusion_Features_for_Cross-Modal_Audio-Video_Generation_ICCV_2025_paper.pdf"},{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Lv_Rethinking_Cross-Modal_Interaction_in_Multimodal_Diffusion_Transformers_ICCV_2025_paper.pdf"},{"title":"Scalable Diffusion Models with Transformers","url":"https://www.researchgate.net/publication/377426954_Scalable_Diffusion_Models_with_Transformers"},{"title":"Gated Condition Injection without Multimodal Attention: Towards Controllable Linear-Attention Transformers","url":"https://arxiv.org/html/2603.27666v1"},{"title":"Gated Fusion Mechanisms","url":"https://www.emergentmind.com/topics/gated-fusion-mechanism"},{"title":"Why Cross-Attention is the Secret Sauce of Multimodal Models | by Jakub Strawa | Medium","url":"https://medium.com/@jakubstrawadev/why-cross-attention-is-the-secret-sauce-of-multimodal-models-f8ec77fc089b"},{"title":"Practice: Building a Diffusion Transformer Block","url":"https://apxml.com/courses/advanced-diffusion-architectures/chapter-3-transformer-diffusion-models/practice-building-dit-block"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/15f4cefb0e143c7ad9d40e879b0a9d0c-Paper-Conference.pdf"},{"title":"GitHub - HaozheLiu-ST/T-GATE: T-GATE: Temporally Gating Attention to Accelerate Diffusion Model for Free! · GitHub","url":"https://github.com/HaozheLiu-ST/T-GATE"}]

Based on the search results, I found some relevant work related to cross-modal gating and diffusion transformers, but I did not find a specific paper or method explicitly titled "DualGate" with the exact specification you mentioned.

However, the search results reveal several related approaches in this research area:

1. **Cross-Modal Interaction in Diffusion Transformers**: A paper titled "Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers" was published at ICCV 2025, which addresses cross-modal fusion in diffusion transformer architectures.

2. **Timestep Conditioning in Diffusion Models**: Cross-modal blocks in diffusion models are conditioned on timestep conditions via adaptive layer normalization, which relates to the per-head timestep conditioning you mentioned.

3. **Gated Conditioning Mechanisms**: A learnable gating module can mitigate information loss in attention interactions and support expressive cross-modal conditioning, demonstrating how gating mechanisms work in recent diffusion frameworks.

4. **Temporal Gating**: Temporally gating attention (T-GATE) is a method that efficiently generates images by caching and reusing attention outputs at scheduled time steps.

If "DualGate" is a very recent paper or uses alternative naming, you might want to search directly on arxiv.org or check recent conference proceedings (ICCV 2025, ICLR 2026, etc.) for the most up-to-date publications on this specific method.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a189e45-8e2f-45eb-acec-945f0b36cd6d",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a077ce1cbc27af79e",
  "type": "user",
  "uuid": "0cbc3069-1849-4936-9f24-7cccb3daaa02",
  "sourceToolAssistantUUID": "3a189e45-8e2f-45eb-acec-945f0b36cd6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-10T19:32:15.309Z_

I now have all the information needed to provide a comprehensive analysis. Here is my report:

---

## LTX-2 Cross-Modality AdaLN Gating: Detailed Architectural Analysis

**Paper**: "LTX-2: Efficient Joint Audio-Visual Foundation Model" (arXiv: 2601.03233, January 2025, Lightricks)

### 1. Is the gating truly conditioned on the other modality's timestep?

**Yes, confirmed from source code.** The cross-modal gate is conditioned on the OTHER modality's diffusion timestep. The implementation in `transformer_args.py` makes this explicit:

```python
cross_timestep = cross_modality.sigma.view(
    modality.timesteps.shape[0], 1, *[1] * len(modality.timesteps.shape[2:])
)
```

The `cross_timestep` originates from `cross_modality.sigma` -- i.e., the sigma (noise level / timestep) of the opposite stream. This is then passed through a dedicated AdaLN embedding:

```python
cross_scale_shift_timestep, cross_gate_timestep = self._prepare_cross_attention_timestep(
    timestep=cross_timestep,  # <-- OTHER modality's sigma
    ...
)
```

Inside `_prepare_cross_attention_timestep()`, a scaling factor is applied before embedding:

```python
av_ca_factor = self.av_ca_timestep_scale_multiplier / timestep_scale_multiplier
gate_noise_timestep, _ = self.cross_gate_adaln(
    timestep.flatten() * av_ca_factor,
    hidden_dtype=hidden_dtype,
)
```

**Critical nuance**: Both `cross_scale_shift_timestep` AND `cross_gate_timestep` derive from the other modality's sigma, but they pass through **separate** AdaLN embedding networks (`cross_scale_shift_adaln` vs `cross_gate_adaln`) with potentially different scaling factors. The scale/shift uses the base multiplier while the gate uses an `av_ca_factor`-adjusted value.

### 2. Is it per-head or per-layer?

**Per-layer, not per-head.** The scale-shift tables are defined as:

```python
self.scale_shift_table_a2v_ca_video = torch.nn.Parameter(
    torch.empty(5, video.dim)   # shape: [5, dim]
)
```

The resulting gate tensor has shape `[batch_size, seq_len, dim]` after squeezing -- it operates on the full hidden dimension, not decomposed per attention head. There is no head-dimension indexing anywhere in the gating logic.

### 3. Does it apply to attention weights or post-attention features?

**Post-attention features (the residual contribution), not attention weights.** The gate multiplies the output of the cross-attention operation before it is added back to the residual stream:

```python
vx = vx + (
    self.audio_to_video_attn(
        vx_scaled,
        context=ax_scaled,
        pe=video.cross_positional_embeddings,
        k_pe=audio.cross_positional_embeddings,
    )
    * gate_out_a2v   # <-- gate applied to cross-attn OUTPUT
    * a2v_mask
)
```

Additionally, the pre-attention inputs (Q from current modality, K/V from other modality) are modulated by scale/shift parameters also derived from the other modality's timestep. But the **gate** specifically controls how much of the cross-attended result gets integrated into the residual.

### 4. How does it differ from standard AdaLN-Zero gating?

Standard AdaLN-Zero (as in DiT) uses a **single** timestep embedding to produce scale, shift, and gate parameters for self-attention and MLP within a single-modality block. LTX-2's cross-modality AdaLN differs in several ways:

| Aspect | Standard AdaLN-Zero | LTX-2 Cross-Modality AdaLN |
|--------|---------------------|---------------------------|
| **Timestep source** | Own stream's timestep | Other modality's timestep (sigma) |
| **Dual timestep** | No -- single conditioning signal | Yes -- scale/shift and gate can use different embeddings of the cross-modal timestep (different scaling factors) |
| **Scope** | Self-attention + MLP within one stream | Cross-attention between two modality streams |
| **Directionality** | N/A | Separate parameter tables per direction (A2V vs V2A), with independent `scale_shift_table_a2v_ca_video` and `scale_shift_table_a2v_ca_audio` |
| **Parameter structure** | Typically `[6, dim]` (scale, shift, gate for attn + MLP) | `[5, dim]` per cross-attn direction (4 scale/shift + 1 gate) |
| **Perturbation support** | No | Yes -- can selectively skip entire cross-attn directions via `PerturbationType.SKIP_A2V_CROSS_ATTN` |

Importantly, LTX-2 **also** uses standard AdaLN-Zero for its self-attention and MLP (conditioned on each stream's own timestep):
```python
vx = vx + self.attn1(...) * vgate_msa   # standard AdaLN-Zero self-attn gate
```

The cross-modality variant is an **additional** mechanism layered on top, specifically for the bidirectional cross-attention blocks.

### Assessment for DualGate's Novelty

Based on this analysis, LTX-2's mechanism is indeed close to a "cross-modal timestep-conditioned gate" concept but has specific characteristics that may leave room for differentiation:

**Overlap with DualGate-like ideas:**
- Gate parameters are conditioned on the other modality's diffusion timestep -- this is the core idea
- It controls cross-modal information flow as a function of denoising stage
- It operates as a learned, adaptive gate (not fixed)

**Potential differentiation points for DualGate:**
- LTX-2's gating is **per-layer** -- if DualGate proposes **per-head** gating, that would be a genuine architectural difference
- LTX-2 gates the **post-attention residual** only -- if DualGate additionally gates attention weights or applies gating at different points (e.g., within the attention computation itself), that differs
- LTX-2 uses the other modality's **sigma/noise-level** specifically -- if DualGate conditions on richer representations (e.g., the other modality's hidden states rather than just its scalar timestep), the conditioning signal is fundamentally different
- LTX-2 applies this only to audio-video cross-attention -- DualGate might target different modality pairs or apply to self-attention as well
- No ablation exists in LTX-2 for this component (as noted by Emergent Mind's analysis), so its individual contribution is unquantified

**Bottom line**: The claim that "post-attention AdaLN gate whose parameters depend on the OTHER modality's timestep" exists in LTX-2 is **confirmed and precise**. This is a real prior art concern for DualGate if DualGate's core novelty is cross-modal timestep-conditioned gating of post-attention features at the layer level. DualGate would need to demonstrate clear architectural or granularity differences (per-head, different conditioning signals, different application points) to maintain a distinct novelty claim.

Sources:
- [LTX-2 Paper (arXiv HTML)](https://arxiv.org/html/2601.03233v1)
- [LTX-2 Paper (arXiv Abstract)](https://arxiv.org/abs/2601.03233)
- [LTX-2 GitHub Repository](https://github.com/Lightricks/LTX-2)
- [LTX-2 Source Code - transformer.py](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-core/src/ltx_core/model/transformer/transformer.py)
- [LTX-2 Source Code - model.py](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-core/src/ltx_core/model/transformer/model.py)
- [Emergent Mind Analysis](https://www.emergentmind.com/papers/2601.03233)
- [HuggingFace Paper Page](https://huggingface.co/papers/2601.03233)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cbc3069-1849-4936-9f24-7cccb3daaa02",
  "isSidechain": true,
  "agentId": "a077ce1cbc27af79e",
  "requestId": "req_011CauSiwTEEZAe4MigpbVtV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a432345-01b7-4725-8eff-42e82e6916ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cjurLRCqXe7TACFaQ368F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1149,
      "cache_read_input_tokens": 24939,
      "output_tokens": 2114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1149
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2114,
          "cache_read_input_tokens": 24939,
          "cache_creation_input_tokens": 1149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1149,
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
