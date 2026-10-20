# Research conversation: Search for these papers that are cited as related work: 1. SHINE by Lee et al., arxiv 2411.09689 - "Probing LLM Hallucin

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a1e666978809ea371.jsonl`
- **Structured JSON:** [`32df8be940e7a3cc1f80.json`](../../sessions/32/32df8be940e7a3cc1f80.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-16T10:13:30.878Z_

Search for these papers that are cited as related work:

1. SHINE by Lee et al., arxiv 2411.09689 - "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge". Search for:
- "arxiv 2411.09689"
- "SHINE perturbation hallucination KL divergence"

2. SSP / "Shaking to Reveal" by Luo et al., arxiv 2506.02696 - "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations". Search for:
- "arxiv 2506.02696"
- "shaking to reveal perturbation hallucination detection"

3. Also search for any OTHER perturbation-based hallucination detection methods from 2025-2026 that might be competing with LSP but not cited. Try:
- "perturbation hallucination detection 2025 2026"
- "hidden state perturbation LLM confidence"
- "intermediate layer perturbation hallucination"
- "residual stream noise hallucination detection"

Report what you find about each paper and any uncited competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "5bbaca97-1aaa-4ebb-b563-b877bbe948d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T10:13:30.881Z_

```json
{
  "parentUuid": "5bbaca97-1aaa-4ebb-b563-b877bbe948d3",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
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
  "uuid": "6045b87c-2a26-4d8f-8f10-ab8d9230f834",
  "timestamp": "2026-05-16T10:13:30.881Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T10:13:33.345Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PYnYe8Ngrawks84Ty3MXt1`</summary>

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
  "parentUuid": "6045b87c-2a26-4d8f-8f10-ab8d9230f834",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb653G1RgENDfFhSzeNpr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0724b518-26f5-4c6b-a893-959fd478db22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WdxwCAS9BjVq2f1ksGtpA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 828,
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

_source line 4 · 2026-05-16T10:13:33.348Z_

<details><summary>↩ Tool result · `toolu_01PYnYe8Ngrawks84Ty3MXt1`</summary>

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
  "parentUuid": "0724b518-26f5-4c6b-a893-959fd478db22",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "e22d27f0-3923-476c-aea9-af2a6bb6fa1c",
  "sourceToolAssistantUUID": "0724b518-26f5-4c6b-a893-959fd478db22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T10:13:36.225Z_

I'll search for each of these papers and related work. Let me run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e22d27f0-3923-476c-aea9-af2a6bb6fa1c",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb653Sj6hSXbQWXZxpbX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5833e118-1a58-42d6-ac1d-655b8167b2ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUUfgKE5TordJBtYyK1oAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 6 · 2026-05-16T10:13:36.227Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V9C8VtRZHkN7cJVv8umgMh`</summary>

```json
{
  "query": "arxiv 2411.09689"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5833e118-1a58-42d6-ac1d-655b8167b2ed",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb653Sj6hSXbQWXZxpbX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fd2dc06-0b65-45ce-93a4-86624d4c3d70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUUfgKE5TordJBtYyK1oAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-16T10:13:36.759Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RJHmeotiHSwWccyHoV2iCp`</summary>

```json
{
  "query": "SHINE perturbation hallucination KL divergence Lee"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fd2dc06-0b65-45ce-93a4-86624d4c3d70",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb653Sj6hSXbQWXZxpbX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c444f0a7-10ba-4caf-b58d-a4ebf3d04b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUUfgKE5TordJBtYyK1oAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 8 · 2026-05-16T10:13:37.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014nJRUJsBRVDjkKFwxvPFPv`</summary>

```json
{
  "query": "arxiv 2506.02696"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c444f0a7-10ba-4caf-b58d-a4ebf3d04b39",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb653Sj6hSXbQWXZxpbX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b42f2921-7ca8-44c8-b7a2-aff99a189618",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUUfgKE5TordJBtYyK1oAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 9 · 2026-05-16T10:13:37.557Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018NXGajQrQrQ18q2qKKgJ5k`</summary>

```json
{
  "query": "shaking to reveal perturbation hallucination detection Luo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b42f2921-7ca8-44c8-b7a2-aff99a189618",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb653Sj6hSXbQWXZxpbX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96511df2-8dc0-46fd-ab5c-249baf94d5a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUUfgKE5TordJBtYyK1oAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

### Tool result

_source line 10 · 2026-05-16T10:13:40.722Z_

<details><summary>↩ Tool result · `toolu_01V9C8VtRZHkN7cJVv8umgMh`</summary>

```text
Web search results for query: "arxiv 2411.09689"

Links: [{"title":"[2411.09689] Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/abs/2411.09689"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689"},{"title":"Acronyms","url":"https://arxiv.org/html/2511.09689"},{"title":"Computer Vision and Pattern Recognition Nov 2024","url":"https://www.arxiv.org/list/cs.CV/2024-11?skip=500&show=50"},{"title":"1 Introduction","url":"https://arxiv.org/html/2508.09689"},{"title":"Adaptive sliding mode control without knowledge of uncertainty bounds","url":"https://arxiv.org/pdf/1802.09689"},{"title":"Amir Atapour Abarghouei's articles on arXiv","url":"https://arxiv.org/a/atapourabarghouei_a_1.html"},{"title":"Hubert P. H. Shum's articles on arXiv","url":"https://arxiv.org/a/shum_h_1.html"},{"title":"arXiv:2411.09680v1 [cond-mat.str-el] 14 Nov 2024","url":"https://arxiv.org/pdf/2411.09680"},{"title":"Contents","url":"https://arxiv.org/html/2504.06689"}]

The paper arxiv 2411.09689 is titled "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge".

The paper introduces a task called hallucination probing that classifies LLM-generated text into three categories (aligned, misaligned, and fabricated), and proposes SHINE, a hallucination probing method that uses perturbations of key entities in prompts without requiring external knowledge, supervised training, or LLM fine-tuning. SHINE achieves state-of-the-art performance in hallucination detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fd2dc06-0b65-45ce-93a4-86624d4c3d70",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "b3ebfcee-4109-401f-a293-76e2e720e926",
  "sourceToolAssistantUUID": "7fd2dc06-0b65-45ce-93a4-86624d4c3d70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T10:13:41.978Z_

<details><summary>↩ Tool result · `toolu_014nJRUJsBRVDjkKFwxvPFPv`</summary>

```text
Web search results for query: "arxiv 2506.02696"

Links: [{"title":"[2506.02696] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696"},{"title":"Computer Science Jun 2025","url":"https://www.arxiv.org/list/cs/2025-06?skip=1475&show=100"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=1400&show=250"},{"title":"Data-Efficient Challenges in Visual Inductive Priors: A Retrospective","url":"https://arxiv.org/html/2506.08612v1"},{"title":"The structure of tiles in ℤ_𝑝^𝑛×ℤ_𝑞 and ℤ_𝑝^𝑛×ℤ_𝑝","url":"https://arxiv.org/html/2411.02696"},{"title":"arXiv.org | 232753 Publications | 16958 Citations | Top authors | Related journals","url":"https://scispace.com/journals/arxiv-org-bl5k1ptr"},{"title":"[2207.02696] YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors","url":"https://arxiv.org/abs/2207.02696"},{"title":"[2509.02696] Unitary and Analytic Renormalisation of Cosmological Correlators","url":"https://arxiv.org/abs/2509.02696"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=3150&show=50"}]

Based on the search results, arXiv paper 2506.02696 is titled "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations".

The paper addresses hallucination as a key obstacle to reliable deployment of large language models in question answering tasks, and examines self-assessment strategies that rely on the model's output confidence to estimate factual accuracy.

The authors propose Sample-Specific Prompting (SSP), a new framework that improves self-assessment by analyzing perturbation sensitivity at intermediate representations. The paper was authored by Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, and Ling Chen and is categorized under Artificial Intelligence (cs.AI).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b42f2921-7ca8-44c8-b7a2-aff99a189618",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "011b1da5-d772-4a38-aeaa-1f5f8a5f2e42",
  "sourceToolAssistantUUID": "b42f2921-7ca8-44c8-b7a2-aff99a189618",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T10:13:43.035Z_

<details><summary>↩ Tool result · `toolu_01RJHmeotiHSwWccyHoV2iCp`</summary>

```text
Web search results for query: "SHINE perturbation hallucination KL divergence Lee"

Links: [{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689"},{"title":"Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/html/2407.05474v1"},{"title":"Detect, Classify, and Fix: Zero-Shot Hallucination Reasoning for LLMs | by Anna Alexandra Grigoryan | Medium","url":"https://thegrigorian.medium.com/detect-classify-and-fix-zero-shot-hallucination-reasoning-for-llms-e1086bb11bca"},{"title":"Diverging Towards Hallucination: Detection of Failures in Vision-Language Models via Multi-token Aggregation","url":"https://arxiv.org/html/2505.11741v1"},{"title":"Uncertainty, Confidence, and Hallucination in Large Language Models","url":"https://hungleai.substack.com/p/uncertainty-confidence-and-hallucination"},{"title":"[2508.10192] Prompt-Response Semantic Divergence Metrics for Faithfulness Hallucination and Misalignment Detection in Large Language Models","url":"https://arxiv.org/abs/2508.10192"},{"title":"Prompt-Response Semantic Divergence Metrics for Faithfulness Hallucination and Misalignment Detection in Large Language Models by Igor Halperin :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5390586.pdf?abstractid=5390586&mirid=1"},{"title":"Mitigating Hallucinations in Large Vision-Language ...","url":"https://ieeexplore.ieee.org/document/11094767/"},{"title":"Kullback–Leibler divergence - Wikipedia","url":"https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence"},{"title":"A White-Box Method for Hallucination Detection","url":"https://aclanthology.org/anthology-files/pdf/emnlp/2024.emnlp-main.116.pdf"}]

Based on the search results, I found highly relevant information about SHINE, a hallucination detection method that uses perturbation and KL divergence. Here's what the research shows:

## SHINE: A Hallucination Detection Method

SHINE is a hallucination probing method that leverages Entity Perturbation Impact to distinguish between aligned, misaligned, and fabricated text.

### Key Mechanism: Entity Perturbation Impact

Low Entity Perturbation Impact measured by KL divergence strongly indicates fabricated text, as its tokens are weakly tied to key entities. More specifically, tokens in aligned and misaligned text, strongly linked to the LLM's knowledge of the entity, have high KL divergence, while most tokens in fabricated text have near-zero values, indicating weak association with the LLM's knowledge.

In empirical results, fabricated text shows a much lower mean KL divergence (0.21) than aligned (0.92) and misaligned (1.36) text.

### Two-Stage Workflow

SHINE classifies LLM-generated text into aligned, misaligned, and fabricated through two steps: Model Knowledge Test and Alignment Test. The Model Knowledge Test identifies whether the LLM has sufficient knowledge to generate a faithful response by perturbing entities in the prompt and evaluating the impact; fabricated text is differentiated at this stage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c444f0a7-10ba-4caf-b58d-a4ebf3d04b39",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "aff06fa1-c7df-4349-b15a-0966c9445174",
  "sourceToolAssistantUUID": "c444f0a7-10ba-4caf-b58d-a4ebf3d04b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T10:13:49.176Z_

<details><summary>↩ Tool result · `toolu_018NXGajQrQrQ18q2qKKgJ5k`</summary>

```text
Web search results for query: "shaking to reveal perturbation hallucination detection Luo"

Links: [{"title":"[2506.02696] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696"},{"title":"[2506.02696v1] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/pdf/2506.02696"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://www.researchgate.net/publication/392371301_Shaking_to_Reveal_Perturbation-Based_Detection_of_LLM_Hallucinations"},{"title":"[Literature Review] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://www.themoonlight.io/en/review/shaking-to-reveal-perturbation-based-detection-of-llm-hallucinations"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations | alphaXiv","url":"https://www.alphaxiv.org/ja/overview/2506.02696v1"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://seongheon-96.github.io/assets/pdf/shaking.pdf"},{"title":"Detecting LLM Hallucinations: Strategies and Overview | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/detecting-llm-hallucinations-strategies-and-overview-57eea69e6a07"},{"title":"VL-Uncertainty: Detecting Hallucination in Large Vision-Language Model via Uncertainty Estimation","url":"https://vl-uncertainty.github.io/"}]

The search results show information about a recent research paper on hallucination detection in large language models. Here's what I found:

## Paper Overview

"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations" is authored by Jinyuan Luo and 4 other authors.

## Problem Statement

Hallucination remains a key obstacle to the reliable deployment of large language models (LLMs) in real-world question answering tasks. As bias accumulates through the model's layers, the final output can diverge from the underlying reasoning process, making output-level confidence an unreliable signal for hallucination detection.

## Proposed Solution

The paper proposes Sample-Specific Prompting (SSP), a new framework that improves self-assessment by analyzing perturbation sensitivity at intermediate representations. SSP dynamically generates noise prompts for each input and employs a lightweight encoder to amplify the changes in representations caused by the perturbation. A contrastive distance metric is then used to quantify these differences and separate truthful from hallucinated responses.

## Key Results

Compared to state-of-the-art methods, the paper improves the hallucination detection accuracy by 4.78% (AUROC) on a challenging TruthfulQA benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96511df2-8dc0-46fd-ab5c-249baf94d5a5",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "3a7c7145-d2c2-4728-b12a-b2071768ee21",
  "sourceToolAssistantUUID": "96511df2-8dc0-46fd-ab5c-249baf94d5a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-16T10:13:51.993Z_

Now let me search for additional competing work that might not be cited.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a7c7145-d2c2-4728-b12a-b2071768ee21",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb654cBtdf4QTwMnau8XZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05c84251-338f-465d-a5ca-3cb0bf528c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZPnRPDSqMwJHQbFEByTH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 10443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3351,
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

_source line 15 · 2026-05-16T10:13:52.499Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AeU6d1tfQudCVrsVEmvN5f`</summary>

```json
{
  "query": "perturbation hallucination detection 2025 2026 LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05c84251-338f-465d-a5ca-3cb0bf528c50",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb654cBtdf4QTwMnau8XZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "095d9ed2-2268-49d4-bfd9-afe87792d1b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZPnRPDSqMwJHQbFEByTH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 10443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3351,
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

_source line 16 · 2026-05-16T10:13:52.952Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016rDxwRYjQyaX1XLvdTJ6HU`</summary>

```json
{
  "query": "hidden state perturbation LLM confidence hallucination 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "095d9ed2-2268-49d4-bfd9-afe87792d1b5",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb654cBtdf4QTwMnau8XZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7b57dbb-e54f-4f01-b36c-47c87ec86433",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZPnRPDSqMwJHQbFEByTH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 10443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3351,
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

_source line 17 · 2026-05-16T10:13:53.495Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bar8dsDru9JhjJxwbjYeLt`</summary>

```json
{
  "query": "intermediate layer perturbation hallucination detection LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7b57dbb-e54f-4f01-b36c-47c87ec86433",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb654cBtdf4QTwMnau8XZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ce6431b-80ce-4694-8b39-5742ded69679",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZPnRPDSqMwJHQbFEByTH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 10443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3351,
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

_source line 18 · 2026-05-16T10:13:53.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KSPySNVBiucYFgHgcm3uvz`</summary>

```json
{
  "query": "residual stream noise hallucination detection LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ce6431b-80ce-4694-8b39-5742ded69679",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb654cBtdf4QTwMnau8XZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f82c68b7-f481-43ab-bbff-cd2ebeb9972c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZPnRPDSqMwJHQbFEByTH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 10443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3351,
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

### Tool result

_source line 19 · 2026-05-16T10:14:00.409Z_

<details><summary>↩ Tool result · `toolu_01AeU6d1tfQudCVrsVEmvN5f`</summary>

```text
Web search results for query: "perturbation hallucination detection 2025 2026 LLM"

Links: [{"title":"LLM Hallucination Statistics 2026: AI Gets Facts Wrong Up to 82% of the Time","url":"https://sqmagazine.co.uk/llm-hallucination-statistics/"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"How to evaluate LLM hallucination rates in engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/how-to-evaluate-llm-hallucination-rates-in-engineering/"},{"title":"[2510.06265] Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/abs/2510.06265"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Detecting hallucinations with LLM-as-a-judge: Prompt engineering and beyond | Datadog","url":"https://www.datadoghq.com/blog/ai/llm-hallucination-detection/"},{"title":"Are you hallucinated? Insights into large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405959525002115"}]

I've successfully performed the web search for "perturbation hallucination detection 2025 2026 LLM". Here are the key findings:

## Perturbation-Based Hallucination Detection

Perturbation-based approaches measure the reproducibility of the answer by regenerating it under different conditions. However, perturbation-based approaches are often prohibitively expensive as they rely on regenerating the answer from the original LLM, often resulting in a 5–10x cost increase due to the number of LLM calls.

## Recent Advances (2025-2026)

A particularly notable development is JPMorgan Chase Bank's 2025 patent on hallucination probability prediction which formalises a process: an incoming query is perturbed n times into lexically divergent but semantically equivalent variations; n+1 independent agents then sample outputs for each variant; a statistical simulation algorithm is applied across those sampled outputs; and the resulting empirical expected hallucination rate becomes the ground truth label for training an encoder classifier.

Multi-agent query perturbation with statistical simulation represents the most technically rigorous pre-generation framework in recent patent filings on LLM hallucination detection.

## Detection Method Taxonomy

Hallucination detection techniques are categorized into retrieval-, uncertainty-, embedding-, learning-, and self-consistency-based techniques. SAC3 extends self-consistency by incorporating semantic-aware cross-checking, including question perturbation (question rephrasing) and cross-model verification (output comparison across different LLMs) to detect points where self-consistency fails.

The search results show active research and patent development in perturbation-based detection methods for LLMs throughout 2025 and 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "095d9ed2-2268-49d4-bfd9-afe87792d1b5",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "b5c070bc-e469-4cce-b533-a096c53eb692",
  "sourceToolAssistantUUID": "095d9ed2-2268-49d4-bfd9-afe87792d1b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T10:14:00.454Z_

<details><summary>↩ Tool result · `toolu_01Bar8dsDru9JhjJxwbjYeLt`</summary>

```text
Web search results for query: "intermediate layer perturbation hallucination detection LLM"

Links: [{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/pdf/2506.02696"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals Citation: Authors. Title. Pages…. DOI:000000/11111.","url":"https://arxiv.org/html/2509.13154"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://seongheon-96.github.io/assets/pdf/shaking.pdf"},{"title":"HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/ba92705991cfbbcedc26e27e833ebbae-Paper-Conference.pdf"},{"title":"awesome-hallucination-detection/README.md at main · EdinburghNLP/awesome-hallucination-detection","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection/blob/main/README.md"},{"title":"Hallucination Detection with the Internal Layers of LLMs","url":"https://www.arxiv.org/pdf/2509.14254"},{"title":"Interpreting, Detecting and Mitigating Object Hallucinations via ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Jiang_Devils_in_Middle_Layers_of_Large_Vision-Language_Models_Interpreting_Detecting_CVPR_2025_paper.pdf"}]

Based on the search results, here's what I found regarding intermediate layer perturbation for hallucination detection in LLMs:

## Sample-Specific Prompting (SSP) Framework

A novel perturbation-based framework called Sample-Specific Prompting (SSP) leverages the differential sensitivity of intermediate representations as a signal for hallucination detection. The key insight is that truthful and hallucinated responses exhibit distinct representational shifts under input perturbations.

### How It Works

Instead of relying on static or handcrafted prompts, SSP learns to dynamically generate controlled noise prompts tailored to each question–answer pair, inducing perturbations that reveal how internal features respond. The noise prompt is appended to the original answer and passed through a shared LLM backbone to induce representational shifts.

The encoder then maps the intermediate representations to a discriminative space and maximize the discrepancy between truthful and hallucinated responses.

### Advantage Over Output-Layer Detection

As bias accumulates through the model's layers, the final output can diverge from the underlying reasoning process, making output-level confidence an unreliable signal for hallucination detection. Intermediate representations, being less influenced by model bias, offer a more faithful view of the model's latent reasoning process.

The research demonstrates that SSP significantly outperforms prior methods across a range of hallucination detection benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ce6431b-80ce-4694-8b39-5742ded69679",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "3de040ac-c032-4b1e-bc0f-aca72623ff86",
  "sourceToolAssistantUUID": "4ce6431b-80ce-4694-8b39-5742ded69679",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T10:14:01.521Z_

<details><summary>↩ Tool result · `toolu_01KSPySNVBiucYFgHgcm3uvz`</summary>

```text
Web search results for query: "residual stream noise hallucination detection LLM"

Links: [{"title":"Hallucinations in LLMs Are Not a Bug in the Data | Towards Data Science","url":"https://towardsdatascience.com/hallucinations-in-llms-are-not-a-bug-in-the-data/"},{"title":"Published as a conference paper at ICLR 2025 REDEEP: DETECTING HALLUCINATION IN","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable ...","url":"https://aclanthology.org/2025.acl-long.880.pdf"},{"title":"Cross-Layer Attention Probing for Fine-Grained Hallucination Detection","url":"https://arxiv.org/html/2509.09700"},{"title":"Constructing Benchmarks and Interventions for Combating Hallucinations in LLMs","url":"https://arxiv.org/pdf/2404.09971"},{"title":"FACTUM: Mechanistic Detection of Citation Hallucination in Long-Form RAG","url":"https://arxiv.org/pdf/2601.05866"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Dissecting the Ledger: Locating and Suppressing “Liar Circuits” in Financial Large Language Models","url":"https://arxiv.org/html/2511.21756"},{"title":"Detecting Hallucinations in Authentic LLM–Human Interactions","url":"https://arxiv.org/html/2510.10539v1"},{"title":"Enhancing Hallucination Detection through Noise Injection","url":"https://arxiv.org/html/2502.03799"}]

Based on the search results, here's what I found about residual stream noise and hallucination detection in LLMs:

## Key Research Findings

### Residual Stream Dynamics in Hallucinations

Research tracks the trajectory of the residual stream — the internal representation vector — layer by layer through the network to understand hallucination mechanisms. When an LLM hallucinates, the internal representation does not go blank but rotates, with both correct and incorrect paths traveling the same distance through the model's representation space, separated by direction rather than magnitude.

### Hallucination Detection Methods

Several recent approaches leverage residual stream analysis:

1. **Cross-Layer Attention Probing (CLAP)**: A novel probing technique that takes the entire LLM residual stream as a sequence of input tokens, with an attention mechanism operating over the layer-wise activations, enabling fine-grained detection of hallucinations among different responses to a given prompt.

2. **ICR Probe**: The ICR Score (Information Contribution to Residual Stream) defines an ICR Probe that aggregates layer-wise residual updates for reference-free hallucination detection.

3. **ReDeEP Method**: Excessive addition of parametric knowledge by Knowledge FFNs leads to hallucinations, aligning with findings that when external context provides sufficient information, shallow layers can generate truthful responses, but over-reliance on parametric knowledge from deeper layers can confuse the model.

### Noise Injection Approach

Recent work shows noise injection induces epistemic uncertainty where the LLM shows greater uncertainty for hallucinations than non-hallucinations, and combining noise injection with prediction layer sampling improves detection effectiveness by capturing both epistemic and aleatoric uncertainty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f82c68b7-f481-43ab-bbff-cd2ebeb9972c",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "f7862863-dc68-4bea-8f38-2c7ffb30b402",
  "sourceToolAssistantUUID": "f82c68b7-f481-43ab-bbff-cd2ebeb9972c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T10:14:01.736Z_

<details><summary>↩ Tool result · `toolu_016rDxwRYjQyaX1XLvdTJ6HU`</summary>

```text
Web search results for query: "hidden state perturbation LLM confidence hallucination 2025"

Links: [{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://openreview.net/pdf?id=LYx4w3CAgy"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/pdf/2506.02696"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971v1"},{"title":"[Literature Review] Do LLMs Know about Hallucination? An Empirical Investigation of LLM's Hidden States","url":"https://www.themoonlight.io/en/review/do-llms-know-about-hallucination-an-empirical-investigation-of-llms-hidden-states"},{"title":"TruthPrInt: Mitigating Large Vision-Language Models Object Hallucination","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Duan_TruthPrInt_Mitigating_Large_Vision-Language_Models_Object_Hallucination_Via_Latent_Truthful-Guided_ICCV_2025_paper.pdf"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"Mitigating Hallucination in Large Language Models (LLMs): An Application-Oriented Survey on RAG, Reasoning, and Agentic Systems","url":"https://arxiv.org/html/2510.24476v1"},{"title":"A Probabilistic Framework for LLM Hallucination Detection ...","url":"https://aclanthology.org/2025.naacl-long.158.pdf"}]

I found several relevant research papers and articles on hidden state perturbation, LLM confidence, and hallucination detection from 2025. Here are the key findings:

## Recent Research on Hidden State Perturbation and Hallucination Detection

**Perturbation-Based Detection Methods:**
Recent methods perform hallucination detection based on the sensitivity of internal representations to input perturbations, rather than relying on static prompts. One notable approach is Sample-Specific Prompting (SSP), which uses a noise prompt generator to produce perturbations adapted to the input, and then maps the intermediate representations to a discriminative space to maximize the discrepancy between truthful and hallucinated responses. This method improves hallucination detection accuracy by 4.78% (AUROC) on the TruthfulQA benchmark.

**Hidden State-Based Confidence Analysis:**
An emerging metric called Causal Faithfulness uses activation patching to measure divergence between causal effects in model answers, operating on internal hidden states via Symmetric Token Replacement instead of using input perturbations.

Recent work introduces the concept of belief state—a measure of model confidence based on answer repetition consistency—to categorize hallucinations into two types: Overconfident (model confidently lies) and Unaware (model guesses due to missing knowledge), proposing BAFH, a lightweight framework that trains a classifier on hidden states to determine belief state.

**Practical Applications:**
Research on "Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)" addresses confidence calibration in LLMs through hidden state analysis, while other approaches train lightweight probes on intermediate hidden states rather than final-layer outputs, since middle layers retain uncertainty signals that the token-projection step throws away.

These 2025 studies demonstrate a strong focus on leveraging internal model representations and perturbation-based techniques to improve both hallucination detection and confidence calibration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7b57dbb-e54f-4f01-b36c-47c87ec86433",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "e531a491-b1e6-44b5-af96-31e1b727ef97",
  "sourceToolAssistantUUID": "d7b57dbb-e54f-4f01-b36c-47c87ec86433",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T10:14:04.466Z_

Let me search for a few more specific potentially competing methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e531a491-b1e6-44b5-af96-31e1b727ef97",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb655XsTkQPpfTDHufncU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7663461a-0bda-4a81-b2e1-c41ebedde56f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRxBFTeYiGLFZhEFEef8p8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1910,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 13794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2333,
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

_source line 24 · 2026-05-16T10:14:05.079Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KcCSPRzAqUubpu6boB2ket`</summary>

```json
{
  "query": "CCPS \"Calibrating LLM Confidence Probing Perturbed Representation Stability\" arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7663461a-0bda-4a81-b2e1-c41ebedde56f",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb655XsTkQPpfTDHufncU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0630a810-66cf-4bf9-b1e4-75e072ca38bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRxBFTeYiGLFZhEFEef8p8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1910,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 13794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2333,
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

_source line 25 · 2026-05-16T10:14:05.472Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0187EWFbjV3cT5qT9L1ZgtUP`</summary>

```json
{
  "query": "\"enhancing hallucination detection through noise injection\" arxiv 2502.03799"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0630a810-66cf-4bf9-b1e4-75e072ca38bf",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb655XsTkQPpfTDHufncU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38e12865-c0bd-43e2-8aa7-a4806526961c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRxBFTeYiGLFZhEFEef8p8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1910,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 13794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2333,
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

_source line 26 · 2026-05-16T10:14:06.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LFynxg1s897RzDtzNLkkba`</summary>

```json
{
  "query": "\"LLM Hallucination Detection Fast Fourier Transform hidden layer\" arxiv 2509.13154"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38e12865-c0bd-43e2-8aa7-a4806526961c",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb655XsTkQPpfTDHufncU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0adc57ab-726d-4127-99f9-d48c80626a32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRxBFTeYiGLFZhEFEef8p8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1910,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 13794,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2333
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1910,
          "output_tokens": 255,
          "cache_read_input_tokens": 13794,
          "cache_creation_input_tokens": 2333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2333,
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

### Tool call

_source line 27 · 2026-05-16T10:14:06.554Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016TjmKDSVniEXMkGzJYgWXx`</summary>

```json
{
  "query": "\"ICR Probe\" hallucination residual stream detection 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0adc57ab-726d-4127-99f9-d48c80626a32",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb655XsTkQPpfTDHufncU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40d55009-73cb-46ef-88d0-8e55fd0ba9d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRxBFTeYiGLFZhEFEef8p8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1910,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 13794,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2333
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1910,
          "output_tokens": 255,
          "cache_read_input_tokens": 13794,
          "cache_creation_input_tokens": 2333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2333,
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

_source line 28 · 2026-05-16T10:14:11.818Z_

<details><summary>↩ Tool result · `toolu_01LFynxg1s897RzDtzNLkkba`</summary>

```text
Web search results for query: ""LLM Hallucination Detection Fast Fourier Transform hidden layer" arxiv 2509.13154"

Links: [{"title":"[2509.13154] LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals","url":"https://arxiv.org/abs/2509.13154"},{"title":"LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals Citation: Authors. Title. Pages…. DOI:000000/11111.","url":"https://arxiv.org/html/2509.13154"},{"title":"Computation and Language 2025","url":"https://www.arxiv.org/list/cs.CL/2025?skip=12200&show=25"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1089&show=500"},{"title":"Arxiv","url":"https://www.arxiv.org/pdf/2509.11154"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=3125&show=2000"},{"title":"Tongyi DeepResearch Technical Report","url":"https://arxiv.org/html/2510.24701v1"},{"title":"Collections - Hugging Face","url":"https://huggingface.co/collections?paper=2509.13311"},{"title":"Alvaro Velasquez","url":"https://sciprofiles.com/profile/author/bkMwQ01EczEybWcrMDZnU1BPM0x0Zz09"},{"title":"Machine Learning Sep 2025","url":"https://www.arxiv.org/list/cs.LG/2025-09?skip=1025&show=500"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals," and it proposes HSAD (Hidden Signal Analysis-based Detection), a novel hallucination detection framework that models the temporal dynamics of hidden representations during autoregressive generation.

The framework works by constructing hidden-layer signals by sampling activations across layers, applying Fast Fourier Transform (FFT) to obtain frequency-domain representations, and extracting the strongest non-DC frequency component as spectral features.

The paper was authored by Jinxin Li, Gang Tu, ShengYu Cheng, Junjie Hu, Jinting Wang, Rui Chen, Zhilong Zhou, and Dongbo Shan.

The paper is available on arXiv (arxiv:2509.13154) and was published on September 16, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0adc57ab-726d-4127-99f9-d48c80626a32",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "1de43a83-1737-4d72-926a-dd11baa5b05d",
  "sourceToolAssistantUUID": "0adc57ab-726d-4127-99f9-d48c80626a32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T10:14:12.720Z_

<details><summary>↩ Tool result · `toolu_01KcCSPRzAqUubpu6boB2ket`</summary>

```text
Web search results for query: "CCPS "Calibrating LLM Confidence Probing Perturbed Representation Stability" arxiv 2025"

Links: [{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250521772K/abstract"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/calibrating-llm-confidence-by-probing-perturbed-representation"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | alphaXiv","url":"https://www.alphaxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed ...","url":"https://www.alphaxiv.org/resources/2505.21772v2"},{"title":"Calibrating LLM Confidence by Probing Perturbed ...","url":"https://bytez.com/docs/arxiv/2505.21772/paper"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"}]

I found the research paper you're looking for. Here are the key details:

## CCPS Paper Overview

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method analyzing internal representational stability in LLMs.

**ArXiv Details:**
- **Paper ID:** 2505.21772
- **Published:** May 27, 2025 (with v2 update September 18, 2025)
- **Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese H. Smiley, Kundan Thind, and Mohammad M. Ghassemi

**How It Works:**
CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness.

**Evaluation Scope:**
CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats.

**Results:**
Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points, all relative to the strongest prior method.

**Additional Resources:**
- The paper was also published at EMNLP 2025 (pages 10448-10514)
- Official code implementation is available on GitHub at: https://github.com/ledengary/CCPS


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0630a810-66cf-4bf9-b1e4-75e072ca38bf",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "96fdd496-5ffc-45ed-a80a-5ac06262c512",
  "sourceToolAssistantUUID": "0630a810-66cf-4bf9-b1e4-75e072ca38bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T10:14:13.478Z_

<details><summary>↩ Tool result · `toolu_016TjmKDSVniEXMkGzJYgWXx`</summary>

```text
Web search results for query: ""ICR Probe" hallucination residual stream detection 2025"

Links: [{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable ...","url":"https://aclanthology.org/2025.acl-long.880.pdf"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.880/"},{"title":"[2507.16488] ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/abs/2507.16488"},{"title":"[2507.16488v1] ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/abs/2507.16488v1"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/html/2507.16488v1"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250716488Z/abstract"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination","url":"https://arxiv.org/pdf/2507.16488"},{"title":"[PDF] ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ICR-Probe:-Tracking-Hidden-State-Dynamics-for-in-Zhang-Hu/bb419a4952376815243456a7d44fa8c3eb78330f"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://www.researchgate.net/publication/393923702_ICR_Probe_Tracking_Hidden_State_Dynamics_for_Reliable_Hallucination_Detection_in_LLMs"},{"title":"Published as a conference paper at ICLR 2025 REDEEP: DETECTING HALLUCINATION IN","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf"}]

Based on the search results, I found comprehensive information about the ICR Probe research from 2025:

## ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection

The ICR Probe is a hallucination detection method which captures the cross-layer evolution of hidden states. The research introduces a novel metric, the ICR Score (Information Contribution to Residual Stream), which quantifies the contribution of modules to the hidden states' update.

### Key Innovation

Existing hallucination detection methods leveraging hidden states predominantly focus on static and isolated representations, overlooking their dynamic evolution across layers, which limits efficacy. To address this limitation, the researchers shift the focus to the hidden state update process and introduce the ICR Score.

### Methodology

The method first probes each layer's residual stream to obtain the ICR Score, then aggregates the ICR Scores across all layers to capture global information. This aggregated signal serves as the input to the probe, which produces the final hallucination detection result.

### Performance

Experimental results show that the ICR Probe achieves superior performance with significantly fewer parameters. Experimental results on three mainstream open-source LLMs demonstrate that the ICR Probe effectively detects hallucinations and outperforms previous methods across multiple datasets.

The paper was published at ACL 2025 (the 63rd Annual Meeting of the Association for Computational Linguistics) by Zhang et al., and became available on arXiv in July 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40d55009-73cb-46ef-88d0-8e55fd0ba9d5",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "2e38a4a8-91d3-4c92-ab77-310ccef0c881",
  "sourceToolAssistantUUID": "40d55009-73cb-46ef-88d0-8e55fd0ba9d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T10:14:14.081Z_

<details><summary>↩ Tool result · `toolu_0187EWFbjV3cT5qT9L1ZgtUP`</summary>

```text
Web search results for query: ""enhancing hallucination detection through noise injection" arxiv 2502.03799"

Links: [{"title":"[2502.03799] Enhancing Hallucination Detection through Noise Injection","url":"https://arxiv.org/abs/2502.03799"},{"title":"Enhancing Hallucination Detection through Noise Injection","url":"https://arxiv.org/html/2502.03799"},{"title":"Enhancing Hallucination Detection through Noise Injection | alphaXiv","url":"https://www.alphaxiv.org/ja/overview/2502.03799v1"},{"title":"Noise Augmented Fine Tuning for Mitigating Hallucinations in Large Language Models","url":"https://arxiv.org/html/2504.03302v2"},{"title":"Enhancing Hallucination Detection with Noise Injection | OpenReview","url":"https://openreview.net/forum?id=2bWf4M5tRo"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=1875&show=2000"},{"title":"Demystifying Hallucination in Speech Foundation Models","url":"https://aclanthology.org/2025.findings-acl.1190.pdf"},{"title":"Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis","url":"https://arxiv.org/html/2502.08663v1"},{"title":"[2407.05474] Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/abs/2407.05474"},{"title":"Hallucinations","url":"https://www.aussieai.com/research/hallucinations"}]

I found the paper! Here's information about arxiv 2502.03799:

## "Enhancing Hallucination Detection through Noise Injection"

**Authors:** Litian Liu, Reza Pourreza, Sunny Panchal, Apratim Bhattacharyya, Yubing Jian, Yao Qin, and Roland Memisevic from Qualcomm AI Research and UC Santa Barbara

**Main Contribution:** The paper addresses the problem that Large Language Models (LLMs) are prone to generating plausible yet incorrect responses known as hallucinations, which is crucial to detect for safe deployment of LLMs.

**Key Approach:** Recent research has linked hallucinations to model uncertainty, suggesting that hallucinations can be detected by measuring dispersion over answer distributions obtained from multiple samples drawn from a model. However, the authors argue that drawing from the distribution over tokens defined by the model is suboptimal for detecting hallucinations, and propose that detection can be improved significantly by taking into account model uncertainty in the Bayesian sense through a simple, training-free approach based on perturbing an appropriate subset of model parameters, or equivalently hidden unit activations, during sampling.

**Status:** The paper is accepted as an ICLR 2026 main conference paper, with the latest version (v3) dated March 1, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38e12865-c0bd-43e2-8aa7-a4806526961c",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "6f0fa638-b6de-4d72-9bd3-e3935926d9b1",
  "sourceToolAssistantUUID": "38e12865-c0bd-43e2-8aa7-a4806526961c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T10:14:17.080Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014aESEzjajhxD8LEL7tB2FB`</summary>

```json
{
  "query": "\"Cross-Layer Attention Probing\" CLAP hallucination detection arxiv 2509.09700"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f0fa638-b6de-4d72-9bd3-e3935926d9b1",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb656SgT7Jx288acuLHps",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b400c1dd-60dd-4ab2-a60a-7d9c823f947f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsgaoAHriz1HTT6H84tTvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1721,
      "cache_creation_input_tokens": 4018,
      "cache_read_input_tokens": 16127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4018,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 33 · 2026-05-16T10:14:17.670Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CQFksCjVeCo11FpnxaSiRb`</summary>

```json
{
  "query": "ReDeEP hallucination detection ICLR 2025 parametric knowledge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b400c1dd-60dd-4ab2-a60a-7d9c823f947f",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb656SgT7Jx288acuLHps",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "644d0348-043e-469f-abe5-10ae7fc28b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsgaoAHriz1HTT6H84tTvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1721,
      "cache_creation_input_tokens": 4018,
      "cache_read_input_tokens": 16127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4018,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 34 · 2026-05-16T10:14:18.239Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012DtTrrwx9H9jBwZojCMRko`</summary>

```json
{
  "query": "LSP \"latent space perturbation\" hallucination detection LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "644d0348-043e-469f-abe5-10ae7fc28b17",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb656SgT7Jx288acuLHps",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f31f4208-4992-4011-8f8b-0e86cd6adc42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsgaoAHriz1HTT6H84tTvY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1721,
      "cache_creation_input_tokens": 4018,
      "cache_read_input_tokens": 16127,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4018
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1721,
          "output_tokens": 186,
          "cache_read_input_tokens": 16127,
          "cache_creation_input_tokens": 4018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4018,
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

_source line 35 · 2026-05-16T10:14:26.671Z_

<details><summary>↩ Tool result · `toolu_012DtTrrwx9H9jBwZojCMRko`</summary>

```text
Web search results for query: "LSP "latent space perturbation" hallucination detection LLM 2025 2026"

Links: [{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"How to evaluate LLM hallucination rates in engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/how-to-evaluate-llm-hallucination-rates-in-engineering/"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"Are you hallucinated? Insights into large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405959525002115"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"[2503.01917] Steer LLM Latents for Hallucination Detection","url":"https://arxiv.org/abs/2503.01917"},{"title":"Steer LLM Latents for Hallucination Detection","url":"https://arxiv.org/html/2503.01917v2"},{"title":"LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals Citation: Authors. Title. Pages…. DOI:000000/11111.","url":"https://arxiv.org/html/2509.13154v1"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971"}]

I found relevant research on latent space perturbation methods for hallucination detection in LLMs from 2025-2026. Here are the key findings:

## Recent Research on LSP and Hallucination Detection

### Perturbation-Based Approaches

Sample-Specific Prompting (SSP) is a framework that improves self-assessment by analyzing perturbation sensitivity at intermediate representations, which offer a more faithful view of the model's latent reasoning process being less influenced by model bias. The method maps both original and perturbed intermediate representations into the same latent space, with an encoder designed to preserve feature information of LLM embeddings while amplifying the discrepancy between truthful and hallucinated responses.

### Latent Space Steering Methods

Recent approaches have leveraged the latent space of LLMs for hallucination detection, but their embeddings, optimized for linguistic coherence rather than factual accuracy, often fail to clearly separate truthful and hallucinated content. Activation engineering enables control over LLM generation during inference by applying task-specific steering vectors into the model's internal representation, with several studies mitigating hallucination by shifting activations along the truthful direction identified by analyzing activation differences between contrastive pairs.

### Patent-Based Innovations

JPMorgan Chase Bank's 2025 patent on hallucination probability prediction formalizes query perturbation: incoming queries are perturbed n times into lexically divergent but semantically equivalent variations, with n+1 independent agents sampling outputs for each variant, and a statistical simulation algorithm applied across sampled outputs to derive empirical expected hallucination rates.

Vodafone Group Services Limited's VAE-based hallucination detection architecture maps LLM output vectors into a dimensionally reduced latent space, comparing them against a distribution of factually grounded responses pre-trained on labeled datasets — enabling hallucination detection in RAG-enhanced LLMs without requiring ground truth at inference time.

These approaches represent the state-of-the-art in using perturbation and latent space manipulation for reliable hallucination detection in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f31f4208-4992-4011-8f8b-0e86cd6adc42",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "9b199c74-7cbe-497c-9f18-9877b9036209",
  "sourceToolAssistantUUID": "f31f4208-4992-4011-8f8b-0e86cd6adc42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T10:14:26.711Z_

<details><summary>↩ Tool result · `toolu_014aESEzjajhxD8LEL7tB2FB`</summary>

```text
Web search results for query: ""Cross-Layer Attention Probing" CLAP hallucination detection arxiv 2509.09700"

Links: [{"title":"[2509.09700] Cross-Layer Attention Probing for Fine-Grained Hallucination Detection","url":"https://arxiv.org/abs/2509.09700"},{"title":"Cross-Layer Attention Probing for Fine-Grained Hallucination Detection","url":"https://arxiv.org/html/2509.09700v1/"},{"title":"Hallucination detection performance of CLAP versus baselines, measured... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Hallucination-detection-performance-of-CLAP-versus-baselines-measured-in-AUC-scores_tbl1_395474068"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://arxiv.org/html/2509.24770v1"},{"title":"VADE: Visual Attention Guided Hallucination Detection and ...","url":"https://aclanthology.org/2025.findings-acl.773.pdf"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=4twbqwV4br"},{"title":"Cross-Layer Attention Probing for Fine-Grained ...","url":"https://chatpaper.com/zh-CN/chatpaper/paper/187999"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v2"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection | Request PDF","url":"https://www.researchgate.net/publication/395972306_Neural_Message-Passing_on_Attention_Graphs_for_Hallucination_Detection"}]

I found the paper! Here's what the search revealed about Cross-Layer Attention Probing (CLAP):

Cross-Layer Attention Probing (CLAP) is a novel activation probing technique for hallucination detection that processes LLM activations across the entire residual stream as a joint sequence.

**Key Features:**

CLAP improves hallucination detection compared to baselines on both greedy decoded responses and responses sampled at higher temperatures, enabling fine-grained detection—the ability to disambiguate hallucinations and non-hallucinations among different sampled responses to a given prompt.

The method constructs a sequence of tokens by considering the activations at each LLM layer as an input token, and employs an attention mechanism over the sequence input.

**Applications:**

CLAP enables a detect-then-mitigate strategy to reduce hallucinations and improve LLM reliability compared to direct mitigation approaches. The combination of CLAP with DoLa (a hallucination mitigation method) significantly reduces the hallucination rate.

**Robustness:**

CLAP maintains high reliability even when applied out-of-distribution.

The paper (arxiv 2509.09700) was published on September 4, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b400c1dd-60dd-4ab2-a60a-7d9c823f947f",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "fbe63fd8-19c7-4418-94fd-1842eab3f205",
  "sourceToolAssistantUUID": "b400c1dd-60dd-4ab2-a60a-7d9c823f947f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-16T10:14:26.776Z_

<details><summary>↩ Tool result · `toolu_01CQFksCjVeCo11FpnxaSiRb`</summary>

```text
Web search results for query: "ReDeEP hallucination detection ICLR 2025 parametric knowledge"

Links: [{"title":"Published as a conference paper at ICLR 2025 REDEEP: DETECTING HALLUCINATION IN","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf"},{"title":"ReDeEP: Detecting Hallucination in Retrieval-","url":"https://iclr.cc/media/iclr-2025/Slides/27644.pdf"},{"title":"GitHub - Jeryi-Sun/ReDEeP-ICLR: The implement of paper:\"ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability\" · GitHub","url":"https://github.com/Jeryi-Sun/ReDEeP-ICLR"},{"title":"ICLR Poster ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability","url":"https://iclr.cc/virtual/2025/poster/27644"},{"title":"ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/7daf60e805e596c3bd1e843e72ea5560-Abstract-Conference.html"},{"title":"ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=ztzZDzgfrh"},{"title":"(PDF) ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability","url":"https://www.researchgate.net/publication/384937652_ReDeEP_Detecting_Hallucination_in_Retrieval-Augmented_Generation_via_Mechanistic_Interpretability"},{"title":"Published as a conference paper at ICLR 2025 REDEEP: DETECTING HALLUCINATION IN","url":"https://www.arxiv.org/pdf/2410.11414v1"},{"title":"Interpretable Signals for Detecting Hallucinations in ...","url":"https://openreview.net/pdf?id=TZzBKwHLwF"},{"title":"[2410.11414] ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability","url":"https://arxiv.org/abs/2410.11414"}]

Based on the web search results, I found comprehensive information about ReDeEP, a paper published at ICLR 2025 focused on hallucination detection in Retrieval-Augmented Generation (RAG) systems.

## Summary of ReDeEP

ReDeEP is a novel method that detects hallucinations by decoupling LLM's utilization of external context and parametric knowledge.

### Key Findings on Parametric Knowledge

The research makes important discoveries about how parametric knowledge relates to hallucinations. Hallucinations occur when the Knowledge FFNs in LLMs overemphasize parametric knowledge in the residual stream, while Copying Heads fail to effectively retain or integrate external knowledge from retrieved content.

More specifically, hallucinations arise from insufficient utilization of external context by Copying Heads and over-reliance on parametric knowledge by Knowledge FFN modules.

### Approach

Mechanistic interpretability effectively decouples the LLM's utilization of external context and parametric knowledge, enabling more accurate detection of RAG hallucinations. ReDeEP surpasses both ECP and PCE methods by incorporating both the External Context Score and Parametric Knowledge Score as covariates in a multivariate regression approach.

### Results and Related Work

ReDeEP significantly improves RAG hallucination detection accuracy, and the authors also introduce AARF, which mitigates hallucinations by modulating the contributions of Knowledge FFNs and Copying Heads.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "644d0348-043e-469f-abe5-10ae7fc28b17",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "d4d28a75-85fe-4214-93d5-e065c515209d",
  "sourceToolAssistantUUID": "644d0348-043e-469f-abe5-10ae7fc28b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T10:14:30.116Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F2HtpTPzFCLiFKHH7RtR9v`</summary>

```json
{
  "query": "\"Steer LLM Latents for Hallucination Detection\" arxiv 2503.01917"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4d28a75-85fe-4214-93d5-e065c515209d",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb657NwWDZKD6pdB7gnoX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f03b6088-b958-4d51-adac-8acedc7dad5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrU357AbJvFaHhNmwAyBk2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1065,
      "cache_creation_input_tokens": 3810,
      "cache_read_input_tokens": 20145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3810,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 39 · 2026-05-16T10:14:30.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J6h5i98BPfwtNv3SbVX6ym`</summary>

```json
{
  "query": "HaloScope hallucination detection NeurIPS 2024 internal representations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f03b6088-b958-4d51-adac-8acedc7dad5d",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb657NwWDZKD6pdB7gnoX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56b703c7-43b8-488c-95d3-5c740f848293",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrU357AbJvFaHhNmwAyBk2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1065,
      "cache_creation_input_tokens": 3810,
      "cache_read_input_tokens": 20145,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3810
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1065,
          "output_tokens": 127,
          "cache_read_input_tokens": 20145,
          "cache_creation_input_tokens": 3810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3810,
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

_source line 40 · 2026-05-16T10:14:36.833Z_

<details><summary>↩ Tool result · `toolu_01F2HtpTPzFCLiFKHH7RtR9v`</summary>

```text
Web search results for query: ""Steer LLM Latents for Hallucination Detection" arxiv 2503.01917"

Links: [{"title":"[2503.01917] Steer LLM Latents for Hallucination Detection","url":"https://arxiv.org/abs/2503.01917"},{"title":"Steer LLM Latents for Hallucination Detection","url":"https://arxiv.org/pdf/2503.01917"},{"title":"How to Steer LLM Latents for Hallucination Detection?","url":"https://www.arxiv.org/pdf/2503.01917v1"},{"title":"How to Steer LLM Latents for Hallucination Detection?","url":"https://arxiv.org/html/2503.01917v1"},{"title":"Paper page - How to Steer LLM Latents for Hallucination Detection?","url":"https://huggingface.co/papers/2503.01917"},{"title":"LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals Citation: Authors. Title. Pages…. DOI:000000/11111.","url":"https://arxiv.org/html/2509.13154v1"},{"title":"How to Steer LLM Latents for Hallucination Detection? | alphaXiv","url":"https://www.alphaxiv.org/abs/2503.01917"},{"title":"(PDF) How to Steer LLM Latents for Hallucination Detection?","url":"https://www.researchgate.net/publication/389579593_How_to_Steer_LLM_Latents_for_Hallucination_Detection"},{"title":"[Literature Review] How to Steer LLM Latents for Hallucination Detection?","url":"https://www.themoonlight.io/en/review/how-to-steer-llm-latents-for-hallucination-detection"},{"title":"Hallucination, Monofacts, and Miscalibration: An Empirical Investigation","url":"https://arxiv.org/html/2502.08666v2"}]

I found the paper! Here's information about "Steer LLM Latents for Hallucination Detection" (arXiv:2503.01917):

## Paper Overview

Hallucinations in LLMs pose a significant concern to their safe deployment in real-world applications. Recent approaches have leveraged the latent space of LLMs for hallucination detection, but their embeddings, optimized for linguistic coherence rather than factual accuracy, often fail to clearly separate truthful and hallucinated content.

## Key Contribution: Truthfulness Separator Vector (TSV)

The paper proposes the Truthfulness Separator Vector (TSV), a lightweight and flexible steering vector that reshapes the LLM's representation space during inference to enhance the separation between truthful and hallucinated outputs, without altering model parameters.

## Methodology

The two-stage framework first trains TSV on a small set of labeled exemplars to form compact and well-separated clusters. It then augments the exemplar set with unlabeled LLM generations, employing an optimal transport-based algorithm for pseudo-labeling combined with a confidence-based filtering process.

## Authors

The paper is authored by Seongheon Park, Xuefeng Du, Min-Hsuan Yeh, Haobo Wang, and Yixuan Li.

The paper was submitted on March 1, 2025, and has a revised version (v2) dated May 22, 2025. You can access it directly at https://arxiv.org/abs/2503.01917.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f03b6088-b958-4d51-adac-8acedc7dad5d",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "21c35d33-fffc-458e-80f3-bd81fe8b5caf",
  "sourceToolAssistantUUID": "f03b6088-b958-4d51-adac-8acedc7dad5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T10:14:37.054Z_

<details><summary>↩ Tool result · `toolu_01J6h5i98BPfwtNv3SbVX6ym`</summary>

```text
Web search results for query: "HaloScope hallucination detection NeurIPS 2024 internal representations"

Links: [{"title":"HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/ba92705991cfbbcedc26e27e833ebbae-Paper-Conference.pdf"},{"title":"GitHub - deeplearning-wisc/haloscope: source code for NeurIPS'24 paper \"HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection\" · GitHub","url":"https://github.com/deeplearning-wisc/haloscope"},{"title":"HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection","url":"https://openreview.net/pdf?id=nfK0ZXFFSn"},{"title":"NeurIPS Poster HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection","url":"https://neurips.cc/virtual/2024/poster/93676"},{"title":"HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection","url":"https://neurips.cc/media/neurips-2024/Slides/93676.pdf"},{"title":"HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection","url":"https://www.researchgate.net/publication/397203607_HaloScope_Harnessing_Unlabeled_LLM_Generations_for_Hallucination_Detection"},{"title":"HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection | PromptLayer","url":"https://www.promptlayer.com/research-papers/haloscope-harnessing-unlabeled-llm-generations-for-hallucination-detection"},{"title":"NeurIPS Poster Hallo3D: Multi-Modal Hallucination Detection and Mitigation for Consistent 3D Content Generation","url":"https://neurips.cc/virtual/2024/poster/93528"},{"title":"NeurIPS Poster LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://neurips.cc/virtual/2024/poster/95584"},{"title":"Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/html/2504.07863v2"}]

I found comprehensive information about HaloScope from NeurIPS 2024. Here's a summary of the key findings:

## Overview

HaloScope is a novel learning framework that leverages unlabeled LLM generations in the wild for hallucination detection. It was presented as a NeurIPS 2024 spotlight paper by Xuefeng Du, Chaowei Xiao, and Yixuan Li.

## How It Works with Internal Representations

HaloScope identifies a subspace in the activation space associated with hallucinated statements, with the top singular vectors forming the latent subspace for membership estimation. The membership estimation score measures the norm of the embedding projected onto the top singular vectors, which exhibits different magnitudes for truthful versus hallucinated data.

## Layer Analysis

An important finding concerns which layers are most effective: hallucination detection performance initially increases from the top to middle layers (e.g., 8-14th layers), followed by a subsequent decline, suggesting a gradual capture of contextual information by LLMs in the first few layers, followed by a tendency towards overconfidence in the final layers due to the autoregressive training objective.

## Performance

HaloScope outperforms uncertainty-based and consistency-based baselines, exhibiting 16.47% and 26.71% improvements.

The official paper and code are available through the NeurIPS proceedings and GitHub repository (deeplearning-wisc/haloscope).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56b703c7-43b8-488c-95d3-5c740f848293",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a1e666978809ea371",
  "type": "user",
  "uuid": "4e78d618-3b93-4ade-939e-e6fa93ae08db",
  "sourceToolAssistantUUID": "56b703c7-43b8-488c-95d3-5c740f848293",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-16T10:15:28.759Z_

Here is my comprehensive report on the papers and competing work:

---

## Paper 1: SHINE (Lee et al., arXiv 2411.09689)

**Title:** "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge"

**Core Method:** SHINE introduces a "hallucination probing" task that classifies LLM-generated text into three categories: aligned, misaligned, and fabricated. It uses Entity Perturbation Impact (measured via KL divergence) to detect hallucinations without requiring external knowledge, supervised training, or LLM fine-tuning.

**How it works (two stages):**
1. **Model Knowledge Test** -- Perturbs key entities in the input prompt and measures KL divergence of the output distribution. Fabricated text shows very low KL divergence (mean 0.21) because tokens are weakly tied to key entities, while aligned (0.92) and misaligned (1.36) text shows higher divergence.
2. **Alignment Test** -- Differentiates aligned from misaligned text after the first stage filters out fabrications.

**Key insight:** If perturbing entities in the prompt barely changes the output distribution, the LLM's response was likely fabricated (not grounded in knowledge about those entities).

---

## Paper 2: SSP / "Shaking to Reveal" (Luo et al., arXiv 2506.02696)

**Title:** "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations"

**Authors:** Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, and Ling Chen

**Core Method:** Sample-Specific Prompting (SSP) -- a framework that detects hallucinations by analyzing perturbation sensitivity at **intermediate representations** rather than output-level confidence.

**How it works:**
- Dynamically generates controlled noise prompts tailored to each question-answer pair (not static/handcrafted prompts)
- Appends the noise prompt to the original answer and passes it through a shared LLM backbone
- Uses a lightweight encoder to map intermediate representations to a discriminative space, maximizing discrepancy between truthful and hallucinated responses
- Employs a contrastive distance metric to quantify representational shifts

**Key insight:** As bias accumulates through LLM layers, final output diverges from underlying reasoning, making output-level confidence unreliable. Intermediate representations offer a more faithful view of the model's latent reasoning.

**Result:** +4.78% AUROC improvement on TruthfulQA over SOTA methods.

---

## Potentially Competing / Uncited Work (2025-2026)

### 1. CCPS -- "Calibrating LLM Confidence by Probing Perturbed Representation Stability" (arXiv 2505.21772, EMNLP 2025)
**Authors:** Khanmohammadi, Miahi, et al.
**Method:** Applies targeted adversarial perturbations to **final hidden states**, extracts features reflecting the model's response to perturbations, and uses a lightweight classifier to predict answer correctness. Reduces Expected Calibration Error by ~55% and Brier score by 21%. Published at EMNLP 2025.
**Relevance to LSP:** Very high -- directly perturbs hidden representations and measures stability, closely related to latent-space perturbation approaches.

### 2. "Enhancing Hallucination Detection through Noise Injection" (arXiv 2502.03799, ICLR 2026)
**Authors:** Liu, Pourreza, et al. (Qualcomm AI Research / UC Santa Barbara)
**Method:** Instead of sampling from the model's token distribution, perturbs an appropriate subset of model parameters (or equivalently hidden unit activations) during sampling to induce epistemic uncertainty. Hallucinations show greater uncertainty than non-hallucinations under noise injection. Training-free approach.
**Status:** Accepted at ICLR 2026 main conference.
**Relevance to LSP:** Extremely high -- directly perturbs hidden activations to detect hallucinations.

### 3. "Steer LLM Latents for Hallucination Detection" (arXiv 2503.01917)
**Authors:** Seongheon Park, Xuefeng Du, Min-Hsuan Yeh, Haobo Wang, Yixuan Li (March 2025)
**Method:** Proposes a Truthfulness Separator Vector (TSV) -- a lightweight steering vector that reshapes the LLM's representation space during inference to enhance separation between truthful and hallucinated outputs without altering model parameters. Uses optimal transport-based pseudo-labeling.
**Relevance to LSP:** High -- operates in latent space to separate truthful/hallucinated content, though it steers rather than perturbs.
**Note:** Authors overlap with the SSP paper (Park, Li).

### 4. ICR Probe -- "Tracking Hidden State Dynamics for Reliable Hallucination Detection" (arXiv 2507.16488, ACL 2025)
**Authors:** Zhang, Hu, et al.
**Method:** Defines an ICR Score (Information Contribution to Residual Stream) that quantifies each layer's contribution to hidden state updates. Aggregates ICR Scores across all layers to capture global dynamics, then feeds this to a lightweight probe for detection.
**Relevance to LSP:** Moderate-high -- analyzes residual stream dynamics layer-by-layer but does not perturb; focuses on how information flows rather than stability under perturbation.

### 5. CLAP -- "Cross-Layer Attention Probing for Fine-Grained Hallucination Detection" (arXiv 2509.09700, September 2025)
**Method:** Treats activations at each LLM layer as input tokens to a cross-layer attention mechanism. Enables fine-grained detection (distinguishing hallucinations among different sampled responses to the same prompt). Robust out-of-distribution.
**Relevance to LSP:** Moderate -- processes the full residual stream but uses attention probing rather than perturbation.

### 6. HSAD -- "LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals" (arXiv 2509.13154, September 2025)
**Authors:** Jinxin Li, Gang Tu, et al.
**Method:** Models temporal dynamics of hidden representations during autoregressive generation. Samples activations across layers, applies FFT to get frequency-domain representations, and extracts spectral features for hallucination classification.
**Relevance to LSP:** Moderate -- analyzes hidden layer signals but from a frequency-domain perspective rather than perturbation.

### 7. ReDeEP -- ICLR 2025 (arXiv 2410.11414)
**Method:** Uses mechanistic interpretability to decouple the LLM's use of external context (via Copying Heads) from parametric knowledge (via Knowledge FFNs). Hallucinations arise when Knowledge FFNs overemphasize parametric knowledge in the residual stream.
**Relevance to LSP:** Moderate -- focused on RAG hallucination and uses mechanistic interpretability rather than perturbation, but operates on residual stream analysis.

### 8. HaloScope -- NeurIPS 2024
**Authors:** Xuefeng Du, Chaowei Xiao, Yixuan Li
**Method:** Identifies a subspace in the activation space associated with hallucinated statements via singular vector decomposition. Finds middle layers (8-14) most effective for detection. Uses unlabeled data.
**Relevance to LSP:** Moderate -- predecessor work from the same research group (Li, Du, Park appear across HaloScope, TSV, and SSP papers).

---

## Key Observations

1. **The Yixuan Li research group** (Wisconsin) appears to be the most prolific in this space, producing HaloScope (NeurIPS 2024), TSV/Steer LLM Latents (March 2025), and SSP/Shaking to Reveal (June 2025) -- all operating on internal representations for hallucination detection.

2. **Most directly competing with any "LSP" method** would be:
   - **CCPS** (EMNLP 2025) -- perturbs hidden states, measures stability
   - **Noise Injection** (ICLR 2026) -- perturbs hidden activations during sampling
   - **SSP** itself -- perturbs intermediate representations via learned noise prompts

3. **The field is converging** on the insight that intermediate/hidden representations are more reliable signals than output-level confidence, with methods diverging on *how* they extract the signal (perturbation, probing, spectral analysis, steering vectors).

Sources:
- [SHINE - arXiv 2411.09689](https://arxiv.org/abs/2411.09689)
- [SSP/Shaking to Reveal - arXiv 2506.02696](https://arxiv.org/abs/2506.02696)
- [CCPS - arXiv 2505.21772](https://arxiv.org/abs/2505.21772)
- [Noise Injection - arXiv 2502.03799](https://arxiv.org/abs/2502.03799)
- [Steer LLM Latents/TSV - arXiv 2503.01917](https://arxiv.org/abs/2503.01917)
- [ICR Probe - arXiv 2507.16488](https://arxiv.org/abs/2507.16488)
- [CLAP - arXiv 2509.09700](https://arxiv.org/abs/2509.09700)
- [HSAD/FFT Method - arXiv 2509.13154](https://arxiv.org/abs/2509.13154)
- [ReDeEP - arXiv 2410.11414](https://arxiv.org/abs/2410.11414)
- [HaloScope - NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/file/ba92705991cfbbcedc26e27e833ebbae-Paper-Conference.pdf)
- [Edinburgh NLP Awesome Hallucination Detection](https://github.com/EdinburghNLP/awesome-hallucination-detection)
- [CCPS GitHub Repository](https://github.com/ledengary/CCPS)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e78d618-3b93-4ade-939e-e6fa93ae08db",
  "isSidechain": true,
  "agentId": "a1e666978809ea371",
  "requestId": "req_011Cb6588tS5jSHyUCZCdL27",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "866dc9f5-8628-4782-98f8-59258066b9f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeGCnNjjwEFSw4QM48peCa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3116,
      "cache_read_input_tokens": 23955,
      "output_tokens": 2537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3116
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2537,
          "cache_read_input_tokens": 23955,
          "cache_creation_input_tokens": 3116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3116,
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
