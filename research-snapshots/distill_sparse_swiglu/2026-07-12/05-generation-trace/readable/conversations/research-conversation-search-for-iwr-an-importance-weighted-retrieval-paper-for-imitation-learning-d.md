# Research conversation: Search for "IWR" - an importance-weighted retrieval paper for imitation learning data selection, reportedly at CoRL 2025

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae8490a92fcb2dd4d.jsonl`
- **Structured JSON:** [`50dd812117dfeed2b872.json`](../../sessions/50/50dd812117dfeed2b872.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-13T11:41:03.011Z_

Search for "IWR" - an importance-weighted retrieval paper for imitation learning data selection, reportedly at CoRL 2025. I need to:

1. Use WebSearch with queries like "IWR importance weighted retrieval imitation learning CoRL 2025", "importance weighted retrieval robot learning data selection", "importance weighted retrieval demonstration selection"
2. Use WebFetch to read the abstract and key details
3. Report: full title, authors, venue, what it does (importance-weighted data selection using density ratios for IL?), and how it relates to the question of filtering vs. weighting demonstrations.

Also try searching "importance weighted data selection robot imitation learning 2025".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ae8490a92fcb2dd4d",
  "type": "user",
  "uuid": "7ef28c9a-bb8a-477d-86ce-9e99af54d634",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T11:41:03.015Z_

```json
{
  "parentUuid": "7ef28c9a-bb8a-477d-86ce-9e99af54d634",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
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
  "uuid": "7954103e-9eee-4091-a470-8b6adeeb46d2",
  "timestamp": "2026-05-13T11:41:03.015Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T11:41:05.245Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then search for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7954103e-9eee-4091-a470-8b6adeeb46d2",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWHfogYHJgKZRPQzkWE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54220e89-d5f1-45ff-8bd7-428af8869e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwcRcAzWkzCcGivQMTRBTR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 695,
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

_source line 4 · 2026-05-13T11:41:05.878Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FQMVZTKxqxGAYinywA3dX4`</summary>

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
  "parentUuid": "54220e89-d5f1-45ff-8bd7-428af8869e7e",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWHfogYHJgKZRPQzkWE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3a476de-b932-435b-8af8-bbdcff96c9fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwcRcAzWkzCcGivQMTRBTR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 8223,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 695
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 695,
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

_source line 5 · 2026-05-13T11:41:05.880Z_

<details><summary>↩ Tool result · `toolu_01FQMVZTKxqxGAYinywA3dX4`</summary>

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
  "parentUuid": "f3a476de-b932-435b-8af8-bbdcff96c9fd",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ae8490a92fcb2dd4d",
  "type": "user",
  "uuid": "dd286e17-3496-41e4-9e76-8f5ca0218358",
  "sourceToolAssistantUUID": "f3a476de-b932-435b-8af8-bbdcff96c9fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T11:41:08.960Z_



Now let me run multiple searches in parallel to find the IWR paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd286e17-3496-41e4-9e76-8f5ca0218358",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWHtTSCHRjAvKYw7DHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ca75ba1-6b77-4f54-82f5-0441752e3988",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DrxvQVduLnygKU4DVjqjfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 7 · 2026-05-13T11:41:09.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jm9e9GcXtRtVncn97skErE`</summary>

```json
{
  "query": "IWR importance weighted retrieval imitation learning CoRL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ca75ba1-6b77-4f54-82f5-0441752e3988",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWHtTSCHRjAvKYw7DHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65f3a6a6-31fa-4839-9c37-35f4146ae868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DrxvQVduLnygKU4DVjqjfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 8 · 2026-05-13T11:41:09.897Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FhizmJ41jRCjRErvEjbEg5`</summary>

```json
{
  "query": "importance weighted retrieval robot learning data selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65f3a6a6-31fa-4839-9c37-35f4146ae868",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWHtTSCHRjAvKYw7DHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfd3d0d9-f78b-468c-a463-01bb2e440332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DrxvQVduLnygKU4DVjqjfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 9 · 2026-05-13T11:41:10.312Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017M9y6tbvpixvKRSZPBEsRN`</summary>

```json
{
  "query": "importance weighted data selection robot imitation learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfd3d0d9-f78b-468c-a463-01bb2e440332",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWHtTSCHRjAvKYw7DHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cba88037-d3c9-4776-ac7f-dd47d472b19c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DrxvQVduLnygKU4DVjqjfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 10 · 2026-05-13T11:41:10.483Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017nY6m5JTftoHX9wdka1Yvc`</summary>

```json
{
  "query": "\"importance weighted retrieval\" demonstration selection density ratio"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cba88037-d3c9-4776-ac7f-dd47d472b19c",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWHtTSCHRjAvKYw7DHv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "823659eb-12c2-4175-861b-48b581bd8d22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DrxvQVduLnygKU4DVjqjfk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8918,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1911
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 215,
          "cache_read_input_tokens": 8918,
          "cache_creation_input_tokens": 1911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1911,
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

_source line 11 · 2026-05-13T11:41:18.112Z_

<details><summary>↩ Tool result · `toolu_017M9y6tbvpixvKRSZPBEsRN`</summary>

```text
Web search results for query: "importance weighted data selection robot imitation learning 2025"

Links: [{"title":"[2509.01657] Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/abs/2509.01657"},{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=wnWYoetLhC"},{"title":"DataMIL : Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/html/2505.09603"},{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://proceedings.mlr.press/v305/xie25a.html"},{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/html/2509.01657"},{"title":"[2505.09603] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/abs/2505.09603"},{"title":"Discriminator-weighted offline imitation learning with unlabeled demonstrations for robotic tasks: Journal of the Chinese Institute of Engineers: Vol 48 , No 6 - Get Access","url":"https://www.tandfonline.com/doi/full/10.1080/02533839.2025.2517354"},{"title":"[PDF] Data Retrieval with Importance Weights for Few-Shot Imitation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Retrieval-with-Importance-Weights-for-Few-Shot-Xie-Chand/9f803de0143a310eefaefa6f8a9ce3435f483599"},{"title":"Robot learning on the job: Human-in-the-loop autonomy and learning during deployment - Huihan Liu, Soroush Nasiriany, Lance Zhang, Zhiyao Bao, Yuke Zhu, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649241273901"},{"title":"IntervenGen: Interventional Data Generation for Robust and Data-Efficient Robot Imitation Learning","url":"https://arxiv.org/html/2405.01472v1"}]

Based on the search results, I found several highly relevant 2025 papers on importance-weighted data selection for robot imitation learning:

## Key Research on Importance-Weighted Data Selection in Robot Imitation Learning (2025)

### 1. **Importance Weighted Retrieval (IWR) for Few-Shot Imitation Learning**

A 2025 paper introduces Importance Weighted Retrieval (IWR), which estimates importance weights—the ratio between target and prior data distributions for retrieval—using Gaussian KDEs. This approach is used for retrieval-based imitation learning, which extracts relevant samples from large, widely available prior datasets to augment a limited demonstration dataset.

By considering the probability ratio, IWR seeks to mitigate the bias of previous selection rules, and by using reasonable modeling parameters, IWR effectively smooths estimates using all data points. Across both simulation environments and real-world evaluations on the Bridge dataset, the method consistently improves performance of existing retrieval-based methods, despite only requiring minor modifications.

### 2. **DataMIL: Policy-Driven Data Selection**

DataMIL is a policy-driven data selection framework built on the datamodels paradigm that reasons about data selection in an end-to-end manner, using the policy itself to identify which data points will most improve performance. The approach was validated on more than 60 simulation and real-world manipulation tasks, demonstrating consistent gains in success rates and superior performance over multiple baselines.

These represent important advances in intelligent data curation for robot imitation learning in 2025, addressing the critical challenge of effectively selecting training data from large diverse datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cba88037-d3c9-4776-ac7f-dd47d472b19c",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ae8490a92fcb2dd4d",
  "type": "user",
  "uuid": "8a201844-79ff-46bb-b299-d59d4031b7ef",
  "sourceToolAssistantUUID": "cba88037-d3c9-4776-ac7f-dd47d472b19c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T11:41:18.177Z_

<details><summary>↩ Tool result · `toolu_01FhizmJ41jRCjRErvEjbEg5`</summary>

```text
Web search results for query: "importance weighted retrieval robot learning data selection"

Links: [{"title":"[2509.01657] Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/abs/2509.01657"},{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=wnWYoetLhC"},{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/html/2509.01657v1"},{"title":"Importance Weighted Retrieval (IWR)","url":"https://www.emergentmind.com/topics/importance-weighted-retrieval-iwr"},{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://proceedings.mlr.press/v305/xie25a.html"},{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://rahulschand.github.io/iwr/"},{"title":"Importance Weighted Retrieval for Few-shot Imitation Learning Amber Xie","url":"https://rss25-roboreps.github.io/papers/30_Importance_Weighted_Retriev.pdf"},{"title":"[PDF] Data Retrieval with Importance Weights for Few-Shot Imitation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Retrieval-with-Importance-Weights-for-Few-Shot-Xie-Chand/9f803de0143a310eefaefa6f8a9ce3435f483599"},{"title":"Task-agnostic Lifelong Robot Learning with Retrieval-based Weighted Local Adaptation","url":"https://arxiv.org/html/2410.02995"},{"title":"Collage: Adaptive Fusion-based Retrieval for Augmented Policy Learning","url":"https://arxiv.org/html/2508.01131"}]

I've completed the web search for "importance weighted retrieval robot learning data selection." Here's a summary of the key findings:

## Overview

Importance Weighted Retrieval (IWR) is a method that estimates importance weights, or the ratio between the target and prior data distributions for retrieval, using Gaussian KDEs.

## Context and Problem

Retrieval-based imitation learning extracts relevant samples from large, widely available prior datasets to augment a limited demonstration dataset in robot learning. Traditional retrieval-based approaches commonly calculate a prior data point's minimum distance to a point in the target dataset in latent space, and while retrieval-based methods have shown success using this metric for data selection, it is equivalent to the limit of a Gaussian kernel density estimate of the target data distribution.

## Key Shortcomings Addressed

Prior retrieval methods rely on high-variance nearest neighbor estimates that are susceptible to noise, and they do not account for the distribution of prior data when retrieving data.

## Solution and Benefits

By considering the probability ratio, IWR seeks to mitigate the bias of previous selection rules, and by using reasonable modeling parameters, IWR effectively smooths estimates using all data points. Across both simulation environments and real-world evaluations on the Bridge dataset, IWR consistently improves performance of existing retrieval-based methods, despite only requiring minor modifications.

## Real-World Performance

On the Bridge dataset, which contains long-horizon manipulation trials, IWR substantially improves policy success rates (sometimes by up to 30%) over basic retrieval strategies, particularly on more complex or extended tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfd3d0d9-f78b-468c-a463-01bb2e440332",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ae8490a92fcb2dd4d",
  "type": "user",
  "uuid": "66c5405d-daf7-44c3-a015-ad20e2e38ada",
  "sourceToolAssistantUUID": "dfd3d0d9-f78b-468c-a463-01bb2e440332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T11:41:18.326Z_

<details><summary>↩ Tool result · `toolu_01Jm9e9GcXtRtVncn97skErE`</summary>

```text
Web search results for query: "IWR importance weighted retrieval imitation learning CoRL 2025"

Links: [{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://rahulschand.github.io/iwr/"},{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/html/2509.01657"},{"title":"[2509.01657] Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/abs/2509.01657"},{"title":"[PDF] Data Retrieval with Importance Weights for Few-Shot Imitation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Retrieval-with-Importance-Weights-for-Few-Shot-Xie-Chand/9f803de0143a310eefaefa6f8a9ce3435f483599"},{"title":"Importance Weighted Retrieval (IWR)","url":"https://www.emergentmind.com/topics/importance-weighted-retrieval-iwr"},{"title":"Importance Weighted Retrieval for Few-shot Imitation Learning Amber Xie","url":"https://rss25-roboreps.github.io/papers/30_Importance_Weighted_Retriev.pdf"},{"title":"Towards Understanding Learning from Human Interventions | OpenReview","url":"https://openreview.net/forum?id=uEtTUMEipU"},{"title":"IWR","url":"https://sites.google.com/stanford.edu/iwr"},{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"Collage: Adaptive Fusion-based Retrieval for Augmented Policy Learning","url":"https://arxiv.org/html/2508.01131v1"}]

Based on the search results, here's what I found about IWR (Importance Weighted Retrieval) for imitation learning at CoRL 2025:

## Overview

Importance Weighted Retrieval (IWR) estimates importance weights, or the ratio between the target and prior data distributions for retrieval, using Gaussian KDEs.

## Problem It Solves

Retrieval-based imitation learning extracts relevant samples from large, widely available prior datasets to augment a limited demonstration dataset. However, previous retrieval methods rely on high-variance nearest neighbor estimates that are susceptible to noise, and do not account for the distribution of prior data when retrieving data.

## Key Approach

IWR addresses these limitations by upweighting samples containing underrepresented objects or occurring later in the demonstrations. IWR applies Gaussian kernel density estimation (KDE) to estimate importance weights, and using Gaussian KDEs produces smoother estimates by considering all data points within a dataset instead of just the nearest-neighbor.

## Results

Across both simulation environments and real-world evaluations on the Bridge dataset, IWR consistently improves performance of existing retrieval-based methods, despite only requiring minor modifications.

## Authors and Conference

The work is authored by Amber Xie, Rahul Chand, Dorsa Sadigh, and Joey Hejna, and was presented at the 9th Annual Conference on Robot Learning in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65f3a6a6-31fa-4839-9c37-35f4146ae868",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ae8490a92fcb2dd4d",
  "type": "user",
  "uuid": "578980db-f762-46c3-afd5-ee9f7863a55e",
  "sourceToolAssistantUUID": "65f3a6a6-31fa-4839-9c37-35f4146ae868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T11:41:20.531Z_

<details><summary>↩ Tool result · `toolu_017nY6m5JTftoHX9wdka1Yvc`</summary>

```text
Web search results for query: ""importance weighted retrieval" demonstration selection density ratio"

Links: [{"title":"Importance Weighted Retrieval (IWR)","url":"https://www.emergentmind.com/topics/importance-weighted-retrieval-iwr"},{"title":"[2509.01657] Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/abs/2509.01657"},{"title":"Importance Weighted Retrieval for Few-shot Imitation Learning Amber Xie","url":"https://rss25-roboreps.github.io/papers/30_Importance_Weighted_Retriev.pdf"},{"title":"Density Ratio Estimation: A Comprehensive Review | Request PDF","url":"https://www.researchgate.net/publication/215705221_Density_Ratio_Estimation_A_Comprehensive_Review"},{"title":"Density-Ratio Weighted Behavioral Cloning: Learning Control Policies from Corrupted Datasets","url":"https://arxiv.org/html/2510.01479v1"},{"title":"A Short Survey on Importance Weighting for Machine Learning","url":"https://arxiv.org/html/2403.10175v2"},{"title":"Density-Ratio Weighted Behavioral Cloning:","url":"https://arxiv.org/pdf/2510.01479"},{"title":"Density Ratio Estimation in Machine Learning | Request PDF","url":"https://www.researchgate.net/publication/215705204_Density_Ratio_Estimation_in_Machine_Learning"},{"title":"Importance sampling - Wikipedia","url":"https://en.wikipedia.org/wiki/Importance_sampling"},{"title":"Density Ratio Estimation in Machine Learning: | Guide books | ACM Digital Library","url":"https://dl.acm.org/doi/book/10.5555/2181148"}]

Based on the web search results, I can provide you with comprehensive information about Importance Weighted Retrieval (IWR) and its connection to demonstration selection and density ratio:

## Overview of Importance Weighted Retrieval

Importance Weighted Retrieval is a technique that uses probabilistic reweighting by estimating likelihood ratios to select relevant data samples from a larger base dataset. It employs Gaussian Kernel Density Estimation over latent representations (often from VAEs) to compute importance weights, reducing high variance and distributional bias seen in nearest-neighbor methods.

## Demonstration Selection and Density Ratio

Retrieval-based imitation learning extracts relevant samples from large, widely available prior datasets to augment a limited demonstration dataset. To determine the relevant data from prior datasets, retrieval-based approaches most commonly calculate a prior data point's minimum distance to a point in the target dataset in latent space.

However, while retrieval-based methods have shown success using this metric for data selection, they demonstrate its equivalence to the limit of a Gaussian kernel density (KDE) estimate of the target data distribution. The method does not account for the distribution of prior data when retrieving data.

## Core Innovation of IWR

IWR estimates importance weights, or the ratio between the target and prior data distributions for retrieval, using Gaussian KDEs. IWR addresses this by normalizing by the prior density, thereby accounting for where prior data is underrepresented (and up-weighting accordingly).

## Practical Benefits

In LIBERO, IWR produces better phase coverage in multi-step tasks (e.g., success on "Mug-Pudding") by selecting samples relevant to critical stages of the demonstration. On the Bridge dataset, which contains long-horizon manipulation trials, IWR substantially improves policy success rates (sometimes by up to 30%) over basic retrieval strategies, particularly on more complex or extended tasks.

By normalizing for the density of prior data, IWR is less susceptible to over-selecting overrepresented (e.g., initial-phase) prior samples, resulting in more balanced and effective training sets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "823659eb-12c2-4175-861b-48b581bd8d22",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ae8490a92fcb2dd4d",
  "type": "user",
  "uuid": "02632be4-2f77-47fa-bdea-922d8076a841",
  "sourceToolAssistantUUID": "823659eb-12c2-4175-861b-48b581bd8d22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-13T11:41:24.473Z_

Excellent, I've found the paper clearly. Now let me fetch the arxiv abstract page and the project page for more precise details (authors, venue confirmation, etc.).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02632be4-2f77-47fa-bdea-922d8076a841",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWJxmB5GowWXAsGSjru",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d35c16b-d0ff-4bce-b9a6-bcd35a82ac4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPKWMG4TBSVavHu63CcTjJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 10829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 16 · 2026-05-13T11:41:25.350Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0131WLvbNRUchn1cn5fwE5aF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.01657",
  "prompt": "Extract the full title, complete list of authors with affiliations, the abstract in full, and any venue/conference information mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d35c16b-d0ff-4bce-b9a6-bcd35a82ac4b",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWJxmB5GowWXAsGSjru",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcf43be3-0b3f-4470-9a38-94519abb820c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPKWMG4TBSVavHu63CcTjJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 10829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 17 · 2026-05-13T11:41:26.766Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QAkygqQNBrWkffjwah55CA`</summary>

```json
{
  "url": "https://proceedings.mlr.press/v305/xie25a.html",
  "prompt": "Extract the full title, complete author list, abstract, venue/proceedings details, and any other metadata about this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcf43be3-0b3f-4470-9a38-94519abb820c",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWJxmB5GowWXAsGSjru",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a257e6c-fec6-4ae2-90ef-a4a0b8082dad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPKWMG4TBSVavHu63CcTjJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 10829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 18 · 2026-05-13T11:41:28.196Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KxW71qYrYyLqrfsz78XQbS`</summary>

```json
{
  "url": "https://rahulschand.github.io/iwr/",
  "prompt": "Extract the full paper title, authors, abstract, key method details, and any information about the venue or conference. Include details about how the importance weighting works, the density ratio approach, and how it relates to filtering vs weighting demonstrations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a257e6c-fec6-4ae2-90ef-a4a0b8082dad",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWJxmB5GowWXAsGSjru",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1872bac5-03ce-41aa-9724-707e4b34bf99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPKWMG4TBSVavHu63CcTjJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 10829,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 348,
          "cache_read_input_tokens": 10829,
          "cache_creation_input_tokens": 3979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3979,
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

_source line 19 · 2026-05-13T11:41:29.616Z_

<details><summary>↩ Tool result · `toolu_0131WLvbNRUchn1cn5fwE5aF`</summary>

```text
# Paper Summary

**Full Title:**
"Data Retrieval with Importance Weights for Few-Shot Imitation Learning"

**Authors:**
- Amber Xie
- Rahul Chand
- Dorsa Sadigh
- Joey Hejna

(Affiliations are not specified in the provided content)

**Abstract:**
The paper addresses few-shot imitation learning through retrieval-based methods. The authors demonstrate that existing retrieval approaches using minimum distance in latent space are equivalent to a limiting case of Gaussian kernel density estimation. They identify two limitations: high-variance nearest neighbor estimates and failure to account for prior data distribution. To remedy these issues, they propose Importance Weighted Retrieval (IWR), which "estimates importance weights, or the ratio between the target and prior data distributions for retrieval, using Gaussian KDEs." The method seeks to reduce bias and smooth estimates across data points, showing consistent performance improvements across simulation and real-world evaluations on the Bridge dataset.

**Venue/Conference:**
Conference on Robot Learning 2025

**Submission Details:**
Submitted September 1, 2025 (arXiv:2509.01657)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcf43be3-0b3f-4470-9a38-94519abb820c",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ae8490a92fcb2dd4d",
  "type": "user",
  "uuid": "a7cbe95f-a4ea-473c-993d-3f07df4d5491",
  "sourceToolAssistantUUID": "fcf43be3-0b3f-4470-9a38-94519abb820c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T11:41:30.170Z_

<details><summary>↩ Tool result · `toolu_01QAkygqQNBrWkffjwah55CA`</summary>

```text
# Paper Metadata Extract

**Title:** Data Retrieval with Importance Weights for Few-Shot Imitation Learning

**Authors:** Amber Xie, Rahul Chand, Dorsa Sadigh, Joey Hejna

**Venue:** The 9th Conference on Robot Learning (CoRL 2025)

**Publication Details:**
- Proceedings of Machine Learning Research, Volume 305
- Pages: 1-16
- Date: September 27-30, 2025
- Editors: Joseph Lim, Shuran Song, Hae-Won Park

**Abstract Summary:**
The paper addresses few-shot imitation learning by improving data retrieval from large prior datasets. The authors identify limitations in existing retrieval-based methods, noting they "rely on high-variance nearest neighbor estimates that are susceptible to noise." They propose Importance Weighted Retrieval (IWR), which uses Gaussian kernel density estimation to calculate probability ratios between target and prior data distributions. Testing on simulation environments and the Bridge dataset demonstrates consistent performance improvements.

**Key Contribution:** IWR overcomes prior selection rule biases by considering distribution ratios rather than minimum distances alone, requiring only minor modifications to existing methods.

**Related Resources:**
- PDF available via MLResearch GitHub
- OpenReview forum discussion link provided
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a257e6c-fec6-4ae2-90ef-a4a0b8082dad",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ae8490a92fcb2dd4d",
  "type": "user",
  "uuid": "e460a864-6390-4473-bd34-19d5cdbc938e",
  "sourceToolAssistantUUID": "3a257e6c-fec6-4ae2-90ef-a4a0b8082dad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T11:41:34.450Z_

<details><summary>↩ Tool result · `toolu_01KxW71qYrYyLqrfsz78XQbS`</summary>

```text
# Paper Summary: Data Retrieval with Importance Weights for Few-Shot Imitation Learning

## Full Title and Authors
**"Data Retrieval with Importance Weights for Few-Shot Imitation Learning"**

Authors: Amber Xie, Rahul Chand, Dorsa Sadigh, Joey Hejna (Stanford)

## Venue
Conference on Robot Learning (CoRL) 2025 - Oral presentation

## Abstract Overview
The paper addresses limitations in retrieval-based imitation learning by proposing a method that overcomes two key problems with existing approaches. Traditional methods rely on "minimum distance to a point in the target dataset in latent space," which suffers from high-variance nearest neighbor estimates and fails to account for prior data distribution. The authors' solution uses probability ratios rather than proximity alone.

## Key Method: Importance Weighted Retrieval (IWR)

**Core Innovation:** The approach estimates "importance weights, or the ratio between the target and prior data distributions" using Gaussian Kernel Density Estimation (KDE).

**Three-Step Process:**
1. Learning a latent encoding for state-action pairs
2. Computing probability distributions over target and prior data with importance weighting
3. Co-training on combined target and retrieved prior samples

**How Importance Weighting Works:** Rather than selecting samples based solely on nearest-neighbor distance, IWR "uses reasonable modeling parameters" to smooth estimates across all available data points, preventing bias from object similarity or similar task configurations.

## Advantages Over Behavior Retrieval (BR)
The method retrieves "a higher portion of directly relevant tasks" and achieves "more balanced distribution across timesteps" by upweighting underrepresented object instances and later-stage demonstrations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1872bac5-03ce-41aa-9724-707e4b34bf99",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ae8490a92fcb2dd4d",
  "type": "user",
  "uuid": "c8e0411a-ee5b-4f12-bb69-88327489c9e5",
  "sourceToolAssistantUUID": "1872bac5-03ce-41aa-9724-707e4b34bf99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-13T11:41:36.996Z_

Now let me get more details about the density ratio mechanism and the filtering vs. weighting distinction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8e0411a-ee5b-4f12-bb69-88327489c9e5",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWKzAYCcVz9Q14f3nV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "264cfb0e-c3d8-4609-982c-8fc93fd0263b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsEWzWRR8grxgPaH6cEbPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 14808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 23 · 2026-05-13T11:41:39.581Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015WoLVmFMjrodDPt7JxnqFP`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.01657",
  "prompt": "Extract detailed information about: 1) How the importance weights are computed (the density ratio between target and prior distributions), 2) The connection between nearest-neighbor retrieval and KDE, 3) How IWR relates to the question of filtering vs. weighting demonstrations - does it do hard filtering (selecting a subset) or soft weighting (assigning continuous weights)? 4) The bandwidth parameter and its role. 5) Key experimental results and improvements. 6) Any discussion of when weighting is better than filtering."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "264cfb0e-c3d8-4609-982c-8fc93fd0263b",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWKzAYCcVz9Q14f3nV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad4bc0a9-28f0-4882-b20c-38801c8e37fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsEWzWRR8grxgPaH6cEbPB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1374,
      "cache_read_input_tokens": 14808,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1374
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 14808,
          "cache_creation_input_tokens": 1374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1374,
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

_source line 24 · 2026-05-13T11:41:52.384Z_

<details><summary>↩ Tool result · `toolu_015WoLVmFMjrodDPt7JxnqFP`</summary>

```text
# Importance Weighted Retrieval: Technical Analysis

## 1. Importance Weight Computation

IWR computes importance weights as the ratio of probability densities: **p_t/p_prior**. Both densities are estimated using Gaussian kernel density estimation (KDE) applied to learned state-action embeddings:

The method models distributions with the formula: "1/|𝒟| ∑ multivariate Gaussian terms" where each Gaussian is centered at an embedded data point with bandwidth h and covariance matrix Σ.

This allows the system to estimate the relative likelihood of prior samples under the target task distribution, enabling principled data selection that accounts for both distributions.

## 2. Connection Between Nearest-Neighbor and KDE

The paper establishes a mathematical equivalence: the original L2 nearest-neighbor retrieval rule represents the limiting case of KDE as bandwidth h→0. Specifically, they show this by converting the min-distance condition to a log-sum-exp formulation:

"The exponential term within the sum is proportional to multivariate Gaussian pdf...
each centered at each data-point in 𝒟_t...proportional to Gaussian KDE."

As bandwidth shrinks to zero, the KDE becomes "sharply peaked" at individual points, recovering the nearest-neighbor behavior. This reveals that prior methods used overly restrictive density assumptions.

## 3. Hard Filtering vs. Soft Weighting

IWR performs **hard filtering but via soft selection**. The method retrieves data using a threshold: points where p_t^KDE/p_prior^KDE > η are selected as a binary choice. However, the authors acknowledge: "IWR is still a biased estimate, as we do not perform importance sampling, but only retrieve based on importance weights."

They note an alternative would be importance resampling for unbiased estimates, but selected thresholding because it "easily integrates with prior methods." The approach thus falls between pure hard filtering and true probabilistic weighting.

## 4. Bandwidth Parameter Role

The bandwidth h is set using "multiplicative factor of Scott's rule," specifically: h = c × |𝒟|^(-1/(d+4)). This parameter controls smoothing: larger bandwidths produce smoother density estimates using all data points, while smaller values emphasize individual points.

Ablations show that halving the bandwidth factor (c from 4 to 2) slightly degrades performance, suggesting "smoother KDEs are slightly better on average." The bandwidth essentially balances bias and variance in density estimation.

## 5. Key Experimental Results

Performance improvements are substantial:

- **Simulation (LIBERO)**: IWR increased success rates by 5.8% over SAILOR, 4.4% over Flow Retrieval, and 5.8% over Behavior Retrieval
- **Real-world (Bridge)**: Improvements are "more significant, increasing success rate by 30% on average" compared to Behavior Retrieval
- **Long-horizon task (Eggplant)**: Partial success improved from 50% to 100% of rollouts

On simpler tasks like Soup-Cheese where baseline methods already performed well (>50% relevant retrievals), IWR offered minimal additional benefit.

## 6. Weighting Benefits vs. Filtering

The paper implicitly argues for weighting through its probabilistic framing. By considering p_prior in the denominator, IWR addresses a key limitation: "The resulting retrieved distribution...is closer to the product of densities p_t · p_prior than p_t." Normalizing by prior distribution reduces bias introduced by sampling from the prior dataset first.

However, the method stops short of full probabilistic weighting during training—it still applies hard thresholds rather than weighting each sample by its importance weight during policy training. This pragmatic choice prioritizes integration with existing methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad4bc0a9-28f0-4882-b20c-38801c8e37fa",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ae8490a92fcb2dd4d",
  "type": "user",
  "uuid": "f869eae0-c243-4967-b6e0-647aa7dbb051",
  "sourceToolAssistantUUID": "ad4bc0a9-28f0-4882-b20c-38801c8e37fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T11:42:17.387Z_

Here is a comprehensive report on the IWR paper.

---

**Full Title:** "Data Retrieval with Importance Weights for Few-Shot Imitation Learning"

**Authors:** Amber Xie, Rahul Chand, Dorsa Sadigh, Joey Hejna (all Stanford)

**Venue:** The 9th Conference on Robot Learning (CoRL 2025) -- Oral presentation. Published in Proceedings of Machine Learning Research, Volume 305, pages 1-16. Conference dates: September 27-30, 2025.

**ArXiv:** 2509.01657 (submitted September 1, 2025)

---

### What It Does

IWR addresses the problem of **retrieval-based few-shot imitation learning**: given a small target demonstration dataset and a large heterogeneous prior dataset, how do you select the most useful prior data to augment training?

**Key insight:** Existing retrieval methods (like Behavior Retrieval) select prior data points based on minimum L2 distance to the target set in a learned latent space. The paper proves this is mathematically equivalent to the **limiting case of a Gaussian KDE** as bandwidth h approaches 0. This means prior methods were implicitly doing density estimation of the target distribution, but with maximally high variance (nearest-neighbor = zero-bandwidth KDE) and **without accounting for the prior data distribution at all**.

**The method:** IWR computes importance weights as the **density ratio p_target / p_prior**, where both densities are estimated via Gaussian KDE over learned state-action embeddings. A prior data point is retrieved if this ratio exceeds a threshold eta. The bandwidth is set using a multiplicative factor of Scott's rule: h = c * |D|^(-1/(d+4)).

**Why the ratio matters:** Without the prior density in the denominator, retrieval is biased toward regions where the prior dataset happens to be dense (e.g., early timesteps in demonstrations, common objects). By normalizing by p_prior, IWR upweights samples that are relevant to the target task but underrepresented in the prior -- such as later-stage demonstration steps or uncommon object interactions.

---

### Filtering vs. Weighting -- The Central Question

This is where IWR sits in an interesting middle ground:

1. **It uses soft/smooth density estimation** (Gaussian KDE with reasonable bandwidth) rather than the hard nearest-neighbor approach of prior work, which considers all data points when estimating densities rather than just the single closest point.

2. **But it applies a hard threshold for final selection**: data points where p_target/p_prior > eta are included; others are excluded. This is binary filtering, not continuous weighting.

3. **It does NOT do importance-weighted training**: The authors explicitly note that "IWR is still a biased estimate, as we do not perform importance sampling, but only retrieve based on importance weights." They chose hard thresholding over true importance resampling because it "easily integrates with prior methods."

So IWR occupies a hybrid position: the **selection criterion** is based on continuous density ratios (a weighting idea), but the **output** is a hard-filtered subset (a filtering operation). The density ratio informs *which* demonstrations to include, but once selected, all retrieved data points are treated equally during policy training.

---

### Key Results

- **Simulation (LIBERO):** +5.8% success rate over Behavior Retrieval, +4.4% over Flow Retrieval, +5.8% over SAILOR
- **Real-world (Bridge dataset):** +30% average success rate over Behavior Retrieval, with the most dramatic gains on long-horizon and complex tasks
- **Ablations:** Smoother KDEs (larger bandwidth) perform slightly better on average; the prior-density normalization is critical to the gains
- On simple tasks where baseline retrieval already works well (>50% relevant retrievals), IWR offers minimal additional benefit

---

### Key Files/URLs

- ArXiv: `https://arxiv.org/abs/2509.01657`
- Project page: `https://rahulschand.github.io/iwr/` and `https://sites.google.com/stanford.edu/iwr`
- Proceedings: `https://proceedings.mlr.press/v305/xie25a.html`

Sources:
- [ArXiv Abstract](https://arxiv.org/abs/2509.01657)
- [ArXiv HTML Full Paper](https://arxiv.org/html/2509.01657)
- [PMLR Proceedings](https://proceedings.mlr.press/v305/xie25a.html)
- [Project Page (Rahul Chand)](https://rahulschand.github.io/iwr/)
- [Stanford Project Page](https://sites.google.com/stanford.edu/iwr)
- [EmergentMind Topic Page](https://www.emergentmind.com/topics/importance-weighted-retrieval-iwr)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f869eae0-c243-4967-b6e0-647aa7dbb051",
  "isSidechain": true,
  "agentId": "ae8490a92fcb2dd4d",
  "requestId": "req_011CazWMJrxjn8fkbUGZRA6s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89328a3b-5ed3-490a-9bf5-ae6019ab87f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAtetnWS2CDzeJt9c54MCW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 16182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1103,
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
