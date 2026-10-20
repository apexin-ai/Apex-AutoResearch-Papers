# Research conversation: I need to verify what the current SOTA is on the LIBERO-Plus camera perturbation axis. A search result mentioned "one mo

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae94922ca10442e5c.jsonl`
- **Structured JSON:** [`e4f4ed7e43001a8b6e96.json`](../../sessions/e4/e4f4ed7e43001a8b6e96.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-10T09:17:54.870Z_

I need to verify what the current SOTA is on the LIBERO-Plus camera perturbation axis.

A search result mentioned "one model achieves 92.8% camera view robustness (37.2 percentage points above next best)" on LIBERO-Plus. This might be from AnyCamVLA or some other method.

Please:
1. Fetch https://arxiv.org/abs/2603.05868 (AnyCamVLA) and check: what does it report on LIBERO-Plus camera performance? Does it report 92.8%?

2. Fetch https://arxiv.org/html/2510.13626v1 (LIBERO-Plus paper) and look at Table results - what baselines are evaluated and what are the camera axis scores?

3. Search for "LIBERO-Plus camera 2026 SOTA" to check if any paper published in 2026 beats OA-WAM's 80.5% camera score on LIBERO-Plus.

4. Check: Is the 92.8% number from AnyCamVLA (which requires known camera extrinsics at test time) or from an end-to-end method?

This is important because the proposal claims OA-WAM at 80.5% is the SOTA on LIBERO-Plus camera axis, and if a method achieves 92.8% this claim is incorrect.

Report clearly: what is the current SOTA on LIBERO-Plus camera axis and which paper/method holds it?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "9b9ac96a-285c-4801-8d8c-a61ee0325140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T09:17:56.005Z_

I'll help you verify the current SOTA on the LIBERO-Plus camera perturbation axis. Let me fetch and analyze the relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b9ac96a-285c-4801-8d8c-a61ee0325140",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdwrRFpEh7wwuw8rAFY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a7b37c62-78b8-40ad-9d1e-cb19b7392476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012Js1SzzxasaHH61ZwJYGW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 770,
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

_source line 3 · 2026-05-10T09:17:56.668Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XXWnaN8FnYLyFgSgpXokm2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.05868",
  "prompt": "What results does this paper report on LIBERO-Plus camera robustness or camera view performance? Report any specific percentages or accuracy numbers mentioned for LIBERO-Plus camera evaluation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7b37c62-78b8-40ad-9d1e-cb19b7392476",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdwrRFpEh7wwuw8rAFY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e1045061-ef63-44b6-83fc-39a3d3b71184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012Js1SzzxasaHH61ZwJYGW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 770,
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

_source line 4 · 2026-05-10T09:17:57.215Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MCz4Zfkf2tmzUCT1unP9nG`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "What are the results in the tables for LIBERO-Plus camera axis evaluation? List all baseline methods evaluated and their camera axis scores/performance numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1045061-ef63-44b6-83fc-39a3d3b71184",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdwrRFpEh7wwuw8rAFY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23fc894a-d398-4fa8-8269-d85008c73a1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012Js1SzzxasaHH61ZwJYGW1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 16155,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 770
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 770,
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

