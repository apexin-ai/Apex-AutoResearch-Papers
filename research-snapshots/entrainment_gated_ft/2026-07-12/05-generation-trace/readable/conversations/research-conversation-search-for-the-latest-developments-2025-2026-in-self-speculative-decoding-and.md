# Research conversation: Search for the latest developments (2025-2026) in self-speculative decoding and sparse attention for LLM inference accel

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a8ae7e4a12f261c81.jsonl`
- **Structured JSON:** [`0eba9f04ef08c1c2b38d.json`](../../sessions/0e/0eba9f04ef08c1c2b38d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-10T20:10:57.024Z_

Search for the latest developments (2025-2026) in self-speculative decoding and sparse attention for LLM inference acceleration. I'm looking for:

1. Any new papers (May-June 2026) that combine per-head adaptive attention with speculative decoding
2. Any papers that do head-level classification/decomposition for attention prediction (not just KV cache compression)
3. Current SOTA throughput numbers for self-speculative decoding on reasoning tasks
4. Any work that challenges or extends TriAttention's MRL-based head classification

Use WebSearch with multiple query variations:
- "self-speculative decoding head adaptive 2026"
- "per-head attention prediction speculative decoding"
- "MRL head classification attention"
- "sparse attention head decomposition LLM"

Report findings concisely, focusing on anything that might affect the novelty or framing of a paper about head-adaptive decomposition for self-speculative decoding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "0fbe3659-37c7-4d6c-831c-64645ab10180",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:10:57.027Z_

```json
{
  "parentUuid": "0fbe3659-37c7-4d6c-831c-64645ab10180",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
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
  "uuid": "09f3e6f9-1622-46cb-b36e-48142d2737ec",
  "timestamp": "2026-05-10T20:10:57.027Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T20:11:00.795Z_



I'll search for the latest developments across these topics. Let me start by loading the WebSearch tool, then run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09f3e6f9-1622-46cb-b36e-48142d2737ec",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVk9W9S6kec1DU7gkDk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc5552de-1bf2-4291-9ecd-0d305fb740d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JcT6KeTdk6E1TthyYZzwa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 766,
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

_source line 4 · 2026-05-10T20:11:01.406Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019J4LmREUKo2BQLie6m5ppr`</summary>

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
  "parentUuid": "fc5552de-1bf2-4291-9ecd-0d305fb740d7",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVk9W9S6kec1DU7gkDk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f4e8bdc-b04a-4b6c-a771-1588854888cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JcT6KeTdk6E1TthyYZzwa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 8223,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 766
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 766,
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

_source line 5 · 2026-05-10T20:11:01.409Z_

<details><summary>↩ Tool result · `toolu_019J4LmREUKo2BQLie6m5ppr`</summary>

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
  "parentUuid": "5f4e8bdc-b04a-4b6c-a771-1588854888cd",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "f41fbb8b-88ed-4c16-b420-74a05b0d6b4e",
  "sourceToolAssistantUUID": "5f4e8bdc-b04a-4b6c-a771-1588854888cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T20:11:04.504Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f41fbb8b-88ed-4c16-b420-74a05b0d6b4e",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVkTzti3szDuepctw4g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "093eaa11-b351-4b33-8ce0-c490e5080d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FmRwknooN4zrBXrdwRfMw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 8989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 7 · 2026-05-10T20:11:09.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FE7UN6Sa2KVbr1grXTagKR`</summary>

```json
{
  "query": "self-speculative decoding head adaptive 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "093eaa11-b351-4b33-8ce0-c490e5080d4d",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVkTzti3szDuepctw4g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12f581e8-2353-4f9e-9116-5bdd1a35212b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FmRwknooN4zrBXrdwRfMw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 8989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 8 · 2026-05-10T20:11:09.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019NShm3dfuSb3QLM3DknAFc`</summary>

```json
{
  "query": "per-head attention prediction speculative decoding 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12f581e8-2353-4f9e-9116-5bdd1a35212b",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVkTzti3szDuepctw4g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67053fbc-e367-48d6-851f-b7c5f8de0fda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FmRwknooN4zrBXrdwRfMw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 8989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 9 · 2026-05-10T20:11:09.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011VGYVX9VZYHb9Bk23LVXDe`</summary>

```json
{
  "query": "MRL head classification attention LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67053fbc-e367-48d6-851f-b7c5f8de0fda",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVkTzti3szDuepctw4g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69358f65-1759-41bb-b6de-88a50d6a5a65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FmRwknooN4zrBXrdwRfMw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 8989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 10 · 2026-05-10T20:11:09.955Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ad2yKovhQc4woexQjJMtHW`</summary>

```json
{
  "query": "sparse attention head decomposition LLM inference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69358f65-1759-41bb-b6de-88a50d6a5a65",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVkTzti3szDuepctw4g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42fca8ee-87eb-4945-8d9f-6b13576ff21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FmRwknooN4zrBXrdwRfMw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 8989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 11 · 2026-05-10T20:11:15.876Z_

<details><summary>↩ Tool result · `toolu_01FE7UN6Sa2KVbr1grXTagKR`</summary>

```text
Web search results for query: "self-speculative decoding head adaptive 2026"

Links: [{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection","url":"https://arxiv.org/html/2605.02888"},{"title":"Speculative Speculative Decoding Tanishq Kumar1,* Tri Dao2,3 Avner May3","url":"https://arxiv.org/pdf/2603.03251"},{"title":"SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification","url":"https://arxiv.org/html/2512.02337v1"},{"title":"CAS-Spec: Cascade Adaptive Self-Speculative Decoding for On-the-Fly Lossless Inference Acceleration of LLMs | OpenReview","url":"https://openreview.net/forum?id=m0bR0sxhfL"},{"title":"Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/html/2605.01106"},{"title":"SpecDec++: Boosting Speculative Decoding via Adaptive Candidate Lengths | OpenReview","url":"https://openreview.net/forum?id=Y131N9fUbU"},{"title":"SELF SPECULATIVE DECODING FOR DIFFUSION ...","url":"https://openreview.net/pdf?id=rKJ7A30lQQ"},{"title":"SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration | OpenReview","url":"https://openreview.net/forum?id=EKJhH5D5wA"},{"title":"GitHub - smart-lty/ParallelSpeculativeDecoding: [ICLR 2025] PEARL: Parallel Speculative Decoding with Adaptive Draft Length · GitHub","url":"https://github.com/smart-lty/parallelspeculativedecoding"}]

Based on the search results, here's what I found about self-speculative decoding with adaptive approaches in 2026:

## Overview

Self-speculative decoding is based on early-exited versions of the larger model, used as the smaller draft model. The smaller draft model, instead of being a separately trained model from the larger verifier model, could simply be a cut-down version of the bigger model.

## Adaptive Approaches in 2026

Several recent papers from 2026 focus on adaptive variants of self-speculative decoding:

**SpecKV (May 2026)**: SpecKV is a lightweight adaptive controller that selects γ per speculation step using signals extracted from the draft model itself. SpecKV achieves a 56.0% improvement in expected tokens per speculation step over the fixed γ=4 default, with only 0.34 ms overhead per decision.

**CAS-Spec**: CAS-Spec constructs speculative draft models by leveraging dynamically switchable inference acceleration (DSIA) strategies, including layer sparsity and activation quantization. The method achieves state-of-the-art acceleration with an average speedup from 1.1× to 2.3× over autoregressive decoding across various LLMs and datasets.

**Component-Aware Self-Speculative Decoding**: This is the first method to exploit the internal architectural heterogeneity of hybrid language models for inference acceleration.

These methods demonstrate the active research focus on making self-speculative decoding more efficient through adaptive mechanisms in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12f581e8-2353-4f9e-9116-5bdd1a35212b",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "912e5b88-dc26-45e0-b22c-0ffd9ff9a415",
  "sourceToolAssistantUUID": "12f581e8-2353-4f9e-9116-5bdd1a35212b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T20:11:16.668Z_

<details><summary>↩ Tool result · `toolu_019NShm3dfuSb3QLM3DknAFc`</summary>

```text
Web search results for query: "per-head attention prediction speculative decoding 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"Efficient and Scalable Speculative Decoding with Multi- ...","url":"https://aclanthology.org/2025.emnlp-main.986.pdf"},{"title":"MIRROR SPECULATIVE DECODING: BREAKING THE SERIAL BARRIER IN LLM INFERENCE","url":"https://arxiv.org/pdf/2510.13161"},{"title":"Linear Predictability of Attention Heads in Large Language Models","url":"https://arxiv.org/html/2603.13314v1"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"ATTENTION HEAD ENTROPY OF LLMS PREDICTS AN","url":"https://openreview.net/pdf/f1d8fabcdf88c7a7a6c264ffba2eef62e00a8f66.pdf"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"},{"title":"LLM Inference Optimization Techniques | Clarifai Guide","url":"https://www.clarifai.com/blog/llm-inference-optimization/"},{"title":"Hardware-Efficient Attention for Fast Decoding","url":"https://arxiv.org/html/2505.21487v1"},{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"}]

Based on the search results, I found several relevant papers and resources on per-head attention prediction and speculative decoding from 2025-2026:

## Key Findings

**Per-Head Attention Prediction:**

Pretrained Transformers develop striking linear dependencies among their attention head activations, where Key, Value, and Query activations of individual heads are linearly predictable from a small set of peer heads across diverse model families. Linear predictability is negligible at initialization and is indeed a learned byproduct of pretraining. This linear predictability can be leveraged for KV cache compression: if K and V states of a "target" head can be accurately reconstructed from a linear combination of K and V states from reference heads, one can store only reference heads and learned projection weights, which differs from concurrent methods that store quantized residuals for all heads.

**Speculative Decoding Advances:**

The speculator and verifier processes run in parallel on separate hardware, with outcomes stored in a "speculation cache". In speculative speculative decoding (SSD), while verification is ongoing, the draft model predicts likely verification outcomes and prepares speculations pre-emptively for them, and if the actual verification outcome is in the predicted set, a speculation can be returned immediately, eliminating drafting overhead entirely.

EAGLE-3, the third version, builds on earlier foundations by introducing multi-layer fused feature representations from the target model and uses a context-aware, dynamic draft tree to propose multiple chained hypotheses, with candidate tokens verified by the target model using parallel tree attention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67053fbc-e367-48d6-851f-b7c5f8de0fda",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "1a68e14e-477e-4a78-bd34-1184cedb8460",
  "sourceToolAssistantUUID": "67053fbc-e367-48d6-851f-b7c5f8de0fda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T20:11:17.461Z_

<details><summary>↩ Tool result · `toolu_01Ad2yKovhQc4woexQjJMtHW`</summary>

```text
Web search results for query: "sparse attention head decomposition LLM inference 2025 2026"

Links: [{"title":"A Visual Guide to Attention Variants in Modern LLMs","url":"https://magazine.sebastianraschka.com/p/visual-attention-variants"},{"title":"Long-Context Generalization with Sparse Attention","url":"https://arxiv.org/pdf/2506.16640"},{"title":"Sparse Attention","url":"https://www.aussieai.com/research/sparse-attention"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"SeerAttention: Learning Intrinsic Sparse Attention in Your LLMs | OpenReview","url":"https://openreview.net/forum?id=HmwneoGoy9"},{"title":"Sparse attention cuts transformer O(n²) complexity | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/sparse-attention-cuts-transformer-on%C2%B2-complexity/"},{"title":"Sparse-Attention Algorithms","url":"https://www.emergentmind.com/topics/sparse-attention-algorithms"},{"title":"How sparse attention solves the memory bottleneck in long-context LLMs - TechTalks","url":"https://bdtechtalks.com/2026/02/23/llm-sparse-attention/"},{"title":"[2507.19595] Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/abs/2507.19595"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://arxiv.org/pdf/2502.11089"}]

Here are the results of the web search for sparse attention head decomposition in LLM inference from 2025-2026:

## Recent Research and Developments

Recent sparse attention research includes methods like S2O: Early Stopping for Sparse Attention via Online Permutation (February 2026), IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse (March 2026), and Scaling Attention via Feature Sparsity (March 2026).

DeepSeek Sparse Attention appeared in the DeepSeek V3.2 line and later in GLM-5, where DeepSeek V3.2 combines it with Multi-head Latent Attention (MLA).

## Key Techniques and Approaches

Adaptive-Scalable α-entmax (ASEntmax) adaptively adjusts sparsity based on sequence length for each attention head and query input. SeerAttention augments conventional attention with a learnable gate that adaptively selects significant blocks in an attention map and deems the rest blocks sparse.

Research assigns different sparsity levels to attention heads and neurons based on their importance scores during inference, enabling dynamic layer-level sparsity optimization at runtime.

## Efficiency and Optimization

Sparse attention techniques limit attention computation to selected subsets of tokens based on fixed patterns, block-wise routing, or clustering strategies, enhancing efficiency while preserving contextual coverage. Some sparse attention methods are plug-and-play at inference (like ProxyAttn, SPLAT, and SharePrefill), while others may require retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42fca8ee-87eb-4945-8d9f-6b13576ff21d",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "22252481-ecd7-47e5-9c3e-3846329535d9",
  "sourceToolAssistantUUID": "42fca8ee-87eb-4945-8d9f-6b13576ff21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T20:11:18.501Z_

<details><summary>↩ Tool result · `toolu_011VGYVX9VZYHb9Bk23LVXDe`</summary>

```text
Web search results for query: "MRL head classification attention LLM 2025 2026"

Links: [{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Attention Mechanism in LLMs Explained (2026)","url":"https://www.buildfastwithai.com/blogs/attention-mechanism-llm-explained"},{"title":"On the Role of Attention Heads in Large Language Model Safety | OpenReview","url":"https://openreview.net/forum?id=h0Ak8A5yqw"},{"title":"ATTENTION HEAD ENTROPY OF LLMS PREDICTS AN","url":"https://openreview.net/pdf/f1d8fabcdf88c7a7a6c264ffba2eef62e00a8f66.pdf"},{"title":"Writing an LLM from scratch, part 12 -- multi-head attention :: Giles' blog","url":"https://www.gilesthomas.com/2025/04/llm-from-scratch-12-multi-head-attention"},{"title":"Attention heads of large language models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40041856/"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"Full LLM Leaderboard 2026 — Advanced Explorer for 300+ AI Models","url":"https://llm-stats.com/leaderboards/llm-leaderboard"},{"title":"Article Not peer-reviewed version Locate, Steer, and Improve: A Practical","url":"https://www.preprints.org/frontend/manuscript/0461f28c43bc6be17ca9822186e8ceb0/download_pub"}]

Based on the search results, here's what I found regarding MRL head classification attention in LLMs for 2025-2026:

## Multi-Head Attention Mechanisms in LLMs (2025-2026)

The search results reveal several key developments in attention head mechanisms and classification:

### Attention Architecture Standards

GQA (Grouped-Query Attention) has become the de facto standard for open-source models in 2025-2026. Multi-head latent attention (MLA), introduced in DeepSeek-V2, takes a fundamentally different approach to the KV cache problem by compressing the full-dimensional key and value vectors into a low-rank latent space before caching.

### Attention Head Classification Research

Recent research has focused on understanding and classifying specific attention head functions. Attention heads play a pivotal role in reasoning and are thought to share similarities with human brain functions, with research exploring their roles and mechanisms to help demystify the internal reasoning processes of LLMs.

### Safety and Interpretability

A novel metric tailored for multi-head attention called the Safety Head ImPortant Score (Ships) was proposed to assess individual heads' contributions to model safety. Additionally, HEAD ENTROPY, a white-box method that uses attention patterns inside the model itself to determine the likelihood of a correct answer, operates on the insight that certain attention heads exhibit distinct entropy patterns when the model generates correct versus incorrect answers.

### Performance Improvements

Flash Attention 4 (March 2026) achieves 1,605 TFLOPs/s on NVIDIA B200 GPUs with 71% hardware utilization, demonstrating significant performance gains in attention computation efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69358f65-1759-41bb-b6de-88a50d6a5a65",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "6edbd954-99a5-4f59-9841-6cf67c139ab2",
  "sourceToolAssistantUUID": "69358f65-1759-41bb-b6de-88a50d6a5a65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T20:11:22.384Z_

Good results. Let me now run more targeted follow-up searches to dig deeper into the most relevant findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6edbd954-99a5-4f59-9841-6cf67c139ab2",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVmimRc716imYyDTVw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "380dded1-e41c-44fa-a63a-2735a7100754",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kKTc9B2aKrBYCFKJ43But",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 837,
      "cache_creation_input_tokens": 2961,
      "cache_read_input_tokens": 10411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2961,
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

_source line 16 · 2026-05-10T20:11:23.417Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ue8fV1pweKSmQFspoUptBC`</summary>

```json
{
  "query": "TriAttention MRL matryoshka attention head classification speculative decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "380dded1-e41c-44fa-a63a-2735a7100754",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVmimRc716imYyDTVw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1576a62-34f1-4b26-9bf4-faefbf48447f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kKTc9B2aKrBYCFKJ43But",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 837,
      "cache_creation_input_tokens": 2961,
      "cache_read_input_tokens": 10411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2961,
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

_source line 17 · 2026-05-10T20:11:24.405Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fo8pRkfVkygeRWmELgkCPM`</summary>

```json
{
  "query": "\"linear predictability of attention heads\" speculative decoding inference acceleration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1576a62-34f1-4b26-9bf4-faefbf48447f",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVmimRc716imYyDTVw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46272962-a427-4edc-a803-4cf8f9cf061c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kKTc9B2aKrBYCFKJ43But",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 837,
      "cache_creation_input_tokens": 2961,
      "cache_read_input_tokens": 10411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2961,
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

_source line 18 · 2026-05-10T20:11:25.399Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015DfYSct42h5AyDMg9oC5up`</summary>

```json
{
  "query": "self-speculative decoding throughput benchmark reasoning tasks 2025 2026 SOTA tokens per second"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46272962-a427-4edc-a803-4cf8f9cf061c",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVmimRc716imYyDTVw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2321c90e-2275-4064-8792-32a0b7569299",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kKTc9B2aKrBYCFKJ43But",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 837,
      "cache_creation_input_tokens": 2961,
      "cache_read_input_tokens": 10411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2961,
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

_source line 19 · 2026-05-10T20:11:25.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RRi154r3BkuvXJNFzY8Hk1`</summary>

```json
{
  "query": "\"component-aware self-speculative decoding\" hybrid language models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2321c90e-2275-4064-8792-32a0b7569299",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVmimRc716imYyDTVw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34ce671c-b2d4-413a-94a3-3926ae9a2e6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kKTc9B2aKrBYCFKJ43But",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 837,
      "cache_creation_input_tokens": 2961,
      "cache_read_input_tokens": 10411,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2961
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 837,
          "output_tokens": 250,
          "cache_read_input_tokens": 10411,
          "cache_creation_input_tokens": 2961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2961,
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

_source line 20 · 2026-05-10T20:11:30.501Z_

<details><summary>↩ Tool result · `toolu_01Ue8fV1pweKSmQFspoUptBC`</summary>

```text
Web search results for query: "TriAttention MRL matryoshka attention head classification speculative decoding"

Links: [{"title":"[2205.13147] Matryoshka Representation Learning","url":"https://arxiv.org/abs/2205.13147"},{"title":"Matryoshka Representation Learning (MRL) from the Ground Up | Aniket Rege","url":"https://aniketrege.github.io/blog/2024/mrl/"},{"title":"GitHub - RAIVNLab/MRL: Code repository for the paper - \"Matryoshka Representation Learning\" · GitHub","url":"https://github.com/RAIVNLab/MRL"},{"title":"Matryoshka Representation Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/c32319f4868da7613d78af9993100e42-Paper-Conference.pdf"},{"title":"What Is Matryoshka Representation Learning in Gemini Embedding 2? | MindStudio","url":"https://www.mindstudio.ai/blog/matryoshka-representation-learning-gemini-embedding-2"},{"title":"SMEC:Rethinking Matryoshka Representation Learning for ...","url":"https://aclanthology.org/2025.emnlp-main.1332.pdf"},{"title":"Matryoshka Representation Learning (MRL)","url":"https://www.emergentmind.com/topics/matryoshka-representation-learning-mrl"},{"title":"🪆 Introduction to Matryoshka Embedding Models","url":"https://huggingface.co/blog/matryoshka"},{"title":"Matryoshka Representation Learning: The Ultimate Guide & How We Use It","url":"https://supermemory.ai/blog/matryoshka-representation-learning-the-ultimate-guide-how-we-use-it/"},{"title":"Matryoshka Representation Learning Explained | by Bilge Ince | Medium","url":"https://medium.com/@aysebilgegunduz/matryoshka-representation-learning-explained-ccfbee83f22b"}]

Based on the search results, I found information about Matryoshka Representation Learning (MRL), but the results don't contain specific information about "TriAttention," "attention head classification," or "speculative decoding" in connection with MRL.

Here's what I found about MRL:

Matryoshka Representation Learning (MRL) is a method which encodes information at different granularities and allows a single embedding to adapt to the computational constraints of downstream tasks. The name comes from matryoshka dolls — the Russian wooden nesting dolls where each doll contains a smaller but complete version of itself inside. MRL embeddings work on the same principle.

MRL trains the model with a joint loss function that applies at multiple scales simultaneously. It's also penalized for poor performance at the first 2,048, 1,536, 1,024, and 768 dimensions. This forces the model to encode the most important semantic information into the earliest dimensions first.

However, the search results do not contain information about TriAttention, attention head classification, or speculative decoding in relation to MRL. These may be more recent developments, alternative approaches, or specialized applications that weren't captured in these results. If you're looking for information about these specific techniques in combination with MRL, you may want to search for more recent research papers or specialized documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1576a62-34f1-4b26-9bf4-faefbf48447f",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "99ab7812-b210-4cc8-aa8c-af122da92abe",
  "sourceToolAssistantUUID": "f1576a62-34f1-4b26-9bf4-faefbf48447f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T20:11:32.337Z_

<details><summary>↩ Tool result · `toolu_01Fo8pRkfVkygeRWmELgkCPM`</summary>

```text
Web search results for query: ""linear predictability of attention heads" speculative decoding inference acceleration 2026"

Links: [{"title":"Linear Predictability of Attention Heads in Large Language Models","url":"https://www.researchgate.net/publication/402479758_Linear_Predictability_of_Attention_Heads_in_Large_Language_Models"},{"title":"Linear Predictability of Attention Heads in Large Language Models","url":"https://arxiv.org/html/2603.13314v1"},{"title":"[2603.13314] Linear Predictability of Attention Heads in Large Language Models","url":"https://arxiv.org/abs/2603.13314"},{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"},{"title":"SpecEE: Accelerating Large Language Model Inference with Speculative Early Exiting | Proceedings of the 52nd Annual International Symposium on Computer Architecture","url":"https://dl.acm.org/doi/10.1145/3695053.3730996"},{"title":"A Visual Guide to Attention Variants in Modern LLMs","url":"https://magazine.sebastianraschka.com/p/visual-attention-variants"},{"title":"Accelerating LLM Inference with Lossless Speculative Decoding Algorithms for Heterogeneous Vocabularies | OpenReview","url":"https://openreview.net/forum?id=vQubr1uBUw&noteId=gx2qp54uTb"},{"title":"Speculative Sampling — TensorRT-LLM","url":"https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html"},{"title":"Paper page - When Linear Attention Meets Autoregressive Decoding: Towards More Effective and Efficient Linearized Large Language Models","url":"https://huggingface.co/papers/2406.07368"},{"title":"When Linear Attention Meets Autoregressive Decoding: Towards More Effective and Efficient Linearized Large Language Models","url":"https://arxiv.org/html/2406.07368v1"}]

Based on my search results, I found highly relevant research on linear predictability of attention heads in large language models. Here's what I found:

## Key Research on Linear Predictability of Attention Heads

Large language model inference is increasingly bottlenecked by the Key-Value (KV) cache. Pretrained Transformers exhibit a pervasive inter-head linear structure where Query, Key, and Value vectors of an attention head can often be reconstructed as a linear combination of a small number of peer heads, typically within the same layer.

### Empirical Results

Across Llama-3.1-8B, Falcon3-10B, OLMo-2-7B, and Qwen3-32B, just 2-5 reference heads recover many target heads with high fidelity (e.g., mean R^2 ≈ 0.76 for Keys on C4 with five references, and frequently R^2 > 0.85 on GSM8K).

### Learned vs. Architectural Property

This predictability is learned rather than architectural: it is largely absent at random initialization, rises rapidly during pretraining, and is supported by a theoretical lower bound showing high mean-squared error for linear prediction at initialization.

## Application to Inference Acceleration

This finding opens a new avenue for optimizing LLM inference, particularly by addressing the memory bottleneck of the KV cache. During inference, systems can cache only the reference heads and reconstruct the others on-the-fly, shrinking memory with minimal extra compute.

This research represents a significant 2026 discovery that connects fine-grained attention head structure to practical inference optimization, complementing other acceleration techniques like speculative decoding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46272962-a427-4edc-a803-4cf8f9cf061c",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "5585d249-4bec-4afc-8c75-d83117292818",
  "sourceToolAssistantUUID": "46272962-a427-4edc-a803-4cf8f9cf061c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T20:11:33.557Z_

<details><summary>↩ Tool result · `toolu_01RRi154r3BkuvXJNFzY8Hk1`</summary>

```text
Web search results for query: ""component-aware self-speculative decoding" hybrid language models 2026"

Links: [{"title":"[2605.01106] Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/abs/2605.01106"},{"title":"Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/html/2605.01106"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"SpecEE: Accelerating Large Language Model Inference with Speculative Early Exiting | Proceedings of the 52nd Annual International Symposium on Computer Architecture","url":"https://dl.acm.org/doi/10.1145/3695053.3730996"},{"title":"(PDF) Self Speculative Decoding for Diffusion Large Language Models","url":"https://www.researchgate.net/publication/396249244_Self_Speculative_Decoding_for_Diffusion_Large_Language_Models"},{"title":"Kangaroo: Lossless Self-Speculative Decoding for Accelerating LLMs via Double Early Exiting | OpenReview","url":"https://openreview.net/forum?id=lT3oc04mDp"},{"title":"Self Speculative Decoding for Diffusion Large Language Model | OpenReview","url":"https://openreview.net/forum?id=rKJ7A30lQQ"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"},{"title":"Speculative Speculative Decoding Tanishq Kumar1,* Tri Dao2,3 Avner May3","url":"https://arxiv.org/pdf/2603.03251"}]

I found relevant research on component-aware self-speculative decoding in hybrid language models from 2026. Here are the key findings:

## Overview

Component-aware self-speculative decoding is the first method to exploit the internal architectural heterogeneity of hybrid language models, isolating the SSM/linear-attention subgraph as a zero-cost internal draft.

## Key Results

The research demonstrates significant differences in performance based on hybrid architecture design:

Parallel hybrids achieve acceptance rates of alpha = 0.68 at draft length k=2 under greedy decoding, while sequential hybrids yield only alpha = 0.038 -- an 18x gap attributable to how each architecture integrates its components.

The property is scale-invariant: Falcon-H1 at 3B reproduces the rates observed at 0.5B.

## Evaluation and Findings

The evaluation was conducted on two architecturally distinct hybrid families: Falcon-H1 (parallel: Mamba-2 + attention per layer) and Qwen3.5 (sequential: interleaved linear and attention layers), with a pure Transformer control (Qwen2.5).

The composition pattern of hybrid models -- not merely the presence of alternative components -- determines whether component-level self-speculation is viable.

For sequential hybrids where this approach struggles, generic LayerSkip achieves 12x higher acceptance rates than the component-aware strategy.

The paper was published on arXiv on May 1, 2026, by Hector Borobia and co-authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34ce671c-b2d4-413a-94a3-3926ae9a2e6c",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "1f2e14f6-56f8-45d5-8139-76ce52f7f6dc",
  "sourceToolAssistantUUID": "34ce671c-b2d4-413a-94a3-3926ae9a2e6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T20:11:33.643Z_

<details><summary>↩ Tool result · `toolu_015DfYSct42h5AyDMg9oC5up`</summary>

```text
Web search results for query: "self-speculative decoding throughput benchmark reasoning tasks 2025 2026 SOTA tokens per second"

Links: [{"title":"Speculative Decoding: Achieving 2-3x LLM Inference Speedup | Introl Blog","url":"https://introl.com/blog/speculative-decoding-llm-inference-speedup-guide-2025"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"Decoding Speculative Decoding","url":"https://aclanthology.org/2025.naacl-long.328.pdf"},{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling","url":"https://www.arxiv.org/pdf/2509.04474"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"An Empirical Study of Speculative Decoding on Software Engineering Tasks","url":"https://arxiv.org/html/2604.26469v1"},{"title":"Efficient LLM System with Speculative Decoding | EECS at UC Berkeley","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-224.html"},{"title":"Rethinking the High-Throughput LLM Inference: An Opportunity for Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=59OJOgKLzN"},{"title":"Speculative Decoding: Speeding LLM Generation","url":"https://www.emergentmind.com/topics/speculative-decoding-technique"}]

Based on the search results, here's what I found about self-speculative decoding throughput benchmarks for reasoning tasks in 2025-2026:

## Self-Speculative Decoding for Reasoning Tasks

SparseSpec is a speculative decoding framework that reuses the same model as the draft and target models (self-speculation), featuring a novel sparse attention mechanism called PillarAttn as the draft model, which accurately selects critical tokens via reusing information from the verification stage. This approach was published in December 2025 and specifically targets reasoning model inference.

Self-speculative decoding is where the smaller draft model is simply a cut-down version of the bigger model, with advantages including only one model to train, partial computations in the smaller model being reusable by the verifier model, and the verifier model effectively overlapping its computations to reduce latency.

## General Speculative Decoding Benchmarks for 2025-2026

Speculative decoding achieves 2-3x speedup without changing output quality. More specifically, NVIDIA demonstrated 3.6x throughput improvements on H200 GPUs.

For reasoning tasks specifically, generating multiple full-length responses or iterative reasoning chains incurs prohibitive computational overhead, leading to a significant latency bottleneck. Speculative decoding has emerged as a leading technique to accelerate autoregressive generation by using a fast draft mechanism to propose candidate token sequences, which are then verified.

However, the search results don't contain specific "tokens per second" SOTA benchmarks for self-speculative decoding on reasoning tasks. The available data focuses on speedup ratios and general throughput improvements rather than absolute token/second measurements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2321c90e-2275-4064-8792-32a0b7569299",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "2f1f94fc-060f-43f0-a6f7-14295832b092",
  "sourceToolAssistantUUID": "2321c90e-2275-4064-8792-32a0b7569299",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T20:11:35.708Z_

Let me run a few more targeted searches to fill in remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f1f94fc-060f-43f0-a6f7-14295832b092",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVnqW1QH8p91AFNKkNt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32a1709d-9890-4410-aaf8-bea8ce7a92b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSZwJDNWKRTCkz1hXX4Uwc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3988,
      "cache_read_input_tokens": 13372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3988,
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

_source line 25 · 2026-05-10T20:11:37.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WXHyZzQNTrGV3EesfCxx2F`</summary>

```json
{
  "query": "arxiv 2605 \"sparse self-speculative decoding\" PillarAttn reasoning model inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32a1709d-9890-4410-aaf8-bea8ce7a92b7",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVnqW1QH8p91AFNKkNt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "764f9941-aedc-46d4-9bd1-a55337b4b66c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSZwJDNWKRTCkz1hXX4Uwc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3988,
      "cache_read_input_tokens": 13372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3988,
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

_source line 26 · 2026-05-10T20:11:38.144Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016QcEUCLiUiFVS3kwwz7krt`</summary>

```json
{
  "query": "CAS-Spec cascade adaptive self-speculative decoding layer sparsity activation quantization 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "764f9941-aedc-46d4-9bd1-a55337b4b66c",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVnqW1QH8p91AFNKkNt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2082babd-5759-4c27-85cd-e5bd21b3267b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSZwJDNWKRTCkz1hXX4Uwc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3988,
      "cache_read_input_tokens": 13372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3988,
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

_source line 27 · 2026-05-10T20:11:38.611Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TrPSmBy3TNgTfFAYWsKA19`</summary>

```json
{
  "query": "SWIFT self-speculative decoding attention head skipping layer skip 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2082babd-5759-4c27-85cd-e5bd21b3267b",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVnqW1QH8p91AFNKkNt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71a49284-05a5-4f5b-aa5b-2071c041c5a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSZwJDNWKRTCkz1hXX4Uwc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3988,
      "cache_read_input_tokens": 13372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3988,
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

_source line 28 · 2026-05-10T20:11:39.379Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BwPzdnBgaBwVo8u1o8FLrm`</summary>

```json
{
  "query": "head-level adaptive sparse attention speculative decoding decomposition draft model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71a49284-05a5-4f5b-aa5b-2071c041c5a7",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVnqW1QH8p91AFNKkNt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b908de4-c264-4c0b-89dd-6d625a3ea6f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSZwJDNWKRTCkz1hXX4Uwc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3988,
      "cache_read_input_tokens": 13372,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3988
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 950,
          "output_tokens": 251,
          "cache_read_input_tokens": 13372,
          "cache_creation_input_tokens": 3988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3988,
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

_source line 29 · 2026-05-10T20:11:44.139Z_

<details><summary>↩ Tool result · `toolu_01WXHyZzQNTrGV3EesfCxx2F`</summary>

```text
Web search results for query: "arxiv 2605 "sparse self-speculative decoding" PillarAttn reasoning model inference"

Links: [{"title":"Accelerating Large-Scale Reasoning Model Inference with ...","url":"https://arxiv.org/pdf/2512.01278"},{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"1 Introduction","url":"https://arxiv.org/html/2512.01278"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2512.01278"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.01278v1"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding – Own Your AI","url":"https://ownyourai.com/accelerating-large-scale-reasoning-model-inference-with-sparse-self-speculative-decoding/"},{"title":"SparseSpec: Sparse Computation Innovations","url":"https://www.emergentmind.com/topics/sparsespec"},{"title":"[Literature Review] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://www.themoonlight.io/en/review/accelerating-large-scale-reasoning-model-inference-with-sparse-self-speculative-decoding"},{"title":"Accelerate Speculative Decoding with Sparse Computation in Verification","url":"https://arxiv.org/html/2512.21911"},{"title":"Accelerating Large Language Model Reasoning via Speculative Search","url":"https://arxiv.org/html/2505.02865v1"}]

Based on the search results, I found the paper you're looking for:

## Summary

The paper is titled "Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding" (arXiv:2512.01278).

### Key Innovation: PillarAttn

SparseSpec features a novel sparse attention mechanism, PillarAttn, as the draft model, which accurately selects critical tokens via elegantly reusing information from the verification stage. PillarAttn selectively loads and computes only the critical tokens—those with the highest attention scores during inference—thereby significantly reducing memory bandwidth usage.

### Framework Overview

SparseSpec is a speculative decoding framework that reuses the same model as the draft and target models (i.e., self-speculation), featuring PillarAttn as the draft model, which accurately selects critical tokens via elegantly reusing information from the verification stage.

### System Optimizations

SparseSpec co-designs self-speculation with three system optimizations: (1) a unified scheduler to batch both draft and verification phases to maximize parallelism, (2) delayed verification for CPU/GPU overlap, and (3) dynamic KV-Cache management to enable host memory offload to maximize GPU memory utilization.

### Performance Results

SparseSpec outperforms state-of-the-art solutions, with an up to 2.13× throughput gain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "764f9941-aedc-46d4-9bd1-a55337b4b66c",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "4eb5bbb2-1f1d-4a43-b778-824bbae251dc",
  "sourceToolAssistantUUID": "764f9941-aedc-46d4-9bd1-a55337b4b66c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T20:11:45.352Z_

<details><summary>↩ Tool result · `toolu_016QcEUCLiUiFVS3kwwz7krt`</summary>

```text
Web search results for query: "CAS-Spec cascade adaptive self-speculative decoding layer sparsity activation quantization 2025"

Links: [{"title":"[2510.26843] CAS-Spec: Cascade Adaptive Self-Speculative Decoding for On-the-Fly Lossless Inference Acceleration of LLMs","url":"https://arxiv.org/abs/2510.26843"},{"title":"CAS-Spec: Cascade Adaptive Self-Speculative Decoding ...","url":"https://www.arxiv.org/pdf/2510.26843"},{"title":"CAS-Spec: Cascade Adaptive Self-Speculative Decoding for On-the-Fly Lossless Inference Acceleration of LLMs","url":"https://arxiv.org/html/2510.26843v1"},{"title":"CAS-Spec: Cascade Adaptive Self-Speculative Decoding for On-the-Fly Lossless Inference Acceleration of LLMs | OpenReview","url":"https://openreview.net/forum?id=m0bR0sxhfL"},{"title":"QSpec: Speculative Decoding with Complementary Quantization Schemes | Request PDF","url":"https://www.researchgate.net/publication/397425466_QSpec_Speculative_Decoding_with_Complementary_Quantization_Schemes"},{"title":"FASTER CASCADES VIA SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=vo9t20wsmd"},{"title":"SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification","url":"https://arxiv.org/html/2512.02337v1"},{"title":"[2405.19261] Faster Cascades via Speculative Decoding","url":"https://arxiv.org/abs/2405.19261"},{"title":"Cascade Speculative Drafting for Even Faster LLM Inference","url":"https://www.researchgate.net/publication/397198670_Cascade_Speculative_Drafting_for_Even_Faster_LLM_Inference"},{"title":"Faster Cascades via Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=vo9t20wsmd"}]

I found comprehensive search results about CAS-Spec. Here's what the research shows:

## CAS-Spec Overview

CAS-Spec (Cascade Adaptive Self-Speculative Decoding) is a method that constructs speculative draft models by leveraging dynamically switchable inference acceleration (DSIA) strategies, including layer sparsity and activation quantization.

## Key Technical Features

CAS-Spec dynamically constructs a hierarchy of speculative draft stages using the target model itself by leveraging Dynamically Switchable Inference Acceleration (DSIA) strategies, including techniques such as layer sparsity and activation quantization.

The research describes several DSIA strategies:
- Layer Sparsity: Skipping a subset of transformer layers or a subset of attention and FFN blocks in the target model to generate draft tokens
- Activation Sparsity: Keeping only a subset of neurons (activations) in each layer to reduce computation and memory movement of weights
- Activation Quantization: Using lower precision (e.g., INT4) for activations and (partial) KV cache of the model during draft generation

## Algorithm and Performance

To coordinate this hierarchy at runtime, CAS-Spec introduces a Dynamic Tree Cascade (DyTC) algorithm to adaptively route the draft models, construct draft trees as well as controlling the draft lengths.

CAS-Spec achieves state-of-the-art acceleration compared to existing on-the-fly speculative decoding methods, with an average speedup from 1.1× to 2.3× over autoregressive decoding across various LLMs and datasets.

The paper was published in October 2025 as a NeurIPS 2025 poster presentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2082babd-5759-4c27-85cd-e5bd21b3267b",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "09c1b31b-dbeb-43ab-a2a7-410eac4fd2c9",
  "sourceToolAssistantUUID": "2082babd-5759-4c27-85cd-e5bd21b3267b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T20:11:45.736Z_

<details><summary>↩ Tool result · `toolu_01TrPSmBy3TNgTfFAYWsKA19`</summary>

```text
Web search results for query: "SWIFT self-speculative decoding attention head skipping layer skip 2025 2026"

Links: [{"title":"SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration | OpenReview","url":"https://openreview.net/forum?id=EKJhH5D5wA"},{"title":"GitHub - hemingkx/SWIFT: [ICLR 2025] SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration","url":"https://github.com/hemingkx/SWIFT"},{"title":"ConfLayers: Adaptive Confidence-based Layer Skipping for Self-Speculative Decoding","url":"https://arxiv.org/html/2604.14612v1"},{"title":"[2410.06916] SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration","url":"https://arxiv.org/abs/2410.06916"},{"title":"swift: on-the-fly self-speculative decod","url":"https://arxiv.org/pdf/2410.06916"},{"title":"LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding","url":"https://arxiv.org/pdf/2404.16710"},{"title":"Enabling Early Exit Inference and Self-Speculative Decoding","url":"https://ai.meta.com/research/publications/layerskip-enabling-early-exit-inference-and-self-speculative-decoding/"},{"title":"CLaSp: In-Context Layer Skip for Self-Speculative Decoding","url":"https://arxiv.org/html/2505.24196v1"},{"title":"GitHub - facebookresearch/LayerSkip: Code for \"LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding\", ACL 2024 · GitHub","url":"https://github.com/facebookresearch/LayerSkip"},{"title":"CLaSp: In-Context Layer Skip for Self-Speculative Decoding","url":"https://aclanthology.org/2025.acl-long.1525.pdf"}]

Based on the search results, I found relevant information about SWIFT and related self-speculative decoding techniques. Here's what I found:

## SWIFT: On-the-Fly Self-Speculative Decoding

SWIFT is a plug-and-play SD solution with layer-skipping, which skips intermediate layers of the target LLM as the compact draft model. SWIFT is an on-the-fly self-speculative decoding algorithm that adaptively selects intermediate layers of LLMs to skip during inference.

In each decoding step, this approach skips intermediate layers of the LLM to efficiently generate draft tokens; these tokens are then validated in parallel by the full-parameter LLM to ensure that the output distribution of the target LLM remains unchanged.

SWIFT achieves speedups of 1.3×∼1.5× over vanilla autoregressive decoding, demonstrating its effectiveness across both greedy decoding and random sampling settings.

## Related Recent Developments

SWIFT further advances this direction by adaptively selecting skip layers at runtime on a per-input basis without additional training, achieving consistent speedups across both open-ended and structured tasks.

Building on SWIFT's work, CLaSp is a dynamic in-context layer-skipping method for self-speculative decoding. Unlike existing methods, CLaSp dynamically adjusts the skipped layer set at each decoding step based on the current context, eliminating the need for pre-optimization or retraining.

The SWIFT paper was submitted to ICLR 2025 and represents an advancement in making speculative decoding more practical without requiring separate draft models or extensive training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71a49284-05a5-4f5b-aa5b-2071c041c5a7",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "7c01c4e5-4a02-498c-b4be-370821aba366",
  "sourceToolAssistantUUID": "71a49284-05a5-4f5b-aa5b-2071c041c5a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T20:11:47.737Z_

<details><summary>↩ Tool result · `toolu_01BwPzdnBgaBwVo8u1o8FLrm`</summary>

```text
Web search results for query: "head-level adaptive sparse attention speculative decoding decomposition draft model 2026"

Links: [{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641v1"},{"title":"Accelerating Large-Scale Reasoning Model Inference with ...","url":"https://arxiv.org/pdf/2512.01278"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"SpecEE: Accelerating Large Language Model Inference with Speculative Early Exiting | Proceedings of the 52nd Annual International Symposium on Computer Architecture","url":"https://dl.acm.org/doi/10.1145/3695053.3730996"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=speculative+decoding"},{"title":"An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"},{"title":"Lossless Large Language Model Acceleration via Self- ...","url":"https://aclanthology.org/2024.acl-long.607.pdf"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"PARALLEL SPECULATIVE DECODING WITH ADAPTIVE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/03b1043052700b1a471996b0baf309d4-Paper-Conference.pdf"}]

I found several relevant research papers related to your query. Here are the key findings:

## Recent Research on Sparse Attention and Speculative Decoding

**SparseSpec with PillarAttn**

SparseSpec features a novel sparse attention mechanism, PillarAttn, as the draft model, which accurately selects critical tokens via elegantly reusing information from the verification stage. SparseSpec identifies the KV-Cache loading as the key bottleneck during token generation, and uses the same model weights with dynamic sparse attention as the draft model to achieve high efficiency and a high acceptance rate without additional training.

**SpecAttn: Speculating Sparse Attention**

SpecAttn is a novel training-free approach that seamlessly integrates with existing speculative decoding techniques to enable efficient sparse attention in pre-trained transformers. The attention patterns computed by draft models during speculative execution contain rich information about token importance that can be leveraged for dynamic, content-aware key-value cache pruning without much additional computational overhead.

**Head-level Adaptation**

Twilight applies adaptive top-p pruning for hierarchical attention sparsity. However, these semi-dynamic schemes still rely on predetermined head patterns or incur extra prediction overhead.

The research from late 2025 and early 2026 shows active development in combining adaptive sparse attention mechanisms with speculative decoding draft models to improve LLM inference efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b908de4-c264-4c0b-89dd-6d625a3ea6f6",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "abcaf9ad-da2e-4e03-9506-271bcc69d3a7",
  "sourceToolAssistantUUID": "1b908de4-c264-4c0b-89dd-6d625a3ea6f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T20:11:50.475Z_

Let me do a final round of targeted searches to cover the remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abcaf9ad-da2e-4e03-9506-271bcc69d3a7",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVoskid8X7kUubnFeWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26daa0b1-4ad3-40b2-9b00-f6e3e9da46f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXMwVJcMDiMn4skb53Hxpp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4880,
      "cache_read_input_tokens": 17360,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4880,
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

_source line 34 · 2026-05-10T20:11:51.424Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RWninfVe6CkYzzsBmG6prx`</summary>

```json
{
  "query": "SpecAttn speculating sparse attention head importance draft model KV cache pruning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26daa0b1-4ad3-40b2-9b00-f6e3e9da46f4",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVoskid8X7kUubnFeWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92e46b84-c7f8-4f41-890b-4dc7e02abb5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXMwVJcMDiMn4skb53Hxpp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4880,
      "cache_read_input_tokens": 17360,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4880,
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

_source line 35 · 2026-05-10T20:11:52.402Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H3KL2em9iSYZZExqhii4VH`</summary>

```json
{
  "query": "\"attention head\" classification decomposition \"draft model\" self-speculative per-head 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92e46b84-c7f8-4f41-890b-4dc7e02abb5e",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVoskid8X7kUubnFeWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2a682ce-ddbb-4a19-a674-158e7bb249e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXMwVJcMDiMn4skb53Hxpp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4880,
      "cache_read_input_tokens": 17360,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4880,
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

_source line 36 · 2026-05-10T20:11:52.707Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018rXny2zNAdfkCngVCFvG7f`</summary>

```json
{
  "query": "SparseSpec PillarAttn throughput tokens per second reasoning DeepSeek R1 benchmark 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2a682ce-ddbb-4a19-a674-158e7bb249e6",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVoskid8X7kUubnFeWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5770f529-d8a2-4b4a-b5c2-0d33ae19a92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXMwVJcMDiMn4skb53Hxpp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4880,
      "cache_read_input_tokens": 17360,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4880
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 17360,
          "cache_creation_input_tokens": 4880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4880,
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

_source line 37 · 2026-05-10T20:11:58.984Z_

<details><summary>↩ Tool result · `toolu_01RWninfVe6CkYzzsBmG6prx`</summary>

```text
Web search results for query: "SpecAttn speculating sparse attention head importance draft model KV cache pruning 2025"

Links: [{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641"},{"title":"SpecAttn: Speculating Sparse Attention Harsh Shah Machine Learning Department","url":"https://arxiv.org/pdf/2510.27641"},{"title":"[2510.27641] SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/abs/2510.27641"},{"title":"SpecAttn: Speculating Sparse Attention Harsh Shah Machine Learning Department","url":"https://openreview.net/pdf?id=5HgJc8B3j5"},{"title":"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/html/2602.07223"},{"title":"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://www.arxiv.org/pdf/2602.07223"},{"title":"Specattn Achieves 75% Speedup Via Sparse Attention, Leveraging Draft Tokens For Efficient Decoding","url":"https://quantumzeitgeist.com/75-percent-attention-specattn-achieves-speedup-sparse-leveraging-draft-tokens-efficient/"},{"title":"[2602.07223] SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/abs/2602.07223"},{"title":"Accelerating Large-Scale Reasoning Model Inference with ...","url":"https://arxiv.org/pdf/2512.01278"},{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"}]

I've found research papers on SpecAttn and related sparse attention techniques for LLM optimization. Here's what the search results show:

## SpecAttn: Speculating Sparse Attention

SpecAttn is a training-free framework that fuses speculative decoding with dynamic sparse attention to drastically reduce the key-value (KV) cache usage in LLM inference. By exploiting the attention weights already computed by the draft model to score and select the most informative tokens at each generation step, SpecAttn prunes the KV-cache significantly without any model modifications, preserving output fidelity while delivering end-to-end latency improvements.

## Key Techniques

SpecAttn employs three core techniques: KL divergence-based layer alignment between draft and target models, a GPU-optimized sorting-free algorithm for top-p token selection from draft attention patterns, and dynamic key-value cache pruning guided by these predictions.

## Performance Results

SpecAttn can reduce KV cache access by up to 78% while maintaining reasonable perplexity degradation (15.29% relative increase for p=0.95). The method excels at balancing efficiency and quality, outperforming existing methods like Quest at similar sparsity levels through context-aware and dynamic pruning.

## Related Work

The search results also reveal a more recent paper from February 2026 on SpecAttn, a self-speculative decoding method with verification-guided sparse attention that identifies critical KV entries as a byproduct of verification and only loads these entries when drafting subsequent tokens. This approach achieves 2.81× higher throughput over vanilla auto-regressive decoding and 1.29× improvement over state-of-the-art sparsity-based self-speculative decoding methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92e46b84-c7f8-4f41-890b-4dc7e02abb5e",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "e5192527-b0bb-4369-bfb8-55a445b46c9e",
  "sourceToolAssistantUUID": "92e46b84-c7f8-4f41-890b-4dc7e02abb5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T20:11:59.894Z_

<details><summary>↩ Tool result · `toolu_018rXny2zNAdfkCngVCFvG7f`</summary>

```text
Web search results for query: "SparseSpec PillarAttn throughput tokens per second reasoning DeepSeek R1 benchmark 2025"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2512.01278"},{"title":"Accelerating Large-Scale Reasoning Model Inference with ...","url":"https://arxiv.org/pdf/2512.01278"},{"title":"DeepSeek R1 0528 - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/deepseek-r1"},{"title":"Open Source DeepSeek R1 Runs at 200 Tokens Per Second on Raspberry Pi | NextBigFuture.com","url":"https://www.nextbigfuture.com/2025/01/open-source-deepseek-r1-runs-at-200-tokens-per-second-on-raspberry-pi.html"},{"title":"How to run DeepSeek-R1 IQ1_S 1.58bit at 140 Token/Sec · Issue #1591 · unslothai/unsloth","url":"https://github.com/unslothai/unsloth/issues/1591"},{"title":"SparseSpec: Sparse Computation Innovations","url":"https://www.emergentmind.com/topics/sparsespec"},{"title":"NVIDIA Blackwell Delivers World-Record DeepSeek-R1 Inference Performance | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/nvidia-blackwell-delivers-world-record-deepseek-r1-inference-performance/"},{"title":"Matthew Berman on X: \"3,872 tokens per second for the full DeepSeek R1!?\" / X","url":"https://x.com/MatthewBerman/status/1885151092121481644"},{"title":"DeepSeek-R1 Now Live With NVIDIA NIM | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/deepseek-r1-nim-microservice/"},{"title":"Run DeepSeek-R1 Dynamic 1.58-bit","url":"https://unsloth.ai/blog/deepseekr1-dynamic"}]

Based on the search results, I found relevant information about SparseSpec with PillarAttn and its performance metrics:

## SparseSpec and PillarAttn Overview

SparseSpec's core innovation is PillarAttn, a dynamic sparse attention mechanism tailored for speculative decoding on reasoning models that selectively loads and computes only the critical tokens—those with the highest attention scores during inference—thereby significantly reducing memory bandwidth usage.

## Throughput Performance

On Qwen3-8B, end-to-end throughput is increased from 690 tokens/sec (baseline) to 1460 tokens/sec, demonstrating substantial performance improvements.

More broadly, SparseSpec outperforms state-of-the-art solutions, with an up to 2.13× throughput gain across various models and datasets.

## Key Technical Features

PillarAttn identifies critical tokens by leveraging the exact attention scores obtained by full attention in each verification phase, with these critical tokens then used in the following draft steps to enable high speculation accuracy through sparsity that adapts to various contexts.

SparseSpec introduces a unified batch scheduler that batches the sparse draft and dense verification into a single batch to amortize weight loading, and evenly distributes requests across draft and verify so per-iteration resource usage stays balanced.

The search results indicate that while SparseSpec was evaluated on reasoning models like Qwen3 variants, the specific benchmark results for DeepSeek R1 were not detailed in these sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5770f529-d8a2-4b4a-b5c2-0d33ae19a92c",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "de63f6eb-57ac-48cd-951a-e4c924cd4b05",
  "sourceToolAssistantUUID": "5770f529-d8a2-4b4a-b5c2-0d33ae19a92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T20:12:01.433Z_

<details><summary>↩ Tool result · `toolu_01H3KL2em9iSYZZExqhii4VH`</summary>

```text
Web search results for query: ""attention head" classification decomposition "draft model" self-speculative per-head 2025 2026 arxiv"

Links: [{"title":"Cross-Attention Speculative Decoding Wei Zhong wei.zhong@lge.com","url":"https://www.arxiv.org/pdf/2505.24544"},{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641v1"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"Speculative Decoding with CTC-based Draft Model for LLM Inference Acceleration","url":"https://arxiv.org/html/2412.00061"},{"title":"MIRROR SPECULATIVE DECODING: BREAKING THE SERIAL BARRIER IN LLM INFERENCE","url":"https://arxiv.org/pdf/2510.13161"},{"title":"[2510.27641] SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/abs/2510.27641"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"Speculative Verification: Exploiting Information Gain to Refine Speculative Decoding","url":"https://arxiv.org/html/2509.24328v1"},{"title":"Linformer: Self-Attention with Linear Complexity","url":"https://arxiv.org/pdf/2006.04768"},{"title":"Q K V softmax αij Attention Mechanisms in Neural Networks","url":"https://arxiv.org/pdf/2601.03329"}]

I found several relevant arxiv papers related to speculative decoding, draft models, and attention mechanisms. Here are the key findings from the search:

## Recent Relevant Papers (2025-2026)

**SpecAttn: Speculating Sparse Attention** introduces a training-free approach that integrates with speculative decoding to enable efficient sparse attention by exploiting attention weights already computed by the draft model during speculative decoding to identify important tokens for the target model.

SpecAttn employs three core techniques: KL divergence-based layer alignment between draft and target models, a GPU-optimized sorting-free algorithm for top-p token selection from draft attention patterns, and dynamic key-value cache pruning guided by these predictions.

**Cross-Attention Speculative Decoding** discusses how while it may seem natural to integrate draft and target model states through cross-attention, prior work has explored this approach, with one example (CAPE) employing a conventional cross-attention decoder that includes a self-attention sublayer, while an alternative approach eliminates half of the attention parameters by using a single-layer cross-attention module followed by an MLP.

**Variational Speculative Decoding** notes that recent work has improved speculative decoding by refining draft model training, with methods like HASS enforcing feature consistency to reduce hidden-state mismatches, GRIFFIN resolving token-level misalignment, and EAGLE-3 incorporating training-time rollouts to better mimic decoding.

**Speculative Verification** research shows that attention heads across layers serve different roles that vary with context, some compute attention scores globally over many tokens while others focus locally on a subset, with single attention heads potentially switching unpredictably between global and local computations, and mapping attention heads between draft and target models does not provide useful signals for speculation accuracy.

These papers appear to address various aspects of the search query, though I did not find a paper that explicitly combines all the specific terms "attention head classification decomposition" with "self-speculative per-head" in that exact combination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2a682ce-ddbb-4a19-a674-158e7bb249e6",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a8ae7e4a12f261c81",
  "type": "user",
  "uuid": "9780e56a-2c01-44a6-baec-5af289473fe7",
  "sourceToolAssistantUUID": "a2a682ce-ddbb-4a19-a674-158e7bb249e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-10T20:12:52.550Z_

Here is a consolidated report of findings across all searches.

---

## 1. Papers Combining Per-Head Adaptive Attention with Speculative Decoding (May-June 2026)

**No paper found that explicitly combines per-head adaptive attention classification with speculative decoding in the May-June 2026 window.** The closest recent work is:

- **Component-Aware Self-Speculative Decoding in Hybrid Language Models** (arXiv:2605.01106, May 1 2026) -- by Hector Borobia et al. This exploits the architectural heterogeneity of hybrid models (e.g., Mamba-2 + attention in Falcon-H1) by isolating the SSM/linear-attention subgraph as a zero-cost internal draft. It operates at the *component* level (attention vs. SSM blocks), not at the *individual head* level. Parallel hybrids achieve acceptance rate alpha=0.68 at k=2, while sequential hybrids yield only alpha=0.038.

- **SpecKV** (arXiv:2605.02888, May 2026) -- a lightweight adaptive controller that selects the speculation length gamma per step using signals from the draft model. Achieves 56% improvement in expected tokens per speculation step. This is adaptive at the *step* level, not the head level.

**Key takeaway:** No one has published head-level adaptive decomposition for self-speculative decoding as of these searches. This appears to be an open niche.

---

## 2. Head-Level Classification/Decomposition for Attention Prediction

Several papers address head-level analysis but none frame it as a decomposition strategy for draft model construction in speculative decoding:

- **Linear Predictability of Attention Heads in Large Language Models** (arXiv:2603.13314, March 2026) -- The most directly relevant paper. Shows that Q, K, V activations of individual heads are linearly predictable from 2-5 "reference" peer heads (mean R^2 ~ 0.76 for keys on C4, frequently > 0.85 on GSM8K). This is a *learned* property, absent at initialization. Applied to KV cache compression (store only reference heads, reconstruct others on-the-fly), but **not connected to speculative decoding**. This paper is a potential threat to novelty if your approach also classifies heads as predictable vs. unpredictable, though the application domain differs.

- **Attention Head Entropy of LLMs** -- Uses entropy of attention patterns to predict correctness of model outputs. Classifies heads by entropy behavior but not for inference acceleration.

- **Safety Head ImPortant Score (Ships)** -- Classifies heads by safety contribution. Not relevant to inference.

- **SpecAttn (arXiv:2510.27641, Oct 2025) and SpecAttn v2 (arXiv:2602.07223, Feb 2026)** -- These are the closest to combining sparse attention with speculative decoding, but they operate at the *token* level (pruning KV cache entries), not at the *head* level. SpecAttn v2 achieves 2.81x throughput over vanilla AR decoding and 1.29x over SOTA sparsity-based self-speculative methods. Importantly, the Speculative Verification paper notes that "mapping attention heads between draft and target models does not provide useful signals for speculation accuracy" -- a finding your paper would need to address or refute if you're claiming head-level decomposition helps.

---

## 3. Current SOTA Throughput for Self-Speculative Decoding on Reasoning Tasks

| Method | Model | Throughput | Speedup |
|--------|-------|-----------|---------|
| **SparseSpec + PillarAttn** | Qwen3-8B | 1460 tok/s (from 690 baseline) | **2.13x** |
| **SpecAttn v2** (Feb 2026) | Various | -- | **2.81x** over AR, 1.29x over prior SOTA |
| **CAS-Spec** (NeurIPS 2025) | Various LLMs | -- | **1.1-2.3x** over AR |
| **SWIFT** (ICLR 2025) | Various | -- | **1.3-1.5x** over AR |

SparseSpec's PillarAttn and SpecAttn v2 represent the current throughput frontier for self-speculative approaches. PillarAttn is notable for reasoning tasks specifically (designed for long-chain reasoning with selective token loading). The absolute throughput of 1460 tok/s on Qwen3-8B is the most concrete number available.

---

## 4. Work Challenging or Extending TriAttention's MRL-Based Head Classification

**No papers were found that reference "TriAttention" or apply Matryoshka Representation Learning (MRL) to attention head classification.** The MRL search results returned only the original MRL embedding work (NeurIPS 2022) and downstream embedding applications. If "TriAttention" is your own unpublished framework, there is no known prior or concurrent work that uses MRL for head-level classification in the attention/inference acceleration space.

However, the **Linear Predictability of Attention Heads** paper (March 2026) implicitly provides an alternative head classification scheme (reference heads vs. predictable heads based on linear regression R^2) that could be seen as a competing framework for head decomposition, even though it doesn't use MRL.

---

## Implications for Novelty of a Head-Adaptive Decomposition Paper

**Strengths of the gap:**
- No existing work combines head-level classification with self-speculative decoding draft construction
- Existing self-speculative methods operate at layer level (LayerSkip, SWIFT, CLaSp), component level (Component-Aware), or token level (SparseSpec, SpecAttn) -- head level is unexplored
- MRL-based head classification has no precedent in this space

**Risks to address:**
1. The Linear Predictability paper (March 2026) establishes that heads have exploitable structure -- you should cite and differentiate
2. The Speculative Verification paper's finding that "head mapping between draft and target does not provide useful signals" needs to be carefully addressed -- your approach would need to show why per-head decomposition *within* the same model (self-speculation) works even if cross-model head mapping doesn't
3. SpecAttn v2's 2.81x speedup sets a high bar for throughput claims
4. Component-Aware Self-Speculative Decoding (May 2026) is the most thematically adjacent concurrent work and should be discussed

---

Sources:
- [Component-Aware Self-Speculative Decoding in Hybrid Language Models](https://arxiv.org/abs/2605.01106)
- [SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection](https://arxiv.org/html/2605.02888)
- [Linear Predictability of Attention Heads in Large Language Models](https://arxiv.org/abs/2603.13314)
- [SpecAttn: Speculating Sparse Attention (v1)](https://arxiv.org/abs/2510.27641)
- [SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding (v2)](https://arxiv.org/abs/2602.07223)
- [SparseSpec: Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding](https://arxiv.org/abs/2512.01278)
- [CAS-Spec: Cascade Adaptive Self-Speculative Decoding](https://arxiv.org/abs/2510.26843)
- [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://arxiv.org/abs/2410.06916)
- [Speculative Speculative Decoding (ICLR 2026)](https://openreview.net/forum?id=aL1Wnml9Ef)
- [CLaSp: In-Context Layer Skip for Self-Speculative Decoding](https://arxiv.org/html/2505.24196v1)
- [Speculative Verification](https://arxiv.org/html/2509.24328v1)
- [A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling](https://www.arxiv.org/pdf/2509.04474)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9780e56a-2c01-44a6-baec-5af289473fe7",
  "isSidechain": true,
  "agentId": "a8ae7e4a12f261c81",
  "requestId": "req_011CauVptLy37JX7g4QfzW5d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca117e77-fcd5-467b-a0c0-2ebd5d3548ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vC5M5uSCW1hpetthmS1Qh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 926,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 22240,
      "output_tokens": 2056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2089
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 926,
          "output_tokens": 2056,
          "cache_read_input_tokens": 22240,
          "cache_creation_input_tokens": 2089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2089,
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
