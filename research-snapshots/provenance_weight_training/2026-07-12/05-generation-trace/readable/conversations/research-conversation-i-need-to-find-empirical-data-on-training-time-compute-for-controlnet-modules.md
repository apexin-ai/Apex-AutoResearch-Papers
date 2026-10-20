# Research conversation: I need to find empirical data on training time/compute for ControlNet modules on Wan 2.2 (a video diffusion transformer 

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae8f10664b54150d4.jsonl`
- **Structured JSON:** [`bd6e5ec3173fcd696fe4.json`](../../sessions/bd/bd6e5ec3173fcd696fe4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

70 recorded events

### User

_source line 1 · 2026-05-10T12:10:46.458Z_

I need to find empirical data on training time/compute for ControlNet modules on Wan 2.2 (a video diffusion transformer model). This is for anchoring compute estimates in a research proposal.

Please search for and fetch:

1. **TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1** on HuggingFace — does this model exist? What training details are reported? How long did ControlNet training on Wan 2.2 take?
   - Try: https://huggingface.co/TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1
   - Try: https://huggingface.co/TheDenk

2. Search for Wan 2.1/2.2 LoRA fine-tuning and ControlNet training time reports:
   - "Wan 2.2 ControlNet training GPU hours"
   - "Wan 2.1 LoRA fine-tuning A40 hours"
   - "WanVideo ControlNet training compute"

3. Search for: "wan video controlnet depth training time H100"

4. Also look for: "video diffusion ControlNet training compute estimate temporal attention overhead"

Please report specific numbers: how many GPU-hours on what hardware, dataset sizes, and any reported training configurations. This is critical for anchoring our 35-70h estimate on H100s.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "fbae4363-9985-48de-a178-74cbb2343a93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T12:10:46.464Z_

```json
{
  "parentUuid": "fbae4363-9985-48de-a178-74cbb2343a93",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
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
  "uuid": "4e14d08e-b4a7-487f-ba5e-d58d773b885d",
  "timestamp": "2026-05-10T12:10:46.464Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T12:10:48.363Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BNsT4hdqDZ4bHHEMrNoBky`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e14d08e-b4a7-487f-ba5e-d58d773b885d",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats8PSMfah8Q8aRk8kE1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1be39bf3-d0d2-4ae2-b942-11f8c2069a25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QZjYa126EX7WVLEQa2P6AC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 8088,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 8088,
          "cache_creation_input_tokens": 886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 886,
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

_source line 4 · 2026-05-10T12:10:48.366Z_

<details><summary>↩ Tool result · `toolu_01BNsT4hdqDZ4bHHEMrNoBky`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "1be39bf3-d0d2-4ae2-b942-11f8c2069a25",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "93545f00-b693-4be8-bc30-364d217acbb9",
  "sourceToolAssistantUUID": "1be39bf3-d0d2-4ae2-b942-11f8c2069a25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T12:10:50.536Z_

I'll fetch the HuggingFace model page and run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93545f00-b693-4be8-bc30-364d217acbb9",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats8XigJS7QL5pBPU5JY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ff133d1-ed36-4d45-9e19-5403f94a3e18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UpyVzjsyw32Hpooe4TTmKv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8974,
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

_source line 6 · 2026-05-10T12:10:52.500Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0122vziG5BrMPfW3ud4qznMi`</summary>

```json
{
  "url": "https://huggingface.co/TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1",
  "prompt": "Extract all training details: GPU hardware used, training duration (hours, days), number of training steps, batch size, dataset size, learning rate, and any other compute-related information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ff133d1-ed36-4d45-9e19-5403f94a3e18",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats8XigJS7QL5pBPU5JY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7c82994-4eff-4f9b-bb6d-3158b4ddd20c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UpyVzjsyw32Hpooe4TTmKv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8974,
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

_source line 7 · 2026-05-10T12:10:53.280Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EurxisMQj7TC27Dg84vtw7`</summary>

```json
{
  "url": "https://huggingface.co/TheDenk",
  "prompt": "List all models available on this profile, especially any Wan 2.1 or Wan 2.2 ControlNet models. Note any training details mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7c82994-4eff-4f9b-bb6d-3158b4ddd20c",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats8XigJS7QL5pBPU5JY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17b612d5-38c3-43fb-885f-109e8e3757f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UpyVzjsyw32Hpooe4TTmKv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8974,
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

_source line 8 · 2026-05-10T12:10:54.015Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NkTvVv56yFY1QpLqpYZHMa`</summary>

```json
{
  "query": "Wan 2.2 ControlNet training GPU hours compute time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17b612d5-38c3-43fb-885f-109e8e3757f4",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats8XigJS7QL5pBPU5JY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbd38992-b6ea-416b-a61e-10665621526d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UpyVzjsyw32Hpooe4TTmKv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8974,
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

_source line 9 · 2026-05-10T12:10:54.164Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VWYaeH2UFQ3LP7Pw31AyWy`</summary>

```json
{
  "query": "Wan 2.1 LoRA fine-tuning A40 training hours video diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbd38992-b6ea-416b-a61e-10665621526d",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats8XigJS7QL5pBPU5JY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7c2bd19-ae7e-4014-ae68-0ff601c1d04b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UpyVzjsyw32Hpooe4TTmKv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8974,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 362,
          "cache_read_input_tokens": 8974,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1888,
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

_source line 10 · 2026-05-10T12:10:56.359Z_

<details><summary>↩ Tool result · `toolu_0122vziG5BrMPfW3ud4qznMi`</summary>

```text
# Training Details Extraction

Based on the provided web page content, **no training details are available**. The page does not contain information about:

- GPU hardware used
- Training duration (hours, days)
- Number of training steps
- Batch size
- Dataset size
- Learning rate
- Other compute-related information

## What the Page Contains

The page is a Hugging Face model card for **TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1**, which includes:

1. **Usage instructions** - How to use the model with Diffusers and other libraries
2. **Code examples** - CLI and minimal code examples for inference
3. **Dependencies** - Required packages (diffusers, transformers, accelerate)
4. **Model specifications** - Base model path: `Wan-AI/Wan2.2-TI2V-5B-Diffusers`
5. **References** - Links to the GitHub repository and original Wan2.2 project

## Recommendation

To find training details, you would need to:
- Check the **GitHub repository**: https://github.com/TheDenk/wan2.2-controlnet
- Consult the **original Wan2.2 documentation**: https://github.com/Wan-Video/Wan2.2
- Review the **model card details** on Hugging Face (may contain additional information not shown in this excerpt)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7c82994-4eff-4f9b-bb6d-3158b4ddd20c",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "d1a49e8c-6939-4fc0-9428-09368eb093c0",
  "sourceToolAssistantUUID": "a7c82994-4eff-4f9b-bb6d-3158b4ddd20c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T12:10:58.608Z_

<details><summary>↩ Tool result · `toolu_01EurxisMQj7TC27Dg84vtw7`</summary>

```text
# TheDenk's Models Overview

## Wan 2.2 ControlNet Models (Latest)

1. **TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1** - Updated Oct 30, 2025 (239 downloads, 10 likes)
2. **TheDenk/wan2.2-t2v-a14b-controlnet-depth-v1** - Updated Oct 30, 2025 (167 downloads, 11 likes)
3. **TheDenk/wan2.2-ti2v-5b-controlnet-tile-v1** - Updated Oct 30, 2025 (38 downloads, 6 likes)
4. **TheDenk/wan2.2-t2v-a14b-controlnet-hed-v1** - Updated Oct 30, 2025 (61 downloads, 4 likes)
5. **TheDenk/wan2.2-ti2v-5b-controlnet-hed-v1** - Updated Oct 30, 2025 (21 downloads, 1 like)
6. **TheDenk/wan2.2-ti2v-5b-controlnet-canny-v1** - Updated Oct 30, 2025 (234 downloads, 1 like)
7. **TheDenk/wan2.2-video-continuation** - Updated Nov 1, 2025 (3 downloads, 2 likes)

## Wan 2.1 ControlNet Models

1. **TheDenk/wan2.1-t2v-14b-controlnet-hed-v1** - Updated May 26, 2025 (100 downloads, 10 likes)
2. **TheDenk/wan2.1-t2v-14b-controlnet-depth-v1** - Updated May 27, 2025 (143 downloads, 5 likes)
3. **TheDenk/wan2.1-t2v-1.3b-controlnet-hed-v1** - Updated May 27, 2025 (100 downloads, 4 likes)
4. **TheDenk/wan2.1-t2v-1.3b-controlnet-depth-v1** - Updated May 30, 2025 (143 downloads, 5 likes)
5. **TheDenk/wan2.1-t2v-1.3b-controlnet-canny-v1** - Updated May 27, 2025 (185 downloads, 1 like)

## Other Assets
- **Total models**: 19
- **Total datasets**: 1 (TheDenk/images_mixing)
- **Code repositories**: https://github.com/TheDenk/wan2.2-controlnet and https://github.com/TheDenk/wan2.1-dilated-controlnet

**Note**: The profile indicates "In a Training Loop 🔄" status. No specific training details are mentioned in the available content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17b612d5-38c3-43fb-885f-109e8e3757f4",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "e0671721-86b2-47d4-b02f-04b95c973815",
  "sourceToolAssistantUUID": "17b612d5-38c3-43fb-885f-109e8e3757f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T12:11:00.283Z_

<details><summary>↩ Tool result · `toolu_01NkTvVv56yFY1QpLqpYZHMa`</summary>

```text
Web search results for query: "Wan 2.2 ControlNet training GPU hours compute time"

Links: [{"title":"How Independent Animators Use Wan 3.0 to Self-Host a Full AI Video Pipeline on a Single GPU Server - Flowith Blog","url":"https://flowith.io/blog/how-independent-animators-use-wan-3-0-self-host-ai-video-pipeline/"},{"title":"How Long It Takes to Train a WAN 2.2 Video LoRA - Complete 2025 Analysis | Apatero Blog - Open Source AI & Programming Tutorials","url":"https://www.apatero.com/blog/wan-22-video-lora-training-time-complete-analysis-2025"},{"title":"Fine-tuning Wan 2.1 With a Curated Dataset on the GPU Cloud (Step-by-Step Guide) | by learn2train.org | Medium","url":"https://learn2train.medium.com/fine-tuning-wan-2-1-with-a-curated-dataset-step-by-step-guide-a6f0b334ab79"},{"title":"GitHub - deepbeepmeep/Wan2GP: A fast AI Video Generator for the GPU Poor. Supports Wan 2.1/2.2, Qwen Image, Hunyuan Video, LTX Video and Flux. · GitHub","url":"https://github.com/deepbeepmeep/Wan2GP"},{"title":"Wan 22 Complete Training Tutorial Text to Image Text to Video Image to Video Windows and Cloud","url":"https://github.com/FurkanGozukara/Stable-Diffusion/wiki/Wan-22-Complete-Training-Tutorial-Text-to-Image-Text-to-Video-Image-to-Video-Windows-and-Cloud"},{"title":"Wan 2.6 / 3.0 FAQ: Model Architecture, Hardware Requirements, Commercial License, and Fine-Tuning Guide - Flowith Blog","url":"https://flowith.io/blog/wan-2-6-3-0-faq-model-architecture-hardware-commercial-license-fine-tuning/"},{"title":"What Is Wan 2.2 Video? Open-Source AI Video with LoRA Support | MindStudio","url":"https://www.mindstudio.ai/blog/what-is-wan-2-2-video-open-source"},{"title":"Wan 2.2 LoRA Training (Windows/Linux)","url":"https://www.stablediffusiontutorials.com/2025/10/wan2.2-lora-training.html"},{"title":"TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1 · Hugging Face","url":"https://huggingface.co/TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1"},{"title":"WAN 2.2 i2v: Second run is 4 5to 5 times slower on AMD GPU (ROCm) · Issue #12672 · Comfy-Org/ComfyUI","url":"https://github.com/Comfy-Org/ComfyUI/issues/12672"}]

Based on the search results, here's what I found regarding Wan 2.2 ControlNet training GPU hours and compute time:

## ControlNet Training Time

I found limited specific information about ControlNet training for Wan 2.2. However, there is a ControlNet implementation available: A ControlNet module for Wan 2.2 exists using the same approach as ControlNet for Wan 2.1, and it's available on Hugging Face.

## General Wan 2.2 Training Times

For reference, here are the broader training time estimates for Wan 2.2:

- **LoRA Training**: Training takes 2-6 hours on a single GPU
- **Detailed Example**: A 287-sample character LoRA at 512x512 with dimension 64 trained in 6 hours 43 minutes on RTX 4090, including 15 epochs and 4,305 total steps with FP16 precision and gradient checkpointing enabled
- **Video LoRA (I2V)**: Training a video LoRA on NVIDIA A6000 with 96 GB VRAM took almost 24 hours

The search results don't contain specific training times for the ControlNet model itself. For more detailed information about ControlNet training specifications, you may want to check the official Wan 2.2 repository or the specific ControlNet implementation on GitHub/Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbd38992-b6ea-416b-a61e-10665621526d",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "8936f08f-11cd-4892-a125-4830f4ccac32",
  "sourceToolAssistantUUID": "cbd38992-b6ea-416b-a61e-10665621526d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T12:11:02.676Z_

<details><summary>↩ Tool result · `toolu_01VWYaeH2UFQ3LP7Pw31AyWy`</summary>

```text
Web search results for query: "Wan 2.1 LoRA fine-tuning A40 training hours video diffusion"

Links: [{"title":"Fine-tuning Wan 2.1 With a Curated Dataset on the GPU Cloud (Step-by-Step Guide) | by learn2train.org | Medium","url":"https://learn2train.medium.com/fine-tuning-wan-2-1-with-a-curated-dataset-step-by-step-guide-a6f0b334ab79"},{"title":"Fine‑Tuning Open Video Generators for Cinematic Scene Synthesis: A Small‑Data Pipeline with LoRA and Wan2.1 I2V*","url":"https://arxiv.org/html/2510.27364v1"},{"title":"Training WAN2.2 for your character/custom-style ultra-realistic images | by Areeb Ahmad | Medium","url":"https://medium.com/@ahmadareeb3026/training-wan2-2-for-your-character-custom-style-ultra-realistic-images-f8993350c862"},{"title":"Train your WAN2.1 Lora model on Windows/Linux","url":"https://www.stablediffusiontutorials.com/2025/03/wan-lora-train.html"},{"title":"WAN 2.1 LoRA Training Time Sanity Check · Issue #152 · tdrussell/diffusion-pipe","url":"https://github.com/tdrussell/diffusion-pipe/issues/152"},{"title":"Wan 2.2 I2V 14B LoRA Training with AI Toolkit | Image-to-Video","url":"https://www.runcomfy.com/trainer/ai-toolkit/wan-2-2-i2v-14b-lora-training"},{"title":"Wan2.2 Fine-Tuning: Tailoring an Advanced Video Generation Model on a Single GPU — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/finetuning-wan-part1/README.html"},{"title":"MimicPC - How to Train Wan2.1 LoRA with Diffusion-Pipe in 6 Steps","url":"https://www.mimicpc.com/learn/how-to-train-wan21-lora-with-diffusion-pipe"},{"title":"WAN Video Generation LoRA Training Guide","url":"https://www.trooper.ai/docs/wan-video-lora-training"},{"title":"Wan 2.2 T2V 14B LoRA Training with AI Toolkit | Text-to-Video","url":"https://www.runcomfy.com/trainer/ai-toolkit/wan-2-2-t2v-14b-lora-training"}]

I found several relevant results about Wan 2.1 LoRA fine-tuning with A40 training. Here's what I discovered:

## Training Time on A40 Hardware

The A40 48GB is a powerful GPU device that can be used for Wan 2.1 LoRA training. For specific training duration estimates, one example trained a LoRA for anime style using WAN2.1 (1.3B) with 14 images on an RTX 3090 with 24GB vRAM, and the whole training time took about 2.5 hours with total 3500 steps.

## Efficient Domain Transfer

LoRA modules integrated into the cross-attention layers of the Wan2.1 I2V-14B model enable efficient domain transfer within hours on a single GPU, which suggests that A40 training should be similarly efficient.

## Key Details About A40 LoRA Training

When using a powerful GPU device like the A40 48GB, it's possible to sample videos while running a training session, making it practical for monitoring training progress.

For video generation after fine-tuning, if you rented the A40 and trained on a dataset, it should take about 15–30 minutes to generate the first video with the default ComfyUI workflow settings.

The search results indicate that training times depend on dataset size, image resolution, number of epochs, and the model variant (1.3B vs 14B) being used.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7c2bd19-ae7e-4014-ae68-0ff601c1d04b",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "17deffca-32f0-4ac6-ab8a-7525a05ef2e9",
  "sourceToolAssistantUUID": "d7c2bd19-ae7e-4014-ae68-0ff601c1d04b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T12:11:05.075Z_

Good first pass. Now let me dig deeper into the GitHub repo for training details, fetch the Medium/apatero articles for specific numbers, and search more targeted queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17deffca-32f0-4ac6-ab8a-7525a05ef2e9",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats9ajXydVud49RLcLSU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7f2a469-34a7-402f-824b-2250e260dd36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CbhMtE79mjAaMWKUwbYdpu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3680,
      "cache_read_input_tokens": 10862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3680,
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

_source line 15 · 2026-05-10T12:11:06.989Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fec53vpqHbckNQTQUo2bdf`</summary>

```json
{
  "url": "https://github.com/TheDenk/wan2.2-controlnet",
  "prompt": "Extract all training details: GPU hardware, training duration in hours, number of steps, batch size, dataset size, learning rate, any compute-related numbers. Look for a Training section or README content about how to train and any reported results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7f2a469-34a7-402f-824b-2250e260dd36",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats9ajXydVud49RLcLSU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddcdd2fd-28ec-46da-902a-0f4e0faa3b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CbhMtE79mjAaMWKUwbYdpu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3680,
      "cache_read_input_tokens": 10862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3680,
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

_source line 16 · 2026-05-10T12:11:08.137Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DuG7Qef4xy6aD9L2SYavJV`</summary>

```json
{
  "url": "https://www.apatero.com/blog/wan-22-video-lora-training-time-complete-analysis-2025",
  "prompt": "Extract all specific training time numbers, GPU types, hours/minutes, dataset sizes, steps, and any hardware configurations mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddcdd2fd-28ec-46da-902a-0f4e0faa3b11",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats9ajXydVud49RLcLSU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c6d880c-2a9d-4608-81d2-262a9e6edecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CbhMtE79mjAaMWKUwbYdpu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3680,
      "cache_read_input_tokens": 10862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3680,
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

_source line 17 · 2026-05-10T12:11:08.513Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018AaPqiunWCvHu2EvhD8x5E`</summary>

```json
{
  "query": "WanVideo ControlNet training compute H100 GPU hours steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c6d880c-2a9d-4608-81d2-262a9e6edecc",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats9ajXydVud49RLcLSU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "252691a8-a264-4a30-9c35-e65f3f08a3b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CbhMtE79mjAaMWKUwbYdpu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3680,
      "cache_read_input_tokens": 10862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3680,
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

_source line 18 · 2026-05-10T12:11:09.058Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LneAGP4pWqa14z4UwuBePe`</summary>

```json
{
  "query": "video diffusion ControlNet training compute temporal attention overhead GPU hours estimate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "252691a8-a264-4a30-9c35-e65f3f08a3b9",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011Cats9ajXydVud49RLcLSU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92991732-f19b-44bf-82d6-0c660c55f7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CbhMtE79mjAaMWKUwbYdpu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3680,
      "cache_read_input_tokens": 10862,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 372,
          "cache_read_input_tokens": 10862,
          "cache_creation_input_tokens": 3680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3680,
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

_source line 19 · 2026-05-10T12:11:10.656Z_

<details><summary>↩ Tool result · `toolu_01Fec53vpqHbckNQTQUo2bdf`</summary>

```text
# Training Details Analysis

Based on my review of the provided GitHub repository content, **no training details are available in this document**.

The repository for "wan2.2-controlnet" contains:
- Inference code and examples
- Pre-trained model links
- Usage instructions for ComfyUI integration
- Example scripts for running the controlnet

However, there is **no training section, documentation about training procedures, or any computational metrics** such as:
- GPU hardware specifications
- Training duration
- Number of training steps
- Batch size
- Dataset size information
- Learning rate settings
- Other training-related compute numbers

The repository focuses exclusively on inference and deployment rather than detailing the training process. For training information, you would need to consult the original Wan2.2 project repository or documentation from Wan-AI.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddcdd2fd-28ec-46da-902a-0f4e0faa3b11",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "9966c281-7f39-4be4-91bc-45868dd01abb",
  "sourceToolAssistantUUID": "ddcdd2fd-28ec-46da-902a-0f4e0faa3b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T12:11:13.083Z_

<details><summary>↩ Tool result · `toolu_018AaPqiunWCvHu2EvhD8x5E`</summary>

```text
Web search results for query: "WanVideo ControlNet training compute H100 GPU hours steps"

Links: [{"title":"GitHub - deepbeepmeep/Wan2GP: A fast AI Video Generator for the GPU Poor. Supports Wan 2.1/2.2, Qwen Image, Hunyuan Video, LTX Video and Flux. · GitHub","url":"https://github.com/deepbeepmeep/Wan2GP"},{"title":"NVIDIA H100 Benchmarks for Large-Scale Training | CoreWeave","url":"https://www.coreweave.com/blog/nvidia-h100-gpu-benchmark-results-what-we-learned-from-large-scale-gpu-testing"},{"title":"GitHub - Wan-Video/Wan2.2: Wan: Open and Advanced Large-Scale Video Generative Models · GitHub","url":"https://github.com/Wan-Video/Wan2.2"},{"title":"Temporal In-Context Fine-Tuning with Temporal Reasoning for Versatile Control of Video Diffusion Models","url":"https://arxiv.org/html/2506.00996v2"},{"title":"How to Run Automatic1111 (Stable Diffusion Web UI) on Runpod","url":"https://www.runpod.io/articles/guides/stable-diffusion-a1111"},{"title":"Image-to-Video AI on GPU Cloud: Deploy LTX-Video, Wan 2.2 I2V, and Hunyuan Video Avatar (2026) | Spheron Blog","url":"https://www.spheron.network/blog/image-to-video-gpu-cloud-ltx-wan-hunyuan/"},{"title":"Training LLMs on H100 PCIe GPUs in the Cloud: Setup and Optimization","url":"https://www.runpod.io/articles/guides/training-llms-h100-pcle-gpus"},{"title":"Wan2.2 Video Generation ComfyUI Official Native Workflow Example - ComfyUI","url":"https://docs.comfy.org/tutorials/video/wan/wan2_2"},{"title":"GitHub - Wan-Video/Wan2.1: Wan: Open and Advanced Large-Scale Video Generative Models · GitHub","url":"https://github.com/Wan-Video/Wan2.1"},{"title":"Breaking MLPerf Training Records with NVIDIA H100 GPUs | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/breaking-mlperf-training-records-with-nvidia-h100-gpus/"}]

Based on the search results, I found some relevant information about ControlNet training on H100 GPUs in the context of video diffusion models:

For ControlNet training, researchers apply LoRA with rank 128, yielding approximately 150M trainable parameters, and requiring approximately 60GB of GPU memory on an NVIDIA H100 GPU.

However, the search results do not contain specific information about WanVideo ControlNet training compute requirements in terms of H100 GPU hours or training steps. The results discuss ControlNet training for CogVideoX models rather than Wan models specifically, and while they mention GPU memory requirements, they don't provide details about the total computational hours or number of training steps required.

If you're looking for more specific information about WanVideo ControlNet training specifications, you may need to consult the official Wan repository documentation or research papers directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "252691a8-a264-4a30-9c35-e65f3f08a3b9",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "a8f922e4-7ac2-4778-878c-abda058e1588",
  "sourceToolAssistantUUID": "252691a8-a264-4a30-9c35-e65f3f08a3b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T12:11:15.332Z_

<details><summary>↩ Tool result · `toolu_01DuG7Qef4xy6aD9L2SYavJV`</summary>

```text
# WAN 2.2 Video LoRA Training Time Data Extraction

## Quick Reference Training Times

**RTX 4090 (24GB):**
- 150 samples, 512x512: 3.8-4.5 hours
- 200 samples, 512x512: 4.5-5.5 hours
- 300 samples, 512x512: 6.2-7.5 hours
- 400 samples, 512x512: 8.0-9.8 hours
- 200 samples, 768x768: 9.5-11.2 hours

**RTX 3090 (24GB):**
- 150 samples, 512x512: 5.5-6.8 hours
- 200 samples, 512x512: 6.8-8.5 hours
- 300 samples, 512x512: 9.5-11.8 hours
- 400 samples, 512x512: 12.2-15.0 hours

**A100 (40GB with batch size 2):**
- 200 samples, 512x512: 2.8-3.5 hours
- 300 samples, 512x512: 3.9-4.8 hours
- 400 samples, 512x512: 5.0-6.2 hours
- 200 samples, 768x768: 4.8-5.9 hours

## Dataset Size Impact

Each 100 additional samples adds approximately 1.5-2.5 hours on RTX 4090 at 512x512 resolution.

## Resolution Scaling

768x768 training takes 2.2x longer than 512x512; 640x640 falls between at 0.64x baseline speed.

## Key Performance Metrics

- Time per step (RTX 4090, 512x512, dim 64): 4.2-4.8 seconds
- A100 with batch size 2 provides 1.6-1.8x speedup versus batch size 1
- FP16 optimization: 1.4-1.6x faster
- XFormers enabled: 1.3-1.5x faster
- Combined optimizations: 1.5-1.8x faster
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c6d880c-2a9d-4608-81d2-262a9e6edecc",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "0bbcd462-99b7-46f2-9011-493f819e5768",
  "sourceToolAssistantUUID": "1c6d880c-2a9d-4608-81d2-262a9e6edecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T12:11:16.325Z_

<details><summary>↩ Tool result · `toolu_01LneAGP4pWqa14z4UwuBePe`</summary>

```text
Web search results for query: "video diffusion ControlNet training compute temporal attention overhead GPU hours estimate"

Links: [{"title":"GitHub - CiaraStrawberry/svd-temporal-controlnet","url":"https://github.com/CiaraStrawberry/svd-temporal-controlnet"},{"title":"CiaraRowles/temporal-controlnet-depth-svd-v1 · Hugging Face","url":"https://huggingface.co/CiaraRowles/temporal-controlnet-depth-svd-v1"},{"title":"Katz: Efficient Workflow Serving for Diffusion Models with ...","url":"https://www.usenix.org/system/files/atc25-li-suyi-katz.pdf"},{"title":"Real-Time Video Generation with Pyramid Attention Broadcast","url":"https://oahzxl.github.io/PAB/"},{"title":"Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention","url":"https://arxiv.org/html/2602.01801"},{"title":"EquiVDM","url":"https://research.nvidia.com/labs/genair/equivdm/"},{"title":"VersVideo: Leveraging Enhanced Temporal Diffusion Models for Versatile Video Generation | OpenReview","url":"https://openreview.net/forum?id=K9sVJ17zvB"},{"title":"Fast Video Generation with Sliding Tile Attention","url":"https://arxiv.org/html/2502.04507v2"},{"title":"Learning Temporally Consistent Video Depth from Video Diffusion Priors","url":"https://arxiv.org/html/2406.01493v2"},{"title":"ControlNet · Hugging Face","url":"https://huggingface.co/docs/diffusers/training/controlnet"}]

I've performed a web search for your query about video diffusion ControlNet training compute and temporal attention overhead. Here's what the search results reveal:

## Key Findings:

**ControlNet Computational Overhead:**
Augmenting a base diffusion model with one ControlNet increases serving latency by 1.6× (up from 2.9 seconds to 4.5 seconds), indicating significant computational costs associated with ControlNets.

**Temporal Attention as a Bottleneck:**
3D attention mechanisms introduce significant computational overhead due to quadratic complexity, making training and inference prohibitively slow as video resolutions and durations increase. In practical terms, even with FlashAttention 3 and a high-end H100 GPU, HunyuanVideo still requires 16 minutes to generate a 5-second 720p video.

**Training Cost Examples:**
One video depth model training takes about 1.5 days on a cluster of 8 Nvidia Tesla A100-80GB GPUs, providing a concrete example of video diffusion training costs.

**Optimization Approaches:**
One method achieves up to a 35% speedup with negligible quality loss through pyramid attention broadcast, while broadcasting temporal attention eliminates communications and results in a significant reduction in communication overhead by over 50%.

The search results indicate that temporal attention is indeed a major computational bottleneck in video diffusion models, though the specific GPU hours estimate for ControlNet training varies depending on model architecture, dataset size, and optimization techniques employed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92991732-f19b-44bf-82d6-0c660c55f7a2",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "2329ed3a-54e9-42ca-9a18-13d1f87a81f2",
  "sourceToolAssistantUUID": "92991732-f19b-44bf-82d6-0c660c55f7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T12:11:20.127Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B6E3kYV9u5jTYSWNu8FPWr`</summary>

```json
{
  "url": "https://github.com/TheDenk/wan2.1-dilated-controlnet",
  "prompt": "Extract all training details: GPU hardware, training duration in hours/days, number of steps, batch size, dataset size, learning rate, any compute numbers. Look for a Training section or any mention of how long training took."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2329ed3a-54e9-42ca-9a18-13d1f87a81f2",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsAbAMYrDiQEvVKQyRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13e42935-b356-4027-bd62-4321d4c27aeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RVnfBGjiZZR4gKZJQwQxh1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 14542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T12:11:22.431Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F5xTkNHruFvD9T9vXmoCky`</summary>

```json
{
  "url": "https://learn2train.medium.com/fine-tuning-wan-2-1-with-a-curated-dataset-step-by-step-guide-a6f0b334ab79",
  "prompt": "Extract all specific training time numbers, GPU types, hours/minutes, dataset sizes, steps, batch sizes, and any hardware configurations mentioned. Also look for ControlNet-specific training information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13e42935-b356-4027-bd62-4321d4c27aeb",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsAbAMYrDiQEvVKQyRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3238318b-cef6-48e9-939f-eaa41b6e187d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RVnfBGjiZZR4gKZJQwQxh1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 14542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T12:11:22.683Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V4b8ndLLyYnUAzbUfxtoSs`</summary>

```json
{
  "query": "TheDenk wan controlnet training details README steps epochs dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3238318b-cef6-48e9-939f-eaa41b6e187d",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsAbAMYrDiQEvVKQyRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4efb3624-1cdf-43c9-9f1c-b256165cf78d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RVnfBGjiZZR4gKZJQwQxh1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 14542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T12:11:23.574Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NR6nhHf947Wfb37wbjrUH6`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.27364v1",
  "prompt": "Extract all training details: GPU hardware, training duration, number of steps, batch size, dataset size, learning rate, and any compute estimates. This is about LoRA fine-tuning of Wan2.1 I2V model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4efb3624-1cdf-43c9-9f1c-b256165cf78d",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsAbAMYrDiQEvVKQyRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6530e5fe-9d41-45b8-810f-4d8553d76cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RVnfBGjiZZR4gKZJQwQxh1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 14542,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 433,
          "cache_read_input_tokens": 14542,
          "cache_creation_input_tokens": 2942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2942,
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

_source line 27 · 2026-05-10T12:11:25.418Z_

<details><summary>↩ Tool result · `toolu_01B6E3kYV9u5jTYSWNu8FPWr`</summary>

```text
# Training Details for Wan2.1 Dilated ControlNet

Based on the provided documentation, here are the available training specifications:

**Hardware Requirements:**
- "Wan 1.3B model requires `18 GB VRAM` with `batch_size=1`"
- GPU memory needs depend on transformer block count (default is 8 via `controlnet_transformer_num_layers`)

**Dataset:**
- OpenVid-1M dataset was used as the foundation
- Training data sourced from CSV files available on Hugging Face

**Training Configuration Parameters Mentioned:**
- `sample_stride`: 2
- `width`: 832, `height`: 480
- `sample_n_frames`: 81 frames

**Notable Absence:**
The documentation does not provide specific information regarding:
- Total training duration (hours/days)
- Number of training steps
- Learning rate values
- Complete dataset size metrics
- Other compute specifications

The repository focuses more on inference usage and dataset preparation procedures than detailed training metrics. For comprehensive training specifications, you would need to consult the training configuration files (`accelerate_config_machine_single.yaml` and `train_controlnet.sh`) referenced in the setup instructions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13e42935-b356-4027-bd62-4321d4c27aeb",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "47747a01-53b6-445f-ad71-12af85763209",
  "sourceToolAssistantUUID": "13e42935-b356-4027-bd62-4321d4c27aeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T12:11:27.749Z_

<details><summary>↩ Tool result · `toolu_01F5xTkNHruFvD9T9vXmoCky`</summary>

```text
# Training Specifications from Wan 2.1 Fine-tuning Guide

## Hardware Configuration
- **GPU Type**: A40 (48GB VRAM minimum)
- **Storage**: 150GB or more
- **Cost**: "$0.44/hr" on RunPod (as of March 2025)

## Training Timeline & Dataset
- **Total project duration**: 3-6 hours (setup, training, and inference combined)
- **Estimated cost**: $2-3 for full workflow
- **Dataset size**: ~100 images with corresponding text captions
- **Training epochs**: Configurable (example shown: modified from 1000 to 20 epochs)
- **Checkpoint frequency**: "save_every_n_epochs = 2" (example configuration)

## Key Metrics
- **Model size**: Wan 2.1 with 14 billion parameters (larger than 1.3B variant)
- **Video generation time**: "15–30 minutes to generate the first video" with default settings on A40
- **Subsequent generations**: Significantly faster after initial model loading

## Important Note
The guide focuses on **LoRA fine-tuning** rather than full model training. No ControlNet-specific training information appears in this document—it covers Wan 2.1 text-to-video and image-to-video adaptation using diffusion-pipe trainer with ComfyUI for inference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3238318b-cef6-48e9-939f-eaa41b6e187d",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "96424c59-85fa-41cd-944f-cc116a05ea5e",
  "sourceToolAssistantUUID": "3238318b-cef6-48e9-939f-eaa41b6e187d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T12:11:29.040Z_

<details><summary>↩ Tool result · `toolu_01NR6nhHf947Wfb37wbjrUH6`</summary>

```text
# LoRA Fine-Tuning Training Details for Wan2.1 I2V

## Hardware & Duration
- **GPU Options**: Single A100-40GB (Google Colab Pro) or dual A100-80GB (RunPod with FSDP)
- **Training Time**: 3 hours 12 minutes (single GPU) or 1 hour 36 minutes (dual GPU setup)
- **Peak Memory**: Under 46 GB per GPU in dual-GPU configuration

## Training Configuration
- **Steps**: 4,000 total steps with early stopping at validation plateau
- **Batch Size**: 11 videos × 4 gradient accumulation = 22 effective batch size
- **Learning Rate**: "3×10⁻⁵" with cosine schedule and 5% warm-up
- **Optimizer**: AdamW (β₁=0.9, β₂=0.999, weight decay=0.01)
- **Precision**: bfloat16 (bf16)

## Dataset Specifications
- **Size**: Approximately 25,000 frame-caption pairs (~16 minutes total footage)
- **Source Material**: ~40 short clips (2-5 seconds each) from El Turco TV production
- **Frame Format**: 1024×576 pixels at 24 FPS, letterboxed to maintain 16:9 aspect ratio
- **Training Windows**: 33-frame temporal segments (~1.4 seconds)

## Key Technical Details
- **LoRA Rank/α**: 8/16 for "lightweight, stable updates"
- **Parameter Modification**: Less than 1% of model parameters adjusted
- **Activation Checkpointing**: Enabled to reduce VRAM footprint
- **Framework**: PyTorch + DeepSpeed with FSDP (Fully Sharded Data Parallelism)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6530e5fe-9d41-45b8-810f-4d8553d76cff",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "4954794d-ee96-4521-9ef7-fcbdabcf2cac",
  "sourceToolAssistantUUID": "6530e5fe-9d41-45b8-810f-4d8553d76cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T12:11:29.503Z_

<details><summary>↩ Tool result · `toolu_01V4b8ndLLyYnUAzbUfxtoSs`</summary>

```text
Web search results for query: "TheDenk wan controlnet training details README steps epochs dataset"

Links: [{"title":"README.md · TheDenk/wan2.1-t2v-14b-controlnet-depth-v1 at main","url":"https://huggingface.co/TheDenk/wan2.1-t2v-14b-controlnet-depth-v1/blob/main/README.md"},{"title":"wan2.2-controlnet/README.md at main · TheDenk/wan2.2-controlnet","url":"https://github.com/TheDenk/wan2.2-controlnet/blob/main/README.md"},{"title":"README.md · TheDenk/wan2.2-t2v-a14b-controlnet-depth-v1 at main","url":"https://huggingface.co/TheDenk/wan2.2-t2v-a14b-controlnet-depth-v1/blob/main/README.md"},{"title":"GitHub - TheDenk/wan2.1-dilated-controlnet: Controlnet module for Wan2.1","url":"https://github.com/TheDenk/wan2.1-dilated-controlnet"},{"title":"GitHub - TheDenk/wan2.2-controlnet: Controlnet module for Wan2.2 · GitHub","url":"https://github.com/TheDenk/wan2.2-controlnet"},{"title":"Train your ControlNet with diffusers","url":"https://huggingface.co/blog/train-your-controlnet"},{"title":"README.md · TheDenk/wan2.2-ti2v-5b-controlnet-hed-v1 at main","url":"https://huggingface.co/TheDenk/wan2.2-ti2v-5b-controlnet-hed-v1/blame/main/README.md"},{"title":"TheDenk/wan2.1-t2v-14b-controlnet-depth-v1 · Hugging Face","url":"https://huggingface.co/TheDenk/wan2.1-t2v-14b-controlnet-depth-v1"},{"title":"ControlNet · Hugging Face","url":"https://huggingface.co/docs/diffusers/training/controlnet"},{"title":"GitHub - shalfun/WanControl: Wan2.1 with Controlnet · GitHub","url":"https://github.com/shalfun/WanControl"}]

Based on the search results, I found information about TheDenk's ControlNet training for Wan video generation models. Here's what I found:

## Training Overview

The OpenVid-1M dataset was taken as the base variant for training TheDenk's ControlNet models.

## Training Steps

The training process involves several key steps:

1. **Extract text embeddings**: Text embeddings are extracted from CSV files using a command that specifies the CSV path, output directory, base model path, device, and data type.

2. **Encode video into VAE latents**: Videos are encoded into VAE latents by specifying the input video directory, output latents directory, base model path, sample stride, dimensions, number of frames, seed, device, and dtype.

3. **Prepare and configure training**: The training process requires setting output_dir, latents_dir, text_embeds_dir and controlnet_video_dir parameters.

## Training Parameters

For the actual training setup, a related implementation shows training parameters including steps_per_epoch of 500, max_epochs of 1000, learning_rate of 4e-5, and control_layers of 15. With control_layers set to 15, the overall memory usage is approximately 26G, and can be reduced to approximately 22G and 19G when set to 10 and 5 respectively.

The README files in the search results focus primarily on inference usage rather than detailed training documentation, so some specific training hyperparameters like exact epoch numbers may not be fully documented in the public README.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4efb3624-1cdf-43c9-9f1c-b256165cf78d",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "8a851f95-18b9-41ec-835c-984a7f75a2da",
  "sourceToolAssistantUUID": "4efb3624-1cdf-43c9-9f1c-b256165cf78d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T12:11:32.229Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013maXbsAqJQogznnF5ZnF1k`</summary>

```json
{
  "url": "https://huggingface.co/TheDenk/wan2.1-t2v-14b-controlnet-depth-v1/blob/main/README.md",
  "prompt": "Extract ALL training details mentioned: GPU hardware, number of GPUs, training duration, hours, steps, epochs, batch size, dataset size, learning rate, any compute numbers. Focus on anything quantitative about training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a851f95-18b9-41ec-835c-984a7f75a2da",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsBZRxRkhQ4gVMWUAVE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4300acbc-ebfd-4f81-8ee7-d732dbb4a9a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017gofo229jiJkChyRbVtxZ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 463,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 17484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2090,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-10T12:11:32.994Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016rs3umxirtpbf78jm5S3uG`</summary>

```json
{
  "url": "https://github.com/TheDenk/wan2.2-controlnet/blob/main/README.md",
  "prompt": "Extract ALL training details mentioned: GPU hardware, number of GPUs, training duration, hours, steps, epochs, batch size, dataset size, learning rate, any compute numbers. Focus on anything quantitative about training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4300acbc-ebfd-4f81-8ee7-d732dbb4a9a6",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsBZRxRkhQ4gVMWUAVE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac755ed7-102a-4d44-bb2f-11db876f88d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017gofo229jiJkChyRbVtxZ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 463,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 17484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2090,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T12:11:33.754Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EYZMUsRM5U8eRSg95YoTqy`</summary>

```json
{
  "query": "\"wan2.1\" OR \"wan 2.1\" controlnet training \"hours\" OR \"days\" OR \"steps\" GPU A100 H100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac755ed7-102a-4d44-bb2f-11db876f88d9",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsBZRxRkhQ4gVMWUAVE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee4ceca4-d028-49e6-8739-450913e2665a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017gofo229jiJkChyRbVtxZ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 463,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 17484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2090,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T12:11:34.366Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TekLzKHoPsq8G91ExwVJj1`</summary>

```json
{
  "url": "https://github.com/shalfun/WanControl",
  "prompt": "Extract all training details: GPU hardware, number of GPUs, training duration in hours/days, steps, dataset size, any compute numbers. Look for any section about training configuration or training time."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee4ceca4-d028-49e6-8739-450913e2665a",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsBZRxRkhQ4gVMWUAVE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70000512-4197-4556-a8c6-d7a1379978e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017gofo229jiJkChyRbVtxZ2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 463,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 17484,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2090
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 463,
          "output_tokens": 443,
          "cache_read_input_tokens": 17484,
          "cache_creation_input_tokens": 2090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2090,
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

_source line 35 · 2026-05-10T12:11:35.119Z_

<details><summary>↩ Tool result · `toolu_013maXbsAqJQogznnF5ZnF1k`</summary>

```text
# Training Details

Based on the provided web page content, **no training details are mentioned**. 

The README.md file contains:
- Model description (Dilated ControlNet for Wan2.1)
- Installation instructions
- Inference examples (CLI, Gradio, and detailed inference parameters)
- Acknowledgements and citations
- Contact information

However, it does **not include any quantitative training information** such as:
- GPU hardware specifications
- Number of GPUs used
- Training duration or hours
- Training steps or epochs
- Batch size
- Dataset size
- Learning rate
- Other compute metrics

The document focuses exclusively on how to use and run inference with the pre-trained model rather than documenting its training process.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4300acbc-ebfd-4f81-8ee7-d732dbb4a9a6",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "0d2c13fb-2242-4a75-86da-5dd6d5acd0e3",
  "sourceToolAssistantUUID": "4300acbc-ebfd-4f81-8ee7-d732dbb4a9a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T12:11:36.960Z_

<details><summary>↩ Tool result · `toolu_016rs3umxirtpbf78jm5S3uG`</summary>

```text
# Training Details Analysis

Based on my review of the provided README.md content, **no training details are mentioned**. 

The document contains:
- Installation and inference instructions
- Model links and available controlnet variants
- Code examples for running inference
- References to the base Wan2.2 model

However, it does not include any quantitative information about training such as GPU hardware, training duration, batch sizes, learning rates, dataset specifications, or computational requirements.

The only training-related reference is: "Original code and models Wan2.2" with a link to the source repository, suggesting readers would need to consult the primary Wan2.2 project for such details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac755ed7-102a-4d44-bb2f-11db876f88d9",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "302bcba0-6041-47d6-9e5a-d15be257a0c5",
  "sourceToolAssistantUUID": "ac755ed7-102a-4d44-bb2f-11db876f88d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T12:11:37.848Z_

<details><summary>↩ Tool result · `toolu_01TekLzKHoPsq8G91ExwVJj1`</summary>

```text
# Training Details from WanControl GitHub Repository

Based on the provided content, here are the documented training specifications:

## GPU Requirements
- **Memory Usage**: Approximately 26GB with `control_layers=15` (default)
- **Reduced Memory Options**: ~22GB with `control_layers=10`, ~19GB with `control_layers=5`

## Training Configuration Parameters
The documentation specifies these hyperparameters:
- Learning rate: 4e-5
- Maximum epochs: 1000
- Steps per epoch: 500
- Gradient accumulation batches: 1
- Dataloader workers: 8

## Notable Limitation
The repository does not specify the number of GPUs used, actual training duration in hours or days, or total dataset size. The training details focus on memory consumption rather than computational time or hardware quantity.

The documentation emphasizes that "most parameters being frozen" enables the relatively modest 26GB footprint despite training a large video generation model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70000512-4197-4556-a8c6-d7a1379978e0",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "abb52e04-6144-4979-b14d-7158618ab55c",
  "sourceToolAssistantUUID": "70000512-4197-4556-a8c6-d7a1379978e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T12:11:39.306Z_

<details><summary>↩ Tool result · `toolu_01EYZMUsRM5U8eRSg95YoTqy`</summary>

```text
Web search results for query: ""wan2.1" OR "wan 2.1" controlnet training "hours" OR "days" OR "steps" GPU A100 H100"

Links: [{"title":"GitHub - deepbeepmeep/Wan2GP: A fast AI Video Generator for the GPU Poor. Supports Wan 2.1/2.2, Qwen Image, Hunyuan Video, LTX Video and Flux. · GitHub","url":"https://github.com/deepbeepmeep/Wan2GP"},{"title":"Wan2.1 Performance Testing Across GPUs","url":"https://www.instasd.com/post/wan2-1-performance-testing-across-gpus"},{"title":"GitHub - Wan-Video/Wan2.1: Wan: Open and Advanced Large-Scale Video Generative Models · GitHub","url":"https://github.com/Wan-Video/Wan2.1"},{"title":"Wan2.2 : AI Video Generation in Budget GPU | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/wan2-2-ai-video-generation-in-budget-gpu-a314238b2a54"},{"title":"WAN Video Generation LoRA Training Guide","url":"https://www.trooper.ai/docs/wan-video-lora-training"},{"title":"Wan2.2 Video Generation ComfyUI Official Native Workflow Example - ComfyUI","url":"https://docs.comfy.org/tutorials/video/wan/wan2_2"},{"title":"Fine-tuning Wan 2.1 With a Curated Dataset on the GPU Cloud (Step-by-Step Guide) | by learn2train.org | Medium","url":"https://medium.com/@learn2train/fine-tuning-wan-2-1-with-a-curated-dataset-step-by-step-guide-a6f0b334ab79"},{"title":"Wan2.1/generate.py at main · Wan-Video/Wan2.1","url":"https://github.com/Wan-Video/Wan2.1/blob/main/README.md"},{"title":"Training benchmarks · Issue #512 · Wan-Video/Wan2.1","url":"https://github.com/Wan-Video/Wan2.1/issues/512"},{"title":"GitHub - Wan-Video/Wan2.2: Wan: Open and Advanced Large-Scale Video Generative Models · GitHub","url":"https://github.com/Wan-Video/Wan2.2"}]

I've performed the web search for "wan2.1" OR "wan 2.1" controlnet training with the specified parameters. However, the search results do not contain specific information about ControlNet training for Wan 2.1 with training duration metrics (hours, days, or steps) on A100 or H100 GPUs.

The results found do include:

- Performance benchmarks showing H100 achieves 85 seconds for 480P and 284 seconds for 720P video generation, and A100 handled 720P in 523 seconds, but these are for inference, not training.

- References to LoRA training on Wan2.2 using multiple GPUs (e.g., 2× A100 40GB), but without specific training duration information.

- A GitHub issue requesting training benchmarks that appears unanswered.

The search results focus primarily on inference performance and LoRA fine-tuning rather than ControlNet-specific training benchmarks. For detailed ControlNet training time information on these GPU types, you may need to check:
- The official Wan-Video GitHub repositories
- Community forums or Discord channels
- GPU cloud provider documentation that offers Wan 2.1 training services


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee4ceca4-d028-49e6-8739-450913e2665a",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "25abe117-d99c-4872-b9a1-45a4ed8b372f",
  "sourceToolAssistantUUID": "ee4ceca4-d028-49e6-8739-450913e2665a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-10T12:11:42.186Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WC7rM4dJVgJHDvRWHCCuUe`</summary>

```json
{
  "url": "https://github.com/Wan-Video/Wan2.1/issues/512",
  "prompt": "Extract all training benchmark data from this issue thread: GPU types, training hours, steps, dataset sizes, batch sizes, and any compute numbers reported by community members."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25abe117-d99c-4872-b9a1-45a4ed8b372f",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsCHNb9Vwu7WV4JYtde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e45b0a65-83a2-4218-bee5-bc700cb1bce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LbkNrT6nhqwMwSaTNDx4aa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 246,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 19574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2213,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-10T12:11:42.569Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XYKakSaRdbGgjSW66ct7ug`</summary>

```json
{
  "query": "CogVideoX ControlNet training compute GPU hours H100 steps dataset size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e45b0a65-83a2-4218-bee5-bc700cb1bce9",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsCHNb9Vwu7WV4JYtde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8a3c722-29c1-45c7-bd1c-93b206ea77be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LbkNrT6nhqwMwSaTNDx4aa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 246,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 19574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2213,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-10T12:11:42.954Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DWfnmEWkcHfmkyRXchtPy4`</summary>

```json
{
  "query": "Wan2.2 fine-tuning ROCm AMD training time hours steps configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8a3c722-29c1-45c7-bd1c-93b206ea77be",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsCHNb9Vwu7WV4JYtde",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f4c452e-a357-438a-817a-376fb580f3b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LbkNrT6nhqwMwSaTNDx4aa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 246,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 19574,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2213
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 246,
          "output_tokens": 224,
          "cache_read_input_tokens": 19574,
          "cache_creation_input_tokens": 2213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2213,
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

_source line 42 · 2026-05-10T12:11:45.759Z_

<details><summary>↩ Tool result · `toolu_01WC7rM4dJVgJHDvRWHCCuUe`</summary>

```text
# Training Benchmark Data Extraction

Based on the provided GitHub issue content, **no training benchmark data is actually reported**. 

The issue is a *request* for information, not a disclosure of benchmarks. The contributor Juan asks the Wan 2.1 team to share:

- "Accelerator type and count (e.g., H100, A100 x 1024)"
- "Global batch size"
- "Training step time / throughput"

However, no actual values, specifications, or responses containing benchmark data appear in this thread excerpt. The issue remains open with no assigned responses or provided metrics from the development team.

To obtain the actual training benchmarks, one would need to review the complete issue thread including any team responses, or consult the original Wan 2.1 research paper directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e45b0a65-83a2-4218-bee5-bc700cb1bce9",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "8afb3db5-343a-4c06-a27a-e832fae340ad",
  "sourceToolAssistantUUID": "e45b0a65-83a2-4218-bee5-bc700cb1bce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T12:11:48.398Z_

<details><summary>↩ Tool result · `toolu_01XYKakSaRdbGgjSW66ct7ug`</summary>

```text
Web search results for query: "CogVideoX ControlNet training compute GPU hours H100 steps dataset size"

Links: [{"title":"GitHub - zai-org/CogVideo: text and image to video generation: CogVideoX (2024) and CogVideo (ICLR 2023) · GitHub","url":"https://github.com/zai-org/CogVideo"},{"title":"CogVideoX · Hugging Face","url":"https://huggingface.co/docs/diffusers/en/training/cogvideox"},{"title":"How to train ControlNet to control CogVideoX 1.5 I2V model · Issue #108 · aigc-apps/VideoX-Fun","url":"https://github.com/aigc-apps/VideoX-Fun/issues/108"},{"title":"GitHub - TheDenk/cogvideox-controlnet: Simple Controlnet module for CogvideoX model.","url":"https://github.com/TheDenk/cogvideox-controlnet"},{"title":"Temporal In-Context Fine-Tuning with Temporal Reasoning for Versatile Control of Video Diffusion Models","url":"https://arxiv.org/html/2506.00996v2"},{"title":"CogVideo/README.md at main · zai-org/CogVideo","url":"https://github.com/zai-org/CogVideo/blob/main/README.md"},{"title":"cuuupid/cogvideox-5b | Readme and Docs","url":"https://replicate.com/cuuupid/cogvideox-5b/readme"},{"title":"zai-org/CogVideoX-5b · EDITED: No H100 needed, very easy model to run across all chips.","url":"https://huggingface.co/zai-org/CogVideoX-5b/discussions/8"},{"title":"GitHub - Alyson0828/CogVideoX: text and image to video generation: CogVideoX (2024) and CogVideo (ICLR 2023)","url":"https://github.com/Alyson0828/CogVideoX"},{"title":"cogvideox-controlnet/cogvideo_controlnet.py at main · TheDenk/cogvideox-controlnet","url":"https://github.com/TheDenk/cogvideox-controlnet/blob/main/cogvideo_controlnet.py"}]

Based on the search results, here's information about CogVideoX ControlNet training compute requirements:

## GPU Memory Requirements

For ControlNet training with LoRA (rank), approximately 150M trainable parameters are required, needing approximately 60GB of GPU memory when using an H100 GPU. All models were fine-tuned using NVIDIA H100 GPUs.

## Training Configuration

In one research implementation, models were fine-tuned using LoRA (rank 128) with 20 training samples over 6,000 steps, a batch size of 2, and a single NVIDIA H100 80GB GPU.

## Hardware Details

For inference, the 2B model requires 48 GB VRAM (such as A6000) and 80 GB for the 5B model, though the exact requirements depend on the specific configuration used.

## Additional Notes

The search results show that CogVideoX ControlNet exists as a simple ControlNet module code that includes the CogVideoX model, but specific details about original training compute hours, full dataset sizes, and other foundational training metrics from the official paper are not available in these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8a3c722-29c1-45c7-bd1c-93b206ea77be",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "bc72eaeb-b85a-4b00-9e29-55e7d7ed6aa1",
  "sourceToolAssistantUUID": "e8a3c722-29c1-45c7-bd1c-93b206ea77be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T12:11:50.285Z_

<details><summary>↩ Tool result · `toolu_01DWfnmEWkcHfmkyRXchtPy4`</summary>

```text
Web search results for query: "Wan2.2 fine-tuning ROCm AMD training time hours steps configuration"

Links: [{"title":"Wan2.2 Fine-Tuning: Tailoring an Advanced Video Generation Model on a Single GPU — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/finetuning-wan-part1/README.html"},{"title":"Accelerating Audio-Driven Video Generation: WAN2.2-S2V on AMD ROCm — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/audio-driven-videogen/README.html"},{"title":"Wan2.2 Fine-Tuning: Tailoring an Advanced Video Generation Model on a Single GPU — ROCm Blogs · ROCm/rocm-blogs · Discussion #109","url":"https://github.com/ROCm/rocm-blogs/discussions/109"},{"title":"Wan-AI/Wan2.1-T2V-1.3B · AMD support","url":"https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B/discussions/14"},{"title":"Running ComfyUI on AMD Instinct — ROCm Blogs","url":"https://rocm.blogs.amd.com/software-tools-optimization/comfyui-on-amd/README.html"},{"title":"Review Generative AI Wan 2.2 T2V 14B Model - Ojambo","url":"https://www.ojambo.com/review-generative-ai-wan-2-2-t2v-14b-model"},{"title":"Using Reinforcement Learning to Fix Text in AI-Generated Videos — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/wan-flow-grpo/README.html"},{"title":"Fine-tuning Wan 2.1 With a Curated Dataset on the GPU Cloud (Step-by-Step Guide) | by learn2train.org | Medium","url":"https://learn2train.medium.com/fine-tuning-wan-2-1-with-a-curated-dataset-step-by-step-guide-a6f0b334ab79"},{"title":"Fine-Tuning Wan 2.2 — AMD Enterprise AI","url":"https://enterprise-ai.docs.amd.com/en/latest/ai-workloads-manifests/media-finetune-wan/helm/README.html"},{"title":"Use ROCm for fine-tuning LLMs — ROCm Documentation","url":"https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/fine-tuning/index.html"}]

Based on the search results, here's what I found about Wan2.2 fine-tuning on ROCm AMD hardware:

## Fine-Tuning Configuration

The Wan2.2 5B model was fine-tuned with LoRA for 10 epochs, repeating the dataset 10 times, which was found to be sufficient to produce desired results. The 14B parameter model was likewise fine-tuned for 10 epochs and 10 repeats on the dataset.

## Training Method

LoRA (Low-Rank Adaptation), a parameter-efficient fine-tuning method, significantly reduces trainable parameters by freezing pre-trained model weights and injecting small trainable rank-decomposition matrices, allowing fine-tuning of Wan2.2 on a single GPU. The DiffSynth framework was used for diffusion-based video generation with seamless LoRA fine-tuning integration.

## Hardware & Environment

Inference was performed using the PyTorch for ROCm training Docker (rocm/pytorch-training:v25.6), and fine-tuning of Wan2.2 is done on a single AMD Instinct MI300X GPU with ROCm and DiffSynth.

## Training Considerations

When using other datasets, you may experiment with the number of epochs and dataset repeats to find the best fine-tuning results. For the 14B model, both low and high noise models were trained, with training benchmarks specifically from low noise model training.

The search results don't include specific training time in hours or detailed step configurations, but the blog references provide access to the complete training scripts on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f4c452e-a357-438a-817a-376fb580f3b1",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "c07b2b3c-3e40-4807-ae20-62c1254fbf4e",
  "sourceToolAssistantUUID": "9f4c452e-a357-438a-817a-376fb580f3b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-10T12:11:57.662Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Hzwe6DQQAS89YE17yUh5kQ`</summary>

```json
{
  "url": "https://rocm.blogs.amd.com/artificial-intelligence/finetuning-wan-part1/README.html",
  "prompt": "Extract ALL training details: GPU hardware type, number of GPUs, training duration in hours/minutes, number of steps, epochs, batch size, dataset size (number of videos/images), learning rate, any throughput numbers (steps/second, samples/second). This is a Wan2.2 fine-tuning article on AMD ROCm."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c07b2b3c-3e40-4807-ae20-62c1254fbf4e",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsD6HckDLvX7VVogWHU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9854eae-9034-44f4-9e3c-adca873370bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011nQNRdFQW7TzbrhFMnKeAv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 21787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-10T12:11:58.458Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QRX6tPWXXj2f1WAhz7GhGK`</summary>

```json
{
  "url": "https://github.com/TheDenk/cogvideox-controlnet",
  "prompt": "Look for any training details: GPU hardware, training duration, steps, epochs, dataset size, learning rate, batch size. Also look for any comparison to how this compares to non-ControlNet training in terms of compute overhead."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9854eae-9034-44f4-9e3c-adca873370bd",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsD6HckDLvX7VVogWHU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a33475fb-82ae-4160-bb08-df929dd868f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011nQNRdFQW7TzbrhFMnKeAv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 21787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-10T12:12:00.093Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0129oboZnugpJckahFiiDjEh`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.00996v2",
  "prompt": "This is about temporal in-context fine-tuning for video diffusion models. Extract all training details: GPU hardware, training duration, compute hours, steps, dataset size, batch size. Also look for any discussion of ControlNet training overhead compared to base model training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a33475fb-82ae-4160-bb08-df929dd868f5",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsD6HckDLvX7VVogWHU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "538a7810-2513-4a49-9d65-1f85921513b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011nQNRdFQW7TzbrhFMnKeAv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 21787,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2759
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 409,
          "cache_read_input_tokens": 21787,
          "cache_creation_input_tokens": 2759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2759,
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

_source line 48 · 2026-05-10T12:12:02.666Z_

<details><summary>↩ Tool result · `toolu_01Hzwe6DQQAS89YE17yUh5kQ`</summary>

```text
# Wan2.2 Fine-Tuning Training Details

## Hardware
- **GPU Type**: AMD Instinct MI300X
- **Number of GPUs**: 1 (single GPU setup demonstrated)
- **VRAM**: 192 GB total available; 31.34 GB allocated for 5B LoRA training

## Training Configuration
- **Model**: Wan2.2-TI2V-5B
- **Epochs**: 5 (primary example); 10 (for comparative results)
- **Dataset Repeats**: 10
- **Learning Rate**: "1e-5"
- **Batch Size**: Not specified in article
- **Input Dimensions**: 480 height × 832 width, 81 frames

## Dataset
- **Source**: Disney-VideoGeneration-Dataset (Steamboat Willie)
- **Dataset Size**: Exact video count not stated
- **Video Length**: 6 seconds at 30 fps (matching training data)

## Performance Metrics
The article does not provide specific training duration, steps per second, or throughput measurements. It focuses on demonstrating feasibility rather than performance benchmarks.

## Key Finding
"LoRA...significantly reduces the number of trainable parameters by freezing the pre-trained model weights and injecting small, trainable rank-decomposition matrices," enabling efficient single-GPU fine-tuning without explicit performance timing data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9854eae-9034-44f4-9e3c-adca873370bd",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "5045970d-08f7-489b-b52c-8c68629ece49",
  "sourceToolAssistantUUID": "c9854eae-9034-44f4-9e3c-adca873370bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T12:12:03.039Z_

<details><summary>↩ Tool result · `toolu_01QRX6tPWXXj2f1WAhz7GhGK`</summary>

```text
# Training Details for CogVideoX ControlNet

Based on the repository documentation, here are the training specifics:

## Hardware Requirements
The project specifies GPU memory needs: "The 2B model requires 48 GB VRAM (For example A6000) and 80 GB for 5B. But it depends on the number of transformer blocks which default is 8."

## Dataset
The implementation uses the OpenVid-1M dataset as its foundation for training data.

## Configurable Parameters
The training setup allows adjustment of `controlnet_transformer_num_layers` (default: 8), which affects memory consumption.

## Notable Limitation
The documentation does not provide specific details about:
- Training duration or number of epochs
- Learning rates or batch sizes
- Number of training steps
- Computational overhead comparisons versus non-ControlNet approaches

The repository focuses on implementation and inference examples rather than comprehensive training metrics. For detailed training specifications, users would need to examine the actual configuration files (`accelerate_config_machine_single.yaml` and `finetune_single_rank.sh`) referenced in the training section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a33475fb-82ae-4160-bb08-df929dd868f5",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "f318be60-ee4a-41ce-a8a2-0dc8549dcca6",
  "sourceToolAssistantUUID": "a33475fb-82ae-4160-bb08-df929dd868f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T12:12:05.166Z_

<details><summary>↩ Tool result · `toolu_0129oboZnugpJckahFiiDjEh`</summary>

```text
# Training Details for Temporal In-Context Fine-Tuning

## Hardware & Compute Resources

**GPU Hardware:**
- Primary: NVIDIA H100 80GB GPU
- Also mentioned: NVIDIA A100 GPU for some experiments

**Training Duration & Steps:**
- "fewer than 1,000 training steps—requiring less than one hour of training time for CogVideoX-5B"
- Main experiments: 6,000 steps with batch size 2
- Low-data regime variant: 2,000 steps

## Memory Requirements

The method demonstrates significant efficiency advantages:

- **TIC-FT with LoRA (rank 128):** ~30GB GPU memory for 49 frames
- **ControlNet with LoRA (rank 128):** ~60GB GPU memory
- **Fun-pose (full fine-tuning):** ~75GB GPU memory

## Dataset Configuration

- Training samples: 10–30 samples per task (main experiments used 20-30)
- Evaluation: 100 samples
- Video format: 49 frames at 10 fps, resized to 480×480 or 848×480

## ControlNet Comparison

The paper notes that ControlNet requires "substantially more memory overhead" and "larger datasets" than TIC-FT. Quantitatively, ControlNet demanded double the VRAM (60GB vs. 30GB), highlighting TIC-FT's computational efficiency advantage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "538a7810-2513-4a49-9d65-1f85921513b6",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "569d41a3-4256-4ae5-8548-efd313ef0d7c",
  "sourceToolAssistantUUID": "538a7810-2513-4a49-9d65-1f85921513b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-10T12:12:07.675Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GYWbPiwAD42NaVYuosDQEo`</summary>

```json
{
  "query": "video ControlNet training \"GPU days\" OR \"GPU hours\" OR \"A100 hours\" OR \"H100 hours\" diffusion transformer 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "569d41a3-4256-4ae5-8548-efd313ef0d7c",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsEBvj5J7tqtJ6qV2yR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e60a5bd-dcf0-45be-b313-e6eebaf4d8e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Tsqk8B8cydh7xSW5Zg1Lbn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 24546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1388,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-10T12:12:09.553Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C9aEjNdzmqcXdoza1Fd22c`</summary>

```json
{
  "url": "https://www.stablediffusiontutorials.com/2025/10/wan2.2-lora-training.html",
  "prompt": "Extract all specific training time numbers, GPU types, hours/minutes, dataset sizes, steps, batch sizes, and hardware configurations. Also note any mention of ControlNet training specifically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e60a5bd-dcf0-45be-b313-e6eebaf4d8e7",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsEBvj5J7tqtJ6qV2yR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39535c8a-1706-4942-ba4d-e961634488e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Tsqk8B8cydh7xSW5Zg1Lbn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 24546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1388,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-10T12:12:09.801Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GG1ENr9m7Rp47qBnpJqCQa`</summary>

```json
{
  "query": "HunyuanVideo ControlNet training GPU hours compute overhead versus LoRA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39535c8a-1706-4942-ba4d-e961634488e7",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsEBvj5J7tqtJ6qV2yR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3e14dfe-39f2-42a5-9ece-8aad82bc66e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Tsqk8B8cydh7xSW5Zg1Lbn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1388,
      "cache_read_input_tokens": 24546,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1388
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 24546,
          "cache_creation_input_tokens": 1388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1388,
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

_source line 54 · 2026-05-10T12:12:15.606Z_

<details><summary>↩ Tool result · `toolu_01C9aEjNdzmqcXdoza1Fd22c`</summary>

```text
# Wan 2.2 LoRA Training: Hardware & Configuration Details

## Training Time
- **24 hours** on NVIDIA A6000 (96GB VRAM) for I2V model
- **2-3 days** estimated for consumer-grade powerful setups

## GPU Requirements
- Minimum: **NVIDIA RTX 4090/5090 with 24GB VRAM** (for images)
- Videos require "much higher" VRAM than images
- Cloud alternative: Runpod at "$2/hr" for decent GPUs

## Training Parameters

**Steps:** 3000-5000 recommended (more steps = longer training)

**Batch Size:** 1

**Gradient Accumulation:** 1

**Learning Rate:** 0.0002 (fast pace) or 0.0001 (default)

**Linear Rank:** 16-32

## Dataset Specifications
- **Image dataset:** 10-15 samples (PNG/JPG)
- **Video dataset:** 5+ seconds minimum
- **Frame count:** 81 frames for I2V models (follows formula: multiple of 4 + 1)

## Resolution Options
- Low VRAM: 256 and 512 pixels
- High VRAM: 512, 768, and 1024 pixels

## Note on ControlNet
The document contains no ControlNet training information; it focuses exclusively on standard LoRA training for Wan 2.2.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39535c8a-1706-4942-ba4d-e961634488e7",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "bbecbe44-2045-42a0-94c7-96e9362c5ad6",
  "sourceToolAssistantUUID": "39535c8a-1706-4942-ba4d-e961634488e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-10T12:12:16.220Z_

<details><summary>↩ Tool result · `toolu_01GG1ENr9m7Rp47qBnpJqCQa`</summary>

```text
Web search results for query: "HunyuanVideo ControlNet training GPU hours compute overhead versus LoRA"

Links: [{"title":"Hunyuan video LoRA training study (Single image/style training)","url":"https://huggingface.co/blog/neph1/hunyuan-lora"},{"title":"GitHub - lucataco/cog-hunyuanvideo-lora-trainer: Memory-optimized training scripts for video models based on Diffusers · GitHub","url":"https://github.com/lucataco/cog-hunyuanvideo-lora-trainer"},{"title":"Training a LoRA for Hunyuan video on Windows | Civitai","url":"https://civitai.com/articles/9798/training-a-lora-for-hunyuan-video-on-windows"},{"title":"GitHub - Zuntan03/EasyHunyuanVideo: HunyuanVideoを簡単に試せる環境です。","url":"https://github.com/Zuntan03/EasyHunyuanVideo"},{"title":"How long to train a WAN or Hunyuan video lora? · Issue #131 · tdrussell/diffusion-pipe","url":"https://github.com/tdrussell/diffusion-pipe/issues/131"},{"title":"Train Your Own LoRA Models for Hunyuan Video and Flux in Google Colab | by 0517 jhj | Medium","url":"https://medium.com/@developerjo0517/train-your-own-lora-models-for-hunyuan-video-and-flux-in-google-colab-3fc965e325d9"},{"title":"GitHub - Tencent-Hunyuan/HunyuanDiT: Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding · GitHub","url":"https://github.com/Tencent/HunyuanDiT"},{"title":"GitHub - AlphafromZion/hunyuan-video-lora-amd: Complete guide + scripts for training HunyuanVideo 1.5 I2V LoRAs on AMD GPUs (ROCm). Battle-tested on RX 9700 XT. · GitHub","url":"https://github.com/AlphafromZion/hunyuan-video-lora-amd"},{"title":"MimicPC - HunyuanVideo with LoRA: Best AI Video Generator","url":"https://www.mimicpc.com/learn/hunyuan-video-with-lora-best-ai-video-generator"},{"title":"Training Custom LoRAs for Hunyuan Video Model (Full Guide)","url":"https://www.youtube.com/watch?v=bCGXvSwFT78"}]

Based on my search results, I found information about HunyuanVideo LoRA training, but the search results do not contain specific comparative data on ControlNet training GPU hours and compute overhead versus LoRA for HunyuanVideo.

Here's what I found about HunyuanVideo LoRA training:

HunyuanVideo LoRA training of 400 steps (100 epochs) takes approximately 1 hour 37 minutes, which is about half the time of LTX LoRA training. This provides some baseline training time information.

Regarding LoRA's computational efficiency, LoRA freezes the original weights of the base model and generates the desired result by inserting a small number of new weights, offering flexibility and scalability; after training a solid base model, you would prefer to have several small LoRA models instead of retraining the entire base model, and due to its cost-effectiveness, LoRA has become a very popular training technique.

However, the search results do not contain specific information comparing ControlNet training GPU hours and compute overhead directly against LoRA for HunyuanVideo. FineTrainers is a library that prioritizes support for LoRA training for video models, and eventually plans to support other methods like controlnets and control-loras, but concrete comparative GPU hour metrics are not available in these results.

To get the specific comparison you're looking for, you would need to consult official HunyuanVideo documentation, research papers, or community benchmarks that specifically measure ControlNet versus LoRA training efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3e14dfe-39f2-42a5-9ece-8aad82bc66e5",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "45930e13-e706-4c54-a3fb-d5535b745441",
  "sourceToolAssistantUUID": "a3e14dfe-39f2-42a5-9ece-8aad82bc66e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-10T12:12:24.422Z_

<details><summary>↩ Tool result · `toolu_01GYWbPiwAD42NaVYuosDQEo`</summary>

```text
Web search results for query: "video ControlNet training "GPU days" OR "GPU hours" OR "A100 hours" OR "H100 hours" diffusion transformer 2024 2025"

Links: [{"title":"GitHub - zai-org/CogVideo: text and image to video generation: CogVideoX (2024) and CogVideo (ICLR 2023) · GitHub","url":"https://github.com/zai-org/CogVideo"},{"title":"NVIDIA A100 GPU Price Guide (2025) - Cloud Rental & Purchase Costs | AI FAQ | Jarvis Labs","url":"https://jarvislabs.ai/ai-faqs/nvidia-a100-gpu-price"},{"title":"H100 Transformer Engine Supercharges AI Training, Delivering Up to 6x Higher Performance Without Losing Accuracy | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/h100-transformer-engine/"},{"title":"Best Cloud GPU for AI Image Generation, Stable Diffusion, and Generative Image Models (May 2026)","url":"https://www.thundercompute.com/blog/best-cloud-gpus-ai-art-generation"},{"title":"H100 vs A100: GPU Benchmarks, Specs & Cloud Pricing Compared (2026) | Jarvis Labs Blog | Jarvis Labs","url":"https://jarvislabs.ai/blog/h100-vs-a100"},{"title":"Best GPU for AI Training 2025: Complete Buying Guide | Griddly","url":"https://www.griddly.ai/learn/for-developers/best-gpu-for-ai-training"},{"title":"H100 vs A100 comparison: Best GPU for LLMs, vision models, and scalable training | Blog — Northflank","url":"https://northflank.com/blog/h100-vs-a100"},{"title":"NVIDIA H100: The Best GPU for LLM Training Today","url":"https://cyfuture.ai/blog/why-nvidia-h100-for-llm-training"},{"title":"NVIDIA Sets New Generative AI Performance and Scale Records in MLPerf Training v4.0 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/nvidia-sets-new-generative-ai-performance-and-scale-records-in-mlperf-training-v4-0/"},{"title":"NVIDIA H100 Deep Dive: Specs, Pricing, Best Uses, and Where to Run It (2026) - Fluence","url":"https://www.fluence.network/blog/nvidia-h100-deep-dive/"}]

The search results provide general information about GPU training performance and comparisons, but don't contain specific information about video ControlNet training costs in GPU days or hours. Let me try a more targeted search.

Links: [{"title":"Stable Diffusion v1.5 Benchmark On Consumer GPUs - SaladCloud Blog","url":"https://blog.salad.com/stable-diffusion-v1-5-benchmark/"},{"title":"Deep Learning GPU Benchmarks 2024 | Restackio","url":"https://www.restack.io/p/deep-learning-answer-gpu-benchmarks-2024-cat-ai"},{"title":"Deep Learning GPU Benchmarks 2024 - aime.info","url":"https://www.aime.info/blog/en/deep-learning-gpu-benchmarks-2024/"},{"title":"Deep Learning GPU Benchmarks: Top Performers in 2024 - SQream","url":"https://sqream.com/blog/deep-learning-gpu-benchmarks/"},{"title":"NVIDIA: MLPerf AI Benchmarks","url":"https://www.nvidia.com/en-us/data-center/resources/mlperf-benchmarks/"},{"title":"Deep Learning GPU Benchmark","url":"https://mtli.github.io/gpubench/"},{"title":"GPU computational performance per dollar - Our World in Data","url":"https://ourworldindata.org/grapher/gpu-price-performance"},{"title":"Cost-Effective Deep Learning GPU Systems: Top 5 Picks (2024)","url":"https://blog.spheron.network/cost-effective-deep-learning-gpu-systems-top-5-picks-2024"},{"title":"The Best GPUs for Deep Learning in 2023 — An In-depth Analysis","url":"https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/"},{"title":"GPU Benchmarks for Deep Learning | Lambda","url":"https://lambda.ai/gpu-benchmarks"}]

Let me try a more specific search for video ControlNet papers or research documentation.

No links found.

Let me try a different approach with a search for video generation model training costs.

Links: [{"title":"Video Generation Models Explosion 2024 - Yen-Chen Lin","url":"https://yenchenlin.me/blog/2025/01/08/video-generation-models-explosion-2024/"},{"title":"Diffusion Models for Video Generation | Lil'Log","url":"https://lilianweng.github.io/posts/2024-04-12-diffusion-video/"},{"title":"GitHub - Vchitect/Latte: [TMLR 2025] Latte: Latent Diffusion Transformer for Video Generation. · GitHub","url":"https://github.com/Vchitect/Latte"},{"title":"Video diffusion generation: comprehensive review and open problems | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11331-6"},{"title":"Optimizing Transformer-Based Diffusion Models for Video Generation with NVIDIA TensorRT | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/optimizing-transformer-based-diffusion-models-for-video-generation-with-nvidia-tensorrt/"},{"title":"Published as a conference paper at ICLR 2025 DYNAMIC DIFFUSION TRANSFORMER","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a44a70acd5d0abc1a252ada9719dd06d-Paper-Conference.pdf"},{"title":"Survey of Video Diffusion Models: Foundations, Implementations, and Applications","url":"https://arxiv.org/html/2504.16081v1"},{"title":"Diffusion-Based Image/Video Generation | Proceedings of the Special Interest Group on Computer Graphics and Interactive Techniques Conference Courses","url":"https://dl.acm.org/doi/10.1145/3721241.3733996"},{"title":"Video generation models as world simulators | OpenAI","url":"https://openai.com/index/video-generation-models-as-world-simulators/"},{"title":"Diffusion Adversarial Post-Training for One-Step Video Generation | OpenReview","url":"https://openreview.net/forum?id=AAgzsnhc28"}]

Let me try one more search specifically for ControlNet architecture and training information.

Links: [{"title":"ControlNet Training and Usage | huggingface-cn/hf-blog-translation | DeepWiki","url":"https://deepwiki.com/huggingface-cn/hf-blog-translation/5.2-controlnet-training-and-usage"},{"title":"ControlNet – Achieving Superior Image Generation Results | LearnOpenCV #","url":"https://learnopencv.com/controlnet/"},{"title":"UniCon: Unidirectional Information Flow for Effective Control of Large-Scale Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=uJqKf24HGN"},{"title":"ControlNet/docs/train.md at main · lllyasviel/ControlNet","url":"https://github.com/lllyasviel/ControlNet/blob/main/docs/train.md"},{"title":"Play in Control - ControlNet training setup guide | Civitai","url":"https://civitai.com/articles/2078/play-in-control-controlnet-training-setup"},{"title":"Paper page - ControlNet-XS: Designing an Efficient and Effective Architecture for Controlling Text-to-Image Diffusion Models","url":"https://huggingface.co/papers/2312.06573"},{"title":"ControlNet-XS: Designing an Efficient and Effective Architecture for Controlling Text-to-Image Diffusion Models","url":"https://arxiv.org/html/2312.06573v1"},{"title":"What are the specs for training a ControlNet? · lllyasviel/ControlNet · Discussion #330","url":"https://github.com/lllyasviel/ControlNet/discussions/330"},{"title":"ControlNet+⁣+: Improving Conditional Controls with Efficient Consistency Feedback Project Page: liming-ai.github.io/ControlNet_Plus_Plus","url":"https://arxiv.org/html/2404.07987v1"},{"title":"ControlNet Training: Improve Your ControlNet Training Dataset","url":"https://voxel51.com/blog/conquering-controlnet"}]

Based on my web search results, I found relevant information about ControlNet training computational costs, though the results focus primarily on image ControlNets rather than video-specific implementations. Here's what I found:

## ControlNet Training Computational Costs

Some of the ControlNet models like the Depth ControlNet take 100s of GPU hours with millions of images to train. More specifically, large-scale training used 8 NVIDIA A100 80 GB GPUs, a dataset with over a million images, and training for more than 50000 steps.

The original ControlNet paper states that ControlNet learns task-specific conditions in an end-to-end way, and the learning is robust even when the training dataset is small (< 50k), and training a ControlNet is as fast as fine-tuning a diffusion model, and the model can be trained on a personal devices.

For more efficient training approaches, UniCon reduces GPU memory usage by one-third and increases training speed by 2.3 times, while maintaining the same adapter parameter size.

## Important Note on Video ControlNet

While the search results provide extensive information about image-based ControlNet training, I did not find specific computational cost data (in GPU days/hours or A100/H100 hours) for **video ControlNet** training in the 2024-2025 timeframe. The results primarily cover:
- Image ControlNet training costs (100s of GPU hours)
- General video diffusion transformer training approaches
- CogVideoX with ControlNet support (mentioned but without training cost details)

For precise video ControlNet training costs with the specific GPU metrics you requested, you may need to consult the original research papers or technical documentation from video generation model developers like OpenAI (Sora) or other organizations working on video ControlNet implementations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e60a5bd-dcf0-45be-b313-e6eebaf4d8e7",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "4b914335-66aa-4fdc-9dbc-da9287c30f8d",
  "sourceToolAssistantUUID": "9e60a5bd-dcf0-45be-b313-e6eebaf4d8e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-10T12:12:27.503Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WKMpYDtkke3cMNadchKDsS`</summary>

```json
{
  "url": "https://github.com/tdrussell/diffusion-pipe/issues/131",
  "prompt": "Extract all training time data from this thread: GPU types (RTX 4090, A100, H100, etc.), specific hours/minutes reported, number of steps, dataset sizes, batch sizes. Focus on empirical reports from community members of how long training actually took."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b914335-66aa-4fdc-9dbc-da9287c30f8d",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsFcEjnoEQVXEMw41Nu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5da79aa-6d92-41ca-b89d-0aa75a13614f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017hMhpUMsYA2iVcugcU2iTa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1446,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 25934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2925,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-10T12:12:28.663Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013b4MiFt2tGgpMMGKKubdiK`</summary>

```json
{
  "url": "https://github.com/tdrussell/diffusion-pipe/issues/152",
  "prompt": "Extract all training time data: GPU types, hours/minutes reported, number of steps, dataset sizes. This is a WAN 2.1 LoRA training time sanity check thread."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5da79aa-6d92-41ca-b89d-0aa75a13614f",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsFcEjnoEQVXEMw41Nu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32182e50-2f0f-4b20-9567-c8182a67834c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017hMhpUMsYA2iVcugcU2iTa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1446,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 25934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2925,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-10T12:12:29.212Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VMurekK1N5KuDw5ioK5pQg`</summary>

```json
{
  "query": "wan2.1 OR wan2.2 controlnet training \"24 hours\" OR \"48 hours\" OR \"72 hours\" OR \"GPU days\" site:github.com OR site:huggingface.co"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32182e50-2f0f-4b20-9567-c8182a67834c",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsFcEjnoEQVXEMw41Nu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70bf4e33-1208-4364-a1fc-78a7901dce05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017hMhpUMsYA2iVcugcU2iTa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1446,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 25934,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2925
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1446,
          "output_tokens": 337,
          "cache_read_input_tokens": 25934,
          "cache_creation_input_tokens": 2925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2925,
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

_source line 60 · 2026-05-10T12:12:31.724Z_

<details><summary>↩ Tool result · `toolu_01WKMpYDtkke3cMNadchKDsS`</summary>

```text
# Training Time Data Extraction

Based on the provided webpage content, **no empirical training time data is available**. 

The page shows only a GitHub issue #131 where user MiloMindbender is *requesting* information about training duration, not reporting it. The issue states:

> "Can someone give me an idea of how long video training for Wan or Hunyuan takes on a 24gb 4090?"

This is a question posed to the community, not a response containing actual performance metrics. The user is explicitly asking for rough estimates from others who have completed training runs, but no replies or data are included in the extracted content.

**To find actual training benchmarks**, you would need to:
- Check the comments/replies to this GitHub issue (not shown here)
- Review closed similar issues in the repository
- Consult the project's documentation or wiki
- Search community forums or Discord channels dedicated to this tool
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5da79aa-6d92-41ca-b89d-0aa75a13614f",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "629d34de-951c-47ab-9982-78ae577767e5",
  "sourceToolAssistantUUID": "a5da79aa-6d92-41ca-b89d-0aa75a13614f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-10T12:12:32.631Z_

<details><summary>↩ Tool result · `toolu_013b4MiFt2tGgpMMGKKubdiK`</summary>

```text
# WAN 2.1 LoRA Training Time Data Extracted

## Training Configuration & Performance

**User's Setup:**
- GPU: NVIDIA A6000 (48GB VRAM)
- CPU: 16 vCPUs, 62GB RAM
- Model: Wan2.1-I2V-14B-480P
- Dataset: 10 videos at 512x512, 63 frames each, 15FPS

**Reported Training Times:**
- Initial configuration: "60-90 seconds per step"
- After adding frame_bucket [63]: "120 to 180 seconds per step"
- Total: Several hours for 10 epochs

**Configuration Modifications:**
- Learning rate: 2e-5 → 6e-5
- Frame buckets: [1, 33] → [1, 33, 63]
- blocks_to_swap: set to 2 (due to OOM issues)

## Comparative Data Point

A commenter mentioned training WAN 2.1 at 720p with a 4090 GPU achieving "32 epochs in 35 minutes using Musubi-Tuner," though the user expresses skepticism about this claim's accuracy.

**Note:** The GitHub issue presents this as a question seeking validation rather than reporting confirmed benchmarks from multiple sources.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32182e50-2f0f-4b20-9567-c8182a67834c",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "bcd165e2-7177-4d59-9917-14e82625c6eb",
  "sourceToolAssistantUUID": "32182e50-2f0f-4b20-9567-c8182a67834c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-10T12:12:34.095Z_

<details><summary>↩ Tool result · `toolu_01VMurekK1N5KuDw5ioK5pQg`</summary>

```text
Web search results for query: "wan2.1 OR wan2.2 controlnet training "24 hours" OR "48 hours" OR "72 hours" OR "GPU days" site:github.com OR site:huggingface.co"

Links: [{"title":"spacepxl/Wan2.1-control-loras · Hugging Face","url":"https://huggingface.co/spacepxl/Wan2.1-control-loras"},{"title":"TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1 · Hugging Face","url":"https://huggingface.co/TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1"},{"title":"TheDenk/wan2.1-t2v-1.3b-controlnet-canny-v1 · Hugging Face","url":"https://huggingface.co/TheDenk/wan2.1-t2v-1.3b-controlnet-canny-v1"},{"title":"TheDenk/wan2.1-t2v-14b-controlnet-depth-v1 · Hugging Face","url":"https://huggingface.co/TheDenk/wan2.1-t2v-14b-controlnet-depth-v1"},{"title":"TheDenk/wan2.1-t2v-14b-controlnet-hed-v1 · Hugging Face","url":"https://huggingface.co/TheDenk/wan2.1-t2v-14b-controlnet-hed-v1"},{"title":"TheDenk/wan2.1-t2v-14b-controlnet-canny-v1 · Hugging Face","url":"https://huggingface.co/TheDenk/wan2.1-t2v-14b-controlnet-canny-v1"},{"title":"TheDenk/wan2.2-ti2v-5b-controlnet-tile-v1 · Hugging Face","url":"https://huggingface.co/TheDenk/wan2.2-ti2v-5b-controlnet-tile-v1"},{"title":"TheDenk/wan2.1-t2v-1.3b-controlnet-depth-v1 · Hugging Face","url":"https://huggingface.co/TheDenk/wan2.1-t2v-1.3b-controlnet-depth-v1"},{"title":"README.md · TheDenk/wan2.2-t2v-a14b-controlnet-depth-v1 at main","url":"https://huggingface.co/TheDenk/wan2.2-t2v-a14b-controlnet-depth-v1/blob/main/README.md"},{"title":"TheDenk/wan2.2-t2v-a14b-controlnet-hed-v1 · Hugging Face","url":"https://huggingface.co/TheDenk/wan2.2-t2v-a14b-controlnet-hed-v1"}]

Based on the search results, I found one relevant result with training time information:

For Wan2.1 ControlNet training, one project reported 62k training steps taking about 3 days on 1x3090 GPU. This was for video-only training using 9-13 frames at 624px area equivalent.

The other search results show various Wan2.1 and Wan2.2 ControlNet model implementations on Hugging Face and GitHub (from TheDenk and other creators), but they don't include specific training time documentation mentioning the 24/48/72 hours or GPU days timeframes you were searching for.

The training duration you're looking for may be documented in the GitHub repositories themselves rather than in the model cards. You might want to check the GitHub repositories directly, particularly the TheDenk repositories linked in the results, which contain the actual training code and documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70bf4e33-1208-4364-a1fc-78a7901dce05",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "37c8efaf-6474-4947-9b1e-73a21ba47b4a",
  "sourceToolAssistantUUID": "70bf4e33-1208-4364-a1fc-78a7901dce05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-10T12:12:37.071Z_

That's a very useful data point. Let me verify the spacepxl control-loras details and fetch a couple more sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37c8efaf-6474-4947-9b1e-73a21ba47b4a",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsGKctJwPBpBBFnxaJc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b573a5d-ab96-4123-8cad-133411432428",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BJiyyyxi9cuCM6zCcVTNB2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3370,
      "cache_read_input_tokens": 28859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3370,
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

_source line 64 · 2026-05-10T12:12:39.307Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G25NPaVnTbX4cbgaJbNxEz`</summary>

```json
{
  "url": "https://huggingface.co/spacepxl/Wan2.1-control-loras",
  "prompt": "Extract ALL training details: GPU hardware, number of GPUs, training duration (hours, days), number of steps, dataset size, batch size, learning rate, any compute numbers. This is a Wan2.1 ControlNet/control-LoRA model. Look for training time like \"3 days on 1x3090\" or similar reports."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b573a5d-ab96-4123-8cad-133411432428",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsGKctJwPBpBBFnxaJc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa1d7bed-8e9a-401d-b1c4-346e1e1a010e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BJiyyyxi9cuCM6zCcVTNB2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3370,
      "cache_read_input_tokens": 28859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3370,
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

_source line 65 · 2026-05-10T12:12:39.724Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SnDmfL5zXP5BNrCdBh9bbD`</summary>

```json
{
  "query": "spacepxl Wan2.1 control-loras training 3090 GPU days steps dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa1d7bed-8e9a-401d-b1c4-346e1e1a010e",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsGKctJwPBpBBFnxaJc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "563b51c2-7b81-4337-888d-539717b69bc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BJiyyyxi9cuCM6zCcVTNB2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3370,
      "cache_read_input_tokens": 28859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3370,
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

_source line 66 · 2026-05-10T12:12:41.597Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YC3abBK3sHKLeT3fM2eJax`</summary>

```json
{
  "url": "https://huggingface.co/docs/diffusers/training/controlnet",
  "prompt": "Extract training time and compute estimates: how many GPU hours, on what hardware, for how many steps is ControlNet training documented to take? Focus on any benchmarks or example training runs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "563b51c2-7b81-4337-888d-539717b69bc5",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsGKctJwPBpBBFnxaJc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87051d75-6ab6-4255-91ef-885374073232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BJiyyyxi9cuCM6zCcVTNB2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3370,
      "cache_read_input_tokens": 28859,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3370
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 362,
          "cache_read_input_tokens": 28859,
          "cache_creation_input_tokens": 3370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3370,
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

_source line 67 · 2026-05-10T12:12:42.074Z_

<details><summary>↩ Tool result · `toolu_01YC3abBK3sHKLeT3fM2eJax`</summary>

````text
# ControlNet

[ControlNet](https://hf.co/papers/2302.05543) models are adapters trained on top of another pretrained model. It allows for a greater degree of control over image generation by conditioning the model with an additional input image. The input image can be a canny edge, depth map, human pose, and many more.

If you're training on a GPU with limited vRAM, you should try enabling the `gradient_checkpointing`, `gradient_accumulation_steps`, and `mixed_precision` parameters in the training command. You can also reduce your memory footprint by using memory-efficient attention with [xFormers](../optimization/xformers).

This guide will explore the [train_controlnet.py](https://github.com/huggingface/diffusers/blob/main/examples/controlnet/train_controlnet.py) training script to help you become familiar with it, and how you can adapt it for your own use-case.

Before running the script, make sure you install the library from source:

```bash
git clone https://github.com/huggingface/diffusers
cd diffusers
pip install .
```

Then navigate to the example folder containing the training script and install the required dependencies for the script you're using:

```bash
cd examples/controlnet
pip install -r requirements.txt
```

> [!TIP]
> 🤗 Accelerate is a library for helping you train on multiple GPUs/TPUs or with mixed-precision. It'll automatically configure your training setup based on your hardware and environment. Take a look at the 🤗 Accelerate [Quick tour](https://huggingface.co/docs/accelerate/quicktour) to learn more.

Initialize an 🤗 Accelerate environment:

```bash
accelerate config
```

To setup a default 🤗 Accelerate environment without choosing any configurations:

```bash
accelerate config default
```

Or if your environment doesn't support an interactive shell, like a notebook, you can use:

```py
from accelerate.utils import write_basic_config

write_basic_config()
```

Lastly, if you want to train a model on your own dataset, take a look at the [Create a dataset for training](create_dataset) guide to learn how to create a dataset that works with the training script.

> [!TIP]
> The following sections highlight parts of the training script that are important for understanding how to modify it, but it doesn't cover every aspect of the script in detail. If you're interested in learning more, feel free to read through the [script](https://github.com/huggingface/diffusers/blob/main/examples/controlnet/train_controlnet.py) and let us know if you have any questions or concerns.

## Script parameters

The training script provides many parameters to help you customize your training run. All of the parameters and their descriptions are found in the [`parse_args()`](https://github.com/huggingface/diffusers/blob/64603389da01082055a901f2883c4810d1144edb/examples/controlnet/train_controlnet.py#L231) function. This function provides default values for each parameter, such as the training batch size and learning rate, but you can also set your own values in the training command if you'd like.

For example, to speedup training with mixed precision using the fp16 format, add the `--mixed_precision` parameter to the training command:

```bash
accelerate launch train_controlnet.py \
  --mixed_precision="fp16"
```

Many of the basic and important parameters are described in the [Text-to-image](text2image#script-parameters) training guide, so this guide just focuses on the relevant parameters for ControlNet:

- `--max_train_samples`: the number of training samples; this can be lowered for faster training, but if you want to stream really large datasets, you'll need to include this parameter and the `--streaming` parameter in your training command
- `--gradient_accumulation_steps`: number of update steps to accumulate before the backward pass; this allows you to train with a bigger batch size than your GPU memory can typically handle

### Min-SNR weighting

The [Min-SNR](https://huggingface.co/papers/2303.09556) weighting strategy can help with training by rebalancing the loss to achieve faster convergence. The training script supports predicting `epsilon` (noise) or `v_prediction`, but Min-SNR is compatible with both prediction types. This weighting strategy is only supported by PyTorch.

Add the `--snr_gamma` parameter and set it to the recommended value of 5.0:

```bash
accelerate launch train_controlnet.py \
  --snr_gamma=5.0
```

## Training script

As with the script parameters, a general walkthrough of the training script is provided in the [Text-to-image](text2image#training-script) training guide. Instead, this guide takes a look at the relevant parts of the ControlNet script.

The training script has a [`make_train_dataset`](https://github.com/huggingface/diffusers/blob/64603389da01082055a901f2883c4810d1144edb/examples/controlnet/train_controlnet.py#L582) function for preprocessing the dataset with image transforms and caption tokenization. You'll see that in addition to the usual caption tokenization and image transforms, the script also includes transforms for the conditioning image.

> [!TIP]
> If you're streaming a dataset on a TPU, performance may be bottlenecked by the 🤗 Datasets library which is not optimized for images. To ensure maximum throughput, you're encouraged to explore other dataset formats like [WebDataset](https://webdataset.github.io/webdataset/), [TorchData](https://github.com/pytorch/data), and [TensorFlow Datasets](https://www.tensorflow.org/datasets/tfless_tfds).

```py
conditioning_image_transforms = transforms.Compose(
    [
        transforms.Resize(args.resolution, interpolation=transforms.InterpolationMode.BILINEAR),
        transforms.CenterCrop(args.resolution),
        transforms.ToTensor(),
    ]
)
```

Within the [`main()`](https://github.com/huggingface/diffusers/blob/64603389da01082055a901f2883c4810d1144edb/examples/controlnet/train_controlnet.py#L713) function, you'll find the code for loading the tokenizer, text encoder, scheduler and models. This is also where the ControlNet model is loaded either from existing weights or randomly initialized from a UNet:

```py
if args.controlnet_model_name_or_path:
    logger.info("Loading existing controlnet weights")
    controlnet = ControlNetModel.from_pretrained(args.controlnet_model_name_or_path)
else:
    logger.info("Initializing controlnet weights from unet")
    controlnet = ControlNetModel.from_unet(unet)
```

The [optimizer](https://github.com/huggingface/diffusers/blob/64603389da01082055a901f2883c4810d1144edb/examples/controlnet/train_controlnet.py#L871) is set up to update the ControlNet parameters:

```py
params_to_optimize = controlnet.parameters()
optimizer = optimizer_class(
    params_to_optimize,
    lr=args.learning_rate,
    betas=(args.adam_beta1, args.adam_beta2),
    weight_decay=args.adam_weight_decay,
    eps=args.adam_epsilon,
)
```

Finally, in the [training loop](https://github.com/huggingface/diffusers/blob/64603389da01082055a901f2883c4810d1144edb/examples/controlnet/train_controlnet.py#L943), the conditioning text embeddings and image are passed to the down and mid-blocks of the ControlNet model:

```py
encoder_hidden_states = text_encoder(batch["input_ids"])[0]
controlnet_image = batch["conditioning_pixel_values"].to(dtype=weight_dtype)

down_block_res_samples, mid_block_res_sample = controlnet(
    noisy_latents,
    timesteps,
    encoder_hidden_states=encoder_hidden_states,
    controlnet_cond=controlnet_image,
    return_dict=False,
)
```

If you want to learn more about how the training loop works, check out the [Understanding pipelines, models and schedulers](../using-diffusers/write_own_pipeline) tutorial which breaks down the basic pattern of the denoising process.

## Launch the script

Now you're ready to launch the training script! 🚀

This guide uses the [fusing/fill50k](https://huggingface.co/datasets/fusing/fill50k) dataset, but remember, you can create and use your own dataset if you want (see the [Create a dataset for training](create_dataset) guide).

Set the environment variable `MODEL_NAME` to a model id on the Hub or a path to a local model and `OUTPUT_DIR` to where you want to save the model.

Download the following images to condition your training with:

```bash
wget https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/controlnet_training/conditioning_image_1.png
wget https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/controlnet_training/conditioning_image_2.png
```

One more thing before you launch the script! Depending on the GPU you have, you may need to enable certain optimizations to train a ControlNet. The default configuration in this script requires ~38GB of vRAM. If you're training on more than one GPU, add the `--multi_gpu` parameter to the `accelerate launch` command.

On a 16GB GPU, you can use bitsandbytes 8-bit optimizer and gradient checkpointing to optimize your training run. Install bitsandbytes:

```py
pip install bitsandbytes
```

Then, add the following parameter to your training command:

```bash
accelerate launch train_controlnet.py \
  --gradient_checkpointing \
  --use_8bit_adam \
```

On a 12GB GPU, you'll need bitsandbytes 8-bit optimizer, gradient checkpointing, xFormers, and set the gradients to `None` instead of zero to reduce your memory-usage.

```bash
accelerate launch train_controlnet.py \
  --use_8bit_adam \
  --gradient_checkpointing \
  --enable_xformers_memory_efficient_attention \
  --set_grads_to_none \
```

On a 8GB GPU, you'll need to use [DeepSpeed](https://www.deepspeed.ai/) to offload some of the tensors from the vRAM to either the CPU or NVME to allow training with less GPU memory.

Run the following command to configure your 🤗 Accelerate environment:

```bash
accelerate config
```

During configuration, confirm that you want to use DeepSpeed stage 2. Now it should be possible to train on under 8GB vRAM by combining DeepSpeed stage 2, fp16 mixed precision, and offloading the model parameters and the optimizer state to the CPU. The drawback is that this requires more system RAM (~25 GB). See the [DeepSpeed documentation](https://huggingface.co/docs/accelerate/usage_guides/deepspeed) for more configuration options. Your configuration file should look something like:

```bash
compute_environment: LOCAL_MACHINE
deepspeed_config:
  gradient_accumulation_steps: 4
  offload_optimizer_device: cpu
  offload_param_device: cpu
  zero3_init_flag: false
  zero_stage: 2
distributed_type: DEEPSPEED
```

You should also change the default Adam optimizer to DeepSpeed’s optimized version of Adam [`deepspeed.ops.adam.DeepSpeedCPUAdam`](https://deepspeed.readthedocs.io/en/latest/optimizers.html#adam-cpu) for a substantial speedup. Enabling `DeepSpeedCPUAdam` requires your system’s CUDA toolchain version to be the same as the one installed with PyTorch.

bitsandbytes 8-bit optimizers don’t seem to be compatible with DeepSpeed at the moment.

That's it! You don't need to add any additional parameters to your training command.

```bash
export MODEL_DIR="stable-diffusion-v1-5/stable-diffusion-v1-5"
export OUTPUT_DIR="path/to/save/model"

accelerate launch train_controlnet.py \
 --pretrained_model_name_or_path=$MODEL_DIR \
 --output_dir=$OUTPUT_DIR \
 --dataset_name=fusing/fill50k \
 --resolution=512 \
 --learning_rate=1e-5 \
 --validation_image "./conditioning_image_1.png" "./conditioning_image_2.png" \
 --validation_prompt "red circle with blue background" "cyan circle with brown floral background" \
 --train_batch_size=1 \
 --gradient_accumulation_steps=4 \
 --push_to_hub
```

Once training is complete, you can use your newly trained model for inference!

```py
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
from diffusers.utils import load_image
import torch

controlnet = ControlNetModel.from_pretrained("path/to/controlnet", torch_dtype=torch.float16)
pipeline = StableDiffusionControlNetPipeline.from_pretrained(
    "path/to/base/model", controlnet=controlnet, torch_dtype=torch.float16
).to("cuda")

control_image = load_image("./conditioning_image_1.png")
prompt = "pale golden rod circle with old lace background"

generator = torch.manual_seed(0)
image = pipeline(prompt, num_inference_steps=20, generator=generator, image=control_image).images[0]
image.save("./output.png")
```

## Stable Diffusion XL

Stable Diffusion XL (SDXL) is a powerful text-to-image model that generates high-resolution images, and it adds a second text-encoder to its architecture. Use the [`train_controlnet_sdxl.py`](https://github.com/huggingface/diffusers/blob/main/examples/controlnet/train_controlnet_sdxl.py) script to train a ControlNet adapter for the SDXL model.

The SDXL training script is discussed in more detail in the [SDXL training](sdxl) guide.

## Next steps

Congratulations on training your own ControlNet! To learn more about how to use your new model, the following guides may be helpful:

- Learn how to [use a ControlNet](../using-diffusers/controlnet) for inference on a variety of tasks.


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87051d75-6ab6-4255-91ef-885374073232",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "2296eb9f-6baa-46c1-9f02-2aec261fc791",
  "sourceToolAssistantUUID": "87051d75-6ab6-4255-91ef-885374073232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-10T12:12:43.544Z_

<details><summary>↩ Tool result · `toolu_01G25NPaVnTbX4cbgaJbNxEz`</summary>

```text
# Training Details for Wan2.1 Control-LoRA Models

Based on the provided content, here are the extracted training details:

## Tile Control-LoRA (1.3b t2v)

| Parameter | Value |
|-----------|-------|
| **GPU Hardware** | 1x NVIDIA RTX 3090 |
| **Number of GPUs** | 1 |
| **Training Duration** | ~3 days |
| **Training Steps** | 62,000 |
| **Dataset** | Videos only |
| **Frame Range** | 9-13 frames per video |
| **Resolution** | 624px area equivalent |
| **Batch Size** | Not specified |
| **Learning Rate** | Not specified (though noted: higher LR used for input layer LoRA) |

## Depth Control-LoRA (1.3b t2v)

| Parameter | Value |
|-----------|-------|
| **GPU Hardware** | Not explicitly stated |
| **Training Steps** | Not specified |
| **Depth Input Source** | DepthAnythingV2-small |
| **Training Data** | Paired depth map videos |

## Key Training Notes

- **Higher learning rate optimization**: A small but significant optimization was to set a higher learning rate for the input layer LoRA weights to accelerate convergence and avoid slow warmup issues typical in ControlNet training.
- **VAE Encoding**: Control videos were encoded through the VAE (scaled format) before concatenation with noisy latent inputs.
- **Training Method**: Similar to Flux Tools approach - expanding the diffusion model input layer with new channels, zero-initialization, and LoRA application.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa1d7bed-8e9a-401d-b1c4-346e1e1a010e",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "fc73d9e7-7d61-43fe-9da6-f1836853844c",
  "sourceToolAssistantUUID": "aa1d7bed-8e9a-401d-b1c4-346e1e1a010e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-10T12:12:50.471Z_

<details><summary>↩ Tool result · `toolu_01SnDmfL5zXP5BNrCdBh9bbD`</summary>

```text
Web search results for query: "spacepxl Wan2.1 control-loras training 3090 GPU days steps dataset"

Links: [{"title":"spacepxl/Wan2.1-control-loras · Hugging Face","url":"https://huggingface.co/spacepxl/Wan2.1-control-loras"},{"title":"README.md · spacepxl/Wan2.1-control-loras at main","url":"https://huggingface.co/spacepxl/Wan2.1-control-loras/blob/main/README.md"},{"title":"Train your WAN2.1 Lora model on Windows/Linux","url":"https://www.stablediffusiontutorials.com/2025/03/wan-lora-train.html"},{"title":"Wan2.1-control-loras | AI Model Details","url":"https://www.aimodels.fyi/models/huggingFace/wan2.1-control-loras-spacepxl"},{"title":"How to train Wan 2.1 LoRAs with Mimic PC | AI Artists' Guild","url":"https://www.patreon.com/posts/how-to-train-wan-137054569"},{"title":"spacepxl/Wan2.1-control-loras at main","url":"https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main"},{"title":"Wan 2.2 LoRA Training (Windows/Linux)","url":"https://www.stablediffusiontutorials.com/2025/10/wan2.2-lora-training.html"},{"title":"spacepxl/Wan2.1-control-loras · v1.1 much improved vs 0.2 on the use case I was playing with","url":"https://huggingface.co/spacepxl/Wan2.1-control-loras/discussions/18"},{"title":"WAN2.1 Lora Training Note | Civitai","url":"https://civitai.com/articles/12980/wan21-lora-training-note"},{"title":"WAN 2.2 local lora training guide [Windows/Linux] | Civitai","url":"https://civitai.com/articles/18985/wan-22-local-lora-training-guide-windowslinux"}]

Based on the search results, here's the information about spacepxl's Wan2.1-control-loras training specifications:

**Training Details:**
The training used videos only with 9-13 frames at 624px area equivalent, requiring 62k training steps and taking about 3 days on 1x3090 GPU.

**Dataset:**
The training dataset consisted of videos only, with 9-13 frames at 624px area equivalent.

**Why Control-LoRAs Instead of ControlNet:**
ControlNet adds significant inference cost and can be difficult to train well, whereas this method is extremely lightweight during inference (practically free if the lora is fused), relatively easy to train, and simple to implement.

This represents an efficient alternative to traditional ControlNet implementations for video generation with the Wan2.1 model, achieving training in approximately 3 GPU days on a single RTX 3090.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "563b51c2-7b81-4337-888d-539717b69bc5",
  "isSidechain": true,
  "promptId": "d18c3425-d226-459e-9d2c-34d672bfc8b3",
  "agentId": "ae8f10664b54150d4",
  "type": "user",
  "uuid": "5ff87ad4-4efc-4af8-a191-6f3153afb8ad",
  "sourceToolAssistantUUID": "563b51c2-7b81-4337-888d-539717b69bc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-10T12:13:47.314Z_

I now have enough data to give a thorough, well-sourced answer. Here is the full research report:

---

## Findings: Empirical Training Compute for ControlNet / Control-LoRA on Wan 2.1/2.2

### 1. TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1 — Does it exist? Training details?

**Yes, the model exists.** It was uploaded on October 30, 2025, to HuggingFace at `TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1`. TheDenk has released a full suite of seven Wan 2.2 ControlNet variants (depth, HED, canny, tile for both TI2V-5B and T2V-A14B architectures) plus five Wan 2.1 ControlNet models.

**Training details reported: none.** The model card, the GitHub repo (`TheDenk/wan2.2-controlnet`), and the related Wan 2.1 dilated-controlnet repo all omit training metrics entirely. No GPU type, no step count, no wall-clock time, no dataset size, no learning rate is stated anywhere in the public documentation. The repos are exclusively inference-focused. TheDenk's profile banner says "In a Training Loop" but provides zero empirical compute numbers.

The only configuration hints extracted from the related `shalfun/WanControl` Wan 2.1 implementation (which uses a similar architecture) are:
- Learning rate: 4e-5
- Max epochs: 1,000 (with 500 steps/epoch = 500,000 total steps if run to completion)
- Gradient accumulation: 1
- VRAM at 15 control layers: ~26 GB; at 10 layers: ~22 GB; at 5 layers: ~19 GB

---

### 2. Best empirical data point for Wan 2.1 ControlNet/control-LoRA training

**spacepxl/Wan2.1-control-loras** (HuggingFace) is the most transparent public disclosure found:

| Parameter | Value |
|-----------|-------|
| Hardware | 1x NVIDIA RTX 3090 (24 GB) |
| Method | Control-LoRA (input channel expansion + LoRA, not a separate encoder block) |
| Steps | ~62,000 |
| Training duration | ~3 days (~72 GPU-hours on a 3090) |
| Dataset | Videos only, 9–13 frames per clip, 624px area equivalent |
| Condition type | Tile (also depth; depth not separately benchmarked) |

This is training the 1.3B T2V Wan 2.1 variant, not the 5B or 14B. The author explicitly notes ControlNet "adds significant inference cost and can be difficult to train well" as justification for using the control-LoRA approach instead.

**Scaling to a 3090 equivalent:** 3090 ≈ 35.6 TFLOPS FP16 vs H100 SXM ≈ 989 TFLOPS FP16 (BF16 with sparsity: ~2x further). A naive FLOP ratio gives an ~28x speedup on H100, meaning a rough lower-bound translation of 72 h / 28 ≈ **2.6 H100-hours** for the 1.3B control-LoRA. However, this does not account for memory bandwidth bottlenecks, dataset/IO overhead, or the step count differences that would be needed for a 5B model.

---

### 3. Wan 2.1 LoRA fine-tuning on A40 (for calibration)

From `learn2train.medium.com` (hands-on report):
- Hardware: A40 (48 GB VRAM)
- Task: LoRA fine-tuning, Wan 2.1 T2V 14B
- Full workflow (setup + train + inference): 3–6 hours total at $0.44/hr (~$2–$3)
- Dataset: ~100 images

From the arXiv paper (arxiv.org/html/2510.27364v1), LoRA fine-tuning of Wan 2.1 I2V-14B:
- Hardware: Single A100-40 GB (or dual A100-80 GB)
- Steps: 4,000
- Batch: 11 videos × 4 gradient accumulation = effective batch 44
- LR: 3×10⁻⁵ with cosine schedule
- Dataset: ~25,000 frame-caption pairs (~40 clips, 2–5 sec each, 1024×576)
- Duration: **3 h 12 min** (single A100-40) | **1 h 36 min** (2x A100-80)

From `diffusion-pipe` issue #152 (community benchmark):
- Hardware: A6000 (48 GB)
- Model: Wan 2.1-I2V-14B-480P
- Dataset: 10 videos, 512×512, 63 frames, 15 FPS
- Step time: 60–90 sec/step (baseline); 120–180 sec/step with 63-frame buckets

From Apatero blog (Wan 2.2 LoRA analysis):
- RTX 4090: 200 samples at 512×512 → 4.5–5.5 h; 200 samples at 768×768 → 9.5–11.2 h
- A100 (40 GB, batch 2): 200 samples at 512×512 → 2.8–3.5 h
- Time per step (RTX 4090, 512×512, rank 64): 4.2–4.8 sec

From `stablediffusiontutorials.com` Wan 2.2 LoRA guide:
- A6000 96 GB: ~24 h for I2V video LoRA
- Recommended steps: 3,000–5,000

---

### 4. Video ControlNet compute overhead vs. LoRA (cross-model evidence)

From arXiv:2506.00996 (Temporal In-Context Fine-Tuning, CogVideoX-5B on H100):

| Method | GPU Memory | Training Duration |
|--------|-----------|-------------------|
| TIC-FT with LoRA (rank 128) | ~30 GB H100 | < 1 h (< 1,000 steps) |
| ControlNet with LoRA (rank 128) | ~60 GB H100 | Multiple hours (6,000 steps, batch 2) |
| Full fine-tune (Fun-pose) | ~75 GB H100 | Much longer |

Key quote: ControlNet requires "substantially more memory overhead" and "larger datasets." It doubles VRAM relative to LoRA-only approaches. The paper also states ControlNet training on CogVideoX-5B with 20 training samples over 6,000 steps, batch size 2, single H100 80 GB. No explicit wall-clock hours are given for the ControlNet condition, but the TIC-FT baseline is < 1 h so ControlNet at 6x steps is likely in the 3–6 h range on H100 for that small dataset.

From image-domain ControlNet (original lllyasviel work, confirmed by community reports):
- Large-scale depth ControlNet: "100s of GPU hours with millions of images" — this is SD1.5-era UNet, not a DiT.

---

### 5. Implications for your 35–70 H100-hour estimate

The only directly comparable published number is spacepxl's **~72 GPU-hours on an RTX 3090** for a Wan 2.1 1.3B control-LoRA (62k steps, low-res video). Scaled to H100 purely by FLOPS this would be ~2–3 H100-hours, but that model is the 1.3B variant, not 5B or 14B, and is a control-LoRA not a full ControlNet encoder block.

For the full ControlNet architecture (TheDenk-style, with dedicated encoder blocks), which involves roughly 2x the VRAM and more parameters than a control-LoRA, and for a larger base model (5B–14B), a more defensible analog is:

- CogVideoX-5B ControlNet: ~6,000 steps, batch 2, single H100 — no wall-clock disclosed, but memory at 60 GB suggests 3–6 h for a small-data regime
- A video depth model (non-Wan): ~1.5 days on 8x A100-80 = 288 A100-hours ≈ 100–150 H100-hours for a full-scale train

Your 35–70 H100-hour estimate for a Wan 2.2 5B ControlNet is plausible for a mid-scale training run (tens of thousands of steps on a dataset of hundreds of videos at moderate resolution). It sits between the small-data CogVideoX case (~5–10 H100-hours) and the full production-scale image ControlNet (hundreds of GPU-hours). The main caveats for anchoring this are:

1. No one has publicly disclosed the actual compute used for TheDenk's Wan 2.2 ControlNets.
2. The control-LoRA approach (spacepxl) is significantly cheaper than the full ControlNet encoder approach (TheDenk) but both exist for Wan 2.1/2.2.
3. Temporal attention in video DiTs (81-frame sequences at 480×832) creates much higher per-step cost vs. image ControlNets; step times of 60–180 sec/step on A6000 for 14B models suggest that even 5,000 steps could be 20–250 GPU-hours depending on hardware.

---

### Sources

- [TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1 on HuggingFace](https://huggingface.co/TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1)
- [TheDenk HuggingFace profile](https://huggingface.co/TheDenk)
- [TheDenk/wan2.2-controlnet GitHub](https://github.com/TheDenk/wan2.2-controlnet)
- [TheDenk/wan2.1-dilated-controlnet GitHub](https://github.com/TheDenk/wan2.1-dilated-controlnet)
- [spacepxl/Wan2.1-control-loras — HuggingFace (62k steps, 3 days, 1x RTX 3090)](https://huggingface.co/spacepxl/Wan2.1-control-loras)
- [arXiv:2506.00996 — Temporal In-Context Fine-Tuning (ControlNet vs LoRA VRAM/steps on H100, CogVideoX-5B)](https://arxiv.org/html/2506.00996v2)
- [arXiv:2510.27364 — LoRA fine-tuning Wan2.1 I2V-14B: 3h12m single A100-40, 4k steps](https://arxiv.org/html/2510.27364v1)
- [Apatero blog — Wan 2.2 LoRA training time analysis (RTX 4090, A100 benchmarks)](https://www.apatero.com/blog/wan-22-video-lora-training-time-complete-analysis-2025)
- [stablediffusiontutorials.com — Wan 2.2 LoRA training (A6000: ~24h for I2V)](https://www.stablediffusiontutorials.com/2025/10/wan2.2-lora-training.html)
- [learn2train.medium.com — Fine-tuning Wan 2.1 on A40 (3–6h total)](https://learn2train.medium.com/fine-tuning-wan-2-1-with-a-curated-dataset-step-by-step-guide-a6f0b334ab79)
- [diffusion-pipe issue #152 — WAN 2.1 LoRA training sanity check (A6000, 60–180s/step)](https://github.com/tdrussell/diffusion-pipe/issues/152)
- [shalfun/WanControl — Wan 2.1 ControlNet training config (LR, steps, VRAM)](https://github.com/shalfun/WanControl)
- [ROCm blog — Wan2.2 fine-tuning on AMD MI300X](https://rocm.blogs.amd.com/artificial-intelligence/finetuning-wan-part1/README.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ff87ad4-4efc-4af8-a191-6f3153afb8ad",
  "isSidechain": true,
  "agentId": "ae8f10664b54150d4",
  "requestId": "req_011CatsHXbzPJvJ32xMFhv4W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a43fedb-3a78-4f3e-b72c-e627873f7732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2a149f8-d4d1-4d29-9ded-21c865f6ab42",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017AaDqY1DSQgioWNAEmRHPv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3687,
      "cache_creation_input_tokens": 1723,
      "cache_read_input_tokens": 32229,
      "output_tokens": 3199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1723
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3687,
          "output_tokens": 3199,
          "cache_read_input_tokens": 32229,
          "cache_creation_input_tokens": 1723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1723,
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