_source line 5 · 2026-05-10T09:17:57.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019KZvjyPviQZgSRkeGJpo1w`</summary>

```json
{
  "query": "LIBERO-Plus camera 2026 SOTA benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23fc894a-d398-4fa8-8269-d85008c73a1f",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdwrRFpEh7wwuw8rAFY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "18bd5334-9249-4d55-818c-03428335d097",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012Js1SzzxasaHH61ZwJYGW1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 16155,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 770
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 296,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 770,
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

_source line 6 · 2026-05-10T09:17:58.786Z_

<details><summary>↩ Tool result · `toolu_01XXWnaN8FnYLyFgSgpXokm2`</summary>

```text
Based on the webpage content provided, I cannot find specific percentages or accuracy numbers for LIBERO-Plus camera robustness or camera view performance.

The abstract mentions that the method was evaluated on "the LIBERO benchmark" and states: "our method consistently outperforms baselines that use data augmentation for policy fine-tuning or additional 3D-aware features for visual input."

However, no concrete performance metrics, accuracy percentages, or specific LIBERO-Plus results are included in this excerpt. To obtain those detailed quantitative results, you would need to access the full paper PDF or HTML version linked on this page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1045061-ef63-44b6-83fc-39a3d3b71184",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "24741879-1a31-4320-b1c6-fd80df030682",
  "sourceToolAssistantUUID": "e1045061-ef63-44b6-83fc-39a3d3b71184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-10T09:18:01.458Z_

<details><summary>↩ Tool result · `toolu_01MCz4Zfkf2tmzUCT1unP9nG`</summary>

```text
# LIBERO-Plus Camera Axis Evaluation Results

Based on Table 2 in the document, here are the camera viewpoint performance scores for all baseline methods evaluated on LIBERO-Plus:

| Model | Camera Score |
|-------|--------------|
| OpenVLA | 0.8% |
| OpenVLA-OFT | 56.4% |
| OpenVLA-OFT_w | 10.4% |
| NORA | 2.2% |
| WorldVLA | 0.1% |
| UniVLA | 1.8% |
| π₀ | 13.8% |
| π₀-Fast | 65.1% |
| RIPT-VLA | 55.2% |
| OpenVLA-OFT_m | 55.6% |
| **Proposed Method (Ours)** | **92.8%** |

The proposed approach achieved "a dramatic improvement in camera view robustness (92.8%), surpassing the next best model by 37.2 percentage points." This represents the most substantial performance gain across any single perturbation dimension tested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23fc894a-d398-4fa8-8269-d85008c73a1f",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "101dafa5-b55c-4c2a-ae78-29baa635b5bd",
  "sourceToolAssistantUUID": "23fc894a-d398-4fa8-8269-d85008c73a1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T09:18:04.284Z_

<details><summary>↩ Tool result · `toolu_019KZvjyPviQZgSRkeGJpo1w`</summary>

```text
Web search results for query: "LIBERO-Plus camera 2026 SOTA benchmark"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"VLA SOTA Leaderboard","url":"https://sota.evomind-tech.com/"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"Evo-SOTA.io/README.md at main · MINT-SJTU/Evo-SOTA.io","url":"https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"}]

Based on the search results, here's what I found about the LIBERO-Plus camera benchmark:

## LIBERO-Plus Overview

LIBERO Plus is an extended benchmark testing robustness across 7 perturbation dimensions: Camera, Robot, Language, Light, Background, Noise, and Layout.

## Camera View Performance (SOTA Results)

The method achieves a dramatic improvement in camera view robustness (92.8%), surpassing the next best model by 37.2 percentage points. This represents the current state-of-the-art performance specifically on the camera perturbation dimension of LIBERO-Plus.

## Key Findings on Camera Robustness

Models are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception. Altering camera position, orientation, or field-of-view causes dramatic performance drops, revealing models' dependence on fixed visual perspectives rather than true 3D understanding.

## Overall Benchmark Details

LIBERO-Plus is an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, and includes a diverse training dataset with over 20,000 successful trajectories collected under systematically varied conditions.

The benchmark reveals that while vision-language-action (VLA) models achieve high success rates on standard LIBERO evaluations, they remain brittle when subjected to camera viewpoint variations and other perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18bd5334-9249-4d55-818c-03428335d097",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "0118287b-d435-4ed8-a47f-f14e1366d774",
  "sourceToolAssistantUUID": "18bd5334-9249-4d55-818c-03428335d097",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T09:18:06.254Z_

Good! I found that the LIBERO-Plus paper (2510.13626) reports 92.8% camera score. Now let me verify which method this is from and check the AnyCamVLA paper more thoroughly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0118287b-d435-4ed8-a47f-f14e1366d774",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdxYewdsAJ5GyfuHnxM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf45fe5f-ff66-4bba-8ef1-b41116b2fcc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LgE2C38k51A11nBTebqgfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2378,
      "cache_read_input_tokens": 16925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2378,
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

_source line 10 · 2026-05-10T09:18:06.894Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TDbv5G1PMBJM9T7MLzDDfL`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "What is the name or title of the proposed method that achieves 92.8% on the camera axis? Is it AnyCamVLA or a different method? What is the method name?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf45fe5f-ff66-4bba-8ef1-b41116b2fcc8",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdxYewdsAJ5GyfuHnxM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "71ca590c-db52-4d1f-98e1-45fb2f72bdde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LgE2C38k51A11nBTebqgfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2378,
      "cache_read_input_tokens": 16925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2378,
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

_source line 11 · 2026-05-10T09:18:07.947Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KrpqJtkQHK5gH5rmqEXtyJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.05868",
  "prompt": "What is the full title and main contribution of this paper? Is this the AnyCamVLA paper? Does it report results on LIBERO-Plus? What camera robustness methods does it use - does it require known camera extrinsics at test time or is it end-to-end?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71ca590c-db52-4d1f-98e1-45fb2f72bdde",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdxYewdsAJ5GyfuHnxM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "75fbeae7-500b-4cfe-abc4-6c0978da6c1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LgE2C38k51A11nBTebqgfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2378,
      "cache_read_input_tokens": 16925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2378,
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

_source line 12 · 2026-05-10T09:18:08.108Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CwejKZp13HhWBwRN4jLBRn`</summary>

```json
{
  "query": "AnyCamVLA LIBERO-Plus camera"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75fbeae7-500b-4cfe-abc4-6c0978da6c1e",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdxYewdsAJ5GyfuHnxM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a7439a4a-9673-42e7-aa3f-5813e2d62ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LgE2C38k51A11nBTebqgfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2378,
      "cache_read_input_tokens": 16925,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2378
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 349,
          "cache_read_input_tokens": 16925,
          "cache_creation_input_tokens": 2378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2378,
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

_source line 13 · 2026-05-10T09:18:10.146Z_

<details><summary>↩ Tool result · `toolu_01TDbv5G1PMBJM9T7MLzDDfL`</summary>

```text
# Method Name for 92.8% Camera Performance

Based on the document, the method that achieves 92.8% on camera viewpoint robustness is not given a specific product name. Rather, it is described as a post-training approach based on OpenVLA-OFT.

The paper states: "Using this dataset, we performed mixed fine-tuning starting from the official OpenVLA-OFT weights" and refers to it as "+ PT" (post-training) in Table 2. The authors identify this as "our method" or "our post-training method."

The document does not introduce a named variant like "AnyCamVLA" or other proprietary title for this approach—it's presented as their robustness improvement strategy within the LIBERO-Plus framework.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71ca590c-db52-4d1f-98e1-45fb2f72bdde",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "7070b37e-e1c1-40a7-bb62-3b59d8661d19",
  "sourceToolAssistantUUID": "71ca590c-db52-4d1f-98e1-45fb2f72bdde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T09:18:11.633Z_

<details><summary>↩ Tool result · `toolu_01KrpqJtkQHK5gH5rmqEXtyJ`</summary>

```text
# AnyCamVLA Paper Summary

**Full Title:** "AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models"

**Yes, this is the AnyCamVLA paper.** It was submitted on March 6, 2026.

## Main Contribution

The paper addresses camera viewpoint sensitivity in Vision-Language-Action models through a zero-shot adaptation approach. The key innovation is using "a feed-forward novel view synthesis model which outputs high-quality target view images, handling both extrinsic and intrinsic parameters" to virtually adjust test-time camera observations to match training configurations without requiring fine-tuning or architectural changes.

## LIBERO Benchmark Results

The abstract mentions evaluation on the LIBERO benchmark, where the method "consistently outperforms baselines that use data augmentation for policy fine-tuning." However, the provided content does **not specify results on LIBERO-Plus** specifically.

## Camera Robustness Approach

The method operates as a "plug-and-play" approach that doesn't require known camera extrinsics at test time. Rather than being end-to-end learning, it uses feed-forward view synthesis to synthesize appropriate camera views, handling both extrinsic and intrinsic camera parameters automatically during inference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75fbeae7-500b-4cfe-abc4-6c0978da6c1e",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "7905671d-cf47-4712-8dcd-47ad2c5aca64",
  "sourceToolAssistantUUID": "75fbeae7-500b-4cfe-abc4-6c0978da6c1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T09:18:15.566Z_

<details><summary>↩ Tool result · `toolu_01CwejKZp13HhWBwRN4jLBRn`</summary>

```text
Web search results for query: "AnyCamVLA LIBERO-Plus camera"

Links: [{"title":"AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05868"},{"title":"[2603.05868] AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05868"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Liber Flip camera test, real footage! See to believe 😍 #liberoflip  | TikTok","url":"https://www.tiktok.com/@matt.camacho24/video/7511039375422065927"},{"title":"Libero Flip Phone Review: Affordable 8K Camera Quality","url":"https://www.tiktok.com/@einnaleondesu/video/7485935172391652615"},{"title":"AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.05868"},{"title":"Libero Flip Camera Review | TikTok","url":"https://www.tiktok.com/discover/libero-flip-camera-review"},{"title":"Libero Flip Front Camera Review","url":"https://www.tiktok.com/discover/libero-flip-front-camera-review"},{"title":"Libero Flip Phone Review Camera","url":"https://www.tiktok.com/discover/libero-flip-phone-review-camera"},{"title":"Libero Flip Camera Test ( DUE TO PUBLIC DEMAND ) - YouTube","url":"https://www.youtube.com/watch?v=PZMfsIDelPU"}]

Based on the search results, here's what I found about AnyCamVLA and LIBERO-Plus:

## AnyCamVLA

AnyCamVLA is a framework for zero-shot camera adaptation for viewpoint-robust Vision-Language-Action models. It proposes a zero-shot camera adaptation framework without additional demonstration data, policy fine-tuning, or architectural modification. The key idea is to virtually adjust test-time camera observations to match the training camera configuration in real-time using a feed-forward novel view synthesis model.

The method demonstrates minimal performance degradation even under large viewpoint shifts (up to 15 cm translation and 60° rotation in camera extrinsics), and it enhances viewpoint robustness in real-world robotic manipulation scenarios, including settings with varying camera extrinsics, intrinsics, and freely moving handheld cameras.

## LIBERO-Plus

LIBERO-Plus is used to construct multi-view simulation data by rendering diverse camera viewpoints using objects and scene textures. LIBERO-Plus offers comprehensive evaluation across seven robustness dimensions and 21 sub-dimensions for assessing model generalization.

The AnyCamVLA paper was published on March 6, 2026, and uses LIBERO-Plus as a benchmark for evaluating the robustness of Vision-Language-Action models for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7439a4a-9673-42e7-aa3f-5813e2d62ec4",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "afe815cd-33d6-49c0-9fb6-8fa83f8a9140",
  "sourceToolAssistantUUID": "a7439a4a-9673-42e7-aa3f-5813e2d62ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T09:18:17.735Z_

Let me get more specific details on AnyCamVLA's LIBERO-Plus camera performance numbers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afe815cd-33d6-49c0-9fb6-8fa83f8a9140",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdyNrs6GHFfn4jba6JZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "11d5fc6b-7a4e-465a-bfc8-a258b6183d59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014jLydxnrBhaGnmdawkcV2c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1703,
      "cache_read_input_tokens": 19303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1703,
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

_source line 17 · 2026-05-10T09:18:18.588Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018XDfwRB9xA9y2JdC7wXweq`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.05868",
  "prompt": "What are the specific quantitative results reported on LIBERO-Plus camera robustness? Look for tables showing camera axis scores, percentages, or accuracy numbers for AnyCamVLA and baseline methods on LIBERO-Plus."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11d5fc6b-7a4e-465a-bfc8-a258b6183d59",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdyNrs6GHFfn4jba6JZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8f12b6b4-1267-47f9-95e0-e85da488b670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014jLydxnrBhaGnmdawkcV2c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1703,
      "cache_read_input_tokens": 19303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1703,
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

_source line 18 · 2026-05-10T09:18:18.783Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GuLxsL15bd52fGdmRVPjei`</summary>

```json
{
  "query": "\"AnyCamVLA\" \"92.8\" LIBERO-Plus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f12b6b4-1267-47f9-95e0-e85da488b670",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdyNrs6GHFfn4jba6JZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9084d79-c96a-4f5f-be30-68c502162031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014jLydxnrBhaGnmdawkcV2c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1703,
      "cache_read_input_tokens": 19303,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1703
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 204,
          "cache_read_input_tokens": 19303,
          "cache_creation_input_tokens": 1703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1703,
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

_source line 19 · 2026-05-10T09:18:24.414Z_

<details><summary>↩ Tool result · `toolu_01GuLxsL15bd52fGdmRVPjei`</summary>

```text
Web search results for query: ""AnyCamVLA" "92.8" LIBERO-Plus"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"LIBERO-plus/index.html at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/index.html"},{"title":"Amazon.com: Libero","url":"https://www.amazon.com/libero/s?k=libero"},{"title":"Libero Academy","url":"https://www.liberoacademy.com/"},{"title":"ALLCAM PCW92ME 92\" HD Projector Screen | AVForums","url":"https://www.avforums.com/threads/allcam-pcw92me-92-hd-projector-screen.914011/"},{"title":"Choose Your Amount - SC Libero","url":"https://www.liberopodcast.com/sclibero"},{"title":"CMI: Libero CL - Multi-Use PDF Logger with USB and Bluetooth","url":"https://www.cmitest.com/produits/libero-cl/"},{"title":"RESTAURANT LIBERO, Omis - Restaurant Reviews, Photos & Phone Number - Tripadvisor","url":"https://www.tripadvisor.com/Restaurant_Review-g644074-d3578735-Reviews-Restaurant_Libero-Omis_Split_Dalmatia_County_Dalmatia.html"},{"title":"Top 9 și încă 80 Libero Scutece bebelusi (de la 21,03 lei)","url":"https://pepita.com/en/diapers-c1382;libero-f808"}]

Based on the search results, I found relevant information about your query. The terms you're searching for relate to a Vision-Language-Action (VLA) benchmark and evaluation results.

The 92.8% figure refers to a success rate achieved under camera perturbations in LIBERO-plus, surpassing the next best model by 37.2 percentage points. 

LIBERO-plus is a generalized benchmark for in-depth robustness analysis of vision-language-action models. The repository contains the official implementation and benchmark for research on in-depth robustness analysis for Vision-Language-Action models, systematically exposing hidden vulnerabilities through comprehensive robustness evaluation across seven perturbation dimensions.

However, I should note that the search results don't contain specific information about "AnyCamVLA" by that exact name. The 92.8% performance metric appears in performance tables for various VLA models tested on the LIBERO-plus benchmark, but I couldn't find a model explicitly identified as "AnyCamVLA" in the search results. If you have more context about this specific model or paper, that might help clarify the connection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9084d79-c96a-4f5f-be30-68c502162031",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "1661daf4-ef20-4828-b3ce-7ad2244fb375",
  "sourceToolAssistantUUID": "d9084d79-c96a-4f5f-be30-68c502162031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T09:18:25.793Z_

<details><summary>↩ Tool result · `toolu_018XDfwRB9xA9y2JdC7wXweq`</summary>

```text
# AnyCamVLA Results on LIBERO Camera Robustness

Based on the provided document, I cannot find specific quantitative results on **LIBERO-Plus** camera robustness. 

The paper does reference LIBERO-Plus in discussing the domain, noting that "Recent evaluations on LIBERO-Plus reveal substantial performance degradation under camera perturbations, with success rates dropping from over 90% to below 30%." However, these cited numbers refer to *baseline* VLA performance, not AnyCamVLA's results on LIBERO-Plus.

## What the Document Does Report

The actual quantitative results presented are from the standard **LIBERO benchmark** (not LIBERO-Plus), showing:

- **Agent camera perturbations** (Table I): AnyCamVLA achieved 94.5% average success rate across all perturbation levels, compared to π₀.₅'s 39.9% on large perturbations

- **Wrist camera perturbations** (Table II): AnyCamVLA achieved 88.6% average success rate versus π₀.₅'s 28.6%

The document does not provide a dedicated table with LIBERO-Plus evaluation results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f12b6b4-1267-47f9-95e0-e85da488b670",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "492994c3-07fd-4ee3-b501-bdb11e0ae686",
  "sourceToolAssistantUUID": "8f12b6b4-1267-47f9-95e0-e85da488b670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T09:18:27.147Z_

Let me check the LIBERO-Plus paper more carefully to identify which method exactly achieves 92.8%:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "492994c3-07fd-4ee3-b501-bdb11e0ae686",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Catdz8beG9ZoKgvvoWRwq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4684ffb0-c848-469c-a17b-30b076005271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H1xjg1qqRuY9A5YcKVQ9TX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 822,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 21006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 619,
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

_source line 22 · 2026-05-10T09:18:28.441Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LXWDRiBhK6NAEmm56bzUcY`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "In Table 2 showing camera axis scores, identify what the \"Proposed Method\" or the method achieving 92.8% is called. Is there an explicit name, acronym, or methodology description? Who are the authors and what is their institutional affiliation that might help identify the method?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4684ffb0-c848-469c-a17b-30b076005271",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Catdz8beG9ZoKgvvoWRwq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "babf5e80-d2f3-4324-a4d9-79e5bec17032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H1xjg1qqRuY9A5YcKVQ9TX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 822,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 21006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 619,
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

_source line 23 · 2026-05-10T09:18:28.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q1X6QiNqdUBx84c7QCwYpU`</summary>

```json
{
  "query": "LIBERO-Plus 2510.13626 authors proposed method 92.8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "babf5e80-d2f3-4324-a4d9-79e5bec17032",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Catdz8beG9ZoKgvvoWRwq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc351c68-f9ac-4fd6-b8a9-fc396e1d2c25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H1xjg1qqRuY9A5YcKVQ9TX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 822,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 21006,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 619
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 822,
          "output_tokens": 224,
          "cache_read_input_tokens": 21006,
          "cache_creation_input_tokens": 619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 619,
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

_source line 24 · 2026-05-10T09:18:31.769Z_

<details><summary>↩ Tool result · `toolu_01LXWDRiBhK6NAEmm56bzUcY`</summary>

```text
# Method Identification from Table 2

Based on the document, the method achieving 92.8% on the camera dimension is identified only as "Ours" in Table 2. 

The paper states: "Using this dataset, we performed mixed fine-tuning based on the official OpenVLA-OFT weights." The approach involves training on their generalized dataset comprising over 20,000 trajectories with systematic perturbations across seven dimensions.

However, the document does not assign an explicit acronym or standalone name to this proposed method beyond referring to it as "our method" or describing it in context of the LIBERO-Plus benchmark work. The authors are from Fudan University, Tongji University, Shanghai Innovation Institute, and National University of Singapore, with the project lead being Siyin Wang.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "babf5e80-d2f3-4324-a4d9-79e5bec17032",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "adbbe1eb-3f87-4586-93cb-e3bcb7e6ecb4",
  "sourceToolAssistantUUID": "babf5e80-d2f3-4324-a4d9-79e5bec17032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T09:18:33.735Z_

<details><summary>↩ Tool result · `toolu_01Q1X6QiNqdUBx84c7QCwYpU`</summary>

```text
Web search results for query: "LIBERO-Plus 2510.13626 authors proposed method 92.8"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626.pdf"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"},{"title":"5.92 kB","url":"https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata/resolve/main/README.md?download=true"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13626v2"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"}]

Based on the search results, I found information about the paper 2510.13626 "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models."

The authors of this paper are Senyu Fei, Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li Ji, Xinzhe He, Shiduo Zhang, Zhaoye Fei, Jinlan Fu, Jingjing Gong, and Xipeng Qiu.

Regarding the 92.8% metric: The proposed method exhibits a dramatic improvement in camera view robustness (92.8%), surpassing the next best model by 37.2 percentage points. Additionally, the method achieves the highest overall success rate (79.6%), outperforming all baseline models across nearly all perturbation types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc351c68-f9ac-4fd6-b8a9-fc396e1d2c25",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "f2be65d6-1cf1-4659-b42c-a075953073d0",
  "sourceToolAssistantUUID": "bc351c68-f9ac-4fd6-b8a9-fc396e1d2c25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T09:18:35.224Z_

Let me verify the claims about OA-WAM and search for any other 2026 papers that might have better camera performance:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2be65d6-1cf1-4659-b42c-a075953073d0",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdziZ4ZdmK6ZaijcGH6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cea19612-72e6-4721-8640-85518244c8cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TKpx6wgdQZjKYXkiMraejB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2036,
      "cache_read_input_tokens": 21625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2036,
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

_source line 27 · 2026-05-10T09:18:35.580Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DtD5unoRMr4i3b9Eyhgjch`</summary>

```json
{
  "query": "OA-WAM LIBERO-Plus camera 80.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cea19612-72e6-4721-8640-85518244c8cf",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdziZ4ZdmK6ZaijcGH6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "43cf1b37-d469-4808-807e-e67930c3b873",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TKpx6wgdQZjKYXkiMraejB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2036,
      "cache_read_input_tokens": 21625,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2036
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 140,
          "cache_read_input_tokens": 21625,
          "cache_creation_input_tokens": 2036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2036,
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

_source line 28 · 2026-05-10T09:18:35.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UYY8eUqhgKS6KEsLaStUtZ`</summary>

```json
{
  "query": "LIBERO-Plus camera axis benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43cf1b37-d469-4808-807e-e67930c3b873",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011CatdziZ4ZdmK6ZaijcGH6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c607b4b-b0d5-4f25-ba44-7968dac7b65b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TKpx6wgdQZjKYXkiMraejB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2036,
      "cache_read_input_tokens": 21625,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2036
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 140,
          "cache_read_input_tokens": 21625,
          "cache_creation_input_tokens": 2036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2036,
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

_source line 29 · 2026-05-10T09:18:41.721Z_

<details><summary>↩ Tool result · `toolu_01DtD5unoRMr4i3b9Eyhgjch`</summary>

```text
Web search results for query: "OA-WAM LIBERO-Plus camera 80.5"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"User guide for 2.4G Wire-Free Security Camera-(O-KAM Pro) – Rraycom","url":"https://rraycom.com/blogs/news/user-guide-for-bw4-and-bw5"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"OGI Inspector and OGI Inspector Plus","url":"https://infraredcameras.com/products/ogi-inspector-and-ogi-inspector-plus"},{"title":"Amazon.com : OM SYSTEM OLYMPUS C-8080 8MP Digital Camera with 5x Optical Wide Zoom : Point And Shoot Digital Cameras : Electronics","url":"https://www.amazon.com/Olympus-C-8080-Digital-Camera-Optical/dp/B0001DKLHS"},{"title":"Olympus Stylus 80 Film Camera Battery at Batteries Plus","url":"https://www.batteriesplus.com/battery/film-camera/olympus/stylus-80"},{"title":"O-KAM Pro Security Camera - 1080P Wireless Outdoor Camera with Night Vision, Motion Detection & 64GB SD Card - Walmart.com","url":"https://www.walmart.com/ip/O-KAM-Pro-Security-Camera-1080P-Wireless-Outdoor-Camera-with-Night-Vision-Motion-Detection/18442703909"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"Mini Wifi Camera, 1080P HD Wireless Wifi Camera Micro Camera for Home Long Life Battery Mini Camcorder Indoor Surveillance with Night Vision Motion Detection : Amazon.it: Electronics","url":"https://www.amazon.it/Telecamera-Microcamera-Videocamera-Sorveglianza-Rilevamento/dp/B09CKQX39N"},{"title":"WirelessCam System Max - aosu","url":"https://www.aosulife.com/products/wirelesscam-system-max"}]

Based on the search results, the query "OA-WAM LIBERO-Plus camera 80.5" doesn't appear to match a specific product or system exactly. However, the search results do provide relevant information about LIBERO-Plus:

LIBERO-Plus is a benchmark designed to rigorously evaluate generalization capabilities along key dimensions, particularly for robotic vision-language-action models. The benchmark comprises 10,030 tasks spanning seven perturbation factors with twenty-one low-level components.

The number "80.5" in your query doesn't clearly correspond to any specific metric in the LIBERO-Plus documentation. If you're looking for:
- **Performance metrics**: A method achieved the highest overall success rate (79.6%), with a dramatic improvement in camera view robustness (92.8%), and significant gains under noise (89.3%) and layout (77.6%) perturbations
- **Camera specifications**: LIBERO-Plus includes Camera Viewpoints perturbations that change the viewpoint/pose and field-of-view of the third-person camera

If you're searching for something different or if "OA-WAM" refers to a specific manufacturer or product line, please provide additional context and I can search for more specific information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43cf1b37-d469-4808-807e-e67930c3b873",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "376f8f83-a44e-44a2-954d-2cde8c036e4c",
  "sourceToolAssistantUUID": "43cf1b37-d469-4808-807e-e67930c3b873",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T09:18:42.319Z_

<details><summary>↩ Tool result · `toolu_01UYY8eUqhgKS6KEsLaStUtZ`</summary>

```text
Web search results for query: "LIBERO-Plus camera axis benchmark 2026"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"}]

Based on the search results, here's information about the LIBERO-Plus camera axis benchmark:

## Overview

LIBERO-Plus is an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, which includes evaluation of camera viewpoints as a key dimension.

## Camera Viewpoint Performance Results

The benchmark reveals significant findings about how VLA (Vision-Language-Action) models perform under camera perturbations:

- A method achieved 92.8% success rate under camera perturbations, surpassing the next best model by 37.2 percentage points
- Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations

## Specific Camera Perturbation Types

Camera viewpoint perturbations include position, orientation, and field-of-view changes. Models are most vulnerable to changes in camera viewpoint and robot initial state, with altering camera position, orientation, or field-of-view causing dramatic performance drops, revealing models' dependence on fixed visual perspectives rather than true 3D understanding.

## Benchmark Structure

LIBERO-Plus offers a robust benchmarking framework with 7 perturbation dimensions and 21 sub-dimensions, providing a fine-grained difficulty scale from L1 to L5.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c607b4b-b0d5-4f25-ba44-7968dac7b65b",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "7e72c0dd-e677-4d42-8b00-1bbda31409e4",
  "sourceToolAssistantUUID": "4c607b4b-b0d5-4f25-ba44-7968dac7b65b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T09:18:43.474Z_

Let me search more specifically for OA-WAM and look for other recent camera robustness methods:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e72c0dd-e677-4d42-8b00-1bbda31409e4",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate1MFRo4Jdx9JvcmGXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9ef93fdf-317c-4728-addd-5029e85fdb37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JY9kTbUSFeYCV2ZYB2qi3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 23661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1951,
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

_source line 32 · 2026-05-10T09:18:43.721Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HjVRtk6Cj3PHMneKY8HvTE`</summary>

```json
{
  "query": "\"OA-WAM\" camera robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ef93fdf-317c-4728-addd-5029e85fdb37",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate1MFRo4Jdx9JvcmGXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bce473bc-f20c-450b-91dc-00a495b6dab9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JY9kTbUSFeYCV2ZYB2qi3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 23661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1951,
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

_source line 33 · 2026-05-10T09:18:43.858Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gyu8WNeYbaq529ED5qo2CA`</summary>

```json
{
  "query": "LIBERO camera robustness 2026 paper new method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bce473bc-f20c-450b-91dc-00a495b6dab9",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate1MFRo4Jdx9JvcmGXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c12139a9-4b03-4d32-85a9-a26a14262abd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JY9kTbUSFeYCV2ZYB2qi3P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 23661,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1951
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 133,
          "cache_read_input_tokens": 23661,
          "cache_creation_input_tokens": 1951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1951,
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

_source line 34 · 2026-05-10T09:18:51.719Z_

<details><summary>↩ Tool result · `toolu_01HjVRtk6Cj3PHMneKY8HvTE`</summary>

```text
Web search results for query: ""OA-WAM" camera robustness"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"Validation of three-dimensional wound measurements using a novel 3D-WAM camera - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/30118155/"},{"title":"Robust Multi-object Tracking for Wide Area Motion Imagery | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8707377/"},{"title":"EC-WAMI: Event Camera-Based Pose Optimization in Remote Sensing and Wide-Area Motion Imagery - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11644785/"},{"title":"WAM front parking camera 360 calibration - OrBit Forums","url":"https://forums.spaycetech.com/showthread.php?tid=257"},{"title":"Wide-area Motion Imagery Intelligence | L3Harris® Fast. Forward.","url":"https://www.l3harris.com/all-capabilities/wide-area-motion-imagery-intelligence"},{"title":"I2VWM: Robust Watermarking for Image to Video Generation","url":"https://arxiv.org/html/2509.17773"},{"title":"Watermark Anything with Localized Messages","url":"https://arxiv.org/html/2411.07231"},{"title":"WAM camera calibration | D5T5.com","url":"https://d5t5.com/wiki/repairs/article-wamcameracalibration"}]

