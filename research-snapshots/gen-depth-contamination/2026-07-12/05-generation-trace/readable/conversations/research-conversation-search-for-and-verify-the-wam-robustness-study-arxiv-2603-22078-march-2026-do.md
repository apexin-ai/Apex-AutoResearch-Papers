# Research conversation: Search for and verify the "WAM Robustness Study" (arXiv 2603.22078, March 2026) - "Do World Action Models Generalize Bet

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a466b09ea00147d6d.jsonl`
- **Structured JSON:** [`206ac21dce8812c96c1f.json`](../../sessions/20/206ac21dce8812c96c1f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-10T19:25:08.810Z_

Search for and verify the "WAM Robustness Study" (arXiv 2603.22078, March 2026) - "Do World Action Models Generalize Better than VLAs? A Robustness Study"

1. Does this paper exist?
2. Does it benchmark WAMs under distributional shifts (camera, lighting, layout perturbations)?
3. Does it use LIBERO-Plus and RoboTwin 2.0-Plus?
4. Does it document significant performance variation under distributional shifts?

Use WebSearch: 
- "world action models generalize VLAs robustness study 2603.22078"
- "LIBERO-Plus RoboTwin robustness WAM VLA"
Then WebFetch the arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1c50d650-056b-494e-9cc6-f7460f80080f",
  "agentId": "a466b09ea00147d6d",
  "type": "user",
  "uuid": "0f3cbc37-4e8e-4fdf-b588-ca88d5397d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T19:25:09.627Z_

I'll search for information about this paper systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f3cbc37-4e8e-4fdf-b588-ca88d5397d84",
  "isSidechain": true,
  "agentId": "a466b09ea00147d6d",
  "requestId": "req_011CauSFZ8YkGsh11Y3qXhmJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1f4c4e3e-cdf5-4c9b-9199-d58747a627e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GJZQhU4ZdGbkK5csdkPhrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 604,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T19:25:09.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YAJoGXtrzjMCGVAAXQ8ciK`</summary>

```json
{
  "query": "world action models generalize VLAs robustness study 2603.22078"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f4c4e3e-cdf5-4c9b-9199-d58747a627e1",
  "isSidechain": true,
  "agentId": "a466b09ea00147d6d",
  "requestId": "req_011CauSFZ8YkGsh11Y3qXhmJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8aaa06d2-cb03-49e8-b5d8-9674e0263a89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GJZQhU4ZdGbkK5csdkPhrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 604,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:25:09.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T5yjAd2SRLhBaYHnCz8Bkc`</summary>

```json
{
  "query": "LIBERO-Plus RoboTwin robustness WAM VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aaa06d2-cb03-49e8-b5d8-9674e0263a89",
  "isSidechain": true,
  "agentId": "a466b09ea00147d6d",
  "requestId": "req_011CauSFZ8YkGsh11Y3qXhmJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "720df6e1-dbca-4678-be5e-7103272b9767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GJZQhU4ZdGbkK5csdkPhrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 16153,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 604
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 132,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 604,
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

_source line 5 · 2026-05-10T19:25:17.960Z_

<details><summary>↩ Tool result · `toolu_01T5yjAd2SRLhBaYHnCz8Bkc`</summary>

```text
Web search results for query: "LIBERO-Plus RoboTwin robustness WAM VLA"

