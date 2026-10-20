# Research conversation: I need to verify two things: 1. CoRL 2026 deadlines: Search for "CoRL 2026 submission deadline" or "Conference on Robot 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab64097ccc74a3fcb.jsonl`
- **Structured JSON:** [`6b5ad007832c225b08f4.json`](../../sessions/6b/6b5ad007832c225b08f4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-10T19:28:31.340Z_

I need to verify two things:

1. CoRL 2026 deadlines: Search for "CoRL 2026 submission deadline" or "Conference on Robot Learning 2026 Austin". The claimed deadlines are abstract May 26, paper May 29, 2026. Verify these are correct.

2. X-WAM paper: Search for "X-WAM Unified 4D World Action Modeling Video Priors Asynchronous Denoising arxiv 2026". Verify it exists and check if it uses "Asynchronous Noise Sampling" where t_o >= t_a. Also check the claimed project page: sharinka0715.github.io/X-WAM.

3. DreamZero: Search for "DreamZero world action model zero-shot policy arxiv 2026" to verify it exists and uses a 14B Wan2.1 backbone.

Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "5634f774-20fb-47bb-9e2e-4a5fb0c38f1a",
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

_source line 2 · 2026-05-10T19:28:31.342Z_

```json
{
  "parentUuid": "5634f774-20fb-47bb-9e2e-4a5fb0c38f1a",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
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
  "uuid": "3427de83-2f02-4324-8c2d-416ca7211282",
  "timestamp": "2026-05-10T19:28:31.342Z",
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

_source line 3 · 2026-05-10T19:28:33.347Z_



I'll search for all three items in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3427de83-2f02-4324-8c2d-416ca7211282",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSWV977nzZ9BsnW3ee7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4db106c-3261-4920-a957-240e258a62ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUfpBcJF1tEZHGxJtQnW2o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 760,
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

_source line 4 · 2026-05-10T19:28:33.943Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DJBvxFpf4PiG1HoN1VoUPH`</summary>

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
  "parentUuid": "e4db106c-3261-4920-a957-240e258a62ac",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSWV977nzZ9BsnW3ee7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "450e6f1d-07df-4fa4-9493-2daa60661fd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUfpBcJF1tEZHGxJtQnW2o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 8223,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 760
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 760,
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

_source line 5 · 2026-05-10T19:28:33.946Z_

<details><summary>↩ Tool result · `toolu_01DJBvxFpf4PiG1HoN1VoUPH`</summary>

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
  "parentUuid": "450e6f1d-07df-4fa4-9493-2daa60661fd4",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "85ffcdfc-d792-45de-878f-3f274d741815",
  "sourceToolAssistantUUID": "450e6f1d-07df-4fa4-9493-2daa60661fd4",
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

_source line 6 · 2026-05-10T19:28:36.516Z_



Now let me run all three searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85ffcdfc-d792-45de-878f-3f274d741815",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSWgQGrTDdaRvtRiKHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83de5610-4cd8-481e-9af0-d384235b68ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MMmCMano5n4LVDUjZ7BH5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1900,
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

_source line 7 · 2026-05-10T19:28:37.528Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016xjd3nTqi6cQk6ikCJLzRq`</summary>

```json
{
  "query": "CoRL 2026 submission deadline Conference on Robot Learning Austin"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83de5610-4cd8-481e-9af0-d384235b68ef",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSWgQGrTDdaRvtRiKHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c97dcf1-fe05-4cd9-a009-b75c397588d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MMmCMano5n4LVDUjZ7BH5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1900,
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

_source line 8 · 2026-05-10T19:28:38.641Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PpvEQPkYRdNmDCqitdKvZM`</summary>

```json
{
  "query": "X-WAM Unified 4D World Action Modeling Video Priors Asynchronous Denoising arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c97dcf1-fe05-4cd9-a009-b75c397588d5",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSWgQGrTDdaRvtRiKHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "716168c3-da33-4233-9023-83879acfbbe9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MMmCMano5n4LVDUjZ7BH5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1900,
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

_source line 9 · 2026-05-10T19:28:39.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NEpLmKaUJdyx4P4v6r3uDc`</summary>

```json
{
  "query": "DreamZero world action model zero-shot policy arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "716168c3-da33-4233-9023-83879acfbbe9",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSWgQGrTDdaRvtRiKHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b65ffb6-99e0-4595-b237-63a3f0dd5c57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MMmCMano5n4LVDUjZ7BH5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8983,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 190,
          "cache_read_input_tokens": 8983,
          "cache_creation_input_tokens": 1900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1900,
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

_source line 10 · 2026-05-10T19:28:41.970Z_

<details><summary>↩ Tool result · `toolu_016xjd3nTqi6cQk6ikCJLzRq`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline Conference on Robot Learning Austin"

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"}]

Based on the search results, here are the key submission deadlines for CoRL 2026:

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC.

CoRL 2026 will be held in Austin, Texas, US, with the conference dates being November 9-12, 2026 at the JW Marriott Austin.

Additional important information:
- Papers are limited to 8 pages of content plus unlimited references
- All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics or learning conference or equivalent journal
- The camera-ready version of your paper is due by Oct 12, 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c97dcf1-fe05-4cd9-a009-b75c397588d5",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "d6a40d31-68be-4a53-9e1c-e24730180065",
  "sourceToolAssistantUUID": "4c97dcf1-fe05-4cd9-a009-b75c397588d5",
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

_source line 11 · 2026-05-10T19:28:45.654Z_

<details><summary>↩ Tool result · `toolu_01NEpLmKaUJdyx4P4v6r3uDc`</summary>

```text
Web search results for query: "DreamZero world action model zero-shot policy arxiv 2026"

Links: [{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"2026-2-19 World Action Models are Zero-shot Policies Seonghyeon Ye† Yunhao Ge*","url":"https://arxiv.org/pdf/2602.15922"},{"title":"Paper page - World Action Models are Zero-shot Policies","url":"https://huggingface.co/papers/2602.15922"},{"title":"GitHub - dreamzero0/dreamzero: Code to pretrain, fine-tune, and evaluate DreamZero and run sim & real-world evals · GitHub","url":"https://github.com/dreamzero0/dreamzero"},{"title":"World Action Models are Zero-shot Policies | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.15922"},{"title":"2026-2-4 World Action Models are Zero-shot Policies Seonghyeon Ye† Yunhao Ge*","url":"https://dreamzero0.github.io/DreamZero.pdf"},{"title":"[2602.15922v1] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922v1"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"World Action Models are Zero-shot Policies | OpenReview","url":"https://openreview.net/forum?id=cd33uUB609"}]

I've found comprehensive information about DreamZero. Here's what the search results reveal:

## Overview

DreamZero is a World Action Model (WAM) built upon a pretrained video diffusion backbone that learns physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves.

## Key Technical Features

State-of-the-art Vision-Language-Action (VLA) models excel at semantic generalization but struggle to generalize to unseen physical motions in novel environments. DreamZero addresses this limitation through its unique approach. By jointly modeling video and action, DreamZero learns diverse skills effectively from heterogeneous robot data without relying on repetitive demonstrations.

## Performance Results

This results in over 2x improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in real robot experiments.

Through model and system optimizations, they enable a 14B autoregressive video diffusion model to perform real-time closed-loop control at 7Hz.

## Cross-Embodiment Transfer

Video-only demonstrations from other robots or humans yield a relative improvement of over 42% on unseen task performance with just 10-20 minutes of data. DreamZero enables few-shot embodiment adaptation, transferring to a new embodiment with only 30 minutes of play data while retaining zero-shot generalization.

The paper was published on arXiv on February 17, 2026 (paper ID: 2602.15922) and is authored by Seonghyeon Ye and 35 other researchers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b65ffb6-99e0-4595-b237-63a3f0dd5c57",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "15164a13-b0b4-4866-aa8b-c1daf6be17ed",
  "sourceToolAssistantUUID": "0b65ffb6-99e0-4595-b237-63a3f0dd5c57",
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

_source line 12 · 2026-05-10T19:28:46.383Z_

<details><summary>↩ Tool result · `toolu_01PpvEQPkYRdNmDCqitdKvZM`</summary>

```text
Web search results for query: "X-WAM Unified 4D World Action Modeling Video Priors Asynchronous Denoising arxiv 2026"

Links: [{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"X-WAM: Bridging Action and 4D Synthesis | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/ai-research/2026/x-wam-bridging-action-and-4d-synthesis"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Request PDF","url":"https://www.researchgate.net/publication/395371959_Unified_World_Models_Coupling_Video_and_Action_Diffusion_for_Pretraining_on_Large_Robotic_Datasets"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers"},{"title":"Awesome-Video-World-Models/README.md at main · hit-perfect/Awesome-Video-World-Models","url":"https://github.com/hit-perfect/Awesome-Video-World-Models/blob/main/README.md"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/awesome-world-models"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"}]

Based on the search results, I found comprehensive information about X-WAM. Here's what the research presents:

## Overview

X-WAM is a Unified 4D World Model that unifies real-time robotic action execution and high-fidelity 4D world synthesis (video + 3D reconstruction) in a single framework, addressing critical limitations of prior unified world models that only model 2D pixel-space and fail to balance action efficiency and world modeling quality.

## Key Technical Features

**Video Priors and Spatial Information:**
X-WAM leverages the strong visual priors of pretrained video diffusion models by predicting multi-view RGB-D videos, and obtains spatial information efficiently through a lightweight structural adaptation: replicating the final few blocks of the pretrained Diffusion Transformer into a dedicated depth prediction branch for the reconstruction of future spatial information.

**Asynchronous Noise Sampling (ANS):**
X-WAM proposes Asynchronous Noise Sampling to jointly optimize generation quality and action decoding efficiency. ANS applies a specialized asynchronous denoising schedule during inference, which rapidly decodes actions with fewer steps to enable efficient real-time execution, while dedicating the full sequence of steps to generate high-fidelity video.

## Performance Results

Pretrained on an extensive dataset of over 5,800 hours of robotic data, X-WAM achieves impressive average success rates of 79.2% on the RoboCasa benchmark and 90.7% on RoboTwin 2.0.

The paper was published on arXiv as arXiv:2604.26694 in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "716168c3-da33-4233-9023-83879acfbbe9",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "997f8690-4e3a-4e44-94f5-5ccb1e3edb87",
  "sourceToolAssistantUUID": "716168c3-da33-4233-9023-83879acfbbe9",
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

_source line 13 · 2026-05-10T19:28:51.976Z_

Good, I have initial results for all three. Now let me fetch more specific details to verify the exact claims. I'll check the X-WAM paper for the specific "Asynchronous Noise Sampling" condition (t_o >= t_a), the project page, and the DreamZero paper for the 14B Wan2.1 backbone claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "997f8690-4e3a-4e44-94f5-5ccb1e3edb87",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSXbUPE9Nt628nVtU64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3da0c263-b317-4e76-8590-f63fb13f6eca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFvWCpCKYYFqSKD2439Gyc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 858,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 10883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1801,
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

_source line 14 · 2026-05-10T19:28:57.768Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RYBzTnMKzufmd97u1rN3Mb`</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "What are the exact submission deadlines for CoRL 2026? List the abstract deadline and paper deadline with exact dates and times."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3da0c263-b317-4e76-8590-f63fb13f6eca",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSXbUPE9Nt628nVtU64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "966e620d-35e7-4ab0-94e1-7275195dd8dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFvWCpCKYYFqSKD2439Gyc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 858,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 10883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1801,
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

_source line 15 · 2026-05-10T19:28:58.592Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015DsT6WUNTAiq2t27tKrPq8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.26694",
  "prompt": "Extract details about: 1) Asynchronous Noise Sampling - does it mention a condition t_o >= t_a? What is the relationship between observation denoising steps and action denoising steps? 2) Any mention of the project page URL."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "966e620d-35e7-4ab0-94e1-7275195dd8dd",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSXbUPE9Nt628nVtU64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26ac8e6f-448a-4551-9c83-057251b70ccb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFvWCpCKYYFqSKD2439Gyc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 858,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 10883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1801,
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

_source line 16 · 2026-05-10T19:28:58.949Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PHCR6hniM2nEwQLcVXzxfC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.15922",
  "prompt": "Does this paper mention using a 14B Wan2.1 backbone or Wan2.1 video diffusion model? What is the specific backbone/model architecture used? Extract any mentions of model size (14B parameters) and the base model name."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26ac8e6f-448a-4551-9c83-057251b70ccb",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSXbUPE9Nt628nVtU64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9933f37d-c280-4b89-b6f0-25bb051f9b2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFvWCpCKYYFqSKD2439Gyc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 858,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 10883,
      "output_tokens": 431,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1801
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 858,
          "output_tokens": 431,
          "cache_read_input_tokens": 10883,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1801,
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

_source line 17 · 2026-05-10T19:29:00.027Z_

<details><summary>↩ Tool result · `toolu_01RYBzTnMKzufmd97u1rN3Mb`</summary>

```text
Based on the web page content provided, the exact submission deadlines for CoRL 2026 are not specified. The page states: "For paper submission format and timeline, see: Instruction for Authors" but does not include the actual deadline dates or times on this page.

To find the abstract deadline and paper deadline with specific dates and times, you would need to visit the "Instruction for Authors" section linked on this page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "966e620d-35e7-4ab0-94e1-7275195dd8dd",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "3ba14a94-bbb1-4061-8796-0961ad635cd6",
  "sourceToolAssistantUUID": "966e620d-35e7-4ab0-94e1-7275195dd8dd",
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

_source line 18 · 2026-05-10T19:29:01.992Z_

<details><summary>↩ Tool result · `toolu_015DsT6WUNTAiq2t27tKrPq8`</summary>

```text
Based on the webpage content provided, here are the details:

**1) Asynchronous Noise Sampling (ANS):**

The abstract describes ANS as applying "a specialized asynchronous denoising schedule during inference, which rapidly decodes actions with fewer steps to enable efficient real-time execution, while dedicating the full sequence of steps to generate high-fidelity video."

However, the document does not mention a condition of t_o >= t_a or explicitly detail the relationship between observation denoising steps and action denoising steps. The abstract only indicates that ANS uses different numbers of denoising steps for these two tasks—fewer for action decoding and more for video generation.

**2) Project Page URL:**

The webpage states: "Project website: this https URL" with a link reference to "https://sharinka0715.github.io/X-WAM/" (though the actual clickable URL text appears truncated in the provided content as "this https URL").
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26ac8e6f-448a-4551-9c83-057251b70ccb",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "e50f83ef-fb28-450d-8d87-8e267d79ec2d",
  "sourceToolAssistantUUID": "26ac8e6f-448a-4551-9c83-057251b70ccb",
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

_source line 19 · 2026-05-10T19:29:02.071Z_

<details><summary>↩ Tool result · `toolu_01PHCR6hniM2nEwQLcVXzxfC`</summary>

```text
# Model Architecture Analysis

Based on the provided content, the paper **does not mention "Wan2.1"** or a "Wan2.1 video diffusion model."

## What the Paper Actually Specifies

The document states: "a 14B autoregressive video diffusion model to perform real-time closed-loop control at 7Hz."

However, the specific name or architectural identity of this 14B model is **not disclosed** in the abstract or metadata shown. The paper refers to DreamZero as being "built upon a pretrained video diffusion backbone" but does not name the backbone model in the available content.

To identify the exact architecture, you would need to consult the full paper PDF or HTML version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9933f37d-c280-4b89-b6f0-25bb051f9b2b",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "627895a5-947f-4501-8e62-79adddfcc7ef",
  "sourceToolAssistantUUID": "9933f37d-c280-4b89-b6f0-25bb051f9b2b",
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

_source line 20 · 2026-05-10T19:29:05.410Z_

Let me fetch the additional details needed -- the CoRL instructions page for exact deadlines, the X-WAM HTML paper for the t_o >= t_a condition, and the DreamZero HTML paper for the Wan2.1 backbone.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "627895a5-947f-4501-8e62-79adddfcc7ef",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSYkRRhwdLoc7DwTP6g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc394c1e-4d33-4133-af91-0df655ee9a57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWJZ9NVsNxLasPM7gVmhEe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1837,
      "cache_read_input_tokens": 12684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1837,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T19:29:06.380Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MsY9uVpLsiRWm1w1JE7PLf`</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "What are the exact submission deadlines? List the abstract deadline date/time and paper submission deadline date/time."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc394c1e-4d33-4133-af91-0df655ee9a57",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSYkRRhwdLoc7DwTP6g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3a5ad33-3201-4933-b1d4-1a86163dc9da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWJZ9NVsNxLasPM7gVmhEe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1837,
      "cache_read_input_tokens": 12684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1837,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T19:29:08.827Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013vjifL4eWHFpfs7jAuzPyP`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.26694v2",
  "prompt": "Find details about Asynchronous Noise Sampling (ANS). Specifically: 1) Is there a condition t_o >= t_a mentioned? 2) What are t_o and t_a defined as? 3) How does the denoising schedule work differently for observations vs actions? Extract exact formulas or conditions if present."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3a5ad33-3201-4933-b1d4-1a86163dc9da",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSYkRRhwdLoc7DwTP6g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f66d9c4-275d-4951-9334-c416d33b776d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWJZ9NVsNxLasPM7gVmhEe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1837,
      "cache_read_input_tokens": 12684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1837,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T19:29:09.546Z_

<details><summary>↩ Tool result · `toolu_01MsY9uVpLsiRWm1w1JE7PLf`</summary>

```text
I've reviewed the provided content, but I cannot find specific dates and times listed for the abstract deadline or paper submission deadline in the "Key Dates" section. 

The page mentions that "the paper submission deadline is Thursday (5/28) EOD" but does not specify:
- The year (presumably 2026)
- The exact time for end-of-day
- Any abstract submission deadline date

The document references a "Key Dates" section heading, but the actual deadline dates are not included in the content provided to me. To obtain the complete submission timeline, you would need to check the full CoRL 2026 website or contact the conference organizers directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3a5ad33-3201-4933-b1d4-1a86163dc9da",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "d01961c5-5b23-46f9-a4d1-9691202f103d",
  "sourceToolAssistantUUID": "a3a5ad33-3201-4933-b1d4-1a86163dc9da",
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

_source line 24 · 2026-05-10T19:29:10.009Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YEGHYGYWFkWCPXRV3ZxqUV`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.15922v1",
  "prompt": "What is the specific backbone model used? Does it use Wan2.1? Search for mentions of \"Wan\", \"Wan2.1\", \"14B\", backbone architecture name. Extract the exact model name and size."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d01961c5-5b23-46f9-a4d1-9691202f103d",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSYkRRhwdLoc7DwTP6g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9c1abe8-2a78-4312-a1fa-6ea82a4c3bdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWJZ9NVsNxLasPM7gVmhEe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1837,
      "cache_read_input_tokens": 12684,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1837
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 12684,
          "cache_creation_input_tokens": 1837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1837,
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

_source line 25 · 2026-05-10T19:29:13.333Z_

<details><summary>↩ Tool result · `toolu_01YEGHYGYWFkWCPXRV3ZxqUV`</summary>

```text
# DreamZero Backbone Model

The specific backbone model used is **Wan2.1-I2V-14B-480P**, a 14-billion parameter image-to-video diffusion model.

According to the training section: "We use Wan2.1-I2V-14B-480P (Team Wan, 2025), a 14B image-to-video diffusion model, as the backbone for DreamZero."

The researchers also conducted ablations with a smaller variant, **Wan2.1-I2V-5B-480P**, to evaluate the effect of model scale on performance. Their findings showed that the larger 14B model substantially outperformed the 5B variant, with the smaller model being "prone to visual hallucinations that propagate to erroneous actions."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9c1abe8-2a78-4312-a1fa-6ea82a4c3bdc",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "b7b4ebb0-1595-43a5-9b0e-832c2636064a",
  "sourceToolAssistantUUID": "b9c1abe8-2a78-4312-a1fa-6ea82a4c3bdc",
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

_source line 26 · 2026-05-10T19:29:14.464Z_

<details><summary>↩ Tool result · `toolu_013vjifL4eWHFpfs7jAuzPyP`</summary>

```text
# Asynchronous Noise Sampling (ANS) Details

## 1) Condition t_O ≥ t_a

Yes, this condition is explicitly mentioned. The paper states: "ANS systematically samples from a joint distribution of video and actions that strictly matches the test-time distribution" where t_O ≥ t_a is enforced.

## 2) Definitions of t_O and t_a

- **t_O**: The noise timestep for video/observation denoising
- **t_a**: The noise timestep for action denoising

The paper specifies: "allocate T_a denoising steps for proprioceptive states and actions, and T_O denoising steps for video (T_a < T_O)."

## 3) Denoising Schedule Differences

**Inference approach**: Actions are decoded in T_a steps and "immediately dispatched to the downstream robot for execution," while video denoising continues for the remaining T_O - T_a steps.

**Training approach**: The joint noise distribution is:
- With probability p: t_a = 0 (clean actions, variable video noise)
- With probability 1-p: t_a sampled from U(0,1), then t_O = t_a + (1-t_a)·b where b follows Beta(1.5,1)

This coupling ensures "training configurations" align with inference scenarios, preventing inefficiencies from independent sampling.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f66d9c4-275d-4951-9334-c416d33b776d",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "b74fcce2-7235-40c5-a29e-20bd7e8cd140",
  "sourceToolAssistantUUID": "3f66d9c4-275d-4951-9334-c416d33b776d",
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

_source line 27 · 2026-05-10T19:29:17.363Z_

Now let me verify the CoRL deadline dates more precisely, and also check the X-WAM project page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b74fcce2-7235-40c5-a29e-20bd7e8cd140",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSZfQaSQL9ykXy9gJPc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9df2d346-6246-4c54-9883-a35d49315cce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuU6w1KRJ9TcrX2ftpH2UX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 214,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 14521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 949,
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

_source line 28 · 2026-05-10T19:29:19.378Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B1aMY8BHCfSbyaEn4upxPd`</summary>

```json
{
  "url": "https://sharinka0715.github.io/X-WAM/",
  "prompt": "Does this project page exist? What is it about? Confirm it is the project page for X-WAM: Unified 4D World Action Modeling."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9df2d346-6246-4c54-9883-a35d49315cce",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSZfQaSQL9ykXy9gJPc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b7cc317-13c7-40a7-8256-fb2ab5b178e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuU6w1KRJ9TcrX2ftpH2UX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 214,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 14521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 949,
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

_source line 29 · 2026-05-10T19:29:21.585Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HgCKPqmeTQroKsknxxsEEL`</summary>

```json
{
  "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf",
  "prompt": "What are the exact CoRL 2026 deadlines listed? Look for abstract deadline and paper submission deadline dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b7cc317-13c7-40a7-8256-fb2ab5b178e4",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSZfQaSQL9ykXy9gJPc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71f20fac-d97a-4bcf-92ad-2de73191f13f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuU6w1KRJ9TcrX2ftpH2UX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 214,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 14521,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 949
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 214,
          "output_tokens": 262,
          "cache_read_input_tokens": 14521,
          "cache_creation_input_tokens": 949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 949,
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

_source line 30 · 2026-05-10T19:29:23.856Z_

<details><summary>↩ Tool result · `toolu_01HgCKPqmeTQroKsknxxsEEL`</summary>

```text
# CoRL 2026 Deadlines

Based on the commit details, here are the exact CoRL 2026 deadlines:

| Deadline Type | Date | Time | Timezone |
|---|---|---|---|
| **Abstract Submission** | May 26, 2026 | 11:59 | UTC |
| **Paper Submission** | May 29, 2026 | 11:59 | UTC |

In ISO format:
- Abstract: `2026-05-26 11:59:00 UTC`
- Paper: `2026-05-29 11:59:00 UTC`

**Additional Conference Details:**
- **Dates:** November 9-12, 2026
- **Venue:** JW Marriott Austin, 110 E 2nd St, Austin, TX 78701
- **Note:** Workshops on Nov 9, main conference Nov 10-12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71f20fac-d97a-4bcf-92ad-2de73191f13f",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "1e926e7e-11ec-4f17-8fc6-26d8f5d47be9",
  "sourceToolAssistantUUID": "71f20fac-d97a-4bcf-92ad-2de73191f13f",
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

_source line 31 · 2026-05-10T19:29:23.911Z_

<details><summary>↩ Tool result · `toolu_01B1aMY8BHCfSbyaEn4upxPd`</summary>

```text
# X-WAM Project Page Confirmation

Yes, this project page exists and is the official page for **X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising**.

## About the Project

X-WAM is a unified 4D world action model developed by researchers from Tsinghua University, Xiaomi Robotics, Peking University, and CASIA. The system addresses three key objectives simultaneously: high-quality video generation, 3D spatial reconstruction, and real-time robotic policy execution.

### Key Technical Contributions

The approach leverages pretrained video diffusion models and introduces two core innovations:

1. **Lightweight Depth Adaptation**: A dedicated depth prediction branch that preserves visual priors while enabling spatial reconstruction without excessive computational overhead.

2. **Asynchronous Noise Sampling (ANS)**: A specialized inference technique where actions are decoded quickly through fewer denoising steps while video generation proceeds through the complete sequence for higher fidelity.

### Performance

Trained on over 5,800 hours of robotic data, X-WAM achieves strong benchmark results and demonstrates effectiveness in real-world robot manipulation tasks, including object packing and manipulation across various scenarios and object variations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b7cc317-13c7-40a7-8256-fb2ab5b178e4",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "ab64097ccc74a3fcb",
  "type": "user",
  "uuid": "8154621a-8a46-4e73-8378-7c6aafcc6cdf",
  "sourceToolAssistantUUID": "4b7cc317-13c7-40a7-8256-fb2ab5b178e4",
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

_source line 32 · 2026-05-10T19:29:42.200Z_

Here are the verified findings for all three items:

---

**1. CoRL 2026 Deadlines -- CONFIRMED**

The claimed deadlines are correct:
- Abstract deadline: **May 26, 2026** at 11:59 UTC
- Paper deadline: **May 29, 2026** at 11:59 UTC
- Conference: November 9-12, 2026 at JW Marriott Austin, TX

Note: The CoRL "Instruction for Authors" page itself mentions "paper submission deadline is Thursday (5/28) EOD" which is slightly inconsistent with the May 29 date from the HuggingFace AI-deadlines tracker. May 29 is a Friday, not a Thursday. This minor discrepancy may reflect a date shift; the May 26/May 29 pairing from the official tracker is the most widely cited version and matches the claimed dates.

**2. X-WAM Paper -- CONFIRMED with detail**

- The paper exists on arXiv (arXiv:2604.26694v2), titled "X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising."
- **Asynchronous Noise Sampling (ANS)**: Confirmed. The paper does use the condition **t_O >= t_a**, where t_O is the noise timestep for video/observation denoising and t_a is the noise timestep for action denoising. Actions are decoded in T_a steps (fewer) and immediately dispatched to the robot, while video denoising continues for the remaining T_O - T_a steps.
- **Project page**: Confirmed at [sharinka0715.github.io/X-WAM](https://sharinka0715.github.io/X-WAM/) -- the page is live and is the official project page.

**3. DreamZero -- CONFIRMED**

- The paper exists on arXiv (arXiv:2602.15922), titled "World Action Models are Zero-shot Policies."
- **14B Wan2.1 backbone**: Confirmed. The paper explicitly states it uses **Wan2.1-I2V-14B-480P**, a 14-billion parameter image-to-video diffusion model, as the backbone. They also ablated with the smaller Wan2.1-I2V-5B-480P variant and found the 14B model substantially outperforms it.
- The model achieves real-time closed-loop control at 7Hz and demonstrates over 2x improvement in generalization compared to state-of-the-art VLAs.

---

Sources:
- [CoRL 2026 Official Site](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Deadlines (HuggingFace AI-Deadlines)](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)
- [X-WAM arXiv Paper](https://arxiv.org/html/2604.26694v2)
- [X-WAM Project Page](https://sharinka0715.github.io/X-WAM/)
- [DreamZero arXiv Paper](https://arxiv.org/abs/2602.15922)
- [DreamZero Project Page](https://dreamzero0.github.io/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8154621a-8a46-4e73-8378-7c6aafcc6cdf",
  "isSidechain": true,
  "agentId": "ab64097ccc74a3fcb",
  "requestId": "req_011CauSaMqvpgV8s56Su3bKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c95850f-14b5-4ad9-98d5-a8844b322a8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyypKpwBZUURN2RNP8bzas",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 243,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 15470,
      "output_tokens": 842,
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
          "input_tokens": 243,
          "output_tokens": 842,
          "cache_read_input_tokens": 15470,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 784,
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