Based on the search results, I found information about OA-WAM in relation to camera robustness:

## OA-WAM: Object-Addressable World Action Model

OA-WAM makes world-action modeling object-addressable through a slot-aware decomposition with a 7B trunk that routes cross-slot attention through a frozen per-object identity address.

### Camera Robustness Performance

OA-WAM sets a new state-of-the-art (SOTA) on the geometric LIBERO-Plus axes with a Geo-Avg of 76.0. It leads on the camera and robot-initial-state axes of LIBERO-Plus, which are most directly aligned with its design hypothesis.

### How It Achieves Robustness

OA-WAM decomposes each frame into N+1 addressable object slots whose cross-slot attention key reads only the identity address subvector, keeping robust manipulation. The results show that explicitly organizing a world model as addressable object states is an effective path toward more robust robot manipulation under scene perturbations.

The key insight is that OA-WAM addresses the poor robustness of existing world action models under manipulation perturbations by providing stable per-object states so that language-conditioned action generation can directly query task-relevant objects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bce473bc-f20c-450b-91dc-00a495b6dab9",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "b8f525b3-e481-48c7-b94a-f232e06f3f00",
  "sourceToolAssistantUUID": "bce473bc-f20c-450b-91dc-00a495b6dab9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T09:18:52.290Z_

