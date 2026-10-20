# Research conversation: Search the web to verify these papers: 1. "EMA Is Not All You Need: Mapping the Boundary Between Structure and Content i

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a24a26c99a74dea2d.jsonl`
- **Structured JSON:** [`df209ce5ac814b565f64.json`](../../sessions/df/df209ce5ac814b565f64.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-10T18:16:26.773Z_

Search the web to verify these papers:

1. "EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context" (arXiv:2604.08556, Apr 2026). Does this paper exist? Does it show that EMA traces suffer irreversible information dilution? What are its key findings about EMA as context representations?

2. "KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference" (arXiv:2504.15364). Does this paper exist? Does it use mean-of-keys (not EMA) as an anchor for KV eviction?

3. "CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference" (arXiv:2604.08584, Apr 2026). Does this paper exist? Does it construct query-centric lookup tables?

Use WebSearch and WebFetch. Search for exact titles and arXiv IDs. Report all details found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a24a26c99a74dea2d",
  "type": "user",
  "uuid": "82ae47a7-bda3-49da-b441-5266e154be96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:16:26.776Z_

```json
{
  "parentUuid": "82ae47a7-bda3-49da-b441-5266e154be96",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
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
  "uuid": "d8bef6f3-f3b7-454b-83ab-7fb6961f3894",
  "timestamp": "2026-05-10T18:16:26.776Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:16:28.977Z_



I'll search for all three papers in parallel using their arXiv IDs and titles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8bef6f3-f3b7-454b-83ab-7fb6961f3894",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM1hensM3xf2zh1VYVN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ffce517-8307-4e71-862e-fb342719a8a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y52MPXQTD9oodryURaXBRk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 780,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 780,
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

_source line 4 · 2026-05-10T18:16:29.241Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XxeMuShSJ9U6DeSebU4oV7`</summary>

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
  "parentUuid": "8ffce517-8307-4e71-862e-fb342719a8a0",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM1hensM3xf2zh1VYVN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d970a777-4cd1-4841-895e-efc0dcc473d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y52MPXQTD9oodryURaXBRk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 780,
      "cache_read_input_tokens": 8223,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 780
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 780,
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

_source line 5 · 2026-05-10T18:16:29.244Z_

<details><summary>↩ Tool result · `toolu_01XxeMuShSJ9U6DeSebU4oV7`</summary>

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
  "parentUuid": "d970a777-4cd1-4841-895e-efc0dcc473d9",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a24a26c99a74dea2d",
  "type": "user",
  "uuid": "6be344cd-618f-460f-8123-c4be161d26c1",
  "sourceToolAssistantUUID": "d970a777-4cd1-4841-895e-efc0dcc473d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:16:32.465Z_



Now let me search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6be344cd-618f-460f-8123-c4be161d26c1",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM1tSBeoh65TRpHqY2c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c402358-1579-428b-94c1-49bb05862f49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoTxwbko9PwhkLEdMSoBWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 7 · 2026-05-10T18:16:33.425Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017rHwy9ZQehKRfBbsLdhwvi`</summary>

```json
{
  "query": "arXiv 2604.08556 \"EMA Is Not All You Need\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c402358-1579-428b-94c1-49bb05862f49",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM1tSBeoh65TRpHqY2c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b98c89fe-114c-4d1f-8313-8a38d324b33b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoTxwbko9PwhkLEdMSoBWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 8 · 2026-05-10T18:16:34.366Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014RrAQJwaawtsmrs5ZKEUML`</summary>

```json
{
  "query": "arXiv 2504.15364 \"KeyDiff\" KV cache eviction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b98c89fe-114c-4d1f-8313-8a38d324b33b",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM1tSBeoh65TRpHqY2c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91bcdd36-7d4a-4fe8-a9f9-5c7a6e0cff4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoTxwbko9PwhkLEdMSoBWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 9 · 2026-05-10T18:16:34.704Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YKCpNnSKvXBA1ySRZnBURb`</summary>

```json
{
  "query": "arXiv 2604.08584 \"CSAttention\" centroid-scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91bcdd36-7d4a-4fe8-a9f9-5c7a6e0cff4d",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM1tSBeoh65TRpHqY2c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e26e2f0-bdcd-4e1c-9d31-ca4994702851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoTxwbko9PwhkLEdMSoBWr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9003,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 190,
          "cache_read_input_tokens": 9003,
          "cache_creation_input_tokens": 1909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1909,
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

_source line 10 · 2026-05-10T18:16:37.610Z_

<details><summary>↩ Tool result · `toolu_017rHwy9ZQehKRfBbsLdhwvi`</summary>

```text
Web search results for query: "arXiv 2604.08556 "EMA Is Not All You Need""

Links: [{"title":"[2604.08556] EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context","url":"https://arxiv.org/abs/2604.08556"},{"title":"EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context","url":"https://arxiv.org/html/2604.08556"}]

I found the paper! Here are the results for arXiv paper 2604.08556:

**Title:** EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context

**Author:** Arth Singh from AIM Intelligence National Institute of Technology Agartala

**Submission Date:** March 17, 2026

**Main Focus:** The paper investigates what efficient sequence models gain over simple temporal averaging by using exponential moving average (EMA) traces as a controlled probe to map the boundary between what fixed-coefficient accumulation can and cannot represent.

**Key Findings:**
- EMA traces encode temporal structure, with a Hebbian architecture using multi-timescale traces achieving 96% of a supervised BiGRU on grammatical role assignment with zero labels, surpassing the supervised model on structure-dependent roles.
- EMA traces destroy token identity, with a 130M-parameter language model using only EMA context reaching C4 perplexity 260 (8x GPT-2).

The paper is available on arXiv at https://arxiv.org/abs/2604.08556


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b98c89fe-114c-4d1f-8313-8a38d324b33b",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a24a26c99a74dea2d",
  "type": "user",
  "uuid": "a2fb2245-43fb-4cf6-9e74-15d5fef0fd72",
  "sourceToolAssistantUUID": "b98c89fe-114c-4d1f-8313-8a38d324b33b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T18:16:41.785Z_

<details><summary>↩ Tool result · `toolu_014RrAQJwaawtsmrs5ZKEUML`</summary>

```text
Web search results for query: "arXiv 2504.15364 "KeyDiff" KV cache eviction"

Links: [{"title":"[2504.15364] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/abs/2504.15364"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/html/2504.15364"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments | alphaXiv","url":"https://www.alphaxiv.org/abs/2504.15364"},{"title":"Paper page - KeDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://huggingface.co/papers/2504.15364"},{"title":"(PDF) KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://www.researchgate.net/publication/391020426_KeDiff_Key_Similarity-Based_KV_Cache_Eviction_for_Long-Context_LLM_Inference_in_Resource-Constrained_Environments"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250415364P/abstract"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"AI Papers on X: \"KeDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments. https://t.co/PpPoCzf8LI\" / X","url":"https://x.com/SciFi/status/1915009674882998569"},{"title":"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://arxiv.org/html/2509.17396v1"},{"title":"Learning to Evict from Key-Value Cache","url":"https://arxiv.org/html/2602.10238v1"}]

Based on the search results, here's what I found about arXiv 2504.15364 "KeyDiff":

## Overview

KeyDiff is a training-free KV cache eviction method based solely on key similarity that can process arbitrarily long prompts within strict resource constraints.

## Key Concept

The method is based on the observation that geometrically distinctive keys during LLM inference tend to have high attention scores. Lower pairwise cosine similarity among keys correlates with higher attention scores, suggesting its utility as a proxy for token importance.

## Technical Details

KeyDiff is an eviction strategy that selects keys based on their similarity to other cached entries without relying on attention scores or future tokens. KeyDiff solves an optimal subset selection problem that maximizes key diversity.

## Performance Results

With an 8K cache budget (~23% KV cache reduction), KeyDiff achieves less than 0.04% performance gap from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B. Additionally, the method achieves up to 30% end-to-end inference latency reduction compared to existing KV cache eviction methods.

## Key Advantages

Notably KeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91bcdd36-7d4a-4fe8-a9f9-5c7a6e0cff4d",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a24a26c99a74dea2d",
  "type": "user",
  "uuid": "c0ef39fe-1d02-49cf-b4b6-b796cdc065c2",
  "sourceToolAssistantUUID": "91bcdd36-7d4a-4fe8-a9f9-5c7a6e0cff4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:16:43.418Z_

<details><summary>↩ Tool result · `toolu_01YKCpNnSKvXBA1ySRZnBURb`</summary>

```text
Web search results for query: "arXiv 2604.08584 "CSAttention" centroid-scoring"

Links: [{"title":"[2604.08584] CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference","url":"https://arxiv.org/abs/2604.08584"},{"title":"CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference","url":"https://arxiv.org/pdf/2604.08584"},{"title":"CSATTENTION: CENTROID-SCORING ATTENTION FOR ...","url":"https://openreview.net/pdf/f7c7eea1df21aabfb9c33743a2966944b5db04a1.pdf"},{"title":"CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference | OpenReview","url":"https://openreview.net/forum?id=CEpNboUJyw"},{"title":"Entropy Centroids as Intrinsic Rewards for Test-Time Scaling","url":"https://arxiv.org/html/2604.26173"},{"title":"Gradient-Direction Sensitivity Reveals Linear-Centroid Coupling Hidden by Optimizer Trajectories","url":"https://arxiv.org/html/2604.25143"},{"title":"In-Context Examples Suppress Scientific Knowledge Recall in LLMs","url":"https://arxiv.org/html/2604.27540"},{"title":"Improving Robustness of Tabular Retrieval via Representational Stability","url":"https://arxiv.org/html/2604.24040"},{"title":"[2604.26954] The Impact of LLM Self-Consistency and Reasoning Effort on Automated Scoring Accuracy and Cost","url":"https://arxiv.org/abs/2604.26954"},{"title":"[2604.14363] The Cost of Language: Centroid Erasure Exposes and Exploits Modal Competition in Multimodal Language Models","url":"https://arxiv.org/abs/2604.14363"}]

Based on the search results, here's what I found about arXiv paper 2604.08584:

## CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference

CSAttention is a training-free sparse attention method optimized for high-throughput serving of reusable contexts.

### Problem It Addresses

Long-context LLMs increasingly rely on extended, reusable prefill prompts for agents and domain Q&A, pushing attention and KV-cache to become the dominant decode-time bottlenecks. While sparse attention reduces computation and transfer costs, it often struggles to maintain accuracy at high sparsity levels due to the inherent distribution shift between Queries and Keys.

### Key Technical Approach

CSAttention adopts a storage-for-computation strategy tailored to the offline-prefill/online-decode setting: it front-loads computation into a one-time offline prefill phase that can be amortized across multiple queries, while aggressively optimizing per-step decoding latency.

For each subspace, queries from prefill are clustered into centroids. For every centroid, CSAttention precomputes partial dot-products with all keys in that subspace as centroid-scores, and stores a compressed Top-L list (indices + scores).

### Performance Results

While keeping only ∼5% tokens, CSAttention maintains performance within statistical noise of the Full model on the global metric, whereas other sparse methods (PQCache, H2O, SparQ, and MagicPig) exhibit more substantial drops. These results demonstrate that the centroid-scoring token retrieval mechanism effectively preserves near-full model accuracy even at very high sparsity levels.

CSAttention achieves up to 4.24× speedup over full attention when decoding 128K context length.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e26e2f0-bdcd-4e1c-9d31-ca4994702851",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a24a26c99a74dea2d",
  "type": "user",
  "uuid": "9f13f2d1-4aa0-4f1c-99d8-967d1b230f82",
  "sourceToolAssistantUUID": "9e26e2f0-bdcd-4e1c-9d31-ca4994702851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T18:16:47.514Z_

Good, all three papers were found. Now let me fetch the detailed content of each paper to answer the specific questions about EMA dilution, mean-of-keys anchoring, and query-centric lookup tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f13f2d1-4aa0-4f1c-99d8-967d1b230f82",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM2vs4kACkmBuiBrdzP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "278a58c1-f2ec-4bae-b9de-3e777eaeedf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDQomytA93AvJq8dxqHxgC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 10912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
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

_source line 14 · 2026-05-10T18:16:51.789Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VTyoJa1Ngs3cXojTYBmUje`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08556",
  "prompt": "Extract all key findings about EMA traces. Specifically: (1) Does the paper show that EMA traces suffer \"irreversible information dilution\"? (2) What are the key findings about EMA as context representations? (3) What is the paper's main argument about what EMA can and cannot represent? (4) Who are the authors? (5) What is the submission date? List all details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "278a58c1-f2ec-4bae-b9de-3e777eaeedf7",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM2vs4kACkmBuiBrdzP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74285eda-621c-4d03-815f-4d495f1c4034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDQomytA93AvJq8dxqHxgC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 10912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
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

_source line 15 · 2026-05-10T18:16:54.461Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KMMFASCgfW31fLExUW8vz1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.15364",
  "prompt": "Extract details about the method. Specifically: (1) Does this paper use \"mean-of-keys\" or EMA as an anchor for KV eviction? (2) What is the exact mechanism used for deciding which KV pairs to evict? (3) Who are the authors? (4) What is the submission date? (5) What is the core technical approach - is it based on pairwise key similarity, mean-of-keys, or something else?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74285eda-621c-4d03-815f-4d495f1c4034",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM2vs4kACkmBuiBrdzP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e0d4493-3e0c-4d22-acde-c735e07a5bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDQomytA93AvJq8dxqHxgC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 10912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
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

_source line 16 · 2026-05-10T18:16:55.927Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HWTucSaRNYcwH6V8SsV4Zb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08584",
  "prompt": "Extract details about the method. Specifically: (1) Does the paper construct \"query-centric lookup tables\"? (2) What exactly is precomputed during prefill? (3) How does centroid-scoring work - are centroids built from queries or keys? (4) Who are the authors? (5) What is the submission date? (6) Describe the offline prefill and online decode phases in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e0d4493-3e0c-4d22-acde-c735e07a5bbc",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM2vs4kACkmBuiBrdzP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3082444f-97ab-483f-abe4-55598224b331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDQomytA93AvJq8dxqHxgC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 10912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2559,
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

_source line 17 · 2026-05-10T18:16:55.993Z_

<details><summary>↩ Tool result · `toolu_01VTyoJa1Ngs3cXojTYBmUje`</summary>

```text
# Key Findings on EMA Traces

**(1) Irreversible Information Dilution:**
Yes. The abstract explicitly states that "Fixed-coefficient accumulation...suffers irreversible information dilution that only learned, input-dependent selection can resolve." The paper invokes the data processing inequality to explain this phenomenon.

**(2) Key Findings About EMA as Context:**
- EMA traces effectively encode temporal structure, with a Hebbian architecture achieving "96% of a supervised BiGRU on grammatical role assignment with zero labels"
- However, EMA traces fundamentally "destroy token identity"
- A 130M-parameter language model relying solely on EMA context achieved dramatically poor performance (C4 perplexity of 260, compared to GPT-2's baseline)

**(3) Main Argument on EMA Capabilities:**
The paper maps boundaries between what fixed-coefficient accumulation can versus cannot represent. The core claim is that while EMA handles structural patterns well, it cannot preserve individual token information due to its lossy, data-independent compression mechanism.

**(4) Authors:**
Arth Singh

**(5) Submission Date:**
March 17, 2026

The paper's central thesis challenges the sufficiency of simple temporal averaging mechanisms, arguing that learned, input-dependent selection mechanisms are necessary for preserving semantic content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74285eda-621c-4d03-815f-4d495f1c4034",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a24a26c99a74dea2d",
  "type": "user",
  "uuid": "e860440a-235e-4c4c-927c-482980fb1c36",
  "sourceToolAssistantUUID": "74285eda-621c-4d03-815f-4d495f1c4034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T18:16:58.189Z_

<details><summary>↩ Tool result · `toolu_01KMMFASCgfW31fLExUW8vz1`</summary>

```text
# KeyDiff Paper Details

**(1) Anchor Mechanism:**
The abstract does not mention "mean-of-keys" or EMA. The method is described as "based solely on key similarity" without specifying an anchor point.

**(2) Eviction Mechanism:**
The paper identifies tokens to retain based on "key diversity" rather than explicit attention scores. The technique relies on "geometrically distinctive keys" that "tend to have high attention scores," but the exact mechanism for deciding which pairs to evict is not detailed in the provided content.

**(3) Authors:**
Junyoung Park, Dalton Jones, Matthew J Morse, Raghavv Goel, Mingu Lee, and Chris Lott

**(4) Submission Date:**
Initial submission: April 21, 2025

**(5) Core Technical Approach:**
The method uses "pairwise key similarity" to identify important tokens. As stated in the abstract: "geometrically distinctive keys during LLM inference tend to have high attention scores." The approach is "training-free" and does not depend on attention mechanisms themselves, allowing compatibility with optimized systems like FlashAttention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e0d4493-3e0c-4d22-acde-c735e07a5bbc",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a24a26c99a74dea2d",
  "type": "user",
  "uuid": "50448d6c-2436-461e-b888-5df461de4428",
  "sourceToolAssistantUUID": "8e0d4493-3e0c-4d22-acde-c735e07a5bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T18:17:01.738Z_

<details><summary>↩ Tool result · `toolu_01HWTucSaRNYcwH6V8SsV4Zb`</summary>

```text
# CSAttention Paper Details

## Authors
Chuxu Song, Zhencan Peng, Jiuqi Wei, and Chuanhui Yang

## Submission Date
March 30, 2026

## Method Components

**(1) Query-Centric Lookup Tables**
Yes, the paper explicitly constructs these. According to the abstract, CSAttention "constructs query-centric lookup tables during offline prefill, whose size remains fixed during decoding."

**(2) Precomputed During Prefill**
The approach "front-loads computation into a one-time offline prefill phase that can be amortized across multiple queries," creating the lookup tables mentioned above.

**(3) Centroid-Scoring Mechanism**
The abstract indicates the method enables "efficient table lookups and GPU-friendly score accumulation" but doesn't explicitly detail whether centroids derive from queries or keys in the provided excerpt. The mechanism appears query-centric based on the lookup table design.

**(4) Offline Prefill vs. Online Decode**
The method follows "the offline-prefill/online-decode setting" where prefill handles expensive computation once, while decode "aggressively optimizes per-step decoding latency" by "replacing full-context scans with efficient table lookups."

## Performance
CSAttention achieves "up to 4.6x inference speedup" at 128K context length under 95% sparsity compared to baseline methods while maintaining accuracy comparable to full attention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3082444f-97ab-483f-abe4-55598224b331",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a24a26c99a74dea2d",
  "type": "user",
  "uuid": "80c0392f-efc8-464e-9c13-5c31cf61da97",
  "sourceToolAssistantUUID": "3082444f-97ab-483f-abe4-55598224b331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T18:17:05.195Z_

Let me get more details on the KeyDiff paper to confirm whether it uses mean-of-keys or not, and more details on CSAttention's centroid mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80c0392f-efc8-464e-9c13-5c31cf61da97",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM4H8zHVGPS1hmgp4aS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7fb4d89-b477-4bc5-be57-46965bf87f75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXBpBKZpZBtLDZGUg1DsQh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 13471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1624,
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

_source line 21 · 2026-05-10T18:17:08.560Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ex5SGWWTNHtaa895DwiMQh`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.15364",
  "prompt": "Look for any mention of \"mean-of-keys\", \"mean key\", \"EMA\", \"exponential moving average\", or \"anchor\" in the paper. What is the exact mechanism for deciding which keys to evict? Does it compute a mean/centroid of all keys and compare distances, or does it use pairwise cosine similarity between keys? Describe the exact eviction algorithm step by step. What similarity metric is used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7fb4d89-b477-4bc5-be57-46965bf87f75",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM4H8zHVGPS1hmgp4aS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70b939c7-c1b4-42fe-9287-00b2ddfae5cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXBpBKZpZBtLDZGUg1DsQh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 13471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1624,
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

_source line 22 · 2026-05-10T18:17:10.129Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017xYpybuHKsEoGbskrB2yH9`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.08584",
  "prompt": "Look for details on how centroids are constructed. Are the centroids built from queries (query-centric) or from keys? How exactly are the lookup tables constructed? What is stored in the lookup tables? Describe the centroid-scoring mechanism step by step. Are centroids formed by clustering prefill queries?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70b939c7-c1b4-42fe-9287-00b2ddfae5cd",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM4H8zHVGPS1hmgp4aS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3526b5b-7f19-4489-b0be-ed1e2dc60fdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXBpBKZpZBtLDZGUg1DsQh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 13471,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 341,
          "cache_read_input_tokens": 13471,
          "cache_creation_input_tokens": 1624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1624,
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

_source line 23 · 2026-05-10T18:17:16.976Z_

<details><summary>↩ Tool result · `toolu_017xYpybuHKsEoGbskrB2yH9`</summary>

```text
# CSAttention: Centroid Construction and Lookup Tables

## Centroid Construction (Query-Centric)

Yes, centroids are built from queries during the offline prefill phase. The paper explicitly states: "For each subspace bb, cluster queries from prefill into CC centroids."

The process involves cosine k-means clustering on GPU. Specifically, prefill queries Q are partitioned into m subspaces, and for each subspace, the method performs: "min{cj(b)} ∑q∈Q minj∈[1..C] ||q(b)/||q(b)||₂ - cj(b)||₂²"

This is fundamentally different from key-centric approaches used in prior work, which only clustered keys. The paper emphasizes this distinction as crucial for handling query-key distribution shift during long-context decoding.

## Lookup Table Construction

For each centroid (b,j), the method computes "centroid-scores" by calculating inner products between the centroid and all prefill keys: "sj(b)(i) = cj(b)(ki(b))⊤"

The lookup tables store "fixed Top-LL pairs (i, sj(b)(i))" as bounded-capacity structures containing key indices and their precomputed scores. These tables remain constant during decoding.

## Centroid-Scoring Mechanism

During decoding, for a new query:

1. **Find nearest centroid** per subspace via cosine similarity
2. **Fetch m short lists** corresponding to selected centroids
3. **Aggregate scores** across subspaces: "score(i) = ∑b=1ᵐ wb·𝒱ĵb(b)[i]"
4. **Select Top-K keys** from accumulated scores

The mechanism avoids full-context scans by leveraging precomputed centroid-to-key partial scores.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3526b5b-7f19-4489-b0be-ed1e2dc60fdc",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a24a26c99a74dea2d",
  "type": "user",
  "uuid": "649ae464-753a-499c-acff-a1b035cd5e70",
  "sourceToolAssistantUUID": "a3526b5b-7f19-4489-b0be-ed1e2dc60fdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T18:17:17.805Z_

<details><summary>↩ Tool result · `toolu_01Ex5SGWWTNHtaa895DwiMQh`</summary>

```text
# KeyDiff Eviction Mechanism

## Core Algorithm

KeyDiff uses an **anchor-based approach** rather than pairwise similarity. The exact mechanism:

1. **Compute anchor vector**: Calculate the mean of all cached keys: μ(K) = (1/n)∑ k_i
2. **Score each key**: Compute cosine similarity between each key and the anchor vector
3. **Evict low-similarity keys**: Keep the N keys with the **lowest** similarity to the anchor

As stated in the paper: "topk(-CosSim(μ(K^),k^i),N)" where the negative sign indicates keys **dissimilar** to the mean are retained.

## Why This Works

The authors explain that "keys with lower average pairwise cosine similarity tend to receive higher attention scores." By selecting keys most different from the anchor (the mean), KeyDiff retains geometrically diverse keys that correlate with importance.

## Efficiency Advantage

Rather than computing O(n²) pairwise similarities, the efficient variant runs in **O(n) time** by using the single anchor vector. This enables compatibility with optimized attention mechanisms like FlashAttention, yielding "up to 30% latency reduction" compared to attention-based methods.

## Similarity Metric

The paper uses **cosine similarity** exclusively, and ablation studies confirm this metric outperforms alternatives like L2 distance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70b939c7-c1b4-42fe-9287-00b2ddfae5cd",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a24a26c99a74dea2d",
  "type": "user",
  "uuid": "2cb54455-3a94-4306-9f03-5dd43c294255",
  "sourceToolAssistantUUID": "70b939c7-c1b4-42fe-9287-00b2ddfae5cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-10T18:17:53.819Z_

Now I have comprehensive details on all three papers. Here is the full report.

---

## Paper 1: "EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context"

**arXiv ID:** 2604.08556 -- **EXISTS: YES**

- **URL:** [https://arxiv.org/abs/2604.08556](https://arxiv.org/abs/2604.08556)
- **Author:** Arth Singh (AIM Intelligence, National Institute of Technology Agartala)
- **Submission date:** March 17, 2026

**Does it show that EMA traces suffer irreversible information dilution?** Yes. The abstract explicitly states that "fixed-coefficient accumulation suffers irreversible information dilution that only learned, input-dependent selection can resolve." The paper invokes the data processing inequality to formally explain this phenomenon.

**Key findings about EMA as context representations:**

1. **EMA encodes temporal structure well.** A Hebbian architecture using multi-timescale EMA traces achieves 96% of a supervised BiGRU on grammatical role assignment with zero labels, and surpasses the supervised model on structure-dependent roles.
2. **EMA destroys token identity.** A 130M-parameter language model using only EMA context reaches a C4 perplexity of 260, which is 8x worse than GPT-2 -- demonstrating that EMA's lossy, data-independent compression cannot preserve individual token information.
3. **The core thesis:** EMA handles structural patterns effectively but fundamentally cannot preserve semantic content. Learned, input-dependent gating (as in real recurrent models) is necessary to cross that boundary.

---

## Paper 2: "KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference"

**arXiv ID:** 2504.15364 -- **EXISTS: YES**

- **URL:** [https://arxiv.org/abs/2504.15364](https://arxiv.org/abs/2504.15364)
- **Authors:** Junyoung Park, Dalton Jones, Matthew J Morse, Raghavv Goel, Mingu Lee, and Chris Lott
- **Submission date:** April 21, 2025

**Does it use mean-of-keys (not EMA) as an anchor for KV eviction?** Yes, it does use mean-of-keys. The paper computes an anchor vector as the mean of all cached keys: `mu(K) = (1/n) * sum(k_i)`. It then computes cosine similarity between each key and this mean anchor. Keys that are **most dissimilar** from the mean (i.e., most geometrically distinctive) are retained, while keys similar to the mean are evicted. The formula is `topk(-CosSim(mu(K), k_i), N)`. This is explicitly a mean-of-keys approach, **not** EMA.

**Additional details:**
- The efficient variant runs in O(n) time (vs O(n^2) for full pairwise similarity) by using the single mean anchor vector.
- This allows compatibility with FlashAttention since it does not require attention scores.
- With an 8K cache budget (~23% KV cache reduction), KeyDiff achieves less than 0.04% performance gap from the non-evicting baseline on LongBench.
- Achieves up to 30% end-to-end inference latency reduction compared to existing KV cache eviction methods.

---

## Paper 3: "CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference"

**arXiv ID:** 2604.08584 -- **EXISTS: YES**

- **URL:** [https://arxiv.org/abs/2604.08584](https://arxiv.org/abs/2604.08584)
- **Authors:** Chuxu Song, Zhencan Peng, Jiuqi Wei, and Chuanhui Yang
- **Submission date:** March 30, 2026
- Also appears on [OpenReview](https://openreview.net/forum?id=CEpNboUJyw)

**Does it construct query-centric lookup tables?** Yes, explicitly. The abstract states CSAttention "constructs query-centric lookup tables during offline prefill, whose size remains fixed during decoding."

**How centroid-scoring works step by step:**

1. **Offline prefill phase:** Prefill queries Q are partitioned into m subspaces. For each subspace, queries are clustered into C centroids using cosine k-means (centroids are built from **queries**, not keys -- this is the "query-centric" aspect).
2. **Centroid-score computation:** For each centroid, the method precomputes inner products (partial dot-products) between the centroid and all prefill keys, storing the Top-L key indices and scores as bounded lookup tables.
3. **Online decode phase:** For a new decode query: (a) find the nearest centroid per subspace via cosine similarity, (b) fetch m short lists from the lookup tables, (c) aggregate scores across subspaces, (d) select Top-K keys from accumulated scores.
4. This replaces full-context scans with efficient table lookups.

**Performance:** At 95% sparsity (keeping only ~5% of tokens), CSAttention maintains accuracy within statistical noise of full attention. Achieves up to 4.24-4.6x speedup over full attention at 128K context length.

---

**Summary:** All three papers exist at their stated arXiv IDs. Paper 1 does show irreversible information dilution of EMA traces. Paper 2 does use mean-of-keys (not EMA) as an anchor. Paper 3 does construct query-centric lookup tables by clustering prefill queries into centroids.

Sources:
- [EMA Is Not All You Need (arXiv:2604.08556)](https://arxiv.org/abs/2604.08556)
- [KeyDiff (arXiv:2504.15364)](https://arxiv.org/abs/2504.15364)
- [KeyDiff on alphaXiv](https://www.alphaxiv.org/abs/2504.15364)
- [KeyDiff on HuggingFace Papers](https://huggingface.co/papers/2504.15364)
- [CSAttention (arXiv:2604.08584)](https://arxiv.org/abs/2604.08584)
- [CSAttention on OpenReview](https://openreview.net/forum?id=CEpNboUJyw)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cb54455-3a94-4306-9f03-5dd43c294255",
  "isSidechain": true,
  "agentId": "a24a26c99a74dea2d",
  "requestId": "req_011CauM5TphrQQVkDwQey2Ap",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "866cca75-7552-4556-b7e4-886b80741f49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01So3x3ZmCsqXadaM9eSTRo8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 468,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 15095,
      "output_tokens": 1582,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 692
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 468,
          "output_tokens": 1582,
          "cache_read_input_tokens": 15095,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 692,
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
