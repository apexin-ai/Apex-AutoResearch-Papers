# Research conversation: I'm reviewing an ML paper idea that applies prioritized experience replay with chunk-decomposed loss to VLA (Vision-Lang

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa8e627ca68bfa3d5.jsonl`
- **Structured JSON:** [`5fb818d28453534b55e2.json`](../../sessions/5f/5fb818d28453534b55e2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-13T17:39:56.426Z_

I'm reviewing an ML paper idea that applies prioritized experience replay with chunk-decomposed loss to VLA (Vision-Language-Action) model SFT. I need to verify several related works and find any missing ones.

Search for:

1. "Token Cleaning ICML 2025 arXiv:2502.01968" — verify this exists and is ICML 2025 Spotlight
2. "iw-SFT supervised fine tuning reinforcement learning arXiv:2507.12856" — verify this exists
3. "Freshness-Aware Prioritized Experience Replay LLM VLM arXiv:2604.16918" — verify this exists
4. "SCIZOR self-supervised data curation imitation learning ICRA 2026" — verify venue
5. "CUPID curating data influence functions CoRL 2025" — verify venue
6. "DataMIL datamodels imitation learning ICLR 2026" — verify venue
7. "adaptive sample weighting robot learning 2026" — find any new competing work
8. "prioritized replay supervised fine-tuning continuous action 2025 2026" — find concurrent work

For each, use WebSearch to find the paper and report: does it exist? What venue? What does it actually do? Is there any work I might be missing that decomposes losses at sub-sample level for robot learning?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "35607709-df60-4d4c-8113-833e9eb32379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T17:39:56.428Z_

```json
{
  "parentUuid": "35607709-df60-4d4c-8113-833e9eb32379",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
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
  "uuid": "42468d1e-e61f-4045-8e38-caa0c7731729",
  "timestamp": "2026-05-13T17:39:56.428Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T17:40:00.121Z_



I'll systematically search for each paper and verify the claims. Let me start by loading the WebSearch tool, then conduct all searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42468d1e-e61f-4045-8e38-caa0c7731729",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyezMd9unuVVzVDGk3u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8e31204-edd7-498e-9326-53f14c9c3f9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsdaG8k8VqZYK4ikrrYDfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 866,
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

_source line 4 · 2026-05-13T17:40:00.374Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LftZm2HVwRVsucAnE1wXWS`</summary>

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
  "parentUuid": "e8e31204-edd7-498e-9326-53f14c9c3f9c",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyezMd9unuVVzVDGk3u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fb810d0-3d2d-45b7-b91c-b85bf0a9fd34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsdaG8k8VqZYK4ikrrYDfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 866,
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

### Tool result

_source line 5 · 2026-05-13T17:40:00.377Z_

<details><summary>↩ Tool result · `toolu_01LftZm2HVwRVsucAnE1wXWS`</summary>

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
  "parentUuid": "0fb810d0-3d2d-45b7-b91c-b85bf0a9fd34",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "a013da63-4002-43b0-b4e9-c94ae0eb8dd6",
  "sourceToolAssistantUUID": "0fb810d0-3d2d-45b7-b91c-b85bf0a9fd34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T17:40:03.342Z_



Now let me conduct all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a013da63-4002-43b0-b4e9-c94ae0eb8dd6",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyfHx3QiF39f7cUFSy1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bd14e3d-7ab6-4bd3-9e5d-9dc604b36078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuAqquwUTsmc4A9oi42jdp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 7 · 2026-05-13T17:40:04.205Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AhVsw4eA2yknL6ENngBywz`</summary>

```json
{
  "query": "Token Cleaning ICML 2025 arXiv 2502.01968"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bd14e3d-7ab6-4bd3-9e5d-9dc604b36078",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyfHx3QiF39f7cUFSy1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb4ff198-1e6a-4250-aead-4955ccea37f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuAqquwUTsmc4A9oi42jdp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 8 · 2026-05-13T17:40:04.748Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XhDJ4vEExb5bLY1f4n9MLb`</summary>

```json
{
  "query": "iw-SFT importance weighted supervised fine tuning reinforcement learning arXiv 2507.12856"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb4ff198-1e6a-4250-aead-4955ccea37f5",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyfHx3QiF39f7cUFSy1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e2bf305-3278-4eff-ab29-d454aa2ee7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuAqquwUTsmc4A9oi42jdp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 9 · 2026-05-13T17:40:04.832Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jw9NL62W3kzDqSSkvGHUNS`</summary>

```json
{
  "query": "Freshness-Aware Prioritized Experience Replay LLM VLM arXiv 2604.16918"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e2bf305-3278-4eff-ab29-d454aa2ee7a2",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyfHx3QiF39f7cUFSy1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a1b0a72-29b7-46a0-919b-3cf032ed5464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuAqquwUTsmc4A9oi42jdp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 10 · 2026-05-13T17:40:05.063Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qd3bNkUjsyPXeLWo8bdH14`</summary>

```json
{
  "query": "SCIZOR self-supervised data curation imitation learning ICRA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a1b0a72-29b7-46a0-919b-3cf032ed5464",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyfHx3QiF39f7cUFSy1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ecac353-d22c-49dc-b6e3-fca051522502",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuAqquwUTsmc4A9oi42jdp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9089,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1422
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 256,
          "cache_read_input_tokens": 9089,
          "cache_creation_input_tokens": 1422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1422,
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

_source line 11 · 2026-05-13T17:40:10.874Z_

<details><summary>↩ Tool result · `toolu_01AhVsw4eA2yknL6ENngBywz`</summary>

```text
Web search results for query: "Token Cleaning ICML 2025 arXiv 2502.01968"

Links: [{"title":"[2502.01968] Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning","url":"https://arxiv.org/abs/2502.01968"},{"title":"arXiv:2502.01968v2 [cs.CL] 9 Jun 2025","url":"https://arxiv.org/pdf/2502.01968"},{"title":"Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning","url":"https://arxiv.org/html/2502.01968"},{"title":"GitHub - UCSC-REAL/TokenCleaning: [ICML 2025] Official implementation of paper \"Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning\"","url":"https://github.com/UCSC-REAL/TokenCleaning"},{"title":"ICML Poster Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning","url":"https://icml.cc/virtual/2025/poster/43777"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=1075&show=25"},{"title":"(PDF) Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning","url":"https://www.researchgate.net/publication/388686220_Token_Cleaning_Fine-Grained_Data_Selection_for_LLM_Supervised_Fine-Tuning"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Tokenization Workshop (TokShop)","url":"https://icml.cc/virtual/2025/workshop/39998"},{"title":"Token Reduction Should Go Beyond Efficiency in ...","url":"https://arxiv.org/pdf/2505.18227"}]

Based on the search results, here's information about the Token Cleaning paper:

## Overview

Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning is authored by Jinlong Pang and 6 other authors, and the paper was accepted at ICML 2025 as a Spotlight presentation.

## Main Contribution

Recent studies show that in supervised fine-tuning (SFT) of large language models (LLMs), data quality matters more than quantity. The paper addresses a specific problem: while most data cleaning methods concentrate on filtering entire samples, the quality of individual tokens within a sample can vary significantly.

## Methodology

The authors investigate token quality from a noisy-label perspective and propose a generic token cleaning pipeline for SFT tasks. Their method filters out uninformative tokens while preserving those carrying key task-specific information. Specifically, they first evaluate token quality by examining the influence of model updates on each token, then apply a threshold-based separation.

## Implementation

The paper proposes two cleaning approaches: Fixed-Model Cleaning applies a one-shot cleaning process to the entire dataset, while Self-Evolving Cleaning follows an iterative approach.

The official implementation is available on GitHub at the UCSC-REAL/TokenCleaning repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb4ff198-1e6a-4250-aead-4955ccea37f5",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "b994f754-a229-4884-b1b8-06dbcaacd856",
  "sourceToolAssistantUUID": "bb4ff198-1e6a-4250-aead-4955ccea37f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T17:40:11.258Z_

<details><summary>↩ Tool result · `toolu_01Qd3bNkUjsyPXeLWo8bdH14`</summary>

```text
Web search results for query: "SCIZOR self-supervised data curation imitation learning ICRA 2026"

Links: [{"title":"SCIZOR: Self-Supervised Data Curation for Large-Scale Imitation Learning","url":"https://ut-austin-rpl.github.io/SCIZOR/"},{"title":"[2505.22626] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/abs/2505.22626"},{"title":"Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/html/2505.22626v2"},{"title":"Huihan Liu on X: \"Our data curation work SCIZOR is accepted to ICRA 2026! Check out this self-supervised data curation approach that removes suboptimal and duplicated data for large-scale imitation learning, led by @YZ_Franklin @yuqi_xie5\" / X","url":"https://x.com/huihan_liu/status/2017698931493195899"},{"title":"SCIZOR: A Self-Supervised Approach to Data Curation for ...","url":"https://openreview.net/pdf?id=Wo8eEdFUDF"},{"title":"GitHub - UT-Austin-RPL/SCIZOR · GitHub","url":"https://github.com/UT-Austin-RPL/SCIZOR"},{"title":"Copyright by Yuqi Xie 2025 1","url":"https://repositories.lib.utexas.edu/bitstreams/d8256e22-405e-4881-87d8-ca3f8008345e/download"},{"title":"(PDF) SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.researchgate.net/publication/392167457_SCIZOR_A_Self-Supervised_Approach_to_Data_Curation_for_Large-Scale_Imitation_Learning"},{"title":"Publications – UT Austin Robot Perception and Learning Lab","url":"https://rpl.cs.utexas.edu/publications/"},{"title":"[Literature Review] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.themoonlight.io/en/review/scizor-a-self-supervised-approach-to-data-curation-for-large-scale-imitation-learning"}]

Based on the search results, here's comprehensive information about SCIZOR:

## Overview

SCIZOR is a self-supervised data curation framework that filters out low-quality state-action pairs to improve the performance of imitation learning policies. The paper was accepted to the 2026 IEEE International Conference on Robotics and Automation (ICRA).

## Key Problem

Large-scale datasets used for policy training often introduce substantial variability in quality, which can negatively impact performance. As a result, automatically curating datasets by filtering low-quality samples to improve quality becomes essential.

## Core Approach

SCIZOR targets two complementary sources of low-quality data: suboptimal data, which hinder learning with undesirable actions, and redundant data, which dilute training with repetitive patterns.

The framework uses two main components:
- A progress-prediction model flags and removes frames that fail to make meaningful task progress, without needing reward signals
- Joint visual-action embeddings are clustered to detect and discard look-alike segments, ensuring diversity

## Results

SCIZOR improves policy performance across diverse large-scale imitation learning benchmarks, showing on average 15.4% improvement.

## Authors and Citation

The paper is authored by Yu Zhang, Yuqi Xie, Huihan Liu, Rutav Shah, Michael Wan, Linxi Fan, and Yuke Zhu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ecac353-d22c-49dc-b6e3-fca051522502",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "098ae3bf-4ec0-4b8e-8abe-49309e0c4900",
  "sourceToolAssistantUUID": "0ecac353-d22c-49dc-b6e3-fca051522502",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T17:40:15.091Z_

<details><summary>↩ Tool result · `toolu_01Jw9NL62W3kzDqSSkvGHUNS`</summary>

```text
Web search results for query: "Freshness-Aware Prioritized Experience Replay LLM VLM arXiv 2604.16918"

Links: [{"title":"[2604.16918] Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning","url":"https://arxiv.org/abs/2604.16918"},{"title":"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning","url":"https://arxiv.org/html/2604.16918"},{"title":"Prioritized Experience Replay | Request PDF","url":"https://www.researchgate.net/publication/319770330_Prioritized_Experience_Replay"},{"title":"RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning","url":"https://arxiv.org/html/2507.07451v1"},{"title":"[PDF] Prioritized Experience Replay | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Prioritized-Experience-Replay-Schaul-Quan/c6170fa90d3b2efede5a2e1660cb23e1c824f2ca"},{"title":"(PDF) Prioritized Experience Replay","url":"https://www.researchgate.net/publication/284219262_Prioritized_Experience_Replay"},{"title":"SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning","url":"https://arxiv.org/html/2511.22367v1"},{"title":"[1511.05952] Prioritized Experience Replay","url":"https://arxiv.org/abs/1511.05952"},{"title":"Efficient RL Training for LLMs with Experience Replay","url":"https://arxiv.org/html/2604.08706"},{"title":"[1511.05952v4] Prioritized Experience Replay","url":"https://export.arxiv.org/abs/1511.05952v4"}]

I found the paper! Here's what I can tell you about arXiv paper 2604.16918:

**Title:** Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning

**Authors:** Weiyu Ma, Yongcheng Zeng, Yan Song, Xinyu Cui, Jian Zhao, Xuhui Liu, and Mohamed Elhoseiny from King Abdullah University of Science and Technology (KAUST), Chinese Academy of Sciences, University College London, and Zhongguancun Institute of Artificial Intelligence

**Main Problem:** Current on-policy RL methods for LLMs discard all collected trajectories after a single gradient update, resulting in poor sample efficiency, particularly wasteful for agentic tasks where multi-turn environment interactions are expensive. Additionally, the rapid policy evolution of billion-parameter models renders stored priorities stale, causing old high-priority trajectories to dominate sampling long after they have become uninformative.

**Solution:** Freshness-Aware PER addresses the priority staleness problem by augmenting any PER-based priority with a multiplicative exponential age decay grounded in effective sample size analysis.

**Results:** Freshness-Aware PER significantly outperforms on-policy baselines, achieving +46% on NQ Search, +367% on Sokoban, and +133% on VLM FrozenLake, while standard PER without age decay consistently degrades performance.

The paper was submitted on April 18, 2026, and code is publicly available at https://github.com/Vision-CAIR/Freshness-Aware-PER.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a1b0a72-29b7-46a0-919b-3cf032ed5464",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "804ebc18-736c-43e1-bf17-684c9896708e",
  "sourceToolAssistantUUID": "6a1b0a72-29b7-46a0-919b-3cf032ed5464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T17:40:17.337Z_

<details><summary>↩ Tool result · `toolu_01XhDJ4vEExb5bLY1f4n9MLb`</summary>

```text
Web search results for query: "iw-SFT importance weighted supervised fine tuning reinforcement learning arXiv 2507.12856"

Links: [{"title":"[2507.12856] Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://arxiv.org/abs/2507.12856"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://arxiv.org/html/2507.12856"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement ...","url":"https://arxiv.org/pdf/2507.12856"},{"title":"Paper page - Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://huggingface.co/papers/2507.12856"},{"title":"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification","url":"https://arxiv.org/html/2508.05629v1"},{"title":"Supervised Fine-Tuning versus Reinforcement Learning:","url":"https://arxiv.org/pdf/2603.13985"},{"title":"Harmonizing Supervised Fine-Tuning and Reinforcement ...","url":"https://arxiv.org/pdf/2508.11408"},{"title":"Anchored Supervised Fine-Tuning","url":"https://arxiv.org/html/2509.23753"},{"title":"[2506.19767] SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning","url":"https://arxiv.org/abs/2506.19767"},{"title":"(PDF) Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://www.researchgate.net/publication/393784242_Supervised_Fine_Tuning_on_Curated_Data_is_Reinforcement_Learning_and_can_be_improved"}]

Based on the search results, here's information about the paper with arXiv ID 2507.12856:

## Overview

Behavior Cloning (BC) on curated (or filtered) data is the predominant paradigm for supervised fine-tuning (SFT) of large language models; as well as for imitation learning of control policies. The paper explores the connection between this approach and reinforcement learning.

## Key Contribution

The paper clarifies that SFT can be understood as maximizing a lower bound on the RL objective in a sparse reward setting. A small modification to SFT leads to an importance weighted variant that behaves closer to training with RL as it: i) optimizes a tighter bound to the RL objective and, ii) can improve performance compared to SFT on curated data. This variant is referred to as importance weighted supervised fine-tuning (iw-SFT).

## Implementation and Results

The method is easy to implement and can be further generalized to training with quality scored data. The resulting SFT variants are competitive with more advanced RL algorithms for large language models and for training policies in continuous control tasks. For example, the method achieves 66.7% on the AIME 2024 dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e2bf305-3278-4eff-ab29-d454aa2ee7a2",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "16d0cefb-63a5-4653-bde0-b9288cb2c259",
  "sourceToolAssistantUUID": "0e2bf305-3278-4eff-ab29-d454aa2ee7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-13T17:40:19.940Z_

Good, first four searches are done. Now let me search for the remaining four.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16d0cefb-63a5-4653-bde0-b9288cb2c259",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazygXkn468gEGb4RbtY1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "445bc81c-0117-4d14-97f3-760e1be52538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNE8Kcg8LDdo2vzP4LsZki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1895,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 16 · 2026-05-13T17:40:20.909Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VFK2tFkxStMBuXMvhednuu`</summary>

```json
{
  "query": "CUPID curating data influence functions CoRL 2025 robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "445bc81c-0117-4d14-97f3-760e1be52538",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazygXkn468gEGb4RbtY1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68c384df-d8fd-4558-ad2b-83f25cedb845",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNE8Kcg8LDdo2vzP4LsZki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1895,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 17 · 2026-05-13T17:40:21.862Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T5FDMFH2Tup8W9D77G1Wrd`</summary>

```json
{
  "query": "DataMIL datamodels imitation learning ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68c384df-d8fd-4558-ad2b-83f25cedb845",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazygXkn468gEGb4RbtY1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c11edbd1-75f5-4f4a-91fb-56f62741f494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNE8Kcg8LDdo2vzP4LsZki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1895,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 18 · 2026-05-13T17:40:22.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015u9m4fe3XXKCsAgvVk58Uw`</summary>

```json
{
  "query": "adaptive sample weighting robot learning 2026 VLA policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c11edbd1-75f5-4f4a-91fb-56f62741f494",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazygXkn468gEGb4RbtY1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37622b37-a256-4ae7-8ed5-5cdf091a358e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNE8Kcg8LDdo2vzP4LsZki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1895,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 19 · 2026-05-13T17:40:23.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017iy1yyLPLbEv8dLM8ZNhsX`</summary>

```json
{
  "query": "prioritized replay supervised fine-tuning continuous action robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37622b37-a256-4ae7-8ed5-5cdf091a358e",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazygXkn468gEGb4RbtY1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6fec79f-516f-44bf-b224-b722220b6788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNE8Kcg8LDdo2vzP4LsZki",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1895,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 10511,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1895,
          "output_tokens": 234,
          "cache_read_input_tokens": 10511,
          "cache_creation_input_tokens": 1956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1956,
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

_source line 20 · 2026-05-13T17:40:27.607Z_

<details><summary>↩ Tool result · `toolu_01VFK2tFkxStMBuXMvhednuu`</summary>

```text
Web search results for query: "CUPID curating data influence functions CoRL 2025 robot learning"

Links: [{"title":"GitHub - agiachris/cupid: Official repository for \"CUPID: Curating Data your Robot Loves with Influence Functions,\" accepted to CoRL 2025. · GitHub","url":"https://github.com/agiachris/cupid"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions | OpenReview","url":"https://openreview.net/forum?id=TqevdDMqrK"},{"title":"[2506.19121] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"[2506.19121v2] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121v2"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://proceedings.mlr.press/v305/agia25a.html"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"[PDF] CUPID: Curating Data your Robot Loves with Influence Functions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CUPID:-Curating-Data-your-Robot-Loves-with-Agia-Sinha/666481cd9e72de8e90e3dd12fb826338f5ce17f0"},{"title":"CUPID: Robot Data Curation via Influence Functions","url":"https://www.emergentmind.com/papers/2506.19121"},{"title":"[Literature Review] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://www.themoonlight.io/en/review/cupid-curating-data-your-robot-loves-with-influence-functions"}]

Here's what I found about CUPID:

## Overview

CUPID ("Curating Data your Robot Loves with Influence Functions") was accepted to CoRL 2025. CUPID is a robot data curation method based on a novel influence function-theoretic formulation for imitation learning policies.

## Core Methodology

Given a set of evaluation rollouts, CUPID estimates the influence of a training demonstration on the policy's expected return, which enables ranking and selection of demonstrations according to their impact on the policy's closed-loop performance. 

CUPID uses influence functions to predictively answer counterfactual questions about the effect of each demonstration on downstream policy performance—for example, answering how a policy's expected return would change if certain demonstrations were upweighted or downweighted during training—without needing to retrain any policies.

## Applications

CUPID curates data by 1) filtering out training demonstrations that harmed the policy's performance and 2) subselecting newly collected trajectories that will most help improve the policy.

## Results

Training with less than 33% of curated data can yield state-of-the-art diffusion policies on the simulated RoboMimic benchmark, with similar gains observed in hardware. Hardware experiments show that the method can identify robust strategies under distribution shift, isolate spurious correlations, and even enhance the post-training of generalist robot policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68c384df-d8fd-4558-ad2b-83f25cedb845",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "60174fd6-e8a3-47cf-99a1-5fc8840e6fae",
  "sourceToolAssistantUUID": "68c384df-d8fd-4558-ad2b-83f25cedb845",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T17:40:28.721Z_

<details><summary>↩ Tool result · `toolu_01T5FDMFH2Tup8W9D77G1Wrd`</summary>

```text
Web search results for query: "DataMIL datamodels imitation learning ICLR 2026"

Links: [{"title":"[2505.09603] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/abs/2505.09603"},{"title":"DATAMIL: SELECTING DATA FOR ROBOT IMITATION ...","url":"https://openreview.net/pdf/82e6c304571ad1e85b44780f29e82e7042b2743f.pdf"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://robin-lab.cs.utexas.edu/datamodels4imitation/"},{"title":"GitHub - UT-Austin-RobIn/datamil: Code release for -- DataMIL: Selecting Data for Robot Imitation Learning with Datamodels · GitHub","url":"https://github.com/UT-Austin-RobIn/datamil"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels | OpenReview","url":"https://openreview.net/forum?id=AcTsKglDdh"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with ...","url":"https://arxiv.org/pdf/2505.09603"},{"title":"DataMIL : Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/html/2505.09603"},{"title":"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://openreview.net/pdf/d1836285b655f13b1f86918922a074b725fa137b.pdf"},{"title":"[Literature Review] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://www.themoonlight.io/en/review/datamil-selecting-data-for-robot-imitation-learning-with-datamodels"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

I found comprehensive information about DataMIL. Here's what the search results show:

## Overview

DataMIL is a policy-driven data selection framework built on the datamodels paradigm that reasons about data selection in an end-to-end manner, using the policy itself to identify which data points will most improve performance.

## Key Innovation

Unlike standard practices that filter data using human notions of quality (e.g., based on semantic or visual similarity), DataMIL directly optimizes data selection for task success, allowing us to select data that enhance the policy while dropping data that degrade it.

## Methodology

To avoid performing expensive rollouts in the environment during selection, DataMIL uses a novel surrogate loss function on task-specific data, allowing it to be used in the real world without degrading performance.

## Research Context

The paper is under review as a conference paper at ICLR 2026. The approach was validated on a suite of more than 60 simulation and real-world manipulation tasks - most notably showing successful data selection from the Open X-Embodiment datasets.

## Results

Across the 50 tasks in MetaWorld, DataMIL shows a 10% performance boost compared to state-of-the-art baselines.

The work addresses a practical problem in robotics: while large datasets improve generalist robot policies, they often don't perform well on specialized tasks, and DataMIL provides a principled way to select relevant data for improved performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c11edbd1-75f5-4f4a-91fb-56f62741f494",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "9ba62be8-112f-4642-978f-22a28fa465fb",
  "sourceToolAssistantUUID": "c11edbd1-75f5-4f4a-91fb-56f62741f494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T17:40:29.285Z_

<details><summary>↩ Tool result · `toolu_015u9m4fe3XXKCsAgvVk58Uw`</summary>

```text
Web search results for query: "adaptive sample weighting robot learning 2026 VLA policy"

Links: [{"title":"Robotic Policy Learning via Human-assisted Action Preference Optimization","url":"https://arxiv.org/html/2506.07127v1"},{"title":"Human-assisted Robotic Policy Refinement via Action Preference Optimization","url":"https://arxiv.org/html/2506.07127"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation","url":"https://www.mdpi.com/2073-8994/18/3/394"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://rlvla.github.io/"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/html/2505.19789v4"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"}]

Based on the search results, I found several relevant papers on adaptive sample weighting and VLA policy learning from 2026. Here are the key findings:

## Adaptive Sample Weighting for VLA Models

A prominent approach involves action preference optimization with adaptive reweighting for VLA models, which leverages decoded continuous actions to guide preference optimization and concentrates gradient optimization on failure-prone interaction actions through dynamic modulation of sample-wise training weighting.

The normalized weighting scheme operates by increasing the weight of samples with high action prediction errors for desirable data, and increasing the weight of samples whose actions are proximate to the failure actions for undesirable data.

This adaptive reweighting method leverages decoded continuous actions to effectively guide preference optimization in the discrete action token space, addressing the challenge of action token probability mismatch via dynamic modulation of sample-wise training weighting.

## Related VLA Policy Learning Methods

The search also revealed complementary approaches:

- VLA-RFT is a Reinforcement Fine-Tuning framework that leverages a data-driven world model as a controllable simulator, where the simulator predicts future visual observations conditioned on actions, allowing policy rollouts with dense, trajectory-level rewards.

- Proximal Policy Optimization (PPO) consistently improves performance for VLA models, with key design choices distilled into an effective fine-tuning recipe.

These methods represent significant advances in making VLA models more robust and sample-efficient through intelligent sample weighting and policy optimization strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37622b37-a256-4ae7-8ed5-5cdf091a358e",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "82541d41-5175-4d91-92ef-233a556c7585",
  "sourceToolAssistantUUID": "37622b37-a256-4ae7-8ed5-5cdf091a358e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-13T17:40:30.623Z_

<details><summary>↩ Tool result · `toolu_017iy1yyLPLbEv8dLM8ZNhsX`</summary>

```text
Web search results for query: "prioritized replay supervised fine-tuning continuous action robot 2025 2026"

Links: [{"title":"Online Fine-Tuning of Pretrained Controllers for Autonomous Driving via Real-Time Recurrent RL","url":"https://arxiv.org/html/2602.02236"},{"title":"Multi-objective trajectory optimization method for industrial robots based on improved TD3 algorithm | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-25949-7"},{"title":"Deep reinforcement learning for path planning of autonomous mobile robots in complicated environments | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-01906-9"},{"title":"𝜋_\"RL\": Online RL Fine-tuning for Flow-based Vision-Language-Action Models","url":"https://arxiv.org/html/2510.25889v1"},{"title":"Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications","url":"https://arxiv.org/html/2408.10215v1"},{"title":"Multi-step first: A lightweight deep reinforcement learning strategy for robust continuous control with partial observability - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0893608025014029"},{"title":"Harmonizing Supervised Fine-Tuning and Reinforcement ...","url":"https://arxiv.org/pdf/2508.11408"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning","url":"https://arxiv.org/html/2510.14830v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"}]

I've performed a web search for your query about prioritized replay, supervised fine-tuning, and continuous action robots in 2025-2026. Here are the relevant findings:

## Key Research Areas

**Prioritized Experience Replay in Robotics:**
A prioritized experience replay mechanism has been introduced to improve the utilization efficiency of critical experiences, thereby enhancing algorithm convergence speed and stability in robot trajectory optimization. Prioritized Experience Replay (PER) is being integrated into robot path planning algorithms to improve sample efficiency and accelerate convergence.

**Supervised Fine-Tuning for Robotic Control:**
Vision-Language-Action (VLA) models follow the standard pre-training and supervised fine-tuning (SFT) paradigm, where VLAs are fine-tuned on large-scale, heterogeneous human demonstration datasets, followed by SFT on the target task to align their capabilities with the specific embodiment and environment.

**Continuous Action Robots and Recent Advances:**
Recent research has been advancing RL fine-tuning approaches, with autoregressive VLAs featuring discrete action decoders, while diffusion- or flow-based VLAs generate actions through iterative refinement in flow matching, offering advantages of generating action chunks in high-frequency and performing highly dexterous tasks.

A paradigm shift in offline-to-online adaptation is represented by work from 2025 that introduces DSRL (Diffusion Steering with Reinforcement Learning) that operates RL entirely in the latent noise space of pretrained diffusion policies.

The research from 2025-2026 shows active development in combining supervised fine-tuning with reinforcement learning approaches for robotic control, particularly for continuous action spaces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6fec79f-516f-44bf-b224-b722220b6788",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "10dc6931-407b-4c5f-a8b9-732d6c815ee8",
  "sourceToolAssistantUUID": "e6fec79f-516f-44bf-b224-b722220b6788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-13T17:40:33.509Z_

Let me do a few more targeted searches to find additional competing/concurrent work and verify some details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10dc6931-407b-4c5f-a8b9-732d6c815ee8",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyhWZs9vx7RWqkCVesK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02d612d0-fac3-41c3-8721-4565af4eae7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkX1VLQt2tp2FYfwY8LG1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5761,
      "cache_read_input_tokens": 12467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5761,
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

_source line 25 · 2026-05-13T17:40:34.583Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019oUb39t3d2evfpZ83He4rv`</summary>

```json
{
  "query": "Token Cleaning ICML 2025 spotlight oral poster presentation type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02d612d0-fac3-41c3-8721-4565af4eae7b",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyhWZs9vx7RWqkCVesK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "feed86c8-2193-4267-bdc4-4e50d1914a48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkX1VLQt2tp2FYfwY8LG1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5761,
      "cache_read_input_tokens": 12467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5761,
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

_source line 26 · 2026-05-13T17:40:34.983Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0166RQpv89f3JDw2bTJUEPwQ`</summary>

```json
{
  "query": "sub-sample token-level loss decomposition robot imitation learning VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feed86c8-2193-4267-bdc4-4e50d1914a48",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyhWZs9vx7RWqkCVesK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6aa2e46-c213-448a-adf2-394f620c17bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkX1VLQt2tp2FYfwY8LG1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5761,
      "cache_read_input_tokens": 12467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5761,
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

_source line 27 · 2026-05-13T17:40:35.924Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VHckj8H4euvyQt81nuXrgP`</summary>

```json
{
  "query": "chunk-level loss weighting action chunking robot policy training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6aa2e46-c213-448a-adf2-394f620c17bb",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyhWZs9vx7RWqkCVesK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11b62606-5ebc-49a8-b094-b09378ff49ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkX1VLQt2tp2FYfwY8LG1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5761,
      "cache_read_input_tokens": 12467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5761,
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

_source line 28 · 2026-05-13T17:40:36.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013L7hhXbydk4U3uaJirvGnk`</summary>

```json
{
  "query": "iw-SFT arXiv 2507.12856 venue conference accepted NeurIPS ICML ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11b62606-5ebc-49a8-b094-b09378ff49ef",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyhWZs9vx7RWqkCVesK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e05a4c36-e125-4da6-be0b-e19705f8b1ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkX1VLQt2tp2FYfwY8LG1s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5761,
      "cache_read_input_tokens": 12467,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5761
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 12467,
          "cache_creation_input_tokens": 5761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5761,
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

_source line 29 · 2026-05-13T17:40:38.330Z_

<details><summary>↩ Tool result · `toolu_019oUb39t3d2evfpZ83He4rv`</summary>

```text
Web search results for query: "Token Cleaning ICML 2025 spotlight oral poster presentation type"

Links: [{"title":"ICML Poster Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning","url":"https://icml.cc/virtual/2025/poster/43777"},{"title":"ICML 2025 Poster Instructions","url":"https://icml.cc/Conferences/2025/PosterInstructions"},{"title":"ICML Poster Spotlights","url":"https://icml.cc/virtual/2024/39086"},{"title":"ICML 2025 Oral Presenter Instructions","url":"https://icml.cc/Conferences/2025/PresenterInstructions"},{"title":"ICML 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/icml-paper-list/icml-2025-paper-list/"},{"title":"ICML.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025"},{"title":"ICML Poster From Language Models over Tokens to Language Models over Characters","url":"https://icml.cc/virtual/2025/poster/43839"},{"title":"ICML 2025 Awards","url":"https://icml.cc/virtual/2025/awards_detail"},{"title":"ICML 2025 Position Paper Track | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2025%2FPosition_Paper_Track"},{"title":"ICML 2025 2025 Spotlight Posters","url":"https://icml.cc/virtual/2025/events/2025SpotlightPosters"}]

Based on the search results, the "Token Cleaning" paper at ICML 2025 investigates token quality from a noisy-label perspective and proposes a generic token cleaning pipeline for supervised fine-tuning tasks. 

The paper is presented as a **poster** at ICML 2025, not as a spotlight or oral presentation. The presentation type is a poster presentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feed86c8-2193-4267-bdc4-4e50d1914a48",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "13dbb7b2-7e6b-4798-855c-2e19bb1b9f79",
  "sourceToolAssistantUUID": "feed86c8-2193-4267-bdc4-4e50d1914a48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T17:40:41.904Z_

<details><summary>↩ Tool result · `toolu_0166RQpv89f3JDw2bTJUEPwQ`</summary>

```text
Web search results for query: "sub-sample token-level loss decomposition robot imitation learning VLA 2025 2026"

Links: [{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Moto: Latent Motion Token as the Bridging Language for ...","url":"https://www.openaccess.thecvf.com/content/ICCV2025/papers/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.pdf"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"}]

Based on the web search results, I found relevant information about Vision-Language-Action (VLA) models and robot imitation learning research from 2025-2026. Here's what the search revealed:

## Key Findings on VLA and Robot Imitation Learning:

Vision-Language-Action (VLA) models enable embodied decision-making but rely heavily on imitation learning, leading to compounding errors and poor robustness under distribution shift.

### Recent VLA Research Trends:

There were 164 Vision-Language-Action (VLA) model submissions at ICLR 2026, with trends in discrete diffusion VLAs, reasoning models, and benchmarks (LIBERO, CALVIN, SIMPLER).

### Token-Level and Action Tokenization Work:

The search results show active research on action tokenization methods. FAST (Efficient Action Tokenization for Vision-Language-Action Models) uses frequency-space (DCT) tokenization to compress action sequences 7x. Additionally, OmniSAT uses B-Splines for compact action representation through a two-stage encoding process and improves upon both FAST and BEAST across LIBERO and SIMPLER benchmarks.

### Commercial VLA Adoption:

By Q2 2025, three major robotics software companies had shipped VLA-based products to enterprise customers, and by Q1 2026, at least eleven commercial deployments are using VLA models as the primary policy backbone.

However, the search results don't contain specific papers focused explicitly on "sub-sample token-level loss decomposition" in VLA imitation learning. You may want to search for more specific terms or check recent arxiv submissions and conference papers from ICLR 2026 or ICRA 2026 for papers directly addressing this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6aa2e46-c213-448a-adf2-394f620c17bb",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "81afa80a-5785-413c-bf50-8b335b40b089",
  "sourceToolAssistantUUID": "f6aa2e46-c213-448a-adf2-394f620c17bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T17:40:42.491Z_

<details><summary>↩ Tool result · `toolu_013L7hhXbydk4U3uaJirvGnk`</summary>

```text
Web search results for query: "iw-SFT arXiv 2507.12856 venue conference accepted NeurIPS ICML ICLR"

Links: [{"title":"[2507.12856] Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://arxiv.org/abs/2507.12856"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement ...","url":"https://arxiv.org/pdf/2507.12856"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://arxiv.org/html/2507.12856"},{"title":"Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning","url":"https://www.arxiv.org/pdf/2602.01058"},{"title":"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification","url":"https://arxiv.org/html/2508.05629v1"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=1050&show=1000"},{"title":"arXiv:2507.02664v2 [cs.CV] 7 Jul 2025","url":"https://arxiv.org/pdf/2507.02664"},{"title":"From Reasoning to Super-Intelligence: A Search-Theoretic Perspective","url":"https://arxiv.org/html/2507.15865v2"},{"title":"SmallThinker: A Family of Efficient Large Language Models Natively Trained for Local Deployment","url":"https://arxiv.org/html/2507.20984v1"},{"title":"BusterX++: Towards Unified Cross-Modal AI-Generated Content Detection and Explanation with MLLM","url":"https://arxiv.org/html/2507.14632v3"}]

Based on the search results, I found information about the paper with arXiv ID 2507.12856:

## Paper Information

The paper is titled "Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)" with arXiv ID 2507.12856.

## Authors and Affiliation

The authors are Chongli Qin and Jost Tobias Springenberg from Independent Research in San Francisco, USA.

## Main Contribution

The paper introduces importance weighted supervised fine-tuning (iw-SFT), which is an importance weighted variant that behaves closer to training with RL as it optimizes a tighter bound to the RL objective and can improve performance compared to SFT on curated data.

## Conference Status

Regarding venue information: Based on the search results, the paper is marked as "Preprint. Under review." as of the version information available. The search results do not indicate acceptance to NeurIPS, ICML, ICLR, or any other specific conference venue at this time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e05a4c36-e125-4da6-be0b-e19705f8b1ff",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "1b2cef40-6cac-4305-a27c-d985bb58852c",
  "sourceToolAssistantUUID": "e05a4c36-e125-4da6-be0b-e19705f8b1ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T17:40:44.397Z_

<details><summary>↩ Tool result · `toolu_01VHckj8H4euvyQt81nuXrgP`</summary>

```text
Web search results for query: "chunk-level loss weighting action chunking robot policy training 2025 2026"

Links: [{"title":"ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/act-policy-explained"},{"title":"Action chunking with Transformers (ACT) robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/action-chunking-with-transformers-act-robot-policy-80519fc024bc"},{"title":"Real time action chunking for robot policies | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/real-time-action-chunking-for-robot-policies-4636cc085a6a"},{"title":"Adaptive Action Chunking for Robotic Imitation Learning","url":"https://www.mdpi.com/2313-7673/11/5/316"},{"title":"Published as a conference paper at ICLR 2026 CHUNKING THE CRITIC:","url":"https://openreview.net/pdf?id=rb5eTktqbc"},{"title":"Action chunking as conditional policy compression - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0010027725001416"},{"title":"ICML Sample-Efficient Reinforcement Learning with Action Chunking","url":"https://icml.cc/virtual/2025/51519"},{"title":"[2507.07969] Reinforcement Learning with Action Chunking","url":"https://arxiv.org/abs/2507.07969"},{"title":"Reinforcement Learning with Action Chunking | OpenReview","url":"https://openreview.net/forum?id=XUks1Y96NR"},{"title":"Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling | OpenReview","url":"https://openreview.net/forum?id=qZmn2hkuzw"}]

I found relevant research on chunk-level loss weighting and action chunking in robot policy training from 2025-2026. Here are the key findings:

## Action Chunking Overview

Action Chunking with Transformers (ACT) is an imitation learning algorithm designed for fine-grained manipulation tasks where the robot takes a sequence of images and current joint state as input and outputs a chunk of future actions—a short sequence of joint position targets—rather than a single next action.

## Weighting Schemes in Temporal Ensembling

For overlapping action chunks that predict values for the same timestep, predictions are averaged with exponentially decaying weights, where the ensembling weight schedule uses an exponential decay formula: w(t) = exp(-t / temperature). The original ACT paper uses temperature = 10 (at 50 Hz), meaning predictions from the current chunk are weighted ~1.0 while predictions from a chunk generated 20 steps ago are weighted ~0.14.

## Recent Advances (2025-2026)

An Adaptive Action Chunking framework published in May 2026 enables robots to dynamically predict the optimal action chunk length based on real-time visual context using an end-to-end dual-branch network comprising a shared visual encoder, a parallel action prediction head, and a chunk-size prediction head.

The model is trained end-to-end by minimizing a weighted sum of the action prediction error and the chunk-size classification error, thereby learning when to adopt which planning horizon.

Additionally, Q-chunking is a recipe for improving reinforcement learning algorithms for long-horizon, sparse-reward tasks designed for the offline-to-online RL setting to maximize the sample-efficiency of online learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11b62606-5ebc-49a8-b094-b09378ff49ef",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "a2f6351c-0e16-4198-beb9-22276bb370e8",
  "sourceToolAssistantUUID": "11b62606-5ebc-49a8-b094-b09378ff49ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T17:40:47.018Z_

Let me do a couple more targeted searches to check the Token Cleaning spotlight claim more carefully and look for any additional missing related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2f6351c-0e16-4198-beb9-22276bb370e8",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyiXTUNU7rmT6pna2EP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71d8d953-5107-4a0a-a059-7cc4305415fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tzn9jfDqs2C1TPm4yb7Ao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 777,
      "cache_creation_input_tokens": 2918,
      "cache_read_input_tokens": 18228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2918,
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

_source line 34 · 2026-05-13T17:40:47.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MQJtEggB8RpUnfaCkLTAVY`</summary>

```json
{
  "query": "ICML 2025 spotlight list Token Cleaning 43777"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71d8d953-5107-4a0a-a059-7cc4305415fa",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyiXTUNU7rmT6pna2EP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d789223-4906-4b71-8194-d29ca74ef284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tzn9jfDqs2C1TPm4yb7Ao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 777,
      "cache_creation_input_tokens": 2918,
      "cache_read_input_tokens": 18228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2918,
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

_source line 35 · 2026-05-13T17:40:48.438Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T8knq7vJtTYe6mWiXLEebs`</summary>

```json
{
  "query": "\"Freshness-Aware Prioritized Experience Replay\" venue conference 2026 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d789223-4906-4b71-8194-d29ca74ef284",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyiXTUNU7rmT6pna2EP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9736747-8405-406f-b483-173e666d0a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tzn9jfDqs2C1TPm4yb7Ao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 777,
      "cache_creation_input_tokens": 2918,
      "cache_read_input_tokens": 18228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2918,
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

_source line 36 · 2026-05-13T17:40:49.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0111SzgfHhi7KRzXKS9P33d3`</summary>

```json
{
  "query": "per-token loss weighting SFT fine-tuning data quality 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9736747-8405-406f-b483-173e666d0a28",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyiXTUNU7rmT6pna2EP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a48b855-e130-4b2b-8d31-0895de2c76a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tzn9jfDqs2C1TPm4yb7Ao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 777,
      "cache_creation_input_tokens": 2918,
      "cache_read_input_tokens": 18228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2918,
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

_source line 37 · 2026-05-13T17:40:49.707Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015fivZa3HuFZCDNE3k92oga`</summary>

```json
{
  "query": "DataMIL ICLR 2026 accepted spotlight oral poster"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a48b855-e130-4b2b-8d31-0895de2c76a4",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyiXTUNU7rmT6pna2EP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31d98512-202c-479b-9325-bec58c14b613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tzn9jfDqs2C1TPm4yb7Ao",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 777,
      "cache_creation_input_tokens": 2918,
      "cache_read_input_tokens": 18228,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2918
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 777,
          "output_tokens": 258,
          "cache_read_input_tokens": 18228,
          "cache_creation_input_tokens": 2918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2918,
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

_source line 38 · 2026-05-13T17:40:51.801Z_

<details><summary>↩ Tool result · `toolu_01MQJtEggB8RpUnfaCkLTAVY`</summary>

```text
Web search results for query: "ICML 2025 spotlight list Token Cleaning 43777"

Links: [{"title":"ICML Poster Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning","url":"https://icml.cc/virtual/2025/poster/43777"},{"title":"Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning","url":"https://icml.cc/media/icml-2025/Slides/43777.pdf"},{"title":"ICML.2025 - Spotlight | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025?group=Spotlight"},{"title":"ICML 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/icml-paper-list/icml-2025-paper-list/"},{"title":"ICML 2025 2025 Spotlight Posters","url":"https://icml.cc/virtual/2025/events/2025SpotlightPosters"},{"title":"ICML Spotlight Paper Presentations","url":"https://icml.cc/virtual/2024/39269"},{"title":"Erfan Shayegani's Post","url":"https://www.linkedin.com/posts/erfan-shayegani_icml-spotlight-vlms-activity-7323783710875488257-shvu"},{"title":"International Conference on Machine Learning (ICML) 2025 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/updates/apple-at-icml-2025"},{"title":"9 must-see posters at ICML 2025 – MIT Jameel Clinic","url":"https://jclinic.mit.edu/must-see-posters-icml-2025/"},{"title":"ICML 2025 - ASSET Center","url":"https://asset.seas.upenn.edu/icml-2025/"}]

Based on the search results, I found information about paper 43777 at ICML 2025:

"Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning" is a paper that investigates token quality from a noisy-label perspective and proposes a generic token cleaning pipeline for SFT tasks, filtering out uninformative tokens while preserving those carrying key task-specific information.

The paper appears to be presented as a poster at ICML 2025 (based on the URL structure showing it as a poster presentation). You can access the full poster page at https://icml.cc/virtual/2025/poster/43777 and the slides are available at https://icml.cc/media/icml-2025/Slides/43777.pdf.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d789223-4906-4b71-8194-d29ca74ef284",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "e295317e-c048-4554-9155-0b9e9d1f1c4e",
  "sourceToolAssistantUUID": "0d789223-4906-4b71-8194-d29ca74ef284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T17:40:52.926Z_

<details><summary>↩ Tool result · `toolu_01T8knq7vJtTYe6mWiXLEebs`</summary>

```text
Web search results for query: ""Freshness-Aware Prioritized Experience Replay" venue conference 2026 accepted"

Links: [{"title":"[1511.05952] Prioritized Experience Replay","url":"https://arxiv.org/abs/1511.05952"},{"title":"Uncertainty Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=aAxzDb0nlO"},{"title":"Prioritized Experience Replay | Request PDF","url":"https://www.researchgate.net/publication/319770330_Prioritized_Experience_Replay"},{"title":"Replay 2026 | Durable Execution conference for building ...","url":"https://replay.temporal.io/"},{"title":"[PDF] Prioritized Experience Replay | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Prioritized-Experience-Replay-Schaul-Quan/c6170fa90d3b2efede5a2e1660cb23e1c824f2ca"},{"title":"Prioritized Experience Replay | BibSonomy","url":"https://www.bibsonomy.org/bibtex/db6e4402b0807938aae61afc45b70f73"},{"title":"Prioritized Experience Replay","url":"https://arxiv.org/pdf/1511.05952"},{"title":"Reliability-Adjusted Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=hmQk2Iwdh0"},{"title":"(PDF) Prioritized Experience Replay","url":"https://www.researchgate.net/publication/284219262_Prioritized_Experience_Replay"},{"title":"DISTRIBUTED PRIORITIZED EXPERIENCE REPLAY","url":"https://openreview.net/pdf?id=H1Dy---0Z"}]

Based on the search results, I found information about "Freshness-Aware Prioritized Experience Replay." Freshness-Aware PER addresses the priority staleness problem by augmenting any PER-based priority with a multiplicative exponential age decay grounded in effective sample size analysis, and is the first work to successfully apply PER to LLM/VLM reinforcement learning.

However, the search results do not contain specific information about which conference venue accepted this paper in 2026 or details about its acceptance status. The ResearchGate source mentions the work but does not specify the conference. To find the specific venue and acceptance details, you would need to search academic conference proceedings directly or check platforms like OpenReview, arXiv, or the conference websites themselves.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9736747-8405-406f-b483-173e666d0a28",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "e3f5cf94-05e4-4dd9-a3da-2bf4c38302a9",
  "sourceToolAssistantUUID": "f9736747-8405-406f-b483-173e666d0a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T17:40:54.591Z_

<details><summary>↩ Tool result · `toolu_015fivZa3HuFZCDNE3k92oga`</summary>

```text
Web search results for query: "DataMIL ICLR 2026 accepted spotlight oral poster"

Links: [{"title":"ICLR 2026 Accepted Papers: Oral Papers, Research Trends & Top Highlights","url":"https://www.bohrium.com/en/blog/research-notes/iclr-2026-accepted-papers-highlights/"},{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"},{"title":"ICLR.2026 - Oral | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026?group=Oral"},{"title":"ICLR 2026 on X: \"Congratulations to all authors of accepted #ICLR2021 papers! 🎉 Notifications are being sent out today. We had 2997 submissions, of which 860 papers have been accepted. Of these, there will be 53 Oral, 114 Spotlight and 693 Poster presentations.\" / X","url":"https://x.com/iclr_conf/status/1349062310992740353?lang=en"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"Paper Digest: ICLR 2026 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2026/02/iclr-2026-papers-highlights/"},{"title":"SPOT @ ICLR 2026 - Workshop on Scaling Post-training for LLMs","url":"https://spoticlr.github.io/"},{"title":"2026 Poster Instructions","url":"https://iclr.cc/Conferences/2026/PosterInstructions"},{"title":"ICML 2025 Poster Instructions","url":"https://icml.cc/Conferences/2025/PosterInstructions"}]

Based on the search results, I found information about DataMIL and ICLR 2026:

DataMIL tackles the practical problem of selecting the right training data from heterogeneous robot datasets, and it appears in the context of robotics research at ICLR 2026.

However, the search results don't contain specific details about whether DataMIL was accepted as an oral, spotlight, or poster presentation at ICLR 2026. The results mention that ICLR 2026 accepted 225 papers as Oral presentations, and provide general information about the different presentation categories, but don't specify the exact presentation type for the DataMIL paper.

For more detailed information about DataMIL's specific presentation format at ICLR 2026, you might want to check the official ICLR 2026 conference website or the OpenReview portal directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31d98512-202c-479b-9325-bec58c14b613",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "dad4d7f9-5fb0-459e-a017-90f262528337",
  "sourceToolAssistantUUID": "31d98512-202c-479b-9325-bec58c14b613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-13T17:40:57.233Z_

<details><summary>↩ Tool result · `toolu_0111SzgfHhi7KRzXKS9P33d3`</summary>

```text
Web search results for query: "per-token loss weighting SFT fine-tuning data quality 2025 2026 arXiv"

Links: [{"title":"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority","url":"https://www.arxiv.org/pdf/2602.01227"},{"title":"Entropy-Adaptive Fine-Tuning: Resolving Confident Conflicts to Mitigate Forgetting","url":"https://arxiv.org/html/2601.02151v1"},{"title":"[2509.16596] Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels","url":"https://arxiv.org/abs/2509.16596"},{"title":"Harmonizing Supervised Fine-Tuning and Reinforcement ...","url":"https://arxiv.org/pdf/2508.11408"},{"title":"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification","url":"https://arxiv.org/html/2508.05629v1"},{"title":"Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels","url":"https://arxiv.org/html/2509.16596"},{"title":"Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning","url":"https://arxiv.org/html/2502.01968"},{"title":"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority","url":"https://arxiv.org/html/2602.01227"},{"title":"[2502.01968] Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning","url":"https://arxiv.org/abs/2502.01968"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://arxiv.org/html/2507.12856"}]

Based on the web search results, I found several recent arXiv papers (from 2025-2026) that discuss per-token loss weighting, SFT fine-tuning, and data quality. Here are the key findings:

## Recent Research on Token-Level Loss Weighting in SFT

**Token Priority and Loss Weighting:**
Recent work shows that techniques like S2FT and SFTKey focus on updating only a fraction of parameters or key tokens. Standard SFT allocates gradient updates proportional to token frequency, but priority-based training redistributes gradient capacity from "redundant" to "informative" regions by assigning priority weights inversely proportional to a token's triviality.

**Data Quality and Token-Level Analysis:**
Recent studies show that in supervised fine-tuning of LLMs, data quality matters more than quantity. While most data cleaning methods concentrate on filtering entire samples, the quality of individual tokens within a sample can vary significantly. Research investigates token quality from a noisy-label perspective and proposes token cleaning pipelines that filter out uninformative tokens while preserving those carrying key task-specific information by examining the influence of model updates on each token.

**Dynamic Loss Reweighting Methods:**
Recent methods include DFT (Dynamic Fine-Tuning), which re-weights the SFT loss according to prediction probability. Entropy-Adaptive Fine-Tuning (EAFT) employs a soft gating mechanism that dynamically modulates the training loss based on token-level entropy.

**Importance Weighting Approach:**
Research shows that SFT can be improved by importance re-weighting of the maximum likelihood objective, with an importance weighted variant (iw-SFT) that optimizes a tighter bound to the RL objective and can improve performance compared to standard SFT on curated data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a48b855-e130-4b2b-8d31-0895de2c76a4",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "2ef2a879-07b9-4de7-8aca-3d4a29a745a3",
  "sourceToolAssistantUUID": "2a48b855-e130-4b2b-8d31-0895de2c76a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-13T17:41:00.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KzYC5pGEM8XyQEPMA8EBa3`</summary>

```json
{
  "query": "arXiv 2602.01227 \"token priority\" SFT fine-tuning venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ef2a879-07b9-4de7-8aca-3d4a29a745a3",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyjUPhnADeTPWVvTPQp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83c32d71-69af-46d3-898d-a3c5e96b9b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mja51c7sL4QCH1WwTDneyJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 795,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 21146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3350,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
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

_source line 43 · 2026-05-13T17:41:01.200Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TT6kAkM2wqsgSiTxjoRhB9`</summary>

```json
{
  "query": "Token Cleaning ICML 2025 spotlight poster papers.cool",
  "allowed_domains": [
    "papers.cool"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83c32d71-69af-46d3-898d-a3c5e96b9b11",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyjUPhnADeTPWVvTPQp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f159301-38f3-455c-858c-39ceff501164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mja51c7sL4QCH1WwTDneyJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 795,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 21146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3350,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
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

_source line 44 · 2026-05-13T17:41:02.056Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KTt1wpS4fk3smqoVPPz58n`</summary>

```json
{
  "query": "Freshness-Aware PER arXiv 2604.16918 ICML 2026 NeurIPS 2026 submitted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f159301-38f3-455c-858c-39ceff501164",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazyjUPhnADeTPWVvTPQp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25d5b0c5-bbbc-4719-acc3-f222a123d2d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mja51c7sL4QCH1WwTDneyJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 795,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 21146,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3350
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 795,
          "output_tokens": 213,
          "cache_read_input_tokens": 21146,
          "cache_creation_input_tokens": 3350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3350,
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

_source line 45 · 2026-05-13T17:41:06.426Z_

<details><summary>↩ Tool result · `toolu_01TT6kAkM2wqsgSiTxjoRhB9`</summary>

```text
Web search results for query: "Token Cleaning ICML 2025 spotlight poster papers.cool"

Links: [{"title":"ICML.2025 - Spotlight | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025?group=Spotlight"},{"title":"ICLR.2025 - Spotlight | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2025?group=Spotlight"},{"title":"ICML.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025"},{"title":"ICML.2025 - Poster | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025?group=Poster"},{"title":"ICLR.2025 - Poster | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2025?group=Poster"},{"title":"ICML.2025 - Oral | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025?group=Oral"},{"title":"ICML.2024 - Spotlight | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2024?group=Spotlight"},{"title":"ICLR.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2025"},{"title":"ICLR.2025 - Oral | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2025?group=Oral"},{"title":"Published as a conference paper at ICLR 2025","url":"https://papers.cool/pdf?url=https%3A%2F%2Fopenreview.net%2Fpdf%3Fid%3DzqzsZ5cXbB"}]

I found the search results from papers.cool for ICML 2025. However, I did not find a paper specifically titled "Token Cleaning" in the spotlight or poster sections. 

The search results show the ICML.2025 Spotlight papers on papers.cool, including papers like "Masked Autoencoders Are Effective Tokenizers for Diffusion Models" and various other spotlight presentations. The ICML.2025 Poster papers are also listed.

If you're looking for a specific paper about "Token Cleaning" at ICML 2025, it may be listed under a different title, or it might be in a different track (such as the general conference papers rather than spotlight or poster presentations). Would you like me to search more broadly for "Token Cleaning ICML 2025" or help you locate a specific paper with more details?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f159301-38f3-455c-858c-39ceff501164",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "daebb52c-5b85-46c2-8d08-4dd39ab8eb43",
  "sourceToolAssistantUUID": "4f159301-38f3-455c-858c-39ceff501164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-13T17:41:06.656Z_

<details><summary>↩ Tool result · `toolu_01KzYC5pGEM8XyQEPMA8EBa3`</summary>

```text
Web search results for query: "arXiv 2602.01227 "token priority" SFT fine-tuning venue"

Links: [{"title":"[2602.01227] Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority","url":"https://arxiv.org/abs/2602.01227"},{"title":"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority","url":"https://arxiv.org/html/2602.01227"},{"title":"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority","url":"https://www.arxiv.org/pdf/2602.01227"},{"title":"SED-SFT: Selectively Encouraging Diversity in Supervised Fine-Tuning","url":"https://arxiv.org/html/2602.07464"},{"title":"[2602.11424v1] Gradients Must Earn Their Influence: Unifying SFT with Generalized Entropic Objectives","url":"https://arxiv.org/abs/2602.11424v1"},{"title":"SFT-GO: Supervised Fine-Tuning with Group Optimization for Large Language Models","url":"https://arxiv.org/html/2506.15021v1"},{"title":"Memory-Efficient Fine-Tuning of Transformers via Token Selection","url":"https://arxiv.org/html/2501.18824v1"},{"title":"Proximal Supervised Fine-Tuning","url":"https://arxiv.org/html/2508.17784v1"},{"title":"[2602.11424] Gradients Must Earn Their Influence: Unifying SFT with Generalized Entropic Objectives","url":"https://arxiv.org/abs/2602.11424"},{"title":"Enhancing Large Language Model Reasoning via Selective Critical Token Fine-Tuning","url":"https://arxiv.org/html/2510.10974v1"}]

Based on the search results, I found information about arXiv paper 2602.01227 on "Token Priority" and SFT fine-tuning. However, I should note that the search results do not explicitly indicate a specific conference or publication venue for this paper.

The paper is arXiv:2602.01227, submitted on February 1, 2026 and last revised on February 9, 2026. 

The paper is titled "Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority" and is authored by Zhanming Shen and 9 other authors.

The paper advocates Token Priority as an essential bridge, formalizing Supervised Fine-Tuning (SFT) not as simple optimization but as a precise distribution reshaping process that aligns raw data with the ideal alignment manifold. The authors analyze recent breakthroughs through a unified lens, categorizing them into two distinct regimes: Positive Priority for noise filtration and Signed Priority for toxic modes unlearning.

The search results indicate this is a recent position paper on arXiv, but do not specify if it has been submitted to or accepted at a particular conference or journal venue beyond its arXiv posting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83c32d71-69af-46d3-898d-a3c5e96b9b11",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "b1127f54-bb26-44b5-a2ff-c30ce13b7074",
  "sourceToolAssistantUUID": "83c32d71-69af-46d3-898d-a3c5e96b9b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-13T17:41:09.074Z_

<details><summary>↩ Tool result · `toolu_01KTt1wpS4fk3smqoVPPz58n`</summary>

```text
Web search results for query: "Freshness-Aware PER arXiv 2604.16918 ICML 2026 NeurIPS 2026 submitted"

Links: [{"title":"[2604.16918] Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning","url":"https://arxiv.org/abs/2604.16918"},{"title":"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning","url":"https://arxiv.org/html/2604.16918"},{"title":"ICML 2026 Papers","url":"https://icml.cc/virtual/2026/papers.html"},{"title":"1 Introduction","url":"https://arxiv.org/html/2604.24357"},{"title":"ICML 2026","url":"https://icml.cc/"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=202&show=2000"},{"title":"Stop Automating Peer Review Without Rigorous Evaluation","url":"https://arxiv.org/html/2605.03202v1"},{"title":"Intern-Atlas: A Methodological Evolution Graph as Research Infrastructure for AI Scientists","url":"https://arxiv.org/html/2604.28158"},{"title":"Multi-Objective Bayesian Optimization via Adaptive 𝜀-Constraints Decomposition","url":"https://arxiv.org/html/2604.15959"}]

Based on the search results, I found information about the paper you're looking for:

The paper titled "Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning" (arXiv:2604.16918) was submitted on April 18, 2026. 

The paper addresses how on-policy RL algorithms like PPO, GRPO, and REINFORCE++ discard all collected trajectories after a single gradient update, resulting in poor sample efficiency. While Experience Replay improves sample efficiency by allowing agents to reuse past trajectories, directly applying Prioritized Experience Replay (PER) to LLMs fails.

The rapid policy evolution of billion-parameter models renders stored priorities stale, causing old high-priority trajectories to dominate sampling long after they have become less relevant.

The authors are Weiyu Ma, Yongcheng Zeng, Yan Song, Xinyu Cui, Jian Zhao, Xuhui Liu, and Mohamed Elhoseiny from King Abdullah University of Science and Technology (KAUST), Chinese Academy of Sciences, University College London, and Zhongguanchan Institute of Artificial Intelligence.

Regarding submission to ICML 2026 or NeurIPS 2026, the search results show the paper was posted to arXiv, but I couldn't find specific information confirming whether it was submitted to those conferences or their acceptance status.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25d5b0c5-bbbc-4719-acc3-f222a123d2d0",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "827cf90b-fe66-46fb-83fb-27f2d23835bb",
  "sourceToolAssistantUUID": "25d5b0c5-bbbc-4719-acc3-f222a123d2d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-13T17:41:13.320Z_

Let me check whether Token Cleaning is indeed a spotlight and check the GitHub repo claim, and also look for the "Self-Improving VLA" paper that appeared in one of my earlier searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "827cf90b-fe66-46fb-83fb-27f2d23835bb",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazykLyF6scSCrGThaSxV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "616826ef-2a3a-4a49-b75d-9f2cfb24beed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJPBpZ7TrbFYygW6JjAV8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3315,
      "cache_read_input_tokens": 24496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3315,
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

_source line 49 · 2026-05-13T17:41:13.839Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Szy3HiaDMfgbBjUtGiJg6F`</summary>

```json
{
  "query": "site:github.com UCSC-REAL TokenCleaning \"ICML 2025 Spotlight\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "616826ef-2a3a-4a49-b75d-9f2cfb24beed",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazykLyF6scSCrGThaSxV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5c53a04-bd5c-4e6c-8233-9c561ff28fb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJPBpZ7TrbFYygW6JjAV8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3315,
      "cache_read_input_tokens": 24496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3315,
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

_source line 50 · 2026-05-13T17:41:14.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UzZJ2zYmsfhUYBD8FMXm14`</summary>

```json
{
  "query": "\"Self-Improving Vision-Language-Action\" PLD per-token loss data quality robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5c53a04-bd5c-4e6c-8233-9c561ff28fb1",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazykLyF6scSCrGThaSxV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c4b38be-2a34-42b9-8ee3-b64f8de1c8d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJPBpZ7TrbFYygW6JjAV8A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3315,
      "cache_read_input_tokens": 24496,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3315
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 24496,
          "cache_creation_input_tokens": 3315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3315,
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

_source line 51 · 2026-05-13T17:41:18.173Z_

<details><summary>↩ Tool result · `toolu_01Szy3HiaDMfgbBjUtGiJg6F`</summary>

```text
Web search results for query: "site:github.com UCSC-REAL TokenCleaning "ICML 2025 Spotlight""

Links: [{"title":"GitHub - mingyin1/Agents_Failure_Attribution: 🏆 ICML 2025 Spotlight","url":"https://github.com/mingyin1/Agents_Failure_Attribution"},{"title":"GitHub - NVlabs/DDO: [ICML 2025 Spotlight] Direct Discriminative Optimization: Supercharging Diffusion/Autoregressive with GAN-type Discrimination","url":"https://github.com/nvlabs/ddo"},{"title":"GitHub - ag2ai/Agents_Failure_Attribution: Benchmark for automated failure attributions in agentic systems (🏆 ICML 2025 Spotlight)","url":"https://github.com/ag2ai/Agents_Failure_Attribution"},{"title":"GitHub - chen2hang/GraNT_NonparametricTeaching: [ICML 2025 Spotlight] &lt;Nonparametric Teaching for Graph Property Learners>","url":"https://github.com/chen2hang/GraNT_NonparametricTeaching"},{"title":"GitHub - real-absolute-AI/RAPID: [ICML 2025 Spotlight] RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding · GitHub","url":"https://github.com/real-absolute-AI/RAPID"},{"title":"GitHub - TsingZ0/PCEvolve: ICML 2025 Spotlight, PCEvolve: Private Contrastive Evolution for Synthetic Dataset Generation via Few-Shot Private Data and Generative APIs","url":"https://github.com/TsingZ0/PCEvolve"},{"title":"GitHub - yannqi/RCTS-RAG: [ICML 2025 Spotlight] Official implementation of the paper: Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger","url":"https://github.com/yannqi/RCTS-RAG"},{"title":"GitHub - sambowyer/no_clt_paper: Code for the ICML 2025 spotlight paper \"Position: Don’t use the CLT in LLM evals with fewer than a few hundred datapoints\"","url":"https://github.com/sambowyer/no_clt_paper"},{"title":"GitHub - drumpt/TIMING: Official PyTorch implementation of TIMING: Temporality-Aware Integrated Gradients for Time Series Explanation (ICML 2025 Spotlight)","url":"https://github.com/drumpt/TIMING"},{"title":"GitHub - wzhuang-xmu/ATP: [ICML 2025 Spotlight] Official implementation of paper \"Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective\".","url":"https://github.com/wzhuang-xmu/ATP"}]

The search didn't find a result specifically matching "UCSC-REAL TokenCleaning" with "ICML 2025 Spotlight" on GitHub. The results returned are other ICML 2025 Spotlight papers from different GitHub repositories, but none match the specific query you requested.

The search results show various ICML 2025 Spotlight papers hosted on GitHub (such as papers on automated failure attribution, diffusion optimization, graph property learning, and other topics), but the particular repository you're looking for with "UCSC-REAL" organization and "TokenCleaning" project name doesn't appear in these results.

You might want to try:
- Searching directly on GitHub for "UCSC-REAL TokenCleaning"
- Checking if the repository might be under a different name or organization
- Visiting the ICML 2025 conference website for a complete list of spotlight papers


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5c53a04-bd5c-4e6c-8233-9c561ff28fb1",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "71b094fe-c827-426f-8dfa-d84415e0cc25",
  "sourceToolAssistantUUID": "d5c53a04-bd5c-4e6c-8233-9c561ff28fb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-13T17:41:22.535Z_

<details><summary>↩ Tool result · `toolu_01UzZJ2zYmsfhUYBD8FMXm14`</summary>

```text
Web search results for query: ""Self-Improving Vision-Language-Action" PLD per-token loss data quality robot 2026"

Links: [{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://arxiv.org/html/2511.00091v1"},{"title":"PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)","url":"https://wenlixiao.com/self-improve-VLA-PLD"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=shqo2VPfc7"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"GitHub - starVLA/starVLA: StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing · GitHub","url":"https://github.com/starVLA/starVLA"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"}]

I found relevant research on your search query. Here's what the results show:

## PLD: Self-Improving Vision-Language-Action Models

Probe, Learn, Distill (PLD) is a three-stage plug-and-play framework that improves VLAs through residual reinforcement learning (RL) and distribution-aware data collection. The paper was accepted at ICLR 2026.

### Framework Overview

The framework includes three stages: In Stage 1, they freeze the VLA backbone and train lightweight residual actors via off-policy RL that take over in states where the base policy fails. In Stage 2, they employ a hybrid rollout scheme that biases residual interventions toward states frequently visited by the base policy. In Stage 3, the curated trajectories are distilled back into the generalist with standard supervised fine-tuning.

### Data Quality and Performance

PLD data yields the highest in-distribution performance while retaining the cross-task generalization property of high-quality human data. PLD achieves a near-saturated 99% task success rate on the LIBERO benchmark, delivers over 50% performance gains in SimplerEnv, and demonstrates a 100% success rate on real-world Franka arm and YAM arm dexterous manipulation tasks.

### Key Findings

Residual policy probing and distribution-aware replay are key to collecting deployment-aligned data that improves VLAs' capabilities on both seen and unseen tasks. RL-generated, policy-aligned data can surpass teleoperation-only demonstrations, offering a scalable path toward self-improving VLA models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c4b38be-2a34-42b9-8ee3-b64f8de1c8d4",
  "isSidechain": true,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "agentId": "aa8e627ca68bfa3d5",
  "type": "user",
  "uuid": "1eabae2a-a9dc-49e0-9dde-bd8deec58cb9",
  "sourceToolAssistantUUID": "0c4b38be-2a34-42b9-8ee3-b64f8de1c8d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-13T17:42:30.635Z_

Now I have a thorough picture. Let me compile the full report.

Here is my comprehensive verification report for each paper, plus additional related work findings:

---

## 1. Token Cleaning (arXiv:2502.01968)

**Exists:** Yes. "Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning" by Jinlong Pang et al., UC Santa Cruz.

**Venue:** ICML 2025, but the claim that it is a **Spotlight** appears to be **incorrect or unverifiable**. The ICML virtual site lists it under `icml.cc/virtual/2025/poster/43777` -- i.e., as a **Poster**, not a Spotlight. The GitHub repo (`UCSC-REAL/TokenCleaning`) labels it as `[ICML 2025]` without the Spotlight tag, and it does not appear in ICML 2025 spotlight lists on papers.cool. You should double-check, but available evidence points to **Poster**, not Spotlight.

**What it does:** Investigates token quality from a noisy-label perspective. Proposes a pipeline that scores individual token quality by examining the influence of model updates on each token, then applies threshold-based separation to filter uninformative tokens. Two modes: Fixed-Model Cleaning (one-shot) and Self-Evolving Cleaning (iterative). This is directly relevant to your paper as it decomposes loss at the sub-sample (token) level for SFT.

---

## 2. iw-SFT (arXiv:2507.12856)

**Exists:** Yes. "Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)" by Chongli Qin and Jost Tobias Springenberg.

**Venue:** As of my search, the paper is marked as **"Preprint. Under review."** No confirmed venue acceptance found. It has **not** been confirmed at any major conference (NeurIPS, ICML, ICLR) based on available evidence.

**What it does:** Shows SFT on curated data can be understood as maximizing a lower bound on the RL objective in a sparse reward setting. Proposes importance weighted SFT (iw-SFT), which re-weights the MLE objective to optimize a tighter bound. Generalizes to quality-scored data. Results competitive with advanced RL algorithms both for LLMs (66.7% on AIME 2024) and continuous control tasks. Highly relevant -- it provides per-sample importance weighting for SFT.

---

## 3. Freshness-Aware PER (arXiv:2604.16918)

**Exists:** Yes. "Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning" by Weiyu Ma et al. (KAUST, CAS, UCL).

**Venue:** Posted to arXiv on April 18, 2026. **No confirmed venue** -- appears to be a preprint, likely under review. Could not find acceptance at ICML 2026, NeurIPS 2026, or elsewhere.

**What it does:** Addresses the failure of standard PER when applied to LLM/VLM RL. The core problem is priority staleness: rapid policy evolution of billion-parameter models makes stored priorities stale. Solution: augments PER priority with multiplicative exponential age decay grounded in effective sample size analysis. Achieves +46% on NQ Search, +367% on Sokoban, +133% on VLM FrozenLake vs. on-policy baselines. Directly relevant as it adapts prioritized replay to large model training, though for RL not SFT.

---

## 4. SCIZOR (arXiv:2505.22626)

**Exists:** Yes. "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning" by Yu Zhang, Yuqi Xie, Huihan Liu, Rutav Shah, Michael Wan, Linxi Fan, Yuke Zhu (UT Austin RPL).

**Venue:** **ICRA 2026 -- confirmed.** Author Huihan Liu posted confirmation on X (Twitter), and the paper appears on OpenReview for ICRA 2026.

**What it does:** Targets two sources of low-quality data: suboptimal data (wrong actions) and redundant data (repetitive patterns). Uses a progress-prediction model to flag frames that fail to make task progress (no reward signals needed), plus joint visual-action embeddings clustered to detect and discard look-alike segments. Averages 15.4% improvement across large-scale imitation learning benchmarks. Relevant as a sample-level curation method (not sub-sample/token-level).

---

## 5. CUPID (arXiv:2506.19121)

**Exists:** Yes. "CUPID: Curating Data your Robot Loves with Influence Functions" by Christopher Agia et al.

**Venue:** **CoRL 2025 -- confirmed.** Published in Proceedings of Machine Learning Research (PMLR), Vol. 305 (`proceedings.mlr.press/v305/agia25a.html`). Also on OpenReview.

**What it does:** Uses influence functions to estimate how each training demonstration affects the policy's expected return, enabling ranking/selection of demonstrations by their impact on closed-loop performance. Can filter harmful demonstrations and subselect helpful new trajectories. Training with <33% of curated data achieves SOTA on RoboMimic. Works at the demonstration (sample) level, not sub-sample level.

---

## 6. DataMIL (arXiv:2505.09603)

**Exists:** Yes. "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels" (UT Austin RobIn Lab).

**Venue:** **ICLR 2026 -- confirmed** (appears on OpenReview as ICLR 2026 conference paper). Specific presentation tier (oral/spotlight/poster) could not be confirmed from search results, but it is accepted.

**What it does:** Policy-driven data selection framework using the datamodels paradigm. Instead of filtering based on human notions of quality, it directly optimizes data selection for task success using a novel surrogate loss on task-specific data. Validated on 60+ simulation and real-world manipulation tasks including Open X-Embodiment datasets. Shows ~10% performance boost on MetaWorld 50 tasks. Operates at sample level.

---

## 7-8. Additional/Competing/Concurrent Work Found

### PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)
- **arXiv:2511.00091** -- "Probe, Learn, Distill" framework
- Accepted at **ICLR 2026**
- Three-stage framework: (1) freeze VLA, train residual actors via off-policy RL; (2) distribution-aware data collection biasing interventions toward states the base policy visits; (3) distill curated trajectories back via SFT
- Achieves 99% on LIBERO, 50%+ gains on SimplerEnv
- Relevant because it uses distribution-aware replay and data quality filtering before SFT distillation

### "Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority" (arXiv:2602.01227)
- Posted February 2026, no confirmed venue
- Formalizes SFT as distribution reshaping via token-level priority
- Categorizes approaches into Positive Priority (noise filtration) and Signed Priority (toxic mode unlearning)
- Directly relevant as a framework paper analyzing per-token loss weighting for SFT

### "Gradients Must Earn Their Influence: Unifying SFT with Generalized Entropic Objectives" (arXiv:2602.11424)
- February 2026 preprint
- Proposes generalized entropic objectives for SFT that modulate gradient influence
- Related to per-token importance weighting

### Entropy-Adaptive Fine-Tuning (EAFT) (arXiv:2601.02151)
- January 2026 preprint
- Uses soft gating mechanism that dynamically modulates training loss based on token-level entropy
- Directly relevant as a token-level dynamic loss reweighting method

### Action Preference Optimization with Adaptive Reweighting for VLA (arXiv:2506.07127)
- Adaptive sample-wise weighting for VLA preference optimization
- Increases weight of samples with high action prediction errors for desirable data
- Relevant as it does sample-level adaptive weighting specifically for VLA models with continuous actions

### Q-Chunking / Chunking the Critic (ICLR 2026)
- Published as ICLR 2026 conference paper
- Recipe for improving RL with action chunking in long-horizon sparse-reward tasks
- Relevant if your chunk-decomposed loss relates to action chunking

---

## Summary: Key Findings and Gaps

**Verification results:**
| Paper | Exists? | Claimed Venue | Actual Venue |
|-------|---------|---------------|--------------|
| Token Cleaning | Yes | ICML 2025 Spotlight | ICML 2025 **Poster** (Spotlight unverified) |
| iw-SFT | Yes | (not specified) | **Preprint, under review** |
| Freshness-Aware PER | Yes | (not specified) | **Preprint** (April 2026) |
| SCIZOR | Yes | ICRA 2026 | **ICRA 2026 -- confirmed** |
| CUPID | Yes | CoRL 2025 | **CoRL 2025 -- confirmed** |
| DataMIL | Yes | ICLR 2026 | **ICLR 2026 -- confirmed** |

**Potentially missing related work for sub-sample level loss decomposition in robot learning:**
1. **Token Priority paper** (arXiv:2602.01227) -- formalizes per-token priority weighting for SFT
2. **EAFT** (arXiv:2601.02151) -- token-level entropy-based dynamic loss modulation
3. **PLD** (ICLR 2026) -- distribution-aware replay + SFT distillation for VLA self-improvement
4. **Action Preference Optimization** (arXiv:2506.07127) -- adaptive sample-wise reweighting for VLA with continuous actions

The existing landscape shows: CUPID, SCIZOR, and DataMIL operate at the **sample/demonstration level**; Token Cleaning and the Token Priority paper operate at the **token level for LLM SFT**; but there appears to be a gap in work that specifically decomposes losses at a **chunk level** (sub-sample but not individual token) for **VLA/robot policy SFT with continuous actions** -- which is the niche your paper idea targets.

Sources:
- [Token Cleaning (arXiv:2502.01968)](https://arxiv.org/abs/2502.01968)
- [Token Cleaning ICML Poster Page](https://icml.cc/virtual/2025/poster/43777)
- [Token Cleaning GitHub](https://github.com/UCSC-REAL/TokenCleaning)
- [iw-SFT (arXiv:2507.12856)](https://arxiv.org/abs/2507.12856)
- [Freshness-Aware PER (arXiv:2604.16918)](https://arxiv.org/abs/2604.16918)
- [SCIZOR (arXiv:2505.22626)](https://arxiv.org/abs/2505.22626)
- [SCIZOR ICRA 2026 confirmation](https://x.com/huihan_liu/status/2017698931493195899)
- [CUPID (arXiv:2506.19121)](https://arxiv.org/abs/2506.19121)
- [CUPID CoRL 2025 proceedings](https://proceedings.mlr.press/v305/agia25a.html)
- [DataMIL (arXiv:2505.09603)](https://arxiv.org/abs/2505.09603)
- [DataMIL OpenReview](https://openreview.net/forum?id=AcTsKglDdh)
- [PLD: Self-Improving VLA (ICLR 2026)](https://wenlixiao.com/self-improve-VLA-PLD)
- [Token Priority (arXiv:2602.01227)](https://arxiv.org/abs/2602.01227)
- [EAFT (arXiv:2601.02151)](https://arxiv.org/html/2601.02151v1)
- [Action Preference Optimization (arXiv:2506.07127)](https://arxiv.org/html/2506.07127v1)
- [ICML 2025 Spotlight List (papers.cool)](https://papers.cool/venue/ICML.2025?group=Spotlight)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eabae2a-a9dc-49e0-9dde-bd8deec58cb9",
  "isSidechain": true,
  "agentId": "aa8e627ca68bfa3d5",
  "requestId": "req_011CazymLYizxYEoBVMQFReP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5038e87a-1fc4-4553-b620-949865f64d27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzCj5gfWNFq5NEF8bKfyyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 27811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2053,
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