<details><summary>↩ Tool result · `toolu_01Gyu8WNeYbaq529ED5qo2CA`</summary>

```text
Web search results for query: "LIBERO camera robustness 2026 paper new method"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"[2603.05868] AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05868"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"}]

Based on the search results, I found several relevant papers on LIBERO camera robustness from 2026:

## LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models

The main paper found is LIBERO-Plus, which analyzes Visual-Language-Action (VLA) models by performing a systematic vulnerability analysis with controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

The analysis reveals critical weaknesses where models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

### New Method for Improving Camera Robustness

The researchers constructed LIBERO-Plus, an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, and created a diverse training dataset with over 20,000 successful trajectories collected under systematically varied conditions. Their proposed method achieves the highest overall success rate (79.6%), outperforming all baseline models across nearly all perturbation types, most notably with a dramatic improvement in camera view robustness (92.8%), surpassing the next best model by 37.2 percentage points.

## AnyCamVLA: Zero-Shot Camera Adaptation (March 2026)

Additionally, another recent paper proposes a zero-shot camera adaptation framework without additional demonstration data, policy fine-tuning, or architectural modification, with the key idea of virtually adjusting test-time camera observations to match the training camera configuration using a feed-forward novel view synthesis model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c12139a9-4b03-4d32-85a9-a26a14262abd",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "6b8f268e-bf3e-44f3-8f43-b17feae3bec1",
  "sourceToolAssistantUUID": "c12139a9-4b03-4d32-85a9-a26a14262abd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-10T09:18:53.743Z_

Excellent! Now I found OA-WAM. Let me get more specific details on OA-WAM's camera score:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b8f268e-bf3e-44f3-8f43-b17feae3bec1",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate25uURf97EkhQUa4x4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "40e93ca0-bdb1-422e-89d2-080e5b5b78d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V7sS8TkrY59sZBR9TTtqLz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 25612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1848,
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

_source line 37 · 2026-05-10T09:18:54.471Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NaaqcmX6FjpCKvbZfQGkzY`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06481v1",
  "prompt": "What are the specific camera axis scores reported for OA-WAM on LIBERO-Plus? What exact percentage or success rate does OA-WAM achieve on the camera perturbation axis? Compare with the baseline methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40e93ca0-bdb1-422e-89d2-080e5b5b78d5",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate25uURf97EkhQUa4x4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fdc33a51-15d4-493b-86df-c678dfd4c647",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V7sS8TkrY59sZBR9TTtqLz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 25612,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 160,
          "cache_read_input_tokens": 25612,
          "cache_creation_input_tokens": 1848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1848,
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

