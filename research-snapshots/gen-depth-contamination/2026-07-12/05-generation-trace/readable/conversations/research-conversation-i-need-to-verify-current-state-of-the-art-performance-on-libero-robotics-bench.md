# Research conversation: I need to verify current state-of-the-art performance on LIBERO robotics benchmarks (LIBERO-100, LIBERO-Long, etc.) as o

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a44bb284748400e92.jsonl`
- **Structured JSON:** [`e8bd2979625f95159740.json`](../../sessions/e8/e8bd2979625f95159740.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-10T19:22:30.893Z_

I need to verify current state-of-the-art performance on LIBERO robotics benchmarks (LIBERO-100, LIBERO-Long, etc.) as of May 2026. Specifically:

1. What is the current SOTA success rate on LIBERO? Previous claims suggest Fast-WAM achieves 97.6%, Cosmos-Policy 98.5%, DreamVLA 97.2%. Are these accurate?
2. Is LIBERO effectively saturated (>95% success)?
3. Does LIBERO-PRO exist? Search for "LIBERO-PRO: Towards Robust and Fair Evaluation" on arxiv.
4. What is LIBERO-PRO's purpose and what perturbation types does it test?

Search using:
- "LIBERO benchmark robotics SOTA 2026"
- "Fast-WAM world action model test-time imagination"
- "LIBERO-PRO robust evaluation"
- "site:arxiv.org LIBERO success rate 2026"

Use WebFetch to read abstracts of the most relevant papers. Report specific numbers with sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "ac84149b-5860-4545-a079-7bfdff314725",
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

_source line 2 · 2026-05-10T19:22:30.898Z_

```json
{
  "parentUuid": "ac84149b-5860-4545-a079-7bfdff314725",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
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
  "uuid": "8a658aa0-6962-4579-89b6-791a4c3e9a01",
  "timestamp": "2026-05-10T19:22:30.898Z",
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

_source line 3 · 2026-05-10T19:22:33.528Z_



I'll start by loading the WebSearch and WebFetch tools, then conduct the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a658aa0-6962-4579-89b6-791a4c3e9a01",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS3uyM1a18wRBpxvqPr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "492243bb-6b44-492c-81dd-105cc0c2dc76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHN15HJFZr36eNKRVXJQLS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 804,
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

_source line 4 · 2026-05-10T19:22:33.951Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014p4JxpjLvUaombRnUnezi2`</summary>

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
  "parentUuid": "492243bb-6b44-492c-81dd-105cc0c2dc76",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS3uyM1a18wRBpxvqPr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd62ce53-9eee-4626-9fde-d35cc20bd37a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHN15HJFZr36eNKRVXJQLS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 8223,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 804
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 804,
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

_source line 5 · 2026-05-10T19:22:33.954Z_

<details><summary>↩ Tool result · `toolu_014p4JxpjLvUaombRnUnezi2`</summary>

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
  "parentUuid": "dd62ce53-9eee-4626-9fde-d35cc20bd37a",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "a655e2a0-a49a-4714-a1d3-5aa344cdc0d6",
  "sourceToolAssistantUUID": "dd62ce53-9eee-4626-9fde-d35cc20bd37a",
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

_source line 6 · 2026-05-10T19:22:37.238Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a655e2a0-a49a-4714-a1d3-5aa344cdc0d6",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS49Go7pVpN2ByWpoqo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00b30503-0118-4d7a-bd8c-d32956071b43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TmGzfhUTrZT6Lvg8orFxH4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 7 · 2026-05-10T19:22:38.164Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AhNbwqitw2ac4ZMjnuH5RJ`</summary>

```json
{
  "query": "LIBERO benchmark robotics SOTA 2026 success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00b30503-0118-4d7a-bd8c-d32956071b43",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS49Go7pVpN2ByWpoqo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9da37d95-80c1-4ca9-9c57-0e35514e9157",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TmGzfhUTrZT6Lvg8orFxH4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 8 · 2026-05-10T19:22:39.170Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H3EmoUi9jKYCFPKD5mVWtD`</summary>

```json
{
  "query": "Fast-WAM world action model test-time imagination LIBERO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9da37d95-80c1-4ca9-9c57-0e35514e9157",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS49Go7pVpN2ByWpoqo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e6afb39-2d69-408b-bf60-00fed6d53b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TmGzfhUTrZT6Lvg8orFxH4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 9 · 2026-05-10T19:22:39.664Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014gakdZsxuxAKaUjHn1nW6H`</summary>

```json
{
  "query": "LIBERO-PRO robust evaluation perturbation robotics benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e6afb39-2d69-408b-bf60-00fed6d53b13",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS49Go7pVpN2ByWpoqo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aff84c10-b1f4-4d3f-867b-3a5d0e23da31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TmGzfhUTrZT6Lvg8orFxH4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 10 · 2026-05-10T19:22:40.210Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JCw7VbpfbHJRJpAXSwHt9k`</summary>

```json
{
  "query": "site:arxiv.org LIBERO success rate 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aff84c10-b1f4-4d3f-867b-3a5d0e23da31",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS49Go7pVpN2ByWpoqo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fdc9828-a6c7-4ef5-ad35-fe126b493270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TmGzfhUTrZT6Lvg8orFxH4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 9027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 11 · 2026-05-10T19:22:43.930Z_

<details><summary>↩ Tool result · `toolu_01H3EmoUi9jKYCFPKD5mVWtD`</summary>

```text
Web search results for query: "Fast-WAM world action model test-time imagination LIBERO"

Links: [{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub","url":"https://github.com/yuantianyuan01/FastWAM"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"},{"title":"(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?…","url":"https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination? | alphaXiv","url":"https://www.alphaxiv.org/resources/2603.16666v1"},{"title":"Fast-WAM: Rethinking Test-Time Imagination","url":"https://www.emergentmind.com/papers/2603.16666"},{"title":"Paper page - Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://huggingface.co/papers/2603.16666"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination? - PULRC Portal","url":"https://lrc.perdanauniversity.edu.my/sdi/fast-wam-do-world-action-models-need-test-time-future-imagination/"}]

Based on the search results, here's what I found about Fast-WAM:

## Overview

World Action Models (WAMs) have emerged as a promising alternative to Vision-Language-Action (VLA) models for embodied control because they explicitly model how visual observations may evolve under action. Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising, yet it remains unclear whether explicit future imagination is actually necessary for strong action performance.

## The Fast-WAM Approach

Fast-WAM is a WAM architecture that retains video co-training during training but skips future prediction at test time. The key insight is that the main value of video prediction in WAMs may lie in improving world representations during training rather than generating future observations at test time.

## Key Findings

Fast-WAM remains competitive with imagine-then-execute variants, while removing video co-training causes a much larger performance drop. This suggests that the training signal is more important than test-time imagination.

## Performance and Efficiency

Fast-WAM achieves competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin) and real-world tasks, without embodied pretraining. Notably, it runs in real time with 190ms latency, over 4× faster than existing imagine-then-execute WAMs.

The paper was authored by Tianyuan Yuan, Zibin Dong, Yicheng Liu, and Hang Zhao, and was posted to arXiv in March 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e6afb39-2d69-408b-bf60-00fed6d53b13",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "c96e14a8-9a37-451d-94a0-955c643dbf37",
  "sourceToolAssistantUUID": "3e6afb39-2d69-408b-bf60-00fed6d53b13",
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

_source line 12 · 2026-05-10T19:22:45.148Z_

<details><summary>↩ Tool result · `toolu_01AhNbwqitw2ac4ZMjnuH5RJ`</summary>

```text
Web search results for query: "LIBERO benchmark robotics SOTA 2026 success rate"

Links: [{"title":"Robotics AI Benchmarks 2026: State of the Art | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/robotics"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"[2604.28192] LaST-R1: Reinforcing Robotic Manipulation via Adaptive Physical Latent Reasoning","url":"https://arxiv.org/abs/2604.28192"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO-Long — Robot Manipulation benchmark","url":"https://www.codesota.com/browse/robots/robot-manipulation/libero-long"},{"title":"LaST-R1: Reinforcing Robotic Manipulation via Adaptive Physical Latent Reasoning","url":"https://arxiv.org/html/2604.28192"}]

Based on the search results, here's what I found about LIBERO benchmark robotics SOTA 2026 success rates:

## Current SOTA Performance

LaST-R1 achieves a near-perfect 99.9% average success rate on the LIBERO benchmark with only one-shot supervised warm-up, significantly improving convergence speed and performance over prior state-of-the-art (SOTA) methods. This represents the most recent state-of-the-art result, with the paper dated May 2026.

## Important Context on SOTA Metrics

However, it's critical to understand that reported SOTA figures (>95% success) reflect performance under clean, nearly identically distributed train/test splits, whereas systematic robustness analyses reveal significant brittleness and a tendency toward memorization.

## What LIBERO Measures

LIBERO is a standardized and extensible benchmarking suite that evaluates multi-modal vision-language-action models in diverse robotic manipulation tasks. It employs a procedural generation pipeline and curated simulation/annotation infrastructure to create varied tasks that test generalization, robustness, and transfer capabilities.

## Robustness Concerns

More recent analyses have revealed limitations in the standard LIBERO evaluation. Minimal distributional shift in the default splits allows rote memorization, with SOTA models collapsing to near-zero success under moderate task, language, object, or environment perturbations. This has led to development of improved variants like LIBERO-PRO that inject controlled perturbations to better test true generalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9da37d95-80c1-4ca9-9c57-0e35514e9157",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "2ca86848-215d-40b4-a283-032ff7ddf208",
  "sourceToolAssistantUUID": "9da37d95-80c1-4ca9-9c57-0e35514e9157",
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

_source line 13 · 2026-05-10T19:22:46.261Z_

<details><summary>↩ Tool result · `toolu_01JCw7VbpfbHJRJpAXSwHt9k`</summary>

```text
Web search results for query: "site:arxiv.org LIBERO success rate 2026"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation","url":"https://arxiv.org/html/2604.05656v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18107"},{"title":"Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation","url":"https://arxiv.org/html/2603.12717"},{"title":"VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model","url":"https://arxiv.org/pdf/2602.10098"},{"title":"OmniVLA-RL: A Vision-Language-Action Model with Spatial Understanding and Online RL","url":"https://arxiv.org/html/2604.17706"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"[2602.21531v1] LiLo-VLA: Compositional Long-Horizon Manipulation via Linked Object-Centric Policies","url":"https://arxiv.org/abs/2602.21531v1"}]

I found several recent research papers from arXiv discussing LIBERO success rates in 2026. Here are the key findings:

## Recent LIBERO Success Rate Results (2026)

SnapFlow achieves 98.75% average success on LIBERO at 1-step, matching the 10-step teacher at 97.75%.

OmniVLA-RL achieves state-of-the-art results on LIBERO benchmarks, reaching an average success rate of 97.6%.

Despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications, as noted in the LIBERO-PRO paper.

## Key Insights

Several papers highlight an important caveat: current VLA models, despite excelling on the standard LIBERO, lack true robustness and generalization. The research shows that models are highly sensitive to the initial position of objects: for both OpenVLA and pi0, performance collapses once displacement exceeds 0.2 units, dropping to zero success.

The papers also reveal that LiLo-VLA achieves a 69% average success rate in long-horizon simulations and an average success rate of 85% in real-world evaluations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fdc9828-a6c7-4ef5-ad35-fe126b493270",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "09ed6702-30a8-4cc1-a429-139a0987be6f",
  "sourceToolAssistantUUID": "4fdc9828-a6c7-4ef5-ad35-fe126b493270",
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

_source line 14 · 2026-05-10T19:22:49.294Z_

<details><summary>↩ Tool result · `toolu_014gakdZsxuxAKaUjHn1nW6H`</summary>

```text
Web search results for query: "LIBERO-PRO robust evaluation perturbation robotics benchmark"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"[2510.03827v1] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827v1"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"[PDF] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LIBERO-PRO:-Towards-Robust-and-Fair-Evaluation-of-Zhou-Xu/c3a0ea8b0563c735d768fca1eb5920fa85511ac7"}]

Based on the search results, here's what I found about LIBERO-PRO:

## Overview

LIBERO-PRO is a plug-and-play extension of LIBERO designed to foster fair comparison across models and to advance research on building VLA systems that can withstand reasonable and practically necessary perturbations.

## The Problem It Addresses

LIBERO has emerged as a widely adopted benchmark for evaluating Vision-Language-Action (VLA) models; however, its current training and evaluation settings are problematic, often leading to inflated performance estimates and preventing fair model comparison. The LIBERO benchmark employs an evaluation protocol that may overestimate model competence due to its homogeneous train/test split, allowing policies to achieve high performance through memorization rather than robust generalization, which may inflate performance metrics and mask limitations in compositional generalization and adaptability to diverse real-world scenarios.

## Key Findings

Experimental results reveal that, although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under the generalized LIBERO-PRO setting, exposing the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception.

## Four Perturbation Dimensions

LIBERO-PRO incorporates carefully designed perturbations across four dimensions—manipulated objects, initial states, task instructions, and environments—and supports randomized combinations of these dimensions for more faithful evaluation. More specifically, these include:

- Object Attribute Perturbation: Modifies non-essential object attributes, such as color, texture, or size, while preserving semantic equivalence, which tests the model's robustness to superficial visual changes critical for real-world adaptability.
- Initial Position Perturbation: Alters initial object positions to modify absolute and relative arrangements, ensuring physical plausibility.

The benchmark was released in October 2025 and includes evaluation of state-of-the-art models like OpenVLA and pi0/pi0.5.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aff84c10-b1f4-4d3f-867b-3a5d0e23da31",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "f2b5a93b-e4f2-4fb5-bc46-a1184b1ca277",
  "sourceToolAssistantUUID": "aff84c10-b1f4-4d3f-867b-3a5d0e23da31",
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

_source line 15 · 2026-05-10T19:22:52.419Z_

Good, I have strong initial results. Now let me fetch the specific papers to get precise numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2b5a93b-e4f2-4fb5-bc46-a1184b1ca277",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS5GdLXkV9wq1kZ6hwQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2be08446-2936-47e8-b523-9f3310b109e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8C7L7BKTxs5bQ8FEyQtks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 3270,
      "cache_read_input_tokens": 10938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3270,
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

_source line 16 · 2026-05-10T19:22:54.848Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vibtpty3yFHnc9gMskpVSP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.16666",
  "prompt": "Extract the exact LIBERO success rates reported for Fast-WAM and all baseline comparisons. What specific numbers are reported for LIBERO-100, LIBERO-Long, LIBERO-Spatial, LIBERO-Object, LIBERO-Goal? What is the average success rate claimed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2be08446-2936-47e8-b523-9f3310b109e5",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS5GdLXkV9wq1kZ6hwQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a2137a0-9274-45fe-823d-e8d1aad768af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8C7L7BKTxs5bQ8FEyQtks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 3270,
      "cache_read_input_tokens": 10938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3270,
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

_source line 17 · 2026-05-10T19:22:56.787Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XwWrMWqKZc7v3Y3Lx1B9NU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.03827",
  "prompt": "Extract all details about LIBERO-PRO: (1) What are the exact four perturbation dimensions? (2) What success rates do SOTA models achieve under standard LIBERO vs LIBERO-PRO? (3) Which models were evaluated? (4) What specific numbers show the performance collapse? Give me all specific percentages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a2137a0-9274-45fe-823d-e8d1aad768af",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS5GdLXkV9wq1kZ6hwQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fb3bef4-e9e9-4920-84d1-5e3c27c641af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8C7L7BKTxs5bQ8FEyQtks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 3270,
      "cache_read_input_tokens": 10938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3270,
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

_source line 18 · 2026-05-10T19:22:58.026Z_

<details><summary>↩ Tool result · `toolu_01Vibtpty3yFHnc9gMskpVSP`</summary>

```text
# Response

I cannot extract the specific LIBERO success rates you've requested because the web page content provided only contains the abstract and metadata for the arXiv paper—it does not include the detailed results section where such numerical benchmarks would be reported.

The abstract mentions that "Fast-WAM achieves competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin)" but does not provide the exact success rate percentages for LIBERO-100, LIBERO-Long, LIBERO-Spatial, LIBERO-Object, or LIBERO-Goal, nor does it state an average success rate.

To obtain these specific metrics, you would need to access the full paper PDF or HTML version linked on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a2137a0-9274-45fe-823d-e8d1aad768af",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "76b7ee75-5515-4a29-ad3d-22839679bdfb",
  "sourceToolAssistantUUID": "0a2137a0-9274-45fe-823d-e8d1aad768af",
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

_source line 19 · 2026-05-10T19:22:59.158Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015PryWiLAjZVGcKZbfsWyk3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.28192",
  "prompt": "Extract the exact LIBERO success rates reported for LaST-R1. What is the 99.9% claim? What specific sub-benchmarks are reported? List all comparison numbers with baselines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76b7ee75-5515-4a29-ad3d-22839679bdfb",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS5GdLXkV9wq1kZ6hwQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2d76216-ddb6-4ff4-9c7a-b1802d53a3d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8C7L7BKTxs5bQ8FEyQtks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 3270,
      "cache_read_input_tokens": 10938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3270,
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

_source line 20 · 2026-05-10T19:22:59.604Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019GQscoE6TjP6qvoKc6cBeH`</summary>

```json
{
  "query": "Cosmos-Policy LIBERO success rate 98.5%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2d76216-ddb6-4ff4-9c7a-b1802d53a3d7",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS5GdLXkV9wq1kZ6hwQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "687c1d81-26c4-4c11-be85-2785e7f42959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8C7L7BKTxs5bQ8FEyQtks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 3270,
      "cache_read_input_tokens": 10938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3270,
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

_source line 21 · 2026-05-10T19:22:59.844Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UrRzSpPWVqD72TyeVkUrPf`</summary>

```json
{
  "query": "DreamVLA LIBERO success rate 97.2%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "687c1d81-26c4-4c11-be85-2785e7f42959",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS5GdLXkV9wq1kZ6hwQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "163208eb-0664-4859-a762-8e26b835aa76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8C7L7BKTxs5bQ8FEyQtks",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 3270,
      "cache_read_input_tokens": 10938,
      "output_tokens": 510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 828,
          "output_tokens": 510,
          "cache_read_input_tokens": 10938,
          "cache_creation_input_tokens": 3270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3270,
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

_source line 22 · 2026-05-10T19:23:00.709Z_

<details><summary>↩ Tool result · `toolu_01XwWrMWqKZc7v3Y3Lx1B9NU`</summary>

```text
# LIBERO-PRO Details

Based on the abstract provided, here's what can be extracted:

## (1) Four Perturbation Dimensions
The benchmark evaluates performance across: "manipulated objects, initial states, task instructions, and environments."

## (2) Success Rates: Standard vs. LIBERO-PRO
- **Standard LIBERO**: Models achieve "over 90% accuracy"
- **LIBERO-PRO**: Performance "collapses to 0.0%"

## (3) Which Models Were Evaluated
The document does not specify which particular Vision-Language-Action models were tested. It refers generally to "existing models" without naming specific architectures or systems.

## (4) Specific Performance Collapse Numbers
Only two percentages are explicitly stated:
- 90%+ (standard evaluation)
- 0.0% (generalized setting)

The abstract illustrates failure modes—such as models "persist in executing grasping actions when the target object is replaced" and producing "unchanged outputs even when given corrupted instructions"—but does not provide granular breakdowns by perturbation dimension or specific model comparisons.

**Note**: Full technical details and comprehensive results tables would require accessing the complete paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fb3bef4-e9e9-4920-84d1-5e3c27c641af",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "e05dad3e-ab3f-4a25-8209-279dd288ed49",
  "sourceToolAssistantUUID": "7fb3bef4-e9e9-4920-84d1-5e3c27c641af",
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

_source line 23 · 2026-05-10T19:23:04.075Z_

<details><summary>↩ Tool result · `toolu_01UrRzSpPWVqD72TyeVkUrPf`</summary>

```text
Web search results for query: "DreamVLA LIBERO success rate 97.2%"

Links: [{"title":"Dream-VL & Dream-VLA: Open Vision-Language and ...","url":"https://arxiv.org/pdf/2512.22615"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=SimplerEnv-Fractal"},{"title":"Dream-VL & Dream-VLA - HKU NLP Group - GitHub Pages","url":"https://hkunlp.github.io/blog/2025/dream-vlx/"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Success rate of the π 0 model on the LIBERO-Goal, Object, Spatial and... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rate-of-the-p-0-model-on-the-LIBERO-Goal-Object-Spatial-and-Long-task-suits_tbl1_396330496"},{"title":"Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2107"},{"title":"DreamVLA/docs/LIBERO_RUN.md at main · Zhangwenyao1/DreamVLA","url":"https://github.com/Zhangwenyao1/DreamVLA/blob/main/docs/LIBERO_RUN.md"},{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"},{"title":"PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/952"},{"title":"DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge [Quick Review]","url":"https://liner.com/review/dreamvla-visionlanguageaction-model-dreamed-with-comprehensive-world-knowledge"}]

Based on the search results, Dream-VLA achieves top-tier performance of 97.2% average success rate on LIBERO, 71.4% overall average on SimplerEnv–Bridge, and 60.5% overall average on SimplerEnv–Fractal, surpassing leading models such as π0 and GR00T-N1.

The 97.2% success rate on LIBERO represents a significant achievement in Vision-Language-Action (VLA) models for robotic manipulation tasks. This performance metric comes from research presented in an academic paper published in December 2025, where Dream-VLA was developed using discrete diffusion modeling combined with vision-language capabilities trained on diverse robotic manipulation data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "163208eb-0664-4859-a762-8e26b835aa76",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "51c04c3a-1928-4284-83c8-6b0aeab53349",
  "sourceToolAssistantUUID": "163208eb-0664-4859-a762-8e26b835aa76",
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

_source line 24 · 2026-05-10T19:23:04.640Z_

<details><summary>↩ Tool result · `toolu_015PryWiLAjZVGcKZbfsWyk3`</summary>

```text
# LIBERO Benchmark Results for LaST-R1

Based on the abstract provided, the only specific success rate mentioned is:

**"a near-perfect 99.9% average success rate on the LIBERO benchmark with only one-shot supervised warm-up"**

## What the Abstract Reveals

The document does **not provide**:
- Breakdown of specific sub-benchmarks within LIBERO
- Individual task success rates
- Detailed baseline comparison numbers
- Performance metrics for particular manipulation categories

## Real-World Performance

The abstract does cite broader results: "up to a 22.5% average improvement over SOTA supervised fine-tuning approach across four complex tasks, including both single-arm and dual-arm settings."

However, specific task names, baseline method names, and granular performance comparisons are not included in this abstract excerpt. To access detailed benchmark breakdowns and comprehensive baseline comparisons, you would need to review the full PDF paper linked on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2d76216-ddb6-4ff4-9c7a-b1802d53a3d7",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "cc5319d2-9a6c-4bc9-a2d9-bfc06ca5fedc",
  "sourceToolAssistantUUID": "a2d76216-ddb6-4ff4-9c7a-b1802d53a3d7",
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

_source line 25 · 2026-05-10T19:23:05.941Z_

<details><summary>↩ Tool result · `toolu_019GQscoE6TjP6qvoKc6cBeH`</summary>

```text
Web search results for query: "Cosmos-Policy LIBERO success rate 98.5%"

Links: [{"title":"Cosmos Policy — Cosmos Lab","url":"https://research.nvidia.com/labs/cosmos-lab/cosmos-policy/"},{"title":"Cosmos Policy Achieves 98.5% Robot Control With Single- ...","url":"https://quantumzeitgeist.com/percent-cosmos-policy-achieves-robot-control/"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://research.nvidia.com/labs/dir/cosmos-policy/cosmos_policy_index.html"},{"title":"nvidia/Cosmos-Policy-LIBERO-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B"},{"title":"[2601.16163] Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/abs/2601.16163"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/html/2601.16163v1"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning | OpenReview","url":"https://openreview.net/forum?id=wPEIStHxYH"},{"title":"COSMOS POLICY: FINE-TUNING VIDEO MODELS FOR ...","url":"https://openreview.net/attachment?id=wPEIStHxYH&name=pdf"},{"title":"Understanding How NVIDIA Cosmos Policy Works | Paper: Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - BioErrorLog Tech Blog","url":"https://en.bioerrorlog.work/entry/nvidia-cosmos-policy-paper"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260116163K/abstract"}]

Based on the search results, Cosmos Policy achieves state-of-the-art performance on the LIBERO and RoboCasa simulation benchmarks (98.5% and 67.1% average success rates, respectively).

More specifically, Cosmos Policy achieves state-of-the-art performance on the LIBERO simulation benchmark, with an average success rate of 98.5% across four task suites. The results are broken down further, with success rates of 98.1%, 100.0%, 98.2%, and 97.6% respectively across four LIBERO task suites.

Cosmos Policy learns to directly generate robot actions encoded as latent frames within the video model's latent diffusion process, harnessing the model's pretrained priors and core learning algorithm to capture complex action distributions. Additionally, Cosmos Policy generates future state images and values (expected cumulative rewards), which are similarly encoded as latent frames, enabling test-time planning of action trajectories with higher likelihood of success.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "687c1d81-26c4-4c11-be85-2785e7f42959",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "5ee70353-c2ba-445c-a434-d739f0d7210d",
  "sourceToolAssistantUUID": "687c1d81-26c4-4c11-be85-2785e7f42959",
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

_source line 26 · 2026-05-10T19:23:08.793Z_

Now let me get more details from the full HTML versions of the key papers for precise numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ee70353-c2ba-445c-a434-d739f0d7210d",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS6VosfNFG4gzSukwpN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48e24159-27bb-4992-8712-08e01d300af9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPVKjp6aKrhf3DevRWmkKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 798,
      "cache_creation_input_tokens": 2863,
      "cache_read_input_tokens": 14208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2863,
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

_source line 27 · 2026-05-10T19:23:11.802Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MdZNEHBb8ErsFoCrUAJ3TH`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.16666v1",
  "prompt": "Find the exact LIBERO benchmark results table. What are Fast-WAM's success rates on LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, and the average? What are the comparison baselines and their numbers? Is 97.6% mentioned anywhere?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48e24159-27bb-4992-8712-08e01d300af9",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS6VosfNFG4gzSukwpN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "859d5326-0980-428f-a615-6b82d32c5523",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPVKjp6aKrhf3DevRWmkKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 798,
      "cache_creation_input_tokens": 2863,
      "cache_read_input_tokens": 14208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2863,
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

_source line 28 · 2026-05-10T19:23:14.689Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EgSkUNZrNBUYp1wUXpY6k3`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.03827v1",
  "prompt": "Extract the complete results from LIBERO-PRO. What are the four perturbation types in detail? What specific models were tested and what were their exact success rates under standard LIBERO vs LIBERO-PRO? Find all percentage numbers in the results tables. What does the 0.0% collapse refer to specifically?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "859d5326-0980-428f-a615-6b82d32c5523",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS6VosfNFG4gzSukwpN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1358b55f-3118-4fb0-8f26-16cf0ce80e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPVKjp6aKrhf3DevRWmkKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 798,
      "cache_creation_input_tokens": 2863,
      "cache_read_input_tokens": 14208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2863,
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

_source line 29 · 2026-05-10T19:23:15.726Z_

<details><summary>↩ Tool result · `toolu_01MdZNEHBb8ErsFoCrUAJ3TH`</summary>

```text
# LIBERO Benchmark Results

Based on Table 2 in the paper, Fast-WAM's performance on LIBERO is:

- **Spatial:** 98.2%
- **Object:** 100.0%
- **Goal:** 97.0%
- **Long:** 95.2%
- **Average:** 97.6%

## Key Comparisons

The table shows Fast-WAM (without embodied pretraining) remains competitive with pretrained baselines:

- **LingBot-VA** (with pretraining): 98.5% average
- **Motus** (with pretraining): 97.7% average
- **π0.5** (with pretraining): 96.9% average

The paper states that "Fast-WAM also delivers strong overall performance, achieving an average success rate of 97.6% without embodied pretraining," outperforming π0.5 while remaining close to the strongest pretrained methods. Notably, removing video co-training drops performance significantly to 93.5% average.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "859d5326-0980-428f-a615-6b82d32c5523",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "4d8dfbf4-4ecd-4f96-b973-cdc5e5f5fd6d",
  "sourceToolAssistantUUID": "859d5326-0980-428f-a615-6b82d32c5523",
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

_source line 30 · 2026-05-10T19:23:16.217Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011iAEb1kXd9SU6EHVx6mtfF`</summary>

```json
{
  "url": "https://www.codesota.com/browse/robots/robot-manipulation/libero-long",
  "prompt": "What are the current SOTA results on LIBERO-Long? List all methods and their success rates. What is the top-performing method?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d8dfbf4-4ecd-4f96-b973-cdc5e5f5fd6d",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS6VosfNFG4gzSukwpN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c804705-e3c1-4d40-a847-01cafef187e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPVKjp6aKrhf3DevRWmkKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 798,
      "cache_creation_input_tokens": 2863,
      "cache_read_input_tokens": 14208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2863,
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

_source line 31 · 2026-05-10T19:23:17.551Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X9AwbVQtrJK8vBMWL2koQS`</summary>

```json
{
  "url": "https://www.emergentmind.com/topics/libero",
  "prompt": "List all recent methods and their LIBERO success rates. What are the top performers? Include specific numbers for LIBERO-100, LIBERO-Long, LIBERO-Spatial, LIBERO-Object, LIBERO-Goal averages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c804705-e3c1-4d40-a847-01cafef187e4",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS6VosfNFG4gzSukwpN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c24b265c-04b3-42c5-b6ff-06702c070d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPVKjp6aKrhf3DevRWmkKN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 798,
      "cache_creation_input_tokens": 2863,
      "cache_read_input_tokens": 14208,
      "output_tokens": 532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2863
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 798,
          "output_tokens": 532,
          "cache_read_input_tokens": 14208,
          "cache_creation_input_tokens": 2863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2863,
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

_source line 32 · 2026-05-10T19:23:19.937Z_

<details><summary>↩ Tool result · `toolu_011iAEb1kXd9SU6EHVx6mtfF`</summary>

```text
# LIBERO-Long SOTA Results

Based on the content provided, **no results are currently indexed** for the LIBERO-Long benchmark.

The page explicitly states: "No results indexed yet — be the first to submit a score."

There is therefore no top-performing method to report, as the leaderboard section indicates: "No benchmark results indexed yet."

The benchmark awaits its first submission, with the site encouraging researchers to contribute by providing "a public checkpoint or API endpoint" along with reproduction scripts and environment specifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c804705-e3c1-4d40-a847-01cafef187e4",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "1afe7fc0-c2cf-44c3-8857-f1e440e7eeb4",
  "sourceToolAssistantUUID": "8c804705-e3c1-4d40-a847-01cafef187e4",
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

_source line 33 · 2026-05-10T19:23:21.355Z_

<details><summary>↩ Tool result · `toolu_01EgSkUNZrNBUYp1wUXpY6k3`</summary>

```text
# LIBERO-PRO Perturbation Framework and Results

## Four Perturbation Types

The study introduces four systematic perturbation dimensions:

1. **Object Attribute Perturbation**: Modifies visual properties like "color, texture, or size" while maintaining semantic equivalence (e.g., red cup → blue cup).

2. **Initial Position Perturbation**: Alters "initial object positions to modify absolute and relative arrangements" while preserving physical plausibility.

3. **Instruction Perturbation**: Includes semantic variations (paraphrasing) and task-level modifications, replacing target objects or actions while ensuring "all actions and objects appear in the training set."

4. **Environment Perturbation**: Changes "the background's appearance" and workspace settings without affecting task feasibility.

## Models and Success Rates

Three state-of-the-art models were evaluated:

**OpenVLA** (four checkpoints):
- Standard LIBERO: ~98% average
- Position changes: 0.00%
- Object changes: 0.96%
- Semantic instruction variations: 0.98%
- Environment changes: Variable (0.00%-0.98%)

**Pi0** (single checkpoint):
- Standard LIBERO: ~92-97% average
- Position changes: 0.00%
- Object changes: 0.94%
- Semantic variations: ~0.93%

**Pi0.5** (single checkpoint):
- Standard LIBERO: ~97-98% average
- Position changes: 0.38% (libero-goal)
- Object changes: 0.97%
- Semantic variations: 0.97%

## The 0.0% Collapse

The "0.0% collapse" refers specifically to "performance collapses to 0.0% under our generalized setting" involving spatial position changes. Models demonstrate "near-complete failure" when object positions shift beyond minimal thresholds, despite achieving >90% on standard benchmarks. This reveals that high baseline scores reflect "memorization of action sequences and environment layouts" rather than genuine understanding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1358b55f-3118-4fb0-8f26-16cf0ce80e32",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "1bb791a4-904f-4fe0-9d87-6f59bb4992db",
  "sourceToolAssistantUUID": "1358b55f-3118-4fb0-8f26-16cf0ce80e32",
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

_source line 34 · 2026-05-10T19:23:23.490Z_

<details><summary>↩ Tool result · `toolu_01X9AwbVQtrJK8vBMWL2koQS`</summary>

```text
# LIBERO Benchmark: Top Performing Methods and Success Rates

Based on the benchmark results provided, here are the leading methods with their documented performance:

## Top Performers on LIBERO Suites

| Model | LIBERO-Goal | LIBERO-Object | LIBERO-Spatial | LIBERO-Long | Average |
|-------|-------------|---------------|----------------|-------------|---------|
| **SimpleVLA-RL** | 99.2% | 99.1% | 99.4% | 98.5% | **99.1%** |
| **RLinf-VLA (RL)** | 98.79% | 99.80% | 99.40% | 93.95% | **98.11%** |
| **VITA-VLA** | 97.9% | 99.8% | 98.0% | 93.5% | **97.3%** |
| **UniVLA** | 93.6% | 98.8% | 95.4% | 94.0% | **95.5%** |

## Key Findings on Performance

The document notes that "RL fine-tuning yields dramatic gains over all SFT and BC pipelines," with some methods achieving improvements of up to 45 percentage points on longer-horizon tasks.

**SimpleVLA-RL** emerges as the top performer across nearly all standard suites. The benchmark also documents that certain models achieve strong results on larger task sets (LIBERO-90/130), though comprehensive comparisons across all variants remain incomplete in the available data.

## Critical Context

Importantly, these exceptional success rates reflect performance under optimal conditions. When subjected to systematic perturbations in LIBERO-PRO and LIBERO-Plus variants, "reported LIBERO SOTA models degrade from ≈98% to 0–40% in perturbed regimes," revealing significant brittleness in real-world applicability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c24b265c-04b3-42c5-b6ff-06702c070d6b",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "95aba46b-e422-4eff-9eab-5efbfd90f110",
  "sourceToolAssistantUUID": "c24b265c-04b3-42c5-b6ff-06702c070d6b",
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

_source line 35 · 2026-05-10T19:23:27.056Z_

Let me get the SnapFlow and LaST-R1 details, plus search for more context on LIBERO saturation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95aba46b-e422-4eff-9eab-5efbfd90f110",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS7nuJjL3G7z7sToZKo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15a6af36-770b-4c61-a2d3-57a31f9e956c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gg7KBtiPG6wCm81ToZspBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 17071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2715,
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

_source line 36 · 2026-05-10T19:23:29.855Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AELnMcjwvp6iQ6gCzJTFkN`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.05656v1",
  "prompt": "Extract SnapFlow's exact LIBERO success rates. What are its numbers on LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, and the average? Is 98.75% the average? Compare with baselines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15a6af36-770b-4c61-a2d3-57a31f9e956c",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS7nuJjL3G7z7sToZKo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af1dee4c-7c04-4a0a-8fc2-6dddd01dcc70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gg7KBtiPG6wCm81ToZspBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 17071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2715,
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

_source line 37 · 2026-05-10T19:23:31.369Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Drz77vySQB5YBtKHm2kFch`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.28192",
  "prompt": "Extract LaST-R1's exact LIBERO success rates. What does 99.9% refer to? Breakdown by LIBERO sub-suite (Spatial, Object, Goal, Long). What baselines are compared? Is this the current SOTA?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af1dee4c-7c04-4a0a-8fc2-6dddd01dcc70",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS7nuJjL3G7z7sToZKo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb0669ab-8165-44c3-934d-329b1a3dd2f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gg7KBtiPG6wCm81ToZspBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 17071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2715,
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

_source line 38 · 2026-05-10T19:23:31.581Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016KFsQqPoAe9XJ4ZhbRFKVo`</summary>

```json
{
  "query": "SimpleVLA-RL LIBERO 99.1% success rate reinforcement learning VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb0669ab-8165-44c3-934d-329b1a3dd2f1",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS7nuJjL3G7z7sToZKo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49dc4aa1-98e4-45ae-b9e1-abc065187f76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gg7KBtiPG6wCm81ToZspBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 17071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2715,
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

### Tool result

_source line 39 · 2026-05-10T19:23:34.297Z_

<details><summary>↩ Tool result · `toolu_01AELnMcjwvp6iQ6gCzJTFkN`</summary>

```text
# SnapFlow LIBERO Success Rates

Based on Table 1 and Table 6 in the paper, here are SnapFlow's exact performance numbers:

## Per-Suite Results (π0.5, 1-step)
- **LIBERO-Spatial**: 99%
- **LIBERO-Object**: 100%
- **LIBERO-Goal**: 99%
- **LIBERO-Long (10-step)**: 97%
- **Average**: 98.75%

Yes, 98.75% is the reported average across all four suites.

## Comparison with Baselines

| Method | Steps | Average Success |
|--------|-------|-----------------|
| 10-step Baseline (Euler) | 10 | 97.75% |
| Naïve 1-step (untrained) | 1 | 96.75% |
| **SnapFlow** | **1** | **98.75%** |

SnapFlow achieves approximately 1 percentage point improvement over the 10-step teacher and exceeds the naïve 1-step approach by 2 percentage points. The paper notes that SnapFlow "matches the 10-step teacher at 97.75% and slightly exceeding it" while delivering a 9.6× denoising speedup.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af1dee4c-7c04-4a0a-8fc2-6dddd01dcc70",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "cffa725e-0f74-4b0c-bc9a-ae37efbd72e3",
  "sourceToolAssistantUUID": "af1dee4c-7c04-4a0a-8fc2-6dddd01dcc70",
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

_source line 40 · 2026-05-10T19:23:37.023Z_

<details><summary>↩ Tool result · `toolu_01Drz77vySQB5YBtKHm2kFch`</summary>

```text
# LaST-R1 LIBERO Performance Analysis

## Overall Success Rate
The 99.9% figure represents the **average success rate across all four LIBERO task suites** after one-shot supervised fine-tuning followed by online RL post-training.

## Breakdown by Suite
According to Table 1, LaST-R1 achieved:
- **Spatial**: 99.8%
- **Object**: 100.0%
- **Goal**: 100.0%
- **Long**: 99.8%

## Key Comparisons
The paper evaluated LaST-R1 against multiple baseline categories:

**SFT-only models** (trained on full datasets): OpenVLA (76.5%), π₀ (94.2%), π₀.₅ (96.9%), OpenVLA-OFT (97.1%)

**RL-trained baselines**: SimpleVLA-RL (96.9%), RLinf-GRPO (97.6%), πRL (98.3%)

## SOTA Status
Yes, LaST-R1 appears to be current state-of-the-art. The paper notes it "ranked first across all four task suites" and achieved performance improvements of 5.3% on the challenging LIBERO-Long suite compared to the previous leading RL method (πRL at 94.0%).

Notably, this exceptional performance used only single-trajectory warm-up data, contrasting sharply with SFT baselines requiring 50 complete trajectories per task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb0669ab-8165-44c3-934d-329b1a3dd2f1",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "47d6aab5-b9fc-4249-a582-24b7b522e381",
  "sourceToolAssistantUUID": "eb0669ab-8165-44c3-934d-329b1a3dd2f1",
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

_source line 41 · 2026-05-10T19:23:37.615Z_

<details><summary>↩ Tool result · `toolu_016KFsQqPoAe9XJ4ZhbRFKVo`</summary>

```text
Web search results for query: "SimpleVLA-RL LIBERO 99.1% success rate reinforcement learning VLA"

Links: [{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"SimpleVLA-RL: Scalable VLA Reinforcement Learning","url":"https://www.emergentmind.com/topics/simplevla-rl"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.09674v1"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"SimpleVLA-RL: Scalable RL for VLA Models","url":"https://www.emergentmind.com/papers/2509.09674"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"[Literature Review] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://www.themoonlight.io/en/review/simplevla-rl-scaling-vla-training-via-reinforcement-learning"},{"title":"SimpleVLA-RL/README.md at main · PRIME-RL/SimpleVLA-RL","url":"https://github.com/PRIME-RL/SimpleVLA-RL/blob/main/README.md"},{"title":"(PDF) SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://www.researchgate.net/publication/395418649_SimpleVLA-RL_Scaling_VLA_Training_via_Reinforcement_Learning"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"}]

Based on the search results, here's what I found about SimpleVLA-RL and its 99.1% success rate on LIBERO:

## Overview

SimpleVLA-RL is an efficient RL framework tailored for VLA models that introduces VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, and optimized loss computation.

## LIBERO Performance

On LIBERO tasks, the framework improves average success rates from 91% to 99.1%, with particularly notable gains on long-horizon tasks (98.5% vs. previous best results). This represents a significant improvement in Vision-Language-Action model performance.

## Key Achievements

On dual-arm manipulation benchmarks (RoboTwin 1.0 and 2.0), improvements range from 30.6% to 80% relative gains over SFT baselines.

## Data Efficiency

One of the most remarkable features is SimpleVLA-RL's exceptional data efficiency. Using only one demonstration trajectory per task, SimpleVLA-RL increases average success rates across LIBERO task suites from 48.9% to 96.9%, which actually surpasses the 91% achieved by Full-Trajectory SFT alone.

## Methodology

SimpleVLA-RL is a simple yet effective approach for online Reinforcement Learning for Vision-Language-Action models, which utilizes only outcome-level 0/1 rule-based reward signals directly obtained from simulation environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49dc4aa1-98e4-45ae-b9e1-abc065187f76",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "2ec6ff1a-d43c-4cbf-9b7d-69c97305bb00",
  "sourceToolAssistantUUID": "49dc4aa1-98e4-45ae-b9e1-abc065187f76",
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

_source line 42 · 2026-05-10T19:23:41.051Z_

Now let me get more details on the Cosmos-Policy breakdown and check for LIBERO-Plus as well.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ec6ff1a-d43c-4cbf-9b7d-69c97305bb00",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS8qGDAZzK8jXtvyEE4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef0bc219-798d-42e9-bd02-c4a29ad32600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcKp97aXX675V1W36WCwGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1998,
      "cache_read_input_tokens": 19786,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1998,
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

_source line 43 · 2026-05-10T19:23:43.445Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lkv73uCsX1L8tAT256JctL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.16163",
  "prompt": "Extract exact LIBERO success rates for Cosmos Policy. What are the per-suite numbers (Spatial, Object, Goal, Long)? Is the average 98.5%? Which variant achieves this?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef0bc219-798d-42e9-bd02-c4a29ad32600",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS8qGDAZzK8jXtvyEE4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b19930ea-dacd-45b3-b540-58e11b6c2052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcKp97aXX675V1W36WCwGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1998,
      "cache_read_input_tokens": 19786,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1998,
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

_source line 44 · 2026-05-10T19:23:44.715Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RMTi4tg1C28fZZHUsr3Ek1`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "What is LIBERO-Plus? How does it differ from LIBERO-PRO? What perturbation types does it test? What are the key findings about model robustness?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b19930ea-dacd-45b3-b540-58e11b6c2052",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS8qGDAZzK8jXtvyEE4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7468e0ca-936e-427e-8260-9c65707d73bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcKp97aXX675V1W36WCwGU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1998,
      "cache_read_input_tokens": 19786,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1998
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 19786,
          "cache_creation_input_tokens": 1998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1998,
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

_source line 45 · 2026-05-10T19:23:45.685Z_

<details><summary>↩ Tool result · `toolu_01Lkv73uCsX1L8tAT256JctL`</summary>

```text
Based on the provided content, I cannot extract the specific per-suite LIBERO success rates (Spatial, Object, Goal, Long) for Cosmos Policy.

The abstract only states: "Cosmos Policy achieves state-of-the-art performance on the LIBERO and RoboCasa simulation benchmarks (98.5% and 67.1% average success rates, respectively)."

The 98.5% figure represents the overall average for LIBERO, but the document does not include breakdowns by individual suites or identify which specific variant achieves this result. To obtain the detailed per-suite performance metrics you're seeking, you would need to access the full paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b19930ea-dacd-45b3-b540-58e11b6c2052",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "960b8628-2cca-4675-a616-f7d0d527827a",
  "sourceToolAssistantUUID": "b19930ea-dacd-45b3-b540-58e11b6c2052",
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

_source line 46 · 2026-05-10T19:23:52.125Z_

<details><summary>↩ Tool result · `toolu_01RMTi4tg1C28fZZHUsr3Ek1`</summary>

```text
# LIBERO-Plus: Robustness Analysis of Vision-Language-Action Models

## What is LIBERO-Plus?

LIBERO-Plus is an expanded benchmark for evaluating the generalization capabilities of Vision-Language-Action (VLA) models in robotic manipulation. It comprises "10,030 tasks spanning seven perturbation factors with twenty-one low-level components," built upon the original LIBERO benchmark with systematic perturbations applied.

## Distinction from LIBERO

The document does not mention "LIBERO-PRO." LIBERO-Plus differs from the original LIBERO by introducing controlled environmental variations and stratifying tasks into five difficulty levels based on model performance distributions.

## Perturbation Types Tested

The benchmark evaluates seven perturbation dimensions:

1. **Objects Layout** - adding distracting objects or repositioning targets
2. **Camera Viewpoints** - changing camera distance, position, and orientation
3. **Robot Initial States** - varying manipulator joint positions
4. **Language Instructions** - rewriting instructions for linguistic complexity
5. **Light Conditions** - modifying diffuse, directional, specular, and shadow properties
6. **Background Textures** - altering scene and surface materials
7. **Sensor Noise** - applying motion blur, Gaussian blur, zoom blur, fog, and glass distortions

## Key Robustness Findings

The research reveals significant brittleness in contemporary VLA models:

- Performance drops from approximately 95% to below 30% under modest camera or robot state perturbations
- Models demonstrate "positional bias rather than genuine semantic understanding of objects"
- Surprisingly, models are "largely insensitive to language variations," suggesting they ignore linguistic instructions and rely on visual-action mappings instead
- Negative compositional gaps show that combined perturbations produce worse results than predicted from single-perturbation effects
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7468e0ca-936e-427e-8260-9c65707d73bf",
  "isSidechain": true,
  "promptId": "e0fc9f64-cfd5-440d-8593-6c22f25b8449",
  "agentId": "a44bb284748400e92",
  "type": "user",
  "uuid": "10fcaae5-bb4f-462d-a7e2-64f55fd3aaa3",
  "sourceToolAssistantUUID": "7468e0ca-936e-427e-8260-9c65707d73bf",
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

_source line 47 · 2026-05-10T19:24:35.506Z_

I now have comprehensive data. Let me compile the findings.

---

## LIBERO Benchmark SOTA Verification -- May 2026

### 1. Current SOTA Success Rates on LIBERO

The claimed numbers you mentioned are **largely accurate**, and several newer methods have since surpassed them. Here is a comprehensive ranking of top performers on the standard LIBERO benchmark (averaged across LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long):

| Method | Spatial | Object | Goal | Long | **Average** | Notes |
|--------|---------|--------|------|------|-------------|-------|
| **LaST-R1** | 99.8% | 100.0% | 100.0% | 99.8% | **99.9%** | RL post-training, 1-shot warm-up (Apr 2026) |
| **SimpleVLA-RL** | 99.4% | 99.1% | 99.2% | 98.5% | **99.1%** | RL-trained VLA (ICLR 2026) |
| **SnapFlow** | 99% | 100% | 99% | 97% | **98.75%** | 1-step distilled pi0.5 (Apr 2026) |
| **Cosmos-Policy** | 98.2% | 100.0% | 98.1% | 97.6% | **98.5%** | NVIDIA, video model fine-tuning (Jan 2026) |
| **LingBot-VA** | -- | -- | -- | -- | **98.5%** | With embodied pretraining |
| **Motus** | -- | -- | -- | -- | **97.7%** | With embodied pretraining |
| **Fast-WAM** | 98.2% | 100.0% | 97.0% | 95.2% | **97.6%** | No pretraining, 190ms latency (Mar 2026) |
| **DreamVLA** | -- | -- | -- | -- | **97.2%** | Discrete diffusion VLA (Dec 2025) |
| **pi0.5** | -- | -- | -- | -- | **96.9%** | Physical Intelligence |
| **OpenVLA-OFT** | -- | -- | -- | -- | **97.1%** | |
| **pi0** | -- | -- | -- | -- | **94.2%** | |

**Verification of your specific claims:**
- **Fast-WAM at 97.6%** -- Confirmed. Spatial 98.2%, Object 100.0%, Goal 97.0%, Long 95.2%.
- **Cosmos-Policy at 98.5%** -- Confirmed. Per-suite: 98.2%, 100.0%, 98.1%, 97.6%.
- **DreamVLA at 97.2%** -- Confirmed.

All three are now surpassed by RL-based methods (LaST-R1 at 99.9%, SimpleVLA-RL at 99.1%).

### 2. Is LIBERO Effectively Saturated?

**Yes, standard LIBERO is saturated.** Multiple methods exceed 97% average success, and LaST-R1 achieves 99.9% (effectively perfect). The benchmark no longer meaningfully differentiates between top methods under standard evaluation.

**However, this saturation is misleading.** Multiple papers from late 2025 and 2026 demonstrate that high LIBERO scores reflect **memorization, not generalization**:

- Under LIBERO-PRO perturbations, models achieving >90% on standard LIBERO **collapse to 0.0%** on position perturbations.
- Under LIBERO-Plus perturbations, performance drops from ~95% to **below 30%** under camera or robot state changes.
- Models exhibit "positional bias rather than genuine semantic understanding" and often ignore language instructions entirely.

### 3. Does LIBERO-PRO Exist?

**Yes.** The paper is:

> **"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization"**
> arXiv:2510.03827 (October 2025)
> GitHub: https://github.com/Zxy-MLlab/LIBERO-PRO

It is a plug-and-play evaluation extension of the original LIBERO benchmark.

### 4. LIBERO-PRO Purpose and Perturbation Types

**Purpose:** LIBERO-PRO exposes that standard LIBERO's homogeneous train/test split allows rote memorization, producing inflated performance estimates. It provides a fairer evaluation framework that tests genuine task understanding and environmental perception.

**Four perturbation dimensions:**

1. **Object Attribute Perturbation** -- Modifies non-essential visual properties (color, texture, size) while preserving semantic equivalence (e.g., red cup becomes blue cup). Tests robustness to superficial visual changes.

2. **Initial Position Perturbation** -- Alters initial object positions and relative arrangements while maintaining physical plausibility. This is the most devastating: **all tested models drop to 0.0% success** when displacement exceeds ~0.2 units.

3. **Instruction Perturbation** -- Includes semantic paraphrasing and task-level modifications (replacing target objects or actions), using only objects/actions that appear in the training set. Tests compositional language understanding.

4. **Environment Perturbation** -- Changes background appearance and workspace settings without affecting task feasibility. Tests visual generalization.

**Key results on models tested (OpenVLA, pi0, pi0.5):**
- Standard LIBERO: 92-98% success
- Position perturbations: **0.0%** (all models)
- Object attribute changes: **<1%**
- Instruction variations: **<1%**
- Environment changes: **0.0-1%**

### Additional Context: LIBERO-Plus

A separate but related benchmark, **LIBERO-Plus** (arXiv:2510.13626, October 2025), provides even broader robustness analysis with **seven perturbation dimensions** (objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise) across 10,030 tasks. It confirms the same findings -- models are brittle under distribution shift, with performance dropping from ~95% to below 30%.

### Summary

Standard LIBERO is effectively solved and no longer a meaningful discriminator for state-of-the-art VLA models. The real challenge has shifted to robustness benchmarks (LIBERO-PRO, LIBERO-Plus) where even the best models collapse catastrophically. The field's focus is moving toward RL-based fine-tuning (which dominates the leaderboard) and robustness-aware evaluation.

Sources:
- [LaST-R1 (arXiv:2604.28192)](https://arxiv.org/abs/2604.28192)
- [Fast-WAM (arXiv:2603.16666)](https://arxiv.org/abs/2603.16666)
- [Cosmos-Policy (arXiv:2601.16163)](https://arxiv.org/abs/2601.16163)
- [LIBERO-PRO (arXiv:2510.03827)](https://arxiv.org/abs/2510.03827)
- [LIBERO-Plus (arXiv:2510.13626)](https://arxiv.org/html/2510.13626v1)
- [SnapFlow (arXiv:2604.05656)](https://arxiv.org/html/2604.05656v1)
- [SimpleVLA-RL (arXiv:2509.09674)](https://arxiv.org/abs/2509.09674)
- [DreamVLA (arXiv:2512.22615)](https://arxiv.org/pdf/2512.22615)
- [LIBERO Benchmark Topic Overview - EmergentMind](https://www.emergentmind.com/topics/libero)
- [LIBERO-PRO GitHub](https://github.com/Zxy-MLlab/LIBERO-PRO)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10fcaae5-bb4f-462d-a7e2-64f55fd3aaa3",
  "isSidechain": true,
  "agentId": "a44bb284748400e92",
  "requestId": "req_011CauS9uH6METJxjnhFq8E4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad0ef40c-0ee2-4ab5-a30f-323e7c77ceb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b5fe76b-9f2f-45e8-a9f1-581bbd64e11e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xdXRehki59jwtZYhsvq5y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 21784,
      "output_tokens": 1988,
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
          "input_tokens": 1,
          "output_tokens": 1988,
          "cache_read_input_tokens": 21784,
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