Links: [{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://www.wispaper.ai/en/blog/world-action-models-generalize-better-than-vlas-20260324/eng"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]","url":"https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/5ee94e80829fff79e4559b0c14bdb1cf32808838.pdf"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"StarVLA-𝜶: Reducing Complexity in Vision-Language-Action Systems","url":"https://arxiv.org/html/2604.11757"}]

Based on the search results, here's what I found about LIBERO-Plus, RoboTwin, robustness, WAM (World Action Models), and VLA (Vision-Language-Action models):

## LIBERO-Plus and RoboTwin Benchmarks

LIBERO-Plus introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise. RoboTwin 2.0-Plus is an in-house benchmark that follows a similar perturbation protocol in the two-arm Aloha-Agilex setup of RoboTwin 2.0.

## Robustness Comparison: WAMs vs. VLAs

By evaluating them on the LIBERO-Plus and RoboTwin 2.0-Plus benchmarks under seven types of perturbations, the study discovers that WAMs (like LingBot-VA and Cosmos-Policy) generally generalize better to visual noise and layout changes due to spatiotemporal priors from video pretraining.

However, the results are nuanced. WAMs achieve strong robustness, with LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus. Despite strong performance in visual perturbations, WAMs show reduced consistency and struggle with geometric perturbations, specifically variations in camera viewpoint and the robot's initial state. LingBot-VA's success rate dropped to 28.9% for camera and 36.2% for robot initial state perturbations on RoboTwin 2.0-Plus.

## VLA Vulnerabilities

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "720df6e1-dbca-4678-be5e-7103272b9767",
  "isSidechain": true,
  "promptId": "1c50d650-056b-494e-9cc6-f7460f80080f",
  "agentId": "a466b09ea00147d6d",
  "type": "user",
  "uuid": "c51416bd-521f-4028-a92b-dfa29d5a1746",
  "sourceToolAssistantUUID": "720df6e1-dbca-4678-be5e-7103272b9767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-10T19:25:18.551Z_

<details><summary>↩ Tool result · `toolu_01YAJoGXtrzjMCGVAAXQ8ciK`</summary>

```text
Web search results for query: "world action models generalize VLAs robustness study 2603.22078"

Links: [{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"Paper page - Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://huggingface.co/papers/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]","url":"https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://www.wispaper.ai/en/blog/world-action-models-generalize-better-than-vlas-20260324/eng"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"Towards Understanding Robustness and Generalization in World Models | OpenReview","url":"https://openreview.net/forum?id=k7nYm2yU5i"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"}]

I found the paper you're looking for! Here's what the research is about:

## Paper Summary

The paper is titled "Do World Action Models Generalize Better than VLAs? A Robustness Study" (arXiv:2603.22078), submitted in March 2026 by researchers from Huawei Technologies and the University of Toronto.

## Key Focus

The paper addresses the challenge of robot action planning in the real world, which requires understanding the current state of the environment and predicting how it will evolve in response to actions. The study compares two approaches:

- **Vision-Language-Action (VLA) models**: VLAs repurpose large-scale vision-language models for robot action generation using action experts and have achieved notable success across robotic tasks, but their performance remains constrained by training data scope and they exhibit limited generalization to unseen scenarios.

- **World Action Models (WAMs)**: WAMs are built upon world models trained on large corpora of video data to predict future states, with their latent representation decoded into robot actions.

## Main Findings

The results show that WAMs achieve strong robustness, with LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus. While VLAs can achieve comparable robustness on certain tasks, they typically require extensive training with diverse robotic datasets, whereas hybrid approaches that partially incorporate video-based dynamic learning exhibit intermediate robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8aaa06d2-cb03-49e8-b5d8-9674e0263a89",
  "isSidechain": true,
  "promptId": "1c50d650-056b-494e-9cc6-f7460f80080f",
  "agentId": "a466b09ea00147d6d",
  "type": "user",
  "uuid": "9de5a34b-364a-4eb4-93a9-6140f9472204",
  "sourceToolAssistantUUID": "8aaa06d2-cb03-49e8-b5d8-9674e0263a89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-10T19:25:19.999Z_

Excellent! The searches confirm the paper exists. Now let me fetch the arXiv page to verify the specific details about benchmarking distributional shifts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9de5a34b-364a-4eb4-93a9-6140f9472204",
  "isSidechain": true,
  "agentId": "a466b09ea00147d6d",
  "requestId": "req_011CauSGGmpyHBvW7nkS8Lpp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0c166b1f-f025-4d66-a5b0-6878f33bdbf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U5nKsbjj8jDpU17PHwcm8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1046,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 16757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1833,
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

_source line 8 · 2026-05-10T19:25:21.316Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NbuAzeqCwYDdHzCx84w2WD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.22078",
  "prompt": "Does the paper benchmark WAMs under distributional shifts including camera, lighting, and layout perturbations? Does it use LIBERO-Plus and RoboTwin 2.0-Plus? Does it document performance variation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c166b1f-f025-4d66-a5b0-6878f33bdbf1",
  "isSidechain": true,
  "agentId": "a466b09ea00147d6d",
  "requestId": "req_011CauSGGmpyHBvW7nkS8Lpp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "72a713c2-43fa-4dfe-88d3-b277edc2154a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U5nKsbjj8jDpU17PHwcm8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1046,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 16757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1833,
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

_source line 9 · 2026-05-10T19:25:21.685Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017ui8h7jRxRLEkbRf7EkDVR`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22078v1",
  "prompt": "What are the specific distributional shifts tested? What are the benchmark datasets? What performance variations are documented?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72a713c2-43fa-4dfe-88d3-b277edc2154a",
  "isSidechain": true,
  "agentId": "a466b09ea00147d6d",
  "requestId": "req_011CauSGGmpyHBvW7nkS8Lpp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d4e69873-1deb-40db-846e-05d004b9db5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U5nKsbjj8jDpU17PHwcm8A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1046,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 16757,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1046,
          "output_tokens": 251,
          "cache_read_input_tokens": 16757,
          "cache_creation_input_tokens": 1833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1833,
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

_source line 10 · 2026-05-10T19:25:25.256Z_

<details><summary>↩ Tool result · `toolu_01NbuAzeqCwYDdHzCx84w2WD`</summary>

```text
# Analysis of WAM Benchmarking in the Paper

Yes, the paper benchmarks WAMs under distributional shifts and uses the specified benchmarks.

**Benchmarks Used:**
The abstract confirms evaluation on "LIBERO-Plus and RoboTwin 2.0-Plus benchmarks under various visual and language perturbations."

**Distributional Shifts:**
The study explicitly tests robustness against "visual and language perturbations," which aligns with the camera, lighting, and layout variations you mention.

**Performance Variation:**
The paper documents substantial performance differences across models. For instance, it reports that "LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus," while noting that "VLAs such as π₀.₅ can achieve comparable robustness on certain tasks" but typically require more extensive training.

The research demonstrates that performance varies significantly depending on whether models incorporate video-based dynamic learning, suggesting the perturbation effects are well-documented across different architectural approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72a713c2-43fa-4dfe-88d3-b277edc2154a",
  "isSidechain": true,
  "promptId": "1c50d650-056b-494e-9cc6-f7460f80080f",
  "agentId": "a466b09ea00147d6d",
  "type": "user",
  "uuid": "9d6c0d70-633f-457e-8bf3-3a5f72a258e7",
  "sourceToolAssistantUUID": "72a713c2-43fa-4dfe-88d3-b277edc2154a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T19:25:27.556Z_

<details><summary>↩ Tool result · `toolu_017ui8h7jRxRLEkbRf7EkDVR`</summary>

```text
# Distributional Shifts, Benchmarks, and Performance Variations

## Distributional Shifts Tested

The paper evaluates robustness across seven perturbation dimensions:

1. **Camera viewpoint** - altering third-person camera pose
2. **Robot initial states** - varying joint configurations
3. **Language** - paraphrasing task instructions
4. **Lighting** - modifying illumination, shadows, color temperature
5. **Background** - changing table and scene textures
6. **Sensor noise** - applying photometric distortions to images
7. **Layout** - introducing task-irrelevant distracting objects

## Benchmark Datasets

**LIBERO-Plus**: Single-arm manipulation using 7-DoF Franka Panda robot with dual cameras at 256×256 resolution.

**RoboTwin 2.0-Plus**: Bimanual manipulation using Aloha-Agilex platform with three cameras at 320×240 resolution (in-house benchmark following similar perturbation protocols).

## Key Performance Variations

- **LingBot-VA** (WAM): 74.2% overall success on RoboTwin 2.0-Plus; particularly strong in lighting (89.0%), noise (80.9%), and layout (87.9%) perturbations
- **Cosmos-Policy** (WAM): 82.2% overall on LIBERO-Plus, 98.5% on original benchmark
- **π0.5** (VLA): 58.6% overall on RoboTwin 2.0-Plus; achieves 85.7% on LIBERO-Plus with perturbations

WAMs demonstrate consistent robustness to visual perturbations but struggle with geometric shifts (camera/robot state changes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4e69873-1deb-40db-846e-05d004b9db5d",
  "isSidechain": true,
  "promptId": "1c50d650-056b-494e-9cc6-f7460f80080f",
  "agentId": "a466b09ea00147d6d",
  "type": "user",
  "uuid": "d34755fd-93fb-4e64-aa28-14a6cd25e404",
  "sourceToolAssistantUUID": "d4e69873-1deb-40db-846e-05d004b9db5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T19:25:32.943Z_

Perfect! I now have comprehensive verification. Here are my findings:

## Verification Results

**1. Does this paper exist?**
✓ **YES** - The paper "Do World Action Models Generalize Better than VLAs? A Robustness Study" (arXiv 2603.22078, March 2026) definitely exists and is published.

**2. Does it benchmark WAMs under distributional shifts (camera, lighting, layout perturbations)?**
✓ **YES** - The paper explicitly benchmarks WAMs under seven types of distributional shifts:
- Camera viewpoint (altering third-person camera pose)
- Lighting (modifying illumination, shadows, color temperature)
- Layout (introducing task-irrelevant distracting objects)
- Robot initial states
- Language perturbations
- Background/texture changes
- Sensor noise

**3. Does it use LIBERO-Plus and RoboTwin 2.0-Plus?**
✓ **YES** - Both benchmarks are used:
- **LIBERO-Plus**: Single-arm manipulation with 7-DoF Franka Panda robot (256×256 resolution dual cameras)
- **RoboTwin 2.0-Plus**: Bimanual manipulation with Aloha-Agilex platform (320×240 resolution three cameras)

**4. Does it document significant performance variation under distributional shifts?**
✓ **YES** - Significant performance variations are documented:
- **LingBot-VA (WAM)**: 74.2% overall on RoboTwin 2.0-Plus, with strong performance on lighting (89.0%), noise (80.9%), and layout (87.9%), but struggles with geometric shifts
- **Cosmos-Policy (WAM)**: 82.2% on LIBERO-Plus, 98.5% on original benchmark
- **π₀.₅ (VLA)**: 58.6% overall on RoboTwin 2.0-Plus
- WAMs show strong robustness to visual perturbations but reduced consistency with geometric perturbations (camera viewpoint, robot initial state changes)

Sources:
- [arXiv 2603.22078 Abstract](https://arxiv.org/abs/2603.22078)
- [arXiv 2603.22078 HTML Version](https://arxiv.org/html/2603.22078v1)
- [HuggingFace Paper Page](https://huggingface.co/papers/2603.22078)
- [Wispaper Summary](https://www.wispaper.ai/en/blog/world-action-models-generalize-better-than-vlas-20260324/eng)
- [LIBERO-Plus Benchmark](https://arxiv.org/abs/2510.13626)
- [LIBERO-Plus GitHub Repository](https://github.com/sylvestf/LIBERO-plus)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d34755fd-93fb-4e64-aa28-14a6cd25e404",
  "isSidechain": true,
  "agentId": "a466b09ea00147d6d",
  "requestId": "req_011CauSGwGbUYjyWr1PJLmFq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "89e2804d-e208-4b3d-9620-a93a844be68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "876d1434-ee5e-418a-858f-b18c0ac4ab82",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MT34tyaww6bR5w9WC8CEFq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2005,
      "cache_read_input_tokens": 18590,
      "output_tokens": 693,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2005
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 693,
          "cache_read_input_tokens": 18590,
          "cache_creation_input_tokens": 2005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2005,
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