_source line 38 · 2026-05-10T09:18:58.517Z_

<details><summary>↩ Tool result · `toolu_01NaaqcmX6FjpCKvbZfQGkzY`</summary>

```text
# OA-WAM Camera Axis Performance on LIBERO-Plus

## OA-WAM's Camera Score

OA-WAM achieves **80.5%** success rate on the camera perturbation axis of LIBERO-Plus.

## Comparison with Baselines

According to Table 2 in the paper, here's how OA-WAM compares to other leading methods on the camera axis:

| Method | Camera Score |
|--------|--------------|
| OA-WAM | 80.5% |
| π0.5 | 75.4% |
| Cosmos-Policy | 75.8% |
| X-VLA | 23.4% |
| GE-Act | 60.7% |

The paper states that OA-WAM achieves "+4.7%" improvement over Cosmos-Policy, which represents "the prior best" on this axis. This camera performance is particularly significant because it demonstrates the model's robustness when viewpoint changes occur while object identities remain constant—exactly the scenario where the object-addressable design provides advantage.

The geometric average (combining camera, robot initial state, and layout axes) reaches 84.3%, representing a "+4.8%" gain over π0.5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdc33a51-15d4-493b-86df-c678dfd4c647",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "f0fb3b52-c064-4de8-9acf-35746151dbba",
  "sourceToolAssistantUUID": "fdc33a51-15d4-493b-86df-c678dfd4c647",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-10T09:18:59.793Z_

Perfect! Now let me verify the exact comparison between these methods and determine which is truly the SOTA:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0fb3b52-c064-4de8-9acf-35746151dbba",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate2YZMHtFL1b8XMUJpf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23dea9b3-ff26-428e-a0f6-e4de600291c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016BotRaLoEvwRw3vKS9Yaa2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 27460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 561,
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

_source line 40 · 2026-05-10T09:19:05.655Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFEY3AmkaNHjcmsEWPq4M4`</summary>

```json
{
  "query": "\"LIBERO-Plus\" camera \"92.8\" -80.5 method name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23dea9b3-ff26-428e-a0f6-e4de600291c8",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate2YZMHtFL1b8XMUJpf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "380b4421-5c5f-4887-bdfb-6577f9c59e91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016BotRaLoEvwRw3vKS9Yaa2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 27460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 561,
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

_source line 41 · 2026-05-10T09:19:07.398Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GukDJ6gcbFsZrCphfZBRqA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.13626",
  "prompt": "What is the full title of this paper and who are the authors? Is the proposed method that achieves 92.8% camera score compared against OA-WAM? What is the date of publication?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "380b4421-5c5f-4887-bdfb-6577f9c59e91",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate2YZMHtFL1b8XMUJpf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b9bc3306-27d5-4951-b1d2-066b84cd396a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016BotRaLoEvwRw3vKS9Yaa2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 27460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 561,
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

_source line 42 · 2026-05-10T09:19:11.366Z_

<details><summary>↩ Tool result · `toolu_01SFEY3AmkaNHjcmsEWPq4M4`</summary>

```text
Web search results for query: ""LIBERO-Plus" camera "92.8" -80.5 method name"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"ZTE Libero 5G IV - Specifications","url":"https://www.devicespecifications.com/en/model/698d5e8a"},{"title":"FlashPro for Libero SoC Design Suite v11.8 User Guide","url":"https://ww1.microchip.com/downloads/aemDocuments/documents/FPGA/core-docs/Libero/11_8_0/Tool/flashpro_ug.pdf"},{"title":"ZTE Libero 5G III - Specifications","url":"https://www.devicespecifications.com/en/model/85f65b98"},{"title":"FlashPro for Libero SoC v11.8 User Guide","url":"http://coredocs.s3.amazonaws.com/Libero/11_8_0/Tool/flashpro_ug.pdf"},{"title":"ZTE Libero Flip - Specifications","url":"https://www.devicespecifications.com/en/model/f83b5f2f"},{"title":"FlashPro User Guide Software v11.9","url":"https://coredocs.s3.amazonaws.com/Libero/11_8_4/Tool/flashpro_ug.pdf"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"}]

Based on the search results, I found relevant information about your query. The method achieves a dramatic improvement in camera view robustness (92.8%), surpassing the next best model by 37.2 percentage points.

The search results indicate this comes from a research paper on LIBERO-Plus, which is "In-depth Robustness Analysis for Vision-Language-Action Models". The 92.8% figure relates to camera robustness performance. However, the search results do not clearly identify a specific method name associated with the -80.5 value you mentioned, or provide the exact name of the method achieving this 92.8% camera robustness score. 

The results show various VLA (Vision-Language-Action) models being evaluated, and it appears this 92.8% score may be associated with a post-training or fine-tuning approach, but the specific method name for the -80.5 metric is not clearly detailed in the available search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "380b4421-5c5f-4887-bdfb-6577f9c59e91",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "15b1a681-6330-4c78-a60e-5eb58203f0e3",
  "sourceToolAssistantUUID": "380b4421-5c5f-4887-bdfb-6577f9c59e91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T09:19:15.329Z_

<details><summary>↩ Tool result · `toolu_01GukDJ6gcbFsZrCphfZBRqA`</summary>

```text
# LIBERO-Plus Paper Analysis

**Full Title:** "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"

**Authors:** The paper has 13 authors, led by Senyu Fei, along with Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li Ji, Xinzhe He, Shiduo Zhang, Zhaoye Fei, Jinlan Fu, Jingjing Gong, and Xipeng Qiu.

**Method Comparison:** The provided content does not contain information about a 92.8% camera score or comparisons with OA-WAM. The abstract discusses performance drops from 95% to below 30% under perturbations but doesn't reference the specific metric you mentioned.

**Publication Date:** The paper was submitted on October 15, 2025, with the most recent version (v3) released on December 26, 2025. It is classified under arXiv identifier 2510.13626 in the Robotics category.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9bc3306-27d5-4951-b1d2-066b84cd396a",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "9d0efa52-7eff-4dde-a53f-8c5cc7677d91",
  "sourceToolAssistantUUID": "b9bc3306-27d5-4951-b1d2-066b84cd396a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-10T09:19:16.708Z_

Let me check if the LIBERO-Plus paper's proposed method is actually the SOTA or if it compares against OA-WAM:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d0efa52-7eff-4dde-a53f-8c5cc7677d91",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate3nPaLPF5QL9YcLuzH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e78acd7-6243-4a00-9e13-303aef261670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SBRmq1nutsnqtL9EN5Ysfw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1276,
      "cache_read_input_tokens": 28021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1276,
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

_source line 45 · 2026-05-10T09:19:17.559Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NbS4vJh3CPryTXf2yq41Wf`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "Does Table 2 or the results section compare against OA-WAM or any method achieving 80.5% on camera? Is OA-WAM listed as a baseline in the evaluation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e78acd7-6243-4a00-9e13-303aef261670",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate3nPaLPF5QL9YcLuzH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3ff1b062-c703-4a15-ac31-d8c406a35866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SBRmq1nutsnqtL9EN5Ysfw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1276,
      "cache_read_input_tokens": 28021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1276,
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

_source line 46 · 2026-05-10T09:19:17.814Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Z3t3pMNiyYx7VXgHao4dd`</summary>

```json
{
  "query": "OA-WAM arxiv 2605.06481 published date 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ff1b062-c703-4a15-ac31-d8c406a35866",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate3nPaLPF5QL9YcLuzH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0e11eae8-1ef0-438b-b15f-ae73f5e5f3c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SBRmq1nutsnqtL9EN5Ysfw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1276,
      "cache_read_input_tokens": 28021,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1276
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 211,
          "cache_read_input_tokens": 28021,
          "cache_creation_input_tokens": 1276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1276,
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

_source line 47 · 2026-05-10T09:19:21.031Z_

<details><summary>↩ Tool result · `toolu_01NbS4vJh3CPryTXf2yq41Wf`</summary>

```text
# Response

Based on my review of the provided document, **OA-WAM is not mentioned anywhere** in this paper, nor does any baseline achieve 80.5% on camera viewpoint robustness prior to the authors' method.

In Table 2 (the main robustness evaluation table), the baseline models listed are:
- OpenVLA
- OpenVLA-OFT
- OpenVLA-OFT_w
- NORA
- WorldVLA
- UniVLA
- π0 and π0-Fast
- RIPT-VLA
- OpenVLA-OFT_m

The highest camera robustness score among baselines is 65.1% (π0-Fast), while the authors' proposed method achieves "92.8%" on camera perturbations. There is no reference to OA-WAM or any competing method achieving approximately 80.5% camera robustness in this document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ff1b062-c703-4a15-ac31-d8c406a35866",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "158a8e29-3626-4376-b9e0-e65ad9ff04dc",
  "sourceToolAssistantUUID": "3ff1b062-c703-4a15-ac31-d8c406a35866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T09:19:24.092Z_

<details><summary>↩ Tool result · `toolu_018Z3t3pMNiyYx7VXgHao4dd`</summary>

```text
Web search results for query: "OA-WAM arxiv 2605.06481 published date 2026"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"Top arXiv papers","url":"https://scirate.com/?date=2026-06-30&page=7&range=56"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"Operator Algebras Apr 2026","url":"https://arxiv.org/list/math.OA/current"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"To appear in the IEEE Symposium on Security & Privacy, May 2026 SoK: After Decades of Web Tracker Detection, What’s Next?","url":"https://arxiv.org/html/2605.02982"},{"title":"1 Introduction","url":"https://arxiv.org/html/2605.03501"}]

Based on the search results, I found information about the OA-WAM paper with arxiv ID 2605.06481:

The paper "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation" was published on May 7, 2026. 

The paper is authored by Yushan Liu, Peibo Sun, Shoujie Li, Yifan Xie, Lingfeng Zhang, Xintao Chao, Shiyuan Dong, Fang Chen, Xiao-Ping Zhang, and Wenbo Ding, and was submitted on May 8, 2026.

OA-WAM is an Object-Addressable World Action Model for robust robot manipulation that decomposes each frame into N+1 slot states, with one robot slot and N object slots.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e11eae8-1ef0-438b-b15f-ae73f5e5f3c0",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "74bb8004-2c56-4500-a8fe-3b6017bb3aad",
  "sourceToolAssistantUUID": "0e11eae8-1ef0-438b-b15f-ae73f5e5f3c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-10T09:19:25.286Z_

Perfect! Now I have the key information. Let me verify the publication timeline to ensure we have the correct SOTA:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74bb8004-2c56-4500-a8fe-3b6017bb3aad",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate4S1WYyJ8DXofUbFQW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6b42a866-6d9a-4927-8869-7f4b7b1e0df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GyaLgCWBVB6vKR8EKBn477",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 29297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
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

_source line 50 · 2026-05-10T09:19:25.711Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CnfWtjDeoTm6pCMwz4me3K`</summary>

```json
{
  "query": "\"2510.13626\" LIBERO-Plus submission date October 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b42a866-6d9a-4927-8869-7f4b7b1e0df6",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate4S1WYyJ8DXofUbFQW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "255209b6-bd6b-4564-b621-ecb943eb9a58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GyaLgCWBVB6vKR8EKBn477",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 29297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
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

_source line 51 · 2026-05-10T09:19:25.975Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HWt5RBTD2dFVjG4ufYEHMj`</summary>

```json
{
  "query": "LIBERO-Plus 92.8 camera method name OpenVLA-OFT fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "255209b6-bd6b-4564-b621-ecb943eb9a58",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate4S1WYyJ8DXofUbFQW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d094c5db-33d0-4e1d-8531-57094600d3c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GyaLgCWBVB6vKR8EKBn477",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 29297,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1124
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 152,
          "cache_read_input_tokens": 29297,
          "cache_creation_input_tokens": 1124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1124,
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

_source line 52 · 2026-05-10T09:19:30.028Z_

<details><summary>↩ Tool result · `toolu_01CnfWtjDeoTm6pCMwz4me3K`</summary>

```text
Web search results for query: ""2510.13626" LIBERO-Plus submission date October 2025"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626.pdf"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"Libero® SoC Design Suite Versions 2025.2 to 12.0 | Microchip Technology","url":"https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/fpga/libero-software-later-versions"},{"title":"User Guide © 2025 Microchip Technology Inc. and its subsidiaries","url":"https://ww1.microchip.com/downloads/aemDocuments/documents/FPGA/swdocs/libero/libero_ecf_ug_2025_1.pdf"},{"title":"Release Notes - Libero SoC v2025.2","url":"https://ww1.microchip.com/downloads/aemdocuments/documents/FPGA/swdocs/libero/libero_soc_v2025_2_release_notes.pdf"}]

Based on the search results, here's the information about the LIBERO-Plus submission:

The paper "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" (arXiv:2510.13626) was submitted on October 15, 2025.

The paper presents a systematic vulnerability analysis of Visual-Language-Action (VLA) models by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

The analysis found that models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "255209b6-bd6b-4564-b621-ecb943eb9a58",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "ef8a0914-c9a6-4a8f-bc20-870e47747752",
  "sourceToolAssistantUUID": "255209b6-bd6b-4564-b621-ecb943eb9a58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-10T09:19:32.693Z_

<details><summary>↩ Tool result · `toolu_01HWt5RBTD2dFVjG4ufYEHMj`</summary>

```text
Web search results for query: "LIBERO-Plus 92.8 camera method name OpenVLA-OFT fine-tuning"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"},{"title":"OpenVLA · OFT | Konnex Docs","url":"https://docs.konnex.world/supported-ai-models/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"}]

Based on the search results, I can provide you with information about the 92.8% camera view robustness metric and OpenVLA-OFT fine-tuning:

## LIBERO-Plus 92.8 Camera Method

The method achieves a dramatic improvement in camera view robustness (92.8%), surpassing the next best model by 37.2 percentage points. This result comes from research on the LIBERO-Plus benchmark, which is an in-depth robustness analysis of vision-language-action models.

## OpenVLA-OFT Fine-Tuning Method

The Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications.

Key aspects of the OpenVLA-OFT approach include:

- OpenVLA-OFT is a parallel decoding variant enabling simultaneous prediction of all actions in a single forward pass, employing continuous action representations through a multi-layer MLP head and trained with an L1 regression objective.

- OpenVLA is fine-tuned with LoRA instead of full fine-tuning.

- The parallel decoding with action chunking alone contributed a 14% absolute improvement in success rate, while continuous action representations added another 5% improvement.

The 92.8% camera robustness result represents state-of-the-art performance on the LIBERO-Plus benchmark when using this optimized fine-tuning approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d094c5db-33d0-4e1d-8531-57094600d3c8",
  "isSidechain": true,
  "promptId": "b3b08c0e-c354-4480-a9ae-2d31e2de6989",
  "agentId": "ae94922ca10442e5c",
  "type": "user",
  "uuid": "7b7dd268-86a5-4a7a-86f2-e74122e2a200",
  "sourceToolAssistantUUID": "d094c5db-33d0-4e1d-8531-57094600d3c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-10T09:19:41.261Z_

Now let me verify whether LIBERO-Plus paper was published before or after OA-WAM, and get the final clarity:

Based on my thorough research, here is the current SOTA on the LIBERO-Plus camera perturbation axis:

## Current SOTA: LIBERO-Plus Proposed Method (92.8%)

**The State-of-the-Art is 92.8% camera robustness**, achieved by the proposed method in the LIBERO-Plus paper (arXiv:2510.13626), submitted October 15, 2025.

### Key Details:

**Method:** The LIBERO-Plus authors' proposed approach based on OpenVLA-OFT fine-tuning on their newly constructed generalized dataset (20,000+ trajectories with systematic camera perturbations across 7 dimensions)

**Camera Score:** 92.8% (surpasses next best by 37.2 percentage points)

**Paper:** "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" by Senyu Fei, Siyin Wang, and 11 co-authors from Fudan University, Tongji University, and National University of Singapore

**Method Type:** End-to-end fine-tuned VLA (vision-language-action) model - NOT a camera adaptation method requiring known extrinsics at test time

### Important Finding About OA-WAM:

OA-WAM (arXiv:2605.06481), submitted May 8, 2026, reports 80.5% camera robustness on LIBERO-Plus. This is **NOT competitive with the LIBERO-Plus benchmark's own proposed method.**

However, OA-WAM is dated **after** the LIBERO-Plus paper's submission (May 2026 vs October 2025), so technically OA-WAM would be a later publication, but **it does not beat 92.8%**.

### Verification on AnyCamVLA:

AnyCamVLA (arXiv:2603.05868, March 6, 2026) reports camera robustness on the **standard LIBERO benchmark** (not LIBERO-Plus specifically):
- Agent camera perturbations: 94.5%
- Wrist camera perturbations: 88.6%

However, AnyCamVLA does NOT report specific LIBERO-Plus camera axis results, so it cannot be directly compared.

## Conclusion:

**The claim that OA-WAM at 80.5% is the SOTA on LIBERO-Plus camera axis is incorrect.** The LIBERO-Plus benchmark paper itself (published October 2025, before OA-WAM in May 2026) demonstrates a superior method achieving 92.8% camera robustness. This is the current published SOTA on the LIBERO-Plus camera perturbation axis.

---

Sources:
- [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626)
- [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/html/2605.06481v1)
- [AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models](https://arxiv.org/abs/2603.05868)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b7dd268-86a5-4a7a-86f2-e74122e2a200",
  "isSidechain": true,
  "agentId": "ae94922ca10442e5c",
  "requestId": "req_011Cate54eQScC9wi5hb5kKf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a287f669-6e56-4a07-bf9f-f4dc0847b6a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "774e368e-31bc-4158-9f0b-e4acf2311522",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WWb2hnGHThv7p5HAvYYRiU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1964,
      "cache_read_input_tokens": 30421,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1964
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 791,
          "cache_read_input_tokens": 30421,
          "cache_creation_input_tokens": 1964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1964,
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
